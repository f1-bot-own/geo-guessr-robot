"""
Game Engine for GeoGuru & GeoGuessr.
Manages group sessions, solo practice, daily challenges, timers, scoring, and lifelines.
"""
import asyncio
import time
import random
from typing import Dict, Set, Optional, List, Tuple, Any, Callable
from dataclasses import dataclass, field

from config import (
    DEFAULT_ROUNDS,
    DEFAULT_ROUND_TIME,
    POINTS_CORRECT,
    POINTS_TIME_BONUS_MULTIPLIER,
    POINTS_WRONG_PENALTY,
    XP_PER_CORRECT,
    XP_PER_WIN,
)
from locales.i18n import t
from game.modes import Question, QuestionOption, generate_question

@dataclass
class AnswerResult:
    status: str  # "correct", "wrong", "already_answered", "inactive", "not_participant"
    points_awarded: int = 0
    penalty: int = 0
    elapsed_time: float = 0.0
    correct_answer_text: str = ""
    is_round_over: bool = False
    is_game_over: bool = False
    user_total_score: int = 0

class GroupGameSession:
    def __init__(
        self,
        chat_id: int,
        mode: str = "mix",
        total_rounds: int = DEFAULT_ROUNDS,
        round_time: int = DEFAULT_ROUND_TIME,
        lang: str = "en",
        duel_participants: Optional[Set[int]] = None,
        host_id: Optional[int] = None,
        host_name: str = "",
        input_mode: str = "both"
    ):
        self.chat_id = chat_id
        self.mode = mode
        self.total_rounds = total_rounds
        self.round_time = round_time
        self.lang = lang
        self.duel_participants = duel_participants  # None for standard multiplayer
        self.host_id = host_id
        self.host_name = host_name
        self.input_mode = input_mode
        
        self.current_round: int = 0
        self.current_question: Optional[Question] = None
        self.round_start_time: float = 0.0
        self.is_active: bool = False
        self.is_round_active: bool = False
        
        self.scores: Dict[int, int] = {}
        self.player_names: Dict[int, str] = {}
        self.answered_users_this_round: Set[int] = set()
        
        self.timer_task: Optional[asyncio.Task] = None
        self.message_id: Optional[int] = None
        self.on_round_timeout: Optional[Callable] = None

    def start_next_round(self) -> Question:
        """Advance to next round and generate fresh question."""
        self.current_round += 1
        self.current_question = generate_question(self.mode, self.lang)
        self.round_start_time = time.time()
        self.answered_users_this_round.clear()
        self.is_active = True
        self.is_round_active = True
        return self.current_question

    def process_answer(self, user_id: int, user_name: str, option_id: str) -> AnswerResult:
        """Process a player's button tap."""
        if not self.is_active or not self.is_round_active or not self.current_question:
            return AnswerResult(status="inactive")
        
        # Check duel constraint
        if self.duel_participants is not None and user_id not in self.duel_participants:
            return AnswerResult(status="not_participant")
        
        # Check if user already guessed wrong this round
        if user_id in self.answered_users_this_round:
            return AnswerResult(status="already_answered")
        
        self.player_names[user_id] = user_name
        if user_id not in self.scores:
            self.scores[user_id] = 0
        
        now = time.time()
        elapsed = max(0.1, now - self.round_start_time)
        
        if option_id == self.current_question.correct_option_id:
            # Correct answer!
            self.is_round_active = False
            
            # Cancel timeout timer if active
            if self.timer_task and not self.timer_task.done():
                self.timer_task.cancel()
                
            # Speed bonus calculation
            remaining_ratio = max(0.0, (self.round_time - elapsed) / self.round_time)
            bonus = int(POINTS_CORRECT * (POINTS_TIME_BONUS_MULTIPLIER - 1) * remaining_ratio)
            points = POINTS_CORRECT + bonus
            
            self.scores[user_id] += points
            is_game_over = (self.current_round >= self.total_rounds)
            if is_game_over:
                self.is_active = False
            
            return AnswerResult(
                status="correct",
                points_awarded=points,
                elapsed_time=elapsed,
                correct_answer_text=self.current_question.correct_answer_text,
                is_round_over=True,
                is_game_over=is_game_over,
                user_total_score=self.scores[user_id]
            )
        else:
            # Wrong answer
            self.answered_users_this_round.add(user_id)
            self.scores[user_id] = max(0, self.scores[user_id] - POINTS_WRONG_PENALTY)
            
            return AnswerResult(
                status="wrong",
                penalty=POINTS_WRONG_PENALTY,
                elapsed_time=elapsed,
                user_total_score=self.scores[user_id]
            )

    def handle_timeout(self) -> Tuple[str, bool]:
        """Mark round as timed out and check if game ended."""
        self.is_round_active = False
        correct_answer = self.current_question.correct_answer_text if self.current_question else ""
        is_game_over = (self.current_round >= self.total_rounds)
        if is_game_over:
            self.is_active = False
        return correct_answer, is_game_over

    def get_standings(self) -> List[Tuple[int, str, int]]:
        """Return standings sorted by score descending: [(user_id, name, score), ...]"""
        sorted_players = sorted(
            self.scores.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return [(uid, self.player_names.get(uid, f"Player {uid}"), score) for uid, score in sorted_players]

    def stop(self):
        """Abort session."""
        self.is_active = False
        self.is_round_active = False
        if self.timer_task and not self.timer_task.done():
            self.timer_task.cancel()


class SoloGameSession:
    """Solo practice session with 3 lives and 2 lifelines."""
    def __init__(self, user_id: int, lang: str = "en", mode: str = "mix", round_time: int = DEFAULT_ROUND_TIME, input_mode: str = "both"):
        self.user_id = user_id
        self.lang = lang
        self.mode = mode
        self.round_time: int = round_time
        self.input_mode: str = input_mode
        self.score: int = 0
        self.lives: int = 3
        self.round_num: int = 0
        self.correct_count: int = 0
        self.lifelines: Dict[str, bool] = {"hint": True, "5050": True}
        self.disabled_option_ids: Set[str] = set()
        self.current_question: Optional[Question] = None
        self.is_active: bool = True
        self.timer_task: Optional[asyncio.Task] = None
        self.message_id: Optional[int] = None

    def handle_timeout(self) -> Tuple[str, bool]:
        """Mark round as timed out, deduct life, and return (correct_answer, is_game_over)."""
        self.lives -= 1
        is_game_over = (self.lives <= 0)
        if is_game_over:
            self.is_active = False
        correct_ans = self.current_question.correct_answer_text if self.current_question else ""
        return correct_ans, is_game_over

    def stop(self):
        """Abort session and cancel timer."""
        self.is_active = False
        if self.timer_task and not self.timer_task.done():
            self.timer_task.cancel()

    def next_question(self) -> Question:
        """Start next question."""
        self.round_num += 1
        self.disabled_option_ids.clear()
        self.current_question = generate_question(self.mode, self.lang)
        return self.current_question

    def process_answer(self, option_id: str) -> Tuple[bool, bool, str]:
        """
        Returns: (is_correct, is_game_over, correct_answer_text)
        """
        if self.timer_task and not self.timer_task.done():
            self.timer_task.cancel()

        if not self.current_question:
            return False, True, ""
        
        if option_id == self.current_question.correct_option_id:
            self.correct_count += 1
            self.score += POINTS_CORRECT
            return True, False, self.current_question.correct_answer_text
        else:
            self.lives -= 1
            is_game_over = (self.lives <= 0)
            if is_game_over:
                self.is_active = False
            return False, is_game_over, self.current_question.correct_answer_text

    def use_hint(self) -> Optional[str]:
        """Use hint lifeline."""
        if not self.lifelines.get("hint") or not self.current_question:
            return None
        self.lifelines["hint"] = False
        return self.current_question.hint_text or "No hint available."

    def use_5050(self) -> List[str]:
        """Use 50/50 lifeline: eliminates 2 incorrect options."""
        if not self.lifelines.get("5050") or not self.current_question:
            return []
        
        incorrect_options = [opt for opt in self.current_question.options if not opt.is_correct]
        to_disable = random.sample(incorrect_options, min(2, len(incorrect_options)))
        for opt in to_disable:
            self.disabled_option_ids.add(opt.id)
            
        self.lifelines["5050"] = False
        return [opt.id for opt in to_disable]


class DailyChallengeSession:
    """Daily Geography Challenge: 5 questions seeded deterministically per day."""
    def __init__(self, user_id: int, date_seed: str, lang: str = "en"):
        self.user_id = user_id
        self.date_seed = date_seed
        self.lang = lang
        self.round_num: int = 0
        self.total_rounds: int = 5
        self.score: int = 0
        self.correct_count: int = 0
        self.is_active: bool = True
        
        # Deterministic generation for date
        rng = random.Random(date_seed)
        self.questions: List[Question] = []
        for _ in range(5):
            mode = rng.choice(["flag", "capital", "landmark", "higher_lower", "coat_of_arms"])
            # Temporarily set seed for question generator consistency
            saved_state = random.getstate()
            random.seed(rng.randint(0, 10000000))
            q = generate_question(mode, lang)
            random.setstate(saved_state)
            self.questions.append(q)

    @property
    def current_question(self) -> Optional[Question]:
        if 0 <= self.round_num < len(self.questions):
            return self.questions[self.round_num]
        return None

    def start_next_round(self) -> Optional[Question]:
        if self.round_num < self.total_rounds:
            q = self.questions[self.round_num]
            return q
        return None

    def process_answer(self, option_id: str) -> Tuple[bool, bool, str]:
        """Returns: (is_correct, is_complete, correct_answer_text)"""
        q = self.current_question
        if not q:
            return False, True, ""
        
        is_correct = (option_id == q.correct_option_id)
        if is_correct:
            self.correct_count += 1
            self.score += POINTS_CORRECT
        
        self.round_num += 1
        is_complete = (self.round_num >= self.total_rounds)
        if is_complete:
            self.is_active = False
            
        return is_correct, is_complete, q.correct_answer_text


class GameManager:
    """Global manager holding active game sessions."""
    def __init__(self):
        self.group_games: Dict[int, GroupGameSession] = {}
        self.solo_games: Dict[int, SoloGameSession] = {}
        self.daily_games: Dict[int, DailyChallengeSession] = {}
        self.setup_states: Dict[int, Dict[str, Any]] = {}

    def get_group_game(self, chat_id: int) -> Optional[GroupGameSession]:
        return self.group_games.get(chat_id)

    def set_group_game(self, chat_id: int, session: GroupGameSession):
        self.group_games[chat_id] = session

    def remove_group_game(self, chat_id: int):
        if chat_id in self.group_games:
            self.group_games[chat_id].stop()
            del self.group_games[chat_id]

    def get_solo_game(self, user_id: int) -> Optional[SoloGameSession]:
        return self.solo_games.get(user_id)

    def set_solo_game(self, user_id: int, session: SoloGameSession):
        self.solo_games[user_id] = session

    def remove_solo_game(self, user_id: int):
        if user_id in self.solo_games:
            self.solo_games[user_id].stop()
            del self.solo_games[user_id]

    def get_daily_game(self, user_id: int) -> Optional[DailyChallengeSession]:
        return self.daily_games.get(user_id)

    def set_daily_game(self, user_id: int, session: DailyChallengeSession):
        self.daily_games[user_id] = session

    def remove_daily_game(self, user_id: int):
        if user_id in self.daily_games:
            del self.daily_games[user_id]

    def get_solo_setup_state(self, user_id: int) -> dict:
        return self.setup_states.get(user_id, {"input_mode": "both", "mode": "mix", "round_time": 30})

    def set_solo_setup_state(self, user_id: int, state: dict):
        current = self.get_solo_setup_state(user_id)
        current.update(state)
        self.setup_states[user_id] = current

# Singleton instance
game_manager = GameManager()
