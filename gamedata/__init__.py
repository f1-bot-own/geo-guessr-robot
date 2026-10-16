"""
Game datasets package (countries, landmarks, streetviews, fun facts).
Renamed from 'data' to prevent collision with Railway persistent volume mounts at /app/data.
"""

import sys
from . import countries, landmarks, streetviews, fun_facts, emojis, contours, celebrities_data, logos_data, presidents_data, historical_data
from .countries import COUNTRIES, COUNTRIES_BY_CODE, get_country, search_country_by_name
from .landmarks import LANDMARKS, LANDMARKS_BY_ID, get_landmark_by_id, get_random_landmarks, get_landmark
from .streetviews import STREETVIEWS, get_streetview, get_random_streetview
from .fun_facts import FUN_FACTS, get_fun_fact
from .emojis import EMOJI_RIDDLES, EMOJI_BY_CODE, get_emoji_riddle
from .contours import CONTOUR_DATA, CONTOUR_BY_CODE, get_contour_url, get_contour_info
from .presidents_data import (
    PRESIDENTS,
    PRESIDENTS_BY_ID,
    get_president_by_id,
    get_random_presidents,
    search_president_by_alias,
)
from .historical_data import (
    HISTORICAL_FIGURES,
    HISTORICAL_BY_ID,
    get_historical_figure_by_id,
    get_random_historical_figures,
    search_historical_by_alias,
)
from .celebrities_data import (
    CELEBRITIES,
    CELEBRITIES_BY_ID,
    get_celebrity_by_id,
    get_random_celebrities,
    search_celebrity_by_alias,
)
from .logos_data import (
    LOGOS,
    LOGOS_BY_ID,
    get_logo_by_id,
    get_random_logos,
    search_logo_by_alias,
)

# Populate sys.modules aliases so legacy or external references to 'data.*'
# resolve directly even if /app/data is mounted as an empty persistent volume in Docker / Railway
sys.modules.setdefault("data", sys.modules[__name__])
sys.modules.setdefault("data.countries", countries)
sys.modules.setdefault("data.landmarks", landmarks)
sys.modules.setdefault("data.streetviews", streetviews)
sys.modules.setdefault("data.fun_facts", fun_facts)
sys.modules.setdefault("data.emojis", emojis)
sys.modules.setdefault("data.contours", contours)
sys.modules.setdefault("data.presidents_data", presidents_data)
sys.modules.setdefault("data.historical_data", historical_data)
sys.modules.setdefault("data.celebrities_data", celebrities_data)
sys.modules.setdefault("data.logos_data", logos_data)

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
    "EMOJI_RIDDLES",
    "EMOJI_BY_CODE",
    "get_emoji_riddle",
    "CONTOUR_DATA",
    "CONTOUR_BY_CODE",
    "get_contour_url",
    "get_contour_info",
    "PRESIDENTS",
    "PRESIDENTS_BY_ID",
    "get_president_by_id",
    "get_random_presidents",
    "search_president_by_alias",
    "HISTORICAL_FIGURES",
    "HISTORICAL_BY_ID",
    "get_historical_figure_by_id",
    "get_random_historical_figures",
    "search_historical_by_alias",
    "CELEBRITIES",
    "CELEBRITIES_BY_ID",
    "get_celebrity_by_id",
    "get_random_celebrities",
    "search_celebrity_by_alias",
    "LOGOS",
    "LOGOS_BY_ID",
    "get_logo_by_id",
    "get_random_logos",
    "search_logo_by_alias",
]

