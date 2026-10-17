"""
Tests for Group Match Category Hub Navigation and Sub-mode Hierarchical Selection:
- Switching between main category hubs view ('categories') and specific hub view ('hub:<name>')
- Verifying buttons and checkmarks for 6 main hubs in get_setup_kb
- Verifying sub-mode rendering inside hubs (e.g. Zakovat: black_box, deduction, world_intellect, blitz, zakovat)
- Verifying [🔙 📁 Barcha toifalar] back navigation
- Verifying format_setup_title dynamic header updates in hub view
- Verifying toggling sub-modes with checkboxes and starting game with sub-modes
"""

import unittest
from unittest.mock import MagicMock, AsyncMock
from games.models import GameMode
from games.session import GameSession
from games.manager import game_manager
from keyboards.game_kb import get_setup_kb, CATEGORY_HUBS_INFO
from handlers.callbacks import cb_game_setup, format_setup_title
from games.question_factory import QuestionFactory


class TestGroupCategoryHubs(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.chat_id = -100123456789
        self.host_id = 998877
        self.session = GameSession(
            chat_id=self.chat_id,
            created_by_user_id=self.host_id,
            host_id=self.host_id,
            host_name="SuperHost",
            is_group=True,
            mode=GameMode.MIX,
            total_rounds=5,
            round_time=30,
            lang="uz"
        )
        self.session.view_mode = "categories"
        game_manager.set_session(self.chat_id, self.session)
        self.bot = MagicMock()

    def tearDown(self):
        game_manager.remove_session(self.chat_id)

    def test_main_category_hubs_keyboard(self):
        """Main view_mode='categories' must render 6 Category Hub buttons with setup:hub:<name> callbacks."""
        kb = get_setup_kb(
            session_id=self.session.session_id,
            mode="mix",
            selected_modes=["mix"],
            lang="uz",
            view_mode="categories"
        )
        buttons = [btn for row in kb.inline_keyboard for btn in row]
        callback_datas = [b.callback_data for b in buttons]

        expected_hubs = [
            "zakovat", "geography", "cosmos_nature",
            "science_logic", "history_culture", "people_brands"
        ]
        for hub in expected_hubs:
            expected_cb = f"setup:hub:{hub}:{self.session.session_id}"
            self.assertIn(expected_cb, callback_datas, f"Hub callback {expected_cb} missing from main menu!")

        # Verify Super Mix callback
        self.assertIn(f"setup:mode:mix:{self.session.session_id}", callback_datas)
        # Verify timers, continent, rounds, launch
        self.assertIn(f"setup:time:30:{self.session.session_id}", callback_datas)
        self.assertIn(f"setup:time:60:{self.session.session_id}", callback_datas)
        self.assertIn(f"setup:continent:{self.session.session_id}", callback_datas)
        self.assertIn(f"setup:rounds:{self.session.session_id}", callback_datas)
        self.assertIn(f"setup:start:{self.session.session_id}", callback_datas)
        self.assertIn(f"setup:cancel:{self.session.session_id}", callback_datas)

    def test_hub_submodes_keyboard_and_checkmarks(self):
        """view_mode='hub:zakovat' renders all Zakovat sub-modes and back button."""
        # When only black_box is selected
        kb = get_setup_kb(
            session_id=self.session.session_id,
            mode="black_box",
            selected_modes=["black_box"],
            lang="uz",
            view_mode="hub:zakovat"
        )
        buttons = [btn for row in kb.inline_keyboard for btn in row]
        texts = {b.callback_data: b.text for b in buttons}

        bbox_cb = f"setup:mode:black_box:{self.session.session_id}"
        deduct_cb = f"setup:mode:deduction:{self.session.session_id}"
        intellect_cb = f"setup:mode:world_intellect:{self.session.session_id}"
        blitz_cb = f"setup:mode:blitz:{self.session.session_id}"
        zako_cb = f"setup:mode:zakovat:{self.session.session_id}"
        back_cb = f"setup:hub:main:{self.session.session_id}"

        self.assertIn(bbox_cb, texts)
        self.assertIn(deduct_cb, texts)
        self.assertIn(intellect_cb, texts)
        self.assertIn(blitz_cb, texts)
        self.assertIn(zako_cb, texts)
        self.assertIn(back_cb, texts)

        # black_box should have checkmark, others should not
        self.assertIn("✅", texts[bbox_cb])
        self.assertNotIn("✅", texts[deduct_cb])
        self.assertNotIn("✅", texts[intellect_cb])
        self.assertNotIn("✅", texts[blitz_cb])
        self.assertNotIn("✅", texts[zako_cb])

    async def test_navigate_into_hub_and_toggle_submodes(self):
        """Host navigates into a hub, toggles sub-modes, and navigates back to main."""
        # 1. Click on Zakovat Hub in main categories setup
        q_hub = MagicMock()
        q_hub.message.chat.id = self.chat_id
        q_hub.from_user.id = self.host_id
        q_hub.data = f"setup:hub:zakovat:{self.session.session_id}"
        q_hub.answer = AsyncMock()
        q_hub.message.edit_text = AsyncMock()

        await cb_game_setup(q_hub, self.bot)

        # Session view_mode must now be 'hub:zakovat'
        self.assertEqual(self.session.view_mode, "hub:zakovat")
        q_hub.message.edit_text.assert_called_once()
        title_text = q_hub.message.edit_text.call_args[1]["text"]
        self.assertIn("Zakovat Intellektual Klubi", title_text)
        self.assertIn("Qora quti", title_text)

        # 2. Toggle 'black_box' sub-mode
        q_bbox = MagicMock()
        q_bbox.message.chat.id = self.chat_id
        q_bbox.from_user.id = self.host_id
        q_bbox.data = f"setup:mode:black_box:{self.session.session_id}"
        q_bbox.answer = AsyncMock()
        q_bbox.message.edit_text = AsyncMock()

        await cb_game_setup(q_bbox, self.bot)

        self.assertEqual(self.session.selected_modes, ["black_box"])
        self.assertEqual(self.session.mode, "black_box")

        # 3. Toggle 'deduction' sub-mode
        q_ded = MagicMock()
        q_ded.message.chat.id = self.chat_id
        q_ded.from_user.id = self.host_id
        q_ded.data = f"setup:mode:deduction:{self.session.session_id}"
        q_ded.answer = AsyncMock()
        q_ded.message.edit_text = AsyncMock()

        await cb_game_setup(q_ded, self.bot)

        self.assertIn("black_box", self.session.selected_modes)
        self.assertIn("deduction", self.session.selected_modes)
        self.assertEqual(len(self.session.selected_modes), 2)
        self.assertEqual(self.session.mode, "mix")

        # 4. Navigate back to main categories view
        q_back = MagicMock()
        q_back.message.chat.id = self.chat_id
        q_back.from_user.id = self.host_id
        q_back.data = f"setup:hub:main:{self.session.session_id}"
        q_back.answer = AsyncMock()
        q_back.message.edit_text = AsyncMock()

        await cb_game_setup(q_back, self.bot)

        self.assertEqual(self.session.view_mode, "categories")
        kb_main = q_back.message.edit_text.call_args[1]["reply_markup"]
        zako_btn = [btn for row in kb_main.inline_keyboard for btn in row if f"setup:hub:zakovat:{self.session.session_id}" in btn.callback_data][0]
        self.assertIn("✅", zako_btn.text, "Zakovat hub must display checkmark when its sub-modes are selected!")

    def test_format_setup_title_in_hub_view(self):
        """format_setup_title shows category overview text and active sub-modes."""
        self.session.view_mode = "hub:science_logic"
        self.session.selected_modes = ["elements", "flash_math"]

        title = format_setup_title(self.session, "uz")
        # Header from CATEGORY_HUBS_INFO
        self.assertIn("Fan & Mantiq", title)
        self.assertIn("Davriy jadval elementlari", title)
        # Active submodes
        self.assertIn("Davriy jadval", title)
        self.assertIn("Tezkor hisob-kitob", title)
        self.assertIn("SuperHost", title)
        self.assertIn("30s", title)
        self.assertIn("5", title)

    def test_next_round_generates_from_selected_submodes(self):
        """GameSession next_round picks from selected sub-modes and creates questions without error."""
        self.session.selected_modes = ["black_box", "deduction"]
        q1 = self.session.next_round()
        self.assertIsNotNone(q1)
        self.assertIn(q1.sub_mode, ["black_box", "deduction"])

        # Test science sub-modes
        self.session.selected_modes = ["elements"]
        q2 = self.session.next_round()
        self.assertIsNotNone(q2)
        self.assertEqual(q2.sub_mode, "elements")


if __name__ == "__main__":
    unittest.main()
