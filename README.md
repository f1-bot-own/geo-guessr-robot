# 🌍 GeoGuru & GeoGuessr Telegram Bot

> **An interactive, competitive Geography Trivia & GeoGuessr Telegram Bot designed primarily for group entertainment and solo practice.**
> Inspired by **GeoGuru** and **GeoGuessr**, featuring world flags, capitals, iconic landmarks, coats of arms, population/area comparisons, and real-time multiplayer duels.

---

## 🚀 Key Features

### 🎮 Game Modes
1. **🏳️ Flag Quiz (`flag`):** Guess sovereign countries by high-resolution flag images.
2. **🏛 Capitals (`capital`):** Test knowledge of world capitals and vice versa.
3. **📸 GeoGuessr Landmarks (`landmark`):** Guess countries from famous UNESCO sites, architecture, and street views (e.g., Registan, Eiffel Tower, Colosseum, Machu Picchu, Angkor Wat).
4. **📊 Higher or Lower (`higher_lower`):** Compare countries by real-world population and land area.
5. **🛡 Coat of Arms (`coat_of_arms`):** Identify sovereign national emblems.
6. **🗺️ Street View / GeoGuessr (`streetview`):** Guess countries from real-world Google Maps / street panoramas with driving side clues and post-round Google Maps links!
7. **🎲 Mix Mode (`mix`):** Non-stop rotation across all challenge modes!

### 👥 Group Party Games
- **Interactive Setup:** Configure game mode, rounds (3 to 20), and round timers (15s to 45s).
- **Fast-paced Scoring:** +100 base points with dynamic speed bonuses (faster answers earn up to 2x points).
- **Streak Multipliers:** Consecutive correct answers award streak bonuses.
- **Anti-Spam & Anti-Cheat:** Players who answer incorrectly receive a -20 pt penalty and are locked out of that round.
- **Direct Chat Text Recognition:** Members can answer either by tapping inline buttons or by typing country names directly in group chat!
- **Between-round Fun Facts:** Educational insights about each country revealed after every round.
- **Podium & Leaderboards:** 🥇 1st, 🥈 2nd, and 🥉 3rd place finishes, group ranking (`/top`), and global ranking (`/leaderboard`).
- **⚔️ 1v1 Duels (`/duel @user`):** Challenge any group member to a head-to-head 3-round duel!

### 🕹 Solo Practice Mode (`/solo`)
- Play solo with 3 lives (`❤️❤️❤️`).
- Lifelines:
  - 💡 **Hint:** Reveals continent and capital.
  - ✂️ **50/50:** Eliminates two incorrect options.
- Dynamic streaks and endless survival mode.

### 📅 Daily Challenge (`/daily`)
- 5 deterministic questions generated per day (seeded by date).
- Global leaderboard parity: every player worldwide tackles the exact same 5 questions each day.
- Tracks daily streak flames (🔥) with bonus XP (+150 XP).

### 🌐 Trilingual Support
- **English (`en`)** — **DEFAULT language upon `/start`** (strictly complies with user specification).
- **Russian (`ru`)** — Полная локализация на русский язык.
- **Uzbek (`uz`)** — O'zbek tiliga to'liq professional tarjima.
- Instant language switching via `/language` or menu buttons.

---

## 📂 Project Structure

```
geoguru-geoguessr-bot/
├── config.py                 # Bot configuration and constants
├── main.py                   # Main entry point and polling loop
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── database/
│   ├── __init__.py
│   └── db.py                 # Async SQLite database (aiosqlite)
├── gamedata/
│   ├── __init__.py
│   ├── countries.py          # 126+ sovereign countries database
│   ├── landmarks.py          # GeoGuessr iconic landmarks & street views
│   ├── streetviews.py        # Dedicated Street Views & Google Maps database (50+ locations)
│   └── fun_facts.py          # Multilingual geography fun facts
├── data/                     # Persistent storage directory (SQLite & photo cache volume mount)
├── games/
│   ├── __init__.py
│   ├── models.py             # Game data models & enums
│   ├── question_factory.py   # Randomized question generators
│   ├── session.py            # Group & duel game session controller
│   ├── solo_session.py       # Solo practice mode controller
│   ├── daily_session.py      # Daily challenge controller
│   ├── manager.py            # Active session registry
│   └── flow.py               # Round orchestration & timeout handlers
├── handlers/
│   ├── __init__.py
│   ├── commands.py           # /start, /game, /stop, /solo, /daily, /profile, etc.
│   ├── callbacks.py          # Inline button callback queries
│   ├── chat_member.py        # Group join greeting event
│   └── text_answers.py       # In-chat text answer recognition
├── keyboards/
│   ├── __init__.py
│   ├── menu_kb.py            # Main menu & language keyboards
│   └── game_kb.py            # Answer options, setup, & duel keyboards
├── locales/
│   ├── __init__.py
│   ├── i18n.py               # Localization helper with fallback
│   ├── en.json               # English translations
│   ├── ru.json               # Russian translations
│   └── uz.json               # Uzbek translations
└── tests/
    ├── __init__.py
    ├── test_geobot.py        # Core end-to-end integration tests
    ├── test_audit_fixes.py   # Verification test suite for group stats, duels, & text matching
    ├── test_data.py          # Countries & landmarks integrity
    ├── test_db.py            # Database CRUD & streak transitions
    ├── test_engine.py        # Game session lifecycles
    ├── test_i18n.py          # Translation fallback & locales
    └── test_modes.py         # Question generation across all modes
```

---

## 🛠 Installation & Setup

### 1. Prerequisites
- Python 3.10+
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)

### 2. Clone and Install Dependencies
```bash
cd geoguru-geoguessr-bot
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Edit `.env` and supply your bot token:
```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
DB_PATH=geobot.db
```

### 4. Run the Bot
```bash
python main.py
```

---

## 🧪 Running Tests

The test suite runs using standard Python `unittest`:
```bash
python -m unittest tests/test_geobot.py -v
```

All 17 tests will run, covering:
- Locales consistency and i18n fallback across en, ru, and uz.
- Verification that `/start` strictly defaults to English (`en`).
- Dataset integrity for 95+ countries and GeoGuessr landmarks.
- Question generation across all modes (Flags, Capitals, Landmarks, Higher/Lower, Coat of Arms, Mix).
- Async SQLite database operations (user profiles, group scores, XP, level calculations, daily challenge streaks).
- Group game session mechanics, answer lockout, timer cancellation, and podium calculations.
- Solo practice lifelines (50/50, Hint) and lives system.
- Edge cases: malformed inputs, unicode characters, score boundaries, and unauthorized duel attempts.

---

## 🎮 Telegram Commands List

| Command | Description |
| :--- | :--- |
| `/start` | Start bot, view private menu, or register group (defaults to English) |
| `/game` | Launch a new group game match with interactive setup |
| `/stop` | Stop the currently running game in the group |
| `/solo` | Launch solo practice mode with 3 lives & lifelines |
| `/daily` | Complete today's Daily Geography Challenge for bonus XP |
| `/profile` | View player level, rank, XP, win rate, and streaks |
| `/leaderboard` | View global top 10 geography champions |
| `/top` | View top 10 players in the current Telegram group |
| `/duel [@user]` | Challenge a group member to a 1v1 geography duel |
| `/language` | Switch bot language (English / Русский / O'zbek) |
| `/help` | Detailed bot guide, rules, and scoring system |
