"""
Game datasets package (countries, landmarks, streetviews, fun facts).
Renamed from 'data' to prevent collision with Railway persistent volume mounts at /app/data.
"""

import sys
from . import (
    countries,
    landmarks,
    streetviews,
    fun_facts,
    emojis,
    contours,
    celebrities_data,
    logos_data,
    presidents_data,
    historical_data,
    nature_data,
    logic_math_data,
    zakovat_data,
    astronomy_data,
    science_data,
    history_data,
    literature_data,
    art_data,
)
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
from .nature_data import (
    NATURE_DATA,
    NATURE_BY_ID,
    NATURE_BY_SUBMODE,
    get_nature_item_by_id,
    get_nature_items_by_submode,
    get_random_nature_item,
)
from .logic_math_data import (
    LOGIC_MATH_DATA,
    LOGIC_BY_ID,
    LOGIC_BY_SUBMODE,
    get_logic_item_by_id,
    get_logic_items_by_submode,
    get_random_logic_item,
)
from .zakovat_data import (
    ZAKOVAT_QUESTIONS,
    ZAKOVAT_BY_ID,
    ZAKOVAT_BY_TYPE,
    BLACK_BOX_QUESTIONS,
    DEDUCTION_QUESTIONS,
    WORLD_INTELLECT_QUESTIONS,
    BLITZ_QUESTIONS,
    get_zakovat_question_by_id,
    get_random_zakovat_questions,
    search_zakovat_by_alias,
    get_zakovat_counts,
)
from .astronomy_data import (
    ASTRONOMY_QUESTIONS,
    ASTRONOMY_BY_ID,
    ASTRONOMY_BY_SUBMODE,
    get_astronomy_question_by_id,
    get_astronomy_questions_by_submode,
    get_random_astronomy_questions,
)
from .science_data import (
    SCIENCE_QUESTIONS,
    SCIENCE_BY_ID,
    SCIENCE_BY_SUBMODE,
    get_science_question_by_id,
    get_science_questions_by_submode,
    get_random_science_questions,
)
from .history_data import (
    HISTORY_DATA,
    HISTORY_QUESTIONS,
    HISTORY_BY_ID,
    HISTORY_BY_SUBMODE,
    HISTORY_BY_SUB_MODE,
    get_history_item_by_id,
    get_history_question_by_id,
    get_history_items_by_submode,
    get_history_questions_by_submode,
    get_random_history_items,
    get_random_history_questions,
    search_history_by_alias,
)
from .literature_data import (
    LITERATURE_DATA,
    LITERATURE_QUESTIONS,
    LITERATURE_BY_ID,
    LITERATURE_BY_SUBMODE,
    LITERATURE_BY_SUB_MODE,
    get_literature_item_by_id,
    get_literature_question_by_id,
    get_literature_items_by_submode,
    get_literature_questions_by_submode,
    get_random_literature_items,
    get_random_literature_questions,
    search_literature_by_alias,
)
from .art_data import (
    ART_DATA,
    ART_QUESTIONS,
    ART_BY_ID,
    ART_BY_SUBMODE,
    ART_BY_SUB_MODE,
    get_art_item_by_id,
    get_art_question_by_id,
    get_art_items_by_submode,
    get_art_questions_by_submode,
    get_random_art_items,
    get_random_art_questions,
    search_art_by_alias,
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
sys.modules.setdefault("data.nature_data", nature_data)
sys.modules.setdefault("data.logic_math_data", logic_math_data)
sys.modules.setdefault("data.zakovat_data", zakovat_data)
sys.modules.setdefault("data.astronomy_data", astronomy_data)
sys.modules.setdefault("data.science_data", science_data)
sys.modules.setdefault("data.history_data", history_data)
sys.modules.setdefault("data.literature_data", literature_data)
sys.modules.setdefault("data.art_data", art_data)

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
    "NATURE_DATA",
    "NATURE_BY_ID",
    "NATURE_BY_SUBMODE",
    "get_nature_item_by_id",
    "get_nature_items_by_submode",
    "get_random_nature_item",
    "LOGIC_MATH_DATA",
    "LOGIC_BY_ID",
    "LOGIC_BY_SUBMODE",
    "get_logic_item_by_id",
    "get_logic_items_by_submode",
    "get_random_logic_item",
    "ZAKOVAT_QUESTIONS",
    "ZAKOVAT_BY_ID",
    "ZAKOVAT_BY_TYPE",
    "BLACK_BOX_QUESTIONS",
    "DEDUCTION_QUESTIONS",
    "WORLD_INTELLECT_QUESTIONS",
    "BLITZ_QUESTIONS",
    "get_zakovat_question_by_id",
    "get_random_zakovat_questions",
    "search_zakovat_by_alias",
    "get_zakovat_counts",
    "ASTRONOMY_QUESTIONS",
    "ASTRONOMY_BY_ID",
    "ASTRONOMY_BY_SUBMODE",
    "get_astronomy_question_by_id",
    "get_astronomy_questions_by_submode",
    "get_random_astronomy_questions",
    "SCIENCE_QUESTIONS",
    "SCIENCE_BY_ID",
    "SCIENCE_BY_SUBMODE",
    "get_science_question_by_id",
    "get_science_questions_by_submode",
    "get_random_science_questions",
    "HISTORY_DATA",
    "HISTORY_QUESTIONS",
    "HISTORY_BY_ID",
    "HISTORY_BY_SUBMODE",
    "HISTORY_BY_SUB_MODE",
    "get_history_item_by_id",
    "get_history_question_by_id",
    "get_history_items_by_submode",
    "get_history_questions_by_submode",
    "get_random_history_items",
    "get_random_history_questions",
    "search_history_by_alias",
    "LITERATURE_DATA",
    "LITERATURE_QUESTIONS",
    "LITERATURE_BY_ID",
    "LITERATURE_BY_SUBMODE",
    "LITERATURE_BY_SUB_MODE",
    "get_literature_item_by_id",
    "get_literature_question_by_id",
    "get_literature_items_by_submode",
    "get_literature_questions_by_submode",
    "get_random_literature_items",
    "get_random_literature_questions",
    "search_literature_by_alias",
    "ART_DATA",
    "ART_QUESTIONS",
    "ART_BY_ID",
    "ART_BY_SUBMODE",
    "ART_BY_SUB_MODE",
    "get_art_item_by_id",
    "get_art_question_by_id",
    "get_art_items_by_submode",
    "get_art_questions_by_submode",
    "get_random_art_items",
    "get_random_art_questions",
    "search_art_by_alias",
]


