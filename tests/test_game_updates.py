"""
Unit and Integration Tests for:
1. Category Selection:
   - 6 categories displayed as buttons (flag, capital, landmark, higher_lower, coat_of_arms, mix)
   - Category switching and solo mode per-category generation
2. Timer Options:
   - Explicit 30s and 60s options (default 30s)
   - Updating timer via setup buttons and cycling
3. Game Type Selection:
   - Group Game vs Solo Mode vs Daily Challenge keyboards
4. Host-Only Configuration Authorization:
   - Only the host who invoked /game can change settings or start the game in groups
   - Non-host clicks trigger show_alert=True with restriction alert
   - Once the game starts, all group members can answer and play together
"""

import unittest
from unittest.mock import AsyncMock, MagicMock, patch
import config
from locales.i18n import t
from games.models import GameMode, Question
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.manager import game_manager
from keyboards.game_kb import (
    get_setup_kb,
    get_category_selection_kb,
    get_game_type_kb,
)
from keyboards.inline import get_game_setup_keyboard
from handlers.callbacks import cb_game_setup, cb_solo_category, cb_game_type
from handlers.group_game import (
    set_mode_callback,
    set_time_callback,
    cycle_mode_callback,
    cycle_time_callback,
    cycle_rounds_callback,
    setup_cancel_callback,
    setup_launch_callback,
    TIME_OPTIONS,
    AVAILABLE_MODES,
)


class TestConfigAndKeyboards(unittest.TestCase):
    def test_default_timer_is_30s_and_options_30_60(self):
        """Verify DEFAULT_ROUND_TIME is 30s and timer options are [30, 60]."""
        self.assertEqual(config.DEFAULT_ROUND_TIME, 30)
        self.assertEqual(config.ROUND_TIME_OPTIONS, [30, 60])
        self.assertEqual(TIME_OPTIONS, [30, 60])

    def test_setup_kb_contains_all_categories_and_30_60_timers(self):
        """get_setup_kb must contain buttons for all 6 categories and explicit 30s/60s timers."""
        kb = get_setup_kb(session_id="test1234", mode="flag", rounds=5, round_time=30, lang="en")
        
        all_buttons = [btn for row in kb.inline_keyboard for btn in row]
        callback_datas = [btn.callback_data for btn in all_buttons]
        button_texts = [btn.text for btn in all_buttons]

        # All 6 categories present in callbacks
        expected_modes = ["flag", "capital", "landmark", "higher_lower", "coat_of_arms", "mix"]
        for m in expected_modes:
            self.assertTrue(
                any(f"setup:mode:{m}:test1234" in cb for cb in callback_datas),
                f"Mode {m} missing from get_setup_kb callback_data!"
            )

        # Flag is currently selected, so it should have checkmark
        flag_btn = [btn for btn in all_buttons if f"setup:mode:flag:test1234" in btn.callback_data][0]
        self.assertIn("✅", flag_btn.text)

        # Explicit 30s and 60s timer buttons
        self.assertTrue(any("setup:time:30:test1234" in cb for cb in callback_datas))
        self.assertTrue(any("setup:time:60:test1234" in cb for cb in callback_datas))
        
        # 30s is selected, so it should have checkmark
        t30_btn = [btn for btn in all_buttons if "setup:time:30:test1234" in btn.callback_data][0]
        self.assertIn("✅", t30_btn.text)
        t60_btn = [btn for btn in all_buttons if "setup:time:60:test1234" in btn.callback_data][0]
        self.assertNotIn("✅", t60_btn.text)

        # Start and Cancel buttons present
        self.assertTrue(any("setup:start:test1234" in cb for cb in callback_datas))
        self.assertTrue(any("setup:cancel:test1234" in cb for cb in callback_datas))

    def test_inline_get_game_setup_keyboard_contains_categories_and_timers(self):
        """get_game_setup_keyboard in inline.py must also contain categories and 30s/60s timers."""
        kb = get_game_setup_keyboard(chat_id=123, mode="capital", rounds=5, time_sec=60, lang="en")
        all_buttons = [btn for row in kb.inline_keyboard for btn in row]
        callback_datas = [btn.callback_data for btn in all_buttons]

        for m in ["flag", "capital", "landmark", "higher_lower", "coat_of_arms", "mix"]:
            self.assertTrue(any(f"setup_set_mode:123:{m}" in cb for cb in callback_datas))

        self.assertTrue(any("setup_set_time:123:30" in cb for cb in callback_datas))
        self.assertTrue(any("setup_set_time:123:60" in cb for cb in callback_datas))

        # 60s has checkmark
        t60_btn = [btn for btn in all_buttons if "setup_set_time:123:60" in btn.callback_data][0]
        self.assertIn("✅", t60_btn.text)

    def test_category_selection_kb_and_game_type_kb(self):
        """Verify standalone category keyboard and game type keyboard."""
        cat_kb = get_category_selection_kb(prefix="solo_cat", lang="en")
        cat_callbacks = [btn.callback_data for row in cat_kb.inline_keyboard for btn in row]
        for m in ["flag", "capital", "landmark", "higher_lower", "coat_of_arms", "mix"]:
            self.assertIn(f"solo_cat:{m}", cat_callbacks)
        self.assertIn("solo_cat:back", cat_callbacks)

        type_kb = get_game_type_kb(lang="en", bot_username="GeoBot")
        type_callbacks = [btn.callback_data for row in type_kb.inline_keyboard for btn in row if btn.callback_data]
        self.assertIn("game_type:solo", type_callbacks)
        self.assertIn("game_type:daily", type_callbacks)
        self.assertIn("game_type:menu", type_callbacks)


class TestHostOnlyAuthorizationInCallbacks(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.chat_id = -100112233
        self.host_id = 1111
        self.other_user_id = 9999
        self.session = GameSession(
            chat_id=self.chat_id,
            created_by_user_id=self.host_id,
            host_id=self.host_id,
            host_name="HostAlice",
            is_group=True,
            lang="en",
            mode="mix",
            total_rounds=5,
            round_time=30
        )
        game_manager.set_session(self.chat_id, self.session)
        self.bot = MagicMock()

    async def asyncTearDown(self):
        game_manager.remove_session(self.chat_id)

    async def test_non_host_setup_click_triggers_alert(self):
        """When a non-host user clicks any setup button, show_alert=True is shown."""
        query = MagicMock()
        query.message.chat.id = self.chat_id
        query.from_user.id = self.other_user_id
        query.from_user.first_name = "IntruderBob"
        query.data = f"setup:mode:flag:{self.session.session_id}"
        query.answer = AsyncMock()

        await cb_game_setup(query, self.bot)

        # Must trigger query.answer with show_alert=True and host message
        query.answer.assert_called_once()
        args, kwargs = query.answer.call_args
        self.assertTrue(kwargs.get("show_alert"))
        alert_text = args[0] if args else kwargs.get("text", "")
        self.assertIn("host", alert_text.lower())

        # Session mode must NOT have changed
        self.assertEqual(self.session.mode, "mix")

    async def test_non_host_cannot_start_or_cancel_game(self):
        """Non-host cannot trigger start or cancel."""
        # Non-host tries to start
        query_start = MagicMock()
        query_start.message.chat.id = self.chat_id
        query_start.from_user.id = self.other_user_id
        query_start.data = f"setup:start:{self.session.session_id}"
        query_start.answer = AsyncMock()

        await cb_game_setup(query_start, self.bot)
        query_start.answer.assert_called_once()
        self.assertTrue(query_start.answer.call_args[1].get("show_alert"))
        self.assertEqual(self.session.status, "setup")

        # Non-host tries to cancel
        query_cancel = MagicMock()
        query_cancel.message.chat.id = self.chat_id
        query_cancel.from_user.id = self.other_user_id
        query_cancel.data = f"setup:cancel:{self.session.session_id}"
        query_cancel.answer = AsyncMock()

        await cb_game_setup(query_cancel, self.bot)
        query_cancel.answer.assert_called_once()
        self.assertTrue(query_cancel.answer.call_args[1].get("show_alert"))
        self.assertIsNotNone(game_manager.get_session(self.chat_id))

    async def test_host_can_change_category_and_timer(self):
        """Host can freely change mode, time, and rounds."""
        # 1. Host sets category to 'flag'
        query_mode = MagicMock()
        query_mode.message.chat.id = self.chat_id
        query_mode.from_user.id = self.host_id
        query_mode.data = f"setup:mode:flag:{self.session.session_id}"
        query_mode.answer = AsyncMock()
        query_mode.message.edit_reply_markup = AsyncMock()

        await cb_game_setup(query_mode, self.bot)
        self.assertEqual(self.session.mode, "flag")

        # 2. Host sets timer to 60s
        query_time = MagicMock()
        query_time.message.chat.id = self.chat_id
        query_time.from_user.id = self.host_id
        query_time.data = f"setup:time:60:{self.session.session_id}"
        query_time.answer = AsyncMock()
        query_time.message.edit_reply_markup = AsyncMock()

        await cb_game_setup(query_time, self.bot)
        self.assertEqual(self.session.round_time, 60)

        # 3. Host sets timer back to 30s
        query_time_30 = MagicMock()
        query_time_30.message.chat.id = self.chat_id
        query_time_30.from_user.id = self.host_id
        query_time_30.data = f"setup:time:30:{self.session.session_id}"
        query_time_30.answer = AsyncMock()
        query_time_30.message.edit_reply_markup = AsyncMock()

        await cb_game_setup(query_time_30, self.bot)
        self.assertEqual(self.session.round_time, 30)

    async def test_all_group_members_can_answer_once_game_starts(self):
        """Once host launches game, all group members (non-hosts) can answer."""
        self.session.start_game()
        self.assertEqual(self.session.status, "in_progress")
        q = self.session.current_question

        # Non-host user answers correctly
        res, points, elapsed = await self.session.check_answer(
            user_id=self.other_user_id,
            user_name="OtherMember",
            option_index=q.correct_index
        )
        self.assertEqual(res, "correct")
        self.assertGreaterEqual(points, config.POINTS_CORRECT)
        self.assertEqual(self.session.scores[self.other_user_id], points)


class TestGroupGameHandlersHostAuthorization(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        from game.engine import game_manager as engine_gm
        self.chat_id = -100998877
        self.host_id = 777
        self.intruder_id = 888
        self.gm = engine_gm
        self.gm.setup_states[self.chat_id] = {
            "host_id": self.host_id,
            "host_name": "HostLeader",
            "mode": "mix",
            "rounds": 5,
            "time": 30,
            "lang": "en"
        }

    async def asyncTearDown(self):
        if self.chat_id in self.gm.setup_states:
            del self.gm.setup_states[self.chat_id]

    async def test_group_game_callbacks_host_check(self):
        """Non-host is rejected across all setup callbacks in group_game.py."""
        # Setup intruder callback
        cb = MagicMock()
        cb.from_user.id = self.intruder_id
        cb.answer = AsyncMock()

        # 1. set_mode
        cb.data = f"setup_set_mode:{self.chat_id}:flag"
        await set_mode_callback(cb)
        cb.answer.assert_called_with(t("host_only_settings_alert", "en"), show_alert=True)
        self.assertEqual(self.gm.setup_states[self.chat_id]["mode"], "mix")

        # 2. set_time
        cb.answer.reset_mock()
        cb.data = f"setup_set_time:{self.chat_id}:60"
        await set_time_callback(cb)
        cb.answer.assert_called_with(t("host_only_settings_alert", "en"), show_alert=True)
        self.assertEqual(self.gm.setup_states[self.chat_id]["time"], 30)

        # 3. cycle_mode
        cb.answer.reset_mock()
        cb.data = f"setup_cycle_mode:{self.chat_id}"
        await cycle_mode_callback(cb)
        cb.answer.assert_called_with(t("host_only_settings_alert", "en"), show_alert=True)

        # 4. cycle_rounds
        cb.answer.reset_mock()
        cb.data = f"setup_cycle_rounds:{self.chat_id}"
        await cycle_rounds_callback(cb)
        cb.answer.assert_called_with(t("host_only_settings_alert", "en"), show_alert=True)

        # 5. cycle_time
        cb.answer.reset_mock()
        cb.data = f"setup_cycle_time:{self.chat_id}"
        await cycle_time_callback(cb)
        cb.answer.assert_called_with(t("host_only_settings_alert", "en"), show_alert=True)

        # 6. cancel
        cb.answer.reset_mock()
        cb.data = f"setup_cancel:{self.chat_id}"
        await setup_cancel_callback(cb)
        cb.answer.assert_called_with(t("host_only_settings_alert", "en"), show_alert=True)
        self.assertIn(self.chat_id, self.gm.setup_states)

        # 7. launch
        cb.answer.reset_mock()
        cb.data = f"setup_launch:{self.chat_id}"
        await setup_launch_callback(cb, MagicMock())
        cb.answer.assert_called_with(t("host_only_settings_alert", "en"), show_alert=True)

    async def test_group_game_callbacks_host_success(self):
        """Host successfully updates mode and time."""
        cb_host = MagicMock()
        cb_host.from_user.id = self.host_id
        cb_host.answer = AsyncMock()
        cb_host.message.edit_reply_markup = AsyncMock()

        # Set mode to landmark
        cb_host.data = f"setup_set_mode:{self.chat_id}:landmark"
        await set_mode_callback(cb_host)
        self.assertEqual(self.gm.setup_states[self.chat_id]["mode"], "landmark")

        # Set time to 60
        cb_host.data = f"setup_set_time:{self.chat_id}:60"
        await set_time_callback(cb_host)
        self.assertEqual(self.gm.setup_states[self.chat_id]["time"], 60)


class TestSoloCategorySelection(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.user_id = 554433
        self.bot = MagicMock()
        mock_db = MagicMock()
        mock_db.get_user = AsyncMock(return_value={"language": "en"})
        self.bot.db = mock_db

    async def asyncTearDown(self):
        game_manager.remove_solo_session(self.user_id)

    async def test_solo_session_with_specific_category(self):
        """SoloGameSession initialized with a specific mode generates questions for that mode."""
        for mode in [GameMode.FLAG, GameMode.CAPITAL, GameMode.LANDMARK, GameMode.HIGHER_LOWER, GameMode.COAT_OF_ARMS]:
            solo = SoloGameSession(user_id=self.user_id, user_name="TestHero", lang="en", mode=mode)
            self.assertEqual(solo.mode, mode)
            q = solo.next_round()
            self.assertEqual(q.mode, mode)

    async def test_cb_solo_category_starts_chosen_mode(self):
        """cb_solo_category callback starts solo session in chosen mode."""
        query = MagicMock()
        query.from_user.id = self.user_id
        query.from_user.first_name = "Hero"
        query.data = "solo_cat:flag"
        query.answer = AsyncMock()
        query.message.delete = AsyncMock()

        with patch("handlers.callbacks.send_solo_round", new_callable=AsyncMock) as mock_send:
            await cb_solo_category(query, self.bot)
            mock_send.assert_called_once()
            solo_session = game_manager.get_solo_session(self.user_id)
            self.assertIsNotNone(solo_session)
            self.assertEqual(solo_session.mode, "flag")
            self.assertEqual(solo_session.round_number, 1)

    async def test_cb_solo_answer_records_user_name_and_username(self):
        """cb_solo_answer passes user's first_name and username to db.record_answer."""
        from handlers.callbacks import cb_solo_answer
        solo = SoloGameSession(user_id=self.user_id, user_name="TestHero", lang="en", mode="flag")
        solo.next_round()
        game_manager.set_solo_session(self.user_id, solo)

        query = MagicMock()
        query.from_user.id = self.user_id
        query.from_user.first_name = "Alice"
        query.from_user.username = "alice_geo"
        query.data = f"solo_ans:{solo.current_question.correct_index}"
        query.answer = AsyncMock()
        query.message.edit_reply_markup = AsyncMock()

        mock_db = MagicMock()
        mock_db.record_answer = AsyncMock()
        self.bot.db = mock_db

        with patch("handlers.callbacks.send_solo_round", new_callable=AsyncMock):
            await cb_solo_answer(query, self.bot)

        mock_db.record_answer.assert_called_once()
        _, kwargs = mock_db.record_answer.call_args
        self.assertEqual(kwargs.get("user_name"), "Alice")
        self.assertEqual(kwargs.get("username"), "alice_geo")

    async def test_cb_solo_hint_refreshes_reply_markup(self):
        """cb_solo_hint updates the reply markup to reflect used hint."""
        from handlers.callbacks import cb_solo_hint
        solo = SoloGameSession(user_id=self.user_id, user_name="TestHero", lang="en", mode="flag")
        solo.next_round()
        game_manager.set_solo_session(self.user_id, solo)

        query = MagicMock()
        query.from_user.id = self.user_id
        query.data = "solo_hint"
        query.answer = AsyncMock()
        query.message.edit_reply_markup = AsyncMock()

        await cb_solo_hint(query)
        self.assertFalse(solo.has_hint)
        query.message.edit_reply_markup.assert_called_once()


class TestEdgeCasesAndAudits(unittest.IsolatedAsyncioTestCase):
    def test_timer_buttons_localization_across_languages(self):
        """Timer buttons use localized text across English, Uzbek, and Russian."""
        # Uzbek
        kb_uz = get_setup_kb(session_id="uz1", mode="mix", rounds=5, round_time=30, lang="uz")
        texts_uz = [btn.text for row in kb_uz.inline_keyboard for btn in row]
        self.assertTrue(any("30s" in t for t in texts_uz))

        # Russian (uses Russian 'с' character)
        kb_ru = get_setup_kb(session_id="ru1", mode="mix", rounds=5, round_time=30, lang="ru")
        texts_ru = [btn.text for row in kb_ru.inline_keyboard for btn in row]
        self.assertTrue(any("30с" in t for t in texts_ru))

    async def test_cb_game_setup_answers_query_even_when_edit_raises_exception(self):
        """query.answer is always called, even if Telegram raises 'message is not modified'."""
        chat_id = -1005544
        host_id = 9988
        session = GameSession(chat_id=chat_id, host_id=host_id, lang="en")
        game_manager.set_session(chat_id, session)

        bot = MagicMock()
        query = MagicMock()
        query.message.chat.id = chat_id
        query.from_user.id = host_id
        query.data = f"setup:time:30:{session.session_id}"
        query.answer = AsyncMock()
        # Simulate TelegramBadRequest: message is not modified
        query.message.edit_reply_markup = AsyncMock(side_effect=Exception("TelegramBadRequest: message not modified"))

        await cb_game_setup(query, bot)
        query.answer.assert_called_once()
        game_manager.remove_session(chat_id)

    async def test_duel_timer_uses_default_30s(self):
        """Duel game setup in callbacks and duel.py uses 30s timer, not 15s or 20s."""
        from handlers.callbacks import cb_duel
        from handlers.duel import handle_duel_accept, PENDING_DUELS

        chat_id = -1004433
        bot = MagicMock()
        mock_db = MagicMock()
        mock_db.get_chat_language = AsyncMock(return_value="en")
        mock_db.update_duel_status = AsyncMock()
        bot.db = mock_db
        bot.send_message = AsyncMock()

        # 1. cb_duel
        query = MagicMock()
        query.message.chat.id = chat_id
        query.from_user.id = 222
        query.data = "duel:accept:111:222:55"
        query.answer = AsyncMock()
        query.message.delete = AsyncMock()

        with patch("handlers.callbacks.send_round_question", new_callable=AsyncMock):
            await cb_duel(query, bot)
            active_session = game_manager.get_session(chat_id)
            self.assertIsNotNone(active_session)
            self.assertEqual(active_session.round_time, config.DEFAULT_ROUND_TIME)
            self.assertEqual(active_session.round_time, 30)
            game_manager.remove_session(chat_id)

        # 2. handle_duel_accept in duel.py
        PENDING_DUELS[99] = {
            "chat_id": chat_id,
            "challenger_id": 111,
            "challenger_name": "A",
            "opponent_id": 222,
            "opponent_name": "B",
            "lang": "en"
        }
        cb_d = MagicMock()
        cb_d.from_user.id = 222
        cb_d.data = "duel_acc:99"
        cb_d.answer = AsyncMock()
        cb_d.message.edit_text = AsyncMock()

        from game.engine import game_manager as engine_gm
        with patch("handlers.duel.launch_next_round", new_callable=AsyncMock), \
             patch("handlers.duel.update_duel_status", new_callable=AsyncMock):
            await handle_duel_accept(cb_d, bot)
            duel_game = engine_gm.get_group_game(chat_id)
            self.assertIsNotNone(duel_game)
            self.assertEqual(duel_game.round_time, config.DEFAULT_ROUND_TIME)
            self.assertEqual(duel_game.round_time, 30)
            engine_gm.remove_group_game(chat_id)

    async def test_round_timeout_clears_reply_markup(self):
        """When round timer expires, inline answer buttons are cleared."""
        from games.flow import handle_round_timeout
        from handlers.group_game import round_timer

        chat_id = -1008899
        bot = MagicMock()
        bot.edit_message_reply_markup = AsyncMock()
        bot.send_message = AsyncMock()

        # 1. games/flow.py
        session = GameSession(chat_id=chat_id, lang="en")
        session.start_game()
        session.round_message_id = 4567
        mock_db = MagicMock()

        with patch("games.flow.proceed_after_round", new_callable=AsyncMock):
            await handle_round_timeout(bot, chat_id, session, round_num=1, db=mock_db)
            bot.edit_message_reply_markup.assert_called_once_with(
                chat_id=chat_id,
                message_id=4567,
                reply_markup=None
            )

        # 2. handlers/group_game.py
        from game.engine import game_manager as engine_gm, GroupGameSession
        bot.edit_message_reply_markup.reset_mock()
        g_session = GroupGameSession(chat_id=chat_id, lang="en", host_id=123, host_name="Host")
        g_session.start_next_round()
        g_session.message_id = 9876
        engine_gm.set_group_game(chat_id, g_session)

        with patch("handlers.group_game.launch_next_round", new_callable=AsyncMock):
            await round_timer(chat_id=chat_id, round_num=1, duration=0, bot=bot)
            bot.edit_message_reply_markup.assert_called_once_with(
                chat_id=chat_id,
                message_id=9876,
                reply_markup=None
            )
            engine_gm.remove_group_game(chat_id)

    def test_group_game_session_stores_host_id_and_host_name(self):
        """GroupGameSession stores host_id and host_name."""
        from game.engine import GroupGameSession
        session = GroupGameSession(chat_id=123, host_id=999, host_name="Captain")
        self.assertEqual(session.host_id, 999)
        self.assertEqual(session.host_name, "Captain")

    async def test_solo_handler_category_selection_flow(self):
        """handlers/solo.py presents categories on /solo without args and starts chosen mode with args."""
        from handlers.solo import handle_solo_command, handle_menu_solo, handle_solo_category
        bot = MagicMock()
        bot.get_me = AsyncMock(return_value=MagicMock(username="GeoGuruBot"))

        with patch("handlers.solo.get_user_language", new_callable=AsyncMock, return_value="en"):
            # /solo without args sends category menu
            msg_no_args = MagicMock()
            msg_no_args.chat.type = "private"
            msg_no_args.from_user.id = 1122
            msg_no_args.text = "/solo"
            msg_no_args.answer = AsyncMock()

            await handle_solo_command(msg_no_args, bot)
            msg_no_args.answer.assert_called_once()
            _, kwargs = msg_no_args.answer.call_args
            self.assertIn("reply_markup", kwargs)

            # /solo flag starts flag mode
            msg_flag = MagicMock()
            msg_flag.chat.id = 1122
            msg_flag.chat.type = "private"
            msg_flag.from_user.id = 1122
            msg_flag.text = "/solo flag"
            with patch("handlers.solo.send_solo_question", new_callable=AsyncMock) as mock_q:
                await handle_solo_command(msg_flag, bot)
                mock_q.assert_called_once()
                from game.engine import game_manager as engine_gm
                s = engine_gm.get_solo_game(1122)
                self.assertIsNotNone(s)
                self.assertEqual(s.mode, "flag")
                engine_gm.remove_solo_game(1122)


if __name__ == "__main__":
    unittest.main()
