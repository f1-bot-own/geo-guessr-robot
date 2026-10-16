"""
Database Schema definitions and DDL for GeoGuru & GeoGuessr Telegram Bot.
Defines SQLite tables, indexes, and PRAGMA settings.
"""

PRAGMA_STATEMENTS = [
    "PRAGMA journal_mode = WAL;",
    "PRAGMA synchronous = NORMAL;",
    "PRAGMA temp_store = MEMORY;",
    "PRAGMA cache_size = -64000;",
    "PRAGMA busy_timeout = 30000;",
]

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    language TEXT DEFAULT 'en',
    xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    total_score INTEGER DEFAULT 0,
    games_played INTEGER DEFAULT 0,
    games_won INTEGER DEFAULT 0,
    correct_answers INTEGER DEFAULT 0,
    total_answers INTEGER DEFAULT 0,
    best_streak INTEGER DEFAULT 0,
    current_streak INTEGER DEFAULT 0,
    last_daily_date TEXT,
    daily_streak INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_CHATS_TABLE = """
CREATE TABLE IF NOT EXISTS chats (
    chat_id INTEGER PRIMARY KEY,
    chat_type TEXT,
    title TEXT,
    language TEXT DEFAULT 'en',
    total_games INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_GROUP_SCORES_TABLE = """
CREATE TABLE IF NOT EXISTS group_scores (
    chat_id INTEGER,
    user_id INTEGER,
    first_name TEXT,
    score INTEGER DEFAULT 0,
    wins INTEGER DEFAULT 0,
    games_played INTEGER DEFAULT 0,
    PRIMARY KEY (chat_id, user_id)
);
"""

CREATE_DUELS_TABLE = """
CREATE TABLE IF NOT EXISTS duels (
    duel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER,
    challenger_id INTEGER,
    challenger_name TEXT,
    opponent_id INTEGER,
    opponent_name TEXT,
    winner_id INTEGER NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_MATCHES_TABLE = """
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER,
    mode TEXT,
    winner_id INTEGER,
    winner_name TEXT,
    winner_score INTEGER,
    players_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_DAILY_CHALLENGES_TABLE = """
CREATE TABLE IF NOT EXISTS daily_challenges (
    user_id INTEGER,
    challenge_date TEXT,
    score INTEGER DEFAULT 0,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, challenge_date)
);
"""

CREATE_SCORE_EVENTS_TABLE = """
CREATE TABLE IF NOT EXISTS score_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    chat_id INTEGER,
    points INTEGER NOT NULL DEFAULT 0,
    xp INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

INDEX_STATEMENTS = [
    "CREATE INDEX IF NOT EXISTS idx_users_total_score ON users(total_score DESC);",
    "CREATE INDEX IF NOT EXISTS idx_users_xp ON users(xp DESC);",
    "CREATE INDEX IF NOT EXISTS idx_group_score ON group_scores(chat_id, score DESC);",
    "CREATE INDEX IF NOT EXISTS idx_score_events_created ON score_events(created_at);",
    "CREATE INDEX IF NOT EXISTS idx_score_events_user_time ON score_events(user_id, created_at);",
    "CREATE INDEX IF NOT EXISTS idx_score_events_chat_time ON score_events(chat_id, created_at);",
]

ALL_TABLES = [
    CREATE_USERS_TABLE,
    CREATE_CHATS_TABLE,
    CREATE_GROUP_SCORES_TABLE,
    CREATE_DUELS_TABLE,
    CREATE_MATCHES_TABLE,
    CREATE_DAILY_CHALLENGES_TABLE,
    CREATE_SCORE_EVENTS_TABLE,
]
