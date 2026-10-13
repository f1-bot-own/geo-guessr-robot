"""Handlers package initialization."""
from .bot_compat import patch_bot_item_access, get_db

from .commands import router as commands_router
from .callbacks import router as callbacks_router
from .chat_member import router as chat_member_router
from .text_answers import router as text_answers_router

__all__ = [
    "commands_router",
    "callbacks_router",
    "chat_member_router",
    "text_answers_router",
    "patch_bot_item_access",
    "get_db",
]
