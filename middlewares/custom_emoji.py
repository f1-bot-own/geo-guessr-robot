"""
aiogram RequestMiddleware to automatically convert standard emojis to
custom animated emojis from the RestrictedEmoji pack for all HTML-parsed messages.
Also assigns icon_custom_emoji_id and color style to keyboard buttons (with fallback protection).
"""
import copy
import logging
import re
from typing import Any
from aiogram.client.default import Default
from aiogram.client.session.middlewares.base import BaseRequestMiddleware
from aiogram.enums import ParseMode
from aiogram.methods import (
    SendMessage,
    EditMessageText,
    SendPhoto,
    SendAnimation,
    SendVideo,
    SendAudio,
    SendDocument,
    SendVoice,
    EditMessageCaption,
)
from locales.custom_emojis import (
    apply_custom_emojis,
    strip_custom_emojis,
    resolve_fallback_emoji_id,
    EMOJI_TO_ID,
)

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


def _determine_button_style(text: str, callback_data: str = "") -> str:
    """
    Determine button style (color) based on text and callback semantics:
    - 'danger' (Red): cancel, decline, stop, back, return, delete, exit, close, clear, off, disabled/eliminated options.
    - 'success' (Green): start, play, accept, add to group, confirm, continue, next, save, select all, active/on options.
    - 'primary' (Blue): default for navigation, menu choices, profiles, settings, quiz answers, and neutral options.
    """
    t_lower = text.lower()
    cb_lower = (callback_data or "").lower()

    # 1. Red (danger) conditions - check first so 'back to categories' or 'cancel start' aren't marked green:
    if (
        text.startswith("❌")
        or text.startswith("🔴")
        or text.startswith("🔙")
        or text.startswith("◀️")
        or text.startswith("⬅️")
        or "✖️" in text
        or text.strip() in ("—", "-", "✖️", "❌")
    ):
        return "danger"

    if (
        "off" in t_lower
        or "o'chirilgan" in t_lower
        or "выкл" in t_lower
    ):
        return "danger"

    danger_keywords = [
        "cancel", "bekor", "отмена",
        "decline", "rad etish", "отклонить",
        "stop", "to'xtatish", "остановить",
        "back", "orqaga", "назад", "qaytish", "вернуться",
        "delete", "o'chirish", "удалить",
        "exit", "chiqish", "выход", "quit", "leave", "tark etish",
        "close", "yopish", "закрыть",
        "clear", "tozalash", "очистить",
        "reject",
    ]
    for k in danger_keywords:
        if k == "back":
            if (
                ("back" in t_lower and "backup" not in t_lower and "feedback" not in t_lower)
                or ("back" in cb_lower and "backup" not in cb_lower and "feedback" not in cb_lower)
            ):
                return "danger"
        elif k in t_lower or k in cb_lower:
            return "danger"

    # 2. Green (success) conditions:
    if (
        text.startswith("✅")
        or text.startswith("🟢")
        or (text.startswith("•") and text.endswith("•"))
    ):
        return "success"

    if (
        "on (" in t_lower
        or "(on)" in t_lower
        or "yoqilgan" in t_lower
        or "вкл" in t_lower
    ):
        return "success"

    success_keywords = [
        "start", "boshlash", "начать", "launch",
        "play", "o'ynash", "играть",
        "accept", "qabul", "принять",
        "add to group", "guruhga qo'shish", "добавить",
        "confirm", "tasdiqlash", "подтвердить",
        "continue", "davom", "продолжить",
        "next", "keyingi", "следующий",
        "save", "saqlash", "сохранить",
        "select all", "barchasini tanlash", "barcha rejim", "все режимы", "all modes", "hammasi",
        "tayyor", "ready", "готов",
    ]
    if any(k in t_lower or k in cb_lower for k in success_keywords):
        return "success"

    # 3. Default: Blue (primary) for all navigation, options, quiz answers, profiles, stats, etc.
    return "primary"


def _enrich_buttons(reply_markup: Any) -> bool:
    """
    Examines keyboard buttons and attaches icon_custom_emoji_id and style (color).
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

            cb_data = getattr(btn, "callback_data", "") or getattr(btn, "url", "")

            # Assign color style: determine semantic style
            current_style = getattr(btn, "style", None)
            if not current_style:
                btn.style = _determine_button_style(text, cb_data)
                modified = True
            elif (text.startswith("✅") or text.startswith("🟢")) and current_style != "success":
                btn.style = "success"
                modified = True
            elif (text.startswith("❌") or text.startswith("🔴") or "✖️" in text or text.strip() in ("—", "-", "✖️", "❌")) and current_style != "danger":
                btn.style = "danger"
                modified = True

            # If icon_custom_emoji_id is already set, skip icon logic
            if getattr(btn, "icon_custom_emoji_id", None):
                continue

            # Check for leading emoji
            m = LEADING_EMOJI_REGEX.match(text)
            if m:
                lead_emoji = m.group(1)
                clean_lead = lead_emoji.replace("\ufe0f", "")
                cid = EMOJI_TO_ID.get(lead_emoji) or EMOJI_TO_ID.get(clean_lead) or resolve_fallback_emoji_id(lead_emoji)
                if cid:
                    rem_text = text[m.end():].strip()
                    if rem_text:
                        btn.icon_custom_emoji_id = str(cid)
                        btn.text = rem_text
                        modified = True

    return modified


class CustomEmojiRequestMiddleware(BaseRequestMiddleware):
    """
    Middleware that intercepts outgoing Telegram API requests and:
    1. Upgrades standard emojis in HTML message texts and photo/media captions to animated <tg-emoji> tags.
    2. Attaches icon_custom_emoji_id and color style to buttons.
    3. Provides automatic fallback retry if Telegram Bot API returns an error on custom emojis or button styles.
    """

    async def __call__(self, make_request, bot, request):
        # 1. Transform message text or photo/media caption
        try:
            if isinstance(request, (SendMessage, EditMessageText)):
                if getattr(request, "text", None):
                    request.text = apply_custom_emojis(request.text)
                    if "<tg-emoji" in request.text and (getattr(request, "parse_mode", None) is None or isinstance(getattr(request, "parse_mode", None), Default)):
                        request.parse_mode = "HTML"
            elif isinstance(request, (SendPhoto, SendAnimation, SendVideo, SendAudio, SendDocument, SendVoice, EditMessageCaption)):
                if getattr(request, "caption", None):
                    request.caption = apply_custom_emojis(request.caption)
                    if "<tg-emoji" in request.caption and (getattr(request, "parse_mode", None) is None or isinstance(getattr(request, "parse_mode", None), Default)):
                        request.parse_mode = "HTML"
        except Exception as e:
            logger.debug(f"Error applying custom emojis to text: {e}")

        # 2. Enrich buttons with icon_custom_emoji_id and color style
        orig_reply_markup = None
        rm = getattr(request, "reply_markup", None)
        if rm:
            try:
                # Save backup in case Telegram rejects icon_custom_emoji_id or style
                orig_reply_markup = copy.deepcopy(rm)
                _enrich_buttons(rm)
            except Exception as e:
                logger.debug(f"Error enriching keyboard buttons: {e}")

        # 3. Make request with fallback protection
        try:
            return await make_request(bot, request)
        except Exception as err:
            err_msg = str(err).lower()
            # If rejected by Telegram due to button parameter restrictions
            if orig_reply_markup and ("emoji" in err_msg or "button" in err_msg or "icon" in err_msg or "style" in err_msg):
                logger.warning(f"Telegram rejected button styling: {err}. Retrying with original buttons.")
                request.reply_markup = orig_reply_markup
                return await make_request(bot, request)
            raise
