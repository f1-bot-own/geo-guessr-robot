"""
Game Flow Controller for GeoGuru & GeoGuessr Bot.
Orchestrates round progression, timeouts, fun facts, and podium displays.
"""

import asyncio
import time
import logging
from typing import Optional, List, Callable, Union, Any, Dict
import aiohttp
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, Message, BufferedInputFile
from aiogram.exceptions import TelegramRetryAfter, TelegramBadRequest
from locales.i18n import t, format_countdown
from .models import Question, GameMode
from .session import GameSession
from .solo_session import SoloGameSession
from .daily_session import DailyChallengeSession
from .manager import game_manager
from keyboards.game_kb import get_question_kb, get_solo_question_kb, get_daily_question_kb
from database.db import format_user_mention
import config

from pathlib import Path
import json

logger = logging.getLogger(__name__)

# Ultra-resilient photo file_id cache mapping image_url -> telegram_file_id
PHOTO_CACHE: Dict[str, str] = {}


def get_default_photo_cache_path() -> Path:
    """Resolve photo cache path to PHOTO_CACHE_PATH if set, or directory containing DB_PATH (e.g. Railway volume)."""
    import os
    env_cache = os.getenv("PHOTO_CACHE_PATH")
    if env_cache:
        return Path(env_cache)
    db_str = str(config.DB_PATH)
    if db_str == ":memory:":
        return config.BASE_DIR / "photo_cache.json"
    return Path(config.DB_PATH).parent / "photo_cache.json"


PHOTO_CACHE_FILE = get_default_photo_cache_path()


def load_photo_cache(file_path: Optional[Path] = None):
    """Load cached telegram file_ids from disk if available."""
    target = file_path or get_default_photo_cache_path()
    if not target.exists():
        legacy_path = config.BASE_DIR / "data" / "photo_cache.json"
        if legacy_path.exists():
            target = legacy_path
        else:
            root_path = config.BASE_DIR / "photo_cache.json"
            if root_path.exists():
                target = root_path

    if target.exists():
        try:
            with open(target, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    PHOTO_CACHE.update(data)
                    logger.info(f"Loaded {len(data)} cached photo file_ids from {target}")
        except Exception as e:
            logger.warning(f"Could not load photo cache from {target}: {e}")


ENABLE_PERSISTENT_CACHE: bool = True

def save_photo_cache(file_path: Optional[Path] = None):
    """Persist cached telegram file_ids to disk."""
    if file_path is None and not ENABLE_PERSISTENT_CACHE:
        return
    target = file_path or get_default_photo_cache_path()
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            json.dump(PHOTO_CACHE, f, indent=2)
    except Exception as e:
        logger.warning(f"Could not save photo cache to {target}: {e}")

async def send_resilient_photo(
    bot: Bot,
    chat_id: int,
    photo_url: str,
    caption: Optional[str] = None,
    reply_markup: Optional[InlineKeyboardMarkup] = None,
    parse_mode: str = "HTML"
) -> Optional[Message]:
    """
    Ultra-resilient photo delivery mechanism:
    1. If cached telegram_file_id exists in PHOTO_CACHE, send directly via photo=file_id (instant, 100% reliable).
    2. If cache miss or cached send fails, attempt sending directly via photo=photo_url.
    3. If sending by URL fails (e.g. 'failed to get HTTP URL content' or any client error),
       immediately download image bytes in Python using aiohttp with custom browser User-Agent
       and send via BufferedInputFile(image_bytes, filename="photo.jpg").
    4. Extract msg.photo[-1].file_id and cache it in PHOTO_CACHE for future instantaneous sends.
    """
    if not photo_url or not isinstance(photo_url, str) or not photo_url.strip():
        return None
    photo_url = photo_url.strip()

    # Telegram caption limit is 1024 chars for photos
    if caption and len(caption) > 1024:
        caption = caption[:1021] + "..."

    # Step 1: Check cache
    if photo_url in PHOTO_CACHE:
        cached_file_id = PHOTO_CACHE[photo_url]
        try:
            msg = await bot.send_photo(
                chat_id=chat_id,
                photo=cached_file_id,
                caption=caption,
                reply_markup=reply_markup,
                parse_mode=parse_mode
            )
            return msg
        except TelegramRetryAfter as e:
            logger.warning(f"TelegramRetryAfter caught on cached photo send for {photo_url}: {e}")
            if e.retry_after <= 3:
                try:
                    await asyncio.sleep(e.retry_after)
                    return await bot.send_photo(
                        chat_id=chat_id,
                        photo=cached_file_id,
                        caption=caption,
                        reply_markup=reply_markup,
                        parse_mode=parse_mode
                    )
                except Exception:
                    pass
            return None
        except Exception as e:
            logger.warning(f"Failed to send cached photo file_id for {photo_url}: {e}. Invalidating cache and retrying.")
            PHOTO_CACHE.pop(photo_url, None)
            save_photo_cache()

    # Step 2: Try direct URL send
    try:
        msg = await bot.send_photo(
            chat_id=chat_id,
            photo=photo_url,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )
        if msg and getattr(msg, "photo", None):
            try:
                fid = msg.photo[-1].file_id
                if fid and isinstance(fid, str):
                    PHOTO_CACHE[photo_url] = fid
                    save_photo_cache()
            except Exception:
                pass
        return msg
    except TelegramRetryAfter as e:
        logger.warning(f"TelegramRetryAfter caught on photo URL send for {photo_url}: {e}")
        return None
    except Exception as e:
        logger.warning(f"Direct photo URL send failed for {photo_url} ({e}). Triggering resilient byte download fallback...")

    # Step 3: Direct byte download fallback with aiohttp
    try:
        headers = {
            "User-Agent": "GeoGuessrTelegramBot/1.0 (https://github.com/f1-bot-own/geo-guessr-robot; contact@geobot.org) Mozilla/5.0"
        }
        timeout = aiohttp.ClientTimeout(total=10, connect=4, sock_read=6)
        async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
            async with session.get(photo_url) as resp:
                if resp.status == 200:
                    image_bytes = await resp.read()
                    if image_bytes:
                        photo_input = BufferedInputFile(image_bytes, filename="photo.jpg")
                        msg = await bot.send_photo(
                            chat_id=chat_id,
                            photo=photo_input,
                            caption=caption,
                            reply_markup=reply_markup,
                            parse_mode=parse_mode
                        )
                        if msg and getattr(msg, "photo", None):
                            try:
                                fid = msg.photo[-1].file_id
                                if fid and isinstance(fid, str):
                                    PHOTO_CACHE[photo_url] = fid
                                    save_photo_cache()
                            except Exception:
                                pass
                        return msg
                else:
                    logger.warning(f"Direct image download failed with HTTP status {resp.status} for {photo_url}")
    except TelegramRetryAfter as e:
        logger.warning(f"TelegramRetryAfter caught during buffered photo send for {photo_url}: {e}")
        return None
    except Exception as dl_err:
        logger.error(f"Resilient byte download and delivery failed for {photo_url}: {dl_err}")

    return None


def get_countdown_checkpoints(duration: int) -> List[int]:
    """
    Returns descending list of remaining seconds at which to edit question post.
    Intervals are chosen safely (every 3-5s or 10s) to avoid Telegram 429 FloodWait.
    Always includes critical thresholds (20s, 10s, 5s) when duration permits.
    """
    if duration <= 3:
        return []
    
    checkpoints = set()
    if duration >= 15:
        # Step every 5s below 30s
        for s in range(5, min(duration, 30), 5):
            checkpoints.add(s)
        # For longer rounds (e.g. 60s), step every 10s above 30s
        for s in range(30, duration, 10):
            checkpoints.add(s)
    elif duration >= 6:
        # For 6-14s durations:
        if 5 < duration:
            checkpoints.add(5)
        if duration - 3 > 0 and duration - 3 != 5:
            checkpoints.add(duration - 3)
    else:
        # 4 or 5 seconds
        checkpoints.add(2)
        
    return sorted(checkpoints, reverse=True)

def format_group_question_text(session: GameSession, remaining_time: Optional[int] = None) -> str:
    """Compose full caption/text for group match question with remaining time."""
    q = session.current_question
    if not q:
        return ""
    mode_label = t(f"mode_{q.mode}", session.lang)
    current_time = remaining_time if remaining_time is not None else session.round_time
    header = t(
        "round_indicator",
        session.lang,
        current=session.current_round,
        total=session.total_rounds,
        mode=mode_label,
        time=current_time
    )
    countdown_str = format_countdown(current_time, session.lang)
    return f"{header}\n\n{q.text}\n\n{countdown_str}"

def format_solo_question_text(session: SoloGameSession, remaining_time: Optional[int] = None) -> str:
    """Compose full caption/text for solo practice question with remaining time."""
    q = session.current_question
    if not q:
        return ""
    current_time = remaining_time if remaining_time is not None else getattr(session, "round_time", config.DEFAULT_ROUND_TIME)
    lives_str = "❤️" * session.lives
    info_line = t(
        "solo_round_info",
        session.lang,
        round=session.round_number,
        score=session.score,
        lives=lives_str
    )
    countdown_str = format_countdown(current_time, session.lang)
    return f"{t('solo_title', session.lang)}\n{info_line}\n\n{q.text}\n\n{countdown_str}"

async def safe_edit_question_message(
    bot: Bot,
    chat_id: int,
    message_id: int,
    text: str,
    reply_markup: Optional[InlineKeyboardMarkup] = None,
    has_photo: bool = False
) -> bool:
    """
    Safely edit question message with rate-limiting & flood-error resilience.
    Returns True if edit succeeded or was not modified, False if skipped due to flood or error.
    """
    try:
        if has_photo:
            try:
                await bot.edit_message_caption(
                    chat_id=chat_id,
                    message_id=message_id,
                    caption=text,
                    reply_markup=reply_markup,
                    parse_mode="HTML"
                )
            except Exception as pe:
                err_pe = str(pe).lower()
                if "no caption" in err_pe or "text" in err_pe:
                    await bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_id,
                        text=text,
                        reply_markup=reply_markup,
                        parse_mode="HTML"
                    )
                else:
                    raise pe
        else:
            try:
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text=text,
                    reply_markup=reply_markup,
                    parse_mode="HTML"
                )
            except Exception as te:
                err_te = str(te).lower()
                if "no text" in err_te or "caption" in err_te:
                    await bot.edit_message_caption(
                        chat_id=chat_id,
                        message_id=message_id,
                        caption=text,
                        reply_markup=reply_markup,
                        parse_mode="HTML"
                    )
                else:
                    raise te
        return True
    except asyncio.CancelledError:
        raise
    except TelegramRetryAfter as e:
        logger.warning(f"TelegramRetryAfter: flood wait {e.retry_after}s on message {message_id}. Skipping edit.")
        return False
    except TelegramBadRequest as e:
        err = str(e).lower()
        if "message is not modified" in err:
            logger.debug("Message not modified on timer edit.")
            return True
        elif "message to edit not found" in err or "message can't be edited" in err or "chat not found" in err:
            logger.warning(f"Question message cannot be edited: {e}")
            return False
        logger.warning(f"TelegramBadRequest on timer edit: {e}")
        return False
    except Exception as e:
        err = str(e).lower()
        if "flood" in err or hasattr(e, "retry_after"):
            logger.warning(f"Flood control caught on timer edit: {e}. Skipping.")
            return False
        elif "not modified" in err:
            logger.debug("Message not modified on timer edit.")
            return True
        elif "blocked" in err or "forbidden" in err or "deactivated" in err:
            logger.warning(f"Bot blocked or chat inactive on timer edit: {e}")
            return False
        logger.warning(f"Unexpected error editing timer message: {e}")
        return False

async def run_round_countdown(
    bot: Bot,
    chat_id: int,
    session: Union[GameSession, SoloGameSession],
    round_num: int,
    timeout_callback: Callable,
    is_solo: bool = False
):
    """
    Run round timer with live countdown edits at safe intervals.
    Automatically handles rate limits, monotonic drift, cancellations, and fires timeout_callback.
    """
    duration = getattr(session, "round_time", config.DEFAULT_ROUND_TIME)
    checkpoints = get_countdown_checkpoints(duration)

    start_mono = time.monotonic()
    for cp in checkpoints:
        target_deadline = start_mono + (duration - cp)
        sleep_duration = target_deadline - time.monotonic()
        if sleep_duration > 0:
            await asyncio.sleep(sleep_duration)

        # Check if round changed or ended under lock and capture current keyboard
        async with session.lock:
            if is_solo:
                if session.status != "in_progress" or session.round_number != round_num:
                    return
            else:
                if session.status != "in_progress" or session.current_round != round_num:
                    return
            current_kb = session.current_kb

        # Perform live countdown update on the message
        if getattr(session, "round_message_id", None):
            if is_solo:
                new_text = format_solo_question_text(session, remaining_time=cp)
            else:
                new_text = format_group_question_text(session, remaining_time=cp)

            await safe_edit_question_message(
                bot=bot,
                chat_id=chat_id,
                message_id=session.round_message_id,
                text=new_text,
                reply_markup=current_kb,
                has_photo=getattr(session, "has_photo", False)
            )

    # Sleep remaining seconds until 0
    final_sleep = (start_mono + duration) - time.monotonic()
    if final_sleep > 0:
        await asyncio.sleep(final_sleep)

    # Final active check before triggering timeout
    async with session.lock:
        if is_solo:
            if session.status != "in_progress" or session.round_number != round_num:
                return
        else:
            if session.status != "in_progress" or session.current_round != round_num:
                return

    res = timeout_callback()
    if asyncio.iscoroutine(res):
        await res

async def send_round_question(bot: Bot, chat_id: int, session: GameSession, db):
    """Deliver question for the current round and start countdown watcher."""
    if session.timer_task and not session.timer_task.done():
        session.timer_task.cancel()

    q = session.current_question
    if not q:
        return

    caption = format_group_question_text(session, remaining_time=session.round_time)
    if getattr(session, "input_mode", "both") == "text":
        kb = None
    else:
        kb = get_question_kb(session.session_id, q.options)
    session.current_kb = kb

    msg = None
    session.has_photo = False
    if q.image_url:
        try:
            msg = await send_resilient_photo(
                bot=bot,
                chat_id=chat_id,
                photo_url=q.image_url,
                caption=caption,
                reply_markup=kb,
                parse_mode="HTML"
            )
            if msg:
                session.has_photo = True
        except Exception as e:
            logger.warning(f"Failed to send question photo ({e}), falling back to text.")

    if not msg:
        try:
            msg = await bot.send_message(
                chat_id=chat_id,
                text=caption,
                reply_markup=kb,
                parse_mode="HTML"
            )
            session.has_photo = False
        except TelegramRetryAfter as e:
            wait_t = e.retry_after + 1
            logger.warning(f"TelegramRetryAfter caught on text question message: {e}. Waiting {wait_t}s...")
            if wait_t <= 35:
                try:
                    await asyncio.sleep(wait_t)
                    msg = await bot.send_message(
                        chat_id=chat_id,
                        text=caption,
                        reply_markup=kb,
                        parse_mode="HTML"
                    )
                    session.has_photo = False
                except Exception as retry_err:
                    logger.error(f"Failed to send question message after flood wait: {retry_err}")
        except Exception as e:
            logger.error(f"Failed to send question message: {e}")

    if not msg:
        logger.error("Failed to send question message even after retries. Pausing and scheduling recovery...")
        await asyncio.sleep(5)
        async with session.lock:
            if session.status != "finished":
                session.next_round()
        await proceed_after_round(bot, chat_id, session, db)
        return

    session.round_message_id = msg.message_id
    current_round_num = session.current_round

    # Launch async live countdown timer task
    async def timer_worker():
        try:
            await run_round_countdown(
                bot=bot,
                chat_id=chat_id,
                session=session,
                round_num=current_round_num,
                timeout_callback=lambda: handle_round_timeout(bot, chat_id, session, current_round_num, db),
                is_solo=False
            )
        except asyncio.CancelledError:
            pass

    session.timer_task = asyncio.create_task(timer_worker())

async def handle_round_timeout(bot: Bot, chat_id: int, session: GameSession, round_num: int, db):
    """Handle case where time runs out without any correct answer."""
    async with session.lock:
        if session.status != "in_progress" or session.current_round != round_num:
            return
        session.status = "between_rounds"
        session.current_kb = None

    q = session.current_question
    correct_ans = q.correct_answer if q else "—"

    # Time's up message
    text = t("time_up_announcement", session.lang, answer=correct_ans)
    if q and q.fun_fact:
        text += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
    if q and getattr(q, "maps_url", None) and q.maps_url not in text:
        text += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
    if not session.is_game_finished():
        text += f"\n\n⏳ {t('next_round_in', session.lang, seconds=3)}"

    # Remove buttons from timed-out question message
    if session.round_message_id:
        try:
            await bot.edit_message_reply_markup(chat_id=chat_id, message_id=session.round_message_id, reply_markup=None)
        except Exception:
            pass

    try:
        await bot.send_message(chat_id=chat_id, text=text, parse_mode="HTML")
    except Exception as e:
        logger.error(f"Error sending timeout announcement: {e}")

    await proceed_after_round(bot, chat_id, session, db)

async def proceed_after_round(bot: Bot, chat_id: int, session: GameSession, db):
    """Check if game is finished or schedule next round."""
    async with session.lock:
        if session.advancing or session.status == "finished":
            return
        session.advancing = True

    try:
        if session.is_game_finished():
            await finish_game(bot, chat_id, session, db)
        else:
            wait_seconds = 3
            await asyncio.sleep(wait_seconds)
            async with session.lock:
                if session.status == "finished":
                    return
                session.status = "in_progress"
                if db and hasattr(db, "get_chat_language"):
                    try:
                        latest_lang = await db.get_chat_language(chat_id)
                        if latest_lang:
                            session.lang = latest_lang
                    except Exception:
                        pass
                session.next_round()

            await send_round_question(bot, chat_id, session, db)
    finally:
        session.advancing = False

async def finish_game(bot: Bot, chat_id: int, session: GameSession, db):
    """Complete match, update DB leaderboards, and print victory podium."""
    session.stop()
    game_manager.remove_session(chat_id)

    podium = session.get_podium()
    winner_id = podium[0][0] if podium and podium[0][2] > 0 else None
    winner_name = podium[0][1] if podium and podium[0][2] > 0 else ""
    winner_score = podium[0][2] if podium and podium[0][2] > 0 else 0

    # Record match in matches table
    await db.record_match(
        chat_id=chat_id,
        mode="duel" if session.is_duel else session.mode,
        winner_id=winner_id,
        winner_name=winner_name,
        winner_score=winner_score,
        players_count=len(podium)
    )

    # Handle duel outcome in database
    if session.is_duel and getattr(session, "duel_id", None):
        await db.update_duel_status(session.duel_id, status="completed", winner_id=winner_id)

    header = f"{t('game_over_title', session.lang)}\n\n{t('final_standings_header', session.lang)}\n"

    if session.is_duel:
        challenger_id = session.created_by_user_id
        target_id = session.duel_target_id
        c_score = session.scores.get(challenger_id, 0)
        t_score = session.scores.get(target_id, 0)
        c_name = session.user_names.get(challenger_id, "Challenger")
        t_name = session.user_names.get(target_id, "Opponent")

        # Update both players in DB
        await db.update_group_player_score(chat_id, challenger_id, c_score, is_win=(winner_id == challenger_id), first_name=c_name)
        await db.update_group_player_score(chat_id, target_id, t_score, is_win=(winner_id == target_id), first_name=t_name)
        if winner_id:
            await db.record_answer(winner_id, is_correct=True, points=0, xp=config.XP_PER_WIN, user_name=c_name if winner_id == challenger_id else t_name)

        c_mention = format_user_mention(challenger_id, c_name)
        t_mention = format_user_mention(target_id, t_name)

        if c_score > t_score:
            outcome = f"🏆 <b>Winner: {c_mention}!</b>\n⚔️ {c_mention} ({c_score} pts) 🆚 {t_mention} ({t_score} pts)"
        elif t_score > c_score:
            outcome = f"🏆 <b>Winner: {t_mention}!</b>\n⚔️ {t_mention} ({t_score} pts) 🆚 {c_mention} ({c_score} pts)"
        else:
            outcome = f"🤝 <b>It's a DRAW!</b>\n⚔️ {c_mention} ({c_score} pts) 🆚 {t_mention} ({t_score} pts)"

        msg_text = f"⚔️ <b>GEOGRAPHY DUEL FINISHED!</b> ⚔️\n\n{outcome}"
    elif not podium:
        msg_text = f"{header}\n{t('no_scores', session.lang)}"
    else:
        rows = []
        for pos, (uid, uname, score) in enumerate(podium, start=1):
            is_winner = (uid == winner_id)
            # Update user stats in DB
            await db.update_group_player_score(chat_id, uid, score, is_win=is_winner, first_name=uname)
            if is_winner:
                await db.record_answer(uid, is_correct=True, points=0, xp=config.XP_PER_WIN, user_name=uname)

            u_mention = format_user_mention(uid, uname)
            if pos == 1:
                rows.append(t("podium_first", session.lang, user=u_mention, score=score))
            elif pos == 2:
                rows.append(t("podium_second", session.lang, user=u_mention, score=score))
            elif pos == 3:
                rows.append(t("podium_third", session.lang, user=u_mention, score=score))
            else:
                rows.append(t("standing_row", session.lang, pos=pos, user=u_mention, score=score))

        msg_text = f"{header}\n" + "\n".join(rows)

    # Increment group total games
    await db.increment_chat_games(chat_id)

    try:
        await bot.send_message(chat_id=chat_id, text=msg_text, parse_mode="HTML")
    except Exception as e:
        logger.error(f"Error sending final game message: {e}")

async def send_solo_round(bot: Bot, user_id: int, session: SoloGameSession, db=None):
    """Send next solo practice round and launch countdown timer."""
    if session.timer_task and not session.timer_task.done():
        session.timer_task.cancel()

    q = session.current_question
    if not q:
        return

    caption = format_solo_question_text(session, remaining_time=session.round_time)
    is_text_only = (getattr(session, "input_mode", "both") == "text")
    kb = get_solo_question_kb(
        options=q.options,
        eliminated=session.eliminated_options,
        has_hint=session.has_hint,
        has_5050=session.has_5050,
        lang=session.lang,
        text_only=is_text_only
    )
    session.current_kb = kb

    msg = None
    session.has_photo = False
    if q.image_url:
        try:
            msg = await send_resilient_photo(
                bot=bot,
                chat_id=user_id,
                photo_url=q.image_url,
                caption=caption,
                reply_markup=kb,
                parse_mode="HTML"
            )
            if msg:
                session.has_photo = True
        except Exception as e:
            logger.warning(f"Failed to send solo photo ({e}), falling back to text.")

    if not msg:
        try:
            msg = await bot.send_message(
                chat_id=user_id,
                text=caption,
                reply_markup=kb,
                parse_mode="HTML"
            )
            session.has_photo = False
        except Exception as e:
            logger.error(f"Failed to send solo question message: {e}")
            return

    session.round_message_id = msg.message_id
    current_round_num = session.round_number

    # Launch live countdown & timeout watcher
    async def solo_timer_worker():
        try:
            await run_round_countdown(
                bot=bot,
                chat_id=user_id,
                session=session,
                round_num=current_round_num,
                timeout_callback=lambda: handle_solo_timeout(bot, user_id, session, current_round_num, db),
                is_solo=True
            )
        except asyncio.CancelledError:
            pass

    session.timer_task = asyncio.create_task(solo_timer_worker())

async def handle_solo_timeout(bot: Bot, user_id: int, session: SoloGameSession, round_num: int, db=None, wait_seconds: float = 2.0):
    """Handle solo mode round expiration: deduct life and advance or game over."""
    async with session.lock:
        if getattr(session, "advancing", False) or session.status != "in_progress" or session.round_number != round_num:
            return
        session.status = "between_rounds"
        session.current_kb = None
        session.advancing = True

    try:
        is_game_over, correct_ans = session.handle_timeout()

        # Clear inline buttons on the question message
        if session.round_message_id:
            try:
                await bot.edit_message_reply_markup(chat_id=user_id, message_id=session.round_message_id, reply_markup=None)
            except Exception:
                pass

        # Record timeout (wrong/missed answer) in database
        if db:
            try:
                await db.record_answer(
                    user_id=user_id,
                    is_correct=False,
                    points=0,
                    user_name=session.user_name
                )
            except Exception as e:
                logger.warning(f"Error recording solo timeout in DB: {e}")

        timeout_header = t("time_up_announcement", session.lang, answer=correct_ans)
        q = session.current_question
        if q and q.fun_fact:
            timeout_header += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
        if q and getattr(q, "maps_url", None) and q.maps_url not in timeout_header:
            timeout_header += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"

        if is_game_over:
            game_over_text = t(
                "solo_game_over",
                session.lang,
                score=session.score,
                correct=session.correct_count
            )
            msg_text = f"{timeout_header}\n\n{game_over_text}"
            game_manager.remove_solo_session(user_id)
            try:
                await bot.send_message(chat_id=user_id, text=msg_text, parse_mode="HTML")
            except Exception as e:
                logger.error(f"Error sending solo game over message: {e}")
        else:
            lives_left = "❤️" * session.lives
            if session.lang == "uz":
                lives_label = f"❤️ Qolgan jonlar: {lives_left}"
            elif session.lang == "ru":
                lives_label = f"❤️ Осталось жизней: {lives_left}"
            else:
                lives_label = f"❤️ Lives remaining: {lives_left}"
            msg_text = f"{timeout_header}\n\n{lives_label}"
            try:
                await bot.send_message(chat_id=user_id, text=msg_text, parse_mode="HTML")
            except Exception as e:
                logger.error(f"Error sending solo timeout message: {e}")

            if wait_seconds > 0:
                await asyncio.sleep(wait_seconds)

            async with session.lock:
                if session.status == "finished":
                    return
                session.status = "in_progress"
                session.next_round()

            await send_solo_round(bot, user_id, session, db)
    finally:
        session.advancing = False


async def send_daily_round(bot: Bot, user_id: int, session: DailyChallengeSession):
    """Send next daily challenge round."""
    q = session.current_question
    if not q:
        return

    round_idx = session.current_round + 1
    total = session.TOTAL_ROUNDS
    info_line = f"📍 <b>Round {round_idx}/{total}</b> | Score: <b>{session.score} pts</b>"
    caption = f"{t('daily_title', session.lang)}\n{info_line}\n\n{q.text}"
    kb = get_daily_question_kb(q.options)

    if q.image_url:
        try:
            msg = await send_resilient_photo(
                bot=bot,
                chat_id=user_id,
                photo_url=q.image_url,
                caption=caption,
                reply_markup=kb,
                parse_mode="HTML"
            )
            if msg:
                return
        except Exception:
            pass

    await bot.send_message(
        chat_id=user_id,
        text=caption,
        reply_markup=kb,
        parse_mode="HTML"
    )
