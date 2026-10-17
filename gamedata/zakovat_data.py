# -*- coding: utf-8 -*-
"""
Zakovat & Intellectual Quiz Dataset (500 Questions).

Subcategories:
- black_box (125 questions): Mystery objects with clues ('Qora quti') + Wikimedia image URLs.
- deduction (125 questions): Logical deduction questions ('X ni toping', Sherlock style).
- world_intellect (125 questions): Islamic Golden Age, philosophy, science trivia & cultural paradoxes.
- blitz (125 questions): Fast-paced, witty, sharp trivia questions.

Total: exactly 500 questions.
"""
from typing import List, Dict, Optional, Any
import random

try:
    from .zakovat_parts.part1_blackbox import BLACK_BOX_QUESTIONS
    from .zakovat_parts.part2_deduction import DEDUCTION_QUESTIONS
    from .zakovat_parts.part3_world_intellect import WORLD_INTELLECT_QUESTIONS
    from .zakovat_parts.part4_blitz import BLITZ_QUESTIONS
except (ImportError, ValueError):
    from gamedata.zakovat_parts.part1_blackbox import BLACK_BOX_QUESTIONS
    from gamedata.zakovat_parts.part2_deduction import DEDUCTION_QUESTIONS
    from gamedata.zakovat_parts.part3_world_intellect import WORLD_INTELLECT_QUESTIONS
    from gamedata.zakovat_parts.part4_blitz import BLITZ_QUESTIONS

ZAKOVAT_QUESTIONS: List[Dict[str, Any]] = (
    BLACK_BOX_QUESTIONS
    + DEDUCTION_QUESTIONS
    + WORLD_INTELLECT_QUESTIONS
    + BLITZ_QUESTIONS
)

# Index by unique ID
ZAKOVAT_BY_ID: Dict[str, Dict[str, Any]] = {
    q["id"]: q for q in ZAKOVAT_QUESTIONS
}

# Index by category / type
ZAKOVAT_BY_TYPE: Dict[str, List[Dict[str, Any]]] = {}
for q in ZAKOVAT_QUESTIONS:
    ZAKOVAT_BY_TYPE.setdefault(q["type"], []).append(q)


def get_zakovat_question_by_id(question_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a single zakovat question by its unique ID."""
    return ZAKOVAT_BY_ID.get(question_id)


def get_random_zakovat_questions(
    count: int = 10, category: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get a random sample of Zakovat questions.
    If category is provided ('black_box', 'deduction', 'world_intellect', 'blitz'),
    only questions from that category are returned.
    """
    if category and category in ZAKOVAT_BY_TYPE:
        pool = ZAKOVAT_BY_TYPE[category]
    else:
        pool = ZAKOVAT_QUESTIONS

    actual_count = min(count, len(pool))
    return random.sample(pool, actual_count)


def search_zakovat_by_alias(query: str, lang: str = "uz") -> List[Dict[str, Any]]:
    """
    Search zakovat questions by query substring against aliases or correct answers.
    """
    normalized = query.strip().lower()
    results = []
    for q in ZAKOVAT_QUESTIONS:
        # Check aliases
        if any(normalized in alias.lower() for alias in q.get("aliases", [])):
            results.append(q)
            continue
        # Check correct answer in the specified language or all languages
        ans = q.get("correct_answer", {})
        if isinstance(ans, dict):
            if normalized in ans.get(lang, "").lower():
                results.append(q)
                continue
            if any(normalized in val.lower() for val in ans.values() if isinstance(val, str)):
                results.append(q)
                continue
    return results


def get_zakovat_counts() -> Dict[str, int]:
    """Return question counts by category and total."""
    counts = {t: len(items) for t, items in ZAKOVAT_BY_TYPE.items()}
    counts["total"] = len(ZAKOVAT_QUESTIONS)
    return counts


__all__ = [
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
]
