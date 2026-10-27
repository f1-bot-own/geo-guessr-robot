"""
Unit tests for custom animated emojis module and request middleware.
Pack: Animated Emoji (https://t.me/addemoji/RestrictedEmoji)
"""
import unittest
from unittest.mock import AsyncMock, MagicMock
from aiogram.methods import SendMessage, EditMessageText, SendPhoto
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from locales.custom_emojis import (
    ce,
    apply_custom_emojis,
    strip_custom_emojis,
    EMOJI_TO_ID,
    NAMED_ALIASES,
)
from locales.i18n import t, t_html
from middlewares.custom_emoji import CustomEmojiRequestMiddleware


class TestCustomEmojis(unittest.TestCase):
    def test_pack_loaded(self):
        """RestrictedEmoji pack must load over 900 unique emojis."""
        self.assertGreater(len(EMOJI_TO_ID), 900)

    def test_named_aliases_exist_and_format_properly(self):
        """Top key icons must have valid animated custom emoji IDs."""
        key_icons = ["trophy", "fire", "star", "earth", "game", "swords", "check", "cross", "robot", "brain", "crown"]
        for icon in key_icons:
            tag = ce(icon)
            self.assertTrue(tag.startswith("<tg-emoji emoji-id=\""))
            self.assertTrue(tag.endswith("</tg-emoji>"))

    def test_raw_emoji_formatting(self):
        """Raw unicode emojis must be converted into <tg-emoji> tags."""
        tag = ce("🏆")
        self.assertEqual(tag, '<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji>')

        tag_fire = ce("🔥")
        self.assertEqual(tag_fire, '<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>')

    def test_apply_custom_emojis_replaces_icons(self):
        """apply_custom_emojis replaces emojis with their corresponding animated tags."""
        sample = "🏆 Oltin medal! 🔥 5 ta ketma-ket! 🎮 O'yin boshlandi!"
        res = apply_custom_emojis(sample)
        self.assertIn('<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji>', res)
        self.assertIn('<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>', res)
        self.assertIn('<tg-emoji emoji-id="5467583879948803288">🎮</tg-emoji>', res)

    def test_apply_custom_emojis_avoids_double_wrapping(self):
        """Already wrapped <tg-emoji> tags must not be wrapped again."""
        already_wrapped = '<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji> va yangisi 🔥'
        res = apply_custom_emojis(already_wrapped)
        # Should only contain one <tg-emoji tag for 🏆
        self.assertEqual(res.count('<tg-emoji emoji-id="5409008750893734809">'), 1)
        # And 🔥 should also be wrapped
        self.assertIn('<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>', res)

    def test_apply_custom_emojis_preserves_html_tags(self):
        """HTML links and formatting tags are preserved intact."""
        html_text = '<b>🏆 Champion!</b> <a href="https://t.me/bot?mode=🔥">Link</a>'
        res = apply_custom_emojis(html_text)
        self.assertTrue(res.startswith('<b><tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji> Champion!</b>'))
        self.assertIn('<a href="https://t.me/bot?mode=🔥">Link</a>', res)

    def test_strip_custom_emojis(self):
        """strip_custom_emojis removes tags and recovers clean unicode emojis."""
        tagged = '<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji> Reyting'
        plain = strip_custom_emojis(tagged)
        self.assertEqual(plain, "🏆 Reyting")

    def test_empty_or_none_safety(self):
        """Empty or None strings return safely without errors."""
        self.assertEqual(apply_custom_emojis(""), "")
        self.assertEqual(apply_custom_emojis(None), None)
        self.assertEqual(strip_custom_emojis(""), "")
        self.assertEqual(strip_custom_emojis(None), None)


class TestCustomEmojiMiddleware(unittest.IsolatedAsyncioTestCase):
    async def test_middleware_transforms_html_send_message(self):
        """SendMessage with HTML parse mode gets custom animated emojis."""
        mw = CustomEmojiRequestMiddleware()
        req = SendMessage(chat_id=1001, text="Salom 🏆 va 🔥!", parse_mode="HTML")
        
        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)
        self.assertIn('<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji>', req.text)
        self.assertIn('<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>', req.text)

    async def test_middleware_transforms_default_parse_mode_message(self):
        """SendMessage with default parse mode (no explicit parse_mode) gets custom emojis."""
        mw = CustomEmojiRequestMiddleware()
        req = SendMessage(chat_id=1001, text="O'yin 🎮 va 🏆")
        
        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        mock_bot.default = DefaultBotProperties(parse_mode=ParseMode.HTML)
        await mw(fake_make_request, mock_bot, req)
        self.assertIn('<tg-emoji emoji-id="5467583879948803288">🎮</tg-emoji>', req.text)
        self.assertIn('<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji>', req.text)

    async def test_middleware_transforms_send_photo_caption(self):
        """SendPhoto caption with HTML parse mode gets custom animated emojis."""
        mw = CustomEmojiRequestMiddleware()
        req = SendPhoto(chat_id=1001, photo="file_id_123", caption="Savol: 🌍 Qaysi davlat?", parse_mode="HTML")

        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)
        self.assertIn('<tg-emoji emoji-id="5399898266265475100">🌍</tg-emoji>', req.caption)

    async def test_middleware_enriches_buttons_with_icon_custom_emoji_id(self):
        """Buttons with leading emojis have icon_custom_emoji_id assigned and text cleaned."""
        mw = CustomEmojiRequestMiddleware()
        btn = InlineKeyboardButton(
            text="🏆 Peshqadamlar jadvali",
            callback_data="menu:lb"
        )
        kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])
        req = SendMessage(chat_id=1001, text="Menyu", reply_markup=kb, parse_mode="HTML")

        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)
        processed_btn = req.reply_markup.inline_keyboard[0][0]
        self.assertEqual(processed_btn.icon_custom_emoji_id, "5409008750893734809")
        self.assertEqual(processed_btn.text, "Peshqadamlar jadvali")

    async def test_middleware_fallback_on_custom_emoji_rejection(self):
        """If Telegram rejects icon_custom_emoji_id, middleware restores original buttons and retries."""
        mw = CustomEmojiRequestMiddleware()
        btn = InlineKeyboardButton(text="🎮 O'yin o'ynash", callback_data="menu:play")
        kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])
        req = SendMessage(chat_id=1001, text="Menyu", reply_markup=kb, parse_mode="HTML")

        calls = []

        async def fake_make_request(bot, r):
            calls.append(r)
            if len(calls) == 1:
                raise Exception("Bad Request: BUTTON_CUSTOM_EMOJI_INVALID")
            return "success"

        mock_bot = MagicMock()
        res = await mw(fake_make_request, mock_bot, req)
        self.assertEqual(res, "success")
        self.assertEqual(len(calls), 2)
        # In second call, original text was restored without error
        self.assertEqual(calls[1].reply_markup.inline_keyboard[0][0].text, "🎮 O'yin o'ynash")


class TestI18nCustomEmojiIntegration(unittest.TestCase):
    def test_t_html_returns_custom_emojis(self):
        """t_html explicitly applies custom animated emojis to translations."""
        res = t_html("welcome_private", "en")
        self.assertIn('<tg-emoji emoji-id="5399898266265475100">🌍</tg-emoji>', res)
        self.assertIn("Welcome to GeoGuru & GeoGuessr Bot!", res)

    def test_t_buttons_remain_clean_plain_text(self):
        """Button keys never contain <tg-emoji> tags even when accessed."""
        btn_text = t("btn_leaderboard", "en")
        self.assertNotIn("<tg-emoji", btn_text)
        self.assertIn("🏆", btn_text)

        btn_text_uz = t("btn_play_game", "uz")
        self.assertNotIn("<tg-emoji", btn_text_uz)
        self.assertIn("🎮", btn_text_uz)
