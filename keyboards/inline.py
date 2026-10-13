"""
Inline keyboards for GeoGuru & GeoGuessr Telegram Bot.
"""
from typing import List, Set, Dict, Optional
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from locales.i18n import t
from game.modes import QuestionOption

def get_language_keyboard() -> InlineKeyboardMarkup:
    """Keyboard for selecting bot language."""
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="set_lang:en")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="set_lang:ru")],
        [InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="set_lang:uz")],
    ])
    return kb

def get_start_keyboard(lang: str = "en", is_group: bool = False, bot_username: str = "") -> InlineKeyboardMarkup:
    """Main menu keyboard for private or group chat."""
    if is_group:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=t("btn_mode", lang, mode="Mix / Setup"), callback_data="menu_group_game")],
            [
                InlineKeyboardButton(text=t("btn_leaderboard", lang), callback_data="menu_group_top"),
                InlineKeyboardButton(text=t("btn_language", lang), callback_data="menu_language")
            ],
            [InlineKeyboardButton(text=t("btn_help", lang), callback_data="menu_help")]
        ])
    
    # Private chat keyboard
    add_group_url = f"https://t.me/{bot_username}?startgroup=true" if bot_username else "https://t.me"
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t("btn_play_game", lang), callback_data="menu:play")
        ],
        [
            InlineKeyboardButton(text=t("btn_play_solo", lang), callback_data="menu_solo"),
            InlineKeyboardButton(text=t("btn_daily", lang), callback_data="menu_daily"),
        ],
        [
            InlineKeyboardButton(text=t("btn_profile", lang), callback_data="menu_profile"),
            InlineKeyboardButton(text=t("btn_leaderboard", lang), callback_data="menu_leaderboard"),
        ],
        [
            InlineKeyboardButton(text=t("btn_add_to_group", lang), url=add_group_url),
        ],
        [
            InlineKeyboardButton(text=t("btn_language", lang), callback_data="menu_language"),
            InlineKeyboardButton(text=t("btn_help", lang), callback_data="menu_help"),
        ]
    ])

def get_game_setup_keyboard(chat_id: int, mode: str, rounds: int, time_sec: int, lang: str = "en", input_mode: str = "both") -> InlineKeyboardMarkup:
    """Setup lobby keyboard for configuring group match with all categories, 30s/60s timers, and input mode."""
    def mode_btn(m_code: str):
        prefix = "✅ " if mode == m_code else ""
        return InlineKeyboardButton(
            text=f"{prefix}{t(f'mode_{m_code}', lang)}",
            callback_data=f"setup_set_mode:{chat_id}:{m_code}"
        )

    t30_prefix = "✅ " if time_sec == 30 else ""
    t60_prefix = "✅ " if time_sec == 60 else ""

    btn_buttons_pfx = "✅ " if input_mode == "buttons" else ""
    btn_text_pfx = "✅ " if input_mode == "text" else ""
    btn_both_pfx = "✅ " if input_mode == "both" else ""

    return InlineKeyboardMarkup(inline_keyboard=[
        # Categories
        [mode_btn("flag"), mode_btn("capital")],
        [mode_btn("landmark"), mode_btn("higher_lower")],
        [mode_btn("coat_of_arms"), mode_btn("streetview")],
        [mode_btn("mix")],
        # Explicit 30s and 60s timer buttons
        [
            InlineKeyboardButton(text=f"{t30_prefix}{t('btn_timer_30s', lang)}", callback_data=f"setup_set_time:{chat_id}:30"),
            InlineKeyboardButton(text=f"{t60_prefix}{t('btn_timer_60s', lang)}", callback_data=f"setup_set_time:{chat_id}:60"),
        ],
        # Input Mode selector
        [
            InlineKeyboardButton(text=f"{btn_buttons_pfx}{t('btn_input_buttons', lang)}", callback_data=f"setup_set_input:{chat_id}:buttons"),
            InlineKeyboardButton(text=f"{btn_text_pfx}{t('btn_input_text', lang)}", callback_data=f"setup_set_input:{chat_id}:text"),
            InlineKeyboardButton(text=f"{btn_both_pfx}{t('btn_input_both', lang)}", callback_data=f"setup_set_input:{chat_id}:both"),
        ],
        # Rounds
        [InlineKeyboardButton(text=t("btn_rounds", lang, rounds=rounds), callback_data=f"setup_cycle_rounds:{chat_id}")],
        # Launch & Cancel
        [InlineKeyboardButton(text=t("btn_start_now", lang), callback_data=f"setup_launch:{chat_id}")],
        [InlineKeyboardButton(text=t("btn_cancel", lang), callback_data=f"setup_cancel:{chat_id}")],
    ])

def get_question_keyboard(round_idx: int, options: List[QuestionOption], prefix: str = "ans") -> InlineKeyboardMarkup:
    """Construct keyboard for question answers."""
    # 2 buttons per row for compact clean UI
    buttons = []
    row = []
    for opt in options:
        btn = InlineKeyboardButton(text=opt.text, callback_data=f"{prefix}:{round_idx}:{opt.id}")
        row.append(btn)
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_solo_keyboard(
    round_idx: int,
    options: List[QuestionOption],
    disabled_ids: Set[str],
    lifelines: Dict[str, bool],
    lang: str = "en",
    text_only: bool = False
) -> Optional[InlineKeyboardMarkup]:
    """Construct solo question keyboard including lifelines."""
    buttons = []
    if not text_only:
        row = []
        for opt in options:
            if opt.id in disabled_ids:
                btn = InlineKeyboardButton(text="—", callback_data="solo_disabled")
            else:
                btn = InlineKeyboardButton(text=opt.text, callback_data=f"solo_ans:{round_idx}:{opt.id}")
            row.append(btn)
            if len(row) == 2:
                buttons.append(row)
                row = []
        if row:
            buttons.append(row)
    
    # Lifelines row
    lifeline_row = []
    if lifelines.get("hint"):
        lifeline_row.append(InlineKeyboardButton(text=t("solo_btn_hint", lang), callback_data="solo_use_hint"))
    if lifelines.get("5050"):
        lifeline_row.append(InlineKeyboardButton(text=t("solo_btn_5050", lang), callback_data="solo_use_5050"))
    
    if lifeline_row:
        buttons.append(lifeline_row)

    if not buttons:
        return None
        
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_duel_invite_keyboard(duel_id: int, lang: str = "en") -> InlineKeyboardMarkup:
    """Keyboard for duel invitation acceptance."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t("duel_accept", lang), callback_data=f"duel_acc:{duel_id}"),
            InlineKeyboardButton(text=t("duel_decline", lang), callback_data=f"duel_dec:{duel_id}")
        ]
    ])
