"""
Group Text Answer Recognizer.
Allows group members to type answers in chat in addition to tapping inline buttons.
Features exact and whole-word matching to eliminate substring false positives,
and supports quick option shortcuts (1-4, A-D).
"""

import re
from aiogram import Router, Bot, F
from aiogram.types import Message
from database.db import Database, format_user_mention
from games.models import GameMode
from games.manager import game_manager
from games.flow import proceed_after_round, send_solo_round
from gamedata.countries import get_country, COUNTRIES
from locales.i18n import t
import config

router = Router()

from .bot_compat import get_db

# Map Cyrillic characters (both Russian and Uzbek Cyrillic) to Latin equivalents
CYRILLIC_TO_LATIN = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
    "ж": "j", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "x", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sh",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
    "ў": "o", "ғ": "g", "қ": "q", "ҳ": "h"
}

def to_latin(text: str) -> str:
    """Transliterate Cyrillic text (Russian and Uzbek Cyrillic) to Latin phonetic representation."""
    if not text:
        return ""
    res = []
    for ch in text.lower():
        res.append(CYRILLIC_TO_LATIN.get(ch, ch))
    return "".join(res)

def _normalize(text: str) -> str:
    """Normalize text by lowering, normalizing ё->е, stripping all apostrophe/quote variants, and stripping extra spaces."""
    if not text:
        return ""
    t = text.lower().replace("ё", "е")
    # Strip all variants of single quotes, apostrophes, accents, and modifiers
    t = re.sub(r"['`’‘‛ʻʼ\^′´\"]", "", t)
    cleaned = re.sub(r"[^\w\s]", " ", t, flags=re.UNICODE)
    return " ".join(cleaned.split())

# Well-known Uzbek Cyrillic and colloquial name variants for countries & capitals
EXTRA_COUNTRY_VARIANTS = {
    "uz": {"ўзбекистон", "узбекистон", "ozbekiston", "uzbekiston", "тошкент", "toshkent"},
    "kz": {"қозоғистон", "казахстан", "qozogiston", "остона", "нурсултон", "астана"},
    "kg": {"қирғизистон", "кыргызстан", "qirgiziston", "бишкек"},
    "tj": {"тожикистон", "таджикистан", "tojikiston", "душанбе"},
    "tm": {"туркманистон", "туркменистан", "туркмения", "turkmaniston", "ашхобод", "ашхабад"},
    "us": {"ақш", "aqsh", "сша", "usa", "америка", "america"},
    "ru": {"россия", "rossiya", "рф", "москва"},
    "gb": {"буюк британия", "британия", "англия", "angliya", "london", "лондон"},
    "cn": {"хитой", "китай", "xitoy", "пекин"},
    "tr": {"туркия", "турция", "turkiya", "анқара", "анкара"},
    "de": {"германия", "germaniya", "берлин"},
    "fr": {"франция", "fransiya", "париж", "parij"},
    "it": {"италия", "italiya", "рим"},
    "es": {"испания", "ispaniya", "мадрид"},
    "af": {"афғонистон", "афганистан", "afgoniston", "kobul", "кабул"},
}

ALL_COUNTRY_NAMES = set()
for c in COUNTRIES:
    for lang_key in ("en", "ru", "uz"):
        if "name" in c and lang_key in c["name"]:
            val = c["name"][lang_key]
            norm_v = _normalize(val)
            ALL_COUNTRY_NAMES.add(norm_v)
            ALL_COUNTRY_NAMES.add(norm_v.replace(" ", ""))
            lat_v = to_latin(norm_v)
            ALL_COUNTRY_NAMES.add(lat_v)
            ALL_COUNTRY_NAMES.add(lat_v.replace(" ", ""))
        if "capital" in c and lang_key in c["capital"]:
            val = c["capital"][lang_key]
            norm_v = _normalize(val)
            ALL_COUNTRY_NAMES.add(norm_v)
            ALL_COUNTRY_NAMES.add(norm_v.replace(" ", ""))
            lat_v = to_latin(norm_v)
            ALL_COUNTRY_NAMES.add(lat_v)
            ALL_COUNTRY_NAMES.add(lat_v.replace(" ", ""))

for code, extra_set in EXTRA_COUNTRY_VARIANTS.items():
    for item in extra_set:
        norm_v = _normalize(item)
        ALL_COUNTRY_NAMES.add(norm_v)
        ALL_COUNTRY_NAMES.add(to_latin(norm_v))

def _matches_any_country(text: str) -> bool:
    norm = _normalize(text)
    lat = to_latin(norm)
    return (
        norm in ALL_COUNTRY_NAMES or
        norm.replace(" ", "") in ALL_COUNTRY_NAMES or
        lat in ALL_COUNTRY_NAMES or
        lat.replace(" ", "") in ALL_COUNTRY_NAMES
    )

def _add_variants(target_set: set, val: str):
    if not val:
        return
    norm = _normalize(val)
    if norm:
        target_set.add(norm)
        if " " in norm:
            target_set.add(norm.replace(" ", ""))
        lat = to_latin(norm)
        if lat:
            target_set.add(lat)
            if " " in lat:
                target_set.add(lat.replace(" ", ""))

def _compile_valid_correct(q) -> set:
    """Compile valid representations of correct answer across languages and Cyrillic/Latin scripts."""
    country = get_country(q.country_code) if q.country_code else None
    valid_correct = set()
    _add_variants(valid_correct, q.correct_answer)

    if getattr(q, "aliases", None):
        for alias in q.aliases:
            _add_variants(valid_correct, alias)

    if country:
        cap_names = set()
        if "capital" in country:
            for l in ("en", "ru", "uz"):
                if l in country["capital"]:
                    _add_variants(cap_names, country["capital"][l])

        country_names = set()
        if "name" in country:
            for l in ("en", "ru", "uz"):
                if l in country["name"]:
                    _add_variants(country_names, country["name"][l])

        # Add extra country variants if code is mapped
        c_code = country.get("code", "").lower()
        if c_code in EXTRA_COUNTRY_VARIANTS:
            for extra_v in EXTRA_COUNTRY_VARIANTS[c_code]:
                _add_variants(country_names, extra_v)

        norm_correct_ans = _normalize(q.correct_answer)
        lat_correct_ans = to_latin(norm_correct_ans)
        if (
            norm_correct_ans in cap_names or
            norm_correct_ans.replace(" ", "") in cap_names or
            lat_correct_ans in cap_names or
            lat_correct_ans.replace(" ", "") in cap_names
        ):
            # Question is asking for the capital! Only capital names are valid
            valid_correct.update(cap_names)
        else:
            # Question is asking for the country name!
            valid_correct.update(country_names)

    if q.mode == "higher_lower":
        _add_variants(valid_correct, q.options[q.correct_index])

    return valid_correct

def _text_matches_valid(norm_text: str, valid_set: set) -> bool:
    if not norm_text:
        return False
    candidates = [norm_text, norm_text.replace(" ", "")]
    lat = to_latin(norm_text)
    if lat and lat not in candidates:
        candidates.append(lat)
        candidates.append(lat.replace(" ", ""))

    for cand in candidates:
        if not cand or len(cand) < 2:
            continue
        if cand in valid_set:
            return True
        for valid in valid_set:
            if not valid or len(valid) < 2:
                continue
            if cand == valid:
                return True
            pattern = r"(?:\b|^)" + re.escape(valid) + r"(?:\b|$)"
            if re.search(pattern, cand):
                return True
    return False

OPTION_SHORTCUTS = {
    "1": 0, "a": 0, "🅰": 0, "🅰️": 0,
    "2": 1, "b": 1, "🅱": 1, "🅱️": 1,
    "3": 2, "c": 2,
    "4": 3, "d": 3,
}

@router.message(F.chat.type.in_({"group", "supergroup"}), F.text, ~F.text.startswith("/"))
async def check_group_text_answer(message: Message, bot: Bot):
    """Detect if a user typed the answer directly into group chat."""
    chat_id = message.chat.id
    session = game_manager.get_session(chat_id)

    if not session or session.status != "in_progress" or not session.current_question:
        return

    q = session.current_question

    if getattr(session, "input_mode", "both") == "buttons":
        return

    user = message.from_user
    if not user or user.is_bot:
        return

    # In duel mode, only the two participants may answer
    if getattr(session, "is_duel", False) and user.id not in (session.created_by_user_id, getattr(session, "duel_target_id", None)):
        return

    raw_text = message.text.strip().lower()
    norm_text = _normalize(raw_text)
    if not norm_text:
        return

    raw_first = (user.first_name or "").strip()
    raw_user = (user.username or "").strip()
    if not raw_first or raw_first == ".":
        user_name = f"@{raw_user.lstrip('@')}" if raw_user and raw_user != "." else f"Player {user.id}"
    else:
        user_name = raw_first
    db = get_db(bot)

    # 1. Check if user typed an option shortcut (e.g. "1", "2", "a", "b", "c", "d")
    shortcut_candidate = norm_text if norm_text in OPTION_SHORTCUTS else raw_text
    if shortcut_candidate in OPTION_SHORTCUTS:
        selected_idx = OPTION_SHORTCUTS[shortcut_candidate]
        if selected_idx < len(q.options):
            result, points, elapsed = await session.check_answer(user.id, user_name, selected_idx)
            if result == "correct":
                session.current_kb = None
                if session.timer_task and not session.timer_task.done():
                    session.timer_task.cancel()
                if session.round_message_id:
                    try:
                        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=session.round_message_id, reply_markup=None)
                    except Exception:
                        pass
                await db.record_answer(user.id, is_correct=True, points=points, xp=config.XP_PER_CORRECT, user_name=user_name, username=user.username, chat_id=chat_id)
                user_mention = format_user_mention(user.id, user_name)
                announcement = t(
                    "correct_answer_announcement",
                    session.lang,
                    user=user_mention,
                    time=elapsed,
                    points=points,
                    answer=q.correct_answer
                )
                if q and getattr(q, "mode", None) == GameMode.BLUR:
                    stage = getattr(q, "blur_stage", 1)
                    if stage == 1:
                        announcement += f"\n🔍 <b>+300 {t('mode_blur', session.lang)} bonus!</b>"
                    elif stage == 2:
                        announcement += f"\n🔍 <b>+150 {t('mode_blur', session.lang)} bonus!</b>"
                if q.fun_fact:
                    announcement += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
                if getattr(q, "maps_url", None) and q.maps_url not in announcement:
                    announcement += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
                if not session.is_game_finished():
                    announcement += f"\n\n⏳ {t('next_round_in', session.lang, seconds=3)}"
                try:
                    await message.reply(text=announcement, parse_mode="HTML")
                except Exception:
                    pass
                await proceed_after_round(bot, chat_id, session, db)
                return
            elif result == "wrong":
                await db.record_answer(user.id, is_correct=False, points=-points, user_name=user_name, username=user.username)
                try:
                    await message.reply(
                        text=t("wrong_answer_alert", session.lang, penalty=points),
                        parse_mode="HTML"
                    )
                except Exception:
                    pass
                return
            elif result == "already_wrong":
                try:
                    await message.reply(
                        text=t("already_answered_wrong", session.lang, user=user_name),
                        parse_mode="HTML"
                    )
                except Exception:
                    pass
                return

    # 2. Compile valid representations of correct answer
    valid_correct = _compile_valid_correct(q)

    # Match check: exact match or whole-token phrase match
    if _text_matches_valid(norm_text, valid_correct):
        result, points, elapsed = await session.check_answer(user.id, user_name, q.correct_index)
        if result == "correct":
            session.current_kb = None
            if session.timer_task and not session.timer_task.done():
                session.timer_task.cancel()
            if session.round_message_id:
                try:
                    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=session.round_message_id, reply_markup=None)
                except Exception:
                    pass

            await db.record_answer(user.id, is_correct=True, points=points, xp=config.XP_PER_CORRECT, user_name=user_name, username=user.username, chat_id=chat_id)
            user_mention = format_user_mention(user.id, user_name)

            announcement = t(
                "correct_answer_announcement",
                session.lang,
                user=user_mention,
                time=elapsed,
                points=points,
                answer=q.correct_answer
            )
            if q and getattr(q, "mode", None) == GameMode.BLUR:
                stage = getattr(q, "blur_stage", 1)
                if stage == 1:
                    announcement += f"\n🔍 <b>+300 {t('mode_blur', session.lang)} bonus!</b>"
                elif stage == 2:
                    announcement += f"\n🔍 <b>+150 {t('mode_blur', session.lang)} bonus!</b>"
            if q.fun_fact:
                announcement += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
            if getattr(q, "maps_url", None) and q.maps_url not in announcement:
                announcement += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
            if not session.is_game_finished():
                announcement += f"\n\n⏳ {t('next_round_in', session.lang, seconds=3)}"

            try:
                await message.reply(text=announcement, parse_mode="HTML")
            except Exception:
                pass
            await proceed_after_round(bot, chat_id, session, db)
            return
        elif result == "already_wrong":
            try:
                await message.reply(
                    text=t("already_answered_wrong", session.lang, user=user_name),
                    parse_mode="HTML"
                )
            except Exception:
                pass
            return

    # 3. Check if user typed one of the distractor options directly
    for idx, opt in enumerate(q.options):
        if idx == q.correct_index:
            continue
        norm_opt = _normalize(opt)
        if norm_opt and _text_matches_valid(norm_text, {norm_opt}):
            result, penalty, _ = await session.check_answer(user.id, user_name, idx)
            if result == "wrong":
                await db.record_answer(user.id, is_correct=False, points=-penalty, user_name=user_name, username=user.username)
                try:
                    await message.reply(
                        text=t("wrong_answer_alert", session.lang, penalty=penalty),
                        parse_mode="HTML"
                    )
                except Exception:
                    pass
            elif result == "already_wrong":
                try:
                    await message.reply(
                        text=t("already_answered_wrong", session.lang, user=user_name),
                        parse_mode="HTML"
                    )
                except Exception:
                    pass
            return

    # 4. Check if user typed any other country/capital or attempted an answer in text-only mode
    is_text_only = (getattr(session, "input_mode", "both") == "text")
    if is_text_only or _matches_any_country(norm_text):
        wrong_idx = (q.correct_index + 1) % len(q.options)
        result, penalty, _ = await session.check_answer(user.id, user_name, wrong_idx)
        if result == "wrong":
            await db.record_answer(user.id, is_correct=False, points=-penalty, user_name=user_name, username=user.username)
            try:
                await message.reply(
                    text=t("wrong_answer_alert", session.lang, penalty=penalty),
                    parse_mode="HTML"
                )
            except Exception:
                pass
        elif result == "already_wrong":
            try:
                await message.reply(
                    text=t("already_answered_wrong", session.lang, user=user_name),
                    parse_mode="HTML"
                )
            except Exception:
                pass
        return

# ----------------- Solo Text Answers -----------------
@router.message(F.chat.type == "private", F.text, ~F.text.startswith("/"))
async def check_solo_text_answer(message: Message, bot: Bot):
    """Detect if a user typed the answer directly into private chat during solo mode."""
    user = message.from_user
    if not user or user.is_bot:
        return

    session = game_manager.get_solo_session(user.id)
    if not session or session.status != "in_progress" or not session.current_question:
        return

    # Check input_mode: ignore text messages if mode is buttons-only
    if getattr(session, "input_mode", "both") == "buttons":
        return

    raw_text = message.text.strip().lower()
    norm_text = _normalize(raw_text)
    if not norm_text:
        return

    q = session.current_question
    db = get_db(bot)

    # 1. Option shortcut check (1-4, a-d)
    shortcut_candidate = norm_text if norm_text in OPTION_SHORTCUTS else raw_text
    if shortcut_candidate in OPTION_SHORTCUTS:
        selected_idx = OPTION_SHORTCUTS[shortcut_candidate]
        if selected_idx < len(q.options):
            if selected_idx in session.eliminated_options:
                try:
                    await message.reply("This option has been eliminated!", parse_mode="HTML")
                except Exception:
                    pass
                return
            await _process_solo_text_guess(message, bot, session, selected_idx, db)
            return

    # 2. Compile valid correct answers
    valid_correct = _compile_valid_correct(q)

    if _text_matches_valid(norm_text, valid_correct):
        await _process_solo_text_guess(message, bot, session, q.correct_index, db)
        return

    # 3. Check distractor options
    for idx, opt in enumerate(q.options):
        if idx == q.correct_index:
            continue
        norm_opt = _normalize(opt)
        if norm_opt and _text_matches_valid(norm_text, {norm_opt}):
            await _process_solo_text_guess(message, bot, session, idx, db)
            return

    # 4. In text-only mode, or if matched any known country/capital in database
    is_text_only = (getattr(session, "input_mode", "both") == "text")
    if is_text_only or _matches_any_country(norm_text):
        wrong_idx = (q.correct_index + 1) % len(q.options)
        await _process_solo_text_guess(message, bot, session, wrong_idx, db)
        return

async def _process_solo_text_guess(message: Message, bot: Bot, session, opt_idx: int, db):
    """Evaluate solo text guess, announce correct answer, update stats, and advance."""
    async with session.lock:
        if session.status != "in_progress" or getattr(session, "advancing", False):
            return
        session.advancing = True

    try:
        # Clear reply markup on active question message
        if session.round_message_id:
            try:
                await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=session.round_message_id, reply_markup=None)
            except Exception:
                pass

        # Cancel active round timer cleanly
        if session.timer_task and not session.timer_task.done():
            session.timer_task.cancel()

        session.current_kb = None

        q = session.current_question
        correct_ans = q.correct_answer if q else ""
        is_correct, points, is_game_over = session.check_answer(opt_idx)
        user = message.from_user
        raw_first = (user.first_name or "").strip()
        raw_user = (user.username or "").strip()
        if not raw_first or raw_first == ".":
            user_name = f"@{raw_user.lstrip('@')}" if raw_user and raw_user != "." else f"Player {user.id}"
        else:
            user_name = raw_first

        if is_correct:
            await db.record_answer(
                user.id,
                is_correct=True,
                points=points,
                xp=config.XP_PER_CORRECT,
                user_name=user_name,
                username=user.username
            )
            text = t("solo_correct_answer_announcement", session.lang, points=points, answer=correct_ans)
            if q and q.fun_fact:
                text += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
            if q and getattr(q, "maps_url", None) and q.maps_url not in text:
                text += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
            try:
                await message.reply(text=text, parse_mode="HTML")
            except Exception:
                pass

            session.next_round()
            session.status = "in_progress"
            await send_solo_round(bot, user.id, session, db)
        else:
            await db.record_answer(
                user.id,
                is_correct=False,
                points=0,
                user_name=user_name,
                username=user.username
            )
            if is_game_over:
                game_over_text = t(
                    "solo_game_over",
                    session.lang,
                    score=session.score,
                    correct=session.correct_count
                )
                text = t("solo_wrong_game_over_announcement", session.lang, answer=correct_ans, game_over=game_over_text)
                if q and q.fun_fact:
                    text += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
                if q and getattr(q, "maps_url", None) and q.maps_url not in text:
                    text += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
                game_manager.remove_solo_session(user.id)
                try:
                    await message.reply(text=text, parse_mode="HTML")
                except Exception:
                    pass
            else:
                lives_str = "❤️" * session.lives
                text = t("solo_wrong_answer_announcement", session.lang, answer=correct_ans, lives=lives_str)
                if q and q.fun_fact:
                    text += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
                if q and getattr(q, "maps_url", None) and q.maps_url not in text:
                    text += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
                try:
                    await message.reply(text=text, parse_mode="HTML")
                except Exception:
                    pass

                session.next_round()
                session.status = "in_progress"
                await send_solo_round(bot, user.id, session, db)
    finally:
        session.advancing = False
