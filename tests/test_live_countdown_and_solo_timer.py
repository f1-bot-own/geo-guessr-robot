"""
Tests for Live Countdown Updates and Solo Mode Round Timer.
Verifies:
1. Solo Mode round timers (30s/60s defaults, timeout deductions, streak reset, game over lifecycle).
2. Live countdown formatting (format_countdown for EN, UZ, RU across normal and critical thresholds).
3. Countdown checkpoints generation and intervals (avoiding Telegram API flood limits).
4. Cancellation of background countdown tasks on answers, lifelines, and /stop.
5. Telegram API error resilience (TelegramRetryAfter, FloodWait, message is not modified).
6. Group and solo question caption/text composition with live remaining time.
"""

import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from aiogram.exceptions import TelegramBadRequest, TelegramRetryAfter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from locales.i18n import t, format_countdown
from games.models import GameMode, Question
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.manager import game_manager
from games.flow import (
    get_countdown_checkpoints,
    format_group_question_text,
    format_solo_question_text,
    safe_edit_question_message,
    run_round_countdown,
    send_solo_round,
    send_round_question,
    handle_solo_timeout,
    handle_round_timeout,
)
from handlers.callbacks import cb_solo_answer, cb_solo_5050, cb_solo_hint, cb_group_answer
from handlers.commands import cmd_stop, cmd_solo
from handlers.text_answers import check_group_text_answer


class TestCountdownFormattingAndCheckpoints(unittest.TestCase):
    def test_countdown_formatting_english(self):
        """English countdown formatting: >5s uses hourglass, <=5s uses warning banner."""
        self.assertEqual(format_countdown(30, "en"), "⏳ Time remaining: 30s")
        self.assertEqual(format_countdown(25, "en"), "⏳ Time remaining: 25s")
        self.assertEqual(format_countdown(10, "en"), "⏳ Time remaining: 10s")
        self.assertEqual(format_countdown(6, "en"), "⏳ Time remaining: 6s")
        self.assertEqual(format_countdown(5, "en"), "⚠️ 5s left!")
        self.assertEqual(format_countdown(2, "en"), "⚠️ 2s left!")
        self.assertEqual(format_countdown(1, "en"), "⚠️ 1s left!")
        self.assertEqual(format_countdown(0, "en"), "⚠️ 0s left!")

    def test_countdown_formatting_uzbek(self):
        """Uzbek countdown formatting: >5s Qolgan vaqt, <=5s warning banner."""
        self.assertEqual(format_countdown(30, "uz"), "⏳ Qolgan vaqt: 30s")
        self.assertEqual(format_countdown(25, "uz"), "⏳ Qolgan vaqt: 25s")
        self.assertEqual(format_countdown(10, "uz"), "⏳ Qolgan vaqt: 10s")
        self.assertEqual(format_countdown(5, "uz"), "⚠️ 5s qoldi!")
        self.assertEqual(format_countdown(1, "uz"), "⚠️ 1s qoldi!")
        self.assertEqual(format_countdown(0, "uz"), "⚠️ 0s qoldi!")

    def test_countdown_formatting_russian(self):
        """Russian countdown formatting: >5s Осталось времени, <=5s warning banner."""
        self.assertEqual(format_countdown(30, "ru"), "⏳ Осталось времени: 30с")
        self.assertEqual(format_countdown(25, "ru"), "⏳ Осталось времени: 25с")
        self.assertEqual(format_countdown(10, "ru"), "⏳ Осталось времени: 10с")
        self.assertEqual(format_countdown(5, "ru"), "⚠️ 5с осталось!")
        self.assertEqual(format_countdown(1, "ru"), "⚠️ 1с осталось!")

    def test_countdown_checkpoints_for_30s(self):
        """30s round must generate safe checkpoints including 25s, 20s, 15s, 10s, 5s."""
        cps = get_countdown_checkpoints(30)
        self.assertEqual(cps, [25, 20, 15, 10, 5])
        # Verify strictly decreasing
        for i in range(len(cps) - 1):
            self.assertGreater(cps[i], cps[i + 1])
            self.assertGreaterEqual(cps[i] - cps[i + 1], 3)  # At least 3s apart

    def test_countdown_checkpoints_for_60s(self):
        """60s round must generate safe checkpoints hitting 20s, 10s, 5s thresholds."""
        cps = get_countdown_checkpoints(60)
        self.assertIn(5, cps)
        self.assertIn(10, cps)
        self.assertIn(20, cps)
        self.assertIn(30, cps)
        # Verify all checkpoints are strictly between 0 and 60
        for cp in cps:
            self.assertGreater(cp, 0)
            self.assertLess(cp, 60)

    def test_countdown_checkpoints_short_durations(self):
        """Edge cases: short durations (10s, 5s, 2s)."""
        cps_10 = get_countdown_checkpoints(10)
        self.assertTrue(len(cps_10) > 0)
        for cp in cps_10:
            self.assertTrue(0 < cp < 10)

        cps_2 = get_countdown_checkpoints(2)
        self.assertEqual(cps_2, [])


class TestSoloSessionTimerAndTimeout(unittest.IsolatedAsyncioTestCase):
    def test_solo_session_timer_attributes(self):
        """SoloGameSession supports round_time, timer_task, and lock."""
        session = SoloGameSession(user_id=101, user_name="Alex", lang="en", round_time=30)
        self.assertEqual(session.round_time, 30)
        self.assertEqual(session.lives, 3)
        self.assertEqual(session.streak, 0)
        self.assertIsNone(session.timer_task)
        self.assertIsNone(session.round_message_id)

        session_60 = SoloGameSession(user_id=102, user_name="Bob", lang="en", round_time=60)
        self.assertEqual(session_60.round_time, 60)

    def test_solo_handle_timeout_deducts_life_and_resets_streak(self):
        """Timeout deducts 1 life and resets streak when lives remain."""
        session = SoloGameSession(user_id=201, user_name="Charlie", lang="en")
        session.next_round()
        session.streak = 4
        self.assertEqual(session.lives, 3)

        is_game_over, ans = session.handle_timeout()
        self.assertFalse(is_game_over)
        self.assertEqual(session.lives, 2)
        self.assertEqual(session.streak, 0)
        self.assertEqual(session.status, "in_progress")

    def test_solo_handle_timeout_ends_game_when_out_of_lives(self):
        """Timeout ends game when lives drop to 0."""
        session = SoloGameSession(user_id=202, user_name="David", lang="en")
        session.next_round()
        session.lives = 1

        is_game_over, ans = session.handle_timeout()
        self.assertTrue(is_game_over)
        self.assertEqual(session.lives, 0)
        self.assertEqual(session.status, "game_over")

    def test_solo_stop_cancels_timer_task(self):
        """session.stop() cancels any running timer task."""
        session = SoloGameSession(user_id=203, user_name="Emma", lang="en")
        mock_task = MagicMock()
        mock_task.done.return_value = False
        session.timer_task = mock_task

        session.stop()
        self.assertEqual(session.status, "finished")
        mock_task.cancel.assert_called_once()


class TestSoloTimeoutHandlerFlow(unittest.IsolatedAsyncioTestCase):
    async def test_handle_solo_timeout_clears_keyboard_and_advances(self):
        """handle_solo_timeout removes markup, decrements life, and advances question."""
        user_id = 301
        session = SoloGameSession(user_id=user_id, user_name="Fiona", lang="en")
        session.next_round()
        session.round_message_id = 777

        bot = MagicMock()
        bot.edit_message_reply_markup = AsyncMock()
        bot.send_message = AsyncMock()

        with patch("games.flow.send_solo_round", new_callable=AsyncMock) as mock_send:
            await handle_solo_timeout(bot, user_id, session, round_num=1, wait_seconds=0)

            # Markup cleared on timed out message
            bot.edit_message_reply_markup.assert_called_once_with(
                chat_id=user_id,
                message_id=777,
                reply_markup=None
            )
            # Timeout notification sent
            bot.send_message.assert_called_once()
            _, kwargs = bot.send_message.call_args
            self.assertIn("Time's up", kwargs.get("text", ""))

            # Session advanced
            self.assertEqual(session.lives, 2)
            self.assertEqual(session.round_number, 2)
            mock_send.assert_called_once_with(bot, user_id, session, None)

    async def test_handle_solo_timeout_game_over_lifecycle(self):
        """handle_solo_timeout ends game and removes session when lives == 0."""
        user_id = 302
        session = SoloGameSession(user_id=user_id, user_name="George", lang="en")
        session.next_round()
        session.lives = 1
        session.round_message_id = 888
        game_manager.set_solo_session(user_id, session)

        bot = MagicMock()
        bot.edit_message_reply_markup = AsyncMock()
        bot.send_message = AsyncMock()

        await handle_solo_timeout(bot, user_id, session, round_num=1, wait_seconds=0)

        # Removed from manager
        self.assertIsNone(game_manager.get_solo_session(user_id))
        self.assertEqual(session.status, "game_over")
        self.assertEqual(session.lives, 0)

        # Game over text sent
        bot.send_message.assert_called_once()
        _, kwargs = bot.send_message.call_args
        self.assertIn("Game Over", kwargs.get("text", ""))


class TestQuestionCaptionComposition(unittest.TestCase):
    def test_group_question_caption_includes_countdown(self):
        """format_group_question_text includes header, prompt, and countdown."""
        session = GameSession(chat_id=-10011, lang="en", round_time=30)
        session.start_game()

        text_30 = format_group_question_text(session, remaining_time=30)
        self.assertIn("Round 1", text_30)
        self.assertIn("⏳ Time remaining: 30s", text_30)

        text_5 = format_group_question_text(session, remaining_time=5)
        self.assertIn("⚠️ 5s left!", text_5)

    def test_solo_question_caption_includes_countdown(self):
        """format_solo_question_text includes solo header, lives, and countdown."""
        session = SoloGameSession(user_id=401, user_name="Hannah", lang="en", round_time=30)
        session.next_round()

        text_25 = format_solo_question_text(session, remaining_time=25)
        self.assertIn("Solo Practice Mode", text_25)
        self.assertIn("Lives: ❤️❤️❤️", text_25)
        self.assertIn("⏳ Time remaining: 25s", text_25)

        text_5 = format_solo_question_text(session, remaining_time=5)
        self.assertIn("⚠️ 5s left!", text_5)


class TestTimerCancellationOnPlayerActions(unittest.IsolatedAsyncioTestCase):
    async def test_solo_answer_cancels_timer_task(self):
        """Submitting a solo answer cleanly cancels the active countdown timer."""
        user_id = 501
        session = SoloGameSession(user_id=user_id, user_name="Ian", lang="en")
        session.next_round()
        game_manager.set_solo_session(user_id, session)

        # Set up a fake running timer task
        async def dummy_timer():
            await asyncio.sleep(100)

        task = asyncio.create_task(dummy_timer())
        session.timer_task = task

        cb = MagicMock()
        cb.data = f"solo_ans:{session.current_question.correct_index}"
        cb.from_user.id = user_id
        cb.from_user.first_name = "Ian"
        cb.from_user.username = "ian501"
        cb.answer = AsyncMock()
        cb.message.edit_reply_markup = AsyncMock()

        bot = MagicMock()
        mock_db = MagicMock()
        mock_db.record_answer = AsyncMock()
        bot.db = mock_db

        with patch("handlers.callbacks.send_solo_round", new_callable=AsyncMock):
            await cb_solo_answer(cb, bot)

        await asyncio.sleep(0)
        self.assertTrue(task.cancelled())
        game_manager.remove_solo_session(user_id)

    async def test_group_answer_cancels_timer_task(self):
        """Submitting a correct group answer cleanly cancels the active timer."""
        chat_id = -100555
        session = GameSession(chat_id=chat_id, lang="en")
        session.start_game()
        game_manager.set_session(chat_id, session)

        async def dummy_timer():
            await asyncio.sleep(100)

        task = asyncio.create_task(dummy_timer())
        session.timer_task = task

        cb = MagicMock()
        cb.data = f"ans:{session.session_id}:{session.current_question.correct_index}"
        cb.from_user.id = 601
        cb.from_user.first_name = "Julia"
        cb.from_user.username = "julia601"
        cb.message.chat.id = chat_id
        cb.answer = AsyncMock()
        cb.message.edit_reply_markup = AsyncMock()

        bot = MagicMock()
        mock_db = MagicMock()
        mock_db.record_answer = AsyncMock()
        bot.db = mock_db
        bot.send_message = AsyncMock()

        with patch("handlers.callbacks.proceed_after_round", new_callable=AsyncMock):
            await cb_group_answer(cb, bot)

        await asyncio.sleep(0)
        self.assertTrue(task.cancelled())
        game_manager.remove_session(chat_id)

    async def test_cmd_stop_cancels_active_solo_timer(self):
        """/stop aborts active solo game and cancels its timer task."""
        user_id = 701
        session = SoloGameSession(user_id=user_id, user_name="Kevin", lang="en")
        session.next_round()
        game_manager.set_solo_session(user_id, session)

        async def dummy_timer():
            await asyncio.sleep(100)

        task = asyncio.create_task(dummy_timer())
        session.timer_task = task

        msg = MagicMock()
        msg.chat.id = user_id
        msg.chat.type = "private"
        msg.from_user.id = user_id
        msg.from_user.first_name = "Kevin"
        msg.answer = AsyncMock()
        msg.reply = AsyncMock()

        bot = MagicMock()
        mock_db = MagicMock()
        bot.db = mock_db

        await cmd_stop(msg, bot)

        await asyncio.sleep(0)
        self.assertTrue(task.cancelled())
        self.assertIsNone(game_manager.get_solo_session(user_id))


class TestFloodErrorResilienceAndSafeEditing(unittest.IsolatedAsyncioTestCase):
    async def test_safe_edit_handles_telegram_retry_after(self):
        """safe_edit_question_message catches TelegramRetryAfter without crashing."""
        bot = MagicMock()
        retry_err = TelegramRetryAfter(
            method=MagicMock(),
            message="Too Many Requests: retry after 4",
            retry_after=4
        )
        bot.edit_message_text = AsyncMock(side_effect=retry_err)

        result = await safe_edit_question_message(
            bot=bot,
            chat_id=1234,
            message_id=5678,
            text="New caption",
            reply_markup=None,
            has_photo=False
        )
        self.assertFalse(result)

    async def test_safe_edit_handles_message_not_modified(self):
        """safe_edit_question_message treats 'message is not modified' gracefully as True."""
        bot = MagicMock()
        not_mod_err = TelegramBadRequest(
            method=MagicMock(),
            message="Bad Request: message is not modified: specified new message content and reply markup are exactly the same"
        )
        bot.edit_message_caption = AsyncMock(side_effect=not_mod_err)

        result = await safe_edit_question_message(
            bot=bot,
            chat_id=1234,
            message_id=5678,
            text="Same caption",
            reply_markup=None,
            has_photo=True
        )
        self.assertTrue(result)

    async def test_safe_edit_handles_generic_floodwait_exception(self):
        """Custom or generic floodwait exceptions with retry_after or 'flood' in text are caught."""
        class MockFloodWait(Exception):
            retry_after = 7

        bot = MagicMock()
        bot.edit_message_text = AsyncMock(side_effect=MockFloodWait("FloodWait 7s"))

        result = await safe_edit_question_message(
            bot=bot,
            chat_id=1234,
            message_id=5678,
            text="Text",
            reply_markup=None,
            has_photo=False
        )
        self.assertFalse(result)

    async def test_safe_edit_propagates_cancellation(self):
        """CancelledError is never swallowed so tasks can abort immediately."""
        bot = MagicMock()
        bot.edit_message_text = AsyncMock(side_effect=asyncio.CancelledError())

        with self.assertRaises(asyncio.CancelledError):
            await safe_edit_question_message(
                bot=bot,
                chat_id=1234,
                message_id=5678,
                text="Text",
                reply_markup=None,
                has_photo=False
            )

    async def test_run_round_countdown_completes_when_edits_flood_limited(self):
        """run_round_countdown continues to timeout even if intermediary edits hit flood limits."""
        session = SoloGameSession(user_id=801, user_name="Laura", lang="en", round_time=6)
        session.next_round()
        session.round_message_id = 999

        bot = MagicMock()
        # Simulate flood error on edit
        bot.edit_message_text = AsyncMock(
            side_effect=TelegramRetryAfter(method=MagicMock(), message="Flood", retry_after=3)
        )

        timeout_called = False

        async def on_timeout():
            nonlocal timeout_called
            timeout_called = True

        with patch("games.flow.get_countdown_checkpoints", return_value=[4, 2]):
            with patch("asyncio.sleep", new_callable=AsyncMock):
                await run_round_countdown(
                    bot=bot,
                    chat_id=801,
                    session=session,
                    round_num=1,
                    timeout_callback=on_timeout,
                    is_solo=True
                )

        self.assertTrue(timeout_called)


class TestEdgeCasesAndLifelineConcurrency(unittest.IsolatedAsyncioTestCase):
    async def test_text_answer_cancels_timer_task_on_correct_match(self):
        """Typing the answer in group chat cancels the running countdown timer."""
        chat_id = -100999
        session = GameSession(chat_id=chat_id, lang="en")
        session.start_game()
        game_manager.set_session(chat_id, session)

        async def dummy_timer():
            await asyncio.sleep(100)

        task = asyncio.create_task(dummy_timer())
        session.timer_task = task
        session.round_message_id = 1111

        msg = MagicMock()
        msg.chat.id = chat_id
        msg.chat.type = "group"
        msg.from_user.id = 888
        msg.from_user.first_name = "Victor"
        msg.from_user.username = "victor888"
        msg.from_user.is_bot = False
        msg.text = session.current_question.correct_answer
        msg.reply = AsyncMock()

        bot = MagicMock()
        bot.db = MagicMock()
        bot.db.record_answer = AsyncMock()
        bot.edit_message_reply_markup = AsyncMock()

        with patch("handlers.text_answers.proceed_after_round", new_callable=AsyncMock):
            await check_group_text_answer(msg, bot)

        await asyncio.sleep(0)
        self.assertTrue(task.cancelled())
        self.assertIsNone(session.current_kb)
        game_manager.remove_session(chat_id)

    async def test_solo_answer_between_rounds_shows_round_ended(self):
        """Clicking answer when session is between_rounds announces 'Round has ended!'."""
        user_id = 901
        session = SoloGameSession(user_id=user_id, user_name="Oscar", lang="en")
        session.next_round()
        session.status = "between_rounds"
        game_manager.set_solo_session(user_id, session)

        cb = MagicMock()
        cb.data = "solo_ans:0"
        cb.from_user.id = user_id
        cb.answer = AsyncMock()

        bot = MagicMock()
        await cb_solo_answer(cb, bot)

        cb.answer.assert_called_once()
        args, kwargs = cb.answer.call_args
        self.assertIn("Round has ended", args[0])
        self.assertFalse(kwargs.get("show_alert", True))
        game_manager.remove_solo_session(user_id)

    async def test_solo_answer_ignores_eliminated_options(self):
        """Clicking an eliminated option does not dock lives or advance the game."""
        user_id = 902
        session = SoloGameSession(user_id=user_id, user_name="Penny", lang="en")
        session.next_round()
        # Eliminate option index 1
        session.eliminated_options.add(1)
        game_manager.set_solo_session(user_id, session)

        cb = MagicMock()
        cb.data = "solo_ans:1"
        cb.from_user.id = user_id
        cb.answer = AsyncMock()

        bot = MagicMock()
        await cb_solo_answer(cb, bot)

        cb.answer.assert_called_once()
        args, kwargs = cb.answer.call_args
        self.assertIn("eliminated", args[0])
        self.assertEqual(session.lives, 3)
        self.assertEqual(session.round_number, 1)
        game_manager.remove_solo_session(user_id)

    async def test_cmd_solo_duration_parsing(self):
        """cmd_solo parses round_time from arguments (e.g., /solo 60 or /solo flag 60)."""
        bot = MagicMock()
        mock_db = MagicMock()
        mock_db.get_or_create_user = AsyncMock(return_value={"language": "en"})
        bot.db = mock_db

        msg = MagicMock()
        msg.chat.id = 903
        msg.chat.type = "private"
        msg.from_user.id = 903
        msg.from_user.first_name = "Quinn"
        msg.text = "/solo 60"
        msg.answer = AsyncMock()

        with patch("handlers.commands.send_solo_round", new_callable=AsyncMock) as mock_send:
            await cmd_solo(msg, bot)
            s = game_manager.get_solo_session(903)
            self.assertIsNotNone(s)
            self.assertEqual(s.round_time, 60)
            self.assertEqual(s.mode, "mix")
            mock_send.assert_called_once()
            game_manager.remove_solo_session(903)

    async def test_cmd_solo_bare_cancels_existing_session(self):
        """cmd_solo bare stops any previously active session to prevent ghost timeouts."""
        user_id = 904
        old_session = SoloGameSession(user_id=user_id, user_name="Riley", lang="en")
        old_session.next_round()
        game_manager.set_solo_session(user_id, old_session)

        async def dummy_timer():
            await asyncio.sleep(100)

        task = asyncio.create_task(dummy_timer())
        old_session.timer_task = task

        bot = MagicMock()
        mock_db = MagicMock()
        mock_db.get_or_create_user = AsyncMock(return_value={"language": "en"})
        bot.db = mock_db

        msg = MagicMock()
        msg.chat.id = user_id
        msg.chat.type = "private"
        msg.from_user.id = user_id
        msg.from_user.first_name = "Riley"
        msg.text = "/solo"
        msg.answer = AsyncMock()

        await cmd_solo(msg, bot)
        await asyncio.sleep(0)
        self.assertTrue(task.cancelled())
        self.assertEqual(old_session.status, "finished")
        self.assertIsNone(game_manager.get_solo_session(user_id))

    async def test_lifeline_5050_preserves_eliminated_options_in_current_kb(self):
        """Using 50/50 updates session.current_kb so countdown edits do not restore buttons."""
        user_id = 905
        session = SoloGameSession(user_id=user_id, user_name="Sam", mode="flag", lang="en")
        session.next_round()
        session.round_message_id = 999
        game_manager.set_solo_session(user_id, session)

        cb = MagicMock()
        cb.from_user.id = user_id
        cb.message.edit_reply_markup = AsyncMock()
        cb.answer = AsyncMock()

        await cb_solo_5050(cb)
        self.assertFalse(session.has_5050)
        self.assertEqual(len(session.eliminated_options), 2)
        self.assertIsNotNone(session.current_kb)

        # Verify that safe_edit in countdown would use the updated current_kb
        bot = MagicMock()
        bot.edit_message_text = AsyncMock()
        await safe_edit_question_message(
            bot=bot,
            chat_id=user_id,
            message_id=session.round_message_id,
            text="Countdown 25s",
            reply_markup=session.current_kb,
            has_photo=False
        )
        _, kwargs = bot.edit_message_text.call_args
        self.assertEqual(kwargs.get("reply_markup"), session.current_kb)
        game_manager.remove_solo_session(user_id)


if __name__ == "__main__":
    unittest.main()
