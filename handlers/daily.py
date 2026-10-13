"""
Daily Geography Challenge handler for GeoGuru & GeoGuessr.
Provides 5 daily seeded geography questions with XP bonuses.
"""
from datetime import date
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from locales.i18n import t
from database.db import (
    get_user_language,
    check_daily_challenge_done,
    record_daily_challenge_done,
    record_answer_result
)
from game.engine import game_manager, DailyChallengeSession
from keyboards.inline import get_question_keyboard
from games.flow import send_resilient_photo

router = Router(name="daily")

@router.message(Command("daily"))
async def handle_daily_command(message: Message, bot: Bot):
    """Start or view today's daily geography challenge."""
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    today_str = date.today().isoformat()

    # Check if already played today
    completed = await check_daily_challenge_done(user_id, today_str)
    if completed:
        msg = t("daily_already_done", lang, score=completed.get("score", 0))
        await message.answer(f"{t('daily_title', lang)}\n\n{msg}", parse_mode="HTML")
        return

    # In group chat, invite to complete daily in PM
    if message.chat.type in ["group", "supergroup"]:
        bot_info = await bot.get_me()
        bot_username = bot_info.username or ""
        await message.answer(
            f"📅 <b>Daily Challenge</b> is played privately!\n\n👉 <a href='https://t.me/{bot_username}?start=daily'>Click here to play today's challenge</a>",
            parse_mode="HTML"
        )
        return

    await start_daily_challenge(message.chat.id, user_id, today_str, lang, bot)

@router.callback_query(F.data == "menu_daily")
async def handle_menu_daily(callback: CallbackQuery, bot: Bot):
    """Start daily challenge from menu button."""
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    today_str = date.today().isoformat()

    completed = await check_daily_challenge_done(user_id, today_str)
    if completed:
        msg = t("daily_already_done", lang, score=completed.get("score", 0))
        await callback.message.answer(f"{t('daily_title', lang)}\n\n{msg}", parse_mode="HTML")
        await callback.answer()
        return

    if callback.message.chat.type in ["group", "supergroup"]:
        bot_info = await bot.get_me()
        bot_username = bot_info.username or ""
        await callback.message.answer(
            f"📅 <b>Daily Challenge</b> is played privately!\n\n👉 <a href='https://t.me/{bot_username}?start=daily'>Click here to play today's challenge</a>",
            parse_mode="HTML"
        )
        await callback.answer()
        return

    await callback.answer()
    await start_daily_challenge(callback.message.chat.id, user_id, today_str, lang, bot)

async def start_daily_challenge(chat_id: int, user_id: int, today_str: str, lang: str, bot: Bot):
    """Create session and send first daily question."""
    session = DailyChallengeSession(user_id=user_id, date_seed=today_str, lang=lang)
    game_manager.set_daily_game(user_id, session)
    await send_daily_question(chat_id, session, bot)

async def send_daily_question(chat_id: int, session: DailyChallengeSession, bot: Bot):
    """Send current question of the daily challenge."""
    q = session.start_next_round()
    if not q:
        return

    lang = session.lang
    round_header = f"{t('daily_title', lang)}\n📍 <b>Question {session.round_num + 1}/{session.total_rounds}</b> | Score: <b>{session.score}</b>\n\n{q.prompt}"
    if q.extra_info and q.mode == "landmark":
        round_header += f"\n\n{q.extra_info}"

    kb = get_question_keyboard(session.round_num, q.options, prefix="daily_ans")

    if q.media_url and q.media_type == "photo":
        try:
            sent_msg = await send_resilient_photo(chat_id=chat_id, photo_url=q.media_url, caption=round_header, reply_markup=kb, parse_mode="HTML", bot=bot)
            if sent_msg:
                return
        except Exception:
            pass

    await bot.send_message(chat_id=chat_id, text=round_header, reply_markup=kb, parse_mode="HTML")

@router.callback_query(F.data.startswith("daily_ans:"))
async def handle_daily_answer(callback: CallbackQuery, bot: Bot):
    """Process answer in daily challenge."""
    parts = callback.data.split(":")
    round_idx = int(parts[1])
    option_id = parts[2]
    user_id = callback.from_user.id

    session = game_manager.get_daily_game(user_id)
    if not session or not session.is_active or session.round_num != round_idx:
        await callback.answer("This question has expired.", show_alert=False)
        return

    is_correct, is_complete, correct_ans = session.process_answer(option_id)
    lang = session.lang

    # Record streak / answer
    await record_answer_result(user_id, is_correct=is_correct, xp_earned=25 if is_correct else 0)

    try:
        await callback.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    if is_correct:
        await callback.answer("🎯 Correct! +100 pts", show_alert=False)
        await callback.message.answer(f"✅ <b>Correct!</b> (Score: {session.score})", parse_mode="HTML")
    else:
        await callback.answer("❌ Wrong!", show_alert=False)
        await callback.message.answer(f"❌ <b>Incorrect!</b> The answer was: <b>{correct_ans}</b>", parse_mode="HTML")

    if is_complete:
        # Finish daily challenge and award +150 bonus XP
        bonus_xp = 150
        await record_daily_challenge_done(
            user_id=user_id,
            score=session.score,
            xp_bonus=bonus_xp,
            challenge_date=session.date_seed
        )
        game_manager.remove_daily_game(user_id)

        finish_msg = t("daily_completed_msg", lang, score=session.score, xp=bonus_xp)
        await callback.message.answer(finish_msg, parse_mode="HTML")
    else:
        await send_daily_question(callback.message.chat.id, session, bot)
