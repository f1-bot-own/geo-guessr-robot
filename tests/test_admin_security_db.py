"""
Unit Tests for Admin Security, Database, and Event Foundation.
Covers:
- config.ADMIN_IDS, is_admin, ADMIN_JWT_SECRET, ADMIN_MASTER_PASSWORD
- database schema & db methods (answer_logs, stats, search, ban/unban, chat_list, difficult_questions)
- events pub/sub event_bus
- games/session.py answer logging, ban check, and event publishing
- webapp/admin_auth.py (OTP lifecycle, IP lockout, initData HMAC validation, JWT session token, require_admin)
"""

import asyncio
import os
import time
import json
import hmac
import hashlib
import unittest
from unittest.mock import MagicMock, AsyncMock
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop


import config
from database.db import (
    Database,
    SearchUsersResult,
    record_answer_log,
    get_admin_dashboard_stats,
    search_users,
    get_user_detail,
    ban_user,
    unban_user,
    is_user_banned,
    get_chat_list,
    get_recent_answer_logs,
    get_difficult_questions,
)
from events.bus import EventBus, event_bus, subscribe, unsubscribe, publish
import webapp.event_bus as webapp_eb
from webapp.admin_auth import (
    create_otp,
    verify_otp,
    record_login_attempt,
    is_ip_locked,
    validate_telegram_init_data,
    create_session_token,
    verify_session_token,
    require_admin,
    verify_master_password,
    _otp_store,
    _ip_lockouts,
)
from games.session import GameSession
from games.models import Question, GameMode


class TestConfigAndAdminHelpers(unittest.TestCase):
    def test_config_admin_settings(self):
        self.assertIsInstance(config.ADMIN_IDS, list)
        self.assertTrue(len(config.ADMIN_IDS) > 0)
        self.assertIn(12345678, config.ADMIN_IDS)
        self.assertTrue(config.is_admin(12345678))
        self.assertFalse(config.is_admin(999999999))
        self.assertFalse(config.is_admin(None))

        # Check JWT Secret and Master Password presence
        self.assertTrue(len(config.ADMIN_JWT_SECRET) > 0)
        self.assertIsInstance(config.ADMIN_MASTER_PASSWORD, str)


class TestEventBus(unittest.IsolatedAsyncioTestCase):
    async def test_pub_sub(self):
        bus = EventBus()
        q = bus.subscribe()
        self.assertIn(q, bus.subscribers)

        bus.publish("test_event", {"hello": "world"})
        self.assertFalse(q.empty())

        item = q.get_nowait()
        self.assertEqual(item["type"], "test_event")
        self.assertEqual(item["data"]["hello"], "world")

        bus.unsubscribe(q)
        self.assertNotIn(q, bus.subscribers)

    async def test_module_level_helpers_and_reexport(self):
        q = subscribe()
        publish("module_event", {"foo": "bar"})
        item = q.get_nowait()
        self.assertEqual(item["type"], "module_event")
        self.assertEqual(item["data"]["foo"], "bar")
        unsubscribe(q)

        # Check webapp.event_bus re-export
        self.assertEqual(webapp_eb.event_bus, event_bus)
        self.assertEqual(webapp_eb.publish, publish)


class TestDatabaseAdminAndLogs(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        import tempfile
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_admin.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.temp_dir.cleanup()

    async def test_ban_unban_user(self):
        user_id = 98765
        self.assertFalse(await self.db.is_user_banned(user_id))

        # Ban user
        success = await self.db.ban_user(user_id, reason="Spamming answers")
        self.assertTrue(success)
        self.assertTrue(await self.db.is_user_banned(user_id))

        # Check user details reflect ban
        detail = await self.db.get_user_detail(user_id)
        self.assertIsNotNone(detail)
        self.assertEqual(detail["is_banned"], 1)
        self.assertEqual(detail["ban_reason"], "Spamming answers")

        # Unban user
        self.assertTrue(await self.db.unban_user(user_id))
        self.assertFalse(await self.db.is_user_banned(user_id))

    async def test_answer_logs_and_stats(self):
        user1 = 1001
        user2 = 1002
        await self.db.get_or_create_user(user1, username="player_one", first_name="Alice")
        await self.db.get_or_create_user(user2, username="player_two", first_name="Bob")

        # Record answer logs
        log1 = await self.db.record_answer_log(
            user_id=user1,
            username="player_one",
            chat_id=-100111,
            mode="flag",
            question_id="FR",
            question_text="Guess the flag of France",
            selected_option="France",
            correct_option="France",
            is_correct=True,
            points=100,
            time_taken=2.5
        )
        self.assertIsInstance(log1, int)

        log2 = await self.db.record_answer_log(
            user_id=user2,
            username="player_two",
            chat_id=-100111,
            mode="flag",
            question_id="FR",
            question_text="Guess the flag of France",
            selected_option="Germany",
            correct_option="France",
            is_correct=False,
            points=-20,
            time_taken=5.0
        )
        self.assertIsInstance(log2, int)

        # Get recent answer logs
        recent = await self.db.get_recent_answer_logs(limit=10)
        self.assertEqual(len(recent), 2)
        self.assertEqual(recent[0]["user_id"], user2)  # DESC order
        self.assertEqual(recent[1]["user_id"], user1)

        # Filter by user_id
        user1_logs = await self.db.get_recent_answer_logs(user_id=user1)
        self.assertEqual(len(user1_logs), 1)
        self.assertEqual(user1_logs[0]["selected_option"], "France")

        # Dashboard stats
        stats = await self.db.get_admin_dashboard_stats()
        self.assertIn("total_users", stats)
        self.assertIn("new_users_today", stats)
        self.assertIn("total_answers", stats)
        self.assertIn("answers_today", stats)
        self.assertIn("correct_answers_today", stats)
        self.assertIn("accuracy_pct", stats)
        self.assertIn("banned_users", stats)
        self.assertIn("top_modes", stats)

        self.assertEqual(stats["total_answers"], 2)
        self.assertEqual(stats["answers_today"], 2)
        self.assertEqual(stats["correct_answers_today"], 1)
        self.assertEqual(stats["accuracy_pct"], 50.0)
        self.assertEqual(stats["banned_users"], 0)

        # Difficult questions
        diff = await self.db.get_difficult_questions(limit=10)
        self.assertEqual(len(diff), 1)
        self.assertEqual(diff[0]["question_id"], "FR")
        self.assertEqual(diff[0]["total_attempts"], 2)
        self.assertEqual(diff[0]["accuracy_pct"], 50.0)

    async def test_search_users_and_unpacking(self):
        await self.db.get_or_create_user(5001, username="alpha_user", first_name="Alexander")
        await self.db.get_or_create_user(5002, username="beta_user", first_name="Beatrice")

        # Search by username substring
        res = await self.db.search_users("alpha")
        self.assertEqual(res["total"], 1)
        self.assertEqual(len(res["users"]), 1)
        self.assertEqual(res["users"][0]["user_id"], 5001)

        # Test tuple unpacking capability: users, total = ...
        users, total = await self.db.search_users("beta")
        self.assertEqual(total, 1)
        self.assertEqual(users[0]["username"], "beta_user")

        # Search by user ID
        res_id = await self.db.search_users("5001")
        self.assertEqual(res_id["total"], 1)
        self.assertEqual(res_id["users"][0]["first_name"], "Alexander")

    async def test_get_chat_list(self):
        await self.db.get_or_create_chat(-100999, chat_type="supergroup", title="Geo Masters", default_lang="en")
        await self.db.increment_chat_games(-100999)

        chats = await self.db.get_chat_list(limit=10)
        self.assertTrue(len(chats) >= 1)
        matched = [c for c in chats if c["chat_id"] == -100999]
        self.assertEqual(len(matched), 1)
        self.assertEqual(matched[0]["title"], "Geo Masters")
        self.assertEqual(matched[0]["total_games"], 1)


class TestAdminAuth(unittest.TestCase):
    def setUp(self):
        _otp_store.clear()
        _ip_lockouts.clear()

    def test_otp_generation_and_verification(self):
        user_id = 777
        code = create_otp(user_id)
        self.assertEqual(len(code), 6)
        self.assertTrue(code.isdigit())

        # Wrong attempt 1
        self.assertFalse(verify_otp(user_id, "000000"))
        # Wrong attempt 2
        self.assertFalse(verify_otp(user_id, "111111"))
        # Correct attempt 3
        self.assertTrue(verify_otp(user_id, code))

        # OTP consumed, cannot re-verify
        self.assertFalse(verify_otp(user_id, code))

    def test_otp_max_attempts_lock(self):
        user_id = 888
        code = create_otp(user_id)
        self.assertFalse(verify_otp(user_id, "000000"))
        self.assertFalse(verify_otp(user_id, "000001"))
        self.assertFalse(verify_otp(user_id, "000002"))  # 3rd attempt fails and invalidates

        # Even with correct code now, it should fail
        self.assertFalse(verify_otp(user_id, code))

    def test_ip_lockout_rate_limiter(self):
        ip = "192.168.1.100"
        self.assertFalse(is_ip_locked(ip))

        for _ in range(4):
            record_login_attempt(ip, success=False)
            self.assertFalse(is_ip_locked(ip))

        # 5th failed attempt triggers lock
        record_login_attempt(ip, success=False)
        self.assertTrue(is_ip_locked(ip))

        # Successful attempt resets lock
        record_login_attempt(ip, success=True)
        self.assertFalse(is_ip_locked(ip))

    def test_telegram_init_data_validation(self):
        bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
        data_pairs = [
            ("auth_date", "1700000000"),
            ("query_id", "AAG_test_123"),
            ("user", json.dumps({"id": 12345678, "first_name": "AdminTester", "username": "admintest"}))
        ]
        # Build valid data_check_string according to spec
        sorted_pairs = sorted(data_pairs, key=lambda x: x[0])
        check_str = "\n".join(f"{k}={v}" for k, v in sorted_pairs)
        secret_key = hmac.new(b"WebAppData", bot_token.encode("utf-8"), hashlib.sha256).digest()
        valid_hash = hmac.new(secret_key, check_str.encode("utf-8"), hashlib.sha256).hexdigest()

        # Construct init_data query string
        init_data = f"auth_date=1700000000&hash={valid_hash}&query_id=AAG_test_123&user={json.dumps({'id': 12345678, 'first_name': 'AdminTester', 'username': 'admintest'})}"

        parsed = validate_telegram_init_data(init_data, bot_token)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed["user"]["id"], 12345678)

        # Tampered init_data must fail
        tampered = init_data.replace("1700000000", "1700000001")
        self.assertIsNone(validate_telegram_init_data(tampered, bot_token))

    def test_jwt_session_token_creation_and_verification(self):
        admin_id = 12345678
        token = create_session_token(admin_id, expires_in=3600, extra_claims={"role": "superadmin"})
        self.assertIsInstance(token, str)
        self.assertEqual(token.count("."), 2)

        # Verify token
        payload = verify_session_token(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload["user_id"], admin_id)
        self.assertEqual(payload["role"], "superadmin")

        # Tampered signature must fail
        tampered_token = token[:-4] + "xxxx"
        self.assertIsNone(verify_session_token(tampered_token))

        # Expired token must fail
        expired_token = create_session_token(admin_id, expires_in=-10)
        self.assertIsNone(verify_session_token(expired_token))



class TestRequireAdminDecorator(AioHTTPTestCase):
    async def get_application(self):
        app = web.Application()

        @require_admin
        async def protected_endpoint(request: web.Request):
            return web.json_response({"ok": True, "admin": request["admin_user"]})

        app.router.add_get("/admin/test", protected_endpoint)
        return app

    @unittest_run_loop
    async def test_no_token_unauthorized(self):
        resp = await self.client.get("/admin/test")
        self.assertEqual(resp.status, 401)
        data = await resp.json()
        self.assertFalse(data["ok"])

    @unittest_run_loop
    async def test_valid_admin_token_bearer_header(self):
        token = create_session_token(12345678)
        resp = await self.client.get("/admin/test", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["admin"]["user_id"], 12345678)

    @unittest_run_loop
    async def test_valid_admin_token_cookie(self):
        token = create_session_token(12345678)
        self.client.session.cookie_jar.update_cookies({"admin_session": token})
        resp = await self.client.get("/admin/test")
        self.assertEqual(resp.status, 200)

    @unittest_run_loop
    async def test_non_admin_token_forbidden(self):
        token = create_session_token(99999999)  # Not in ADMIN_IDS
        resp = await self.client.get("/admin/test", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(resp.status, 403)



class TestGameSessionIntegration(unittest.IsolatedAsyncioTestCase):
    async def test_banned_user_rejected_and_event_publishing(self):
        import tempfile
        from database.db import Database

        with tempfile.TemporaryDirectory() as tmp:
            test_db = Database(os.path.join(tmp, "session_test.db"))
            await test_db.init_db()

            # Temporarily configure default db to test_db
            import database.db as db_mod
            old_inst = db_mod._default_instance
            db_mod._default_instance = test_db

            try:
                # Ban user 666
                await test_db.ban_user(666, reason="Cheating")

                session = GameSession(chat_id=-100555, mode=GameMode.FLAG, total_rounds=3)
                q = Question(
                    text="Which country?",
                    options=["Italy", "France", "Spain", "Germany"],
                    correct_index=1,
                    correct_answer="France",
                    mode=GameMode.FLAG,
                    country_code="FR"
                )
                session.current_question = q

                session.status = "in_progress"

                # Banned user answers -> returned "banned"
                res_banned, pts_b, _ = await session.check_answer(666, "BannedPlayer", 1)
                self.assertEqual(res_banned, "banned")

                # Allowed user answers correctly
                q_events = subscribe()
                res_ok, pts_ok, _ = await session.check_answer(777, "ValidPlayer", 1)
                self.assertEqual(res_ok, "correct")
                self.assertTrue(pts_ok > 0)

                # Check answer was logged in answer_logs
                logs = await test_db.get_recent_answer_logs(user_id=777)
                self.assertEqual(len(logs), 1)
                self.assertEqual(logs[0]["is_correct"], 1)
                self.assertEqual(logs[0]["selected_option"], "France")

                # Check event was emitted
                event_found = False
                while not q_events.empty():
                    ev = q_events.get_nowait()
                    if ev["type"] == "answer_submitted" and ev["data"].get("user_id") == 777:
                        event_found = True
                        break
                self.assertTrue(event_found)
                unsubscribe(q_events)
            finally:
                db_mod._default_instance = old_inst


if __name__ == "__main__":
    unittest.main()
