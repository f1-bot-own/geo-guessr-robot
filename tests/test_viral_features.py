"""
Unit tests for the 4 Viral GeoGuessr / GeoGuru Features:
1. Emoji Riddle (GameMode.EMOJI)
2. Contour / Silhouette (GameMode.CONTOUR)
3. Continent Filter (Asia, Europe, Africa, Americas, Oceania, All)
4. WebApp Blur / Zoom-In Reveal
"""
import os
import unittest
from games.models import GameMode, Question
from games.question_factory import QuestionFactory
from games.session import GameSession
from games.solo_session import SoloGameSession
from keyboards.game_kb import get_setup_kb, get_solo_setup_kb, get_category_selection_kb
from gamedata.emojis import EMOJI_RIDDLES, get_emoji_riddle
from gamedata.contours import CONTOUR_DATA, CONTOUR_BY_CODE, get_contour_info, get_contour_url


class TestViralFeatures(unittest.TestCase):

    def test_emoji_dataset_integrity(self):
        """Test emoji riddles data loaded and has required fields."""
        self.assertGreaterEqual(len(EMOJI_RIDDLES), 50)
        uz_riddle = get_emoji_riddle("UZ")
        self.assertIsNotNone(uz_riddle)
        self.assertIn("emojis", uz_riddle)
        self.assertIn("hint", uz_riddle)
        self.assertIn("uz", uz_riddle["hint"])
        self.assertIn("ru", uz_riddle["hint"])
        self.assertIn("en", uz_riddle["hint"])

    def test_contour_dataset_integrity(self):
        """Test contour dataset loaded and has valid URLs and shape trivia."""
        self.assertGreaterEqual(len(CONTOUR_DATA), 40)
        it_contour = get_contour_info("IT")
        self.assertIsNotNone(it_contour)
        self.assertIn("shape_trivia", it_contour)
        self.assertTrue(it_contour["shape_trivia"]["uz"].lower().find("etik") != -1 or "etik" in it_contour["shape_trivia"]["uz"])
        it_url = get_contour_url("IT")
        self.assertTrue(it_url.endswith("/it/1024.png"))

    def test_emoji_question_generation(self):
        """Test generating emoji riddle questions in uz, ru, en."""
        for lang in ("uz", "ru", "en"):
            q = QuestionFactory.generate(GameMode.EMOJI, lang=lang)
            self.assertEqual(q.mode, GameMode.EMOJI)
            self.assertIsNotNone(q.country_code)
            self.assertIn(q.country_code.lower(), [c["code"].lower() for c in EMOJI_RIDDLES])
            self.assertEqual(len(q.options), 4)
            self.assertIn(q.correct_answer, q.options)
            self.assertTrue(len(set(q.options)) == 4, "Options must be distinct")
            self.assertTrue(len(q.text) > 0)

    def test_contour_question_generation(self):
        """Test generating silhouette/contour questions in uz, ru, en."""
        for lang in ("uz", "ru", "en"):
            q = QuestionFactory.generate(GameMode.CONTOUR, lang=lang)
            self.assertEqual(q.mode, GameMode.CONTOUR)
            self.assertIsNotNone(q.country_code)
            self.assertIn(q.country_code.lower(), CONTOUR_BY_CODE)
            self.assertIsNotNone(q.image_url)
            self.assertTrue(q.image_url.startswith("https://raw.githubusercontent.com/djaiss/mapsicon/"))
            self.assertEqual(len(q.options), 4)
            self.assertIn(q.correct_answer, q.options)
            self.assertTrue(len(set(q.options)) == 4, "Options must be distinct")

    def test_continent_filtering(self):
        """Test continent filtering restricts country selection appropriately."""
        # European countries test
        for _ in range(5):
            q_eu = QuestionFactory.generate(GameMode.FLAG, lang="en", continent="europe")
            from gamedata.countries import COUNTRIES
            c_dict = next((c for c in COUNTRIES if c["code"] == q_eu.country_code), None)
            self.assertIsNotNone(c_dict)
            self.assertIn("europe", c_dict["continent"]["en"].lower())

        # Asian countries test
        for _ in range(5):
            q_as = QuestionFactory.generate(GameMode.FLAG, lang="uz", continent="asia")
            c_dict = next((c for c in COUNTRIES if c["code"] == q_as.country_code), None)
            self.assertIsNotNone(c_dict)
            self.assertIn("asia", c_dict["continent"]["en"].lower())

        # Emoji with continent filter
        for _ in range(5):
            q_emoji = QuestionFactory.generate(GameMode.EMOJI, lang="en", continent="asia")
            c_dict = next((c for c in COUNTRIES if c["code"] == q_emoji.country_code), None)
            if c_dict and "continent" in c_dict:
                self.assertIn("asia", c_dict["continent"]["en"].lower())

    def test_group_session_continent(self):
        """Test GameSession handles continent configuration."""
        session = GameSession(chat_id=123, lang="uz", continent="europe")
        self.assertEqual(session.continent, "europe")
        session.continent = "asia"
        self.assertEqual(session.continent, "asia")

    def test_solo_session_continent(self):
        """Test SoloGameSession handles continent configuration."""
        session = SoloGameSession(user_id=456, user_name="Alex", lang="en", continent="africa")
        self.assertEqual(session.continent, "africa")

    def test_keyboards_include_new_modes_and_continent(self):
        """Test keyboards generate buttons for Emoji, Contour, and Continent filter."""
        # Group setup keyboard
        kb_group = get_setup_kb(
            session_id="test1234",
            mode="flag",
            rounds=5,
            round_time=30,
            lang="uz",
            continent="all"
        )
        buttons_group = [btn.text for row in kb_group.inline_keyboard for btn in row]
        self.assertTrue(any("qit" in b.lower() for b in buttons_group), f"Continent button missing in {buttons_group}")
        self.assertTrue(any("emoji" in b.lower() for b in buttons_group), f"Emoji button missing in {buttons_group}")
        self.assertTrue(any("kontur" in b.lower() or "soya" in b.lower() for b in buttons_group), f"Contour button missing in {buttons_group}")

        # Solo setup keyboard
        kb_solo = get_solo_setup_kb(
            mode="emoji",
            round_time=30,
            lang="en",
            continent="asia"
        )
        buttons_solo = [btn.text for row in kb_solo.inline_keyboard for btn in row]
        self.assertTrue(any("Continent" in b for b in buttons_solo), f"Continent button missing in solo: {buttons_solo}")

        # Solo category keyboard
        kb_cat = get_category_selection_kb(lang="ru")
        buttons_cat = [btn.text for row in kb_cat.inline_keyboard for btn in row]
        self.assertTrue(any("Эмодзи" in b for b in buttons_cat), f"Emoji category missing in {buttons_cat}")
        self.assertTrue(any("Контур" in b for b in buttons_cat), f"Contour category missing in {buttons_cat}")

    def test_webapp_blur_elements(self):
        """Test webapp files contain blur reveal elements and translations."""
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html_path = os.path.join(root, "webapp", "index.html")
        css_path = os.path.join(root, "webapp", "style.css")
        js_path = os.path.join(root, "webapp", "app.js")

        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn('id="blurToggleBtn"', html)
        self.assertIn('id="blurPill"', html)
        self.assertIn('id="metricBlurBonus"', html)

        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()
        self.assertIn(".blurred-reveal", css)
        self.assertIn(".blur-pill", css)
        self.assertIn(".bonus-box", css)

        with open(js_path, "r", encoding="utf-8") as f:
            js = f.read()
        self.assertIn("startBlurReveal", js)
        self.assertIn("stopBlurReveal", js)
        self.assertIn("toggleBlurMode", js)
        self.assertIn("blurBonus", js)


if __name__ == "__main__":
    unittest.main()
