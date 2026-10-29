"""
Menu Keyboards for Private Chat, Language Selection, and Mini App.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from locales.i18n import t
import config

def get_miniapp_button(lang: str = "en") -> InlineKeyboardButton:
    """Create Mini App WebAppInfo button if valid HTTPS URL configured, else callback button."""
    if config.WEBAPP_URL and config.WEBAPP_URL.startswith("https://"):
        return InlineKeyboardButton(
            text=t("btn_miniapp", lang),
            web_app=WebAppInfo(url=config.WEBAPP_URL),
            style="primary"
        )
    return InlineKeyboardButton(
        text=t("btn_miniapp", lang),
        callback_data="menu:miniapp",
        style="primary"
    )

def get_miniapp_launch_kb(lang: str = "en") -> InlineKeyboardMarkup:
    """Generate keyboard with standalone Mini App launch button."""
    if config.WEBAPP_URL and config.WEBAPP_URL.startswith("https://"):
        btn = InlineKeyboardButton(
            text=t("btn_miniapp_launch", lang),
            web_app=WebAppInfo(url=config.WEBAPP_URL),
            style="success"
        )
    else:
        btn = InlineKeyboardButton(
            text=t("btn_miniapp_launch", lang),
            callback_data="menu:miniapp_info",
            style="success"
        )
    return InlineKeyboardMarkup(inline_keyboard=[[btn]])

def get_main_menu_kb(lang: str = "en", bot_username: str = "") -> InlineKeyboardMarkup:
    """Generate main interactive menu keyboard."""
    add_group_url = f"https://t.me/{bot_username}?startgroup=true" if bot_username else "https://t.me"
    
    keyboard = [
        [
            InlineKeyboardButton(text=t("btn_play_game", lang), callback_data="menu:play", style="success")
        ],
        [
            InlineKeyboardButton(text=t("btn_play_solo", lang), callback_data="menu:solo", style="primary"),
            InlineKeyboardButton(text=t("btn_group_game", lang), url=add_group_url, style="primary")
        ],
        [
            InlineKeyboardButton(text=t("btn_daily", lang), callback_data="menu:daily", style="primary")
        ],
        [
            InlineKeyboardButton(text=t("btn_profile", lang), callback_data="menu:profile", style="primary"),
            InlineKeyboardButton(text=t("btn_leaderboard", lang), callback_data="menu:leaderboard", style="primary")
        ],
        [
            InlineKeyboardButton(text=t("btn_language", lang), callback_data="menu:language", style="primary"),
            InlineKeyboardButton(text=t("btn_help", lang), callback_data="menu:help", style="primary")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_language_kb() -> InlineKeyboardMarkup:
    """Generate language selection keyboard."""
    keyboard = [
        [
            InlineKeyboardButton(text="🇬🇧 English", callback_data="set_lang:en", style="primary"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="set_lang:ru", style="primary"),
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="set_lang:uz", style="success")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
