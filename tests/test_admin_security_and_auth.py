"""
Security & Authentication Unit and Integration Tests for GeoGuru Web Admin Dashboard.

Verifies:
1. 2FA OTP generation (6-digit, 5-minute expiry, single-use, attempt limits).
2. Brute-force IP lockout (5 failed attempts -> 15-minute lock / 429 Too Many Requests).
3. Telegram WebApp HMAC-SHA256 signature verification (valid accepted, forged/tampered rejected).
4. Session tokens & JWT lifecycle (valid verified, expired rejected, tampered signature rejected, revoked rejected).
5. @require_admin route decorator (401 for unauthenticated, 403 for authenticated non-admin, 200 for admin).
"""

import os
import json
import time
import hmac
import hashlib
import unittest
from unittest.mock import patch
from urllib.parse import urlencode

from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

import config
from webapp.admin_auth import (
    is_admin,
    generate_otp,
    create_otp,
    verify_otp,
    is_ip_locked,
    record_failed_attempt,
    record_login_attempt,
    clear_ip_attempts,
    reset_ip_lockouts,
    reset_otp_store,
    reset_session_store,
    create_session,
    create_session_token,
    verify_session_token,
    validate_session,
    delete_session,
    verify_telegram_webapp,
    validate_telegram_init_data,
    require_admin,
    _otp_store,
    _ip_lockouts,
    _sessions,
    _revoked_tokens,
    OTP_EXPIRY_SECONDS,
    MAX_FAILED_ATTEMPTS,
    LOCKOUT_DURATION_SECONDS,
)


class TestAdminOTP(unittest.TestCase):
    """Test 2FA OTP creation, entropy, expiration, and one-time use."""

    def setUp(self):
        reset_otp_store()

    def test_otp_format_and_entropy(self):
        """OTP must be a 6-digit numeric string between 100000 and 999999."""
        codes = set()
        for i in range(10):
            code = create_otp(1000 + i)
            self.assertEqual(len(code), 6)
            self.assertTrue(code.isdigit())
            val = int(code)
            self.assertGreaterEqual(val, 100000)
            self.assertLessEqual(val, 999999)
            codes.add(code)
        # Verify codes have entropy
        self.assertGreater(len(codes), 5)

    def test_generate_otp_alias(self):
        """generate_otp and create_otp are interchangeable."""
        code1 = generate_otp(2001)
        self.assertEqual(len(code1), 6)
        self.assertTrue(verify_otp(2001, code1))

    def test_otp_one_time_use(self):
        """Once verified successfully, the OTP cannot be reused."""
        user_id = 3001
        code = create_otp(user_id)
        # First verification succeeds
        self.assertTrue(verify_otp(user_id, code))
        # Second verification with same code fails immediately
        self.assertFalse(verify_otp(user_id, code))

    def test_otp_wrong_code(self):
        """Submitting incorrect OTP returns False."""
        user_id = 4001
        code = create_otp(user_id)
        wrong_code = "000000" if code != "000000" else "111111"
        self.assertFalse(verify_otp(user_id, wrong_code))

    def test_otp_expiration(self):
        """OTP expires after 5 minutes (300 seconds)."""
        user_id = 5001
        code = create_otp(user_id)
        # Advance clock past OTP_EXPIRY_SECONDS (301s)
        future_time = time.time() + OTP_EXPIRY_SECONDS + 5
        with patch("time.time", return_value=future_time):
            self.assertFalse(verify_otp(user_id, code))

    def test_otp_max_attempt_lockout(self):
        """OTP is invalidated after 3 failed verification attempts."""
        user_id = 6001
        code = create_otp(user_id)
        self.assertFalse(verify_otp(user_id, "999991"))
        self.assertFalse(verify_otp(user_id, "999992"))
        self.assertFalse(verify_otp(user_id, "999993"))  # 3rd failure
        # Even if submitted correctly now, it was purged
        self.assertFalse(verify_otp(user_id, code))


class TestBruteForceIPLockout(unittest.TestCase):
    """Test brute-force attack prevention, IP lockout duration, and reset."""

    def setUp(self):
        reset_ip_lockouts()

    def test_ip_lockout_threshold(self):
        """IP should lock out only on the 5th failed attempt."""
        ip = "198.51.100.42"
        self.assertFalse(is_ip_locked(ip))

        # 4 consecutive failures -> not locked yet
        for i in range(MAX_FAILED_ATTEMPTS - 1):
            record_failed_attempt(ip)
            self.assertFalse(is_ip_locked(ip), f"IP should not be locked at attempt {i+1}")

        # 5th failure -> locked
        record_failed_attempt(ip)
        self.assertTrue(is_ip_locked(ip))

    def test_record_login_attempt_alias(self):
        """record_login_attempt(ip, success=False) functions identically."""
        ip = "198.51.100.43"
        for _ in range(5):
            record_login_attempt(ip, success=False)
        self.assertTrue(is_ip_locked(ip))

    def test_ip_lockout_auto_expires_after_15_minutes(self):
        """Lockout expires automatically after 15 minutes (900 seconds)."""
        ip = "198.51.100.44"
        now = time.time()
        for _ in range(MAX_FAILED_ATTEMPTS):
            record_failed_attempt(ip)
        self.assertTrue(is_ip_locked(ip))

        # Check after 14 minutes -> still locked
        with patch("time.time", return_value=now + 840):
            self.assertTrue(is_ip_locked(ip))

        # Check after 15 minutes and 5 seconds -> unlocked and cleared
        with patch("time.time", return_value=now + LOCKOUT_DURATION_SECONDS + 5):
            self.assertFalse(is_ip_locked(ip))
            # Cache is cleared
            self.assertNotIn(ip, _ip_lockouts)

    def test_successful_auth_clears_attempts(self):
        """Successful authentication immediately clears failed attempt count."""
        ip = "198.51.100.45"
        for _ in range(MAX_FAILED_ATTEMPTS - 1):
            record_failed_attempt(ip)
        self.assertFalse(is_ip_locked(ip))

        # Successful login resets
        clear_ip_attempts(ip)
        self.assertNotIn(ip, _ip_lockouts)

        # Further 4 failures still do not lock
        for _ in range(MAX_FAILED_ATTEMPTS - 1):
            record_failed_attempt(ip)
        self.assertFalse(is_ip_locked(ip))


class TestTelegramWebAppHMAC(unittest.TestCase):
    """Test validation of Telegram Mini App initData HMAC-SHA256 signatures."""

    def setUp(self):
        self.bot_token = "123456789:ABCdefGHIjklMNOpqrSTUvwxYZ_1234567"

    def _generate_valid_init_data(self, user_dict, bot_token=None):
        token = bot_token or self.bot_token
        params = {
            "auth_date": str(int(time.time())),
            "query_id": "AAG_TEST_INIT_DATA_12345",
            "user": json.dumps(user_dict, separators=(",", ":")),
        }
        data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(params.items()))
        secret_key = hmac.new(b"WebAppData", token.strip().encode("utf-8"), hashlib.sha256).digest()
        calc_hash = hmac.new(secret_key, data_check_string.encode("utf-8"), hashlib.sha256).hexdigest()
        params["hash"] = calc_hash
        return urlencode(params)

    def test_valid_signature_accepted(self):
        """Valid initData signature passes and returns parsed user."""
        user = {"id": 12345678, "first_name": "TestAdmin", "username": "admin_bot"}
        init_data = self._generate_valid_init_data(user)

        parsed = verify_telegram_webapp(init_data, bot_token=self.bot_token)
        self.assertIsNotNone(parsed)
        # Should support both user sub-dict and top-level unpacked keys
        self.assertEqual(parsed.get("id"), 12345678)
        self.assertEqual(parsed.get("first_name"), "TestAdmin")
        self.assertEqual(parsed["user"]["id"], 12345678)

    def test_tampered_hash_rejected(self):
        """Altering the HMAC hash causes verification to fail."""
        user = {"id": 12345678, "first_name": "TestAdmin"}
        init_data = self._generate_valid_init_data(user)
        # Tamper the hash parameter
        tampered_data = init_data.replace("hash=", "hash=deadbeef0000")
        self.assertIsNone(verify_telegram_webapp(tampered_data, bot_token=self.bot_token))

    def test_tampered_payload_rejected(self):
        """Modifying the user payload without recalculating hash fails."""
        user = {"id": 12345678, "first_name": "TestAdmin"}
        init_data = self._generate_valid_init_data(user)
        # Tamper the user id inside init_data
        tampered_data = init_data.replace("12345678", "99999999")
        self.assertIsNone(verify_telegram_webapp(tampered_data, bot_token=self.bot_token))

    def test_wrong_bot_token_rejected(self):
        """Valid data checked against different bot token fails."""
        user = {"id": 12345678, "first_name": "TestAdmin"}
        init_data = self._generate_valid_init_data(user, bot_token="999999:OTHER_BOT_TOKEN_AAA")
        self.assertIsNone(verify_telegram_webapp(init_data, bot_token=self.bot_token))

    def test_empty_or_malformed_init_data(self):
        """Empty string or data without hash returns None."""
        self.assertIsNone(verify_telegram_webapp("", bot_token=self.bot_token))
        self.assertIsNone(verify_telegram_webapp(None, bot_token=self.bot_token))
        self.assertIsNone(verify_telegram_webapp("auth_date=1234&user=test", bot_token=self.bot_token))


class TestAdminSessionTokens(unittest.TestCase):
    """Test cryptographic JWT session creation, validation, expiration, and tampering."""

    def setUp(self):
        reset_session_store()

    def test_valid_token_lifecycle(self):
        """Session token is created, verified, and retrieves admin claims."""
        token = create_session_token(12345678, extra_claims={"role": "superadmin", "name": "Alice"})
        self.assertIsNotNone(token)
        self.assertIn(".", token)

        payload = verify_session_token(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload["user_id"], 12345678)
        self.assertEqual(payload.get("role"), "superadmin")
        self.assertEqual(payload.get("name"), "Alice")

        # Also validate via validate_session
        session = validate_session(token)
        self.assertIsNotNone(session)
        self.assertEqual(session["user_id"], 12345678)

    def test_expired_token_rejected(self):
        """Expired session token is rejected and returns None."""
        # Create token that expired 10 seconds ago
        token = create_session_token(12345678, expires_in=-10)
        self.assertIsNone(verify_session_token(token))
        self.assertIsNone(validate_session(token))

    def test_tampered_token_signature_rejected(self):
        """Modifying signature characters causes HMAC verification to fail."""
        token = create_session_token(12345678)
        parts = token.split(".")
        # Tamper signature part
        tampered_sig = ("A" if parts[2][0] != "A" else "B") + parts[2][1:]
        tampered_token = f"{parts[0]}.{parts[1]}.{tampered_sig}"

        self.assertIsNone(verify_session_token(tampered_token))
        self.assertIsNone(validate_session(tampered_token))

    def test_tampered_token_payload_rejected(self):
        """Modifying claims in payload causes signature mismatch."""
        token = create_session_token(12345678)
        parts = token.split(".")
        # Tamper payload part
        tampered_payload = ("X" if parts[1][0] != "X" else "Y") + parts[1][1:]
        tampered_token = f"{parts[0]}.{tampered_payload}.{parts[2]}"

        self.assertIsNone(verify_session_token(tampered_token))
        self.assertIsNone(validate_session(tampered_token))

    def test_delete_session_revokes_token(self):
        """Deleting session invalidates the token even before expiration."""
        token = create_session_token(12345678)
        self.assertIsNotNone(verify_session_token(token))

        delete_session(token)
        self.assertIsNone(verify_session_token(token))
        self.assertIsNone(validate_session(token))


class TestRequireAdminDecorator(AioHTTPTestCase):
    """
    Integration tests for @require_admin route decorator.
    Verifies 401 for unauthenticated, 403 for non-admin, and 200 for authorized admin.
    """

    async def get_application(self):
        app = web.Application()

        @require_admin
        async def protected_endpoint(request: web.Request) -> web.Response:
            admin_user = request.get("admin_user", {})
            return web.json_response({
                "ok": True,
                "message": "Welcome admin",
                "admin_id": request.get("admin_user_id"),
                "user": admin_user
            })

        app.router.add_get("/api/test-protected", protected_endpoint)
        app.router.add_post("/api/test-protected", protected_endpoint)
        return app

    def setUp(self):
        super().setUp()
        reset_session_store()
        reset_ip_lockouts()
        # Set config admin IDs
        self.admin_id = 12345678
        self.non_admin_id = 99999999
        config.ADMIN_IDS = [self.admin_id]

    @unittest_run_loop
    async def test_unauthenticated_request_returns_401(self):
        """Request without token returns 401 Unauthorized."""
        resp = await self.client.get("/api/test-protected")
        self.assertEqual(resp.status, 401)
        data = await resp.json()
        self.assertFalse(data["ok"])
        self.assertIn("Unauthorized", data["error"])

    @unittest_run_loop
    async def test_invalid_token_returns_401(self):
        """Request with corrupted or forged token returns 401 Unauthorized."""
        headers = {"Authorization": "Bearer completely-forged-invalid-token"}
        resp = await self.client.get("/api/test-protected", headers=headers)
        self.assertEqual(resp.status, 401)
        data = await resp.json()
        self.assertFalse(data["ok"])

    @unittest_run_loop
    async def test_expired_token_returns_401(self):
        """Request with expired token returns 401 Unauthorized."""
        expired_token = create_session_token(self.admin_id, expires_in=-10)
        headers = {"Authorization": f"Bearer {expired_token}"}
        resp = await self.client.get("/api/test-protected", headers=headers)
        self.assertEqual(resp.status, 401)

    @unittest_run_loop
    async def test_authenticated_non_admin_returns_403(self):
        """Request with valid token of NON-ADMIN user returns 403 Forbidden."""
        non_admin_token = create_session_token(self.non_admin_id, extra_claims={"role": "player"})
        headers = {"Authorization": f"Bearer {non_admin_token}"}
        resp = await self.client.get("/api/test-protected", headers=headers)
        self.assertEqual(resp.status, 403)
        data = await resp.json()
        self.assertFalse(data["ok"])
        self.assertIn("Forbidden", data["error"])

    @unittest_run_loop
    async def test_valid_admin_bearer_header_returns_200(self):
        """Authorized admin with Bearer token passes and gets 200 OK."""
        token = create_session_token(self.admin_id, extra_claims={"username": "superadmin"})
        headers = {"Authorization": f"Bearer {token}"}
        resp = await self.client.get("/api/test-protected", headers=headers)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["admin_id"], self.admin_id)

    @unittest_run_loop
    async def test_valid_admin_cookie_returns_200(self):
        """Authorized admin with HttpOnly cookie passes and gets 200 OK."""
        token = create_session_token(self.admin_id)
        self.client.session.cookie_jar.update_cookies({"admin_session": token})
        resp = await self.client.get("/api/test-protected")
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])

    @unittest_run_loop
    async def test_valid_admin_query_param_returns_200(self):
        """Authorized admin with ?token= query parameter passes (e.g. for SSE stream)."""
        token = create_session_token(self.admin_id)
        resp = await self.client.get(f"/api/test-protected?token={token}")
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data["ok"])


if __name__ == "__main__":
    unittest.main()
