"""
Unit tests for resilient photo delivery mechanism in GeoGuru & GeoGuessr Bot.
Tests:
1. In-memory PHOTO_CACHE lookup and instant send with telegram file_id.
2. Telegram URL failure fallback: automatic byte download via aiohttp and delivery as BufferedInputFile.
3. Cache extraction and persistence of file_id after successful photo send.
4. Cache invalidation when cached file_id fails.
5. Complete failure fallback to text message in games/flow.py (send_round_question and send_solo_round).
6. URL validity of data/streetviews.py and data/landmarks.py.
"""

import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from aiogram import Bot
from aiogram.types import Message, BufferedInputFile
from aiogram.exceptions import TelegramBadRequest, TelegramRetryAfter
from pathlib import Path
import tempfile

from games.flow import (
    send_resilient_photo,
    PHOTO_CACHE,
    send_round_question,
    send_solo_round,
    load_photo_cache,
    save_photo_cache,
    ENABLE_PERSISTENT_CACHE,
)
import games.flow
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.models import Question, GameMode
from gamedata.landmarks import LANDMARKS
from gamedata.streetviews import STREETVIEWS


class TestPhotoResilience(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        games.flow.ENABLE_PERSISTENT_CACHE = False
        PHOTO_CACHE.clear()
        self.bot = AsyncMock(spec=Bot)

    def tearDown(self):
        PHOTO_CACHE.clear()
        games.flow.ENABLE_PERSISTENT_CACHE = True

    async def test_cache_hit_sends_file_id_directly(self):
        """If image_url is in PHOTO_CACHE, send directly using cached file_id."""
        url = "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f"
        cached_id = "AgACAgIAAxkBAAIBZ2X..."
        PHOTO_CACHE[url] = cached_id

        mock_msg = MagicMock(spec=Message)
        self.bot.send_photo.return_value = mock_msg

        res = await send_resilient_photo(
            bot=self.bot,
            chat_id=12345,
            photo_url=url,
            caption="Test Caption"
        )

        self.assertEqual(res, mock_msg)
        self.bot.send_photo.assert_called_once_with(
            chat_id=12345,
            photo=cached_id,
            caption="Test Caption",
            reply_markup=None,
            parse_mode="HTML"
        )

    async def test_cache_miss_url_success_populates_cache(self):
        """When not cached, send via URL and cache the returned file_id."""
        url = "https://images.unsplash.com/photo-1552832230-c0197dd311b5"
        self.assertNotIn(url, PHOTO_CACHE)

        mock_photo_size = MagicMock()
        mock_photo_size.file_id = "AgACAgIA_NEW_FILE_ID"
        mock_msg = MagicMock(spec=Message)
        mock_msg.photo = [mock_photo_size]
        self.bot.send_photo.return_value = mock_msg

        res = await send_resilient_photo(
            bot=self.bot,
            chat_id=12345,
            photo_url=url,
            caption="Colosseum"
        )

        self.assertEqual(res, mock_msg)
        self.bot.send_photo.assert_called_once_with(
            chat_id=12345,
            photo=url,
            caption="Colosseum",
            reply_markup=None,
            parse_mode="HTML"
        )
        self.assertEqual(PHOTO_CACHE.get(url), "AgACAgIA_NEW_FILE_ID")

    async def test_telegram_url_failure_triggers_byte_download_fallback(self):
        """
        When Telegram fails with 'failed to get HTTP URL content', download image
        bytes in Python and send as BufferedInputFile, then cache file_id.
        """
        url = "https://example.com/blocked-image.jpg"
        self.assertNotIn(url, PHOTO_CACHE)

        # 1st call (URL) raises TelegramBadRequest
        # 2nd call (BufferedInputFile) succeeds
        url_error = TelegramBadRequest(
            method="sendPhoto",
            message="Bad Request: failed to get HTTP URL content"
        )
        mock_photo_size = MagicMock()
        mock_photo_size.file_id = "FILE_ID_FROM_BUFFERED_BYTES"
        mock_msg = MagicMock(spec=Message)
        mock_msg.photo = [mock_photo_size]

        self.bot.send_photo.side_effect = [url_error, mock_msg]

        fake_image_bytes = b"\xff\xd8\xff\xe0\x00\x10JFIFfakeimagecontent"

        # Mock aiohttp download
        mock_resp = AsyncMock()
        mock_resp.status = 200
        mock_resp.read = AsyncMock(return_value=fake_image_bytes)

        mock_ctx = AsyncMock()
        mock_ctx.__aenter__.return_value = mock_resp
        mock_ctx.__aexit__.return_value = None

        mock_session_inst = MagicMock()
        mock_session_inst.get.return_value = mock_ctx
        mock_session_inst.__aenter__.return_value = mock_session_inst
        mock_session_inst.__aexit__.return_value = None

        with patch("aiohttp.ClientSession", return_value=mock_session_inst):
            res = await send_resilient_photo(
                bot=self.bot,
                chat_id=12345,
                photo_url=url,
                caption="Resilient Image"
            )

        self.assertEqual(res, mock_msg)
        self.assertEqual(self.bot.send_photo.call_count, 2)

        # Verify second call received a BufferedInputFile
        second_call_kwargs = self.bot.send_photo.call_args_list[1][1]
        sent_photo_arg = second_call_kwargs["photo"]
        self.assertIsInstance(sent_photo_arg, BufferedInputFile)
        self.assertEqual(sent_photo_arg.data, fake_image_bytes)

        # Verify cached
        self.assertEqual(PHOTO_CACHE.get(url), "FILE_ID_FROM_BUFFERED_BYTES")

    async def test_cache_invalidation_when_cached_file_id_fails(self):
        """If cached file_id fails, it should be evicted and fallback attempted."""
        url = "https://images.unsplash.com/photo-test"
        PHOTO_CACHE[url] = "EXPIRED_FILE_ID"

        # 1st call with cached file_id fails
        # 2nd call with URL succeeds
        mock_photo_size = MagicMock()
        mock_photo_size.file_id = "NEW_VALID_FILE_ID"
        mock_msg = MagicMock(spec=Message)
        mock_msg.photo = [mock_photo_size]

        self.bot.send_photo.side_effect = [
            TelegramBadRequest(method="sendPhoto", message="Wrong file_id"),
            mock_msg
        ]

        res = await send_resilient_photo(
            bot=self.bot,
            chat_id=12345,
            photo_url=url,
            caption="Test"
        )

        self.assertEqual(res, mock_msg)
        self.assertEqual(PHOTO_CACHE.get(url), "NEW_VALID_FILE_ID")

    async def test_flow_send_round_question_sets_has_photo_true(self):
        """send_round_question sets session.has_photo = True when photo send succeeds."""
        session = GameSession(chat_id=-1001, mode="streetview", total_rounds=1)
        q = Question(
            mode="streetview",
            text="Where is this?",
            options=["USA", "Canada", "Mexico", "Brazil"],
            correct_index=0,
            correct_answer="USA",
            country_code="us",
            image_url="https://images.unsplash.com/photo-1534430480872-3498386e7856"
        )
        session.current_question = q
        session.current_round = 1

        mock_msg = MagicMock(spec=Message)
        mock_msg.message_id = 777
        mock_msg.photo = [MagicMock(file_id="PHOTO_123")]

        with patch("games.flow.send_resilient_photo", new_callable=AsyncMock) as mock_send_resilient:
            mock_send_resilient.return_value = mock_msg
            await send_round_question(self.bot, chat_id=-1001, session=session, db=AsyncMock())

            self.assertTrue(session.has_photo)
            self.assertEqual(session.round_message_id, 777)
            if session.timer_task:
                session.timer_task.cancel()

    async def test_flow_send_round_question_fallback_to_text_when_photo_fails(self):
        """When photo send returns None, send_round_question falls back to text and has_photo=False."""
        session = GameSession(chat_id=-1002, mode="streetview", total_rounds=1)
        q = Question(
            mode="streetview",
            text="Where is this?",
            options=["France", "Germany", "Italy", "Spain"],
            correct_index=0,
            correct_answer="France",
            country_code="fr",
            image_url="https://images.unsplash.com/broken-url"
        )
        session.current_question = q
        session.current_round = 1

        text_msg = MagicMock(spec=Message)
        text_msg.message_id = 888
        self.bot.send_message.return_value = text_msg

        with patch("games.flow.send_resilient_photo", new_callable=AsyncMock) as mock_send_resilient:
            mock_send_resilient.return_value = None
            await send_round_question(self.bot, chat_id=-1002, session=session, db=AsyncMock())

            self.assertFalse(session.has_photo)
            self.assertEqual(session.round_message_id, 888)
            self.bot.send_message.assert_called_once()
            if session.timer_task:
                session.timer_task.cancel()

    async def test_flow_send_solo_round_sets_has_photo_true(self):
        """send_solo_round sets session.has_photo = True when photo send succeeds."""
        session = SoloGameSession(user_id=12345, user_name="TestUser", mode="landmark")
        q = Question(
            mode="landmark",
            text="Name this landmark",
            options=["Eiffel Tower", "Big Ben", "Colosseum", "Petra"],
            correct_index=0,
            correct_answer="Eiffel Tower",
            country_code="fr",
            image_url="https://images.unsplash.com/photo-1511739001486-6bfe10ce785f"
        )
        session.current_question = q
        session.round_number = 1

        mock_msg = MagicMock(spec=Message)
        mock_msg.message_id = 999
        mock_msg.photo = [MagicMock(file_id="SOLO_PHOTO_ID")]

        with patch("games.flow.send_resilient_photo", new_callable=AsyncMock) as mock_send_resilient:
            mock_send_resilient.return_value = mock_msg
            await send_solo_round(self.bot, user_id=12345, session=session, db=AsyncMock())

            self.assertTrue(session.has_photo)
            self.assertEqual(session.round_message_id, 999)
            if session.timer_task:
                session.timer_task.cancel()

    async def test_telegram_retry_after_on_cache_preserves_cache(self):
        """TelegramRetryAfter should NOT invalidate the cache and must not hammer fallback."""
        url = "https://images.unsplash.com/photo-flood"
        PHOTO_CACHE[url] = "CACHED_FILE_123"

        flood_err = TelegramRetryAfter(
            method=MagicMock(),
            message="Flood control exceeded",
            retry_after=10
        )
        self.bot.send_photo.side_effect = flood_err

        res = await send_resilient_photo(
            bot=self.bot,
            chat_id=12345,
            photo_url=url,
            caption="Test Flood"
        )

        self.assertIsNone(res)
        # Verify cached file_id was NOT purged due to rate-limit
        self.assertEqual(PHOTO_CACHE.get(url), "CACHED_FILE_123")
        # Ensure it called send_photo only once (did not hammer direct URL or byte download during flood)
        self.assertEqual(self.bot.send_photo.call_count, 1)

    async def test_long_caption_truncated_to_telegram_limit(self):
        """Captions exceeding 1024 characters must be safely truncated to prevent TelegramBadRequest."""
        url = "https://images.unsplash.com/photo-caption"
        PHOTO_CACHE[url] = "VALID_FID"

        mock_msg = MagicMock(spec=Message)
        self.bot.send_photo.return_value = mock_msg

        long_caption = "A" * 1500
        res = await send_resilient_photo(
            bot=self.bot,
            chat_id=12345,
            photo_url=url,
            caption=long_caption
        )

        self.assertEqual(res, mock_msg)
        called_caption = self.bot.send_photo.call_args[1]["caption"]
        self.assertLessEqual(len(called_caption), 1024)
        self.assertTrue(called_caption.endswith("..."))

    async def test_empty_or_invalid_url_returns_none(self):
        """Empty, non-string, or whitespace URL must return None immediately."""
        self.assertIsNone(await send_resilient_photo(self.bot, 12345, ""))
        self.assertIsNone(await send_resilient_photo(self.bot, 12345, "   "))
        self.assertIsNone(await send_resilient_photo(self.bot, 12345, None))
        self.assertEqual(self.bot.send_photo.call_count, 0)

    def test_photo_cache_save_and_load_persistence(self):
        """Verify save_photo_cache and load_photo_cache persist and restore cache to disk."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            cache_file = Path(tmp_dir) / "test_cache.json"
            PHOTO_CACHE.clear()
            PHOTO_CACHE["https://images.unsplash.com/sample1"] = "FID_1"
            PHOTO_CACHE["https://images.unsplash.com/sample2"] = "FID_2"

            save_photo_cache(cache_file)
            self.assertTrue(cache_file.exists())

            PHOTO_CACHE.clear()
            self.assertEqual(len(PHOTO_CACHE), 0)

            load_photo_cache(cache_file)
            self.assertEqual(PHOTO_CACHE.get("https://images.unsplash.com/sample1"), "FID_1")
            self.assertEqual(PHOTO_CACHE.get("https://images.unsplash.com/sample2"), "FID_2")


class TestDataImageUrlsIntegrity(unittest.TestCase):

    def test_all_landmarks_have_valid_cdn_urls(self):
        """Ensure every landmark has a valid HTTP/HTTPS CDN URL without old broken Wikimedia thumb URLs."""
        self.assertGreaterEqual(len(LANDMARKS), 30)
        for lm in LANDMARKS:
            url = lm.get("image_url", "")
            self.assertTrue(url.startswith("https://"), f"Landmark {lm['id']} must have https URL: {url}")
            self.assertNotIn("800px-", url, f"Landmark {lm['id']} still contains broken 800px- thumbnail: {url}")
            self.assertTrue(
                any(domain in url for domain in ("images.unsplash.com", "upload.wikimedia.org", "wikimedia.org")),
                f"Landmark {lm['id']} should use reliable CDN: {url}"
            )

    def test_all_streetviews_have_valid_cdn_urls(self):
        """Ensure every streetview has a valid HTTP/HTTPS CDN URL without old broken Wikimedia thumb URLs."""
        self.assertGreaterEqual(len(STREETVIEWS), 50)
        for sv in STREETVIEWS:
            url = sv.get("image_url", "")
            self.assertTrue(url.startswith("https://"), f"Streetview {sv['id']} must have https URL: {url}")
            self.assertNotIn("800px-", url, f"Streetview {sv['id']} still contains broken 800px- thumbnail: {url}")
            self.assertIn("images.unsplash.com", url, f"Streetview {sv['id']} should use reliable CDN: {url}")


if __name__ == "__main__":
    unittest.main()
