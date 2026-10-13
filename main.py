"""
Main Entry Point for GeoGuru & GeoGuessr Telegram Bot.
"""

import sys
import asyncio
import logging

if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand

from handlers.bot_compat import patch_bot_item_access
patch_bot_item_access()

import config
from database.db import Database
from handlers import (
    commands_router,
    callbacks_router,
    chat_member_router,
    text_answers_router,
)
from games.flow import load_photo_cache

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("GeoBot")

async def setup_bot_commands(bot: Bot):
    """Register menu commands with Telegram."""
    commands = [
        BotCommand(command="start", description="Start bot / Asosiy menyu"),
        BotCommand(command="game", description="Start group game / Guruhda o'yin boshlash"),
        BotCommand(command="stop", description="Stop active game / O'yinni to'xtatish"),
        BotCommand(command="solo", description="Solo practice / Yakkaxon o'yin"),
        BotCommand(command="daily", description="Daily challenge / Kunlik topshiriq"),
        BotCommand(command="profile", description="Your profile & rank / Profil"),
        BotCommand(command="leaderboard", description="Global top players / Global reyting"),
        BotCommand(command="top", description="Group top players / Guruh peshqadamlari"),
        BotCommand(command="duel", description="1v1 challenge / Duelga chaqirish"),
        BotCommand(command="language", description="Change language / Tilni o'zgartirish"),
        BotCommand(command="help", description="Rules & instructions / Qo'llanma"),
    ]
    try:
        await bot.set_my_commands(commands)
    except Exception as e:
        logger.warning(f"Could not register bot commands: {e}")

async def main():
    logger.info("Initializing GeoGuru & GeoGuessr Bot...")

    # Initialize async database
    db = Database(config.DB_PATH)
    await db.init_db()

    # Load persistent photo cache
    load_photo_cache()

    if config.BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or not config.BOT_TOKEN:
        logger.warning(
            "⚠️ BOT_TOKEN is not set! Database initialized successfully.\n"
            "To connect live to Telegram:\n"
            "1. Obtain a token from @BotFather\n"
            "2. Add BOT_TOKEN=123456:ABC-DEF in .env\n"
            "3. Run python main.py"
        )
        return

    # Initialize bot and dispatcher
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    bot.db = db
    bot["db"] = db

    dp = Dispatcher()
    dp["db"] = db

    # Register routers in priority order
    dp.include_router(commands_router)
    dp.include_router(callbacks_router)
    dp.include_router(chat_member_router)
    dp.include_router(text_answers_router)

    # Setup menu commands
    await setup_bot_commands(bot)

    logger.info("Bot started successfully. Waiting for updates...")
    try:
        await dp.start_polling(bot, db=db)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
