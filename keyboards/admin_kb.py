"""
Admin Keyboards for GeoGuru Telegram Bot.
Includes WebApp dashboard launcher and interactive admin controls.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import config


def get_admin_dashboard_url() -> str:
    """Resolve full URL to Web Admin Dashboard."""
    base = config.WEBAPP_URL or ""
    if base:
        clean_base = base.rstrip("/")
        if clean_base.endswith("/admin"):
            return clean_base
        return f"{clean_base}/admin"
    return ""


def get_admin_keyboard() -> InlineKeyboardMarkup:
    """Generate main inline admin control panel keyboard."""
    admin_url = get_admin_dashboard_url()

    # Top Row: WebApp Dashboard launcher
    if admin_url and admin_url.startswith("https://"):
        web_btn = InlineKeyboardButton(
            text="🌐 Web Dashboardni ochish",
            web_app=WebAppInfo(url=admin_url)
        )
    elif admin_url:
        web_btn = InlineKeyboardButton(
            text="🌐 Web Dashboardni ochish",
            url=admin_url
        )
    else:
        web_btn = InlineKeyboardButton(
            text="🌐 Web Dashboard haqida",
            callback_data="admin:web_info"
        )

    keyboard = [
        [web_btn],
        [
            InlineKeyboardButton(text="📊 Statistika", callback_data="admin:stats"),
            InlineKeyboardButton(text="📢 Xabar yuborish", callback_data="admin:broadcast"),
        ],
        [
            InlineKeyboardButton(text="💾 DB Backup olish", callback_data="admin:backup"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_admin_back_kb() -> InlineKeyboardMarkup:
    """Back button to return to admin menu."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="◀️ Admin menyusiga qaytish", callback_data="admin:menu")]
        ]
    )
