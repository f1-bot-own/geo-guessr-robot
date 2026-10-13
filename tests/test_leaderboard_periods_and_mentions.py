"""
Unit tests for time-based leaderboards (daily, weekly, monthly, all-time)
and clickable user profile mentions (<a href="tg://user?id=...">).
"""

import unittest
import asyncio
import tempfile
import os
from unittest.mock import AsyncMock, MagicMock

from database.db import (
    Database,
    format_user_mention,
    get_global_leaderboard,
    get_group_leaderboard
)
from keyboards.game_kb import get_leaderboard_kb
from handlers.commands import format_leaderboard_text
from handlers.callbacks import cb_leaderboard_period

class TestLeaderboardPeriodsAndMentions(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_lb.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.tmp_dir.cleanup()

    def test_format_user_mention(self):
        """Verify user mentions format as clickable Telegram profile links with HTML escaping."""
        # Standard name
        mention = format_user_mention(1234567, "Azizbek")
        self.assertEqual(mention, '<a href="tg://user?id=1234567">Azizbek</a>')

        # Special characters must be safely HTML escaped
        mention_html = format_user_mention(999999, "<Master> & 'Hero' \"Q\"")
        self.assertIn('&lt;Master&gt;', mention_html)
        self.assertIn('&amp;', mention_html)
        self.assertIn('tg://user?id=999999', mention_html)

        # Empty or whitespace-only name fallback
        mention_empty = format_user_mention(555, "  ")
        self.assertEqual(mention_empty, '<a href="tg://user?id=555">Player 555</a>')

        # None or invalid user_id fallback
        mention_no_id = format_user_mention(None, "Guest")
        self.assertEqual(mention_no_id, '<b>Guest</b>')

    async def test_time_based_leaderboard_data(self):
        """Verify score_events are recorded and filtered by daily, weekly, monthly, and all-time."""
        user1 = 101
        user2 = 102
        group_id = -100555

        # Register users
        await self.db.get_or_create_user(user1, username="player_one", first_name="Player One")
        await self.db.get_or_create_user(user2, username="player_two", first_name="Player Two")

        # user1 scores 120 points and 25 xp in group
        await self.db.record_answer(user1, is_correct=True, points=120, xp=25, user_name="Player One", chat_id=group_id)

        # user2 scores 80 points in solo (chat_id=None)
        await self.db.record_answer(user2, is_correct=True, points=80, xp=25, user_name="Player Two", chat_id=None)

        # Check Global All-Time
        global_all = await self.db.get_global_leaderboard(limit=10, period="all_time")
        self.assertEqual(len(global_all), 2)
        self.assertEqual(global_all[0]["user_id"], user1)
        self.assertEqual(global_all[0]["total_score"], 120)

        # Check Global Daily
        global_daily = await self.db.get_global_leaderboard(limit=10, period="daily")
        self.assertEqual(len(global_daily), 2)
        self.assertEqual(global_daily[0]["user_id"], user1)
        self.assertEqual(global_daily[0]["total_score"], 120)

        # Check Global Weekly and Monthly
        global_weekly = await self.db.get_global_leaderboard(limit=10, period="weekly")
        self.assertEqual(len(global_weekly), 2)
        global_monthly = await self.db.get_global_leaderboard(limit=10, period="monthly")
        self.assertEqual(len(global_monthly), 2)

        # Check Group Daily
        group_daily = await self.db.get_group_leaderboard(group_id, limit=10, period="daily")
        self.assertEqual(len(group_daily), 1)
        self.assertEqual(group_daily[0]["user_id"], user1)
        self.assertEqual(group_daily[0]["score"], 120)

    def test_leaderboard_keyboard(self):
        """Verify keyboard has Daily, Weekly, Monthly, and All-Time with active indicator."""
        kb = get_leaderboard_kb(lb_type="global", current_period="daily", lang="uz")
        buttons = [btn for row in kb.inline_keyboard for btn in row]
        self.assertEqual(len(buttons), 4)

        # First button (daily) should have active indicator
        self.assertTrue(buttons[0].text.startswith("•"))
        self.assertEqual(buttons[0].callback_data, "lb_period:global:daily")
        self.assertEqual(buttons[1].callback_data, "lb_period:global:weekly")
        self.assertEqual(buttons[2].callback_data, "lb_period:global:monthly")
        self.assertEqual(buttons[3].callback_data, "lb_period:global:all_time")

    def test_format_leaderboard_text(self):
        """Verify formatted text includes clickable links and medals."""
        players = [
            {"user_id": 111, "first_name": "Alisher", "total_score": 300, "level": 3},
            {"user_id": 222, "first_name": "Bobur", "total_score": 150, "level": 2},
        ]
        text = format_leaderboard_text(players, lb_type="global", period="weekly", lang="uz")
        self.assertIn("Haftalik", text)
        self.assertIn('<a href="tg://user?id=111">Alisher</a>', text)
        self.assertIn("300 pts", text)
        self.assertIn("🥇", text)
        self.assertIn("🥈", text)

        # Empty leaderboard
        empty_text = format_leaderboard_text([], lb_type="global", period="daily", lang="uz")
        self.assertIn("yo'q", empty_text)

    async def test_cb_leaderboard_period_handler(self):
        """Verify cb_leaderboard_period edits text with updated leaderboard and keyboard."""
        bot = MagicMock()
        bot.db = self.db
        bot["db"] = self.db

        query = MagicMock()
        query.data = "lb_period:global:weekly"
        query.message = MagicMock()
        query.message.chat = MagicMock()
        query.message.chat.id = 12345
        query.message.chat.type = "private"
        query.from_user = MagicMock()
        query.from_user.id = 12345
        query.message.edit_text = AsyncMock()
        query.answer = AsyncMock()

        await cb_leaderboard_period(query, bot)
        query.message.edit_text.assert_called_once()
        _, kwargs = query.message.edit_text.call_args
        self.assertIn("parse_mode", kwargs)
        self.assertEqual(kwargs["parse_mode"], "HTML")
        query.answer.assert_called_once()

if __name__ == "__main__":
    unittest.main()
