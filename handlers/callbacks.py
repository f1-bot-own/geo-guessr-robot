"""
Callback Query Handlers for GeoGuru & GeoGuessr Telegram Bot.
Handles answers, game setup, lifelines, menu navigation, languages, and duels.
"""

import asyncio
import inspect
from datetime import datetime
from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from locales.i18n import t, get_rank_name
from database.db import Database, format_user_mention
from games.models import GameMode
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.daily_session import DailyChallengeSession
from games.manager import game_manager
from games.flow import send_round_question, proceed_after_round, send_solo_round, send_daily_round
from keyboards.menu_kb import get_main_menu_kb, get_language_kb
from keyboards.game_kb import (
    get_setup_kb,
    get_solo_setup_kb,
    get_solo_question_kb,
    get_daily_question_kb,
    get_category_selection_kb,
    get_category_overview_text,
    get_hub_subcategories_kb,
    get_game_type_kb,
    get_leaderboard_kb,
    CATEGORY_HUBS_INFO,
)
import config

router = Router()

from .bot_compat import get_db

# ----------------- Group Game Answers -----------------
@router.callback_query(F.data.startswith("ans:"))
async def cb_group_answer(query: CallbackQuery, bot: Bot):
    """Handle option button click during an active group round."""
    db = get_db(bot)
    parts = query.data.split(":")
    if len(parts) != 3:
        await query.answer()
        return

    _, session_id, opt_str = parts
    try:
        opt_idx = int(opt_str)
    except ValueError:
        await query.answer()
        return

    chat = query.message.chat if query.message else None
    user = query.from_user
    if not chat or not user:
        await query.answer()
        return

    chat_id = chat.id
    session = game_manager.get_session(chat_id)

    if not session or session.session_id != session_id:
        await query.answer("⚠️ This game session has ended.", show_alert=True)
        if query.message:
            try:
                await query.message.edit_reply_markup(reply_markup=None)
            except Exception:
                pass
        return

    if getattr(session, "input_mode", "both") == "text":
        await query.answer("✍️ Text Only mode is enabled! Type your answer in the chat.", show_alert=True)
        return

    user_name = user.first_name or user.username or f"User {user.id}"
    result, points, elapsed = await session.check_answer(user.id, user_name, opt_idx)

    if result == "banned":
        await query.answer("⛔ Your account has been banned from participating.", show_alert=True)
    elif result == "inactive":
        await query.answer("⏰ Round has ended or question answered!", show_alert=False)

    elif result == "not_allowed":
        await query.answer("⚔️ This duel is only between the challenged players!", show_alert=True)
    elif result == "already_wrong":
        await query.answer(t("already_answered_wrong", session.lang, user=user_name), show_alert=True)
    elif result == "wrong":
        await query.answer(t("wrong_answer_alert", session.lang, penalty=points), show_alert=True)
        await db.record_answer(user.id, is_correct=False, points=-points, user_name=user_name, username=user.username)
    elif result == "correct":
        # Cancel round timer immediately
        if session.timer_task and not session.timer_task.done():
            session.timer_task.cancel()
        session.current_kb = None

        # Send immediate popup feedback
        await query.answer("🎯 Correct!", show_alert=False)
        try:
            await query.message.edit_reply_markup(reply_markup=None)
        except Exception:
            pass
        await db.record_answer(user.id, is_correct=True, points=points, xp=config.XP_PER_CORRECT, user_name=user_name, username=user.username, chat_id=chat_id)

        q = session.current_question
        correct_ans = q.correct_answer if q else "—"
        user_mention = format_user_mention(user.id, user_name)
        text = t(
            "correct_answer_announcement",
            session.lang,
            user=user_mention,
            time=elapsed,
            points=points,
            answer=correct_ans
        )
        if q and getattr(q, "mode", None) == GameMode.BLUR:
            stage = getattr(q, "blur_stage", 1)
            if stage == 1:
                text += f"\n🔍 <b>+300 {t('mode_blur', session.lang)} bonus!</b>"
            elif stage == 2:
                text += f"\n🔍 <b>+150 {t('mode_blur', session.lang)} bonus!</b>"
        if q and q.fun_fact:
            text += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
        if q and getattr(q, "maps_url", None) and q.maps_url not in text:
            text += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
        if not session.is_game_finished():
            text += f"\n\n⏳ {t('next_round_in', session.lang, seconds=3)}"

        try:
            await bot.send_message(chat_id=chat_id, text=text, parse_mode="HTML")
        except Exception:
            pass

        await proceed_after_round(bot, chat_id, session, db)

# ----------------- Game Setup Controls -----------------
def format_setup_title(session, lang: str) -> str:
    """Format clear, dynamic game setup header showing active modes, blur, continent, and host."""
    host_name = getattr(session, "host_name", "") or session.user_names.get(session.created_by_user_id) or "Host"
    selected = getattr(session, "selected_modes", [])

    all_cat_modes = [
        "zakovat", "astronomy", "science", "history", "literature", "art", "nature", "logic_math",
        "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview",
        "emoji", "contour", "president", "historical", "celebrity", "logo"
    ]
    view_mode = getattr(session, "view_mode", "categories")
    hub_modes_map = {
        "zakovat": ["zakovat", "black_box", "deduction", "world_intellect", "blitz"],
        "geography": [
            "flag", "capital", "landmark", "higher_lower", "coat_of_arms",
            "streetview", "emoji", "contour", "geo_mix"
        ],
        "cosmos_nature": ["astronomy", "nature", "telescope_zoom", "macro_texture", "human_anatomy", "cosmos_nature_mix"],
        "science_logic": ["science", "logic_math", "elements", "flash_math", "odd_one_out", "science_logic_mix"],
        "history_culture": ["history", "literature", "art", "quotes", "art_fragment", "history_culture_mix"],
        "people_brands": ["president", "historical", "celebrity", "logo", "person"],
    }

    if not selected:
        modes_str = t("no_modes_selected_hint", lang)
        count_display = "0"
    elif "mix" in selected or set(all_cat_modes).issubset(set(selected)):
        modes_str = {
            "uz": "🎲 SUPER MIX (Barcha 6 ta toifa, 4,000+ savol)",
            "ru": "🎲 SUPER MIX (Все 6 категорий, 4,000+ вопросов)",
            "en": "🎲 SUPER MIX (All 6 categories, 4,000+ questions)"
        }.get(lang, "🎲 SUPER MIX")
        count_display = "4,000+"
    elif view_mode.startswith("hub:"):
        btn_dict = {b[0]: b[1] for h in CATEGORY_HUBS_INFO.values() for b in h["buttons"]}
        selected_labels = []
        for m in selected:
            if m in btn_dict:
                selected_labels.append(btn_dict[m].get(lang, btn_dict[m].get("en", m)))
            elif t(f"mode_{m}", lang):
                selected_labels.append(t(f"mode_{m}", lang))
            else:
                selected_labels.append(m)
        if selected_labels:
            modes_str = ", ".join(selected_labels)
            count_display = str(len(selected_labels))
        else:
            modes_str = t("no_modes_selected_hint", lang)
            count_display = "0"
    else:
        active_hubs = []
        for h_key, h_info in CATEGORY_HUBS_INFO.items():
            t_modes = hub_modes_map.get(h_key, [])
            if any(m in selected for m in t_modes):
                active_hubs.append(h_info["icon"] + " " + h_info["title"].get(lang, h_key))
        if active_hubs:
            modes_str = ", ".join(active_hubs)
            count_display = str(len(active_hubs))
        else:
            selected_names = [t(f"mode_{m}", lang) for m in selected if t(f"mode_{m}", lang)]
            if len(selected_names) <= 3:
                modes_str = ", ".join(selected_names)
            else:
                modes_str = ", ".join(selected_names[:3]) + f" (+{len(selected_names) - 3})"
            count_display = str(len(selected))

    is_blur = getattr(session, "is_blur", False)
    blur_status = t("status_enabled", lang) if is_blur else t("status_disabled", lang)
    cont = getattr(session, "continent", "all")
    continent_str = t(f"filter_continent_{cont}", lang)
    input_m = getattr(session, "input_mode", "both")
    input_str = t(f"btn_input_{input_m}", lang)

    if view_mode.startswith("hub:"):
        hub_key = view_mode.split(":", 1)[1]
        if hub_key in CATEGORY_HUBS_INFO:
            cat_summary = get_category_overview_text(lang=lang, hub=hub_key) + "\n\n"
        else:
            cat_summary = ""
    elif view_mode == "detailed":
        cat_summary = ""
    else:
        cat_summary = {
            "uz": (
                "📁 <b>Mavjud toifalar (Jami 6 ta asosiy toifa, 24+ yo'nalish, 4,000+ savol):</b>\n"
                "1. 🎓 <b>Zakovat Klubi</b> (500) — Qora quti, Deduksiya, Jahon intellekti, Blits\n"
                "2. 🌍 <b>Geografiya & GeoGuessr</b> (1,000+) — Bayroqlar, Poytaxtlar, Obidalar, Gerblar, Xaritalar\n"
                "3. 🌌 <b>Koinot & Tabiat</b> (800) — Astronomiya, Teleskop, Hayvonot olami, Anatomiya\n"
                "4. 🔬 <b>Fan & Mantiq</b> (800) — Kimyo, Fizika, Ixtirolar, Tezkor Matematika\n"
                "5. 📜 <b>Tarix, Adabiyot & San'at</b> (1,200) — Tarix, Durdona asarlar, Rassomchilik\n"
                "6. 👑 <b>Shaxslar & Brendlar</b> (400+) — Prezidentlar, Yulduzlar, Brend logolari\n"
                "7. 🔍 <b>Blur Reveal</b> (+300 bonus) | 8. 🎲 <b>SUPER MIX</b> (Barchasi)\n\n"
            ),
            "ru": (
                "📁 <b>Доступные категории (Всего 6 категорий, 24+ направлений, 4,000+ вопросов):</b>\n"
                "1. 🎓 <b>Клуб Заковат</b> (500) — Чёрный ящик, Дедукция, Мировой интеллект, Блиц\n"
                "2. 🌍 <b>География и GeoGuessr</b> (1,000+) — Флаги, Столицы, Достопримечательности, Гербы\n"
                "3. 🌌 <b>Космос и Природа</b> (800) — Астрономия, Снимки телескопов, Биология\n"
                "4. 🔬 <b>Наука и Логика</b> (800) — Химия, Физика, Изобретения, Быстрый счёт\n"
                "5. 📜 <b>История и Искусство</b> (1,200) — Всемирная история, Шедевры литературы, Архитектура\n"
                "6. 👑 <b>Личности и Бренды</b> (400+) — Президенты, Знаменитости, Логотипы\n"
                "7. 🔍 <b>Blur Reveal</b> (+300) | 8. 🎲 <b>SUPER MIX</b> (Все темы)\n\n"
            ),
            "en": (
                "📁 <b>Available Categories (6 Main Categories, 4,000+ Questions):</b>\n"
                "1. 🎓 <b>Zakovat Club</b> (500) — Black Box, Logic & Deduction, World Intellect, Blitz\n"
                "2. 🌍 <b>Geography & GeoGuessr</b> (1,000+) — Flags, Capitals, Landmarks, Coats of Arms\n"
                "3. 🌌 <b>Cosmos & Nature</b> (800) — Astronomy, Deep Space, Wildlife, Human Anatomy\n"
                "4. 🔬 <b>Science & Logic</b> (800) — Chemistry, Physics, Inventions, Fast Math\n"
                "5. 📜 <b>History, Literature & Art</b> (1,200) — World History, Literary Classics, Art\n"
                "6. 👑 <b>People & Brands</b> (400+) — Presidents, Historical Figures, Celebrities, Logos\n"
                "7. 🔍 <b>Blur Reveal</b> (+300) | 8. 🎲 <b>SUPER MIX</b> (All Subjects)\n\n"
            )
        }.get(lang, "")

    text = (
        f"⚙️ <b>{t('game_setup_title', lang)}</b>\n"
        f"👑 <b>{t('host_label', lang)}:</b> {host_name}\n\n"
        f"{cat_summary}"
        f"🎯 <b>{t('selected_modes_label', lang)} ({count_display}):</b>\n"
        f"👉 <i>{modes_str}</i>\n\n"
        f"🔍 <b>Blur:</b> {blur_status}\n"
        f"🌐 <b>{t('btn_continent_label', lang)}:</b> {continent_str}\n"
        f"⏱ <b>{t('timer_label', lang)}:</b> {session.round_time}s | 🔢 <b>{t('rounds_label', lang)}:</b> {session.total_rounds}\n"
        f"🎮 <b>{t('input_label', lang)}:</b> {input_str}\n\n"
        f"<i>{t('multi_select_hint', lang)}</i>"
    )
    return text

@router.callback_query(F.data.startswith("setup:"))
async def cb_game_setup(query: CallbackQuery, bot: Bot):
    """Handle interactive game setup configuration with host-only authorization."""
    parts = query.data.split(":")
    if len(parts) == 4:
        _, action, param, session_id = parts
    elif len(parts) == 3:
        _, action, session_id = parts
        param = None
    else:
        await query.answer()
        return

    chat = query.message.chat if query.message else None
    user = query.from_user
    if not chat or not user:
        await query.answer()
        return

    chat_id = chat.id
    session = game_manager.get_session(chat_id)

    if not session or session.session_id != session_id or session.status != "setup":
        await query.answer("⚠️ Setup is expired or game already started.", show_alert=True)
        if query.message:
            try:
                await query.message.edit_reply_markup(reply_markup=None)
            except Exception:
                pass
        return

    # HOST-ONLY AUTHORIZATION: Only the host can adjust setup parameters or start the game
    host_id = getattr(session, "host_id", None) or session.created_by_user_id
    if host_id and user.id != host_id:
        host_name = getattr(session, "host_name", "") or session.user_names.get(host_id) or "Host"
        alert_msg = t("host_only_settings_alert", session.lang, host=host_name)
        await query.answer(alert_msg, show_alert=True)
        return

    rounds_cycle = [5, 10, 15, 20, 3]
    continents = ["all", "asia", "europe", "africa", "americas", "oceania"]
    all_cat_modes = [
        "zakovat", "astronomy", "science", "history", "literature", "art", "nature", "logic_math",
        "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview",
        "emoji", "contour", "president", "historical", "celebrity", "logo"
    ]

    if action == "mode":
        if not hasattr(session, "selected_modes") or session.selected_modes is None:
            session.selected_modes = []

        hub_mix_submodes = {
            "zakovat": ["black_box", "deduction", "world_intellect", "blitz"],
            "geo_mix": [
                "flag", "capital", "landmark", "higher_lower", "coat_of_arms",
                "streetview", "emoji", "contour"
            ],
            "cosmos_nature_mix": [
                "astronomy", "nature", "telescope_zoom", "macro_texture", "human_anatomy"
            ],
            "science_logic_mix": [
                "science", "logic_math", "elements", "flash_math", "odd_one_out"
            ],
            "history_culture_mix": [
                "history", "literature", "art", "quotes", "art_fragment"
            ],
            "person": ["president", "historical", "celebrity", "logo"],
        }

        if param == "mix":
            if set(session.selected_modes) == set(all_cat_modes) or "mix" in session.selected_modes:
                session.selected_modes = []
                session.mode = ""
            else:
                session.selected_modes = list(all_cat_modes)
                session.mode = "mix"
        elif param in hub_mix_submodes:
            sub_list = hub_mix_submodes[param]
            if "mix" in session.selected_modes:
                session.selected_modes = [param] + list(sub_list)
            elif param in session.selected_modes or set(sub_list).issubset(set(session.selected_modes)):
                session.selected_modes = [m for m in session.selected_modes if m != param and m not in sub_list]
            else:
                for m in [param] + list(sub_list):
                    if m not in session.selected_modes:
                        session.selected_modes.append(m)
        elif "mix" in session.selected_modes:
            session.selected_modes = [param]
            session.mode = param
        else:
            parent_mix = None
            parent_subs = []
            for h_mix, h_subs in hub_mix_submodes.items():
                if param in h_subs:
                    parent_mix = h_mix
                    parent_subs = h_subs
                    break

            if parent_mix and (parent_mix in session.selected_modes or set(parent_subs).issubset(set(session.selected_modes))):
                if parent_mix in session.selected_modes:
                    session.selected_modes.remove(parent_mix)
                for m in parent_subs:
                    if m != param and m not in session.selected_modes:
                        session.selected_modes.append(m)
                if param in session.selected_modes:
                    session.selected_modes.remove(param)
            elif param in session.selected_modes:
                session.selected_modes.remove(param)
                if parent_mix and parent_mix in session.selected_modes:
                    session.selected_modes.remove(parent_mix)
            else:
                session.selected_modes.append(param)
                if parent_mix and set(parent_subs).issubset(set(session.selected_modes)):
                    if parent_mix not in session.selected_modes:
                        session.selected_modes.append(parent_mix)

        if len(session.selected_modes) == 1:
            session.mode = session.selected_modes[0]
        elif len(session.selected_modes) > 1:
            session.mode = "mix"
        else:
            session.mode = ""
    elif action in ("hub", "cat"):
        if param == "main":
            session.view_mode = "categories"
        elif param in CATEGORY_HUBS_INFO:
            session.view_mode = f"hub:{param}"
        else:
            session.view_mode = "categories"
    elif action == "view":
        session.view_mode = param
    elif action == "all":
        session.selected_modes = list(all_cat_modes)
        session.mode = "mix"
        await query.answer(t("all_modes_selected", session.lang))
    elif action == "flags_only":
        session.selected_modes = ["flag"]
        session.mode = "flag"
        await query.answer(t("flags_only_selected", session.lang))
    elif action == "blur":
        session.is_blur = not getattr(session, "is_blur", False)
        alert = t("blur_enabled_alert", session.lang) if session.is_blur else t("blur_disabled_alert", session.lang)
        await query.answer(alert)
    elif action == "continent":
        if param and param in continents:
            session.continent = param
        else:
            curr_c = getattr(session, "continent", "all")
            curr_c_idx = continents.index(curr_c) if curr_c in continents else 0
            session.continent = continents[(curr_c_idx + 1) % len(continents)]
    elif action == "rounds":
        if param and param.isdigit():
            session.total_rounds = int(param)
        else:
            current_idx = rounds_cycle.index(session.total_rounds) if session.total_rounds in rounds_cycle else 0
            session.total_rounds = rounds_cycle[(current_idx + 1) % len(rounds_cycle)]
    elif action == "time":
        if param and param.isdigit() and int(param) in (30, 60):
            session.round_time = int(param)
        else:
            session.round_time = 60 if session.round_time == 30 else 30
    elif action == "input":
        input_modes = ["buttons", "text", "both"]
        if param and param in input_modes:
            session.input_mode = param
        else:
            curr = getattr(session, "input_mode", "both")
            curr_idx = input_modes.index(curr) if curr in input_modes else 0
            session.input_mode = input_modes[(curr_idx + 1) % len(input_modes)]
    elif action == "start":
        selected = getattr(session, "selected_modes", [])
        if not selected or len(selected) == 0:
            await query.answer(t("please_select_at_least_one_mode", session.lang), show_alert=True)
            return
        await query.answer("🚀 Launching game!")
        try:
            await query.message.delete()
        except Exception:
            pass
        session.start_game()
        await send_round_question(bot, chat_id, session, get_db(bot))
        return
    elif action == "cancel":
        game_manager.remove_session(chat_id)
        await query.answer("Game cancelled.")
        try:
            await query.message.edit_text("❌ <i>Game setup cancelled.</i>", parse_mode="HTML")
        except Exception:
            pass
        return

    # Update keyboard and message with new settings
    kb = get_setup_kb(
        session_id=session.session_id,
        mode=session.mode,
        rounds=session.total_rounds,
        round_time=session.round_time,
        lang=session.lang,
        input_mode=getattr(session, "input_mode", "both"),
        continent=getattr(session, "continent", "all"),
        selected_modes=getattr(session, "selected_modes", [session.mode]),
        is_blur=getattr(session, "is_blur", False),
        view_mode=getattr(session, "view_mode", "categories")
    )
    title_text = format_setup_title(session, session.lang)
    try:
        await query.message.edit_text(text=title_text, reply_markup=kb, parse_mode="HTML")
    except Exception:
        try:
            await query.message.edit_reply_markup(reply_markup=kb)
        except Exception:
            pass
    if action not in ("all", "flags_only", "blur"):
        await query.answer()

# ----------------- Daily Challenge Answers -----------------
@router.callback_query(F.data.startswith("daily_ans:"))
async def cb_daily_answer(query: CallbackQuery, bot: Bot):
    """Handle daily challenge round answer."""
    db = get_db(bot)
    user = query.from_user
    if not user:
        await query.answer()
        return

    parts = query.data.split(":")
    if len(parts) != 2 or not parts[1].isdigit():
        await query.answer()
        return
    opt_idx = int(parts[1])

    session = game_manager.get_daily_session(user.id)
    if not session or session.status != "in_progress":
        await query.answer("⚠️ Today's challenge ended or expired.", show_alert=True)
        if query.message:
            try:
                await query.message.edit_reply_markup(reply_markup=None)
            except Exception:
                pass
        return

    is_correct, points, is_finished, correct_answer = session.check_answer(opt_idx)

    try:
        await query.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    if is_correct:
        await query.answer(f"🎯 Correct! +{points} pts", show_alert=False)
    else:
        await query.answer(f"❌ Incorrect! Correct answer: {correct_answer}", show_alert=True)

    if not is_finished:
        await send_daily_round(bot, user.id, session)
    else:
        bonus_xp = 150
        await db.record_daily_completion(user.id, session.date_str, score=session.score, xp=bonus_xp)
        await db.record_answer(user.id, is_correct=True, points=session.score, xp=bonus_xp, user_name=user.first_name)

        user_row = await db.get_user(user.id)
        streak = (user_row.get("daily_streak", 1) if user_row else 1)
        game_manager.remove_daily_session(user.id)

        msg = (
            f"{t('daily_completed_msg', session.lang, score=session.score, xp=bonus_xp)}\n\n"
            f"🎯 <b>Accuracy:</b> {session.correct_count}/{session.TOTAL_ROUNDS} correct\n"
            f"🔥 <b>Daily Streak:</b> {streak} day(s)!\n\n"
            f"<i>Come back tomorrow for a new challenge!</i>"
        )
        try:
            await bot.send_message(chat_id=user.id, text=msg, parse_mode="HTML")
        except Exception:
            pass

# ----------------- Solo Mode Answers & Lifelines -----------------
@router.callback_query(F.data.startswith("solo_ans:"))
async def cb_solo_answer(query: CallbackQuery, bot: Bot):
    """Handle solo mode question answer with optimized low-latency concurrent processing."""
    db = get_db(bot)
    user = query.from_user
    if not user:
        await query.answer()
        return

    parts = query.data.split(":")
    if len(parts) != 2 or not parts[1].isdigit():
        await query.answer()
        return
    opt_idx = int(parts[1])

    session = game_manager.get_solo_session(user.id)
    if not session:
        await query.answer("⚠️ Solo session ended. Start a new one with /solo!", show_alert=True)
        if query.message:
            try:
                await query.message.edit_reply_markup(reply_markup=None)
            except Exception:
                pass
        return

    if getattr(session, "input_mode", "both") == "text":
        await query.answer("✍️ Text Only mode is enabled! Type your answer in the chat.", show_alert=True)
        return

    async with session.lock:
        if session.status != "in_progress" or getattr(session, "advancing", False):
            await query.answer("⏰ Round has ended!", show_alert=False)
            return
        session.advancing = True

    try:
        if opt_idx in session.eliminated_options:
            await query.answer("This option has been eliminated!", show_alert=False)
            return

        session.current_kb = None

        # Cancel active countdown timer cleanly on answer
        if session.timer_task and not session.timer_task.done():
            session.timer_task.cancel()

        q = session.current_question
        correct_ans = q.correct_answer if q else ""
        is_correct, points, is_game_over = session.check_answer(opt_idx)

        user_name = user.first_name or user.username or "Player"
        if is_correct:
            await query.answer(f"🎯 Correct! +{points} pts", show_alert=False)
            try:
                await query.message.edit_reply_markup(reply_markup=None)
            except Exception:
                pass
            await db.record_answer(user.id, is_correct=True, points=points, xp=config.XP_PER_CORRECT, user_name=user_name, username=user.username)
            text = t("solo_correct_answer_announcement", session.lang, points=points, answer=correct_ans)
            if q and q.fun_fact:
                text += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
            if q and getattr(q, "maps_url", None) and q.maps_url not in text:
                text += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"

            session.next_round()
            session.status = "in_progress"

            try:
                await bot.send_message(chat_id=user.id, text=text, parse_mode="HTML")
            except Exception:
                pass
            await send_solo_round(bot, user.id, session, db)
        else:
            if is_game_over:
                await query.answer("💔 Out of lives!", show_alert=True)
                try:
                    await query.message.edit_reply_markup(reply_markup=None)
                except Exception:
                    pass
                await db.record_answer(user.id, is_correct=False, points=0, user_name=user_name, username=user.username)
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
                    await bot.send_message(chat_id=user.id, text=text, parse_mode="HTML")
                except Exception:
                    pass
            else:
                lives_str = "❤️" * session.lives
                await query.answer(f"❌ Wrong answer! Lives remaining: {session.lives}", show_alert=True)
                try:
                    await query.message.edit_reply_markup(reply_markup=None)
                except Exception:
                    pass
                await db.record_answer(user.id, is_correct=False, points=0, user_name=user_name, username=user.username)
                text = t("solo_wrong_answer_announcement", session.lang, answer=correct_ans, lives=lives_str)
                if q and q.fun_fact:
                    text += f"\n\n💡 <b>Fact:</b> {q.fun_fact}"
                if q and getattr(q, "maps_url", None) and q.maps_url not in text:
                    text += f"\n🗺️ <a href=\"{q.maps_url}\">{t('streetview_view_maps', session.lang)}</a>"
                try:
                    await bot.send_message(chat_id=user.id, text=text, parse_mode="HTML")
                except Exception:
                    pass

                session.next_round()
                session.status = "in_progress"
                await send_solo_round(bot, user.id, session, db)
    finally:
        session.advancing = False

@router.callback_query(F.data == "solo_hint")
async def cb_solo_hint(query: CallbackQuery):
    """Deliver solo hint lifeline."""
    user = query.from_user
    if not user:
        await query.answer()
        return
    session = game_manager.get_solo_session(user.id)
    if not session or session.status != "in_progress" or not session.has_hint:
        await query.answer("Hint is already used!", show_alert=True)
        return

    async with session.lock:
        hint_text = session.use_hint()
        if session.current_question:
            is_text_only = (getattr(session, "input_mode", "both") == "text")
            kb = get_solo_question_kb(
                options=session.current_question.options,
                eliminated=session.eliminated_options,
                has_hint=session.has_hint,
                has_5050=session.has_5050,
                lang=session.lang,
                text_only=is_text_only
            )
            session.current_kb = kb
            try:
                await query.message.edit_reply_markup(reply_markup=kb)
            except Exception:
                pass
    await query.answer(hint_text or "No hint available.", show_alert=True)

@router.callback_query(F.data == "solo_5050")
async def cb_solo_5050(query: CallbackQuery):
    """Apply 50/50 lifeline removing two incorrect answers."""
    user = query.from_user
    if not user:
        await query.answer()
        return
    session = game_manager.get_solo_session(user.id)
    if not session or session.status != "in_progress" or not session.has_5050:
        await query.answer("50/50 is already used!", show_alert=True)
        return

    async with session.lock:
        session.use_5050()
        is_text_only = (getattr(session, "input_mode", "both") == "text")
        kb = get_solo_question_kb(
            options=session.current_question.options,
            eliminated=session.eliminated_options,
            has_hint=session.has_hint,
            has_5050=session.has_5050,
            lang=session.lang,
            text_only=is_text_only
        )
        session.current_kb = kb
        try:
            await query.message.edit_reply_markup(reply_markup=kb)
            await query.answer("✂️ Two wrong answers eliminated!")
        except Exception:
            await query.answer()

@router.callback_query(F.data == "solo_ignore")
async def cb_solo_ignore(query: CallbackQuery):
    await query.answer("This option has been eliminated!", show_alert=False)

# ----------------- Language Switcher -----------------
@router.callback_query(F.data.startswith("set_lang:"))
async def cb_set_language(query: CallbackQuery, bot: Bot):
    """Update language for user or group."""
    db = get_db(bot)
    parts = query.data.split(":")
    if len(parts) < 2:
        await query.answer()
        return
    new_lang = parts[1]
    if new_lang not in config.SUPPORTED_LANGUAGES:
        new_lang = "en"

    chat = query.message.chat if query.message else None
    user = query.from_user
    if not user:
        await query.answer()
        return

    lang_names = {"en": "English 🇬🇧", "ru": "Русский 🇷🇺", "uz": "O'zbekcha 🇺🇿"}
    lang_name = lang_names.get(new_lang, new_lang)

    if chat and chat.type in ("group", "supergroup"):
        await db.set_chat_language(chat.id, new_lang)
        active_session = game_manager.get_session(chat.id)
        if active_session:
            active_session.lang = new_lang
        try:
            from game.engine import game_manager as engine_gm
            eng_session = engine_gm.get_group_game(chat.id)
            if eng_session:
                eng_session.lang = new_lang
        except Exception:
            pass
    else:
        await db.set_user_language(user.id, new_lang)
        active_solo = game_manager.get_solo_session(user.id)
        if active_solo:
            active_solo.lang = new_lang
        try:
            from game.engine import game_manager as engine_gm
            eng_solo = engine_gm.get_solo_game(user.id)
            if eng_solo:
                eng_solo.lang = new_lang
        except Exception:
            pass

    text = t("lang_changed", new_lang, lang_name=lang_name)
    await query.answer(f"Language: {lang_name}")
    if query.message:
        try:
            await query.message.edit_text(text=text, parse_mode="HTML")
        except Exception:
            try:
                await query.message.answer(text=text, parse_mode="HTML")
            except Exception:
                pass

# ----------------- Main Menu Navigation -----------------
@router.callback_query(F.data.startswith("menu:"))
async def cb_main_menu(query: CallbackQuery, bot: Bot):
    """Handle menu item clicks."""
    db = get_db(bot)
    parts = query.data.split(":")
    if len(parts) < 2:
        await query.answer()
        return
    action = parts[1]
    user = query.from_user
    if not user:
        await query.answer()
        return
    user_data = await db.get_user(user.id)
    lang = user_data.get("language", "en") if user_data else "en"

    if action == "play":
        bot_info = await bot.get_me()
        await query.answer()
        try:
            await query.message.edit_text(
                text=t("choose_game_type", lang),
                reply_markup=get_game_type_kb(lang, bot_username=bot_info.username),
                parse_mode="HTML"
            )
        except Exception:
            try:
                await bot.send_message(
                    chat_id=user.id,
                    text=t("choose_game_type", lang),
                    reply_markup=get_game_type_kb(lang, bot_username=bot_info.username),
                    parse_mode="HTML"
                )
            except Exception:
                pass
    elif action == "solo":
        # Present all categories cleanly as buttons
        await query.answer()
        cur_input = game_manager.get_solo_setup_state(user.id).get("input_mode", "both")
        try:
            await query.message.edit_text(
                text=get_category_overview_text(lang),
                reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=cur_input),
                parse_mode="HTML"
            )
        except Exception:
            try:
                await bot.send_message(
                    chat_id=user.id,
                    text=get_category_overview_text(lang),
                    reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=cur_input),
                    parse_mode="HTML"
                )
            except Exception:
                pass
    elif action == "daily":
        today_str = datetime.utcnow().strftime("%Y-%m-%d")
        if not await db.can_play_daily(user.id, today_str):
            record = await db.check_daily_challenge_done(user.id, today_str)
            score = record.get("score", 100) if record else 100
            await query.answer(t("daily_already_done", lang, score=score), show_alert=True)
            return
        daily_session = DailyChallengeSession(user.id, user.first_name or "Player", lang=lang, date_str=today_str)
        game_manager.set_daily_session(user.id, daily_session)
        await query.answer("📅 Launching Daily Challenge!")
        try:
            await bot.send_message(
                chat_id=user.id,
                text=f"{t('daily_title', lang)}\n🎯 <i>5 unique questions for today! Answer all to earn bonus XP!</i>",
                parse_mode="HTML"
            )
        except Exception:
            pass
        await send_daily_round(bot, user.id, daily_session)
    elif action == "profile":
        await query.answer()
        lvl = user_data.get("level", 1) if user_data else 1
        xp = user_data.get("xp", 0) if user_data else 0
        games = user_data.get("games_played", 0) if user_data else 0
        wins = user_data.get("games_won", 0) if user_data else 0
        correct = user_data.get("correct_answers", 0) if user_data else 0
        total = user_data.get("total_answers", 0) if user_data else 0
        streak = user_data.get("best_streak", 0) if user_data else 0
        accuracy = int((correct / max(1, total)) * 100) if total > 0 else 0
        rank = get_rank_name(lvl, lang)

        text = (
            f"{t('profile_title', lang, name=user.first_name or 'Player')}\n\n"
            f"{t('profile_details', lang, rank=rank, level=lvl, xp=xp, games=games, wins=wins, correct=correct, total=total, accuracy=accuracy, streak=streak)}"
        )
        try:
            await bot.send_message(chat_id=user.id, text=text, parse_mode="HTML")
        except Exception:
            pass
    elif action == "leaderboard":
        await query.answer()
        from handlers.commands import format_leaderboard_text
        top_players = await db.get_global_leaderboard(limit=10, period="all_time")
        text = format_leaderboard_text(top_players, lb_type="global", period="all_time", lang=lang)
        kb = get_leaderboard_kb(lb_type="global", current_period="all_time", lang=lang)
        try:
            await bot.send_message(chat_id=user.id, text=text, reply_markup=kb, parse_mode="HTML")
        except Exception:
            pass
    elif action == "language":
        await query.answer()
        try:
            await bot.send_message(chat_id=user.id, text=t("choose_lang", lang), reply_markup=get_language_kb(), parse_mode="HTML")
        except Exception:
            pass
    elif action == "help":
        await query.answer()
        try:
            await bot.send_message(chat_id=user.id, text=t("help_text", lang), parse_mode="HTML")
        except Exception:
            pass
    elif action in ("miniapp", "miniapp_info"):
        await query.answer()
        from keyboards.menu_kb import get_miniapp_launch_kb
        try:
            await bot.send_message(
                chat_id=user.id,
                text=t("miniapp_intro", lang),
                reply_markup=get_miniapp_launch_kb(lang),
                parse_mode="HTML"
            )
        except Exception:
            pass

# ----------------- Game Type Selection -----------------
@router.callback_query(F.data.startswith("game_type:"))
async def cb_game_type(query: CallbackQuery, bot: Bot):
    """Handle Game Type selection (Group vs Solo vs Daily)."""
    db = get_db(bot)
    parts = query.data.split(":")
    if len(parts) < 2:
        await query.answer()
        return
    action = parts[1]
    user = query.from_user
    if not user:
        await query.answer()
        return
    user_data = await db.get_user(user.id)
    lang = user_data.get("language", "en") if user_data else "en"

    if action == "solo":
        await query.answer()
        cur_input = game_manager.get_solo_setup_state(user.id).get("input_mode", "both")
        try:
            await query.message.edit_text(
                text=get_category_overview_text(lang),
                reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=cur_input),
                parse_mode="HTML"
            )
        except Exception:
            try:
                await bot.send_message(
                    chat_id=user.id,
                    text=get_category_overview_text(lang),
                    reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=cur_input),
                    parse_mode="HTML"
                )
            except Exception:
                pass
    elif action == "daily":
        today_str = datetime.utcnow().strftime("%Y-%m-%d")
        if not await db.can_play_daily(user.id, today_str):
            record = await db.check_daily_challenge_done(user.id, today_str)
            score = record.get("score", 100) if record else 100
            await query.answer(t("daily_already_done", lang, score=score), show_alert=True)
            return
        daily_session = DailyChallengeSession(user.id, user.first_name or "Player", lang=lang, date_str=today_str)
        game_manager.set_daily_session(user.id, daily_session)
        await query.answer("📅 Launching Daily Challenge!")
        try:
            await bot.send_message(
                chat_id=user.id,
                text=f"{t('daily_title', lang)}\n🎯 <i>5 unique questions for today! Answer all to earn bonus XP!</i>",
                parse_mode="HTML"
            )
        except Exception:
            pass
        await send_daily_round(bot, user.id, daily_session)
    elif action == "menu":
        bot_info = await bot.get_me()
        await query.answer()
        try:
            await query.message.edit_text(
                text=t("welcome_private", lang),
                reply_markup=get_main_menu_kb(lang, bot_username=bot_info.username),
                parse_mode="HTML"
            )
        except Exception:
            pass

# ----------------- Solo Category Selection -----------------
@router.callback_query(F.data.startswith("solo_cat:"))
async def cb_solo_category(query: CallbackQuery, bot: Bot):
    """Handle solo mode category selection and start solo match."""
    parts = query.data.split(":")
    if len(parts) < 2:
        await query.answer()
        return
    cat = parts[1]
    db = get_db(bot)
    user = query.from_user
    if not user:
        await query.answer()
        return
    user_data = await db.get_user(user.id)
    lang = user_data.get("language", "en") if user_data else "en"

    if cat == "back":
        bot_info = await bot.get_me()
        await query.answer()
        try:
            await query.message.edit_text(
                text=t("welcome_private", lang),
                reply_markup=get_main_menu_kb(lang, bot_username=bot_info.username),
                parse_mode="HTML"
            )
        except Exception:
            pass
        return

    if cat == "input":
        mode_val = parts[2] if len(parts) > 2 else "both"
        game_manager.set_solo_setup_state(user.id, {"input_mode": mode_val})
        new_kb = get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=mode_val)
        try:
            await query.message.edit_reply_markup(reply_markup=new_kb)
        except Exception:
            pass
        await query.answer()
        return

    if cat == "hub":
        hub_name = parts[2] if len(parts) > 2 else "main"
        await query.answer()
        cur_input = game_manager.get_solo_setup_state(user.id).get("input_mode", "both")
        if hub_name == "main":
            try:
                await query.message.edit_text(
                    text=get_category_overview_text(lang),
                    reply_markup=get_category_selection_kb(prefix="solo_cat", lang=lang, input_mode=cur_input),
                    parse_mode="HTML"
                )
            except Exception:
                pass
        else:
            try:
                await query.message.edit_text(
                    text=get_category_overview_text(lang, hub=hub_name),
                    reply_markup=get_hub_subcategories_kb(hub=hub_name, prefix="solo_cat", lang=lang),
                    parse_mode="HTML"
                )
            except Exception:
                pass
        return

    hub_modes_map = {
        "zakovat": ["black_box", "deduction", "world_intellect", "blitz"],
        "geo_mix": [
            "flag", "capital", "landmark", "higher_lower", "coat_of_arms",
            "streetview", "emoji", "contour"
        ],
        "cosmos_nature_mix": [
            "telescope_zoom", "cosmic_scale", "constellations", "space_missions",
            "macro_texture", "animal_scale", "nature_emoji", "human_anatomy"
        ],
        "science_logic_mix": [
            "elements", "prototypes", "scientists", "macro_science",
            "flash_math", "odd_one_out", "logic_sequence", "classic_riddles"
        ],
        "history_culture_mix": [
            "timeline", "empire_maps", "who_am_i", "artifacts",
            "quotes", "book_emojis", "authors", "characters",
            "art_fragment", "architecture", "artist_styles", "sculptures"
        ],
        "person": ["president", "historical", "celebrity", "logo"],
        "astronomy": ["telescope_zoom", "cosmic_scale", "constellations", "space_missions"],
        "nature": ["macro_texture", "animal_scale", "nature_emoji", "human_anatomy"],
        "science": ["elements", "prototypes", "scientists", "macro_science"],
        "logic_math": ["flash_math", "odd_one_out", "logic_sequence", "classic_riddles"],
        "history": ["timeline", "empire_maps", "who_am_i", "artifacts"],
        "literature": ["quotes", "book_emojis", "authors", "characters"],
        "art": ["art_fragment", "architecture", "artist_styles", "sculptures"],
        "mix": [
            "flag", "capital", "landmark", "higher_lower", "coat_of_arms",
            "streetview", "emoji", "contour", "president", "historical",
            "celebrity", "logo", "black_box", "deduction", "world_intellect", "blitz",
            "telescope_zoom", "cosmic_scale", "constellations", "space_missions",
            "elements", "prototypes", "scientists", "macro_science",
            "timeline", "empire_maps", "who_am_i", "artifacts",
            "quotes", "book_emojis", "authors", "characters",
            "art_fragment", "architecture", "artist_styles", "sculptures",
            "macro_texture", "animal_scale", "nature_emoji", "human_anatomy",
            "flash_math", "odd_one_out", "logic_sequence", "classic_riddles"
        ]
    }

    if cat in hub_modes_map:
        selected_modes = hub_modes_map[cat]
        chosen_mode = cat
    elif cat in getattr(GameMode, "VALID_MODES", []):
        selected_modes = [cat]
        chosen_mode = cat
    elif cat == "blur":
        selected_modes = ["flag", "president", "landmark", "coat_of_arms", "logo"]
        chosen_mode = "blur"
    else:
        selected_modes = hub_modes_map["mix"]
        chosen_mode = "mix"

    existing = game_manager.get_solo_session(user.id)
    if existing:
        existing.stop()

    saved_state = game_manager.get_solo_setup_state(user.id)
    chosen_input_mode = saved_state.get("input_mode", "both")
    chosen_continent = saved_state.get("continent", "all")

    is_blur_mode = (cat == "blur")
    round_time = 60 if (chosen_mode in ("zakovat", "black_box", "deduction", "world_intellect")) else config.DEFAULT_ROUND_TIME

    solo_session = SoloGameSession(
        user_id=user.id,
        user_name=user.first_name or "Player",
        lang=lang,
        mode=chosen_mode,
        round_time=round_time,
        input_mode=chosen_input_mode,
        continent=chosen_continent,
        selected_modes=selected_modes,
        is_blur=is_blur_mode
    )
    game_manager.set_solo_session(user.id, solo_session)
    solo_session.next_round()

    mode_display = t(f"mode_{chosen_mode}", lang)
    if not mode_display or mode_display == f"mode_{chosen_mode}":
        mode_display = chosen_mode.replace("_", " ").title()
    await query.answer(f"Starting {mode_display}!")
    try:
        await query.message.delete()
    except Exception:
        pass
    await send_solo_round(bot, user.id, solo_session, db)

# ----------------- Solo Setup Lobby -----------------
@router.callback_query(F.data.startswith("solo_setup:"))
async def cb_solo_setup(query: CallbackQuery, bot: Bot):
    """Handle interactive solo mode setup."""
    parts = query.data.split(":")
    if len(parts) < 2:
        await query.answer()
        return
    action = parts[1]
    param = parts[2] if len(parts) > 2 else None
    user = query.from_user
    if not user:
        await query.answer()
        return
    db = get_db(bot)
    user_data = await db.get_user(user.id)
    lang = user_data.get("language", "en") if user_data else "en"
    state = game_manager.get_solo_setup_state(user.id)
    if "selected_modes" not in state or state["selected_modes"] is None:
        init_mode = state.get("mode", "")
        if init_mode and init_mode not in ("mix", "blur"):
            state["selected_modes"] = [init_mode]
        else:
            state["selected_modes"] = []
        state["is_blur"] = state.get("is_blur", init_mode == "blur")

    continents = ["all", "asia", "europe", "africa", "americas", "oceania"]
    all_cat_modes = [
        "zakovat", "astronomy", "science", "history", "literature", "art", "nature", "logic_math",
        "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview",
        "emoji", "contour", "president", "historical", "celebrity", "logo"
    ]

    if action == "mode":
        if "selected_modes" not in state or state["selected_modes"] is None:
            state["selected_modes"] = []

        if param == "mix":
            if set(state["selected_modes"]) == set(all_cat_modes) or "mix" in state["selected_modes"]:
                state["selected_modes"] = []
                state["mode"] = ""
            else:
                state["selected_modes"] = list(all_cat_modes)
                state["mode"] = "mix"
        elif "mix" in state["selected_modes"]:
            state["selected_modes"] = [param]
            state["mode"] = param
        else:
            if param in state["selected_modes"]:
                state["selected_modes"].remove(param)
            else:
                state["selected_modes"].append(param)

            if len(state["selected_modes"]) == 1:
                state["mode"] = state["selected_modes"][0]
            elif len(state["selected_modes"]) > 1:
                state["mode"] = "mix"
            else:
                state["mode"] = ""
    elif action == "all":
        state["selected_modes"] = list(all_cat_modes)
        state["mode"] = "mix"
        await query.answer(t("all_modes_selected", lang))
    elif action == "flags_only":
        state["selected_modes"] = ["flag"]
        state["mode"] = "flag"
        await query.answer(t("flags_only_selected", lang))
    elif action == "blur":
        state["is_blur"] = not state.get("is_blur", False)
        alert = t("blur_enabled_alert", lang) if state["is_blur"] else t("blur_disabled_alert", lang)
        await query.answer(alert)
    elif action == "continent":
        if param in continents:
            state["continent"] = param
        else:
            curr_c = state.get("continent", "all")
            curr_c_idx = continents.index(curr_c) if curr_c in continents else 0
            state["continent"] = continents[(curr_c_idx + 1) % len(continents)]
    elif action == "time":
        if param and param.isdigit():
            state["round_time"] = int(param)
    elif action == "input":
        if param in ["buttons", "text", "both"]:
            state["input_mode"] = param
    elif action == "start":
        selected = state.get("selected_modes")
        if not selected or len(selected) == 0:
            await query.answer(t("please_select_at_least_one_mode", lang), show_alert=True)
            return
        existing = game_manager.get_solo_session(user.id)
        if existing:
            existing.stop()
        solo_session = SoloGameSession(
            user_id=user.id,
            user_name=user.first_name or "Player",
            lang=lang,
            mode=state.get("mode", "mix"),
            round_time=state.get("round_time", 30),
            input_mode=state.get("input_mode", "both"),
            continent=state.get("continent", "all"),
            selected_modes=state.get("selected_modes"),
            is_blur=state.get("is_blur", False)
        )
        game_manager.set_solo_session(user.id, solo_session)
        solo_session.next_round()
        try:
            await query.message.delete()
        except Exception:
            pass
        await query.answer("Starting solo game!")
        await send_solo_round(bot, user.id, solo_session, db)
        return
    elif action == "cancel":
        try:
            await query.message.delete()
        except Exception:
            pass
        await query.answer("Solo setup cancelled.")
        return

    game_manager.set_solo_setup_state(user.id, state)
    kb = get_solo_setup_kb(
        mode=state.get("mode", "mix"),
        round_time=state.get("round_time", 30),
        input_mode=state.get("input_mode", "both"),
        lang=lang,
        continent=state.get("continent", "all"),
        selected_modes=state.get("selected_modes"),
        is_blur=state.get("is_blur", False)
    )
    try:
        await query.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass
    if action not in ("all", "flags_only", "blur"):
        await query.answer()

# ----------------- Duel Acceptance -----------------
@router.callback_query(F.data.startswith("duel:"))
async def cb_duel(query: CallbackQuery, bot: Bot):
    """Handle duel acceptance or decline."""
    db = get_db(bot)
    parts = query.data.split(":")
    if len(parts) < 4 or not parts[2].isdigit() or not parts[3].isdigit():
        await query.answer()
        return

    action = parts[1]
    challenger_id = int(parts[2])
    target_id = int(parts[3])
    duel_id = int(parts[4]) if len(parts) >= 5 and parts[4].isdigit() else 0
    chat = query.message.chat if query.message else None
    user = query.from_user
    if not chat or not user:
        await query.answer()
        return

    chat_id = chat.id

    # Authorization: target can accept/decline; challenger can decline (cancel); others cannot
    if user.id != target_id and not (action == "decline" and user.id == challenger_id):
        await query.answer("Only the challenged player can accept or decline this duel!", show_alert=True)
        return

    lang = await db.get_chat_language(chat_id)
    invite = game_manager.get_duel_invite(chat_id)

    # Check expiration: if active invite exists in chat, duel_id must match.
    if invite and duel_id and invite.get("duel_id") != duel_id:
        await query.answer("⚠️ This duel challenge has expired or already ended.", show_alert=True)
        if query.message:
            try:
                await query.message.edit_reply_markup(reply_markup=None)
            except Exception:
                pass
        return

    # Check database status if duel invite is not in memory
    if not invite and duel_id and hasattr(db, "get_duel"):
        get_duel_fn = getattr(db, "get_duel", None)
        if callable(get_duel_fn):
            res = get_duel_fn(duel_id)
            duel_record = await res if inspect.isawaitable(res) else res
            if isinstance(duel_record, dict) and duel_record.get("status") in ("expired", "declined", "completed"):
                await query.answer("⚠️ This duel challenge has expired or already ended.", show_alert=True)
                if query.message:
                    try:
                        await query.message.edit_reply_markup(reply_markup=None)
                    except Exception:
                        pass
                return

    if action == "decline":
        if invite:
            exp_task = invite.get("expire_task")
            if exp_task and not exp_task.done():
                exp_task.cancel()
            game_manager.remove_duel_invite(chat_id)
        if duel_id:
            await db.update_duel_status(duel_id, status="declined")
        await query.answer("Duel declined.")
        try:
            decline_msg = t("duel_declined", lang) if user.id == target_id else "❌ <i>Duel challenge cancelled by challenger.</i>"
            await query.message.edit_text(decline_msg, parse_mode="HTML")
        except Exception:
            pass
        return

    if action == "accept":
        # Check if game already in progress in chat
        active_session = game_manager.get_session(chat_id)
        if active_session and active_session.status in ("in_progress", "setup", "between_rounds"):
            await query.answer(t("game_already_active", lang), show_alert=True)
            return

        if invite:
            exp_task = invite.get("expire_task")
            if exp_task and not exp_task.done():
                exp_task.cancel()
            game_manager.remove_duel_invite(chat_id)
        if duel_id:
            await db.update_duel_status(duel_id, status="active")
        await query.answer("⚔️ Duel Accepted! Starting 3-round battle!")
        
        # Start a 3-round duel
        session = GameSession(
            chat_id=chat_id,
            created_by_user_id=challenger_id,
            is_group=True,
            lang=lang,
            mode="mix",
            total_rounds=3,
            round_time=config.DEFAULT_ROUND_TIME,
            is_duel=True,
            duel_target_id=target_id,
            duel_id=duel_id
        )
        game_manager.set_session(chat_id, session)

        try:
            await query.message.delete()
        except Exception:
            pass

        session.start_game()
        try:
            await bot.send_message(
                chat_id=chat_id,
                text=f"⚔️ <b>DUEL STARTED!</b>\n3 intense rounds! Only the two duelists may answer!",
                parse_mode="HTML"
            )
        except Exception:
            pass
        await send_round_question(bot, chat_id, session, db)

# ----------------- Time-based Leaderboard Period Switcher -----------------
@router.callback_query(F.data.startswith("lb_period:"))
async def cb_leaderboard_period(query: CallbackQuery, bot: Bot):
    """Handle interactive period switching for global and group leaderboards."""
    db = get_db(bot)
    parts = query.data.split(":")
    if len(parts) < 3:
        await query.answer()
        return

    lb_type = parts[1]  # "global" or "group"
    period = parts[2]   # "daily", "weekly", "monthly", "all_time"
    chat = query.message.chat if query.message else None
    user = query.from_user
    if not chat or not user:
        await query.answer()
        return
    chat_id = chat.id

    if lb_type == "group" and chat.type in ("group", "supergroup"):
        lang = await db.get_chat_language(chat_id)
        players = await db.get_group_leaderboard(chat_id, limit=10, period=period)
    else:
        user_data = await db.get_user(user.id)
        lang = user_data.get("language", "en") if user_data else "en"
        players = await db.get_global_leaderboard(limit=10, period=period)

    from handlers.commands import format_leaderboard_text
    text = format_leaderboard_text(players, lb_type=lb_type, period=period, lang=lang)
    kb = get_leaderboard_kb(lb_type=lb_type, current_period=period, lang=lang)

    try:
        await query.message.edit_text(text=text, reply_markup=kb, parse_mode="HTML")
    except Exception:
        pass
    await query.answer()

