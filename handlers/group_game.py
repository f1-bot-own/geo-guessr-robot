"""
Multiplayer and Group game handlers for GeoGuru & GeoGuessr Telegram Bot.
Includes setup lobby, interactive round flow, timers, scoring, and podium celebrations.
"""
import asyncio
from typing import Optional, Dict, Any, List
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    DEFAULT_ROUNDS,
    DEFAULT_ROUND_TIME,
    MIN_ROUNDS,
    MAX_ROUNDS,
    MIN_ROUND_TIME,
    MAX_ROUND_TIME,
    XP_PER_CORRECT,
    XP_PER_WIN,
    POINTS_WRONG_PENALTY
)
from locales.i18n import t
from database.db import (
    get_user_language,
    record_answer_result,
    record_match_player_stats,
    record_match,
    format_user_mention
)
from game.engine import game_manager, GroupGameSession, AnswerResult
from game.modes import Question
from keyboards.inline import get_game_setup_keyboard, get_question_keyboard
from games.flow import send_resilient_photo

router = Router(name="group_game")

AVAILABLE_MODES = ["mix", "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview"]
ROUNDS_OPTIONS = [3, 5, 10, 15, 20]
TIME_OPTIONS = [30, 60]

@router.message(Command("game"))
async def handle_game_command(message: Message):
    """Launch game setup or alert if a match is already underway."""
    chat_id = message.chat.id
    lang = await get_user_language(message.from_user.id)

    # Check if a game is currently playing
    active_game = game_manager.get_group_game(chat_id)
    if active_game and active_game.is_active:
        await message.answer(t("game_already_active", lang))
        return

    host_id = message.from_user.id
    host_name = message.from_user.full_name or message.from_user.first_name or "Host"

    # Initialize setup lobby settings
    game_manager.setup_states[chat_id] = {
        "host_id": host_id,
        "host_name": host_name,
        "mode": "mix",
        "rounds": DEFAULT_ROUNDS,
        "time": DEFAULT_ROUND_TIME,
        "lang": lang,
        "input_mode": "both"
    }

    setup_kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode="mix",
        rounds=DEFAULT_ROUNDS,
        time_sec=DEFAULT_ROUND_TIME,
        lang=lang,
        input_mode="both"
    )

    setup_title = t("game_setup_host_title", lang, host=host_name)
    await message.answer(
        setup_title,
        reply_markup=setup_kb,
        parse_mode="HTML"
    )

@router.callback_query(F.data == "menu_group_game")
async def handle_menu_group_game(callback: CallbackQuery):
    """Callback shortcut for starting group game."""
    chat_id = callback.message.chat.id
    lang = await get_user_language(callback.from_user.id)

    active_game = game_manager.get_group_game(chat_id)
    if active_game and active_game.is_active:
        await callback.answer(t("game_already_active", lang), show_alert=True)
        return

    host_id = callback.from_user.id
    host_name = callback.from_user.full_name or callback.from_user.first_name or "Host"

    game_manager.setup_states[chat_id] = {
        "host_id": host_id,
        "host_name": host_name,
        "mode": "mix",
        "rounds": DEFAULT_ROUNDS,
        "time": DEFAULT_ROUND_TIME,
        "lang": lang,
        "input_mode": "both"
    }

    setup_kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode="mix",
        rounds=DEFAULT_ROUNDS,
        time_sec=DEFAULT_ROUND_TIME,
        lang=lang,
        input_mode="both"
    )

    setup_title = t("game_setup_host_title", lang, host=host_name)
    await callback.message.answer(
        setup_title,
        reply_markup=setup_kb,
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data.startswith("setup_set_mode:"))
async def set_mode_callback(callback: CallbackQuery):
    parts = callback.data.split(":")
    chat_id = int(parts[1])
    target_mode = parts[2]
    state = game_manager.setup_states.get(chat_id)
    if not state:
        await callback.answer("Setup expired. Type /game again.")
        return

    host_id = state.get("host_id")
    if host_id and callback.from_user.id != host_id:
        await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
        return

    if target_mode in AVAILABLE_MODES:
        state["mode"] = target_mode

    kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode=state["mode"],
        rounds=state["rounds"],
        time_sec=state["time"],
        lang=state["lang"]
    )
    try:
        await callback.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass
    await callback.answer()

@router.callback_query(F.data.startswith("setup_set_time:"))
async def set_time_callback(callback: CallbackQuery):
    parts = callback.data.split(":")
    chat_id = int(parts[1])
    target_time = int(parts[2])
    state = game_manager.setup_states.get(chat_id)
    if not state:
        await callback.answer("Setup expired. Type /game again.")
        return

    host_id = state.get("host_id")
    if host_id and callback.from_user.id != host_id:
        await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
        return

    if target_time in TIME_OPTIONS:
        state["time"] = target_time

    kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode=state["mode"],
        rounds=state["rounds"],
        time_sec=state["time"],
        lang=state["lang"],
        input_mode=state.get("input_mode", "both")
    )
    try:
        await callback.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass
    await callback.answer()

@router.callback_query(F.data.startswith("setup_set_input:"))
async def set_input_callback(callback: CallbackQuery):
    parts = callback.data.split(":")
    chat_id = int(parts[1])
    target_input = parts[2]
    state = game_manager.setup_states.get(chat_id)
    if not state:
        await callback.answer("Setup expired. Type /game again.")
        return

    host_id = state.get("host_id")
    if host_id and callback.from_user.id != host_id:
        await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
        return

    if target_input in ["buttons", "text", "both"]:
        state["input_mode"] = target_input

    kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode=state["mode"],
        rounds=state["rounds"],
        time_sec=state["time"],
        lang=state["lang"],
        input_mode=state.get("input_mode", "both")
    )
    try:
        await callback.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass
    await callback.answer()

@router.callback_query(F.data.startswith("setup_cycle_mode:"))
async def cycle_mode_callback(callback: CallbackQuery):
    chat_id = int(callback.data.split(":")[1])
    state = game_manager.setup_states.get(chat_id)
    if not state:
        await callback.answer("Setup expired. Type /game again.")
        return

    host_id = state.get("host_id")
    if host_id and callback.from_user.id != host_id:
        await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
        return

    curr_mode = state["mode"]
    next_idx = (AVAILABLE_MODES.index(curr_mode) + 1) % len(AVAILABLE_MODES)
    state["mode"] = AVAILABLE_MODES[next_idx]

    kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode=state["mode"],
        rounds=state["rounds"],
        time_sec=state["time"],
        lang=state["lang"],
        input_mode=state.get("input_mode", "both")
    )
    try:
        await callback.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass
    await callback.answer()

@router.callback_query(F.data.startswith("setup_cycle_rounds:"))
async def cycle_rounds_callback(callback: CallbackQuery):
    chat_id = int(callback.data.split(":")[1])
    state = game_manager.setup_states.get(chat_id)
    if not state:
        await callback.answer("Setup expired. Type /game again.")
        return

    host_id = state.get("host_id")
    if host_id and callback.from_user.id != host_id:
        await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
        return

    curr_rounds = state["rounds"]
    curr_idx = ROUNDS_OPTIONS.index(curr_rounds) if curr_rounds in ROUNDS_OPTIONS else 0
    next_idx = (curr_idx + 1) % len(ROUNDS_OPTIONS)
    state["rounds"] = ROUNDS_OPTIONS[next_idx]

    kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode=state["mode"],
        rounds=state["rounds"],
        time_sec=state["time"],
        lang=state["lang"],
        input_mode=state.get("input_mode", "both")
    )
    try:
        await callback.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass
    await callback.answer()

@router.callback_query(F.data.startswith("setup_cycle_time:"))
async def cycle_time_callback(callback: CallbackQuery):
    chat_id = int(callback.data.split(":")[1])
    state = game_manager.setup_states.get(chat_id)
    if not state:
        await callback.answer("Setup expired. Type /game again.")
        return

    host_id = state.get("host_id")
    if host_id and callback.from_user.id != host_id:
        await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
        return

    curr_time = state["time"]
    curr_idx = TIME_OPTIONS.index(curr_time) if curr_time in TIME_OPTIONS else 0
    next_idx = (curr_idx + 1) % len(TIME_OPTIONS)
    state["time"] = TIME_OPTIONS[next_idx]

    kb = get_game_setup_keyboard(
        chat_id=chat_id,
        mode=state["mode"],
        rounds=state["rounds"],
        time_sec=state["time"],
        lang=state["lang"],
        input_mode=state.get("input_mode", "both")
    )
    try:
        await callback.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass
    await callback.answer()

@router.callback_query(F.data.startswith("setup_cancel:"))
async def setup_cancel_callback(callback: CallbackQuery):
    chat_id = int(callback.data.split(":")[1])
    state = game_manager.setup_states.get(chat_id)
    if state:
        host_id = state.get("host_id")
        if host_id and callback.from_user.id != host_id:
            await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
            return

    if chat_id in game_manager.setup_states:
        del game_manager.setup_states[chat_id]
    try:
        await callback.message.delete()
    except Exception:
        pass
    await callback.answer("Game setup cancelled.")

@router.callback_query(F.data.startswith("setup_launch:"))
async def setup_launch_callback(callback: CallbackQuery, bot: Bot):
    chat_id = int(callback.data.split(":")[1])
    state = game_manager.setup_states.get(chat_id)
    if not state:
        await callback.answer("Setup expired. Type /game again.")
        return

    host_id = state.get("host_id")
    if host_id and callback.from_user.id != host_id:
        await callback.answer(t("host_only_settings_alert", state.get("lang", "en")), show_alert=True)
        return

    # Delete lobby message
    try:
        await callback.message.delete()
    except Exception:
        pass

    # Create new session
    session = GroupGameSession(
        chat_id=chat_id,
        mode=state["mode"],
        total_rounds=state["rounds"],
        round_time=state["time"],
        lang=state["lang"],
        host_id=host_id,
        host_name=state.get("host_name", ""),
        input_mode=state.get("input_mode", "both")
    )
    game_manager.set_group_game(chat_id, session)
    if chat_id in game_manager.setup_states:
        del game_manager.setup_states[chat_id]

    await callback.answer("Starting game!")
    await launch_next_round(chat_id, bot)

async def launch_next_round(chat_id: int, bot: Bot):
    """Generate question, send it with options, and start round timer."""
    session = game_manager.get_group_game(chat_id)
    if not session or not session.is_active:
        return

    question = session.start_next_round()
    lang = session.lang
    mode_name = t(f"mode_{question.mode}", lang)

    indicator = t(
        "round_indicator",
        lang,
        current=session.current_round,
        total=session.total_rounds,
        mode=mode_name,
        time=session.round_time
    )

    caption = f"{indicator}\n\n{question.prompt}"
    if question.extra_info and question.mode == "landmark":
        caption += f"\n\n{question.extra_info}"

    keyboard = None if session.input_mode == "text" else get_question_keyboard(session.current_round, question.options, prefix="ans")

    sent_msg = None
    if question.media_url and question.media_type == "photo":
        try:
            sent_msg = await send_resilient_photo(
                bot=bot,
                chat_id=chat_id,
                photo_url=question.media_url,
                caption=caption,
                reply_markup=keyboard,
                parse_mode="HTML"
            )
        except Exception:
            pass
        if not sent_msg:
            # Fallback to text message if photo delivery fails
            sent_msg = await bot.send_message(
                chat_id=chat_id,
                text=caption,
                reply_markup=keyboard,
                parse_mode="HTML"
            )
    else:
        sent_msg = await bot.send_message(
            chat_id=chat_id,
            text=caption,
            reply_markup=keyboard,
            parse_mode="HTML"
        )

    if sent_msg:
        session.message_id = sent_msg.message_id

    # Launch round timer
    round_num = session.current_round
    session.timer_task = asyncio.create_task(
        round_timer(chat_id, round_num, session.round_time, bot)
    )

async def round_timer(chat_id: int, round_num: int, duration: int, bot: Bot):
    """Timer coroutine that triggers when round time expires."""
    try:
        await asyncio.sleep(duration)
    except asyncio.CancelledError:
        return

    session = game_manager.get_group_game(chat_id)
    if not session or session.current_round != round_num or not session.is_round_active:
        return

    # Time's up!
    correct_ans, is_game_over = session.handle_timeout()
    lang = session.lang
    current_q = session.current_question

    if session.message_id:
        try:
            await bot.edit_message_reply_markup(chat_id=chat_id, message_id=session.message_id, reply_markup=None)
        except Exception:
            pass

    timeout_text = t("time_up_announcement", lang, answer=correct_ans)
    if current_q and getattr(current_q, "extra_info", None) and current_q.mode == "streetview":
        timeout_text += f"\n\n{current_q.extra_info}"
    await bot.send_message(chat_id=chat_id, text=timeout_text, parse_mode="HTML")

    if is_game_over:
        await finish_game(chat_id, bot)
    else:
        await bot.send_message(chat_id=chat_id, text=t("next_round_in", lang, seconds=3), parse_mode="HTML")
        await asyncio.sleep(3)
        await launch_next_round(chat_id, bot)

@router.callback_query(F.data.startswith("ans:"))
async def handle_game_answer(callback: CallbackQuery, bot: Bot):
    """Handle tap on a question option button in multiplayer match."""
    parts = callback.data.split(":")
    round_idx = int(parts[1])
    option_id = parts[2]
    chat_id = callback.message.chat.id
    user_id = callback.from_user.id
    user_name = callback.from_user.full_name or callback.from_user.first_name or "Player"

    session = game_manager.get_group_game(chat_id)
    if not session or not session.is_active:
        await callback.answer("No active game in this chat.", show_alert=False)
        return

    if getattr(session, "input_mode", "both") == "text":
        await callback.answer("Text-only mode is active! Type your answer in chat.", show_alert=True)
        return

    if session.current_round != round_idx or not session.is_round_active:
        await callback.answer("This round has already finished!", show_alert=False)
        return

    res = session.process_answer(user_id=user_id, user_name=user_name, option_id=option_id)
    lang = session.lang

    if res.status == "already_answered":
        await callback.answer(t("already_answered_wrong", lang, user=user_name), show_alert=True)
        return

    if res.status == "not_participant":
        await callback.answer("Only duel participants can answer!", show_alert=True)
        return

    if res.status == "wrong":
        await record_answer_result(user_id, is_correct=False)
        await callback.answer(t("wrong_answer_alert", lang, penalty=res.penalty), show_alert=True)
        return

    if res.status == "correct":
        # Correct answer!
        await callback.answer()
        await record_answer_result(user_id, is_correct=True, xp_earned=XP_PER_CORRECT)

        current_q = session.current_question
        user_mention = format_user_mention(user_id, user_name)
        # Announce round victory
        announce = t(
            "correct_answer_announcement",
            lang,
            user=user_mention,
            time=res.elapsed_time,
            points=res.points_awarded,
            answer=res.correct_answer_text
        )
        if current_q and getattr(current_q, "extra_info", None) and current_q.mode == "streetview":
            announce += f"\n\n{current_q.extra_info}"
        await bot.send_message(chat_id=chat_id, text=announce, parse_mode="HTML")

        # Disable keyboard on answered question
        try:
            await callback.message.edit_reply_markup(reply_markup=None)
        except Exception:
            pass

        if res.is_game_over:
            await finish_game(chat_id, bot)
        else:
            await bot.send_message(chat_id=chat_id, text=t("next_round_in", lang, seconds=3), parse_mode="HTML")
            await asyncio.sleep(3)
            await launch_next_round(chat_id, bot)

async def finish_game(chat_id: int, bot: Bot):
    """Calculate final standings, announce podium, and update records."""
    session = game_manager.get_group_game(chat_id)
    if not session:
        return

    lang = session.lang
    standings = session.get_standings()
    lines = [t("game_over_title", lang), "", t("final_standings_header", lang), ""]

    winner_id = None
    winner_name = ""
    winner_score = 0

    if standings:
        for idx, (uid, uname, score) in enumerate(standings, start=1):
            u_mention = format_user_mention(uid, uname)
            if idx == 1:
                winner_id = uid
                winner_name = uname
                winner_score = score
                lines.append(t("podium_first", lang, user=u_mention, score=score))
                # Award winner bonus XP
                await record_match_player_stats(uid, chat_id, uname, is_win=True, score=score, xp_bonus=XP_PER_WIN)
            elif idx == 2:
                lines.append(t("podium_second", lang, user=u_mention, score=score))
                await record_match_player_stats(uid, chat_id, uname, is_win=False, score=score, xp_bonus=XP_PER_WIN // 2)
            elif idx == 3:
                lines.append(t("podium_third", lang, user=u_mention, score=score))
                await record_match_player_stats(uid, chat_id, uname, is_win=False, score=score, xp_bonus=XP_PER_WIN // 4)
            else:
                lines.append(t("standing_row", lang, pos=idx, user=u_mention, score=score))
                await record_match_player_stats(uid, chat_id, uname, is_win=False, score=score, xp_bonus=10)
    else:
        lines.append(t("no_scores", lang))

    # Log match history
    await record_match(
        chat_id=chat_id,
        mode=session.mode,
        winner_id=winner_id,
        winner_name=winner_name,
        winner_score=winner_score,
        players_count=len(standings)
    )

    # Clean up session
    game_manager.remove_group_game(chat_id)
    await bot.send_message(chat_id=chat_id, text="\n".join(lines), parse_mode="HTML")

@router.message(Command("stop"))
async def handle_stop_game(message: Message):
    """Abort currently active match in this chat."""
    chat_id = message.chat.id
    lang = await get_user_language(message.from_user.id)
    session = game_manager.get_group_game(chat_id)

    if not session or not session.is_active:
        await message.answer(t("no_game_active", lang))
        return

    session.stop()
    game_manager.remove_group_game(chat_id)
    user_name = message.from_user.full_name or "User"
    await message.answer(t("game_stopped", lang, user=user_name))
