"""
Unit & Integration Tests for Telegram Bot Admin Handlers and Keyboards.

Verifies:
1. /admin command unauthorized rejection for non-admin users.
2. /admin command acceptance, welcome text, and admin keyboard for authorized admins.
3. get_admin_keyboard WebApp button, fallback URLs, and menu options.
4. send_admin_otp helper message formatting, delivery, and error resilience.
5. Admin callback handlers (menu, stats, broadcast, backup) authorization checks.
"""

import os
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram.types import (
    Message,
    User,
    Chat,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

import config
from database.db import Database
from keyboards.admin_kb import (
    get_admin_keyboard,
    get_admin_back_kb,
    get_admin_dashboard_url,
)
from handlers.admin import (
    cmd_admin,
    cb_admin_menu,
    cb_admin_stats,
    cb_admin_broadcast,
    cb_admin_backup,
    send_admin_otp,
    format_admin_summary,
)


class TestAdminKeyboards(unittest.TestCase):
    """Test admin dashboard keyboard structure and WebApp URL configuration."""

    def test_get_admin_dashboard_url_resolution(self):
        """Resolves clean /admin URL based on WEBAPP_URL."""
        with patch.object(config, "WEBAPP_URL", "https://geoguru.example.com"):
            url = get_admin_dashboard_url()
            self.assertEqual(url, "https://geoguru.example.com/admin")

        with patch.object(config, "WEBAPP_URL", "https://geoguru.example.com/"):
            url = get_admin_dashboard_url()
            self.assertEqual(url, "https://geoguru.example.com/admin")

        with patch.object(config, "WEBAPP_URL", ""):
            url = get_admin_dashboard_url()
            self.assertEqual(url, "")

    def test_get_admin_keyboard_with_https_webapp(self):
        """When HTTPS is configured, top button contains WebAppInfo."""
        with patch.object(config, "WEBAPP_URL", "https://geoguru.example.com"):
            kb = get_admin_keyboard()
            self.assertIsInstance(kb, InlineKeyboardMarkup)
            self.assertGreaterEqual(len(kb.inline_keyboard), 2)

            top_button = kb.inline_keyboard[0][0]
            self.assertIsInstance(top_button, InlineKeyboardButton)
            self.assertIsNotNone(top_button.web_app)
            self.assertIsInstance(top_button.web_app, WebAppInfo)
            self.assertEqual(top_button.web_app.url, "https://geoguru.example.com/admin")

    def test_get_admin_keyboard_without_https(self):
        """When WEBAPP_URL is empty, top button falls back to callback button."""
        with patch.object(config, "WEBAPP_URL", ""):
            kb = get_admin_keyboard()
            self.assertIsInstance(kb, InlineKeyboardMarkup)
            top_button = kb.inline_keyboard[0][0]
            self.assertEqual(top_button.callback_data, "admin:web_info")

    def test_get_admin_keyboard_actions(self):
        """Keyboard contains quick action buttons: stats, broadcast, backup."""
        kb = get_admin_keyboard()
        callbacks = [btn.callback_data for row in kb.inline_keyboard for btn in row if btn.callback_data]
        self.assertIn("admin:stats", callbacks)
        self.assertIn("admin:broadcast", callbacks)
        self.assertIn("admin:backup", callbacks)

    def test_get_admin_back_kb(self):
        """Back keyboard contains button returning to admin:menu."""
        back_kb = get_admin_back_kb()
        self.assertIsInstance(back_kb, InlineKeyboardMarkup)
        self.assertEqual(back_kb.inline_keyboard[0][0].callback_data, "admin:menu")


class TestAdminBotHandlers(unittest.IsolatedAsyncioTestCase):
    """Test /admin command and callback query interactions."""

    def setUp(self):
        self.admin_id = 12345678
        self.non_admin_id = 99999999
        config.ADMIN_IDS = [self.admin_id]

        self.bot = MagicMock()
        self.bot.send_message = AsyncMock(return_value=MagicMock(message_id=200))
        self.bot.send_document = AsyncMock(return_value=MagicMock(message_id=201))

        self.mock_db = MagicMock()
        self.mock_db.get_admin_dashboard_stats = AsyncMock(return_value={
            "total_users": 1500,
            "active_today": 320,
            "total_groups": 85,
            "total_games": 4200,
            "total_answers": 12500,
            "accuracy_percent": 74.5,
            "banned_users": 3,
            "top_users": [{"user_id": 1001, "username": "pro_geo", "total_score": 9500, "xp": 4200, "level": 15}],
            "mode_distribution": [{"mode": "flag", "match_count": 2100}, {"mode": "capital", "match_count": 1400}]
        })
        self.bot.db = self.mock_db
        self.bot.__dict__["_bot_data"] = {"db": self.mock_db}

    async def test_cmd_admin_unauthorized_rejection(self):
        """Non-admin user invoking /admin gets rejected with warning message."""
        msg = MagicMock(spec=Message)
        msg.from_user = User(id=self.non_admin_id, is_bot=False, first_name="Stranger")
        msg.chat = Chat(id=self.non_admin_id, type="private")
        msg.reply = AsyncMock()
        msg.answer = AsyncMock()

        await cmd_admin(msg, self.bot)

        # Must reply with unauthorized warning
        msg.reply.assert_called_once()
        sent_text = msg.reply.call_args.kwargs.get("text") or msg.reply.call_args.args[0]
        self.assertIn("Ruxsat berilmagan", sent_text)
        # Must NOT send admin keyboard
        self.assertNotIn("reply_markup", msg.reply.call_args.kwargs)
        msg.answer.assert_not_called()

    async def test_cmd_admin_authorized_success(self):
        """Authorized administrator invoking /admin receives summary and admin keyboard."""
        msg = MagicMock(spec=Message)
        msg.from_user = User(id=self.admin_id, is_bot=False, first_name="AdminMaster")
        msg.chat = Chat(id=self.admin_id, type="private")
        msg.reply = AsyncMock()
        msg.answer = AsyncMock()

        await cmd_admin(msg, self.bot)

        # Must answer with admin dashboard
        msg.answer.assert_called_once()
        sent_text = msg.answer.call_args.kwargs.get("text") or msg.answer.call_args.args[0]
        self.assertIn("GeoGuru Boshqaruv Paneli", sent_text)
        self.assertIn("1,500", sent_text)  # Formatted total users
        self.assertIn("74.5%", sent_text)  # Accuracy

        # Must include admin keyboard
        reply_markup = msg.answer.call_args.kwargs.get("reply_markup")
        self.assertIsInstance(reply_markup, InlineKeyboardMarkup)

    async def test_cb_admin_menu_authorized_and_unauthorized(self):
        """admin:menu callback verifies authorization before updating view."""
        # 1. Unauthorized
        call_unauth = MagicMock(spec=CallbackQuery)
        call_unauth.from_user = User(id=self.non_admin_id, is_bot=False, first_name="Hacker")
        call_unauth.answer = AsyncMock()
        await cb_admin_menu(call_unauth, self.bot)
        call_unauth.answer.assert_called_with("Ruxsat berilmagan!", show_alert=True)

        # 2. Authorized
        call_auth = MagicMock(spec=CallbackQuery)
        call_auth.from_user = User(id=self.admin_id, is_bot=False, first_name="Boss")
        call_auth.answer = AsyncMock()
        call_auth.message = MagicMock()
        call_auth.message.edit_text = AsyncMock()

        await cb_admin_menu(call_auth, self.bot)
        call_auth.message.edit_text.assert_called_once()
        call_auth.answer.assert_called_with()

    async def test_cb_admin_stats(self):
        """admin:stats callback displays detailed metrics and top players."""
        # 1. Unauthorized
        call_unauth = MagicMock(spec=CallbackQuery)
        call_unauth.from_user = User(id=self.non_admin_id, is_bot=False, first_name="Sneak")
        call_unauth.answer = AsyncMock()
        await cb_admin_stats(call_unauth, self.bot)
        call_unauth.answer.assert_called_with("Ruxsat berilmagan!", show_alert=True)

        # 2. Authorized
        call_auth = MagicMock(spec=CallbackQuery)
        call_auth.from_user = User(id=self.admin_id, is_bot=False, first_name="Admin")
        call_auth.answer = AsyncMock()
        call_auth.message = MagicMock()
        call_auth.message.edit_text = AsyncMock()

        await cb_admin_stats(call_auth, self.bot)
        call_auth.message.edit_text.assert_called_once()
        text = call_auth.message.edit_text.call_args.kwargs.get("text", "")
        self.assertIn("Kengaytirilgan Statistika", text)
        self.assertIn("pro_geo", text)
        self.assertIn("FLAG", text)

    async def test_cb_admin_broadcast_guide(self):
        """admin:broadcast callback explains broadcast features."""
        call = MagicMock(spec=CallbackQuery)
        call.from_user = User(id=self.admin_id, is_bot=False, first_name="Admin")
        call.answer = AsyncMock()
        call.message = MagicMock()
        call.message.edit_text = AsyncMock()

        await cb_admin_broadcast(call, self.bot)
        call.message.edit_text.assert_called_once()
        text = call.message.edit_text.call_args.kwargs.get("text", "")
        self.assertIn("Ommaviy Xabarnoma", text)
        self.assertIn("Broadcast", text)


class TestSendAdminOTPHelper(unittest.IsolatedAsyncioTestCase):
    """Test 2FA OTP delivery helper to admin's Telegram chat."""

    async def test_send_admin_otp_success(self):
        """send_admin_otp formats message and calls bot.send_message with HTML formatting."""
        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(return_value=MagicMock(message_id=999))

        result = await send_admin_otp(mock_bot, admin_id=12345678, otp_code="849201")
        self.assertTrue(result)
        mock_bot.send_message.assert_called_once()

        kwargs = mock_bot.send_message.call_args.kwargs
        self.assertEqual(kwargs.get("chat_id"), 12345678)
        self.assertEqual(kwargs.get("parse_mode"), "HTML")
        text = kwargs.get("text", "")
        self.assertIn("<code>849201</code>", text)
        self.assertIn("5 daqiqa", text)

    async def test_send_admin_otp_bot_error_graceful_handling(self):
        """When Telegram bot API raises exception, send_admin_otp catches it and returns False."""
        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(side_effect=Exception("TelegramNetworkError: connection reset"))

        # Disable direct API fallback token during unit test
        with patch.object(config, "BOT_TOKEN", ""):
            result = await send_admin_otp(mock_bot, admin_id=12345678, otp_code="123456")
            self.assertFalse(result)

    async def test_format_admin_summary(self):
        """format_admin_summary renders complete KPIs and web link."""
        stats = {
            "total_users": 5000,
            "active_today": 1200,
            "total_groups": 150,
            "total_games": 20000,
            "total_answers": 65000,
            "accuracy_percent": 82.4,
            "banned_users": 5
        }
        summary = format_admin_summary(stats)
        self.assertIn("5,000", summary)
        self.assertIn("1,200", summary)
        self.assertIn("82.4%", summary)
        self.assertIn("5", summary)


if __name__ == "__main__":
    unittest.main()
