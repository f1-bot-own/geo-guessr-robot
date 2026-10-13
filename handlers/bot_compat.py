"""
Aiogram Bot backward compatibility and database resolution layer.
Enables dictionary-style item access (bot['db']) and attribute access (bot.db)
on aiogram 3 Bot instances without clobbering internal Bot methods or properties.
"""

from typing import Any, Dict, Optional, Iterator
from aiogram import Bot
from database.db import Database, get_default_db

# Reserved names for Bot class members and instance attributes that must not be
# exposed as dictionary items or corrupted by dictionary item assignment.
BOT_RESERVED_NAMES = set(dir(Bot)) | {"session", "default", "_Bot__token", "_me", "token", "id"}


def _get_bot_data(bot: Bot) -> Dict[Any, Any]:
    """Retrieve or initialize the isolated data dictionary on a Bot instance."""
    data = bot.__dict__.get("_bot_data")
    if data is None:
        data = {}
        bot.__dict__["_bot_data"] = data
    return data


def _bot_getitem(self: Bot, key: Any) -> Any:
    """Retrieve an item from the bot's data store or custom instance attributes."""
    data = _get_bot_data(self)
    if key in data:
        return data[key]
    if isinstance(key, str) and key not in BOT_RESERVED_NAMES and hasattr(self, key):
        return getattr(self, key)
    raise KeyError(key)


def _bot_setitem(self: Bot, key: Any, value: Any) -> None:
    """Store an item in the bot's data store, syncing safe attribute names."""
    data = _get_bot_data(self)
    data[key] = value
    # Only mirror to instance attribute if it's a valid identifier and does not
    # conflict with aiogram.Bot class methods, attributes, or properties.
    if isinstance(key, str) and key.isidentifier() and key not in BOT_RESERVED_NAMES:
        setattr(self, key, value)


def _bot_delitem(self: Bot, key: Any) -> None:
    """Delete an item from the bot's data store and any mirrored attribute."""
    data = _get_bot_data(self)
    found = False
    if key in data:
        del data[key]
        found = True
    if isinstance(key, str) and key not in BOT_RESERVED_NAMES and hasattr(self, key):
        try:
            delattr(self, key)
            found = True
        except AttributeError:
            pass
    if not found:
        raise KeyError(key)


def _bot_contains(self: Bot, key: Any) -> bool:
    """Check if key exists in the bot's data store or custom instance attributes."""
    data = _get_bot_data(self)
    if key in data:
        return True
    if isinstance(key, str) and key not in BOT_RESERVED_NAMES and hasattr(self, key):
        return True
    return False


def _bot_get(self: Bot, key: Any, default: Any = None) -> Any:
    """Get value with default fallback."""
    try:
        return self[key]
    except KeyError:
        return default


def _bot_keys(self: Bot) -> set:
    """Return keys currently stored in the bot's data container."""
    keys = set(_get_bot_data(self).keys())
    for attr in self.__dict__:
        if not attr.startswith("_") and attr not in BOT_RESERVED_NAMES:
            keys.add(attr)
    return keys


def _bot_values(self: Bot) -> list:
    """Return values currently stored in the bot's data container."""
    return [self[k] for k in _bot_keys(self)]


def _bot_items(self: Bot) -> list:
    """Return (key, value) pairs currently stored in the bot's data container."""
    return [(k, self[k]) for k in _bot_keys(self)]


def _bot_len(self: Bot) -> int:
    """Return count of items in the bot's data container."""
    return len(_bot_keys(self))


def _bot_iter(self: Bot) -> Iterator[Any]:
    """Iterate over keys in the bot's data container."""
    return iter(_bot_keys(self))


def patch_bot_item_access() -> None:
    """Patch aiogram.Bot to support dictionary-style data access safely."""
    _bot_getitem._is_compat_patch = True
    Bot.__getitem__ = _bot_getitem

    _bot_setitem._is_compat_patch = True
    Bot.__setitem__ = _bot_setitem

    _bot_delitem._is_compat_patch = True
    Bot.__delitem__ = _bot_delitem

    _bot_contains._is_compat_patch = True
    Bot.__contains__ = _bot_contains

    _bot_get._is_compat_patch = True
    Bot.get = _bot_get

    _bot_keys._is_compat_patch = True
    Bot.keys = _bot_keys

    _bot_values._is_compat_patch = True
    Bot.values = _bot_values

    _bot_items._is_compat_patch = True
    Bot.items = _bot_items

    _bot_len._is_compat_patch = True
    Bot.__len__ = _bot_len

    _bot_iter._is_compat_patch = True
    Bot.__iter__ = _bot_iter


def get_db(bot: Bot) -> Database:
    """
    Resolve Database instance associated with a Bot instance.
    Checks bot.db attribute first, then bot['db'] item access,
    and falls back to default database singleton.
    """
    if hasattr(bot, "db") and getattr(bot, "db") is not None:
        return getattr(bot, "db")
    try:
        return bot["db"]
    except (TypeError, KeyError, AttributeError):
        pass
    return get_default_db()


# Automatically apply patch when module is imported
patch_bot_item_access()
