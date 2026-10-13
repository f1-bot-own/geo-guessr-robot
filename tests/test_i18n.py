"""
Unit tests for internationalization (i18n) module.
"""
import unittest
from locales.i18n import t, get_rank_name, LOCALES

class TestI18n(unittest.TestCase):

    def test_supported_languages_loaded(self):
        for lang in ["en", "ru", "uz"]:
            self.assertIn(lang, LOCALES)
            self.assertGreater(len(LOCALES[lang]), 10)

    def test_default_is_english(self):
        # Empty or None language should default to English
        res_default = t("welcome_private")
        res_en = t("welcome_private", "en")
        self.assertEqual(res_default, res_en)
        self.assertIn("Welcome to GeoGuru & GeoGuessr Bot", res_default)

    def test_translations_exist(self):
        keys_to_test = [
            "welcome_private",
            "welcome_group",
            "help_text",
            "game_setup_title",
            "game_over_title",
            "mode_flag",
            "mode_capital",
            "mode_landmark",
            "mode_higher_lower",
            "mode_coat_of_arms",
            "mode_mix"
        ]
        for lang in ["en", "ru", "uz"]:
            for key in keys_to_test:
                val = t(key, lang)
                self.assertNotEqual(val, key, f"Missing key {key} for lang {lang}")

    def test_formatting_parameters(self):
        msg = t("round_indicator", "en", current=1, total=5, mode="Flag Quiz", time=20)
        self.assertIn("Round 1/5", msg)
        self.assertIn("Flag Quiz", msg)
        self.assertIn("20s", msg)

    def test_ranks(self):
        for lang in ["en", "ru", "uz"]:
            r1 = get_rank_name(1, lang)
            r5 = get_rank_name(10, lang)
            r7 = get_rank_name(30, lang)
            self.assertTrue(len(r1) > 0)
            self.assertTrue(len(r5) > 0)
            self.assertTrue(len(r7) > 0)

if __name__ == "__main__":
    unittest.main()
