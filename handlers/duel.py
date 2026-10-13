"""
1v1 Geography Duel handler for GeoGuru & GeoGuessr.
Enables challenging members in Telegram groups to head-to-head 3-round matches.
"""
from typing import Dict, Any
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from locales.i18n import t
from database.db import (
    get_user_language,
    create_duel,
    get_duel,
    update_duel_status
)
from config import DEFAULT_ROUND_TIME
from game.engine import game_manager, GroupGameSession
from keyboards.inline import get_duel_invite_keyboard
from handlers.group_game import launch_next_round

router = Router(name="duel")

# Track in-memory pending duels
PENDING_DUELS: Dict[int, Dict[str, Any]] = {}

@router.message(Command("duel"))
async def handle_duel_command(message: Message):
    """Initiate a 1v1 duel in group chat."""
    if message.chat.type not in ["group", "supergroup"]:
        await message.answer("⚔️ Duels can only be played inside Telegram groups! Add me to a group to duel friends.")
        return

    challenger = message.from_user
    challenger_name = challenger.full_name or challenger.first_name
    lang = await get_user_language(challenger.id)

    target_user = None
    if message.reply_to_message and message.reply_to_message.from_user:
        target_user = message.reply_to_message.from_user

    if not target_user or target_user.id == challenger.id or target_user.is_bot:
        await message.answer(
            "⚔️ <b>How to start a Duel:</b>\nReply to any member's message in this group with <code>/duel</code> to challenge them to a 1v1 geography match!",
            parse_mode="HTML"
        )
        return

    opponent_name = target_user.full_name or target_user.first_name

    # Check if game already in progress in chat
    active_game = game_manager.get_group_game(message.chat.id)
    if active_game and active_game.is_active:
        await message.answer(t("game_already_active", lang))
        return

    duel_id = await create_duel(
        chat_id=message.chat.id,
        challenger_id=challenger.id,
        challenger_name=challenger_name,
        opponent_id=target_user.id,
        opponent_name=opponent_name
    )

    PENDING_DUELS[duel_id] = {
        "chat_id": message.chat.id,
        "challenger_id": challenger.id,
        "challenger_name": challenger_name,
        "opponent_id": target_user.id,
        "opponent_name": opponent_name,
        "lang": lang
    }

    invite_text = t("duel_invite", lang, challenger=f"<b>{challenger_name}</b>", target=f"<b>{opponent_name}</b>")
    kb = get_duel_invite_keyboard(duel_id, lang)
    await message.answer(invite_text, reply_markup=kb, parse_mode="HTML")

@router.callback_query(F.data.startswith("duel_acc:"))
async def handle_duel_accept(callback: CallbackQuery, bot: Bot):
    """Handle duel acceptance by opponent."""
    duel_id = int(callback.data.split(":")[1])
    duel = PENDING_DUELS.get(duel_id)
    if not duel:
        duel = await get_duel(duel_id)

    if not duel:
        await callback.answer("Duel expired.", show_alert=True)
        return

    user_id = callback.from_user.id
    if user_id != duel["opponent_id"]:
        await callback.answer("Only the challenged player can accept this duel!", show_alert=True)
        return

    chat_id = duel["chat_id"]
    lang = duel.get("lang", "en")

    await update_duel_status(duel_id, status="accepted")
    if duel_id in PENDING_DUELS:
        del PENDING_DUELS[duel_id]

    try:
        await callback.message.edit_text(
            f"⚔️ <b>Duel Accepted!</b>\n{duel['challenger_name']} vs {duel['opponent_name']}\n3 Rounds • Fastest correct answer wins!",
            parse_mode="HTML"
        )
    except Exception:
        pass

    # Launch duel game session
    session = GroupGameSession(
        chat_id=chat_id,
        mode="mix",
        total_rounds=3,
        round_time=DEFAULT_ROUND_TIME,
        lang=lang,
        duel_participants={duel["challenger_id"], duel["opponent_id"]}
    )
    game_manager.set_group_game(chat_id, session)

    await launch_next_round(chat_id, bot)
    await callback.answer()

@router.callback_query(F.data.startswith("duel_dec:"))
async def handle_duel_decline(callback: CallbackQuery):
    """Handle duel decline by opponent."""
    duel_id = int(callback.data.split(":")[1])
    duel = PENDING_DUELS.get(duel_id)
    if not duel:
        duel = await get_duel(duel_id)

    if not duel:
        await callback.answer("Duel expired.", show_alert=True)
        return

    user_id = callback.from_user.id
    if user_id != duel["opponent_id"] and user_id != duel["challenger_id"]:
        await callback.answer("You are not part of this duel!", show_alert=True)
        return

    lang = duel.get("lang", "en")
    await update_duel_status(duel_id, status="declined")
    if duel_id in PENDING_DUELS:
        del PENDING_DUELS[duel_id]

    try:
        await callback.message.edit_text(t("duel_declined", lang))
    except Exception:
        pass

    await callback.answer("Duel declined.")
