"""
Unit tests for Database & Engine Specialist Upgrades.
Verifies:
- CREATE_ADMIN_LOGINS_TABLE in schema & db initialization
- record_admin_login and get_recent_admin_logins
- get_recent_users
- adjust_user_score (cannot be negative)
- set_user_level
- reset_user_stats
- get_user_full_profile (returns user, stats, answers)
- answer_logs capture in record_answer & record_answer_result
- clean display names (never lone '.')
- EventBus payload for 'answer'
"""

import os
import tempfile
import unittest
from database.db import (
    Database,
    resolve_clean_user_name,
    format_user_mention,
    record_admin_login,
    get_recent_admin_logins,
    get_recent_users,
    adjust_user_score,
    set_user_level,
    reset_user_stats,
    get_user_full_profile,
    record_answer,
    record_answer_result,
    set_default_db
)
from events.bus import event_bus


class TestDatabaseEngineUpgrade(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_upgrade.db")
        self.db = Database(self.db_path)
        await self.db.init_db()
        set_default_db(self.db)

    async def asyncTearDown(self):
        set_default_db(None)
        self.temp_dir.cleanup()

    async def test_admin_logins_table_and_methods(self):
        # Record admin login
        login_id1 = await self.db.record_admin_login(
            user_id=12345,
            username="admin_boss",
            ip="192.168.1.1",
            user_agent="Mozilla/5.0",
            auth_method="otp"
        )
        self.assertIsInstance(login_id1, int)
        self.assertGreater(login_id1, 0)

        login_id2 = await record_admin_login(
            user_id=67890,
            username="sec_admin",
            ip="10.0.0.1",
            user_agent="TelegramBot",
            auth_method="master_password"
        )
        self.assertGreater(login_id2, login_id1)

        # Retrieve recent logins
        logins = await self.db.get_recent_admin_logins(limit=10)
        self.assertEqual(len(logins), 2)
        self.assertEqual(logins[0]["user_id"], 67890)
        self.assertEqual(logins[0]["auth_method"], "master_password")
        self.assertEqual(logins[1]["user_id"], 12345)
        self.assertEqual(logins[1]["auth_method"], "otp")

    async def test_get_recent_users(self):
        # Create users
        for i in range(5):
            await self.db.get_or_create_user(
                user_id=1000 + i,
                username=f"user_{i}",
                first_name=f"Player_{i}"
            )

        recent = await self.db.get_recent_users(limit=3)
        self.assertEqual(len(recent), 3)
        self.assertIn("user_id", recent[0])
        self.assertIn("username", recent[0])
        self.assertIn("first_name", recent[0])
        self.assertIn("created_at", recent[0])

    async def test_adjust_user_score(self):
        uid = 555
        # Initial adjust (adds 100)
        score1 = await self.db.adjust_user_score(uid, 100)
        self.assertEqual(score1, 100)

        # Add 50
        score2 = await adjust_user_score(uid, 50)
        self.assertEqual(score2, 150)

        # Deduct 80
        score3 = await self.db.adjust_user_score(uid, -80)
        self.assertEqual(score3, 70)

        # Deduct more than current total (cannot be negative)
        score4 = await self.db.adjust_user_score(uid, -200)
        self.assertEqual(score4, 0)

    async def test_set_user_level(self):
        uid = 777
        new_lvl = await self.db.set_user_level(uid, 15)
        self.assertEqual(new_lvl, 15)

        user = await self.db.get_user(uid)
        self.assertEqual(user["level"], 15)

        # Test module-level wrapper
        lvl2 = await set_user_level(uid, 42)
        self.assertEqual(lvl2, 42)
        user2 = await self.db.get_user(uid)
        self.assertEqual(user2["level"], 42)

    async def test_reset_user_stats(self):
        uid = 888
        await self.db.get_or_create_user(uid, username="speedy", first_name="Speedy")
        await self.db.record_answer(uid, is_correct=True, points=300, xp=150)
        await self.db.set_user_level(uid, 5)

        user_before = await self.db.get_user(uid)
        self.assertGreater(user_before["total_score"], 0)
        self.assertGreater(user_before["xp"], 0)
        self.assertGreater(user_before["correct_answers"], 0)

        # Reset
        res = await self.db.reset_user_stats(uid)
        self.assertTrue(res)

        user_after = await self.db.get_user(uid)
        self.assertEqual(user_after["total_score"], 0)
        self.assertEqual(user_after["xp"], 0)
        self.assertEqual(user_after["level"], 1)
        self.assertEqual(user_after["total_answers"], 0)
        self.assertEqual(user_after["correct_answers"], 0)
        self.assertEqual(user_after["games_played"], 0)
        self.assertEqual(user_after["games_won"], 0)
        self.assertEqual(user_after["current_streak"], 0)
        self.assertEqual(user_after["best_streak"], 0)

    async def test_answer_logs_captured_always(self):
        uid = 999
        await self.db.get_or_create_user(uid, username="tester", first_name="Tester")

        # 1. record_answer must insert into answer_logs
        await self.db.record_answer(
            user_id=uid,
            is_correct=True,
            points=120,
            xp=25,
            user_name="Tester",
            username="tester",
            chat_id=-100123,
            mode="flag",
            question_id="UZ",
            question_text="Flag of Uzbekistan",
            selected_option="Uzbekistan",
            correct_option="Uzbekistan",
            time_taken=2.1,
            chat_title="Geography Club"
        )

        logs = await self.db.get_recent_answer_logs(limit=10, user_id=uid)
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]["is_correct"], 1)
        self.assertEqual(logs[0]["points"], 120)
        self.assertEqual(logs[0]["selected_option"], "Uzbekistan")
        self.assertEqual(logs[0]["user_answer"], "Uzbekistan")
        self.assertEqual(logs[0]["correct_answer"], "Uzbekistan")

        # 2. record_answer_result must delegate and insert into answer_logs
        await self.db.record_answer_result(
            user_id=uid,
            is_correct=False,
            xp_earned=0,
            points=-20,
            user_name="Tester",
            username="tester",
            chat_id=-100123,
            mode="capital",
            question_id="FR",
            question_text="Capital of France",
            selected_option="Lyon",
            correct_option="Paris",
            time_taken=4.5
        )

        logs2 = await self.db.get_recent_answer_logs(limit=10, user_id=uid)
        self.assertEqual(len(logs2), 2)
        self.assertEqual(logs2[0]["is_correct"], 0)
        self.assertEqual(logs2[0]["selected_option"], "Lyon")
        self.assertEqual(logs2[0]["correct_option"], "Paris")

    async def test_get_user_full_profile(self):
        uid = 111
        await self.db.get_or_create_user(uid, username="gamer", first_name="Gamer")
        await self.db.record_answer(uid, is_correct=True, points=100, xp=25)
        await self.db.record_answer(uid, is_correct=False, points=0, xp=0)

        profile = await self.db.get_user_full_profile(uid)
        self.assertIsNotNone(profile)
        self.assertIn("user", profile)
        self.assertIn("stats", profile)
        self.assertIn("accuracy", profile["stats"])
        self.assertEqual(profile["stats"]["accuracy"], 50.0)
        self.assertEqual(len(profile["answers"]), 2)

    async def test_clean_display_name_never_lone_dot(self):
        # If first_name is empty or ".", fallback to @username or Player {id}
        name1 = resolve_clean_user_name(100, first_name=".", username="cool_user")
        self.assertEqual(name1, "@cool_user")

        name2 = resolve_clean_user_name(200, first_name="", username="cool_user2")
        self.assertEqual(name2, "@cool_user2")

        name3 = resolve_clean_user_name(300, first_name=".", username="")
        self.assertEqual(name3, "Player 300")

        name4 = resolve_clean_user_name(400, first_name="  .  ", username=None)
        self.assertEqual(name4, "Player 400")

        name5 = resolve_clean_user_name(500, first_name="Alice", username="alice_w")
        self.assertEqual(name5, "Alice")

        # Mention formatting
        mention_dot = format_user_mention(123, ".")
        self.assertNotIn(">.</a>", mention_dot)
        self.assertIn(">Player 123</a>", mention_dot)

    async def test_event_bus_payload_for_answer(self):
        q = event_bus.subscribe()
        try:
            await self.db.record_answer(
                user_id=1234,
                is_correct=True,
                points=100,
                xp=25,
                user_name=".",
                username="dot_player",
                chat_id=-100999,
                mode="flag",
                question_text="Which country?",
                selected_option="Brazil",
                correct_option="Brazil",
                chat_title="GeoGroup"
            )

            # Find the "answer" event
            found_event = None
            while not q.empty():
                ev = q.get_nowait()
                if ev.get("type") == "answer":
                    found_event = ev
                    break

            self.assertIsNotNone(found_event)
            data = found_event["data"]

            # Verify all required keys
            required_keys = [
                "user_id", "user_name", "username", "mode", "question_text",
                "selected_option", "correct_option", "is_correct", "points",
                "xp", "chat_id", "chat_title", "timestamp"
            ]
            for key in required_keys:
                self.assertIn(key, data, f"Key '{key}' missing from EventBus 'answer' payload")

            # Check that user_name is never a lone dot
            self.assertNotEqual(data["user_name"], ".")
            self.assertEqual(data["user_name"], "@dot_player")
            self.assertEqual(data["chat_title"], "GeoGroup")
            self.assertEqual(data["is_correct"], True)
        finally:
            event_bus.unsubscribe(q)


if __name__ == "__main__":
    unittest.main()
