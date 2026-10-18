"""
Telegram Bot Admin Handlers for GeoGuru & GeoGuessr.
Handles /admin command, admin inline menu, quick stats,
database backup download, and 2FA OTP delivery.
"""

import os
import logging
from pathlib import Path
from typing import Optional
from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile

import config
from config import is_admin
from keyboards.admin_kb import get_admin_keyboard, get_admin_back_kb, get_admin_dashboard_url
from .bot_compat import get_db

logger = logging.getLogger("AdminHandler")

router = Router(name="admin_router")


async def send_admin_otp(bot: Bot, admin_id: int, otp_code: str) -> bool:
    """
    Send 2FA OTP code to admin chat via Telegram bot with clean Uzbek formatting.
    """
    text = (
        "🔐 <b>GeoGuru Admin 2FA Tasdiqlash Kodi</b>\n\n"
        f"Sizning bir martalik kodingiz: <code>{otp_code}</code>\n"
        "⏳ Amal qilish muddati: 5 daqiqa.\n\n"
        "⚠️ Bu kodni hech kimga bermang!"
    )
    try:
        await bot.send_message(chat_id=admin_id, text=text, parse_mode="HTML")
        return True
    except Exception as exc:
        logger.warning(f"Failed to send 2FA OTP to admin {admin_id}: {exc}")
        return False


def format_admin_summary(stats: dict) -> str:
    """Format quick admin stats summary in Uzbek."""
    total_users = stats.get("total_users", 0)
    active_today = stats.get("active_today", 0)
    total_groups = stats.get("total_groups", 0)
    total_games = stats.get("total_games", 0)
    total_answers = stats.get("total_answers", 0)
    accuracy = stats.get("accuracy_percent", 0.0)
    banned = stats.get("banned_users", 0)

    web_url = get_admin_dashboard_url()
    web_hint = f"\n🔗 <i>Web Panel:</i> <a href=\"{web_url}\">{web_url}</a>" if web_url else ""

    return (
        "⚙️ <b>GeoGuru Boshqaruv Paneli (Admin)</b>\n\n"
        "📊 <b>Tezkor ko'rsatkichlar:</b>\n"
        f"👤 Foydalanuvchilar: <b>{total_users:,}</b> (Bugun faol: <b>{active_today:,}</b>)\n"
        f"🚫 Bloklanganlar: <b>{banned:,}</b> ta\n"
        f"💬 Guruhlar: <b>{total_groups:,}</b> ta\n"
        f"🎮 Jami o'yinlar: <b>{total_games:,}</b> ta\n"
        f"🎯 Berilgan javoblar: <b>{total_answers:,}</b> (Aniqlik: <b>{accuracy}%</b>)\n"
        f"{web_hint}\n\n"
        "Quyidagi tugmalar orqali Web Dashboardni ochishingiz yoki amallarni bajarishingiz mumkin:"
    )


@router.message(Command("admin"))
async def cmd_admin(message: Message, bot: Bot):
    """
    Handle /admin command.
    Checks if sender is in configured ADMIN_IDS.
    """
    user_id = message.from_user.id if message.from_user else None

    if not is_admin(user_id):
        await message.reply(
            "⛔️ <b>Ruxsat berilmagan</b>\n\n"
            "Siz bot administratori emassiz. Agar bu xatolik deb hisoblasangiz, bosh administrator bilan bog'laning.",
            parse_mode="HTML"
        )
        return

    db = get_db(bot)
    stats = {}
    if hasattr(db, "get_admin_dashboard_stats"):
        stats = await db.get_admin_dashboard_stats()

    text = format_admin_summary(stats)
    await message.answer(
        text=text,
        reply_markup=get_admin_keyboard(),
        parse_mode="HTML",
        disable_web_page_preview=True
    )


@router.callback_query(F.data == "admin:menu")
async def cb_admin_menu(call: CallbackQuery, bot: Bot):
    """Return to main admin menu."""
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat berilmagan!", show_alert=True)
        return

    db = get_db(bot)
    stats = {}
    if hasattr(db, "get_admin_dashboard_stats"):
        stats = await db.get_admin_dashboard_stats()

    text = format_admin_summary(stats)
    try:
        await call.message.edit_text(
            text=text,
            reply_markup=get_admin_keyboard(),
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    except Exception:
        pass
    await call.answer()


@router.callback_query(F.data == "admin:stats")
async def cb_admin_stats(call: CallbackQuery, bot: Bot):
    """Show detailed stats and top players."""
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat berilmagan!", show_alert=True)
        return

    db = get_db(bot)
    stats = await db.get_admin_dashboard_stats() if hasattr(db, "get_admin_dashboard_stats") else {}

    top_users = stats.get("top_users", [])
    top_text = ""
    for idx, u in enumerate(top_users[:5], 1):
        uname = u.get("username") or u.get("first_name") or f"ID {u.get('user_id')}"
        top_text += f"{idx}. <b>{uname}</b> — {u.get('total_score', 0):,} ball ({u.get('xp', 0):,} XP, Lvl {u.get('level', 1)})\n"

    modes = stats.get("mode_distribution", [])
    mode_text = ""
    for m in modes:
        mode_text += f"• {m.get('mode', 'standard').upper()}: <b>{m.get('match_count', 0)}</b> ta o'yin\n"

    empty_top = "Ma'lumot yo'q"
    empty_modes = "Hozircha o'yinlar qayd etilmagan"
    top_summary = top_text.strip() if top_text else empty_top
    mode_summary = mode_text.strip() if mode_text else empty_modes

    details = (
        "📊 <b>Kengaytirilgan Statistika</b>\n\n"
        f"<b>🏆 Top 5 Peshqadam:</b>\n{top_summary}\n\n"
        f"<b>🎮 O'yin rejimlari taqsimoti:</b>\n{mode_summary}"
    )

    try:
        await call.message.edit_text(
            text=details,
            reply_markup=get_admin_back_kb(),
            parse_mode="HTML"
        )
    except Exception:
        pass
    await call.answer()


@router.callback_query(F.data == "admin:broadcast")
async def cb_admin_broadcast(call: CallbackQuery, bot: Optional[Bot] = None):
    """Provide guidance on Web Broadcast Composer."""
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat berilmagan!", show_alert=True)
        return

    web_url = get_admin_dashboard_url()
    text = (
        "📢 <b>Ommaviy Xabarnoma (Broadcast)</b>\n\n"
        "Xabarnomalarni vizual tahrirlash, rasm va tugmalar qo'shish hamda "
        "jonli yuborish jarayonini kuzatish uchun <b>Web Dashboard</b> ning "
        "<b>Broadcast</b> bo'limidan foydalaning.\n\n"
        f"🌐 Web Panel havolasi: <a href=\"{web_url}\">{web_url}</a>\n\n"
        "<i>Anti-flood himoyasi (25 msg/s) avtomatik ishlaydi.</i>"
    )
    try:
        await call.message.edit_text(
            text=text,
            reply_markup=get_admin_back_kb(),
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    except Exception:
        pass
    await call.answer()


@router.callback_query(F.data == "admin:backup")
async def cb_admin_backup(call: CallbackQuery, bot: Bot):
    """Send geobot.db directly to admin as Telegram document."""
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat berilmagan!", show_alert=True)
        return

    await call.answer("Baza fayli tayyorlanmoqda...")

    db = get_db(bot)
    db_path = getattr(db, "db_path", None) or config.DB_PATH
    p = Path(db_path)

    if not p.is_file():
        candidates = [Path("geobot.db"), Path("data/geobot.db"), Path("/data/geobot.db")]
        for c in candidates:
            if c.is_file():
                p = c
                break

    if not p.is_file():
        await call.message.answer(f"❌ Xatolik: Baza fayli topilmadi ({db_path})")
        return

    try:
        doc = FSInputFile(str(p), filename="geobot_backup.db")
        await call.message.answer_document(
            document=doc,
            caption="💾 <b>GeoGuru SQLite Database Backup</b>\nYuklab olindi va arxivlandi.",
            parse_mode="HTML"
        )
    except Exception as exc:
        await call.message.answer(f"❌ Backup yuborishda xatolik: {exc}")


@router.callback_query(F.data == "admin:web_info")
async def cb_admin_web_info(call: CallbackQuery):
    """Information when WEBAPP_URL is not HTTPS."""
    web_url = get_admin_dashboard_url() or f"http://localhost:{config.WEBAPP_PORT}/admin"
    await call.answer()
    await call.message.answer(
        f"🌐 <b>Web Dashboardga kirish:</b>\n\n"
        f"Brauzer orqali quyidagi manzilga kiring:\n<code>{web_url}</code>\n\n"
        "Telegram ID raqamingizni kiritib 2FA kodi orqali kiring.",
        parse_mode="HTML"
    )
