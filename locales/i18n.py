"""
Internationalization (i18n) module for GeoGuru & GeoGuessr Bot.
Provides string translation with fallback to English.
"""
import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

LOCALES_DIR = Path(__file__).resolve().parent

LOCALES: Dict[str, Dict[str, Any]] = {}

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

def t(key: str, lang: str = "en", **kwargs) -> str:
    """
    Get a localized string by key and format it with provided kwargs.
    Defaults to 'en' (English).
    """
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
        try:
            return val.format(**kwargs)
        except Exception:
            return val
    return str(val)

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

