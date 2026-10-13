"""
Question and game modes generator for GeoGuru & GeoGuessr.
Implements:
- Flag Quiz
- Capital Cities
- GeoGuessr Landmarks
- Higher / Lower (Population & Area)
- Coats of Arms
- Mix Mode
"""
import random
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

from gamedata.countries import COUNTRIES
from gamedata.landmarks import LANDMARKS
from gamedata.streetviews import STREETVIEWS
from locales.i18n import t

@dataclass
class QuestionOption:
    id: str
    text: str
    is_correct: bool

@dataclass
class Question:
    mode: str
    prompt: str
    options: List[QuestionOption]
    correct_option_id: str
    correct_answer_text: str
    media_url: Optional[str] = None
    media_type: Optional[str] = None  # "photo"
    extra_info: Optional[str] = None
    country_code: Optional[str] = None
    hint_text: Optional[str] = None

def generate_flag_question(lang: str = "en") -> Question:
    """Generate a flag quiz question: identify country from flag."""
    target = random.choice(COUNTRIES)
    distractors = [c for c in COUNTRIES if c["code"] != target["code"]]
    sampled_distractors = random.sample(distractors, 3)
    
    choices = [target] + sampled_distractors
    random.shuffle(choices)
    
    options = []
    correct_id = target["code"]
    for c in choices:
        name = c["name"].get(lang, c["name"]["en"])
        options.append(QuestionOption(
            id=c["code"],
            text=f"{c['flag_emoji']} {name}",
            is_correct=(c["code"] == correct_id)
        ))
    
    target_name = target["name"].get(lang, target["name"]["en"])
    prompt = f"{t('question_flag', lang)}\n\n🏳️ {target['flag_emoji']}"
    
    return Question(
        mode="flag",
        prompt=prompt,
        options=options,
        correct_option_id=correct_id,
        correct_answer_text=f"{target['flag_emoji']} {target_name}",
        media_url=target.get("flag_url"),
        media_type="photo",
        country_code=target["code"],
        hint_text=f"Capital: {target['capital'].get(lang, target['capital']['en'])} | {target['continent'].get(lang, target['continent']['en'])}"
    )

def generate_capital_question(lang: str = "en") -> Question:
    """
    Generate a capital question:
    50% chance: 'What is the capital of X?'
    50% chance: 'Which country has the capital Y?'
    """
    target = random.choice(COUNTRIES)
    distractors = [c for c in COUNTRIES if c["code"] != target["code"]]
    sampled_distractors = random.sample(distractors, 3)
    
    is_capital_of_country = random.choice([True, False])
    target_country_name = target["name"].get(lang, target["name"]["en"])
    target_capital_name = target["capital"].get(lang, target["capital"]["en"])
    
    if is_capital_of_country:
        prompt = t("question_capital_of_country", lang, country=f"<b>{target['flag_emoji']} {target_country_name}</b>")
        choices = [target] + sampled_distractors
        random.shuffle(choices)
        
        options = []
        correct_id = target["code"]
        for c in choices:
            cap = c["capital"].get(lang, c["capital"]["en"])
            options.append(QuestionOption(
                id=c["code"],
                text=f"🏛 {cap}",
                is_correct=(c["code"] == correct_id)
            ))
        
        correct_text = f"🏛 {target_capital_name} ({target_country_name})"
    else:
        prompt = t("question_country_of_capital", lang, capital=f"<b>{target_capital_name}</b>")
        choices = [target] + sampled_distractors
        random.shuffle(choices)
        
        options = []
        correct_id = target["code"]
        for c in choices:
            c_name = c["name"].get(lang, c["name"]["en"])
            options.append(QuestionOption(
                id=c["code"],
                text=f"{c['flag_emoji']} {c_name}",
                is_correct=(c["code"] == correct_id)
            ))
        
        correct_text = f"{target['flag_emoji']} {target_country_name}"

    return Question(
        mode="capital",
        prompt=prompt,
        options=options,
        correct_option_id=correct_id,
        correct_answer_text=correct_text,
        country_code=target["code"],
        hint_text=f"Located in: {target['continent'].get(lang, target['continent']['en'])}"
    )

def generate_landmark_question(lang: str = "en") -> Question:
    """Generate a GeoGuessr landmark question: guess country from sight photo."""
    landmark = random.choice(LANDMARKS)
    country_code = landmark["country_code"]
    
    # Target country
    target_country = next((c for c in COUNTRIES if c["code"] == country_code), None)
    if not target_country:
        target_country = {
            "code": country_code,
            "name": {"en": "Target", "ru": "Цель", "uz": "Nishon"},
            "flag_emoji": "🌐",
            "capital": {"en": landmark.get("city", {}).get(lang, "City")},
            "continent": landmark.get("continent", {"en": "World", "ru": "Мир", "uz": "Dunyo"})
        }
        
    distractors = [c for c in COUNTRIES if c["code"] != country_code]
    sampled_distractors = random.sample(distractors, 3)
    
    choices = [target_country] + sampled_distractors
    random.shuffle(choices)
    
    options = []
    correct_id = country_code
    for c in choices:
        c_name = c["name"].get(lang, c["name"]["en"])
        options.append(QuestionOption(
            id=c["code"],
            text=f"{c.get('flag_emoji', '🌐')} {c_name}",
            is_correct=(c["code"] == correct_id)
        ))
        
    landmark_name = landmark["name"].get(lang, landmark["name"]["en"])
    hint_dict = landmark.get("hint") or landmark.get("clue") or {}
    hint = hint_dict.get(lang, hint_dict.get("en", ""))
    prompt = t("question_landmark", lang, landmark=landmark_name)
    target_country_name = target_country["name"].get(lang, target_country["name"]["en"])
    city_name = landmark.get("city", {}).get(lang, landmark.get("city", {}).get("en", ""))
    
    return Question(
        mode="landmark",
        prompt=prompt,
        options=options,
        correct_option_id=correct_id,
        correct_answer_text=f"{target_country.get('flag_emoji', '')} {target_country_name} ({city_name})" if city_name else f"{target_country.get('flag_emoji', '')} {target_country_name}",
        media_url=landmark.get("image_url"),
        media_type="photo",
        extra_info=f"💡 <i>{hint}</i>" if hint else None,
        country_code=country_code,
        hint_text=hint
    )


def generate_higher_lower_question(lang: str = "en") -> Question:
    """Generate a Higher or Lower question comparing Population or Land Area."""
    compare_type = random.choice(["population", "area"])
    c1, c2 = random.sample(COUNTRIES, 2)
    
    # Avoid ties
    if compare_type == "population":
        while c1["population"] == c2["population"]:
            c1, c2 = random.sample(COUNTRIES, 2)
        v1, v2 = c1["population"], c2["population"]
        larger = c1 if v1 > v2 else c2
        prompt_key = "question_higher_lower_population"
    else:
        while c1["area_sq_km"] == c2["area_sq_km"]:
            c1, c2 = random.sample(COUNTRIES, 2)
        v1, v2 = c1["area_sq_km"], c2["area_sq_km"]
        larger = c1 if v1 > v2 else c2
        prompt_key = "question_higher_lower_area"

    c1_name = f"{c1['flag_emoji']} {c1['name'].get(lang, c1['name']['en'])}"
    c2_name = f"{c2['flag_emoji']} {c2['name'].get(lang, c2['name']['en'])}"
    
    prompt = t(prompt_key, lang, c1=c1_name, c2=c2_name)
    
    options = [
        QuestionOption(id="c1", text=f"🅰️ {c1_name}", is_correct=(larger == c1)),
        QuestionOption(id="c2", text=f"🅱️ {c2_name}", is_correct=(larger == c2)),
    ]
    
    if compare_type == "population":
        extra = t("higher_lower_stat_pop", lang, c1=c1_name, v1=c1["population"], c2=c2_name, v2=c2["population"])
    else:
        extra = t("higher_lower_stat_area", lang, c1=c1_name, v1=c1["area_sq_km"], c2=c2_name, v2=c2["area_sq_km"])
        
    larger_name = f"{larger['flag_emoji']} {larger['name'].get(lang, larger['name']['en'])}"
    
    return Question(
        mode="higher_lower",
        prompt=prompt,
        options=options,
        correct_option_id="c1" if larger == c1 else "c2",
        correct_answer_text=larger_name,
        extra_info=extra,
        country_code=larger["code"],
        hint_text=f"Capital: {larger['capital'].get(lang, larger['capital']['en'])}"
    )

def generate_coat_of_arms_question(lang: str = "en") -> Question:
    """Generate a Coat of Arms guessing question."""
    # Filter countries with coat_of_arms_url
    candidates = [c for c in COUNTRIES if c.get("coat_of_arms_url")]
    target = random.choice(candidates)
    distractors = [c for c in COUNTRIES if c["code"] != target["code"]]
    sampled = random.sample(distractors, 3)
    
    choices = [target] + sampled
    random.shuffle(choices)
    
    options = []
    correct_id = target["code"]
    for c in choices:
        c_name = c["name"].get(lang, c["name"]["en"])
        options.append(QuestionOption(
            id=c["code"],
            text=f"{c['flag_emoji']} {c_name}",
            is_correct=(c["code"] == correct_id)
        ))
        
    target_name = target["name"].get(lang, target["name"]["en"])
    prompt = t("question_coat_of_arms", lang)
    
    return Question(
        mode="coat_of_arms",
        prompt=prompt,
        options=options,
        correct_option_id=correct_id,
        correct_answer_text=f"{target['flag_emoji']} {target_name}",
        media_url=target["coat_of_arms_url"],
        media_type="photo",
        country_code=target["code"],
        hint_text=f"Continent: {target['continent'].get(lang, target['continent']['en'])} | Capital: {target['capital'].get(lang, target['capital']['en'])}"
    )

def generate_streetview_question(lang: str = "en") -> Question:
    """Generate a Street View GeoGuessr question: guess country from street photo."""
    target_sv = random.choice(STREETVIEWS)
    country_code = target_sv["country_code"]
    target_country = next((c for c in COUNTRIES if c["code"] == country_code), None)
    if not target_country:
        target_country = {
            "code": country_code,
            "name": {"en": "Target", "ru": "Цель", "uz": "Nishon"},
            "flag_emoji": "🌐",
            "capital": {"en": "Capital"},
            "continent": {"en": "World", "ru": "Мир", "uz": "Dunyo"}
        }

    distractors = [c for c in COUNTRIES if c["code"] != country_code]
    sampled_distractors = random.sample(distractors, 3)
    choices = [target_country] + sampled_distractors
    random.shuffle(choices)

    options = []
    correct_id = country_code
    for c in choices:
        c_name = c["name"].get(lang, c["name"]["en"])
        options.append(QuestionOption(
            id=c["code"],
            text=f"{c.get('flag_emoji', '🌐')} {c_name}",
            is_correct=(c["code"] == correct_id)
        ))

    target_name = target_country["name"].get(lang, target_country["name"]["en"])
    loc_title = target_sv.get("location", {}).get(lang, target_sv.get("location", {}).get("en", ""))
    maps_link = target_sv.get("maps_url") or f"https://www.google.com/maps?q={target_sv['lat']},{target_sv['lng']}"
    maps_text = t("streetview_view_maps", lang)

    driving_side = target_sv.get("driving_side", "right")
    ds_str = ("Right" if driving_side == "right" else "Left") if lang == "en" else (("правостороннее" if driving_side == "right" else "левостороннее") if lang == "ru" else ("o'ng" if driving_side == "right" else "chap"))
    continent = target_country["continent"].get(lang, target_country["continent"]["en"])

    hint = t("solo_hint_streetview", lang, driving_side=ds_str, continent=continent)
    prompt = t("question_streetview", lang)

    return Question(
        mode="streetview",
        prompt=prompt,
        options=options,
        correct_option_id=correct_id,
        correct_answer_text=f"{target_country.get('flag_emoji', '')} {target_name}",
        media_url=target_sv.get("image_url"),
        media_type="photo",
        extra_info=f"📍 {loc_title}\n🗺 <a href=\"{maps_link}\">{maps_text}</a>",
        country_code=country_code,
        hint_text=hint
    )

def generate_question(mode: str = "mix", lang: str = "en") -> Question:
    """
    Generate question based on specified game mode.
    Modes: 'flag', 'capital', 'landmark', 'higher_lower', 'coat_of_arms', 'streetview', 'mix'
    """
    if mode == "mix":
        selected_mode = random.choice(["flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview"])
    else:
        selected_mode = mode
        
    if selected_mode == "flag":
        return generate_flag_question(lang)
    elif selected_mode == "capital":
        return generate_capital_question(lang)
    elif selected_mode == "landmark":
        return generate_landmark_question(lang)
    elif selected_mode == "higher_lower":
        return generate_higher_lower_question(lang)
    elif selected_mode == "coat_of_arms":
        return generate_coat_of_arms_question(lang)
    elif selected_mode == "streetview":
        return generate_streetview_question(lang)
    else:
        return generate_flag_question(lang)
