"""
Chat Member Events Handler.
Welcomes group members when the bot is added to a new chat.
"""

from aiogram import Router, Bot
from aiogram.types import ChatMemberUpdated
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, JOIN_TRANSITION
from database.db import Database
from locales.i18n import t

router = Router()

from .bot_compat import get_db

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def on_bot_added_to_group(event: ChatMemberUpdated, bot: Bot):
    """Triggered when the bot is added to a group or supergroup."""
    chat = event.chat
    if chat.type not in ("group", "supergroup"):
        return

    db: Database = get_db(bot)
    # Register chat with default English language ('en')
    chat_data = await db.get_or_create_chat(
        chat_id=chat.id,
        chat_type=chat.type,
        title=chat.title,
        default_lang="en"
    )
    lang = chat_data.get("language", "en")

    welcome_text = (
        f"{t('welcome_group', lang)}\n\n"
        f"💡 <i>Type /game to launch a match, or /help to see all commands and rules!</i>"
    )

    try:
        await bot.send_message(
            chat_id=chat.id,
            text=welcome_text,
            parse_mode="HTML"
        )
    except Exception:
        pass
