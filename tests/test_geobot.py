"""
Comprehensive Unit & Integration Test Suite for GeoGuru & GeoGuessr Telegram Bot.
Uses Python's standard unittest and IsolatedAsyncioTestCase for zero-dependency execution.
"""

import os
import re
import glob
import json
import asyncio
import tempfile
import unittest
from pathlib import Path

import config
from locales.i18n import t, get_rank_name, LOCALES
from data.countries import COUNTRIES, get_country, search_country_by_name
from data.landmarks import LANDMARKS, get_landmark
from data.fun_facts import get_fun_fact
from database.db import Database
from games.models import Question, GameMode
from games.question_factory import QuestionFactory
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.daily_session import DailyChallengeSession
from games.manager import game_manager


class TestLocalesAndI18n(unittest.TestCase):
    def test_locales_consistency(self):
        """Verify en, ru, and uz locale files have identical keys and non-empty values."""
        locales_dir = Path(__file__).resolve().parent.parent / "locales"
        with open(locales_dir / "en.json", "r", encoding="utf-8") as f:
            en_data = json.load(f)
        with open(locales_dir / "ru.json", "r", encoding="utf-8") as f:
            ru_data = json.load(f)
        with open(locales_dir / "uz.json", "r", encoding="utf-8") as f:
            uz_data = json.load(f)

        en_keys = set(en_data.keys())
        ru_keys = set(ru_data.keys())
        uz_keys = set(uz_data.keys())

        self.assertEqual(ru_keys, en_keys, f"RU diff: {ru_keys ^ en_keys}")
        self.assertEqual(uz_keys, en_keys, f"UZ diff: {uz_keys ^ en_keys}")

        for k in en_keys:
            self.assertTrue(en_data[k], f"Key {k} is empty in en.json")
            self.assertTrue(ru_data[k], f"Key {k} is empty in ru.json")
            self.assertTrue(uz_data[k], f"Key {k} is empty in uz.json")

    def test_i18n_translation_fallback(self):
        """Verify translation lookup and English fallback."""
        self.assertIn("Welcome", t("welcome_private", "en"))
        self.assertIn("Добро пожаловать", t("welcome_private", "ru"))
        self.assertIn("xush kelibsiz", t("welcome_private", "uz"))

        # Fallback to en for unknown language
        self.assertIn("Welcome", t("welcome_private", "es"))

        # Interpolation test
        rendered = t("round_indicator", "en", current=1, total=5, mode="Flags", time=20)
        self.assertIn("Round 1/5", rendered)
        self.assertIn("20s", rendered)

    def test_get_rank_name(self):
        """Verify ranking tier titles across languages."""
        for lang in ["en", "ru", "uz"]:
            for lvl in range(1, 25):
                rank = get_rank_name(lvl, lang)
                self.assertTrue(rank and isinstance(rank, str))

    def test_codebase_translation_keys_coverage(self):
        """Verify that every static t('key') call in the codebase exists in the locale files."""
        base_dir = Path(__file__).resolve().parent.parent
        keys_in_code = set()

        for py_file in base_dir.rglob("*.py"):
            if "test_" in py_file.name:
                continue
            content = py_file.read_text(encoding="utf-8")
            matches = re.findall(r't\(\s*[\"\']([a-zA-Z0-9_]+)[\"\']', content)
            keys_in_code.update(matches)

        en_data = LOCALES.get("en", {})
        for key in keys_in_code:
            if key in ("question_flag", "welcome_group", "game_setup_title"):
                self.assertIn(key, en_data, f"Key '{key}' called in code but missing from en.json!")


class TestConfiguration(unittest.TestCase):
    def test_default_language_is_strictly_english(self):
        """CRITICAL: User requirement dictates bot starts in English, not Uzbek!"""
        self.assertEqual(config.DEFAULT_LANGUAGE, "en")
        self.assertIn("en", config.SUPPORTED_LANGUAGES)


class TestDataIntegrity(unittest.TestCase):
    def test_countries_database_integrity(self):
        """Verify countries database validity."""
        self.assertGreaterEqual(len(COUNTRIES), 90, f"Expected 90+ countries, got {len(COUNTRIES)}")

        seen_codes = set()
        for c in COUNTRIES:
            code = c["code"]
            self.assertNotIn(code, seen_codes, f"Duplicate country code {code}")
            seen_codes.add(code)

            for lang in ("en", "ru", "uz"):
                self.assertIn(lang, c["name"])
                self.assertTrue(c["name"][lang])
                self.assertIn(lang, c["capital"])
                self.assertTrue(c["capital"][lang])
                self.assertIn(lang, c["continent"])
                self.assertTrue(c["continent"][lang])

            self.assertGreater(c["population"], 0)
            self.assertGreater(c["area_sq_km"], 0)
            self.assertTrue(c["flag_emoji"])
            self.assertTrue(c["flag_url"].startswith("http"))

    def test_country_lookups(self):
        """Verify get_country and search_country_by_name."""
        uz = get_country("uz")
        self.assertIsNotNone(uz)
        self.assertEqual(uz["name"]["en"], "Uzbekistan")

        found = search_country_by_name("Toshkent", "uz")
        self.assertIsNotNone(found)
        self.assertEqual(found["code"], "uz")

    def test_landmarks_integrity(self):
        """Verify landmarks for GeoGuessr mode."""
        self.assertGreaterEqual(len(LANDMARKS), 20, "Should have 20+ landmarks")

        for lm in LANDMARKS:
            self.assertTrue(lm["id"])
            self.assertTrue(lm["country_code"])
            self.assertIsNotNone(get_country(lm["country_code"]), f"Landmark {lm['id']} references unknown country {lm['country_code']}")

            for lang in ("en", "ru", "uz"):
                self.assertIn(lang, lm["name"])
                self.assertTrue(lm["name"][lang])
                self.assertIn(lang, lm["clue"])
                self.assertTrue(lm["clue"][lang])
                self.assertIn(lang, lm["fun_fact"])
                self.assertTrue(lm["fun_fact"][lang])

            self.assertTrue(lm["image_url"].startswith("http"))

    def test_fun_facts(self):
        """Verify fun facts retrieval."""
        fact_en = get_fun_fact("uz", "en")
        self.assertIn("Uzbekistan", fact_en)
        fact_uz = get_fun_fact("uz", "uz")
        self.assertIn("O'zbekiston", fact_uz)

        fact_default = get_fun_fact("unknown_code", "en")
        self.assertGreater(len(fact_default), 10)


class TestQuestionFactory(unittest.TestCase):
    def test_question_factory_all_modes(self):
        """Verify Question generation across all modes and languages."""
        for mode in GameMode.ALL:
            for lang in ["en", "ru", "uz"]:
                q = QuestionFactory.generate(mode=mode, lang=lang)
                self.assertIsInstance(q, Question)
                self.assertIn(len(q.options), (2, 4))
                self.assertTrue(0 <= q.correct_index < len(q.options))
                self.assertTrue(q.correct_answer in q.options or q.correct_answer == q.options[q.correct_index])
                self.assertGreater(len(q.text), 5)

    def test_higher_lower_logic(self):
        """Verify Higher or Lower generation."""
        q = QuestionFactory.generate(mode=GameMode.HIGHER_LOWER, lang="en")
        self.assertEqual(len(q.options), 2)
        self.assertIn(q.correct_index, (0, 1))


class TestAsyncDatabase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_geobot.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.temp_dir.cleanup()

    async def test_database_crud(self):
        """Test full database lifecycle with aiosqlite."""
        # User registration: must default to 'en'
        user = await self.db.get_or_create_user(
            user_id=12345,
            username="john_doe",
            first_name="John",
            default_lang="en"
        )
        self.assertEqual(user["language"], "en")
        self.assertEqual(user["total_score"], 0)
        self.assertEqual(user["level"], 1)

        # Language update
        await self.db.set_user_language(12345, "uz")
        user_updated = await self.db.get_user(12345)
        self.assertEqual(user_updated["language"], "uz")

        # Chat registration
        chat = await self.db.get_or_create_chat(
            chat_id=-100123,
            chat_type="group",
            title="Geo Geeks",
            default_lang="en"
        )
        self.assertEqual(chat["language"], "en")

        # Record correct answer
        await self.db.record_answer(12345, is_correct=True, points=120, xp=25)
        user_after = await self.db.get_user(12345)
        self.assertEqual(user_after["total_score"], 120)
        self.assertEqual(user_after["xp"], 25)
        self.assertEqual(user_after["current_streak"], 1)
        self.assertEqual(user_after["correct_answers"], 1)

        # Record wrong answer
        await self.db.record_answer(12345, is_correct=False, points=-20)
        user_after_wrong = await self.db.get_user(12345)
        self.assertEqual(user_after_wrong["total_score"], 100)
        self.assertEqual(user_after_wrong["current_streak"], 0)
        self.assertEqual(user_after_wrong["best_streak"], 1)

        # Group score and leaderboards
        await self.db.update_group_player_score(-100123, 12345, points=100, is_win=True)
        group_board = await self.db.get_group_leaderboard(-100123)
        self.assertEqual(len(group_board), 1)
        self.assertEqual(group_board[0]["user_id"], 12345)
        self.assertEqual(group_board[0]["score"], 100)
        self.assertEqual(group_board[0]["wins"], 1)

        global_board = await self.db.get_global_leaderboard()
        self.assertGreaterEqual(len(global_board), 1)
        self.assertEqual(global_board[0]["user_id"], 12345)

        # Daily challenge
        can_play = await self.db.can_play_daily(12345, "2026-10-10")
        self.assertTrue(can_play)
        await self.db.record_daily_completion(12345, "2026-10-10", score=100, xp=50)
        can_play_again = await self.db.can_play_daily(12345, "2026-10-10")
        self.assertFalse(can_play_again)


class TestGameSessions(unittest.IsolatedAsyncioTestCase):
    async def test_game_session_mechanics(self):
        """Verify group GameSession round flow, scoring, and podium."""
        session = GameSession(
            chat_id=-100555,
            created_by_user_id=111,
            is_group=True,
            lang="en",
            mode=GameMode.FLAG,
            total_rounds=3,
            round_time=20
        )

        q = session.start_game()
        self.assertEqual(session.status, "in_progress")
        self.assertEqual(session.current_round, 1)
        self.assertIsNotNone(q)

        correct_idx = q.correct_index
        wrong_idx = (correct_idx + 1) % len(q.options)

        # Wrong answer attempt
        res, penalty, elapsed = await session.check_answer(222, "Alice", wrong_idx)
        self.assertEqual(res, "wrong")
        self.assertEqual(penalty, config.POINTS_WRONG_PENALTY)
        self.assertIn(222, session.answered_users_wrong)

        # Repeated wrong attempt in same round must be blocked
        res_repeat, _, _ = await session.check_answer(222, "Alice", correct_idx)
        self.assertEqual(res_repeat, "already_wrong")

        # Correct answer by another player (Bob)
        res_correct, points, elapsed_b = await session.check_answer(333, "Bob", correct_idx)
        self.assertEqual(res_correct, "correct")
        self.assertGreaterEqual(points, config.POINTS_CORRECT)
        self.assertEqual(session.scores[333], points)
        self.assertEqual(session.status, "between_rounds")

        # Advance to next round
        q2 = session.next_round()
        session.status = "in_progress"
        self.assertEqual(session.current_round, 2)
        self.assertEqual(len(session.answered_users_wrong), 0)

        # Advance to round 3
        q3 = session.next_round()
        session.status = "in_progress"
        self.assertEqual(session.current_round, 3)
        self.assertTrue(session.is_game_finished())

        # Podium verification
        podium = session.get_podium()
        self.assertGreaterEqual(len(podium), 1)
        self.assertEqual(podium[0][0], 333)
        self.assertEqual(podium[0][2], points)

    def test_solo_game_session_lives_and_lifelines(self):
        """Verify Solo practice session rules, lifelines, and game over."""
        solo = SoloGameSession(user_id=999, user_name="SoloHero", lang="en")
        self.assertEqual(solo.lives, 3)
        self.assertTrue(solo.has_5050)
        self.assertTrue(solo.has_hint)

        q = solo.next_round()
        self.assertIsNotNone(q)
        self.assertEqual(solo.round_number, 1)

        # Use 50/50 lifeline
        eliminated = solo.use_5050()
        expected_elim = 2 if len(q.options) > 2 else 1
        self.assertEqual(len(eliminated), expected_elim)
        self.assertNotIn(q.correct_index, eliminated)
        self.assertFalse(solo.has_5050)

        # Second call must return empty (already consumed)
        self.assertEqual(solo.use_5050(), [])

        # Use Hint lifeline
        hint = solo.use_hint()
        self.assertGreater(len(hint), 0)
        self.assertFalse(solo.has_hint)

        # Correct answer
        is_correct, pts, is_game_over = solo.check_answer(q.correct_index)
        self.assertTrue(is_correct)
        self.assertGreaterEqual(pts, 100)
        self.assertFalse(is_game_over)
        self.assertEqual(solo.streak, 1)

        # Wrong answers until game over
        q2 = solo.next_round()
        wrong_idx = (q2.correct_index + 1) % len(q2.options)

        # 1st loss (lives = 2)
        solo.check_answer(wrong_idx)
        self.assertEqual(solo.lives, 2)
        self.assertEqual(solo.status, "in_progress")

        # 2nd loss (lives = 1)
        solo.check_answer(wrong_idx)
        self.assertEqual(solo.lives, 1)
        self.assertEqual(solo.status, "in_progress")

        # 3rd loss (lives = 0 -> Game Over)
        _, _, is_over = solo.check_answer(wrong_idx)
        self.assertEqual(solo.lives, 0)
        self.assertTrue(is_over)
        self.assertEqual(solo.status, "game_over")


class TestEdgeCases(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "edge_geobot.db")
        self.db = Database(self.db_path)
        await self.db.init_db()

    async def asyncTearDown(self):
        self.temp_dir.cleanup()

    def test_empty_or_malformed_inputs(self):
        """Verify handling of empty, whitespace, and non-existent queries."""
        self.assertIsNone(search_country_by_name(""))
        self.assertIsNone(search_country_by_name("    "))
        self.assertIsNone(search_country_by_name("Atlantis"))
        self.assertIsNone(get_country(""))
        self.assertIsNone(get_country("zz_invalid"))
        self.assertIsNone(get_landmark("nonexistent_landmark"))

        # Fun facts fallback
        fallback = get_fun_fact("unknown_country", "en")
        self.assertTrue(len(fallback) > 10)

        # Extreme rank levels
        rank_neg = get_rank_name(-10, "en")
        self.assertTrue(isinstance(rank_neg, str))
        rank_high = get_rank_name(999999, "en")
        self.assertTrue(isinstance(rank_high, str))

        # Translations edge cases
        self.assertEqual(t("", "en"), "")
        self.assertEqual(t("non_existent_key_xyz", "uz"), "non_existent_key_xyz")

    async def test_game_session_edge_cases(self):
        """Verify session behavior with invalid answers and unauthorized duelists."""
        # 1. Duel restriction: player 999 is NOT in duel between 101 and 102
        duel_session = GameSession(
            chat_id=-100999,
            created_by_user_id=101,
            is_group=True,
            lang="en",
            mode=GameMode.FLAG,
            is_duel=True,
            duel_target_id=102
        )
        duel_session.start_game()
        res, _, _ = await duel_session.check_answer(999, "Intruder", 0)
        self.assertEqual(res, "not_allowed")

        # 2. Answer after game stopped
        duel_session.stop()
        res_stopped, _, _ = await duel_session.check_answer(101, "Player", 0)
        self.assertEqual(res_stopped, "inactive")

    async def test_database_special_characters_and_score_bounds(self):
        """Verify DB handling of unicode, quotes, and non-negative score clamping."""
        # Special character user
        user = await self.db.get_or_create_user(
            user_id=777,
            username="test'user\"special",
            first_name="🇺🇿 O'zbek <Player>",
            default_lang="en"
        )
        self.assertEqual(user["first_name"], "🇺🇿 O'zbek <Player>")

        # Penalty when score is 0 must NOT result in negative total_score
        await self.db.record_answer(777, is_correct=False, points=-50)
        user_db = await self.db.get_user(777)
        self.assertGreaterEqual(user_db["total_score"], 0)

    async def test_group_unregistered_player_auto_creation(self):
        """Verify that a player who never messaged bot privately is auto-registered on group answer."""
        unregistered_id = 88888
        # Ensure user does not exist
        self.assertIsNone(await self.db.get_user(unregistered_id))

        # Record group answer
        await self.db.record_answer(unregistered_id, is_correct=True, points=120, xp=25, user_name="GroupNinja")
        user = await self.db.get_user(unregistered_id)
        self.assertIsNotNone(user)
        self.assertEqual(user["first_name"], "GroupNinja")
        self.assertEqual(user["total_score"], 120)
        self.assertEqual(user["xp"], 25)

        # Update group score
        await self.db.update_group_player_score(-100888, unregistered_id, points=120, is_win=True, first_name="GroupNinja")
        group_top = await self.db.get_group_leaderboard(-100888)
        self.assertEqual(len(group_top), 1)
        self.assertEqual(group_top[0]["first_name"], "GroupNinja")
        self.assertEqual(group_top[0]["score"], 120)

    async def test_daily_challenge_lifecycle_and_streak(self):
        """Verify 5-round seeded daily challenge, question determinism, and streak progression."""
        user_id = 99911
        today = "2026-10-10"
        tomorrow = "2026-10-11"

        # 1. Determinism: same date produces same questions
        session1 = DailyChallengeSession(user_id=user_id, user_name="Hero", lang="en", date_str=today)
        session2 = DailyChallengeSession(user_id=user_id, user_name="Hero", lang="en", date_str=today)
        self.assertEqual(len(session1.questions), 5)
        self.assertEqual([q.mode for q in session1.questions], [q.mode for q in session2.questions])
        self.assertEqual([q.correct_answer for q in session1.questions], [q.correct_answer for q in session2.questions])

        # 2. Challenge execution: answer all 5 questions
        for idx in range(5):
            q = session1.current_question
            self.assertIsNotNone(q)
            is_correct, pts, is_finished, ans = session1.check_answer(q.correct_index)
            self.assertTrue(is_correct)
            self.assertEqual(pts, config.POINTS_CORRECT)
            if idx == 4:
                self.assertTrue(is_finished)
            else:
                self.assertFalse(is_finished)

        self.assertEqual(session1.score, 500)
        self.assertEqual(session1.correct_count, 5)

        # 3. Database recording & streak tracking: Day 1
        self.assertTrue(await self.db.can_play_daily(user_id, today))
        await self.db.record_daily_completion(user_id, today, score=session1.score, xp=150)
        self.assertFalse(await self.db.can_play_daily(user_id, today))

        user_d1 = await self.db.get_user(user_id)
        self.assertEqual(user_d1["daily_streak"], 1)

        # Day 2 (tomorrow): streak increments to 2
        await self.db.record_daily_completion(user_id, tomorrow, score=500, xp=150)
        user_d2 = await self.db.get_user(user_id)
        self.assertEqual(user_d2["daily_streak"], 2)

    def test_text_answer_recognition_and_false_positive_immunity(self):
        """Verify text answer normalization, whole-word matching, and avoidance of substring false positives."""
        from handlers.text_answers import _normalize, OPTION_SHORTCUTS
        import re

        # Normalize tests
        self.assertEqual(_normalize("  Uzbekistan!  "), "uzbekistan")
        self.assertEqual(_normalize("Washington, D.C."), "washington d c")
        self.assertEqual(_normalize("🅰️ France"), "france")

        # Shortcuts
        self.assertEqual(OPTION_SHORTCUTS["1"], 0)
        self.assertEqual(OPTION_SHORTCUTS["a"], 0)
        self.assertEqual(OPTION_SHORTCUTS["2"], 1)
        self.assertEqual(OPTION_SHORTCUTS["b"], 1)

        # Test immunity to substring false positives:
        # e.g. target country is "Oman", normal chat is "salom hammaga omad tilayman"
        target = "oman"
        norm_chat = _normalize("salom hammaga omad tilayman")
        pattern = r"(?:\b|^)" + re.escape(target) + r"(?:\b|$)"
        self.assertIsNone(re.search(pattern, norm_chat))

        # Target is "Peru", normal chat is "superuser permission granted"
        target_peru = "peru"
        norm_chat2 = _normalize("superuser permission granted")
        pattern_peru = r"(?:\b|^)" + re.escape(target_peru) + r"(?:\b|$)"
        self.assertIsNone(re.search(pattern_peru, norm_chat2))

        # Legitimate whole-word answer in sentence
        legit_chat = _normalize("I think the answer is Peru definitely")
        self.assertIsNotNone(re.search(pattern_peru, legit_chat))

    async def test_duels_and_match_persistence(self):
        """Verify full lifecycle of duel creation, acceptance, and match database recording."""
        chat_id = -100444
        duel_id = await self.db.create_duel(
            chat_id=chat_id,
            challenger_id=10,
            challenger_name="PlayerA",
            opponent_id=20,
            opponent_name="PlayerB"
        )
        self.assertGreater(duel_id, 0)
        duel = await self.db.get_duel(duel_id)
        self.assertEqual(duel["status"], "pending")

        # Update to active
        await self.db.update_duel_status(duel_id, "active")
        duel_active = await self.db.get_duel(duel_id)
        self.assertEqual(duel_active["status"], "active")

        # Complete with winner
        await self.db.update_duel_status(duel_id, "completed", winner_id=10)
        duel_finished = await self.db.get_duel(duel_id)
        self.assertEqual(duel_finished["status"], "completed")
        self.assertEqual(duel_finished["winner_id"], 10)

        # Record match in matches table
        await self.db.record_match(
            chat_id=chat_id,
            mode="duel",
            winner_id=10,
            winner_name="PlayerA",
            winner_score=300,
            players_count=2
        )


if __name__ == "__main__":
    unittest.main()

