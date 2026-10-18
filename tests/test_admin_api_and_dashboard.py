"""
Admin API & Dashboard Integration Tests for GeoGuru Telegram Bot.

Uses aiohttp.test_utils.AioHTTPTestCase to test:
1. GET /api/admin/stats (KPIs, accuracy %, modes distribution, 24h activity)
2. GET /api/admin/users & GET /api/admin/users/{user_id} (search, pagination, details)
3. POST /api/admin/users/ban & is_user_banned (ban/unban and game score prevention)
4. POST /api/admin/users/adjust-xp (manual XP adjustments)
5. GET /api/admin/groups (group analytics & games)
6. GET /api/admin/answers (recent logs & difficult questions)
7. POST /api/admin/broadcast & GET /api/admin/broadcast/status (broadcast engine & validation)
8. GET /api/admin/backup-db (sqlite database download stream)
9. GET /api/admin/live-stream (SSE streaming & EventBus event propagation)
10. GET /api/admin/logs (in-memory ring buffer log capture)
"""

import os
import sys
import json
import time
import asyncio
import tempfile
import logging
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

import config
from events.bus import event_bus
from database.db import Database, get_default_db
from games import GameSession, GameMode, Question
from webapp.admin_auth import (
    create_session_token,
    reset_session_store,
    reset_ip_lockouts,
)
from webapp.admin_api import register_admin_routes, log_buffer


class TestAdminAPIsAndDashboard(AioHTTPTestCase):
    """Full-stack integration tests for Admin API endpoints and database operations."""

    async def get_application(self):
        # Create isolated temporary database for each test run
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "test_api_geobot.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

        # Update global default instance to point to our test database
        import database.db as db_mod
        db_mod._default_instance = self.db

        app = web.Application()
        app["db"] = self.db
        self.mock_bot = MagicMock()
        self.mock_bot.send_message = AsyncMock(return_value=MagicMock(message_id=101))
        self.mock_bot.send_photo = AsyncMock(return_value=MagicMock(message_id=102))
        app["bot"] = self.mock_bot

        register_admin_routes(app)
        return app

    def setUp(self):
        super().setUp()
        reset_session_store()
        reset_ip_lockouts()

        self.admin_id = 12345678
        self.non_admin_id = 99999999
        config.ADMIN_IDS = [self.admin_id]
        self.admin_token = create_session_token(self.admin_id, extra_claims={"username": "superadmin"})
        self.auth_headers = {"Authorization": f"Bearer {self.admin_token}"}

    async def tearDownAsync(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    async def _seed_test_data(self):
        """Populate database with users, answer logs, and group scores."""
        # Create users
        await self.db.get_or_create_user(1001, username="alice_geo", first_name="Alice", default_lang="en")
        await self.db.get_or_create_user(1002, username="bob_traveller", first_name="Bob", default_lang="uz")
        await self.db.get_or_create_user(1003, username="charlie_maps", first_name="Charlie", default_lang="ru")


        # Record answer logs (Alice: 2 correct, Bob: 1 correct 1 wrong)
        await self.db.record_answer_log(
            user_id=1001, username="alice_geo", chat_id=-100101, mode="flag",
            question_id="UZ", question_text="Guess the flag of Uzbekistan",
            selected_option="Uzbekistan", correct_option="Uzbekistan",
            is_correct=True, points=100, time_taken=3.2
        )
        await self.db.record_answer_log(
            user_id=1001, username="alice_geo", chat_id=-100101, mode="capital",
            question_id="FR", question_text="Capital of France?",
            selected_option="Paris", correct_option="Paris",
            is_correct=True, points=90, time_taken=4.1
        )
        await self.db.record_answer_log(
            user_id=1002, username="bob_traveller", chat_id=-100101, mode="flag",
            question_id="DE", question_text="Guess the flag of Germany",
            selected_option="Belgium", correct_option="Germany",
            is_correct=False, points=-20, time_taken=6.5
        )

        # Create chat & record group scores
        await self.db.get_or_create_chat(-100101, "supergroup", "Geography Masters", "en")
        await self.db.record_match_player_stats(1001, -100101, "Alice", is_win=True, score=250, xp_bonus=50)
        await self.db.record_match_player_stats(1002, -100101, "Bob", is_win=False, score=120, xp_bonus=20)

    @unittest_run_loop
    async def test_get_stats_endpoint(self):
        """GET /api/admin/stats returns platform KPIs, accuracy, and mode distribution."""
        await self._seed_test_data()

        resp = await self.client.get("/api/admin/stats", headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])

        stats = data["stats"]
        self.assertGreaterEqual(stats["total_users"], 3)
        self.assertEqual(stats["total_answers"], 3)
        self.assertEqual(stats["answers_today"], 3)
        self.assertEqual(stats["correct_answers_today"], 2)
        # Accuracy: 2 correct out of 3 = 66.7%
        self.assertAlmostEqual(stats["accuracy_pct"], 66.7, delta=0.5)
        self.assertAlmostEqual(stats["accuracy_percent"], 66.7, delta=0.5)

        # Mode distribution checks
        mode_dist = stats["mode_distribution"]
        self.assertIsInstance(mode_dist, list)
        modes_present = [m["mode"] for m in mode_dist]
        self.assertIn("flag", modes_present)

    @unittest_run_loop
    async def test_get_users_search_and_pagination(self):
        """GET /api/admin/users handles search filtering and limit/offset pagination."""
        await self._seed_test_data()

        # 1. Search by username
        resp = await self.client.get("/api/admin/users?query=alice", headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["total"], 1)
        self.assertEqual(data["users"][0]["username"], "alice_geo")

        # 2. Search by user_id
        resp_id = await self.client.get("/api/admin/users?query=1002", headers=self.auth_headers)
        data_id = await resp_id.json()
        self.assertEqual(data_id["total"], 1)
        self.assertEqual(data_id["users"][0]["first_name"], "Bob")

        # 3. Pagination with limit=2
        resp_page = await self.client.get("/api/admin/users?limit=2&offset=0", headers=self.auth_headers)
        data_page = await resp_page.json()
        self.assertEqual(len(data_page["users"]), 2)
        self.assertGreaterEqual(data_page["total"], 3)

    @unittest_run_loop
    async def test_get_user_detail(self):
        """GET /api/admin/users/{user_id} returns detailed user profile and answer logs."""
        await self._seed_test_data()

        resp = await self.client.get("/api/admin/users/1001", headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])

        user_detail = data["user"]
        self.assertEqual(user_detail["user_id"], 1001)
        self.assertEqual(user_detail["username"], "alice_geo")
        self.assertIn("recent_answers", user_detail)
        self.assertGreaterEqual(len(user_detail["recent_answers"]), 2)

        # Unknown user returns 404
        resp_404 = await self.client.get("/api/admin/users/99999", headers=self.auth_headers)
        self.assertEqual(resp_404.status, 404)

    @unittest_run_loop
    async def test_user_ban_unban_and_game_score_prevention(self):
        """
        POST /api/admin/users/ban sets ban status.
        Verifies is_user_banned returns True and banned user is blocked from scoring in GameSession.
        """
        await self._seed_test_data()
        target_user = 1002

        # 1. Initially user is not banned
        self.assertFalse(await self.db.is_user_banned(target_user))

        # 2. Ban user via API
        ban_payload = {
            "user_id": target_user,
            "ban": True,
            "reason": "Using automated script"
        }
        resp = await self.client.post("/api/admin/users/ban", json=ban_payload, headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertTrue(data["banned"])

        # Verify DB reflects ban and reason
        self.assertTrue(await self.db.is_user_banned(target_user))
        user_info = await self.db.get_user(target_user)
        self.assertEqual(user_info["is_banned"], 1)
        self.assertEqual(user_info["ban_reason"], "Using automated script")

        # 3. Verify banned user cannot score in GameSession
        session = GameSession(chat_id=-100101, mode=GameMode.FLAG, total_rounds=1)
        session.current_question = Question(
            text="Which country?",
            options=["Italy", "Germany", "France", "Spain"],
            correct_index=1,
            correct_answer="Germany",
            mode=GameMode.FLAG,
            country_code="DE"
        )
        session.status = "in_progress"

        # Banned user attempts to check answer -> rejected with 'banned' and 0 points
        result, points, _ = await session.check_answer(target_user, "Bob", 1)
        self.assertEqual(result, "banned")
        self.assertEqual(points, 0)
        self.assertNotIn(target_user, session.scores)

        # Non-banned user answers correctly -> receives points
        allowed_user = 1001
        res_ok, pts_ok, _ = await session.check_answer(allowed_user, "Alice", 1)
        self.assertEqual(res_ok, "correct")
        self.assertGreater(pts_ok, 0)
        self.assertIn(allowed_user, session.scores)

        # 4. Unban user via API
        unban_payload = {"user_id": target_user, "ban": False}
        resp_unban = await self.client.post("/api/admin/users/ban", json=unban_payload, headers=self.auth_headers)
        self.assertEqual(resp_unban.status, 200)
        self.assertFalse(await self.db.is_user_banned(target_user))

    @unittest_run_loop
    async def test_adjust_user_xp_endpoint(self):
        """POST /api/admin/users/adjust-xp updates total XP and recomputes level."""
        await self._seed_test_data()

        payload = {"user_id": 1003, "xp": 1500}
        resp = await self.client.post("/api/admin/users/adjust-xp", json=payload, headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["xp"], 1500)

        # Verify in database
        user = await self.db.get_user(1003)
        self.assertEqual(user["xp"], 1500)
        self.assertGreater(user["level"], 1)

    @unittest_run_loop
    async def test_get_groups_endpoint(self):
        """GET /api/admin/groups returns list of registered groups and statistics."""
        await self._seed_test_data()

        resp = await self.client.get("/api/admin/groups", headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertGreaterEqual(data["total"], 1)
        group = data["groups"][0]
        self.assertEqual(group["chat_id"], -100101)
        self.assertEqual(group["title"], "Geography Masters")

    @unittest_run_loop
    async def test_get_answers_endpoint(self):
        """GET /api/admin/answers returns recent logs and difficult questions analysis."""
        await self._seed_test_data()

        resp = await self.client.get("/api/admin/answers?limit=10", headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertIn("recent_answers", data)
        self.assertIn("difficult_questions", data)
        self.assertEqual(len(data["recent_answers"]), 3)

    @unittest_run_loop
    async def test_broadcast_validation_and_job_execution(self):
        """
        POST /api/admin/broadcast validates targets and starts background delivery.
        GET /api/admin/broadcast/status tracks progress.
        """
        await self._seed_test_data()

        # 1. Validation failure: missing text
        resp_err = await self.client.post("/api/admin/broadcast", json={"target": "all", "text": ""}, headers=self.auth_headers)
        self.assertEqual(resp_err.status, 400)

        # 2. Validation failure: invalid target
        resp_target_err = await self.client.post("/api/admin/broadcast", json={"target": "invalid_group", "text": "Hello"}, headers=self.auth_headers)
        self.assertEqual(resp_target_err.status, 400)

        # 3. Successful broadcast start
        broadcast_payload = {
            "target": "users",
            "text": "🌟 <b>New Weekend Tournament!</b>\nJoin now!",
            "button_text": "Play Now",
            "button_url": "https://t.me/geoguru_bot"
        }
        resp = await self.client.post("/api/admin/broadcast", json=broadcast_payload, headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        broadcast_id = data["broadcast_id"]
        self.assertIsNotNone(broadcast_id)

        # Give background broadcast worker a brief moment to process
        await asyncio.sleep(0.15)

        # 4. Check broadcast status
        resp_status = await self.client.get(f"/api/admin/broadcast/status?broadcast_id={broadcast_id}", headers=self.auth_headers)
        self.assertEqual(resp_status.status, 200)
        status_data = await resp_status.json()
        self.assertTrue(status_data["ok"])
        self.assertIsNotNone(status_data["job"])
        self.assertIn(status_data["job"]["status"], ("running", "completed"))
        # Verify bot.send_message was invoked for recipients
        self.assertTrue(self.mock_bot.send_message.called)

    @unittest_run_loop
    async def test_backup_database_download(self):
        """GET /api/admin/backup-db downloads geobot.db as a file attachment."""
        resp = await self.client.get("/api/admin/backup-db", headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        self.assertIn("Content-Disposition", resp.headers)
        self.assertIn("geobot_backup", resp.headers["Content-Disposition"])
        body = await resp.read()
        # SQLite header check: first 16 bytes must start with "SQLite format 3"
        self.assertTrue(body.startswith(b"SQLite format 3"))

    @unittest_run_loop
    async def test_live_stream_sse_endpoint(self):
        """GET /api/admin/live-stream connects SSE client and receives EventBus events."""
        # Clear previous events from history
        if hasattr(event_bus, "clear_history"):
            event_bus.clear_history()
        elif hasattr(event_bus, "_history"):
            event_bus._history.clear()

        # Using ?token= query parameter as standard for EventSource / SSE
        token_url = f"/api/admin/live-stream?token={self.admin_token}"

        resp = await self.client.get(token_url)
        self.assertEqual(resp.status, 200)
        self.assertEqual(resp.headers.get("Content-Type"), "text/event-stream")

        # Read initial connection payload
        initial_chunk = await resp.content.read(128)
        self.assertIn(b"event: connected", initial_chunk)

        # Trigger live event on EventBus
        event_bus.publish("test_system_alert", {"msg": "Server is healthy"})

        # Read stream until the published event arrives
        found = False
        deadline = time.time() + 3.0
        while time.time() < deadline:
            try:
                chunk = await asyncio.wait_for(resp.content.read(512), timeout=1.0)
                if b"event: test_system_alert" in chunk:
                    found = True
                    break
            except asyncio.TimeoutError:
                break

        self.assertTrue(found, "SSE stream must deliver event published to event_bus")
        resp.close()


    @unittest_run_loop
    async def test_logs_endpoint(self):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)
        test_msg = f"Audit log verification entry {int(time.time())}"
        root_logger.info(test_msg)


        resp = await self.client.get("/api/admin/logs?lines=20", headers=self.auth_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertGreaterEqual(data["count"], 1)
        found = any(test_msg in line for line in data["lines"])
        self.assertTrue(found, "Newly logged message must appear in admin logs response")


if __name__ == "__main__":
    unittest.main()
