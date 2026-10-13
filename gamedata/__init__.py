"""
Game datasets package (countries, landmarks, streetviews, fun facts).
Renamed from 'data' to prevent collision with Railway persistent volume mounts at /app/data.
"""

import sys
from . import countries, landmarks, streetviews, fun_facts
from .countries import COUNTRIES, COUNTRIES_BY_CODE, get_country, search_country_by_name
from .landmarks import LANDMARKS, LANDMARKS_BY_ID, get_landmark_by_id, get_random_landmarks, get_landmark
from .streetviews import STREETVIEWS, get_streetview, get_random_streetview
from .fun_facts import FUN_FACTS, get_fun_fact

# Populate sys.modules aliases so legacy or external references to 'data.*'
# resolve directly even if /app/data is mounted as an empty persistent volume in Docker / Railway
sys.modules.setdefault("data", sys.modules[__name__])
sys.modules.setdefault("data.countries", countries)
sys.modules.setdefault("data.landmarks", landmarks)
sys.modules.setdefault("data.streetviews", streetviews)
sys.modules.setdefault("data.fun_facts", fun_facts)

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
