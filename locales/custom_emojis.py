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
    "🕰": EMOJI_TO_ID.get("⏰", "5413704112220949842"),
    # Warnings & Alerts & Info
    "⚠️": EMOJI_TO_ID.get("❗", "5467928559664242360"),
    "⚠": EMOJI_TO_ID.get("❗", "5467928559664242360"),
    "ℹ️": EMOJI_TO_ID.get("💡", "5472146462362048818"),
    "ℹ": EMOJI_TO_ID.get("💡", "5472146462362048818"),
    # Calendar & Schedules
    "📅": EMOJI_TO_ID.get("📆", "5431897022456145283"),
    "🗓": EMOJI_TO_ID.get("📆", "5431897022456145283"),
    # Game & Shields
    "🎲": EMOJI_TO_ID.get("🎮", "5467583879948803288"),
    "🕹": EMOJI_TO_ID.get("🎮", "5467583879948803288"),
    "🛡": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🛡️": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🛑": EMOJI_TO_ID.get("❌", "5465665476971471368"),
    # Settings, Tools & UI Controls
    "⚙": EMOJI_TO_ID.get("🔑", "5330115548900501467"),
    "⚙️": EMOJI_TO_ID.get("🔑", "5330115548900501467"),
    "📢": EMOJI_TO_ID.get("🔔", "5242628160297641831"),
    "📣": EMOJI_TO_ID.get("🔔", "5242628160297641831"),
    "📯": EMOJI_TO_ID.get("🔔", "5242628160297641831"),
    "💾": EMOJI_TO_ID.get("📂", "5431721976769027887"),
    "📁": EMOJI_TO_ID.get("📂", "5431721976769027887"),
    "🗂": EMOJI_TO_ID.get("📂", "5431721976769027887"),
    "🗄": EMOJI_TO_ID.get("📂", "5431721976769027887"),
    "⛔": EMOJI_TO_ID.get("❌", "5465665476971471368"),
    "🚫": EMOJI_TO_ID.get("❌", "5465665476971471368"),
    "🔴": EMOJI_TO_ID.get("❌", "5465665476971471368"),
    "🗑": EMOJI_TO_ID.get("❌", "5465665476971471368"),
    "🟢": EMOJI_TO_ID.get("✅", "5427009714745517609"),
    "🔘": EMOJI_TO_ID.get("⌨️", "5472111548572900003"),  # Buttons only -> Keyboard
    "🔵": EMOJI_TO_ID.get("💎", "5471952986970267163"),
    "🔷": EMOJI_TO_ID.get("💎", "5471952986970267163"),
    "🔹": EMOJI_TO_ID.get("💎", "5471952986970267163"),
    "🟡": EMOJI_TO_ID.get("🏆", "5409008750893734809"),
    "🔶": EMOJI_TO_ID.get("🏆", "5409008750893734809"),
    "🔸": EMOJI_TO_ID.get("🏆", "5409008750893734809"),
    "⚪": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "⬜": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "⬛": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🔟": EMOJI_TO_ID.get("🏆", "5409008750893734809"),
    # Game buttons
    "🎲": "5467583879948803288",  # Game Controller 🎮 for all Mix / Super Mix buttons
    "🫀": "5470166383654347072",  # Heart ❤️ for Anatomy
    "🛡️": "5408935401442267103",  # Crossed Swords ⚔️ for Coats of Arms
    "🛡": "5408935401442267103",
    "📁": "5433653135799228968",  # Folder 📁 for Categories
    "📁️": "5433653135799228968",
    # Visual modes & quiz categories
    "📸": EMOJI_TO_ID.get("🗽", "5454219968948229067"),  # Landmark / Photo
    "📷": EMOJI_TO_ID.get("🗽", "5454219968948229067"),
    "⛩": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Asia / Architecture
    "⛩️": EMOJI_TO_ID.get("🏰", "5429403746696189687"),
    "🌌": EMOJI_TO_ID.get("🔭", "5372846474881146350"),  # Astronomy & Space -> Telescope
    "🪐": EMOJI_TO_ID.get("🔭", "5372846474881146350"),  # Planets -> Telescope
    "🏷": EMOJI_TO_ID.get("🎫", "5418010521309815154"),  # Logo / Brand
    "🏷️": EMOJI_TO_ID.get("🎫", "5418010521309815154"),
    "📜": EMOJI_TO_ID.get("🏛", "5359778044745622115"),  # History & Art -> Classical Monument / Temple
    "🏛": "5359778044745622115",
    "📦": EMOJI_TO_ID.get("🎁", "5199749070830197566"),  # Black Box / Gift
    "🎒": EMOJI_TO_ID.get("🎁", "5199749070830197566"),  # Backpack
    "👝": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🧩": EMOJI_TO_ID.get("🧠", "5237799019329105246"),  # Riddle / Puzzle
    "🅰": EMOJI_TO_ID.get("🥇", "5280735858926822987"),  # Option A
    "🅰️": EMOJI_TO_ID.get("🥇", "5280735858926822987"),
    "🅱": EMOJI_TO_ID.get("🥈", "5283195573812340110"),  # Option B
    "🅱️": EMOJI_TO_ID.get("🥈", "5283195573812340110"),
    "🔀": EMOJI_TO_ID.get("🔄", "5264727218734524899"),  # Shuffle / Both -> Reload / Cycle
    "🔙": EMOJI_TO_ID.get("👈", "5469735272017043817"),  # Back button -> Left Pointer
    "◀️": EMOJI_TO_ID.get("👈", "5469735272017043817"),
    "◀": EMOJI_TO_ID.get("👈", "5469735272017043817"),
    "⬅️": EMOJI_TO_ID.get("👈", "5469735272017043817"),
    "⬅": EMOJI_TO_ID.get("👈", "5469735272017043817"),
    "👇": EMOJI_TO_ID.get("👇", "5470177992950946662"),
    "🔢": EMOJI_TO_ID.get("📊", "5431577498364158238"),  # Numbers / Rounds
    # Nature, Geography & Landscapes
    "🌊": EMOJI_TO_ID.get("🌍", "5399898266265475100"),  # Ocean / Wave
    "🕳": EMOJI_TO_ID.get("🌍", "5399898266265475100"),
    "🪨": EMOJI_TO_ID.get("🌍", "5399898266265475100"),
    "🏔": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Mountain
    "⛰": EMOJI_TO_ID.get("🏰", "5429403746696189687"),
    "🗻": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Mt Fuji
    "🌋": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Volcano
    "🏛": EMOJI_TO_ID.get("🏰", "5429403746696189687"),
    "🕌": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Mosque
    "⛪": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Church
    "🏚": EMOJI_TO_ID.get("🏰", "5429403746696189687"),
    "🏙": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Cityscape
    "🗼": EMOJI_TO_ID.get("🏰", "5429403746696189687"),  # Tokyo Tower
    "🎪": EMOJI_TO_ID.get("🏰", "5429403746696189687"),
    "⛺": EMOJI_TO_ID.get("🏰", "5429403746696189687"),
    "🏜": EMOJI_TO_ID.get("☀️", "5469947168523558652"),  # Desert
    "☉": EMOJI_TO_ID.get("☀️", "5469947168523558652"),  # Sun symbol
    "🌾": EMOJI_TO_ID.get("🌿", "5449850741667668411"),  # Rice / Crop
    "🍃": EMOJI_TO_ID.get("🌿", "5449850741667668411"),  # Leaf
    "🎋": EMOJI_TO_ID.get("🌿", "5449850741667668411"),  # Bamboo
    "🌙": EMOJI_TO_ID.get("🌟", "5458799228719472718"),  # Moon
    "🪐": EMOJI_TO_ID.get("🌟", "5458799228719472718"),  # Planet
    "🌪": EMOJI_TO_ID.get("☁️", "5287571024500498635"),  # Tornado
    "🌫": EMOJI_TO_ID.get("☁️", "5287571024500498635"),  # Fog
    "🌬": EMOJI_TO_ID.get("☁️", "5287571024500498635"),  # Wind
    "💨": EMOJI_TO_ID.get("☁️", "5287571024500498635"),
    "💧": EMOJI_TO_ID.get("🌧", "5283243028905994049"),  # Droplet
    "🧊": EMOJI_TO_ID.get("❄️", "5431895003821513760"),  # Ice
    # Animals & Nature
    "🦅": EMOJI_TO_ID.get("🐦", "5332594174527022579"),  # Eagle
    "🐗": EMOJI_TO_ID.get("🐷", "5357233044694508227"),  # Boar
    "🐒": EMOJI_TO_ID.get("🐵", "5465449362807070392"),  # Monkey
    "🦨": EMOJI_TO_ID.get("🐱", "5282816560128336499"),  # Skunk
    "🐡": EMOJI_TO_ID.get("🐟", "5382210409824525356"),  # Fish
    "🦪": EMOJI_TO_ID.get("🐟", "5382210409824525356"),  # Oyster
    "🐚": EMOJI_TO_ID.get("🐟", "5382210409824525356"),  # Shell
    "🪸": EMOJI_TO_ID.get("🐟", "5382210409824525356"),  # Coral
    # Food & Agriculture
    "🍎": EMOJI_TO_ID.get("🍓", "5469963154391833732"),  # Apple
    "🍊": EMOJI_TO_ID.get("🍓", "5469963154391833732"),  # Orange
    "🥭": EMOJI_TO_ID.get("🍓", "5469963154391833732"),  # Mango
    "🍇": EMOJI_TO_ID.get("🍓", "5469963154391833732"),  # Grape
    "🥝": EMOJI_TO_ID.get("🍓", "5469963154391833732"),  # Kiwi
    "🫒": EMOJI_TO_ID.get("🍓", "5469963154391833732"),  # Olive
    "🥩": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Meat
    "🥟": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Dumpling
    "🍝": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Pasta
    "🍜": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Ramen
    "🍲": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Pot
    "🍛": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Curry
    "🥘": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Pan
    "🫓": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Flatbread
    "🥐": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Croissant
    "🧇": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Waffle
    "🧀": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Cheese
    "🥥": EMOJI_TO_ID.get("🍖", "5470159421512359552"),  # Coconut
    "🍵": EMOJI_TO_ID.get("🍕", "5370980663778351052"),  # Tea
    "🍬": EMOJI_TO_ID.get("🍫", "5348308557919970713"),  # Candy
    "🌶": EMOJI_TO_ID.get("🌿", "5449850741667668411"),  # Pepper
    "🌽": EMOJI_TO_ID.get("🌿", "5449850741667668411"),  # Corn
    "🥚": EMOJI_TO_ID.get("🍕", "5370980663778351052"),  # Egg
    # Vehicles & Transportation
    "🚢": EMOJI_TO_ID.get("✈️", "5361600266225326825"),  # Ship
    "🚣": EMOJI_TO_ID.get("✈️", "5361600266225326825"),  # Boat
    "⚓": EMOJI_TO_ID.get("✈️", "5361600266225326825"),  # Anchor
    "🚌": EMOJI_TO_ID.get("🚗", "5445085952194124000"),  # Bus
    "🚒": EMOJI_TO_ID.get("🚗", "5445085952194124000"),  # Fire engine
    "🚜": EMOJI_TO_ID.get("🚗", "5445085952194124000"),  # Tractor
    "🚘": EMOJI_TO_ID.get("🚗", "5445085952194124000"),  # Automobile
    "🛵": EMOJI_TO_ID.get("🚗", "5445085952194124000"),  # Scooter
    "🚲": EMOJI_TO_ID.get("🚗", "5445085952194124000"),  # Bicycle
    "🪂": EMOJI_TO_ID.get("🚀", "5445284980978621387"),  # Parachute
    "⛷": EMOJI_TO_ID.get("🚀", "5445284980978621387"),  # Ski
    "🏇": EMOJI_TO_ID.get("🚀", "5445284980978621387"),  # Horse racing
    # People, Professions & Roles
    "♂": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "♀": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👧": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👦": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👨": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👩": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👴": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🧑": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🧒": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👮": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🕵": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🤵": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👰": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🧖": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🧘": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🚶": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "🧕": EMOJI_TO_ID.get("👤", "5373012449597335010"),
    "👭": EMOJI_TO_ID.get("👥", "5372926953978341366"),
    "👸": EMOJI_TO_ID.get("👑", "5467406098367521267"),
    "🤴": EMOJI_TO_ID.get("👑", "5467406098367521267"),
    "🧙": EMOJI_TO_ID.get("🧠", "5237799019329105246"),
    "🧝": EMOJI_TO_ID.get("🧠", "5237799019329105246"),
    "🧜": EMOJI_TO_ID.get("🧠", "5237799019329105246"),
    "🦹": EMOJI_TO_ID.get("🧠", "5237799019329105246"),
    "🏃": EMOJI_TO_ID.get("⚡", "5431449001532594346"),
    # Science, Health, Objects
    "🫀": EMOJI_TO_ID.get("❤️", "5449505950283078474"),
    "🩸": EMOJI_TO_ID.get("❤️", "5449505950283078474"),
    "🧬": EMOJI_TO_ID.get("🔬", "5379679518740978720"),
    "⚛": EMOJI_TO_ID.get("🔬", "5379679518740978720"),
    "⚕": EMOJI_TO_ID.get("🔬", "5379679518740978720"),
    "⚖": EMOJI_TO_ID.get("📖", "5226512880362332956"),
    "🪦": EMOJI_TO_ID.get("📖", "5226512880362332956"),
    "✉": EMOJI_TO_ID.get("📖", "5226512880362332956"),
    "📋": EMOJI_TO_ID.get("📖", "5226512880362332956"),
    "📐": EMOJI_TO_ID.get("📖", "5226512880362332956"),
    "🔪": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🔨": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "⛏": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🪡": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🪤": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "🚪": EMOJI_TO_ID.get("🔑", "5330115548900501467"),
    "🔒": EMOJI_TO_ID.get("🔑", "5330115548900501467"),
    "👓": EMOJI_TO_ID.get("🔍", "5188217332748527444"),
    "🕶": EMOJI_TO_ID.get("🔍", "5188217332748527444"),
    "📻": EMOJI_TO_ID.get("💬", "5465300082628763143"),
    "🔋": EMOJI_TO_ID.get("⚡", "5431449001532594346"),
    "🖌": EMOJI_TO_ID.get("🎨", "5431456208487716895"),
    "🥋": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🩰": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🧢": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "👒": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🧣": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🧥": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "👘": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🦺": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🥼": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🦰": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🦱": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🧶": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "📿": EMOJI_TO_ID.get("🎁", "5199749070830197566"),
    "🏈": EMOJI_TO_ID.get("🎮", "5467583879948803288"),
    "🏉": EMOJI_TO_ID.get("🎮", "5467583879948803288"),
    "🆚": EMOJI_TO_ID.get("⚔", "5408935401442267103"),
    "➡": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "⬅": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "🦯": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "🪞": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "🪶": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "🧴": EMOJI_TO_ID.get("✨", "5472164874886846699"),
    "🎎": EMOJI_TO_ID.get("✨", "5472164874886846699"),
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

DEFAULT_CUSTOM_EMOJI_ID = "5458799228719472718"  # Animated glowing star


def resolve_fallback_emoji_id(char: str) -> str:
    """Resolve any emoji character to the closest animated custom emoji ID in RestrictedEmoji pack."""
    clean = char.replace("\ufe0f", "")
    if clean in FALLBACK_ALIASES:
        return FALLBACK_ALIASES[clean]
    if char in FALLBACK_ALIASES:
        return FALLBACK_ALIASES[char]
    if clean in EMOJI_TO_ID:
        return EMOJI_TO_ID[clean]
    if char in EMOJI_TO_ID:
        return EMOJI_TO_ID[char]
    return DEFAULT_CUSTOM_EMOJI_ID


# Pre-compile replacement regex matching existing HTML tags OR any mapped emojis OR any remaining unicode emoji
_SORTED_EMOJIS = sorted(EMOJI_TO_ID.keys(), key=lambda x: len(x), reverse=True)
_TAG_PATTERN = r"<tg-emoji\b[^>]*>.*?</tg-emoji>|<code\b[^>]*>.*?</code>|<pre\b[^>]*>.*?</pre>|<[^>]+>"
_EMOJI_PATTERN = "|".join(re.escape(e) for e in _SORTED_EMOJIS)
_ANY_EMOJI_PATTERN = (
    r"[\U0001F1E6-\U0001F1FF]{2}|"
    r"[\U0001F300-\U0001FAFF]|"
    r"[\u2600-\u27bf]|"
    r"[\u2300-\u23ff]|"
    r"[\u2b50\u2b55\u203c\u2049\u2139\u2194-\u21aa\u2934\u2935\u2b05-\u2b07\u2b1b\u2b1c\u3030\u303d\u3297\u3299]"
)
_COMBINED_REGEX = re.compile(
    f"({_TAG_PATTERN})|({_EMOJI_PATTERN})|({_ANY_EMOJI_PATTERN})",
    re.DOTALL
) if _SORTED_EMOJIS else None
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
    if not cid:
        cid = resolve_fallback_emoji_id(key_or_emoji)

    fb = fallback or ID_TO_EMOJI.get(cid, key_or_emoji)
    return f'<tg-emoji emoji-id="{cid}">{fb}</tg-emoji>'


def apply_custom_emojis(text: str) -> str:
    """
    Replace matching emojis in HTML text with Telegram custom emoji tags:
    <tg-emoji emoji-id="...">emoji</tg-emoji>

    Safely preserves existing HTML tags and avoids double-wrapping.
    Guarantees all emojis are transformed into custom animated emojis matched to their direction.
    """
    if not text or not _COMBINED_REGEX:
        return text

    def _replacer(match: re.Match) -> str:
        # Group 1: If it matched an HTML tag or already wrapped tg-emoji, leave untouched
        tag = match.group(1)
        if tag:
            return tag

        # Group 2: Matched a known mapped emoji
        em = match.group(2)
        if em:
            cid = EMOJI_TO_ID.get(em) or EMOJI_TO_ID.get(em.replace("\ufe0f", ""))
            if cid:
                disp = ID_TO_EMOJI.get(cid, em)
                return f'<tg-emoji emoji-id="{cid}">{disp}</tg-emoji>'

        # Group 3: Any other unicode emoji
        other_em = match.group(3)
        if other_em:
            cid = resolve_fallback_emoji_id(other_em)
            disp = ID_TO_EMOJI.get(cid, other_em)
            return f'<tg-emoji emoji-id="{cid}">{disp}</tg-emoji>'

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
