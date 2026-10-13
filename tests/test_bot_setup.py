"""
Unit and Integration Tests for Bot initialization, database binding, and get_db resolvers.
Verifies fix for: TypeError: 'Bot' object does not support item assignment
"""

import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from aiogram import Bot, Dispatcher
from database.db import Database, get_default_db
import handlers
from handlers.bot_compat import get_db as get_db_compat
from handlers.commands import get_db as get_db_commands
from handlers.callbacks import get_db as get_db_callbacks
from handlers.text_answers import get_db as get_db_text_answers
from handlers.chat_member import get_db as get_db_chat_member
import config


class TestBotItemAccessAndDatabaseBinding(unittest.TestCase):
    def setUp(self):
        self.bot = Bot(token="1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi")
        self.dummy_db = Database(":memory:")

    def test_bot_item_assignment(self):
        """bot['db'] = db must not raise TypeError: 'Bot' object does not support item assignment."""
        try:
            self.bot["db"] = self.dummy_db
        except TypeError as e:
            self.fail(f"Item assignment raised TypeError: {e}")
        self.assertIs(self.bot["db"], self.dummy_db)
        self.assertIs(self.bot.db, self.dummy_db)

    def test_bot_item_retrieval_and_contains(self):
        """bot supports __getitem__, __contains__, and get()."""
        self.bot["custom_key"] = "test_value"
        self.assertEqual(self.bot["custom_key"], "test_value")
        self.assertTrue("custom_key" in self.bot)
        self.assertFalse("nonexistent_key" in self.bot)
        self.assertEqual(self.bot.get("custom_key"), "test_value")
        self.assertEqual(self.bot.get("nonexistent_key", "default"), "default")

    def test_bot_missing_key_raises_key_error(self):
        """Accessing missing key raises KeyError, matching standard dict semantics."""
        with self.assertRaises(KeyError):
            _ = self.bot["completely_absent_key_xyz"]

    def test_bot_non_string_keys(self):
        """bot supports integer and tuple keys without crashing setattr."""
        self.bot[42] = "answer"
        self.assertEqual(self.bot[42], "answer")
        self.assertTrue(42 in self.bot)

        self.bot[("compound", "key")] = 999
        self.assertEqual(self.bot[("compound", "key")], 999)
        self.assertTrue(("compound", "key") in self.bot)

    def test_bot_delitem(self):
        """del bot['key'] deletes the item and raises KeyError if accessed again."""
        self.bot["removable"] = "data"
        self.assertEqual(self.bot["removable"], "data")
        del self.bot["removable"]
        self.assertFalse("removable" in self.bot)
        with self.assertRaises(KeyError):
            _ = self.bot["removable"]

    def test_bot_dict_protocol_methods(self):
        """bot supports keys(), values(), items(), len(), and iter()."""
        self.bot["k1"] = "v1"
        self.bot["k2"] = "v2"
        self.assertIn("k1", self.bot.keys())
        self.assertIn("k2", self.bot.keys())
        self.assertIn("v1", self.bot.values())
        self.assertIn("v2", self.bot.values())
        self.assertIn(("k1", "v1"), self.bot.items())
        self.assertGreaterEqual(len(self.bot), 2)
        iterated_keys = list(iter(self.bot))
        self.assertIn("k1", iterated_keys)
        self.assertIn("k2", iterated_keys)

    def test_bot_does_not_expose_framework_methods_in_contains(self):
        """Internal Bot methods/attributes like send_message and token are not reported as dict items."""
        self.assertFalse("send_message" in self.bot)
        self.assertFalse("token" in self.bot)
        self.assertFalse("session" in self.bot)
        self.assertFalse("get_me" in self.bot)

    def test_bot_internal_methods_not_corrupted_by_item_assignment(self):
        """Assigning bot['session'] or bot['send_message'] does not overwrite Bot attributes."""
        original_session = self.bot.session
        original_send_message = self.bot.send_message

        self.bot["session"] = "custom_session_token"
        self.assertEqual(self.bot["session"], "custom_session_token")
        # Framework attribute is preserved
        self.assertIs(self.bot.session, original_session)

        self.bot["send_message"] = "mock_send"
        self.assertEqual(self.bot["send_message"], "mock_send")
        self.assertIs(self.bot.send_message.__func__, Bot.send_message)

    def test_get_db_resolvers_via_attribute(self):
        """All get_db resolvers find db via bot.db attribute."""
        bot = Bot(token="1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi")
        bot.db = self.dummy_db

        self.assertIs(get_db_compat(bot), self.dummy_db)
        self.assertIs(get_db_commands(bot), self.dummy_db)
        self.assertIs(get_db_callbacks(bot), self.dummy_db)
        self.assertIs(get_db_text_answers(bot), self.dummy_db)
        self.assertIs(get_db_chat_member(bot), self.dummy_db)

    def test_get_db_resolvers_via_item(self):
        """All get_db resolvers find db via bot['db'] item access."""
        bot = Bot(token="1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi")
        bot["db"] = self.dummy_db

        self.assertIs(get_db_compat(bot), self.dummy_db)
        self.assertIs(get_db_commands(bot), self.dummy_db)
        self.assertIs(get_db_callbacks(bot), self.dummy_db)
        self.assertIs(get_db_text_answers(bot), self.dummy_db)
        self.assertIs(get_db_chat_member(bot), self.dummy_db)

    def test_get_db_resolvers_fallback_to_default_db(self):
        """All get_db resolvers gracefully fall back to get_default_db() when no db is attached."""
        bot = Bot(token="1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi")
        if hasattr(bot, "db"):
            delattr(bot, "db")
        if hasattr(bot, "_bot_data") and "db" in bot._bot_data:
            del bot._bot_data["db"]

        default_db = get_default_db()
        self.assertIs(get_db_compat(bot), default_db)
        self.assertIs(get_db_commands(bot), default_db)
        self.assertIs(get_db_callbacks(bot), default_db)
        self.assertIs(get_db_text_answers(bot), default_db)
        self.assertIs(get_db_chat_member(bot), default_db)

    def test_dispatcher_workflow_data_binding(self):
        """Dispatcher workflow data receives db object cleanly."""
        dp = Dispatcher()
        dp["db"] = self.dummy_db
        self.assertIs(dp["db"], self.dummy_db)


class TestMainBotStartup(unittest.IsolatedAsyncioTestCase):
    async def test_main_initialization_flow(self):
        """Verify main() runs initialization without TypeError: 'Bot' object does not support item assignment."""
        import main

        with patch("config.BOT_TOKEN", "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi"), \
             patch("main.Database.init_db", new_callable=AsyncMock) as mock_db_init, \
             patch("main.setup_bot_commands", new_callable=AsyncMock) as mock_setup, \
             patch.object(Dispatcher, "start_polling", new_callable=AsyncMock) as mock_poll:

            # Run main()
            await main.main()

            # Verify Database initialization was triggered
            self.assertTrue(mock_db_init.called)

            # Verify setup_bot_commands was invoked with the Bot instance
            self.assertTrue(mock_setup.called)
            bot_arg = mock_setup.call_args[0][0]
            self.assertIsInstance(bot_arg, Bot)
            self.assertIsNotNone(bot_arg.db)
            self.assertEqual(bot_arg["db"], bot_arg.db)

            # Verify start_polling was invoked with bot and db keyword argument
            self.assertTrue(mock_poll.called)
            self.assertIs(mock_poll.call_args[0][0], bot_arg)
            self.assertIn("db", mock_poll.call_args[1])
            self.assertIs(mock_poll.call_args[1]["db"], bot_arg.db)

    async def test_main_early_exit_when_token_unset(self):
        """Verify main() gracefully logs warning and returns when BOT_TOKEN is unset."""
        import main

        with patch("config.BOT_TOKEN", "YOUR_BOT_TOKEN_HERE"), \
             patch("main.Database.init_db", new_callable=AsyncMock), \
             patch.object(Dispatcher, "start_polling", new_callable=AsyncMock) as mock_poll:

            await main.main()
            self.assertFalse(mock_poll.called)


if __name__ == "__main__":
    unittest.main()
