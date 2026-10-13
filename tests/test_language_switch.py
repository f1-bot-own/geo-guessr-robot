"""
Unit tests for language switching persistence and live session synchronization.
"""

import unittest
import tempfile
import os
from unittest.mock import MagicMock, AsyncMock

from database.db import Database
from games.session import GameSession
from games.manager import game_manager
from games.flow import proceed_after_round

class TestLanguageSwitchPersistence(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_lang.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.tmp_dir.cleanup()

    async def test_set_chat_language_unregistered_chat(self):
        """Verify set_chat_language inserts and persists language for a chat that was never in chats table."""
        chat_id = -100998877
        # Initially, chat does not exist -> fallback to 'en'
        lang_init = await self.db.get_chat_language(chat_id)
        self.assertEqual(lang_init, "en")

        # Now set language to 'uz'
        await self.db.set_chat_language(chat_id, "uz")

        # Should now return 'uz'
        lang_after = await self.db.get_chat_language(chat_id)
        self.assertEqual(lang_after, "uz")

        # Update again to 'ru'
        await self.db.set_chat_language(chat_id, "ru")
        lang_ru = await self.db.get_chat_language(chat_id)
        self.assertEqual(lang_ru, "ru")

    async def test_set_user_language_unregistered_user(self):
        """Verify set_user_language inserts and persists language for an unregistered user."""
        user_id = 887766
        await self.db.set_user_language(user_id, "uz")
        lang = await self.db.get_user_language(user_id)
        self.assertEqual(lang, "uz")

    async def test_live_session_language_update(self):
        """Verify that when a session is running and language is changed in DB, proceed_after_round syncs it."""
        chat_id = -100112233
        bot = MagicMock()
        bot.send_message = AsyncMock()

        # Session created originally in English
        session = GameSession(
            chat_id=chat_id,
            created_by_user_id=1,
            lang="en",
            mode="flag",
            total_rounds=5
        )
        session.current_round = 1
        session.status = "in_progress"
        game_manager.set_session(chat_id, session)

        # Chat language updated to Uzbek in database
        await self.db.set_chat_language(chat_id, "uz")

        # When proceed_after_round executes, it must re-sync session.lang to 'uz'
        # and next round question text must be in Uzbek
        with unittest.mock.patch("asyncio.sleep", new_callable=AsyncMock):
            with unittest.mock.patch("games.flow.send_round_question", new_callable=AsyncMock) as mock_send:
                await proceed_after_round(bot, chat_id, session, self.db)
                self.assertEqual(session.lang, "uz")
                self.assertEqual(session.current_round, 2)
                self.assertIn("bayrog'i", session.current_question.text)

        game_manager.remove_session(chat_id)

if __name__ == "__main__":
    unittest.main()
