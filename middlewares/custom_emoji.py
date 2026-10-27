"""
aiogram RequestMiddleware to automatically convert standard emojis to
custom animated emojis from the RestrictedEmoji pack for all HTML-parsed messages.
Also ensures button texts remain clean unicode (no broken HTML tags).
"""
import logging
from aiogram.client.session.middlewares.base import BaseRequestMiddleware
from aiogram.methods import SendMessage, EditMessageText, SendPhoto
from locales.custom_emojis import apply_custom_emojis, strip_custom_emojis

logger = logging.getLogger(__name__)


class CustomEmojiRequestMiddleware(BaseRequestMiddleware):
    """
    Middleware that intercepts outgoing Telegram API requests and:
    1. Upgrades standard emojis in HTML message texts and photo captions to animated <tg-emoji> tags.
    2. Strips any stray <tg-emoji> tags from inline or reply keyboard button labels.
    """

    async def __call__(self, make_request, bot, request):
        try:
            # 1. Transform text messages with custom animated emojis when HTML parse mode is active
            if isinstance(request, (SendMessage, EditMessageText)):
                pm = getattr(request, "parse_mode", None)
                is_html = pm == "HTML" or (
                    pm is None
                    and getattr(bot, "default", None)
                    and getattr(bot.default, "parse_mode", None) == "HTML"
                )
                if is_html and getattr(request, "text", None):
                    request.text = apply_custom_emojis(request.text)

            # 2. Transform photo captions with custom animated emojis when HTML parse mode is active
            elif isinstance(request, SendPhoto):
                pm = getattr(request, "parse_mode", None)
                is_html = pm == "HTML" or (
                    pm is None
                    and getattr(bot, "default", None)
                    and getattr(bot.default, "parse_mode", None) == "HTML"
                )
                if is_html and getattr(request, "caption", None):
                    request.caption = apply_custom_emojis(request.caption)

            # 3. Guard keyboard buttons against raw HTML entities
            rm = getattr(request, "reply_markup", None)
            if rm:
                if hasattr(rm, "inline_keyboard"):
                    for row in rm.inline_keyboard:
                        for btn in row:
                            if btn.text and "<tg-emoji" in btn.text:
                                btn.text = strip_custom_emojis(btn.text)
                elif hasattr(rm, "keyboard"):
                    for row in rm.keyboard:
                        for btn in row:
                            if btn.text and "<tg-emoji" in btn.text:
                                btn.text = strip_custom_emojis(btn.text)

        except Exception as e:
            logger.debug(f"CustomEmojiRequestMiddleware warning: {e}")

        return await make_request(bot, request)
