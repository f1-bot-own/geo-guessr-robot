"""
Unit tests verifying fixes from the Telegram Handlers & Flow Audit:
1. Callback data parsing resilience (IndexError / ValueError protection).
2. Host authorization in group setup.
3. Session and duel expiration handling.
4. Duel flow: invite duplicate prevention, cancellation, acceptance, non-participant text isolation, and score tie resolution.
5. Telegram error resilience in text answers.
6. Stop command comprehensive cleanup across group, solo, daily, and duel sessions.
7. Keyboard generation safety for arbitrary option counts.
"""

import asyncio
import os
import tempfile
import unittest
from unittest.mock import MagicMock, AsyncMock, patch

from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from database.db import Database
from games.models import Question, GameMode
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.daily_session import DailyChallengeSession
from games.manager import game_manager
from games.flow import finish_game
from handlers.commands import cmd_game, cmd_stop, cmd_duel, cmd_blur
from handlers.callbacks import (
    cb_group_answer,
    cb_game_setup,
    cb_daily_answer,
    cb_solo_answer,
    cb_solo_hint,
    cb_solo_5050,
    cb_set_language,
    cb_main_menu,
    cb_game_type,
    cb_solo_category,
    cb_solo_setup,
    cb_duel,
    cb_leaderboard_period,
)
from handlers.text_answers import check_group_text_answer, check_solo_text_answer
from keyboards.game_kb import get_question_kb, get_solo_question_kb, get_daily_question_kb
import config


class TestHandlersAndFlowAudit(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_audit.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

        self.bot = MagicMock()
        self.bot.db = self.db
        self.bot.edit_message_reply_markup = AsyncMock()
        self.bot.send_message = AsyncMock()
        self.bot.get_me = AsyncMock(return_value=MagicMock(username="GeoGuruBot"))

        # Clean in-memory manager
        game_manager.sessions.clear()
        game_manager.solo_sessions.clear()
        game_manager.daily_sessions.clear()
        game_manager.duel_invites.clear()
        game_manager.solo_setup_states.clear()

    async def asyncTearDown(self):
        game_manager.sessions.clear()
        game_manager.solo_sessions.clear()
        game_manager.daily_sessions.clear()
        game_manager.duel_invites.clear()
        self.temp_dir.cleanup()

    # ---------------- 1. Callback Data Parsing Resilience ----------------
    async def test_malformed_callback_data_does_not_crash(self):
        """Ensure callbacks do not raise ValueError or IndexError when receiving malformed or truncated data."""
        malformed_queries = [
            ("ans:invalid", cb_group_answer),
            ("ans:sess:not_a_number", cb_group_answer),
            ("ans:too:many:parts:here", cb_group_answer),
            ("setup:too:many:values:unpacked:session", cb_game_setup),
            ("setup:only_two", cb_game_setup),
            ("daily_ans:not_number", cb_daily_answer),
            ("daily_ans:", cb_daily_answer),
            ("daily_ans", cb_daily_answer),
            ("solo_ans:not_number", cb_solo_answer),
            ("solo_ans:", cb_solo_answer),
            ("set_lang", cb_set_language),
            ("menu", cb_main_menu),
            ("game_type", cb_game_type),
            ("solo_cat", cb_solo_category),
            ("solo_setup", cb_solo_setup),
            ("duel:accept:not_int:not_int", cb_duel),
            ("duel:only_two", cb_duel),
            ("lb_period:only_two", cb_leaderboard_period),
        ]

        for data, handler in malformed_queries:
            query = MagicMock()
            query.data = data
            query.from_user.id = 12345
            query.message.chat.id = -100123
            query.message.chat.type = "group"
            query.answer = AsyncMock()

            # Calling handler should not raise any unhandled exceptions
            try:
                if handler in (cb_solo_hint, cb_solo_5050):
                    await handler(query)
                else:
                    await handler(query, self.bot)
            except Exception as exc:
                self.fail(f"Handler {handler.__name__} crashed with {type(exc).__name__}: {exc} on data '{data}'")

    # ---------------- 2. Session Expiration Handling ----------------
    async def test_session_expiration_alerts_and_cleans_markup(self):
        """Clicking expired group or solo session buttons returns alert and cleans reply markup."""
        # 1. Group answer on non-existent session
        query = MagicMock()
        query.data = "ans:expired_sess_id:0"
        query.from_user.id = 555
        query.message.chat.id = -100999
        query.message.edit_reply_markup = AsyncMock()
        query.answer = AsyncMock()

        await cb_group_answer(query, self.bot)
        query.answer.assert_called_with("⚠️ This game session has ended.", show_alert=True)
        query.message.edit_reply_markup.assert_called_with(reply_markup=None)

        # 2. Setup on expired setup session
        query.data = "setup:mode:flag:expired_sess_id"
        query.answer.reset_mock()
        query.message.edit_reply_markup.reset_mock()
        await cb_game_setup(query, self.bot)
        query.answer.assert_called_with("⚠️ Setup is expired or game already started.", show_alert=True)
        query.message.edit_reply_markup.assert_called_with(reply_markup=None)

        # 3. Solo answer on non-existent session
        query.data = "solo_ans:1"
        query.answer.reset_mock()
        query.message.edit_reply_markup.reset_mock()
        await cb_solo_answer(query, self.bot)
        query.answer.assert_called_with("⚠️ Solo session ended. Start a new one with /solo!", show_alert=True)
        query.message.edit_reply_markup.assert_called_with(reply_markup=None)

        # 4. Daily answer on non-existent session
        query.data = "daily_ans:0"
        query.answer.reset_mock()
        query.message.edit_reply_markup.reset_mock()
        await cb_daily_answer(query, self.bot)
        query.answer.assert_called_with("⚠️ Today's challenge ended or expired.", show_alert=True)
        query.message.edit_reply_markup.assert_called_with(reply_markup=None)

    # ---------------- 3. Host Authorization in Group Setup ----------------
    async def test_host_authorization_in_setup(self):
        """Only the designated host can alter setup parameters or launch group games."""
        host_id = 111
        intruder_id = 999
        chat_id = -100444

        session = GameSession(
            chat_id=chat_id,
            created_by_user_id=host_id,
            host_id=host_id,
            host_name="HostUser",
            is_group=True,
            lang="en"
        )
        game_manager.set_session(chat_id, session)

        query = MagicMock()
        query.data = f"setup:time:60:{session.session_id}"
        query.from_user.id = intruder_id
        query.message.chat.id = chat_id
        query.message.edit_text = AsyncMock()
        query.answer = AsyncMock()

        # Intruder attempts to change round time
        await cb_game_setup(query, self.bot)
        query.answer.assert_called_with("⚠️ Only the game host can change settings or start the game!", show_alert=True)
        self.assertEqual(session.round_time, 30)  # unchanged

        # Host changes round time
        query.from_user.id = host_id
        query.answer.reset_mock()
        await cb_game_setup(query, self.bot)
        self.assertEqual(session.round_time, 60)
        query.message.edit_text.assert_called()

    # ---------------- 4. Duel Flow & Edge Cases ----------------
    async def test_duel_flow_and_duplicate_prevention(self):
        """Duel creation, duplicate challenge blocking, and acceptance/decline flow."""
        chat_id = -100555
        challenger_id = 101
        target_id = 102

        msg = MagicMock()
        msg.chat.id = chat_id
        msg.chat.type = "group"
        msg.from_user.id = challenger_id
        msg.from_user.first_name = "Challenger"
        msg.reply_to_message.from_user.id = target_id
        msg.reply_to_message.from_user.first_name = "Target"
        msg.reply_to_message.from_user.is_bot = False
        msg.reply = AsyncMock()
        msg.answer = AsyncMock(return_value=MagicMock(message_id=456))

        # First duel creation
        await cmd_duel(msg, self.bot)
        msg.answer.assert_called_once()
        self.assertIsNotNone(game_manager.get_duel_invite(chat_id))

        # Attempt to create duplicate duel while first is pending
        msg.reply.reset_mock()
        await cmd_duel(msg, self.bot)
        msg.reply.assert_called_with(
            "⚔️ There is already a pending duel challenge in this chat! Accept or decline it first, or use /stop.",
            parse_mode="HTML"
        )

        invite = game_manager.get_duel_invite(chat_id)
        duel_id = invite["duel_id"]
        exp_task = invite.get("expire_task")

        # Third party cannot accept duel
        cb_intruder = MagicMock()
        cb_intruder.data = f"duel:accept:{challenger_id}:{target_id}:{duel_id}"
        cb_intruder.from_user.id = 999
        cb_intruder.message.chat.id = chat_id
        cb_intruder.answer = AsyncMock()
        await cb_duel(cb_intruder, self.bot)
        cb_intruder.answer.assert_called_with("Only the challenged player can accept or decline this duel!", show_alert=True)
        self.assertIsNotNone(game_manager.get_duel_invite(chat_id))

        # Challenger can decline (cancel) their duel
        cb_cancel = MagicMock()
        cb_cancel.data = f"duel:decline:{challenger_id}:{target_id}:{duel_id}"
        cb_cancel.from_user.id = challenger_id
        cb_cancel.message.chat.id = chat_id
        cb_cancel.message.edit_text = AsyncMock()
        cb_cancel.answer = AsyncMock()
        await cb_duel(cb_cancel, self.bot)
        cb_cancel.answer.assert_called_with("Duel declined.")
        self.assertIsNone(game_manager.get_duel_invite(chat_id))
        await asyncio.sleep(0)
        self.assertTrue(exp_task.cancelled())

    async def test_duel_score_tie_resolution(self):
        """In a tied duel, match is recorded as a DRAW without falsely awarding victory XP."""
        chat_id = -100777
        challenger_id = 201
        target_id = 202

        session = GameSession(
            chat_id=chat_id,
            created_by_user_id=challenger_id,
            is_group=True,
            lang="en",
            mode="mix",
            total_rounds=3,
            is_duel=True,
            duel_target_id=target_id,
            duel_id=88
        )
        session.user_names[challenger_id] = "Alice"
        session.user_names[target_id] = "Bob"
        session.scores[challenger_id] = 150
        session.scores[target_id] = 150

        game_manager.set_session(chat_id, session)

        mock_db = MagicMock()
        mock_db.record_match = AsyncMock()
        mock_db.update_duel_status = AsyncMock()
        mock_db.update_group_player_score = AsyncMock()
        mock_db.record_answer = AsyncMock()
        mock_db.increment_chat_games = AsyncMock()

        await finish_game(self.bot, chat_id, session, mock_db)

        # Winner ID must be None on a tie
        mock_db.record_match.assert_called_once()
        call_kwargs = mock_db.record_match.call_args[1]
        self.assertIsNone(call_kwargs["winner_id"])

        mock_db.update_duel_status.assert_called_with(88, status="completed", winner_id=None)

        # Neither player receives a victory
        for call in mock_db.update_group_player_score.call_args_list:
            is_win = call[1].get("is_win")
            self.assertFalse(is_win)

        # Victory XP was NOT awarded
        mock_db.record_answer.assert_not_called()

    async def test_duel_text_isolation(self):
        """Non-participants typing in group chat during a duel are ignored."""
        chat_id = -100888
        challenger_id = 301
        target_id = 302
        intruder_id = 303

        session = GameSession(
            chat_id=chat_id,
            created_by_user_id=challenger_id,
            is_group=True,
            lang="en",
            mode="flag",
            is_duel=True,
            duel_target_id=target_id
        )
        session.status = "in_progress"
        q = Question(
            mode=GameMode.FLAG,
            text="Which country?",
            options=["France", "Germany", "Spain", "Italy"],
            correct_index=0,
            correct_answer="France",
            country_code="FR"
        )
        session.current_question = q
        game_manager.set_session(chat_id, session)

        # Intruder attempts to answer in group
        msg = MagicMock()
        msg.chat.id = chat_id
        msg.chat.type = "group"
        msg.from_user.id = intruder_id
        msg.from_user.is_bot = False
        msg.text = "France"
        msg.reply = AsyncMock()

        await check_group_text_answer(msg, self.bot)
        # Intruder answer must be completely ignored
        msg.reply.assert_not_called()
        self.assertEqual(session.scores, {})

    # ---------------- 5. Telegram Error Resilience in Text Answers ----------------
    async def test_text_answer_resilient_to_telegram_bad_request(self):
        """Handler gracefully catches TelegramBadRequest when replying to text answers."""
        chat_id = -100999
        user_id = 401

        session = GameSession(chat_id=chat_id, created_by_user_id=user_id, is_group=True, lang="en", mode="capital")
        session.status = "in_progress"
        session.current_question = Question(
            mode=GameMode.CAPITAL,
            text="Capital of France?",
            options=["Paris", "Berlin", "Rome", "Madrid"],
            correct_index=0,
            correct_answer="Paris",
            country_code="FR"
        )
        game_manager.set_session(chat_id, session)

        msg = MagicMock()
        msg.chat.id = chat_id
        msg.chat.type = "group"
        msg.from_user.id = user_id
        msg.from_user.first_name = "Charlie"
        msg.from_user.username = "charlie"
        msg.from_user.is_bot = False
        msg.text = "Berlin"  # wrong answer
        msg.reply = AsyncMock(side_effect=TelegramBadRequest(method=MagicMock(), message="Bad Request: message to be replied not found"))

        # Should not raise exception
        try:
            await check_group_text_answer(msg, self.bot)
        except Exception as exc:
            self.fail(f"check_group_text_answer raised {exc}")

    # ---------------- 6. Stop Command Comprehensive Cleanup ----------------
    async def test_cmd_stop_cleans_all_sessions_and_timers(self):
        """/stop cleanly terminates group session, solo session, daily challenge, pending duels, and background timers."""
        chat_id = -100333
        user_id = 501

        # 1. Group session with active timer
        grp_session = GameSession(chat_id=chat_id, created_by_user_id=user_id, is_group=True, lang="en")
        grp_task = asyncio.create_task(asyncio.sleep(100))
        grp_session.timer_task = grp_task
        grp_session.round_message_id = 1111
        game_manager.set_session(chat_id, grp_session)

        # 2. Solo session with active timer
        solo_session = SoloGameSession(user_id=user_id, user_name="Alice", lang="en")
        solo_task = asyncio.create_task(asyncio.sleep(100))
        solo_session.timer_task = solo_task
        solo_session.round_message_id = 2222
        game_manager.set_solo_session(user_id, solo_session)

        # 3. Daily challenge session
        daily_session = DailyChallengeSession(user_id=user_id, user_name="Alice", lang="en")
        game_manager.set_daily_session(user_id, daily_session)

        # 4. Pending duel invite with expiration task
        duel_task = asyncio.create_task(asyncio.sleep(100))
        game_manager.set_duel_invite(chat_id, {
            "duel_id": 99,
            "expire_task": duel_task
        })

        msg = MagicMock()
        msg.chat.id = chat_id
        msg.chat.type = "group"
        msg.from_user.id = user_id
        msg.from_user.first_name = "Alice"
        msg.answer = AsyncMock()
        msg.reply = AsyncMock()

        await cmd_stop(msg, self.bot)

        await asyncio.sleep(0)
        # All timers cancelled
        self.assertTrue(grp_task.cancelled())
        self.assertTrue(solo_task.cancelled())
        self.assertTrue(duel_task.cancelled())

        # All sessions removed
        self.assertIsNone(game_manager.get_session(chat_id))
        self.assertIsNone(game_manager.get_solo_session(user_id))
        self.assertIsNone(game_manager.get_daily_session(user_id))
        self.assertIsNone(game_manager.get_duel_invite(chat_id))

        # Players notified
        msg.answer.assert_called_once()

    async def test_cmd_stop_anonymous_admin_guard(self):
        """/stop does not crash when message.from_user is None (anonymous group admin)."""
        chat_id = -100222
        session = GameSession(chat_id=chat_id, created_by_user_id=999, is_group=True, lang="en")
        game_manager.set_session(chat_id, session)

        msg = MagicMock()
        msg.chat.id = chat_id
        msg.chat.type = "group"
        msg.from_user = None  # Anonymous admin
        msg.sender_chat.id = chat_id
        msg.sender_chat.title = "Group Channel"
        msg.answer = AsyncMock()
        msg.reply = AsyncMock()

        await cmd_stop(msg, self.bot)
        self.assertIsNone(game_manager.get_session(chat_id))
        msg.answer.assert_called_once()

    # ---------------- 7. Dynamic Keyboard Option Safety ----------------
    def test_keyboard_generation_for_arbitrary_option_counts(self):
        """Ensure question keyboards render without IndexError for 1, 2, 3, 4, or 5 options."""
        for count in [1, 2, 3, 4, 5]:
            options = [f"Option {i}" for i in range(count)]
            kb_group = get_question_kb("sess1", options)
            self.assertIsNotNone(kb_group)

            kb_solo = get_solo_question_kb(options, eliminated=set(), has_hint=True, has_5050=True)
            self.assertIsNotNone(kb_solo)

            kb_daily = get_daily_question_kb(options)
            self.assertIsNotNone(kb_daily)


if __name__ == "__main__":
    unittest.main()
