"""
Menu Keyboards for Private Chat and Language Selection.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from locales.i18n import t

def get_main_menu_kb(lang: str = "en", bot_username: str = "") -> InlineKeyboardMarkup:
    """Generate main interactive menu keyboard."""
    add_group_url = f"https://t.me/{bot_username}?startgroup=true" if bot_username else "https://t.me"
    
    keyboard = [
        [
            InlineKeyboardButton(text=t("btn_play_game", lang), callback_data="menu:play")
        ],
        [
            InlineKeyboardButton(text=t("btn_play_solo", lang), callback_data="menu:solo"),
            InlineKeyboardButton(text=t("btn_group_game", lang), url=add_group_url)
        ],
        [
            InlineKeyboardButton(text=t("btn_daily", lang), callback_data="menu:daily")
        ],
        [
            InlineKeyboardButton(text=t("btn_profile", lang), callback_data="menu:profile"),
            InlineKeyboardButton(text=t("btn_leaderboard", lang), callback_data="menu:leaderboard")
        ],
        [
            InlineKeyboardButton(text=t("btn_language", lang), callback_data="menu:language"),
            InlineKeyboardButton(text=t("btn_help", lang), callback_data="menu:help")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_language_kb() -> InlineKeyboardMarkup:
    """Generate language selection keyboard."""
    keyboard = [
        [
            InlineKeyboardButton(text="🇬🇧 English", callback_data="set_lang:en"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="set_lang:ru"),
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="set_lang:uz")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
