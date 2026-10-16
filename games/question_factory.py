"""
Question Factory for GeoGuru & GeoGuessr Bot.
Generates balanced, randomized questions for all supported game modes.
"""

import random
from typing import Optional, Set, List
from gamedata.countries import COUNTRIES, get_country
from gamedata.landmarks import LANDMARKS
from gamedata.streetviews import STREETVIEWS, get_random_streetview
from gamedata.fun_facts import get_fun_fact
from gamedata.emojis import EMOJI_RIDDLES, get_emoji_riddle
from gamedata.contours import CONTOUR_DATA, get_contour_url, get_contour_info
from locales.i18n import t
from .models import Question, GameMode

def _matches_continent(country_dict: dict, continent: Optional[str]) -> bool:
    """Check if country belongs to specified continent."""
    if not continent or continent.lower() in ("all", "world", "dunyo", "мир"):
        return True
    c_cont = country_dict.get("continent", {}).get("en", "").lower()
    cont = continent.lower()
    if cont == "asia":
        return "asia" in c_cont
    elif cont == "europe":
        return "europe" in c_cont
    elif cont == "africa":
        return "africa" in c_cont
    elif cont in ("americas", "america", "north america", "south america"):
        return "america" in c_cont
    elif cont == "oceania":
        return "oceania" in c_cont
    return True

class QuestionFactory:
    @staticmethod
    def generate(
        mode: str,
        lang: str = "en",
        exclude_codes: Optional[Set[str]] = None,
        continent: Optional[str] = None
    ) -> Question:
        if mode == GameMode.MIX:
            chosen_mode = random.choice([
                GameMode.FLAG,
                GameMode.CAPITAL,
                GameMode.LANDMARK,
                GameMode.HIGHER_LOWER,
                GameMode.COAT_OF_ARMS,
                GameMode.STREETVIEW,
                GameMode.EMOJI,
                GameMode.CONTOUR,
            ])
            return QuestionFactory.generate(chosen_mode, lang, exclude_codes, continent)
        
        if mode == GameMode.FLAG:
            return QuestionFactory._gen_flag(lang, exclude_codes, continent)
        elif mode == GameMode.CAPITAL:
            return QuestionFactory._gen_capital(lang, exclude_codes, continent)
        elif mode == GameMode.LANDMARK:
            return QuestionFactory._gen_landmark(lang, exclude_codes, continent)
        elif mode == GameMode.HIGHER_LOWER:
            return QuestionFactory._gen_higher_lower(lang, exclude_codes, continent)
        elif mode == GameMode.COAT_OF_ARMS:
            return QuestionFactory._gen_coat_of_arms(lang, exclude_codes, continent)
        elif mode == GameMode.STREETVIEW:
            return QuestionFactory._gen_streetview(lang, exclude_codes, continent)
        elif mode == GameMode.EMOJI:
            return QuestionFactory._gen_emoji(lang, exclude_codes, continent)
        elif mode == GameMode.CONTOUR:
            return QuestionFactory._gen_contour(lang, exclude_codes, continent)
        else:
            return QuestionFactory._gen_flag(lang, exclude_codes, continent)

    @staticmethod
    def _get_country_candidates(
        exclude_codes: Optional[Set[str]] = None,
        continent: Optional[str] = None
    ) -> List[dict]:
        pool = COUNTRIES
        if continent and continent.lower() not in ("all", "world"):
            filtered_cont = [c for c in COUNTRIES if _matches_continent(c, continent)]
            if len(filtered_cont) >= 4:
                pool = filtered_cont
        if exclude_codes:
            filtered_exc = [c for c in pool if c["code"] not in exclude_codes]
            if len(filtered_exc) >= 4:
                pool = filtered_exc
        return pool

    @staticmethod
    def _gen_flag(
        lang: str,
        exclude_codes: Optional[Set[str]],
        continent: Optional[str] = None
    ) -> Question:
        pool = QuestionFactory._get_country_candidates(exclude_codes, continent)
        target = random.choice(pool)
        
        # 3 distractors from candidate pool or same continent
        other_countries = [c for c in pool if c["code"] != target["code"]]
        if len(other_countries) < 3:
            other_countries = [c for c in COUNTRIES if c["code"] != target["code"]]
        distractors = random.sample(other_countries, 3)
        
        options = [d["name"].get(lang, d["name"]["en"]) for d in distractors]
        correct_name = target["name"].get(lang, target["name"]["en"])
        
        options.append(correct_name)
        random.shuffle(options)
        correct_index = options.index(correct_name)

        text = t("question_flag", lang)
        fun_fact = get_fun_fact(target["code"], lang)

        return Question(
            mode=GameMode.FLAG,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=correct_name,
            country_code=target["code"],
            image_url=target.get("flag_url"),
            fun_fact=fun_fact
        )

    @staticmethod
    def _gen_capital(
        lang: str,
        exclude_codes: Optional[Set[str]],
        continent: Optional[str] = None
    ) -> Question:
        pool = QuestionFactory._get_country_candidates(exclude_codes, continent)
        target = random.choice(pool)
        other_countries = [c for c in pool if c["code"] != target["code"]]
        if len(other_countries) < 3:
            other_countries = [c for c in COUNTRIES if c["code"] != target["code"]]
        distractors = random.sample(other_countries, 3)

        # 50% ask capital of country, 50% ask country of capital
        if random.random() < 0.5:
            target_country_name = target["name"].get(lang, target["name"]["en"])
            text = t("question_capital_of_country", lang, country=target_country_name)
            correct_capital = target["capital"].get(lang, target["capital"]["en"])
            options = [d["capital"].get(lang, d["capital"]["en"]) for d in distractors]
            options.append(correct_capital)
            random.shuffle(options)
            correct_index = options.index(correct_capital)
            answer_text = correct_capital
        else:
            target_cap_name = target["capital"].get(lang, target["capital"]["en"])
            text = t("question_country_of_capital", lang, capital=target_cap_name)
            correct_country = target["name"].get(lang, target["name"]["en"])
            options = [d["name"].get(lang, d["name"]["en"]) for d in distractors]
            options.append(correct_country)
            random.shuffle(options)
            correct_index = options.index(correct_country)
            answer_text = correct_country

        fun_fact = get_fun_fact(target["code"], lang)

        return Question(
            mode=GameMode.CAPITAL,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=answer_text,
            country_code=target["code"],
            image_url=target.get("flag_url"),
            fun_fact=fun_fact
        )

    @staticmethod
    def _gen_landmark(
        lang: str,
        exclude_codes: Optional[Set[str]],
        continent: Optional[str] = None
    ) -> Question:
        lm_pool = LANDMARKS
        if continent and continent.lower() not in ("all", "world"):
            filtered_cont = [l for l in LANDMARKS if _matches_continent(get_country(l["country_code"]) or {}, continent)]
            if len(filtered_cont) >= 4:
                lm_pool = filtered_cont
        if exclude_codes:
            filtered = [l for l in lm_pool if l["country_code"] not in exclude_codes]
            if len(filtered) >= 4:
                lm_pool = filtered

        target_lm = random.choice(lm_pool)
        target_country = get_country(target_lm["country_code"])
        if not target_country:
            target_country = COUNTRIES[0]

        other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"] and _matches_continent(c, continent)]
        if len(other_countries) < 3:
            other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"]]
        distractors = random.sample(other_countries, 3)

        correct_name = target_country["name"].get(lang, target_country["name"]["en"])
        options = [d["name"].get(lang, d["name"]["en"]) for d in distractors]
        options.append(correct_name)
        random.shuffle(options)
        correct_index = options.index(correct_name)

        lm_name = target_lm["name"].get(lang, target_lm["name"]["en"])
        clue = target_lm["clue"].get(lang, target_lm["clue"]["en"])
        
        text = f"{t('question_landmark', lang, landmark=lm_name)}\n\n💡 <i>{clue}</i>"
        fun_fact = target_lm["fun_fact"].get(lang, target_lm["fun_fact"]["en"])

        return Question(
            mode=GameMode.LANDMARK,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=correct_name,
            country_code=target_country["code"],
            image_url=target_lm.get("image_url"),
            fun_fact=f"🏛 {lm_name}: {fun_fact}"
        )

    @staticmethod
    def _gen_higher_lower(
        lang: str,
        exclude_codes: Optional[Set[str]],
        continent: Optional[str] = None
    ) -> Question:
        pool = QuestionFactory._get_country_candidates(exclude_codes, continent)
        if len(pool) < 2:
            pool = COUNTRIES
        c1, c2 = random.sample(pool, 2)
        c1_name = c1["name"].get(lang, c1["name"]["en"])
        c2_name = c2["name"].get(lang, c2["name"]["en"])

        compare_population = random.random() < 0.5
        if compare_population:
            text = t("question_higher_lower_population", lang, c1=c1_name, c2=c2_name)
            if c1["population"] >= c2["population"]:
                correct_index = 0
                correct_answer = c1_name
            else:
                correct_index = 1
                correct_answer = c2_name
            stat_info = t("higher_lower_stat_pop", lang, c1=c1_name, v1=c1["population"], c2=c2_name, v2=c2["population"])
        else:
            text = t("question_higher_lower_area", lang, c1=c1_name, c2=c2_name)
            if c1["area_sq_km"] >= c2["area_sq_km"]:
                correct_index = 0
                correct_answer = c1_name
            else:
                correct_index = 1
                correct_answer = c2_name
            stat_info = t("higher_lower_stat_area", lang, c1=c1_name, v1=c1["area_sq_km"], c2=c2_name, v2=c2["area_sq_km"])

        options = [f"🅰️ {c1_name}", f"🅱️ {c2_name}"]
        correct_answer = options[correct_index]
        target_country = c1 if correct_index == 0 else c2

        return Question(
            mode=GameMode.HIGHER_LOWER,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=correct_answer,
            country_code=target_country["code"],
            fun_fact=stat_info,
            stat_info=stat_info
        )

    @staticmethod
    def _gen_coat_of_arms(
        lang: str,
        exclude_codes: Optional[Set[str]],
        continent: Optional[str] = None
    ) -> Question:
        pool = [c for c in COUNTRIES if c.get("coat_of_arms_url") and _matches_continent(c, continent)]
        if len(pool) < 4:
            pool = [c for c in COUNTRIES if c.get("coat_of_arms_url")]
        if exclude_codes:
            filtered = [c for c in pool if c["code"] not in exclude_codes]
            if len(filtered) >= 4:
                pool = filtered

        target = random.choice(pool)
        other_countries = [c for c in pool if c["code"] != target["code"]]
        if len(other_countries) < 3:
            other_countries = [c for c in COUNTRIES if c["code"] != target["code"]]
        distractors = random.sample(other_countries, 3)

        correct_name = target["name"].get(lang, target["name"]["en"])
        options = [d["name"].get(lang, d["name"]["en"]) for d in distractors]
        options.append(correct_name)
        random.shuffle(options)
        correct_index = options.index(correct_name)

        text = t("question_coat_of_arms", lang)
        fun_fact = get_fun_fact(target["code"], lang)

        return Question(
            mode=GameMode.COAT_OF_ARMS,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=correct_name,
            country_code=target["code"],
            image_url=target.get("coat_of_arms_url"),
            fun_fact=fun_fact
        )

    @staticmethod
    def _gen_streetview(
        lang: str,
        exclude_codes: Optional[Set[str]] = None,
        continent: Optional[str] = None
    ) -> Question:
        sv_pool = STREETVIEWS
        if continent and continent.lower() not in ("all", "world"):
            filtered_cont = [s for s in STREETVIEWS if _matches_continent(get_country(s["country_code"]) or {}, continent)]
            if len(filtered_cont) >= 4:
                sv_pool = filtered_cont
        if exclude_codes:
            filtered = [s for s in sv_pool if s["country_code"] not in exclude_codes]
            if len(filtered) >= 4:
                sv_pool = filtered

        target_sv = random.choice(sv_pool)
        target_country = get_country(target_sv["country_code"])
        if not target_country:
            target_country = COUNTRIES[0]

        other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"] and _matches_continent(c, continent)]
        if len(other_countries) < 3:
            other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"]]
        distractors = random.sample(other_countries, 3)

        correct_name = target_country["name"].get(lang, target_country["name"]["en"])
        options = [d["name"].get(lang, d["name"]["en"]) for d in distractors]
        options.append(correct_name)
        random.shuffle(options)
        correct_index = options.index(correct_name)

        loc_title = target_sv.get("location", {}).get(lang, target_sv.get("location", {}).get("en", ""))
        maps_link = target_sv.get("maps_url") or f"https://www.google.com/maps?q={target_sv['lat']},{target_sv['lng']}"
        maps_btn_text = t("streetview_view_maps", lang)

        clue_hint = target_sv.get("clues", {}).get("hint", {}).get(lang, target_sv.get("clues", {}).get("hint", {}).get("en", ""))

        fun_fact_parts = [f"📍 {loc_title}", f"🗺️ <a href=\"{maps_link}\">{maps_btn_text}</a>"]
        if clue_hint:
            fun_fact_parts.append(f"💡 {clue_hint}")
        fun_fact = "\n".join(fun_fact_parts)

        text = t("question_streetview", lang)

        return Question(
            mode=GameMode.STREETVIEW,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=correct_name,
            country_code=target_country["code"],
            image_url=target_sv.get("image_url"),
            fun_fact=fun_fact,
            maps_url=maps_link,
            location_title=loc_title,
            driving_side=target_sv.get("driving_side", "right")
        )

    @staticmethod
    def _gen_emoji(
        lang: str,
        exclude_codes: Optional[Set[str]] = None,
        continent: Optional[str] = None
    ) -> Question:
        pool = EMOJI_RIDDLES
        if continent and continent.lower() not in ("all", "world"):
            filtered_cont = [r for r in EMOJI_RIDDLES if _matches_continent(get_country(r["code"]) or {}, continent)]
            if len(filtered_cont) >= 4:
                pool = filtered_cont
        if exclude_codes:
            filtered_exc = [r for r in pool if r["code"] not in exclude_codes]
            if len(filtered_exc) >= 4:
                pool = filtered_exc

        target_riddle = random.choice(pool)
        target_country = get_country(target_riddle["code"]) or COUNTRIES[0]

        other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"] and _matches_continent(c, continent)]
        if len(other_countries) < 3:
            other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"]]
        distractors = random.sample(other_countries, 3)

        correct_name = target_country["name"].get(lang, target_country["name"]["en"])
        options = [d["name"].get(lang, d["name"]["en"]) for d in distractors]
        options.append(correct_name)
        random.shuffle(options)
        correct_index = options.index(correct_name)

        hint_text = target_riddle.get("hint", {}).get(lang, target_riddle.get("hint", {}).get("en", ""))
        text = t("question_emoji", lang, emojis=target_riddle["emojis"], hint=hint_text)
        fun_fact = get_fun_fact(target_country["code"], lang)

        return Question(
            mode=GameMode.EMOJI,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=correct_name,
            country_code=target_country["code"],
            image_url=None,
            fun_fact=fun_fact
        )

    @staticmethod
    def _gen_contour(
        lang: str,
        exclude_codes: Optional[Set[str]] = None,
        continent: Optional[str] = None
    ) -> Question:
        pool = CONTOUR_DATA
        if continent and continent.lower() not in ("all", "world"):
            filtered_cont = [c for c in CONTOUR_DATA if _matches_continent(get_country(c["code"]) or {}, continent)]
            if len(filtered_cont) >= 4:
                pool = filtered_cont
        if exclude_codes:
            filtered_exc = [c for c in pool if c["code"] not in exclude_codes]
            if len(filtered_exc) >= 4:
                pool = filtered_exc

        target_contour = random.choice(pool)
        target_country = get_country(target_contour["code"]) or COUNTRIES[0]

        other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"] and _matches_continent(c, continent)]
        if len(other_countries) < 3:
            other_countries = [c for c in COUNTRIES if c["code"] != target_country["code"]]
        distractors = random.sample(other_countries, 3)

        correct_name = target_country["name"].get(lang, target_country["name"]["en"])
        options = [d["name"].get(lang, d["name"]["en"]) for d in distractors]
        options.append(correct_name)
        random.shuffle(options)
        correct_index = options.index(correct_name)

        contour_url = get_contour_url(target_country["code"])
        trivia_text = target_contour.get("shape_trivia", {}).get(lang, target_contour.get("shape_trivia", {}).get("en", ""))
        text = t("question_contour", lang)
        fun_fact = trivia_text or get_fun_fact(target_country["code"], lang)

        return Question(
            mode=GameMode.CONTOUR,
            text=text,
            options=options,
            correct_index=correct_index,
            correct_answer=correct_name,
            country_code=target_country["code"],
            image_url=contour_url,
            fun_fact=fun_fact
        )

    @staticmethod
    def create_streetview_question(
        lang: str = "en",
        exclude_codes: Optional[Set[str]] = None,
        continent: Optional[str] = None
    ) -> Question:
        return QuestionFactory._gen_streetview(lang, exclude_codes, continent)


def create_streetview_question(
    lang: str = "en",
    exclude_codes: Optional[Set[str]] = None,
    continent: Optional[str] = None
) -> Question:
    """Generate a streetview question with 4 country options (1 correct + 3 random distractors)."""
    return QuestionFactory.create_streetview_question(lang, exclude_codes, continent)

