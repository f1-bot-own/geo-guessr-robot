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
    MIX = "mix"

    ALL = [FLAG, CAPITAL, LANDMARK, HIGHER_LOWER, COAT_OF_ARMS, STREETVIEW, EMOJI, CONTOUR, MIX]

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
