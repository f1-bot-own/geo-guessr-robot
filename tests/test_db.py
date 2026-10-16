"""
Unit tests for database module using an isolated temporary SQLite database.
"""
import os
import unittest
import tempfile
from pathlib import Path

# Override DB_PATH before importing database.db
temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
temp_db_path = temp_db.name
temp_db.close()

os.environ["DB_PATH"] = temp_db_path

import config
config.DB_PATH = temp_db_path

import database.db as db

class TestDatabase(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        await db.init_db()

    async def asyncTearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        try:
            if os.path.exists(temp_db_path):
                os.remove(temp_db_path)
        except Exception:
            pass

    def test_level_calculation(self):
        self.assertEqual(db.calculate_level(0), 1)
        self.assertEqual(db.calculate_level(199), 1)
        self.assertEqual(db.calculate_level(200), 2)
        self.assertEqual(db.calculate_level(800), 3)

    async def test_user_creation_and_default_language_is_en(self):
        user = await db.get_or_create_user(user_id=101, first_name="John", username="john_doe")
        self.assertIsNotNone(user)
        self.assertEqual(user["user_id"], 101)
        # MUST default to English ('en')
        self.assertEqual(user["language"], "en")

        lang = await db.get_user_language(101)
        self.assertEqual(lang, "en")

    async def test_language_switch(self):
        await db.get_or_create_user(user_id=102, first_name="Alice")
        await db.set_user_language(102, "uz")
        lang = await db.get_user_language(102)
        self.assertEqual(lang, "uz")

        await db.set_user_language(102, "ru")
        lang2 = await db.get_user_language(102)
        self.assertEqual(lang2, "ru")

    async def test_answer_result_and_streak(self):
        await db.get_or_create_user(user_id=103, first_name="Bob")

        # 3 correct answers
        await db.record_answer_result(user_id=103, is_correct=True, xp_earned=25)
        await db.record_answer_result(user_id=103, is_correct=True, xp_earned=25)
        await db.record_answer_result(user_id=103, is_correct=True, xp_earned=25)

        user = await db.get_user(103)
        self.assertEqual(user["xp"], 75)
        self.assertEqual(user["current_streak"], 3)
        self.assertEqual(user["best_streak"], 3)
        self.assertEqual(user["correct_answers"], 3)

        # 1 wrong answer resets current streak, keeps best
        await db.record_answer_result(user_id=103, is_correct=False, xp_earned=0)
        user_after = await db.get_user(103)
        self.assertEqual(user_after["current_streak"], 0)
        self.assertEqual(user_after["best_streak"], 3)
        self.assertEqual(user_after["total_answers"], 4)

    async def test_match_stats_and_group_leaderboard(self):
        chat_id = -100555
        await db.get_or_create_user(user_id=201, first_name="Winner")
        await db.get_or_create_user(user_id=202, first_name="RunnerUp")

        await db.record_match_player_stats(user_id=201, chat_id=chat_id, first_name="Winner", is_win=True, score=350, xp_bonus=100)
        await db.record_match_player_stats(user_id=202, chat_id=chat_id, first_name="RunnerUp", is_win=False, score=150, xp_bonus=50)

        group_board = await db.get_group_leaderboard(chat_id)
        self.assertGreaterEqual(len(group_board), 2)
        self.assertEqual(group_board[0]["user_id"], 201)
        self.assertEqual(group_board[0]["score"], 350)
        self.assertEqual(group_board[0]["games_won"], 1)

    async def test_empty_leaderboard_queries_do_not_crash(self):
        """Leaderboard queries on empty database / non-existent chat must return empty list without crashing."""
        empty_chat_id = -999999999
        for period in ["all_time", "daily", "weekly", "monthly"]:
            res_group = await db.get_group_leaderboard(empty_chat_id, limit=10, period=period)
            self.assertIsInstance(res_group, list)
            self.assertEqual(len(res_group), 0)

        # Chat ID is None
        res_none = await db.get_group_leaderboard(None, limit=10)
        self.assertEqual(res_none, [])

        # Limit edge cases (negative, zero, overly large)
        res_limit_zero = await db.get_global_leaderboard(limit=0)
        self.assertIsInstance(res_limit_zero, list)

        res_limit_neg = await db.get_global_leaderboard(limit=-5)
        self.assertIsInstance(res_limit_neg, list)

    async def test_add_user_xp(self):
        """add_user_xp awards XP, recalculates level, and creates user if missing."""
        uid = 888777
        new_xp = await db.add_user_xp(uid, 300, first_name="MiniAppGamer")
        self.assertEqual(new_xp, 300)

        u = await db.get_user(uid)
        self.assertIsNotNone(u)
        self.assertEqual(u["xp"], 300)
        self.assertEqual(u["level"], db.calculate_level(300))

        # Award more XP
        updated_xp = await db.add_user_xp(uid, 500)
        self.assertEqual(updated_xp, 800)
        u2 = await db.get_user(uid)
        self.assertEqual(u2["xp"], 800)
        self.assertEqual(u2["level"], 3)

    async def test_daily_challenge(self):
        user_id = 301
        today = "2026-10-10"
        
        # Check initially not done
        init_done = await db.check_daily_challenge_done(user_id, today)
        self.assertIsNone(init_done)

        # Record completed
        await db.get_or_create_user(user_id=user_id, first_name="DailyPlayer")
        await db.record_daily_challenge_done(user_id, score=400, xp_bonus=150, challenge_date=today)

        after_done = await db.check_daily_challenge_done(user_id, today)
        self.assertIsNotNone(after_done)
        self.assertEqual(after_done["score"], 400)

    async def test_daily_streak_reset_on_skip_and_active_check(self):
        """Skipping a day properly breaks and resets the daily streak."""
        user_id = 302
        await db.get_or_create_user(user_id=user_id, first_name="StreakPlayer")

        # Day 1
        await db.record_daily_challenge_done(user_id, score=200, challenge_date="2026-10-10")
        u = await db.get_user(user_id)
        self.assertEqual(u["daily_streak"], 1)
        self.assertEqual(await db.get_daily_streak(user_id, today_date="2026-10-10"), 1)
        self.assertEqual(await db.get_daily_streak(user_id, today_date="2026-10-11"), 1)

        # Day 2 (consecutive)
        await db.record_daily_challenge_done(user_id, score=250, challenge_date="2026-10-11")
        u = await db.get_user(user_id)
        self.assertEqual(u["daily_streak"], 2)

        # Skip Day 3 (2026-10-12)
        # Check active streak on Day 4 before playing -> streak is broken (0)
        self.assertEqual(await db.get_daily_streak(user_id, today_date="2026-10-13"), 0)

        # Complete challenge on Day 4 (2026-10-13) -> streak must reset to 1
        await db.record_daily_challenge_done(user_id, score=300, challenge_date="2026-10-13")
        u_after = await db.get_user(user_id)
        self.assertEqual(u_after["daily_streak"], 1)
        self.assertEqual(await db.get_daily_streak(user_id, today_date="2026-10-13"), 1)

    async def test_daily_challenge_timestamp_format_resilience(self):
        """Dates formatted with timestamp or ISO time must parse safely without raising ValueError."""
        user_id = 303
        await db.get_or_create_user(user_id=user_id, first_name="TimePlayer")

        # Completion with ISO timestamp containing T and seconds
        await db.record_daily_challenge_done(user_id, score=100, challenge_date="2026-10-15T14:30:00")
        record = await db.check_daily_challenge_done(user_id, "2026-10-15")
        self.assertIsNotNone(record)
        self.assertEqual(record["score"], 100)

    async def test_duels(self):
        duel_id = await db.create_duel(
            chat_id=-100777,
            challenger_id=401,
            challenger_name="Challenger",
            opponent_id=402,
            opponent_name="Opponent"
        )
        self.assertGreater(duel_id, 0)

        duel = await db.get_duel(duel_id)
        self.assertEqual(duel["status"], "pending")

        await db.update_duel_status(duel_id, status="completed", winner_id=401)
        updated = await db.get_duel(duel_id)
        self.assertEqual(updated["status"], "completed")
        self.assertEqual(updated["winner_id"], 401)

if __name__ == "__main__":
    unittest.main()
