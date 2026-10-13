"""
Main Entry Point for GeoGuru & GeoGuessr Telegram Bot.
"""

import sys
import os
import time
import asyncio
import logging
import traceback
from typing import Optional

if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Configure logging to stdout immediately so Railway's deploy log capture displays all messages
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("GeoBot")

try:
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
except Exception as exc:
    tb = traceback.format_exc()
    msg = f"❌ CRITICAL: Fatal startup import exception:\n{tb}"
    logger.error(msg)
    print(msg, file=sys.stderr)
    print(msg, file=sys.stdout)
    sys.stderr.flush()
    sys.stdout.flush()
    if __name__ == "__main__" and "unittest" not in sys.modules and not os.getenv("TESTING"):
        time.sleep(3600)
        sys.exit(1)
    raise


def is_bot_token_valid(token: Optional[str]) -> bool:
    """Validate whether BOT_TOKEN is present and matches the basic Telegram bot token format."""
    if not token or token == "YOUR_BOT_TOKEN_HERE":
        return False
    parts = token.strip().split(":")
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1]:
        return False
    return True


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

    if not is_bot_token_valid(config.BOT_TOKEN):
        logger.error(
            "❌ CRITICAL: BOT_TOKEN is missing! Set BOT_TOKEN in Railway Variables.\n"
            "To connect live to Telegram:\n"
            "1. Obtain a token from @BotFather\n"
            "2. Add BOT_TOKEN=123456:ABC-DEF in Railway Variables or .env\n"
            "3. Restart the deployment"
        )
        sys.stdout.flush()
        sys.stderr.flush()
        # Prevent tight restart loop in Railway container
        if "unittest" not in sys.modules and not os.getenv("TESTING"):
            await asyncio.sleep(3600)
        return

    # Initialize bot and dispatcher
    bot = Bot(
        token=config.BOT_TOKEN.strip(),
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
    sys.stdout.flush()
    try:
        await dp.start_polling(bot, db=db)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
    except Exception as exc:
        # Full traceback output flushed immediately to both stdout and stderr
        # so Railway Deploy Logs capture it even with @level filters
        tb = traceback.format_exc()
        msg = f"❌ CRITICAL: Fatal startup exception:\n{tb}"
        logger.error(msg)
        print(msg, file=sys.stderr)
        print(msg, file=sys.stdout)
        sys.stderr.flush()
        sys.stdout.flush()
        if "unittest" not in sys.modules and not os.getenv("TESTING"):
            time.sleep(3600)
        sys.exit(1)
