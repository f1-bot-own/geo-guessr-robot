"""
Comprehensive QA & Security Tests for Admin Telemetry & User Management.

Covers:
1. `admin_logins` table: login recording on OTP (/api/admin/verify-otp) and WebApp
   (/api/admin/verify-webapp) auth with exact timestamp, IP, user agent, and retrieval
   of last 50 logins.
2. `get_recent_users(50)`: latest 50 registered users sorted by created_at DESC with
   all required fields.
3. `adjust_user_score`, `adjust_user_xp`, `set_user_level`, `reset_user_stats`: points
   addition/deduction (clamped at 0), level changes (>= 1), and full stats wipeout.
4. `get_user_full_profile`: returns user profile, computed stats (accuracy %, win rate %),
   and recent answer logs (last 100).
5. `answer_logs` completeness & clean display names: verify record_answer,
   record_answer_result, and check_answer always insert into answer_logs, and EventBus
   emits "answer" events with clean display names (never a lone '.', falls back to @username
   or Player {user_id}).
6. Admin API endpoints:
   - GET /api/admin/logins
   - GET /api/admin/users/recent
   - GET /api/admin/users/{user_id}/full
   - POST /api/admin/users/adjust-points
   - POST /api/admin/users/set-level
   - POST /api/admin/users/reset-stats
   - GET /api/admin/answers/history
   - Pre-populated SSE stream (GET /api/admin/live-stream).
   - Auth guards (401 unauthorized, 403 forbidden) & payload validation (400 bad request).
"""

import os
import sys
import json
import time
import hmac
import hashlib
import asyncio
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlencode
from unittest.mock import AsyncMock, MagicMock, patch

from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

import config
from events.bus import event_bus, subscribe, unsubscribe
from database.db import Database, resolve_clean_user_name, format_user_mention
from games import GameSession, GameMode, Question
from webapp.admin_auth import (
    create_session_token,
    create_otp,
    reset_session_store,
    reset_ip_lockouts,
)
from webapp.admin_api import register_admin_routes


class TestAdminDatabaseTelemetryAndUserMgmt(unittest.IsolatedAsyncioTestCase):
    """Deep unit tests for Database telemetry, user management methods, and name sanitization."""

    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "test_db_telemetry.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

        # Update global default instance to point to our test database
        import database.db as db_mod
        self.old_instance = db_mod._default_instance
        db_mod._default_instance = self.db

    async def asyncTearDown(self):
        import database.db as db_mod
        db_mod._default_instance = self.old_instance
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    # -------------------------------------------------------------
    # 1. admin_logins Table & Methods
    # -------------------------------------------------------------
    async def test_admin_logins_recording_and_retrieval(self):
        """Verify record_admin_login stores records with exact IP, UA, timestamp, and emits event."""
        q_events = subscribe()
        try:
            # Record 3 logins
            id1 = await self.db.record_admin_login(
                user_id=101, username="admin_one", ip="192.168.1.10",
                user_agent="Mozilla/5.0 TestUA", auth_method="OTP"
            )
            id2 = await self.db.record_admin_login(
                user_id=102, username="admin_two", ip="10.0.0.5",
                user_agent="TelegramBot WebApp", auth_method="WebApp"
            )
            id3 = await self.db.record_admin_login(
                user_id=101, username="admin_one", ip="192.168.1.10",
                user_agent="Mozilla/5.0 TestUA", auth_method="OTP"
            )

            self.assertGreater(id1, 0)
            self.assertGreater(id2, id1)
            self.assertGreater(id3, id2)

            # Check EventBus emitted "admin_login" event
            login_events = []
            while not q_events.empty():
                ev = q_events.get_nowait()
                if ev.get("type") == "admin_login":
                    login_events.append(ev.get("data", {}))

            self.assertEqual(len(login_events), 3)
            self.assertEqual(login_events[0]["user_id"], 101)
            self.assertEqual(login_events[0]["auth_method"], "OTP")
            self.assertEqual(login_events[1]["user_id"], 102)
            self.assertEqual(login_events[1]["auth_method"], "WebApp")

            # Check get_recent_admin_logins / get_admin_logins
            logins = await self.db.get_recent_admin_logins(limit=50)
            self.assertEqual(len(logins), 3)
            # Latest first (DESC)
            self.assertEqual(logins[0]["id"], id3)
            self.assertEqual(logins[0]["user_id"], 101)
            self.assertEqual(logins[0]["ip"], "192.168.1.10")
            self.assertEqual(logins[0]["user_agent"], "Mozilla/5.0 TestUA")
            self.assertEqual(logins[0]["auth_method"], "OTP")
            self.assertTrue(bool(logins[0]["created_at"]))

            self.assertEqual(logins[1]["id"], id2)
            self.assertEqual(logins[1]["user_id"], 102)
            self.assertEqual(logins[1]["auth_method"], "WebApp")

            # Check limit slicing
            single_login = await self.db.get_recent_admin_logins(limit=1)
            self.assertEqual(len(single_login), 1)
            self.assertEqual(single_login[0]["id"], id3)

            # Check alias get_admin_logins
            alias_logins = await self.db.get_admin_logins(limit=50)
            self.assertEqual(len(alias_logins), 3)
        finally:
            unsubscribe(q_events)

    # -------------------------------------------------------------
    # 2. get_recent_users(50)
    # -------------------------------------------------------------
    async def test_get_recent_users_limit_and_order(self):
        """get_recent_users returns latest registered users ordered by created_at DESC with full fields."""
        # Create 55 users
        for i in range(1, 56):
            await self.db.get_or_create_user(
                user_id=1000 + i,
                username=f"user_{i}",
                first_name=f"Player_{i}",
                default_lang="en"
            )

        users = await self.db.get_recent_users(limit=50)
        self.assertEqual(len(users), 50)

        # Verify fields
        required_fields = {
            "user_id", "username", "first_name", "language", "xp", "level",
            "total_score", "created_at"
        }
        for u in users:
            for field in required_fields:
                self.assertIn(field, u)

        # Ordering check: highest user_id / latest created_at should be first
        self.assertEqual(users[0]["user_id"], 1055)
        self.assertEqual(users[49]["user_id"], 1006)

    # -------------------------------------------------------------
    # 3. User Points, XP, Level, Stats Reset
    # -------------------------------------------------------------
    async def test_adjust_user_score_addition_and_deduction(self):
        """adjust_user_score adds/subtracts points, clamps at 0, and emits score_adjusted event."""
        user_id = 2001
        await self.db.get_or_create_user(user_id, username="score_tester", first_name="Score Tester")

        q_events = subscribe()
        try:
            # Add points
            score1 = await self.db.adjust_user_score(user_id, 100)
            self.assertEqual(score1, 100)

            user = await self.db.get_user(user_id)
            self.assertEqual(user["total_score"], 100)

            # Add more points
            score2 = await self.db.adjust_user_score(user_id, 50)
            self.assertEqual(score2, 150)

            # Deduct points
            score3 = await self.db.adjust_user_score(user_id, -70)
            self.assertEqual(score3, 80)

            # Deduct more than current balance -> clamped at 0
            score4 = await self.db.adjust_user_score(user_id, -200)
            self.assertEqual(score4, 0)

            # Verify score_adjusted events
            score_events = []
            while not q_events.empty():
                ev = q_events.get_nowait()
                if ev.get("type") == "score_adjusted":
                    score_events.append(ev.get("data", {}))
            self.assertEqual(len(score_events), 4)
            self.assertEqual(score_events[-1]["score"], 0)
        finally:
            unsubscribe(q_events)

    async def test_adjust_user_xp_and_level_recalculation(self):
        """adjust_user_xp sets total XP, updates level, and emits xp_adjusted event."""
        user_id = 2002
        await self.db.get_or_create_user(user_id, username="xp_tester", first_name="XP Tester")

        q_events = subscribe()
        try:
            # Set XP to 1000
            xp1 = await self.db.adjust_user_xp(user_id, 1000)
            self.assertEqual(xp1, 1000)

            user = await self.db.get_user(user_id)
            self.assertEqual(user["xp"], 1000)
            expected_level = self.db.calculate_level(1000)
            self.assertEqual(user["level"], expected_level)

            # Set negative XP -> clamped at 0, level 1
            xp2 = await self.db.adjust_user_xp(user_id, -50)
            self.assertEqual(xp2, 0)
            user_after = await self.db.get_user(user_id)
            self.assertEqual(user_after["xp"], 0)
            self.assertEqual(user_after["level"], 1)

            # Verify event bus
            xp_events = []
            while not q_events.empty():
                ev = q_events.get_nowait()
                if ev.get("type") == "xp_adjusted":
                    xp_events.append(ev.get("data", {}))
            self.assertEqual(len(xp_events), 2)
            self.assertEqual(xp_events[0]["xp"], 1000)
            self.assertEqual(xp_events[1]["xp"], 0)
        finally:
            unsubscribe(q_events)

    async def test_set_user_level_clamping(self):
        """set_user_level sets level directly, clamping at >= 1, and emits level_adjusted event."""
        user_id = 2003
        await self.db.get_or_create_user(user_id, username="lvl_tester", first_name="Level Tester")

        q_events = subscribe()
        try:
            lvl1 = await self.db.set_user_level(user_id, 7)
            self.assertEqual(lvl1, 7)
            user = await self.db.get_user(user_id)
            self.assertEqual(user["level"], 7)

            # Clamp to 1 on zero or negative input
            lvl2 = await self.db.set_user_level(user_id, 0)
            self.assertEqual(lvl2, 1)

            lvl3 = await self.db.set_user_level(user_id, -10)
            self.assertEqual(lvl3, 1)

            events = []
            while not q_events.empty():
                ev = q_events.get_nowait()
                if ev.get("type") == "level_adjusted":
                    events.append(ev.get("data", {}))
            self.assertEqual(len(events), 3)
            self.assertEqual(events[0]["level"], 7)
            self.assertEqual(events[1]["level"], 1)
        finally:
            unsubscribe(q_events)

    async def test_reset_user_stats_wipeout(self):
        """reset_user_stats wipes score, xp, answers, wins, streaks, group_scores, and sets level=1."""
        user_id = 2004
        await self.db.get_or_create_user(user_id, username="reset_tester", first_name="Reset Tester")
        await self.db.adjust_user_score(user_id, 650)
        await self.db.adjust_user_xp(user_id, 800)
        await self.db.set_user_level(user_id, 4)

        # Record group score & match stats
        await self.db.get_or_create_chat(-100999, "supergroup", "Test Chat", "en")
        await self.db.record_match_player_stats(user_id, -100999, "Reset Tester", is_win=True, score=250, xp_bonus=50)

        # Record answer logs
        await self.db.record_answer(
            user_id=user_id, is_correct=True, points=100, xp=25,
            user_name="Reset Tester", username="reset_tester", chat_id=-100999
        )

        q_events = subscribe()
        try:
            res = await self.db.reset_user_stats(user_id)
            self.assertTrue(res)

            user = await self.db.get_user(user_id)
            self.assertEqual(user["total_score"], 0)
            self.assertEqual(user["xp"], 0)
            self.assertEqual(user["level"], 1)
            self.assertEqual(user["games_played"], 0)
            self.assertEqual(user["games_won"], 0)
            self.assertEqual(user["correct_answers"], 0)
            self.assertEqual(user["total_answers"], 0)
            self.assertEqual(user["current_streak"], 0)
            self.assertEqual(user["best_streak"], 0)

            # Verify group_scores deleted
            async with self.db._connect() as conn:
                cursor = await conn.execute("SELECT COUNT(*) FROM group_scores WHERE user_id = ?", (user_id,))
                group_count = (await cursor.fetchone())[0]
            self.assertEqual(group_count, 0)

            # Verify stats_reset / user_stats_reset event emitted
            reset_event_found = False
            while not q_events.empty():
                ev = q_events.get_nowait()
                if ev.get("type") in ("stats_reset", "user_stats_reset") and ev.get("data", {}).get("user_id") == user_id:
                    reset_event_found = True
                    break
            self.assertTrue(reset_event_found)
        finally:
            unsubscribe(q_events)

    # -------------------------------------------------------------
    # 4. get_user_full_profile
    # -------------------------------------------------------------
    async def test_get_user_full_profile_stats_and_answers(self):
        """get_user_full_profile computes accurate stats (accuracy %, win rate %) and returns last answers."""
        # Non-existent user returns None
        self.assertIsNone(await self.db.get_user_full_profile(99999999))

        user_id = 2005
        await self.db.get_or_create_user(user_id, username="profile_tester", first_name="Profile Tester")

        # Zero answers initially -> accuracy 0.0, win rate 0.0
        prof_empty = await self.db.get_user_full_profile(user_id)
        self.assertIsNotNone(prof_empty)
        self.assertEqual(prof_empty["stats"]["accuracy"], 0.0)
        self.assertEqual(prof_empty["stats"]["win_rate"], 0.0)
        self.assertEqual(len(prof_empty["answers"]), 0)

        # Record 4 answers: 3 correct, 1 wrong -> accuracy = 75.0%
        for i in range(3):
            await self.db.record_answer(
                user_id=user_id, is_correct=True, points=100, xp=25,
                user_name="Profile Tester", username="profile_tester",
                mode="flag", question_id=f"Q_{i}", question_text=f"Flag {i}?",
                selected_option="Correct Country", correct_option="Correct Country"
            )
        await self.db.record_answer(
            user_id=user_id, is_correct=False, points=-20, xp=0,
            user_name="Profile Tester", username="profile_tester",
            mode="flag", question_id="Q_wrong", question_text="Flag Wrong?",
            selected_option="Wrong Country", correct_option="Target Country"
        )

        # Simulate 2 games played, 1 won -> win rate = 50.0%
        async with self.db._connect() as conn:
            await conn.execute("UPDATE users SET games_played = 2, games_won = 1 WHERE user_id = ?", (user_id,))
            await conn.commit()

        prof = await self.db.get_user_full_profile(user_id)
        self.assertIsNotNone(prof)
        self.assertEqual(prof["user_id"], user_id)
        self.assertEqual(prof["stats"]["total_answers"], 4)
        self.assertEqual(prof["stats"]["correct_answers"], 3)
        self.assertAlmostEqual(prof["stats"]["accuracy"], 75.0, delta=0.1)
        self.assertAlmostEqual(prof["accuracy"], 75.0, delta=0.1)
        self.assertAlmostEqual(prof["stats"]["win_rate"], 50.0, delta=0.1)
        self.assertAlmostEqual(prof["win_rate"], 50.0, delta=0.1)

        # Verify answers are populated and latest first
        answers = prof["answers"]
        self.assertEqual(len(answers), 4)
        self.assertEqual(answers[0]["question_id"], "Q_wrong")
        self.assertEqual(answers[0]["is_correct"], 0)
        self.assertEqual(answers[0]["selected_option"], "Wrong Country")
        self.assertEqual(answers[0]["user_answer"], "Wrong Country")
        self.assertEqual(answers[0]["correct_answer"], "Target Country")

    # -------------------------------------------------------------
    # 5. answer_logs Completeness & Display Name Sanitization
    # -------------------------------------------------------------
    def test_resolve_clean_user_name_edge_cases(self):
        """resolve_clean_user_name sanitizes names, preventing lone dots."""
        # Clean names stay intact
        self.assertEqual(resolve_clean_user_name(1001, "Alice", "alice"), "Alice")
        self.assertEqual(resolve_clean_user_name(1001, "Bob Traveller", "bob"), "Bob Traveller")

        # Lone dot with username -> falls back to @username
        self.assertEqual(resolve_clean_user_name(1001, ".", "alice_geo"), "@alice_geo")
        self.assertEqual(resolve_clean_user_name(1001, ".", "@alice_geo"), "@alice_geo")
        self.assertEqual(resolve_clean_user_name(1001, " . ", "alice_geo"), "@alice_geo")

        # Lone dot without username -> falls back to Player {user_id}
        self.assertEqual(resolve_clean_user_name(1001, ".", None), "Player 1001")
        self.assertEqual(resolve_clean_user_name(1001, ".", ""), "Player 1001")
        self.assertEqual(resolve_clean_user_name(1001, ".", "."), "Player 1001")

        # None / empty first_name
        self.assertEqual(resolve_clean_user_name(1001, None, "geostar"), "@geostar")
        self.assertEqual(resolve_clean_user_name(1001, "", None), "Player 1001")
        self.assertEqual(resolve_clean_user_name(1001, "   ", ""), "Player 1001")

        # format_user_mention helper
        mention1 = format_user_mention(1001, ".")
        self.assertIn("Player 1001", mention1)
        self.assertNotIn(">.<", mention1)

        mention2 = format_user_mention(1001, "Charlie")
        self.assertIn("Charlie", mention2)

    async def test_record_answer_and_record_answer_result_insert_into_answer_logs(self):
        """record_answer and record_answer_result always insert into answer_logs and emit clean display names."""
        q_events = subscribe()
        try:
            # User with dot first_name and username
            user_id = 3001
            await self.db.record_answer(
                user_id=user_id,
                is_correct=True,
                points=100,
                xp=25,
                user_name=".",
                username="dot_master",
                chat_id=-100222,
                mode="capital",
                question_id="JP",
                question_text="Capital of Japan?",
                selected_option="Tokyo",
                correct_option="Tokyo"
            )

            # Check answer_logs
            logs = await self.db.get_recent_answer_logs(user_id=user_id)
            self.assertEqual(len(logs), 1)
            self.assertEqual(logs[0]["selected_option"], "Tokyo")
            self.assertEqual(logs[0]["is_correct"], 1)

            # Check record_answer_result delegating to record_answer
            await self.db.record_answer_result(
                user_id=user_id,
                is_correct=False,
                points=-20,
                xp_earned=0,
                user_name=".",
                username="dot_master",
                chat_id=-100222,
                mode="capital",
                question_id="IT",
                question_text="Capital of Italy?",
                selected_option="Milan",
                correct_option="Rome"
            )

            logs_after = await self.db.get_recent_answer_logs(user_id=user_id)
            self.assertEqual(len(logs_after), 2)

            # Inspect EventBus events
            answer_events = []
            while not q_events.empty():
                ev = q_events.get_nowait()
                if ev.get("type") == "answer":
                    answer_events.append(ev.get("data", {}))

            self.assertGreaterEqual(len(answer_events), 2)
            # Display name must never be a lone dot
            for ev_data in answer_events:
                self.assertNotEqual(ev_data["user_name"], ".")
                self.assertIn(ev_data["user_name"], ("@dot_master", "dot_master", f"Player {user_id}"))
        finally:
            unsubscribe(q_events)

    async def test_session_check_answer_always_logs_and_sanitizes_dot_names(self):
        """games/session.py check_answer logs both correct and wrong answers to answer_logs with sanitized names."""
        session = GameSession(chat_id=-100888, mode=GameMode.CAPITAL, total_rounds=2)
        q = Question(
            text="What is the capital of France?",
            options=["Berlin", "Madrid", "Paris", "Rome"],
            correct_index=2,
            correct_answer="Paris",
            mode=GameMode.CAPITAL,
            country_code="FR"
        )
        session.current_question = q
        session.status = "in_progress"

        dot_user_id = 4001
        # 1. Wrong answer
        res_wrong, pts_wrong, _ = await session.check_answer(dot_user_id, ".", 0)
        self.assertEqual(res_wrong, "wrong")

        # 2. Correct answer from another user with lone dot
        dot_user_id2 = 4002
        res_corr, pts_corr, _ = await session.check_answer(dot_user_id2, " . ", 2)
        self.assertEqual(res_corr, "correct")
        self.assertGreater(pts_corr, 0)

        # Verify both answers are present in answer_logs
        logs_wrong = await self.db.get_recent_answer_logs(user_id=dot_user_id)
        self.assertEqual(len(logs_wrong), 1)
        self.assertEqual(logs_wrong[0]["is_correct"], 0)
        self.assertEqual(logs_wrong[0]["selected_option"], "Berlin")

        logs_corr = await self.db.get_recent_answer_logs(user_id=dot_user_id2)
        self.assertEqual(len(logs_corr), 1)
        self.assertEqual(logs_corr[0]["is_correct"], 1)
        self.assertEqual(logs_corr[0]["selected_option"], "Paris")

        # Verify session internal name storage cleaned up the lone dots
        self.assertEqual(session.user_names[dot_user_id], f"Player {dot_user_id}")
        self.assertEqual(session.user_names[dot_user_id2], f"Player {dot_user_id2}")


class TestAdminTelemetryAndUserMgmtAPI(AioHTTPTestCase):
    """Full HTTP API integration tests for all 8 Admin endpoints and security guards."""

    async def get_application(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "test_api_telemetry.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

        import database.db as db_mod
        db_mod._default_instance = self.db

        self.mock_bot = MagicMock()
        self.mock_bot.send_message = AsyncMock(return_value=MagicMock(message_id=201))
        self.mock_bot.send_photo = AsyncMock(return_value=MagicMock(message_id=202))

        from webapp.server import create_web_app
        app = create_web_app(db=self.db, bot=self.mock_bot)
        return app

    def setUp(self):
        super().setUp()
        reset_session_store()
        reset_ip_lockouts()

        self.admin_id = 99887766
        self.non_admin_id = 11223344
        config.ADMIN_IDS = [self.admin_id]

        self.admin_token = create_session_token(self.admin_id, extra_claims={"username": "rootadmin"})
        self.non_admin_token = create_session_token(self.non_admin_id, extra_claims={"username": "guest"})

        self.admin_headers = {"Authorization": f"Bearer {self.admin_token}"}
        self.non_admin_headers = {"Authorization": f"Bearer {self.non_admin_token}"}

    async def tearDownAsync(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    async def _seed_data(self):
        """Populate database with users and answer logs."""
        for i in range(1, 15):
            await self.db.get_or_create_user(
                user_id=5000 + i,
                username=f"user_{i}",
                first_name=f"Player_{i}",
                default_lang="en"
            )
            # Give points & XP
            await self.db.adjust_user_score(5000 + i, i * 50)
            await self.db.adjust_user_xp(5000 + i, i * 100)

        # Seed answer logs
        for i in range(1, 6):
            await self.db.record_answer_log(
                user_id=5001,
                username="user_1",
                chat_id=-100101,
                mode="flag",
                question_id=f"FR_{i}",
                question_text=f"Flag Question {i}",
                selected_option="France",
                correct_option="France",
                is_correct=1,
                points=100,
                time_taken=2.5
            )

    # -------------------------------------------------------------
    # Security Guards (401 Unauthorized & 403 Forbidden)
    # -------------------------------------------------------------
    @unittest_run_loop
    async def test_auth_guards_on_all_endpoints(self):
        """Verify all admin endpoints reject missing (401) or non-admin (403) tokens."""
        endpoints = [
            ("GET", "/api/admin/logins"),
            ("GET", "/api/admin/users/recent"),
            ("GET", "/api/admin/users/5001/full"),
            ("POST", "/api/admin/users/adjust-points"),
            ("POST", "/api/admin/users/set-level"),
            ("POST", "/api/admin/users/reset-stats"),
            ("GET", "/api/admin/answers/history"),
            ("GET", "/api/admin/live-stream"),
        ]

        for method, path in endpoints:
            # 1. Missing auth header -> 401
            if method == "GET":
                resp_no_auth = await self.client.get(path)
            else:
                resp_no_auth = await self.client.post(path, json={"user_id": 5001})
            self.assertEqual(
                resp_no_auth.status, 401,
                f"{method} {path} should return 401 when unauthenticated"
            )

            # 2. Non-admin token -> 403
            if method == "GET":
                resp_forbidden = await self.client.get(path, headers=self.non_admin_headers)
            else:
                resp_forbidden = await self.client.post(path, headers=self.non_admin_headers, json={"user_id": 5001})
            self.assertEqual(
                resp_forbidden.status, 403,
                f"{method} {path} should return 403 when authenticated as non-admin"
            )

    # -------------------------------------------------------------
    # 6. Admin API Endpoints
    # -------------------------------------------------------------
    @unittest_run_loop
    async def test_api_logins_endpoint(self):
        """GET /api/admin/logins returns recent admin logins."""
        await self.db.record_admin_login(self.admin_id, "rootadmin", "127.0.0.1", "TestClient/1.0", "OTP")
        await self.db.record_admin_login(self.admin_id, "rootadmin", "10.0.0.1", "TestClient/1.0", "WebApp")

        resp = await self.client.get("/api/admin/logins?limit=10", headers=self.admin_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        logins = data["logins"]
        self.assertEqual(len(logins), 2)
        self.assertEqual(logins[0]["auth_method"], "WebApp")
        self.assertEqual(logins[1]["auth_method"], "OTP")

    @unittest_run_loop
    async def test_api_users_recent_endpoint(self):
        """GET /api/admin/users/recent returns recently registered users."""
        await self._seed_data()
        resp = await self.client.get("/api/admin/users/recent?limit=10", headers=self.admin_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        users = data["users"]
        self.assertEqual(len(users), 10)
        # Latest first
        self.assertEqual(users[0]["user_id"], 5014)

    @unittest_run_loop
    async def test_api_user_full_profile_endpoint(self):
        """GET /api/admin/users/{user_id}/full returns complete profile, stats, and answers."""
        await self._seed_data()

        # Success case
        resp = await self.client.get("/api/admin/users/5001/full", headers=self.admin_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["user_id"], 5001)
        self.assertIn("stats", data)
        self.assertIn("answers", data)
        self.assertEqual(len(data["answers"]), 5)

        # 404 for unknown user
        resp_404 = await self.client.get("/api/admin/users/9999999/full", headers=self.admin_headers)
        self.assertEqual(resp_404.status, 404)

        # 400 for invalid user_id
        resp_400 = await self.client.get("/api/admin/users/invalid_id/full", headers=self.admin_headers)
        self.assertEqual(resp_400.status, 400)

    @unittest_run_loop
    async def test_api_user_adjust_points_endpoint(self):
        """POST /api/admin/users/adjust-points sets or adds user score/points."""
        await self._seed_data()

        # Direct set
        resp_set = await self.client.post(
            "/api/admin/users/adjust-points",
            headers=self.admin_headers,
            json={"user_id": 5001, "points": 500, "mode": "set"}
        )
        self.assertEqual(resp_set.status, 200)
        data_set = await resp_set.json()
        self.assertTrue(data_set["ok"])
        self.assertEqual(data_set["points"], 500)

        # Add delta
        resp_add = await self.client.post(
            "/api/admin/users/adjust-points",
            headers=self.admin_headers,
            json={"user_id": 5001, "points": 150, "mode": "add"}
        )
        self.assertEqual(resp_add.status, 200)
        data_add = await resp_add.json()
        self.assertEqual(data_add["points"], 650)

        # Deduct delta clamped at 0
        resp_deduct = await self.client.post(
            "/api/admin/users/adjust-points",
            headers=self.admin_headers,
            json={"user_id": 5001, "points": -1000, "mode": "add"}
        )
        self.assertEqual(resp_deduct.status, 200)
        data_deduct = await resp_deduct.json()
        self.assertEqual(data_deduct["points"], 0)

        # 400 on invalid payload
        resp_bad = await self.client.post(
            "/api/admin/users/adjust-points",
            headers=self.admin_headers,
            json={"user_id": "abc", "points": "xyz"}
        )
        self.assertEqual(resp_bad.status, 400)

    @unittest_run_loop
    async def test_api_user_set_level_endpoint(self):
        """POST /api/admin/users/set-level directly changes user level (>= 1)."""
        await self._seed_data()

        resp = await self.client.post(
            "/api/admin/users/set-level",
            headers=self.admin_headers,
            json={"user_id": 5001, "level": 12}
        )
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["level"], 12)

        # Clamped at 1
        resp_clamp = await self.client.post(
            "/api/admin/users/set-level",
            headers=self.admin_headers,
            json={"user_id": 5001, "level": -5}
        )
        self.assertEqual(resp_clamp.status, 200)
        data_clamp = await resp_clamp.json()
        self.assertEqual(data_clamp["level"], 1)

        # 400 on invalid payload
        resp_bad = await self.client.post(
            "/api/admin/users/set-level",
            headers=self.admin_headers,
            json={"user_id": 5001, "level": "not_an_int"}
        )
        self.assertEqual(resp_bad.status, 400)

    @unittest_run_loop
    async def test_api_user_reset_stats_endpoint(self):
        """POST /api/admin/users/reset-stats completely resets user stats."""
        await self._seed_data()

        resp = await self.client.post(
            "/api/admin/users/reset-stats",
            headers=self.admin_headers,
            json={"user_id": 5001}
        )
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])

        # Check DB
        user = await self.db.get_user(5001)
        self.assertEqual(user["total_score"], 0)
        self.assertEqual(user["xp"], 0)
        self.assertEqual(user["level"], 1)

        # 400 on invalid payload
        resp_bad = await self.client.post(
            "/api/admin/users/reset-stats",
            headers=self.admin_headers,
            json={"user_id": "not_valid"}
        )
        self.assertEqual(resp_bad.status, 400)

    @unittest_run_loop
    async def test_api_answers_history_endpoint(self):
        """GET /api/admin/answers/history returns logs and supports mode & query filters."""
        await self._seed_data()

        # Seed an additional capital question
        await self.db.record_answer_log(
            user_id=5002,
            username="user_2",
            chat_id=-100101,
            mode="capital",
            question_id="UZ_1",
            question_text="Capital of Uzbekistan?",
            selected_option="Tashkent",
            correct_option="Tashkent",
            is_correct=1,
            points=100,
            time_taken=1.8
        )

        # 1. Unfiltered
        resp = await self.client.get("/api/admin/answers/history?limit=50", headers=self.admin_headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertGreaterEqual(data["total"], 6)

        # 2. Mode filter
        resp_mode = await self.client.get("/api/admin/answers/history?mode=capital", headers=self.admin_headers)
        self.assertEqual(resp_mode.status, 200)
        data_mode = await resp_mode.json()
        self.assertEqual(data_mode["total"], 1)
        self.assertEqual(data_mode["answers"][0]["selected_option"], "Tashkent")

        # 3. Query search filter
        resp_q = await self.client.get("/api/admin/answers/history?query=Uzbekistan", headers=self.admin_headers)
        self.assertEqual(resp_q.status, 200)
        data_q = await resp_q.json()
        self.assertEqual(data_q["total"], 1)

    @unittest_run_loop
    async def test_live_stream_prepopulated_history(self):
        """GET /api/admin/live-stream sends initial event: connected and pre-populates history."""
        await self._seed_data()

        token_url = f"/api/admin/live-stream?token={self.admin_token}"
        resp = await self.client.get(token_url)
        self.assertEqual(resp.status, 200)
        self.assertEqual(resp.headers.get("Content-Type"), "text/event-stream")

        # Read initial chunk
        connected_chunk = await resp.content.read(128)
        self.assertIn(b"event: connected", connected_chunk)

        # Read stream until pre-populated answer events arrive
        received_answers = False
        deadline = time.time() + 4.0
        while time.time() < deadline:
            try:
                chunk = await asyncio.wait_for(resp.content.read(1024), timeout=1.0)
                if not chunk:
                    break
                if b"event: answer" in chunk and b"France" in chunk:
                    received_answers = True
                    break
            except asyncio.TimeoutError:
                break
        self.assertTrue(received_answers, "Pre-populated answers should be streamed via SSE")

        # Publish a live event and ensure it streams through
        event_bus.publish("user_stats_reset", {"user_id": 5001})
        received_live = False
        deadline = time.time() + 4.0
        while time.time() < deadline:
            try:
                chunk = await asyncio.wait_for(resp.content.read(1024), timeout=1.0)
                if not chunk:
                    break
                if b"event: user_stats_reset" in chunk:
                    received_live = True
                    break
            except asyncio.TimeoutError:
                break
        self.assertTrue(received_live, "Live event should be streamed via SSE")

    # -------------------------------------------------------------
    # Login Audit Generation on OTP and WebApp Auth Endpoints
    # -------------------------------------------------------------
    @unittest_run_loop
    async def test_otp_and_webapp_auth_creates_admin_login_audit(self):
        """Authentication on /api/admin/verify-otp and /api/admin/verify-webapp records audit entries."""
        # 1. OTP Auth
        otp = create_otp(self.admin_id)
        otp_payload = {"user_id": self.admin_id, "otp": otp}
        otp_headers = {"User-Agent": "AdminBrowser/2.0"}

        resp_otp = await self.client.post("/api/admin/verify-otp", json=otp_payload, headers=otp_headers)
        self.assertEqual(resp_otp.status, 200)
        data_otp = await resp_otp.json()
        self.assertTrue(data_otp["ok"])

        # Check DB audit record created
        logins = await self.db.get_recent_admin_logins(limit=10)
        self.assertGreaterEqual(len(logins), 1)
        self.assertEqual(logins[0]["user_id"], self.admin_id)
        self.assertEqual(logins[0]["auth_method"], "OTP")
        self.assertEqual(logins[0]["user_agent"], "AdminBrowser/2.0")

        # 2. WebApp Auth
        bot_token = config.BOT_TOKEN or "123456789:ABCdefGHIjklMNOpqrSTUvwxYZ_1234567"
        config.BOT_TOKEN = bot_token

        user_dict = {"id": self.admin_id, "first_name": "Root Admin", "username": "rootadmin"}
        params = {
            "auth_date": str(int(time.time())),
            "query_id": "AAG_TEST_AUDIT_LOG",
            "user": json.dumps(user_dict, separators=(",", ":")),
        }
        data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(params.items()))
        secret_key = hmac.new(b"WebAppData", bot_token.strip().encode("utf-8"), hashlib.sha256).digest()
        calc_hash = hmac.new(secret_key, data_check_string.encode("utf-8"), hashlib.sha256).hexdigest()
        params["hash"] = calc_hash
        init_data = urlencode(params)

        webapp_headers = {"User-Agent": "TelegramAdminClient/5.0"}
        resp_webapp = await self.client.post(
            "/api/admin/verify-webapp",
            json={"init_data": init_data},
            headers=webapp_headers
        )
        self.assertEqual(resp_webapp.status, 200)
        data_webapp = await resp_webapp.json()
        self.assertTrue(data_webapp["ok"])

        # Check DB audit record created for WebApp
        logins_after = await self.db.get_recent_admin_logins(limit=10)
        self.assertGreaterEqual(len(logins_after), 2)
        # Latest first
        self.assertEqual(logins_after[0]["user_id"], self.admin_id)
        self.assertEqual(logins_after[0]["auth_method"], "WebApp")
        self.assertEqual(logins_after[0]["user_agent"], "TelegramAdminClient/5.0")

        # Verify through GET /api/admin/logins endpoint as well
        resp_logins = await self.client.get("/api/admin/logins", headers=self.admin_headers)
        self.assertEqual(resp_logins.status, 200)
        api_logins_data = await resp_logins.json()
        self.assertGreaterEqual(len(api_logins_data["logins"]), 2)

    @unittest_run_loop
    async def test_admin_page_server_auth_gate(self):
        """GET /admin blocks unauthenticated users from receiving dashboard markup and serves login page."""
        # Unauthenticated: no cookies or headers
        resp_unauth = await self.client.get("/admin")
        self.assertEqual(resp_unauth.status, 200)
        html_unauth = await resp_unauth.text()
        self.assertIn("GeoGuru Admin", html_unauth)
        self.assertIn("Xavfsiz 2FA Autentifikatsiyasi", html_unauth)
        # Verify ZERO dashboard markup leaks
        self.assertNotIn("So'nggi 50 ta Yangi", html_unauth)
        self.assertNotIn("Ulangan Telegram Guruhlari", html_unauth)
        self.assertNotIn("Ommaviy Xabarnoma Yaratish", html_unauth)

        # Authenticated: with cookie
        self.client.session.cookie_jar.update_cookies({"admin_session": self.admin_token})
        resp_auth = await self.client.get("/admin")
        self.assertEqual(resp_auth.status, 200)
        html_auth = await resp_auth.text()
        self.assertIn("mainDashboard", html_auth)
        self.assertIn("So'nggi 50 ta Yangi", html_auth)


if __name__ == "__main__":
    unittest.main()
