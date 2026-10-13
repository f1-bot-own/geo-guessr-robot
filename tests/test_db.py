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
