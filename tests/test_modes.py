"""
Unit tests for question generators across all game modes.
"""
import unittest
from game.modes import (
    generate_flag_question,
    generate_capital_question,
    generate_landmark_question,
    generate_higher_lower_question,
    generate_coat_of_arms_question,
    generate_streetview_question,
    generate_question
)

class TestGameModes(unittest.TestCase):

    def test_flag_question(self):
        q = generate_flag_question("en")
        self.assertEqual(q.mode, "flag")
        self.assertEqual(len(q.options), 4)
        correct_opts = [o for o in q.options if o.is_correct]
        self.assertEqual(len(correct_opts), 1)
        self.assertEqual(correct_opts[0].id, q.correct_option_id)
        self.assertIsNotNone(q.media_url)

    def test_capital_question(self):
        q = generate_capital_question("uz")
        self.assertEqual(q.mode, "capital")
        self.assertEqual(len(q.options), 4)
        correct_opts = [o for o in q.options if o.is_correct]
        self.assertEqual(len(correct_opts), 1)
        self.assertEqual(correct_opts[0].id, q.correct_option_id)

    def test_landmark_question(self):
        q = generate_landmark_question("ru")
        self.assertEqual(q.mode, "landmark")
        self.assertEqual(len(q.options), 4)
        correct_opts = [o for o in q.options if o.is_correct]
        self.assertEqual(len(correct_opts), 1)
        self.assertEqual(correct_opts[0].id, q.correct_option_id)
        self.assertIsNotNone(q.media_url)
        self.assertIsNotNone(q.hint_text)

    def test_higher_lower_question(self):
        q = generate_higher_lower_question("en")
        self.assertEqual(q.mode, "higher_lower")
        self.assertEqual(len(q.options), 2)
        correct_opts = [o for o in q.options if o.is_correct]
        self.assertEqual(len(correct_opts), 1)
        self.assertEqual(correct_opts[0].id, q.correct_option_id)
        self.assertIsNotNone(q.extra_info)

    def test_coat_of_arms_question(self):
        q = generate_coat_of_arms_question("en")
        self.assertEqual(q.mode, "coat_of_arms")
        self.assertEqual(len(q.options), 4)
        correct_opts = [o for o in q.options if o.is_correct]
        self.assertEqual(len(correct_opts), 1)
        self.assertEqual(correct_opts[0].id, q.correct_option_id)
        self.assertIsNotNone(q.media_url)

    def test_streetview_question(self):
        q = generate_streetview_question("en")
        self.assertEqual(q.mode, "streetview")
        self.assertEqual(len(q.options), 4)
        correct_opts = [o for o in q.options if o.is_correct]
        self.assertEqual(len(correct_opts), 1)
        self.assertEqual(correct_opts[0].id, q.correct_option_id)
        self.assertIsNotNone(q.media_url)
        self.assertIsNotNone(q.hint_text)
        self.assertIsNotNone(q.extra_info)
        self.assertIn("google.com/maps", q.extra_info)

    def test_mix_generator_robustness(self):
        for _ in range(40):
            q = generate_question("mix", "en")
            self.assertIn(q.mode, ["flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview"])
            self.assertGreaterEqual(len(q.options), 2)
            self.assertTrue(any(o.is_correct for o in q.options))

if __name__ == "__main__":
    unittest.main()
