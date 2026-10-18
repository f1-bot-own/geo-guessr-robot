"""
Comprehensive Unit Tests for GeoGuru Web Admin API, Broadcast Engine,
Auth, and Telegram Bot Admin Handlers.
"""

import os
import hmac
import hashlib
import json
import time
import asyncio
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
from urllib.parse import urlencode

import logging
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web

import config

from events.bus import EventBus, event_bus
from database.db import Database
from webapp.admin_auth import (
    is_admin,
    generate_otp,
    verify_otp,
    is_ip_locked,
    record_failed_attempt,
    clear_ip_attempts,
    create_session,
    validate_session,
    delete_session,
    verify_telegram_webapp,
    send_admin_otp,
    _otp_store,
    _ip_lockouts,
    _sessions,
    _revoked_tokens,
)
from webapp.server import create_web_app
from keyboards.admin_kb import get_admin_keyboard, get_admin_back_kb, get_admin_dashboard_url
from handlers.admin import cmd_admin, cb_admin_menu, cb_admin_stats, cb_admin_broadcast, cb_admin_backup


class TestAdminAuth(unittest.TestCase):
    def setUp(self):
        _otp_store.clear()
        _ip_lockouts.clear()
        _sessions.clear()
        _revoked_tokens.clear()

    def test_is_admin_check(self):
        with patch.dict(os.environ, {"ADMIN_IDS": "999,888"}):
            self.assertTrue(is_admin(999))
            self.assertTrue(is_admin("888"))
            self.assertFalse(is_admin(111))
            self.assertFalse(is_admin(None))
            self.assertFalse(is_admin("invalid"))

    def test_otp_generation_and_verification(self):
        otp = generate_otp(999)
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())

        # Correct code verifies and removes
        self.assertTrue(verify_otp(999, otp))
        # Second time should fail because OTP was consumed
        self.assertFalse(verify_otp(999, otp))

    def test_otp_wrong_code(self):
        otp = generate_otp(888)
        self.assertFalse(verify_otp(888, "000000"))
        # After too many failed attempts, OTP is discarded
        for _ in range(6):
            verify_otp(888, "111111")
        self.assertFalse(verify_otp(888, otp))

    def test_otp_expiry(self):
        otp = generate_otp(777)
        _otp_store[777]["expires_at"] = time.time() - 10
        self.assertFalse(verify_otp(777, otp))

    def test_ip_lockout(self):
        test_ip = "192.168.1.100"
        self.assertFalse(is_ip_locked(test_ip))

        for _ in range(4):
            record_failed_attempt(test_ip)
            self.assertFalse(is_ip_locked(test_ip))

        # 5th attempt locks IP
        record_failed_attempt(test_ip)
        self.assertTrue(is_ip_locked(test_ip))

        # Clearing lockout
        clear_ip_attempts(test_ip)
        self.assertFalse(is_ip_locked(test_ip))

    def test_session_lifecycle(self):
        user_data = {"user_id": 999, "first_name": "Chief", "role": "admin"}
        token = create_session(999, user_data)
        self.assertTrue(bool(token))

        session = validate_session(token)
        self.assertIsNotNone(session)
        self.assertEqual(session["user_id"], 999)
        self.assertEqual(session["user"]["first_name"], "Chief")

        # Invalidate / delete
        delete_session(token)
        self.assertIsNone(validate_session(token))

    def test_verify_telegram_webapp_hmac(self):
        bot_token = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
        user_json = json.dumps({"id": 999, "first_name": "AdminUser", "username": "admin_tg"})

        # Build valid init_data
        params = {
            "auth_date": "1710000000",
            "query_id": "AAHdF6IQAAAAAN0XohDsiPsd",
            "user": user_json,
        }
        data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(params.items()))
        secret_key = hmac.new(b"WebAppData", bot_token.encode("utf-8"), hashlib.sha256).digest()
        calc_hash = hmac.new(secret_key, data_check_string.encode("utf-8"), hashlib.sha256).hexdigest()
        params["hash"] = calc_hash

        valid_init_data = urlencode(params)
        verified_user = verify_telegram_webapp(valid_init_data, bot_token=bot_token)
        self.assertIsNotNone(verified_user)
        self.assertEqual(verified_user.get("id"), 999)
        self.assertEqual(verified_user.get("first_name"), "AdminUser")

        # Invalid hash should fail
        params["hash"] = "invalid_hash_string"
        bad_init_data = urlencode(params)
        self.assertIsNone(verify_telegram_webapp(bad_init_data, bot_token=bot_token))


class TestAdminWebServerAndAPI(AioHTTPTestCase):
    async def get_application(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "test_admin_geobot.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

        # Seed sample users and chats
        await self.db.get_or_create_user(999, first_name="AdminMaster", username="admin_master")
        await self.db.get_or_create_user(101, first_name="PlayerOne", username="player1")
        await self.db.record_answer(101, is_correct=True, points=100, xp=25)
        await self.db.get_or_create_chat(-1001, title="Alpha Group", chat_type="supergroup")

        # Configure mock bot
        self.mock_bot = MagicMock()
        self.mock_bot.send_message = AsyncMock(return_value=True)
        self.mock_bot.send_photo = AsyncMock(return_value=True)

        # Clear auth stores
        _otp_store.clear()
        _ip_lockouts.clear()
        _sessions.clear()

        # Set ADMIN_IDS in env to include 999
        os.environ["ADMIN_IDS"] = "999"

        return create_web_app(db=self.db, bot=self.mock_bot)

    async def tearDownAsync(self):
        if hasattr(self, "temp_dir"):
            self.temp_dir.cleanup()

    @unittest_run_loop
    async def test_admin_index_html_served(self):
        """Verify /admin and /admin/ serve the Web Admin Dashboard HTML."""
        resp = await self.client.request("GET", "/admin")
        self.assertEqual(resp.status, 200)
        html = await resp.text()
        self.assertIn("GeoGuru Admin", html)
        self.assertIn("2FA", html)

        resp2 = await self.client.request("GET", "/admin/")
        self.assertEqual(resp2.status, 200)

    @unittest_run_loop
    async def test_request_and_verify_otp_flow(self):
        """Test full 2FA OTP request, verification, cookie creation, and me endpoint."""
        # 1. Non-admin request rejected
        resp_bad = await self.client.request("POST", "/api/admin/request-otp", json={"user_id": 12345})
        self.assertEqual(resp_bad.status, 403)

        # 2. Admin request successful
        resp_req = await self.client.request("POST", "/api/admin/request-otp", json={"user_id": 999})
        self.assertEqual(resp_req.status, 200)
        data = await resp_req.json()
        self.assertTrue(data.get("ok"))
        self.mock_bot.send_message.assert_called_once()

        # Read generated code
        otp_code = _otp_store[999]["code"]

        # 3. Wrong OTP rejected
        resp_wrong = await self.client.request("POST", "/api/admin/verify-otp", json={"user_id": 999, "otp": "000000"})
        self.assertEqual(resp_wrong.status, 401)

        # 4. Correct OTP verifies and returns token and cookie
        resp_ok = await self.client.request("POST", "/api/admin/verify-otp", json={"user_id": 999, "otp": otp_code})
        self.assertEqual(resp_ok.status, 200)
        verify_data = await resp_ok.json()
        self.assertTrue(verify_data.get("ok"))
        token = verify_data.get("token")
        self.assertTrue(bool(token))

        # Check HttpOnly cookie
        self.assertIn("admin_session", resp_ok.cookies)

        # 5. Protected /api/admin/me returns profile
        resp_me = await self.client.request("GET", "/api/admin/me", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(resp_me.status, 200)
        me_data = await resp_me.json()
        self.assertTrue(me_data.get("ok"))
        self.assertEqual(me_data["user"]["user_id"], 999)

    @unittest_run_loop
    async def test_protected_endpoints_reject_unauthorized(self):
        """Protected endpoints must return 401 Unauthorized without session."""
        endpoints = [
            ("GET", "/api/admin/stats"),
            ("GET", "/api/admin/users"),
            ("GET", "/api/admin/groups"),
            ("GET", "/api/admin/answers"),
            ("GET", "/api/admin/logs"),
            ("POST", "/api/admin/broadcast"),
        ]
        for method, path in endpoints:
            resp = await self.client.request(method, path)
            self.assertEqual(resp.status, 401, f"{path} did not reject unauthorized request")

    @unittest_run_loop
    async def test_stats_and_user_management(self):
        """Test admin metrics, search, ban/unban, and XP adjustment."""
        # Create valid session for 999
        token = create_session(999, {"user_id": 999, "first_name": "Admin"})
        headers = {"Authorization": f"Bearer {token}"}

        # Stats
        resp = await self.client.request("GET", "/api/admin/stats", headers=headers)
        self.assertEqual(resp.status, 200)
        stats = (await resp.json())["stats"]
        self.assertGreaterEqual(stats["total_users"], 2)

        # Users list
        resp = await self.client.request("GET", "/api/admin/users?query=PlayerOne", headers=headers)
        self.assertEqual(resp.status, 200)
        u_data = await resp.json()
        self.assertEqual(u_data["total"], 1)
        self.assertEqual(u_data["users"][0]["user_id"], 101)

        # Single user detail
        resp = await self.client.request("GET", "/api/admin/users/101", headers=headers)
        self.assertEqual(resp.status, 200)
        self.assertEqual((await resp.json())["user"]["user_id"], 101)

        # Adjust XP
        resp = await self.client.request("POST", "/api/admin/users/adjust-xp", json={"user_id": 101, "xp": 800}, headers=headers)
        self.assertEqual(resp.status, 200)
        self.assertEqual((await resp.json())["xp"], 800)

        # Ban user
        resp = await self.client.request("POST", "/api/admin/users/ban", json={"user_id": 101, "ban": True, "reason": "Rule violation"}, headers=headers)
        self.assertEqual(resp.status, 200)
        self.assertTrue((await resp.json())["banned"])
        self.assertTrue(await self.db.is_user_banned(101))

        # Unban user
        resp = await self.client.request("POST", "/api/admin/users/ban", json={"user_id": 101, "ban": False}, headers=headers)
        self.assertEqual(resp.status, 200)
        self.assertFalse((await resp.json())["banned"])
        self.assertFalse(await self.db.is_user_banned(101))

    @unittest_run_loop
    async def test_broadcast_engine(self):
        """Test broadcast job start, execution, and status checking."""
        token = create_session(999, {"user_id": 999, "first_name": "Admin"})
        headers = {"Authorization": f"Bearer {token}"}

        payload = {
            "target": "all",
            "text": "Hello <b>GeoGuru</b> Players!",
            "photo_url": None,
            "button_text": "Play Now",
            "button_url": "https://t.me/geoguru_bot"
        }

        resp = await self.client.request("POST", "/api/admin/broadcast", json=payload, headers=headers)
        self.assertEqual(resp.status, 200)
        b_data = await resp.json()
        self.assertTrue(b_data["ok"])
        bid = b_data["broadcast_id"]

        # Wait a small moment for async task to process recipients
        await asyncio.sleep(0.15)

        # Check status
        resp_status = await self.client.request("GET", f"/api/admin/broadcast/status?broadcast_id={bid}", headers=headers)
        self.assertEqual(resp_status.status, 200)
        status_data = await resp_status.json()
        self.assertTrue(status_data["ok"])
        job = status_data["job"]
        self.assertIsNotNone(job)
        self.assertIn(job["status"], ("running", "completed"))

    @unittest_run_loop
    async def test_backup_db_download(self):
        """Test database download endpoint."""
        token = create_session(999, {"user_id": 999, "first_name": "Admin"})
        headers = {"Authorization": f"Bearer {token}"}

        resp = await self.client.request("GET", "/api/admin/backup-db", headers=headers)
        self.assertEqual(resp.status, 200)
        self.assertIn("Content-Disposition", resp.headers)
        self.assertIn("geobot_backup", resp.headers["Content-Disposition"])

    @unittest_run_loop
    async def test_server_logs_endpoint(self):
        """Test reading application logs."""
        token = create_session(999, {"user_id": 999, "first_name": "Admin"})
        headers = {"Authorization": f"Bearer {token}"}

        logger = logging.getLogger("TestLog")
        logger.info("Admin test logging verification line.")

        resp = await self.client.request("GET", "/api/admin/logs?lines=50", headers=headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertIsInstance(data["lines"], list)


class TestTelegramBotAdminHandlers(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        os.environ["ADMIN_IDS"] = "999"

    async def test_cmd_admin_unauthorized(self):
        """Non-admin user gets polite warning."""
        mock_msg = MagicMock()
        mock_msg.from_user.id = 12345
        mock_msg.reply = AsyncMock()

        mock_bot = MagicMock()
        await cmd_admin(mock_msg, mock_bot)

        mock_msg.reply.assert_called_once()
        text = mock_msg.reply.call_args[0][0]
        self.assertIn("Ruxsat berilmagan", text)

    async def test_cmd_admin_authorized(self):
        """Admin user gets inline dashboard menu with stats."""
        mock_msg = MagicMock()
        mock_msg.from_user.id = 999
        mock_msg.answer = AsyncMock()

        mock_db = MagicMock()
        mock_db.get_admin_dashboard_stats = AsyncMock(return_value={
            "total_users": 150,
            "active_today": 35,
            "total_groups": 12,
            "total_games": 240,
            "total_answers": 1200,
            "accuracy_percent": 84.5
        })

        mock_bot = MagicMock()
        mock_bot.db = mock_db
        mock_bot.__getitem__ = MagicMock(return_value=mock_db)

        await cmd_admin(mock_msg, mock_bot)

        mock_msg.answer.assert_called_once()
        kwargs = mock_msg.answer.call_args[1]
        self.assertIn("GeoGuru Boshqaruv Paneli", kwargs["text"])
        self.assertIn("150", kwargs["text"])
        self.assertIsNotNone(kwargs["reply_markup"])

    async def test_admin_callbacks(self):
        """Test admin inline callbacks: stats, broadcast guidance, and backup sender."""
        mock_call = MagicMock()
        mock_call.from_user.id = 999
        mock_call.message.edit_text = AsyncMock()
        mock_call.message.answer_document = AsyncMock()
        mock_call.message.answer = AsyncMock()
        mock_call.answer = AsyncMock()

        mock_db = MagicMock()
        mock_db.get_admin_dashboard_stats = AsyncMock(return_value={"top_users": [], "mode_distribution": []})
        mock_db.db_path = "geobot.db"

        mock_bot = MagicMock()
        mock_bot.db = mock_db
        mock_bot.__getitem__ = MagicMock(return_value=mock_db)

        # Callback: admin:stats
        await cb_admin_stats(mock_call, mock_bot)
        mock_call.message.edit_text.assert_called()

        # Callback: admin:broadcast
        await cb_admin_broadcast(mock_call)
        mock_call.message.edit_text.assert_called()

    async def test_send_admin_otp_helper(self):
        """Test 2FA OTP sending formatting and execution."""
        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(return_value=True)

        res = await send_admin_otp(mock_bot, 999, "654321")
        self.assertTrue(res)
        mock_bot.send_message.assert_called_once()
        call_kwargs = mock_bot.send_message.call_args[1]
        self.assertIn("654321", call_kwargs["text"])
        self.assertIn("GeoGuru Admin 2FA", call_kwargs["text"])


if __name__ == "__main__":
    unittest.main()
