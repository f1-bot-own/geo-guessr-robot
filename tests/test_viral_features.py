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
            continent="all",
            view_mode="detailed"
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
        from keyboards.game_kb import get_hub_subcategories_kb
        kb_cat = get_category_selection_kb(lang="ru")
        buttons_cat = [btn.text for row in kb_cat.inline_keyboard for btn in row]
        self.assertTrue(any("География" in b for b in buttons_cat), f"Geography category missing in {buttons_cat}")

        kb_sub = get_hub_subcategories_kb(hub="geography", lang="ru")
        buttons_sub = [btn.text for row in kb_sub.inline_keyboard for btn in row]
        self.assertTrue(any("Эмодзи" in b for b in buttons_sub), f"Emoji category missing in {buttons_sub}")
        self.assertTrue(any("Контур" in b for b in buttons_sub), f"Contour category missing in {buttons_sub}")

    def test_blur_question_generation(self):
        """Test generating blur questions in uz, ru, en."""
        for lang in ("uz", "ru", "en"):
            q = QuestionFactory.generate(GameMode.BLUR, lang=lang)
            self.assertEqual(q.mode, GameMode.BLUR)
            self.assertIsNotNone(q.image_url)
            self.assertEqual(len(q.options), 4)
            self.assertIn(q.correct_answer, q.options)
            self.assertEqual(len(set(q.options)), 4, "Options must be distinct")
            self.assertEqual(q.blur_stage, 1)

    def test_blur_engine_stages(self):
        """Test blur engine processes image into 3 progressive reveal stages."""
        from games.blur_engine import process_image_to_stages
        from PIL import Image
        import io
        img = Image.new("RGB", (200, 200), color="blue")
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        raw_bytes = buf.getvalue()

        stages = process_image_to_stages(raw_bytes)
        self.assertEqual(len(stages), 3)
        for stage_bytes in stages:
            self.assertIsInstance(stage_bytes, bytes)
            self.assertGreater(len(stage_bytes), 0)

    def test_group_session_blur_bonus(self):
        """Test GameSession awards speed bonus based on blur stage."""
        import asyncio
        session = GameSession(chat_id=999, lang="en", mode=GameMode.BLUR)
        q = Question(
            mode=GameMode.BLUR,
            text="Guess this country:",
            options=["France", "Germany", "Italy", "Spain"],
            correct_index=0,
            correct_answer="France",
            country_code="fr",
            image_url="https://flagcdn.com/w640/fr.png"
        )
        session.current_question = q
        session.round_start_time = 0.0
        session.status = "in_progress"

        # Stage 1: +300 bonus
        q.blur_stage = 1
        res, pts_s1, _ = asyncio.run(session.check_answer(user_id=1, user_name="Alice", option_index=0))
        self.assertEqual(res, "correct")
        self.assertGreaterEqual(pts_s1, 400) # 100 base + 300 bonus

        # Stage 2: +150 bonus
        session.status = "in_progress"
        session.answered_users_wrong.clear()
        q.blur_stage = 2
        res2, pts_s2, _ = asyncio.run(session.check_answer(user_id=2, user_name="Bob", option_index=0))
        self.assertEqual(res2, "correct")
        self.assertEqual(pts_s1 - pts_s2, 150) # Difference is exactly the 150 bonus diff

    def test_solo_session_blur_bonus(self):
        """Test SoloGameSession awards speed bonus based on blur stage."""
        session = SoloGameSession(user_id=888, user_name="Charlie", lang="uz", mode=GameMode.BLUR)
        q = Question(
            mode=GameMode.BLUR,
            text="Bu qaysi davlat?",
            options=["O'zbekiston", "Qozog'iston", "Tojikiston", "Qirg'iziston"],
            correct_index=0,
            correct_answer="O'zbekiston",
            country_code="uz",
            image_url="https://flagcdn.com/w640/uz.png"
        )
        session.current_question = q

        # Stage 1: 100 base + 300 bonus = 400
        q.blur_stage = 1
        is_corr, pts, is_over = session.check_answer(0)
        self.assertTrue(is_corr)
        self.assertEqual(pts, 400)
        self.assertFalse(is_over)

    def test_countdown_checkpoints_blur(self):
        """Test countdown checkpoints include blur transition thresholds."""
        from games.flow import get_countdown_checkpoints
        cp_blur = get_countdown_checkpoints(20, is_blur=True)
        self.assertIn(13, cp_blur)
        self.assertIn(7, cp_blur)

    def test_keyboards_include_blur_mode(self):
        """Test blur mode button appears in keyboards."""
        kb_group = get_setup_kb(
            session_id="blur123",
            mode="blur",
            rounds=5,
            round_time=20,
            lang="uz",
            continent="all"
        )
        buttons_group = [btn.text for row in kb_group.inline_keyboard for btn in row]
        self.assertTrue(any("xira" in b.lower() or "blur" in b.lower() for b in buttons_group), f"Blur missing: {buttons_group}")


if __name__ == "__main__":
    unittest.main()
