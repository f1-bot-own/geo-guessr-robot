"""
Internationalization (i18n) module for GeoGuru & GeoGuessr Bot.
Provides string translation with fallback to English and safe template formatting.
"""
import json
import logging
import string
from pathlib import Path
from typing import Any, Dict, Optional
from .custom_emojis import apply_custom_emojis, strip_custom_emojis, ce

logger = logging.getLogger(__name__)

LOCALES_DIR = Path(__file__).resolve().parent

LOCALES: Dict[str, Dict[str, Any]] = {}


class SafeFormatter(string.Formatter):
    """
    Formatter that preserves placeholders when missing from kwargs,
    preventing KeyError or ValueError and allowing partial interpolation.
    """
    def get_value(self, key, args, kwargs):
        if isinstance(key, str):
            if key in kwargs:
                return kwargs[key]
            return "{" + key + "}"
        elif isinstance(key, int):
            if key < len(args):
                return args[key]
            return "{" + str(key) + "}"
        return "{" + str(key) + "}"


_safe_formatter = SafeFormatter()


def load_locales():
    """Load all JSON locale files from the locales directory."""
    global LOCALES
    for lang in ["en", "ru", "uz"]:
        file_path = LOCALES_DIR / f"{lang}.json"
        if file_path.exists():
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    LOCALES[lang] = json.load(f)
            except Exception as e:
                logger.error(f"Failed to load locale {lang}: {e}")
                LOCALES[lang] = {}
        else:
            LOCALES[lang] = {}


# Initial load
load_locales()


_PLAIN_TEXT_PREFIXES = ("btn_", "lang_btn_", "solo_btn_", "status_")
_PLAIN_TEXT_SUFFIXES = ("_alert",)
_PLAIN_TEXT_KEYS = {"duel_accept", "duel_decline", "solo_round_info"}


def t(key: str, lang: str = "en", as_html: bool = False, **kwargs) -> str:
    """
    Get a localized string by key and format it with provided kwargs.
    Defaults to 'en' (English).
    Safely handles missing keys, missing format arguments, and None/empty keys without raising KeyError.
    """
    if key is None:
        return ""
    if not isinstance(key, str):
        key = str(key)

    if not lang or lang not in LOCALES:
        lang = "en"
    
    # Check in target language
    lang_dict = LOCALES.get(lang, {})
    val = lang_dict.get(key)
    
    # Fallback to English if missing
    if val is None:
        en_dict = LOCALES.get("en", {})
        val = en_dict.get(key, key)
    
    if isinstance(val, str):
        if not kwargs:
            res = val
        else:
            try:
                res = _safe_formatter.format(val, **kwargs)
            except Exception:
                res = val
    else:
        res = str(val) if val is not None else ""

    if not res:
        return res

    # If key was not found and returned fallback key itself, don't wrap
    if val == key and key not in lang_dict and key not in LOCALES.get("en", {}):
        return res

    if as_html:
        # Never wrap button labels or alerts with <tg-emoji>
        if (
            key.startswith(_PLAIN_TEXT_PREFIXES)
            or key.endswith(_PLAIN_TEXT_SUFFIXES)
            or key in _PLAIN_TEXT_KEYS
        ):
            return strip_custom_emojis(res)
        return apply_custom_emojis(res)

    return strip_custom_emojis(res)


def t_html(key: str, lang: str = "en", **kwargs) -> str:
    """Convenience helper to get localized string with animated custom emojis applied."""
    return t(key, lang, as_html=True, **kwargs)


def get_rank_name(level: int, lang: str = "en") -> str:
    """Return rank name based on user level."""
    if not lang or lang not in LOCALES:
        lang = "en"
    
    ranks = LOCALES.get(lang, {}).get("ranks") or LOCALES.get("en", {}).get("ranks", {})
    
    # Map level to rank tier (1 to 7)
    tier = min(max(1, (level // 3) + 1), 7)
    return ranks.get(str(tier), "🌐 GeoGuru")


def format_countdown(seconds: int, lang: str = "en") -> str:
    """
    Format remaining time countdown string with safe warning thresholds.
    Threshold: <= 5 seconds uses warning indicator '⚠️ X left!'.
    Normal: > 5 seconds uses hourglass indicator '⏳ Time remaining: Xs'.
    Supports 'en', 'uz', 'ru'.
    """
    sec = max(0, int(seconds))
    if sec <= 5:
        if lang == "uz":
            return f"⚠️ {sec}s qoldi!"
        elif lang == "ru":
            return f"⚠️ {sec}с осталось!"
        else:
            return f"⚠️ {sec}s left!"
    else:
        if lang == "uz":
            return f"⏳ Qolgan vaqt: {sec}s"
        elif lang == "ru":
            return f"⏳ Осталось времени: {sec}с"
        else:
            return f"⏳ Time remaining: {sec}s"
