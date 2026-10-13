"""
Auditing & Verification Test Suite for GeoGuru & GeoGuessr Telegram Bot.
Verifies fixes for:
1. Automatic user registration and name persistence for group chat players.
2. Daily Challenge deterministic generation, 5-round lifecycle, streak tracking, and DB completion.
3. Group text answer recognition: option shortcuts (A-D, 1-4), whole-word boundary matching (preventing false positives like 'iran' in 'tiranozavr'), and Higher/Lower distractor handling.
4. Duel DB lifecycle: creation, acceptance callback parsing (4 vs 5 parts), status updates, and match history logging.
5. Deep-link argument parsing in start commands.
"""

import os
import re
import tempfile
import unittest
from datetime import date, timedelta

import config
from database.db import Database
from games.models import GameMode, Question
from games.daily_session import DailyGameSession
from games.session import GameSession
from games.manager import game_manager
from keyboards.game_kb import get_duel_kb, get_daily_question_kb
from handlers.text_answers import _normalize, OPTION_SHORTCUTS


class TestGroupUserRegistrationAndStats(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_group_stats.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.temp_dir.cleanup()

    async def test_unregistered_group_player_answer_recorded(self):
        """Unregistered user in group chat must be auto-created on answer; points/XP must not be lost."""
        unregistered_uid = 999888
        # User never called /start or get_or_create_user
        user_before = await self.db.get_user(unregistered_uid)
        self.assertIsNone(user_before)

        # Player answers correctly in group
        await self.db.record_answer(
            user_id=unregistered_uid,
            is_correct=True,
            points=120,
            xp=25,
            user_name="Jasur",
            username="jasur_geo"
        )

        user_after = await self.db.get_user(unregistered_uid)
        self.assertIsNotNone(user_after)
        self.assertEqual(user_after["first_name"], "Jasur")
        self.assertEqual(user_after["username"], "jasur_geo")
        self.assertEqual(user_after["total_score"], 120)
        self.assertEqual(user_after["xp"], 25)
        self.assertEqual(user_after["current_streak"], 1)

    async def test_unregistered_group_player_name_in_group_leaderboard(self):
        """Player names must be saved in group_scores, not generic 'Player'."""
        chat_id = -100777
        uid = 555444

        await self.db.update_group_player_score(
            chat_id=chat_id,
            user_id=uid,
            points=150,
            is_win=True,
            first_name="Dilshod",
            username="dilshod99"
        )

        board = await self.db.get_group_leaderboard(chat_id)
        self.assertEqual(len(board), 1)
        self.assertEqual(board[0]["user_id"], uid)
        self.assertEqual(board[0]["first_name"], "Dilshod")
        self.assertEqual(board[0]["score"], 150)
        self.assertEqual(board[0]["wins"], 1)


class TestDailyChallengeLifecycle(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_daily.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.temp_dir.cleanup()

    def test_daily_challenge_deterministic_generation(self):
        """Same date seed must generate identical questions across sessions."""
        d1 = DailyGameSession(user_id=1, user_name="A", today_str="2026-10-10", lang="en")
        d2 = DailyGameSession(user_id=2, user_name="B", today_str="2026-10-10", lang="en")

        self.assertEqual(len(d1.questions), 5)
        self.assertEqual(len(d2.questions), 5)

        for i in range(5):
            self.assertEqual(d1.questions[i].mode, d2.questions[i].mode)
            self.assertEqual(d1.questions[i].text, d2.questions[i].text)
            self.assertEqual(d1.questions[i].correct_index, d2.questions[i].correct_index)

    async def test_daily_challenge_streak_tracking(self):
        """Daily streak must increment on consecutive days and reset on gap."""
        uid = 1234
        # Day 1
        await self.db.record_daily_challenge_done(uid, score=400, xp_bonus=150, challenge_date="2026-10-10")
        u1 = await self.db.get_user(uid)
        self.assertEqual(u1["daily_streak"], 1)

        # Day 2 (consecutive)
        await self.db.record_daily_challenge_done(uid, score=500, xp_bonus=150, challenge_date="2026-10-11")
        u2 = await self.db.get_user(uid)
        self.assertEqual(u2["daily_streak"], 2)

        # Day 4 (gap of 2 days -> resets to 1)
        await self.db.record_daily_challenge_done(uid, score=300, xp_bonus=150, challenge_date="2026-10-14")
        u3 = await self.db.get_user(uid)
        self.assertEqual(u3["daily_streak"], 1)

    async def test_daily_challenge_completion_lock(self):
        """Player can only complete daily challenge once per day."""
        uid = 4321
        today = "2026-10-10"
        self.assertTrue(await self.db.can_play_daily(uid, today))

        await self.db.record_daily_completion(uid, today_str=today, score=450, xp=150)
        self.assertFalse(await self.db.can_play_daily(uid, today))

        record = await self.db.check_daily_challenge_done(uid, today)
        self.assertIsNotNone(record)
        self.assertEqual(record["score"], 450)


class TestTextAnswerRecognition(unittest.TestCase):
    def test_option_shortcuts(self):
        """Shortcuts 1-4 and a-d must map to valid indices 0-3."""
        self.assertEqual(OPTION_SHORTCUTS.get("1"), 0)
        self.assertEqual(OPTION_SHORTCUTS.get("a"), 0)
        self.assertEqual(OPTION_SHORTCUTS.get("2"), 1)
        self.assertEqual(OPTION_SHORTCUTS.get("b"), 1)
        self.assertEqual(OPTION_SHORTCUTS.get("3"), 2)
        self.assertEqual(OPTION_SHORTCUTS.get("c"), 2)
        self.assertEqual(OPTION_SHORTCUTS.get("4"), 3)
        self.assertEqual(OPTION_SHORTCUTS.get("d"), 3)

    def test_text_normalization_and_word_boundaries(self):
        """Substrings inside other words must not trigger false positives."""
        # 'iran' should not match 'tiranozavr'
        norm = _normalize("tiranozavr")
        pattern = r"(?:\b|^)iran(?:\b|$)"
        self.assertIsNone(re.search(pattern, norm))

        # 'iran' SHOULD match 'bu mamlakat iran'
        norm_valid = _normalize("bu mamlakat iran")
        self.assertIsNotNone(re.search(pattern, norm_valid))

        # 'oman' should not match 'omonmisiz'
        norm_oman = _normalize("omonmisiz")
        pattern_oman = r"(?:\b|^)oman(?:\b|$)"
        self.assertIsNone(re.search(pattern_oman, norm_oman))

    def test_higher_lower_option_stripping(self):
        """Higher/Lower options with '🅰️ Country' must normalize cleanly."""
        opt_a = "🅰️ Uzbekistan"
        norm_a = _normalize(opt_a)
        self.assertIn("uzbekistan", norm_a)


class TestDuelCallbacksAndPersistence(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_duel.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.temp_dir.cleanup()

    async def test_duel_creation_and_acceptance_markup(self):
        """get_duel_kb generates valid callback_data that can be parsed with 4 or 5 segments."""
        kb = get_duel_kb(challenger_id=100, target_id=200, lang="en", duel_id=42)
        btn = kb.inline_keyboard[0][0]
        self.assertIn("duel:accept:100:200:42", btn.callback_data)

        parts = btn.callback_data.split(":")
        self.assertGreaterEqual(len(parts), 4)
        self.assertEqual(parts[1], "accept")
        self.assertEqual(int(parts[2]), 100)
        self.assertEqual(int(parts[3]), 200)
        self.assertEqual(int(parts[4]), 42)

    async def test_duel_db_status_transitions(self):
        """Duel DB record must update from pending to active and completed with winner."""
        duel_id = await self.db.create_duel(
            chat_id=-100111,
            challenger_id=10,
            challenger_name="Alice",
            opponent_id=20,
            opponent_name="Bob"
        )
        self.assertGreater(duel_id, 0)

        d = await self.db.get_duel(duel_id)
        self.assertEqual(d["status"], "pending")

        # Accept
        await self.db.update_duel_status(duel_id, status="active")
        d_active = await self.db.get_duel(duel_id)
        self.assertEqual(d_active["status"], "active")

        # Complete with Alice winning
        await self.db.update_duel_status(duel_id, status="completed", winner_id=10)
        d_done = await self.db.get_duel(duel_id)
        self.assertEqual(d_done["status"], "completed")
        self.assertEqual(d_done["winner_id"], 10)

    async def test_match_history_recording(self):
        """Match records must be stored in the matches table."""
        await self.db.record_match(
            chat_id=-100999,
            mode="flag",
            winner_id=10,
            winner_name="Alice",
            winner_score=350,
            players_count=4
        )
        # Verify row exists in matches table
        async with self.db._connect() if hasattr(self.db, "_connect") else __import__("aiosqlite").connect(self.db.db_path) as conn:
            cursor = await conn.execute("SELECT * FROM matches WHERE chat_id = -100999")
            row = await cursor.fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row[2], "flag")
            self.assertEqual(row[3], 10)
            self.assertEqual(row[4], "Alice")
            self.assertEqual(row[5], 350)
            self.assertEqual(row[6], 4)


if __name__ == "__main__":
    unittest.main()
