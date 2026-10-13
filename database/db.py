"""
Async SQLite Database Module for GeoGuru & GeoGuessr Telegram Bot.
Handles user profiles, XP, levels, chat settings, group leaderboards, daily streaks, duels, and match history.
Supports both object-oriented (Database class) and modular function-based interfaces.
"""

import aiosqlite
import logging
from typing import Optional, Dict, List, Any
from pathlib import Path
from datetime import date

import config

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    @staticmethod
    def calculate_level(xp: int) -> int:
        """Calculate player level: Level = 1 + int((XP / 200) ** 0.5)"""
        if xp < 0:
            return 1
        return 1 + int((xp / 200) ** 0.5)

    async def init_db(self):
        """Create necessary tables and indexes if they do not exist."""
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
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
            """)

            await db.execute("""
                CREATE TABLE IF NOT EXISTS chats (
                    chat_id INTEGER PRIMARY KEY,
                    chat_type TEXT,
                    title TEXT,
                    language TEXT DEFAULT 'en',
                    total_games INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            await db.execute("""
                CREATE TABLE IF NOT EXISTS group_scores (
                    chat_id INTEGER,
                    user_id INTEGER,
                    first_name TEXT,
                    score INTEGER DEFAULT 0,
                    wins INTEGER DEFAULT 0,
                    games_played INTEGER DEFAULT 0,
                    PRIMARY KEY (chat_id, user_id)
                );
            """)

            await db.execute("""
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
            """)

            await db.execute("""
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
            """)

            await db.execute("""
                CREATE TABLE IF NOT EXISTS daily_challenges (
                    user_id INTEGER,
                    challenge_date TEXT,
                    score INTEGER DEFAULT 0,
                    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (user_id, challenge_date)
                );
            """)

            # Indexes for leaderboards
            await db.execute("CREATE INDEX IF NOT EXISTS idx_users_total_score ON users(total_score DESC);")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_users_xp ON users(xp DESC);")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_group_score ON group_scores(chat_id, score DESC);")

            await db.commit()
            logger.info("Database schema initialized successfully.")

    async def get_or_create_user(
        self,
        user_id: int,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        default_lang: str = "en"
    ) -> Dict[str, Any]:
        """Fetch user or insert new user with default language 'en'."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = await cursor.fetchone()
            if row:
                user_dict = dict(row)
                if username and username != user_dict.get("username") or first_name and first_name != user_dict.get("first_name"):
                    await db.execute(
                        "UPDATE users SET username = ?, first_name = ? WHERE user_id = ?",
                        (username or user_dict.get("username"), first_name or user_dict.get("first_name"), user_id)
                    )
                    await db.commit()
                    user_dict["username"] = username or user_dict.get("username")
                    user_dict["first_name"] = first_name or user_dict.get("first_name")
                return user_dict

            await db.execute(
                """
                INSERT INTO users (user_id, username, first_name, language)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, username or "", first_name or "Player", default_lang)
            )
            await db.commit()

            cursor = await db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            new_row = await cursor.fetchone()
            return dict(new_row)

    async def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user by ID."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def set_user_language(self, user_id: int, language: str):
        """Update preferred user language."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("UPDATE users SET language = ? WHERE user_id = ?", (language, user_id))
            await db.commit()

    async def get_user_language(self, user_id: int) -> str:
        """Get user preferred language or fallback to 'en'."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("SELECT language FROM users WHERE user_id = ?", (user_id,))
            row = await cursor.fetchone()
            return row[0] if row and row[0] else config.DEFAULT_LANGUAGE

    async def get_or_create_chat(
        self,
        chat_id: int,
        chat_type: str = "group",
        title: Optional[str] = None,
        default_lang: str = "en"
    ) -> Dict[str, Any]:
        """Fetch or insert chat settings."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,))
            row = await cursor.fetchone()
            if row:
                chat_dict = dict(row)
                if title and title != chat_dict.get("title"):
                    await db.execute("UPDATE chats SET title = ? WHERE chat_id = ?", (title, chat_id))
                    await db.commit()
                    chat_dict["title"] = title
                return chat_dict

            await db.execute(
                """
                INSERT INTO chats (chat_id, chat_type, title, language)
                VALUES (?, ?, ?, ?)
                """,
                (chat_id, chat_type, title or "Group", default_lang)
            )
            await db.commit()

            cursor = await db.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,))
            new_row = await cursor.fetchone()
            return dict(new_row)

    async def get_chat_language(self, chat_id: int) -> str:
        """Get chat language or fallback to 'en'."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("SELECT language FROM chats WHERE chat_id = ?", (chat_id,))
            row = await cursor.fetchone()
            return row[0] if row and row[0] else "en"

    async def set_chat_language(self, chat_id: int, language: str):
        """Update group chat language."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("UPDATE chats SET language = ? WHERE chat_id = ?", (language, chat_id))
            await db.commit()

    async def record_answer_result(self, user_id: int, is_correct: bool, xp_earned: int = 0, user_name: Optional[str] = None):
        """Record player's answer, streak, and XP update, auto-registering user if needed."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT xp, total_score, current_streak, best_streak FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                await db.execute(
                    """
                    INSERT INTO users (user_id, username, first_name, language)
                    VALUES (?, '', ?, 'en')
                    """,
                    (user_id, user_name or "Player")
                )
                await db.commit()
                cursor = await db.execute("SELECT xp, total_score, current_streak, best_streak FROM users WHERE user_id = ?", (user_id,))
                user = await cursor.fetchone()

            curr_xp = max(0, user["xp"] + xp_earned)
            curr_streak = user["current_streak"] + 1 if is_correct else 0
            best_streak = max(user["best_streak"], curr_streak)
            new_level = self.calculate_level(curr_xp)

            if is_correct:
                await db.execute(
                    """
                    UPDATE users
                    SET xp = ?, level = ?,
                        correct_answers = correct_answers + 1,
                        total_answers = total_answers + 1,
                        current_streak = ?, best_streak = ?
                    WHERE user_id = ?
                    """,
                    (curr_xp, new_level, curr_streak, best_streak, user_id)
                )
            else:
                await db.execute(
                    """
                    UPDATE users
                    SET total_answers = total_answers + 1, current_streak = 0
                    WHERE user_id = ?
                    """,
                    (user_id,)
                )

            await db.commit()

    async def record_answer(self, user_id: int, is_correct: bool, points: int = 0, xp: int = 0, user_name: Optional[str] = None, username: Optional[str] = None):
        """Record answer with points and xp, auto-registering user if needed."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT xp, total_score, current_streak, best_streak FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                await db.execute(
                    """
                    INSERT INTO users (user_id, username, first_name, language)
                    VALUES (?, ?, ?, 'en')
                    """,
                    (user_id, username or "", user_name or "Player")
                )
                await db.commit()
                cursor = await db.execute("SELECT xp, total_score, current_streak, best_streak FROM users WHERE user_id = ?", (user_id,))
                user = await cursor.fetchone()

            curr_xp = max(0, user["xp"] + xp)
            curr_score = max(0, user["total_score"] + points)
            curr_streak = user["current_streak"] + 1 if is_correct else 0
            best_streak = max(user["best_streak"], curr_streak)
            new_level = self.calculate_level(curr_xp)

            if is_correct:
                await db.execute(
                    """
                    UPDATE users
                    SET total_score = ?, xp = ?, level = ?,
                        correct_answers = correct_answers + 1,
                        total_answers = total_answers + 1,
                        current_streak = ?, best_streak = ?
                    WHERE user_id = ?
                    """,
                    (curr_score, curr_xp, new_level, curr_streak, best_streak, user_id)
                )
            else:
                await db.execute(
                    """
                    UPDATE users
                    SET total_score = ?, total_answers = total_answers + 1, current_streak = 0
                    WHERE user_id = ?
                    """,
                    (curr_score, user_id)
                )

            await db.commit()

    async def record_match_player_stats(self, user_id: int, chat_id: Optional[int], first_name: str, is_win: bool, score: int, xp_bonus: int = 0):
        """Update match records for user and group, auto-registering user if needed."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT xp, total_score FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                await db.execute(
                    """
                    INSERT INTO users (user_id, username, first_name, language)
                    VALUES (?, '', ?, 'en')
                    """,
                    (user_id, first_name or "Player")
                )
                await db.commit()
                cursor = await db.execute("SELECT xp, total_score FROM users WHERE user_id = ?", (user_id,))
                user = await cursor.fetchone()

            if user:
                new_xp = max(0, user["xp"] + xp_bonus)
                new_level = self.calculate_level(new_xp)
                new_score = max(0, user["total_score"] + score)
                await db.execute(
                    """
                    UPDATE users
                    SET total_score = ?, xp = ?, level = ?,
                        games_played = games_played + 1,
                        games_won = games_won + ?
                    WHERE user_id = ?
                    """,
                    (new_score, new_xp, new_level, 1 if is_win else 0, user_id)
                )

            if chat_id and chat_id < 0:
                await db.execute(
                    """
                    INSERT INTO group_scores (chat_id, user_id, first_name, score, wins, games_played)
                    VALUES (?, ?, ?, ?, ?, 1)
                    ON CONFLICT(chat_id, user_id) DO UPDATE SET
                        first_name = ?,
                        score = MAX(0, group_scores.score + ?),
                        wins = group_scores.wins + ?,
                        games_played = group_scores.games_played + 1
                    """,
                    (chat_id, user_id, first_name, score, 1 if is_win else 0, first_name, score, 1 if is_win else 0)
                )

            await db.commit()

    async def update_group_player_score(self, chat_id: int, user_id: int, points: int, is_win: bool = False, first_name: str = "Player", username: str = ""):
        """Update user score in a specific group chat, ensuring user and player name are saved."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                await db.execute(
                    """
                    INSERT INTO users (user_id, username, first_name, language)
                    VALUES (?, ?, ?, 'en')
                    """,
                    (user_id, username or "", first_name or "Player")
                )
                await db.commit()

            await db.execute(
                """
                INSERT INTO group_scores (chat_id, user_id, first_name, score, wins, games_played)
                VALUES (?, ?, ?, ?, ?, 1)
                ON CONFLICT(chat_id, user_id) DO UPDATE SET
                    first_name = excluded.first_name,
                    score = MAX(0, group_scores.score + excluded.score),
                    wins = group_scores.wins + excluded.wins,
                    games_played = group_scores.games_played + 1
                """,
                (chat_id, user_id, first_name or "Player", points, 1 if is_win else 0)
            )
            await db.execute(
                """
                UPDATE users
                SET games_played = games_played + 1,
                    games_won = games_won + ?
                WHERE user_id = ?
                """,
                (1 if is_win else 0, user_id)
            )
            await db.commit()

    async def increment_chat_games(self, chat_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("UPDATE chats SET total_games = total_games + 1 WHERE chat_id = ?", (chat_id,))
            await db.commit()

    async def get_global_leaderboard(self, limit: int = 10) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT user_id, username, first_name, total_score, level, xp, games_won, games_played, correct_answers, total_answers
                FROM users
                ORDER BY xp DESC, total_score DESC, games_won DESC
                LIMIT ?
                """,
                (limit,)
            )
            rows = await cursor.fetchall()
            return [dict(r) for r in rows]

    async def get_group_leaderboard(self, chat_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT gs.user_id, COALESCE(u.username, '') AS username, COALESCE(gs.first_name, u.first_name, 'Player') AS first_name, gs.score, gs.wins, gs.wins AS games_won, gs.games_played
                FROM group_scores gs
                LEFT JOIN users u ON gs.user_id = u.user_id
                WHERE gs.chat_id = ?
                ORDER BY gs.score DESC, gs.wins DESC
                LIMIT ?
                """,
                (chat_id, limit)
            )
            rows = await cursor.fetchall()
            return [dict(r) for r in rows]

    async def check_daily_challenge_done(self, user_id: int, challenge_date: Optional[str] = None) -> Optional[Dict[str, Any]]:
        d_str = challenge_date or date.today().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                "SELECT * FROM daily_challenges WHERE user_id = ? AND challenge_date = ?",
                (user_id, d_str)
            )
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def record_daily_challenge_done(self, user_id: int, score: int, xp_bonus: int = 150, challenge_date: Optional[str] = None):
        d_str = challenge_date or date.today().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT OR REPLACE INTO daily_challenges (user_id, challenge_date, score, completed_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (user_id, d_str, score)
            )
            # Award XP & update daily streak
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT xp, last_daily_date, daily_streak FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                await db.execute("INSERT INTO users (user_id, language) VALUES (?, 'en')", (user_id,))
                await db.commit()
                cursor = await db.execute("SELECT xp, last_daily_date, daily_streak FROM users WHERE user_id = ?", (user_id,))
                user = await cursor.fetchone()

            last_date_str = user["last_daily_date"] if user else None
            curr_streak = (user["daily_streak"] if user and user["daily_streak"] else 0)
            if last_date_str:
                try:
                    last_d = date.fromisoformat(last_date_str)
                    this_d = date.fromisoformat(d_str)
                    diff = (this_d - last_d).days
                    if diff == 1:
                        new_streak = curr_streak + 1
                    elif diff == 0:
                        new_streak = max(1, curr_streak)
                    else:
                        new_streak = 1
                except Exception:
                    new_streak = 1
            else:
                new_streak = 1

            new_xp = (user["xp"] if user else 0) + xp_bonus
            new_level = self.calculate_level(new_xp)
            await db.execute(
                "UPDATE users SET xp = ?, level = ?, last_daily_date = ?, daily_streak = ? WHERE user_id = ?",
                (new_xp, new_level, d_str, new_streak, user_id)
            )
            await db.commit()

    async def can_play_daily(self, user_id: int, today_str: str) -> bool:
        done = await self.check_daily_challenge_done(user_id, today_str)
        return done is None

    async def record_daily_completion(self, user_id: int, today_str: str, score: int, xp: int):
        await self.record_daily_challenge_done(user_id, score=score, xp_bonus=xp, challenge_date=today_str)

    async def create_duel(self, chat_id: int, challenger_id: int, challenger_name: str, opponent_id: int, opponent_name: str) -> int:
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                INSERT INTO duels (chat_id, challenger_id, challenger_name, opponent_id, opponent_name, status)
                VALUES (?, ?, ?, ?, ?, 'pending')
                """,
                (chat_id, challenger_id, challenger_name, opponent_id, opponent_name)
            )
            duel_id = cursor.lastrowid
            await db.commit()
            return duel_id

    async def get_duel(self, duel_id: int) -> Optional[Dict[str, Any]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT * FROM duels WHERE duel_id = ?", (duel_id,))
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def update_duel_status(self, duel_id: int, status: str, winner_id: Optional[int] = None):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "UPDATE duels SET status = ?, winner_id = ? WHERE duel_id = ?",
                (status, winner_id, duel_id)
            )
            await db.commit()

    async def record_match(self, chat_id: int, mode: str, winner_id: Optional[int], winner_name: str, winner_score: int, players_count: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT INTO matches (chat_id, mode, winner_id, winner_name, winner_score, players_count)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (chat_id, mode, winner_id, winner_name, winner_score, players_count)
            )
            await db.commit()

# Default singleton instance for convenience functions
_default_instance: Optional[Database] = None

def get_default_db() -> Database:
    global _default_instance
    if _default_instance is None or _default_instance.db_path != config.DB_PATH:
        _default_instance = Database(config.DB_PATH)
    return _default_instance

def calculate_level(xp: int) -> int:
    return Database.calculate_level(xp)

async def init_db(db_path: Optional[str] = None):
    db = Database(db_path) if db_path else get_default_db()
    await db.init_db()

async def get_or_create_user(user_id: int, first_name: str = "", username: str = "", language: str = "en") -> Dict[str, Any]:
    return await get_default_db().get_or_create_user(user_id, username=username, first_name=first_name, default_lang=language)

async def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    return await get_default_db().get_user(user_id)

async def set_user_language(user_id: int, language: str):
    return await get_default_db().set_user_language(user_id, language)

async def get_user_language(user_id: int) -> str:
    return await get_default_db().get_user_language(user_id)

async def record_answer_result(user_id: int, is_correct: bool, xp_earned: int = 0):
    return await get_default_db().record_answer_result(user_id, is_correct, xp_earned)

async def record_match_player_stats(user_id: int, chat_id: Optional[int], first_name: str, is_win: bool, score: int, xp_bonus: int = 0):
    return await get_default_db().record_match_player_stats(user_id, chat_id, first_name, is_win, score, xp_bonus)

async def get_global_leaderboard(limit: int = 10) -> List[Dict[str, Any]]:
    return await get_default_db().get_global_leaderboard(limit)

async def get_group_leaderboard(chat_id: int, limit: int = 10) -> List[Dict[str, Any]]:
    return await get_default_db().get_group_leaderboard(chat_id, limit)

async def check_daily_challenge_done(user_id: int, challenge_date: Optional[str] = None) -> Optional[Dict[str, Any]]:
    return await get_default_db().check_daily_challenge_done(user_id, challenge_date)

async def record_daily_challenge_done(user_id: int, score: int, xp_bonus: int = 150, challenge_date: Optional[str] = None):
    return await get_default_db().record_daily_challenge_done(user_id, score, xp_bonus, challenge_date)

async def create_duel(chat_id: int, challenger_id: int, challenger_name: str, opponent_id: int, opponent_name: str) -> int:
    return await get_default_db().create_duel(chat_id, challenger_id, challenger_name, opponent_id, opponent_name)

async def get_duel(duel_id: int) -> Optional[Dict[str, Any]]:
    return await get_default_db().get_duel(duel_id)

async def update_duel_status(duel_id: int, status: str, winner_id: Optional[int] = None):
    return await get_default_db().update_duel_status(duel_id, status, winner_id)

async def record_match(chat_id: int, mode: str, winner_id: Optional[int], winner_name: str, winner_score: int, players_count: int):
    return await get_default_db().record_match(chat_id, mode, winner_id, winner_name, winner_score, players_count)
