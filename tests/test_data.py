"""
Unit tests for data integrity in GeoGuru & GeoGuessr.
"""
import unittest
from data.countries import COUNTRIES, COUNTRIES_BY_CODE, get_country, search_country_by_name
from data.landmarks import LANDMARKS, LANDMARKS_BY_ID, get_landmark_by_id, get_random_landmarks

class TestDataIntegrity(unittest.TestCase):

    def test_countries_count(self):
        self.assertGreaterEqual(len(COUNTRIES), 120, "Should have at least 120 countries")

    def test_country_fields(self):
        for c in COUNTRIES:
            self.assertIn("code", c)
            self.assertEqual(len(c["code"]), 2, f"Country code should be 2 chars: {c['code']}")
            self.assertIn("name", c)
            self.assertIn("en", c["name"])
            self.assertIn("ru", c["name"])
            self.assertIn("uz", c["name"])
            self.assertIn("capital", c)
            self.assertIn("continent", c)
            self.assertIn("flag_emoji", c)
            self.assertGreater(c["population"], 0, f"Population must be > 0: {c['code']}")
            self.assertGreater(c["area_sq_km"], 0, f"Area must be > 0: {c['code']}")
            self.assertIn("flag_url", c)

    def test_country_lookup(self):
        uz = get_country("uz")
        self.assertIsNotNone(uz)
        self.assertEqual(uz["capital"]["en"], "Tashkent")
        self.assertEqual(uz["flag_emoji"], "🇺🇿")

        search_res = search_country_by_name("Tashkent")
        self.assertIsNotNone(search_res)
        self.assertEqual(search_res["code"], "uz")

    def test_landmarks_count_and_validity(self):
        self.assertGreaterEqual(len(LANDMARKS), 20, "Should have at least 20 landmarks")
        for lm in LANDMARKS:
            self.assertIn("id", lm)
            self.assertIn("name", lm)
            self.assertIn("en", lm["name"])
            self.assertIn("ru", lm["name"])
            self.assertIn("uz", lm["name"])
            self.assertIn("country_code", lm)
            self.assertIn(lm["country_code"], COUNTRIES_BY_CODE, f"Landmark {lm['id']} references unknown country {lm['country_code']}")
            self.assertIn("image_url", lm)
            self.assertTrue(lm["image_url"].startswith("http"), f"Image url must be http(s): {lm['image_url']}")
            self.assertIn("hint", lm)

    def test_landmark_lookup(self):
        eiffel = get_landmark_by_id("eiffel_tower")
        self.assertIsNotNone(eiffel)
        self.assertEqual(eiffel["country_code"], "fr")

        samples = get_random_landmarks(3)
        self.assertEqual(len(samples), 3)

if __name__ == "__main__":
    unittest.main()
