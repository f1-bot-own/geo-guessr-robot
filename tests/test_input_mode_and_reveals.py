"""
Tests for Input Mode Configuration (Buttons / Text / Both) and Correct Answer Reveal.
Verifies:
1. Input mode settings in group setup and solo lobby (buttons, text, both).
2. Question keyboard in text-only mode (options hidden, lifelines preserved).
3. Blocking of button clicks when input_mode is text-only.
4. Ignoring chat text answers when input_mode is buttons-only.
5. Solo text answer evaluation (shortcuts, multilingual names, distractors, eliminated options).
6. Prominent reveal of the correct answer on every round end (correct, wrong, timeout)
   across EN, UZ, and RU.
"""

import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, User, Chat

import config
from locales.i18n import t
from games.models import GameMode, Question
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.manager import game_manager
from keyboards.game_kb import (
    get_setup_kb,
    get_category_selection_kb,
    get_solo_question_kb,
    get_solo_setup_kb,
)
from keyboards.inline import (
    get_game_setup_keyboard,
    get_solo_keyboard,
    get_question_keyboard,
)
from handlers.callbacks import (
    cb_group_answer,
    cb_solo_answer,
    cb_game_setup,
    cb_solo_category,
)
from handlers.text_answers import (
    check_group_text_answer,
    check_solo_text_answer,
    _normalize,
)
from games.flow import (
    handle_round_timeout,
    handle_solo_timeout,
)


class TestInputModeKeyboards(unittest.TestCase):
    def test_group_setup_kb_input_modes(self):
        """Setup keyboard has input mode row and reflects selected mode."""
        for mode in ("buttons", "text", "both"):
            kb = get_setup_kb(
                session_id="s123",
                mode="mix",
                rounds=5,
                round_time=30,
                lang="en",
                input_mode=mode
            )
            # Find the input mode buttons row
            all_buttons = [btn for row in kb.inline_keyboard for btn in row]
            callbacks = [b.callback_data for b in all_buttons]

            self.assertIn("setup:input:buttons:s123", callbacks)
            self.assertIn("setup:input:text:s123", callbacks)
            self.assertIn("setup:input:both:s123", callbacks)

            # Selected button should have indicator checkmark
            for btn in all_buttons:
                if btn.callback_data == f"setup:input:{mode}:s123":
                    self.assertTrue("🔘" in btn.text or "✍️" in btn.text or "🔀" in btn.text)
                    self.assertIn("✅", btn.text)

    def test_solo_category_selection_kb_input_modes(self):
        """Category selection keyboard contains input mode toggle row."""
        for mode in ("buttons", "text", "both"):
            kb = get_category_selection_kb(prefix="solo_cat", lang="en", input_mode=mode)
            all_buttons = [btn for row in kb.inline_keyboard for btn in row]
            callbacks = [b.callback_data for b in all_buttons]

            self.assertIn("solo_cat:input:buttons", callbacks)
            self.assertIn("solo_cat:input:text", callbacks)
            self.assertIn("solo_cat:input:both", callbacks)

            for btn in all_buttons:
                if btn.callback_data == f"solo_cat:input:{mode}":
                    self.assertIn("✅", btn.text)

    def test_solo_question_kb_text_only_mode(self):
        """In text-only mode, solo keyboard omits choice options but preserves lifelines."""
        options = ["France", "Germany", "Italy", "Spain"]
        # Normal mode
        kb_normal = get_solo_question_kb(
            options=options,
            eliminated=set(),
            has_hint=True,
            has_5050=True,
            lang="en",
            text_only=False
        )
        self.assertIsNotNone(kb_normal)
        texts_normal = [btn.text for row in kb_normal.inline_keyboard for btn in row]
        self.assertIn("France", texts_normal)
        self.assertIn("💡 Hint", texts_normal)
        self.assertIn("✂️ 50/50", texts_normal)

        # Text-only mode: only lifelines present
        kb_text = get_solo_question_kb(
            options=options,
            eliminated=set(),
            has_hint=True,
            has_5050=True,
            lang="en",
            text_only=True
        )
        self.assertIsNotNone(kb_text)
        texts_text = [btn.text for row in kb_text.inline_keyboard for btn in row]
        self.assertNotIn("France", texts_text)
        self.assertNotIn("Germany", texts_text)
        self.assertIn("💡 Hint", texts_text)
        self.assertIn("✂️ 50/50", texts_text)

        # Text-only mode with lifelines exhausted shows disabled icons
        kb_empty = get_solo_question_kb(
            options=options,
            eliminated=set(),
            has_hint=False,
            has_5050=False,
            lang="en",
            text_only=True
        )
        self.assertIsNotNone(kb_empty)
        texts_empty = [btn.text for row in kb_empty.inline_keyboard for btn in row]
        self.assertIn("💡 ✖️", texts_empty)
        self.assertIn("✂️ ✖️", texts_empty)

    def test_inline_get_solo_keyboard_text_only(self):
        """inline.py get_solo_keyboard respects text_only flag."""
        from game.modes import QuestionOption
        options = [
            QuestionOption(id="a", text="Option A", is_correct=True),
            QuestionOption(id="b", text="Option B", is_correct=False),
        ]
        lifelines = {"hint": True, "5050": False}

        # Normal
        kb = get_solo_keyboard(1, options, set(), lifelines, lang="en", text_only=False)
        self.assertIsNotNone(kb)
        texts = [btn.text for row in kb.inline_keyboard for btn in row]
        self.assertIn("Option A", texts)

        # Text only
        kb_text = get_solo_keyboard(1, options, set(), lifelines, lang="en", text_only=True)
        self.assertIsNotNone(kb_text)
        texts_text = [btn.text for row in kb_text.inline_keyboard for btn in row]
        self.assertNotIn("Option A", texts_text)
        self.assertIn("💡 Hint", texts_text)


class TestCorrectAnswerRevealLocales(unittest.TestCase):
    def test_locales_reveal_translations(self):
        """All languages must have proper correct answer reveal keys."""
        ans = "Tashkent"
        for lang, expected_phrase in [
            ("en", "✅ Correct Answer: <b>Tashkent</b>"),
            ("uz", "✅ To'g'ri javob: <b>Tashkent</b>"),
            ("ru", "✅ Правильный ответ: <b>Tashkent</b>"),
        ]:
            rev = t("correct_answer_reveal", lang, answer=ans)
            self.assertEqual(rev, expected_phrase)

            solo_cor = t("solo_correct_answer_announcement", lang, points=100, answer=ans)
            self.assertIn(expected_phrase, solo_cor)

            solo_wrg = t("solo_wrong_answer_announcement", lang, answer=ans, lives="❤️❤️")
            self.assertIn(expected_phrase, solo_wrg)

            solo_gov = t("solo_wrong_game_over_announcement", lang, answer=ans, game_over="GAME OVER")
            self.assertIn(expected_phrase, solo_gov)


class TestInputModeCallbacksAndGuards(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.bot = AsyncMock()
        self.chat = Chat(id=-100123, type="group")
        self.user = User(id=42, is_bot=False, first_name="Tester", username="tester")

    async def test_group_setup_toggle_input_mode(self):
        """Clicking input mode in group setup updates session.input_mode."""
        session = GameSession(chat_id=-100123, host_id=42, host_name="Tester")
        game_manager.set_session(-100123, session)

        query = MagicMock(spec=CallbackQuery)
        query.data = f"setup:input:text:{session.session_id}"
        query.from_user = self.user
        query.message = MagicMock()
        query.message.chat = self.chat
        query.message.edit_reply_markup = AsyncMock()
        query.answer = AsyncMock()

        await cb_game_setup(query, self.bot)

        self.assertEqual(session.input_mode, "text")
        query.message.edit_reply_markup.assert_called_once()

    async def test_solo_category_toggle_input_mode(self):
        """Clicking input mode in solo category selection updates solo setup state."""
        query = MagicMock(spec=CallbackQuery)
        query.data = "solo_cat:input:buttons"
        query.from_user = self.user
        query.message = MagicMock()
        query.message.chat = Chat(id=42, type="private")
        query.message.edit_reply_markup = AsyncMock()
        query.answer = AsyncMock()

        with patch("handlers.callbacks.get_db") as mock_db:
            db_inst = AsyncMock()
            db_inst.get_user.return_value = {"language": "en"}
            mock_db.return_value = db_inst

            await cb_solo_category(query, self.bot)

            state = game_manager.get_solo_setup_state(42)
            self.assertEqual(state.get("input_mode"), "buttons")
            query.message.edit_reply_markup.assert_called_once()

    async def test_button_answer_blocked_in_text_only_group_game(self):
        """In text-only mode, clicking a group answer button shows an alert and ignores answer."""
        session = GameSession(chat_id=-100123, host_id=42, host_name="Tester", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            text="Capital of France?",
            options=["Paris", "Berlin", "Rome", "Madrid"],
            correct_index=0,
            correct_answer="Paris",
            mode=GameMode.CAPITAL,
            country_code="FR"
        )
        game_manager.set_session(-100123, session)

        query = MagicMock(spec=CallbackQuery)
        query.data = f"ans:{session.session_id}:0"
        query.from_user = self.user
        query.message = MagicMock()
        query.message.chat = self.chat
        query.answer = AsyncMock()

        with patch("handlers.callbacks.get_db") as mock_db:
            mock_db.return_value = AsyncMock()
            await cb_group_answer(query, self.bot)

        query.answer.assert_called_once_with(
            "✍️ Text Only mode is enabled! Type your answer in the chat.",
            show_alert=True
        )
        self.assertEqual(len(session.scores), 0)

    async def test_button_answer_blocked_in_text_only_solo_game(self):
        """In text-only mode, clicking a solo answer button shows an alert and ignores answer."""
        session = SoloGameSession(user_id=42, user_name="Tester", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            text="Capital of Spain?",
            options=["Madrid", "Lisbon", "Rome", "Athens"],
            correct_index=0,
            correct_answer="Madrid",
            mode=GameMode.CAPITAL,
            country_code="ES"
        )
        game_manager.set_solo_session(42, session)

        query = MagicMock(spec=CallbackQuery)
        query.data = "solo_ans:0"
        query.from_user = self.user
        query.message = MagicMock()
        query.message.chat = Chat(id=42, type="private")
        query.answer = AsyncMock()

        await cb_solo_answer(query, self.bot)

        query.answer.assert_called_once_with(
            "✍️ Text Only mode is enabled! Type your answer in the chat.",
            show_alert=True
        )
        self.assertEqual(session.score, 0)


class TestTextAnswerHandling(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.bot = AsyncMock()
        self.user = User(id=42, is_bot=False, first_name="Player", username="player")

    async def test_solo_text_answer_ignored_in_buttons_mode(self):
        """In buttons-only mode, solo text answers in chat are ignored."""
        session = SoloGameSession(user_id=42, user_name="Player", input_mode="buttons")
        session.status = "in_progress"
        session.current_question = Question(
            text="Capital of Germany?",
            options=["Munich", "Berlin", "Frankfurt", "Hamburg"],
            correct_index=1,
            correct_answer="Berlin",
            mode=GameMode.CAPITAL,
            country_code="DE"
        )
        game_manager.set_solo_session(42, session)

        msg = MagicMock(spec=Message)
        msg.chat = Chat(id=42, type="private")
        msg.from_user = self.user
        msg.text = "Berlin"
        msg.reply = AsyncMock()

        await check_solo_text_answer(msg, self.bot)

        msg.reply.assert_not_called()
        self.assertEqual(session.score, 0)

    async def test_solo_text_answer_correct_shortcut_in_both_mode(self):
        """Typing '2' or 'b' when option 2 is correct awards points and reveals answer."""
        session = SoloGameSession(user_id=42, user_name="Player", input_mode="both")
        session.status = "in_progress"
        session.current_question = Question(
            text="Capital of Germany?",
            options=["Munich", "Berlin", "Frankfurt", "Hamburg"],
            correct_index=1,
            correct_answer="Berlin",
            mode=GameMode.CAPITAL,
            country_code="DE"
        )
        game_manager.set_solo_session(42, session)

        msg = MagicMock(spec=Message)
        msg.chat = Chat(id=42, type="private")
        msg.from_user = self.user
        msg.text = "2"
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_get_db, \
             patch("handlers.text_answers.send_solo_round", new_callable=AsyncMock) as mock_send_next:
            db_inst = AsyncMock()
            mock_get_db.return_value = db_inst

            await check_solo_text_answer(msg, self.bot)

            self.assertGreater(session.score, 0)
            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("✅ Correct Answer: <b>Berlin</b>", reply_text)
            mock_send_next.assert_called_once()

    async def test_solo_text_answer_correct_multilingual_name(self):
        """Typing answer name in Uzbek or Russian matches and awards points."""
        session = SoloGameSession(user_id=42, user_name="Player", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            text="Identify this country by flag",
            options=["Uzbekistan", "Kazakhstan", "Kyrgyzstan", "Tajikistan"],
            correct_index=0,
            correct_answer="Uzbekistan",
            mode=GameMode.FLAG,
            country_code="UZ"
        )
        game_manager.set_solo_session(42, session)

        # In Uzbek: "O'zbekiston"
        msg = MagicMock(spec=Message)
        msg.chat = Chat(id=42, type="private")
        msg.from_user = self.user
        msg.text = "O'zbekiston"
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_get_db, \
             patch("handlers.text_answers.send_solo_round", new_callable=AsyncMock) as mock_send_next:
            db_inst = AsyncMock()
            mock_get_db.return_value = db_inst

            await check_solo_text_answer(msg, self.bot)

            self.assertGreater(session.score, 0)
            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("✅ Correct Answer: <b>Uzbekistan</b>", reply_text)

    async def test_solo_text_answer_eliminated_option_rejected(self):
        """Typing an option index eliminated by 50/50 is rejected without penalty."""
        session = SoloGameSession(user_id=42, user_name="Player", input_mode="text")
        session.status = "in_progress"
        session.eliminated_options.add(2)
        session.current_question = Question(
            text="Which country?",
            options=["A", "B", "C", "D"],
            correct_index=0,
            correct_answer="A",
            mode=GameMode.FLAG,
            country_code="FR"
        )
        game_manager.set_solo_session(42, session)

        msg = MagicMock(spec=Message)
        msg.chat = Chat(id=42, type="private")
        msg.from_user = self.user
        msg.text = "3"  # Index 2
        msg.reply = AsyncMock()

        await check_solo_text_answer(msg, self.bot)

        msg.reply.assert_called_once_with("This option has been eliminated!", parse_mode="HTML")
        self.assertEqual(session.lives, 3)

    async def test_solo_text_answer_wrong_reveals_correct_answer(self):
        """A wrong text guess deducts a life and reveals the correct answer."""
        session = SoloGameSession(user_id=42, user_name="Player", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            text="Capital of Italy?",
            options=["Rome", "Milan", "Naples", "Turin"],
            correct_index=0,
            correct_answer="Rome",
            mode=GameMode.CAPITAL,
            country_code="IT"
        )
        game_manager.set_solo_session(42, session)

        msg = MagicMock(spec=Message)
        msg.chat = Chat(id=42, type="private")
        msg.from_user = self.user
        msg.text = "Milan"
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_get_db, \
             patch("handlers.text_answers.send_solo_round", new_callable=AsyncMock) as mock_send_next:
            db_inst = AsyncMock()
            mock_get_db.return_value = db_inst

            await check_solo_text_answer(msg, self.bot)

            self.assertEqual(session.lives, 2)
            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("✅ Correct Answer: <b>Rome</b>", reply_text)
            self.assertIn("❤️ Lives remaining: ❤️❤️", reply_text)


class TestTimeoutCorrectAnswerAnnouncements(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.bot = AsyncMock()
        self.chat = Chat(id=-100123, type="group")
        self.user = User(id=42, is_bot=False, first_name="Tester", username="tester")

    async def test_group_timeout_reveals_correct_answer(self):
        """Group round timeout announcement prominently reveals correct answer."""
        session = GameSession(chat_id=-100123, host_id=42, host_name="Tester", lang="en")
        session.status = "in_progress"
        session.current_question = Question(
            text="Capital of Japan?",
            options=["Tokyo", "Kyoto", "Osaka", "Nagoya"],
            correct_index=0,
            correct_answer="Tokyo",
            mode=GameMode.CAPITAL,
            country_code="JP"
        )
        game_manager.set_session(-100123, session)

        with patch("games.flow.proceed_after_round", new_callable=AsyncMock):
            await handle_round_timeout(self.bot, -100123, session, session.current_round, AsyncMock())

            self.bot.send_message.assert_called()
            sent_text = self.bot.send_message.call_args[1]["text"]
            self.assertIn("✅ Correct Answer: <b>Tokyo</b>", sent_text)

    async def test_solo_timeout_reveals_correct_answer(self):
        """Solo round timeout announcement prominently reveals correct answer."""
        session = SoloGameSession(user_id=42, user_name="Tester", lang="uz")
        session.status = "in_progress"
        session.current_question = Question(
            text="Qaysi davlat poytaxti?",
            options=["Madrid", "Rim", "Parij", "Berlin"],
            correct_index=2,
            correct_answer="Parij",
            mode=GameMode.CAPITAL,
            country_code="FR"
        )
        game_manager.set_solo_session(42, session)

        with patch("games.flow.send_solo_round", new_callable=AsyncMock):
            await handle_solo_timeout(self.bot, 42, session, session.round_number, AsyncMock(), wait_seconds=0)

            self.bot.send_message.assert_called()
            sent_text = self.bot.send_message.call_args[1]["text"]
            self.assertIn("✅ To'g'ri javob: <b>Parij</b>", sent_text)

    async def test_solo_timeout_reveals_correct_answer_russian_lives_label(self):
        """Solo round timeout announcement in Russian contains localized lives text."""
        session = SoloGameSession(user_id=42, user_name="Tester", lang="ru")
        session.status = "in_progress"
        session.current_question = Question(
            text="Какая столица?",
            options=["Мадрид", "Рим", "Париж", "Берлин"],
            correct_index=2,
            correct_answer="Париж",
            mode=GameMode.CAPITAL,
            country_code="FR"
        )
        game_manager.set_solo_session(42, session)

        with patch("games.flow.send_solo_round", new_callable=AsyncMock):
            await handle_solo_timeout(self.bot, 42, session, session.round_number, AsyncMock(), wait_seconds=0)

            self.bot.send_message.assert_called()
            sent_text = self.bot.send_message.call_args[1]["text"]
            self.assertIn("✅ Правильный ответ: <b>Париж</b>", sent_text)
            self.assertIn("Осталось жизней: ❤️❤️", sent_text)

    async def test_capital_question_does_not_accept_country_name(self):
        """Typing country name (France) when question asks for capital (Paris) is rejected/wrong."""
        session = GameSession(chat_id=-100123, host_id=42, host_name="Tester", lang="en", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            text="What is the capital of France?",
            options=["Paris", "Berlin", "Rome", "Madrid"],
            correct_index=0,
            correct_answer="Paris",
            mode=GameMode.CAPITAL,
            country_code="FR"
        )
        game_manager.set_session(-100123, session)

        msg = MagicMock(spec=Message)
        msg.chat = self.chat
        msg.from_user = self.user
        msg.text = "France"
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_db, \
             patch("games.flow.proceed_after_round", new_callable=AsyncMock) as mock_proceed:
            mock_db.return_value = AsyncMock()
            await check_group_text_answer(msg, self.bot)

            # France is the country, not the capital! It should NOT be accepted as correct!
            self.assertEqual(session.scores.get(42, 0), 0)
            self.assertIn(42, session.answered_users_wrong)
            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("❌ Wrong!", reply_text)
            mock_proceed.assert_not_called()

    async def test_group_text_answer_evaluates_arbitrary_country_in_text_mode(self):
        """In text-only group mode, guessing an incorrect country not in options deducts points."""
        session = GameSession(chat_id=-100123, host_id=42, host_name="Tester", lang="en", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            text="Identify this country by flag",
            options=["Uzbekistan", "Kazakhstan", "Kyrgyzstan", "Tajikistan"],
            correct_index=0,
            correct_answer="Uzbekistan",
            mode=GameMode.FLAG,
            country_code="UZ"
        )
        game_manager.set_session(-100123, session)

        msg = MagicMock(spec=Message)
        msg.chat = self.chat
        msg.from_user = self.user
        msg.text = "Canada"  # Canada is not among the 4 options
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_db:
            db_inst = AsyncMock()
            mock_db.return_value = db_inst
            await check_group_text_answer(msg, self.bot)

            # User must receive wrong answer penalty and reply
            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("❌ Wrong! -20 pts", reply_text)
            db_inst.record_answer.assert_called_once_with(42, is_correct=False, points=-20, user_name="Tester", username="tester")

            # Subsequent attempt in the same round warns user that they already answered
            msg.reply.reset_mock()
            await check_group_text_answer(msg, self.bot)
            msg.reply.assert_called_once()
            reply_text2 = msg.reply.call_args[1]["text"]
            self.assertIn("you already gave an incorrect answer for this round", reply_text2)

    async def test_uzbek_name_matching_without_apostrophe(self):
        """Uzbek answer 'Ozbekiston' matches 'O'zbekiston'."""
        session = SoloGameSession(user_id=42, user_name="Player", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            text="Qaysi davlat?",
            options=["O'zbekiston", "Qozog'iston", "Qirg'iziston", "Tojikiston"],
            correct_index=0,
            correct_answer="O'zbekiston",
            mode=GameMode.FLAG,
            country_code="UZ"
        )
        game_manager.set_solo_session(42, session)

        msg = MagicMock(spec=Message)
        msg.chat = Chat(id=42, type="private")
        msg.from_user = self.user
        msg.text = "Ozbekiston"  # typed without apostrophe
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_get_db, \
             patch("handlers.text_answers.send_solo_round", new_callable=AsyncMock):
            mock_get_db.return_value = AsyncMock()
            await check_solo_text_answer(msg, self.bot)

            self.assertGreater(session.score, 0)
            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("O'zbekiston", reply_text)

    async def test_handlers_solo_input_category_toggle(self):
        """handlers.solo.handle_solo_category handles 'input' toggle without crashing."""
        from handlers.solo import handle_solo_category

        query = MagicMock(spec=CallbackQuery)
        query.data = "solo_cat:input:text"
        query.from_user = self.user
        query.message = MagicMock()
        query.message.chat = Chat(id=42, type="private")
        query.message.edit_reply_markup = AsyncMock()
        query.answer = AsyncMock()

        with patch("handlers.solo.get_user_language", new_callable=AsyncMock) as mock_lang:
            mock_lang.return_value = "en"
            await handle_solo_category(query, self.bot)

            state = game_manager.get_solo_setup_state(42)
            self.assertEqual(state.get("input_mode"), "text")
            query.message.edit_reply_markup.assert_called_once()


if __name__ == "__main__":
    unittest.main()
