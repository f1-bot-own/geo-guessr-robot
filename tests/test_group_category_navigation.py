"""
Unit and Integration Tests for Group Category Navigation and Interactive Sub-Modes.

Tests:
1. Category Hubs rendering by default (get_setup_kb with view_mode='categories')
2. Drilldown into specific hubs (get_setup_kb with view_mode='hub:zakovat', 'hub:geography', etc.)
3. Host-only hub navigation and back to main categories (cb_game_setup)
4. Sub-mode selection and checkmark toggling inside hubs (setup:mode:<sub_mode>:<session_id>)
5. Dynamic title formatting in hub view with descriptions and questions count (format_setup_title)
6. GameSession execution and question generation with sub-modes and hub modes
"""

import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from keyboards.game_kb import get_setup_kb, CATEGORY_HUBS_INFO
from handlers.callbacks import cb_game_setup, format_setup_title
from games.session import GameSession
from games.manager import game_manager
from games.models import GameMode
from locales.i18n import t


class TestGroupCategoryNavigation(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.chat_id = -100123456789
        self.host_id = 11112222
        self.other_user_id = 99998888
        self.session_id = "testnav1"
        self.session = GameSession(
            chat_id=self.chat_id,
            created_by_user_id=self.host_id,
            host_id=self.host_id,
            host_name="HostAlice",
            is_group=True,
            lang="en",
            mode="mix",
            total_rounds=5,
            round_time=30,
            view_mode="categories"
        )
        self.session.session_id = self.session_id
        game_manager.set_session(self.chat_id, self.session)
        self.bot = MagicMock()

    async def asyncTearDown(self):
        game_manager.remove_session(self.chat_id)

    def test_group_setup_renders_category_hubs_by_default(self):
        """Verify get_setup_kb(view_mode='categories') contains all 6 hub buttons, Blur, Super Mix, Continent, Timers, Input, Rounds, Start, Cancel."""
        for v_mode in ("categories", None):
            if v_mode is None:
                kb = get_setup_kb(session_id=self.session_id, lang="en")
            else:
                kb = get_setup_kb(session_id=self.session_id, view_mode=v_mode, lang="en")

            all_buttons = [btn for row in kb.inline_keyboard for btn in row]
            callbacks = [btn.callback_data for btn in all_buttons]

            # 1. Verify all 6 hub buttons are present
            expected_hubs = [
                "zakovat",
                "geography",
                "cosmos_nature",
                "science_logic",
                "history_culture",
                "people_brands"
            ]
            for h in expected_hubs:
                expected_cb = f"setup:hub:{h}:{self.session_id}"
                self.assertIn(
                    expected_cb,
                    callbacks,
                    f"Hub button {expected_cb} missing in view_mode='{v_mode}'!"
                )

            # 2. Verify Blur toggle button
            self.assertIn(f"setup:blur:{self.session_id}", callbacks)

            # 3. Verify Super Mix button
            self.assertIn(f"setup:mode:mix:{self.session_id}", callbacks)

            # 4. Verify Continent Filter button
            self.assertIn(f"setup:continent:{self.session_id}", callbacks)

            # 5. Verify Explicit Timers (30s and 60s)
            self.assertIn(f"setup:time:30:{self.session_id}", callbacks)
            self.assertIn(f"setup:time:60:{self.session_id}", callbacks)

            # 6. Verify Input modes (Buttons, Text, Both)
            self.assertIn(f"setup:input:buttons:{self.session_id}", callbacks)
            self.assertIn(f"setup:input:text:{self.session_id}", callbacks)
            self.assertIn(f"setup:input:both:{self.session_id}", callbacks)

            # 7. Verify Rounds selector
            self.assertIn(f"setup:rounds:{self.session_id}", callbacks)

            # 8. Verify Start button
            self.assertIn(f"setup:start:{self.session_id}", callbacks)

            # 9. Verify Cancel button
            self.assertIn(f"setup:cancel:{self.session_id}", callbacks)

    def test_group_setup_drilldown_into_hub(self):
        """Verify get_setup_kb(view_mode='hub:zakovat') contains buttons for black_box, deduction, world_intellect, blitz, zakovat, and setup:hub:main back button."""
        kb = get_setup_kb(
            session_id=self.session_id,
            view_mode="hub:zakovat",
            selected_modes=[],
            lang="en"
        )
        all_buttons = [btn for row in kb.inline_keyboard for btn in row]
        callbacks = [btn.callback_data for btn in all_buttons]

        expected_submodes = ["black_box", "deduction", "world_intellect", "blitz", "zakovat"]
        for sub in expected_submodes:
            expected_cb = f"setup:mode:{sub}:{self.session_id}"
            self.assertIn(
                expected_cb,
                callbacks,
                f"Submode {sub} callback {expected_cb} missing in hub:zakovat view!"
            )

        # Back button to return to main categories
        expected_back_cb = f"setup:hub:main:{self.session_id}"
        self.assertIn(
            expected_back_cb,
            callbacks,
            f"Back button {expected_back_cb} missing in hub:zakovat view!"
        )

        # Common bottom controls also available
        self.assertIn(f"setup:start:{self.session_id}", callbacks)
        self.assertIn(f"setup:cancel:{self.session_id}", callbacks)

    def test_group_setup_drilldown_geography(self):
        """Verify get_setup_kb(view_mode='hub:geography') contains flag, capital, landmark, higher_lower, coat_of_arms, streetview, emoji, contour, geo_mix, and setup:hub:main back button."""
        kb = get_setup_kb(
            session_id=self.session_id,
            view_mode="hub:geography",
            selected_modes=[],
            lang="en"
        )
        all_buttons = [btn for row in kb.inline_keyboard for btn in row]
        callbacks = [btn.callback_data for btn in all_buttons]

        expected_modes = [
            "flag", "capital", "landmark", "higher_lower", "coat_of_arms",
            "streetview", "emoji", "contour", "geo_mix"
        ]
        for m in expected_modes:
            expected_cb = f"setup:mode:{m}:{self.session_id}"
            self.assertIn(
                expected_cb,
                callbacks,
                f"Geography submode {m} callback {expected_cb} missing in hub:geography view!"
            )

        expected_back_cb = f"setup:hub:main:{self.session_id}"
        self.assertIn(
            expected_back_cb,
            callbacks,
            f"Back button {expected_back_cb} missing in hub:geography view!"
        )

    async def test_cb_game_setup_hub_navigation(self):
        """Simulate host clicking setup:hub:zakovat:<session_id> -> verify session.view_mode becomes 'hub:zakovat'. Then clicking setup:hub:main:<session_id> -> verify session.view_mode returns to 'categories'."""
        self.assertEqual(self.session.view_mode, "categories")

        # Step 1: Host drills down into Zakovat Hub
        query = MagicMock()
        query.message.chat.id = self.chat_id
        query.message.edit_text = AsyncMock()
        query.message.edit_reply_markup = AsyncMock()
        query.from_user.id = self.host_id
        query.from_user.first_name = "HostAlice"
        query.data = f"setup:hub:zakovat:{self.session_id}"
        query.answer = AsyncMock()

        await cb_game_setup(query, self.bot)

        # Verify session view_mode is now 'hub:zakovat'
        self.assertEqual(self.session.view_mode, "hub:zakovat")
        query.message.edit_text.assert_called_once()
        call_kwargs = query.message.edit_text.call_args.kwargs
        kb = call_kwargs.get("reply_markup")
        all_callbacks = [btn.callback_data for row in kb.inline_keyboard for btn in row]
        self.assertIn(f"setup:mode:black_box:{self.session_id}", all_callbacks)
        self.assertIn(f"setup:hub:main:{self.session_id}", all_callbacks)

        # Step 2: Host clicks Back to All Categories button
        query_back = MagicMock()
        query_back.message.chat.id = self.chat_id
        query_back.message.edit_text = AsyncMock()
        query_back.message.edit_reply_markup = AsyncMock()
        query_back.from_user.id = self.host_id
        query_back.from_user.first_name = "HostAlice"
        query_back.data = f"setup:hub:main:{self.session_id}"
        query_back.answer = AsyncMock()

        await cb_game_setup(query_back, self.bot)

        # Verify session view_mode returned to 'categories'
        self.assertEqual(self.session.view_mode, "categories")
        query_back.message.edit_text.assert_called_once()
        call_kwargs_back = query_back.message.edit_text.call_args.kwargs
        kb_back = call_kwargs_back.get("reply_markup")
        all_callbacks_back = [btn.callback_data for row in kb_back.inline_keyboard for btn in row]
        self.assertIn(f"setup:hub:zakovat:{self.session_id}", all_callbacks_back)
        self.assertIn(f"setup:hub:geography:{self.session_id}", all_callbacks_back)

    async def test_cb_game_setup_submode_toggling(self):
        """Simulate host clicking setup:mode:black_box:<session_id> while in zakovat hub -> verify black_box is added to session.selected_modes and checkmark appears."""
        self.session.view_mode = "hub:zakovat"
        self.session.selected_modes = []

        query = MagicMock()
        query.message.chat.id = self.chat_id
        query.message.edit_text = AsyncMock()
        query.message.edit_reply_markup = AsyncMock()
        query.from_user.id = self.host_id
        query.from_user.first_name = "HostAlice"
        query.data = f"setup:mode:black_box:{self.session_id}"
        query.answer = AsyncMock()

        await cb_game_setup(query, self.bot)

        # Verify black_box is in selected_modes
        self.assertIn("black_box", self.session.selected_modes)

        # Verify checkmark appears on the button
        call_kwargs = query.message.edit_text.call_args.kwargs
        kb = call_kwargs.get("reply_markup")
        all_buttons = [btn for row in kb.inline_keyboard for btn in row]
        black_box_btn = [btn for btn in all_buttons if btn.callback_data == f"setup:mode:black_box:{self.session_id}"][0]
        self.assertIn("✅", black_box_btn.text)

        # Toggle OFF: Host clicks black_box again
        query_toggle = MagicMock()
        query_toggle.message.chat.id = self.chat_id
        query_toggle.message.edit_text = AsyncMock()
        query_toggle.message.edit_reply_markup = AsyncMock()
        query_toggle.from_user.id = self.host_id
        query_toggle.from_user.first_name = "HostAlice"
        query_toggle.data = f"setup:mode:black_box:{self.session_id}"
        query_toggle.answer = AsyncMock()

        await cb_game_setup(query_toggle, self.bot)

        # Verify black_box is deselected and checkmark is removed
        self.assertNotIn("black_box", self.session.selected_modes)
        call_kwargs_off = query_toggle.message.edit_text.call_args.kwargs
        kb_off = call_kwargs_off.get("reply_markup")
        all_buttons_off = [btn for row in kb_off.inline_keyboard for btn in row]
        btn_off = [btn for btn in all_buttons_off if btn.callback_data == f"setup:mode:black_box:{self.session_id}"][0]
        self.assertNotIn("✅", btn_off.text)

    def test_format_setup_title_in_hub_view(self):
        """Verify format_setup_title displays the specific hub description and questions count when view_mode is 'hub:zakovat'."""
        self.session.view_mode = "hub:zakovat"
        self.session.selected_modes = ["black_box"]

        # 1. English
        title_en = format_setup_title(self.session, "en")
        self.assertIn("Zakovat Intellectual Club", title_en)
        self.assertIn("500 Questions", title_en)
        self.assertIn("Black Box", title_en)
        self.assertIn("Logic & Deduction", title_en)
        self.assertIn("125", title_en)

        # 2. Uzbek
        title_uz = format_setup_title(self.session, "uz")
        self.assertIn("Zakovat Intellektual Klubi", title_uz)
        self.assertIn("500 ta savol", title_uz)
        self.assertIn("Qora quti", title_uz)
        self.assertIn("Mantiq & Deduksiya", title_uz)

        # 3. Russian
        title_ru = format_setup_title(self.session, "ru")
        self.assertIn("Интеллектуальный Клуб Заковат", title_ru)
        self.assertIn("500 вопросов", title_ru)
        self.assertIn("Чёрный ящик", title_ru)
        self.assertIn("Дедукция и Логика", title_ru)

        # 4. Geography Hub
        self.session.view_mode = "hub:geography"
        title_geo = format_setup_title(self.session, "en")
        self.assertIn("Geography & GeoGuessr", title_geo)
        self.assertIn("1,000+", title_geo)
        self.assertIn("Street View", title_geo)

    async def test_non_host_cannot_navigate_hubs(self):
        """Verify non-host user is rejected with alert when trying to drill down into hub."""
        query = MagicMock()
        query.message.chat.id = self.chat_id
        query.from_user.id = self.other_user_id
        query.from_user.first_name = "IntruderBob"
        query.data = f"setup:hub:zakovat:{self.session_id}"
        query.answer = AsyncMock()

        await cb_game_setup(query, self.bot)

        query.answer.assert_called_once()
        args, kwargs = query.answer.call_args
        self.assertTrue(kwargs.get("show_alert"))
        alert_msg = args[0] if args else kwargs.get("text", "")
        self.assertIn("host", alert_msg.lower())
        self.assertEqual(self.session.view_mode, "categories")

    def test_all_six_hubs_drilldown_contain_submodes_and_back_button(self):
        """Verify get_setup_kb correctly generates drilldown keyboards for all 6 hubs."""
        for hub_key, hub_data in CATEGORY_HUBS_INFO.items():
            kb = get_setup_kb(session_id=self.session_id, view_mode=f"hub:{hub_key}", lang="en")
            all_buttons = [btn for row in kb.inline_keyboard for btn in row]
            callbacks = [btn.callback_data for btn in all_buttons]

            # All buttons from hub_data must be present
            for code, _ in hub_data["buttons"]:
                self.assertIn(
                    f"setup:mode:{code}:{self.session_id}",
                    callbacks,
                    f"Button {code} missing in hub {hub_key}!"
                )

            # Back button must be present
            self.assertIn(
                f"setup:hub:main:{self.session_id}",
                callbacks,
                f"Back button missing in hub {hub_key}!"
            )

    def test_game_session_generates_questions_for_submodes_and_hub_mixes(self):
        """Verify GameSession next_round works seamlessly with sub-modes and hub mixes."""
        # 1. Zakovat black_box sub-mode
        session_bbox = GameSession(
            chat_id=self.chat_id,
            host_id=self.host_id,
            mode="black_box",
            selected_modes=["black_box"],
            total_rounds=3
        )
        q1 = session_bbox.start_game()
        self.assertIsNotNone(q1)
        self.assertTrue(q1.is_black_box or "black box" in q1.text.lower() or "qora quti" in q1.text.lower())

        # 2. Geography geo_mix
        session_geomix = GameSession(
            chat_id=self.chat_id,
            host_id=self.host_id,
            mode="geo_mix",
            selected_modes=["geo_mix"],
            total_rounds=3
        )
        q2 = session_geomix.start_game()
        self.assertIsNotNone(q2)
        self.assertIn(q2.mode, [
            GameMode.FLAG, GameMode.CAPITAL, GameMode.LANDMARK, GameMode.HIGHER_LOWER,
            GameMode.COAT_OF_ARMS, GameMode.STREETVIEW, GameMode.EMOJI, GameMode.CONTOUR
        ])


if __name__ == "__main__":
    unittest.main()
