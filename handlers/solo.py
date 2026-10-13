"""
Solo Practice Mode handler for GeoGuru & GeoGuessr.
Provides solo geography practice with 3 lives and 2 lifelines (Hint, 50/50).
"""
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from locales.i18n import t
from database.db import get_user_language, record_answer_result
from game.engine import game_manager, SoloGameSession
from keyboards.inline import get_solo_keyboard
from keyboards.game_kb import get_category_selection_kb
from games.flow import send_resilient_photo

router = Router(name="solo")

@router.message(Command("solo"))
async def handle_solo_command(message: Message, bot: Bot):
    """Start solo game mode with category selection."""
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    # In group chats, invite user to play solo in private chat
    if message.chat.type in ["group", "supergroup"]:
        bot_info = await bot.get_me()
        bot_username = bot_info.username or ""
        await message.answer(
            f"🕹 <b>Solo practice mode</b> is best played in private chat!\n\n👉 <a href='https://t.me/{bot_username}?start=solo'>Click here to play Solo</a>",
            parse_mode="HTML"
        )
        return

    text_parts = (message.text or "").strip().split()
    chosen_mode = None
    chosen_time = 30
    chosen_input = "both"
    modes = ["flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview", "mix"]
    for part in text_parts[1:]:
        p = part.lower()
        if p in modes:
            chosen_mode = p
        elif p.isdigit() and int(p) in (30, 60):
            chosen_time = int(p)
        elif p in ("buttons", "text", "both"):
            chosen_input = p

    if chosen_mode or (len(text_parts) > 1 and chosen_time in (30, 60)) or chosen_input != "both":
        if not chosen_mode:
            chosen_mode = "mix"
        await start_solo_game(message.chat.id, user_id, lang, bot, mode=chosen_mode, round_time=chosen_time, input_mode=chosen_input)
    else:
        await message.answer(
            text=t("choose_category", lang),
            reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=chosen_input),
            parse_mode="HTML"
        )

@router.callback_query(F.data == "menu_solo")
async def handle_menu_solo(callback: CallbackQuery, bot: Bot):
    """Start solo mode from menu button by presenting category selection."""
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)

    if callback.message.chat.type in ["group", "supergroup"]:
        bot_info = await bot.get_me()
        bot_username = bot_info.username or ""
        await callback.message.answer(
            f"🕹 <b>Solo practice mode</b> is best played in private chat!\n\n👉 <a href='https://t.me/{bot_username}?start=solo'>Click here to play Solo</a>",
            parse_mode="HTML"
        )
        await callback.answer()
        return

    await callback.answer()
    try:
        await callback.message.edit_text(
            text=t("choose_category", lang),
            reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang),
            parse_mode="HTML"
        )
    except Exception:
        await callback.message.answer(
            text=t("choose_category", lang),
            reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang),
            parse_mode="HTML"
        )

@router.callback_query(F.data.startswith("solo_cat:"))
async def handle_solo_category(callback: CallbackQuery, bot: Bot):
    """Handle category selection for solo mode."""
    parts = callback.data.split(":")
    cat = parts[1]
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    if cat == "back":
        await callback.answer()
        try:
            await callback.message.delete()
        except Exception:
            pass
        return

    if cat == "input":
        mode_val = parts[2] if len(parts) > 2 else "both"
        game_manager.set_solo_setup_state(user_id, {"input_mode": mode_val})
        try:
            from games.manager import game_manager as global_gm
            global_gm.set_solo_setup_state(user_id, {"input_mode": mode_val})
        except Exception:
            pass
        new_kb = get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=mode_val)
        try:
            await callback.message.edit_reply_markup(reply_markup=new_kb)
        except Exception:
            pass
        await callback.answer()
        return

    modes = ["flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview", "mix"]
    chosen_mode = cat if cat in modes else "mix"
    saved_state = game_manager.get_solo_setup_state(user_id)
    chosen_input = saved_state.get("input_mode", "both")

    await callback.answer(f"Starting {t(f'mode_{chosen_mode}', lang)}!")
    try:
        await callback.message.delete()
    except Exception:
        pass
    await start_solo_game(callback.message.chat.id, user_id, lang, bot, mode=chosen_mode, input_mode=chosen_input)

async def start_solo_game(chat_id: int, user_id: int, lang: str, bot: Bot, mode: str = "mix", round_time: int = 30, input_mode: str = "both"):
    """Initialize and send the first question of solo mode."""
    session = SoloGameSession(user_id=user_id, lang=lang, mode=mode, round_time=round_time, input_mode=input_mode)
    game_manager.set_solo_game(user_id, session)
    await send_solo_question(chat_id, session, bot)

async def send_solo_question(chat_id: int, session: SoloGameSession, bot: Bot):
    """Send current question with status bar and lifelines."""
    q = session.next_question()
    lang = session.lang

    lives_str = "❤️ " * session.lives
    status = t("solo_round_info", lang, round=session.round_num, score=session.score, lives=lives_str)
    header = f"{t('solo_title', lang)}\n{status}\n\n{q.prompt}"

    if q.extra_info and q.mode == "landmark":
        header += f"\n\n{q.extra_info}"

    kb = get_solo_keyboard(
        round_idx=session.round_num,
        options=q.options,
        disabled_ids=session.disabled_option_ids,
        lifelines=session.lifelines,
        lang=lang,
        text_only=(getattr(session, "input_mode", "both") == "text")
    )

    if session.timer_task and not session.timer_task.done():
        session.timer_task.cancel()

    sent_msg = None
    if q.media_url and q.media_type == "photo":
        try:
            sent_msg = await send_resilient_photo(bot=bot, chat_id=chat_id, photo_url=q.media_url, caption=header, reply_markup=kb, parse_mode="HTML")
        except Exception:
            pass

    if not sent_msg:
        sent_msg = await bot.send_message(chat_id=chat_id, text=header, reply_markup=kb, parse_mode="HTML")

    if sent_msg:
        session.message_id = sent_msg.message_id

@router.callback_query(F.data.startswith("solo_ans:"))
async def handle_solo_answer(callback: CallbackQuery, bot: Bot):
    """Handle option selection in solo mode."""
    parts = callback.data.split(":")
    round_idx = int(parts[1])
    option_id = parts[2]
    user_id = callback.from_user.id

    session = game_manager.get_solo_game(user_id)
    if not session or not session.is_active or session.round_num != round_idx:
        await callback.answer("This question is no longer active.", show_alert=False)
        return

    if getattr(session, "input_mode", "both") == "text":
        await callback.answer("Text-only mode is active! Type your answer in chat.", show_alert=True)
        return

    q = session.current_question
    is_correct, is_game_over, correct_ans = session.process_answer(option_id)
    lang = session.lang

    # Update database
    await record_answer_result(user_id, is_correct=is_correct, xp_earned=25 if is_correct else 0)

    # Disable buttons on answered message
    try:
        await callback.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    if is_correct:
        await callback.answer("🎯 Correct! +100 pts", show_alert=False)
        reveal_str = t("correct_answer_reveal", lang, answer=correct_ans)
        ans_text = f"✅ <b>Correct!</b>\n{reveal_str}\nScore: <b>{session.score} pts</b>"
        if q and getattr(q, "extra_info", None) and q.mode == "streetview":
            ans_text += f"\n\n{q.extra_info}"
        await callback.message.answer(ans_text, parse_mode="HTML")
        await send_solo_question(callback.message.chat.id, session, bot)
    else:
        await callback.answer("❌ Wrong answer!", show_alert=False)
        if is_game_over:
            game_over_msg = t(
                "solo_game_over",
                lang,
                score=session.score,
                correct=session.correct_count
            )
            text = t("solo_wrong_game_over_announcement", lang, answer=correct_ans, game_over=game_over_msg)
            if q and getattr(q, "extra_info", None) and q.mode == "streetview":
                text += f"\n\n{q.extra_info}"
            await callback.message.answer(text, parse_mode="HTML")
            game_manager.remove_solo_game(user_id)
        else:
            lives_left = "❤️ " * session.lives
            text = t("solo_wrong_answer_announcement", lang, answer=correct_ans, lives=lives_left)
            if q and getattr(q, "extra_info", None) and q.mode == "streetview":
                text += f"\n\n{q.extra_info}"
            await callback.message.answer(text, parse_mode="HTML")
            await send_solo_question(callback.message.chat.id, session, bot)

@router.callback_query(F.data == "solo_use_hint")
async def handle_solo_hint(callback: CallbackQuery):
    """Handle 💡 Hint lifeline button."""
    user_id = callback.from_user.id
    session = game_manager.get_solo_game(user_id)
    if not session or not session.is_active:
        await callback.answer("No active solo game.", show_alert=False)
        return

    hint_text = session.use_hint()
    if hint_text:
        await callback.answer(f"💡 Hint: {hint_text}", show_alert=True)
        # Refresh keyboard to remove hint button
        q = session.current_question
        if q:
            kb = get_solo_keyboard(
                session.round_num,
                q.options,
                session.disabled_option_ids,
                session.lifelines,
                session.lang,
                text_only=(getattr(session, "input_mode", "both") == "text")
            )
            try:
                await callback.message.edit_reply_markup(reply_markup=kb)
            except Exception:
                pass
    else:
        await callback.answer("Hint lifeline already used!", show_alert=True)

@router.callback_query(F.data == "solo_use_5050")
async def handle_solo_5050(callback: CallbackQuery):
    """Handle ✂️ 50/50 lifeline button."""
    user_id = callback.from_user.id
    session = game_manager.get_solo_game(user_id)
    if not session or not session.is_active:
        await callback.answer("No active solo game.", show_alert=False)
        return

    removed = session.use_5050()
    if removed:
        await callback.answer("✂️ 50/50 used! Two wrong answers eliminated.", show_alert=True)
        q = session.current_question
        if q:
            kb = get_solo_keyboard(
                session.round_num,
                q.options,
                session.disabled_option_ids,
                session.lifelines,
                session.lang,
                text_only=(getattr(session, "input_mode", "both") == "text")
            )
            try:
                await callback.message.edit_reply_markup(reply_markup=kb)
            except Exception:
                pass
    else:
        await callback.answer("50/50 lifeline already used!", show_alert=True)

@router.callback_query(F.data == "solo_disabled")
async def handle_solo_disabled(callback: CallbackQuery):
    await callback.answer("This option was removed by 50/50 lifeline!", show_alert=True)
