"""
Custom Animated Emojis Module for GeoGuru & GeoGuessr Telegram Bot.
Sticker Pack: Animated Emoji (https://t.me/addemoji/RestrictedEmoji)
Pack Name: RestrictedEmoji
"""
import json
import re
from pathlib import Path
from typing import Dict, Optional, Tuple

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "restricted_emojis.json"

# Base maps from restricted_emojis.json
EMOJI_TO_ID: Dict[str, str] = {}
ID_TO_EMOJI: Dict[str, str] = {}

if DATA_FILE.exists():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            items = json.load(f)
            for item in items:
                e = item["emoji"]
                cid = item["custom_emoji_id"]
                EMOJI_TO_ID[e] = cid
                ID_TO_EMOJI[cid] = e
                clean = e.replace("\ufe0f", "")
                if clean not in EMOJI_TO_ID:
                    EMOJI_TO_ID[clean] = cid
    except Exception:
        pass

# Fallback & semantic aliases for bot icons to the best animated emojis in the pack
FALLBACK_ALIASES: Dict[str, str] = {
    # Globe / Map / Navigation
    "🌐": EMOJI_TO_ID.get("🌍", "5399898266265475100"),
    "📍": EMOJI_TO_ID.get("🧭", "5433825729060018456"),
    "🗺️": EMOJI_TO_ID.get("🗺", "5415803062738504079"),
    # Timers / Clocks
    "⏱": EMOJI_TO_ID.get("⏰", "5413704112220949842"),
    "⏱️": EMOJI_TO_ID.get("⏰", "5413704112220949842"),
    # Warnings & Alerts
    "⚠️": EMOJI_TO_ID.get("❗", "5467928559664242360"),
    "⚠": EMOJI_TO_ID.get("❗", "5467928559664242360"),
    # Calendar & Schedules
    "📅": EMOJI_TO_ID.get("📆", "5431897022456145283"),
    "🗓": EMOJI_TO_ID.get("📆", "5431897022456145283"),
    # Game & Shields
    "🎲": EMOJI_TO_ID.get("🎮", "5467583879948803288"),
    "🕹": EMOJI_TO_ID.get("🎮", "5467583879948803288"),
    "🛡": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🛡️": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🛑": EMOJI_TO_ID.get("❌", "5465665476971471368"),
    # Settings & tools
    "⚙": EMOJI_TO_ID.get("🔑", "5330115548900501467"),
    "⚙️": EMOJI_TO_ID.get("🔑", "5330115548900501467"),
}

for k, v in FALLBACK_ALIASES.items():
    if k not in EMOJI_TO_ID:
        EMOJI_TO_ID[k] = v

# Named shortcuts for easy programmatic use: ce("trophy"), ce("fire"), etc.
NAMED_ALIASES: Dict[str, Tuple[str, str]] = {
    "trophy": ("🏆", "5409008750893734809"),
    "first_place": ("🥇", "5280735858926822987"),
    "second_place": ("🥈", "5283195573812340110"),
    "third_place": ("🥉", "5282750778409233531"),
    "fire": ("🔥", "5420315771991497307"),
    "streak": ("🔥", "5420315771991497307"),
    "star": ("⭐", "5435957248314579621"),
    "sparkles": ("✨", "5472164874886846699"),
    "earth": ("🌍", "5399898266265475100"),
    "globe": ("🌍", "5399898266265475100"),
    "map": ("🗺️", "5415803062738504079"),
    "compass": ("🧭", "5433825729060018456"),
    "game": ("🎮", "5467583879948803288"),
    "swords": ("⚔️", "5408935401442267103"),
    "duel": ("⚔️", "5408935401442267103"),
    "target": ("🎯", "5350460637182993292"),
    "crown": ("👑", "5467406098367521267"),
    "robot": ("🤖", "5372981976804366741"),
    "brain": ("🧠", "5237799019329105246"),
    "check": ("✅", "5427009714745517609"),
    "cross": ("❌", "5465665476971471368"),
    "question": ("❓", "5467666648263564704"),
    "exclamation": ("❗", "5467928559664242360"),
    "warning": ("⚠️", "5467928559664242360"),
    "bulb": ("💡", "5472146462362048818"),
    "hint": ("💡", "5472146462362048818"),
    "rocket": ("🚀", "5445284980978621387"),
    "alarm": ("⏰", "5413704112220949842"),
    "clock": ("⏰", "5413704112220949842"),
    "timer": ("⏰", "5413704112220949842"),
    "hourglass": ("⏳", "5451732530048802485"),
    "lightning": ("⚡", "5431449001532594346"),
    "stats": ("📊", "5431577498364158238"),
    "chart": ("📊", "5431577498364158238"),
    "growth": ("📈", "5373001317042101552"),
    "heart": ("❤️", "5449505950283078474"),
    "broken_heart": ("💔", "5471954395719539651"),
    "user": ("👤", "5373012449597335010"),
    "users": ("👥", "5372926953978341366"),
    "books": ("📚", "5373098009640836781"),
    "book": ("📖", "5226512880362332956"),
    "art": ("🎨", "5431456208487716895"),
    "castle": ("🏰", "5429403746696189687"),
    "landmarks": ("🗽", "5454219968948229067"),
    "party": ("🎉", "5436040291507247633"),
    "gift": ("🎁", "5199749070830197566"),
    "coins": ("🪙", "5379600444098093058"),
    "money": ("💰", "5375296873982604963"),
    "diamond": ("💎", "5471952986970267163"),
    "search": ("🔍", "5188217332748527444"),
    "car": ("🚗", "5445085952194124000"),
    "movie": ("🎬", "5375464961822695044"),
    "food": ("🍔", "5372998546788194447"),
    "pizza": ("🍕", "5370980663778351052"),
    "muscle": ("💪", "5471883477219549006"),
    "thumbsup": ("👍", "5469770542288478598"),
    "thumbsdown": ("👎", "5472309400536358507"),
    "bell": ("🔔", "5242628160297641831"),
    "flag_finish": ("🏁", "5411520005386806155"),
    "flag_white": ("🏳️", "5411285332668720752"),
    "flag_red": ("🚩", "5411175424455613715"),
    "calendar": ("📆", "5431897022456145283"),
    "folder": ("📂", "5431721976769027887"),
    "chat": ("💬", "5465300082628763143"),
    "science": ("🔬", "5379679518740978720"),
    "key": ("🔑", "5330115548900501467"),
}

# Pre-compile replacement regex matching existing HTML tags OR any mapped emojis
_SORTED_EMOJIS = sorted(EMOJI_TO_ID.keys(), key=lambda x: len(x), reverse=True)
_TAG_PATTERN = r"<tg-emoji\b[^>]*>.*?</tg-emoji>|<[^>]+>"
_EMOJI_PATTERN = "|".join(re.escape(e) for e in _SORTED_EMOJIS)
_COMBINED_REGEX = re.compile(f"({_TAG_PATTERN})|({_EMOJI_PATTERN})", re.DOTALL) if _SORTED_EMOJIS else None
_STRIP_REGEX = re.compile(r"<tg-emoji\b[^>]*>(.*?)</tg-emoji>", re.DOTALL)


def ce(key_or_emoji: str, fallback: Optional[str] = None) -> str:
    """
    Format a custom emoji tag for Telegram HTML parse_mode:
    <tg-emoji emoji-id="...">fallback</tg-emoji>

    Supports named aliases ('trophy', 'fire', 'star', etc.) or raw unicode emojis ('🏆', '🔥').
    """
    if key_or_emoji in NAMED_ALIASES:
        fallback_char, cid = NAMED_ALIASES[key_or_emoji]
        fb = fallback or fallback_char
        return f'<tg-emoji emoji-id="{cid}">{fb}</tg-emoji>'

    cid = EMOJI_TO_ID.get(key_or_emoji) or EMOJI_TO_ID.get(key_or_emoji.replace("\ufe0f", ""))
    if cid:
        fb = fallback or key_or_emoji
        return f'<tg-emoji emoji-id="{cid}">{fb}</tg-emoji>'

    return fallback or key_or_emoji


def apply_custom_emojis(text: str) -> str:
    """
    Replace matching emojis in HTML text with Telegram custom emoji tags:
    <tg-emoji emoji-id="...">emoji</tg-emoji>

    Safely preserves existing HTML tags and avoids double-wrapping.
    """
    if not text or not _COMBINED_REGEX:
        return text

    def _replacer(match: re.Match) -> str:
        # If it matched an HTML tag or already wrapped tg-emoji, leave untouched
        tag = match.group(1)
        if tag:
            return tag
        
        # Matched an emoji
        em = match.group(2)
        if em and em in EMOJI_TO_ID:
            cid = EMOJI_TO_ID[em]
            return f'<tg-emoji emoji-id="{cid}">{em}</tg-emoji>'
        return match.group(0)

    return _COMBINED_REGEX.sub(_replacer, text)


def strip_custom_emojis(text: str) -> str:
    """
    Remove <tg-emoji> tags from text, leaving only the fallback emojis.
    Use for keyboard button texts or plain alerts.
    """
    if not text or "<tg-emoji" not in text:
        return text
    return _STRIP_REGEX.sub(r"\1", text)
