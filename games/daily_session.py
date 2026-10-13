"""
Daily Geography Challenge Session.
Generates a deterministic 5-question daily challenge based on date seed.
Modes: Flag -> Capital -> Landmark -> Higher/Lower -> Coat of Arms.
"""
import random
from typing import Optional, List, Tuple
from .models import Question, GameMode
from .question_factory import QuestionFactory
import config

class DailyGameSession:
    TOTAL_ROUNDS = 5

    def __init__(self, user_id: int, user_name: str, today_str: Optional[str] = None, lang: str = "en", date_str: Optional[str] = None):
        self.user_id = user_id
        self.user_name = user_name
        self.today_str = today_str or date_str or "2026-10-10"
        self.date_str = self.today_str
        self.lang = lang

        self.round_number = 1
        self.total_rounds = 5
        self.score = 0
        self.correct_count = 0
        self.status = "in_progress"

        # Deterministic generation using date seed
        rng = random.Random(f"{self.today_str}_{lang}")
        modes = [
            GameMode.FLAG,
            GameMode.CAPITAL,
            GameMode.LANDMARK,
            GameMode.HIGHER_LOWER,
            GameMode.COAT_OF_ARMS
        ]
        
        saved_state = random.getstate()
        random.seed(rng.randint(0, 10000000))
        self.questions: List[Question] = []
        used_codes = set()
        for mode in modes:
            q = QuestionFactory.generate(mode=mode, lang=lang, exclude_codes=used_codes)
            if q.country_code:
                used_codes.add(q.country_code)
            self.questions.append(q)
        random.setstate(saved_state)

    @property
    def current_round(self) -> int:
        return self.round_number - 1

    @property
    def current_question(self) -> Optional[Question]:
        idx = self.round_number - 1
        if 0 <= idx < len(self.questions):
            return self.questions[idx]
        return None

    def check_answer(self, option_index: int) -> Tuple[bool, int, bool, str]:
        """
        Evaluate answer.
        Returns: (is_correct, points_earned, is_completed, correct_answer)
        """
        q = self.current_question
        if not q or self.status != "in_progress":
            return (False, 0, True, "")

        is_correct = (option_index == q.correct_index)
        points = 0
        if is_correct:
            self.correct_count += 1
            points = config.POINTS_CORRECT
            self.score += points

        is_completed = (self.round_number >= self.total_rounds)
        if is_completed:
            self.status = "completed"
        else:
            self.round_number += 1

        return (is_correct, points, is_completed, q.correct_answer)

    def next_round(self):
        """Ensure next daily question is returned."""
        return self.current_question

# Alias for compatibility
DailyChallengeSession = DailyGameSession
