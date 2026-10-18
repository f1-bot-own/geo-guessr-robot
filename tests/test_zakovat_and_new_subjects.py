"""
Unit and integration tests for Zakovat and 7 new multidisciplinary subjects.
Verifies all 3,300 questions, QuestionFactory generation, i18n, and keyboard integration.
"""

import unittest
from games.models import GameMode, Question
from games.question_factory import QuestionFactory
from gamedata import (
    ZAKOVAT_QUESTIONS,
    ASTRONOMY_QUESTIONS,
    SCIENCE_QUESTIONS,
    HISTORY_DATA,
    LITERATURE_DATA,
    ART_DATA,
    NATURE_DATA,
    LOGIC_MATH_DATA
)
from keyboards.game_kb import get_setup_kb, get_solo_setup_kb, get_category_selection_kb
from locales.i18n import t

class TestZakovatAndNewSubjects(unittest.TestCase):

    def test_dataset_counts_and_integrity(self):
        """Verify that all 3,300 curated questions exist with valid structure."""
        datasets = [
            ("zakovat", ZAKOVAT_QUESTIONS, 500),
            ("astronomy", ASTRONOMY_QUESTIONS, 400),
            ("science", SCIENCE_QUESTIONS, 400),
            ("history", HISTORY_DATA, 400),
            ("literature", LITERATURE_DATA, 400),
            ("art", ART_DATA, 400),
            ("nature", NATURE_DATA, 400),
            ("logic_math", LOGIC_MATH_DATA, 400)
        ]

        total_questions = 0
        for name, data, expected_count in datasets:
            self.assertEqual(
                len(data),
                expected_count,
                f"Dataset {name} should have {expected_count} items, found {len(data)}"
            )
            total_questions += len(data)

            # Spot check 10 items per dataset
            for item in data[:10]:
                self.assertIn("id", item)
                self.assertIn("question", item)
                self.assertIn("options", item)
                self.assertIn("correct_answer", item)

                # Check 3 languages
                for lang in ("uz", "ru", "en"):
                    self.assertIn(lang, item["question"], f"Missing {lang} in {item['id']}")
                    self.assertTrue(len(item["question"][lang].strip()) > 0)
                    self.assertIn(lang, item["options"], f"Missing {lang} options in {item['id']}")
                    options = item["options"][lang]
                    self.assertEqual(len(options), 4, f"{item['id']} {lang} must have 4 options")
                    self.assertEqual(len(set(options)), 4, f"{item['id']} {lang} has duplicate options: {options}")

                    # Verify correct answer matches options
                    corr = item["correct_answer"].get(lang)
                    if corr:
                        self.assertIn(corr, options, f"Correct answer '{corr}' not in options {options} for {item['id']}")

        self.assertEqual(total_questions, 3300)

    def test_zakovat_sub_types(self):
        """Verify Zakovat subcategories: black_box, deduction, world_intellect, blitz."""
        types = [q.get("type") or q.get("sub_mode") for q in ZAKOVAT_QUESTIONS]
        self.assertGreaterEqual(types.count("black_box"), 100)
        self.assertGreaterEqual(types.count("deduction"), 100)
        self.assertGreaterEqual(types.count("world_intellect"), 100)
        self.assertGreaterEqual(types.count("blitz"), 100)

    def test_question_factory_generation_for_all_modes(self):
        """Verify QuestionFactory generates questions without error for each mode in all languages."""
        modes = [
            GameMode.ZAKOVAT,
            GameMode.ASTRONOMY,
            GameMode.SCIENCE,
            GameMode.HISTORY,
            GameMode.LITERATURE,
            GameMode.ART,
            GameMode.NATURE,
            GameMode.LOGIC_MATH
        ]

        for mode in modes:
            for lang in ("uz", "ru", "en"):
                q = QuestionFactory.generate(mode=mode, lang=lang)
                self.assertIsInstance(q, Question, f"Failed to generate {mode} for {lang}")
                self.assertEqual(q.mode, mode)
                self.assertTrue(len(q.text) > 0, f"Question text empty for {mode} in {lang}")
                self.assertEqual(len(q.options), 4, f"Options not 4 for {mode} in {lang}")
                self.assertEqual(len(set(q.options)), 4, f"Duplicate options in {mode} for {lang}")
                self.assertIn(
                    q.correct_answer,
                    q.options,
                    f"Correct answer '{q.correct_answer}' not in options {q.options} for {mode} in {lang}"
                )
                self.assertEqual(q.options[q.correct_index], q.correct_answer)

    def test_black_box_flag(self):
        """Verify black box questions have is_black_box set to True."""
        bb_q = QuestionFactory.generate(mode=GameMode.ZAKOVAT, lang="uz", sub_mode="black_box")
        self.assertTrue(bb_q.is_black_box)

    def test_keyboards_contain_new_modes(self):
        """Verify setup keyboards render buttons for the new modes."""
        kb_setup = get_setup_kb(session_id="test_sess", lang="uz", view_mode="detailed")
        button_texts = [btn.text for row in kb_setup.inline_keyboard for btn in row]

        # Check category hubs view too
        kb_hubs = get_setup_kb(session_id="test_sess", lang="uz", view_mode="categories")
        hub_texts = [btn.text for row in kb_hubs.inline_keyboard for btn in row]
        self.assertTrue(any("Zakovat" in text for text in hub_texts))
        self.assertTrue(any("Geografiya" in text for text in hub_texts))

        # Check for presence of Zakovat and subjects
        self.assertTrue(any("Zakovat" in text for text in button_texts))
        self.assertTrue(any("Astronomiya" in text for text in button_texts))
        self.assertTrue(any("Kimyo" in text for text in button_texts))
        self.assertTrue(any("Tarix" in text for text in button_texts))
        self.assertTrue(any("Adabiyot" in text for text in button_texts))
        self.assertTrue(any("San'at" in text for text in button_texts))
        self.assertTrue(any("Tabiat" in text for text in button_texts))
        self.assertTrue(any("Mantiq" in text for text in button_texts))

        # Check solo setup
        kb_solo = get_solo_setup_kb(lang="en")
        solo_texts = [btn.text for row in kb_solo.inline_keyboard for btn in row]
        self.assertTrue(any("Zakovat" in text for text in solo_texts))
        self.assertTrue(any("Astronomy" in text for text in solo_texts))

        # Check category selection
        kb_cat = get_category_selection_kb(lang="ru")
        cat_texts = [btn.text for row in kb_cat.inline_keyboard for btn in row]
        self.assertTrue(any("Заковат" in text for text in cat_texts))
        self.assertTrue(any("Космос" in text for text in cat_texts))

    def test_mix_mode_includes_all_new_subjects(self):
        """Verify MIX mode can sample from new modes as well as geography."""
        sampled_modes = set()
        for _ in range(120):
            q = QuestionFactory.generate(mode=GameMode.MIX, lang="uz")
            sampled_modes.add(q.mode)

        self.assertIn(GameMode.ZAKOVAT, sampled_modes)
        self.assertGreater(len(sampled_modes), 5)

    def test_category_overview_text(self):
        """Verify get_category_overview_text returns structured category counts and sub-modes."""
        from keyboards.game_kb import get_category_overview_text
        for lang in ("uz", "ru", "en"):
            overview = get_category_overview_text(lang)
            self.assertIn("6", overview)
            self.assertIn("Zakovat" if lang != "ru" else "Заковат", overview)
            self.assertIn("4,000", overview)

        # Specific hub headers
        zako_hub = get_category_overview_text("uz", hub="zakovat")
        self.assertIn("Qora quti", zako_hub)
        self.assertIn("Deduksiya", zako_hub)
        self.assertIn("Jahon intellekti", zako_hub)
        self.assertIn("Blits", zako_hub)

    def test_hub_subcategories_keyboards(self):
        """Verify subcategory keyboards for all hubs contain proper buttons and back navigation."""
        from keyboards.game_kb import get_hub_subcategories_kb, CATEGORY_HUBS_INFO
        for hub_key in CATEGORY_HUBS_INFO:
            kb = get_hub_subcategories_kb(hub=hub_key, prefix="solo_cat", lang="uz")
            callbacks = [btn.callback_data for row in kb.inline_keyboard for btn in row]
            self.assertIn("solo_cat:hub:main", callbacks, f"Back button missing in hub {hub_key}")
            # Ensure at least 4 subcategory buttons
            self.assertGreaterEqual(len(callbacks), 5)

    def test_solo_session_submode_generation(self):
        """Verify SoloGameSession generates questions accurately for individual sub-modes."""
        from games.solo_session import SoloGameSession
        for sub_mode in ("black_box", "telescope_zoom", "elements", "quotes", "macro_texture", "flash_math"):
            session = SoloGameSession(
                user_id=12345,
                user_name="Tester",
                lang="uz",
                mode=sub_mode,
                selected_modes=[sub_mode]
            )
            q = session.next_round()
            self.assertIsNotNone(q)
            self.assertEqual(len(q.options), 4)
            self.assertIn(q.correct_answer, q.options)

if __name__ == "__main__":
    unittest.main()

