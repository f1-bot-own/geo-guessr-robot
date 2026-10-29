"""
Unit tests for custom animated emojis module and request middleware with button styling.
Ensures direction-matched custom emojis from RestrictedEmoji pack (https://t.me/addemoji/RestrictedEmoji)
are cleanly applied to messages, and buttons receive both custom emoji icons and colors.
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
from middlewares.custom_emoji import CustomEmojiRequestMiddleware, _determine_button_style


class TestCustomEmojis(unittest.TestCase):
    def test_pack_loaded(self):
        """RestrictedEmoji pack must load over 900 unique emojis."""
        self.assertGreater(len(EMOJI_TO_ID), 900)

    def test_named_aliases_exist_and_format_properly(self):
        """Top key icons must return direction-matched custom emoji tags."""
        key_icons = ["trophy", "fire", "star", "earth", "game", "swords", "check", "cross", "robot", "brain", "crown"]
        for icon in key_icons:
            tag = ce(icon)
            self.assertTrue(tag.startswith("<tg-emoji emoji-id=\""))
            self.assertTrue(tag.endswith("</tg-emoji>"))

    def test_raw_emoji_formatting(self):
        """Raw unicode emojis must return custom emoji tags with valid IDs."""
        tag_trophy = ce("🏆")
        self.assertEqual(tag_trophy, '<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji>')

        tag_fire = ce("🔥")
        self.assertEqual(tag_fire, '<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>')

    def test_apply_custom_emojis_replaces_icons(self):
        """apply_custom_emojis wraps emojis with their corresponding custom emoji tags."""
        sample = "🏆 Oltin medal! 🔥 5 ta ketma-ket! 🎮 O'yin boshlandi!"
        res = apply_custom_emojis(sample)
        self.assertIn('<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji>', res)
        self.assertIn('<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>', res)
        self.assertIn('<tg-emoji emoji-id="5467583879948803288">🎮</tg-emoji>', res)

    def test_direction_matched_emojis_in_overview(self):
        """Every game category has a distinct direction-matched custom emoji ID."""
        self.assertEqual(EMOJI_TO_ID["🎓"], "5375163339154399459")  # Zakovat
        self.assertEqual(EMOJI_TO_ID["🌍"], "5399898266265475100")  # Geography
        self.assertEqual(EMOJI_TO_ID["🌌"], "5372846474881146350")  # Cosmos -> Telescope 🔭
        self.assertEqual(EMOJI_TO_ID["🔬"], "5379679518740978720")  # Science -> Microscope 🔬
        self.assertEqual(EMOJI_TO_ID["📜"], "5359778044745622115")  # History -> Temple 🏛
        self.assertEqual(EMOJI_TO_ID["👑"], "5467406098367521267")  # People -> Crown 👑
        self.assertEqual(EMOJI_TO_ID["🔍"], "5188217332748527444")  # Blur -> Search 🔍
        self.assertEqual(EMOJI_TO_ID["🎲"], "5467583879948803288")  # Super Mix -> Game Controller 🎮
        self.assertEqual(EMOJI_TO_ID["🔘"], "5472111548572900003")  # Buttons -> Keyboard ⌨️
        self.assertEqual(EMOJI_TO_ID["✍️"], "5470060791883374114")  # Text -> Writing ✍️
        self.assertEqual(EMOJI_TO_ID["🔀"], "5264727218734524899")  # Both -> Cycle 🔄
        self.assertEqual(EMOJI_TO_ID["🔙"], "5469735272017043817")  # Back -> Pointer 👈

    def test_apply_custom_emojis_avoids_double_wrapping(self):
        """Already wrapped <tg-emoji> tags must not be wrapped again."""
        already_wrapped = '<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji> va yangisi 🔥'
        res = apply_custom_emojis(already_wrapped)
        self.assertEqual(res.count('<tg-emoji emoji-id="5409008750893734809">'), 1)
        self.assertIn('<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>', res)

    def test_apply_custom_emojis_preserves_html_tags(self):
        """HTML links and formatting tags are preserved intact."""
        html_text = '<b>🏆 Champion!</b> <a href="https://t.me/bot?mode=fire">Link</a>'
        res = apply_custom_emojis(html_text)
        self.assertTrue(res.startswith('<b><tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji> Champion!</b>'))
        self.assertIn('<a href="https://t.me/bot?mode=fire">Link</a>', res)

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


class TestButtonStylingRules(unittest.TestCase):
    def test_determine_button_style_green_actions(self):
        """Start, play, accept, add, confirm, and active toggles receive green success style."""
        self.assertEqual(_determine_button_style("🚀 O'yinni boshlash", "setup:launch"), "success")
        self.assertEqual(_determine_button_style("🎮 O'yin o'ynash", "menu:play"), "success")
        self.assertEqual(_determine_button_style("⚔️ Qabul qilish", "duel_acc:123"), "success")
        self.assertEqual(_determine_button_style("➕ Guruhga qo'shish", ""), "success")
        self.assertEqual(_determine_button_style("✅ 30s", "setup:time:30"), "success")
        self.assertEqual(_determine_button_style("• 🏆 All-Time •", "lb:all_time"), "success")
        self.assertEqual(_determine_button_style("🔘 Barcha rejimlar (Hammasi)", "setup:all_modes"), "success")
        self.assertEqual(_determine_button_style("✅ 10 ta", "setup:rounds:10"), "success")
        self.assertEqual(_determine_button_style("• 10 •", "setup:rounds:10"), "success")

    def test_determine_button_style_red_actions(self):
        """Cancel, decline, stop, back, eliminated answers, and exhausted lifelines receive red danger style."""
        self.assertEqual(_determine_button_style("❌ Bekor qilish", "setup:cancel"), "danger")
        self.assertEqual(_determine_button_style("❌ Rad etish", "duel_dec:123"), "danger")
        self.assertEqual(_determine_button_style("🔙 Orqaga", "menu:back"), "danger")
        self.assertEqual(_determine_button_style("🔙 📁 Barcha toifalar", "setup:hub:main"), "danger")
        self.assertEqual(_determine_button_style("◀️ Admin menyusiga qaytish", "admin:menu"), "danger")
        self.assertEqual(_determine_button_style("🛑 Stop", "stop_game"), "danger")
        self.assertEqual(_determine_button_style("Blur: ❌ OFF", "setup:blur"), "danger")
        self.assertEqual(_determine_button_style("✂️ ✖️", "solo_ignore"), "danger")
        self.assertEqual(_determine_button_style("💡 ✖️", "solo_ignore"), "danger")
        self.assertEqual(_determine_button_style("✖️", "solo_ignore"), "danger")
        self.assertEqual(_determine_button_style("—", "solo_disabled"), "danger")

    def test_determine_button_style_blue_navigation(self):
        """Menu navigation, profile, leaderboard, help, categories, and neutral options receive blue primary style."""
        self.assertEqual(_determine_button_style("👤 Mening profilim", "menu:profile"), "primary")
        self.assertEqual(_determine_button_style("🏆 Peshqadamlar", "menu:leaderboard"), "primary")
        self.assertEqual(_determine_button_style("🌐 Tilni o'zgartirish", "menu:lang"), "primary")
        self.assertEqual(_determine_button_style("❓ Qo'llanma", "menu:help"), "primary")
        self.assertEqual(_determine_button_style("Paris", "ans:0"), "primary")
        self.assertEqual(_determine_button_style("🔘 Faqat tugmalar", "setup:input:buttons"), "primary")
        self.assertEqual(_determine_button_style("✍️ Faqat matn", "setup:input:text"), "primary")
        self.assertEqual(_determine_button_style("🔀 Har ikkisi", "setup:input:both"), "primary")
        self.assertEqual(_determine_button_style("🌍 Geografiya (1,000+)", "setup:hub:geo"), "primary")
        self.assertEqual(_determine_button_style("🎓 Zakovat Klubi (500)", "setup:cat:zakovat"), "primary")


class TestCustomEmojiMiddleware(unittest.IsolatedAsyncioTestCase):
    async def test_middleware_cleans_html_send_message(self):
        """SendMessage gets animated custom emojis."""
        mw = CustomEmojiRequestMiddleware()
        req = SendMessage(chat_id=1001, text="Salom 🏆 va 🔥!", parse_mode="HTML")
        
        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)
        self.assertIn('<tg-emoji emoji-id="5409008750893734809">🏆</tg-emoji>', req.text)
        self.assertIn('<tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>', req.text)

    async def test_middleware_transforms_send_photo_caption(self):
        """SendPhoto caption gets custom animated emojis."""
        mw = CustomEmojiRequestMiddleware()
        req = SendPhoto(chat_id=1001, photo="file_id_123", caption="Savol: 🌍 Qaysi davlat?", parse_mode="HTML")

        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)
        self.assertIn('<tg-emoji emoji-id="5399898266265475100">🌍</tg-emoji>', req.caption)

    async def test_middleware_enriches_buttons_with_icons_and_style(self):
        """Buttons receive custom emoji icon and style color without star degradation."""
        mw = CustomEmojiRequestMiddleware()
        btn_start = InlineKeyboardButton(text="🚀 O'yinni boshlash", callback_data="setup:launch")
        btn_cancel = InlineKeyboardButton(text="❌ Bekor qilish", callback_data="setup:cancel")
        btn_prof = InlineKeyboardButton(text="👤 Profil", callback_data="menu:profile")
        kb = InlineKeyboardMarkup(inline_keyboard=[[btn_start], [btn_cancel], [btn_prof]])
        req = SendMessage(chat_id=1001, text="Menyu", reply_markup=kb, parse_mode="HTML")

        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)
        
        b0 = req.reply_markup.inline_keyboard[0][0]
        self.assertEqual(b0.style, "success")
        self.assertEqual(b0.icon_custom_emoji_id, "5445284980978621387")  # Rocket custom emoji
        self.assertEqual(b0.text, "O'yinni boshlash")

        b1 = req.reply_markup.inline_keyboard[1][0]
        self.assertEqual(b1.style, "danger")
        self.assertEqual(b1.icon_custom_emoji_id, "5465665476971471368")  # Cross custom emoji
        self.assertEqual(b1.text, "Bekor qilish")

        b2 = req.reply_markup.inline_keyboard[2][0]
        self.assertEqual(b2.style, "primary")
        self.assertEqual(b2.icon_custom_emoji_id, "5373012449597335010")  # User custom emoji
        self.assertEqual(b2.text, "Profil")

    async def test_category_buttons_enrich_with_matched_direction_icons(self):
        """Game category buttons receive their specific direction-matched custom emoji icons."""
        mw = CustomEmojiRequestMiddleware()
        btn_zakovat = InlineKeyboardButton(text="🎓 Zakovat Klubi (500)", callback_data="setup:cat:zakovat")
        btn_koinot = InlineKeyboardButton(text="🌌 Koinot & Tabiat (800)", callback_data="setup:cat:astronomy")
        btn_geo = InlineKeyboardButton(text="🌍 Geografiya (1,000+)", callback_data="setup:cat:geo")
        btn_tarix = InlineKeyboardButton(text="📜 Tarix & San'at (1,200)", callback_data="setup:cat:history")
        btn_mix = InlineKeyboardButton(text="🎲 SUPER MIX (Barchasi - 4,000+)", callback_data="setup:cat:mix")
        btn_both = InlineKeyboardButton(text="✅ 🔀 Har ikkisi", callback_data="setup:input:both")
        btn_back = InlineKeyboardButton(text="🔙 Orqaga", callback_data="setup:hub:main")
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [btn_zakovat], [btn_koinot], [btn_geo], [btn_tarix], [btn_mix], [btn_both], [btn_back]
        ])
        req = SendMessage(chat_id=1001, text="Toifalar", reply_markup=kb, parse_mode="HTML")

        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)

        # 🎓 Zakovat -> Cap
        b_zakovat = req.reply_markup.inline_keyboard[0][0]
        self.assertEqual(b_zakovat.icon_custom_emoji_id, "5375163339154399459")
        self.assertEqual(b_zakovat.text, "Zakovat Klubi (500)")
        self.assertEqual(b_zakovat.style, "primary")

        # 🌌 Koinot -> Telescope 🔭 (matched!)
        b_koinot = req.reply_markup.inline_keyboard[1][0]
        self.assertEqual(b_koinot.icon_custom_emoji_id, "5372846474881146350")
        self.assertEqual(b_koinot.text, "Koinot & Tabiat (800)")
        self.assertEqual(b_koinot.style, "primary")

        # 🌍 Geografiya -> Globe 🌍
        b_geo = req.reply_markup.inline_keyboard[2][0]
        self.assertEqual(b_geo.icon_custom_emoji_id, "5399898266265475100")
        self.assertEqual(b_geo.text, "Geografiya (1,000+)")
        self.assertEqual(b_geo.style, "primary")

        # 📜 Tarix -> Temple 🏛 (matched!)
        b_tarix = req.reply_markup.inline_keyboard[3][0]
        self.assertEqual(b_tarix.icon_custom_emoji_id, "5359778044745622115")
        self.assertEqual(b_tarix.text, "Tarix & San'at (1,200)")
        self.assertEqual(b_tarix.style, "primary")

        # 🎲 SUPER MIX -> Game Controller 🎮 (matched!)
        b_mix = req.reply_markup.inline_keyboard[4][0]
        self.assertEqual(b_mix.icon_custom_emoji_id, "5467583879948803288")
        self.assertEqual(b_mix.text, "SUPER MIX (Barchasi - 4,000+)")
        self.assertEqual(b_mix.style, "primary")

        # ✅ 🔀 Har ikkisi -> Cycle 🔄 (matched and green style!)
        b_both = req.reply_markup.inline_keyboard[5][0]
        self.assertEqual(b_both.icon_custom_emoji_id, "5264727218734524899")
        self.assertEqual(b_both.text, "Har ikkisi")
        self.assertEqual(b_both.style, "success")

        # 🔙 Orqaga -> Pointer 👈 (matched and red style!)
        b_back = req.reply_markup.inline_keyboard[6][0]
        self.assertEqual(b_back.icon_custom_emoji_id, "5469735272017043817")
        self.assertEqual(b_back.text, "Orqaga")
        self.assertEqual(b_back.style, "danger")

    async def test_admin_buttons_enrich_with_styles_and_icons(self):
        """Admin buttons receive custom emoji icons and primary style."""
        mw = CustomEmojiRequestMiddleware()
        btn_broadcast = InlineKeyboardButton(text="📢 Xabar yuborish", callback_data="admin:broadcast")
        btn_backup = InlineKeyboardButton(text="💾 DB Backup olish", callback_data="admin:backup")
        kb = InlineKeyboardMarkup(inline_keyboard=[[btn_broadcast], [btn_backup]])
        req = SendMessage(chat_id=1001, text="Admin panel", reply_markup=kb, parse_mode="HTML")

        async def fake_make_request(bot, r):
            return r

        mock_bot = MagicMock()
        await mw(fake_make_request, mock_bot, req)

        b0 = req.reply_markup.inline_keyboard[0][0]
        self.assertEqual(b0.style, "primary")
        self.assertEqual(b0.icon_custom_emoji_id, "5242628160297641831")  # Bell custom emoji
        self.assertEqual(b0.text, "Xabar yuborish")

        b1 = req.reply_markup.inline_keyboard[1][0]
        self.assertEqual(b1.style, "primary")
        self.assertEqual(b1.icon_custom_emoji_id, "5431721976769027887")  # Folder custom emoji
        self.assertEqual(b1.text, "DB Backup olish")

    async def test_middleware_fallback_on_rejection(self):
        """If Telegram rejects button styling, middleware restores original buttons and retries."""
        mw = CustomEmojiRequestMiddleware()
        btn = InlineKeyboardButton(text="🎮 O'yin o'ynash", callback_data="menu:play")
        kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])
        req = SendMessage(chat_id=1001, text="Menyu", reply_markup=kb, parse_mode="HTML")

        calls = []

        async def fake_make_request(bot, r):
            calls.append(r)
            if len(calls) == 1:
                raise Exception("Bad Request: BUTTON_STYLE_INVALID")
            return "success"

        mock_bot = MagicMock()
        res = await mw(fake_make_request, mock_bot, req)
        self.assertEqual(res, "success")
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[1].reply_markup.inline_keyboard[0][0].text, "🎮 O'yin o'ynash")


class TestI18nCustomEmojiIntegration(unittest.TestCase):
    def test_t_html_returns_custom_emojis(self):
        """t_html returns HTML with custom animated emojis."""
        res = t_html("welcome_private", "en")
        self.assertIn('<tg-emoji emoji-id="5399898266265475100">🌍</tg-emoji>', res)
        self.assertIn("Welcome to GeoGuru & GeoGuessr Bot!", res)

    def test_t_buttons_remain_clean_plain_text(self):
        """Button keys never contain <tg-emoji> tags."""
        btn_text = t("btn_leaderboard", "en")
        self.assertNotIn("<tg-emoji", btn_text)
        self.assertIn("🏆", btn_text)

        btn_text_uz = t("btn_play_game", "uz")
        self.assertNotIn("<tg-emoji", btn_text_uz)
        self.assertIn("🎮", btn_text_uz)
