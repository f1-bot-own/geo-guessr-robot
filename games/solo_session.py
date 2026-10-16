"""
Solo Game Session Module with Lives, Streak, and Lifelines.
"""

import asyncio
import random
from typing import Optional, Set, List, Tuple, Any
from .models import Question, GameMode
from .question_factory import QuestionFactory
from gamedata.countries import get_country
from locales.i18n import t
import config

class SoloGameSession:
    def __init__(
        self,
        user_id: int,
        user_name: str,
        lang: str = "en",
        mode: str = GameMode.MIX,
        round_time: int = config.DEFAULT_ROUND_TIME,
        input_mode: str = "both",
        continent: str = "all"
    ):
        self.user_id: int = user_id
        self.user_name: str = user_name
        self.lang: str = lang
        self.mode: str = mode
        self.round_time: int = round_time
        self.input_mode: str = input_mode if input_mode in ("buttons", "text", "both") else "both"
        self.continent: str = continent or "all"
        
        self.lives: int = 3
        self.score: int = 0
        self.round_number: int = 0
        self.correct_count: int = 0
        self.streak: int = 0
        self.max_streak: int = 0
        
        self.current_question: Optional[Question] = None
        self.eliminated_options: Set[int] = set()
        self.hint_used: bool = False
        self.has_5050: bool = True
        self.has_hint: bool = True
        
        self.used_country_codes: Set[str] = set()
        self.status: str = "in_progress"
        self.round_message_id: Optional[int] = None
        self.timer_task: Optional[asyncio.Task] = None
        self.has_photo: bool = False
        self.current_kb: Optional[Any] = None
        self.lock: asyncio.Lock = asyncio.Lock()
        self.advancing: bool = False

    def next_round(self) -> Question:
        """Advance to next solo question."""
        self.round_number += 1
        self.eliminated_options.clear()
        
        q = QuestionFactory.generate(
            mode=self.mode,
            lang=self.lang,
            exclude_codes=self.used_country_codes,
            continent=self.continent
        )
        self.current_question = q
        if q.country_code:
            self.used_country_codes.add(q.country_code)
        return q

    def use_5050(self) -> List[int]:
        """Eliminate two incorrect options."""
        if not self.has_5050 or not self.current_question:
            return []
        self.has_5050 = False
        
        correct_idx = self.current_question.correct_index
        wrong_indices = [i for i in range(len(self.current_question.options)) if i != correct_idx]
        
        eliminated = random.sample(wrong_indices, min(2, len(wrong_indices)))
        self.eliminated_options.update(eliminated)
        return eliminated

    def use_hint(self) -> str:
        """Provide a continent and capital hint, or driving side & continent for street view."""
        if not self.has_hint or not self.current_question:
            return ""
        self.has_hint = False
        
        country = get_country(self.current_question.country_code)
        if not country:
            return ""
        
        continent = country["continent"].get(self.lang, country["continent"]["en"])

        if self.current_question.mode == "streetview" or getattr(self.current_question, "mode", "") == "streetview":
            driving_side = getattr(self.current_question, "driving_side", "right") or "right"
            if self.lang == "uz":
                ds_str = "o'ng" if driving_side == "right" else "chap"
            elif self.lang == "ru":
                ds_str = "правостороннее" if driving_side == "right" else "левостороннее"
            else:
                ds_str = "Right" if driving_side == "right" else "Left"
            return t("solo_hint_streetview", self.lang, driving_side=ds_str, continent=continent)

        capital = country["capital"].get(self.lang, country["capital"]["en"])
        return t("solo_hint_text", self.lang, continent=continent, capital=capital)

    def check_answer(self, option_index: int) -> Tuple[bool, int, bool]:
        """
        Evaluate answer.
        Returns: (is_correct, points_earned, is_game_over)
        """
        if not self.current_question or self.status != "in_progress":
            return (False, 0, True)

        if option_index in self.eliminated_options:
            return (False, 0, False)

        if option_index == self.current_question.correct_index:
            self.correct_count += 1
            self.streak += 1
            self.max_streak = max(self.max_streak, self.streak)
            
            # Base 100 pts + streak bonus
            points = 100 + (self.streak - 1) * 10
            self.score += points
            return (True, points, False)
        else:
            self.streak = 0
            self.lives -= 1
            if self.lives <= 0:
                self.status = "game_over"
                return (False, 0, True)
            return (False, 0, False)

    def handle_timeout(self) -> Tuple[bool, str]:
        """
        Evaluate round timeout: deduct a life, reset streak, and check if game over.
        Returns: (is_game_over, correct_answer)
        """
        self.streak = 0
        self.lives -= 1
        correct_ans = self.current_question.correct_answer if self.current_question else ""
        is_game_over = (self.lives <= 0)
        if is_game_over:
            self.status = "game_over"
        return (is_game_over, correct_ans)

    def stop(self):
        """Cancel active timer task and finish session."""
        self.status = "finished"
        self.current_kb = None
        if self.timer_task and not self.timer_task.done():
            self.timer_task.cancel()

