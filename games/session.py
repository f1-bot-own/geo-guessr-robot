"""
GameSession Class for Group Matches & Duels.
Manages rounds, countdowns, scores, and winner calculations.
"""

import time
import asyncio
import uuid
from typing import Dict, Set, Optional, Tuple, List, Any
from .models import Question, GameMode
from .question_factory import QuestionFactory
import config

class GameSession:
    def __init__(
        self,
        chat_id: int,
        created_by_user_id: int = 0,
        is_group: bool = True,
        lang: str = "en",
        mode: str = GameMode.MIX,
        total_rounds: int = config.DEFAULT_ROUNDS,
        round_time: int = config.DEFAULT_ROUND_TIME,
        is_duel: bool = False,
        duel_target_id: Optional[int] = None,
        duel_id: Optional[int] = None,
        host_id: Optional[int] = None,
        host_name: str = "",
        input_mode: str = "both",
        continent: str = "all"
    ):
        self.session_id: str = str(uuid.uuid4())[:8]
        self.chat_id: int = chat_id
        self.created_by_user_id: int = host_id if host_id is not None else created_by_user_id
        self.host_id: int = self.created_by_user_id
        self.host_name: str = host_name
        self.is_group: bool = is_group
        self.lang: str = lang
        self.mode: str = mode
        self.total_rounds: int = total_rounds
        self.round_time: int = round_time
        self.input_mode: str = input_mode if input_mode in ("buttons", "text", "both") else "both"
        self.continent: str = continent or "all"
        
        # Duel settings
        self.is_duel: bool = is_duel
        self.duel_target_id: Optional[int] = duel_target_id
        self.duel_id: Optional[int] = duel_id

        # State tracking
        self.current_round: int = 0
        self.status: str = "setup"  # setup, in_progress, between_rounds, finished
        self.scores: Dict[int, int] = {}
        self.user_names: Dict[int, str] = {}
        self.user_streaks: Dict[int, int] = {}
        
        self.current_question: Optional[Question] = None
        self.used_country_codes: Set[str] = set()
        self.answered_users_wrong: Set[int] = set()
        self.round_start_time: float = 0.0
        self.round_message_id: Optional[int] = None
        self.timer_task: Optional[asyncio.Task] = None
        self.has_photo: bool = False
        self.current_kb: Optional[Any] = None
        self.lock: asyncio.Lock = asyncio.Lock()
        self.advancing: bool = False

    def start_game(self) -> Question:
        """Start the game session and return the first question."""
        self.status = "in_progress"
        return self.next_round()

    def next_round(self) -> Question:
        """Advance to next round and generate fresh question."""
        self.current_round += 1
        self.answered_users_wrong.clear()
        
        q = QuestionFactory.generate(
            mode=self.mode,
            lang=self.lang,
            exclude_codes=self.used_country_codes,
            continent=self.continent
        )
        self.current_question = q
        if q.country_code:
            self.used_country_codes.add(q.country_code)
            
        self.round_start_time = time.time()
        return q

    async def check_answer(
        self,
        user_id: int,
        user_name: str,
        option_index: int
    ) -> Tuple[str, int, float]:
        """
        Evaluate user answer.
        Returns tuple: (result_type, points, elapsed_time)
        result_type in: ["correct", "wrong", "already_wrong", "not_allowed", "inactive"]
        """
        async with self.lock:
            if self.status != "in_progress" or not self.current_question:
                return ("inactive", 0, 0.0)

            # In duel mode, only the two participants may answer
            if self.is_duel:
                if user_id not in (self.created_by_user_id, self.duel_target_id):
                    return ("not_allowed", 0, 0.0)

            # Prevent multiple attempts if previously wrong in this round
            if user_id in self.answered_users_wrong:
                return ("already_wrong", 0, 0.0)

            elapsed = max(0.1, round(time.time() - self.round_start_time, 2))

            # Store player display name
            self.user_names[user_id] = user_name

            if option_index == self.current_question.correct_index:
                # Correct Answer!
                # Calculate speed bonus: max bonus when answered in 0s, 0 bonus at round_time
                time_ratio = max(0.0, (self.round_time - elapsed) / self.round_time)
                speed_bonus = int(time_ratio * config.POINTS_CORRECT * (config.POINTS_TIME_BONUS_MULTIPLIER - 1))
                
                # Streak bonus
                current_streak = self.user_streaks.get(user_id, 0) + 1
                self.user_streaks[user_id] = current_streak
                streak_bonus = min(50, (current_streak - 1) * 10)

                # Blur mode speed bonus: Stage 1 = +300, Stage 2 = +150
                blur_bonus = 0
                if getattr(self.current_question, "mode", None) == GameMode.BLUR:
                    stage = getattr(self.current_question, "blur_stage", 1)
                    if stage == 1:
                        blur_bonus = 300
                    elif stage == 2:
                        blur_bonus = 150

                total_points = config.POINTS_CORRECT + speed_bonus + streak_bonus + blur_bonus
                self.scores[user_id] = self.scores.get(user_id, 0) + total_points

                # Mark round as answered
                self.status = "between_rounds"
                return ("correct", total_points, elapsed)
            else:
                # Wrong Answer
                self.answered_users_wrong.add(user_id)
                self.user_streaks[user_id] = 0
                penalty = config.POINTS_WRONG_PENALTY
                self.scores[user_id] = max(0, self.scores.get(user_id, 0) - penalty)
                return ("wrong", penalty, elapsed)

    def is_game_finished(self) -> bool:
        """Check if all rounds are completed."""
        return self.current_round >= self.total_rounds

    def get_podium(self) -> List[Tuple[int, str, int]]:
        """Return list of (user_id, name, score) sorted by score descending."""
        results = [
            (uid, self.user_names.get(uid, f"User {uid}"), score)
            for uid, score in self.scores.items()
        ]
        results.sort(key=lambda x: x[2], reverse=True)
        return results

    def stop(self):
        """Cancel timer and mark session finished."""
        self.status = "finished"
        self.current_kb = None
        if self.timer_task and not self.timer_task.done():
            self.timer_task.cancel()
