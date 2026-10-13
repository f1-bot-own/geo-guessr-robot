"""
Game Keyboards for Group Matches, Setup, Solo, and Duels.
"""

from typing import List, Set
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from locales.i18n import t
from games.models import GameMode

def get_setup_kb(
    session_id: str,
    mode: str = "mix",
    rounds: int = 5,
    round_time: int = 30,
    lang: str = "en",
    input_mode: str = "both"
) -> InlineKeyboardMarkup:
    """Generate game setup parameters keyboard with explicit categories, 30s/60s timers, and input mode."""
    def mode_btn(m_code: str):
        prefix = "✅ " if mode == m_code else ""
        return InlineKeyboardButton(
            text=f"{prefix}{t(f'mode_{m_code}', lang)}",
            callback_data=f"setup:mode:{m_code}:{session_id}"
        )

    t30_prefix = "✅ " if round_time == 30 else ""
    t60_prefix = "✅ " if round_time == 60 else ""

    btn_buttons_pfx = "✅ " if input_mode == "buttons" else ""
    btn_text_pfx = "✅ " if input_mode == "text" else ""
    btn_both_pfx = "✅ " if input_mode == "both" else ""

    keyboard = [
        # Explicit Category selection buttons
        [mode_btn("flag"), mode_btn("capital")],
        [mode_btn("landmark"), mode_btn("higher_lower")],
        [mode_btn("coat_of_arms"), mode_btn("streetview")],
        [mode_btn("mix")],
        # Explicit 30s / 60s timer buttons
        [
            InlineKeyboardButton(
                text=f"{t30_prefix}{t('btn_timer_30s', lang)}",
                callback_data=f"setup:time:30:{session_id}"
            ),
            InlineKeyboardButton(
                text=f"{t60_prefix}{t('btn_timer_60s', lang)}",
                callback_data=f"setup:time:60:{session_id}"
            )
        ],
        # Input mode selection: Buttons Only / Text Only / Both
        [
            InlineKeyboardButton(
                text=f"{btn_buttons_pfx}{t('btn_input_buttons', lang)}",
                callback_data=f"setup:input:buttons:{session_id}"
            ),
            InlineKeyboardButton(
                text=f"{btn_text_pfx}{t('btn_input_text', lang)}",
                callback_data=f"setup:input:text:{session_id}"
            ),
            InlineKeyboardButton(
                text=f"{btn_both_pfx}{t('btn_input_both', lang)}",
                callback_data=f"setup:input:both:{session_id}"
            )
        ],
        # Rounds selector
        [
            InlineKeyboardButton(
                text=t("btn_rounds", lang, rounds=rounds),
                callback_data=f"setup:rounds:{session_id}"
            )
        ],
        # Launch & Cancel
        [
            InlineKeyboardButton(
                text=t("btn_start_now", lang),
                callback_data=f"setup:start:{session_id}"
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_cancel", lang),
                callback_data=f"setup:cancel:{session_id}"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_category_selection_kb(
    prefix: str = "solo_cat",
    lang: str = "en",
    input_mode: str = "both"
) -> InlineKeyboardMarkup:
    """Generate keyboard for selecting a category and input mode for solo mode."""
    btn_buttons_pfx = "✅ " if input_mode == "buttons" else ""
    btn_text_pfx = "✅ " if input_mode == "text" else ""
    btn_both_pfx = "✅ " if input_mode == "both" else ""

    keyboard = [
        [
            InlineKeyboardButton(text=t("mode_flag", lang), callback_data=f"{prefix}:flag"),
            InlineKeyboardButton(text=t("mode_capital", lang), callback_data=f"{prefix}:capital")
        ],
        [
            InlineKeyboardButton(text=t("mode_landmark", lang), callback_data=f"{prefix}:landmark"),
            InlineKeyboardButton(text=t("mode_higher_lower", lang), callback_data=f"{prefix}:higher_lower")
        ],
        [
            InlineKeyboardButton(text=t("mode_coat_of_arms", lang), callback_data=f"{prefix}:coat_of_arms"),
            InlineKeyboardButton(text=t("mode_streetview", lang), callback_data=f"{prefix}:streetview")
        ],
        [
            InlineKeyboardButton(text=t("mode_mix", lang), callback_data=f"{prefix}:mix")
        ],
        [
            InlineKeyboardButton(
                text=f"{btn_buttons_pfx}{t('btn_input_buttons', lang)}",
                callback_data=f"{prefix}:input:buttons"
            ),
            InlineKeyboardButton(
                text=f"{btn_text_pfx}{t('btn_input_text', lang)}",
                callback_data=f"{prefix}:input:text"
            ),
            InlineKeyboardButton(
                text=f"{btn_both_pfx}{t('btn_input_both', lang)}",
                callback_data=f"{prefix}:input:both"
            )
        ],
        [
            InlineKeyboardButton(text=t("btn_back", lang), callback_data=f"{prefix}:back")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_solo_setup_kb(
    mode: str = "mix",
    round_time: int = 30,
    input_mode: str = "both",
    lang: str = "en"
) -> InlineKeyboardMarkup:
    """Generate interactive solo setup lobby keyboard."""
    def mode_btn(m_code: str):
        pfx = "✅ " if mode == m_code else ""
        return InlineKeyboardButton(
            text=f"{pfx}{t(f'mode_{m_code}', lang)}",
            callback_data=f"solo_setup:mode:{m_code}"
        )

    t30_pfx = "✅ " if round_time == 30 else ""
    t60_pfx = "✅ " if round_time == 60 else ""

    btn_buttons_pfx = "✅ " if input_mode == "buttons" else ""
    btn_text_pfx = "✅ " if input_mode == "text" else ""
    btn_both_pfx = "✅ " if input_mode == "both" else ""

    keyboard = [
        [mode_btn("flag"), mode_btn("capital")],
        [mode_btn("landmark"), mode_btn("higher_lower")],
        [mode_btn("coat_of_arms"), mode_btn("streetview")],
        [mode_btn("mix")],
        [
            InlineKeyboardButton(
                text=f"{t30_pfx}{t('btn_timer_30s', lang)}",
                callback_data="solo_setup:time:30"
            ),
            InlineKeyboardButton(
                text=f"{t60_pfx}{t('btn_timer_60s', lang)}",
                callback_data="solo_setup:time:60"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{btn_buttons_pfx}{t('btn_input_buttons', lang)}",
                callback_data="solo_setup:input:buttons"
            ),
            InlineKeyboardButton(
                text=f"{btn_text_pfx}{t('btn_input_text', lang)}",
                callback_data="solo_setup:input:text"
            ),
            InlineKeyboardButton(
                text=f"{btn_both_pfx}{t('btn_input_both', lang)}",
                callback_data="solo_setup:input:both"
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_start_now", lang),
                callback_data="solo_setup:start"
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_cancel", lang),
                callback_data="solo_setup:cancel"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_game_type_kb(lang: str = "en", bot_username: str = "") -> InlineKeyboardMarkup:
    """Generate keyboard for selecting Game Type (Group vs Solo vs Daily)."""
    add_group_url = f"https://t.me/{bot_username}?startgroup=true" if bot_username else "https://t.me"
    keyboard = [
        [
            InlineKeyboardButton(text=t("btn_play_solo", lang), callback_data="game_type:solo"),
            InlineKeyboardButton(text=t("btn_group_game", lang), url=add_group_url)
        ],
        [
            InlineKeyboardButton(text=t("btn_daily", lang), callback_data="game_type:daily")
        ],
        [
            InlineKeyboardButton(text=t("btn_back", lang), callback_data="game_type:menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_question_kb(session_id: str, options: List[str]) -> InlineKeyboardMarkup:
    """Generate answer buttons for an active group round."""
    buttons = []
    # If 2 options (Higher/Lower)
    if len(options) == 2:
        keyboard = [
            [InlineKeyboardButton(text=options[0], callback_data=f"ans:{session_id}:0")],
            [InlineKeyboardButton(text=options[1], callback_data=f"ans:{session_id}:1")]
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    # 4 options in 2x2 grid
    keyboard = [
        [
            InlineKeyboardButton(text=options[0], callback_data=f"ans:{session_id}:0"),
            InlineKeyboardButton(text=options[1], callback_data=f"ans:{session_id}:1")
        ],
        [
            InlineKeyboardButton(text=options[2], callback_data=f"ans:{session_id}:2"),
            InlineKeyboardButton(text=options[3], callback_data=f"ans:{session_id}:3")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_solo_question_kb(
    options: List[str],
    eliminated: Set[int],
    has_hint: bool,
    has_5050: bool,
    lang: str = "en",
    text_only: bool = False
) -> InlineKeyboardMarkup:
    """Generate solo question buttons with lifelines. In text_only mode, option buttons are omitted."""
    lifeline_row = []
    if has_hint:
        lifeline_row.append(InlineKeyboardButton(text=t("solo_btn_hint", lang), callback_data="solo_hint"))
    else:
        lifeline_row.append(InlineKeyboardButton(text="💡 ✖️", callback_data="solo_ignore"))

    if has_5050:
        lifeline_row.append(InlineKeyboardButton(text=t("solo_btn_5050", lang), callback_data="solo_5050"))
    else:
        lifeline_row.append(InlineKeyboardButton(text="✂️ ✖️", callback_data="solo_ignore"))

    if text_only:
        return InlineKeyboardMarkup(inline_keyboard=[lifeline_row])

    def make_btn(idx: int):
        if idx in eliminated:
            return InlineKeyboardButton(text="✖️", callback_data="solo_ignore")
        return InlineKeyboardButton(text=options[idx], callback_data=f"solo_ans:{idx}")

    if len(options) == 2:
        option_rows = [
            [make_btn(0)],
            [make_btn(1)]
        ]
    else:
        option_rows = [
            [make_btn(0), make_btn(1)],
            [make_btn(2), make_btn(3)]
        ]

    option_rows.append(lifeline_row)
    return InlineKeyboardMarkup(inline_keyboard=option_rows)

def get_daily_question_kb(options: List[str]) -> InlineKeyboardMarkup:
    """Generate answer buttons for a daily challenge round."""
    if len(options) == 2:
        keyboard = [
            [InlineKeyboardButton(text=options[0], callback_data="daily_ans:0")],
            [InlineKeyboardButton(text=options[1], callback_data="daily_ans:1")]
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    keyboard = [
        [
            InlineKeyboardButton(text=options[0], callback_data="daily_ans:0"),
            InlineKeyboardButton(text=options[1], callback_data="daily_ans:1")
        ],
        [
            InlineKeyboardButton(text=options[2], callback_data="daily_ans:2"),
            InlineKeyboardButton(text=options[3], callback_data="daily_ans:3")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_duel_kb(challenger_id: int, target_id: int, lang: str = "en", duel_id: int = 0) -> InlineKeyboardMarkup:
    """Generate duel challenge acceptance keyboard."""
    keyboard = [
        [
            InlineKeyboardButton(
                text=t("duel_accept", lang),
                callback_data=f"duel:accept:{challenger_id}:{target_id}:{duel_id}"
            ),
            InlineKeyboardButton(
                text=t("duel_decline", lang),
                callback_data=f"duel:decline:{challenger_id}:{target_id}:{duel_id}"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
