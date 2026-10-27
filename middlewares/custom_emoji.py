"""
aiogram RequestMiddleware to automatically convert standard emojis to
custom animated emojis from the RestrictedEmoji pack for all HTML-parsed messages.
Also assigns icon_custom_emoji_id to keyboard buttons (with fallback protection).
"""
import copy
import logging
import re
from typing import Any
from aiogram.client.default import Default
from aiogram.client.session.middlewares.base import BaseRequestMiddleware
from aiogram.enums import ParseMode
from aiogram.methods import SendMessage, EditMessageText, SendPhoto
from locales.custom_emojis import apply_custom_emojis, strip_custom_emojis, EMOJI_TO_ID

logger = logging.getLogger(__name__)

# Regex to detect leading emoji on button labels
LEADING_EMOJI_REGEX = re.compile(
    r"^("
    r"[\U0001F1E6-\U0001F1FF]{2}|"  # Country flags
    r"[\U0001F300-\U0001F5FF]|"
    r"[\U0001F600-\U0001F64F]|"
    r"[\U0001F680-\U0001F6FF]|"
    r"[\U0001F700-\U0001F77F]|"
    r"[\U0001F780-\U0001F7FF]|"
    r"[\U0001F800-\U0001F8FF]|"
    r"[\U0001F900-\U0001F9FF]|"
    r"[\U0001FA00-\U0001FA6F]|"
    r"[\U0001FA70-\U0001FAFF]|"
    r"[\U00002702-\U000027B0]|"
    r"[\U000024C2-\U0001F251]|"
    r"[\U00002600-\U000026FF]|"
    r"[\U00002300-\U000023FF]"
    r")\ufe0f?\s*",
    flags=re.UNICODE,
)


def _is_html_mode(request: Any, bot: Any) -> bool:
    """Check if the request is formatted as HTML (explicitly or by bot default)."""
    pm = getattr(request, "parse_mode", None)
    if pm in ("HTML", ParseMode.HTML):
        return True
    if pm is None or isinstance(pm, Default):
        default_pm = getattr(getattr(bot, "default", None), "parse_mode", None)
        if default_pm in ("HTML", ParseMode.HTML):
            return True
        # If bot default is None, our application standard is HTML
        return True
    return False


def _enrich_buttons(reply_markup: Any) -> bool:
    """
    Examines keyboard buttons and attaches icon_custom_emoji_id when a leading emoji is detected.
    Returns True if any button was modified.
    """
    if not reply_markup:
        return False

    rows = getattr(reply_markup, "inline_keyboard", None) or getattr(reply_markup, "keyboard", None) or []
    modified = False

    for row in rows:
        for btn in row:
            text = getattr(btn, "text", None)
            if not text:
                continue

            # Strip any stray HTML tags from text
            if "<tg-emoji" in text:
                btn.text = strip_custom_emojis(text)
                text = btn.text

            # If icon_custom_emoji_id is already set, skip
            if getattr(btn, "icon_custom_emoji_id", None):
                continue

            # Check for leading emoji
            m = LEADING_EMOJI_REGEX.match(text)
            if m:
                lead_emoji = m.group(1)
                clean_lead = lead_emoji.replace("\ufe0f", "")
                cid = EMOJI_TO_ID.get(lead_emoji) or EMOJI_TO_ID.get(clean_lead)
                if cid:
                    btn.icon_custom_emoji_id = str(cid)
                    rem_text = text[m.end():].strip()
                    if rem_text:
                        btn.text = rem_text
                    modified = True

    return modified


class CustomEmojiRequestMiddleware(BaseRequestMiddleware):
    """
    Middleware that intercepts outgoing Telegram API requests and:
    1. Upgrades standard emojis in HTML message texts and photo captions to animated <tg-emoji> tags.
    2. Attaches icon_custom_emoji_id to buttons so Telegram displays custom emojis on keyboard buttons.
    3. Provides automatic fallback retry if Telegram Bot API returns an error on icon_custom_emoji_id.
    """

    async def __call__(self, make_request, bot, request):
        # 1. Transform message text or photo caption
        try:
            if isinstance(request, (SendMessage, EditMessageText)):
                if _is_html_mode(request, bot) and getattr(request, "text", None):
                    request.text = apply_custom_emojis(request.text)
            elif isinstance(request, SendPhoto):
                if _is_html_mode(request, bot) and getattr(request, "caption", None):
                    request.caption = apply_custom_emojis(request.caption)
        except Exception as e:
            logger.debug(f"Error applying custom emojis to text: {e}")

        # 2. Enrich buttons with icon_custom_emoji_id
        orig_reply_markup = None
        rm = getattr(request, "reply_markup", None)
        if rm:
            try:
                # Save backup in case Telegram rejects icon_custom_emoji_id
                orig_reply_markup = copy.deepcopy(rm)
                _enrich_buttons(rm)
            except Exception as e:
                logger.debug(f"Error enriching keyboard buttons: {e}")

        # 3. Make request with fallback protection
        try:
            return await make_request(bot, request)
        except Exception as err:
            err_msg = str(err).lower()
            # If rejected by Telegram due to custom emoji button restrictions (e.g. non-premium bot owner)
            if orig_reply_markup and ("emoji" in err_msg or "button" in err_msg or "icon" in err_msg):
                logger.warning(f"Telegram rejected button custom emoji: {err}. Retrying with original buttons.")
                request.reply_markup = orig_reply_markup
                return await make_request(bot, request)
            raise
