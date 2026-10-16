"""
Tests for new game modes and 100+ dataset requirements:
- PRESIDENTS (>= 100)
- HISTORICAL_FIGURES (>= 100)
- CELEBRITIES (>= 100)
- LOGOS (>= 100)
- PERSON (Combined >= 300)
- QuestionFactory generation & text matching
"""

import unittest
from games.models import GameMode, Question
from games.question_factory import QuestionFactory
from gamedata import PRESIDENTS, HISTORICAL_FIGURES, CELEBRITIES, LOGOS
from handlers.text_answers import _normalize, _compile_valid_correct


class TestNewModesAndDatasets(unittest.TestCase):
    def test_dataset_minimum_100_counts(self):
        """Every requested category must have >= 100 high quality verified entries."""
        self.assertGreaterEqual(len(PRESIDENTS), 100, f"Presidents count {len(PRESIDENTS)} < 100")
        self.assertGreaterEqual(len(HISTORICAL_FIGURES), 100, f"Historical count {len(HISTORICAL_FIGURES)} < 100")
        self.assertGreaterEqual(len(CELEBRITIES), 100, f"Celebrities count {len(CELEBRITIES)} < 100")
        self.assertGreaterEqual(len(LOGOS), 100, f"Logos count {len(LOGOS)} < 100")

    def test_image_urls_non_empty(self):
        """All items must have valid image URLs."""
        for name, dataset in [
            ("Presidents", PRESIDENTS),
            ("Historical", HISTORICAL_FIGURES),
            ("Celebrities", CELEBRITIES),
            ("Logos", LOGOS),
        ]:
            for item in dataset:
                self.assertTrue(item.get("image_url"), f"Item missing image_url in {name}: {item.get('id')}")
                self.assertTrue(item["image_url"].startswith("http"), f"Invalid image_url in {name}: {item.get('image_url')}")

    def test_question_generation_for_all_modes_and_languages(self):
        """Test QuestionFactory generation for all 5 new modes across uz, ru, en."""
        modes = [
            GameMode.PRESIDENT,
            GameMode.HISTORICAL,
            GameMode.CELEBRITY,
            GameMode.PERSON,
            GameMode.LOGO,
        ]
        languages = ["uz", "ru", "en"]

        for mode in modes:
            for lang in languages:
                q = QuestionFactory.generate(mode=mode, lang=lang)
                self.assertIsNotNone(q, f"Question generation failed for mode {mode} and lang {lang}")
                self.assertIsInstance(q, Question)
                self.assertTrue(q.image_url, f"Missing image_url for mode {mode}")
                self.assertEqual(len(q.options), 4, f"Options count != 4 for mode {mode}")
                self.assertIn(q.correct_answer, q.options, f"Correct answer not in options for {mode}")
                self.assertTrue(q.aliases and len(q.aliases) > 0, f"Aliases empty for {mode}")

    def test_text_matching_aliases(self):
        """Test that chat answer matching recognizes aliases."""
        q = QuestionFactory.generate(mode=GameMode.PRESIDENT, lang="uz")
        valid_answers = _compile_valid_correct(q)
        self.assertGreater(len(valid_answers), 0)
        # The correct answer normalized should be recognized
        norm_ans = _normalize(q.correct_answer)
        self.assertIn(norm_ans, valid_answers)


if __name__ == "__main__":
    unittest.main()
