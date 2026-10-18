"""
GameSession Class for Group Matches & Duels.
Manages rounds, countdowns, scores, and winner calculations.
"""

import time
import random
import asyncio
import uuid
from typing import Dict, Set, Optional, Tuple, List, Any
from .models import Question, GameMode
from .question_factory import QuestionFactory
from locales.i18n import t
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
        continent: str = "all",
        selected_modes: Optional[List[str]] = None,
        is_blur: bool = False,
        view_mode: str = "categories"
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
        self.view_mode: str = view_mode
        
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
        try:
            from events.bus import publish
            publish("game_started", {
                "chat_id": self.chat_id,
                "host_id": self.created_by_user_id,
                "mode": self.mode,
                "rounds": self.total_rounds,
            })
        except Exception:
            pass
        return self.next_round()

    def next_round(self) -> Question:
        """Advance to next round and generate fresh question from selected modes."""
        self.current_round += 1
        self.answered_users_wrong.clear()
        
        valid_modes = getattr(GameMode, "VALID_MODES", [
            GameMode.FLAG, GameMode.CAPITAL, GameMode.LANDMARK, GameMode.HIGHER_LOWER,
            GameMode.COAT_OF_ARMS, GameMode.STREETVIEW, GameMode.EMOJI, GameMode.CONTOUR,
            GameMode.PRESIDENT, GameMode.HISTORICAL, GameMode.CELEBRITY, GameMode.PERSON, GameMode.LOGO
        ])
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
        result_type in: ["correct", "wrong", "already_wrong", "not_allowed", "inactive", "banned"]
        """
        async with self.lock:
            if self.status != "in_progress" or not self.current_question:
                return ("inactive", 0, 0.0)

            # Check if user is banned
            try:
                from database.db import get_default_db
                db = get_default_db()
                if hasattr(db, "is_user_banned") and await db.is_user_banned(user_id):
                    return ("banned", 0, 0.0)
            except Exception:
                pass

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

            # Question metadata for logging
            q = self.current_question
            q_options = getattr(q, "options", [])
            sel_opt = q_options[option_index] if (0 <= option_index < len(q_options)) else str(option_index)
            corr_idx = getattr(q, "correct_index", 0)
            corr_opt = q_options[corr_idx] if (0 <= corr_idx < len(q_options)) else ""
            q_id = getattr(q, "question_id", None) or getattr(q, "country_code", "") or str(self.current_round)
            q_text = getattr(q, "text", "")
            q_mode = getattr(q, "mode", self.mode)

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

                # Log answer and emit event
                try:
                    from database.db import get_default_db
                    db = get_default_db()
                    if hasattr(db, "record_answer_log"):
                        await db.record_answer_log(
                            user_id=user_id,
                            username=user_name,
                            chat_id=self.chat_id,
                            mode=q_mode,
                            question_id=str(q_id),
                            question_text=q_text,
                            selected_option=sel_opt,
                            correct_option=corr_opt,
                            is_correct=1,
                            points=total_points,
                            time_taken=elapsed
                        )
                except Exception:
                    pass

                return ("correct", total_points, elapsed)
            else:
                # Wrong Answer
                self.answered_users_wrong.add(user_id)
                self.user_streaks[user_id] = 0
                penalty = config.POINTS_WRONG_PENALTY
                self.scores[user_id] = max(0, self.scores.get(user_id, 0) - penalty)

                # Log answer and emit event
                try:
                    from database.db import get_default_db
                    db = get_default_db()
                    if hasattr(db, "record_answer_log"):
                        await db.record_answer_log(
                            user_id=user_id,
                            username=user_name,
                            chat_id=self.chat_id,
                            mode=q_mode,
                            question_id=str(q_id),
                            question_text=q_text,
                            selected_option=sel_opt,
                            correct_option=corr_opt,
                            is_correct=0,
                            points=-penalty,
                            time_taken=elapsed
                        )
                except Exception:
                    pass

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
