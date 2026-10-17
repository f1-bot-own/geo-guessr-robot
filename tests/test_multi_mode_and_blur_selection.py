"""
Tests for Multi-Mode Selection and Blur Reveal Control:
- Toggling categories with checkboxes
- Selecting multiple modes simultaneously
- Presets: All modes / Flags only
- Dedicated Blur ON / OFF toggle
- Verifying that when specific categories are blurred, questions only come from those categories
- Verifying solo setup lobby multi-mode support
"""

import unittest
from unittest.mock import MagicMock, AsyncMock
from games.models import GameMode, Question
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.manager import game_manager
from keyboards.game_kb import get_setup_kb, get_solo_setup_kb
from handlers.callbacks import cb_game_setup, cb_solo_setup, format_setup_title


class TestMultiModeAndBlurSelection(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.chat_id = 99887766
        self.host_id = 112233
        self.session = GameSession(
            chat_id=self.chat_id,
            created_by_user_id=self.host_id,
            is_group=True,
            mode=GameMode.MIX,
            total_rounds=5,
            round_time=30,
            lang="uz"
        )
        game_manager.set_session(self.chat_id, self.session)
        self.bot = MagicMock()

    def tearDown(self):
        game_manager.remove_session(self.chat_id)

    def test_setup_keyboard_contains_checkboxes_and_blur_toggle(self):
        """get_setup_kb must render checkboxes for modes and dedicated blur toggle button."""
        kb = get_setup_kb(
            session_id=self.session.session_id,
            mode="flag",
            selected_modes=["flag", "president"],
            is_blur=True,
            lang="uz",
            view_mode="detailed"
        )
        buttons = [btn for row in kb.inline_keyboard for btn in row]
        callback_datas = [b.callback_data for b in buttons]
        texts = {b.callback_data: b.text for b in buttons}

        # Check that flag and president have checkmarks
        flag_cb = f"setup:mode:flag:{self.session.session_id}"
        pres_cb = f"setup:mode:president:{self.session.session_id}"
        logo_cb = f"setup:mode:logo:{self.session.session_id}"
        blur_cb = f"setup:blur:{self.session.session_id}"

        self.assertIn(flag_cb, callback_datas)
        self.assertIn(pres_cb, callback_datas)
        self.assertIn(logo_cb, callback_datas)
        self.assertIn(blur_cb, callback_datas)

        self.assertIn("✅", texts[flag_cb])
        self.assertIn("✅", texts[pres_cb])
        self.assertNotIn("✅", texts[logo_cb])
        self.assertIn("✅", texts[blur_cb])

    async def test_multi_mode_toggle_in_callbacks(self):
        """Host can toggle modes on and off like checkboxes."""
        # 1. Switch from mix to flag
        q1 = MagicMock()
        q1.message.chat.id = self.chat_id
        q1.from_user.id = self.host_id
        q1.data = f"setup:mode:flag:{self.session.session_id}"
        q1.answer = AsyncMock()
        q1.message.edit_text = AsyncMock()
        await cb_game_setup(q1, self.bot)

        self.assertEqual(self.session.selected_modes, ["flag"])
        self.assertEqual(self.session.mode, "flag")

        # 2. Add president to selected modes
        q2 = MagicMock()
        q2.message.chat.id = self.chat_id
        q2.from_user.id = self.host_id
        q2.data = f"setup:mode:president:{self.session.session_id}"
        q2.answer = AsyncMock()
        q2.message.edit_text = AsyncMock()
        await cb_game_setup(q2, self.bot)

        self.assertIn("flag", self.session.selected_modes)
        self.assertIn("president", self.session.selected_modes)
        self.assertEqual(len(self.session.selected_modes), 2)

        # 3. Add logo
        q3 = MagicMock()
        q3.message.chat.id = self.chat_id
        q3.from_user.id = self.host_id
        q3.data = f"setup:mode:logo:{self.session.session_id}"
        q3.answer = AsyncMock()
        q3.message.edit_text = AsyncMock()
        await cb_game_setup(q3, self.bot)

        self.assertIn("logo", self.session.selected_modes)
        self.assertEqual(len(self.session.selected_modes), 3)

        # 4. Remove flag
        q4 = MagicMock()
        q4.message.chat.id = self.chat_id
        q4.from_user.id = self.host_id
        q4.data = f"setup:mode:flag:{self.session.session_id}"
        q4.answer = AsyncMock()
        q4.message.edit_text = AsyncMock()
        await cb_game_setup(q4, self.bot)

        self.assertNotIn("flag", self.session.selected_modes)
        self.assertIn("president", self.session.selected_modes)
        self.assertIn("logo", self.session.selected_modes)

    async def test_blur_toggle_in_callbacks(self):
        """Host can toggle blur effect on/off."""
        self.assertFalse(self.session.is_blur)

        q_blur = MagicMock()
        q_blur.message.chat.id = self.chat_id
        q_blur.from_user.id = self.host_id
        q_blur.data = f"setup:blur:{self.session.session_id}"
        q_blur.answer = AsyncMock()
        q_blur.message.edit_text = AsyncMock()

        await cb_game_setup(q_blur, self.bot)
        self.assertTrue(self.session.is_blur)

        await cb_game_setup(q_blur, self.bot)
        self.assertFalse(self.session.is_blur)

    def test_next_round_generates_only_selected_modes_with_blur(self):
        """When host selects only flags and turns on blur, all questions are blurred flags."""
        self.session.selected_modes = ["flag"]
        self.session.is_blur = True

        for _ in range(5):
            q = self.session.next_round()
            self.assertEqual(q.mode, GameMode.BLUR)
            self.assertTrue(q.image_url)
            self.assertIn("bayroq", q.text.lower())

    def test_solo_multi_mode_and_blur(self):
        """SoloGameSession supports selected_modes and blur effect."""
        solo = SoloGameSession(
            user_id=123,
            user_name="Player",
            selected_modes=["president"],
            is_blur=True,
            lang="uz"
        )
        self.assertEqual(solo.selected_modes, ["president"])
        self.assertTrue(solo.is_blur)

        q = solo.next_round()
        self.assertEqual(q.mode, GameMode.BLUR)
        self.assertIn("inson", q.text.lower())

    def test_initially_no_buttons_selected_and_zero_modes_displayed(self):
        """When selected_modes is empty, NO buttons have checkmark and title shows (0)."""
        kb = get_setup_kb(
            session_id=self.session.session_id,
            mode="mix",
            selected_modes=[],
            is_blur=False,
            lang="uz"
        )
        buttons = [btn for row in kb.inline_keyboard for btn in row]
        mode_buttons = [b for b in buttons if b.callback_data.startswith("setup:mode:")]
        for btn in mode_buttons:
            self.assertNotIn("✅", btn.text, f"Button {btn.text} should NOT have a checkmark!")

        self.session.selected_modes = []
        title = format_setup_title(self.session, "uz")
        self.assertIn("(0)", title)
        self.assertIn("Hech biri tanlanmagan", title)

    async def test_cannot_start_without_selecting_at_least_one_mode(self):
        """Pressing Start when selected_modes is empty displays alert and blocks game launch."""
        self.session.selected_modes = []
        q_start = MagicMock()
        q_start.message.chat.id = self.chat_id
        q_start.from_user.id = self.host_id
        q_start.data = f"setup:start:{self.session.session_id}"
        q_start.answer = AsyncMock()

        await cb_game_setup(q_start, self.bot)

        # Must show alert requesting to select at least one mode
        q_start.answer.assert_called_once()
        alert_text = q_start.answer.call_args[0][0]
        self.assertIn("kamida bitta", alert_text)
        self.assertEqual(self.session.status, "setup")

    async def test_solo_cannot_start_without_selecting_at_least_one_mode(self):
        """Solo mode also blocks starting if no modes are selected."""
        user_id = 554433
        game_manager.set_solo_setup_state(user_id, {"selected_modes": []})

        q_start = MagicMock()
        q_start.from_user.id = user_id
        q_start.data = "solo_setup:start"
        q_start.answer = AsyncMock()

        mock_db = MagicMock()
        mock_db.get_user = AsyncMock(return_value={"language": "en"})
        with unittest.mock.patch("handlers.callbacks.get_db", return_value=mock_db):
            await cb_solo_setup(q_start, self.bot)

        q_start.answer.assert_called_once()
        alert_text = q_start.answer.call_args[0][0]
        self.assertIn("at least one mode", alert_text)
        self.assertIsNone(game_manager.get_solo_session(user_id))


if __name__ == "__main__":
    unittest.main()

