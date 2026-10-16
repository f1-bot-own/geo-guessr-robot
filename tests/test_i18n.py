"""
Unit tests for internationalization (i18n) module.
"""
import re
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

    def test_missing_formatting_arguments_does_not_raise(self):
        """Missing format parameters should not raise KeyError and should partially format available params."""
        # round_indicator requires: current, total, mode, time
        # Provide only 'current'
        msg = t("round_indicator", "en", current=1)
        self.assertIsInstance(msg, str)
        self.assertIn("Round 1/{total}", msg)
        self.assertIn("{mode}", msg)
        self.assertIn("{time}", msg)

    def test_extra_arguments_ignored(self):
        """Extra format parameters not present in template should be safely ignored."""
        msg = t("game_setup_title", "en", extra_param_foo="bar", unused_number=42)
        self.assertIsInstance(msg, str)
        self.assertTrue(len(msg) > 0)

    def test_missing_key_fallback(self):
        """Non-existent translation keys should return the key itself without raising KeyError."""
        res = t("non_existent_key_xyz", "en")
        self.assertEqual(res, "non_existent_key_xyz")

        res_uz = t("non_existent_key_xyz", "uz")
        self.assertEqual(res_uz, "non_existent_key_xyz")

    def test_none_or_empty_key(self):
        """None or empty key should return empty string without errors."""
        self.assertEqual(t(None), "")
        self.assertEqual(t(""), "")

    def test_locale_keys_and_placeholders_consistency(self):
        """All languages (en, ru, uz) must share the same key set and identical format placeholders."""
        en_keys = set(LOCALES["en"].keys())
        ru_keys = set(LOCALES["ru"].keys())
        uz_keys = set(LOCALES["uz"].keys())

        self.assertEqual(en_keys, ru_keys, f"Keys mismatch en vs ru: {en_keys ^ ru_keys}")
        self.assertEqual(en_keys, uz_keys, f"Keys mismatch en vs uz: {en_keys ^ uz_keys}")

        placeholder_pattern = re.compile(r"\{([a-zA-Z0-9_]+)\}")
        for k in en_keys:
            en_val = LOCALES["en"][k]
            ru_val = LOCALES["ru"][k]
            uz_val = LOCALES["uz"][k]

            if isinstance(en_val, str):
                en_ph = set(placeholder_pattern.findall(en_val))
                ru_ph = set(placeholder_pattern.findall(ru_val)) if isinstance(ru_val, str) else set()
                uz_ph = set(placeholder_pattern.findall(uz_val)) if isinstance(uz_val, str) else set()
                self.assertEqual(en_ph, ru_ph, f"Placeholder mismatch in key '{k}' between en and ru")
                self.assertEqual(en_ph, uz_ph, f"Placeholder mismatch in key '{k}' between en and uz")

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
