"""
Common command handlers: /start, /help, /language, /profile, /leaderboard, /top.
Ensures default language is English on start as requested.
"""
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from config import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES
from locales.i18n import t, get_rank_name
from database.db import (
    get_or_create_user,
    set_user_language,
    get_user_language,
    set_chat_language,
    get_chat_language,
    get_user,
    get_global_leaderboard,
    get_group_leaderboard,
    calculate_level,
    format_user_mention
)
from keyboards.inline import get_start_keyboard, get_language_keyboard, get_leaderboard_kb

router = Router(name="common")

@router.message(CommandStart())
async def handle_start(message: Message):
    """
    Handle /start command.
    CRITICAL: Default language must be English ('en') on start as required.
    """
    user_id = message.from_user.id
    first_name = message.from_user.first_name or "Player"
    username = message.from_user.username or ""
    
    # Check if user already exists
    existing_user = await get_user(user_id)
    if existing_user:
        lang = existing_user.get("language") or DEFAULT_LANGUAGE
    else:
        # Explicitly ensure English is set as default upon start
        lang = DEFAULT_LANGUAGE
        await get_or_create_user(
            user_id=user_id,
            first_name=first_name,
            username=username,
            language=DEFAULT_LANGUAGE
        )

    is_group = message.chat.type in ["group", "supergroup"]
    bot_info = await message.bot.get_me()
    bot_username = bot_info.username or ""

    if is_group:
        welcome_text = t("welcome_group", lang)
    else:
        welcome_text = t("welcome_private", lang)

    keyboard = get_start_keyboard(lang=lang, is_group=is_group, bot_username=bot_username)
    await message.answer(welcome_text, reply_markup=keyboard, parse_mode="HTML")

@router.message(Command("help"))
async def handle_help(message: Message):
    """Handle /help command."""
    lang = await get_user_language(message.from_user.id)
    help_text = t("help_text", lang)
    await message.answer(help_text, parse_mode="HTML")

@router.message(Command("language"))
async def handle_language(message: Message):
    """Handle /language command to switch language."""
    lang = await get_user_language(message.from_user.id)
    prompt = t("choose_lang", lang)
    await message.answer(prompt, reply_markup=get_language_keyboard(), parse_mode="HTML")

@router.callback_query(F.data.startswith("set_lang:"))
async def handle_set_language_callback(callback: CallbackQuery):
    """Process language selection callback for both users and groups."""
    user_id = callback.from_user.id
    chat = callback.message.chat
    new_lang = callback.data.split(":")[1]
    
    if new_lang in SUPPORTED_LANGUAGES:
        if chat.type in ("group", "supergroup"):
            await set_chat_language(chat.id, new_lang)
            try:
                from games.manager import game_manager as gm
                active = gm.get_session(chat.id)
                if active:
                    active.lang = new_lang
            except Exception:
                pass
        else:
            await set_user_language(user_id, new_lang)

        lang_names = {"en": "English 🇬🇧", "ru": "Русский 🇷🇺", "uz": "O'zbekcha 🇺🇿"}
        confirmation = t("lang_changed", new_lang, lang_name=lang_names.get(new_lang, new_lang))
        await callback.answer()
        try:
            await callback.message.edit_text(confirmation, parse_mode="HTML")
        except Exception:
            await callback.message.answer(confirmation, parse_mode="HTML")
    else:
        await callback.answer("Unsupported language", show_alert=True)

@router.message(Command("profile"))
async def handle_profile(message: Message):
    """Handle /profile command: show user stats, level, XP, rank and streaks."""
    user_id = message.from_user.id
    user = await get_user(user_id)
    
    if not user:
        user = await get_or_create_user(
            user_id=user_id,
            first_name=message.from_user.first_name or "Player",
            username=message.from_user.username or "",
            language=DEFAULT_LANGUAGE
        )

    lang = user.get("language") or DEFAULT_LANGUAGE
    name = message.from_user.full_name or "Player"
    xp = user.get("xp", 0)
    level = calculate_level(xp)
    rank = get_rank_name(level, lang)
    games = user.get("games_played", 0)
    wins = user.get("games_won", 0)
    correct = user.get("correct_answers", 0)
    total = user.get("total_answers", 0)
    streak = user.get("best_streak", 0)
    accuracy = int((correct / total) * 100) if total > 0 else 0

    header = t("profile_title", lang, name=name)
    details = t(
        "profile_details",
        lang,
        rank=rank,
        level=level,
        xp=xp,
        games=games,
        wins=wins,
        correct=correct,
        total=total,
        accuracy=accuracy,
        streak=streak
    )

    text = f"{header}\n\n{details}"
    await message.answer(text, parse_mode="HTML")

@router.message(Command("leaderboard"))
async def handle_leaderboard(message: Message):
    """Handle /leaderboard: global top 10 players."""
    lang = await get_user_language(message.from_user.id)
    leaders = await get_global_leaderboard(10, period="all_time")
    
    from handlers.commands import format_leaderboard_text
    text = format_leaderboard_text(leaders, lb_type="global", period="all_time", lang=lang)
    kb = get_leaderboard_kb(lb_type="global", current_period="all_time", lang=lang)
    await message.answer(text, reply_markup=kb, parse_mode="HTML")

@router.message(Command("top"))
async def handle_group_top(message: Message):
    """Handle /top command: group leaderboard."""
    if message.chat.type not in ["group", "supergroup"]:
        await message.answer("👥 This command is for Telegram groups. Use /leaderboard for global ranking.")
        return

    lang = await get_user_language(message.from_user.id)
    leaders = await get_group_leaderboard(message.chat.id, 10, period="all_time")

    from handlers.commands import format_leaderboard_text
    text = format_leaderboard_text(leaders, lb_type="group", period="all_time", lang=lang)
    kb = get_leaderboard_kb(lb_type="group", current_period="all_time", lang=lang)
    await message.answer(text, reply_markup=kb, parse_mode="HTML")

# Callback shortcuts from start menu
@router.callback_query(F.data == "menu_language")
async def cb_menu_language(callback: CallbackQuery):
    lang = await get_user_language(callback.from_user.id)
    prompt = t("choose_lang", lang)
    await callback.message.answer(prompt, reply_markup=get_language_keyboard(), parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "menu_help")
async def cb_menu_help(callback: CallbackQuery):
    lang = await get_user_language(callback.from_user.id)
    await callback.message.answer(t("help_text", lang), parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "menu_profile")
async def cb_menu_profile(callback: CallbackQuery):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    lang = user.get("language") if user else DEFAULT_LANGUAGE
    name = callback.from_user.full_name or "Player"
    xp = user.get("xp", 0) if user else 0
    level = calculate_level(xp)
    rank = get_rank_name(level, lang)
    games = user.get("games_played", 0) if user else 0
    wins = user.get("games_won", 0) if user else 0
    correct = user.get("correct_answers", 0) if user else 0
    total = user.get("total_answers", 0) if user else 0
    streak = user.get("best_streak", 0) if user else 0
    accuracy = int((correct / total) * 100) if total > 0 else 0

    header = t("profile_title", lang, name=name)
    details = t("profile_details", lang, rank=rank, level=level, xp=xp, games=games, wins=wins, correct=correct, total=total, accuracy=accuracy, streak=streak)
    await callback.message.answer(f"{header}\n\n{details}", parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "menu_leaderboard")
async def cb_menu_leaderboard(callback: CallbackQuery):
    lang = await get_user_language(callback.from_user.id)
    leaders = await get_global_leaderboard(10, period="all_time")
    from handlers.commands import format_leaderboard_text
    text = format_leaderboard_text(leaders, lb_type="global", period="all_time", lang=lang)
    kb = get_leaderboard_kb(lb_type="global", current_period="all_time", lang=lang)
    await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "menu_group_top")
async def cb_menu_group_top(callback: CallbackQuery):
    if callback.message.chat.type not in ["group", "supergroup"]:
        await callback.answer("Only available in groups!", show_alert=True)
        return
    lang = await get_user_language(callback.from_user.id)
    leaders = await get_group_leaderboard(callback.message.chat.id, 10, period="all_time")
    from handlers.commands import format_leaderboard_text
    text = format_leaderboard_text(leaders, lb_type="group", period="all_time", lang=lang)
    kb = get_leaderboard_kb(lb_type="group", current_period="all_time", lang=lang)
    await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()
