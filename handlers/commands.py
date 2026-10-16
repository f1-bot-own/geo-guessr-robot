"""
Bot Command Handlers for GeoGuru & GeoGuessr Telegram Bot.
Includes: /start, /help, /game, /stop, /solo, /daily, /profile, /leaderboard, /top, /language, /duel.
"""

import json
from datetime import datetime
from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from locales.i18n import t, get_rank_name
from database.db import Database, format_user_mention
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.daily_session import DailyChallengeSession
from games.manager import game_manager
from games.flow import send_round_question, send_solo_round, send_daily_round
from keyboards.menu_kb import get_main_menu_kb, get_language_kb, get_miniapp_launch_kb
from keyboards.game_kb import (
    get_setup_kb,
    get_duel_kb,
    get_category_selection_kb,
    get_game_type_kb,
    get_leaderboard_kb,
)
import config

router = Router()

from .bot_compat import get_db

@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    """
    Handle /start command.
    CRITICAL: Default language is strictly English ('en') on start!
    """
    db = get_db(bot)
    user = message.from_user
    chat = message.chat

    if chat.type in ("group", "supergroup"):
        # Group chat registration
        chat_data = await db.get_or_create_chat(
            chat_id=chat.id,
            chat_type=chat.type,
            title=chat.title,
            default_lang="en"
        )
        lang = chat_data.get("language", "en")
        await message.reply(
            text=t("welcome_group", lang),
            parse_mode="HTML"
        )
    else:
        # Private chat registration (always defaults to 'en')
        user_data = await db.get_or_create_user(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            default_lang="en"
        )
        lang = user_data.get("language", "en")
        bot_info = await bot.get_me()

        # Handle deep links like /start solo or /start daily
        text_parts = (message.text or "").strip().split()
        if len(text_parts) > 1:
            arg = text_parts[1].lower()
            if arg == "solo":
                await cmd_solo(message, bot)
                return
            elif arg == "daily":
                await cmd_daily(message, bot)
                return
        
        await message.answer(
            text=t("welcome_private", lang),
            reply_markup=get_main_menu_kb(lang, bot_username=bot_info.username),
            parse_mode="HTML"
        )

@router.message(Command("help"))
async def cmd_help(message: Message, bot: Bot):
    """Display comprehensive bot commands and gameplay guide."""
    db = get_db(bot)
    lang = "en"
    if message.chat.type in ("group", "supergroup"):
        lang = await db.get_chat_language(message.chat.id)
    else:
        user_data = await db.get_user(message.from_user.id)
        if user_data:
            lang = user_data.get("language", "en")

    await message.reply(
        text=t("help_text", lang),
        parse_mode="HTML"
    )

@router.message(Command("game", "startgame"))
async def cmd_game(message: Message, bot: Bot):
    """
    Start or configure a game match.
    In groups: presents interactive game setup menu with host-only authorization.
    In private: directs user to game type selection.
    """
    db = get_db(bot)
    chat = message.chat
    user = message.from_user

    if chat.type not in ("group", "supergroup"):
        # Suggest game type selection in private
        user_data = await db.get_user(user.id)
        lang = user_data.get("language", "en") if user_data else "en"
        bot_info = await bot.get_me()
        await message.answer(
            text=t("choose_game_type", lang),
            reply_markup=get_game_type_kb(lang, bot_username=bot_info.username),
            parse_mode="HTML"
        )
        return

    # Check if a game is already active
    active_session = game_manager.get_session(chat.id)
    lang = await db.get_chat_language(chat.id)

    if active_session and active_session.status in ("in_progress", "setup", "between_rounds"):
        await message.reply(text=t("game_already_active", lang), parse_mode="HTML")
        return

    # Create new session in setup mode with host authorization
    user_name = user.first_name or user.username or "Host"
    text_parts = (message.text or "").strip().split()
    chosen_mode = "mix"
    chosen_continent = "all"
    modes = (
        "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview",
        "emoji", "contour", "blur", "president", "historical", "celebrity", "person", "logo", "mix"
    )
    continents = ("all", "asia", "europe", "africa", "americas", "oceania")
    for part in text_parts[1:]:
        p = part.lower()
        if p in modes:
            chosen_mode = p
        elif p in continents:
            chosen_continent = p

    session = GameSession(
        chat_id=chat.id,
        created_by_user_id=user.id,
        is_group=True,
        lang=lang,
        mode=chosen_mode,
        total_rounds=config.DEFAULT_ROUNDS,
        round_time=config.DEFAULT_ROUND_TIME,
        host_id=user.id,
        host_name=user_name,
        continent=chosen_continent
    )
    session.user_names[user.id] = user_name
    game_manager.set_session(chat.id, session)

    kb = get_setup_kb(
        session_id=session.session_id,
        mode=session.mode,
        rounds=session.total_rounds,
        round_time=session.round_time,
        lang=lang,
        input_mode=session.input_mode,
        continent=session.continent
    )

    setup_title = t("game_setup_host_title", lang, host=user_name)
    await message.answer(
        text=setup_title,
        reply_markup=kb,
        parse_mode="HTML"
    )

@router.message(Command("emoji"))
async def cmd_emoji(message: Message, bot: Bot):
    """Direct shortcut command to launch an Emoji Riddle game."""
    message.text = "/game emoji"
    await cmd_game(message, bot)

@router.message(Command("contour", "silhouette"))
async def cmd_contour(message: Message, bot: Bot):
    """Direct shortcut command to launch a Country Contour game."""
    message.text = "/game contour"
    await cmd_game(message, bot)

@router.message(Command("blur", "xira"))
async def cmd_blur(message: Message, bot: Bot):
    """Direct shortcut command to launch a Blur Reveal game."""
    message.text = "/game blur"
    await cmd_game(message, bot)

@router.message(Command("president", "prezident"))
async def cmd_president(message: Message, bot: Bot):
    """Direct shortcut command to launch a Presidents & Leaders game."""
    message.text = "/game president"
    await cmd_game(message, bot)

@router.message(Command("history", "tarix"))
async def cmd_history(message: Message, bot: Bot):
    """Direct shortcut command to launch a Historical Figures game."""
    message.text = "/game historical"
    await cmd_game(message, bot)

@router.message(Command("celebrity", "stars", "yulduzlar", "mashhurlar"))
async def cmd_celebrity(message: Message, bot: Bot):
    """Direct shortcut command to launch a Celebrities game."""
    message.text = "/game celebrity"
    await cmd_game(message, bot)

@router.message(Command("person", "shaxs", "kimbu"))
async def cmd_person(message: Message, bot: Bot):
    """Direct shortcut command to launch a Famous People game."""
    message.text = "/game person"
    await cmd_game(message, bot)

@router.message(Command("logo", "brend"))
async def cmd_logo(message: Message, bot: Bot):
    """Direct shortcut command to launch a Logo Guessr game."""
    message.text = "/game logo"
    await cmd_game(message, bot)

@router.message(Command("stop"))
async def cmd_stop(message: Message, bot: Bot):
    """Abort the active game session."""
    db = get_db(bot)
    chat = message.chat
    user = message.from_user
    lang = await db.get_chat_language(chat.id) if chat.type in ("group", "supergroup") else "en"

    active_session = game_manager.get_session(chat.id)
    solo_session = game_manager.get_solo_session(user.id)

    if not active_session and not solo_session:
        await message.reply(text=t("no_game_active", lang), parse_mode="HTML")
        return

    if active_session:
        active_session.stop()
        if active_session.round_message_id:
            try:
                await bot.edit_message_reply_markup(chat_id=chat.id, message_id=active_session.round_message_id, reply_markup=None)
            except Exception:
                pass
        active_session.current_kb = None
        game_manager.remove_session(chat.id)

    if solo_session:
        solo_session.stop()
        if solo_session.round_message_id:
            try:
                await bot.edit_message_reply_markup(chat_id=user.id, message_id=solo_session.round_message_id, reply_markup=None)
            except Exception:
                pass
        solo_session.current_kb = None
        game_manager.remove_solo_session(user.id)
    
    user_name = user.first_name or user.username or "Admin"
    await message.answer(text=t("game_stopped", lang, user=user_name), parse_mode="HTML")

@router.message(Command("solo"))
async def cmd_solo(message: Message, bot: Bot):
    """Launch solo practice mode with category selection."""
    db = get_db(bot)
    user = message.from_user

    if message.chat.type in ("group", "supergroup"):
        bot_info = await bot.get_me()
        await message.reply(
            text=f"🕹 <b>Solo mode is played in private chat!</b>\n👉 <a href='https://t.me/{bot_info.username}?start=solo'>Click here to play Solo</a>",
            parse_mode="HTML"
        )
        return

    user_data = await db.get_or_create_user(user.id, user.username, user.first_name, default_lang="en")
    lang = user_data.get("language", "en")

    # Stop any existing running solo session cleanly
    existing = game_manager.get_solo_session(user.id)
    if existing:
        existing.stop()
        game_manager.remove_solo_session(user.id)

    # Check if a category, duration, and/or input mode argument was provided (e.g., /solo flag, /solo 60, /solo text, /solo flag 60 text)
    text_parts = (message.text or "").strip().split()
    chosen_mode = None
    chosen_time = config.DEFAULT_ROUND_TIME
    chosen_input = None
    modes = (
        "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview",
        "emoji", "contour", "blur", "president", "historical", "celebrity", "person", "logo", "mix"
    )
    input_modes = ("buttons", "text", "both")

    for part in text_parts[1:]:
        p = part.lower()
        if p in modes:
            chosen_mode = p
        elif p.isdigit() and int(p) in (30, 60):
            chosen_time = int(p)
        elif p in input_modes:
            chosen_input = p

    saved_state = game_manager.get_solo_setup_state(user.id)
    if chosen_input:
        saved_state["input_mode"] = chosen_input
        game_manager.set_solo_setup_state(user.id, saved_state)
    effective_input_mode = chosen_input or saved_state.get("input_mode", "both")

    if chosen_mode or (len(text_parts) > 1 and chosen_time in (30, 60)) or chosen_input:
        if not chosen_mode:
            chosen_mode = "mix"

        solo_session = SoloGameSession(
            user_id=user.id,
            user_name=user.first_name or "Player",
            lang=lang,
            mode=chosen_mode,
            round_time=chosen_time,
            input_mode=effective_input_mode
        )
        game_manager.set_solo_session(user.id, solo_session)
        solo_session.next_round()
        await send_solo_round(bot, user.id, solo_session, db)
    else:
        # Cleanly present all categories as buttons for the player to choose
        await message.answer(
            text=t("choose_category", lang),
            reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=effective_input_mode),
            parse_mode="HTML"
        )

@router.message(Command("daily"))
async def cmd_daily(message: Message, bot: Bot):
    """Daily Geography Challenge: 5 seeded questions with streak tracking."""
    db = get_db(bot)
    user = message.from_user

    if message.chat.type in ("group", "supergroup"):
        bot_info = await bot.get_me()
        await message.reply(
            text=f"📅 <b>Daily Challenge is played in private chat!</b>\n👉 <a href='https://t.me/{bot_info.username}?start=daily'>Click here to play today's Daily Challenge</a>",
            parse_mode="HTML"
        )
        return

    user_data = await db.get_or_create_user(user.id, user.username, user.first_name, default_lang="en")
    lang = user_data.get("language", "en")

    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    can_play = await db.can_play_daily(user.id, today_str)

    if not can_play:
        record = await db.check_daily_challenge_done(user.id, today_str)
        prev_score = record.get("score", 0) if record else 100
        await message.reply(
            text=t("daily_already_done", lang, score=prev_score),
            parse_mode="HTML"
        )
        return

    # Start 5-round seeded daily challenge
    daily_session = DailyChallengeSession(
        user_id=user.id,
        user_name=user.first_name or "Player",
        lang=lang,
        date_str=today_str
    )
    game_manager.set_daily_session(user.id, daily_session)

    await message.answer(
        text=f"{t('daily_title', lang)}\n🎯 <i>5 unique questions for today! Answer all to earn bonus XP & increase your daily streak!</i>",
        parse_mode="HTML"
    )
    await send_daily_round(bot, user.id, daily_session)

@router.message(Command("profile"))
async def cmd_profile(message: Message, bot: Bot):
    """Show player statistics, XP, level, rank, and badges."""
    db = get_db(bot)
    user = message.from_user
    user_data = await db.get_or_create_user(user.id, user.username, user.first_name, default_lang="en")
    lang = user_data.get("language", "en")

    level = user_data.get("level", 1)
    xp = user_data.get("xp", 0)
    games = user_data.get("games_played", 0)
    wins = user_data.get("games_won", 0)
    correct = user_data.get("correct_answers", 0)
    total_answers = user_data.get("total_answers", 0)
    streak = user_data.get("best_streak", 0)
    accuracy = int((correct / max(1, total_answers)) * 100) if total_answers > 0 else 0
    rank = get_rank_name(level, lang)

    user_name = user.first_name or user.username or "Player"
    text = (
        f"{t('profile_title', lang, name=user_name)}\n\n"
        f"{t('profile_details', lang, rank=rank, level=level, xp=xp, games=games, wins=wins, correct=correct, total=total_answers, accuracy=accuracy, streak=streak)}"
    )

    await message.reply(text=text, parse_mode="HTML")

def format_leaderboard_text(players: list, lb_type: str = "global", period: str = "all_time", lang: str = "en") -> str:
    """Format global or group leaderboard with clickable profile mentions and localized period title."""
    period_title_key = f"leaderboard_period_{period}"
    period_name = t(period_title_key, lang)
    if lb_type == "global":
        title = t("leaderboard_global_title_period", lang, period=period_name)
    else:
        title = t("leaderboard_group_title_period", lang, period=period_name)

    if not players:
        return f"{title}\n\n{t('empty_leaderboard_period', lang)}"

    rows = [title, ""]
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    for idx, player in enumerate(players):
        medal = medals[idx] if idx < len(medals) else f"{idx + 1}."
        user_id = player.get("user_id")
        raw_name = player.get("first_name") or player.get("username") or f"Player {user_id}"
        mention = format_user_mention(user_id, raw_name)
        if lb_type == "global":
            score = player.get("total_score", 0)
            lvl = player.get("level", 1)
            rows.append(f"{medal} {mention} — <b>{score} pts</b> (Lvl {lvl})")
        else:
            score = player.get("score", 0)
            wins = player.get("wins", 0)
            rows.append(f"{medal} {mention} — <b>{score} pts</b> (🏆 {wins} wins)")
    return "\n".join(rows)

@router.message(Command("leaderboard"))
async def cmd_leaderboard(message: Message, bot: Bot):
    """Show global top 10 geography players with period switching."""
    db = get_db(bot)
    user = message.from_user
    user_data = await db.get_user(user.id)
    lang = user_data.get("language", "en") if user_data else "en"

    args = (message.text or "").strip().split()[1:]
    period = "all_time"
    if args:
        a = args[0].lower()
        if a in ("daily", "day", "kunlik", "день"):
            period = "daily"
        elif a in ("weekly", "week", "haftalik", "неделя"):
            period = "weekly"
        elif a in ("monthly", "month", "oylik", "месяц"):
            period = "monthly"
        elif a in ("all", "alltime", "all_time", "barcha", "asosiy", "все"):
            period = "all_time"

    top_players = await db.get_global_leaderboard(limit=10, period=period)
    text = format_leaderboard_text(top_players, lb_type="global", period=period, lang=lang)
    kb = get_leaderboard_kb(lb_type="global", current_period=period, lang=lang)
    await message.reply(text=text, reply_markup=kb, parse_mode="HTML")

@router.message(Command("top"))
async def cmd_top(message: Message, bot: Bot):
    """Show group chat top 10 leaderboard with period switching."""
    db = get_db(bot)
    chat = message.chat

    if chat.type not in ("group", "supergroup"):
        # Forward to global leaderboard in private
        await cmd_leaderboard(message, bot)
        return

    lang = await db.get_chat_language(chat.id)

    args = (message.text or "").strip().split()[1:]
    period = "all_time"
    if args:
        a = args[0].lower()
        if a in ("daily", "day", "kunlik", "день"):
            period = "daily"
        elif a in ("weekly", "week", "haftalik", "неделя"):
            period = "weekly"
        elif a in ("monthly", "month", "oylik", "месяц"):
            period = "monthly"
        elif a in ("all", "alltime", "all_time", "barcha", "asosiy", "все"):
            period = "all_time"

    top_players = await db.get_group_leaderboard(chat.id, limit=10, period=period)
    text = format_leaderboard_text(top_players, lb_type="group", period=period, lang=lang)
    kb = get_leaderboard_kb(lb_type="group", current_period=period, lang=lang)
    await message.reply(text=text, reply_markup=kb, parse_mode="HTML")

@router.message(Command("language", "lang"))
async def cmd_language(message: Message, bot: Bot):
    """Change user or chat language, supporting direct language argument (e.g. /language uz)."""
    db = get_db(bot)
    args = (message.text or "").strip().split()[1:]
    if args:
        chosen = args[0].lower().strip().lstrip("@").split("@")[0]
        lang_map = {
            "uz": "uz", "uzbek": "uz", "o'zbek": "uz", "oʻzbek": "uz", "uzbekcha": "uz",
            "ru": "ru", "rus": "ru", "russian": "ru", "рус": "ru", "русский": "ru",
            "en": "en", "eng": "en", "english": "en", "анг": "en", "английский": "en"
        }
        if chosen in lang_map:
            new_lang = lang_map[chosen]
            lang_names = {"en": "English 🇬🇧", "ru": "Русский 🇷🇺", "uz": "O'zbekcha 🇺🇿"}
            lang_name = lang_names.get(new_lang, new_lang)
            if message.chat.type in ("group", "supergroup"):
                await db.set_chat_language(message.chat.id, new_lang)
                active_session = game_manager.get_session(message.chat.id)
                if active_session:
                    active_session.lang = new_lang
                try:
                    from game.engine import game_manager as engine_gm
                    eng_session = engine_gm.get_group_game(message.chat.id)
                    if eng_session:
                        eng_session.lang = new_lang
                except Exception:
                    pass
            else:
                await db.set_user_language(message.from_user.id, new_lang)
                active_solo = game_manager.get_solo_session(message.from_user.id)
                if active_solo:
                    active_solo.lang = new_lang
                try:
                    from game.engine import game_manager as engine_gm
                    eng_solo = engine_gm.get_solo_game(message.from_user.id)
                    if eng_solo:
                        eng_solo.lang = new_lang
                except Exception:
                    pass

            confirmation = t("lang_changed", new_lang, lang_name=lang_name)
            await message.reply(text=confirmation, parse_mode="HTML")
            return

    lang = "en"
    if message.chat.type in ("group", "supergroup"):
        lang = await db.get_chat_language(message.chat.id)
    else:
        user_data = await db.get_user(message.from_user.id)
        if user_data:
            lang = user_data.get("language", "en")

    await message.reply(
        text=t("choose_lang", lang),
        reply_markup=get_language_kb(),
        parse_mode="HTML"
    )

@router.message(Command("duel"))
async def cmd_duel(message: Message, bot: Bot):
    """Challenge a chat member to a 1v1 geography duel."""
    db = get_db(bot)
    chat = message.chat
    challenger = message.from_user

    if chat.type not in ("group", "supergroup"):
        await message.reply("⚔️ Duels can only be played in group chats! Add me to a group to duel friends.")
        return

    lang = await db.get_chat_language(chat.id)

    # Check target
    target_user = None
    if message.reply_to_message and message.reply_to_message.from_user:
        target_user = message.reply_to_message.from_user
    elif message.entities:
        # Check text mention
        for ent in message.entities:
            if ent.type == "text_mention" and ent.user:
                target_user = ent.user
                break

    if not target_user or target_user.id == challenger.id or target_user.is_bot:
        await message.reply("⚔️ Reply to a player's message with <code>/duel</code> to challenge them!")
        return

    # Check active game
    if game_manager.get_session(chat.id):
        await message.reply(t("game_already_active", lang), parse_mode="HTML")
        return

    # Create duel in database
    challenger_name = challenger.first_name or challenger.username or "Challenger"
    target_name = target_user.first_name or target_user.username or "Target"
    duel_id = await db.create_duel(
        chat_id=chat.id,
        challenger_id=challenger.id,
        challenger_name=challenger_name,
        opponent_id=target_user.id,
        opponent_name=target_name
    )

    # Create pending duel invite
    game_manager.set_duel_invite(chat.id, {
        "duel_id": duel_id,
        "challenger_id": challenger.id,
        "challenger_name": challenger_name,
        "target_id": target_user.id,
        "target_name": target_name,
        "lang": lang
    })

    c_mention = format_user_mention(challenger.id, challenger_name)
    t_mention = format_user_mention(target_user.id, target_name)
    text = t(
        "duel_invite",
        lang,
        challenger=c_mention,
        target=t_mention
    )
    await message.answer(
        text=text,
        reply_markup=get_duel_kb(challenger.id, target_user.id, lang, duel_id=duel_id),
        parse_mode="HTML"
    )


@router.message(Command("miniapp", "map"))
async def cmd_miniapp(message: Message, bot: Bot):
    """Launch or explain the GeoGuessr Telegram Mini App."""
    db = get_db(bot)
    user_data = await db.get_user(message.from_user.id)
    lang = user_data.get("language", "en") if user_data else "en"

    await message.answer(
        text=t("miniapp_intro", lang),
        reply_markup=get_miniapp_launch_kb(lang),
        parse_mode="HTML"
    )


@router.message(F.web_app_data)
async def handle_miniapp_data(message: Message, bot: Bot):
    """
    Handle score and match completion payload sent back from GeoGuessr Telegram Mini App.
    Awards user XP, updates user statistics, and posts a celebratory summary in the chat.
    """
    db = get_db(bot)
    user = message.from_user
    user_data = await db.get_user(user.id)
    lang = user_data.get("language", "en") if user_data else "en"

    try:
        raw_data = message.web_app_data.data
        data = json.loads(raw_data)
        if data.get("action") == "miniapp_score":
            score = int(data.get("total_score", 0))
            rank = data.get("rank", "Explorer")
            # Proportional XP reward: up to 500 XP
            xp_awarded = min(500, max(25, int(score / 50)))

            user_name = user.first_name or user.username or "Player"
            await db.record_answer(
                user_id=user.id,
                is_correct=True,
                points=score,
                xp=xp_awarded,
                user_name=user_name,
                username=user.username
            )

            await message.reply(
                text=t("miniapp_result_msg", lang, score=f"{score:,}", rank=rank, xp=xp_awarded),
                reply_markup=get_miniapp_launch_kb(lang),
                parse_mode="HTML"
            )
            return
    except Exception as exc:
        pass
