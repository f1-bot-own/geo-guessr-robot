"""
Game datasets package (countries, landmarks, streetviews, fun facts).
Renamed from 'data' to prevent collision with Railway persistent volume mounts at /app/data.
"""

from .countries import COUNTRIES, COUNTRIES_BY_CODE, get_country, search_country_by_name
from .landmarks import LANDMARKS, LANDMARKS_BY_ID, get_landmark_by_id, get_random_landmarks, get_landmark
from .streetviews import STREETVIEWS, get_streetview, get_random_streetview
from .fun_facts import FUN_FACTS, get_fun_fact

__all__ = [
    "COUNTRIES",
    "COUNTRIES_BY_CODE",
    "get_country",
    "search_country_by_name",
    "LANDMARKS",
    "LANDMARKS_BY_ID",
    "get_landmark_by_id",
    "get_random_landmarks",
    "get_landmark",
    "STREETVIEWS",
    "get_streetview",
    "get_random_streetview",
    "FUN_FACTS",
    "get_fun_fact",
]
