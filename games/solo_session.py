"""
Solo Game Session Module with Lives, Streak, and Lifelines.
"""

import asyncio
import random
from typing import Optional, Set, List, Tuple, Any
from .models import Question, GameMode
from .question_factory import QuestionFactory, _find_country
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
        continent: str = "all",
        selected_modes: Optional[List[str]] = None,
        is_blur: bool = False
    ):
        self.user_id: int = user_id
        self.user_name: str = user_name
        self.lang: str = lang
        self.mode: str = mode
        self.round_time: int = round_time
        self.input_mode: str = input_mode if input_mode in ("buttons", "text", "both") else "both"
        self.continent: str = continent or "all"
        
        # Multi-mode and blur state
        if selected_modes:
            self.selected_modes: List[str] = list(selected_modes)
        elif mode == GameMode.BLUR:
            self.selected_modes = [GameMode.FLAG]
        elif mode == GameMode.MIX:
            self.selected_modes = ["mix"]
        else:
            self.selected_modes = [mode]

        self.is_blur: bool = is_blur or (mode == GameMode.BLUR)

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
        """Advance to next solo question from selected modes."""
        self.round_number += 1
        self.eliminated_options.clear()
        
        valid_modes = [
            GameMode.FLAG, GameMode.CAPITAL, GameMode.LANDMARK, GameMode.HIGHER_LOWER,
            GameMode.COAT_OF_ARMS, GameMode.STREETVIEW, GameMode.EMOJI, GameMode.CONTOUR,
            GameMode.PRESIDENT, GameMode.HISTORICAL, GameMode.CELEBRITY, GameMode.PERSON, GameMode.LOGO
        ]
        active_modes = [
            m for m in getattr(self, "selected_modes", [])
            if m in valid_modes and m not in ("mix", "blur")
        ]
        if not active_modes:
            if self.mode and self.mode in valid_modes and self.mode not in ("mix", "blur"):
                active_modes = [self.mode]
            else:
                active_modes = [
                    GameMode.FLAG, GameMode.CAPITAL, GameMode.LANDMARK,
                    GameMode.PRESIDENT, GameMode.HISTORICAL, GameMode.CELEBRITY, GameMode.LOGO
                ]
        
        round_mode = random.choice(active_modes)

        q = QuestionFactory.generate(
            mode=round_mode,
            lang=self.lang,
            exclude_codes=self.used_country_codes,
            continent=self.continent
        )

        if getattr(self, "is_blur", False) and q and q.image_url:
            q.mode = GameMode.BLUR
            if round_mode == GameMode.FLAG:
                q.text = t("question_blur_flag", self.lang)
            elif round_mode in (GameMode.PRESIDENT, GameMode.HISTORICAL, GameMode.CELEBRITY, GameMode.PERSON):
                q.text = t("question_blur_person", self.lang)
            elif round_mode == GameMode.LOGO:
                q.text = t("question_blur_logo", self.lang)
            elif round_mode == GameMode.LANDMARK:
                q.text = t("question_blur_landmark", self.lang)
            elif round_mode == GameMode.COAT_OF_ARMS:
                q.text = t("question_blur_coat", self.lang)

        self.current_question = q
        if q and q.country_code:
            self.used_country_codes.add(q.country_code)
        return q

    def use_5050(self) -> List[int]:
        """Eliminate two incorrect options safely."""
        if not self.has_5050 or not self.current_question or self.eliminated_options:
            return []
        
        correct_idx = self.current_question.correct_index
        wrong_indices = [i for i in range(len(self.current_question.options)) if i != correct_idx]
        if len(wrong_indices) < 2:
            return []

        self.has_5050 = False
        eliminated = random.sample(wrong_indices, 2)
        self.eliminated_options.update(eliminated)
        return eliminated

    def use_hint(self) -> str:
        """Provide a smart hint without leaking the answer, handling any mode or missing ISO code."""
        if not self.has_hint or not self.current_question:
            return ""
        self.has_hint = False

        q = self.current_question
        country = None
        if q.country_code:
            country = _find_country(q.country_code)

        # Mode-specific smart hints
        if q.mode == "streetview" or getattr(q, "mode", "") == "streetview":
            continent_str = ""
            if country and "continent" in country:
                continent_str = country["continent"].get(self.lang, country["continent"]["en"])
            driving_side = getattr(q, "driving_side", "right") or "right"
            if self.lang == "uz":
                ds_str = "o'ng" if driving_side == "right" else "chap"
            elif self.lang == "ru":
                ds_str = "правостороннее" if driving_side == "right" else "левостороннее"
            else:
                ds_str = "Right" if driving_side == "right" else "Left"
            if continent_str:
                return t("solo_hint_streetview", self.lang, driving_side=ds_str, continent=continent_str)
            return f"💡 Driving side: {ds_str}"

        if country:
            continent = country.get("continent", {}).get(self.lang, country.get("continent", {}).get("en", ""))
            capital = country.get("capital", {}).get(self.lang, country.get("capital", {}).get("en", ""))
            c_name = country.get("name", {}).get(self.lang, country.get("name", {}).get("en", ""))
            
            if q.mode in (GameMode.FLAG, GameMode.COAT_OF_ARMS, GameMode.CONTOUR, GameMode.BLUR, GameMode.EMOJI):
                return t("solo_hint_text", self.lang, continent=continent, capital=capital)
            elif q.mode == GameMode.CAPITAL:
                # Do not leak the capital when asking for capital!
                if self.lang == "uz":
                    return f"💡 Qit'a: {continent}"
                elif self.lang == "ru":
                    return f"💡 Континент: {continent}"
                else:
                    return f"💡 Continent: {continent}"
            elif q.mode in (GameMode.PRESIDENT, GameMode.HISTORICAL, GameMode.CELEBRITY, GameMode.PERSON, GameMode.LOGO):
                if self.lang == "uz":
                    return f"💡 Hudud/Qit'a: {continent}, Davlat: {c_name}"
                elif self.lang == "ru":
                    return f"💡 Регион/Континент: {continent}, Страна: {c_name}"
                else:
                    return f"💡 Region/Continent: {continent}, Origin: {c_name}"

        # If no country resolved (e.g. historical figure without direct country, or world):
        if q.mode in (GameMode.PRESIDENT, GameMode.HISTORICAL, GameMode.CELEBRITY, GameMode.PERSON):
            if self.lang == "uz":
                return "💡 Maslahat: Tarixiy davr va shaxsning faoliyat sohasiga e'tibor bering!"
            elif self.lang == "ru":
                return "💡 Подсказка: Обратите внимание на историческую эпоху и сферу деятельности!"
            else:
                return "💡 Hint: Pay attention to the historical era and field of prominence!"
        elif q.mode == GameMode.LOGO:
            if self.lang == "uz":
                return "💡 Maslahat: Brendning faoliyat sohasi va xalqaro bozoriga e'tibor bering!"
            elif self.lang == "ru":
                return "💡 Подсказка: Обратите внимание на сферу деятельности бренда!"
            else:
                return "💡 Hint: Think about the brand's industry and global market!"

        # Generic fallback
        if self.lang == "uz":
            return "💡 Maslahat: Variantlarni diqqat bilan solishtiring!"
        elif self.lang == "ru":
            return "💡 Подсказка: Внимательно сравните предложенные варианты!"
        else:
            return "💡 Hint: Carefully compare the available options!"

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
            if getattr(self.current_question, "mode", None) == GameMode.BLUR:
                stage = getattr(self.current_question, "blur_stage", 1)
                if stage == 1:
                    points += 300
                elif stage == 2:
                    points += 150
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

