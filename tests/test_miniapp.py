"""
Unit tests for GeoGuessr Telegram Mini App.
Tests web server endpoints, keyboard creation, and command/data handlers.
"""

import os
import json
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from webapp.server import create_web_app
from keyboards.menu_kb import get_miniapp_button, get_miniapp_launch_kb, get_main_menu_kb
from handlers.commands import cmd_miniapp, handle_miniapp_data
from handlers.callbacks import cb_main_menu


class TestMiniAppWebServer(AioHTTPTestCase):
    async def get_application(self):
        self.mock_db = MagicMock()
        self.mock_db.add_user_xp = AsyncMock()
        return create_web_app(db=self.mock_db)

    @unittest_run_loop
    async def test_health_endpoint(self):
        """Verify /health endpoint returns 200 and healthy status."""
        resp = await self.client.request("GET", "/health")
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertEqual(data.get("status"), "healthy")

    @unittest_run_loop
    async def test_index_page(self):
        """Verify / and /miniapp serve HTML page with Pannellum 360 viewer."""
        resp = await self.client.request("GET", "/")
        self.assertEqual(resp.status, 200)
        text = await resp.text()
        self.assertIn("GeoGuessr Mini App", text)
        self.assertIn("pannellum", text.lower())
        self.assertIn("panoramaViewer", text)
        self.assertIn("mapLayerToggle", text)

        resp2 = await self.client.request("GET", "/miniapp")
        self.assertEqual(resp2.status, 200)

    @unittest_run_loop
    async def test_panorama_assets_served(self):
        """Verify 360 equirectangular panoramas are served statically."""
        resp = await self.client.request("GET", "/panoramas/swiss-alps.jpg")
        self.assertEqual(resp.status, 200)
        self.assertEqual(resp.headers.get("Content-Type"), "image/jpeg")

    @unittest_run_loop
    async def test_score_api_submission(self):
        """Verify /api/miniapp/score handles score payload and awards XP."""
        payload = {"user_id": 12345, "score": 20000, "rounds": 5}
        resp = await self.client.request("POST", "/api/miniapp/score", json=payload)
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data.get("ok"))
        self.mock_db.add_user_xp.assert_called_once_with(12345, 400)

    @unittest_run_loop
    async def test_score_api_negative_score_rejected(self):
        """Negative scores must be rejected with 400 Bad Request."""
        payload = {"user_id": 12345, "score": -100}
        resp = await self.client.request("POST", "/api/miniapp/score", json=payload)
        self.assertEqual(resp.status, 400)
        data = await resp.json()
        self.assertFalse(data.get("ok"))
        self.assertIn("between 0 and 25000", data.get("error", ""))

    @unittest_run_loop
    async def test_score_api_excessive_score_rejected(self):
        """Scores above 25,000 must be rejected with 400 Bad Request."""
        payload = {"user_id": 12345, "score": 30000}
        resp = await self.client.request("POST", "/api/miniapp/score", json=payload)
        self.assertEqual(resp.status, 400)
        data = await resp.json()
        self.assertFalse(data.get("ok"))
        self.assertIn("between 0 and 25000", data.get("error", ""))

    @unittest_run_loop
    async def test_score_api_non_integer_score_rejected(self):
        """Non-integer scores must be rejected with 400 Bad Request."""
        payload = {"user_id": 12345, "score": "twenty_thousand"}
        resp = await self.client.request("POST", "/api/miniapp/score", json=payload)
        self.assertEqual(resp.status, 400)
        data = await resp.json()
        self.assertFalse(data.get("ok"))

    @unittest_run_loop
    async def test_score_api_missing_score_rejected(self):
        """Payload without score field must be rejected with 400 Bad Request."""
        payload = {"user_id": 12345}
        resp = await self.client.request("POST", "/api/miniapp/score", json=payload)
        self.assertEqual(resp.status, 400)
        data = await resp.json()
        self.assertFalse(data.get("ok"))

    @unittest_run_loop
    async def test_score_api_invalid_user_id_rejected(self):
        """Non-integer or non-positive user_id must be rejected with 400 Bad Request."""
        # Non-integer string
        resp1 = await self.client.request("POST", "/api/miniapp/score", json={"user_id": "invalid_user", "score": 1000})
        self.assertEqual(resp1.status, 400)

        # Negative user_id
        resp2 = await self.client.request("POST", "/api/miniapp/score", json={"user_id": -99, "score": 1000})
        self.assertEqual(resp2.status, 400)

    @unittest_run_loop
    async def test_score_api_invalid_rounds_rejected(self):
        """Rounds out of range 1-50 must be rejected with 400 Bad Request."""
        resp = await self.client.request("POST", "/api/miniapp/score", json={"user_id": 12345, "score": 1000, "rounds": 0})
        self.assertEqual(resp.status, 400)

    @unittest_run_loop
    async def test_score_api_invalid_json_rejected(self):
        """Malformed JSON or non-dict payloads must return 400 Bad Request."""
        resp = await self.client.request("POST", "/api/miniapp/score", data="not json", headers={"Content-Type": "application/json"})
        self.assertEqual(resp.status, 400)


class TestMiniAppKeyboards(unittest.TestCase):
    def test_miniapp_button_without_url(self):
        """When WEBAPP_URL is empty, button falls back to callback query."""
        with patch("config.WEBAPP_URL", ""):
            btn = get_miniapp_button("en")
            self.assertEqual(btn.callback_data, "menu:miniapp")
            self.assertIsNone(btn.web_app)

    def test_miniapp_button_with_https_url(self):
        """When WEBAPP_URL is https, button uses WebAppInfo."""
        with patch("config.WEBAPP_URL", "https://geobot.up.railway.app"):
            btn = get_miniapp_button("uz")
            self.assertIsNotNone(btn.web_app)
            self.assertEqual(btn.web_app.url, "https://geobot.up.railway.app")

    def test_main_menu_does_not_include_miniapp_button(self):
        """Main menu keyboard has play game as top row and excludes miniapp button when removed."""
        kb = get_main_menu_kb("en")
        first_btn = kb.inline_keyboard[0][0]
        self.assertIn("Play Game", first_btn.text)
        all_texts = [btn.text for row in kb.inline_keyboard for btn in row]
        self.assertFalse(any("Mini App" in text for text in all_texts))


class TestMiniAppHandlers(unittest.IsolatedAsyncioTestCase):
    async def test_cmd_miniapp(self):
        """Test /miniapp command response."""
        mock_msg = MagicMock()
        mock_msg.from_user.id = 999
        mock_msg.answer = AsyncMock()

        mock_bot = MagicMock()
        mock_db = MagicMock()
        mock_db.get_user = AsyncMock(return_value={"language": "uz"})
        mock_bot.db = mock_db
        mock_bot.__getitem__ = MagicMock(return_value=mock_db)

        await cmd_miniapp(mock_msg, mock_bot)
        mock_msg.answer.assert_called_once()
        sent_text = mock_msg.answer.call_args[1]["text"]
        self.assertIn("GeoGuessr Mini App", sent_text)

    async def test_handle_web_app_data(self):
        """Test Telegram WebApp data submission message handler."""
        mock_msg = MagicMock()
        mock_msg.from_user.id = 888
        mock_msg.from_user.first_name = "PlayerOne"
        mock_msg.from_user.username = "player1"
        mock_msg.web_app_data.data = json.dumps({
            "action": "miniapp_score",
            "total_score": 22500,
            "rank": "Geo Legend"
        })
        mock_msg.reply = AsyncMock()

        mock_bot = MagicMock()
        mock_db = MagicMock()
        mock_db.get_user = AsyncMock(return_value={"language": "uz"})
        mock_db.record_answer = AsyncMock()
        mock_bot.db = mock_db
        mock_bot.__getitem__ = MagicMock(return_value=mock_db)

        await handle_miniapp_data(mock_msg, mock_bot)
        mock_db.record_answer.assert_called_once()
        call_kwargs = mock_db.record_answer.call_args[1]
        self.assertEqual(call_kwargs["points"], 22500)
        self.assertEqual(call_kwargs["xp"], 450)
        mock_msg.reply.assert_called_once()


if __name__ == "__main__":
    unittest.main()
