"""
Async SQLite Database Module for GeoGuru & GeoGuessr Telegram Bot.
Handles user profiles, XP, levels, chat settings, group leaderboards, daily streaks, duels, and match history.
Supports both object-oriented (Database class) and modular function-based interfaces.
"""

import aiosqlite
import logging
import time
from typing import Optional, Dict, List, Any
from pathlib import Path
from datetime import date, datetime, timezone
import html

import config
from database import schema
from events.bus import event_bus

logger = logging.getLogger(__name__)

def resolve_clean_user_name(user_id: Optional[int], first_name: Optional[str] = None, username: Optional[str] = None) -> str:
    """Resolve clean display name: never a lone dot. If empty or '.', resolve to @username or Player {user_id}."""
    name = (first_name or "").strip()
    if not name or name == ".":
        u = (username or "").strip().lstrip("@")
        if u and u != ".":
            return f"@{u}"
        return f"Player {user_id}" if user_id else "Player"
    return name

def format_user_mention(user_id: Optional[int], name: Optional[str]) -> str:
    """Format user name as a clickable Telegram profile link <a href="tg://user?id=...">...</a>."""
    raw_name = (name or "").strip()
    if not raw_name or raw_name == ".":
        raw_name = f"Player {user_id}" if user_id else "Player"
    safe_name = html.escape(raw_name)
    if user_id and user_id > 0:
        return f'<a href="tg://user?id={user_id}">{safe_name}</a>'
    return f'<b>{safe_name}</b>'

class SearchUsersResult(dict):
    """Dictionary supporting unpacking as (users, total) and key access."""
    def __iter__(self):
        return iter((self.get("users", []), self.get("total", 0)))

class Database:

    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        """Return an aiosqlite connection with busy_timeout configured for lock prevention."""
        return aiosqlite.connect(self.db_path, timeout=30.0)

    @staticmethod
    def calculate_level(xp: int) -> int:
        """Calculate player level: Level = 1 + int((XP / 200) ** 0.5)"""
        if xp < 0:
            return 1
        return 1 + int((xp / 200) ** 0.5)

    async def init_db(self):
        """Create necessary tables and indexes if they do not exist."""
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        
        async with self._connect() as db:
            for pragma in schema.PRAGMA_STATEMENTS:
                await db.execute(pragma)

            for table_ddl in schema.ALL_TABLES:
                await db.execute(table_ddl)

            # Migrations for existing databases
            try:
                await db.execute("ALTER TABLE users ADD COLUMN is_banned INTEGER DEFAULT 0")
            except Exception:
                pass
            try:
                await db.execute("ALTER TABLE users ADD COLUMN ban_reason TEXT")
            except Exception:
                pass

            # Migrations for answer_logs columns
            for col, col_def in [
                ("username", "TEXT"),
                ("mode", "TEXT"),
                ("question_id", "TEXT"),
                ("selected_option", "TEXT"),
                ("correct_option", "TEXT"),
                ("points", "INTEGER DEFAULT 0"),
                ("time_taken", "REAL DEFAULT 0"),
            ]:
                try:
                    await db.execute(f"ALTER TABLE answer_logs ADD COLUMN {col} {col_def}")
                except Exception:
                    pass


            for index_ddl in schema.INDEX_STATEMENTS:
                await db.execute(index_ddl)

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
        async with self._connect() as db:
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
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def set_user_language(self, user_id: int, language: str):
        """Update preferred user language, ensuring user record exists."""
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO users (user_id, language)
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET language = excluded.language
                """,
                (user_id, language)
            )
            await db.commit()

    async def get_user_language(self, user_id: int) -> str:
        """Get user preferred language or fallback to 'en'."""
        async with self._connect() as db:
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
        async with self._connect() as db:
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
                ON CONFLICT(chat_id) DO UPDATE SET language = excluded.language
                """,
                (chat_id, chat_type, title or "Group", default_lang)
            )
            await db.commit()

            cursor = await db.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,))
            new_row = await cursor.fetchone()
            return dict(new_row)

    async def get_chat_language(self, chat_id: int) -> str:
        """Get chat language or fallback to 'en'."""
        async with self._connect() as db:
            cursor = await db.execute("SELECT language FROM chats WHERE chat_id = ?", (chat_id,))
            row = await cursor.fetchone()
            return row[0] if row and row[0] else "en"

    async def set_chat_language(self, chat_id: int, language: str):
        """Update group chat language, ensuring chat record exists."""
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO chats (chat_id, chat_type, title, language)
                VALUES (?, 'group', 'Group', ?)
                ON CONFLICT(chat_id) DO UPDATE SET language = excluded.language
                """,
                (chat_id, language)
            )
            await db.commit()

    async def record_answer_result(
        self,
        user_id: int,
        is_correct: bool,
        xp_earned: int = 0,
        user_name: Optional[str] = None,
        points: int = 0,
        username: Optional[str] = None,
        chat_id: Optional[int] = None,
        mode: Optional[str] = None,
        question_id: Optional[str] = None,
        question_text: Optional[str] = None,
        selected_option: Optional[str] = None,
        correct_option: Optional[str] = None,
        time_taken: float = 0.0,
        chat_title: Optional[str] = None,
        **kwargs: Any
    ):
        """Record player's answer by delegating to record_answer, ensuring answer_logs insertion."""
        return await self.record_answer(
            user_id=user_id,
            is_correct=is_correct,
            points=points,
            xp=xp_earned,
            user_name=user_name,
            username=username,
            chat_id=chat_id,
            mode=mode,
            question_id=question_id,
            question_text=question_text,
            selected_option=selected_option,
            correct_option=correct_option,
            time_taken=time_taken,
            chat_title=chat_title,
            **kwargs
        )

    async def record_score_event(self, user_id: int, points: int, xp: int = 0, chat_id: Optional[int] = None):
        """Record an incremental score/XP event for time-based leaderboards (daily/weekly/monthly)."""
        if points <= 0 and xp <= 0:
            return
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO score_events (user_id, chat_id, points, xp)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, chat_id, max(0, points), max(0, xp))
            )
            await db.commit()

    async def record_answer(
        self,
        user_id: int,
        is_correct: bool,
        points: int = 0,
        xp: int = 0,
        user_name: Optional[str] = None,
        username: Optional[str] = None,
        chat_id: Optional[int] = None,
        mode: Optional[str] = None,
        question_id: Optional[str] = None,
        question_text: Optional[str] = None,
        selected_option: Optional[str] = None,
        correct_option: Optional[str] = None,
        time_taken: float = 0.0,
        chat_title: Optional[str] = None,
        **kwargs: Any
    ):
        """Record answer with points and xp, auto-registering user, updating streaks, and ALWAYS inserting into answer_logs."""
        if await self.is_user_banned(user_id):
            return

        clean_user_name = resolve_clean_user_name(user_id, user_name, username)
        clean_username = (username or "").strip().lstrip("@")

        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT username, first_name, xp, total_score, current_streak, best_streak FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                await db.execute(
                    """
                    INSERT INTO users (user_id, username, first_name, language)
                    VALUES (?, ?, ?, 'en')
                    """,
                    (user_id, clean_username, clean_user_name)
                )
                await db.commit()
                cursor = await db.execute("SELECT username, first_name, xp, total_score, current_streak, best_streak FROM users WHERE user_id = ?", (user_id,))
                user = await cursor.fetchone()
            else:
                db_fn = user["first_name"] or ""
                db_un = user["username"] or ""
                if (not db_fn or db_fn == ".") and clean_user_name:
                    await db.execute(
                        "UPDATE users SET first_name = ?, username = COALESCE(NULLIF(username, ''), ?) WHERE user_id = ?",
                        (clean_user_name, clean_username, user_id)
                    )
                    await db.commit()

            if (not user_name or user_name.strip() in ("", ".")) and user and user["first_name"] and user["first_name"].strip() not in ("", "."):
                clean_user_name = user["first_name"].strip()
            if not clean_username and user and user["username"]:
                clean_username = user["username"].strip().lstrip("@")

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

            # ALWAYS insert into answer_logs!
            await db.execute(
                """
                INSERT INTO answer_logs (
                    user_id, username, chat_id, mode, question_id,
                    question_text, selected_option, correct_option,
                    is_correct, points, time_taken
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    clean_username or clean_user_name,
                    chat_id,
                    mode or "",
                    question_id or "",
                    question_text or "",
                    selected_option or "",
                    correct_option or "",
                    1 if is_correct else 0,
                    int(points),
                    float(time_taken)
                )
            )

            resolved_chat_title = chat_title or ""
            if chat_id and not resolved_chat_title:
                c_cursor = await db.execute("SELECT title FROM chats WHERE chat_id = ?", (chat_id,))
                c_row = await c_cursor.fetchone()
                if c_row and c_row["title"]:
                    resolved_chat_title = c_row["title"]

            await db.commit()

        event_bus.publish("answer", {
            "user_id": user_id,
            "user_name": clean_user_name,
            "username": clean_username,
            "mode": mode or "",
            "question_text": question_text or "",
            "selected_option": selected_option or "",
            "correct_option": correct_option or "",
            "is_correct": bool(is_correct),
            "points": int(points),
            "xp": int(xp),
            "chat_id": chat_id,
            "chat_title": resolved_chat_title,
            "timestamp": time.time()
        })

        if is_correct and (points > 0 or xp > 0):
            await self.record_score_event(user_id, points, xp, chat_id=chat_id)

    async def add_user_xp(self, user_id: int, xp_to_add: int, first_name: str = "Player", username: str = "") -> int:
        """
        Award XP directly to a user (e.g. from Mini App completion), updating level and recording score event.
        Returns the new total XP.
        """
        if await self.is_user_banned(user_id):
            return 0
        xp_to_add = max(0, int(xp_to_add))
        if xp_to_add == 0:
            user = await self.get_user(user_id)
            return user.get("xp", 0) if user else 0

        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT xp FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                await db.execute(
                    """
                    INSERT INTO users (user_id, username, first_name, language, xp, level)
                    VALUES (?, ?, ?, 'en', 0, 1)
                    """,
                    (user_id, username or "", first_name or "Player")
                )
                await db.commit()
                curr_xp = 0
            else:
                curr_xp = user["xp"] or 0

            new_xp = curr_xp + xp_to_add
            new_level = self.calculate_level(new_xp)

            await db.execute(
                "UPDATE users SET xp = ?, level = ? WHERE user_id = ?",
                (new_xp, new_level, user_id)
            )
            await db.commit()

        await self.record_score_event(user_id, points=0, xp=xp_to_add)
        return new_xp

    async def record_match_player_stats(self, user_id: int, chat_id: Optional[int], first_name: str, is_win: bool, score: int, xp_bonus: int = 0):
        """Update match records for user and group, auto-registering user if needed."""
        async with self._connect() as db:
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

        if score > 0 or xp_bonus > 0:
            await self.record_score_event(user_id, points=score, xp=xp_bonus, chat_id=chat_id)

    async def update_group_player_score(self, chat_id: int, user_id: int, points: int, is_win: bool = False, first_name: str = "Player", username: str = ""):
        """Update user score in a specific group chat, ensuring user and player name are saved."""
        async with self._connect() as db:
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
        async with self._connect() as db:
            await db.execute("UPDATE chats SET total_games = total_games + 1 WHERE chat_id = ?", (chat_id,))
            await db.commit()

    async def get_global_leaderboard(self, limit: int = 10, period: str = "all_time") -> List[Dict[str, Any]]:
        try:
            limit = max(1, min(100, int(limit)))
        except (ValueError, TypeError):
            limit = 10

        period = (period or "all_time").lower()
        intervals = {
            "daily": "-1 day",
            "weekly": "-7 days",
            "monthly": "-30 days",
        }
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            if period in intervals:
                interval_val = intervals[period]
                cursor = await db.execute(
                    """
                    SELECT 
                        se.user_id,
                        COALESCE(u.username, '') AS username,
                        COALESCE(u.first_name, 'Player') AS first_name,
                        SUM(se.points) AS total_score,
                        COALESCE(u.level, 1) AS level,
                        SUM(se.xp) AS xp,
                        COALESCE(u.games_won, 0) AS games_won,
                        COALESCE(u.games_played, 0) AS games_played,
                        COUNT(se.id) AS correct_answers,
                        COALESCE(u.total_answers, 0) AS total_answers
                    FROM score_events se
                    LEFT JOIN users u ON se.user_id = u.user_id
                    WHERE se.created_at >= datetime('now', ?)
                    GROUP BY se.user_id
                    HAVING SUM(se.points) > 0 OR SUM(se.xp) > 0
                    ORDER BY total_score DESC, xp DESC
                    LIMIT ?
                    """,
                    (interval_val, limit)
                )
            else:
                cursor = await db.execute(
                    """
                    SELECT user_id, username, first_name, total_score, level, xp, games_won, games_played, correct_answers, total_answers
                    FROM users
                    ORDER BY total_score DESC, xp DESC, games_won DESC
                    LIMIT ?
                    """,
                    (limit,)
                )
            rows = await cursor.fetchall()
            return [dict(r) for r in rows]

    async def get_group_leaderboard(self, chat_id: Optional[int], limit: int = 10, period: str = "all_time") -> List[Dict[str, Any]]:
        if chat_id is None:
            return []

        try:
            limit = max(1, min(100, int(limit)))
        except (ValueError, TypeError):
            limit = 10

        period = (period or "all_time").lower()
        intervals = {
            "daily": "-1 day",
            "weekly": "-7 days",
            "monthly": "-30 days",
        }
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            if period in intervals:
                interval_val = intervals[period]
                cursor = await db.execute(
                    """
                    SELECT 
                        se.user_id,
                        COALESCE(u.username, '') AS username,
                        COALESCE(gs.first_name, u.first_name, 'Player') AS first_name,
                        SUM(se.points) AS score,
                        COALESCE(gs.wins, 0) AS wins,
                        COALESCE(gs.wins, 0) AS games_won,
                        COALESCE(gs.games_played, 0) AS games_played
                    FROM score_events se
                    LEFT JOIN users u ON se.user_id = u.user_id
                    LEFT JOIN group_scores gs ON se.user_id = gs.user_id AND se.chat_id = gs.chat_id
                    WHERE se.chat_id = ? AND se.created_at >= datetime('now', ?)
                    GROUP BY se.user_id
                    HAVING SUM(se.points) > 0
                    ORDER BY score DESC
                    LIMIT ?
                    """,
                    (chat_id, interval_val, limit)
                )
            else:
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
        clean_d_str = str(d_str).strip().split()[0].split('T')[0]
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                "SELECT * FROM daily_challenges WHERE user_id = ? AND challenge_date = ?",
                (user_id, clean_d_str)
            )
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def record_daily_challenge_done(self, user_id: int, score: int, xp_bonus: int = 150, challenge_date: Optional[str] = None):
        raw_d_str = challenge_date or date.today().isoformat()
        clean_d_str = str(raw_d_str).strip().split()[0].split('T')[0]

        async with self._connect() as db:
            await db.execute(
                """
                INSERT OR REPLACE INTO daily_challenges (user_id, challenge_date, score, completed_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (user_id, clean_d_str, max(0, score))
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
                    clean_last_date = str(last_date_str).strip().split()[0].split('T')[0]
                    last_d = date.fromisoformat(clean_last_date)
                    this_d = date.fromisoformat(clean_d_str)
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

            new_xp = (user["xp"] if user else 0) + max(0, xp_bonus)
            new_level = self.calculate_level(new_xp)
            await db.execute(
                "UPDATE users SET xp = ?, level = ?, last_daily_date = ?, daily_streak = ? WHERE user_id = ?",
                (new_xp, new_level, clean_d_str, new_streak, user_id)
            )
            await db.commit()

        if score > 0 or xp_bonus > 0:
            await self.record_score_event(user_id, points=max(0, score), xp=max(0, xp_bonus), chat_id=None)

    async def get_daily_streak(self, user_id: int, today_date: Optional[str] = None) -> int:
        """
        Get player's active daily streak.
        If the player hasn't played today or yesterday (gap > 1 day), streak is broken and returns 0.
        """
        user = await self.get_user(user_id)
        if not user or not user.get("last_daily_date"):
            return 0
        last_date_str = user["last_daily_date"]
        streak = user.get("daily_streak", 0)
        if streak <= 0:
            return 0
        try:
            today_str = today_date or date.today().isoformat()
            clean_last = str(last_date_str).strip().split()[0].split('T')[0]
            clean_today = str(today_str).strip().split()[0].split('T')[0]
            last_d = date.fromisoformat(clean_last)
            today_d = date.fromisoformat(clean_today)
            diff = (today_d - last_d).days
            if diff <= 1:
                return streak
            return 0
        except Exception:
            return 0

    async def can_play_daily(self, user_id: int, today_str: str) -> bool:
        done = await self.check_daily_challenge_done(user_id, today_str)
        return done is None

    async def record_daily_completion(self, user_id: int, today_str: str, score: int, xp: int):
        await self.record_daily_challenge_done(user_id, score=score, xp_bonus=xp, challenge_date=today_str)

    async def create_duel(self, chat_id: int, challenger_id: int, challenger_name: str, opponent_id: int, opponent_name: str) -> int:
        async with self._connect() as db:
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
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT * FROM duels WHERE duel_id = ?", (duel_id,))
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def update_duel_status(self, duel_id: int, status: str, winner_id: Optional[int] = None):
        async with self._connect() as db:
            await db.execute(
                "UPDATE duels SET status = ?, winner_id = ? WHERE duel_id = ?",
                (status, winner_id, duel_id)
            )
            await db.commit()

    async def record_match(self, chat_id: int, mode: str, winner_id: Optional[int], winner_name: str, winner_score: int, players_count: int):
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO matches (chat_id, mode, winner_id, winner_name, winner_score, players_count)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (chat_id, mode, winner_id, winner_name, winner_score, players_count)
            )
            await db.commit()

    async def ban_user(self, user_id: int, reason: str = "") -> bool:
        """Ban user and record reason."""
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO users (user_id, is_banned, ban_reason)
                VALUES (?, 1, ?)
                ON CONFLICT(user_id) DO UPDATE SET is_banned = 1, ban_reason = excluded.ban_reason
                """,
                (user_id, reason or "Banned by administrator")
            )
            await db.commit()
        event_bus.publish("user_banned", {"user_id": user_id, "reason": reason})
        return True

    async def unban_user(self, user_id: int) -> bool:
        """Unban user."""
        async with self._connect() as db:
            await db.execute(
                "UPDATE users SET is_banned = 0, ban_reason = NULL WHERE user_id = ?",
                (user_id,)
            )
            await db.commit()
        event_bus.publish("user_unbanned", {"user_id": user_id})
        return True

    async def is_user_banned(self, user_id: int) -> bool:
        """Check if user is banned."""
        async with self._connect() as db:
            cursor = await db.execute("SELECT is_banned FROM users WHERE user_id = ?", (user_id,))
            row = await cursor.fetchone()
            return bool(row and row[0])

    async def adjust_user_xp(self, user_id: int, xp: int) -> int:
        """Set user's total XP to a specific value and recompute level."""
        new_xp = max(0, int(xp))
        new_level = self.calculate_level(new_xp)
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO users (user_id, xp, level)
                VALUES (?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET xp = excluded.xp, level = excluded.level
                """,
                (user_id, new_xp, new_level)
            )
            await db.commit()
        event_bus.publish("xp_adjusted", {"user_id": user_id, "xp": new_xp, "level": new_level})
        return new_xp

    async def adjust_user_score(self, user_id: int, points: int) -> int:
        """Add or subtract from total_score (cannot be negative), return new total_score."""
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT total_score FROM users WHERE user_id = ?", (user_id,))
            user = await cursor.fetchone()
            if not user:
                new_score = max(0, points)
                await db.execute(
                    """
                    INSERT INTO users (user_id, total_score, language)
                    VALUES (?, ?, 'en')
                    """,
                    (user_id, new_score)
                )
            else:
                curr_score = user["total_score"] or 0
                new_score = max(0, curr_score + points)
                await db.execute(
                    "UPDATE users SET total_score = ? WHERE user_id = ?",
                    (new_score, user_id)
                )
            await db.commit()
        event_bus.publish("score_adjusted", {"user_id": user_id, "score": new_score, "delta": points})
        return new_score

    async def adjust_user_points(self, user_id: int, points: int) -> int:
        """Set user's total score / points to a specific value."""
        new_points = max(0, int(points))
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO users (user_id, total_score)
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET total_score = excluded.total_score
                """,
                (user_id, new_points)
            )
            await db.commit()
        event_bus.publish("points_adjusted", {"user_id": user_id, "points": new_points})
        return new_points

    async def set_user_level(self, user_id: int, level: int) -> int:
        """Set user's level directly."""
        new_level = max(1, int(level))
        async with self._connect() as db:
            await db.execute(
                """
                INSERT INTO users (user_id, level)
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
                """,
                (user_id, new_level)
            )
            await db.commit()
        event_bus.publish("level_adjusted", {"user_id": user_id, "level": new_level})
        return new_level

    async def reset_user_stats(self, user_id: int) -> bool:
        """Reset user's game statistics: score=0, xp=0, level=1, total_answers=0, correct_answers=0, games_played=0, games_won=0, current_streak=0, best_streak=0."""
        async with self._connect() as db:
            await db.execute(
                """
                UPDATE users
                SET xp = 0, level = 1, total_score = 0,
                    games_played = 0, games_won = 0,
                    correct_answers = 0, total_answers = 0,
                    best_streak = 0, current_streak = 0, daily_streak = 0
                WHERE user_id = ?
                """,
                (user_id,)
            )
            await db.execute("DELETE FROM group_scores WHERE user_id = ?", (user_id,))
            await db.commit()
        event_bus.publish("user_stats_reset", {"user_id": user_id})
        event_bus.publish("stats_reset", {"user_id": user_id})
        return True

    async def record_admin_login(
        self,
        user_id: int,
        username: str = "",
        ip: str = "",
        user_agent: str = "",
        auth_method: str = "otp"
    ) -> int:
        """Record successful administrator login attempt."""
        async with self._connect() as db:
            cursor = await db.execute(
                """
                INSERT INTO admin_logins (user_id, username, ip, user_agent, auth_method)
                VALUES (?, ?, ?, ?, ?)
                """,
                (user_id, username or "", ip or "", user_agent or "", auth_method or "otp")
            )
            await db.commit()
            login_id = cursor.lastrowid
        event_bus.publish("admin_login", {
            "id": login_id,
            "user_id": user_id,
            "username": username or "",
            "ip": ip or "",
            "auth_method": auth_method or "otp"
        })
        return login_id

    async def get_recent_admin_logins(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Return the last administrator logins."""
        limit = max(1, min(100, int(limit)))
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT al.id, al.user_id, al.username, al.ip, al.user_agent, al.auth_method, al.created_at,
                       COALESCE(NULLIF(u.first_name, '.'), al.username, 'Admin') as first_name
                FROM admin_logins al
                LEFT JOIN users u ON al.user_id = u.user_id
                ORDER BY al.created_at DESC, al.id DESC
                LIMIT ?
                """,
                (limit,)
            )
            return [dict(r) for r in await cursor.fetchall()]

    async def get_admin_logins(self, limit: int = 50) -> List[Dict[str, Any]]:
        return await self.get_recent_admin_logins(limit)

    async def get_recent_users(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Fetch the last 50 newly registered users (created_at DESC)."""
        limit = max(1, min(100, int(limit)))
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT user_id, username, first_name, language, xp, level, total_score,
                       games_played, games_won, correct_answers, total_answers,
                       best_streak, current_streak, is_banned, ban_reason, created_at
                FROM users
                ORDER BY created_at DESC, user_id DESC
                LIMIT ?
                """,
                (limit,)
            )
            return [dict(r) for r in await cursor.fetchall()]

    async def get_user_full_profile(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Return user full profile with stats and last 100 answers."""
        user = await self.get_user(user_id)
        if not user:
            return None
        
        user_dict = dict(user)
        total_answers = int(user_dict.get("total_answers") or 0)
        correct_answers = int(user_dict.get("correct_answers") or 0)
        accuracy = round((correct_answers / total_answers * 100), 1) if total_answers > 0 else 0.0

        games_played = int(user_dict.get("games_played") or 0)
        games_won = int(user_dict.get("games_won") or 0)
        win_rate = round((games_won / games_played * 100), 1) if games_played > 0 else 0.0

        stats = {
            "total_score": int(user_dict.get("total_score") or 0),
            "xp": int(user_dict.get("xp") or 0),
            "level": int(user_dict.get("level") or 1),
            "win_rate": win_rate,
            "accuracy": accuracy,
            "correct_answers": correct_answers,
            "total_answers": total_answers,
            "games_played": games_played,
            "games_won": games_won,
            "best_streak": int(user_dict.get("best_streak") or 0),
            "current_streak": int(user_dict.get("current_streak") or 0),
            "streak": int(user_dict.get("current_streak") or 0),
            "daily_streak": int(user_dict.get("daily_streak") or 0),
            "is_banned": bool(user_dict.get("is_banned")),
            "ban_reason": user_dict.get("ban_reason") or "",
            "created_at": user_dict.get("created_at") or "",
        }

        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT al.id, al.user_id, al.username, al.chat_id, al.mode,
                       al.question_id, al.question_text, al.selected_option,
                       al.correct_option, al.selected_option AS user_answer,
                       al.correct_option AS correct_answer, al.is_correct,
                       al.points, al.time_taken, al.created_at, c.title as chat_title
                FROM answer_logs al
                LEFT JOIN chats c ON al.chat_id = c.chat_id
                WHERE al.user_id = ?
                ORDER BY al.id DESC
                LIMIT 100
                """,
                (user_id,)
            )
            answers = [dict(r) for r in await cursor.fetchall()]

            cursor = await db.execute(
                """
                SELECT gs.chat_id, gs.score, gs.wins, gs.games_played, c.title
                FROM group_scores gs
                LEFT JOIN chats c ON gs.chat_id = c.chat_id
                WHERE gs.user_id = ?
                ORDER BY gs.score DESC
                """,
                (user_id,)
            )
            groups = [dict(r) for r in await cursor.fetchall()]

        return {
            **user_dict,
            "user": user_dict,
            "stats": stats,
            "answers": answers,
            "recent_answers": answers,
            "accuracy": accuracy,
            "win_rate": win_rate,
            "groups": groups
        }

    async def get_answers_history(
        self,
        query: Optional[str] = None,
        mode: Optional[str] = None,
        correct: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Fetch answer logs with filtering by search text, mode, and correctness."""
        limit = max(1, min(100, int(limit)))
        offset = max(0, int(offset))
        conditions = []
        params: List[Any] = []

        if query:
            clean_q = f"%{query.strip()}%"
            conditions.append("(al.question_text LIKE ? OR al.username LIKE ? OR u.first_name LIKE ? OR al.selected_option LIKE ? OR CAST(al.user_id AS TEXT) LIKE ?)")
            params.extend([clean_q, clean_q, clean_q, clean_q, clean_q])

        if mode and mode != "all":
            conditions.append("LOWER(al.mode) = LOWER(?)")
            params.append(mode.strip())

        if correct is not None and correct != "" and correct != "all":
            if str(correct).lower() in ("true", "1", "yes", "correct"):
                conditions.append("al.is_correct = 1")
            elif str(correct).lower() in ("false", "0", "no", "incorrect"):
                conditions.append("al.is_correct = 0")

        where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            count_sql = f"""
                SELECT COUNT(*) FROM answer_logs al
                LEFT JOIN users u ON al.user_id = u.user_id
                {where_clause}
            """
            cursor = await db.execute(count_sql, params)
            total = (await cursor.fetchone())[0]

            query_sql = f"""
                SELECT al.id, al.user_id, al.username, al.chat_id, al.mode,
                       al.question_id, al.question_text, al.selected_option,
                       al.correct_option, al.is_correct, al.points, al.time_taken,
                       al.created_at,
                       COALESCE(u.first_name, al.username, 'Player') as first_name,
                       c.title as chat_title
                FROM answer_logs al
                LEFT JOIN users u ON al.user_id = u.user_id
                LEFT JOIN chats c ON al.chat_id = c.chat_id
                {where_clause}
                ORDER BY al.id DESC
                LIMIT ? OFFSET ?
            """
            cursor = await db.execute(query_sql, params + [limit, offset])
            answers = [dict(r) for r in await cursor.fetchall()]

            return {
                "answers": answers,
                "total": total,
                "limit": limit,
                "offset": offset
            }

    async def record_answer_log(
        self,
        user_id: int,
        username: Optional[str] = None,
        chat_id: Optional[int] = None,
        mode: Optional[str] = None,
        question_id: Optional[str] = None,
        question_text: Optional[str] = None,
        selected_option: Optional[str] = None,
        correct_option: Optional[str] = None,
        is_correct: bool | int = False,
        points: int = 0,
        time_taken: float = 0.0
    ) -> int:
        """Insert an answer log record and publish rich event to EventBus."""
        async with self._connect() as db:
            cursor = await db.execute(
                """
                INSERT INTO answer_logs (
                    user_id, username, chat_id, mode, question_id,
                    question_text, selected_option, correct_option,
                    is_correct, points, time_taken
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    username or "",
                    chat_id,
                    mode or "",
                    question_id or "",
                    question_text or "",
                    selected_option or "",
                    correct_option or "",
                    1 if is_correct else 0,
                    int(points),
                    float(time_taken)
                )
            )
            await db.commit()
            row_id = cursor.lastrowid

        # Determine safe display name preventing lone "."
        first_name = ""
        db_username = username or ""
        try:
            async with self._connect() as db:
                db.row_factory = aiosqlite.Row
                c = await db.execute("SELECT first_name, username FROM users WHERE user_id = ?", (user_id,))
                u_row = await c.fetchone()
                if u_row:
                    first_name = u_row["first_name"] or ""
                    if not db_username:
                        db_username = u_row["username"] or ""
        except Exception:
            pass

        if first_name and first_name.strip() not in (".", "..", "...", ""):
            display_name = f"{first_name} (@{db_username})" if db_username else first_name
        elif db_username:
            display_name = f"@{db_username}"
        else:
            display_name = f"User #{user_id}"

        # Resolve clean category
        m_upper = (mode or "ZAKOVAT").upper()
        if "GEO" in m_upper or "FLAG" in m_upper or "CAPITAL" in m_upper:
            cat = "GEOGRAPHY"
        elif "COSMOS" in m_upper or "ASTRO" in m_upper:
            cat = "COSMOS"
        elif "SCIENCE" in m_upper:
            cat = "SCIENCE"
        elif "HIST" in m_upper:
            cat = "HISTORY"
        elif "DUEL" in m_upper:
            cat = "DUEL"
        elif chat_id and chat_id < 0:
            cat = "GROUP"
        elif "SOLO" in m_upper:
            cat = "SOLO"
        else:
            cat = "ZAKOVAT"

        chat_tag = f"Guruh: #{chat_id}" if chat_id and chat_id < 0 else "Shaxsiy"
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        payload = {
            "id": row_id,
            "user_id": user_id,
            "username": db_username,
            "first_name": first_name,
            "user_name": display_name,
            "chat_id": chat_id,
            "chat_tag": chat_tag,
            "category": cat,
            "mode": mode or "SOLO",
            "question_id": question_id or "",
            "question_text": question_text or "",
            "selected_option": selected_option or "",
            "correct_option": correct_option or "",
            "is_correct": bool(is_correct),
            "points": int(points),
            "xp": int(points // 4 if is_correct else 0),
            "time_taken": float(time_taken),
            "created_at": now_str,
            "node_hash": f"tg-dc{((user_id or 0) % 5) + 1} · #{str(user_id or 0)[-4:]}"
        }

        event_bus.publish("answer", payload)
        event_bus.publish("answer_submitted", payload)
        return row_id

    async def log_answer(self, user_id: int, chat_id: Optional[int], question_text: str, user_answer: str, correct_answer: str, is_correct: bool):
        """Compatibility wrapper for recording answer logs."""
        return await self.record_answer_log(
            user_id=user_id,
            chat_id=chat_id,
            question_text=question_text,
            selected_option=user_answer,
            correct_option=correct_answer,
            is_correct=is_correct
        )

    async def get_admin_dashboard_stats(self) -> Dict[str, Any]:
        """Aggregate platform metrics for admin dashboard."""
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row

            # Users stats
            cursor = await db.execute("""
                SELECT 
                    COUNT(*) as total_users,
                    SUM(CASE WHEN is_banned = 1 THEN 1 ELSE 0 END) as banned_users,
                    COALESCE(SUM(correct_answers), 0) as total_correct,
                    COALESCE(SUM(total_answers), 0) as total_answers
                FROM users
            """)
            u_row = dict(await cursor.fetchone() or {})
            total_users = u_row.get("total_users") or 0
            banned_users = u_row.get("banned_users") or 0

            # New users today
            cursor = await db.execute("SELECT COUNT(*) FROM users WHERE DATE(created_at) = DATE('now')")
            new_users_today = (await cursor.fetchone())[0]

            # Groups count
            cursor = await db.execute("SELECT COUNT(*) FROM chats WHERE chat_type IN ('group', 'supergroup') OR chat_id < 0")
            total_groups = (await cursor.fetchone())[0]

            # Total games (max of matches count or chat total_games sum)
            cursor = await db.execute("SELECT COUNT(*) FROM matches")
            matches_count = (await cursor.fetchone())[0]
            cursor = await db.execute("SELECT COALESCE(SUM(total_games), 0) FROM chats")
            chat_games_count = (await cursor.fetchone())[0]
            total_games = max(matches_count, chat_games_count)

            # Answers from answer_logs
            cursor = await db.execute("""
                SELECT 
                    COUNT(*) as total_logs,
                    COALESCE(SUM(is_correct), 0) as correct_logs,
                    COALESCE(SUM(CASE WHEN DATE(created_at) = DATE('now') THEN 1 ELSE 0 END), 0) as answers_today,
                    COALESCE(SUM(CASE WHEN DATE(created_at) = DATE('now') AND is_correct = 1 THEN 1 ELSE 0 END), 0) as correct_today
                FROM answer_logs
            """)
            al_row = dict(await cursor.fetchone() or {})
            total_answers = al_row.get("total_logs") or 0
            correct_answers = al_row.get("correct_logs") or 0
            answers_today = al_row.get("answers_today") or 0
            correct_answers_today = al_row.get("correct_today") or 0

            # Fallback if answer_logs has no records yet
            if total_answers == 0:
                total_answers = u_row.get("total_answers") or 0
                correct_answers = u_row.get("total_correct") or 0

            accuracy_pct = round((correct_answers / total_answers * 100), 1) if total_answers > 0 else 0.0

            # Top modes: list of (mode, count)
            cursor = await db.execute("""
                SELECT mode, COUNT(*) as cnt
                FROM answer_logs
                WHERE mode IS NOT NULL AND mode != ''
                GROUP BY mode
                ORDER BY cnt DESC
                LIMIT 5
            """)
            top_modes = [(r["mode"], r["cnt"]) for r in await cursor.fetchall()]
            if not top_modes:
                cursor = await db.execute("""
                    SELECT mode, COUNT(*) as cnt
                    FROM matches
                    WHERE mode IS NOT NULL AND mode != ''
                    GROUP BY mode
                    ORDER BY cnt DESC
                    LIMIT 5
                """)
                top_modes = [(r["mode"], r["cnt"]) for r in await cursor.fetchall()]

            # Active users today (from score_events)
            cursor = await db.execute("SELECT COUNT(DISTINCT user_id) as active_today FROM score_events WHERE created_at >= date('now')")
            active_today = (await cursor.fetchone())[0]

            # 24h activity by hour
            cursor = await db.execute("""
                SELECT strftime('%H:00', created_at) as hour_label, COUNT(*) as event_count, COALESCE(SUM(points), 0) as points_sum
                FROM score_events
                WHERE created_at >= datetime('now', '-24 hours')
                GROUP BY strftime('%H:00', created_at)
                ORDER BY hour_label ASC
            """)
            activity_24h = [dict(r) for r in await cursor.fetchall()]

            # Recent 5 top users
            cursor = await db.execute("""
                SELECT user_id, username, first_name, total_score, xp, level
                FROM users
                ORDER BY total_score DESC, xp DESC
                LIMIT 5
            """)
            top_users = [dict(r) for r in await cursor.fetchall()]

            mode_dist = [{"mode": m, "match_count": c} for m, c in top_modes]

            return {
                "total_users": total_users,
                "new_users_today": new_users_today,
                "total_groups": total_groups,
                "total_games": total_games,
                "total_answers": total_answers,
                "answers_today": answers_today,
                "correct_answers_today": correct_answers_today,
                "accuracy_pct": accuracy_pct,
                "accuracy_percent": accuracy_pct,
                "banned_users": banned_users,
                "top_modes": top_modes,
                "active_today": active_today,
                "activity_24h": activity_24h,
                "mode_distribution": mode_dist,
                "top_users": top_users,
            }

    async def search_users(self, query: str = "", limit: int = 50, offset: int = 0) -> SearchUsersResult:
        """Search users matching user_id, username, or first_name with total count."""
        limit = max(1, min(100, int(limit)))
        offset = max(0, int(offset))
        query = (query or "").strip()

        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            if not query:
                cursor = await db.execute("SELECT COUNT(*) FROM users")
                total = (await cursor.fetchone())[0]

                cursor = await db.execute(
                    """
                    SELECT user_id, username, first_name, language, xp, level, total_score,
                           games_played, games_won, correct_answers, total_answers,
                           best_streak, current_streak, is_banned, ban_reason, created_at
                    FROM users
                    ORDER BY total_score DESC, xp DESC
                    LIMIT ? OFFSET ?
                    """,
                    (limit, offset)
                )
            else:
                clean_q = f"%{query}%"
                uid = int(query) if query.isdigit() or (query.startswith("-") and query[1:].isdigit()) else None
                if uid is not None:
                    cursor = await db.execute(
                        "SELECT COUNT(*) FROM users WHERE user_id = ? OR username LIKE ? OR first_name LIKE ?",
                        (uid, clean_q, clean_q)
                    )
                    total = (await cursor.fetchone())[0]

                    cursor = await db.execute(
                        """
                        SELECT user_id, username, first_name, language, xp, level, total_score,
                               games_played, games_won, correct_answers, total_answers,
                               best_streak, current_streak, is_banned, ban_reason, created_at
                        FROM users
                        WHERE user_id = ? OR username LIKE ? OR first_name LIKE ?
                        ORDER BY total_score DESC, xp DESC
                        LIMIT ? OFFSET ?
                        """,
                        (uid, clean_q, clean_q, limit, offset)
                    )
                else:
                    cursor = await db.execute(
                        "SELECT COUNT(*) FROM users WHERE username LIKE ? OR first_name LIKE ?",
                        (clean_q, clean_q)
                    )
                    total = (await cursor.fetchone())[0]

                    cursor = await db.execute(
                        """
                        SELECT user_id, username, first_name, language, xp, level, total_score,
                               games_played, games_won, correct_answers, total_answers,
                               best_streak, current_streak, is_banned, ban_reason, created_at
                        FROM users
                        WHERE username LIKE ? OR first_name LIKE ?
                        ORDER BY total_score DESC, xp DESC
                        LIMIT ? OFFSET ?
                        """,
                        (clean_q, clean_q, limit, offset)
                    )

            rows = await cursor.fetchall()
            users_list = [dict(r) for r in rows]
            return SearchUsersResult({
                "users": users_list,
                "total": total,
                "limit": limit,
                "offset": offset,
            })

    async def get_admin_users(self, query: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        """Compatibility wrapper for user search and pagination."""
        return await self.search_users(query=query or "", limit=limit, offset=offset)

    async def get_user_detail(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user details including recent 10 answer logs and verified stats."""
        user = await self.get_user(user_id)
        if not user:
            return None
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT * FROM answer_logs
                WHERE user_id = ?
                ORDER BY created_at DESC, id DESC
                LIMIT 10
                """,
                (user_id,)
            )
            answers = [dict(r) for r in await cursor.fetchall()]

            data = dict(user)
            data["user"] = dict(user)
            data["recent_answers"] = answers
            return data

    async def get_admin_user_detail(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Detailed user profile with recent activity, answers, and group scores."""
        detail = await self.get_user_detail(user_id)
        if not detail:
            return None
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                "SELECT id, chat_id, points, xp, created_at FROM score_events WHERE user_id = ? ORDER BY id DESC LIMIT 20",
                (user_id,)
            )
            detail["recent_events"] = [dict(r) for r in await cursor.fetchall()]

            cursor = await db.execute(
                """
                SELECT gs.chat_id, gs.score, gs.wins, gs.games_played, c.title
                FROM group_scores gs
                LEFT JOIN chats c ON gs.chat_id = c.chat_id
                WHERE gs.user_id = ?
                ORDER BY gs.score DESC
                """,
                (user_id,)
            )
            detail["groups"] = [dict(r) for r in await cursor.fetchall()]

            cursor = await db.execute(
                "SELECT challenge_date, score, completed_at FROM daily_challenges WHERE user_id = ? ORDER BY challenge_date DESC LIMIT 10",
                (user_id,)
            )
            detail["daily_history"] = [dict(r) for r in await cursor.fetchall()]
            return detail

    async def get_chat_list(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        """List groups and chats with total_games, title, language."""
        limit = max(1, min(100, int(limit)))
        offset = max(0, int(offset))
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT chat_id, chat_type, title, language, total_games, created_at
                FROM chats
                ORDER BY total_games DESC, created_at DESC
                LIMIT ? OFFSET ?
                """,
                (limit, offset)
            )
            return [dict(r) for r in await cursor.fetchall()]

    async def get_admin_groups(self, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        """List groups with game and member statistics."""
        limit = max(1, min(100, int(limit)))
        offset = max(0, int(offset))
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT COUNT(*) FROM chats WHERE chat_type IN ('group', 'supergroup')")
            total = (await cursor.fetchone())[0]

            cursor = await db.execute(
                """
                SELECT c.chat_id, c.title, c.chat_type, c.language, c.total_games, c.created_at,
                       COUNT(gs.user_id) as players_count,
                       COALESCE(SUM(gs.score), 0) as total_group_score
                FROM chats c
                LEFT JOIN group_scores gs ON c.chat_id = gs.chat_id
                WHERE c.chat_type IN ('group', 'supergroup')
                GROUP BY c.chat_id
                ORDER BY c.total_games DESC, total_group_score DESC
                LIMIT ? OFFSET ?
                """,
                (limit, offset)
            )
            groups = [dict(r) for r in await cursor.fetchall()]
            return {
                "total": total,
                "groups": groups
            }

    async def get_recent_answer_logs(
        self,
        limit: int = 50,
        offset: int = 0,
        user_id: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Retrieve recent answer logs, optionally filtered by user_id."""
        limit = max(1, min(100, int(limit)))
        offset = max(0, int(offset))
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            if user_id is not None:
                cursor = await db.execute(
                    """
                    SELECT al.*, al.selected_option AS user_answer, al.correct_option AS correct_answer,
                           COALESCE(u.username, '') as user_username, COALESCE(u.first_name, 'Player') as first_name
                    FROM answer_logs al
                    LEFT JOIN users u ON al.user_id = u.user_id
                    WHERE al.user_id = ?
                    ORDER BY al.id DESC
                    LIMIT ? OFFSET ?
                    """,
                    (user_id, limit, offset)
                )
            else:
                cursor = await db.execute(
                    """
                    SELECT al.*, al.selected_option AS user_answer, al.correct_option AS correct_answer,
                           COALESCE(u.username, '') as user_username, COALESCE(u.first_name, 'Player') as first_name
                    FROM answer_logs al
                    LEFT JOIN users u ON al.user_id = u.user_id
                    ORDER BY al.id DESC
                    LIMIT ? OFFSET ?
                    """,
                    (limit, offset)
                )
            return [dict(r) for r in await cursor.fetchall()]

    async def get_difficult_questions(self, limit: int = 20) -> List[Dict[str, Any]]:
        """Return questions with lowest accuracy rate from answer_logs."""
        limit = max(1, min(100, int(limit)))
        async with self._connect() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT 
                    question_id,
                    question_text,
                    mode,
                    COUNT(*) as total_attempts,
                    SUM(is_correct) as correct_count,
                    ROUND(CAST(SUM(is_correct) AS REAL) / COUNT(*) * 100, 1) as accuracy_pct
                FROM answer_logs
                WHERE (question_id IS NOT NULL AND question_id != '')
                   OR (question_text IS NOT NULL AND question_text != '')
                GROUP BY COALESCE(NULLIF(question_id, ''), question_text)
                ORDER BY accuracy_pct ASC, total_attempts DESC
                LIMIT ?
                """,
                (limit,)
            )
            return [dict(r) for r in await cursor.fetchall()]

    async def get_admin_answers(self, limit: int = 50) -> Dict[str, Any]:
        """Fetch recent answer logs and difficult questions analysis."""
        limit = max(1, min(100, int(limit)))
        recent_logs = await self.get_recent_answer_logs(limit=limit)
        difficult_questions = await self.get_difficult_questions(limit=15)
        return {
            "recent_answers": recent_logs,
            "difficult_questions": difficult_questions
        }

    async def get_all_broadcast_recipients(self, target: str = "all") -> List[int]:
        """Fetch recipient chat/user IDs for broadcasting."""
        target = (target or "all").lower()
        recipients = set()
        async with self._connect() as db:
            if target in ("all", "users"):
                cursor = await db.execute("SELECT user_id FROM users WHERE is_banned = 0")
                for r in await cursor.fetchall():
                    recipients.add(r[0])
            if target in ("all", "groups"):
                cursor = await db.execute("SELECT chat_id FROM chats WHERE chat_type IN ('group', 'supergroup')")
                for r in await cursor.fetchall():
                    recipients.add(r[0])
        return sorted(list(recipients))



# Default singleton instance for convenience functions
_default_instance: Optional[Database] = None

def get_default_db() -> Database:
    global _default_instance
    if _default_instance is None:
        _default_instance = Database(config.DB_PATH)
    return _default_instance

def set_default_db(db: Optional[Database]) -> None:
    global _default_instance
    _default_instance = db


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

async def record_answer_result(
    user_id: int,
    is_correct: bool,
    xp_earned: int = 0,
    user_name: Optional[str] = None,
    points: int = 0,
    username: Optional[str] = None,
    chat_id: Optional[int] = None,
    mode: Optional[str] = None,
    question_id: Optional[str] = None,
    question_text: Optional[str] = None,
    selected_option: Optional[str] = None,
    correct_option: Optional[str] = None,
    time_taken: float = 0.0,
    chat_title: Optional[str] = None,
    **kwargs: Any
):
    return await get_default_db().record_answer_result(
        user_id=user_id,
        is_correct=is_correct,
        xp_earned=xp_earned,
        user_name=user_name,
        points=points,
        username=username,
        chat_id=chat_id,
        mode=mode,
        question_id=question_id,
        question_text=question_text,
        selected_option=selected_option,
        correct_option=correct_option,
        time_taken=time_taken,
        chat_title=chat_title,
        **kwargs
    )

async def record_answer(
    user_id: int,
    is_correct: bool,
    points: int = 0,
    xp: int = 0,
    user_name: Optional[str] = None,
    username: Optional[str] = None,
    chat_id: Optional[int] = None,
    mode: Optional[str] = None,
    question_id: Optional[str] = None,
    question_text: Optional[str] = None,
    selected_option: Optional[str] = None,
    correct_option: Optional[str] = None,
    time_taken: float = 0.0,
    chat_title: Optional[str] = None,
    **kwargs: Any
):
    return await get_default_db().record_answer(
        user_id=user_id,
        is_correct=is_correct,
        points=points,
        xp=xp,
        user_name=user_name,
        username=username,
        chat_id=chat_id,
        mode=mode,
        question_id=question_id,
        question_text=question_text,
        selected_option=selected_option,
        correct_option=correct_option,
        time_taken=time_taken,
        chat_title=chat_title,
        **kwargs
    )

async def add_user_xp(user_id: int, xp_to_add: int, first_name: str = "Player", username: str = "") -> int:
    return await get_default_db().add_user_xp(user_id, xp_to_add, first_name=first_name, username=username)

async def record_match_player_stats(user_id: int, chat_id: Optional[int], first_name: str, is_win: bool, score: int, xp_bonus: int = 0):
    return await get_default_db().record_match_player_stats(user_id, chat_id, first_name, is_win, score, xp_bonus)

async def get_global_leaderboard(limit: int = 10, period: str = "all_time") -> List[Dict[str, Any]]:
    return await get_default_db().get_global_leaderboard(limit, period)

async def get_group_leaderboard(chat_id: int, limit: int = 10, period: str = "all_time") -> List[Dict[str, Any]]:
    return await get_default_db().get_group_leaderboard(chat_id, limit, period)

async def check_daily_challenge_done(user_id: int, challenge_date: Optional[str] = None) -> Optional[Dict[str, Any]]:
    return await get_default_db().check_daily_challenge_done(user_id, challenge_date)

async def record_daily_challenge_done(user_id: int, score: int, xp_bonus: int = 150, challenge_date: Optional[str] = None):
    return await get_default_db().record_daily_challenge_done(user_id, score, xp_bonus, challenge_date)

async def get_daily_streak(user_id: int, today_date: Optional[str] = None) -> int:
    return await get_default_db().get_daily_streak(user_id, today_date)

async def create_duel(chat_id: int, challenger_id: int, challenger_name: str, opponent_id: int, opponent_name: str) -> int:
    return await get_default_db().create_duel(chat_id, challenger_id, challenger_name, opponent_id, opponent_name)

async def get_duel(duel_id: int) -> Optional[Dict[str, Any]]:
    return await get_default_db().get_duel(duel_id)

async def update_duel_status(duel_id: int, status: str, winner_id: Optional[int] = None):
    return await get_default_db().update_duel_status(duel_id, status, winner_id)

async def record_match(chat_id: int, mode: str, winner_id: Optional[int], winner_name: str, winner_score: int, players_count: int):
    return await get_default_db().record_match(chat_id, mode, winner_id, winner_name, winner_score, players_count)

async def set_chat_language(chat_id: int, language: str):
    return await get_default_db().set_chat_language(chat_id, language)

async def get_chat_language(chat_id: int) -> str:
    return await get_default_db().get_chat_language(chat_id)

async def ban_user(user_id: int, reason: str = "") -> bool:
    return await get_default_db().ban_user(user_id, reason)

async def unban_user(user_id: int) -> bool:
    return await get_default_db().unban_user(user_id)

async def is_user_banned(user_id: int) -> bool:
    return await get_default_db().is_user_banned(user_id)

async def adjust_user_xp(user_id: int, xp: int) -> int:
    return await get_default_db().adjust_user_xp(user_id, xp)

async def get_admin_dashboard_stats() -> Dict[str, Any]:
    return await get_default_db().get_admin_dashboard_stats()

async def get_admin_users(query: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return await get_default_db().get_admin_users(query, limit, offset)

async def get_admin_user_detail(user_id: int) -> Optional[Dict[str, Any]]:
    return await get_default_db().get_admin_user_detail(user_id)

async def get_admin_groups(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return await get_default_db().get_admin_groups(limit, offset)

async def get_admin_answers(limit: int = 50) -> Dict[str, Any]:
    return await get_default_db().get_admin_answers(limit)

async def log_answer(user_id: int, chat_id: Optional[int], question_text: str, user_answer: str, correct_answer: str, is_correct: bool):
    return await get_default_db().log_answer(user_id, chat_id, question_text, user_answer, correct_answer, is_correct)

async def record_answer_log(
    user_id: int,
    username: Optional[str] = None,
    chat_id: Optional[int] = None,
    mode: Optional[str] = None,
    question_id: Optional[str] = None,
    question_text: Optional[str] = None,
    selected_option: Optional[str] = None,
    correct_option: Optional[str] = None,
    is_correct: bool | int = False,
    points: int = 0,
    time_taken: float = 0.0
) -> int:
    return await get_default_db().record_answer_log(
        user_id=user_id,
        username=username,
        chat_id=chat_id,
        mode=mode,
        question_id=question_id,
        question_text=question_text,
        selected_option=selected_option,
        correct_option=correct_option,
        is_correct=is_correct,
        points=points,
        time_taken=time_taken
    )

async def search_users(query: str = "", limit: int = 50, offset: int = 0) -> SearchUsersResult:
    return await get_default_db().search_users(query=query, limit=limit, offset=offset)

async def get_user_detail(user_id: int) -> Optional[Dict[str, Any]]:
    return await get_default_db().get_user_detail(user_id)

async def get_chat_list(limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
    return await get_default_db().get_chat_list(limit=limit, offset=offset)

async def get_recent_answer_logs(limit: int = 50, offset: int = 0, user_id: Optional[int] = None) -> List[Dict[str, Any]]:
    return await get_default_db().get_recent_answer_logs(limit=limit, offset=offset, user_id=user_id)

async def get_difficult_questions(limit: int = 20) -> List[Dict[str, Any]]:
    return await get_default_db().get_difficult_questions(limit=limit)

async def get_all_broadcast_recipients(target: str = "all") -> List[int]:
    return await get_default_db().get_all_broadcast_recipients(target)

async def record_admin_login(user_id: int, username: str = "", ip: str = "", user_agent: str = "", auth_method: str = "otp") -> int:
    return await get_default_db().record_admin_login(user_id, username, ip, user_agent, auth_method)

async def get_recent_admin_logins(limit: int = 50) -> List[Dict[str, Any]]:
    return await get_default_db().get_recent_admin_logins(limit)

async def get_recent_users(limit: int = 50) -> List[Dict[str, Any]]:
    return await get_default_db().get_recent_users(limit)

async def adjust_user_score(user_id: int, points: int) -> int:
    return await get_default_db().adjust_user_score(user_id, points)

async def set_user_level(user_id: int, level: int) -> int:
    return await get_default_db().set_user_level(user_id, level)

async def reset_user_stats(user_id: int) -> bool:
    return await get_default_db().reset_user_stats(user_id)

async def get_user_full_profile(user_id: int) -> Optional[Dict[str, Any]]:
    return await get_default_db().get_user_full_profile(user_id)


async def adjust_user_points(user_id: int, points: int) -> int:
    return await get_default_db().adjust_user_points(user_id, points)

async def set_user_level(user_id: int, level: int) -> int:
    return await get_default_db().set_user_level(user_id, level)

async def reset_user_stats(user_id: int) -> bool:
    return await get_default_db().reset_user_stats(user_id)

async def record_admin_login(user_id: int, username: str = "", ip: str = "", user_agent: str = "", auth_method: str = "OTP") -> int:
    return await get_default_db().record_admin_login(user_id, username, ip, user_agent, auth_method)

async def get_admin_logins(limit: int = 50) -> List[Dict[str, Any]]:
    return await get_default_db().get_admin_logins(limit)

async def get_recent_users(limit: int = 50) -> List[Dict[str, Any]]:
    return await get_default_db().get_recent_users(limit)

async def get_user_full_profile(user_id: int) -> Optional[Dict[str, Any]]:
    return await get_default_db().get_user_full_profile(user_id)

async def get_answers_history(query: Optional[str] = None, mode: Optional[str] = None, correct: Optional[str] = None, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    return await get_default_db().get_answers_history(query, mode, correct, limit, offset)


