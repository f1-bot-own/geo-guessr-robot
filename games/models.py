"""
Game Models and Dataclasses for GeoGuru & GeoGuessr.
"""

from dataclasses import dataclass
from typing import List, Optional

class GameMode:
    FLAG = "flag"
    CAPITAL = "capital"
    LANDMARK = "landmark"
    HIGHER_LOWER = "higher_lower"
    COAT_OF_ARMS = "coat_of_arms"
    STREETVIEW = "streetview"
    EMOJI = "emoji"
    CONTOUR = "contour"
    BLUR = "blur"
    PRESIDENT = "president"
    HISTORICAL = "historical"
    CELEBRITY = "celebrity"
    PERSON = "person"
    LOGO = "logo"
    MIX = "mix"

    ZAKOVAT = "zakovat"
    ASTRONOMY = "astronomy"
    SCIENCE = "science"
    HISTORY = "history"
    LITERATURE = "literature"
    ART = "art"
    NATURE = "nature"
    LOGIC_MATH = "logic_math"

    ALL = [
        FLAG, CAPITAL, LANDMARK, HIGHER_LOWER, COAT_OF_ARMS,
        STREETVIEW, EMOJI, CONTOUR, BLUR,
        PRESIDENT, HISTORICAL, CELEBRITY, PERSON, LOGO,
        ZAKOVAT, ASTRONOMY, SCIENCE, HISTORY, LITERATURE, ART, NATURE, LOGIC_MATH,
        MIX
    ]

@dataclass
class Question:
    mode: str
    text: str
    options: List[str]
    correct_index: int
    correct_answer: str
    country_code: str
    image_url: Optional[str] = None
    fun_fact: Optional[str] = None
    stat_info: Optional[str] = None
    maps_url: Optional[str] = None
    location_title: Optional[str] = None
    driving_side: Optional[str] = None
    blur_stages: Optional[tuple] = None
    blur_stage: int = 1
    aliases: Optional[List[str]] = None
    sub_mode: Optional[str] = None
    is_black_box: bool = False
