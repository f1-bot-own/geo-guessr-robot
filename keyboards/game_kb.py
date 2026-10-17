"""
Game Keyboards for Group Matches, Setup, Solo, and Duels.
"""

from typing import List, Set, Optional, Dict, Any
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from locales.i18n import t
from games.models import GameMode

def get_setup_kb(
    session_id: str,
    mode: str = "mix",
    rounds: int = 5,
    round_time: int = 30,
    lang: str = "en",
    input_mode: str = "both",
    continent: str = "all",
    selected_modes: Optional[List[str]] = None,
    is_blur: bool = False,
    view_mode: str = "categories"
) -> InlineKeyboardMarkup:
    """Generate game setup parameters keyboard with clean category hubs or detailed mode checkboxes."""
    if selected_modes is None:
        if mode and mode not in ("mix", "blur"):
            selected_modes = [mode]
        elif mode == "blur":
            selected_modes = []
            is_blur = True
        else:
            selected_modes = []

    all_cat_modes = [
        "zakovat", "astronomy", "science", "history", "literature", "art", "nature", "logic_math",
        "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview",
        "emoji", "contour", "president", "historical", "celebrity", "logo"
    ]

    hub_modes_map = {
        "zakovat": ["zakovat", "black_box", "deduction", "world_intellect", "blitz"],
        "geography": [
            "flag", "capital", "landmark", "higher_lower", "coat_of_arms",
            "streetview", "emoji", "contour", "geo_mix"
        ],
        "cosmos_nature": ["astronomy", "nature", "telescope_zoom", "macro_texture", "human_anatomy", "cosmos_nature_mix"],
        "science_logic": ["science", "logic_math", "elements", "flash_math", "odd_one_out", "science_logic_mix"],
        "history_culture": ["history", "literature", "art", "quotes", "art_fragment", "history_culture_mix"],
        "people_brands": ["president", "historical", "celebrity", "logo", "person"],
    }

    t30_prefix = "✅ " if round_time == 30 else ""
    t60_prefix = "✅ " if round_time == 60 else ""

    btn_buttons_pfx = "✅ " if input_mode == "buttons" else ""
    btn_text_pfx = "✅ " if input_mode == "text" else ""
    btn_both_pfx = "✅ " if input_mode == "both" else ""

    blur_status = t("status_enabled", lang) if is_blur else t("status_disabled", lang)
    blur_btn_text = f"🔍 Blur: {blur_status}"

    common_bottom_rows = [
        # Continent Filter button
        [
            InlineKeyboardButton(
                text=t("btn_continent", lang, continent=t(f"filter_continent_{continent}", lang)),
                callback_data=f"setup:continent:{session_id}"
            )
        ],
        # Explicit 30s / 60s timer buttons
        [
            InlineKeyboardButton(
                text=f"{t30_prefix}{t('btn_timer_30s', lang)}",
                callback_data=f"setup:time:30:{session_id}"
            ),
            InlineKeyboardButton(
                text=f"{t60_prefix}{t('btn_timer_60s', lang)}",
                callback_data=f"setup:time:60:{session_id}"
            )
        ],
        # Input mode selection: Buttons Only / Text Only / Both
        [
            InlineKeyboardButton(
                text=f"{btn_buttons_pfx}{t('btn_input_buttons', lang)}",
                callback_data=f"setup:input:buttons:{session_id}"
            ),
            InlineKeyboardButton(
                text=f"{btn_text_pfx}{t('btn_input_text', lang)}",
                callback_data=f"setup:input:text:{session_id}"
            ),
            InlineKeyboardButton(
                text=f"{btn_both_pfx}{t('btn_input_both', lang)}",
                callback_data=f"setup:input:both:{session_id}"
            )
        ],
        # Rounds selector
        [
            InlineKeyboardButton(
                text=t("btn_rounds", lang, rounds=rounds),
                callback_data=f"setup:rounds:{session_id}"
            )
        ],
        # Launch & Cancel
        [
            InlineKeyboardButton(
                text=t("btn_start_now", lang),
                callback_data=f"setup:start:{session_id}"
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_cancel", lang),
                callback_data=f"setup:cancel:{session_id}"
            )
        ]
    ]

    if view_mode == "detailed":
        def mode_btn(m_code: str):
            if m_code == "mix":
                is_sel = (
                    "mix" in (selected_modes or []) or
                    (bool(selected_modes) and set(all_cat_modes).issubset(set(selected_modes)))
                )
            else:
                is_sel = m_code in (selected_modes or []) and "mix" not in (selected_modes or [])
            prefix = "✅ " if is_sel else ""
            return InlineKeyboardButton(
                text=f"{prefix}{t(f'mode_{m_code}', lang)}",
                callback_data=f"setup:mode:{m_code}:{session_id}"
            )

        back_to_hubs_text = {
            "uz": "📁 Toifalar bo'yicha ko'rish",
            "ru": "📁 Просмотр по категориям",
            "en": "📁 View by Categories"
        }.get(lang, "📁 View by Categories")

        detailed_keyboard = [
            [InlineKeyboardButton(text=back_to_hubs_text, callback_data=f"setup:view:categories:{session_id}")],
            [mode_btn("zakovat")],
            [mode_btn("astronomy"), mode_btn("science")],
            [mode_btn("history"), mode_btn("literature")],
            [mode_btn("art"), mode_btn("nature")],
            [mode_btn("logic_math"), mode_btn("mix")],
            [mode_btn("flag"), mode_btn("capital")],
            [mode_btn("landmark"), mode_btn("higher_lower")],
            [mode_btn("coat_of_arms"), mode_btn("streetview")],
            [mode_btn("emoji"), mode_btn("contour")],
            [mode_btn("president"), mode_btn("historical")],
            [mode_btn("celebrity"), mode_btn("logo")],
            [
                InlineKeyboardButton(text=t("btn_select_all_modes", lang), callback_data=f"setup:all:{session_id}"),
                InlineKeyboardButton(text=t("btn_only_flags", lang), callback_data=f"setup:flags_only:{session_id}")
            ],
            [InlineKeyboardButton(text=blur_btn_text, callback_data=f"setup:blur:{session_id}")]
        ] + common_bottom_rows
        return InlineKeyboardMarkup(inline_keyboard=detailed_keyboard)

    if view_mode.startswith("hub:"):
        hub_code = view_mode.split(":", 1)[1]
        hub_data = CATEGORY_HUBS_INFO.get(hub_code)
        if hub_data:
            buttons_raw = hub_data["buttons"]

            def is_sub_selected(code: str) -> bool:
                if not selected_modes:
                    return False
                if "mix" in selected_modes or set(all_cat_modes).issubset(set(selected_modes)):
                    return True
                if code in selected_modes:
                    return True
                hub_mix_code = {
                    "zakovat": "zakovat",
                    "geography": "geo_mix",
                    "cosmos_nature": "cosmos_nature_mix",
                    "science_logic": "science_logic_mix",
                    "history_culture": "history_culture_mix",
                    "people_brands": "person"
                }.get(hub_code)
                if hub_mix_code and hub_mix_code in selected_modes:
                    return True
                if code in ("zakovat", "geo_mix", "cosmos_nature_mix", "science_logic_mix", "history_culture_mix", "person"):
                    sub_c = [c for c, _ in buttons_raw if c != code]
                    if sub_c and set(sub_c).issubset(set(selected_modes)):
                        return True
                return False

            hub_rows = []
            i = 0
            while i < len(buttons_raw):
                c1, n1 = buttons_raw[i]
                is_mix_1 = "mix" in c1.lower() or c1 in ("zakovat", "person")
                if is_mix_1 or i == len(buttons_raw) - 1:
                    pfx = "✅ " if is_sub_selected(c1) else ""
                    hub_rows.append([
                        InlineKeyboardButton(
                            text=f"{pfx}{n1.get(lang, n1.get('en', c1))}",
                            callback_data=f"setup:mode:{c1}:{session_id}"
                        )
                    ])
                    i += 1
                else:
                    c2, n2 = buttons_raw[i + 1]
                    is_mix_2 = "mix" in c2.lower() or c2 in ("zakovat", "person")
                    if is_mix_2:
                        pfx1 = "✅ " if is_sub_selected(c1) else ""
                        hub_rows.append([
                            InlineKeyboardButton(
                                text=f"{pfx1}{n1.get(lang, n1.get('en', c1))}",
                                callback_data=f"setup:mode:{c1}:{session_id}"
                            )
                        ])
                        i += 1
                    else:
                        pfx1 = "✅ " if is_sub_selected(c1) else ""
                        pfx2 = "✅ " if is_sub_selected(c2) else ""
                        hub_rows.append([
                            InlineKeyboardButton(
                                text=f"{pfx1}{n1.get(lang, n1.get('en', c1))}",
                                callback_data=f"setup:mode:{c1}:{session_id}"
                            ),
                            InlineKeyboardButton(
                                text=f"{pfx2}{n2.get(lang, n2.get('en', c2))}",
                                callback_data=f"setup:mode:{c2}:{session_id}"
                            )
                        ])
                        i += 2

            back_label = {
                "uz": "🔙 📁 Barcha toifalar",
                "ru": "🔙 📁 Все категории",
                "en": "🔙 📁 All Categories"
            }.get(lang, "🔙 📁 All Categories")

            hub_rows.append([
                InlineKeyboardButton(text=back_label, callback_data=f"setup:hub:main:{session_id}")
            ])
            return InlineKeyboardMarkup(inline_keyboard=hub_rows + common_bottom_rows)

    # DEFAULT: CATEGORY HUBS VIEW
    zako_title = CATEGORY_HUBS_INFO["zakovat"]["title"].get(lang, "Zakovat Club (500)")
    geo_title = CATEGORY_HUBS_INFO["geography"]["title"].get(lang, "Geography (1,000+)")
    cos_title = CATEGORY_HUBS_INFO["cosmos_nature"]["title"].get(lang, "Cosmos & Nature (800)")
    sci_title = CATEGORY_HUBS_INFO["science_logic"]["title"].get(lang, "Science & Logic (800)")
    his_title = CATEGORY_HUBS_INFO["history_culture"]["title"].get(lang, "History & Art (1,200)")
    peo_title = CATEGORY_HUBS_INFO["people_brands"]["title"].get(lang, "People & Brands")

    def hub_btn(hub_code: str, title: str, icon: str):
        target_modes = hub_modes_map.get(hub_code, [])
        is_sel = (
            "mix" in (selected_modes or []) or
            (bool(selected_modes) and set(all_cat_modes).issubset(set(selected_modes))) or
            any(m in (selected_modes or []) for m in target_modes)
        )
        pfx = "✅ " if is_sel else ""
        return InlineKeyboardButton(
            text=f"{pfx}{icon} {title}",
            callback_data=f"setup:hub:{hub_code}:{session_id}"
        )

    is_super_mix = (
        "mix" in (selected_modes or []) or
        (bool(selected_modes) and set(all_cat_modes).issubset(set(selected_modes)))
    )
    mix_pfx = "✅ " if is_super_mix else ""
    super_mix_title = {
        "uz": f"{mix_pfx}🎲 SUPER MIX (Barchasi - 4,000+)",
        "ru": f"{mix_pfx}🎲 SUPER MIX (Все темы - 4,000+)",
        "en": f"{mix_pfx}🎲 SUPER MIX (All Subjects - 4,000+)"
    }.get(lang, f"{mix_pfx}🎲 SUPER MIX (4,000+)")

    detail_btn_text = {
        "uz": "📋 Aniq yo'nalishlar (Batafsil tanlash)",
        "ru": "📋 Выбрать точные направления",
        "en": "📋 Select Specific Sub-modes"
    }.get(lang, "📋 Select Specific Sub-modes")

    category_keyboard = [
        # Flagship Zakovat Hub
        [hub_btn("zakovat", zako_title, "🎓")],
        # Geography & Cosmos Hubs
        [hub_btn("geography", geo_title, "🌍"), hub_btn("cosmos_nature", cos_title, "🌌")],
        # Science & History Hubs
        [hub_btn("science_logic", sci_title, "🔬"), hub_btn("history_culture", his_title, "📜")],
        # People Hub & Blur Toggle
        [hub_btn("people_brands", peo_title, "👑"), InlineKeyboardButton(text=blur_btn_text, callback_data=f"setup:blur:{session_id}")],
        # Super Mix
        [InlineKeyboardButton(text=super_mix_title, callback_data=f"setup:mode:mix:{session_id}")],
        # Detailed mode view toggle
        [InlineKeyboardButton(text=detail_btn_text, callback_data=f"setup:view:detailed:{session_id}")]
    ] + common_bottom_rows
    return InlineKeyboardMarkup(inline_keyboard=category_keyboard)

CATEGORY_HUBS_INFO: Dict[str, Any] = {
    "zakovat": {
        "icon": "🎓",
        "title": {
            "uz": "Zakovat Klubi (500)",
            "ru": "Клуб Заковат (500)",
            "en": "Zakovat Club (500)"
        },
        "header": {
            "uz": "🎓 <b>Zakovat Intellektual Klubi (500 ta savol)</b>\n\nUshbu toifa ichida 4 xil noyob intellektual yo'nalish mavjud:\n\n• 📦 <b>Qora quti</b> (125 ta) — Sirli buyumni toping (javobdan so'ng rasm ochiladi)\n• 🔍 <b>Mantiq & Deduksiya</b> (125 ta) — 'X ni toping' va Sherlok Holms uslubidagi savollar\n• 🏛 <b>Jahon intellekti</b> (125 ta) — Falsafa, ilm-fan va Islom oltin davri durdonalari\n• ⚡ <b>Zakovat Blits</b> (125 ta) — O'tkir zehn va tezkor intellektual savollar\n• 🎲 <b>Zakovat Mix</b> (500 ta) — Barcha zakovat savollari aralash\n\n👇 <b>O'ynash uchun yo'nalishni tanlang:</b>",
            "ru": "🎓 <b>Интеллектуальный Клуб Заковат (500 вопросов)</b>\n\nВ этой категории 4 уникальных интеллектуальных направления:\n\n• 📦 <b>Чёрный ящик</b> (125) — Угадайте скрытый предмет (фото откроется после ответа)\n• 🔍 <b>Дедукция и Логика</b> (125) — Вопросы стиля «Найдите X» и загадки Шерлока\n• 🏛 <b>Мировой Интеллект</b> (125) — Философия, наука и шедевры Золотого века\n• ⚡ <b>Заковат Блиц</b> (125) — Острый ум и быстрые вопросы\n• 🎲 <b>Заковат Микс</b> (500) — Все вопросы Заковат вперемешку\n\n👇 <b>Выберите направление для игры:</b>",
            "en": "🎓 <b>Zakovat Intellectual Club (500 Questions)</b>\n\nThis category contains 4 unique intellectual directions:\n\n• 📦 <b>Black Box</b> (125) — Guess the mystery object (photo revealed after answer)\n• 🔍 <b>Logic & Deduction</b> (125) — 'Find X' and Sherlock Holmes-style riddles\n• 🏛 <b>World Intellect</b> (125) — Philosophy, world science & Golden Age culture\n• ⚡ <b>Zakovat Blitz</b> (125) — Quick-witted trivia questions\n• 🎲 <b>Zakovat Mix</b> (500) — All Zakovat questions mixed\n\n👇 <b>Select a direction to play:</b>"
        },
        "buttons": [
            ("black_box", {"uz": "📦 Qora quti (125)", "ru": "📦 Чёрный ящик (125)", "en": "📦 Black Box (125)"}),
            ("deduction", {"uz": "🔍 Mantiq & Deduksiya (125)", "ru": "🔍 Дедукция (125)", "en": "🔍 Deduction (125)"}),
            ("world_intellect", {"uz": "🏛 Jahon intellekti (125)", "ru": "🏛 Мировой интеллект (125)", "en": "🏛 World Intellect (125)"}),
            ("blitz", {"uz": "⚡ Zakovat Blits (125)", "ru": "⚡ Заковат Блиц (125)", "en": "⚡ Zakovat Blitz (125)"}),
            ("zakovat", {"uz": "🎲 Zakovat Mix (500 ta barchasi)", "ru": "🎲 Заковат Микс (Все 500)", "en": "🎲 Zakovat Mix (All 500)"}),
        ]
    },
    "geography": {
        "icon": "🌍",
        "title": {
            "uz": "Geografiya (1,000+)",
            "ru": "География (1,000+)",
            "en": "Geography (1,000+)"
        },
        "header": {
            "uz": "🌍 <b>Geografiya & GeoGuessr (1,000+ ta savol)</b>\n\nDunyo davlatlari, madaniyati va xaritalari bo'yicha 8 xil yo'nalish:\n\n• 🏳️ <b>Bayroqlar</b> — Dunyo davlatlari bayroqlari\n• 🏛 <b>Poytaxtlar</b> — Davlatlarning rasmiy poytaxtlari\n• 📸 <b>Mashhur obidalar</b> — Dunyoning me'moriy diqqatga sazovor joylari\n• 📊 <b>Katta yoki Kichik</b> — Aholi va hududni solishtirish\n• 🛡 <b>Davlat gerblari</b> — Rasmiy davlat gerblari\n• 🗺️ <b>Street View</b> — Dunyo ko'chalaridan panoramik ko'rinish\n• 🧩 <b>Emoji jumboq</b> — Emojilar orqali davlatni topish\n• 🗺 <b>Davlat konturi</b> — Xaritadagi shakliga qarab topish\n• 🎲 <b>Geografiya Mix</b> — Barcha geografik savollar aralash\n\n👇 <b>O'ynash uchun yo'nalishni tanlang:</b>",
            "ru": "🌍 <b>География и GeoGuessr (1,000+ вопросов)</b>\n\n8 направлений по странам мира, культурам и картам:\n\n• 🏳️ <b>Флаги</b> — Флаги всех стран мира\n• 🏛 <b>Столицы</b> — Официальные столицы государств\n• 📸 <b>Достопримечательности</b> — Мировые памятники архитектуры\n• 📊 <b>Больше или меньше</b> — Сравнение населения и площади\n• 🛡 <b>Гербы стран</b> — Официальные гербы\n• 🗺️ <b>Street View</b> — Панорамы улиц со всего мира\n• 🧩 <b>Эмодзи-загадка</b> — Угадай страну по эмодзи\n• 🗺 <b>Контур страны</b> — Угадай страну по очертанию\n• 🎲 <b>География Микс</b> — Все вопросы географии вперемешку\n\n👇 <b>Выберите направление для игры:</b>",
            "en": "🌍 <b>Geography & GeoGuessr (1,000+ Questions)</b>\n\n8 directions across world nations, culture, and maps:\n\n• 🏳️ <b>Flags</b> — National flags of world countries\n• 🏛 <b>Capitals</b> — Official country capitals\n• 📸 <b>Landmarks</b> — Famous world landmarks\n• 📊 <b>Higher or Lower</b> — Comparing population and area\n• 🛡 <b>Coats of Arms</b> — Official coats of arms\n• 🗺️ <b>Street View</b> — Panoramic street exploration\n• 🧩 <b>Emoji Riddle</b> — Guess country from emoji clues\n• 🗺 <b>Country Contour</b> — Guess country by outline shape\n• 🎲 <b>Geography Mix</b> — All geography modes mixed\n\n👇 <b>Select a direction to play:</b>"
        },
        "buttons": [
            ("flag", {"uz": "🏳️ Bayroqlar", "ru": "🏳️ Флаги", "en": "🏳️ Flags"}),
            ("capital", {"uz": "🏛 Poytaxtlar", "ru": "🏛 Столицы", "en": "🏛 Capitals"}),
            ("landmark", {"uz": "📸 Mashhur obidalar", "ru": "📸 Достопримечательности", "en": "📸 Landmarks"}),
            ("higher_lower", {"uz": "📊 Katta yoki Kichik", "ru": "📊 Больше или меньше", "en": "📊 Higher or Lower"}),
            ("coat_of_arms", {"uz": "🛡 Davlat gerblari", "ru": "🛡 Гербы стран", "en": "🛡 Coats of Arms"}),
            ("streetview", {"uz": "🗺️ Street View", "ru": "🗺️ Просмотр улиц", "en": "🗺️ Street View"}),
            ("emoji", {"uz": "🧩 Emoji jumboq", "ru": "🧩 Эмодзи-загадки", "en": "🧩 Emoji Riddles"}),
            ("contour", {"uz": "🗺 Davlat konturi", "ru": "🗺 Контуры стран", "en": "🗺 Contours"}),
            ("geo_mix", {"uz": "🎲 Geografiya Mix (Barchasi)", "ru": "🎲 География Микс (Все)", "en": "🎲 Geography Mix (All)"}),
        ]
    },
    "cosmos_nature": {
        "icon": "🌌",
        "title": {
            "uz": "Koinot & Tabiat (800)",
            "ru": "Космос и Природа (800)",
            "en": "Cosmos & Nature (800)"
        },
        "header": {
            "uz": "🌌 <b>Koinot & Tabiat (800 ta savol)</b>\n\nFazo sirlari va yovvoyi tabiat mo'jizalari:\n\n• 🌌 <b>Astronomiya & Koinot</b> (400 ta) — Sayyoralar, tumanliklar, yulduz turkumlari\n• 🦁 <b>Tabiat & Biologiya</b> (400 ta) — Noyob hayvonlar, inson tanasi, o'simliklar\n• 🔭 <b>Teleskop & Planetalar</b> (100 ta) — James Webb va Hubble suratlari\n• 🐾 <b>Hayvonot olami & Makro</b> (100 ta) — Hayvon terisi/patlari makro suratlari\n• 🎲 <b>Koinot & Tabiat Mix</b> (800 ta) — Ikkala toifa aralash\n\n👇 <b>O'ynash uchun yo'nalishni tanlang:</b>",
            "ru": "🌌 <b>Космос и Природа (800 вопросов)</b>\n\nТайны Вселенной и чудеса дикой природы:\n\n• 🌌 <b>Астрономия и Космос</b> (400) — Планеты, туманности, созвездия\n• 🦁 <b>Природа и Биология</b> (400) — Редкие животные, анатомия человека\n• 🔭 <b>Телескопы и Планеты</b> (100) — Снимки James Webb и Hubble\n• 🐾 <b>Животный мир и Макро</b> (100) — Макро-фотографии чешуи, перьев и меха\n• 🎲 <b>Космос и Природа Микс</b> (800) — Обе темы вперемешку\n\n👇 <b>Выберите направление для игры:</b>",
            "en": "🌌 <b>Cosmos & Nature (800 Questions)</b>\n\nMysteries of deep space and the wonders of wildlife:\n\n• 🌌 <b>Astronomy & Cosmos</b> (400) — Planets, nebulae, constellations\n• 🦁 <b>Nature & Biology</b> (400) — Rare wildlife, human anatomy\n• 🔭 <b>Telescope & Planets</b> (100) — James Webb & Hubble deep field photos\n• 🐾 <b>Wildlife & Macro</b> (100) — Animal macro texture photos\n• 🎲 <b>Cosmos & Nature Mix</b> (800) — Both themes combined\n\n👇 <b>Select a direction to play:</b>"
        },
        "buttons": [
            ("astronomy", {"uz": "🌌 Astronomiya (400)", "ru": "🌌 Астрономия (400)", "en": "🌌 Astronomy (400)"}),
            ("nature", {"uz": "🦁 Tabiat & Biologiya (400)", "ru": "🦁 Природа (400)", "en": "🦁 Nature (400)"}),
            ("telescope_zoom", {"uz": "🔭 Teleskop & Planetalar", "ru": "🔭 Снимки телескопов", "en": "🔭 Telescopes & Planets"}),
            ("macro_texture", {"uz": "🐾 Hayvonlar & Makro", "ru": "🐾 Животные и Макро", "en": "🐾 Wildlife & Macro"}),
            ("human_anatomy", {"uz": "🫀 Inson anatomiyasi", "ru": "🫀 Анатомия человека", "en": "🫀 Human Anatomy"}),
            ("cosmos_nature_mix", {"uz": "🎲 Koinot & Tabiat Mix", "ru": "🎲 Космос и Природа Микс", "en": "🎲 Cosmos & Nature Mix"}),
        ]
    },
    "science_logic": {
        "icon": "🔬",
        "title": {
            "uz": "Fan & Mantiq (800)",
            "ru": "Наука и Логика (800)",
            "en": "Science & Logic (800)"
        },
        "header": {
            "uz": "🔬 <b>Fan & Mantiq (800 ta savol)</b>\n\nAniqlik, ixtirolar va tezkor aql charxi:\n\n• 🔬 <b>Kimyo & Fizika</b> (400 ta) — Davriy jadval, birinchi prototiplar, olimlar\n• 🧠 <b>Mantiq & Matematika</b> (400 ta) — Tezkor arifmetika, 4-ortiqchasi, qonuniyatlar\n• 🧪 <b>Davriy jadval elementlari</b> (100 ta) — Belgilar va kimyoviy xossalar\n• ⚡ <b>Tezkor hisob-kitob</b> (100 ta) — Flash Math arifmetikasi\n• 🎲 <b>Fan & Mantiq Mix</b> (800 ta) — Barcha ilmiy savollar aralash\n\n👇 <b>O'ynash uchun yo'nalishni tanlang:</b>",
            "ru": "🔬 <b>Наука и Логика (800 вопросов)</b>\n\nТочные науки, изобретения и зарядка для ума:\n\n• 🔬 <b>Химия и Физика</b> (400) — Таблица Менделеева, первые прототипы, учёные\n• 🧠 <b>Логика и Математика</b> (400) — Быстрый счёт, четвёртый лишний, числовые ряды\n• 🧪 <b>Элементы таблицы</b> (100) — Символы и свойства элементов\n• ⚡ <b>Быстрый счёт</b> (100) — Flash Math арифметика\n• 🎲 <b>Наука и Логика Микс</b> (800) — Все научные темы вперемешку\n\n👇 <b>Выберите направление для игры:</b>",
            "en": "🔬 <b>Science & Logic (800 Questions)</b>\n\nPrecise sciences, great inventions, and brain training:\n\n• 🔬 <b>Chemistry & Physics</b> (400) — Periodic table, first prototypes, scientists\n• 🧠 <b>Logic & Fast Math</b> (400) — Speed arithmetic, odd one out, sequences\n• 🧪 <b>Periodic Elements</b> (100) — Symbols and properties\n• ⚡ <b>Fast Math</b> (100) — Flash math calculation tricks\n• 🎲 <b>Science & Logic Mix</b> (800) — All scientific themes combined\n\n👇 <b>Select a direction to play:</b>"
        },
        "buttons": [
            ("science", {"uz": "🔬 Kimyo & Fizika (400)", "ru": "🔬 Химия и Физика (400)", "en": "🔬 Chemistry & Physics (400)"}),
            ("logic_math", {"uz": "🧠 Mantiq & Matematika (400)", "ru": "🧠 Логика и Математика (400)", "en": "🧠 Logic & Math (400)"}),
            ("elements", {"uz": "🧪 Davriy jadval", "ru": "🧪 Элементы", "en": "🧪 Periodic Elements"}),
            ("flash_math", {"uz": "⚡ Tezkor hisob-kitob", "ru": "⚡ Быстрый счёт", "en": "⚡ Fast Math"}),
            ("odd_one_out", {"uz": "4️⃣ To'rtinchisi ortiqcha", "ru": "4️⃣ Четвёртый лишний", "en": "4️⃣ Odd One Out"}),
            ("science_logic_mix", {"uz": "🎲 Fan & Mantiq Mix", "ru": "🎲 Наука и Логика Микс", "en": "🎲 Science & Logic Mix"}),
        ]
    },
    "history_culture": {
        "icon": "📜",
        "title": {
            "uz": "Tarix & San'at (1,200)",
            "ru": "История и Искусство (1,200)",
            "en": "History & Art (1,200)"
        },
        "header": {
            "uz": "📜 <b>Tarix, Adabiyot & San'at (1,200 ta savol)</b>\n\nInsoniyat sivilizatsiyasi va durdona madaniyat:\n\n• 📜 <b>Jahon & O'zbekiston Tarixi</b> (400 ta) — Tarixiy janglar, imperiyalar xaritalari, shaxslar\n• 📚 <b>Adabiyot & Asarlar</b> (400 ta) — Aforizmlar, kitob emojilari, shoirlar\n• 🎨 <b>San'at & Me'morchilik</b> (400 ta) — Kartina parchalari, jahon mo'jizalari, haykallar\n• 🎲 <b>Madaniyat Mix</b> (1,200 ta) — Barcha tarix, adabiyot va san'at savollari\n\n👇 <b>O'ynash uchun yo'nalishni tanlang:</b>",
            "ru": "📜 <b>История, Литература и Искусство (1,200 вопросов)</b>\n\nИстория цивилизаций и шедевры культуры:\n\n• 📜 <b>Всемирная История</b> (400) — Битвы, карты империй, исторические лица\n• 📚 <b>Литература и Книги</b> (400) — Цитаты, эмодзи-книги, классики\n• 🎨 <b>Искусство и Архитектура</b> (400) — Фрагменты картин, шедевры, скульптуры\n• 🎲 <b>Культура Микс</b> (1,200) — Все темы культуры вперемешку\n\n👇 <b>Выберите направление для игры:</b>",
            "en": "📜 <b>History, Literature & Art (1,200 Questions)</b>\n\nHuman civilizations and cultural masterpieces:\n\n• 📜 <b>World History</b> (400) — Battles, empire maps, legendary figures\n• 📚 <b>Literature & Classics</b> (400) — Quotes, book emojis, famous authors\n• 🎨 <b>Art & Architecture</b> (400) — Art fragments, architectural wonders\n• 🎲 <b>Culture Mix</b> (1,200) — All culture themes combined\n\n👇 <b>Select a direction to play:</b>"
        },
        "buttons": [
            ("history", {"uz": "📜 Tarix (400)", "ru": "📜 История (400)", "en": "📜 History (400)"}),
            ("literature", {"uz": "📚 Adabiyot & Asarlar (400)", "ru": "📚 Литература (400)", "en": "📚 Literature (400)"}),
            ("art", {"uz": "🎨 San'at & Me'morchilik (400)", "ru": "🎨 Искусство (400)", "en": "🎨 Art (400)"}),
            ("quotes", {"uz": "📖 Mashhur iqtiboslar", "ru": "📖 Цитаты и афоризмы", "en": "📖 Famous Quotes"}),
            ("art_fragment", {"uz": "🖼 Kartina parchalari", "ru": "🖼 Шедевры живописи", "en": "🖼 Art Fragments"}),
            ("history_culture_mix", {"uz": "🎲 Madaniyat Mix (1,200 ta)", "ru": "🎲 Культура Микс (1,200)", "en": "🎲 Culture Mix (1,200)"}),
        ]
    },
    "people_brands": {
        "icon": "👑",
        "title": {
            "uz": "Shaxslar & Brendlar",
            "ru": "Личности и Бренды",
            "en": "People & Brands"
        },
        "header": {
            "uz": "👑 <b>Shaxslar & Brendlar (400+ ta savol)</b>\n\nBuyuk arboblar, yulduzlar va jahon brendlari:\n\n• 🏛 <b>Prezidentlar va Yetakchilar</b> — Davlat rahbarlari va siyosatchilar\n• 👑 <b>Buyuk Tarixiy Shaxslar</b> — Sarkardalar, imperatorlar, allomalar\n• 🌟 <b>Yulduzlar va Mashhurlar</b> — Kino, musiqa va sport yulduzlari\n• 🏷 <b>Brend va Klub Logolari</b> — Jahon brendlari va futbol klublari\n• 👤 <b>Barcha Shaxslar Mix</b> — Barcha insonlar aralash\n\n👇 <b>O'ynash uchun yo'nalishni tanlang:</b>",
            "ru": "👑 <b>Личности и Бренды (400+ вопросов)</b>\n\nВеликие лидеры, звёзды и мировые бренды:\n\n• 🏛 <b>Президенты и Лидеры</b> — Главы государств\n• 👑 <b>Исторические Личности</b> — Полководцы, императоры, мыслители\n• 🌟 <b>Звёзды и Знаменитости</b> — Кино, музыка, спорт\n• 🏷 <b>Логотипы Брендов</b> — Мировые компании и клубы\n• 👤 <b>Все Личности (Микс)</b> — Все категории людей\n\n👇 <b>Выберите направление для игры:</b>",
            "en": "👑 <b>People & Brands (400+ Questions)</b>\n\nWorld leaders, celebrities, and iconic brands:\n\n• 🏛 <b>Presidents & Leaders</b> — Heads of state\n• 👑 <b>Historical Figures</b> — Commanders, emperors, scholars\n• 🌟 <b>Celebrities & Stars</b> — Movie, music, sports stars\n• 🏷 <b>Brand & Club Logos</b> — World logos & football clubs\n• 👤 <b>All People (Mix)</b> — All persons combined\n\n👇 <b>Select a direction to play:</b>"
        },
        "buttons": [
            ("president", {"uz": "🏛 Prezidentlar", "ru": "🏛 Президенты", "en": "🏛 Presidents"}),
            ("historical", {"uz": "👑 Tarixiy Shaxslar", "ru": "👑 Исторические Личности", "en": "👑 Historical Figures"}),
            ("celebrity", {"uz": "🌟 Yulduzlar", "ru": "🌟 Знаменитости", "en": "🌟 Celebrities"}),
            ("logo", {"uz": "🏷 Brend Logolari", "ru": "🏷 Логотипы", "en": "🏷 Brand Logos"}),
            ("person", {"uz": "👤 Barcha Shaxslar Mix", "ru": "👤 Все Личности (Микс)", "en": "👤 All People (Mix)"}),
        ]
    }
}

def get_category_overview_text(lang: str = "en", hub: Optional[str] = None) -> str:
    """Compose rich, formatted overview of all categories or a specific hub."""
    if hub and hub in CATEGORY_HUBS_INFO:
        return CATEGORY_HUBS_INFO[hub]["header"].get(lang, CATEGORY_HUBS_INFO[hub]["header"]["en"])

    if lang == "uz":
        return (
            "📁 <b>O'yin Kategoriyalari (Jami 6 ta asosiy toifa, 24+ yo'nalish, 4,000+ savol)</b>\n\n"
            "O'yinda mavjud barcha yo'nalishlar qulay toifalarga ajratilgan. Har bir toifa ichida alohida yo'nalishlar bor:\n\n"
            "1. 🎓 <b>Zakovat Klubi</b> (500 savol) — Qora quti, Deduksiya, Jahon intellekti, Blits\n"
            "2. 🌍 <b>Geografiya & GeoGuessr</b> (1,000+ savol) — Bayroqlar, Poytaxtlar, Obidalar, Gerblar, Xaritalar\n"
            "3. 🌌 <b>Koinot & Tabiat</b> (800 savol) — Astronomiya, Teleskop, Hayvonot olami, Anatomiya\n"
            "4. 🔬 <b>Fan & Mantiq</b> (800 savol) — Kimyo, Fizika, Ixtirolar, Tezkor Matematika\n"
            "5. 📜 <b>Tarix, Adabiyot & San'at</b> (1,200 savol) — Tarix, Durdona asarlar, Rassomchilik\n"
            "6. 👑 <b>Shaxslar & Brendlar</b> (400+ savol) — Prezidentlar, Yulduzlar, Brend logolari\n"
            "7. 🔍 <b>Blur Reveal</b> — Rasmni xiralikdan ochib topish (+300 bonus)\n"
            "8. 🎲 <b>SUPER MIX</b> — Barcha fanlar va toifalar aralash!\n\n"
            "👇 <b>Toifani tanlang va uning ichidagi yo'nalishlarni ko'ring:</b>"
        )
    elif lang == "ru":
        return (
            "📁 <b>Категории Игры (Всего 6 основных категорий, 24+ направлений, 4,000+ вопросов)</b>\n\n"
            "Все доступные режимы удобно разделены по категориям. Внутри каждой категории есть свои направления:\n\n"
            "1. 🎓 <b>Клуб Заковат</b> (500 вопросов) — Чёрный ящик, Дедукция, Мировой интеллект, Блиц\n"
            "2. 🌍 <b>География и GeoGuessr</b> (1,000+ вопросов) — Флаги, Столицы, Достопримечательности, Гербы, Панорамы\n"
            "3. 🌌 <b>Космос и Природа</b> (800 вопросов) — Астрономия, Снимки телескопов, Биология, Животный мир\n"
            "4. 🔬 <b>Наука и Логика</b> (800 вопросов) — Химия, Физика, Изобретения, Быстрый счёт\n"
            "5. 📜 <b>История, Литература и Искусство</b> (1,200 вопросов) — Всемирная история, Шедевры, Архитектура\n"
            "6. 👑 <b>Личности и Бренды</b> (400+ вопросов) — Президенты, Знаменитости, Исторические деятели, Логотипы\n"
            "7. 🔍 <b>Blur Reveal</b> — Размытые фото (+300 бонус)\n"
            "8. 🎲 <b>SUPER MIX</b> — Все категории вперемешку!\n\n"
            "👇 <b>Выберите категорию, чтобы посмотреть направления:</b>"
        )
    else:
        return (
            "📁 <b>Game Categories (6 Main Categories, 24+ Sub-modes, 4,000+ Questions)</b>\n\n"
            "All game modes are neatly organized into categories. Each category contains unique sub-directions:\n\n"
            "1. 🎓 <b>Zakovat Club</b> (500 questions) — Black Box, Logic & Deduction, World Intellect, Blitz\n"
            "2. 🌍 <b>Geography & GeoGuessr</b> (1,000+ questions) — Flags, Capitals, Landmarks, Coats of Arms, Street View\n"
            "3. 🌌 <b>Cosmos & Nature</b> (800 questions) — Astronomy, Deep Space, Biology, Wildlife, Anatomy\n"
            "4. 🔬 <b>Science & Logic</b> (800 questions) — Chemistry, Physics, Inventions, Fast Math & Riddles\n"
            "5. 📜 <b>History, Literature & Art</b> (1,200 questions) — World History, Literary Classics, Art & Architecture\n"
            "6. 👑 <b>People & Brands</b> (400+ questions) — Presidents, Historical Figures, Celebrities, Logos\n"
            "7. 🔍 <b>Blur Reveal</b> — Guess from blurred images (+300 bonus)\n"
            "8. 🎲 <b>SUPER MIX</b> — All subjects and categories mixed!\n\n"
            "👇 <b>Select a category to explore its modes:</b>"
        )

def get_hub_subcategories_kb(
    hub: str,
    prefix: str = "solo_cat",
    lang: str = "en"
) -> InlineKeyboardMarkup:
    """Generate keyboard for the sub-categories inside a specific hub."""
    hub_data = CATEGORY_HUBS_INFO.get(hub)
    if not hub_data:
        return get_category_selection_kb(prefix=prefix, lang=lang)

    keyboard = []
    buttons_raw = hub_data["buttons"]
    i = 0
    while i < len(buttons_raw):
        # If last item or mix
        if i == len(buttons_raw) - 1 or "mix" in buttons_raw[i][0].lower():
            code, name_dict = buttons_raw[i]
            keyboard.append([
                InlineKeyboardButton(
                    text=name_dict.get(lang, name_dict.get("en", code)),
                    callback_data=f"{prefix}:{code}"
                )
            ])
            i += 1
        else:
            c1, n1 = buttons_raw[i]
            c2, n2 = buttons_raw[i + 1]
            keyboard.append([
                InlineKeyboardButton(text=n1.get(lang, n1.get("en", c1)), callback_data=f"{prefix}:{c1}"),
                InlineKeyboardButton(text=n2.get(lang, n2.get("en", c2)), callback_data=f"{prefix}:{c2}")
            ])
            i += 2

    back_label = {
        "uz": "🔙 📁 Barcha toifalar",
        "ru": "🔙 📁 Все категории",
        "en": "🔙 📁 All Categories"
    }.get(lang, "🔙 📁 All Categories")

    keyboard.append([
        InlineKeyboardButton(text=back_label, callback_data=f"{prefix}:hub:main")
    ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_category_selection_kb(
    prefix: str = "solo_cat",
    lang: str = "en",
    input_mode: str = "both"
) -> InlineKeyboardMarkup:
    """Generate clean hierarchical category hubs keyboard for solo and setup modes."""
    btn_buttons_pfx = "✅ " if input_mode == "buttons" else ""
    btn_text_pfx = "✅ " if input_mode == "text" else ""
    btn_both_pfx = "✅ " if input_mode == "both" else ""

    zako_title = CATEGORY_HUBS_INFO["zakovat"]["title"].get(lang, "Zakovat Club (500)")
    geo_title = CATEGORY_HUBS_INFO["geography"]["title"].get(lang, "Geography (1,000+)")
    cos_title = CATEGORY_HUBS_INFO["cosmos_nature"]["title"].get(lang, "Cosmos & Nature (800)")
    sci_title = CATEGORY_HUBS_INFO["science_logic"]["title"].get(lang, "Science & Logic (800)")
    his_title = CATEGORY_HUBS_INFO["history_culture"]["title"].get(lang, "History & Art (1,200)")
    peo_title = CATEGORY_HUBS_INFO["people_brands"]["title"].get(lang, "People & Brands")

    super_mix_title = {
        "uz": "🎲 SUPER MIX (Barchasi - 4,000+)",
        "ru": "🎲 SUPER MIX (Все темы - 4,000+)",
        "en": "🎲 SUPER MIX (All Subjects - 4,000+)"
    }.get(lang, "🎲 SUPER MIX (4,000+)")

    keyboard = [
        # Flagship Zakovat Hub
        [
            InlineKeyboardButton(text=f"🎓 {zako_title}", callback_data=f"{prefix}:hub:zakovat")
        ],
        # Geography & Cosmos Hubs
        [
            InlineKeyboardButton(text=f"🌍 {geo_title}", callback_data=f"{prefix}:hub:geography"),
            InlineKeyboardButton(text=f"🌌 {cos_title}", callback_data=f"{prefix}:hub:cosmos_nature")
        ],
        # Science & History Hubs
        [
            InlineKeyboardButton(text=f"🔬 {sci_title}", callback_data=f"{prefix}:hub:science_logic"),
            InlineKeyboardButton(text=f"📜 {his_title}", callback_data=f"{prefix}:hub:history_culture")
        ],
        # People & Blur
        [
            InlineKeyboardButton(text=f"👑 {peo_title}", callback_data=f"{prefix}:hub:people_brands"),
            InlineKeyboardButton(text=t("mode_blur", lang), callback_data=f"{prefix}:blur")
        ],
        # Super Mix
        [
            InlineKeyboardButton(text=super_mix_title, callback_data=f"{prefix}:mix")
        ],
        # Input mode selection
        [
            InlineKeyboardButton(
                text=f"{btn_buttons_pfx}{t('btn_input_buttons', lang)}",
                callback_data=f"{prefix}:input:buttons"
            ),
            InlineKeyboardButton(
                text=f"{btn_text_pfx}{t('btn_input_text', lang)}",
                callback_data=f"{prefix}:input:text"
            ),
            InlineKeyboardButton(
                text=f"{btn_both_pfx}{t('btn_input_both', lang)}",
                callback_data=f"{prefix}:input:both"
            )
        ],
        # Back to Main Menu
        [
            InlineKeyboardButton(text=t("btn_back", lang), callback_data=f"{prefix}:back")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_solo_setup_kb(
    mode: str = "mix",
    round_time: int = 30,
    input_mode: str = "both",
    lang: str = "en",
    continent: str = "all",
    selected_modes: Optional[List[str]] = None,
    is_blur: bool = False
) -> InlineKeyboardMarkup:
    """Generate interactive solo setup lobby keyboard with multi-mode checkboxes and blur toggle."""
    if selected_modes is None:
        if mode and mode not in ("mix", "blur"):
            selected_modes = [mode]
        elif mode == "blur":
            selected_modes = []
            is_blur = True
        else:
            selected_modes = []

    all_cat_modes = [
        "zakovat", "astronomy", "science", "history", "literature", "art", "nature", "logic_math",
        "flag", "capital", "landmark", "higher_lower", "coat_of_arms", "streetview",
        "emoji", "contour", "president", "historical", "celebrity", "logo"
    ]

    def mode_btn(m_code: str):
        if m_code == "mix":
            is_sel = (
                "mix" in (selected_modes or []) or
                (bool(selected_modes) and set(all_cat_modes).issubset(set(selected_modes)))
            )
        else:
            is_sel = m_code in (selected_modes or []) and "mix" not in (selected_modes or [])
        pfx = "✅ " if is_sel else ""
        return InlineKeyboardButton(
            text=f"{pfx}{t(f'mode_{m_code}', lang)}",
            callback_data=f"solo_setup:mode:{m_code}"
        )

    t30_pfx = "✅ " if round_time == 30 else ""
    t60_pfx = "✅ " if round_time == 60 else ""

    btn_buttons_pfx = "✅ " if input_mode == "buttons" else ""
    btn_text_pfx = "✅ " if input_mode == "text" else ""
    btn_both_pfx = "✅ " if input_mode == "both" else ""

    blur_status = t("status_enabled", lang) if is_blur else t("status_disabled", lang)
    blur_btn_text = f"🔍 Blur: {blur_status}"

    keyboard = [
        # Flagship Zakovat Mode
        [mode_btn("zakovat")],
        # Science & Cosmos
        [mode_btn("astronomy"), mode_btn("science")],
        # Humanities & Literature
        [mode_btn("history"), mode_btn("literature")],
        # Art & Nature
        [mode_btn("art"), mode_btn("nature")],
        # Logic & Math + Mix
        [mode_btn("logic_math"), mode_btn("mix")],
        # Geography & Culture modes
        [mode_btn("flag"), mode_btn("capital")],
        [mode_btn("landmark"), mode_btn("higher_lower")],
        [mode_btn("coat_of_arms"), mode_btn("streetview")],
        [mode_btn("emoji"), mode_btn("contour")],
        [mode_btn("president"), mode_btn("historical")],
        [mode_btn("celebrity"), mode_btn("logo")],
        # Presets: All modes / Flags only
        [
            InlineKeyboardButton(text=t("btn_select_all_modes", lang), callback_data="solo_setup:all"),
            InlineKeyboardButton(text=t("btn_only_flags", lang), callback_data="solo_setup:flags_only")
        ],
        # Blur Effect ON / OFF toggle
        [
            InlineKeyboardButton(text=blur_btn_text, callback_data="solo_setup:blur")
        ],
        # Continent Filter
        [
            InlineKeyboardButton(
                text=t("btn_continent", lang, continent=t(f"filter_continent_{continent}", lang)),
                callback_data="solo_setup:continent"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{t30_pfx}{t('btn_timer_30s', lang)}",
                callback_data="solo_setup:time:30"
            ),
            InlineKeyboardButton(
                text=f"{t60_pfx}{t('btn_timer_60s', lang)}",
                callback_data="solo_setup:time:60"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{btn_buttons_pfx}{t('btn_input_buttons', lang)}",
                callback_data="solo_setup:input:buttons"
            ),
            InlineKeyboardButton(
                text=f"{btn_text_pfx}{t('btn_input_text', lang)}",
                callback_data="solo_setup:input:text"
            ),
            InlineKeyboardButton(
                text=f"{btn_both_pfx}{t('btn_input_both', lang)}",
                callback_data="solo_setup:input:both"
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_start_now", lang),
                callback_data="solo_setup:start"
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_cancel", lang),
                callback_data="solo_setup:cancel"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_game_type_kb(lang: str = "en", bot_username: str = "") -> InlineKeyboardMarkup:
    """Generate keyboard for selecting Game Type (Group vs Solo vs Daily)."""
    add_group_url = f"https://t.me/{bot_username}?startgroup=true" if bot_username else "https://t.me"
    keyboard = [
        [
            InlineKeyboardButton(text=t("btn_play_solo", lang), callback_data="game_type:solo"),
            InlineKeyboardButton(text=t("btn_group_game", lang), url=add_group_url)
        ],
        [
            InlineKeyboardButton(text=t("btn_daily", lang), callback_data="game_type:daily")
        ],
        [
            InlineKeyboardButton(text=t("btn_back", lang), callback_data="game_type:menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_question_kb(session_id: str, options: List[str]) -> InlineKeyboardMarkup:
    """Generate answer buttons for an active group round."""
    if len(options) == 2:
        keyboard = [
            [InlineKeyboardButton(text=options[0], callback_data=f"ans:{session_id}:0")],
            [InlineKeyboardButton(text=options[1], callback_data=f"ans:{session_id}:1")]
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    keyboard = []
    for i in range(0, len(options), 2):
        row = [
            InlineKeyboardButton(text=options[j], callback_data=f"ans:{session_id}:{j}")
            for j in range(i, min(i + 2, len(options)))
        ]
        keyboard.append(row)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_solo_question_kb(
    options: List[str],
    eliminated: Set[int],
    has_hint: bool,
    has_5050: bool,
    lang: str = "en",
    text_only: bool = False
) -> InlineKeyboardMarkup:
    """Generate solo question buttons with lifelines. In text_only mode, option buttons are omitted."""
    lifeline_row = []
    if has_hint:
        lifeline_row.append(InlineKeyboardButton(text=t("solo_btn_hint", lang), callback_data="solo_hint"))
    else:
        lifeline_row.append(InlineKeyboardButton(text="💡 ✖️", callback_data="solo_ignore"))

    if has_5050:
        lifeline_row.append(InlineKeyboardButton(text=t("solo_btn_5050", lang), callback_data="solo_5050"))
    else:
        lifeline_row.append(InlineKeyboardButton(text="✂️ ✖️", callback_data="solo_ignore"))

    if text_only:
        return InlineKeyboardMarkup(inline_keyboard=[lifeline_row])

    def make_btn(idx: int):
        if idx in eliminated:
            return InlineKeyboardButton(text="✖️", callback_data="solo_ignore")
        return InlineKeyboardButton(text=options[idx], callback_data=f"solo_ans:{idx}")

    if len(options) == 2:
        option_rows = [
            [make_btn(0)],
            [make_btn(1)]
        ]
    else:
        option_rows = []
        for i in range(0, len(options), 2):
            row = [make_btn(j) for j in range(i, min(i + 2, len(options)))]
            option_rows.append(row)

    option_rows.append(lifeline_row)
    return InlineKeyboardMarkup(inline_keyboard=option_rows)

def get_daily_question_kb(options: List[str]) -> InlineKeyboardMarkup:
    """Generate answer buttons for a daily challenge round."""
    if len(options) == 2:
        keyboard = [
            [InlineKeyboardButton(text=options[0], callback_data="daily_ans:0")],
            [InlineKeyboardButton(text=options[1], callback_data="daily_ans:1")]
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    keyboard = []
    for i in range(0, len(options), 2):
        row = [
            InlineKeyboardButton(text=options[j], callback_data=f"daily_ans:{j}")
            for j in range(i, min(i + 2, len(options)))
        ]
        keyboard.append(row)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_duel_kb(challenger_id: int, target_id: int, lang: str = "en", duel_id: int = 0) -> InlineKeyboardMarkup:
    """Generate duel challenge acceptance keyboard."""
    keyboard = [
        [
            InlineKeyboardButton(
                text=t("duel_accept", lang),
                callback_data=f"duel:accept:{challenger_id}:{target_id}:{duel_id}"
            ),
            InlineKeyboardButton(
                text=t("duel_decline", lang),
                callback_data=f"duel:decline:{challenger_id}:{target_id}:{duel_id}"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_leaderboard_kb(lb_type: str = "global", current_period: str = "all_time", lang: str = "en") -> InlineKeyboardMarkup:
    """Generate keyboard for switching leaderboard periods (daily, weekly, monthly, all-time)."""
    periods = [
        ("daily", t("btn_lb_daily", lang)),
        ("weekly", t("btn_lb_weekly", lang)),
        ("monthly", t("btn_lb_monthly", lang)),
        ("all_time", t("btn_lb_all_time", lang)),
    ]
    buttons = []
    row = []
    for p_key, p_label in periods:
        prefix = "• " if p_key == current_period else ""
        suffix = " •" if p_key == current_period else ""
        btn_text = f"{prefix}{p_label}{suffix}"
        row.append(InlineKeyboardButton(text=btn_text, callback_data=f"lb_period:{lb_type}:{p_key}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)
