"""
Unit tests for Game Engine & Logic Audit fixes:
1. Continent filter fallback & few/no item resilience across all game modes.
2. Guarantee of 4 unique options and correct_answer presence in QuestionFactory.
3. Fuzzy text answer matching across Cyrillic, Latin, and apostrophe/modifier variations.
4. SoloGameSession lifeline safety (duplicate 50/50 calls, hints on non-ISO questions).
5. GameSession & SoloGameSession next_round() resilience with empty or invalid selected_modes.
"""

import unittest
from games.models import GameMode, Question
from games.question_factory import QuestionFactory, _matches_continent, _find_country
from games.session import GameSession
from games.solo_session import SoloGameSession
from handlers.text_answers import _normalize, _compile_valid_correct, _text_matches_valid, to_latin


class TestContinentFilterResilience(unittest.TestCase):
    def test_oceania_and_africa_landmarks(self):
        """Oceania (1 landmark) and Africa (2 landmarks) must generate valid questions without crashing."""
        for cont in ("oceania", "africa"):
            for lang in ("en", "uz", "ru"):
                q = QuestionFactory.generate(mode=GameMode.LANDMARK, lang=lang, continent=cont)
                self.assertIsNotNone(q)
                self.assertEqual(len(q.options), 4)
                self.assertEqual(len(set(q.options)), 4, f"Duplicates found in options: {q.options}")
                self.assertIn(q.correct_answer, q.options)
                self.assertEqual(q.options[q.correct_index], q.correct_answer)

    def test_logo_empty_continents_fallback_gracefully(self):
        """Africa and Oceania have 0 logos; QuestionFactory must fallback gracefully without crashing."""
        for cont in ("africa", "oceania", "antarctica"):
            for lang in ("en", "uz", "ru"):
                q = QuestionFactory.generate(mode=GameMode.LOGO, lang=lang, continent=cont)
                self.assertIsNotNone(q)
                self.assertEqual(len(q.options), 4)
                self.assertEqual(len(set(q.options)), 4, f"Duplicates found in logo options: {q.options}")
                self.assertIn(q.correct_answer, q.options)
                self.assertEqual(q.options[q.correct_index], q.correct_answer)

    def test_president_and_celebrity_continent_filtering(self):
        """Presidents and celebrities must generate valid questions with 4 unique options for all continents."""
        for cont in ("asia", "europe", "americas", "africa", "oceania"):
            for mode in (GameMode.PRESIDENT, GameMode.CELEBRITY, GameMode.HISTORICAL):
                q = QuestionFactory.generate(mode=mode, lang="en", continent=cont)
                self.assertIsNotNone(q)
                self.assertEqual(len(q.options), 4)
                self.assertEqual(len(set(q.options)), 4, f"Duplicates in {mode} ({cont}): {q.options}")
                self.assertIn(q.correct_answer, q.options)
                self.assertEqual(q.options[q.correct_index], q.correct_answer)

    def test_streetview_emoji_contour_oceania(self):
        """Streetview, Emoji, Contour have <= 3 items in Oceania; must generate properly with 4 options."""
        for mode in (GameMode.STREETVIEW, GameMode.EMOJI, GameMode.CONTOUR, GameMode.COAT_OF_ARMS):
            q = QuestionFactory.generate(mode=mode, lang="uz", continent="oceania")
            self.assertIsNotNone(q)
            self.assertEqual(len(q.options), 4)
            self.assertEqual(len(set(q.options)), 4)
            self.assertIn(q.correct_answer, q.options)
            self.assertEqual(q.options[q.correct_index], q.correct_answer)


class TestQuestionFactoryFourUniqueOptions(unittest.TestCase):
    def test_all_modes_four_unique_options_and_correct_index(self):
        """Every 4-choice mode must strictly produce 4 unique options with valid correct_index."""
        four_choice_modes = [
            GameMode.FLAG, GameMode.CAPITAL, GameMode.LANDMARK, GameMode.COAT_OF_ARMS,
            GameMode.STREETVIEW, GameMode.EMOJI, GameMode.CONTOUR, GameMode.BLUR,
            GameMode.PRESIDENT, GameMode.HISTORICAL, GameMode.CELEBRITY, GameMode.PERSON,
            GameMode.LOGO
        ]
        for mode in four_choice_modes:
            for _ in range(5):
                q = QuestionFactory.generate(mode=mode, lang="en")
                self.assertEqual(len(q.options), 4, f"Mode {mode} options length != 4")
                self.assertEqual(len(set(q.options)), 4, f"Mode {mode} options contain duplicates: {q.options}")
                self.assertIn(q.correct_answer, q.options)
                self.assertEqual(q.options[q.correct_index], q.correct_answer)
                self.assertTrue(0 <= q.correct_index <= 3)

    def test_higher_lower_two_unique_options(self):
        """Higher/Lower mode must strictly produce 2 unique options."""
        for _ in range(10):
            q = QuestionFactory.generate(mode=GameMode.HIGHER_LOWER, lang="en")
            self.assertEqual(len(q.options), 2)
            self.assertEqual(len(set(q.options)), 2)
            self.assertIn(q.correct_answer, q.options)
            self.assertEqual(q.options[q.correct_index], q.correct_answer)


class TestFuzzyTextMatchingCyrillicLatinAndApostrophes(unittest.TestCase):
    def test_uzbekistan_variants_normalization_and_matching(self):
        """O'zbekiston, Ozbekiston, Ўзбекистон, Узбекистон, Uzbekistan must all match correctly."""
        q = QuestionFactory.generate(mode=GameMode.FLAG, lang="uz")
        # Force question to be Uzbekistan
        q.country_code = "uz"
        q.correct_answer = "O'zbekiston"
        q.options = ["O'zbekiston", "Tojikiston", "Qozog'iston", "Qirg'iziston"]
        q.correct_index = 0

        valid_answers = _compile_valid_correct(q)

        # Test various input spellings from Uzbek and Russian users
        test_inputs = [
            "O'zbekiston",
            "Ozbekiston",
            "ozbekiston",
            "O‘zbekiston",  # left single quote \u2018
            "O’zbekiston",  # right single quote \u2019
            "Oʻzbekiston",  # modifier letter turned comma \u02bb
            "Oʼzbekiston",  # modifier letter apostrophe \u02bc
            "O`zbekiston",  # grave accent
            "Ўзбекистон",   # Uzbek Cyrillic with Ў
            "ўзбекистон",
            "Узбекистон",   # Uzbek Cyrillic on Russian keyboard (У)
            "узбекистон",
            "Узбекистан",   # Russian Cyrillic
            "узбекистан",
            "Uzbekistan",   # English
            "uzbekistan",
        ]

        for inp in test_inputs:
            norm = _normalize(inp)
            matched = _text_matches_valid(norm, valid_answers)
            self.assertTrue(matched, f"Failed to match valid Uzbekistan input: '{inp}' (normalized: '{norm}')")

    def test_kazakhstan_and_tajikistan_cyrillic_matching(self):
        """Cyrillic forms like Қозоғистон, Тожикистон must match their country questions."""
        q_kz = Question(
            mode=GameMode.FLAG,
            text="",
            options=["Qozog'iston", "Rossiya", "Xitoy", "Turkiya"],
            correct_index=0,
            correct_answer="Qozog'iston",
            country_code="kz"
        )
        valid_kz = _compile_valid_correct(q_kz)
        for inp in ("Қозоғистон", "Казахстан", "Qozogiston", "Kazakhstan"):
            norm = _normalize(inp)
            self.assertTrue(_text_matches_valid(norm, valid_kz), f"Failed to match: {inp}")

    def test_apostrophe_normalization_equality(self):
        """Different Unicode apostrophes must normalize to the exact same string."""
        s1 = _normalize("O'zbekiston")
        s2 = _normalize("O‘zbekiston")
        s3 = _normalize("O’zbekiston")
        s4 = _normalize("Oʻzbekiston")
        s5 = _normalize("Oʼzbekiston")
        s6 = _normalize("Ozbekiston")
        self.assertEqual(s1, "ozbekiston")
        self.assertEqual(s1, s2)
        self.assertEqual(s1, s3)
        self.assertEqual(s1, s4)
        self.assertEqual(s1, s5)
        self.assertEqual(s1, s6)


class TestSoloSessionLifelines(unittest.TestCase):
    def test_use_5050_cannot_be_called_twice_in_same_round(self):
        """50/50 lifeline can only be used once per game session."""
        session = SoloGameSession(user_id=101, user_name="Alice")
        session.next_round()
        self.assertTrue(session.has_5050)

        first_call = session.use_5050()
        self.assertEqual(len(first_call), 2)
        self.assertFalse(session.has_5050)
        self.assertEqual(len(session.eliminated_options), 2)

        # Second call in the same round must return []
        second_call = session.use_5050()
        self.assertEqual(second_call, [])
        self.assertEqual(len(session.eliminated_options), 2)

    def test_use_5050_on_two_option_question(self):
        """50/50 on a 2-option question (like higher/lower) must safely return [] without eliminating the wrong option."""
        session = SoloGameSession(user_id=102, user_name="Bob")
        session.current_question = Question(
            mode=GameMode.HIGHER_LOWER,
            text="Compare",
            options=["🅰️ Country A", "🅱️ Country B"],
            correct_index=0,
            correct_answer="🅰️ Country A",
            country_code="us"
        )
        res = session.use_5050()
        self.assertEqual(res, [])
        self.assertEqual(len(session.eliminated_options), 0)

    def test_use_hint_on_questions_without_iso_code(self):
        """use_hint() on questions without an ISO code must provide a safe hint and not leak the answer."""
        modes_to_test = [
            (GameMode.HISTORICAL, "world", "Amir Temur"),
            (GameMode.PRESIDENT, "Uzbekistan", "Shavkat Mirziyoyev"),
            (GameMode.CELEBRITY, "Portugal", "Cristiano Ronaldo"),
            (GameMode.LOGO, "world", "Apple"),
        ]
        for mode, code, answer in modes_to_test:
            session = SoloGameSession(user_id=103, user_name="Charlie", lang="en")
            session.current_question = Question(
                mode=mode,
                text="Who is this?",
                options=[answer, "Distractor 1", "Distractor 2", "Distractor 3"],
                correct_index=0,
                correct_answer=answer,
                country_code=code,
                fun_fact=f"{answer} is a world famous figure."
            )
            hint = session.use_hint()
            self.assertTrue(hint and len(hint) > 0, f"Hint was empty for mode {mode}")
            self.assertFalse(session.has_hint)
            # Crucial: Hint must NOT leak the correct answer!
            self.assertNotIn(answer.lower(), hint.lower(), f"Hint leaked correct answer '{answer}' in mode {mode}!")

            # Second call to hint must return empty string
            second_hint = session.use_hint()
            self.assertEqual(second_hint, "")


class TestSessionSelectedModesResilience(unittest.TestCase):
    def test_game_session_next_round_with_empty_or_invalid_modes(self):
        """GameSession.next_round() must handle empty or invalid selected_modes gracefully."""
        invalid_cases = [
            [],
            ["invalid_mode"],
            ["unknown_1", "unknown_2"],
            ["mix"],
            ["blur"],
            ["mix", "blur"],
        ]
        for invalid_modes in invalid_cases:
            session = GameSession(
                chat_id=1001,
                selected_modes=invalid_modes,
                mode=GameMode.MIX
            )
            q = session.next_round()
            self.assertIsNotNone(q)
            self.assertIsInstance(q, Question)
            self.assertIn(q.mode, GameMode.ALL)
            self.assertGreaterEqual(len(q.options), 2)
            self.assertIn(q.correct_answer, q.options)

    def test_solo_session_next_round_with_empty_or_invalid_modes(self):
        """SoloGameSession.next_round() must handle empty or invalid selected_modes gracefully."""
        invalid_cases = [
            [],
            ["unknown_mode_xyz"],
            ["mix"],
            ["blur"],
        ]
        for invalid_modes in invalid_cases:
            session = SoloGameSession(
                user_id=1002,
                user_name="Player",
                selected_modes=invalid_modes,
                mode=GameMode.MIX
            )
            q = session.next_round()
            self.assertIsNotNone(q)
            self.assertIsInstance(q, Question)
            self.assertIn(q.mode, GameMode.ALL)
            self.assertGreaterEqual(len(q.options), 2)
            self.assertIn(q.correct_answer, q.options)


if __name__ == "__main__":
    unittest.main()
