# -*- coding: utf-8 -*-
"""
GeoGuru Game Dataset: Nature, Biology, Ecology & Animal Database.
Contains 400 rich multilingual questions across 4 engaging sub-modes:
1. macro_texture (100 items): High-resolution macro close-ups of animal fur, scales, feathers, skin & eyes.
2. animal_scale (100 items): Higher/Lower scientific comparisons of animal speeds, lifespans, weights & diving depths.
3. nature_emoji (100 items): Witty emoji riddles to identify remarkable animals, birds, marine life and rare plants.
4. human_anatomy (100 items): Fascinating human body biology, organs, sensory faculties and physiological wonders.
"""
import random
from typing import Optional, List, Dict, Any

NATURE_DATA: List[Dict[str, Any]] = [   {   'id': 'nature_macro_001_zebra',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Zebra', "Yo'lbars", 'Okapi', 'Giyena'],
                       'ru': ['Зебра', 'Тигр', 'Окапи', 'Гиена'],
                       'en': ['Zebra', 'Tiger', 'Okapi', 'Hyena']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Zebra', 'ru': 'Зебра', 'en': 'Zebra'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Zebra_stripes_detail.jpg/800px-Zebra_stripes_detail.jpg',
        'fun_fact': {   'uz': "Zebraning chiziqlari odam barmoq izi kabi mutlaqo betakror bo'lib, tsetse pashshalarini "
                              "chalg'itishga va haroratni boshqarishga yordam beradi.",
                        'ru': 'Полосы каждой зебры уникальны, как отпечатки пальцев. Они дезориентируют мух цеце и '
                              'помогают рассеивать тепло.',
                        'en': 'Every zebra has a unique stripe pattern acting like a fingerprint, confusing biting '
                              'tsetse flies and creating convective cooling currents.'},
        'aliases': ['zebra', 'zebr', 'зебра', 'равнинная зебра']},
    {   'id': 'nature_macro_002_cheetah',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Qoplon', 'Gepard', 'Yaguar', 'Serval'],
                       'ru': ['Леопард', 'Гепард', 'Ягуар', 'Сервал'],
                       'en': ['Leopard', 'Cheetah', 'Jaguar', 'Serval']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Gepard', 'ru': 'Гепард', 'en': 'Cheetah'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cheetah_fur_macro.jpg/800px-Cheetah_fur_macro.jpg',
        'fun_fact': {   'uz': "Gepard mo'ynasidagi qora dog'lar yaxlit va to'liq bo'ladi, qoplon yoki yaguarnikidek "
                              'ichi ochiq halqa (rozetka) hosil qilmaydi.',
                        'ru': 'Пятна на шкуре гепарда сплошные и круглые, в отличие от полых колец-розеток леопарда '
                              'или ягуара.',
                        'en': 'Cheetah spots are solid round black spots, distinctly different from the open rosette '
                              'patterns of leopards and jaguars.'},
        'aliases': ['gepard', 'гепард', 'cheetah']},
    {   'id': 'nature_macro_003_leopard',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Gepard', 'Giyena', 'Qoplon (Leopard)', 'Puma'],
                       'ru': ['Гепард', 'Гиена', 'Леопард', 'Пума'],
                       'en': ['Cheetah', 'Hyena', 'Leopard', 'Cougar']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Qoplon (Leopard)', 'ru': 'Леопард', 'en': 'Leopard'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Leopard_fur_pattern_macro.jpg/800px-Leopard_fur_pattern_macro.jpg',
        'fun_fact': {   'uz': "Qoplonning mo'ynasidagi naqshlar o'rtasida qora nuqtasi bo'lmagan bo'sh rozetka "
                              "halqalaridan iborat bo'ladi.",
                        'ru': 'Розетки леопарда представляют собой полые кольца без центральной темной точки, что '
                              'отличает его от ягуара.',
                        'en': 'Leopard rosettes are hollow circular clusters without internal spots, optimizing '
                              'camouflage in savannah woodlands.'},
        'aliases': ['qoplon', 'leopard', 'леопард']},
    {   'id': 'nature_macro_004_jaguar',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Qoplon', 'Gepard', 'Oselot', 'Yaguar'],
                       'ru': ['Леопард', 'Гепард', 'Оцелот', 'Ягуар'],
                       'en': ['Leopard', 'Cheetah', 'Ocelot', 'Jaguar']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Yaguar', 'ru': 'Ягуар', 'en': 'Jaguar'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Jaguar_rosette_detail.jpg/800px-Jaguar_rosette_detail.jpg',
        'fun_fact': {   'uz': "Yaguarning rozetkalari ichida mayda qora nuqtalar bo'ladi. Bu uni qoplondan "
                              'ajratishning eng ishonchli usulidir.',
                        'ru': 'В центре крупных розеток ягуара почти всегда находятся маленькие черные пятнышки-точки.',
                        'en': 'Jaguar rosettes are larger than those of leopards and feature one or more small central '
                              'black dots inside the rings.'},
        'aliases': ['yaguar', 'ягуар', 'jaguar']},
    {   'id': 'nature_macro_005_bengal_tiger',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Yo'lbars", 'Qoplon', 'Zebra', 'Sher'],
                       'ru': ['Тигр', 'Леопард', 'Зебра', 'Лев'],
                       'en': ['Tiger', 'Leopard', 'Zebra', 'Lion']},
        'correct_index': 0,
        'correct_answer': {'uz': "Yo'lbars", 'ru': 'Тигр', 'en': 'Tiger'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Tiger_stripes_macro_texture.jpg/800px-Tiger_stripes_macro_texture.jpg',
        'fun_fact': {   'uz': "Yo'lbarsning chiziqlari faqat junida emas, balki bevosita uning terisida ham qora "
                              "pigment bilan chizilgan bo'ladi.",
                        'ru': 'Полосы тигра дублируются прямо на коже: если тигра побрить, он всё равно останется '
                              'полосатым.',
                        'en': "A tiger's stripes are pigmented directly on its skin; a shaved tiger still displays its "
                              'characteristic camouflage stripes.'},
        'aliases': ['yolbars', "yo'lbars", 'тигр', 'tiger']},
    {   'id': 'nature_macro_006_snow_leopard',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Gepard', 'Qor qoploni (Ilvirs)', 'Silovsin', "Yo'lbars"],
                       'ru': ['Гепард', 'Снежный барс (Ирбис)', 'Рысь', 'Тигр'],
                       'en': ['Cheetah', 'Snow Leopard', 'Lynx', 'Tiger']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qor qoploni (Ilvirs)', 'ru': 'Снежный барс (Ирбис)', 'en': 'Snow Leopard'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Snow_leopard_fur_macro.jpg/800px-Snow_leopard_fur_macro.jpg',
        'fun_fact': {   'uz': "Ilvirsning qalin tutunsimon mo'ynasi kvadrat santimetriga 4000 tagacha junga ega "
                              "bo'lib, baland tog' qahratonidan saqlaydi.",
                        'ru': 'Шерсть снежного барса достигает 12 см в длину и имеет до 4000 волосков на квадратный '
                              'сантиметр.',
                        'en': 'Snow leopards have fur up to 12 cm long with up to 4,000 hairs per cm², insulating them '
                              'in extreme Himalayan winters.'},
        'aliases': ['qor qoploni', 'ilvirs', 'снежный барс', 'ирбис', 'snow leopard']},
    {   'id': 'nature_macro_007_giraffe',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Zebra', 'Bongo', 'Jirafa', 'Okapi'],
                       'ru': ['Зебра', 'Бонго', 'Жираф', 'Окапи'],
                       'en': ['Zebra', 'Bongo', 'Giraffe', 'Okapi']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Jirafa', 'ru': 'Жираф', 'en': 'Giraffe'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Giraffe_pattern_detail.jpg/800px-Giraffe_pattern_detail.jpg',
        'fun_fact': {   'uz': "Jirafaning har bir poligon shaklidagi dog'i ostida qon tomir to'ri joylashgan bo'lib, "
                              'tanani sovutishga yordam beradi.',
                        'ru': 'Под каждым темным пятном жирафа скрыта густая сеть кровеносных сосудов, рассеивающих '
                              'тепло тела.',
                        'en': "Under each dark patch on a giraffe's coat is a sophisticated vascular network that "
                              'radiates excess body heat.'},
        'aliases': ['jirafa', 'жираф', 'giraffe']},
    {   'id': 'nature_macro_008_peacock',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Qirg'ovul", "To'ti", 'Kolibri', 'Tovus'],
                       'ru': ['Фазан', 'Попугай', 'Колибри', 'Павлин'],
                       'en': ['Pheasant', 'Parrot', 'Hummingbird', 'Peacock']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Tovus', 'ru': 'Павлин', 'en': 'Peacock'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Peacock_feather_detail.jpg/800px-Peacock_feather_detail.jpg',
        'fun_fact': {   'uz': "Tovus patlarining kamalaksimon jilvasi kimyoviy pigmentdan emas, balki yorug'likni "
                              'qaytaruvchi foton kristallardan yuzaga keladi.',
                        'ru': 'Переливающийся окрас перьев павлина создается не пигментами, а оптической '
                              'интерференцией наноструктур.',
                        'en': 'Peacock feather iridescence is purely structural, produced by nanoscale 2D photonic '
                              'crystal gratings reflecting light.'},
        'aliases': ['tovus', 'павлин', 'peacock']},
    {   'id': 'nature_macro_009_chameleon',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Xameleon', 'Iguana', 'Gekkon', 'Agama'],
                       'ru': ['Хамелеон', 'Игуана', 'Геккон', 'Агама'],
                       'en': ['Chameleon', 'Iguana', 'Gecko', 'Agama']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Xameleon', 'ru': 'Хамелеон', 'en': 'Chameleon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Chameleon_scales_macro.jpg/800px-Chameleon_scales_macro.jpg',
        'fun_fact': {   'uz': "Xameleon terisidagi oltiburchakli tangachalar ostidagi guanin nanokristallari oralig'i "
                              "o'zgarishi hisobiga rangi o'zgaradi.",
                        'ru': 'Хамелеон меняет цвет благодаря изменению расстояния между нанокристаллами гуанина в '
                              'клетках кожи.',
                        'en': 'Chameleons tune the nanoscale spacing between guanine crystals within dermal '
                              'iridophores to dynamically shift colors.'},
        'aliases': ['xameleon', 'хамелеон', 'chameleon']},
    {   'id': 'nature_macro_010_nile_crocodile',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Alligator', 'Nil timsohi', 'Gavial', 'Komodo varani'],
                       'ru': ['Аллигатор', 'Нильский крокодил', 'Гавиал', 'Комодский варан'],
                       'en': ['Alligator', 'Nile Crocodile', 'Gharial', 'Komodo dragon']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Nil timsohi', 'ru': 'Нильский крокодил', 'en': 'Nile Crocodile'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Crocodile_scales_texture.jpg/800px-Crocodile_scales_texture.jpg',
        'fun_fact': {   'uz': 'Timsoh terisidagi toshdek qattiq plastinkalar osteoderma deb ataluvchi suyak '
                              "to'qimasidan iborat haqiqiy sovutdir.",
                        'ru': 'Роговые щитки крокодила содержат костные пластинки (остеодермы), создающие прочную '
                              'природную броню.',
                        'en': 'Crocodile armor consists of bony osteoderm plates embedded within thick dermal scutes, '
                              'providing bullet-grade resilience.'},
        'aliases': ['timsoh', 'nil timsohi', 'крокодил', 'нильский крокодил', 'crocodile']},
    {   'id': 'nature_macro_011_great_white_shark',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Delfin', 'Manta', 'Oq akula', 'Skat'],
                       'ru': ['Дельфин', 'Манта', 'Белая акула', 'Скат'],
                       'en': ['Dolphin', 'Manta Ray', 'Great White Shark', 'Stingray']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Oq akula', 'ru': 'Белая акула', 'en': 'Great White Shark'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Shark_skin_placoid_scales_SEM.jpg/800px-Shark_skin_placoid_scales_SEM.jpg',
        'fun_fact': {   'uz': "Akula terisi plakoid tangachalar (teri tishchalari) bilan qoplangan bo'lib, suv "
                              'turbulentligini keskin kamaytiradi.',
                        'ru': 'Кожа акулы покрыта плакоидными чешуйками (кожными зубчиками), снижающими '
                              'гидродинамическое сопротивление.',
                        'en': 'Shark skin is paved with microscopic tooth-like placoid scales (dermal denticles) '
                              'reducing drag and preventing biofilm formation.'},
        'aliases': ['oq akula', 'akula', 'белая акула', 'акула', 'great white shark']},
    {   'id': 'nature_macro_012_monarch_butterfly',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Ipak qurti', "Tovusko'z", 'Machaon', 'Monarx kapalagi'],
                       'ru': ['Павлиноглазка', 'Шелкопряд', 'Махаон', 'Данаида монарх'],
                       'en': ['Peacock Butterfly', 'Silkworm', 'Swallowtail', 'Monarch Butterfly']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Monarx kapalagi', 'ru': 'Данаида монарх', 'en': 'Monarch Butterfly'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Butterfly_wing_scales_macro.jpg/800px-Butterfly_wing_scales_macro.jpg',
        'fun_fact': {   'uz': 'Kapalak qanotidagi chang aslida koshin kabi bir-birini qoplab turuvchi minglab '
                              'mikroskopik xitin tangachalardir.',
                        'ru': 'Пыльца на крыльях бабочек состоит из тысяч микроскопических хитиновых чешуек, уложенных '
                              'в виде черепицы.',
                        'en': 'Butterfly wing dust consists of thousands of microscopic overlapping chitin scales '
                              'arranged like roof shingles.'},
        'aliases': ['monarx', 'monarx kapalagi', 'данаида монарх', 'monarch butterfly']},
    {   'id': 'nature_macro_013_blue_morpho',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Ko'k Morfo kapalagi", 'Monarx', 'Machaon', 'Boychechak'],
                       'ru': ['Бабочка Морфо', 'Махаон', 'Монарх', 'Аполлон'],
                       'en': ['Blue Morpho Butterfly', 'Swallowtail', 'Monarch', 'Apollo']},
        'correct_index': 0,
        'correct_answer': {'uz': "Ko'k Morfo kapalagi", 'ru': 'Бабочка Морфо', 'en': 'Blue Morpho Butterfly'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Morpho_peleides_wing_scales.jpg/800px-Morpho_peleides_wing_scales.jpg',
        'fun_fact': {   'uz': "Ko'k Morfoda ko'k pigment yo'q; uning yaltirashi qanotdagi archasimon "
                              "nanotuzilmalarning yorug'likni qaytarishidan paydo bo'ladi.",
                        'ru': 'В крыльях морфо нет синего пигмента; металлический синий цвет возникает из-за '
                              'преломления света в наноструктурах чешуек.',
                        'en': 'Blue Morpho wings contain zero blue pigment; their iridescence is purely structural, '
                              'produced by tree-like nanoscale ribs.'},
        'aliases': ['morfo', 'kok morfo', 'бабочка морфо', 'морфо', 'blue morpho']},
    {   'id': 'nature_macro_014_honeybee',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Chivin', 'Asalari', 'Chigirtka', 'Ninachi'],
                       'ru': ['Комар', 'Медоносная пчела', 'Саранча', 'Стрекоза'],
                       'en': ['Mosquito', 'Honeybee', 'Locust', 'Dragonfly']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Asalari', 'ru': 'Медоносная пчела', 'en': 'Honeybee'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Apis_mellifera_compound_eye.jpg/800px-Apis_mellifera_compound_eye.jpg',
        'fun_fact': {   'uz': "Asalarining murakkab ko'zlari orasida mayda tukchalar o'sadi, ular shamol yo'nalishini "
                              'aniqlashga xizmat qiladi.',
                        'ru': 'Глаза пчелы покрыты тонкими чувствительными волосками, улавливающими воздушные потоки '
                              'во время полета.',
                        'en': 'Honeybee compound eyes are laced with sensory hairs that measure wind direction and '
                              'prevent dust accumulation during flight.'},
        'aliases': ['asalari', 'пчела', 'медоносная пчела', 'honeybee', 'bee']},
    {   'id': 'nature_macro_015_dragonfly',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Asalari', 'Pashsha', 'Ninachi', "Qo'ng'iz"],
                       'ru': ['Пчела', 'Муха', 'Стрекоза', 'Жук'],
                       'en': ['Bee', 'Housefly', 'Dragonfly', 'Beetle']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Ninachi', 'ru': 'Стрекоза', 'en': 'Dragonfly'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Dragonfly_compound_eye_macro.jpg/800px-Dragonfly_compound_eye_macro.jpg',
        'fun_fact': {   'uz': "Ninachining har bir ko'zida 30 000 tagacha alohida ommatidiy bo'lib, u deyarli 360 "
                              "darajali panoramik ko'rish imkonini beradi.",
                        'ru': 'Глаз стрекозы содержит до 30 000 фасеток (омматидиев), обеспечивая непрерывный круговой '
                              'обзор.',
                        'en': 'Each dragonfly eye possesses up to 30,000 ommatidia lenses, conferring near-spherical '
                              'vision for aerial interception.'},
        'aliases': ['ninachi', 'стрекоза', 'dragonfly']},
    {   'id': 'nature_macro_016_owl_feathers',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Burgut', 'Lochin', "Qarg'a", 'Boyqush'],
                       'ru': ['Беркут', 'Сокол', 'Ворона', 'Сова (Филин)'],
                       'en': ['Eagle', 'Falcon', 'Crow', 'Owl']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Boyqush', 'ru': 'Сова (Филин)', 'en': 'Owl'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Owl_feather_serrations_macro.jpg/800px-Owl_feather_serrations_macro.jpg',
        'fun_fact': {   'uz': 'Boyqush qanot patlarining chekkasidagi taroqsimon mayda tishlar havo oqimini tarqatib, '
                              'mutlaqo shovqinsiz uchish imkonini beradi.',
                        'ru': 'Зубчатый гребень на маховых перьях совы глушит акустические завихрения, делая полет '
                              'абсолютно беззвучным.',
                        'en': "Comb-like serrations along the leading edge of an owl's primary feathers suppress "
                              'acoustic vortices for silent flight.'},
        'aliases': ['boyqush', 'filin', 'сова', 'филин', 'owl']},
    {   'id': 'nature_macro_017_scarlet_macaw',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Qizil Ara to'tisi", 'Tovus', 'Kakadu', 'Flamingo'],
                       'ru': ['Красный ара', 'Павлин', 'Какаду', 'Фламинго'],
                       'en': ['Scarlet Macaw', 'Peacock', 'Cockatoo', 'Flamingo']},
        'correct_index': 0,
        'correct_answer': {'uz': "Qizil Ara to'tisi", 'ru': 'Красный ара', 'en': 'Scarlet Macaw'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Scarlet_macaw_feather_texture.jpg/800px-Scarlet_macaw_feather_texture.jpg',
        'fun_fact': {   'uz': "Ara to'tisining yorqin qizil va sariq ranglari faqat to'tisimonlar organizmida "
                              "sintezlanadigan psittakofulvin pigmentlariga bog'liq.",
                        'ru': 'Красные оттенки перьев ара синтезируются пигментами пситтакофульвинами, встречающимися '
                              'исключительно у попугаев.',
                        'en': 'Scarlet macaw feathers get their striking hues from psittacofulvins, rare lipochrome '
                              'pigments unique to the parrot family.'},
        'aliases': ['ara', 'qizil ara', 'красный ара', 'ара', 'scarlet macaw']},
    {   'id': 'nature_macro_018_greater_flamingo',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Oqqush', 'Flamingo', 'Pelikan', 'Ibis'],
                       'ru': ['Лебедь', 'Фламинго', 'Пеликан', 'Ибис'],
                       'en': ['Swan', 'Greater Flamingo', 'Pelican', 'Ibis']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Flamingo', 'ru': 'Фламинго', 'en': 'Greater Flamingo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flamingo_feathers_close_up.jpg/800px-Flamingo_feathers_close_up.jpg',
        'fun_fact': {   'uz': "Flamingo patlarining pushti rangi uning ozuqasidagi mikro suv o'tlari va qisqichbaqalar "
                              'tarkibidagi karotinoidlardan olinadi.',
                        'ru': 'Розовый цвет перьев фламинго обусловлен накоплением бета-каротина и кантаксантина из '
                              'потребляемых ракообразных.',
                        'en': 'Flamingo feathers acquire their signature pink plumage from carotenoid pigments '
                              'extracted from digested Artemia brine shrimp.'},
        'aliases': ['flamingo', 'фламинго', 'greater flamingo']},
    {   'id': 'nature_macro_019_emperor_penguin',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["O'rdak", "G'oz", 'Imperator pingvini', 'Albatros'],
                       'ru': ['Утка', 'Гусь', 'Императорский пингвин', 'Альбатрос'],
                       'en': ['Duck', 'Goose', 'Emperor Penguin', 'Albatross']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Imperator pingvini', 'ru': 'Императорский пингвин', 'en': 'Emperor Penguin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Penguin_feathers_detail.jpg/800px-Penguin_feathers_detail.jpg',
        'fun_fact': {   'uz': 'Pingvin patlari kvadrat santimetriga 100 tagacha zichlikda joylashib, qattiq shamol va '
                              "muzdek suv o'tishiga to'sqinlik qiladi.",
                        'ru': 'Перья пингвинов чешуйчатые и сверхплотные (до 100 на см²), полностью защищают птицу от '
                              'антарктической ледяной воды.',
                        'en': 'Emperor penguin scale-like contour feathers overlap at 100 per cm² to form an '
                              'impervious barrier against freezing ocean water.'},
        'aliases': ['pingvin', 'imperator pingvini', 'пингвин', 'императорский пингвин', 'emperor penguin']},
    {   'id': 'nature_macro_020_polar_bear',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Qo'ng'ir ayiq", "Qutb bo'risi", 'Panda', 'Oq ayiq'],
                       'ru': ['Бурый медведь', 'Полярный волк', 'Панда', 'Белый медведь'],
                       'en': ['Grizzly Bear', 'Arctic Wolf', 'Giant Panda', 'Polar Bear']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Oq ayiq', 'ru': 'Белый медведь', 'en': 'Polar Bear'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Polar_bear_fur_macro.jpg/800px-Polar_bear_fur_macro.jpg',
        'fun_fact': {   'uz': 'Oq ayiqning juni aslida rangsiz shaffof naychalardan iborat, uning ostidagi terisi esa '
                              'quyosh issiqligini yutuvchi qora rangdadir.',
                        'ru': 'Шерсть белого медведя полая и прозрачная, а кожа под ней совершенно черная, поглощающая '
                              'ультрафиолетовое излучение.',
                        'en': 'Polar bear guard hairs are hollow and transparent, trapping insulating air, while the '
                              'skin underneath is completely black.'},
        'aliases': ['oq ayiq', 'белый медведь', 'polar bear']},
    {   'id': 'nature_macro_021_giant_panda',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Ulkan panda', 'Koala', 'Qora ayiq', 'Tapir'],
                       'ru': ['Большая панда', 'Коала', 'Барибал', 'Тапир'],
                       'en': ['Giant Panda', 'Koala', 'Black Bear', 'Tapir']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Ulkan panda', 'ru': 'Большая панда', 'en': 'Giant Panda'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Giant_Panda_fur_texture.jpg/800px-Giant_Panda_fur_texture.jpg',
        'fun_fact': {   'uz': "Pandaning qalin jun qatlami yog'li bo'lib, nam bambuk o'rmonlaridagi yomg'ir va qor "
                              "tomchilarini o'ziga yuqtirmay qaytaradi.",
                        'ru': 'Плотная шерсть панды пропитана водоотталкивающим жировым секретом, спасающим её в сырых '
                              'горных бамбуковых чащах.',
                        'en': 'Giant panda fur is oily and thick, providing water-repellent protection in damp, rainy '
                              'Sichuan bamboo cloud forests.'},
        'aliases': ['panda', 'katta panda', 'большая панда', 'панда', 'giant panda']},
    {   'id': 'nature_macro_022_koala',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Vombat', 'Koala', 'Dangasa (Sloth)', 'Possum'],
                       'ru': ['Вомбат', 'Коала', 'Ленивец', 'Опоссум'],
                       'en': ['Wombat', 'Koala', 'Sloth', 'Opossum']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Koala', 'ru': 'Коала', 'en': 'Koala'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Koala_fur_close_up.jpg/800px-Koala_fur_close_up.jpg',
        'fun_fact': {   'uz': "Koalaning jilosiz jun qoplami yomg'irpo'shdek suv o'tkazmaydi va eukalipt daraxtlarida "
                              'quyosh nurlarini samarali qaytaradi.',
                        'ru': 'Густая шерсть коалы действует как натуральный дождевик, отталкивая воду и защищая от '
                              'температурных перепадов.',
                        'en': "A koala's thick, woolly fur functions like a raincoat, insulating the marsupial against "
                              'rain, wind, and severe temperature fluctuations.'},
        'aliases': ['koala', 'коала', 'koala']},
    {   'id': 'nature_macro_023_ring_tailed_lemur',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Yenot', 'Skuns', 'Halqali lemur', 'Lori'],
                       'ru': ['Енот', 'Скунс', 'Кошачий лемур', 'Лори'],
                       'en': ['Raccoon', 'Skunk', 'Ring-tailed Lemur', 'Loris']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Halqali lemur', 'ru': 'Кошачий лемур', 'en': 'Ring-tailed Lemur'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Ring-tailed_lemur_tail_stripes.jpg/800px-Ring-tailed_lemur_tail_stripes.jpg',
        'fun_fact': {   'uz': "Halqali lemur dumida aniq 13 ta oq va 13 ta qora halqa bo'ladi, bu to'da a'zolariga "
                              "baland o'tlar orasida aloqa saqlashga xizmat qiladi.",
                        'ru': 'Хвост кошачьего лемура украшен ровно 13 черными и 13 белыми полосами и служит '
                              'визуальным маяком в стае.',
                        'en': 'The tail of a ring-tailed lemur has exactly 13 alternating black and white rings, held '
                              'high like a flag for troop cohesion.'},
        'aliases': ['lemur', 'halqali lemur', 'лемур', 'кошачий лемур', 'ring-tailed lemur']},
    {   'id': 'nature_macro_024_red_panda',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Tulki', 'Yenot', 'Sincob', 'Qizil panda'],
                       'ru': ['Лиса', 'Енот', 'Белка', 'Красная панда'],
                       'en': ['Fox', 'Raccoon', 'Squirrel', 'Red Panda']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Qizil panda', 'ru': 'Красная панда', 'en': 'Red Panda'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Red_Panda_fur_detail.jpg/800px-Red_Panda_fur_detail.jpg',
        'fun_fact': {   'uz': "Qizil pandaning oyoq tagi ham qalin jun bilan qoplangan bo'lib, u qor va muzli "
                              "novdalarda sirg'anmasdan yurishga yordam beradi.",
                        'ru': 'Подошвы лап красной панды полностью покрыты густой шерстью, предотвращающей скольжение '
                              'по обледенелым ветвям.',
                        'en': "The soles of a red panda's paws are completely covered in dense insulating fur, "
                              'providing traction on icy high-altitude branches.'},
        'aliases': ['qizil panda', 'красная панда', 'red panda']},
    {   'id': 'nature_macro_025_european_hedgehog',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Tipratikan', 'Jayra', 'Yexidna', 'Tenrek'],
                       'ru': ['Обыкновенный ёж', 'Дикобраз', 'Ехидна', 'Тенрек'],
                       'en': ['European Hedgehog', 'Porcupine', 'Echidna', 'Tenrec']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Tipratikan', 'ru': 'Обыкновенный ёж', 'en': 'European Hedgehog'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Hedgehog_quills_macro.jpg/800px-Hedgehog_quills_macro.jpg',
        'fun_fact': {   'uz': "Tipratikanning 5000 dan 7000 tagacha bo'lgan ninalari ichi g'ovak bo'shliqdan iborat "
                              "bo'lib, o'zaro keratin to'siqlar bilan mustahkamlangan.",
                        'ru': 'Иглы ежа (до 7000 штук) полые внутри и укреплены продольными кератиновыми перегородками '
                              'для легкости и прочности.',
                        'en': 'A hedgehog possesses up to 7,000 hollow spines reinforced with internal keratin struts '
                              'to absorb severe impact shocks.'},
        'aliases': ['tipratikan', 'еж', 'ёж', 'обыкновенный еж', 'hedgehog']},
    {   'id': 'nature_macro_026_crested_porcupine',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Tipratikan', 'Jayra', 'Yexidna', 'Pangolin'],
                       'ru': ['Ёж', 'Хохлатый дикобраз', 'Ехидна', 'Панголин'],
                       'en': ['Hedgehog', 'Crested Porcupine', 'Echidna', 'Pangolin']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Jayra', 'ru': 'Хохлатый дикобраз', 'en': 'Crested Porcupine'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Porcupine_quills_macro_detail.jpg/800px-Porcupine_quills_macro_detail.jpg',
        'fun_fact': {   'uz': 'Jayra ninalari uzunligi 35 santimetrgacha yetadi va ularning uchidagi mayda ilmoqchalar '
                              'yirtqich terisiga chuqur botib ketadi.',
                        'ru': 'Иглы дикобраза достигают 35 см в длину и имеют микроскопические зазубрины, затрудняющие '
                              'их извлечение из раны.',
                        'en': 'Porcupine quills can reach 35 cm in length and are equipped with backward-facing '
                              'microscopic barbs that work deeper into predator flesh.'},
        'aliases': ['jayra', 'дикобраз', 'хохлатый дикобраз', 'porcupine']},
    {   'id': 'nature_macro_027_sunda_pangolin',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Bronenosets', 'Timsoh', 'Pangolin', 'Kaltakesak'],
                       'ru': ['Броненосец', 'Крокодил', 'Яванский панголин', 'Ящерица'],
                       'en': ['Armadillo', 'Crocodile', 'Sunda Pangolin', 'Lizard']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Pangolin', 'ru': 'Яванский панголин', 'en': 'Sunda Pangolin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Pangolin_scales_detail.jpg/800px-Pangolin_scales_detail.jpg',
        'fun_fact': {   'uz': "Pangolin — tanasi keratin tangachalar bilan to'liq qoplangan yer yuzidagi yagona "
                              'sutemizuvchi hayvondir.',
                        'ru': 'Панголины — единственные млекопитающие на Земле, чье тело покрыто крупными подвижными '
                              'кератиновыми чешуями.',
                        'en': 'Pangolins are the only known mammals with large, protective keratin scales covering '
                              'their skin, comprising 20% of their body weight.'},
        'aliases': ['pangolin', 'панголин', 'яванский панголин']},
    {   'id': 'nature_macro_028_nine_banded_armadillo',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Pangolin', 'Toshbaqa', 'Gekkon', 'Bronenosets'],
                       'ru': ['Панголин', 'Черепаха', 'Геккон', 'Девятипоясный броненосец'],
                       'en': ['Pangolin', 'Tortoise', 'Gecko', 'Nine-banded Armadillo']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Bronenosets', 'ru': 'Девятипоясный броненосец', 'en': 'Nine-banded Armadillo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Armadillo_carapace_macro.jpg/800px-Armadillo_carapace_macro.jpg',
        'fun_fact': {   'uz': "Bronenosets sovuti suyaklashgan teri plastinkalaridan iborat bo'lib, harakatchan "
                              "belbog'lar unga koptokdek dumalash imkonini beradi.",
                        'ru': 'Панцирь броненосца состоит из окостеневших кожных щитков, соединенных эластичными '
                              'полосами соединительной ткани.',
                        'en': "An armadillo's shell consists of true dermal bone plates overlaid with small epidermal "
                              'scales, joined by flexible skin bands.'},
        'aliases': ['bronenosets', 'броненосец', 'девятипоясный броненосец', 'armadillo']},
    {   'id': 'nature_macro_029_galapagos_tortoise',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Galapagos toshbaqasi', 'Dengiz toshbaqasi', 'Timsoh', 'Armadillo'],
                       'ru': ['Галапагосская черепаха', 'Морская черепаха', 'Крокодил', 'Броненосец'],
                       'en': ['Galapagos Tortoise', 'Sea Turtle', 'Crocodile', 'Armadillo']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Galapagos toshbaqasi', 'ru': 'Галапагосская черепаха', 'en': 'Galapagos Tortoise'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Tortoise_shell_scutes_detail.jpg/800px-Tortoise_shell_scutes_detail.jpg',
        'fun_fact': {   'uz': "Toshbaqa kosasidagi konsentrik halqalar daraxt yillik halqalari kabi o'sish davrlarini "
                              "ko'rsatadi.",
                        'ru': 'Концентрические кольца на щитках панциря черепахи отражают периоды активного роста '
                              'животного.',
                        'en': 'Growth rings (sulci) on tortoise carapace scutes record seasonal growth spurts, similar '
                              'to the growth rings of trees.'},
        'aliases': ['galapagos toshbaqasi', 'toshbaqa', 'галапагосская черепаха', 'черепаха', 'galapagos tortoise']},
    {   'id': 'nature_macro_030_green_sea_turtle',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Quruqlik toshbaqasi', 'Yashil dengiz toshbaqasi', 'Pangolin', 'Alligator'],
                       'ru': ['Сухопутная черепаха', 'Зеленая черепаха', 'Панголин', 'Аллигатор'],
                       'en': ['Land Tortoise', 'Green Sea Turtle', 'Pangolin', 'Alligator']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Yashil dengiz toshbaqasi', 'ru': 'Зеленая черепаха', 'en': 'Green Sea Turtle'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Sea_turtle_carapace_macro.jpg/800px-Sea_turtle_carapace_macro.jpg',
        'fun_fact': {   'uz': 'Dengiz toshbaqasining kosasi suvda suzish qarshiligini kamaytirish uchun tekis va '
                              'gidrodinamik shaklda shakllangan.',
                        'ru': 'Панцирь зеленой морской черепахи обтекаемый и гладкий для минимизации трения о воду при '
                              'дальних миграциях.',
                        'en': 'Green sea turtle carapaces are hydrodynamically streamlined and lightweight compared to '
                              'the domed shells of terrestrial tortoises.'},
        'aliases': [   'yashil toshbaqa',
                       'dengiz toshbaqasi',
                       'зеленая черепаха',
                       'морская черепаха',
                       'green sea turtle']},
    {   'id': 'nature_macro_031_blue_whale',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Kashalot', 'Oq kit', "Ko'k kit", 'Morj'],
                       'ru': ['Кашалот', 'Белуха', 'Синий кит', 'Морж'],
                       'en': ['Sperm Whale', 'Beluga', 'Blue Whale', 'Walrus']},
        'correct_index': 2,
        'correct_answer': {'uz': "Ko'k kit", 'ru': 'Синий кит', 'en': 'Blue Whale'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Blue_whale_ventral_grooves_macro.jpg/800px-Blue_whale_ventral_grooves_macro.jpg',
        'fun_fact': {   'uz': "Ko'k kitning tomog'idagi 60 dan 90 tagacha bo'lgan chuqur burmalar ozuqa yutayotganda "
                              'tomoq qopini ulkan hajmda kengaytirishga imkon beradi.',
                        'ru': 'Продольные складки на горле синего кита позволяют глотке растягиваться, вмещая до 90 '
                              'тонн воды с крилем.',
                        'en': 'The 60 to 90 ventral throat grooves of a blue whale expand accordion-style to engulf up '
                              'to 90 metric tons of water and krill in a single gulp.'},
        'aliases': ['kok kit', "ko'k kit", 'синий кит', 'blue whale']},
    {   'id': 'nature_macro_032_manta_ray',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Akula', 'Skat-xvostokol', 'Kit', 'Manta'],
                       'ru': ['Акула', 'Хвостокол', 'Кит', 'Гигантский морской дьявол (Манта)'],
                       'en': ['Shark', 'Stingray', 'Whale', 'Giant Manta Ray']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Manta', 'ru': 'Гигантский морской дьявол (Манта)', 'en': 'Giant Manta Ray'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Manta_ray_skin_dermal_denticles.jpg/800px-Manta_ray_skin_dermal_denticles.jpg',
        'fun_fact': {   'uz': "Manta tanasi ham xuddi akulalar kabi mayda teri tishchalari bilan qoplangan bo'lib, "
                              "unga baxmalsimon silliqlik bag'ishlaydi.",
                        'ru': 'Кожа манты покрыта мелкими кожными зубчиками, создающими бархатистую текстуру и '
                              'защищающими от паразитов.',
                        'en': 'Manta rays possess minute dermal denticles embedded in their skin, giving it a velvety '
                              'texture and repelling biofouling parasites.'},
        'aliases': ['manta', 'manta daryosi', 'манта', 'морской дьявол', 'manta ray']},
    {   'id': 'nature_macro_033_giant_pacific_octopus',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Ulkan Tinch okean sakkizoyog'i", 'Kalmar', 'Siyohbaliq', 'Meduza'],
                       'ru': ['Гигантский осьминог', 'Кальмар', 'Каракатица', 'Медуза'],
                       'en': ['Giant Pacific Octopus', 'Squid', 'Cuttlefish', 'Jellyfish']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Ulkan Tinch okean sakkizoyog'i",
                              'ru': 'Гигантский осьминог',
                              'en': 'Giant Pacific Octopus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octopus_skin_chromatophores_macro.jpg/800px-Octopus_skin_chromatophores_macro.jpg',
        'fun_fact': {   'uz': 'Sakkizoyoq terisidagi millionlab elastik pigment qopchalari (xromatoforlar) '
                              "millisoniyalar ichida kengayib rangni o'zgartiradi.",
                        'ru': 'Хроматофоры кожи осьминога управляются мышцами напрямую от нервной системы, меняя цвет '
                              'за миллисекунды.',
                        'en': 'Octopus skin chromatophores are elastic pigment sacs directly wired to the brain, '
                              'expanding or contracting within milliseconds.'},
        'aliases': ['sakkizoyoq', 'ulkan sakkizoyoq', 'осьминог', 'гигантский осьминог', 'octopus']},
    {   'id': 'nature_macro_034_cuttlefish',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Sakkizoyoq', 'Siyohbaliq (Karakatitsa)', 'Kalmar', 'Nautilus'],
                       'ru': ['Осьминог', 'Каракатица', 'Кальмар', 'Наутилус'],
                       'en': ['Octopus', 'Cuttlefish', 'Squid', 'Nautilus']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Siyohbaliq (Karakatitsa)', 'ru': 'Каракатица', 'en': 'Cuttlefish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Cuttlefish_skin_texture_papillae.jpg/800px-Cuttlefish_skin_texture_papillae.jpg',
        'fun_fact': {   'uz': 'Karakatitsa nafaqat rangini, balki terisidagi maxsus papillalarni shishirib marjon '
                              'qoyalar yoki qum relyingini 3D shaklida takrorlay oladi.',
                        'ru': 'Каракатица способна мгновенно менять не только цвет, но и 3D-текстуру кожи с помощью '
                              'мышечных бугорков (папилл).',
                        'en': 'Cuttlefish can dynamically alter both skin pigmentation and physical 3D topography '
                              'using muscular papillae to mimic coral and rocks.'},
        'aliases': ['siyohbaliq', 'karakatitsa', 'каракатица', 'cuttlefish']},
    {   'id': 'nature_macro_035_blue_ringed_octopus',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Oddiy sakkizoyoq', 'Dengiz anemonasi', "Ko'k halqali sakkizoyoq", 'Kalmar'],
                       'ru': ['Обычный осьминог', 'Актиния', 'Синекольчатый осьминог', 'Кальмар'],
                       'en': ['Common Octopus', 'Sea Anemone', 'Blue-ringed Octopus', 'Squid']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Ko'k halqali sakkizoyoq",
                              'ru': 'Синекольчатый осьминог',
                              'en': 'Blue-ringed Octopus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Blue-ringed_octopus_macro.jpg/800px-Blue-ringed_octopus_macro.jpg',
        'fun_fact': {   'uz': "Ko'k halqali sakkizoyoq xavf sezganda uning tanasidagi elektr ko'k halqalar yorqin "
                              "chaqnab ogohlantiradi; uning zahari bir necha daqiqada o'ldiradi.",
                        'ru': 'При угрозе синекольчатый осьминог пульсирует яркими сапфировыми кольцами, предупреждая '
                              'о смертоносном тетродотоксине.',
                        'en': 'When threatened, the blue-ringed octopus flashes iridescent blue rings illuminated by '
                              'multi-layer iridophores, warning of lethal tetrodotoxin.'},
        'aliases': ['kok halqali sakkizoyoq', 'синекольчатый осьминог', 'blue-ringed octopus']},
    {   'id': 'nature_macro_036_starfish',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Dengiz tipratikani', 'Dengiz bodringi', 'Ofiura', 'Dengiz yulduzi'],
                       'ru': ['Морской еж', 'Голотурия', 'Офиура', 'Морская звезда'],
                       'en': ['Sea Urchin', 'Sea Cucumber', 'Brittle Star', 'Sea Star (Starfish)']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Dengiz yulduzi', 'ru': 'Морская звезда', 'en': 'Sea Star (Starfish)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Starfish_skin_ossicles_macro.jpg/800px-Starfish_skin_ossicles_macro.jpg',
        'fun_fact': {   'uz': 'Dengiz yulduzining ustki terisi ohaklangan mayda plastinkalar va terini axlatlardan '
                              "tozalovchi mikroskopik qisqichlar (peditsellyariyalar) bilan to'la.",
                        'ru': 'Поверхность морской звезды покрыта известковыми бугорками и микроскопическими '
                              'щипчиками-педицелляриями, очищающими кожу.',
                        'en': 'Sea star skin features calcified dermal ossicles and microscopic claw-like '
                              'pedicellariae that clear parasites and debris from the dermis.'},
        'aliases': ['dengiz yulduzi', 'морская звезда', 'starfish', 'sea star']},
    {   'id': 'nature_macro_037_crown_of_thorns',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Tikanli toj dengiz yulduzi', 'Oddiy dengiz yulduzi', 'Dengiz kirpisi', 'Aktiniya'],
                       'ru': ['Терновый венец', 'Обычная звезда', 'Морской еж', 'Актиния'],
                       'en': ['Crown-of-thorns Starfish', 'Common Starfish', 'Sea Urchin', 'Anemone']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Tikanli toj dengiz yulduzi',
                              'ru': 'Терновый венец',
                              'en': 'Crown-of-thorns Starfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Acanthaster_planci_thorns_macro.jpg/800px-Acanthaster_planci_thorns_macro.jpg',
        'fun_fact': {   'uz': "Ushbu yulduzning 4-5 santimetrli o'tkir tikanlari zaharli pliaplizin moddasi bilan "
                              "qoplangan bo'lib, marjon poliplari bilan oziqlanadi.",
                        'ru': 'Иглы морской звезды «терновый венец» пропитаны токсинами-сапонинами и могут наносить '
                              'сильнейшие ожоги.',
                        'en': 'The venomous spines of the crown-of-thorns starfish can reach 5 cm in length, secreting '
                              'plancitoxin enzymes that dissolve coral tissue.'},
        'aliases': ['ternoviy venets', 'tikanli toj', 'терновый венец', 'crown-of-thorns']},
    {   'id': 'nature_macro_038_sea_urchin',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Dengiz yulduzi', 'Dengiz tipratikani', 'Krab', 'Oroliq marjoni'],
                       'ru': ['Морская звезда', 'Морской ёж', 'Краб', 'Коралл'],
                       'en': ['Sea Star', 'Sea Urchin', 'Crab', 'Coral']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Dengiz tipratikani', 'ru': 'Морской ёж', 'en': 'Sea Urchin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Sea_urchin_spines_macro.jpg/800px-Sea_urchin_spines_macro.jpg',
        'fun_fact': {   'uz': "Dengiz tipratikanining ninalari kalsiy karbonat kristallaridan iborat bo'lib, sharli "
                              "bo'g'imlar yordamida barcha tomonga harakatlanadi.",
                        'ru': 'Иглы морского ежа состоят из монокристаллов кальцита и крепятся к панцирю с помощью '
                              'подвижных шаровидных суставов.',
                        'en': 'Sea urchin spines are composed of single-crystal calcite and articulate on '
                              'ball-and-socket joints driven by circular muscle fibers.'},
        'aliases': ['dengiz tipratikani', 'морской еж', 'морской ёж', 'sea urchin']},
    {   'id': 'nature_macro_039_moray_eel',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Ilonbaliq', 'Dengiz iloni', 'Murena', 'Akula'],
                       'ru': ['Угорь', 'Морская змея', 'Мурена', 'Акула'],
                       'en': ['Conger Eel', 'Sea Snake', 'Moray Eel', 'Shark']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Murena', 'ru': 'Мурена', 'en': 'Moray Eel'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Moray_eel_skin_macro.jpg/800px-Moray_eel_skin_macro.jpg',
        'fun_fact': {   'uz': "Murenada tangacha bo'lmaydi; uning qalin terisi himoyalovchi zaharli shilliq qatlam "
                              "bilan qoplangan bo'ladi.",
                        'ru': 'У мурены полностью отсутствует чешуя; ее плотная кожа покрыта ядовитой бактерицидной '
                              'слизью.',
                        'en': 'Moray eels lack scales entirely; their tough, leathery skin is cloaked in a thick layer '
                              'of toxic, antimicrobial mucus.'},
        'aliases': ['murena', 'мурена', 'moray eel']},
    {   'id': 'nature_macro_040_clownfish',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Zolotoy ribka', 'Guppi', 'Xirurg baliq', 'Masxaraboz baliq (Amfiprion)'],
                       'ru': ['Золотая рыбка', 'Гуппи', 'Рыба-хирург', 'Рыба-клоун (Амфиприон)'],
                       'en': ['Goldfish', 'Guppy', 'Surgeonfish', 'Clownfish']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Masxaraboz baliq (Amfiprion)', 'ru': 'Рыба-клоун (Амфиприон)', 'en': 'Clownfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Amphiprion_ocellaris_skin_macro.jpg/800px-Clownfish_skin_macro.jpg',
        'fun_fact': {   'uz': 'Masxaraboz baliq terisidagi maxsus shilliq qatlam dengiz anemonlarining kuydiruvchi '
                              "zaharli paypaslagichlaridan to'liq himoya qiladi.",
                        'ru': 'Слизь на чешуе рыбы-клоуна химически имитирует состав самой актинии, поэтому та не '
                              'жалит своего жильца.',
                        'en': "A clownfish's mucosal coat chemically mimics the sea anemone's own mucus, preventing "
                              'nematocysts from stinging the fish.'},
        'aliases': ['masxaraboz baliq', 'amfiprion', 'рыба-клоун', 'амфиприон', 'clownfish']},
    {   'id': 'nature_macro_041_seahorse',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Dengiz oti', 'Ignabaliq', 'Krab', 'Krevetka'],
                       'ru': ['Морской конёк', 'Рыба-игла', 'Краб', 'Креветка'],
                       'en': ['Seahorse', 'Pipefish', 'Crab', 'Shrimp']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Dengiz oti', 'ru': 'Морской конёк', 'en': 'Seahorse'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Seahorse_bony_rings_macro.jpg/800px-Seahorse_bony_rings_macro.jpg',
        'fun_fact': {   'uz': "Dengiz otining tanasida tangachalar o'rniga tashqi suyak halqalari bo'lib, u "
                              'yirtqichlar bosimiga chidamli mustahkam karkas hosil qiladi.',
                        'ru': 'Тело морского конька заключено в панцирь из костных сегментных колец, способный '
                              'выдерживать сильное сжатие.',
                        'en': 'Instead of traditional scales, seahorses possess fused rectangular bony plates arranged '
                              'in rings that resist crushing forces.'},
        'aliases': ['dengiz oti', 'морской конек', 'морской конёк', 'seahorse']},
    {   'id': 'nature_macro_042_tokay_gecko',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Iguana', 'Gekkon', 'Varan', 'Salamandra'],
                       'ru': ['Игуана', 'Геккон токи', 'Варан', 'Саламандра'],
                       'en': ['Iguana', 'Tokay Gecko', 'Monitor Lizard', 'Salamander']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Gekkon', 'ru': 'Геккон токи', 'en': 'Tokay Gecko'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gecko_foot_setae_macro.jpg/800px-Gecko_foot_setae_macro.jpg',
        'fun_fact': {   'uz': 'Gekkon oyoqlaridagi millionlab mikroskopik tukchalar (setae) van-der-Vaals molekulyar '
                              'tortishish kuchi orqali shisha devorlarda yurishga imkon beradi.',
                        'ru': 'Миллионы наноразмерных щетинок на лапках геккона удерживают его на гладком стекле за '
                              'счет сил Ван-дер-Ваальса.',
                        'en': 'Gecko foot pads feature millions of microscopic setae terminating in spatulae that '
                              'generate molecular van der Waals adhesion.'},
        'aliases': ['gekkon', 'геккон', 'геккон токи', 'tokay gecko', 'gecko']},
    {   'id': 'nature_macro_043_marine_iguana',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Yashil iguana', 'Varan', 'Dengiz iguanasi', 'Xameleon'],
                       'ru': ['Зеленая игуана', 'Варан', 'Морская игуана', 'Хамелеон'],
                       'en': ['Green Iguana', 'Monitor Lizard', 'Marine Iguana', 'Chameleon']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Dengiz iguanasi', 'ru': 'Морская игуана', 'en': 'Marine Iguana'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Marine_iguana_head_scales_macro.jpg/800px-Marine_iguana_head_scales_macro.jpg',
        'fun_fact': {   'uz': 'Dengiz iguanasi Galapagoda okean suvidan ortiqcha tuzni burni orqali aksirib chiqaradi, '
                              'natijada bosh tangachalari oq tuz qatlami bilan qoplanadi.',
                        'ru': 'Морские игуаны выводят избыток соли через носовые железы, «чихая» соляным раствором, '
                              'покрывающим их чешую коркой.',
                        'en': 'Marine iguanas expel excess ingested sea salt through specialized nasal glands, '
                              'encrusting their cranial scales in white salt crystals.'},
        'aliases': ['dengiz iguanasi', 'морская игуана', 'marine iguana']},
    {   'id': 'nature_macro_044_poison_dart_frog',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': [   'Daraxt qurbaqasi',
                                 'Qoraqurbaqa',
                                 'Suv qurbaqasi',
                                 'Zaharli daraxt qurbaqasi (Drevolaz)'],
                       'ru': ['Квакша', 'Жаба', 'Тритон', 'Древолаз (Ядовитая лягушка)'],
                       'en': ['Tree Frog', 'Toad', 'Newt', 'Poison Dart Frog']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Zaharli daraxt qurbaqasi (Drevolaz)',
                              'ru': 'Древолаз (Ядовитая лягушка)',
                              'en': 'Poison Dart Frog'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Dendrobates_tinctorius_skin_macro.jpg/800px-Dendrobates_tinctorius_skin_macro.jpg',
        'fun_fact': {   'uz': 'Drevolazning terisidagi yorqin ogohlantiruvchi ranglar (aposematizm) yirtqichlarni '
                              "uning o'ta halokatli alkaloid zaharidan ogoh etadi.",
                        'ru': 'Яркая ядовитая окраска древолаза служит апосематическим сигналом: в коже одной особи '
                              'содержится яд, способный убить 10 человек.',
                        'en': 'The vivid coloration of poison dart frogs is aposematic warning coloration; their '
                              'granular skin glands secrete lethal batrachotoxins.'},
        'aliases': ['drevolaz', 'zaharli qurbaqa', 'древолаз', 'ядовитая лягушка', 'poison dart frog']},
    {   'id': 'nature_macro_045_red_eyed_tree_frog',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Qizilko'z daraxt qurbaqasi", 'Drevolaz', 'Qoraqurbaqa', 'Aksolotl'],
                       'ru': ['Красноглазая квакша', 'Древолаз', 'Жаба', 'Аксалотль'],
                       'en': ['Red-eyed Tree Frog', 'Poison Dart Frog', 'Toad', 'Axolotl']},
        'correct_index': 0,
        'correct_answer': {'uz': "Qizilko'z daraxt qurbaqasi", 'ru': 'Красноглазая квакша', 'en': 'Red-eyed Tree Frog'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Agalychnis_callidryas_eye_macro.jpg/800px-Agalychnis_callidryas_eye_macro.jpg',
        'fun_fact': {   'uz': "Ushbu qurbaqaning yorqin yoqut ko'zlari va zumrad yashil orqasi yirtqich hujum qilgan "
                              "lahzada uni karaxt qilib qo'yish (startle display) uchun xizmat qiladi.",
                        'ru': 'Внезапно распахивая огромные алые глаза, эта квакша ошеломляет хищника на пару секунд, '
                              'успевая скрыться.',
                        'en': 'The startling ruby-red eyes of Agalychnis callidryas serve as a flash-defense mechanism '
                              'to paralyze visually hunting predators with shock.'},
        'aliases': ['qizilkoz daraxt qurbagasi', 'красноглазая квакша', 'red-eyed tree frog']},
    {   'id': 'nature_macro_046_common_toad',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Yashil baqa', 'Qoraqurbaqa', 'Drevolaz', 'Salamandra'],
                       'ru': ['Лягушка', 'Обыкновенная жаба', 'Древолаз', 'Саламандра'],
                       'en': ['Pond Frog', 'Common Toad', 'Dart Frog', 'Salamander']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qoraqurbaqa', 'ru': 'Обыкновенная жаба', 'en': 'Common Toad'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Bufo_bufo_parotoid_macro.jpg/800px-Bufo_bufo_parotoid_macro.jpg',
        'fun_fact': {   'uz': "Qoraqurbaqa terisidagi so'galsimon bo'rtmalar orasida parotid bezlar joylashgan bo'lib, "
                              'ular bufotoxin deb ataluvchi achchiq zahar ishlab chiqaradi.',
                        'ru': 'Бугорки на коже жабы — это железы, а за глазами расположены крупные околоушные железы '
                              '(паротиды), выделяющие токсин буфотоксин.',
                        'en': "A toad's warty dermal glands and prominent post-orbital parotoid glands secrete "
                              'foul-tasting, cardioactive bufotoxins.'},
        'aliases': ['qoraqurbaqa', 'жаба', 'обыкновенная жаба', 'toad', 'common toad']},
    {   'id': 'nature_macro_047_axolotl',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Salamandra', 'Triton', 'Aksolotl', 'Baqachanoq'],
                       'ru': ['Саламандра', 'Тритон', 'Аксалотль', 'Протей'],
                       'en': ['Salamander', 'Newt', 'Axolotl', 'Olm']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Aksolotl', 'ru': 'Аксалотль', 'en': 'Axolotl'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Axolotl_external_gills_macro.jpg/800px-Axolotl_external_gills_macro.jpg',
        'fun_fact': {   'uz': "Aksolotl boshidagi shoxdek ko'ringan qizil patsimon tuzilmalar uning qon tomirlariga "
                              'boy tashqi jabralari hisoblanadi.',
                        'ru': 'Ветвистые красные отростки по бокам головы аксолотля — это внешние жабры, через которые '
                              'он поглощает кислород из воды.',
                        'en': "The feathery ruffs protruding from an axolotl's head are vascularized external gills "
                              'coated in delicate respiratory filaments.'},
        'aliases': ['aksolotl', 'аксолотль', 'axolotl']},
    {   'id': 'nature_macro_048_toco_toucan',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Qarqara', 'Kakadu', 'Pelikan', 'Tukan'],
                       'ru': ['Цапля', 'Какаду', 'Пеликан', 'Большой тукан'],
                       'en': ['Heron', 'Cockatoo', 'Pelican', 'Toco Toucan']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Tukan', 'ru': 'Большой тукан', 'en': 'Toco Toucan'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Toco_toucan_beak_macro.jpg/800px-Toco_toucan_beak_macro.jpg',
        'fun_fact': {   'uz': "Tukanning ulkan tumshug'i qattiq bo'lsa-da juda yengil, chunki uning ichi ko'piksimon "
                              "keratin va suyak to'ridan iborat.",
                        'ru': 'Огромный клюв тукана удивительно легкий: внутри он состоит из губчатой сети костных '
                              'балочек и пенистого кератина.',
                        'en': "A toucan's massive bill comprises an ultra-lightweight cellular matrix of bony "
                              'trabeculae wrapped in a keratin sheath, acting as a thermal radiator.'},
        'aliases': ['tukan', 'тукан', 'большой тукан', 'toucan', 'toco toucan']},
    {   'id': 'nature_macro_049_bald_eagle',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Oqbosh burgut', 'Lochin', 'Qoraburgut', 'Kondor'],
                       'ru': ['Белоголовый орлан', 'Сокол', 'Беркут', 'Кондор'],
                       'en': ['Bald Eagle', 'Falcon', 'Golden Eagle', 'Condor']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Oqbosh burgut', 'ru': 'Белоголовый орлан', 'en': 'Bald Eagle'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Bald_eagle_eye_and_cere_macro.jpg/800px-Bald_eagle_eye_and_cere_macro.jpg',
        'fun_fact': {   'uz': "Burgut ko'zidagi ikkita ko'rish chuqurchasi (fovea) tufayli u odamdan 4-5 baravar "
                              "uzoqroqdagi o'ljani tiniq ko'ra oladi.",
                        'ru': 'Орлы обладают бифокальным зрением благодаря двум центральным ямкам в сетчатке, различая '
                              'добычу за 3 километра.',
                        'en': 'Bald eagles possess two foveae per eye, providing both forward stereoscopic depth '
                              'perception and ultra-sharp peripheral vision.'},
        'aliases': ['oqbosh burgut', 'burgut', 'белоголовый орлан', 'орлан', 'bald eagle']},
    {   'id': 'nature_macro_050_domestic_cat',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['It', "Mushuk (ko'zi)", "Bo'ri", 'Tulki'],
                       'ru': ['Собака', 'Домашняя кошка', 'Волк', 'Шакал'],
                       'en': ['Dog', 'Domestic Cat', 'Wolf', 'Jackal']},
        'correct_index': 1,
        'correct_answer': {'uz': "Mushuk (ko'zi)", 'ru': 'Домашняя кошка', 'en': 'Domestic Cat'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Cat_eye_slit_pupil_macro.jpg/800px-Cat_eye_slit_pupil_macro.jpg',
        'fun_fact': {   'uz': "Mushukning vertikal yoriqsimon qorachig'i yorug'lik miqdorini 135 baravargacha "
                              "o'zgartirib, kechasi mukammal ov qilishga imkon beradi.",
                        'ru': 'Вертикальный щелевидный зрачок кошки может расширяться в 135 раз, позволяя охотиться и '
                              'в темноте, и на ярком солнце.',
                        'en': "A cat's vertical slit pupil can expand its area by a factor of 135, providing "
                              'extraordinary optical dynamic range for ambush predation.'},
        'aliases': ['mushuk', 'кошка', 'домашняя кошка', 'cat', 'domestic cat']},
    {   'id': 'nature_macro_051_domestic_goat',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Ot', 'Sigir', "Echki (ko'zi)", "Qo'y"],
                       'ru': ['Лошадь', 'Корова', 'Коза (глаз)', 'Олень'],
                       'en': ['Horse', 'Cow', 'Goat', 'Deer']},
        'correct_index': 2,
        'correct_answer': {'uz': "Echki (ko'zi)", 'ru': 'Коза (глаз)', 'en': 'Goat'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Goat_eye_horizontal_pupil_macro.jpg/800px-Goat_eye_horizontal_pupil_macro.jpg',
        'fun_fact': {   'uz': "Echkilarning gorizontal to'rtburchak qorachig'i o'tlayotganda gorizont bo'ylab 320-340 "
                              "darajali keng panoramani ko'rishga xizmat qiladi.",
                        'ru': 'Горизонтальные прямоугольные зрачки коз всегда остаются параллельными земле, '
                              'обеспечивая панорамный обзор на 340 градусов.',
                        'en': 'Goats feature horizontal rectangular pupils that rotate to stay parallel with the '
                              'horizon, scanning 340 degrees for predators while grazing.'},
        'aliases': ['echki', 'коза', 'глаз козы', 'goat']},
    {   'id': 'nature_macro_052_thorny_devil',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Xameleon', 'Iguana', 'Varan', 'Tikanli ajdarho (Molox)'],
                       'ru': ['Хамелеон', 'Игуана', 'Варан', 'Молох (Колючий дьявол)'],
                       'en': ['Chameleon', 'Iguana', 'Monitor Lizard', 'Thorny Devil']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Tikanli ajdarho (Molox)', 'ru': 'Молох (Колючий дьявол)', 'en': 'Thorny Devil'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Moloch_horridus_spines_macro.jpg/800px-Moloch_horridus_spines_macro.jpg',
        'fun_fact': {   'uz': 'Molox tikanlari orasidagi kapillyar ariqchalar orqali shudring yoki nam qumdagi suv '
                              "to'g'ridan-to'g'ri kaltakesakning og'ziga oqib boradi.",
                        'ru': 'Кожа молоха пронизана капиллярными микробороздками: любая влага с песка за счет физики '
                              'капилляров сама течет прямо в рот ящерицы.',
                        'en': "Hygroscopic skin grooves between the thorny devil's conical spines draw ambient "
                              'moisture and morning dew straight into its mouth via capillary action.'},
        'aliases': ['molox', 'tikanli ajdarho', 'молох', 'колючий дьявол', 'thorny devil']},
    {   'id': 'nature_macro_053_gila_monster',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Jila-maxluq (Gila)', 'Iguana', 'Xameleon', 'Timsoh'],
                       'ru': ['Аризонский ядозуб (Жилатье)', 'Игуана', 'Хамелеон', 'Крокодил'],
                       'en': ['Gila Monster', 'Iguana', 'Chameleon', 'Crocodile']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Jila-maxluq (Gila)', 'ru': 'Аризонский ядозуб (Жилатье)', 'en': 'Gila Monster'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Gila_monster_beaded_skin_macro.jpg/800px-Gila_monster_beaded_skin_macro.jpg',
        'fun_fact': {   'uz': 'Jila-maxluqning terisi marjon donalari kabi mayda suyakli osteodermalar bilan qoplangan '
                              "bo'lib, unga qattiq beaded (munchoqli) ko'rinish beradi.",
                        'ru': 'Кожа аризонского ядозуба покрыта бугристыми чешуйками-остеодермами, напоминающими '
                              'россыпь полированного черного и розового бисера.',
                        'en': 'The bead-like dorsal scales of the venomous Gila monster contain rounded osteoderm '
                              'ossicles forming a chain-mail defensive shield.'},
        'aliases': ['jila maxluq', 'yadozub', 'ядозуб', 'аризонский ядозуб', 'gila monster']},
    {   'id': 'nature_macro_054_armadillo_girdled_lizard',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Iguana', "Kichik belbog'dum kaltakesak", 'Gekkon', 'Agama'],
                       'ru': ['Игуана', 'Малый поясохвост', 'Геккон', 'Агама'],
                       'en': ['Iguana', 'Armadillo Girdled Lizard', 'Gecko', 'Agama']},
        'correct_index': 1,
        'correct_answer': {   'uz': "Kichik belbog'dum kaltakesak",
                              'ru': 'Малый поясохвост',
                              'en': 'Armadillo Girdled Lizard'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Ouroborus_cataphractus_scales_macro.jpg/800px-Ouroborus_cataphractus_scales_macro.jpg',
        'fun_fact': {   'uz': "Bu kaltakesak xavf paytida dumini og'ziga tishlab, tikanli doira (ouroboros) shaklini "
                              "oladi va yirtqichlarga o'zining mustahkam tikanli sovutini ko'rsatadi.",
                        'ru': 'При угрозе поясохвост сворачивается в жесткое кольцо, закусив собственный хвост, '
                              'выставляя наружу непробиваемые шипы.',
                        'en': 'When threatened, the armadillo girdled lizard curls into a ring by seizing its tail in '
                              'its jaws, presenting an armored ball of sharp spines.'},
        'aliases': ['poyasoxvost', 'belbogdum', 'поясохвост', 'armadillo girdled lizard']},
    {   'id': 'nature_macro_055_african_bush_elephant',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Begemot', 'Karkidon', 'Afrika fili', 'Tapir'],
                       'ru': ['Бегемот', 'Носорог', 'Африканский слон', 'Тапир'],
                       'en': ['Hippopotamus', 'Rhinoceros', 'African Bush Elephant', 'Tapir']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Afrika fili', 'ru': 'Африканский слон', 'en': 'African Bush Elephant'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Elephant_skin_cracks_macro.jpg/800px-Elephant_skin_cracks_macro.jpg',
        'fun_fact': {   'uz': 'Fil terisidagi chuqur yoriqlar namlik va loyni ushlab turadi, bu esa issiq savannada '
                              'tanani uzoq vaqt salqin saqlashga yordam beradi.',
                        'ru': 'Микротрещины на коже слона задерживают воду в 10 раз дольше гладкой кожи, охлаждая '
                              'гиганта через испарение.',
                        'en': "The intricate network of microscopic crevices in an African elephant's epidermis holds "
                              'water and mud 10 times longer than smooth skin.'},
        'aliases': ['fil', 'afrika fili', 'слон', 'африканский слон', 'african elephant']},
    {   'id': 'nature_macro_056_white_rhinoceros',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Fil', 'Begemot', 'Buyvol', 'Oq karkidon'],
                       'ru': ['Слон', 'Бегемот', 'Буйвол', 'Белый носорог'],
                       'en': ['Elephant', 'Hippopotamus', 'Buffalo', 'White Rhinoceros']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Oq karkidon', 'ru': 'Белый носорог', 'en': 'White Rhinoceros'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Rhinoceros_skin_folds_macro.jpg/800px-Rhinoceros_skin_folds_macro.jpg',
        'fun_fact': {   'uz': "Karkidon terisi 5 santimetrgacha qalinlikda bo'lib, uning shoxi esa suyakdan emas, "
                              'balki soch va tirnoq kabi sof keratindan tashkil topgan.',
                        'ru': 'Кожа носорога достигает 5 см в толщину, а его рог состоит исключительно из плотного '
                              'спрессованного кератина, без кости.',
                        'en': 'A rhinoceros has hide up to 5 cm thick, and its nasal horn is made entirely of '
                              'compressed keratin fibers rather than bone.'},
        'aliases': ['karkidon', 'oq karkidon', 'носорог', 'белый носорог', 'white rhinoceros', 'rhino']},
    {   'id': 'nature_macro_057_hippopotamus',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Begemot', 'Fil', 'Karkidon', 'Dengiz fili'],
                       'ru': ['Обыкновенный бегемот', 'Слон', 'Носорог', 'Морской слон'],
                       'en': ['Hippopotamus', 'Elephant', 'Rhinoceros', 'Elephant Seal']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Begemot', 'ru': 'Обыкновенный бегемот', 'en': 'Hippopotamus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Hippopotamus_skin_red_sweat_macro.jpg/800px-Hippopotamus_skin_red_sweat_macro.jpg',
        'fun_fact': {   'uz': "Begemot terisi qizg'ish suyuqlik ('qonli ter') ajratadi; bu suyuqlik quyosh nurlaridan "
                              'himoyalovchi krem va antibakterial vositadir.',
                        'ru': 'Кожа бегемота выделяет так называемый «кровавый пот» — вязкую красную жидкость, '
                              'служащую природным солнцезащитным кремом и антисептиком.',
                        'en': "Hippos secrete 'blood sweat', a reddish-orange fluid containing hipposudoric acid that "
                              'acts as an all-natural sunscreen and antibiotic.'},
        'aliases': ['begemot', 'гиппопотам', 'бегемот', 'hippopotamus', 'hippo']},
    {   'id': 'nature_macro_058_walrus',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Dengiz fili', 'Morj', 'Tyulen', 'Kalan'],
                       'ru': ['Морской слон', 'Морж', 'Тюлень', 'Калан'],
                       'en': ['Elephant Seal', 'Walrus', 'Seal', 'Sea Otter']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Morj', 'ru': 'Морж', 'en': 'Walrus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Walrus_skin_folds_macro.jpg/800px-Walrus_skin_folds_macro.jpg',
        'fun_fact': {   'uz': "Morjning terisi 10 santimetrgacha bo'lgan qalin yog' qatlami (blubber) bilan qoplangan "
                              "bo'lib, Arktika muzli suvlarida issiqlikni saqlaydi.",
                        'ru': 'Кожа моржа вместе с подкожным жиром имеет толщину до 15 см, надежно защищая его от '
                              'смертоносного арктического холода.',
                        'en': 'A walrus has wrinkled skin up to 10 cm thick supported by up to 15 cm of blubber, '
                              'isolating internal organs from freezing polar brine.'},
        'aliases': ['morj', 'морж', 'walrus']},
    {   'id': 'nature_macro_059_sea_otter',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Oddiy qunduz', 'Norka', 'Dengiz qunduzi (Kalan)', 'Tyulen'],
                       'ru': ['Речной бобр', 'Норка', 'Калан (Морская выдра)', 'Тюлень'],
                       'en': ['River Beaver', 'Mink', 'Sea Otter', 'Harbor Seal']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Dengiz qunduzi (Kalan)', 'ru': 'Калан (Морская выдра)', 'en': 'Sea Otter'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Sea_otter_fur_density_macro.jpg/800px-Sea_otter_fur_density_macro.jpg',
        'fun_fact': {   'uz': 'Kalan hayvonot olamidagi eng zich junga ega: santimetr kvadratiga 150 000 tagacha tuk '
                              "to'g'ri keladi va terisiga umuman suv yetib bormaydi.",
                        'ru': 'Шерсть калана — самая плотная в мире животных (до 150 000 волосков на см²); вода '
                              'никогда не касается его кожи.',
                        'en': 'Sea otters have the densest fur in the animal kingdom, with up to 150,000 hairs per '
                              'cm², trapping a layer of air to stay completely dry.'},
        'aliases': ['kalan', 'dengiz qunduzi', 'калан', 'морская выдра', 'sea otter']},
    {   'id': 'nature_macro_060_platypus',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Yexidna', 'Qunduz', 'Ondatra', "O'rdakburun"],
                       'ru': ['Ехидна', 'Бобр', 'Ондатра', 'Утконос'],
                       'en': ['Echidna', 'Beaver', 'Muskrat', 'Platypus']},
        'correct_index': 3,
        'correct_answer': {'uz': "O'rdakburun", 'ru': 'Утконос', 'en': 'Platypus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Platypus_waterproof_fur_macro.jpg/800px-Platypus_waterproof_fur_macro.jpg',
        'fun_fact': {   'uz': "O'rdakburun mo'ynasi suv ostida ultrabinafsha nurlari ostida yashil-ko'k rangda "
                              'biofluoressensiya taratadi.',
                        'ru': 'Мех утконоса не только абсолютно непромокаем, но и светится зелено-голубым светом под '
                              'ультрафиолетовыми лучами (биофлуоресценция).',
                        'en': 'Platypus fur is completely waterproof and biofluorescent, glowing a vivid cyan-green '
                              'under ultraviolet illumination.'},
        'aliases': ['ordakburun', "o'rdakburun", 'утконос', 'platypus']},
    {   'id': 'nature_macro_061_short_beaked_echidna',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Yexidna', 'Tipratikan', 'Jayra', 'Pangolin'],
                       'ru': ['Австралийская ехидна', 'Ёж', 'Дикобраз', 'Панголин'],
                       'en': ['Short-beaked Echidna', 'Hedgehog', 'Porcupine', 'Pangolin']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Yexidna', 'ru': 'Австралийская ехидна', 'en': 'Short-beaked Echidna'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Echidna_spines_detail_macro.jpg/800px-Echidna_spines_detail_macro.jpg',
        'fun_fact': {   'uz': "Yexidna tuxum qo'yuvchi sutemizuvchi bo'lib, uning mustahkam ninalari qattiqlashgan "
                              "jundan o'zgargan keratin naychalardir.",
                        'ru': 'Ехидна откладывает яйца, а ее иглы — это видоизмененные полые волосы из кератина длиной '
                              'до 6 сантиметров.',
                        'en': 'The short-beaked echidna is an egg-laying monotreme whose sturdy spines are modified '
                              'hollow hair shafts of keratin.'},
        'aliases': ['yexidna', 'ехидна', 'австралийская ехидна', 'echidna']},
    {   'id': 'nature_macro_062_honey_badger',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Bo'rsiq", "Asalxo'r (Medoyed)", 'Rosomaxa', 'Skuns'],
                       'ru': ['Барсук', 'Медоед (Ратель)', 'Росомаха', 'Скунс'],
                       'en': ['Badger', 'Honey Badger', 'Wolverine', 'Skunk']},
        'correct_index': 1,
        'correct_answer': {'uz': "Asalxo'r (Medoyed)", 'ru': 'Медоед (Ратель)', 'en': 'Honey Badger'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Honey_badger_thick_skin_macro.jpg/800px-Honey_badger_thick_skin_macro.jpg',
        'fun_fact': {   'uz': "Asalxo'rning terisi 6 millimetr qalinlikda va shunchalik erkin joylashganki, yirtqich "
                              'uni tishlaganda ham tana ichida bemalol burilib qarshi zarba bera oladi.',
                        'ru': 'Шкура медоеда толщиной 6 мм настолько свободна, что если хищник схватит его за '
                              'загривок, медоед может повернуться внутри шкуры и укусить в ответ.',
                        'en': 'Honey badgers possess 6-mm-thick rubbery skin so loose that if bitten from behind, they '
                              'can twist around completely inside their skin to bite back.'},
        'aliases': ['asalxor', "asalxo'r", 'medoyed', 'медоед', 'ратель', 'honey badger']},
    {   'id': 'nature_macro_063_wolverine',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Bo'rsiq", 'Suvsar', 'Rosomaxa', 'Samur'],
                       'ru': ['Барсук', 'Куница', 'Росомаха', 'Соболь'],
                       'en': ['Badger', 'Marten', 'Wolverine', 'Sable']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Rosomaxa', 'ru': 'Росомаха', 'en': 'Wolverine'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Wolverine_frost_resistant_fur_macro.jpg/800px-Wolverine_frost_resistant_fur_macro.jpg',
        'fun_fact': {   'uz': "Rosomaxa mo'ynasi suv va muz bug'larini o'ziga yopishtirmaydi; shu bois uning junida "
                              "qishda qirov yoki muz qatlami hosil bo'lmaydi.",
                        'ru': 'Шерсть росомахи содержит природный гидрофобный слой: дыхание и пар не кристаллизуются '
                              'на ней в виде инея.',
                        'en': 'Wolverine guard hairs are naturally hydrophobic and resist moisture crystallization, '
                              'preventing frost from forming around the face.'},
        'aliases': ['rosomaxa', 'росомаха', 'wolverine']},
    {   'id': 'nature_macro_064_arctic_fox',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Oddiy tulki', 'Korsak', 'Fenek', 'Qutb tulkisi (Pesets)'],
                       'ru': ['Рыжая лисица', 'Корсак', 'Фенек', 'Песец (Полярная лисица)'],
                       'en': ['Red Fox', 'Corsac', 'Fennec', 'Arctic Fox']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Qutb tulkisi (Pesets)', 'ru': 'Песец (Полярная лисица)', 'en': 'Arctic Fox'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Arctic_fox_winter_fur_macro.jpg/800px-Arctic_fox_winter_fur_macro.jpg',
        'fun_fact': {   'uz': "Qutb tulkisi qishda oq, yozda esa kulrang-qo'ng'ir rangga kiradi; uning qishki mo'ynasi "
                              '-50 °C sovuqda ham tanani 38 °C da saqlab turadi.',
                        'ru': 'Песец меняет окрас с серо-бурого летом на ослепительно белый зимой; его мех выдерживает '
                              'морозы до -70 °C без потери тепла.',
                        'en': 'The arctic fox shifts from brown in summer to pure white in winter, boasting the '
                              'warmest fur of any mammal relative to its weight.'},
        'aliases': ['pesets', 'qutb tulkisi', 'песец', 'полярная лисица', 'arctic fox']},
    {   'id': 'nature_macro_065_gray_wolf',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Bo'ri", 'Chiyobori', 'Koyot', 'Dingo'],
                       'ru': ['Серый волк', 'Шакал', 'Койот', 'Динго'],
                       'en': ['Gray Wolf', 'Jackal', 'Coyote', 'Dingo']},
        'correct_index': 0,
        'correct_answer': {'uz': "Bo'ri", 'ru': 'Серый волк', 'en': 'Gray Wolf'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Gray_wolf_dense_fur_macro.jpg/800px-Gray_wolf_dense_fur_macro.jpg',
        'fun_fact': {   'uz': "Bo'rining mo'ynasi ikki qavatli bo'lib, suv o'tkazmaydigan uzun qattiq tuklar ostida "
                              'issiqlikni mukammal saqlovchi mayin tivit qavati yotadi.',
                        'ru': 'Мех волка состоит из жесткого остевого волоса, отталкивающего воду, и густого '
                              'подшерстка, сохраняющего сухое тепло.',
                        'en': "A wolf's coat features a coarse outer layer of guard hairs that shed water and snow, "
                              'covering a dense insulating woolly undercoat.'},
        'aliases': ['bori', "bo'ri", 'волк', 'серый волк', 'gray wolf', 'wolf']},
    {   'id': 'nature_macro_066_dromedary_camel',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Lama', 'Tuya (Dromedar)', 'Alpaka', 'Ot'],
                       'ru': ['Лама', 'Одногорбый верблюд (Дромедар)', 'Альпака', 'Лошадь'],
                       'en': ['Llama', 'Dromedary Camel', 'Alpaca', 'Horse']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Tuya (Dromedar)', 'ru': 'Одногорбый верблюд (Дромедар)', 'en': 'Dromedary Camel'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Camel_wool_texture_macro.jpg/800px-Camel_wool_texture_macro.jpg',
        'fun_fact': {   'uz': "Tuya juni quyosh radiatsiyasini aks ettirib, tashqi harorat 70 °C bo'lganda ham hayvon "
                              'terisini 40 °C darajada saqlaydi.',
                        'ru': 'Шерсть верблюда настолько плотная, что препятствует проникновению пустынного зноя '
                              'внутрь, экономя влагу организма.',
                        'en': 'Camel fleece acts as an exceptional thermal insulator, reflecting solar radiation and '
                              'reducing cutaneous evaporation in 50 °C desert heat.'},
        'aliases': ['tuya', 'dromedar', 'верблюд', 'дромедар', 'camel', 'dromedary']},
    {   'id': 'nature_macro_067_alpaca',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Lama', 'Vikunya', 'Alpaka', "Qo'y"],
                       'ru': ['Лама', 'Викунья', 'Альпака', 'Овца'],
                       'en': ['Llama', 'Vicuña', 'Alpaca', 'Sheep']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Alpaka', 'ru': 'Альпака', 'en': 'Alpaca'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Alpaca_fleece_fiber_macro.jpg/800px-Alpaca_fleece_fiber_macro.jpg',
        'fun_fact': {   'uz': "Alpaka juni tolalari ichi g'ovak mikroskopik havo kameralariga ega bo'lib, qo'y junidan "
                              '3 baravar yengil va 5 baravar issiqroqdir.',
                        'ru': 'Волокна шерсти альпаки полые внутри, благодаря чему они в разы легче овечьей шерсти и '
                              'не содержат ланолина (гипоаллергенны).',
                        'en': 'Alpaca fleece contains microscopic air pockets that make it five times warmer and '
                              'significantly lighter than sheep wool, naturally lanolin-free.'},
        'aliases': ['alpaka', 'альпака', 'alpaca']},
    {   'id': 'nature_macro_068_okapi',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Zebra', 'Jirafa', 'Antilopa', 'Okapi'],
                       'ru': ['Зебра', 'Жираф', 'Антилопа', 'Окапи'],
                       'en': ['Zebra', 'Giraffe', 'Antelope', 'Okapi']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Okapi', 'ru': 'Окапи', 'en': 'Okapi'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Okapi_striped_rump_macro.jpg/800px-Okapi_striped_rump_macro.jpg',
        'fun_fact': {   'uz': "Okapining orqa oyoqlarida zebraga o'xshash chiziqlar bor, ammo u aslida jirafalar "
                              'oilasiga kiruvchi yagona yaqin qarindoshdir.',
                        'ru': 'Полосы на бедрах окапи напоминают зебру, однако анатомически это скрытное лесное '
                              'животное является ближайшим родственником жирафа.',
                        'en': 'Though an okapi sports zebra-like stripes on its hindquarters, it is the only living '
                              'relative of the giraffe.'},
        'aliases': ['okapi', 'окапи', 'okapi']},
    {   'id': 'nature_macro_069_bongo_antelope',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Bongo antilopasi', 'Kudu', 'Kiyik', 'Zebra'],
                       'ru': ['Антилопа Бонго', 'Куду', 'Олень', 'Зебра'],
                       'en': ['Bongo Antelope', 'Kudu', 'Deer', 'Zebra']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Bongo antilopasi', 'ru': 'Антилопа Бонго', 'en': 'Bongo Antelope'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Bongo_antelope_stripes_macro.jpg/800px-Bongo_antelope_stripes_macro.jpg',
        'fun_fact': {   'uz': "Bongo kiyigining qizg'ish mo'ynasidagi 10-15 ta oq vertikal chiziq quyosh nurlari quyuq "
                              "tropik o'rmonda sinishini mukammal takrorlaydi.",
                        'ru': 'Белые вертикальные полосы на каштановой шкуре бонго создают оптический камуфляж среди '
                              'густых зарослей тропического леса.',
                        'en': 'The bright chestnut coat of a bongo is marked with 10 to 15 vertical white stripes, '
                              'breaking up its silhouette in dense African rainforests.'},
        'aliases': ['bongo', 'bongo antilopasi', 'бонго', 'антилопа бонго', 'bongo antelope']},
    {   'id': 'nature_macro_070_malayan_tapir',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Chorva cho'chqasi", 'Malaya tapiri', 'Panda', 'Qoplon'],
                       'ru': ['Кабан', 'Чепрачный тапир', 'Панда', 'Леопард'],
                       'en': ['Wild Boar', 'Malayan Tapir', 'Panda', 'Leopard']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Malaya tapiri', 'ru': 'Чепрачный тапир', 'en': 'Malayan Tapir'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Malayan_tapir_coat_pattern.jpg/800px-Malayan_tapir_coat_pattern.jpg',
        'fun_fact': {   'uz': "Malaya tapirining orqa qismidagi oq 'chopon' (cheprak) oydin kechalarda uning ulkan "
                              "tanasini qoya toshlaridek ko'rsatib, yirtqichlardan yashiradi.",
                        'ru': 'Контрастное белое «седло» на теле чепрачного тапира визуально дробит силуэт животного '
                              'при лунном свете в джунглях.',
                        'en': 'The crisp black-and-white saddle pattern of the Malayan tapir breaks up its body '
                              'outline in moonlit jungle foliage (disruptive coloration).'},
        'aliases': ['tapir', 'malaya tapiri', 'тапир', 'чепрачный тапир', 'malayan tapir']},
    {   'id': 'nature_macro_071_warthog',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Yovvoyi cho'chqa", 'Pekari', "So'galli to'ng'iz (Borodavochnik)", 'Begemot'],
                       'ru': ['Дикий кабан', 'Пекари', 'Бородавочник', 'Бегемот'],
                       'en': ['Wild Boar', 'Peccary', 'Common Warthog', 'Hippo']},
        'correct_index': 2,
        'correct_answer': {'uz': "So'galli to'ng'iz (Borodavochnik)", 'ru': 'Бородавочник', 'en': 'Common Warthog'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Warthog_mane_bristles_macro.jpg/800px-Warthog_mane_bristles_macro.jpg',
        'fun_fact': {   'uz': "So'galli to'ng'iz orqasidagi uzun qattiq yoli xavf sezganda tikkayib, uning hajmini "
                              "yirtqichlarga kattaroq qilib ko'rsatadi.",
                        'ru': 'Грива бородавочника состоит из редкой жесткой щетины, встающей дыбом при возбуждении '
                              'для зрительного увеличения габаритов.',
                        'en': 'The coarse mane bristles of a warthog stand erect along its spine during confrontation, '
                              'making the animal look significantly larger.'},
        'aliases': ['borodavochnik', 'sogalli tongiz', 'бородавочник', 'warthog']},
    {   'id': 'nature_macro_072_colugo',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Uchar sincob', "Ko'rshapalak", 'Possum', 'Kolugo (Uchar lemur)'],
                       'ru': ['Белка-летяга', 'Летучая мышь', 'Опоссум', 'Малайский шерстокрыл (Кагуан)'],
                       'en': ['Flying Squirrel', 'Bat', 'Glider', 'Sunda Colugo']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Kolugo (Uchar lemur)', 'ru': 'Малайский шерстокрыл (Кагуан)', 'en': 'Sunda Colugo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Colugo_patagium_pattern_macro.jpg/800px-Colugo_patagium_pattern_macro.jpg',
        'fun_fact': {   'uz': "Kolugoning keng uchish pardasidagi lishayniksimon naqshlar daraxt po'stlog'i bilan shu "
                              "darajada qo'shilib ketadiki, uni 1 metrdan ham payqab bo'lmaydi.",
                        'ru': 'Шерсть шерстокрыла имитирует кору дерева, покрытую лишайником, обеспечивая '
                              'феноменальную маскировку в кронах.',
                        'en': "The colugo's extensive gliding membrane is cryptically mottled like lichen-encrusted "
                              'tree bark, rendering it nearly invisible against trunks.'},
        'aliases': ['kolugo', 'kaguan', 'шерстокрыл', 'кагуан', 'colugo']},
    {   'id': 'nature_macro_073_sugar_glider',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Shakarli uchar posum', 'Uchar sincob', "Ko'rshapalak", 'Kalamush'],
                       'ru': ['Сахарный летающий поссум', 'Белка-летяга', 'Летучая мышь', 'Мышь'],
                       'en': ['Sugar Glider', 'Flying Squirrel', 'Bat', 'Dormouse']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Shakarli uchar posum', 'ru': 'Сахарный летающий поссум', 'en': 'Sugar Glider'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Sugar_glider_fur_patagium_macro.jpg/800px-Sugar_glider_fur_patagium_macro.jpg',
        'fun_fact': {   'uz': "Shakarli posumning bilagidan to'pig'igacha cho'ziluvchi nozik momiq patagiy pardasi "
                              "unga daraxtdan daraxtga 50 metrgacha uchib o'tish imkonini beradi.",
                        'ru': 'Шелковистая летательная перепонка (патагий) позволяет сахарному поссуму планировать на '
                              'расстояние более 45 метров.',
                        'en': 'A sugar glider possesses a velvety gliding membrane (patagium) that extends from fifth '
                              'finger to first toe, allowing glides over 45 meters.'},
        'aliases': ['shakarli posum', 'possum', 'сахарный поссум', 'sugar glider']},
    {   'id': 'nature_macro_074_fruit_bat',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Oddiy ko'rshapalak", "Mevaxo'r ko'rshapalak (Qanot membranasi)", 'Qush', 'Kapalak'],
                       'ru': ['Обычная летучая мышь', 'Крылан (Летучая лисица)', 'Птица', 'Бабочка'],
                       'en': ['Microbat', 'Fruit Bat (Flying Fox)', 'Bird', 'Moth']},
        'correct_index': 1,
        'correct_answer': {   'uz': "Mevaxo'r ko'rshapalak (Qanot membranasi)",
                              'ru': 'Крылан (Летучая лисица)',
                              'en': 'Fruit Bat (Flying Fox)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Bat_wing_membrane_dactylopatagium_macro.jpg/800px-Bat_wing_membrane_dactylopatagium_macro.jpg',
        'fun_fact': {   'uz': "Ko'rshapalak qanoti suyaklari juda uzun barmoqlar orasiga tortilgan elastik teridan "
                              "iborat bo'lib, mikroskop ostida qon tomir kapillyarlari yaqqol ko'rinadi.",
                        'ru': 'Перепонка крыла крылана образована тончайшей эластичной кожей с развитой капиллярной '
                              'сетью, натянутой на пальцы кисти.',
                        'en': 'Bat wing membranes (dactylopatagium) consist of living double-layered skin rich in '
                              'blood vessels, elastic elastin fibers, and touch receptors.'},
        'aliases': ['korshapalak', 'qanotli tulki', 'крылан', 'летучая лисица', 'fruit bat', 'flying fox']},
    {   'id': 'nature_macro_075_luna_moth',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Morfo', 'Ipak qurti', 'Oy kapalagi (Luna)', 'Atlas'],
                       'ru': ['Морфо', 'Шелкопряд', 'Американская лунная моль', 'Атлас'],
                       'en': ['Morpho', 'Silkmoth', 'Luna Moth', 'Atlas Moth']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Oy kapalagi (Luna)', 'ru': 'Американская лунная моль', 'en': 'Luna Moth'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Actias_luna_wing_scales_macro.jpg/800px-Actias_luna_wing_scales_macro.jpg',
        'fun_fact': {   'uz': "Oy kapalagining shaffof oynasimon 'ko'zlari' bo'lgan ohak-yashil qanotlari yirtqich "
                              "ko'rshapalaklarning exolokatsiya to'lqinlarini chalg'itadi.",
                        'ru': 'Хвостатые выросты на крыльях лунной моли закручивают ультразвуковые волны летучих '
                              'мышей, отводя их атаку от жизненно важных органов.',
                        'en': 'The lime-green wings and twisted hindwing tails of the luna moth spin in flight to '
                              'scramble the echolocation sonar of hunting bats.'},
        'aliases': ['oy kapalagi', 'luna moth', 'лунная моль', 'luna moth']},
    {   'id': 'nature_macro_076_atlas_moth',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Oy kapalagi', 'Machaon', 'Monarx', 'Atlas kapalagi'],
                       'ru': ['Лунная моль', 'Махаон', 'Монарх', 'Павлиноглазка Атлас'],
                       'en': ['Luna Moth', 'Swallowtail', 'Monarch', 'Atlas Moth']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Atlas kapalagi', 'ru': 'Павлиноглазка Атлас', 'en': 'Atlas Moth'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Attacus_atlas_snake_head_wing_tip_macro.jpg/800px-Attacus_atlas_snake_head_wing_tip_macro.jpg',
        'fun_fact': {   'uz': 'Atlas kapalagining qanot uchlaridagi naqshlar zaharli kobra ilonining boshini shu qadar '
                              "aniq aks ettiradiki, qushlar unga yaqinlashishdan qo'rqadi.",
                        'ru': 'Кончики передних крыльев бабочки атлас филигранно имитируют голову ядовитой змеи, '
                              'отпугивая птиц-хищников.',
                        'en': "The apical tips of the atlas moth's forewings remarkably resemble the head of a cobra, "
                              'twitching to deter insectivorous birds.'},
        'aliases': ['atlas', 'atlas kapalagi', 'павлиноглазка атлас', 'atlas moth']},
    {   'id': 'nature_macro_077_jewel_beetle',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Nefrit qo'ng'izi (Zlatka)", "May qo'ng'izi", 'Bronzovka', 'Xonqizi'],
                       'ru': ['Жук-златка', 'Майский жук', 'Бронзовка', 'Божья коровка'],
                       'en': ['Jewel Beetle', 'Cockchafer', 'Rose Chafer', 'Ladybug']},
        'correct_index': 0,
        'correct_answer': {'uz': "Nefrit qo'ng'izi (Zlatka)", 'ru': 'Жук-златка', 'en': 'Jewel Beetle'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Jewel_beetle_elytra_structural_color_macro.jpg/800px-Jewel_beetle_elytra_structural_color_macro.jpg',
        'fun_fact': {   'uz': "Bu qo'ng'iz qattiqqanotining metall tovlanuvchi yashil-oltin jilvasi ko'p qatlamli "
                              "xitin nanostrukturalarining yorug'lik interferensiyasi tufaylidir.",
                        'ru': 'Металлический изумрудный блеск надкрылий жука-златки создается интерференцией света в '
                              'многослойной кутикуле.',
                        'en': "The metallic iridescent color of a jewel beetle's elytra is generated by multi-layered "
                              'chitin reflectors acting as natural Bragg mirrors.'},
        'aliases': ['zlatka', 'nefrit qongizi', 'златка', 'жук-златка', 'jewel beetle']},
    {   'id': 'nature_macro_078_peacock_spider',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Qora beva', "Tovus o'rgimchagi", 'Tarantul', 'Krestovik'],
                       'ru': ['Черная вдова', 'Павлиний паук', 'Тарантул', 'Крестовик'],
                       'en': ['Black Widow', 'Peacock Spider', 'Tarantula', 'Orb-weaver']},
        'correct_index': 1,
        'correct_answer': {'uz': "Tovus o'rgimchagi", 'ru': 'Павлиний паук', 'en': 'Peacock Spider'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Maratus_volans_abdomen_macro.jpg/800px-Maratus_volans_abdomen_macro.jpg',
        'fun_fact': {   'uz': "Uzunligi bor-yo'g'i 4-5 mm bo'lgan bu sakrovchi o'rgimchak urg'ochisini jalb qilish "
                              "uchun qornidagi kamalak rangli yelpig'ichini tovusdek yoyadi.",
                        'ru': 'Самец павлиньего паука раскрывает крошечный радужный щиток на брюшке и исполняет '
                              'сложный брачный танец.',
                        'en': 'Male peacock spiders display miniature abdominal flaps adorned with structural '
                              'micro-scales and nano-gratings during courtship dances.'},
        'aliases': ['tovus orgimchagi', 'павлиний паук', 'peacock spider']},
    {   'id': 'nature_macro_079_brazilian_wandering_spider',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Tarantul', "Giyoh o'rgimchak", "Braziliya sayyoh o'rgimchagi", 'Qora beva'],
                       'ru': ['Тарантул', 'Крестовик', 'Бразильский странствующий паук', 'Черная вдова'],
                       'en': ['Tarantula', 'Huntsman', 'Brazilian Wandering Spider', 'Black Widow']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Braziliya sayyoh o'rgimchagi",
                              'ru': 'Бразильский странствующий паук',
                              'en': 'Brazilian Wandering Spider'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Phoneutria_chelicerae_red_hairs_macro.jpg/800px-Phoneutria_chelicerae_red_hairs_macro.jpg',
        'fun_fact': {   'uz': "Bu xavfli o'rgimchakning qizil tuklar bilan qoplangan yirik xelitseralari (jag'lari) "
                              'kuchli neyrotoksin ajratib chiqaradi.',
                        'ru': 'Хелицеры бразильского странствующего паука покрыты густыми красноватыми волосками и '
                              'снабжены смертоносными ядовитыми коготками.',
                        'en': 'The chelicerae of the venomous Brazilian wandering spider (Phoneutria) are cloaked in '
                              'vivid red hairs, signalling potent neurotoxins.'},
        'aliases': [   'braziliya orgimchagi',
                       'sayyoh orgimchak',
                       'странствующий паук',
                       'бразильский странствующий паук',
                       'brazilian wandering spider']},
    {   'id': 'nature_macro_080_emperor_scorpion',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Qora chayon', "O'rgimchak", 'Qisqichbaqa', 'Imperator chayoni'],
                       'ru': ['Песчаный скорпион', 'Паук', 'Рак', 'Императорский скорпион'],
                       'en': ['Deathstalker', 'Spider', 'Crayfish', 'Emperor Scorpion']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Imperator chayoni', 'ru': 'Императорский скорпион', 'en': 'Emperor Scorpion'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Pandinus_imperator_cuticle_granules_macro.jpg/800px-Pandinus_imperator_cuticle_granules_macro.jpg',
        'fun_fact': {   'uz': "Imperator chayonining qattiq granullangan xitin qobig'i ultrabinafsha nurlari ostida "
                              "yorqin feruza (ko'k-yashil) rangda porlaydi.",
                        'ru': 'Экзоскелет императорского скорпиона содержит бета-карболин, заставляющий его ярко '
                              'светиться бирюзовым цветом в ультрафиолете.',
                        'en': 'The heavily granulated cuticle of an emperor scorpion contains beta-carbolines that '
                              'fluoresce brilliant cyan under UV light.'},
        'aliases': ['imperator chayoni', 'chayon', 'императорский скорпион', 'скорпион', 'emperor scorpion']},
    {   'id': 'nature_macro_081_mexican_redknee',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Meksika qiziltizimli tarantuli', 'Qora beva', 'Qora qurt', 'Golyat'],
                       'ru': ['Мексиканский красноколенный птицеед', 'Черная вдова', 'Каракурт', 'Голиаф'],
                       'en': ['Mexican Redknee Tarantula', 'Black Widow', 'Brown Recluse', 'Goliath Birdeater']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Meksika qiziltizimli tarantuli',
                              'ru': 'Мексиканский красноколенный птицеед',
                              'en': 'Mexican Redknee Tarantula'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Brachypelma_hamorii_urticating_hairs_macro.jpg/800px-Brachypelma_hamorii_urticating_hairs_macro.jpg',
        'fun_fact': {   'uz': "Tarantul qornidagi mayda tikanli tuklar (urticating hairs) xavf tug'ilganda oyoqlar "
                              "bilan yirtqichning ko'ziga qarab sochib yuboriladi.",
                        'ru': 'При опасности птицеед счесывает задними лапками с брюшка стрекательные волоски с '
                              'микрозубчиками, вызывающими жжение.',
                        'en': 'Tarantulas defend themselves by kicking microscopic barbed urticating setae from their '
                              'abdomen into the eyes and mucosa of attackers.'},
        'aliases': [   'qiziltizim tarantul',
                       'tarantul',
                       'красноколенный птицеед',
                       'птицеед',
                       'mexican redknee tarantula']},
    {   'id': 'nature_macro_082_red_lionfish',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Fugu', 'Qanotdor baliq (Krylatka)', 'Skumbriya', 'Dengiz oti'],
                       'ru': ['Фугу', 'Крылатка-зебра (Рыба-лев)', 'Скумбрия', 'Морской конек'],
                       'en': ['Pufferfish', 'Red Lionfish', 'Mackerel', 'Seahorse']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qanotdor baliq (Krylatka)', 'ru': 'Крылатка-зебра (Рыба-лев)', 'en': 'Red Lionfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Pterois_volitans_fin_spines_macro.jpg/800px-Pterois_volitans_fin_spines_macro.jpg',
        'fun_fact': {   'uz': "Krylatkaning yo'l-yo'l jilvali suzgich ninalari ichida kuchli oqsil zahari bo'lib, "
                              "uning sanchilishi odamda chidab bo'lmas og'riq uyg'otadi.",
                        'ru': 'Каждый из лучей спинного плавника крылатки представляет собой полую иглу, соединенную с '
                              'железой высокотоксичного яда.',
                        'en': 'Each elongated dorsal spine of a red lionfish functions like a hypodermic needle '
                              'delivering venomous acetylcholine toxins.'},
        'aliases': ['qanotdor baliq', 'krylatka', 'рыба-лев', 'крылатка', 'lionfish', 'red lionfish']},
    {   'id': 'nature_macro_083_pufferfish',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Kambala', 'Skumbriya', 'Sharbaliq (Fugu)', 'Barracuda'],
                       'ru': ['Камбала', 'Скумбрия', 'Рыба-фугу (Иглобрюх)', 'Барракуда'],
                       'en': ['Flounder', 'Mackerel', 'Pufferfish', 'Barracuda']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Sharbaliq (Fugu)', 'ru': 'Рыба-фугу (Иглобрюх)', 'en': 'Pufferfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Pufferfish_erected_spines_macro.jpg/800px-Pufferfish_erected_spines_macro.jpg',
        'fun_fact': {   'uz': 'Sharbaliq xavf paytida suv yoki havoni ichiga yutib koptokdek shishadi va uning '
                              "terisidagi o'tkir tikanlar tikka turadi.",
                        'ru': 'При испуге иглобрюх накачивает желудок водой, превращаясь в шар с торчащими во все '
                              'стороны острыми кожными шипами.',
                        'en': 'When alarmed, pufferfish inflate their elastic stomachs with water, erecting modified '
                              'dermal scales that become sharp spikes.'},
        'aliases': ['sharbaliq', 'fugu', 'рыба-фугу', 'иглобрюх', 'pufferfish']},
    {   'id': 'nature_macro_084_ocean_sunfish',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Kit akula', 'Manta', 'Tyunets', 'Oybaliq (Mola mola)'],
                       'ru': ['Китовая акула', 'Манта', 'Тунец', 'Обыкновенная луна-рыба'],
                       'en': ['Whale Shark', 'Manta', 'Tuna', 'Ocean Sunfish (Mola)']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Oybaliq (Mola mola)', 'ru': 'Обыкновенная луна-рыба', 'en': 'Ocean Sunfish (Mola)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Mola_mola_skin_texture_macro.jpg/800px-Mola_mola_skin_texture_macro.jpg',
        'fun_fact': {   'uz': "Oybaliqning 7 santimetrgacha qalinlikdagi qo'pol terisi tangachasiz bo'lib, dag'alligi "
                              "bo'yicha yirik qumqog'ozni eslatadi.",
                        'ru': 'Кожа луны-рыбы толщиной до 7 см не имеет чешуи, покрыта слоем хрящеподобного коллагена '
                              'и грубая, как наждак.',
                        'en': 'Ocean sunfish have scaleless skin up to 7 cm thick supported by a dense cartilaginous '
                              'collagen layer with the texture of coarse sandpaper.'},
        'aliases': ['oybaliq', 'mola mola', 'луна-рыба', 'мола-мола', 'ocean sunfish', 'mola']},
    {   'id': 'nature_macro_085_flamingo_tongue_snail',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Flamingo tili shilliqurti', 'Konus shilliqurti', 'Nautilus', 'Kauri'],
                       'ru': ['Улитка «Язык фламинго»', 'Улитка-конус', 'Наутилус', 'Каури'],
                       'en': ['Flamingo Tongue Snail', 'Cone Snail', 'Nautilus', 'Cowrie']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Flamingo tili shilliqurti',
                              'ru': 'Улитка «Язык фламинго»',
                              'en': 'Flamingo Tongue Snail'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Cyphoma_gibbosum_mantle_macro.jpg/800px-Flamingo_tongue_snail_macro.jpg',
        'fun_fact': {   'uz': "Bu shilliqurtning qobig'i aslida oppoq rangda; uning yorqin sariq-qora dog'lari "
                              "chig'anoqni ustidan o'rab oluvchi tirik mantiyasidir.",
                        'ru': 'Раковина этой улитки чисто белая; знаменитые оранжевые леопардовые пятна принадлежат '
                              'живой мантии, обволакивающей раковину.',
                        'en': "The flamingo tongue snail's shell is solid white; its famous leopard-like pattern "
                              'resides entirely in its live, retractable mantle tissue.'},
        'aliases': ['flamingo tili', 'язык фламинго', 'улитка язык фламинго', 'flamingo tongue snail']},
    {   'id': 'nature_macro_086_giant_clam',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Ustritsa', 'Ulkan tridakna', 'Midiya', 'Dengiz taroqchasi'],
                       'ru': ['Устрица', 'Гигантская тридакна', 'Мидия', 'Морской гребешок'],
                       'en': ['Oyster', 'Giant Clam', 'Mussel', 'Scallop']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Ulkan tridakna', 'ru': 'Гигантская тридакна', 'en': 'Giant Clam'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Tridacna_gigas_iridophore_mantle_macro.jpg/800px-Tridacna_gigas_iridophore_mantle_macro.jpg',
        'fun_fact': {   'uz': "Tridakna mantiyasining zumrad va feruza tovlanishi uning to'qimalarida simbioz "
                              "yashovchi mikroskopik zooksantella suvo'tlaridan kelib chiqadi.",
                        'ru': 'Фантастические узоры мантии тридакны создаются одноклеточными водорослями '
                              'зооксантеллами, производящими для моллюска сахара.',
                        'en': "A giant clam's mantle hosts millions of symbiotic zooxanthellae algae beneath "
                              'iridescent iridocyte cells that scatter sunlight for photosynthesis.'},
        'aliases': ['tridakna', 'тридакна', 'гигантская тридакна', 'giant clam']},
    {   'id': 'nature_macro_087_brain_coral',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Dengiz yelpig'ichi", 'Shoxmarjon', 'Miyasimon marjon (Platigyra)', 'Gugurtmarjon'],
                       'ru': ['Морской веер', 'Акропора', 'Мозговой коралл', 'Актиния'],
                       'en': ['Sea Fan', 'Staghorn Coral', 'Brain Coral', 'Anemone']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Miyasimon marjon (Platigyra)', 'ru': 'Мозговой коралл', 'en': 'Brain Coral'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Brain_coral_meandroid_skeleton_macro.jpg/800px-Brain_coral_meandroid_skeleton_macro.jpg',
        'fun_fact': {   'uz': 'Miyasimon marjon yuzasidagi egri-bugri labirintlar yuzlab poliplarning kalsiy '
                              'karbonatdan qurilgan umumiy skelet tizimidir.',
                        'ru': 'Извилистые борозды мозгового коралла формируются колонией генетически идентичных '
                              'полипов, выделяющих карбонат кальция.',
                        'en': 'The meandroid grooves of brain coral are built by colonies of cloned polyps secreting '
                              'continuous walls of calcium carbonate skeleton.'},
        'aliases': ['miyasimon marjon', 'marjon', 'мозговой коралл', 'коралл', 'brain coral']},
    {   'id': 'nature_macro_088_ball_python',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Kobra', "Bo'g'ma ilon", 'Chiqildoq ilon', 'Qirollik pitoni'],
                       'ru': ['Кобра', 'Удав', 'Гремучая змея', 'Королевский питон'],
                       'en': ['Cobra', 'Boa Constrictor', 'Rattlesnake', 'Ball Python']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Qirollik pitoni', 'ru': 'Королевский питон', 'en': 'Ball Python'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Ball_python_scale_pattern_macro.jpg/800px-Ball_python_scale_pattern_macro.jpg',
        'fun_fact': {   'uz': "Qirollik pitonining silliq qoramtir tangachalari unga xavf tug'ilganda boshini "
                              'ichkariga yashirib zich koptok shakliga kirishga imkon beradi.',
                        'ru': 'Гладкие чешуйки королевского питона помогают ему сворачиваться в тугой шар при '
                              'опасности, пряча уязвимую голову внутри колец.',
                        'en': 'Ball pythons have smooth, tightly fitted dorsal scales that assist them in curling into '
                              'a defensive sphere with the head tucked safely inside.'},
        'aliases': ['qirollik pitoni', 'piton', 'королевский питон', 'питон', 'ball python']},
    {   'id': 'nature_macro_089_gaboon_viper',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Gabon qora iloni (Karkidon ilon)', 'Gyurza', 'Kobra', 'Efa'],
                       'ru': ['Габонская гадюка', 'Гюрза', 'Кобра', 'Эфа'],
                       'en': ['Gaboon Viper', 'Levant Viper', 'Cobra', 'Saw-scaled Viper']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Gabon qora iloni (Karkidon ilon)', 'ru': 'Габонская гадюка', 'en': 'Gaboon Viper'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Bitis_gabonica_leaf_litter_camo_macro.jpg/800px-Bitis_gabonica_leaf_litter_camo_macro.jpg',
        'fun_fact': {   'uz': 'Gabon ilonining geometrik uchburchak va rombsimon tangachalari quruq xazon yaproqlari '
                              "to'shamasini shunchalik mukammal nusxalaydiki, uni bosib olmaguncha payqab bo'lmaydi.",
                        'ru': 'Геометрический узор на чешуе габонской гадюки — непревзойденный образец природного '
                              'камуфляжа под опавшую листву джунглей.',
                        'en': 'The complex hourglass and velvet geometric scales of the Gaboon viper provide '
                              'world-class disruptive camouflage on rainforest floors.'},
        'aliases': ['gabon iloni', 'габонская гадюка', 'gaboon viper']},
    {   'id': 'nature_macro_090_king_cobra',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Mamba', 'Qirol kobra', 'Piton', 'Varan'],
                       'ru': ['Черная мамба', 'Королевская кобра', 'Питон', 'Варан'],
                       'en': ['Black Mamba', 'King Cobra', 'Python', 'Monitor Lizard']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qirol kobra', 'ru': 'Королевская кобра', 'en': 'King Cobra'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/King_cobra_chevron_scales_macro.jpg/800px-King_cobra_chevron_scales_macro.jpg',
        'fun_fact': {   'uz': "Qirol kobraning bo'yin tangachalari kengayganda qo'rqinchli kapyushon hosil qiladi; u "
                              'asosan boshqa ilonlar bilan oziqlanadi.',
                        'ru': 'Гладкие шевронные чешуи королевской кобры натягиваются на подвижные шейные ребра, '
                              'образуя устрашающий боевой капюшон.',
                        'en': 'Smooth chevron-aligned dorsal scales on a king cobra stretch over elongated mobile '
                              'cervical ribs to form its towering intimidation hood.'},
        'aliases': ['qirol kobra', 'kobra', 'королевская кобра', 'кобра', 'king cobra']},
    {   'id': 'nature_macro_091_diamondback_rattlesnake',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Misbosh ilon', 'Kobra', 'Olmossimon chiqildoq ilon', 'Piton'],
                       'ru': ['Медноголовый щитомордник', 'Кобра', 'Техасский гремучник', 'Питон'],
                       'en': ['Copperhead', 'Cobra', 'Western Diamondback Rattlesnake', 'Python']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Olmossimon chiqildoq ilon',
                              'ru': 'Техасский гремучник',
                              'en': 'Western Diamondback Rattlesnake'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Crotalus_atrox_keeled_diamond_scales_macro.jpg/800px-Crotalus_atrox_keeled_diamond_scales_macro.jpg',
        'fun_fact': {   'uz': "Chiqildoq ilon tangachalari o'rtasida qovurg'acha (kiliya) bo'lib, uning dumi uchidagi "
                              "po'st tashlashdan qolgan quruq bo'g'inlar soniyasiga 50 marta titrab jaranglaydi.",
                        'ru': 'Чешуя гремучника килеватая (с продольным ребрышком), а его погремок на хвосте состоит '
                              'из полых кератиновых сегментов.',
                        'en': 'Keeled diamond-shaped scales scatter glare, while interlocking hollow keratin segments '
                              'on the tail vibrate at 50 Hz to sound a warning rattle.'},
        'aliases': ['chiqildoq ilon', 'гремучник', 'гремучая змея', 'diamondback', 'rattlesnake']},
    {   'id': 'nature_macro_092_emerald_tree_boa',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Yashil mamba', 'Piton', 'Qora ilon', "Zumrad daraxt bo'g'ma iloni"],
                       'ru': ['Зеленая мамба', 'Питон', 'Гадюка', 'Собакоголовый удав'],
                       'en': ['Green Mamba', 'Python', 'Viper', 'Emerald Tree Boa']},
        'correct_index': 3,
        'correct_answer': {'uz': "Zumrad daraxt bo'g'ma iloni", 'ru': 'Собакоголовый удав', 'en': 'Emerald Tree Boa'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Corallus_caninus_scales_macro.jpg/800px-Corallus_caninus_scales_macro.jpg',
        'fun_fact': {   'uz': "Zumrad bo'g'ma iloni terisi to'q yashil tangachalar bo'ylab chaqmoqsimon oq chiziqlar "
                              "bilan bezatilgan bo'lib, lianalar orasida mukammal niqoblanadi.",
                        'ru': 'Ярко-зеленая чешуя собакоголового удава пересечена зигзагообразными белыми полосками, '
                              'имитирующими блики на листьях.',
                        'en': 'Vivid emerald-green dorsal scales intersected by lightning-white stripes provide '
                              'absolute camouflage amid sun-drenched Amazonian vine thickets.'},
        'aliases': ['zumrad bogma ilon', 'собакоголовый удав', 'emerald tree boa']},
    {   'id': 'nature_macro_093_green_tree_python',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Yashil daraxt pitoni', "Zumrad bo'g'ma ilon", 'Kobra', 'Alligator'],
                       'ru': ['Зеленый древесный питон', 'Собакоголовый удав', 'Кобра', 'Аллигатор'],
                       'en': ['Green Tree Python', 'Emerald Tree Boa', 'Cobra', 'Alligator']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Yashil daraxt pitoni', 'ru': 'Зеленый древесный питон', 'en': 'Green Tree Python'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Morelia_viridis_scales_macro.jpg/800px-Morelia_viridis_scales_macro.jpg',
        'fun_fact': {   'uz': "Yashil piton bolalari tug'ilganda qizil yoki sariq rangda bo'ladi va faqat voyaga "
                              'yetgach tangachalari yashil rangga aylanadi.',
                        'ru': 'Молодые особи зеленого питона рождаются канареечно-желтыми или кирпично-красными, меняя '
                              'чешую на изумрудную только к взрослому возрасту.',
                        'en': 'Green tree python hatchlings are born bright canary yellow or brick red, undergoing '
                              'ontogenetic color shifts into green scales upon maturity.'},
        'aliases': ['yashil daraxt pitoni', 'зеленый питон', 'древесный питон', 'green tree python']},
    {   'id': 'nature_macro_094_housefly',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Chivin', "Uy pashshasi (fasetali ko'zlari)", 'Asalari', 'Chigirtka'],
                       'ru': ['Комар', 'Комнатная муха (глаз)', 'Пчела', 'Саранча'],
                       'en': ['Mosquito', 'Housefly', 'Bee', 'Locust']},
        'correct_index': 1,
        'correct_answer': {'uz': "Uy pashshasi (fasetali ko'zlari)", 'ru': 'Комнатная муха (глаз)', 'en': 'Housefly'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Musca_domestica_compound_eye_macro.jpg/800px-Musca_domestica_compound_eye_macro.jpg',
        'fun_fact': {   'uz': "Uy pashshasining qizil fasetali ko'zlari soniyasiga 250 tagacha tasvir kadrini qayta "
                              "ishlaydi (odam esa atigi 60 ta kadrni ko'radi).",
                        'ru': 'Глаза комнатной мухи обрабатывают до 250 кадров в секунду, поэтому движение '
                              'человеческой руки кажется мухе замедленным фильмом.',
                        'en': "A housefly's compound eye has a flicker fusion rate of 250 Hz (compared to ~60 Hz in "
                              'humans), perceiving human swatting attempts in slow motion.'},
        'aliases': ['pashsha', 'uy pashshasi', 'муха', 'комнатная муха', 'housefly']},
    {   'id': 'nature_macro_095_seven_spot_ladybug',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Kolorado qo'ng'izi", 'Bronzovka', 'Xonqizi (Ladybug)', 'Klobuk'],
                       'ru': ['Колорадский жук', 'Бронзовка', 'Семиточечная божья коровка', 'Клоп'],
                       'en': ['Colorado Beetle', 'Rose Chafer', 'Seven-spotted Ladybug', 'Stink Bug']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Xonqizi (Ladybug)',
                              'ru': 'Семиточечная божья коровка',
                              'en': 'Seven-spotted Ladybug'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Coccinella_septempunctata_elytra_macro.jpg/800px-Coccinella_septempunctata_elytra_macro.jpg',
        'fun_fact': {   'uz': "Xonqizining qizil qattiqqanotlaridagi qora dog'lar ogohlantiruvchi belgi bo'lib, u xavf "
                              'paytida tizzalaridan achchiq zaharli sariq suyuqlik chiqaradi.',
                        'ru': 'Красные надкрылья божьей коровки предупреждают хищников о горькой гемолимфе, выделяемой '
                              'суставами лапок при опасности.',
                        'en': 'The glossy scarlet elytra with black dots signal chemical deterrence; disturbed '
                              'ladybugs reflex-bleed toxic foul-smelling yellow alkaloids.'},
        'aliases': ['xonqizi', 'божья коровка', 'ladybug', 'ladybird']},
    {   'id': 'nature_macro_096_giant_anteater',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Pangolin', 'Yexidna', 'Ayiq', "Ulkan chumolixo'r"],
                       'ru': ['Панголин', 'Ехидна', 'Медведь', 'Гигантский муравьед'],
                       'en': ['Pangolin', 'Echidna', 'Bear', 'Giant Anteater']},
        'correct_index': 3,
        'correct_answer': {'uz': "Ulkan chumolixo'r", 'ru': 'Гигантский муравьед', 'en': 'Giant Anteater'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Giant_anteater_coat_macro.jpg/800px-Giant_anteater_coat_macro.jpg',
        'fun_fact': {   'uz': "Chumolixo'rning qo'pol va qattiq juni chumoli va termitlar chaqishidan to'liq himoya "
                              "qiladi, uning dumi esa kechasi ko'rpa vazifasini o'taydi.",
                        'ru': 'Жесткая, похожая на солому шерсть гигантского муравьеда непробиваема для жвал миллионов '
                              'разъяренных термитов.',
                        'en': "A giant anteater's wiry, straw-like coat repels stinging termite bites, while its "
                              'enormous bushy tail acts as an insulating blanket at night.'},
        'aliases': ['chumolixor', "ulkan chumolixo'r", 'гигантский муравьед', 'муравьед', 'giant anteater']},
    {   'id': 'nature_macro_097_golden_pheasant',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["Oltin qirg'ovul", 'Tovus', 'Jannat qushi', 'Kaptar'],
                       'ru': ['Золотой фазан', 'Павлин', 'Райская птица', 'Голубь'],
                       'en': ['Golden Pheasant', 'Peacock', 'Bird-of-paradise', 'Pigeon']},
        'correct_index': 0,
        'correct_answer': {'uz': "Oltin qirg'ovul", 'ru': 'Золотой фазан', 'en': 'Golden Pheasant'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Chrysolophus_pictus_ruff_cape_macro.jpg/800px-Chrysolophus_pictus_ruff_cape_macro.jpg',
        'fun_fact': {   'uz': "Oltin qirg'ovul bo'ynidagi to'q sariq va qora yo'l-yo'l yoqa patlari tovusnikidek "
                              "yelpig'ich shaklida yoyilib namoyish etiladi.",
                        'ru': 'Яркий воротник самца золотого фазана состоит из тончайших оранжево-черных перьев, '
                              'раскрывающихся веером при токовании.',
                        'en': 'The cape feathers of a male golden pheasant form a graphic orange and black ruff that '
                              'fans out around the face in courtship displays.'},
        'aliases': ['oltin qirnovul', 'золотой фазан', 'фазан', 'golden pheasant']},
    {   'id': 'nature_macro_098_toco_toucan_eye',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ["To'ti", "Tukan (ko'z atrofi)", 'Burgut', 'Straus'],
                       'ru': ['Попугай', 'Тукан токо (окологлазничная область)', 'Орел', 'Страус'],
                       'en': ['Parrot', 'Toco Toucan (Periorbital skin)', 'Eagle', 'Ostrich']},
        'correct_index': 1,
        'correct_answer': {   'uz': "Tukan (ko'z atrofi)",
                              'ru': 'Тукан токо (окологлазничная область)',
                              'en': 'Toco Toucan (Periorbital skin)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Ramphastos_toco_periorbital_skin_macro.jpg/800px-Ramphastos_toco_periorbital_skin_macro.jpg',
        'fun_fact': {   'uz': "Tukanning ko'z atrofidagi yorqin to'q sariq va ko'k rangli teri patsiz bo'lib, uning "
                              'yuz ifodasi va vizual aloqasini kuchaytiradi.',
                        'ru': 'Яркая неоново-оранжевая кожа вокруг глаз тукана лишена перьев и контрастирует с '
                              'глубоким сапфировым кольцом радужки.',
                        'en': 'The featherless periorbital facial skin of the toco toucan is saturated in brilliant '
                              'orange and blue carotenoid pigmentation.'},
        'aliases': ['tukan', 'тукан', 'toco toucan']},
    {   'id': 'nature_macro_099_reef_manta_belly',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Akula', 'Skat', "Manta (qorin dog'lari)", 'Kit'],
                       'ru': ['Акула', 'Скат', 'Рифовая манта (брюшной узор)', 'Кит'],
                       'en': ['Shark', 'Stingray', 'Reef Manta Ray (Ventral pattern)', 'Whale']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Manta (qorin dog'lari)",
                              'ru': 'Рифовая манта (брюшной узор)',
                              'en': 'Reef Manta Ray (Ventral pattern)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Manta_alfredi_ventral_spotting_macro.jpg/800px-Manta_alfredi_ventral_spotting_macro.jpg',
        'fun_fact': {   'uz': "Har bir mantaning qornidagi qora dog'lar kombinatsiyasi mutlaqo noyob bo'lib, dengiz "
                              'biologlari ularni xuddi pasport kabi taniy oladilar.',
                        'ru': 'Пятна на белом брюхе каждой манты строго индивидуальны на протяжении всей жизни, служа '
                              'естественным ID-паспортом особи.',
                        'en': 'Every manta ray carries a permanent, unique pattern of dark spots on its white ventral '
                              'belly that biologists use for photo-ID tracking.'},
        'aliases': ['manta', 'rif mantasi', 'рифовая манта', 'манта', 'reef manta']},
    {   'id': 'nature_macro_100_leafy_seadragon',
        'sub_mode': 'macro_texture',
        'question': {   'uz': 'Ushbu makro suratda qaysi jonzotning terisi / patlari / naqshi tasvirlangan?',
                        'ru': 'Кожа, оперение или текстура какого животного показаны на этом макроснимке?',
                        'en': "Which animal's skin, feathers, or pattern is shown in this macro close-up?"},
        'options': {   'uz': ['Dengiz oti', 'Ignabaliq', 'Dengiz anemonasi', 'Yaproqsimon dengiz ajdahosi'],
                       'ru': ['Морской конек', 'Рыба-игла', 'Актиния', 'Лиственный морской дракон (Тряпичник)'],
                       'en': ['Seahorse', 'Pipefish', 'Sea Anemone', 'Leafy Seadragon']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Yaproqsimon dengiz ajdahosi',
                              'ru': 'Лиственный морской дракон (Тряпичник)',
                              'en': 'Leafy Seadragon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Leafy_seadragon_dermal_appendages_macro.jpg/800px-Leafy_seadragon_dermal_appendages_macro.jpg',
        'fun_fact': {   'uz': "Bu baliq tanasidagi suvo'tiga o'xshash barcha bargsimon o'simtalar suzishga emas, balki "
                              "marjon va suvo'tlari orasida g'oyib bo'lishga xizmat qiladi.",
                        'ru': 'Листовидные наросты на теле морского тряпичника служат исключительно для маскировки под '
                              'плавающие бурые водоросли.',
                        'en': 'The leafy appendages of Phycodurus eques serve purely for camouflage among drifting '
                              'kelp beds, propelled only by translucent dorsal fins.'},
        'aliases': ['dengiz ajdahosi', 'yaproqsimon ajdarho', 'тряпичник', 'морской дракон', 'leafy seadragon']},
    {   'id': 'nature_scale_001_fastest_animal_dive',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Qaysi jonzot sho'ng'ish paytida yer yuzidagi eng yuqori tezlikka (389 km/soat) "
                              'erishadi?',
                        'ru': 'Какое животное развивает максимальную скорость на Земле при пикировании (до 389 км/ч)?',
                        'en': 'Which animal reaches the highest recorded speed on Earth during a dive (up to 389 '
                              'km/h)?'},
        'options': {   'uz': ['Lochin (Sapsan)', 'Gepard', 'Oltin burgut', 'Qora marlin'],
                       'ru': ['Сапсан', 'Гепард', 'Беркут', 'Черный марлин'],
                       'en': ['Peregrine Falcon', 'Cheetah', 'Golden Eagle', 'Black Marlin']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Lochin (Sapsan)', 'ru': 'Сапсан', 'en': 'Peregrine Falcon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Falco_peregrinus_head.jpg/800px-Falco_peregrinus_head.jpg',
        'fun_fact': {   'uz': "Sapsan o'ljaga sho'ng'iyotganda soatiga 389 km tezlikka erishadi. Uning burnidagi "
                              "maxsus to'siqlar yuqori bosimli havoning o'pkaga urilishini sekinlashtiradi.",
                        'ru': 'При пикировании сапсан разгоняется до 389 км/ч. Костные бугорки в его ноздрях '
                              'рассеивают набегающий поток воздуха, позволяя дышать.',
                        'en': 'In a hunting dive (stoop), the peregrine falcon reaches speeds up to 389 km/h (242 '
                              'mph), using specialized nasal baffles to regulate airflow.'},
        'aliases': ['sapsan', 'lochin', 'сапсан', 'сокол', 'peregrine falcon', 'falcon']},
    {   'id': 'nature_scale_002_fastest_land_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Quruqlikdagi eng tez yuguruvchi sutemizuvchi hayvon qaysi (110–120 km/soat)?',
                        'ru': 'Какое наземное млекопитающее является самым быстрым в мире (110–120 км/ч)?',
                        'en': 'Which land mammal is the fastest sprinter on Earth, reaching 110–120 km/h?'},
        'options': {   'uz': ['Vilorog (Pronghorn)', 'Gepard', 'Sher', "Bo'ri"],
                       'ru': ['Вилорог', 'Гепард', 'Лев', 'Волк'],
                       'en': ['Pronghorn', 'Cheetah', 'Lion', 'Wolf']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Gepard', 'ru': 'Гепард', 'en': 'Cheetah'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Cheetah_running_full_speed.jpg/800px-Cheetah_running_full_speed.jpg',
        'fun_fact': {   'uz': 'Gepard 0 dan 100 km/soat tezlikka atigi 3 soniyada erishadi, ammo u bu tezlikni '
                              "bor-yo'g'i 400-500 metr masofada ushlab tura oladi.",
                        'ru': 'Гепард разгоняется до 100 км/ч всего за 3 секунды, быстрее большинства спорткаров, но '
                              'выдерживает спринт лишь на дистанции до 500 метров.',
                        'en': 'The cheetah accelerates from 0 to 100 km/h in just 3 seconds, though it can only '
                              'sustain this anaerobic sprint for roughly 400–500 meters.'},
        'aliases': ['gepard', 'гепард', 'cheetah']},
    {   'id': 'nature_scale_003_fastest_swimmer',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Dunyo okeanida eng tez suzuvchi baliq qaysi hisoblanadi (110–129 km/soat)?',
                        'ru': 'Какая рыба считается самой быстрой в мировом океане (до 110–129 км/ч)?',
                        'en': 'Which fish is recognized as the fastest swimmer in the global ocean, reaching up to '
                              '110–129 km/h?'},
        'options': {   'uz': ['Oq akula', 'Tyunets (Tuna)', 'Qora marlin (Yelkanbaliq)', 'Barracuda'],
                       'ru': ['Белая акула', 'Синий тунец', 'Черный марлин (Парусник)', 'Барракуда'],
                       'en': ['Great White Shark', 'Bluefin Tuna', 'Black Marlin (Sailfish)', 'Barracuda']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Qora marlin (Yelkanbaliq)',
                              'ru': 'Черный марлин (Парусник)',
                              'en': 'Black Marlin (Sailfish)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Sailfish_underwater_speed.jpg/800px-Sailfish_underwater_speed.jpg',
        'fun_fact': {   'uz': "Qora marlin va yelkanbaliq gidrodinamik nayzasimon tumshug'i tufayli suv qarshiligini "
                              'yengib, qisqa masofada 120 km/soatdan ortiq tezlikda harakatlana oladi.',
                        'ru': 'Благодаря мечевидному роструму и серповидному хвосту парусник и черный марлин способны '
                              'разгоняться в воде до 120–129 км/ч.',
                        'en': 'The black marlin and sailfish streamline their bodies by folding dorsal fins into '
                              'grooves, clocking burst speeds up to 129 km/h.'},
        'aliases': ['marlin', 'qora marlin', 'yelkanbaliq', 'парусник', 'черный марлин', 'sailfish', 'marlin']},
    {   'id': 'nature_scale_004_fastest_level_flight_bird',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Gorizontal tekis parvozda (sho'ng'ishsiz) eng tez uchadigan qush qaysi (111–170 "
                              'km/soat)?',
                        'ru': 'Какая птица развивает наибольшую скорость в горизонтальном полете без пикирования '
                              '(111–170 км/ч)?',
                        'en': 'Which bird holds the record for the fastest horizontal flapping flight without diving '
                              '(111–170 km/h)?'},
        'options': {   'uz': ['Burgut', "O'rdak", 'Lochin', 'Ignadumli tezuchar (Swift)'],
                       'ru': ['Беркут', 'Кряква', 'Сапсан', 'Иглохвостый стриж'],
                       'en': ['Golden Eagle', 'Mallard', 'Peregrine Falcon', 'White-throated Needletail (Swift)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Ignadumli tezuchar (Swift)',
                              'ru': 'Иглохвостый стриж',
                              'en': 'White-throated Needletail (Swift)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Hirundapus_caudacutus_flight.jpg/800px-Hirundapus_caudacutus_flight.jpg',
        'fun_fact': {   'uz': 'Ignadumli tezuchar gorizontal tekis uchishda soatiga 170 km tezlikka erishadi va bir '
                              "necha oy davomida yerga qo'nmasdan havoda yashay oladi.",
                        'ru': 'Иглохвостый стриж развивает рекордные 170 км/ч в активном машущем полете и может '
                              'проводить в воздухе непрерывно до 10 месяцев.',
                        'en': 'The white-throated needletail can reach 170 km/h in sustained horizontal flapping '
                              'flight, staying airborne for months at a time.'},
        'aliases': ['strij', 'tezuchar', 'стриж', 'иглохвостый стриж', 'swift', 'needletail']},
    {   'id': 'nature_scale_005_fastest_running_bird',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Yer yuzidagi eng tez yuguruvchi qush qaysi (70 km/soat)?',
                        'ru': 'Какая птица является самым быстрым бегуном на суше (до 70 км/ч)?',
                        'en': 'Which bird is the fastest runner on land, reaching speeds up to 70 km/h?'},
        'options': {   'uz': ['Tuyaqush (Straus)', 'Emu', 'Kazuar', 'Kivi'],
                       'ru': ['Африканский страус', 'Эму', 'Казуар', 'Киви'],
                       'en': ['Ostrich', 'Emu', 'Cassowary', 'Kiwi']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Tuyaqush (Straus)', 'ru': 'Африканский страус', 'en': 'Ostrich'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Struthio_camelus_running.jpg/800px-Struthio_camelus_running.jpg',
        'fun_fact': {   'uz': 'Tuyaqush soatiga 70 km tezlikda yuguradi va bir qadamining uzunligi 4-5 metrgacha '
                              'yetishi mumkin.',
                        'ru': 'Страус развивает скорость до 70 км/ч, делая шаги длиной до 5 метров, и может бежать на '
                              'высокой скорости полчаса.',
                        'en': 'Ostriches run at steady speeds up to 70 km/h with 5-meter strides, making them the '
                              'fastest creatures on two legs.'},
        'aliases': ['tuyaqush', 'straus', 'страус', 'африканский страус', 'ostrich']},
    {   'id': 'nature_scale_006_fastest_reptile_land',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Quruqlikda eng tez yuguruvchi kaltakesak turi qaysi (35–40 km/soat)?',
                        'ru': 'Какая ящерица бегает быстрее всех на суше (до 35–40 км/ч)?',
                        'en': 'Which lizard is the fastest sprinter on land, reaching 35–40 km/h?'},
        'options': {   'uz': ['Komodo varani', 'Qora tikanquyruq iguana', 'Xameleon', 'Gekkon'],
                       'ru': ['Комодский варан', 'Черная шипохвостая игуана', 'Хамелеон', 'Геккон'],
                       'en': ['Komodo Dragon', 'Black Spiny-tailed Iguana', 'Chameleon', 'Gecko']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Qora tikanquyruq iguana',
                              'ru': 'Черная шипохвостая игуана',
                              'en': 'Black Spiny-tailed Iguana'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Ctenosaura_similis_running.jpg/800px-Ctenosaura_similis_running.jpg',
        'fun_fact': {   'uz': 'Qora tikanquyruq iguana (Ctenosaura similis) Ginnesning rekordlar kitobiga dunyodagi '
                              'eng tez yuguruvchi kaltakesak (34.6 km/soat) sifatida kiritilgan.',
                        'ru': 'Черная игуана внесена в Книгу рекордов Гиннесса со скоростью бега 34,9 км/ч, спасаясь '
                              'от хищников на задних лапах.',
                        'en': 'The black spiny-tailed iguana holds the Guinness World Record for lizard sprint speed '
                              'at 34.9 km/h (21.7 mph).'},
        'aliases': ['qora iguana', 'tikanquyruq iguana', 'черная игуана', 'black spiny-tailed iguana', 'iguana']},
    {   'id': 'nature_scale_007_slowest_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Yer yuzidagi eng sekin harakatlanuvchi sutemizuvchi qaysi (soatiga atigi 0.24 km)?',
                        'ru': 'Какое млекопитающее является самым медлительным на Земле (около 0,24 км/ч)?',
                        'en': 'Which mammal is recognized as the slowest-moving on Earth (around 0.24 km/h)?'},
        'options': {   'uz': ['Koala', 'Sekin lori', 'Uch barmoqli yalqov (Sloth)', 'Tipratikan'],
                       'ru': ['Коала', 'Медленный лори', 'Трёхпалый ленивец', 'Ёж'],
                       'en': ['Koala', 'Slow Loris', 'Three-toed Sloth', 'Hedgehog']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Uch barmoqli yalqov (Sloth)', 'ru': 'Трёхпалый ленивец', 'en': 'Three-toed Sloth'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Bradypus_tridactylus_sloth.jpg/800px-Bradypus_tridactylus_sloth.jpg',
        'fun_fact': {   'uz': 'Yalqov daraxt shoxlarida daqiqasiga 2-4 metr tezlikda siljiydi. Uning ovqat hazm qilish '
                              'jarayoni 1 oygacha vaqt olishi mumkin.',
                        'ru': 'Трехпалый ленивец двигается со средней скоростью около 2 метров в минуту, а '
                              'переваривание одного листа занимает у него до 30 дней.',
                        'en': 'A three-toed sloth moves at a maximum tree speed of 2–4 meters per minute, with a '
                              'metabolic rate so low that digesting one leaf takes up to a month.'},
        'aliases': ['yalqov', 'dangasa', 'ленивец', 'трехпалый ленивец', 'sloth', 'three-toed sloth']},
    {   'id': 'nature_scale_008_fastest_insect_flight',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Havoda eng yuqori parvoz tezligiga erisha oladigan hasharot qaysi (soatiga 50–90 km)?',
                        'ru': 'Какое насекомое летает быстрее всех в мире (до 50–90 км/ч)?',
                        'en': 'Which insect is widely considered the fastest flyer in the world (up to 50–90 km/h)?'},
        'options': {   'uz': ['Asalari', 'Pashsha', "May qo'ng'izi", 'Ninachi (Avstraliya ninachisi)'],
                       'ru': ['Медоносная пчела', 'Комнатная муха', 'Майский жук', 'Стрекоза (Австралийская)'],
                       'en': ['Honeybee', 'Housefly', 'Cockchafer', 'Dragonfly (Australian Dragonfly)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Ninachi (Avstraliya ninachisi)',
                              'ru': 'Стрекоза (Австралийская)',
                              'en': 'Dragonfly (Australian Dragonfly)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Austrophlebia_costalis_dragonfly.jpg/800px-Austrophlebia_costalis_dragonfly.jpg',
        'fun_fact': {   'uz': 'Avstraliya ulkan ninachisi (Austrophlebia costalis) qisqa masofalarda soatiga 97 km '
                              "gacha tezlikda uchib, havoda to'satdan to'xtash va orqaga uchish qobiliyatiga ega.",
                        'ru': 'Некоторые виды крупных стрекоз способны развивать скорость до 90 км/ч и совершать '
                              'сложнейшие фигуры пилотажа.',
                        'en': 'Australian giant dragonflies can achieve bursts approaching 90 km/h, hovering, flying '
                              'backwards, and pulling up to 30 Gs during aerial prey capture.'},
        'aliases': ['ninachi', 'стрекоза', 'dragonfly']},
    {   'id': 'nature_scale_009_fastest_predatory_strike',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "O'ljaga zarba berish tezligi bo'yicha hayvonot olamidagi mutlaq rekordchi qaysi "
                              '(soniyasiga 23 metr, 10 400 G)?',
                        'ru': 'Какое морское животное наносит самый быстрый удар в природе (23 м/с, ускорение 10 400 '
                              'G)?',
                        'en': 'Which marine animal delivers the fastest predatory strike in nature (23 m/s, 10,400 G '
                              'acceleration)?'},
        'options': {   'uz': ['Beshiktebratar qisqichbaqa (Mantis Shrimp)', 'Meduza', 'Oq akula', 'Kalmar'],
                       'ru': ['Рак-богомол', 'Медуза', 'Белая акула', 'Кальмар'],
                       'en': ['Mantis Shrimp', 'Jellyfish', 'Great White Shark', 'Squid']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Beshiktebratar qisqichbaqa (Mantis Shrimp)',
                              'ru': 'Рак-богомол',
                              'en': 'Mantis Shrimp'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Odontodactylus_scyllarus_mantis_shrimp.jpg/800px-Odontodactylus_scyllarus_mantis_shrimp.jpg',
        'fun_fact': {   'uz': "Ushbu qisqichbaqa dactil bolg'achasi bilan o'q tezligida zarba beradi; zarba suvda "
                              "kavitatsiya pufakchasi hosil qilib, 4500 °C haroratli yorug'lik chaqnashi yuzaga "
                              'keltiradi.',
                        'ru': 'Удар клешни рака-богомола равен по ускорению пуле 22 калибра, вызывая схлопывание '
                              'кавитационных пузырей с температурой поверхности Солнца.',
                        'en': 'The peacock mantis shrimp strikes with the acceleration of a .22 caliber bullet, '
                              'generating acoustic cavitation bubbles that flash at 4,500 °C.'},
        'aliases': ['beshiktebratar qisqichbaqa', 'rak bogomol', 'рак-богомол', 'mantis shrimp']},
    {   'id': 'nature_scale_010_fastest_jaw_movement',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yer yuzidagi jag'ini eng tez yopish rekordiga ega jonzot qaysi (soatiga 320 km "
                              'tezlikda)?',
                        'ru': 'Какое насекомое смыкает челюсти быстрее всех на Земле (до 320 км/ч)?',
                        'en': 'Which creature snaps its jaws shut faster than any other on Earth (up to 320 km/h)?'},
        'options': {   'uz': ['Chayon', 'Drakula chumolisi (Mystrium camillae)', 'Qora beva', 'Termit'],
                       'ru': ['Скорпион', 'Муравей-дракула', 'Черная вдова', 'Термит'],
                       'en': ['Scorpion', 'Dracula Ant (Mystrium camillae)', 'Black Widow', 'Termite']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Drakula chumolisi (Mystrium camillae)',
                              'ru': 'Муравей-дракула',
                              'en': 'Dracula Ant (Mystrium camillae)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Mystrium_camillae_mandibles.jpg/800px-Mystrium_camillae_mandibles.jpg',
        'fun_fact': {   'uz': "Drakula chumolisi o'z jag'larini barmoqni shiqillatgan kabi taranglab, sekundiga 90 "
                              "metr (soatiga 320 km) tezlikda uradi, bu odam ko'z pirpiratishidan 5000 baravar tezdir.",
                        'ru': 'Муравей Mystrium camillae с силой щелкает мандибулами со скоростью до 90 м/с, что в '
                              '5000 раз быстрее человеческого моргания.',
                        'en': 'The Dracula ant snaps its mandibles like a spring-loaded finger snap at 90 m/s (320 '
                              'km/h), making it the fastest animal appendage motion.'},
        'aliases': ['chumoli', 'drakula chumolisi', 'муравей', 'муравей-дракула', 'dracula ant']},
    {   'id': 'nature_scale_011_longest_living_vertebrate',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yer yuzida eng uzoq umr ko'ruvchi umurtqali hayvon qaysi (400 yildan ortiq)?",
                        'ru': 'Какое позвоночное животное на Земле живет дольше всех (более 400 лет)?',
                        'en': 'Which vertebrate animal on Earth has the longest documented lifespan (over 400 years)?'},
        'options': {   'uz': ['Galapagos toshbaqasi', 'Bukri kit', 'Grenlandiya qutb akulasi', "Ko'k kit"],
                       'ru': ['Галапагосская черепаха', 'Горбатый кит', 'Гренландская полярная акула', 'Синий кит'],
                       'en': ['Galapagos Tortoise', 'Humpback Whale', 'Greenland Shark', 'Blue Whale']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Grenlandiya qutb akulasi',
                              'ru': 'Гренландская полярная акула',
                              'en': 'Greenland Shark'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Somniosus_microcephalus_greenland_shark.jpg/800px-Somniosus_microcephalus_greenland_shark.jpg',
        'fun_fact': {   'uz': "Grenlandiya akulasi yiliga atigi 1 santimetr o'sadi va 150 yoshga yetgandagina nasl "
                              "berish qobiliyatiga ega bo'ladi. U 400-500 yilgacha yashay oladi.",
                        'ru': 'Гренландские акулы растут по 1 см в год и достигают половой зрелости лишь к 150 годам, '
                              'доживая до 400–500 лет в арктических глубинах.',
                        'en': 'Greenland sharks grow only ~1 cm per year and do not reach reproductive maturity until '
                              'age 150, living for upwards of 400 to 500 years.'},
        'aliases': ['grenlandiya akulasi', 'qutb akulasi', 'гренландская акула', 'полярная акула', 'greenland shark']},
    {   'id': 'nature_scale_012_longest_living_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Sutemizuvchilar orasida eng uzoq umr ko'rish bo'yicha rekordchi qaysi (200 yildan "
                              'ortiq)?',
                        'ru': 'Какое млекопитающее является рекордсменом-долгожителем (живет свыше 200 лет)?',
                        'en': 'Which mammal holds the record for the longest lifespan, living over 200 years?'},
        'options': {   'uz': ['Afrika fili', 'Odam', 'Kashalot', 'Grenlandiya kiti (Bowhead Whale)'],
                       'ru': ['Африканский слон', 'Человек', 'Кашалот', 'Гренландский кит (Полярный кит)'],
                       'en': ['African Elephant', 'Human', 'Sperm Whale', 'Bowhead Whale']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Grenlandiya kiti (Bowhead Whale)',
                              'ru': 'Гренландский кит (Полярный кит)',
                              'en': 'Bowhead Whale'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Balaena_mysticetus_bowhead_whale.jpg/800px-Balaena_mysticetus_bowhead_whale.jpg',
        'fun_fact': {   'uz': "Grenlandiya kitlarining tanasidan 100 yildan ko'proq vaqt oldin yasalgan qadimiy suyak "
                              'garpunlar topilgan; ular DNK tuzatish mexanizmlari evaziga saratonga chalinmaydi.',
                        'ru': 'В телах гренландских китов находили гарпуны XIX века; их гены обладают уникальными '
                              'механизмами репарации ДНК, защищающими от старения.',
                        'en': 'Bowhead whales live over 211 years; genetic studies reveal enhanced DNA repair and '
                              'duplication of cancer-resistant genes like ERCC1.'},
        'aliases': ['grenlandiya kiti', 'qutb kiti', 'гренландский кит', 'полярный кит', 'bowhead whale']},
    {   'id': 'nature_scale_013_longest_living_non_colonial_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dunyodagi eng uzoq umr ko'rgan yakka jonzot — 'Ming' nomli okean qisqichbaqasimon "
                              'mollyuskasi (Quahog) necha yil yashagan?',
                        'ru': 'Сколько лет прожил моллюск «Мин» (Ocean Quahog) — самое старое индивидуальное животное, '
                              'когда-либо найденное учеными?',
                        'en': "How old was 'Ming', the ocean quahog clam confirmed as the oldest individual "
                              'non-colonial animal ever discovered?'},
        'options': {   'uz': ['507 yil', '250 yil', '375 yil', '720 yil'],
                       'ru': ['507 лет', '250 лет', '375 лет', '720 лет'],
                       'en': ['507 years', '250 years', '375 years', '720 years']},
        'correct_index': 0,
        'correct_answer': {'uz': '507 yil', 'ru': '507 лет', 'en': '507 years'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Arctica_islandica_ocean_quahog.jpg/800px-Arctica_islandica_ocean_quahog.jpg',
        'fun_fact': {   'uz': 'Ming nomli Arctica islandica mollyuskasi Islandiya yaqinida topilgan va 507 yoshda '
                              "bo'lgan. U 1499-yilda — Kolumb sayohatlari davrida tug'ilgan.",
                        'ru': 'Моллюск «Мин» родился в 1499 году при династии Мин и прожил 507 лет, пока исследователи '
                              'не вскрыли его раковину для подсчета годовых колец.',
                        'en': 'Ming the ocean quahog was born in 1499 during the Ming dynasty and lived 507 years on '
                              'the seabed north of Iceland before collection in 2006.'},
        'aliases': ['507 yil', '507', '507 лет', '507 years']},
    {   'id': 'nature_scale_014_biologically_immortal_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Qaysi meduza qariganida o'z hujayralarini orqaga qaytarib (transdifferensiatsiya), yosh "
                              "polip shakliga o'tib o'lmaslikka erishadi?",
                        'ru': 'Какая медуза считается биологически бессмертной благодаря способности превращаться '
                              'обратно в молодой полип?',
                        'en': 'Which jellyfish is biologically immortal, capable of reverting its mature cells back '
                              'into a juvenile polyp colony?'},
        'options': {   'uz': ['Aureliya', 'Turritopsis dohrnii (Boqiy meduza)', 'Dengiz arisi', 'Sianeya'],
                       'ru': ['Аурелия', 'Turritopsis dohrnii (Бессмертная медуза)', 'Морская оса', 'Цианея'],
                       'en': [   'Moon Jellyfish',
                                 'Immortal Jellyfish (Turritopsis dohrnii)',
                                 'Box Jellyfish',
                                 "Lion's Mane Jellyfish"]},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Turritopsis dohrnii (Boqiy meduza)',
                              'ru': 'Turritopsis dohrnii (Бессмертная медуза)',
                              'en': 'Immortal Jellyfish (Turritopsis dohrnii)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Turritopsis_dohrnii_underwater.jpg/800px-Turritopsis_dohrnii_underwater.jpg',
        'fun_fact': {   'uz': "Turritopsis dohrnii shikastlanganda yoki qariganida o'z meduza to'qimalarini yosh "
                              'poliplarga aylantira oladi va bu jarayonni cheksiz takrorlaydi.',
                        'ru': 'При стрессе или старении клетки Turritopsis dohrnii перепрограммируются, превращая '
                              'взрослую медузу обратно в юный полип.',
                        'en': 'Turritopsis dohrnii escapes natural death by transdifferentiating mature adult cells '
                              'back into totipotent stem cells, rebooting its lifecycle indefinitely.'},
        'aliases': ['boqiy meduza', 'turritopsis', 'бессмертная медуза', 'turritopsis dohrnii', 'immortal jellyfish']},
    {   'id': 'nature_scale_015_longest_living_bird',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yovvoyi tabiatda eng uzoq umr ko'rish bo'yicha rekordchi qush qaysi (Uizdom nomli "
                              'albatros 73 yoshdan oshgan)?',
                        'ru': 'Какая птица является рекордсменом-долгожителем в дикой природе (самка альбатроса Уиздом '
                              'перешагнула 73 года)?',
                        'en': 'Which bird holds the record for the oldest wild bird in history, with individual '
                              "'Wisdom' surpassing 73 years of age?"},
        'options': {   'uz': ['Burgut', "Qizil ara to'tisi", 'Laysan albatrosi', 'Pelikan'],
                       'ru': ['Беркут', 'Красный ара', 'Лайсанский альбатрос', 'Пеликан'],
                       'en': ['Golden Eagle', 'Scarlet Macaw', 'Laysan Albatross', 'Pelican']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Laysan albatrosi', 'ru': 'Лайсанский альбатрос', 'en': 'Laysan Albatross'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Phoebastria_immutabilis_laysan_albatross.jpg/800px-Phoebastria_immutabilis_laysan_albatross.jpg',
        'fun_fact': {   'uz': "Uizdom nomli albatros 1956-yilda ilk bor halqalangandi. U o'z umri davomida 40 dan "
                              "ortiq jo'jani muvaffaqiyatli ulg'aytirgan va 5 million km uchgan.",
                        'ru': 'Самка альбатроса Уиздом, окольцованная в 1956 году, вырастила более 40 птенцов и '
                              'налетала свыше 5 миллионов километров над океаном.',
                        'en': 'Banded in 1956, Wisdom the Laysan albatross has flown over 3 million miles and raised '
                              'more than 40 chicks well into her 70s.'},
        'aliases': [   'albatros',
                       'laysan albatrosi',
                       'альбатрос',
                       'лайсанский альбатрос',
                       'albatross',
                       'laysan albatross']},
    {   'id': 'nature_scale_016_shortest_lifespan_insect',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Voyaga yetgan holatida bor-yo'g'i bir necha soatdan bir kungacha yashaydigan hasharot "
                              'qaysi?',
                        'ru': 'Какое взрослое насекомое (имаго) живет меньше всех на Земле — всего от нескольких часов '
                              'до одних суток?',
                        'en': 'Which insect has the shortest adult (imago) lifespan on Earth, living anywhere from a '
                              'few hours to just one day?'},
        'options': {   'uz': ['Chivin', 'Chigirtka', 'Asalari', 'Bir kunlik hasharot (Kunlik pashsha / Mayfly)'],
                       'ru': ['Комар', 'Саранча', 'Медоносная пчела', 'Подёнка'],
                       'en': ['Mosquito', 'Locust', 'Honeybee', 'Mayfly']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Bir kunlik hasharot (Kunlik pashsha / Mayfly)', 'ru': 'Подёнка', 'en': 'Mayfly'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Ephemeroptera_mayfly_macro.jpg/800px-Ephemeroptera_mayfly_macro.jpg',
        'fun_fact': {   'uz': "Kunlik pashshaning voyaga yetgan davrida og'zi va oshqozoni umuman bo'lmaydi; uning "
                              "yagona vazifasi bir necha soat ichida juftlasha olish va tuxum qo'yishdir.",
                        'ru': 'Взрослые подёнки лишены ротового аппарата и пищеварительной системы: их единственная '
                              'цель — спариться и отложить яйца за несколько часов жизни.',
                        'en': 'Adult mayflies (Ephemeroptera) have vestigial mouthparts and non-functional digestive '
                              'tracts, living only hours to mate and lay eggs.'},
        'aliases': ['podenka', 'kunlik pashsha', 'поденка', 'подёнка', 'mayfly']},
    {   'id': 'nature_scale_017_longest_living_reptile',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Quruqlikdagi eng uzoq umr ko'ruvchi sudralib yuruvchi jonivor qaysi (Jonatan nomli "
                              'toshbaqa 190 yoshdan oshgan)?',
                        'ru': 'Какое наземное пресмыкающееся живет дольше всех (самец черепахи Джонатан перешагнул '
                              'рубеж в 190 лет)?',
                        'en': "Which terrestrial reptile holds the record for longevity, exemplified by 'Jonathan' who "
                              'has surpassed 190 years?'},
        'options': {   'uz': ['Seyшел ulkan toshbaqasi', 'Komodo varani', 'Nil timsohi', 'Alligator'],
                       'ru': ['Сейшельская гигантская черепаха', 'Комодский варан', 'Нильский крокодил', 'Аллигатор'],
                       'en': ['Seychelles Giant Tortoise', 'Komodo Dragon', 'Nile Crocodile', 'Alligator']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Seyшел ulkan toshbaqasi',
                              'ru': 'Сейшельская гигантская черепаха',
                              'en': 'Seychelles Giant Tortoise'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Jonathan_giant_tortoise_St_Helena.jpg/800px-Jonathan_giant_tortoise_St_Helena.jpg',
        'fun_fact': {   'uz': "Muqaddas Yelena orolida yashovchi Jonatan nomli toshbaqa taxminan 1832-yilda tug'ilgan "
                              'va hozirda yer yuzidagi eng keksa tirik quruqlik jonzoti hisoblanadi.',
                        'ru': 'Черепаха Джонатан родился около 1832 года на Сейшелах и пережил две мировые войны и 40 '
                              'президентов США на острове Святой Елены.',
                        'en': 'Jonathan the Seychelles giant tortoise was hatched around 1832 and is verified by '
                              'Guinness as the oldest known living land animal.'},
        'aliases': ['jonatan', 'seyshel toshbaqasi', 'сейшельская черепаха', 'джонатан', 'giant tortoise', 'tortoise']},
    {   'id': 'nature_scale_018_longest_living_rodent',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Kemiruvchilar orasida 30-32 yil umr ko'rib, saratonga mutlaqo chalinmaydigan noyob "
                              'jonivor qaysi?',
                        'ru': 'Какой грызун-долгожитель живет до 32 лет и практически не подвержен заболеванию раком?',
                        'en': 'Which rodent lives up to 32 years and is exceptionally resistant to developing cancer?'},
        'options': {   'uz': ['Dala sichqoni', "Yalang'och yerqazar (Naked mole-rat)", 'Kalamush', 'Sincob'],
                       'ru': ['Полевка', 'Голый землекоп', 'Серая крыса', 'Белка'],
                       'en': ['Field Mouse', 'Naked Mole-rat', 'Norway Rat', 'Tree Squirrel']},
        'correct_index': 1,
        'correct_answer': {   'uz': "Yalang'och yerqazar (Naked mole-rat)",
                              'ru': 'Голый землекоп',
                              'en': 'Naked Mole-rat'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Heterocephalus_glaber_naked_mole_rat.jpg/800px-Heterocephalus_glaber_naked_mole_rat.jpg',
        'fun_fact': {   'uz': "Oddiy sichqonlar 2-3 yil yashagan holda, yalang'och yerqazar 30 yildan ortiq yashaydi. "
                              "Uning tanasidagi yuqori molekulyar gialuron kislotasi o'smalar paydo bo'lishiga yo'l "
                              "qo'ymaydi.",
                        'ru': 'Голый землекоп живет в 10 раз дольше обычных мышей благодаря сверхустойчивости белков и '
                              'уникальной высокомолекулярной гиалуроновой кислоте.',
                        'en': 'Naked mole-rats live over 30 years with negligible senescence, shielded from cancer by '
                              'unique high-molecular-mass hyaluronan.'},
        'aliases': ['yerqazar', 'yalangoch yerqazar', 'голый землекоп', 'землекоп', 'naked mole-rat', 'mole rat']},
    {   'id': 'nature_scale_019_longest_living_fish_freshwater',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Chuchuk suv baliqlari orasida eng uzoq umr ko'rish bo'yicha mashhur yapon karpi (Koi) "
                              'necha yil yashagan?',
                        'ru': 'До какого рекордного возраста дожила знаменитая японская рыба кои по кличке Ханако?',
                        'en': "To what verified record age did the famous Japanese koi carp named 'Hanako' survive?"},
        'options': {   'uz': ['105 yil', '150 yil', '226 yil', '310 yil'],
                       'ru': ['105 лет', '150 лет', '226 лет', '310 лет'],
                       'en': ['105 years', '150 years', '226 years', '310 years']},
        'correct_index': 2,
        'correct_answer': {'uz': '226 yil', 'ru': '226 лет', 'en': '226 years'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Koi_Hanako_carp.jpg/800px-Koi_Hanako_carp.jpg',
        'fun_fact': {   'uz': "Xanako laqabli qizil yapon karpi 1751-yilda tug'ilib, 1977-yilda 226 yoshida nobud "
                              "bo'lgan. Uning yoshi tangachalaridagi yillik halqalar orqali aniqlangan.",
                        'ru': 'Карп кои Ханако родился в 1751 году во времена сёгуната Токугава и прожил 226 лет; '
                              'возраст был определен по кольцам чешуи профессором Косихарой.',
                        'en': 'Hanako, a scarlet koi carp from Japan, lived from 1751 to 1977, reaching a verified age '
                              'of 226 confirmed by counting growth rings on her scales.'},
        'aliases': ['226 yil', '226', '226 лет', '226 years', 'hanako']},
    {   'id': 'nature_scale_020_longest_living_invertebrate_coral',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Gavayida topilgan qora chuqur dengiz marjon koloniyasi (Leiopathes) necha yoshda deb '
                              'baholangan?',
                        'ru': 'Сколько тысяч лет насчитывает возраст глубоководных колоний черных кораллов Leiopathes '
                              'у Гавайских островов?',
                        'en': 'How many years old are the deep-sea black coral colonies (Leiopathes) discovered near '
                              'the Hawaiian islands?'},
        'options': {   'uz': ['800 yil', '1200 yil', '10 500 yil', '4265 yil'],
                       'ru': ['800 лет', '1200 лет', '10 500 лет', '4265 лет'],
                       'en': ['800 years', '1,200 years', '10,500 years', '4,265 years']},
        'correct_index': 3,
        'correct_answer': {'uz': '4265 yil', 'ru': '4265 лет', 'en': '4,265 years'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Leiopathes_black_coral_deep_sea.jpg/800px-Leiopathes_black_coral_deep_sea.jpg',
        'fun_fact': {   'uz': '400 metr chuqurlikdagi qora marjonlarning radiouglerod tahlili ularning yoshi 4200 '
                              "yildan ortiq ekanini ko'rsatdi, bu ularni yer yuzidagi eng qadimiy tirik organizmlardan "
                              'biriga aylantiradi.',
                        'ru': 'Радиоуглеродный анализ полипов черного коралла показал возраст 4265 лет: они начали '
                              'расти во времена строительства египетских пирамид.',
                        'en': 'Radiocarbon dating of Hawaiian deep-sea black coral Leiopathes glaberrima revealed '
                              'continuous colony growth for over 4,265 years.'},
        'aliases': ['4265 yil', '4265', '4265 лет', '4265 years']},
    {   'id': 'nature_scale_021_heaviest_animal_ever',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yer yuzi tarixida yashagan eng ulkan va eng og'ir hayvon qaysi (vazni 190-200 "
                              'tonnagacha)?',
                        'ru': 'Какое животное является самым тяжелым и крупным за всю историю планеты (до 190–200 '
                              'тонн)?',
                        'en': 'Which animal is the largest and heaviest creature known to have ever existed on Earth '
                              '(up to 190–200 tonnes)?'},
        'options': {   'uz': ["Ko'k kit (Moviy kit)", 'Titanozavr', 'Kashalot', 'Megalodon'],
                       'ru': ['Синий кит (Блювал)', 'Титанозавр', 'Кашалот', 'Мегалодон'],
                       'en': ['Blue Whale', 'Titanosaur', 'Sperm Whale', 'Megalodon']},
        'correct_index': 0,
        'correct_answer': {'uz': "Ko'k kit (Moviy kit)", 'ru': 'Синий кит (Блювал)', 'en': 'Blue Whale'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Balaenoptera_musculus_swimming.jpg/800px-Balaenoptera_musculus_swimming.jpg',
        'fun_fact': {   'uz': "Ko'k kitning yuragi yengil avtomobil kattaligida (600 kg) bo'lib, uning tili esa bitta "
                              'butun fil vazniga teng (taxminan 3-4 tonna).',
                        'ru': 'Сердце синего кита весит около 600 кг и сравнимо с автомобилем Volkswagen Beetle, а '
                              'язык весит столько же, сколько взрослый африканский слон.',
                        'en': 'A blue whale can weigh nearly 200 metric tons; its heart weighs ~600 kg, and its tongue '
                              'alone weighs as much as an entire adult elephant.'},
        'aliases': ['kok kit', "ko'k kit", 'синий кит', 'блювал', 'blue whale']},
    {   'id': 'nature_scale_022_heaviest_land_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Hozirgi kunda quruqlikda yashovchi eng og'ir hayvon qaysi (vazni 6-10 tonnagacha)?",
                        'ru': 'Какое животное является самым тяжелым наземным млекопитающим современности (до 6–10 '
                              'тонн)?',
                        'en': 'Which animal is the heaviest living land mammal on Earth today (weighing 6–10 tonnes)?'},
        'options': {   'uz': ['Osiyo fili', 'Afrika savannasi fili', 'Oq karkidon', 'Begemot'],
                       'ru': ['Азиатский слон', 'Африканский саванный слон', 'Белый носорог', 'Бегемот'],
                       'en': ['Asian Elephant', 'African Bush Elephant', 'White Rhinoceros', 'Hippopotamus']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Afrika savannasi fili',
                              'ru': 'Африканский саванный слон',
                              'en': 'African Bush Elephant'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/African_Elephant_Loxodonta_africana_male.jpg/800px-African_Elephant_Loxodonta_africana_male.jpg',
        'fun_fact': {   'uz': "Tarixda qayd etilgan eng yirik afrika erkak filining vazni 10.4 tonnani, yag'rin bo'yi "
                              'esa 4 metrdan ortiqni tashkil etgan.',
                        'ru': 'Рекордный самец африканского слона, застреленный в Анголе в 1974 году, весил 10,4 тонны '
                              'при высоте в холке 4,16 метра.',
                        'en': 'The largest documented African bush elephant stood 4.16 meters tall at the shoulder and '
                              'weighed a staggering 10.4 metric tonnes.'},
        'aliases': ['afrika fili', 'fil', 'африканский слон', 'слон', 'african bush elephant', 'african elephant']},
    {   'id': 'nature_scale_023_heaviest_land_carnivore',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Quruqlikdagi eng yirik va eng og'ir yirtqich sutemizuvchi qaysi (erkaklari 800-1000 kg "
                              'gacha)?',
                        'ru': 'Какое сухопутное хищное млекопитающее является самым тяжелым в мире (самцы до 800–1000 '
                              'кг)?',
                        'en': 'Which terrestrial mammalian carnivore is the heaviest on Earth (males reaching '
                              '800–1,000 kg)?'},
        'options': {   'uz': ["Sibir yo'lbarsi", 'Afrika sheri', "Oq ayiq (Qutb ayig'i)", "Kodiak qo'ng'ir ayig'i"],
                       'ru': ['Амурский тигр', 'Африканский лев', 'Белый медведь', 'Медведь кодьяк'],
                       'en': ['Siberian Tiger', 'African Lion', 'Polar Bear', 'Kodiak Bear']},
        'correct_index': 2,
        'correct_answer': {'uz': "Oq ayiq (Qutb ayig'i)", 'ru': 'Белый медведь', 'en': 'Polar Bear'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Polar_Bear_standing_snow.jpg/800px-Polar_Bear_standing_snow.jpg',
        'fun_fact': {   'uz': "Tarixda qayd etilgan eng og'ir oq ayiqning vazni 1002 kg bo'lib, uning orqa oyoqlarida "
                              "tik turgan bo'yi 3.4 metrga yetgan.",
                        'ru': 'Крупнейший измеренный белый медведь весил ровно 1002 кг и, поднявшись на дыбы, достигал '
                              'высоты 3,39 метра.',
                        'en': 'The largest wild polar bear ever recorded weighed 1,002 kg (2,209 lb) and stood 3.39 m '
                              'tall on its hind legs.'},
        'aliases': ['oq ayiq', 'qutb ayigi', 'белый медведь', 'polar bear']},
    {   'id': 'nature_scale_024_heaviest_reptile',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Hozirgi kunda yer yuzida yashovchi eng og'ir sudralib yuruvchi (reptiliya) qaysi "
                              '(1000–1300 kg)?',
                        'ru': 'Какая рептилия является самой тяжелой и крупной из ныне живущих (до 1000–1300 кг)?',
                        'en': 'Which reptile is the largest and heaviest living specimen on Earth today (reaching '
                              '1,000–1,300 kg)?'},
        'options': {   'uz': [   'Terili dengiz toshbaqasi',
                                 'Nil timsohi',
                                 'Komodo varani',
                                 'Taroqli timsoh (Dengiz timsohi)'],
                       'ru': [   'Кожистая черепаха',
                                 'Нильский крокодил',
                                 'Комодский варан',
                                 'Гребнистый крокодил (Морской)'],
                       'en': ['Leatherback Sea Turtle', 'Nile Crocodile', 'Komodo Dragon', 'Saltwater Crocodile']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Taroqli timsoh (Dengiz timsohi)',
                              'ru': 'Гребнистый крокодил (Морской)',
                              'en': 'Saltwater Crocodile'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Crocodylus_porosus_saltwater.jpg/800px-Crocodylus_porosus_saltwater.jpg',
        'fun_fact': {   'uz': "Taroqli timsohlar uzunligi 6-7 metrga, og'irligi esa 1300 kg dan oshishi mumkin. Ular "
                              "ochiq okeanda yuzlab kilometr suzib o'ta oladi.",
                        'ru': 'Гребнистый крокодил достигает 7 метров в длину и массы более тонны; рекордный крокодил '
                              'Лолионг весил 1075 кг.',
                        'en': 'Saltwater crocodiles reach lengths of over 6.3 meters and weights exceeding 1,200 kg, '
                              'capable of traversing open oceans.'},
        'aliases': [   'taroqli timsoh',
                       'dengiz timsohi',
                       'гребнистый крокодил',
                       'морской крокодил',
                       'saltwater crocodile']},
    {   'id': 'nature_scale_025_heaviest_flying_bird',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Uchish qobiliyatiga ega bo'lgan eng og'ir qush turi qaysi (vazni 18-20 kg gacha)?",
                        'ru': 'Какая птица является самой тяжелой среди всех летающих птиц планеты (до 18–20 кг)?',
                        'en': 'Which bird holds the record as the heaviest bird capable of flight (weighing up to '
                              '18–20 kg)?'},
        'options': {   'uz': ["Kori tuvalog'i (Kori Bustard)", 'And kondori', 'Tovus', 'Oqqush-shipun'],
                       'ru': ['Африканская большая дрофа (Кори)', 'Андский кондор', 'Павлин', 'Лебедь-шипун'],
                       'en': ['Kori Bustard', 'Andean Condor', 'Peacock', 'Mute Swan']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Kori tuvalog'i (Kori Bustard)",
                              'ru': 'Африканская большая дрофа (Кори)',
                              'en': 'Kori Bustard'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ardeotis_kori_standing.jpg/800px-Ardeotis_kori_standing.jpg',
        'fun_fact': {   'uz': "Afrika savannalarida yashovchi kori tuvalog'ining erkaklari 19 kg gacha tosh bosadi, bu "
                              "esa qushlarning aerodinamik uchish chegarasidagi eng yuqori og'irlikdir.",
                        'ru': 'Самцы дрофы кори весят до 19 кг; это максимальная масса тела, при которой птица еще '
                              'способна взлететь с разбега.',
                        'en': 'Male kori bustards regularly reach 19 kg (42 lb), representing the biological upper '
                              'weight limit for avian flight.'},
        'aliases': ['kori tuvalogi', 'tuvaloq', 'дрофа кори', 'большая дрофа', 'kori bustard', 'bustard']},
    {   'id': 'nature_scale_026_heaviest_rodent',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dunyodagi eng og'ir va eng yirik kemiruvchi hayvon qaysi (vazni 60–80 kg)?",
                        'ru': 'Какой грызун является самым тяжелым и крупным в мире (масса 60–80 кг)?',
                        'en': 'Which animal is the largest and heaviest living rodent on Earth, weighing up to 60–80 '
                              'kg?'},
        'options': {   'uz': ['Qunduz (Bobr)', "Kapibara (Suv cho'chqasi)", 'Jayra', 'Nutriya'],
                       'ru': ['Канадский бобр', 'Капибара (Водосвинка)', 'Дикобраз', 'Нутрия'],
                       'en': ['Beaver', 'Capybara', 'Porcupine', 'Nutria']},
        'correct_index': 1,
        'correct_answer': {'uz': "Kapibara (Suv cho'chqasi)", 'ru': 'Капибара (Водосвинка)', 'en': 'Capybara'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Hydrochoerus_hydrochaeris_capybara.jpg/800px-Hydrochoerus_hydrochaeris_capybara.jpg',
        'fun_fact': {   'uz': "Janubiy Amerika suv bo'ylarida to'dalashib yashovchi kapibaralar suvda ajoyib suzadi va "
                              '5 daqiqagacha suv ostida nafas olmay tura oladi.',
                        'ru': 'Капибара достигает массы 65-80 кг и имеет перепонки между пальцами, позволяющие '
                              'превосходно плавать и нырять.',
                        'en': 'Capybaras can reach 80 kg; semi-aquatic herbivores native to South America, they have '
                              'webbed feet and can stay submerged for 5 minutes.'},
        'aliases': ['kapibara', 'капибара', 'водосвинка', 'capybara']},
    {   'id': 'nature_scale_027_heaviest_bony_fish',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dunyodagi eng og'ir suyakli baliq qaysi hisoblanadi (vazni 2744 kg gacha)?",
                        'ru': 'Какая костная рыба является самой тяжелой в мире (до 2744 кг)?',
                        'en': 'Which is the heaviest bony fish (Osteichthyes) ever recorded in the world (up to 2,744 '
                              'kg)?'},
        'options': {   'uz': [   'Beluga osyotri',
                                 'Atlantika treskasi',
                                 'Ulkan quyoshbaliq (Mola alexandrini / Mola mola)',
                                 'Gigant treska'],
                       'ru': ['Белуга', 'Атлантическая треска', 'Гигантская луна-рыба (Mola)', 'Гигантский групер'],
                       'en': [   'Beluga Sturgeon',
                                 'Atlantic Cod',
                                 'Giant Sunfish (Mola alexandrini)',
                                 'Goliath Grouper']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Ulkan quyoshbaliq (Mola alexandrini / Mola mola)',
                              'ru': 'Гигантская луна-рыба (Mola)',
                              'en': 'Giant Sunfish (Mola alexandrini)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Mola_alexandrini_sunfish.jpg/800px-Mola_alexandrini_sunfish.jpg',
        'fun_fact': {   'uz': '2021-yilda Azor orollarida tutilgan ulkan quyoshbaliqning vazni 2744 kg (deyarli 3 '
                              'tonna)ni tashkil etib, Ginnesning rekordlar kitobiga kirdi.',
                        'ru': 'Экземпляр шишкоголовой луны-рыбы, найденный у Азорских островов в 2021 году, весил '
                              'рекордные 2744 кг при длине 3,25 метра.',
                        'en': 'A giant sunfish (Mola alexandrini) weighed off the Azores in 2021 weighed 2,744 kg '
                              '(6,049 lb), the heaviest bony fish in history.'},
        'aliases': ['oybaliq', 'quyoshbaliq', 'mola mola', 'луна-рыба', 'mola alexandrini', 'sunfish']},
    {   'id': 'nature_scale_028_heaviest_invertebrate',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Umurtqasiz hayvonlar orasida eng og'ir va eng katta ko'zga ega bo'lgan jonivor qaysi "
                              '(495 kg)?',
                        'ru': 'Какое беспозвоночное животное является самым тяжелым на планете (до 495 кг)?',
                        'en': 'Which invertebrate is the heaviest on the planet, possessing eyes the size of soccer '
                              'balls (up to 495 kg)?'},
        'options': {   'uz': [   'Ulkan sakkizoyoq',
                                 'Gigant tridakna',
                                 'Gigant qisqichbaqa',
                                 'Ulkan kolossal kalmar (Mesonychoteuthis hamiltoni)'],
                       'ru': [   'Гигантский осьминог',
                                 'Гигантская тридакна',
                                 'Японский краб-паук',
                                 'Колоссальный кальмар'],
                       'en': ['Giant Octopus', 'Giant Clam', 'Japanese Spider Crab', 'Colossal Squid']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Ulkan kolossal kalmar (Mesonychoteuthis hamiltoni)',
                              'ru': 'Колоссальный кальмар',
                              'en': 'Colossal Squid'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Mesonychoteuthis_hamiltoni_specimen.jpg/800px-Mesonychoteuthis_hamiltoni_specimen.jpg',
        'fun_fact': {   'uz': 'Antarktika sovuq suvlarida yashovchi kolossal kalmarning paypaslagichlarida aylanuvchi '
                              "po'latdek o'tkir ilmoqlar va diametri 27 sm bo'lgan ulkan ko'zlar bor.",
                        'ru': 'Колоссальный кальмар весит до 495 кг, а его глаза диаметром 27 см — самые большие среди '
                              'всех существ, когда-либо живших на Земле.',
                        'en': 'The colossal squid weighs up to 495 kg and possesses 27-cm eyes equipped with rotating '
                              'hooks on its tentacles to battle sperm whales.'},
        'aliases': ['kolossal kalmar', 'kalmar', 'колоссальный кальмар', 'кальмар', 'colossal squid']},
    {   'id': 'nature_scale_029_tallest_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yer yuzidagi eng baland bo'yli hayvon qaysi (bo'yi 5.8 metrgacha)?",
                        'ru': 'Какое животное на Земле является самым высоким (рост до 5,8 метра)?',
                        'en': 'Which animal is the tallest living terrestrial creature on Earth (standing up to 5.8 '
                              'meters)?'},
        'options': {   'uz': ['Jirafa', 'Afrika fili', 'Tuyaqush', 'Moa'],
                       'ru': ['Жираф', 'Африканский слон', 'Страус', 'Моа'],
                       'en': ['Giraffe', 'African Elephant', 'Ostrich', 'Moa']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Jirafa', 'ru': 'Жираф', 'en': 'Giraffe'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Giraffa_camelopardalis_standing.jpg/800px-Giraffa_camelopardalis_standing.jpg',
        'fun_fact': {   'uz': "Jirafaning bo'yin umurtqalari odamnikidek atigi 7 ta bo'lsa-da, har bir umurtqasining "
                              "uzunligi 25 santimetrdan ortiq bo'ladi.",
                        'ru': 'Шея жирафа содержит ровно 7 позвонков — столько же, сколько у человека или мыши, но '
                              'каждый позвонок достигает 28 см в длину.',
                        'en': 'Despite its extraordinary height, a giraffe has only 7 cervical neck vertebrae, '
                              'identical in number to humans, each elongated to 28 cm.'},
        'aliases': ['jirafa', 'жираф', 'giraffe']},
    {   'id': 'nature_scale_030_longest_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Okean tubida topilgan va uzunligi 45-50 metrgacha yetadigan eng uzun mustamlaka jonzot '
                              'qaysi?',
                        'ru': 'Какое морское колониальное существо считается самым длинным животным в мире (до 45–50 '
                              'метров)?',
                        'en': 'Which deep-sea siphonophore is recognized as the longest animal specimen ever measured '
                              '(reaching 45–50 meters)?'},
        'options': {   'uz': ["Ko'k kit", 'Sifonofora (Apolemia)', 'Gigant kalmar', 'Ip qurt'],
                       'ru': ['Синий кит', 'Глубоководная сифонофора (Apolemia)', 'Гигантский кальмар', 'Немертина'],
                       'en': ['Blue Whale', 'Siphonophore (Apolemia)', 'Giant Squid', 'Bootlace Worm']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Sifonofora (Apolemia)',
                              'ru': 'Глубоководная сифонофора (Apolemia)',
                              'en': 'Siphonophore (Apolemia)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Apolemia_siphonophore_deep_sea.jpg/800px-Apolemia_siphonophore_deep_sea.jpg',
        'fun_fact': {   'uz': '2020-yilda Avstraliyaning Ningalu kanyonida Schmidt instituti olimlari 45 metr '
                              'uzunlikdagi spiral shaklidagi ulkan Apolemia sifonoforasini kashf qilishdi.',
                        'ru': 'В 2020 году у берегов Австралии ученые зафиксировали спиральную сифонофору длиной около '
                              '45-47 метров, превосходящую синего кита.',
                        'en': 'In 2020, oceanographers filmed a giant Apolemia siphonophore off Western Australia with '
                              'an outer ring measuring 47 meters in total length.'},
        'aliases': ['sifonofora', 'сифонофора', 'siphonophore', 'apolemia']},
    {   'id': 'nature_scale_031_deepest_diving_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dengiz sutemizuvchilari orasida eng chuqurga sho'ng'ish rekordini o'rnatgan jonivor "
                              'qaysi (2992 metr)?',
                        'ru': 'Какое морское млекопитающее является абсолютным рекордсменом по глубине погружения (до '
                              '2992 метров)?',
                        'en': 'Which marine mammal holds the absolute world record for the deepest dive ever recorded '
                              '(reaching 2,992 meters)?'},
        'options': {   'uz': ['Kashalot', 'Dengiz fili', "Kyuve tumshuqli kiti (Cuvier's beaked whale)", "Ko'k kit"],
                       'ru': ['Кашалот', 'Южный морской слон', 'Клюворыл Кювье', 'Синий кит'],
                       'en': ['Sperm Whale', 'Southern Elephant Seal', "Cuvier's Beaked Whale", 'Blue Whale']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Kyuve tumshuqli kiti (Cuvier's beaked whale)",
                              'ru': 'Клюворыл Кювье',
                              'en': "Cuvier's Beaked Whale"},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ziphius_cavirostris_cuviers_beaked_whale.jpg/800px-Ziphius_cavirostris_cuviers_beaked_whale.jpg',
        'fun_fact': {   'uz': "Kyuve tumshuqli kiti qariyb 3000 metr chuqurlikka sho'ng'ib, suv ostida 3 soat 42 "
                              'daqiqa nafas olmay tura olgan.',
                        'ru': 'Клюворыл Кювье опустился на глубину 2992 метра и находился под водой 222 минуты без '
                              'единого вдоха, сжимая легкие для избежания кессонной болезни.',
                        'en': "A tagged Cuvier's beaked whale dived to 2,992 meters (9,816 ft) and stayed submerged "
                              'for 3 hours and 42 minutes, tolerating crushing pressure.'},
        'aliases': [   'kyuve kiti',
                       'tumshuqli kit',
                       'клюворыл',
                       'клюворыл кювье',
                       'cuviers beaked whale',
                       'beaked whale']},
    {   'id': 'nature_scale_032_deepest_diving_pinniped',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Kurakoyoqlilar (tyulenlar) orasida eng chuqurga sho'ng'iy oladigan jonivor qaysi (2388 "
                              'metr)?',
                        'ru': 'Какой тюлень ныряет глубже всех среди всех ластоногих планеты (до 2388 метров)?',
                        'en': 'Which pinniped seal dives the deepest among all seals and sea lions (reaching 2,388 '
                              'meters)?'},
        'options': {   'uz': [   'Ueddell tyuleni',
                                 'Morj',
                                 'Dengiz sheri',
                                 'Janubiy dengiz fili (Southern Elephant Seal)'],
                       'ru': ['Тюлень Уэдделла', 'Морж', 'Морской лев', 'Южный морской слон'],
                       'en': ['Weddell Seal', 'Walrus', 'Sea Lion', 'Southern Elephant Seal']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Janubiy dengiz fili (Southern Elephant Seal)',
                              'ru': 'Южный морской слон',
                              'en': 'Southern Elephant Seal'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mirounga_leonina_male_antarctica.jpg/800px-Mirounga_leonina_male_antarctica.jpg',
        'fun_fact': {   'uz': "Janubiy dengiz filining qonida kislorod tashuvchi mioglobin miqdori favqulodda ko'p "
                              "bo'lib, u 2 soatgacha suv ostida ov qila oladi.",
                        'ru': 'Южные морские слоны способны задерживать дыхание на 2 часа и нырять на 2388 метров '
                              'благодаря огромному объему крови и высокому уровню миоглобина.',
                        'en': 'Southern elephant seals store 90% of their oxygen in blood and muscle rather than '
                              'lungs, permitting routine 2-hour dives beyond 2,000 meters.'},
        'aliases': [   'dengiz fili',
                       'janubiy dengiz fili',
                       'морской слон',
                       'южный морской слон',
                       'elephant seal',
                       'southern elephant seal']},
    {   'id': 'nature_scale_033_deepest_diving_bird',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Qushlar orasida eng chuqur suv qa'riga sho'ng'iy oladigan chempion qaysi (564 metr)?",
                        'ru': 'Какая птица ныряет глубже всех в мире (до 564 метров)?',
                        'en': 'Which bird holds the record for the deepest dive into the ocean (down to 564 meters)?'},
        'options': {   'uz': ['Imperator pingvini', 'Gagara', "O'rdak", 'Albatros'],
                       'ru': ['Императорский пингвин', 'Чернозобая гагара', 'Баклан', 'Альбатрос'],
                       'en': ['Emperor Penguin', 'Common Loon', 'Cormorant', 'Albatross']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Imperator pingvini', 'ru': 'Императорский пингвин', 'en': 'Emperor Penguin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Aptenodytes_forsteri_emperor_penguin_underwater.jpg/800px-Aptenodytes_forsteri_emperor_penguin_underwater.jpg',
        'fun_fact': {   'uz': "Imperator pingvini 564 metr chuqurlikka sho'ng'iy oladi; suv ostida uning yurak urishi "
                              'daqiqasiga 15-20 martagacha sekinlashadi.',
                        'ru': 'Императорский пингвин погружается на глубину свыше 500 метров в ледяные антарктические '
                              'воды, замедляя пульс до 15 ударов в минуту.',
                        'en': 'Emperor penguins withstand 50 atmospheres of pressure down to 564 meters, depressing '
                              'their heart rate from 200 bpm to just 15 bpm.'},
        'aliases': ['imperator pingvini', 'pingvin', 'императорский пингвин', 'пингвин', 'emperor penguin']},
    {   'id': 'nature_scale_034_deepest_diving_reptile',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Sudralib yuruvchilar (toshbaqalar) orasida eng chuqurga sho'ng'iy oladigan jonivor "
                              'qaysi (1280 metr)?',
                        'ru': 'Какая рептилия ныряет на наибольшую глубину среди всех пресмыкающихся (до 1280 метров)?',
                        'en': 'Which reptile holds the record for the deepest dive among all living reptiles (down to '
                              '1,280 meters)?'},
        'options': {   'uz': [   'Yashil toshbaqa',
                                 'Terili dengiz toshbaqasi (Leatherback)',
                                 'Taroqli timsoh',
                                 'Dengiz iloni'],
                       'ru': ['Зеленая черепаха', 'Кожистая морская черепаха', 'Гребнистый крокодил', 'Морская змея'],
                       'en': ['Green Sea Turtle', 'Leatherback Sea Turtle', 'Saltwater Crocodile', 'Sea Snake']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Terili dengiz toshbaqasi (Leatherback)',
                              'ru': 'Кожистая морская черепаха',
                              'en': 'Leatherback Sea Turtle'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Dermochelys_coriacea_leatherback.jpg/800px-Dermochelys_coriacea_leatherback.jpg',
        'fun_fact': {   'uz': 'Terili toshbaqaning elastik yumshoq kosasi va qon tomir tizimi unga 1280 metr '
                              'chuqurlikdagi ulkan gidrostatik bosimga bardosh berishga imkon beradi.',
                        'ru': 'В отличие от других черепах, панцирь кожистой черепахи образован гибкой хрящевой '
                              'тканью, сжимающейся под колоссальным давлением океана.',
                        'en': 'The flexible, oil-saturated cartilaginous carapace of the leatherback sea turtle '
                              'compresses smoothly under pressure, facilitating 1,280 m dives.'},
        'aliases': ['terili toshbaqa', 'кожистая черепаха', 'leatherback', 'leatherback sea turtle']},
    {   'id': 'nature_scale_035_deepest_living_fish',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Okeanning eng chuqur joyi — Mariana botig'ida (8336 metr) topilgan eng chuqur baliq "
                              'qaysi?',
                        'ru': 'Какая рыба обитает на максимальной глубине в океане (до 8336 метров в Марианской '
                              'впадине)?',
                        'en': 'Which fish holds the record for living at the deepest ocean depths (observed at 8,336 '
                              'meters in the Mariana Trench)?'},
        'options': {   'uz': [   'Dengiz shaytoni (Anglerfish)',
                                 'Qilichbaliq',
                                 "Mariana dengiz shilliqbalig'i (Snailfish)",
                                 'Morona'],
                       'ru': ['Удильщик', 'Рыба-сабля', 'Марианский морской слизень (Pseudoliparis)', 'Батизавр'],
                       'en': ['Anglerfish', 'Cutlassfish', 'Mariana Snailfish (Pseudoliparis)', 'Deep-sea Lizardfish']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Mariana dengiz shilliqbalig'i (Snailfish)",
                              'ru': 'Марианский морской слизень (Pseudoliparis)',
                              'en': 'Mariana Snailfish (Pseudoliparis)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pseudoliparis_swirei_mariana_snailfish.jpg/800px-Pseudoliparis_swirei_mariana_snailfish.jpg',
        'fun_fact': {   'uz': "Mariana shilliqbalig'i tanasida trimetilaminoksid (TMAO) moddasi bo'lib, u oqsillarni "
                              '8000 metr chuqurlikdagi 1000 atmosfera bosimidan himoya qiladi.',
                        'ru': 'Тело рыбы Pseudoliparis полупрозрачно и богато осмолитом ТМАО, предотвращающим '
                              'денатурацию белков при давлении 1000 атмосфер.',
                        'en': 'Pseudoliparis swirei thrives under 1,000 bar of hydrostatic pressure at 8,336 meters, '
                              'stabilized by high concentrations of TMAO piezolytes.'},
        'aliases': [   'mariana shilliqbaligi',
                       'marina snailfish',
                       'марианский слизень',
                       'snailfish',
                       'mariana snailfish']},
    {   'id': 'nature_scale_036_deepest_living_squid',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Filippin botig'ida 6212 metr chuqurlikda tasvirga olingan eng chuqur boshoyoqli "
                              'mollyuska qaysi?',
                        'ru': 'Какой глубоководный кальмар был зафиксирован на рекордной глубине 6212 метров в '
                              'Филиппинском желобе?',
                        'en': 'Which deep-sea cephalopod was documented swimming at a record-setting depth of 6,212 '
                              'meters in the Philippine Trench?'},
        'options': {   'uz': [   'Vampir kalmar',
                                 'Kolossal kalmar',
                                 'Nautilus',
                                 'Ulkan qanotli kalmar (Magnapinna / Bigfin squid)'],
                       'ru': [   'Адский вампир',
                                 'Колоссальный кальмар',
                                 'Наутилус',
                                 'Глубоководный длиннорукий кальмар (Магнапинна)'],
                       'en': ['Vampire Squid', 'Colossal Squid', 'Nautilus', 'Bigfin Squid (Magnapinna)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Ulkan qanotli kalmar (Magnapinna / Bigfin squid)',
                              'ru': 'Глубоководный длиннорукий кальмар (Магнапинна)',
                              'en': 'Bigfin Squid (Magnapinna)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Magnapinna_squid_deep_sea.jpg/800px-Magnapinna_squid_deep_sea.jpg',
        'fun_fact': {   'uz': "Magnapinna kalmarining paypaslagichlari 8 metr uzunlikka cho'zilib, tanasidan 90 gradus "
                              "burchak ostida tushadi va suv tubida o'lja ilintiradi.",
                        'ru': 'Щупальца магнапинны в 15-20 раз длиннее ее мантии и напоминают длинные тонкие нити, '
                              'волочащиеся по абиссальному дну.',
                        'en': 'Magnapinna squids drift above abyssal plains with 8-meter elbowed tentacles trailing '
                              'downwards to snag benthic organisms.'},
        'aliases': ['magnapinna', 'katta qanotli kalmar', 'магнапинна', 'bigfin squid', 'magnapinna squid']},
    {   'id': 'nature_scale_037_deepest_living_octopus',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yava botig'ida qariyb 7000 metr chuqurlikda topilgan 'quloqli' sakkizoyoq qaysi?",
                        'ru': 'Какой осьминог с «ушками»-плавниками обитает на рекордной глубине до 7000 метров в '
                              'Зондском желобе?',
                        'en': "Which 'eared' octopod was observed crawling and hovering at a record depth of nearly "
                              '7,000 meters in the Java Trench?'},
        'options': {   'uz': [   "Dambo sakkizoyog'i (Grimpoteuthis)",
                                 "Ko'k halqali sakkizoyoq",
                                 'Ulkan sakkizoyoq',
                                 'Argonavt'],
                       'ru': [   'Осьминог Дамбо (Гримпотевтис)',
                                 'Синекольчатый осьминог',
                                 'Гигантский осьминог',
                                 'Аргонавт'],
                       'en': ['Dumbo Octopus (Grimpoteuthis)', 'Blue-ringed Octopus', 'Giant Octopus', 'Argonaut']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Dambo sakkizoyog'i (Grimpoteuthis)",
                              'ru': 'Осьминог Дамбо (Гримпотевтис)',
                              'en': 'Dumbo Octopus (Grimpoteuthis)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Grimpoteuthis_dumbo_octopus.jpg/800px-Grimpoteuthis_dumbo_octopus.jpg',
        'fun_fact': {   'uz': "Dambo sakkizoyog'i multfilm filchasi Damoga o'xshash quloqsimon suzgichlarini qoqib, "
                              'abissal zulmatda sekin suzadi.',
                        'ru': 'Осьминог Дамбо машет плавниками, напоминающими уши сказочного слоненка, передвигаясь в '
                              'полной тьме под колоссальным давлением.',
                        'en': 'Grimpoteuthis octopods flap ear-like fin projections to glide gracefully through the '
                              'hadal zone at depths down to 6,957 meters.'},
        'aliases': ['dambo', 'dambo sakkizoyogi', 'дамбо', 'осьминог дамбо', 'dumbo octopus']},
    {   'id': 'nature_scale_038_longest_breath_hold_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Suv ostida bir marta nafas olmasdan eng uzoq tura olish bo'yicha dunyo rekordi (222 "
                              'daqiqa) qaysi hayvonga tegishli?',
                        'ru': 'Какой рекорд задержки дыхания под водой (222 минуты) зафиксирован среди диких '
                              'млекопитающих?',
                        'en': 'What is the longest single breath-hold ever recorded for any wild mammal (222 '
                              'minutes)?'},
        'options': {   'uz': ['Delfin', 'Kyuve kiti (Ziphius cavirostris)', 'Kashalot', 'Morj'],
                       'ru': ['Афалина', 'Клюворыл Кювье', 'Кашалот', 'Морж'],
                       'en': ['Bottlenose Dolphin', "Cuvier's Beaked Whale", 'Sperm Whale', 'Walrus']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Kyuve kiti (Ziphius cavirostris)',
                              'ru': 'Клюворыл Кювье',
                              'en': "Cuvier's Beaked Whale"},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Ziphius_cavirostris_breach.jpg/800px-Ziphius_cavirostris_breach.jpg',
        'fun_fact': {   'uz': '2020-yilda olimlar Kyuve kiti 3 soat 42 daqiqa (222 daqiqa) davomida sirtga chiqmasdan '
                              'chuqurlikda qolganini hujjatlashtirishdi.',
                        'ru': 'Ученые зафиксировали рекордное погружение клюворыла длительностью 3 часа 42 минуты, при '
                              'котором метаболизм животного замедлился до минимума.',
                        'en': "In 2020, Duke University researchers logged a Cuvier's beaked whale dive lasting 3 "
                              'hours and 42 minutes without taking a single breath.'},
        'aliases': ['kyuve kiti', 'клюворыл', 'cuviers beaked whale']},
    {   'id': 'nature_scale_039_deepest_living_crustacean',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Mariana botig'ining eng chuqur nuqtasi — 10 900 metr tubida yashovchi amfipoda "
                              'qisqichbaqasimon jonivor qaysi?',
                        'ru': 'Какой рачок-бокоплав (амфипода) процветает на самом дне Бездны Челленджера на глубине '
                              '10 900 метров?',
                        'en': 'Which amphipod crustacean thrives at the very bottom of Challenger Deep at a depth of '
                              '10,900 meters?'},
        'options': {   'uz': ['Dengiz krabi', 'Krevetka', 'Gigant amfipoda (Hirondellea gigas)', 'Langust'],
                       'ru': [   'Камчатский краб',
                                 'Глубоководная креветка',
                                 'Глубоководная амфипода (Hirondellea gigas)',
                                 'Лангуст'],
                       'en': ['King Crab', 'Deep-sea Shrimp', 'Hadal Amphipod (Hirondellea gigas)', 'Spiny Lobster']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Gigant amfipoda (Hirondellea gigas)',
                              'ru': 'Глубоководная амфипода (Hirondellea gigas)',
                              'en': 'Hadal Amphipod (Hirondellea gigas)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Hirondellea_gigas_amphipod.jpg/800px-Hirondellea_gigas_amphipod.jpg',
        'fun_fact': {   'uz': "Hirondellea gigas o'zining xitin qobig'ini dengiz cho'kindilaridagi alyuminiy ionlari "
                              'yordamida mustahkamlab, ulkan bosim ostida erib ketishdan saqlaydi.',
                        'ru': 'Hirondellea gigas синтезирует гелеобразный слой гидроксида алюминия на панцире, чтобы '
                              'известковый скелет не растворился под давлением 110 МПа.',
                        'en': 'Hirondellea gigas extracts aluminum from hadal sediment to reinforce its exoskeleton '
                              'against carbonate dissolution at 11,000 meters.'},
        'aliases': ['amfipoda', 'hirondellea gigas', 'амфипода', 'hadal amphipod']},
    {   'id': 'nature_scale_040_deepest_living_mollusk',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Okeanning 8000 metrdan ortiq hadal zonasida yashovchi bivalviya (ikki pallali) qaysi '
                              'turkumga kiradi?',
                        'ru': 'Какой двустворчатый моллюск обитает на колоссальных глубинах более 8000 метров в '
                              'желобах ультраабиссали?',
                        'en': 'Which bivalve mollusk genus holds the record for surviving at extreme hadal depths '
                              'exceeding 8,000 meters?'},
        'options': {   'uz': ['Ustritsa', 'Midiya', 'Perlovitsa', 'Vesicomya / Hadimacara'],
                       'ru': ['Устрица', 'Мидия', 'Перловица', 'Весикомии (Vesicomyidae)'],
                       'en': ['Oyster', 'Mussel', 'River Mussel', 'Hadal Clams (Vesicomyidae)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Vesicomya / Hadimacara',
                              'ru': 'Весикомии (Vesicomyidae)',
                              'en': 'Hadal Clams (Vesicomyidae)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Vesicomyidae_clam_hydrothermal_vent.jpg/800px-Vesicomyidae_clam_hydrothermal_vent.jpg',
        'fun_fact': {   'uz': 'Hadal bivalviyalari gidrotermal buloqlar yaqinida xemosintetik bakteriyalar vositasida '
                              'vodorod sulfidini energiyaga aylantirib oziqlanadi.',
                        'ru': 'Глубоководные моллюски живут благодаря эндосимбиотическим хемосинтезирующим бактериям, '
                              'окисляющим метан и сероводород во мраке океана.',
                        'en': 'Hadal vesicomyid clams rely entirely on intracellular sulfur-oxidizing bacteria that '
                              'perform chemosynthesis without sunlight.'},
        'aliases': ['vesicomya', 'hadal clam', 'весикомия', 'vesicomyidae']},
    {   'id': 'nature_scale_041_strongest_bite_force_absolute',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Hozirgi kunda tirik hayvonlar orasida o'lchangan eng yuqori jag' tishlash kuchi qaysi "
                              'hayvonga tegishli (16 460 Nyuton)?',
                        'ru': 'У какого ныне живущего животного зарегистрирована самая мощная абсолютная сила укуса '
                              '(до 16 460 Ньютонов)?',
                        'en': 'Which living animal holds the record for the highest measured absolute bite force (up '
                              'to 16,460 Newtons)?'},
        'options': {   'uz': ['Taroqli timsoh (Dengiz timsohi)', 'Oq akula', 'Giyena', 'Begemot'],
                       'ru': ['Гребнистый крокодил', 'Белая акула', 'Пятнистая гиена', 'Бегемот'],
                       'en': ['Saltwater Crocodile', 'Great White Shark', 'Spotted Hyena', 'Hippopotamus']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Taroqli timsoh (Dengiz timsohi)',
                              'ru': 'Гребнистый крокодил',
                              'en': 'Saltwater Crocodile'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Saltwater_crocodile_jaws_bite.jpg/800px-Saltwater_crocodile_jaws_bite.jpg',
        'fun_fact': {   'uz': "Doktor Gregori Erikson o'tkazgan tajribada 5 metrlik taroqli timsoh datchikni 16 460 N "
                              'kuch bilan qisgan, bu yuk mashinasini ushlab turishga tengdir.',
                        'ru': 'Сила сжатия челюстей гребнистого крокодила достигает 1,6 тонны на квадратный сантиметр, '
                              'что легко крушит кости буйвола и панцири морских черепах.',
                        'en': 'Biologist Gregory Erickson recorded a 16,460-Newton (3,700 lbf) bite from a 5.2-meter '
                              'saltwater crocodile, matching a T. rex in pressure.'},
        'aliases': ['timsoh', 'taroqli timsoh', 'крокодил', 'гребнистый крокодил', 'saltwater crocodile']},
    {   'id': 'nature_scale_042_strongest_bite_mammal_absolute',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Quruqlik sutemizuvchilari orasida eng kuchli jag' bosimiga ega bo'lgan o'txo'r gigant "
                              'qaysi (12 600 Nyuton)?',
                        'ru': 'Какое наземное млекопитающее обладает сильнейшим укусом (около 12 600 Ньютонов)?',
                        'en': 'Which land mammal possesses the most crushing bite force measured (around 12,600 '
                              'Newtons)?'},
        'options': {   'uz': ['Sher', 'Begemot (Gippopotam)', "Grizli ayig'i", 'Yaguar'],
                       'ru': ['Лев', 'Обыкновенный бегемот', 'Медведь гризли', 'Ягуар'],
                       'en': ['Lion', 'Hippopotamus', 'Grizzly Bear', 'Jaguar']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Begemot (Gippopotam)', 'ru': 'Обыкновенный бегемот', 'en': 'Hippopotamus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Hippopotamus_yawn_canines.jpg/800px-Hippopotamus_yawn_canines.jpg',
        'fun_fact': {   'uz': "Begemotning 50 santimetrli o'tkir qoziq tishlari va ulkan jag' mushaklari bir "
                              "tishlashda to'liq qayiqni ikkiga bo'lib yuborishga qodir.",
                        'ru': 'Бегемот способен перекусить пополам взрослого нильского крокодила; его клыки вырастают '
                              'до 50 см и самозатачиваются при трении.',
                        'en': 'A hippopotamus can bite with 12,600 N (2,800 lbf) of force, enough to snap a canoe in '
                              'two or bite an adult crocodile clean in half.'},
        'aliases': ['begemot', 'gippopotam', 'бегемот', 'гиппопотам', 'hippopotamus', 'hippo']},
    {   'id': 'nature_scale_043_strongest_bite_big_cat',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Mushuksimonlar (katta mushuklar) orasida tana hajmiga nisbatan eng kuchli jag'ga ega "
                              "bo'lgan yirtqich qaysi (toshbaqa kosasini teshadi)?",
                        'ru': 'Какая большая кошка обладает самым мощным укусом, способным прокусить череп каймана и '
                              'панцирь броненосца?',
                        'en': 'Which big cat possesses the most powerful bite relative to size, regularly crushing '
                              'turtle shells and caiman skulls?'},
        'options': {   'uz': ['Sher', "Yo'lbars", 'Yaguar', 'Qoplon'],
                       'ru': ['Лев', 'Тигр', 'Ягуар', 'Леопард'],
                       'en': ['Lion', 'Tiger', 'Jaguar', 'Leopard']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Yaguar', 'ru': 'Ягуар', 'en': 'Jaguar'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Jaguar_canines_skull_bite.jpg/800px-Jaguar_canines_skull_bite.jpg',
        'fun_fact': {   'uz': "Yaguar o'ljasini bo'g'ib o'ldirmaydi, balki to'g'ridan-to'g'ri o'ljasining quloqlari "
                              'orasidan bosh suyagini tishlab teshadi.',
                        'ru': 'В отличие от других кошек, ягуар убивает добычу не удушением, а прямым прокусыванием '
                              'височных костей черепа или панциря черепах.',
                        'en': 'Unlike lions and tigers that strangle prey, jaguars pierce temporal bones of the skull '
                              'directly with canines driven by massive jaw adductores.'},
        'aliases': ['yaguar', 'ягуар', 'jaguar']},
    {   'id': 'nature_scale_044_strongest_relative_weight_lifter',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "O'z tana vazniga nisbatan eng ko'p yuk ko'tara oladigan mutlaq jismoniy chempion qaysi "
                              "(o'z vaznidan 1141 baravar ortiq)?",
                        'ru': 'Какое насекомое является сильнейшим существом на планете относительно массы тела '
                              '(поднимает в 1141 раз больше своего веса)?',
                        'en': 'Which insect is the strongest living creature relative to body weight, pulling 1,141 '
                              'times its own mass?'},
        'options': {   'uz': ['Chumoli', 'Qisqichbaqa', "Gerkules qo'ng'izi", "Go'ng qo'ng'izi (Onthophagus taurus)"],
                       'ru': ['Муравей-листорез', 'Рак-богомол', 'Жук-геркулес', 'Жук-навозник (Onthophagus taurus)'],
                       'en': [   'Leafcutter Ant',
                                 'Mantis Shrimp',
                                 'Hercules Beetle',
                                 'Horned Dung Beetle (Onthophagus taurus)']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Go'ng qo'ng'izi (Onthophagus taurus)",
                              'ru': 'Жук-навозник (Onthophagus taurus)',
                              'en': 'Horned Dung Beetle (Onthophagus taurus)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Onthophagus_taurus_male.jpg/800px-Onthophagus_taurus_male.jpg',
        'fun_fact': {   'uz': "Bu qo'ng'izning kuchi 70 kg vaznli odamning 80 tonna (6 ta ikki qavatli London "
                              "avtobusi) yukni ko'tarishi bilan barobardir.",
                        'ru': 'Это эквивалентно тому, как если бы человек весом 70 кг нес на плечах 6 двухэтажных '
                              'автобусов массой 80 тонн.',
                        'en': 'Onthophagus taurus pulling 1,141 times its own weight is equivalent to an average human '
                              'lifting 80 metric tonnes (six double-decker buses).'},
        'aliases': ['gong qongizi', 'onthophagus', 'жук-навозник', 'навозник', 'dung beetle', 'horned dung beetle']},
    {   'id': 'nature_scale_045_strongest_relative_jumper',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "O'z tana uzunligiga nisbatan eng baland va uzoqqa sakrovchi hasharot qaysi (o'z "
                              "bo'yidan 100-150 baravar)?",
                        'ru': 'Какое насекомое совершает самый высокий прыжок относительно размера своего тела (в '
                              '100–150 раз превышая собственный рост)?',
                        'en': 'Which insect achieves the highest jump relative to body length (jumping over 100–150 '
                              'times its own body height)?'},
        'options': {   'uz': ["Burgaga o'xshash ko'pikchi (Froghopper / Pennitsa)", 'Burga', 'Chigirtka', 'Kenguru'],
                       'ru': ['Пенница слюнявая (Слюнявчик)', 'Блоха', 'Кузнечик', 'Кенгуру'],
                       'en': ['Meadow Froghopper (Spittlebug)', 'Flea', 'Grasshopper', 'Kangaroo']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Burgaga o'xshash ko'pikchi (Froghopper / Pennitsa)",
                              'ru': 'Пенница слюнявая (Слюнявчик)',
                              'en': 'Meadow Froghopper (Spittlebug)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Philaenus_spumarius_froghopper.jpg/800px-Philaenus_spumarius_froghopper.jpg',
        'fun_fact': {   'uz': "Ko'pikchi sakraganda 4000 m/s² tezlanish (400 G kuch) hosil qiladi, bu burgalardan 4 "
                              'baravar kuchliroqdir.',
                        'ru': 'Пенница взлетает с ускорением 400 G, катапультируя тело на высоту до 70 см благодаря '
                              'катапультному механизму из эластичного белка резилина.',
                        'en': 'The meadow froghopper accelerates at 4,000 m/s² (400 G), storing energy in resilin '
                              'biomechanical arches to launch 70 cm into the air.'},
        'aliases': ['kopikchi', 'pennitsa', 'пенница', 'пенница слюнявая', 'froghopper', 'spittlebug']},
    {   'id': 'nature_scale_046_highest_acceleration_prey_capture',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "O'ljani tutish paytida eng yuqori burchak tezlanishiga erishuvchi kameleon tilining "
                              'tezlanishi qancha (G-kuchi)?',
                        'ru': 'Какую колоссальную перегрузку (G) развивает кончик языка хамелеона при молниеносном '
                              'выбросе за добычей?',
                        'en': "What peak acceleration (in Gs) does a chameleon's tongue tip reach when catapulting "
                              'toward insect prey?'},
        'options': {   'uz': ['25 G', '264 G', '50 G', '500 G'],
                       'ru': ['25 G', '264 G', '50 G', '500 G'],
                       'en': ['25 G', '264 G', '50 G', '500 G']},
        'correct_index': 1,
        'correct_answer': {'uz': '264 G', 'ru': '264 G', 'en': '264 G'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Chameleon_tongue_strike_macro.jpg/800px-Chameleon_tongue_strike_macro.jpg',
        'fun_fact': {   'uz': "Kichik roze xameleoni (Rhampholeon spinosus) o'z tilini 0.01 soniyada 264 G tezlanish "
                              "bilan otib chiqaradi va uning tili tana uzunligidan 2.5 baravar uzun cho'ziladi.",
                        'ru': 'Язык карликового хамелеона разгоняется от 0 до 97 км/ч за одну сотую секунды, создавая '
                              'перегрузку до 264 G.',
                        'en': 'The rosette pygmy chameleon accelerates its tongue at 264 G (2,590 m/s²), reaching full '
                              'extension in 0.01 seconds powered by collagen elastic recoil.'},
        'aliases': ['264 g', '264', '264g']},
    {   'id': 'nature_scale_047_loudest_animal_sound',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Dengiz ostida eng kuchli tovush (230-236 detsibell) chiqaradigan yirik sutemizuvchi '
                              'qaysi?',
                        'ru': 'Какое животное производит самый громкий звук в океане (до 230–236 децибел)?',
                        'en': 'Which animal produces the loudest acoustic vocalization/clicks in the ocean (up to '
                              '230–236 decibels)?'},
        'options': {   'uz': ["Ko'k kit", 'Bukri kit', 'Kashalot (Sperm Whale)', 'Delfin'],
                       'ru': ['Синий кит', 'Горбатый кит', 'Кашалот', 'Афалина'],
                       'en': ['Blue Whale', 'Humpback Whale', 'Sperm Whale', 'Bottlenose Dolphin']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Kashalot (Sperm Whale)', 'ru': 'Кашалот', 'en': 'Sperm Whale'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Physeter_macrocephalus_sperm_whale.jpg/800px-Physeter_macrocephalus_sperm_whale.jpg',
        'fun_fact': {   'uz': "Kashalotning spermaset a'zosi orqali chiqariladigan exolokatsiya chertishlari 236 dB ga "
                              'yetadi va suv ostida yuzlab kilometrga tarqaladi.',
                        'ru': 'Эхолокационные щелчки спермацетового органа кашалота достигают 236 дБ, будучи способны '
                              'оглушить рыбу и акул на близком расстоянии.',
                        'en': 'Sperm whale echolocation clicks register up to 236 dB re 1 μPa, focusing sonic energy '
                              'through massive spermaceti and junk oil organs.'},
        'aliases': ['kashalot', 'кашалот', 'sperm whale']},
    {   'id': 'nature_scale_048_loudest_relative_shrimp',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Qisqichini qarsillatganda 218 dB tovush va 4700 °C qizigan plazma hosil qiluvchi '
                              'mittigina jonivor qaysi?',
                        'ru': 'Какая крошечная креветка при щелчке клешней создает акустический импульс в 218 дБ и '
                              'вспышку с температурой 4700 °C?',
                        'en': 'Which tiny crustacean produces a 218-dB acoustic blast and a 4,700 °C plasma cavitation '
                              'bubble by snapping its claw?'},
        'options': {   'uz': [   'Krill',
                                 'Mantis krevetka',
                                 'Dengiz qisqichbaqasi',
                                 'Pistolet-krevetka (Snapping Shrimp)'],
                       'ru': ['Криль', 'Рак-богомол', 'Омар', 'Креветка-пистолет (Раки-щелкуны)'],
                       'en': ['Krill', 'Mantis Shrimp', 'Lobster', 'Snapping Shrimp (Pistol Shrimp)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Pistolet-krevetka (Snapping Shrimp)',
                              'ru': 'Креветка-пистолет (Раки-щелкуны)',
                              'en': 'Snapping Shrimp (Pistol Shrimp)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Alpheus_pistol_snapping_shrimp.jpg/800px-Alpheus_pistol_snapping_shrimp.jpg',
        'fun_fact': {   'uz': 'Alpheus turkumiga kiruvchi pistolet-krevetka qisqichini 100 km/soat tezlikda yopadi; '
                              "hosil bo'lgan kavitatsiya pufakchasi portlaganda sonoluminessensiya yorug'lik chaqnashi "
                              'yuz beradi.',
                        'ru': 'При схлопывании кавитационного пузыря креветки-пистолета температура внутри на '
                              'микросекунду превышает температуру поверхности Солнца.',
                        'en': 'Snapping shrimp snap their enlarged claw at 100 km/h, generating acoustic cavitation '
                              'bubbles that collapse with sonoluminescence and shockwaves.'},
        'aliases': ['pistolet krevetka', 'креветка пистолет', 'креветка-пистолет', 'pistol shrimp', 'snapping shrimp']},
    {   'id': 'nature_scale_049_deadliest_venom_land_snake',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Quruqlik ilonlari orasida zahari eng kuchli bo'lgan tur qaysi (bir chaqishi 100 nafar "
                              "odamni o'ldirishga yetadi)?",
                        'ru': 'Какая сухопутная змея обладает самым токсичным ядом в мире (одна доза способна убить '
                              '100 человек)?',
                        'en': 'Which land snake possesses the most toxic venom on Earth (one bite contains enough '
                              'neurotoxin to kill 100 humans)?'},
        'options': {   'uz': [   'Ichki taypan (Inland Taipan / Oxyuranus microlepidotus)',
                                 'Qora mamba',
                                 'Qirol kobra',
                                 'Qora ilon'],
                       'ru': [   'Внутриматериковый тайпан (Грозная змея)',
                                 'Черная мамба',
                                 'Королевская кобра',
                                 'Песчаная эфа'],
                       'en': ['Inland Taipan', 'Black Mamba', 'King Cobra', 'Saw-scaled Viper']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Ichki taypan (Inland Taipan / Oxyuranus microlepidotus)',
                              'ru': 'Внутриматериковый тайпан (Грозная змея)',
                              'en': 'Inland Taipan'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Oxyuranus_microlepidotus_inland_taipan.jpg/800px-Oxyuranus_microlepidotus_inland_taipan.jpg',
        'fun_fact': {   'uz': "Ichki taypanning LD50 ko'rsatkichi atigi 0.025 mg/kg ni tashkil etadi, bu uning "
                              'zaharini kobra zaharidan 50 baravar kuchliroq qiladi.',
                        'ru': 'Одного укуса внутриматерикового тайпана с летальной дозой LD50 = 0,025 мг/кг достаточно '
                              'для гибели 100 человек или 250 000 мышей.',
                        'en': "The inland taipan's venom has a murine LD50 of 0.025 mg/kg; a single 110-mg yield can "
                              'theoretically kill 100 adult men.'},
        'aliases': ['taypan', 'ichki taypan', 'тайпан', 'внутриматериковый тайпан', 'inland taipan']},
    {   'id': 'nature_scale_050_deadliest_marine_creature',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Dunyodagi eng zaharli dengiz jonzoti hisoblangan va zahari 2-3 daqiqada yurakni '
                              "to'xtatuvchi meduza qaysi?",
                        'ru': 'Какое морское животное считается самым ядовитым в мире (его яд убивает человека за 2–3 '
                              'минуты)?',
                        'en': 'Which marine creature is recognized as having the most lethal venom in the ocean, '
                              'killing an adult within 2–3 minutes?'},
        'options': {   'uz': [   'Moviy halqali sakkizoyoq',
                                 'Avstraliya dengiz arisi (Box Jellyfish / Chironex fleckeri)',
                                 'Konus shilliqurti',
                                 'Borodavchatka (Stonefish)'],
                       'ru': [   'Синекольчатый осьминог',
                                 'Морская оса (Австралийская кубомедуза)',
                                 'Географический конус',
                                 'Рыба-камень'],
                       'en': [   'Blue-ringed Octopus',
                                 'Sea Wasp Box Jellyfish (Chironex fleckeri)',
                                 'Geography Cone',
                                 'Reef Stonefish']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Avstraliya dengiz arisi (Box Jellyfish / Chironex fleckeri)',
                              'ru': 'Морская оса (Австралийская кубомедуза)',
                              'en': 'Sea Wasp Box Jellyfish (Chironex fleckeri)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Chironex_fleckeri_box_jellyfish.jpg/800px-Chironex_fleckeri_box_jellyfish.jpg',
        'fun_fact': {   'uz': "Dengiz arisining 60 tagacha bo'lgan 3 metrlik paypaslagichlarida millionlab "
                              "nematosistalar bo'lib, ularning zahari hujayra membranalarida teshik ochib yurakni "
                              'falaj qiladi.',
                        'ru': 'Одна особь Chironex fleckeri содержит достаточно кардиотоксина, чтобы убить 60 взрослых '
                              'людей за несколько минут.',
                        'en': 'Chironex fleckeri carries enough pore-forming cardiotoxin in its 3-meter tentacles to '
                              'cause hyperkalemia and cardiac arrest in 60 people within minutes.'},
        'aliases': ['dengiz arisi', 'morskaya osa', 'морская оса', 'кубомедуза', 'box jellyfish', 'sea wasp']},
    {   'id': 'nature_scale_051_most_sleep_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Kuniga 20–22 soatgacha uxlab, sutemizuvchilar orasida uyqu davomiyligi bo'yicha rekord "
                              "o'rnatgan jonivor qaysi?",
                        'ru': 'Какое млекопитающее спит больше всех животных в мире (до 20–22 часов в сутки)?',
                        'en': 'Which mammal holds the record for the longest daily sleep duration, sleeping 20 to 22 '
                              'hours per day?'},
        'options': {   'uz': ['Dangasa (Sloth)', 'Sher', 'Koala', 'Mushuk'],
                       'ru': ['Ленивец', 'Лев', 'Коала', 'Кошка'],
                       'en': ['Sloth', 'Lion', 'Koala', 'Domestic Cat']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Koala', 'ru': 'Коала', 'en': 'Koala'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Koala_sleeping_eucalyptus_branch.jpg/800px-Koala_sleeping_eucalyptus_branch.jpg',
        'fun_fact': {   'uz': "Koala iste'mol qiladigan eukalipt barglarida kaloriya juda kam va zaharli moddalar "
                              "bo'lgani sababli, energiyani tejash uchun u kunning 90% qismini uyquda o'tkazadi.",
                        'ru': 'Эвкалиптовые листья малокалорийны и токсичны, поэтому для их детоксикации и сохранения '
                              'сил коала проводит во сне до 22 часов в сутки.',
                        'en': 'Because eucalyptus leaves are nutrient-poor and packed with toxins, koalas conserve '
                              'metabolic energy by sleeping up to 22 hours daily.'},
        'aliases': ['koala', 'коала', 'koala']},
    {   'id': 'nature_scale_052_least_sleep_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Sutemizuvchilar orasida sutkasiga eng kam (atigi 30 daqiqadan 2 soatgacha) uxlaydigan '
                              'hayvon qaysi?',
                        'ru': 'Какое млекопитающее спит меньше всех в дикой природе (всего от 30 минут до 2 часов в '
                              'сутки)?',
                        'en': 'Which land mammal requires the least total sleep, sleeping only 30 minutes to 2 hours '
                              'per day?'},
        'options': {   'uz': ['Ot', 'Fil', 'Tuyokli kiyik', 'Jirafa'],
                       'ru': ['Лошадь', 'Слон', 'Антилопа гну', 'Жираф'],
                       'en': ['Horse', 'Elephant', 'Wildebeest', 'Giraffe']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Jirafa', 'ru': 'Жираф', 'en': 'Giraffe'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Giraffe_resting_standing.jpg/800px-Giraffe_resting_standing.jpg',
        'fun_fact': {   'uz': "Jirafalar yirtqichlar hujumidan ehtiyot bo'lish uchun asosan tik turgan holda, 5-10 "
                              'daqiqalik qisqa muddatlarda uxlaydi.',
                        'ru': 'Из-за уязвимости перед львами жирафы спят короткими сессиями по 5 минут, стоя на ногах, '
                              'суммарно около получаса в день.',
                        'en': 'Due to predation pressure, adult giraffes sleep standing up in 5-minute naps totaling '
                              'roughly 30 minutes to 2 hours in a 24-hour cycle.'},
        'aliases': ['jirafa', 'жираф', 'giraffe']},
    {   'id': 'nature_scale_053_largest_wingspan_bird',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Hozirgi tirik qushlar orasida eng katta qanot qulochiga ega bo'lgan chempion qaysi "
                              '(3.5–3.7 metr)?',
                        'ru': 'Какая птица обладает самым большим размахом крыльев среди всех ныне живущих пернатых '
                              '(до 3,5–3,7 метра)?',
                        'en': 'Which living bird possesses the largest wingspan in the world today (measuring up to '
                              '3.5–3.7 meters)?'},
        'options': {   'uz': [   'Sayohatchi albatros (Wandering Albatross)',
                                 'And kondori',
                                 'Jingalak pelikan',
                                 'Qoraburgut'],
                       'ru': ['Странствующий альбатрос', 'Андский кондор', 'Кудрявый пеликан', 'Черный гриф'],
                       'en': ['Wandering Albatross', 'Andean Condor', 'Dalmatian Pelican', 'Cinereous Vulture']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Sayohatchi albatros (Wandering Albatross)',
                              'ru': 'Странствующий альбатрос',
                              'en': 'Wandering Albatross'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Diomedea_exulans_wandering_albatross_wingspan.jpg/800px-Diomedea_exulans_wandering_albatross_wingspan.jpg',
        'fun_fact': {   'uz': 'Sayohatchi albatros qanotlarini maxsus qulflanuvchi paylar yordamida '
                              'harakatlantirmasdan, dinamik parvoz usulida Janubiy okean ustida minglab kilometr qanot '
                              'qoqmasdan ucha oladi.',
                        'ru': 'Специальный связочный замок фиксирует крылья странствующего альбатроса в расправленном '
                              'виде без мышечных усилий при планировании над волнами.',
                        'en': 'The wandering albatross locks its 3.6-meter wings via shoulder tendon locks, '
                              'dynamic-soaring across Antarctic oceans with virtually no muscle effort.'},
        'aliases': [   'sayohatchi albatros',
                       'albatros',
                       'странствующий альбатрос',
                       'альбатрос',
                       'wandering albatross',
                       'albatross']},
    {   'id': 'nature_scale_054_longest_migration_distance',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yer yuzidagi eng uzun yillik migratsiya rekordchisi bo'lgan va Arktikadan Antarktidaga "
                              'uchib borib qaytuvchi qush qaysi (yiliga 70 000–90 000 km)?',
                        'ru': 'Какая птица совершает самую длинную ежегодную миграцию в мире от Арктики до Антарктики '
                              'и обратно (70 000–90 000 км в год)?',
                        'en': 'Which bird completes the longest annual migration of any animal, travelling from the '
                              'Arctic to Antarctica and back (70,000–90,000 km/yr)?'},
        'options': {   'uz': ["Bo'ronqush", 'Qutb baliqchisi (Qutb krachkasi / Arctic Tern)', 'Turna', 'Lochin'],
                       'ru': ['Буревестник', 'Полярная крачка', 'Серый журавль', 'Сапсан'],
                       'en': ['Sooty Shearwater', 'Arctic Tern', 'Common Crane', 'Peregrine Falcon']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Qutb baliqchisi (Qutb krachkasi / Arctic Tern)',
                              'ru': 'Полярная крачка',
                              'en': 'Arctic Tern'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sterna_paradisaea_arctic_tern_flight.jpg/800px-Sterna_paradisaea_arctic_tern_flight.jpg',
        'fun_fact': {   'uz': "Qutb krachkasi hayoti davomida Yer bilan Oy orasidagi masofani uch marta bosib o'tishga "
                              "teng masofani (2.4 million km) uchib o'tadi va yer yuzida boshqa har qanday jonzotdan "
                              "ko'ra ko'proq kunduzgi quyosh nurini ko'radi.",
                        'ru': 'Полярная крачка видит больше дневного света, чем любое другое существо на Земле, '
                              'проводя два лета в год — арктическое и антарктическое.',
                        'en': 'The Arctic tern experiences two summers per year, logging up to 90,000 km annually and '
                              'flying the equivalent of 3 round trips to the Moon over its 30-year life.'},
        'aliases': ['qutb krachkasi', 'krachka', 'полярная крачка', 'крачка', 'arctic tern']},
    {   'id': 'nature_scale_055_longest_nonstop_flight',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Biror marta ham to'xtamasdan va qo'nmasdan Tinch okeani uzra eng uzun to'xtovsiz "
                              'parvozni (13 560 km, 11 kun) amalga oshirgan qush qaysi?',
                        'ru': 'Какая перелетная птица совершила рекордный беспосадочный перелет через Тихий океан (13 '
                              '560 км за 11 дней без отдыха)?',
                        'en': 'Which migratory shorebird completed the longest documented non-stop flight in history '
                              '(13,560 km in 11 days without landing)?'},
        'options': {   'uz': ['Qorayaloq', 'Burgut', 'Kichik veretenik (Bar-tailed Godwit)', "G'oz"],
                       'ru': ['Ржанка', 'Орел', 'Малый веретенник', 'Канадская казарка'],
                       'en': ['Pacific Golden Plover', 'Golden Eagle', 'Bar-tailed Godwit', 'Canada Goose']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Kichik veretenik (Bar-tailed Godwit)',
                              'ru': 'Малый веретенник',
                              'en': 'Bar-tailed Godwit'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Limosa_lapponica_bar_tailed_godwit.jpg/800px-Limosa_lapponica_bar_tailed_godwit.jpg',
        'fun_fact': {   'uz': "Alyaskadan Yangi Zelandiyaga uchib o'tish oldidan bu qush o'z ichki a'zolarining "
                              "yarmini kichraytirib, tanasining 55% ini yog' zaxirasi bilan to'ldiradi.",
                        'ru': 'Перед рекордным перелетом веретенник атрофирует часть пищеварительного тракта, '
                              'превращая половину массы тела в высококалорийный жир.',
                        'en': 'Bar-tailed godwit 4BBRW flew 13,560 km non-stop from Alaska to Tasmania in 264 hours, '
                              'shrinking its digestive organs to maximize fat payload.'},
        'aliases': ['veretenik', 'малый веретенник', 'веретенник', 'bar-tailed godwit', 'godwit']},
    {   'id': 'nature_scale_056_highest_flying_bird',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Everest cho'qqisidan ham balandroqda — 11 300 metr balandlikda samolyot bilan "
                              "to'qnashgan eng baland uchuvchi qush qaysi?",
                        'ru': 'Какая птица является рекордсменом по высоте полета (зафиксировано столкновение с '
                              'самолетом на высоте 11 300 метров)?',
                        'en': 'Which bird holds the altitude record for avian flight, confirmed after colliding with a '
                              'commercial jetliner at 11,300 meters (37,000 ft)?'},
        'options': {   'uz': [   "Tog' g'ozi (Bar-headed Goose)",
                                 'Oqqush',
                                 'Kondor',
                                 "Ryuppel tasqarasi (Rüppell's Vulture)"],
                       'ru': ['Горный гусь', 'Лебедь-кликун', 'Кондор', 'Сип Рюппеля (Африканский гриф)'],
                       'en': ['Bar-headed Goose', 'Whooper Swan', 'Andean Condor', "Rüppell's Vulture"]},
        'correct_index': 3,
        'correct_answer': {   'uz': "Ryuppel tasqarasi (Rüppell's Vulture)",
                              'ru': 'Сип Рюппеля (Африканский гриф)',
                              'en': "Rüppell's Vulture"},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Gyps_rueppellii_flying.jpg/800px-Gyps_rueppellii_flying.jpg',
        'fun_fact': {   'uz': "Ryuppel tasqarasining qonidagi maxsus gemoglobin moddasi stratosferadagi o'ta past "
                              "kislorod va -50 °C qahratonda ham kislorodni samarali bog'lay oladi.",
                        'ru': 'Кровь сипа Рюппеля содержит особый мутантный гемоглобин, способный насыщаться '
                              'кислородом в разреженном воздухе на высоте полета лайнеров.',
                        'en': "Rüppell's vulture possesses genetically modified hemoglobin alpha subunits with "
                              'exceptional oxygen affinity, functioning at 37,000 feet.'},
        'aliases': ['ryuppel tasqarasi', 'tasqara', 'сип рюппеля', 'гриф', 'ruppells vulture']},
    {   'id': 'nature_scale_057_highest_heart_rate_vertebrate',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Tinch holatda yuragi daqiqasiga 1200–1260 marta uruvchi eng yuqori pulsga ega jonzot '
                              'qaysi?',
                        'ru': 'У какого животного самое частое сердцебиение в состоянии покоя (до 1200–1260 ударов в '
                              'минуту)?',
                        'en': 'Which animal possesses the highest recorded resting heart rate, beating up to '
                              '1,200–1,260 times per minute?'},
        'options': {   'uz': ["Kolibri (Ko'k tomoqli kolibri)", 'Etrusk yerqazari', 'Sichqon', 'Kanareyka'],
                       'ru': ['Колибри', 'Карликовая многозубка', 'Домовая мышь', 'Канарейка'],
                       'en': ['Hummingbird', 'Etruscan Shrew', 'House Mouse', 'Canary']},
        'correct_index': 0,
        'correct_answer': {'uz': "Kolibri (Ko'k tomoqli kolibri)", 'ru': 'Колибри', 'en': 'Hummingbird'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Hummingbird_hovering_macro.jpg/800px-Hummingbird_hovering_macro.jpg',
        'fun_fact': {   'uz': 'Kolibri parvoz paytida soniyasiga 80 marta qanot qoqadi va uning yuragi 1260 marta '
                              'uradi; kechasi esa u karaxtlik (torpor) holatiga tushib pulsini 50 martagacha '
                              'tushiradi.',
                        'ru': 'Сердце колибри в полете делает до 21 удара в секунду, а ночью птица впадает в '
                              'анабиоз-торпор, замедляя пульс до 50 ударов для экономии сил.',
                        'en': 'Hummingbird hearts contract at 1,260 bpm during hovering flight, dropping into '
                              'nocturnal torpor to conserve calories when ambient temperatures fall.'},
        'aliases': ['kolibri', 'колибри', 'hummingbird']},
    {   'id': 'nature_scale_058_lowest_heart_rate_vertebrate',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Sho'ng'ish paytida yurak urishi daqiqasiga atigi 2 martagacha tushadigan ulkan jonivor "
                              'qaysi?',
                        'ru': 'У какого гиганта зафиксирована самая низкая частота пульса при нырянии (всего 2 удара в '
                              'минуту)?',
                        'en': 'Which creature has the lowest recorded active diving heart rate, slowing down to just 2 '
                              'beats per minute?'},
        'options': {   'uz': ['Fil', "Ko'k kit", 'Toshbaqa', 'Timsoh'],
                       'ru': ['Слон', 'Синий кит', 'Галапагосская черепаха', 'Крокодил'],
                       'en': ['African Elephant', 'Blue Whale', 'Giant Tortoise', 'Crocodile']},
        'correct_index': 1,
        'correct_answer': {'uz': "Ko'k kit", 'ru': 'Синий кит', 'en': 'Blue Whale'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Blue_whale_underwater_pulse.jpg/800px-Blue_whale_underwater_pulse.jpg',
        'fun_fact': {   'uz': "Stenford universiteti biologlari ko'k kitga datchik o'rnatganda, u chuqur suv ostida "
                              'yuragini daqiqasiga 2 martagacha sekinlashtirganini aniqlashdi.',
                        'ru': 'Датчики ЭКГ, прикрепленные к синему киту, показали брадикардию до 2 ударов в минуту при '
                              'глубоких погружениях за крилем.',
                        'en': 'Biologging ECG tags on blue whales recorded bradycardia drops down to 2 bpm during deep '
                              'foraging dives, conserving oxygen for essential brain function.'},
        'aliases': ['kok kit', 'синий кит', 'blue whale']},
    {   'id': 'nature_scale_059_fastest_reproduction_rate',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Nazariy jihatdan bir mavsumda bitta urg'ochisi 600 milliarddan ortiq avlod qoldira "
                              'oladigan hasharot qaysi?',
                        'ru': 'Какое насекомое способно за один сезон теоретически дать потомство более чем в 600 '
                              'миллиардов особей?',
                        'en': 'Which insect possesses such extreme parthenogenetic fecundity that a single female '
                              'could theoretically yield 600 billion descendants in one season?'},
        'options': {   'uz': ['Chivin', 'Chigirtka', "O'simlik biti (Tlya / Aphid)", 'Asalari'],
                       'ru': ['Комар', 'Саранча', 'Тля', 'Медоносная пчела'],
                       'en': ['Mosquito', 'Locust', 'Aphid', 'Honeybee']},
        'correct_index': 2,
        'correct_answer': {'uz': "O'simlik biti (Tlya / Aphid)", 'ru': 'Тля', 'en': 'Aphid'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Aphid_parthenogenesis_macro.jpg/800px-Aphid_parthenogenesis_macro.jpg',
        'fun_fact': {   'uz': "Tlyalar partenogenez yo'li bilan erkaklarsiz ko'paya oladi; tug'ilgan urg'ochi tlya "
                              "tanasida allaqachon keyingi avlod embrionlari rivojlanayotgan bo'ladi ('teleskopik "
                              "avlodlar').",
                        'ru': 'Самка тли рождает живых клонированных самок, которые уже беременны следующим поколением '
                              'еще до своего рождения.',
                        'en': 'Aphids exhibit telescoping generations: virgin females give birth to live nymphs that '
                              'already contain developing embryos inside their own bodies.'},
        'aliases': ['tlya', 'osimlik biti', 'тля', 'aphid']},
    {   'id': 'nature_scale_060_longest_gestation_period',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Sutemizuvchilar orasida homiladorlik davri eng uzoq (22 oy / qariyb 2 yil) davom '
                              'etadigan jonivor qaysi?',
                        'ru': 'У какого млекопитающего самая длительная беременность в мире (около 22 месяцев)?',
                        'en': 'Which mammal has the longest gestation period of any living terrestrial animal (lasting '
                              'up to 22 months)?'},
        'options': {   'uz': ['Karkidon', 'Zebra', 'Begemot', 'Fil (Afrika va Osiyo fili)'],
                       'ru': ['Носорог', 'Зебра', 'Бегемот', 'Слон (Африканский и Азиатский)'],
                       'en': ['Rhinoceros', 'Zebra', 'Hippopotamus', 'Elephant']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Fil (Afrika va Osiyo fili)',
                              'ru': 'Слон (Африканский и Азиатский)',
                              'en': 'Elephant'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/African_Elephant_mother_calf.jpg/800px-African_Elephant_mother_calf.jpg',
        'fun_fact': {   'uz': "Fil bolasi ona qornida 660 kun (qariyb 2 yil) rivojlanadi va tug'ilganda uning vazni "
                              '100-120 kg ni tashkil qiladi.',
                        'ru': 'Беременность слонихи длится почти два года (до 680 дней), что необходимо для '
                              'сложнейшего формирования массивного мозга слоненка.',
                        'en': 'Elephants carry developing fetuses for nearly 22 months (up to 680 days), required to '
                              "develop the calf's advanced brain and neural network."},
        'aliases': ['fil', 'слон', 'elephant']},
    {   'id': 'nature_scale_061_fastest_canine',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Qaysi it zoti yugurish tezligi bo'yicha eng yuqori rekordga ega (72 km/soat)?",
                        'ru': 'Какая порода собак развивает максимальную скорость бега (до 72 км/ч)?',
                        'en': 'Which dog breed is the fastest runner in the canine world (up to 72 km/h)?'},
        'options': {   'uz': ['Greyxaund (Greyhound)', 'Husky', 'Nemis ovcharkasi', 'Buldog'],
                       'ru': ['Грейхаунд', 'Хаски', 'Немецкая овчарка', 'Бульдог'],
                       'en': ['Greyhound', 'Siberian Husky', 'German Shepherd', 'Bulldog']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Greyxaund (Greyhound)', 'ru': 'Грейхаунд', 'en': 'Greyhound'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Greyhound_racing_sprint.jpg/800px-Greyhound_racing_sprint.jpg',
        'fun_fact': {   'uz': "Greyxaund egiluvchan umurtqa pog'onasi va ulkan yuragi tufayli 6 qadamda 70 km/soat "
                              'tezlikka erishadi.',
                        'ru': 'Грейхаунд развивает скорость до 72 км/ч благодаря двойному подвесному галопу и '
                              'массивному сердцу.',
                        'en': 'The greyhound reaches top sprint speed in six strides using a double-suspension rotary '
                              'gallop.'},
        'aliases': ['greyxaund', 'грейхаунд', 'greyhound']},
    {   'id': 'nature_scale_062_fastest_marine_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Okeandagi eng tez suzuvchi sutemizuvchi jonivor qaysi (56 km/soat)?',
                        'ru': 'Какое морское млекопитающее является самым быстрым пловцом (до 56 км/ч)?',
                        'en': 'Which marine mammal is the fastest swimmer in the oceans (reaching up to 56 km/h)?'},
        'options': {   'uz': ['Moviy kit', 'Kosatka (Qotil kit)', 'Beluxa', 'Morj'],
                       'ru': ['Синий кит', 'Косатка', 'Белуха', 'Морж'],
                       'en': ['Blue Whale', 'Killer Whale (Orca)', 'Beluga', 'Walrus']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Kosatka (Qotil kit)', 'ru': 'Косатка', 'en': 'Killer Whale (Orca)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Orca_jumping_speed.jpg/800px-Orca_jumping_speed.jpg',
        'fun_fact': {   'uz': "Kosatkalar ulkan gidrodinamik dumi bilan kuchli zarba berib 56 km/soat tezlikda to'dani "
                              'quvib yetadi.',
                        'ru': 'Косатки весом до 8 тонн способны развивать скорость 56 км/ч при совместной охоте.',
                        'en': 'Orcas weigh up to 8 tonnes yet cruise at burst speeds of 56 km/h (35 mph) while '
                              'hydroplaning near the surface.'},
        'aliases': ['kosatka', 'orca', 'косатка', 'killer whale']},
    {   'id': 'nature_scale_063_largest_amphibian',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dunyodagi eng katta va eng og'ir amfibiya qaysi (uzunligi 1.8 metr, 50 kg)?",
                        'ru': 'Какая амфибия является самой крупной в мире (длина до 1,8 м, вес до 50 кг)?',
                        'en': 'Which creature is the largest and heaviest amphibian in the world (up to 1.8 m, 50 '
                              'kg)?'},
        'options': {   'uz': ['Aksolotl', 'Goliath qurbaqasi', 'Xitoy ulkan salamandrasi', 'Oddiy triton'],
                       'ru': ['Аксалотль', 'Лягушка-голиаф', 'Китайская исполинская саламандра', 'Обыкновенный тритон'],
                       'en': ['Axolotl', 'Goliath Frog', 'Chinese Giant Salamander', 'Smooth Newt']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Xitoy ulkan salamandrasi',
                              'ru': 'Китайская исполинская саламандра',
                              'en': 'Chinese Giant Salamander'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Andrias_davidianus_giant_salamander.jpg/800px-Andrias_davidianus_giant_salamander.jpg',
        'fun_fact': {   'uz': "Bu qadimgi amfibiya daryo tubida yashaydi va o'pkalari kichik bo'lgani sababli "
                              "kislorodni g'adir-budur terisi orqali yutadi.",
                        'ru': 'Китайская исполинская саламандра дышит почти исключительно через складчатую кожу в '
                              'холодных горных реках.',
                        'en': 'Andrias davidianus can grow to 1.8 meters, respiring directly through wrinkled skin in '
                              'clear mountain streams.'},
        'aliases': ['xitoy salamandrasi', 'salamandra', 'исполинская саламандра', 'chinese giant salamander']},
    {   'id': 'nature_scale_064_largest_frog',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dunyodagi eng katta qurbaqa qaysi (bo'yi 32 sm, og'irligi 3.3 kg)?",
                        'ru': 'Какая лягушка является самой крупной на планете (длина до 32 см, вес до 3,3 кг)?',
                        'en': 'Which frog holds the title of the largest living anuran frog in the world (up to 3.3 '
                              'kg)?'},
        'options': {   'uz': [   "Qizilko'z qurbaqa",
                                 'Buqa qurbaqa',
                                 'Zaharli drevolaz',
                                 'Goliat qurbaqasi (Goliath frog)'],
                       'ru': ['Красноглазая квакша', 'Лягушка-бык', 'Древолаз', 'Лягушка-голиаф'],
                       'en': ['Red-eyed Tree Frog', 'Bullfrog', 'Poison Dart Frog', 'Goliath Frog']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Goliat qurbaqasi (Goliath frog)', 'ru': 'Лягушка-голиаф', 'en': 'Goliath Frog'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Conraua_goliath_frog.jpg/800px-Conraua_goliath_frog.jpg',
        'fun_fact': {   'uz': 'Goliat qurbaqasi bir sakrashda 3 metrgacha masofaga ucha oladi, ammo uning ovoz '
                              "chiqaruvchi rezonator qopchalari bo'lmaydi.",
                        'ru': 'Лягушка-голиаф способна совершать прыжки на 3 метра в длину, но полностью нема из-за '
                              'отсутствия голосового мешка.',
                        'en': 'Conraua goliath reaches 3.3 kg; despite its immense size, it lacks a vocal sac and '
                              'produces no mating call.'},
        'aliases': ['goliat', 'goliat qurbagasi', 'голиаф', 'лягушка-голиаф', 'goliath frog']},
    {   'id': 'nature_scale_065_largest_invertebrate_wingspan',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Qanot qulochi bo'yicha dunyodagi eng katta kapalak qaysi (30 santimetrgacha)?",
                        'ru': 'Какая бабочка имеет самый большой размах крыльев в мире (до 30 см)?',
                        'en': 'Which moth holds the record for the largest wingspan in the insect world (measuring up '
                              'to 30 cm)?'},
        'options': {   'uz': ['Oq jodugar kapalagi (Thysania agrippina)', 'Monarx', 'Atlas kapalagi', "Tovusko'z"],
                       'ru': ['Тизания Агриппина (Белая колдунья)', 'Монарх', 'Павлиноглазка Атлас', 'Махаон'],
                       'en': ['White Witch Moth (Thysania agrippina)', 'Monarch', 'Atlas Moth', 'Swallowtail']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Oq jodugar kapalagi (Thysania agrippina)',
                              'ru': 'Тизания Агриппина (Белая колдунья)',
                              'en': 'White Witch Moth (Thysania agrippina)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Thysania_agrippina_white_witch.jpg/800px-Thysania_agrippina_white_witch.jpg',
        'fun_fact': {   'uz': "Oq jodugarning qanotlari 30 sm gacha yetib, havoda qushdek ko'rinadi.",
                        'ru': 'Размах крыльев тизании агриппины достигает 30 сантиметров, что делает её '
                              'непревзойденным гигантом ночного неба.',
                        'en': 'Thysania agrippina boasts a wingspan up to 30 cm (12 inches), navigating Central and '
                              'South American forest canopies like a bat.'},
        'aliases': ['oq jodugar', 'тизания', 'тизания агриппина', 'white witch moth', 'thysania agrippina']},
    {   'id': 'nature_scale_066_largest_spider_mass',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Og'irligi bo'yicha dunyodagi eng og'ir o'rgimchak qaysi (175 grammgacha)?",
                        'ru': 'Какой паук является самым тяжелым в мире по массе тела (до 175 граммов)?',
                        'en': 'Which spider is recognized as the heaviest spider in the world by body mass (up to 175 '
                              'grams)?'},
        'options': {   'uz': ['Qora beva', "Goliat qushxo'ri (Theraphosa blondi)", 'Krestovik', "Banan o'rgimchagi"],
                       'ru': ['Черная вдова', 'Птицеед-голиаф (Терафоза Блонда)', 'Крестовик', 'Банановый паук'],
                       'en': ['Black Widow', 'Goliath Birdeater (Theraphosa blondi)', 'Orb Weaver', 'Banana Spider']},
        'correct_index': 1,
        'correct_answer': {   'uz': "Goliat qushxo'ri (Theraphosa blondi)",
                              'ru': 'Птицеед-голиаф (Терафоза Блонда)',
                              'en': 'Goliath Birdeater (Theraphosa blondi)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Theraphosa_blondi_goliath_birdeater.jpg/800px-Theraphosa_blondi_goliath_birdeater.jpg',
        'fun_fact': {   'uz': "Goliat qushxo'rining oyoq qulochi 30 sm ga, zaharli tirnoqlari esa 3.8 sm ga yetadi.",
                        'ru': 'Масса птицееда-голиафа сопоставима со щенком, а его клыки способны прокусить череп '
                              'змеи.',
                        'en': 'Theraphosa blondi weighs up to 175 grams with 3.8-cm venomous fangs, feeding primarily '
                              'on frogs, lizards, and small snakes.'},
        'aliases': ['goliat qushxori', 'tarantul', 'птицеед-голиаф', 'птицеед', 'goliath birdeater']},
    {   'id': 'nature_scale_067_longest_snake_length',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Tarixda rasman o'lchangan eng uzun ilon turi qaysi (uzunligi 7-9 metrgacha)?",
                        'ru': 'Какая змея признана самой длинной в мире по официальным измерениям (до 7–9 метров)?',
                        'en': 'Which snake is recognized as the longest in the world by official measurements '
                              '(reaching 7–9 meters)?'},
        'options': {   'uz': ['Yashil anakonda', 'Kobra', "To'rsimon piton (Reticulated Python)", 'Qora mamba'],
                       'ru': ['Зеленая анаконда', 'Королевская кобра', 'Сетчатый питон', 'Черная мамба'],
                       'en': ['Green Anaconda', 'King Cobra', 'Reticulated Python', 'Black Mamba']},
        'correct_index': 2,
        'correct_answer': {   'uz': "To'rsimon piton (Reticulated Python)",
                              'ru': 'Сетчатый питон',
                              'en': 'Reticulated Python'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Malayopython_reticulatus_python.jpg/800px-Malayopython_reticulatus_python.jpg',
        'fun_fact': {   'uz': "To'rsimon piton Ginnes rekordiga ko'ra 9 metrdan oshgan; anakonda esa og'irligi "
                              "bo'yicha undan og'irroqdir.",
                        'ru': 'Сетчатый питон — самая длинная змея планеты, тогда как зеленая анаконда превосходит его '
                              'по массе и толщине.',
                        'en': 'The reticulated python holds the record for maximum verified body length, confirmed at '
                              'over 8 meters in Southeast Asia.'},
        'aliases': ['torsimon piton', 'piton', 'сетчатый питон', 'reticulated python']},
    {   'id': 'nature_scale_068_heaviest_snake',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dunyodagi eng og'ir va baquvvat ilon qaysi (vazni 150-220 kg gacha)?",
                        'ru': 'Какая змея является самой тяжелой и массивной в мире (масса до 150–220 кг)?',
                        'en': 'Which snake holds the title of the heaviest and most massive snake in the world (up to '
                              '150–220 kg)?'},
        'options': {   'uz': ["To'rsimon piton", 'Qora ilon', 'Kobra', 'Yashil anakonda'],
                       'ru': ['Сетчатый питон', 'Гюрза', 'Кобра', 'Зеленая анаконда'],
                       'en': ['Reticulated Python', 'Viper', 'Cobra', 'Green Anaconda']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Yashil anakonda', 'ru': 'Зеленая анаконда', 'en': 'Green Anaconda'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Eunectes_murinus_green_anaconda.jpg/800px-Eunectes_murinus_green_anaconda.jpg',
        'fun_fact': {   'uz': "Yashil anakonda suvda o'zining 200 kg og'irligini oson boshqaradi va kiyik hamda "
                              'kaymanlarni butunligicha yutadi.',
                        'ru': 'Анаконда вдвое массивнее питона такой же длины; обхват ее тела может превышать 1 метр.',
                        'en': 'Green anacondas are twice as thick as pythons of comparable length, easily swallowing '
                              'caimans, deer, and capybaras.'},
        'aliases': ['anakonda', 'yashil anakonda', 'анаконда', 'зеленая анаконда', 'green anaconda', 'anaconda']},
    {   'id': 'nature_scale_069_largest_crustacean_span',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Bo'g'imoyoqlilar orasida eng uzun oyoq qulochiga ega bo'lgan jonivor qaysi (3.8 "
                              'metrgacha)?',
                        'ru': 'Какое членистоногое обладает самым большим размахом конечностей (до 3,8 метра)?',
                        'en': 'Which arthropod possesses the largest leg span in the world, spanning up to 3.8 meters '
                              'tip to tip?'},
        'options': {   'uz': [   "Yapon o'rgimchak-krabi (Japanese Spider Crab)",
                                 'Orol krevetkasi',
                                 'Langust',
                                 'Dengiz chayoni'],
                       'ru': ['Японский краб-паук', 'Королевский краб', 'Лангуст', 'Омар'],
                       'en': ['Japanese Spider Crab', 'King Crab', 'Spiny Lobster', 'American Lobster']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Yapon o'rgimchak-krabi (Japanese Spider Crab)",
                              'ru': 'Японский краб-паук',
                              'en': 'Japanese Spider Crab'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Macrocheira_kaempferi_spider_crab.jpg/800px-Macrocheira_kaempferi_spider_crab.jpg',
        'fun_fact': {   'uz': "Yapon krab-o'rgimchagi 100 yildan ortiq yashay oladi va Tinch okeanining 300 metr "
                              'chuqurliklarida harakatlanadi.',
                        'ru': 'Японский краб-паук живет до 100 лет и имеет размах передних клешней до 3,8 метра при '
                              'панцире диаметром 40 см.',
                        'en': 'Macrocheira kaempferi can live for a century in abyssal waters off Japan, spanning '
                              'nearly 4 meters between outstretched chelipeds.'},
        'aliases': ['yapon krabi', 'orgimchak krab', 'краб-паук', 'японский краб-паук', 'japanese spider crab']},
    {   'id': 'nature_scale_070_largest_carnivorous_marsupial',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Hozirgi kunda tirik qolgan eng yirik yirtqich xaltali hayvon qaysi?',
                        'ru': 'Какое сумчатое хищное животное является самым крупным из ныне живущих?',
                        'en': 'Which animal is the largest living carnivorous marsupial on Earth today?'},
        'options': {   'uz': ["Xaltali bo'ri (Tilatsin)", 'Tasmaniya iblisi (Tasmanian Devil)', 'Kenguru', 'Vombat'],
                       'ru': ['Сумчатый волк', 'Тасманийский дьявол', 'Кенгуру', 'Вомбат'],
                       'en': ['Thylacine', 'Tasmanian Devil', 'Kangaroo', 'Wombat']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Tasmaniya iblisi (Tasmanian Devil)',
                              'ru': 'Тасманийский дьявол',
                              'en': 'Tasmanian Devil'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Sarcophilus_harrisii_tasmanian_devil.jpg/800px-Sarcophilus_harrisii_tasmanian_devil.jpg',
        'fun_fact': {   'uz': "Tasmaniya iblisining tishlash kuchi o'z tana vazniga nisbatan bo'ridan ham ustundir; u "
                              'suyaklarni xuddi shakar kabi maydalaydi.',
                        'ru': 'Относительно массы тела укус тасманийского дьявола сильнее укуса льва, что позволяет '
                              'ему перемалывать черепа добычи.',
                        'en': 'Sarcophilus harrisii possesses the highest bite-force-to-body-mass quotient of any '
                              'living predatory land mammal.'},
        'aliases': ['tasmaniya iblisi', 'тасманийский дьявол', 'tasmanian devil']},
    {   'id': 'nature_scale_071_deepest_plant_photosynthesis',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Eng chuqurda (268 metrda) topilgan fotosintez qiluvchi qizil suvo'ti qaysi?",
                        'ru': 'Какая водоросль способна фотосинтезировать на рекордной глубине 268 метров при '
                              'минимальном свете?',
                        'en': 'Which red alga holds the depth record for photosynthetic plant life at 268 meters '
                              'down?'},
        'options': {   'uz': ['Laminariya', 'Sargassum', "Qizil koral suvo'ti (Coralline red alga)", 'Xlorella'],
                       'ru': ['Ламинария', 'Саргассум', 'Глубоководная коралловая водоросль', 'Хлорелла'],
                       'en': ['Kelp', 'Sargassum', 'Coralline Red Algae', 'Chlorella']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Qizil koral suvo'ti (Coralline red alga)",
                              'ru': 'Глубоководная коралловая водоросль',
                              'en': 'Coralline Red Algae'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Coralline_algae_deep_macro.jpg/800px-Coralline_algae_deep_macro.jpg',
        'fun_fact': {   'uz': "Bu suvo'ti yorug'lik sirtning 0.0005% ini tashkil qiluvchi zulmatda ham fotosintez "
                              'qiladi.',
                        'ru': 'Эта водоросль улавливает сотые доли процента солнечного света на глубине свыше 260 '
                              'метров.',
                        'en': 'Crustose coralline red algae capture mere fractions of a percent of surface photons at '
                              '268 meters.'},
        'aliases': ['qizil suvoti', 'водоросль', 'coralline algae']},
    {   'id': 'nature_scale_072_highest_altitude_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dengiz sathidan 6739 metr balandlikda (vulqon cho'qqisida) yashovchi sutemizuvchi "
                              'qaysi?',
                        'ru': 'Какое млекопитающее обитает на рекордной высоте 6739 метров на вершине вулкана '
                              'Льюльяйльяко?',
                        'en': 'Which mammal holds the world record for living at the highest altitude on Earth (6,739 '
                              'meters)?'},
        'options': {   'uz': ['Qor qoploni', 'Yak', 'Vikunya', 'Sariq dumaloq quloqli sichqon (Phyllotis vaccarum)'],
                       'ru': ['Снежный барс', 'Як', 'Викунья', 'Листоухий хомячок'],
                       'en': ['Snow Leopard', 'Wild Yak', 'Vicuña', 'Yellow-rumped Leaf-eared Mouse']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Sariq dumaloq quloqli sichqon (Phyllotis vaccarum)',
                              'ru': 'Листоухий хомячок',
                              'en': 'Yellow-rumped Leaf-eared Mouse'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Phyllotis_vaccarum_high_altitude.jpg/800px-Phyllotis_vaccarum_high_altitude.jpg',
        'fun_fact': {   'uz': "Bu sichqon And tog'lari cho'qqisidagi qor va muzliklar orasida -30 °C da yashay oladi.",
                        'ru': 'Этот грызун живет на высоте почти 7 километров, опровергнув пределы выживаемости '
                              'млекопитающих.',
                        'en': 'Phyllotis vaccarum survives freezing gales at 6,739 m atop Andean volcano '
                              'Llullaillaco.'},
        'aliases': ['bargquloq sichqon', 'листоухий хомячок', 'leaf-eared mouse']},
    {   'id': 'nature_scale_073_longest_insect_body',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Tana uzunligi bo'yicha dunyodagi eng uzun hasharot qaysi (64 santimetrgacha)?",
                        'ru': 'Какое насекомое является самым длинным в мире от кончика передних ног (до 64 см)?',
                        'en': 'Which insect holds the world record for longest total body length (up to 64 cm)?'},
        'options': {   'uz': [   'Ulkan tayoqcha (Phryganistria chinensis)',
                                 'Chigirtka',
                                 'Beshiktebratar',
                                 "May qo'ng'izi"],
                       'ru': ['Китайский палочник Фриганистрия', 'Кузнечик', 'Богомол', 'Жук-усач'],
                       'en': ['Giant Stick Insect (Phryganistria)', 'Katydid', 'Mantis', 'Longhorn Beetle']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Ulkan tayoqcha (Phryganistria chinensis)',
                              'ru': 'Китайский палочник Фриганистрия',
                              'en': 'Giant Stick Insect (Phryganistria)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Phryganistria_chinensis_stick_insect.jpg/800px-Phryganistria_chinensis_stick_insect.jpg',
        'fun_fact': {   'uz': "Xitoyda topilgan bu hasharot uzunligi bo'yicha odam qo'lidek keladi va ingichka novdaga "
                              "o'xshaydi.",
                        'ru': 'Длина палочника с вытянутыми ногами превышает 64 см, что делает его длиннейшим '
                              'насекомым планеты.',
                        'en': 'Phryganistria chinensis reaches 64 cm with legs extended, mimicking a tree branch.'},
        'aliases': ['tayoqcha hasharot', 'палочник', 'stick insect']},
    {   'id': 'nature_scale_074_heaviest_insect',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Og'irligi bo'yicha dunyodagi eng og'ir hasharot qaysi (vazni 71 grammgacha)?",
                        'ru': 'Какое насекомое является самым тяжелым в мире (масса до 71 грамма)?',
                        'en': 'Which insect holds the record as the heaviest documented insect in the world (up to 71 '
                              'grams)?'},
        'options': {   'uz': ["Gerkules qo'ng'izi", 'Ulkan Veta (Giant Weta)', "Golyat qo'ng'izi", 'Beshiktebratar'],
                       'ru': ['Жук-геркулес', 'Гигантская уэта (Deinacrida)', 'Жук-голиаф', 'Богомол'],
                       'en': ['Hercules Beetle', 'Giant Weta', 'Goliath Beetle', 'Praying Mantis']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Ulkan Veta (Giant Weta)', 'ru': 'Гигантская уэта (Deinacrida)', 'en': 'Giant Weta'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Deinacrida_heteracantha_giant_weta.jpg/800px-Deinacrida_heteracantha_giant_weta.jpg',
        'fun_fact': {   'uz': "Yangi Zelandiyada yashovchi ulkan veta chumchuqdan 3 baravar og'irroq bo'lishi mumkin.",
                        'ru': 'Гигантская уэта весит втрое больше воробья и не летает из-за массивного брюшка.',
                        'en': 'A pregnant female Little Barrier giant weta reached 71 g (2.5 oz), heavier than a house '
                              'sparrow.'},
        'aliases': ['veta', 'уэта', 'giant weta']},
    {   'id': 'nature_scale_075_highest_blood_pressure_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Yuragi 2.5 metr balandlikdagi boshga qon haydash uchun eng yuqori qon bosimiga (280/180 '
                              'mm sim. ust.) ega hayvon qaysi?',
                        'ru': 'У какого животного самое высокое артериальное давление (до 280/180 мм рт. ст.)?',
                        'en': 'Which animal generates the highest systemic arterial blood pressure (up to 280/180 '
                              'mmHg)?'},
        'options': {   'uz': ['Fil', "Ko'k kit", 'Jirafa', 'Ot'],
                       'ru': ['Слон', 'Синий кит', 'Жираф', 'Лошадь'],
                       'en': ['Elephant', 'Blue Whale', 'Giraffe', 'Horse']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Jirafa', 'ru': 'Жираф', 'en': 'Giraffe'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Giraffe_drinking_water_posture.jpg/800px-Giraffe_drinking_water_posture.jpg',
        'fun_fact': {   'uz': "Jirafaning yuragi 11 kg tosh bosadi va boshini egganida insult bo'lmasligi uchun bo'yin "
                              'arteriyasida maxsus klapanlar bor.',
                        'ru': 'Чтобы прокачать кровь на высоту 2,5 метра к мозгу, сердце жирафа весом 11 кг создает '
                              'давление 280 мм рт. ст.',
                        'en': "A giraffe's 11-kg heart pumps at 280/180 mmHg, regulated by carotid valves to prevent "
                              'brain hemorrhages.'},
        'aliases': ['jirafa', 'жираф', 'giraffe']},
    {   'id': 'nature_scale_076_largest_single_cell_organism',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Dunyodagi eng katta bir hujayrali organizm deb hisoblanuvchi suv o'ti qaysi (bo'yi 3 "
                              'metrgacha)?',
                        'ru': 'Какой одноклеточный организм признан крупнейшим на планете (длина до 3 метров)?',
                        'en': 'Which coenocytic green alga is considered the largest single-celled organism on Earth '
                              '(growing up to 3 meters)?'},
        'options': {   'uz': ['Amyoba', 'Infuzoriya tufelka', 'Evglena', 'Kaulerpa (Caulerpa taxifolia)'],
                       'ru': ['Амеба', 'Инфузория-туфелька', 'Эвглена зеленая', 'Каулерпа (Caulerpa)'],
                       'en': ['Amoeba', 'Paramecium', 'Euglena', 'Caulerpa taxifolia']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Kaulerpa (Caulerpa taxifolia)',
                              'ru': 'Каулерпа (Caulerpa)',
                              'en': 'Caulerpa taxifolia'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Caulerpa_taxifolia_single_cell.jpg/800px-Caulerpa_taxifolia_single_cell.jpg',
        'fun_fact': {   'uz': "Kaulerpa butun tana bo'ylab ichki hujayra to'siqlarisiz faqat bitta gigant ko'p yadroli "
                              'hujayradan iborat.',
                        'ru': 'Каулерпа — гигантская сифоновая водоросль без клеточных перегородок, содержащая '
                              'миллионы ядер в одной клетке.',
                        'en': 'Caulerpa consists of a single continuous multinucleated syncytium without internal '
                              'cellular partitions.'},
        'aliases': ['kaulerpa', 'каулерпа', 'caulerpa']},
    {   'id': 'nature_scale_077_thickest_skin_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Yer yuzidagi eng qalin teriga (15 santimetrgacha) ega jonivor qaysi?',
                        'ru': 'Какое морское животное имеет самую толстую кожу на планете (до 15 см)?',
                        'en': 'Which animal possesses the thickest skin of any living creature (up to 15 cm)?'},
        'options': {   'uz': ['Kit akulasi (Whale Shark)', 'Fil', 'Begemot', 'Morj'],
                       'ru': ['Китовая акула', 'Слон', 'Бегемот', 'Морж'],
                       'en': ['Whale Shark', 'Elephant', 'Hippopotamus', 'Walrus']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Kit akulasi (Whale Shark)', 'ru': 'Китовая акула', 'en': 'Whale Shark'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Rhincodon_typus_whale_shark_skin.jpg/800px-Rhincodon_typus_whale_shark_skin.jpg',
        'fun_fact': {   'uz': "Kit akulasining qalin terisi kollagen tolalardan iborat bo'lib, unga qattiq yirtqich "
                              "zarbalaridan to'liq himoya beradi.",
                        'ru': 'Кожа китовой акулы толщиной 15 см представляет собой гибкий бронежилет из плотных слоев '
                              'коллагена.',
                        'en': 'Whale shark hide can measure up to 15 cm thick, offering bullet-proof tensile strength '
                              'against predatory bites.'},
        'aliases': ['kit akulasi', 'китовая акула', 'whale shark']},
    {   'id': 'nature_scale_078_largest_land_predator_ever',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yer yuzida yashagan eng yirik yirtqich dinozavr qaysi (bo'yi 15 metr, vazni 8-9 tonna)?",
                        'ru': 'Какой хищный динозавр признан крупнейшим в истории планеты (длина до 15–16 м)?',
                        'en': "Which carnivorous dinosaur was the longest known predatory theropod in Earth's history "
                              '(15 meters long)?'},
        'options': {   'uz': [   'Tirannozavr (T. rex)',
                                 'Spinozavr (Spinosaurus aegyptiacus)',
                                 'Giganotozavr',
                                 'Alloszavr'],
                       'ru': ['Тираннозавр рекс', 'Спинозавр', 'Гиганотозавр', 'Аллозавр'],
                       'en': ['Tyrannosaurus Rex', 'Spinosaurus', 'Giganotosaurus', 'Allosaurus']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Spinozavr (Spinosaurus aegyptiacus)', 'ru': 'Спинозавр', 'en': 'Spinosaurus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Spinosaurus_aegyptiacus_restoration.jpg/800px-Spinosaurus_aegyptiacus_restoration.jpg',
        'fun_fact': {   'uz': 'Spinozavr suvda va quruqlikda yashagan; uning orqasidagi 1.8 metrlik ulkan yelkan '
                              'suzish va haroratni boshqarishga xizmat qilgan.',
                        'ru': 'Спинозавр превосходил тираннозавра по длине и вел полуводный образ жизни, охотясь на '
                              'гигантских рыб мелового периода.',
                        'en': 'Spinosaurus measured over 15 meters, sporting crocodile-like jaws and an iconic '
                              '1.8-meter dorsal neural sail.'},
        'aliases': ['spinozavr', 'спинозавр', 'spinosaurus']},
    {   'id': 'nature_scale_079_fastest_wingbeat_frequency',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Parvoz paytida qanotlarini soniyasiga 1000 martagacha qoqa oladigan hasharot qaysi?',
                        'ru': 'Какое насекомое совершает рекордную частоту взмахов крыльями (до 1000 взмахов в '
                              'секунду)?',
                        'en': 'Which insect achieves the fastest wingbeat frequency known (up to 1,000 beats per '
                              'second)?'},
        'options': {   'uz': ['Asalari', 'Pashsha', 'Mitti chivin (Forcipomyia ceratopogonid midge)', 'Kolibri'],
                       'ru': ['Пчела', 'Муха', 'Мокрец (Forcipomyia)', 'Колибри'],
                       'en': ['Honeybee', 'Housefly', 'Biting Midge (Forcipomyia)', 'Hummingbird']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Mitti chivin (Forcipomyia ceratopogonid midge)',
                              'ru': 'Мокрец (Forcipomyia)',
                              'en': 'Biting Midge (Forcipomyia)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Ceratopogonidae_midge_macro.jpg/800px-Ceratopogonidae_midge_macro.jpg',
        'fun_fact': {   'uz': 'Bu mittigina hasharotning asinxron qanot mushaklari nerv signallaridan mustaqil '
                              'ravishda rezonans orqali 1046 Hz chastotada tebranadi.',
                        'ru': 'Асинхронные мышцы крыльев мокрецов вибрируют с частотой более 1000 Гц за счет '
                              'миогенного самоподдерживающегося резонанса.',
                        'en': 'Forcipomyia midges oscillate flight muscles at 1,046 Hz via stretch-activated '
                              'asynchronous muscle contraction.'},
        'aliases': ['chivin', 'mokrets', 'мокрец', 'midge', 'biting midge']},
    {   'id': 'nature_scale_080_longest_claws_land_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Tarixdagi eng uzun tirnoqlarga ega hayvon qaysi (tirnoqlari 70–100 santimetrgacha)?',
                        'ru': 'Какое животное обладало самыми длинными когтями в истории (до 70–100 см в длину)?',
                        'en': "Which prehistoric animal possessed the longest claws in Earth's history (measuring up "
                              'to 70–100 cm)?'},
        'options': {   'uz': ['Grizli ayiq', 'Dangasa', 'Anteater', 'Terizinozavr (Therizinosaurus)'],
                       'ru': ['Медведь гризли', 'Гигантский ленивец', 'Муравьед', 'Теризинозавр'],
                       'en': ['Grizzly Bear', 'Giant Ground Sloth', 'Giant Anteater', 'Therizinosaurus']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Terizinozavr (Therizinosaurus)', 'ru': 'Теризинозавр', 'en': 'Therizinosaurus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Therizinosaurus_claws_fossil.jpg/800px-Therizinosaurus_claws_fossil.jpg',
        'fun_fact': {   'uz': "Terizinozavr ulkan o'roqsimon tirnoqlarini yirtqichlardan himoyalanish va baland "
                              'shoxlarni egish uchun ishlatgan.',
                        'ru': 'Когти теризинозавра напоминали метровые сабли из кератина и кости, служа для пригибания '
                              'крон и защиты.',
                        'en': 'Therizinosaurus possessed scythe-like ungual claws extending up to 1 meter in sheath '
                              'length along each finger.'},
        'aliases': ['terizinozavr', 'теризинозавр', 'therizinosaurus']},
    {   'id': 'nature_scale_081_longest_tongue_relative',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Tana uzunligiga nisbatan eng uzun tilga ega jonivor qaysi (tili o'z bo'yidan 1.5 "
                              'baravar uzun)?',
                        'ru': 'Какое животное имеет самый длинный язык относительно размеров тела (в 1,5 раза длиннее '
                              'самого тела)?',
                        'en': 'Which creature has the longest tongue relative to its body length (1.5 times its total '
                              'body size)?'},
        'options': {   'uz': ['Xameleon', 'Zirhli kiyik', 'Girafa', "Chumolixo'r"],
                       'ru': ['Хамелеон', 'Олень', 'Жираф', 'Муравьед'],
                       'en': ['Chameleon', 'Deer', 'Giraffe', 'Anteater']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Xameleon', 'ru': 'Хамелеон', 'en': 'Chameleon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Chameleon_tongue_macro_reach.jpg/800px-Chameleon_tongue_macro_reach.jpg',
        'fun_fact': {   'uz': "Xameleon tili murakkab kollagen elastik prujinalar orqali o'qdek otiladi.",
                        'ru': 'Язык хамелеона длиннее его тела в полтора-два раза и присасывается к жертве вакуумной '
                              'чашей.',
                        'en': "A chameleon's tongue is up to twice its snout-vent length, terminating in a muscular "
                              'suction cup.'},
        'aliases': ['xameleon', 'хамелеон', 'chameleon']},
    {   'id': 'nature_scale_082_largest_eyes_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Hayvonot olamidagi eng katta ko'zlar (diametri 27-30 sm) qaysi jonivorga tegishli?",
                        'ru': 'У какого животного самые большие глаза в мире (диаметром до 27–30 см)?',
                        'en': 'Which animal possesses the largest eyes in the entire animal kingdom (27–30 cm in '
                              'diameter)?'},
        'options': {   'uz': ["Ko'k kit", 'Ulkan kalmar (Kolossal kalmar)', 'Kashalot', 'Oq akula'],
                       'ru': ['Синий кит', 'Колоссальный кальмар', 'Кашалот', 'Белая акула'],
                       'en': ['Blue Whale', 'Colossal Squid', 'Sperm Whale', 'Great White Shark']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Ulkan kalmar (Kolossal kalmar)',
                              'ru': 'Колоссальный кальмар',
                              'en': 'Colossal Squid'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Giant_squid_eye_preserved.jpg/800px-Giant_squid_eye_preserved.jpg',
        'fun_fact': {   'uz': "Kalmar ko'zlari voleybol to'pidek keladi va qorong'u okean tubida harakatlanayotgan "
                              'kashalotlarni payqashga yordam beradi.',
                        'ru': 'Глаза колоссального кальмара размером с баскетбольный мяч улавливают биолюминесценцию '
                              'на глубине 2000 метров.',
                        'en': 'Colossal squid eyes measure 27 cm across, optimized to detect photophore '
                              'bioluminescence stimulated by diving whales.'},
        'aliases': ['kalmar', 'kolossal kalmar', 'кальмар', 'colossal squid']},
    {   'id': 'nature_scale_083_highest_blood_sugar_tolerance',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "O'z qonida shakar miqdorini 30 baravargacha xavfsiz oshira oladigan qush qaysi?",
                        'ru': 'Какая птица может без вреда для здоровья повышать уровень сахара в крови до уровня, '
                              'смертельного для человека?',
                        'en': 'Which bird can safely tolerate blood glucose levels up to 30 times higher than humans '
                              'without diabetes?'},
        'options': {   'uz': ['Chumchuq', "Qaldirg'och", 'Kolibri', 'Boyqush'],
                       'ru': ['Воробей', 'Ласточка', 'Колибри', 'Сова'],
                       'en': ['Sparrow', 'Swallow', 'Hummingbird', 'Owl']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Kolibri', 'ru': 'Колибри', 'en': 'Hummingbird'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Hummingbird_flower_nectar.jpg/800px-Hummingbird_flower_nectar.jpg',
        'fun_fact': {   'uz': 'Kolibri shirin nektar bilan oziqlangani sababli qondagi shakarni tezda mushaklariga '
                              "yo'naltiradi.",
                        'ru': 'Метаболизм колибри моментально сжигает глюкозу нектара прямо в мышцах крыльев.',
                        'en': 'Hummingbirds process sugar so rapidly that glucose is directly oxidized by flight '
                              'muscles within minutes of ingestion.'},
        'aliases': ['kolibri', 'колибри', 'hummingbird']},
    {   'id': 'nature_scale_084_densest_bone_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Sutemizuvchilar orasida suv ostida suzishni osonlashtiruvchi eng zich va og'ir "
                              'suyaklarga ega hayvon qaysi?',
                        'ru': 'Какое млекопитающее обладает самыми плотными и тяжелыми костями скелета для погружения '
                              '(пахиостоз)?',
                        'en': 'Which aquatic mammal possesses the densest, heaviest bones to act as natural diving '
                              'ballast (pachyostosis)?'},
        'options': {   'uz': ['Delfin', 'Oq ayiq', 'Tyulen', 'Lamantin (Manati / Dengiz sigiri)'],
                       'ru': ['Дельфин', 'Белый медведь', 'Тюлень', 'Ламантин (Морская корова)'],
                       'en': ['Dolphin', 'Polar Bear', 'Seal', 'Manatee']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Lamantin (Manati / Dengiz sigiri)',
                              'ru': 'Ламантин (Морская корова)',
                              'en': 'Manatee'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Trichechus_manatus_underwater.jpg/800px-Trichechus_manatus_underwater.jpg',
        'fun_fact': {   'uz': "Lamantin qovurg'alarida suyak iligi bo'shliqlari bo'lmaydi; qattiq suyaklar unga suv "
                              'tubida suzmasdan turishga imkon beradi.',
                        'ru': 'Кости ламантина лишены костномозгового канала и уплотнены, играя роль естественного '
                              'балластного пояса.',
                        'en': 'Manatee ribs are solid bone with no marrow cavities, providing neutral buoyancy ballast '
                              'while grazing submerged sea grass.'},
        'aliases': ['lamantin', 'ламантин', 'морская корова', 'manatee']},
    {   'id': 'nature_scale_085_lowest_metabolic_rate_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Barcha sutemizuvchilar orasida eng past asosiy metabolizmga ega jonivor qaysi?',
                        'ru': 'У какого млекопитающего самый медленный уровень метаболизма среди всех теплокровных '
                              'животных?',
                        'en': 'Which mammal exhibits the lowest basal metabolic rate of any non-hibernating '
                              'warm-blooded animal?'},
        'options': {   'uz': ['Uch barmoqli yalqov', 'Koala', 'Tipratikan', 'Armadillo'],
                       'ru': ['Трёхпалый ленивец', 'Коала', 'Ёж', 'Броненосец'],
                       'en': ['Three-toed Sloth', 'Koala', 'Hedgehog', 'Armadillo']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Uch barmoqli yalqov', 'ru': 'Трёхпалый ленивец', 'en': 'Three-toed Sloth'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Bradypus_tridactylus_sloth.jpg/800px-Bradypus_tridactylus_sloth.jpg',
        'fun_fact': {   'uz': 'Yalqovning tana harorati atrof-muhitga qarab 24 °C gacha tushishi mumkin.',
                        'ru': 'Температура тела ленивца может падать до 24 °C, он меняет температуру вместе с '
                              'окружающей средой.',
                        'en': 'Sloths have metabolic rates so low that their body temperature fluctuates with ambient '
                              'temperature like a poikilotherm.'},
        'aliases': ['yalqov', 'ленивец', 'sloth']},
    {   'id': 'nature_scale_086_deepest_living_shark',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Okeanning 3700 metr chuqurlikdagi qa'rida qayd etilgan eng chuqur yashovchi akula "
                              'qaysi?',
                        'ru': 'Какая акула обитает на самой большой зарегистрированной глубине (до 3700 метров)?',
                        'en': 'Which shark holds the scientific record for the deepest habitat depth ever documented '
                              '(down to 3,700 meters)?'},
        'options': {   'uz': [   'Oq akula',
                                 'Portugaliya it-akulasi (Centroscymnus coelolepis)',
                                 'Grenlandiya akulasi',
                                 "Bolg'abosh akula"],
                       'ru': ['Белая акула', 'Португальская акула', 'Гренландская акула', 'Акула-молот'],
                       'en': ['Great White', 'Portuguese Dogfish', 'Greenland Shark', 'Hammerhead']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Portugaliya it-akulasi (Centroscymnus coelolepis)',
                              'ru': 'Португальская акула',
                              'en': 'Portuguese Dogfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Centroscymnus_coelolepis_deep_sea.jpg/800px-Centroscymnus_coelolepis_deep_sea.jpg',
        'fun_fact': {   'uz': "Bu kichik akula qorong'u abissal tekisliklarda yashaydi va ulkan jigari hisobiga suzish "
                              'qobiliyatini saqlaydi.',
                        'ru': 'Эта глубоководная акула держится на глубинах до 3700 метров благодаря гигантской '
                              'печени, наполненной скваленом.',
                        'en': 'The Portuguese dogfish relies on a squalene-rich liver comprising 30% of its body '
                              'weight to maintain buoyancy at 3,700 m.'},
        'aliases': ['portugaliya akulasi', 'португальская акула', 'portuguese dogfish']},
    {   'id': 'nature_scale_087_highest_flying_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Ko'rshapalaklar orasida eng balandda (3000 metrgacha) parvoz qila oladigan chempion "
                              'qaysi?',
                        'ru': 'Какая летучая мышь летает выше всех среди рукокрылых (на высоте до 3000 метров)?',
                        'en': 'Which bat species holds the altitude record for chiropteran flight (cruising up to '
                              '3,000 meters altitude)?'},
        'options': {   'uz': [   "Vampir ko'rshapalak",
                                 'Uchar tulki',
                                 "Braziliya erkin quyruqli ko'rshapalagi",
                                 'Ushanka'],
                       'ru': ['Летучая мышь-вампир', 'Крылан', 'Бразильский складчатогуб', 'Ушан'],
                       'en': ['Vampire Bat', 'Flying Fox', 'Brazilian Free-tailed Bat', 'Long-eared Bat']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Braziliya erkin quyruqli ko'rshapalagi",
                              'ru': 'Бразильский складчатогуб',
                              'en': 'Brazilian Free-tailed Bat'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tadarida_brasiliensis_bat_flight.jpg/800px-Tadarida_brasiliensis_bat_flight.jpg',
        'fun_fact': {   'uz': "Bu ko'rshapalak soatiga 160 km gorizontal tezlikka erishib, har qanday qushdan tezroq "
                              'gorizontal ucha oladi.',
                        'ru': 'Бразильский складчатогуб развивает горизонтальную скорость 160 км/ч, опережая стрижей и '
                              'ласточек.',
                        'en': 'Tadarida brasiliensis reaches verified horizontal speeds of 160 km/h (100 mph), flying '
                              'up to 3,000 meters.'},
        'aliases': ['braziliya korshapalagi', 'складчатогуб', 'free-tailed bat']},
    {   'id': 'nature_scale_088_longest_insect_migration',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Hasharotlar orasida avloddan avlodga o'tib 4000 km masofani bosib o'tuvchi venger "
                              'qaysi?',
                        'ru': 'Какое насекомое совершает знаменитый многопоколенный перелет длиной более 4000 км через '
                              'весь континент?',
                        'en': 'Which insect undertakes an iconic multi-generational migratory flight spanning over '
                              '4,000 km across North America?'},
        'options': {   'uz': ['Nil chigirtkasi', 'Asalari', 'Ninachi', 'Monarx kapalagi (Danaus plexippus)'],
                       'ru': ['Перелетная саранча', 'Медоносная пчела', 'Стрекоза', 'Данаида монарх'],
                       'en': ['Desert Locust', 'Honeybee', 'Dragonfly', 'Monarch Butterfly']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Monarx kapalagi (Danaus plexippus)',
                              'ru': 'Данаида монарх',
                              'en': 'Monarch Butterfly'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Monarch_Butterfly_Danaus_plexippus.jpg/800px-Monarch_Butterfly_Danaus_plexippus.jpg',
        'fun_fact': {   'uz': "Kanadadan Meksika qarag'ayzorlariga yetib borish uchun kapalaklarning 4 ta avlodi "
                              'almashadi.',
                        'ru': 'Четвертое «суперпоколение» монархов живет в 8 раз дольше родителей и в одиночку '
                              'пролетает тысячи километров к местам зимовки.',
                        'en': "The 'Methuselah generation' of monarchs flies 4,000 km to Michoacán, Mexico, living up "
                              'to 8 months compared to 4 weeks for earlier broods.'},
        'aliases': ['monarx', 'данаида монарх', 'monarch butterfly']},
    {   'id': 'nature_scale_089_largest_colony_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Bir g'orda 20 milliontadan ortiq jonivor yig'iladigan dunyodagi eng yirik "
                              "sutemizuvchilar to'dasi qaysi?",
                        'ru': 'Какое млекопитающее образует крупнейшие колонии в одной пещере (до 20 миллионов особей '
                              'в пещере Бракен)?',
                        'en': 'Which mammal gathers in the largest known single-cave aggregation on Earth (up to 20 '
                              'million bats in Bracken Cave)?'},
        'options': {   'uz': ["Meksika erkin quyruqli ko'rshapalagi", 'Kulrang kalamush', 'Gnu antilopasi', 'Panda'],
                       'ru': ['Мексиканский складчатогуб', 'Серая крыса', 'Антилопа гну', 'Панда'],
                       'en': ['Mexican Free-tailed Bat', 'Norway Rat', 'Wildebeest', 'Giant Panda']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Meksika erkin quyruqli ko'rshapalagi",
                              'ru': 'Мексиканский складчатогуб',
                              'en': 'Mexican Free-tailed Bat'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Bracken_Cave_bats_emergence.jpg/800px-Bracken_Cave_bats_emergence.jpg',
        'fun_fact': {   'uz': "Bracken g'oridagi 20 million ko'rshapalak har kecha 100 tonnadan ortiq hasharotlarni "
                              'yeb tugatadi.',
                        'ru': 'Колония в пещере Бракен в Техасе каждую ночь уничтожает до 150 тонн '
                              'насекомых-вредителей.',
                        'en': 'The Bracken Cave roost hosts over 20 million bats, constituting the largest '
                              'concentration of warm-blooded animals on Earth.'},
        'aliases': ['korshapalak to dashi', 'складчатогуб', 'mexican free-tailed bat']},
    {   'id': 'nature_scale_090_highest_g_force_peck',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Daraxtni tumshug'i bilan urganda miyasi 1200–1400 G kuchiga chiday oladigan qush qaysi?",
                        'ru': 'Какая птица переносит перегрузки до 1200–1400 G при долблении дерева без сотрясения '
                              'мозга?',
                        'en': 'Which bird withstands repetitive deceleration forces up to 1,200–1,400 G while drumming '
                              'against tree trunks?'},
        'options': {   'uz': ['Burgut', 'Qizilishton (Woodpecker)', "To'ti", 'Kaptar'],
                       'ru': ['Орел', 'Дятел', 'Попугай', 'Голубь'],
                       'en': ['Eagle', 'Woodpecker', 'Parrot', 'Pigeon']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qizilishton (Woodpecker)', 'ru': 'Дятел', 'en': 'Woodpecker'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Dendrocopos_major_great_spotted_woodpecker.jpg/800px-Dendrocopos_major_great_spotted_woodpecker.jpg',
        'fun_fact': {   'uz': "Qizilishtonning tili bosh suyagi atrofidan aylanib o'tib, zarba paytida miyani elastik "
                              'tasmadek mahkamlab turadi.',
                        'ru': 'Подъязычная кость дятла обвивает весь череп, действуя как амортизирующий ремень '
                              'безопасности при ударах со скоростью 20 раз в секунду.',
                        'en': "A woodpecker's elongated hyoid apparatus wraps completely around the cranium, "
                              'functioning like a biological seatbelt against 1,200 G shocks.'},
        'aliases': ['qizilishton', 'дятел', 'woodpecker']},
    {   'id': 'nature_scale_091_deepest_living_sponge',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Okeanning 8840 metr chuqurligidagi hadal zonasida topilgan shisha buluti qaysi?',
                        'ru': 'Какая стеклянная губка была обнаружена на рекордной глубине 8840 метров в '
                              'Курило-Камчатском желобе?',
                        'en': 'Which glass sponge (Hexactinellida) was recovered from hadal waters at 8,840 meters in '
                              'the Kuril-Kamchatka Trench?'},
        'options': {   'uz': ['Marjon', 'Dengiz anemonasi', 'Shisha gubka (Hyalonema / Hexactinellida)', 'Meduza'],
                       'ru': ['Коралл', 'Актиния', 'Стеклянная губка (Гексактинеллида)', 'Медуза'],
                       'en': ['Coral', 'Sea Anemone', 'Glass Sponge (Hexactinellida)', 'Jellyfish']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Shisha gubka (Hyalonema / Hexactinellida)',
                              'ru': 'Стеклянная губка (Гексактинеллида)',
                              'en': 'Glass Sponge (Hexactinellida)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Euplectella_aspergillum_glass_sponge.jpg/800px-Euplectella_aspergillum_glass_sponge.jpg',
        'fun_fact': {   'uz': "Shisha bulutlarning skeleti toza kremnezem (shisha) tolalardan iborat bo'lib, ular "
                              'zamonaviy optik tolalardan mustahkamroqdir.',
                        'ru': 'Скелет стеклянных губок построен из чистого диоксида кремния и проводит свет '
                              'эффективнее современных оптоволоконных кабелей.',
                        'en': 'Hexactinellid glass sponges build intricate biosilica spicule skeletons that outlast '
                              'steel and channel light like fiber-optic cables.'},
        'aliases': ['shisha gubka', 'стеклянная губка', 'glass sponge']},
    {   'id': 'nature_scale_092_longest_furred_mammal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yungi 90 santimetrgacha yetib, yer yuzidagi eng uzun junga ega bo'lgan tuyoqli hayvon "
                              'qaysi?',
                        'ru': 'Какое копытное животное обладает самой длинной шерстью в мире (до 90 см под брюхом)?',
                        'en': 'Which ungulate mammal has the longest fur coat in the animal kingdom, growing up to 90 '
                              'cm beneath its belly?'},
        'options': {   'uz': ["Qo'y", 'Bizon', 'Lama', "Qadimgi yovvoyi qo'tos (Yak / Bos mutus)"],
                       'ru': ['Овца', 'Бизон', 'Лама', 'Дикий як'],
                       'en': ['Domestic Sheep', 'Bison', 'Llama', 'Wild Yak']},
        'correct_index': 3,
        'correct_answer': {'uz': "Qadimgi yovvoyi qo'tos (Yak / Bos mutus)", 'ru': 'Дикий як', 'en': 'Wild Yak'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Bos_mutus_wild_yak_tibetan_plateau.jpg/800px-Bos_mutus_wild_yak_tibetan_plateau.jpg',
        'fun_fact': {   'uz': "Tibet baland tog'larida yashovchi qo'tosning qalin etak yungi uni -40 °C qahraton va "
                              "qor bo'ronlaridan saqlaydi.",
                        'ru': 'Густая свисающая юбка из шерсти дикого яка защищает его от промерзшей земли Тибета на '
                              'высоте до 5000 метров.',
                        'en': 'Wild yaks sport a shaggy fringe coat reaching 90 cm in length, insulating against -40 '
                              '°C winds on the Tibetan Plateau.'},
        'aliases': ['qotos', "qo'tos", 'як', 'дикий як', 'yak', 'wild yak']},
    {   'id': 'nature_scale_093_largest_carnivorous_dinosaur_bite',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Fosil tahlillariga ko'ra tarixdagi eng kuchli tishlash kuchiga (35 000–57 000 Nyuton) "
                              'ega dinozavr qaysi?',
                        'ru': 'Какой динозавр обладал сокрушительной силой укуса в 35 000–57 000 Ньютонов, крушившей '
                              'кости трицератопсов?',
                        'en': 'Which dinosaur exerted the greatest estimated terrestrial bite force in prehistory '
                              '(35,000 to 57,000 Newtons)?'},
        'options': {   'uz': ['Tirannozavr reks (Tyrannosaurus rex)', 'Velotsiraptor', 'Spinozavr', 'Karnotavr'],
                       'ru': ['Тираннозавр рекс', 'Велоцираптор', 'Спинозавр', 'Карнотавр'],
                       'en': ['Tyrannosaurus rex', 'Velociraptor', 'Spinosaurus', 'Carnotaurus']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Tirannozavr reks (Tyrannosaurus rex)',
                              'ru': 'Тираннозавр рекс',
                              'en': 'Tyrannosaurus rex'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Tyrannosaurus_rex_skull_bite_force.jpg/800px-Tyrannosaurus_rex_skull_bite_force.jpg',
        'fun_fact': {   'uz': 'T. rex ning mustahkam bosh suyagi va arra tishlari unga 6 tonnagacha bosim berib, '
                              'suyaklarni kukun qilish imkonini bergan.',
                        'ru': 'Компьютерное моделирование показало, что Т-рекс буквально взрывал толстые кости добычи '
                              'силой давления 6 тонн.',
                        'en': 'Biomechanical models reveal T. rex generated 57,000 N of bite force, pulverizing bone '
                              'via thick, banana-shaped conical teeth.'},
        'aliases': ['tirannozavr', 't-rex', 'тираннозавр', 'ти-рекс', 'tyrannosaurus', 't rex']},
    {   'id': 'nature_scale_094_heaviest_flying_bird_wingspan',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Qanot qulochi 3.2 metr bo'lgan dunyodagi eng og'ir yirtqich qush qaysi (15 kg)?",
                        'ru': 'Какая хищная птица является самой тяжелой и летает над горными пиками с размахом '
                              'крыльев до 3,2 метра?',
                        'en': 'Which is the heaviest bird of prey in the Americas, weighing up to 15 kg with a '
                              '3.2-meter wingspan?'},
        'options': {   'uz': ['Burgut', 'And kondori (Andean Condor)', 'Qoraburgut', 'Garpiya'],
                       'ru': ['Беркут', 'Андский кондор', 'Черный гриф', 'Гарпия'],
                       'en': ['Golden Eagle', 'Andean Condor', 'Cinereous Vulture', 'Harpy Eagle']},
        'correct_index': 1,
        'correct_answer': {'uz': 'And kondori (Andean Condor)', 'ru': 'Андский кондор', 'en': 'Andean Condor'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Vultur_gryphus_andean_condor_flight.jpg/800px-Vultur_gryphus_andean_condor_flight.jpg',
        'fun_fact': {   'uz': 'And kondori ulkan vazniga qaramay, iliq havo oqimlarida soatlab qanot qoqmasdan 5000 '
                              'metr balandlikda ucha oladi.',
                        'ru': 'Андский кондор использует восходящие термические потоки, преодолевая до 170 км без '
                              'единого взмаха гигантских крыльев.',
                        'en': 'Vultur gryphus weighs up to 15 kg, relying on thermal updrafts to soar for hundreds of '
                              'miles without flapping.'},
        'aliases': ['kondor', 'and kondori', 'кондор', 'андский кондор', 'andean condor']},
    {   'id': 'nature_scale_095_highest_salt_tolerance_fish',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Sho'rligi dengiz suvidan 3 baravar yuqori bo'lgan tuzli ko'llarda yashay oladigan baliq "
                              'qaysi?',
                        'ru': 'Какая рыба способна жить в гиперсоленых водоемах с соленостью втрое выше океанской?',
                        'en': 'Which pupfish can survive in hypersaline desert springs with salt concentrations three '
                              'times higher than seawater?'},
        'options': {   'uz': ['Forel', 'Karp', 'Sahro baliqchasi (Cyprinodon salinus / Desert Pupfish)', 'Losos'],
                       'ru': ['Форель', 'Карп', 'Пустынный карпозубик', 'Лосось'],
                       'en': ['Trout', 'Carp', 'Desert Pupfish', 'Salmon']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Sahro baliqchasi (Cyprinodon salinus / Desert Pupfish)',
                              'ru': 'Пустынный карпозубик',
                              'en': 'Desert Pupfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cyprinodon_salinus_pupfish.jpg/800px-Cyprinodon_salinus_pupfish.jpg',
        'fun_fact': {   'uz': "O'lim vodiysida yashovchi bu baliq suv harorati 47 °C ga chiqqanda va tuz miqdori "
                              'haddan tashqari oshganda ham yashayveradi.',
                        'ru': 'Пустынный карпозубик в Долине Смерти выдерживает колебания температур от 0 до 47 °C и '
                              'экстремальную концентрацию соли.',
                        'en': 'Cyprinodon salinus survives in Death Valley creeks where temperatures reach 47 °C and '
                              'salinities exceed ocean levels by 300%.'},
        'aliases': ['sahro baliqchasi', 'карпозубик', 'desert pupfish']},
    {   'id': 'nature_scale_096_highest_radiation_tolerance_animal',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Odamni o'ldiradigan radiatsiyadan 1000 baravar kuchli nurlanishga (5000 Gy) chidaydigan "
                              'mikroskopik jonzot qaysi?',
                        'ru': 'Какое микроскопическое животное способно выдержать дозу радиации в 5000 Грей, '
                              'смертельную для человека в тысячекратном размере?',
                        'en': 'Which microscopic invertebrate can withstand ionizing radiation doses of 5,000 Gy—over '
                              '1,000 times the lethal human dose?'},
        'options': {   'uz': ['Amyoba', 'Nematoda', 'Infuzoriya', 'Tixoxodka (Suv ayiqchasi / Tardigrade)'],
                       'ru': ['Амеба', 'Нематода', 'Инфузория', 'Тихоходка (Tardigrada)'],
                       'en': ['Amoeba', 'Nematode', 'Rotifer', 'Tardigrade (Water Bear)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Tixoxodka (Suv ayiqchasi / Tardigrade)',
                              'ru': 'Тихоходка (Tardigrada)',
                              'en': 'Tardigrade (Water Bear)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Tardigrade_SEM_macro.jpg/800px-Tardigrade_SEM_macro.jpg',
        'fun_fact': {   'uz': 'Tixoxodka anabioz holatida mutlaq nol (-273 °C) sovuqda va ochiq kosmos vakuumida ham '
                              'tirik qoladi.',
                        'ru': 'Тихоходки синтезируют уникальный белок Dsup, защищающий нити ДНК от распада под '
                              'воздействием космического излучения.',
                        'en': 'Tardigrades protect their genome using Dsup (damage suppressor) proteins, tolerating '
                              'open space vacuum and -272 °C temperatures.'},
        'aliases': ['tixoxodka', 'suv ayigi', 'тихоходка', 'tardigrade', 'water bear']},
    {   'id': 'nature_scale_097_deepest_living_insect',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "Yer qa'ridagi g'orlarning 2000 metr chuqurligida yashovchi qanotsiz hasharot qaysi?",
                        'ru': 'Какое бескрылое членистоногое обитает в глубочайшей пещере мира Крубера-Воронья на '
                              'глубине свыше 1980 метров?',
                        'en': 'Which wingless springtail insect was discovered living at record subterranean depths '
                              'exceeding 1,980 meters in Krubera Cave?'},
        'options': {   'uz': [   "Plutomurus ortobalaganensis (G'or kollombolasi)",
                                 "G'or chigirtkasi",
                                 "Ko'r qo'ng'iz",
                                 'Qirkayoq'],
                       'ru': [   'Плутомурус (Plutomurus ortobalaganensis)',
                                 'Пещерный сверчок',
                                 'Слепой жук',
                                 'Многоножка'],
                       'en': ['Cave Springtail (Plutomurus)', 'Cave Cricket', 'Blind Beetle', 'Centipede']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Plutomurus ortobalaganensis (G'or kollombolasi)",
                              'ru': 'Плутомурус (Plutomurus ortobalaganensis)',
                              'en': 'Cave Springtail (Plutomurus)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Plutomurus_ortobalaganensis_subterranean.jpg/800px-Plutomurus_ortobalaganensis_subterranean.jpg',
        'fun_fact': {   'uz': "Dunyodagi eng chuqur g'or tubida yashovchi bu jonzotning ko'zlari va pigmenti "
                              "bo'lmaydi.",
                        'ru': 'Это существо живет в полной тьме на глубине 2 км под землей, питаясь плесневыми '
                              'грибками на камнях.',
                        'en': 'Plutomurus ortobalaganensis thrives in total darkness 2 km underground, completely '
                              'lacking eyes and pigments.'},
        'aliases': ['plutomurus', 'плутомурус', 'springtail', 'cave springtail']},
    {   'id': 'nature_scale_098_fastest_organism_turn_acceleration',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "O'z yo'nalishini sekundiga 15 marta to'satdan 90 gradusga o'zgartira oladigan eng "
                              'chaqqon havo ovchisi qush qaysi?',
                        'ru': 'Какая птица способна мгновенно менять курс на 90 градусов за доли секунды, маневрируя в '
                              'густом лесу?',
                        'en': 'Which raptor executes 90-degree aerial turns in fractions of a second, navigating dense '
                              'forest branches with ultimate agility?'},
        'options': {   'uz': ['Burgut', "Quriy (Qirg'iy / Eurasian Sparrowhawk)", 'Boyqush', 'Lochin'],
                       'ru': ['Беркут', 'Ястреб-перепелятник', 'Сова', 'Сапсан'],
                       'en': ['Golden Eagle', 'Eurasian Sparrowhawk', 'Owl', 'Falcon']},
        'correct_index': 1,
        'correct_answer': {   'uz': "Quriy (Qirg'iy / Eurasian Sparrowhawk)",
                              'ru': 'Ястреб-перепелятник',
                              'en': 'Eurasian Sparrowhawk'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Accipiter_nisus_sparrowhawk_agility.jpg/800px-Accipiter_nisus_sparrowhawk_agility.jpg',
        'fun_fact': {   'uz': "Qirg'iyning qisqa yumaloq qanotlari va uzun dumi daraxt shoxlari orasida havoda "
                              'aqlbovar qilmas burilishlar yasashga imkon beradi.',
                        'ru': 'Короткие закругленные крылья и длинный рулевой хвост ястреба работают как совершенные '
                              'закрылки в лесной чаще.',
                        'en': 'Accipiter nisus uses short, rounded wings and a rudder-like long tail to maneuver '
                              'through dense thickets at high speed.'},
        'aliases': ['qirgiy', 'quriy', 'ястреб', 'ястреб-перепелятник', 'sparrowhawk']},
    {   'id': 'nature_scale_099_largest_marine_carnivore_toothed',
        'sub_mode': 'animal_scale',
        'question': {   'uz': 'Tishli yirtqichlar orasida eng ulkan bosh va eng katta tishlarga ega dengiz giganti '
                              'qaysi (20 metr, 50 tonna)?',
                        'ru': 'Какое современное зубатое хищное животное является крупнейшим на Земле (до 20 метров и '
                              '50 тонн)?',
                        'en': 'Which modern toothed predator is the largest on Earth, reaching 20 meters in length and '
                              'weighing over 50 tonnes?'},
        'options': {   'uz': ['Kosatka', 'Oq akula', 'Kashalot', 'Megalodon'],
                       'ru': ['Косатка', 'Белая акула', 'Кашалот', 'Мегалодон'],
                       'en': ['Orca', 'Great White Shark', 'Sperm Whale', 'Megalodon']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Kashalot', 'ru': 'Кашалот', 'en': 'Sperm Whale'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Physeter_macrocephalus_sperm_whale.jpg/800px-Physeter_macrocephalus_sperm_whale.jpg',
        'fun_fact': {   'uz': 'Kashalotning har bir tishi 1 kg gacha tosh bosadi va u 2000 metr chuqurlikda ulkan '
                              'kalmarlarni ovlaydi.',
                        'ru': 'Нижняя челюсть кашалота вооружена 40-50 массивными зубами, каждый из которых весит до '
                              'одного килограмма.',
                        'en': 'Sperm whales are the largest living toothed predators, diving 2,000 meters to hunt '
                              'colossal squids with 1-kg teeth.'},
        'aliases': ['kashalot', 'кашалот', 'sperm whale']},
    {   'id': 'nature_scale_100_strongest_electric_discharge',
        'sub_mode': 'animal_scale',
        'question': {   'uz': "O'z tanasida 860 Volt kuchlanishli elektr toki hosil qilib o'ljasini karaxt qiluvchi "
                              'suv jonzoti qaysi?',
                        'ru': 'Какая рыба способна генерировать электрический разряд напряжением до 860 Вольт?',
                        'en': 'Which aquatic creature can generate an electric shock discharging up to 860 Volts?'},
        'options': {   'uz': ['Elektr skat', 'Som baliq', 'Akula', 'Elektr ilonbaliq (Electrophorus voltai)'],
                       'ru': ['Электрический скат', 'Сом', 'Акула', 'Электрический угорь'],
                       'en': ['Electric Ray', 'Catfish', 'Shark', 'Electric Eel (Electrophorus voltai)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Elektr ilonbaliq (Electrophorus voltai)',
                              'ru': 'Электрический угорь',
                              'en': 'Electric Eel (Electrophorus voltai)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Electrophorus_electricus_eel.jpg/800px-Electrophorus_electricus_eel.jpg',
        'fun_fact': {   'uz': '2019-yilda kashf qilingan Electrophorus voltai 860 V kuchlanish chiqarib, tirik '
                              "tabiatdagi eng kuchli bioelektr manbai bo'lib qolmoqda.",
                        'ru': 'Электроциты угря Вольта соединены последовательно, выдавая импульс 860 Вольт, способный '
                              'оглушить лошадь.',
                        'en': 'Electrophorus voltai produces 860-Volt discharges from thousands of stacked electrocyte '
                              'cells arranged in series.'},
        'aliases': ['elektr ilonbaliq', 'электрический угорь', 'electric eel']},
    {   'id': 'nature_emoji_001_okapi',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦓 + 🦒",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦓 + 🦒',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦓 + 🦒'},
        'options': {   'uz': ['Okapi', 'Zebra', 'Jirafa', 'Antilopa'],
                       'ru': ['Окапи', 'Зебра', 'Жираф', 'Антилопа'],
                       'en': ['Okapi', 'Zebra', 'Giraffe', 'Antelope']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Okapi', 'ru': 'Окапи', 'en': 'Okapi'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Okapi_striped_rump_macro.jpg/800px-Okapi_striped_rump_macro.jpg',
        'fun_fact': {   'uz': "Okapining orqa qismida zebranikidek chiziqlar bo'lsa-da, u biologik jihatdan jirafaning "
                              'yagona tirik qarindoshidir.',
                        'ru': 'Несмотря на полосы как у зебры, окапи — единственный ныне живущий родственник жирафа с '
                              'синим длинным языком.',
                        'en': 'Though sporting zebra-like stripes on its legs, the forest-dwelling okapi is the only '
                              'living relative of the giraffe.'},
        'aliases': ['okapi', 'окапи', 'okapi']},
    {   'id': 'nature_emoji_002_platypus',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦆 + 🦫 + 🥚",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦆 + 🦫 + 🥚',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦆 + 🦫 + 🥚'},
        'options': {   'uz': ['Yexidna', "O'rdakburun (Platipus)", 'Qunduz', 'Ondatra'],
                       'ru': ['Ехидна', 'Утконос', 'Бобр', 'Ондатра'],
                       'en': ['Echidna', 'Platypus', 'Beaver', 'Muskrat']},
        'correct_index': 1,
        'correct_answer': {'uz': "O'rdakburun (Platipus)", 'ru': 'Утконос', 'en': 'Platypus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Platypus_waterproof_fur_macro.jpg/800px-Platypus_waterproof_fur_macro.jpg',
        'fun_fact': {   'uz': "O'rdakburun tuxum qo'yuvchi sutemizuvchi bo'lib, erkaklarining orqa panjasida zaharli "
                              "nayza bo'ladi va tumshug'i bilan elektr impulslarini sezadi.",
                        'ru': 'Утконос откладывает яйца, выкармливает детенышей молоком через кожу, а самцы обладают '
                              'ядовитыми шпорами на лапах.',
                        'en': 'The platypus is an egg-laying mammal with a duck-like bill capable of electroreception '
                              'and venomous spurs on male hind legs.'},
        'aliases': ['ordakburun', "o'rdakburun", 'утконос', 'platypus']},
    {   'id': 'nature_emoji_003_narwhal',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌊 + 🦄 + 🐋",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌊 + 🦄 + 🐋',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌊 + 🦄 + 🐋'},
        'options': {   'uz': ['Beluxa', 'Kashalot', 'Narval (Dengiz birshoxi)', 'Kosatka'],
                       'ru': ['Белуха', 'Кашалот', 'Нарвал', 'Косатка'],
                       'en': ['Beluga', 'Sperm Whale', 'Narwhal', 'Orca']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Narval (Dengiz birshoxi)', 'ru': 'Нарвал', 'en': 'Narwhal'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Monodon_monoceros_narwhals_arctic.jpg/800px-Monodon_monoceros_narwhals_arctic.jpg',
        'fun_fact': {   'uz': "Narvalning 'shoxi' aslida uning yuqori jag'idan 3 metrgacha o'sib chiqqan spiral "
                              'shaklidagi chap qoziq tishidir; unda millionlab asab tolalari bor.',
                        'ru': '«Рог» нарвала — это видоизмененный левый клык длиной до 3 метров, пронизанный '
                              'миллионами чувствительных нервных окончаний.',
                        'en': "The narwhal's iconic tusk is an overgrown, spiraled left canine tooth up to 3 meters "
                              'long with 10 million sensory nerve pathways.'},
        'aliases': ['narval', 'нарвал', 'narwhal']},
    {   'id': 'nature_emoji_004_echidna',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦔 + 🐜 + 🥚",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦔 + 🐜 + 🥚',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦔 + 🐜 + 🥚'},
        'options': {   'uz': ['Tipratikan', 'Jayra', 'Pangolin', 'Yexidna'],
                       'ru': ['Ёж', 'Дикобраз', 'Панголин', 'Ехидна'],
                       'en': ['Hedgehog', 'Porcupine', 'Pangolin', 'Short-beaked Echidna']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Yexidna', 'ru': 'Ехидна', 'en': 'Short-beaked Echidna'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Echidna_spines_detail_macro.jpg/800px-Echidna_spines_detail_macro.jpg',
        'fun_fact': {   'uz': "Yexidna tuxum qo'yadi va bolasi tuxumdan chiqqach, onasining qornidagi xaltasida sut "
                              'yalash orqali oziqlanadi.',
                        'ru': 'Ехидна откладывает одно кожистое яйцо и вынашивает его в брюшной сумке, где '
                              'вылупившийся детеныш слизывает молоко.',
                        'en': 'The echidna lays a single soft-shelled egg directly into its maternal pouch, where the '
                              'puggle hatches and laps up milk.'},
        'aliases': ['yexidna', 'ехидна', 'echidna']},
    {   'id': 'nature_emoji_005_basilisk_lizard',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦎 + 👑 + 🏃\u200d♂️ + 🌊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦎 + 👑 + 🏃\u200d♂️ + '
                              '🌊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦎 + 👑 + 🏃\u200d♂️ + '
                              '🌊'},
        'options': {   'uz': ['Vasilisk kaltakesagi (Iso Masih kaltakesagi)', 'Xameleon', 'Gekkon', 'Komodo varani'],
                       'ru': ['Шлемоносный василиск', 'Хамелеон', 'Геккон', 'Комодский варан'],
                       'en': ['Common Basilisk (Jesus Lizard)', 'Chameleon', 'Gecko', 'Komodo Dragon']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Vasilisk kaltakesagi (Iso Masih kaltakesagi)',
                              'ru': 'Шлемоносный василиск',
                              'en': 'Common Basilisk (Jesus Lizard)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Basiliscus_basiliscus_running_water.jpg/800px-Basiliscus_basiliscus_running_water.jpg',
        'fun_fact': {   'uz': 'Vasilisk oyoq barmoqlaridagi maxsus teri qatlamlari yordamida suv betini tez urib, '
                              "cho'kmasdan suv ustida yugurib o'ta oladi.",
                        'ru': 'Василиск способен пробегать по воде со скоростью 12 км/ч благодаря перепонкам на лапах, '
                              'создающим воздушные карманы.',
                        'en': 'The basilisk lizard can sprint across water surfaces for tens of meters using fringed '
                              'toes to trap buoyant air pockets.'},
        'aliases': ['vasilisk', 'василиск', 'basilisk', 'jesus lizard']},
    {   'id': 'nature_emoji_006_sloth',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌲 + 🦥 + 💤 + 🍃",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌲 + 🦥 + 💤 + 🍃',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌲 + 🦥 + 💤 + 🍃'},
        'options': {   'uz': ['Koala', 'Yalqov (Sloth)', 'Possum', 'Lori'],
                       'ru': ['Коала', 'Трёхпалый ленивец', 'Опоссум', 'Лори'],
                       'en': ['Koala', 'Sloth', 'Opossum', 'Slow Loris']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Yalqov (Sloth)', 'ru': 'Трёхпалый ленивец', 'en': 'Sloth'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Bradypus_tridactylus_sloth.jpg/800px-Bradypus_tridactylus_sloth.jpg',
        'fun_fact': {   'uz': "Yalqovning mo'ynasida yashil mikrosuv o'tlari o'sadi, bu unga daraxt shoxlarida "
                              'yirtqich qushlardan yashirinishga yordam beradi.',
                        'ru': 'В шерсти ленивца растут симбиотические зеленые водоросли и живут уникальные '
                              'бабочки-огневки, создающие маскировочный микробиом.',
                        'en': "A sloth's fur hosts symbiotic green algae and specialized moths that provide green "
                              'camouflage in rainforest canopies.'},
        'aliases': ['yalqov', 'ленивец', 'sloth']},
    {   'id': 'nature_emoji_007_leafy_seadragon',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌊 + 🐉 + 🌿",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌊 + 🐉 + 🌿',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌊 + 🐉 + 🌿'},
        'options': {   'uz': ['Dengiz oti', 'Ignabaliq', 'Yaproqsimon dengiz ajdahosi', 'Skat'],
                       'ru': ['Морской конек', 'Рыба-игла', 'Лиственный морской дракон (Тряпичник)', 'Скат'],
                       'en': ['Seahorse', 'Pipefish', 'Leafy Seadragon', 'Stingray']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Yaproqsimon dengiz ajdahosi',
                              'ru': 'Лиственный морской дракон (Тряпичник)',
                              'en': 'Leafy Seadragon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Leafy_seadragon_dermal_appendages_macro.jpg/800px-Leafy_seadragon_dermal_appendages_macro.jpg',
        'fun_fact': {   'uz': "Bu baliq suvo'ti barglariga o'xshash tana qismlari tufayli yirtqichlardan butunlay "
                              "ko'rinmas bo'lib oladi.",
                        'ru': 'Все листовидные выросты морского дракона-тряпичника служат исключительно камуфляжем, '
                              'плавает он прозрачными плавничками.',
                        'en': 'Leafy seadragons possess intricate leaf-shaped protrusions across their bodies to mimic '
                              'floating kelp fronds.'},
        'aliases': ['dengiz ajdahosi', 'тряпичник', 'leafy seadragon']},
    {   'id': 'nature_emoji_008_blue_ringed_octopus',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐙 + 🔵 + 💍 + ☠️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐙 + 🔵 + 💍 + ☠️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐙 + 🔵 + 💍 + ☠️'},
        'options': {   'uz': ['Oddiy sakkizoyoq', 'Kalmar', 'Meduza', "Ko'k halqali sakkizoyoq"],
                       'ru': ['Обычный осьминог', 'Кальмар', 'Медуза', 'Синекольчатый осьминог'],
                       'en': ['Common Octopus', 'Squid', 'Jellyfish', 'Blue-ringed Octopus']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Ko'k halqali sakkizoyoq",
                              'ru': 'Синекольчатый осьминог',
                              'en': 'Blue-ringed Octopus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Blue-ringed_octopus_macro.jpg/800px-Blue-ringed_octopus_macro.jpg',
        'fun_fact': {   'uz': "Golf to'pidek keladigan bu mittigina sakkizoyoqning zahari 26 ta katta yoshli odamni "
                              "daqiqalar ichida o'ldirishga yetadi.",
                        'ru': 'Этот крошечный осьминог размером с мячик для гольфа несет в слюнных железах достаточно '
                              'тетродотоксина, чтобы убить 26 человек.',
                        'en': 'Measuring only 12–20 cm, the blue-ringed octopus carries enough tetrodotoxin to '
                              'paralyze 26 adult humans within minutes.'},
        'aliases': ['kok halqali sakkizoyoq', 'синекольчатый осьминог', 'blue-ringed octopus']},
    {   'id': 'nature_emoji_009_rafflesia',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌸 + 🥩 + 👃🤢",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌸 + 🥩 + 👃🤢',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌸 + 🥩 + 👃🤢'},
        'options': {   'uz': ['Raffleziya Arnoldi (Murdaguli)', 'Venera pashshatutari', 'Lotos', 'Viktoriya regiya'],
                       'ru': ['Раффлезия Арнольда (Трупный цветок)', 'Венерина мухоловка', 'Лотос', 'Виктория регия'],
                       'en': ['Rafflesia arnoldii (Corpse Flower)', 'Venus Flytrap', 'Lotus', 'Victoria amazonica']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Raffleziya Arnoldi (Murdaguli)',
                              'ru': 'Раффлезия Арнольда (Трупный цветок)',
                              'en': 'Rafflesia arnoldii (Corpse Flower)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Rafflesia_arnoldii_flower_bloom.jpg/800px-Rafflesia_arnoldii_flower_bloom.jpg',
        'fun_fact': {   'uz': "Raffleziya yer yuzidagi eng katta yakka gul (diametri 1 metr, og'irligi 10 kg) bo'lib, "
                              "changlatuvchi go'sht pashshalarini jalb qilish uchun chirigan go'sht hidi chiqaradi.",
                        'ru': 'Раффлезия не имеет листьев, стебля и корней, паразитируя на лианах, и пахнет тухлым '
                              'мясом для привлечения падальных мух.',
                        'en': "Rafflesia arnoldii produces the world's largest individual flower (up to 1 m across) "
                              'and reeks of rotting meat to attract carrion flies.'},
        'aliases': ['raffleziya', 'раффлезия', 'rafflesia']},
    {   'id': 'nature_emoji_010_venus_flytrap',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🪰 + 🪴 + 🩸 + 🪤",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🪰 + 🪴 + 🩸 + 🪤',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🪰 + 🪴 + 🩸 + 🪤'},
        'options': {   'uz': ['Nepentes', 'Venera pashshatutari (Dionaea)', 'Rosyanka', 'Kaktus'],
                       'ru': ['Непентес', 'Венерина мухоловка', 'Росянка', 'Кактус'],
                       'en': ['Pitcher Plant', 'Venus Flytrap', 'Sundew', 'Cactus']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Venera pashshatutari (Dionaea)', 'ru': 'Венерина мухоловка', 'en': 'Venus Flytrap'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Dionaea_muscipula_closing_trap.jpg/800px-Dionaea_muscipula_closing_trap.jpg',
        'fun_fact': {   'uz': "Ushbu yirtqich o'simlik bargidagi sezgir tukchalariga 20 soniya ichida ikki marta "
                              "tegilsa, qopqon soniyaning o'ndan bir qismida shartta yopiladi.",
                        'ru': 'Ловушка мухоловки захлопывается за 0,1 секунды только при повторном касании волосков, '
                              'чтобы не тратить силы на дождевые капли.',
                        'en': 'The Venus flytrap snaps shut in 100 milliseconds only when trigger hairs are brushed '
                              'twice within 20 seconds to confirm live prey.'},
        'aliases': ['venera pashshatutari', 'мухоловка', 'венерина мухоловка', 'venus flytrap']},
    {   'id': 'nature_emoji_011_roadrunner',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🏜️ + 🌵 + 🐦 + ⚡",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🏜️ + 🌵 + 🐦 + ⚡',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🏜️ + 🌵 + 🐦 + ⚡'},
        'options': {   'uz': ['Tuyaqush', 'Qizilishton', "Kaliforniya yo'lchi qushi (Roadrunner)", 'Kolibri'],
                       'ru': ['Страус', 'Дятел', 'Калифорнийская кукушка-подорожник', 'Колибри'],
                       'en': ['Ostrich', 'Woodpecker', 'Greater Roadrunner', 'Hummingbird']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Kaliforniya yo'lchi qushi (Roadrunner)",
                              'ru': 'Калифорнийская кукушка-подорожник',
                              'en': 'Greater Roadrunner'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Geococcyx_californianus_roadrunner.jpg/800px-Geococcyx_californianus_roadrunner.jpg',
        'fun_fact': {   'uz': "Yo'lchi qush sahro bo'ylab soatiga 42 km tezlikda yugurib, zaharli chiqildoq ilonlarni "
                              'boshiga zarba berib ovlaydi.',
                        'ru': 'Кукушка-подорожник бегает по пустыне со скоростью 42 км/ч, охотясь на гремучих змей и '
                              'скорпионов.',
                        'en': 'The greater roadrunner sprints across desert sands at 42 km/h, capturing venomous '
                              'rattlesnakes by beating them against rocks.'},
        'aliases': ['yolchi qush', 'roadrunner', 'подорожник', 'кукушка-подорожник', 'greater roadrunner']},
    {   'id': 'nature_emoji_012_vampire_bat',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦇 + 🩸 + 🧛 + 🌙",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦇 + 🩸 + 🧛 + 🌙',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦇 + 🩸 + 🧛 + 🌙'},
        'options': {   'uz': ['Uchar tulki', 'Boyqush', "Mitti ko'rshapalak", "Qonxo'r ko'rshapalak (Vampir)"],
                       'ru': ['Крылан', 'Сова', 'Нетопырь', 'Обыкновенный вампир (Десмод)'],
                       'en': ['Flying Fox', 'Barn Owl', 'Pipistrelle', 'Common Vampire Bat']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Qonxo'r ko'rshapalak (Vampir)",
                              'ru': 'Обыкновенный вампир (Десмод)',
                              'en': 'Common Vampire Bat'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Desmodus_rotundus_vampire_bat.jpg/800px-Desmodus_rotundus_vampire_bat.jpg',
        'fun_fact': {   'uz': "Vampir ko'rshapalakning so'lagida drakulin deb ataluvchi kuchli antikoagulyant modda "
                              "bo'lib, o'lja qonining ivib qolishiga yo'l qo'ymaydi.",
                        'ru': 'Слюна летучей мыши-вампира содержит фермент дракулин, предотвращающий свертывание крови '
                              'жертвы во время слизывания.',
                        'en': 'The saliva of the vampire bat contains draculin, a potent anticoagulant that prevents '
                              'host blood from clotting while feeding.'},
        'aliases': ['vampir korshapalak', 'вампир', 'летучая мышь вампир', 'vampire bat']},
    {   'id': 'nature_emoji_013_anglerfish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐟 + 💡 + 🎣 + 🌊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐟 + 💡 + 🎣 + 🌊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐟 + 💡 + 🎣 + 🌊'},
        'options': {   'uz': ['Dengiz shaytoni (Udilshik)', 'Murena', 'Kambala', 'Akula'],
                       'ru': ['Глубоководный удильщик (Морской чёрт)', 'Мурена', 'Камбала', 'Акула'],
                       'en': ['Humpback Anglerfish', 'Moray Eel', 'Flounder', 'Shark']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Dengiz shaytoni (Udilshik)',
                              'ru': 'Глубоководный удильщик (Морской чёрт)',
                              'en': 'Humpback Anglerfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Melanocetus_johnsonii_anglerfish.jpg/800px-Melanocetus_johnsonii_anglerfish.jpg',
        'fun_fact': {   'uz': "Udilshik boshidagi yorug'lik chiqaruvchi 'qarmoq' (illitsiy) simbiotik bioluminessent "
                              'bakteriyalar hisobiga yonadi.',
                        'ru': 'Светящаяся «удочка» самки удильщика светится в бездне океана благодаря миллионам '
                              'симбиотических бактерий Photobacterium.',
                        'en': 'Female anglerfish dangle a modified dorsal spine (illicium) tipped with bioluminescent '
                              'Photobacterium symbionts to lure prey.'},
        'aliases': ['udilshik', 'dengiz shaytoni', 'удильщик', 'морской черт', 'anglerfish']},
    {   'id': 'nature_emoji_014_mantis_shrimp',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦞 + 🥊 + 🌈 + ⚡",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦞 + 🥊 + 🌈 + ⚡',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦞 + 🥊 + 🌈 + ⚡'},
        'options': {   'uz': ['Orol krabi', 'Beshiktebratar qisqichbaqa (Mantis Shrimp)', 'Langust', 'Omar'],
                       'ru': ['Камчатский краб', 'Рак-богомол', 'Лангуст', 'Омар'],
                       'en': ['King Crab', 'Peacock Mantis Shrimp', 'Spiny Lobster', 'American Lobster']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Beshiktebratar qisqichbaqa (Mantis Shrimp)',
                              'ru': 'Рак-богомол',
                              'en': 'Peacock Mantis Shrimp'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Odontodactylus_scyllarus_mantis_shrimp.jpg/800px-Odontodactylus_scyllarus_mantis_shrimp.jpg',
        'fun_fact': {   'uz': "Bu qisqichbaqaning ko'zlarida 16 xil rang fotoretseptori bo'lib (odamda bor-yo'g'i 3 "
                              "ta), ultrabinafsha va polyarizatsiyalangan yorug'likni ko'ra oladi.",
                        'ru': 'Глаза рака-богомола содержат 16 типов фоторецепторов и различают циркулярно '
                              'поляризованный свет, невидимый никому на Земле.',
                        'en': 'Peacock mantis shrimp have 16 distinct photoreceptor types and process circular '
                              'polarized light through compound trinocular eyes.'},
        'aliases': ['rak bogomol', 'beshiktebratar qisqichbaqa', 'рак-богомол', 'mantis shrimp']},
    {   'id': 'nature_emoji_015_emperor_penguin',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐦 + ❄️ + 👑 + 🧊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐦 + ❄️ + 👑 + 🧊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐦 + ❄️ + 👑 + 🧊'},
        'options': {   'uz': ['Gagarka', 'Kivi', 'Imperator pingvini', 'Albatros'],
                       'ru': ['Гагарка', 'Киви', 'Императорский пингвин', 'Альбатрос'],
                       'en': ['Auk', 'Kiwi', 'Emperor Penguin', 'Albatross']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Imperator pingvini', 'ru': 'Императорский пингвин', 'en': 'Emperor Penguin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Penguin_feathers_detail.jpg/800px-Penguin_feathers_detail.jpg',
        'fun_fact': {   'uz': "Imperator pingvini qahraton qishda -50 °C sovuq va bo'ronlarda erkaklari tuxumni "
                              'panjalari ustida qorin burmasi ostida 2 oy isitib boqadi.',
                        'ru': 'Самец императорского пингвина два месяца голодает среди антарктической пурги, согревая '
                              'яйцо в выводковой сумке на лапах.',
                        'en': 'Male emperor penguins fast for over 60 days in -50 °C Antarctic blizzards, incubating a '
                              'single egg on their feet beneath a brood pouch.'},
        'aliases': ['imperator pingvini', 'пингвин', 'императорский пингвин', 'emperor penguin']},
    {   'id': 'nature_emoji_016_chameleon',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦎 + 👅 + 🎯 + 🎨",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦎 + 👅 + 🎯 + 🎨',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦎 + 👅 + 🎯 + 🎨'},
        'options': {   'uz': ['Gekkon', 'Iguana', 'Varan', 'Xameleon'],
                       'ru': ['Геккон', 'Игуана', 'Варан', 'Хамелеон'],
                       'en': ['Gecko', 'Iguana', 'Monitor Lizard', 'Chameleon']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Xameleon', 'ru': 'Хамелеон', 'en': 'Chameleon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Chameleon_scales_macro.jpg/800px-Chameleon_scales_macro.jpg',
        'fun_fact': {   'uz': "Xameleonning ko'zlari bir-biridan mustaqil harakatlanib, bir vaqtning o'zida ikkita "
                              "turli yo'nalishni 360 daraja kuzata oladi.",
                        'ru': 'Глаза хамелеона двигаются абсолютно независимо друг от друга, позволяя одновременно '
                              'сканировать местность и целиться языком.',
                        'en': "A chameleon's eyes pivot stereoscopically and independently, providing two distinct "
                              'panoramic visual feeds simultaneously.'},
        'aliases': ['xameleon', 'хамелеон', 'chameleon']},
    {   'id': 'nature_emoji_017_giant_panda',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦥 + 🐻 + 🌿 + 🎋",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦥 + 🐻 + 🌿 + 🎋',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦥 + 🐻 + 🌿 + 🎋'},
        'options': {   'uz': ["Ulkan panda (Bambuk ayig'i)", "Qo'ng'ir ayiq", 'Koala', 'Qizil panda'],
                       'ru': ['Большая панда', 'Бурый медведь', 'Коала', 'Красная панда'],
                       'en': ['Giant Panda', 'Grizzly Bear', 'Koala', 'Red Panda']},
        'correct_index': 0,
        'correct_answer': {'uz': "Ulkan panda (Bambuk ayig'i)", 'ru': 'Большая панда', 'en': 'Giant Panda'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Giant_Panda_fur_texture.jpg/800px-Giant_Panda_fur_texture.jpg',
        'fun_fact': {   'uz': 'Panda kuniga 12 dan 38 kg gacha bambuk eydi va uning bilagida bambukni ushlash uchun '
                              'maxsus soxta bosh barmoq (sesamoid suyak) mavjud.',
                        'ru': 'У панды есть видоизмененная кость запястья («ложный шестой палец»), позволяющая ловко '
                              'удерживать стебли бамбука при еде.',
                        'en': 'Giant pandas possess an enlarged radial sesamoid wrist bone functioning as an opposable '
                              "'pseudo-thumb' to grasp bamboo stalks."},
        'aliases': ['panda', 'katta panda', 'панда', 'большая панда', 'giant panda']},
    {   'id': 'nature_emoji_018_hummingbird',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐦 + ⚡ + 🌺 + 🔄",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐦 + ⚡ + 🌺 + 🔄',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐦 + ⚡ + 🌺 + 🔄'},
        'options': {   'uz': ["Qaldirg'och", 'Kolibri', 'Kanareyka', "To'ti"],
                       'ru': ['Ласточка', 'Колибри', 'Канарейка', 'Попугай'],
                       'en': ['Swallow', 'Hummingbird', 'Canary', 'Parrot']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Kolibri', 'ru': 'Колибри', 'en': 'Hummingbird'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Hummingbird_hovering_macro.jpg/800px-Hummingbird_hovering_macro.jpg',
        'fun_fact': {   'uz': 'Kolibri yer yuzida orqaga qarab ucha oladigan yagona qush hisoblanadi; uning qanotlari '
                              'sakkiz raqami (∞) shaklida harakatlanadi.',
                        'ru': 'Колибри — единственные птицы, способные летать задом наперед и зависать на месте '
                              'благодаря восьмеркообразным движениям крыльев.',
                        'en': 'Hummingbirds are the only birds that can fly backwards and upside down, rotating their '
                              'wings in a horizontal figure-eight pattern.'},
        'aliases': ['kolibri', 'колибри', 'hummingbird']},
    {   'id': 'nature_emoji_019_koala',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐨 + 🌿 + 🇦🇺 + 😴",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐨 + 🌿 + 🇦🇺 + 😴',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐨 + 🌿 + 🇦🇺 + 😴'},
        'options': {   'uz': ['Kenguru', 'Vombat', 'Koala', 'Possum'],
                       'ru': ['Кенгуру', 'Вомбат', 'Коала', 'Опоссум'],
                       'en': ['Kangaroo', 'Wombat', 'Koala', 'Opossum']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Koala', 'ru': 'Коала', 'en': 'Koala'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Koala_fur_close_up.jpg/800px-Koala_fur_close_up.jpg',
        'fun_fact': {   'uz': "Koalalar ham xuddi odamlar kabi barmoq izlariga ega bo'lib, mikroskop ostida ularning "
                              'barmoq izini inson izidan ajratish deyarli imkonsizdir.',
                        'ru': 'Отпечатки пальцев коалы настолько похожи на человеческие, что их трудно различить даже '
                              'криминалистам под электронным микроскопом.',
                        'en': 'Koalas have epidermal friction ridge fingerprints so structurally identical to humans '
                              'that they can confuse forensic crime-scene scans.'},
        'aliases': ['koala', 'коала', 'koala']},
    {   'id': 'nature_emoji_020_red_kangaroo',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦘 + 🥊 + 👶 + 👝",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦘 + 🥊 + 👶 + 👝',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦘 + 🥊 + 👶 + 👝'},
        'options': {   'uz': ['Vombat', 'Koala', 'Vallabi', 'Qizil kenguru'],
                       'ru': ['Вомбат', 'Коала', 'Валлаби', 'Рыжий кенгуру'],
                       'en': ['Wombat', 'Koala', 'Wallaby', 'Red Kangaroo']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Qizil kenguru', 'ru': 'Рыжий кенгуру', 'en': 'Red Kangaroo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Macropus_rufus_red_kangaroo_hop.jpg/800px-Macropus_rufus_red_kangaroo_hop.jpg',
        'fun_fact': {   'uz': "Kenguru bolasi tug'ilganida atigi 2 santimetr bo'lib, ko'zlari ojiz holda onasining "
                              'juniga tirmashib qorin xaltasiga emaklab boradi.',
                        'ru': 'Новорожденный кенгуренок размером с вишневую косточку (2 см) самостоятельно проползает '
                              'путь по шерсти матери в сумку к соску.',
                        'en': 'A red kangaroo joey is born at jellybean size (~2 cm) and crawls unassisted through '
                              'maternal fur to latch onto a pouch teat.'},
        'aliases': ['kenguru', 'qizil kenguru', 'кенгуру', 'red kangaroo']},
    {   'id': 'nature_emoji_021_armadillo',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦔 + 🛡️ + ⚽ + 🌎",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦔 + 🛡️ + ⚽ + 🌎',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦔 + 🛡️ + ⚽ + 🌎'},
        'options': {   'uz': ['Bronenosets', 'Pangolin', 'Tipratikan', 'Toshbaqa'],
                       'ru': ['Трехпоясный броненосец', 'Панголин', 'Ёж', 'Черепаха'],
                       'en': ['Three-banded Armadillo', 'Pangolin', 'Hedgehog', 'Tortoise']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Bronenosets', 'ru': 'Трехпоясный броненосец', 'en': 'Three-banded Armadillo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Armadillo_carapace_macro.jpg/800px-Armadillo_carapace_macro.jpg',
        'fun_fact': {   'uz': "Uch belbog'li bronenosets xavf tug'ilganda boshi va dumini ichkariga qamrab, butunlay "
                              "o'q o'tmas koptok shakliga kirishga qodir yagona turdir.",
                        'ru': 'Трехпоясный броненосец — единственный броненосец, способный сворачиваться в абсолютно '
                              'замкнутый шар, защищенный броней.',
                        'en': 'Three-banded armadillos are the only armadillo species capable of rolling into a '
                              'completely sealed, predator-proof sphere.'},
        'aliases': ['bronenosets', 'броненосец', 'armadillo']},
    {   'id': 'nature_emoji_022_komodo_dragon',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦎 + 🐉 + 🏝️ + 🥩",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦎 + 🐉 + 🏝️ + 🥩',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦎 + 🐉 + 🏝️ + 🥩'},
        'options': {   'uz': ['Alligator', 'Komodo ajdahosi (Ulkan varan)', 'Timsoh', 'Iguana'],
                       'ru': ['Аллигатор', 'Комодский варан', 'Крокодил', 'Игуана'],
                       'en': ['Alligator', 'Komodo Dragon', 'Crocodile', 'Iguana']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Komodo ajdahosi (Ulkan varan)', 'ru': 'Комодский варан', 'en': 'Komodo Dragon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Varanus_komodoensis_dragon.jpg/800px-Varanus_komodoensis_dragon.jpg',
        'fun_fact': {   'uz': "Komodo varani yer yuzidagi eng yirik kaltakesak bo'lib, pastki jag'idagi zahar bezlari "
                              "o'lja qonini ivishini to'xtatib shokka tushiradi.",
                        'ru': 'Комодский варан достигает длины 3 метра; в его нижней челюсти находятся железы, '
                              'выделяющие токсичные белки, вызывающие коллапс.',
                        'en': "The Komodo dragon is the world's largest lizard, deploying lower jaw venom glands that "
                              'induce shock and stop blood clotting in large prey.'},
        'aliases': ['komodo varani', 'varan', 'комодский варан', 'варан', 'komodo dragon']},
    {   'id': 'nature_emoji_023_firefly',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🪲 + 💡 + 🌙 + ✨",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🪲 + 💡 + 🌙 + ✨',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🪲 + 💡 + 🌙 + ✨'},
        'options': {   'uz': ['Asalari', 'Ninachi', "Yoritqich qo'ng'iz (Svetlyachok)", 'Zlatka'],
                       'ru': ['Пчела', 'Стрекоза', 'Светлячок', 'Златка'],
                       'en': ['Honeybee', 'Dragonfly', 'Firefly (Lightning Bug)', 'Jewel Beetle']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Yoritqich qo'ng'iz (Svetlyachok)",
                              'ru': 'Светлячок',
                              'en': 'Firefly (Lightning Bug)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Lampyridae_firefly_bioluminescence.jpg/800px-Lampyridae_firefly_bioluminescence.jpg',
        'fun_fact': {   'uz': "Svetlyachokning nuri 100% 'sovuq yorug'lik' hisoblanadi; lampochkalardan farqli "
                              "o'laroq, unda energiyaning biror foizi ham issiqlikka aylanmaydi.",
                        'ru': 'Свечение светлячка имеет 100% КПД: реакция люциферина с кислородом при участии АТФ не '
                              'производит тепловых потерь.',
                        'en': 'Fireflies produce 100% cold light through enzymatic luciferase oxidation of luciferin, '
                              'dissipating virtually zero energy as heat.'},
        'aliases': ['svetlyachok', 'yoruglik qongizi', 'светлячок', 'firefly']},
    {   'id': 'nature_emoji_024_honey_badger',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦡 + 🍯 + 🐍 + 🛡️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦡 + 🍯 + 🐍 + 🛡️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦡 + 🍯 + 🐍 + 🛡️'},
        'options': {   'uz': ["Bo'rsiq", 'Skuns', 'Rosomaxa', "Asalxo'r (Medoyed)"],
                       'ru': ['Барсук', 'Скунс', 'Росомаха', 'Медоед'],
                       'en': ['Badger', 'Skunk', 'Wolverine', 'Honey Badger']},
        'correct_index': 3,
        'correct_answer': {'uz': "Asalxo'r (Medoyed)", 'ru': 'Медоед', 'en': 'Honey Badger'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Honey_badger_thick_skin_macro.jpg/800px-Honey_badger_thick_skin_macro.jpg',
        'fun_fact': {   'uz': "Ginnes rekordlari kitobida dunyodagi 'eng qo'rqmas hayvon' deb e'lon qilingan medoyed "
                              'kobra va qora mamba zahriga tabiiy immunitetga ega.',
                        'ru': 'Книга Гиннесса называет медоеда самым бесстрашным зверем планеты: после укуса '
                              'смертельной кобры он просто засыпает на пару часов и идет дальше.',
                        'en': "Ranked as the world's most fearless creature by Guinness, the honey badger shrugs off "
                              'lethal cobra bites via mutated nicotinic acetylcholine receptors.'},
        'aliases': ['asalxor', 'medoyed', 'медоед', 'honey badger']},
    {   'id': 'nature_emoji_025_giant_anteater',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐜 + 👅 + 🐜 + 🐾",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐜 + 👅 + 🐜 + 🐾',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐜 + 👅 + 🐜 + 🐾'},
        'options': {   'uz': ["Ulkan chumolixo'r", 'Pangolin', 'Yexidna', 'Armadillo'],
                       'ru': ['Гигантский муравьед', 'Панголин', 'Ехидна', 'Броненосец'],
                       'en': ['Giant Anteater', 'Pangolin', 'Echidna', 'Armadillo']},
        'correct_index': 0,
        'correct_answer': {'uz': "Ulkan chumolixo'r", 'ru': 'Гигантский муравьед', 'en': 'Giant Anteater'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Giant_anteater_coat_macro.jpg/800px-Giant_anteater_coat_macro.jpg',
        'fun_fact': {   'uz': "Chumolixo'rning tili 60 santimetrgacha cho'zilib, daqiqasiga 160 marta kirib-chiqadi; u "
                              'kuniga 35 000 ta chumoli va termitni yutadi.',
                        'ru': 'Язык муравьеда длиной 60 см совершает до 160 движений в минуту, покрываясь липкой '
                              'слюной для захвата 30 000 насекомых в день.',
                        'en': 'A giant anteater flicks its 60-cm saliva-coated tongue up to 160 times per minute, '
                              'consuming 35,000 ants and termites daily without teeth.'},
        'aliases': ['chumolixor', 'муравьед', 'гигантский муравьед', 'giant anteater']},
    {   'id': 'nature_emoji_026_humpback_whale',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌊 + 🐋 + 🎵 + 🐳",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌊 + 🐋 + 🎵 + 🐳',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌊 + 🐋 + 🎵 + 🐳'},
        'options': {   'uz': ["Ko'k kit", 'Bukri kit (Gorbatyy kit)', 'Kashalot', 'Narval'],
                       'ru': ['Синий кит', 'Горбатый кит', 'Кашалот', 'Нарвал'],
                       'en': ['Blue Whale', 'Humpback Whale', 'Sperm Whale', 'Narwhal']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Bukri kit (Gorbatyy kit)', 'ru': 'Горбатый кит', 'en': 'Humpback Whale'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Humpback_Whale_underwater_shot.jpg/800px-Humpback_Whale_underwater_shot.jpg',
        'fun_fact': {   'uz': "Erkak bukri kitlar okean bo'ylab bir necha soat davom etadigan murakkab 'qo'shiqlar' "
                              "kuylaydi va bu kuylar butun okean populyatsiyasi bo'ylab yangilanib turadi.",
                        'ru': 'Песни горбатых китов длятся часами и подчиняются законам музыкальной гармонии, '
                              'передаваясь через тысячи километров океана.',
                        'en': 'Male humpback whales compose complex, evolving acoustic songs lasting hours, '
                              'transmitted across entire ocean basins via acoustic sound channels.'},
        'aliases': ['bukri kit', 'gorbatyy kit', 'горбатый кит', 'humpback whale']},
    {   'id': 'nature_emoji_027_golden_eagle',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦅 + 👑 + 🏔️ + 🇲🇽",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦅 + 👑 + 🏔️ + 🇲🇽',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦅 + 👑 + 🏔️ + 🇲🇽'},
        'options': {   'uz': ['Lochin', 'Quriy', 'Burgut (Berkut)', 'Kondor'],
                       'ru': ['Сокол', 'Ястреб', 'Беркут', 'Кондор'],
                       'en': ['Falcon', 'Hawk', 'Golden Eagle', 'Condor']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Burgut (Berkut)', 'ru': 'Беркут', 'en': 'Golden Eagle'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Aquila_chrysaetos_golden_eagle.jpg/800px-Aquila_chrysaetos_golden_eagle.jpg',
        'fun_fact': {   'uz': "Burgut Markaziy Osiyo xalqlari tomonidan asrlar davomida bo'ri va kiyiklarni ovlash "
                              "uchun o'rgatib kelingan eng kuchli yirtqich qushdir.",
                        'ru': 'Беркут развивает скорость пикирования до 320 км/ч и способен одолеть взрослого волка '
                              'или лисицу благодаря сокрушительной хватке когтей.',
                        'en': 'With diving speeds up to 320 km/h and massive talons exerting 400 psi of pressure, '
                              'golden eagles are traditionally flown at wolves across Central Asia.'},
        'aliases': ['burgut', 'berkut', 'беркут', 'golden eagle']},
    {   'id': 'nature_emoji_028_snowy_owl',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦉 + ❄️ + 🤍 + 🧊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦉 + ❄️ + 🤍 + 🧊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦉 + ❄️ + 🤍 + 🧊'},
        'options': {   'uz': ['Boyqush', 'Lochin', "Qarg'a", 'Qutb boyqushi (Oq boyqush)'],
                       'ru': ['Филин', 'Кречет', 'Ворон', 'Белая (полярная) сова'],
                       'en': ['Barn Owl', 'Gyrfalcon', 'Raven', 'Snowy Owl']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Qutb boyqushi (Oq boyqush)', 'ru': 'Белая (полярная) сова', 'en': 'Snowy Owl'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Bubo_scandiacus_snowy_owl.jpg/800px-Bubo_scandiacus_snowy_owl.jpg',
        'fun_fact': {   'uz': "Boshqa boyqushlardan farqli o'laroq, oq boyqush Arktikaning qutb kunlari sharoitida "
                              'kunduzi ham faol ov qiladi va lemminglar bilan oziqlanadi.',
                        'ru': 'В отличие от ночных сов, полярная сова охотится днем в условиях бесконечного полярного '
                              'дня тундры.',
                        'en': 'Unlike most nocturnal owls, the snowy owl hunts by daylight during the continuous '
                              'sunshine of Arctic tundra summers.'},
        'aliases': ['oq boyqush', 'qutb boyqushi', 'белая сова', 'полярная сова', 'snowy owl']},
    {   'id': 'nature_emoji_029_beaver',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦫 + 🪵 + 🌊 + 🪓",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦫 + 🪵 + 🌊 + 🪓',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦫 + 🪵 + 🌊 + 🪓'},
        'options': {   'uz': ['Qunduz (Bobr)', 'Ondatra', 'Nutriya', 'Suvsar'],
                       'ru': ['Обыкновенный бобр', 'Ондатра', 'Нутрия', 'Выдра'],
                       'en': ['Beaver', 'Muskrat', 'Nutria', 'Otter']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Qunduz (Bobr)', 'ru': 'Обыкновенный бобр', 'en': 'Beaver'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Castor_fiber_beaver_dam.jpg/800px-Castor_fiber_beaver_dam.jpg',
        'fun_fact': {   'uz': "Qunduzning to'q sariq tishlari temir minerallari bilan mustahkamlangan bo'lib, daraxt "
                              "yog'ochini kesishda hech qachon to'planib sinmaydi.",
                        'ru': 'Оранжевый цвет резцов бобра объясняется высоким содержанием железа в эмали, делающим '
                              'зубы тверже легированной стали.',
                        'en': "A beaver's incisors are infused with iron compounds that turn the enamel orange, "
                              'conferring acid-resistant self-sharpening chisel strength.'},
        'aliases': ['qunduz', 'bobr', 'бобр', 'beaver']},
    {   'id': 'nature_emoji_030_flying_squirrel',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐿️ + 🪂 + 🌲 + 🌙",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐿️ + 🪂 + 🌲 + 🌙',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐿️ + 🪂 + 🌲 + 🌙'},
        'options': {   'uz': ['Oddiy sincob', 'Uchar sincob (Letyaga)', "Ko'rshapalak", 'Possum'],
                       'ru': ['Обыкновенная белка', 'Обыкновенная летяга', 'Летучая мышь', 'Опоссум'],
                       'en': ['Tree Squirrel', 'Siberian Flying Squirrel', 'Bat', 'Opossum']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Uchar sincob (Letyaga)',
                              'ru': 'Обыкновенная летяга',
                              'en': 'Siberian Flying Squirrel'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Pteromys_volans_flying_squirrel.jpg/800px-Pteromys_volans_flying_squirrel.jpg',
        'fun_fact': {   'uz': 'Letyaga old va orqa oyoqlari orasidagi terili patagiy pardasi yordamida daraxtdan '
                              'daraxtga 50–90 metr masofaga bemalol parvoz qiladi.',
                        'ru': 'Летяга планирует между деревьями на расстояние до 90 метров, используя пушистый хвост '
                              'как руль и тормозной парашют.',
                        'en': 'Flying squirrels maneuver through dense boreal forest canopies on parachute-like '
                              'patagial membranes, gliding over 90 meters.'},
        'aliases': ['uchar sincob', 'letyaga', 'летяга', 'flying squirrel']},
    {   'id': 'nature_emoji_031_fennec_fox',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐱 + 🏜️ + 👂👂",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐱 + 🏜️ + 👂👂',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐱 + 🏜️ + 👂👂'},
        'options': {   'uz': ['Korsak', 'Chiyobori', 'Fenek tulkisi', 'Pesets'],
                       'ru': ['Корсак', 'Шакал', 'Фенек', 'Песец'],
                       'en': ['Corsac Fox', 'Jackal', 'Fennec Fox', 'Arctic Fox']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Fenek tulkisi', 'ru': 'Фенек', 'en': 'Fennec Fox'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Vulpes_zerda_fennec_fox.jpg/800px-Vulpes_zerda_fennec_fox.jpg',
        'fun_fact': {   'uz': 'Fenekning 15 sm li ulkan quloqlari qum ostidagi hasharotlar qimirlashini eshitish bilan '
                              "birga Sahroi Kabir issig'ida tanani sovutadi.",
                        'ru': 'Огромные уши фенека служат радиаторами для охлаждения крови под палящим солнцем Сахары.',
                        'en': 'The 15-cm ears of the fennec fox radiate body heat and locate subterranean insects '
                              'moving beneath desert sands.'},
        'aliases': ['fenek', 'фенек', 'fennec fox']},
    {   'id': 'nature_emoji_032_quagga',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐴 + 🦓 + 🖤",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐴 + 🦓 + 🖤',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐴 + 🦓 + 🖤'},
        'options': {   'uz': ['Zebra', 'Ot', 'Eshak', 'Kvakka (Quagga)'],
                       'ru': ['Зебра', 'Лошадь', 'Осел', 'Квагга'],
                       'en': ['Zebra', 'Horse', 'Donkey', 'Quagga']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Kvakka (Quagga)', 'ru': 'Квагга', 'en': 'Quagga'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Quagga_photo_1870.jpg/800px-Quagga_photo_1870.jpg',
        'fun_fact': {   'uz': "Kvakkaning faqat old qismi zebradek chiziqli bo'lib, orqa qismi oddiy qo'ng'ir otga "
                              "o'xshagan; u XIX asr oxirida butunlay qirib yuborilgan.",
                        'ru': 'Квагга имела полосы только спереди, напоминая сзади лошадь; вид был полностью истреблен '
                              'человеком в 1883 году.',
                        'en': 'The extinct quagga displayed zebra stripes only on its head and neck, transitioning '
                              'into a plain brown equine coat.'},
        'aliases': ['kvakka', 'квагга', 'quagga']},
    {   'id': 'nature_emoji_033_dodo',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦤 + 🏝️ + 🪦",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦤 + 🏝️ + 🪦',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦤 + 🏝️ + 🪦'},
        'options': {   'uz': ['Dodo qushi (Dront)', 'Kivi', 'Straus', 'Pingvin'],
                       'ru': ['Маврикийский дронт (Додо)', 'Киви', 'Страус', 'Пингвин'],
                       'en': ['Dodo', 'Kiwi', 'Ostrich', 'Penguin']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Dodo qushi (Dront)', 'ru': 'Маврикийский дронт (Додо)', 'en': 'Dodo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Raphus_cucullatus_dodo_model.jpg/800px-Raphus_cucullatus_dodo_model.jpg',
        'fun_fact': {   'uz': "Mavrikiy orolida yirtqichlarsiz yashagan dodo odamlardan mutlaqo qo'rqmagan va shu "
                              'sababli XVII asrda dengizchilar tomonidan qisqa muddatda qirib bitirilgan.',
                        'ru': 'Додо не умел летать и не боялся людей, став всемирным символом вымирания видов по вине '
                              'человеческой беспечности.',
                        'en': 'Endemic to Mauritius, the flightless dodo lacked innate fear of humans and was hunted '
                              'to extinction within decades of discovery.'},
        'aliases': ['dodo', 'dront', 'додо', 'дронт', 'dodo bird']},
    {   'id': 'nature_emoji_034_woolly_mammoth',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐘 + ❄️ + 🪨 + 🦴",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐘 + ❄️ + 🪨 + 🦴',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐘 + ❄️ + 🪨 + 🦴'},
        'options': {   'uz': ['Afrika fili', 'Junli mamont', 'Mastodont', 'Karkidon'],
                       'ru': ['Африканский слон', 'Шерстистый мамонт', 'Мастодонт', 'Шерстистый носорог'],
                       'en': ['African Elephant', 'Woolly Mammoth', 'Mastodon', 'Woolly Rhino']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Junli mamont', 'ru': 'Шерстистый мамонт', 'en': 'Woolly Mammoth'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Mammuthus_primigenius_reconstruction.jpg/800px-Mammuthus_primigenius_reconstruction.jpg',
        'fun_fact': {   'uz': "Mamontning 1 metrli qalin juni va 10 sm lik yog' qatlami unga Pleystotsen muzlik "
                              'davrining -50 °C sovuqlarida yashash imkonini bergan.',
                        'ru': 'Мамонты обладали изогнутыми 4-метровыми бивнями для разгребания снега и кровью с особым '
                              'морозостойким гемоглобином.',
                        'en': 'Woolly mammoths featured 4-meter curved tusks to clear snowpack and antifreeze '
                              'hemoglobin that unloaded oxygen in sub-zero cold.'},
        'aliases': ['mamont', 'мамонт', 'woolly mammoth']},
    {   'id': 'nature_emoji_035_maned_wolf',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐺 + 🌿 + 🦵 + 🦊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐺 + 🌿 + 🦵 + 🦊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐺 + 🌿 + 🦵 + 🦊'},
        'options': {   'uz': ["Bo'ri", 'Chiyobori', "Yolli bo'ri", 'Dingo'],
                       'ru': ['Серый волк', 'Шакал', 'Гривистый волк', 'Динго'],
                       'en': ['Gray Wolf', 'Jackal', 'Maned Wolf', 'Dingo']},
        'correct_index': 2,
        'correct_answer': {'uz': "Yolli bo'ri", 'ru': 'Гривистый волк', 'en': 'Maned Wolf'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Chrysocyon_brachyurus_maned_wolf.jpg/800px-Chrysocyon_brachyurus_maned_wolf.jpg',
        'fun_fact': {   'uz': "Yolli bo'rining g'ayritabiiy uzun oyoqlari baland Janubiy Amerika pampas o'tloqlari "
                              "ustidan atrofni ko'rish uchun moslashgan.",
                        'ru': 'Непропорционально длинные ходульные лапы гривистого волка помогают ему высматривать '
                              'грызунов над высокой травой саванн серрадо.',
                        'en': 'The stilt-like long legs of the maned wolf are an evolutionary adaptation for peering '
                              'over tall savanna grasses in the Brazilian Cerrado.'},
        'aliases': ['yolli bori', 'гривистый волк', 'maned wolf']},
    {   'id': 'nature_emoji_036_glowworm',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🪱 + 💡 + 🌌 + 🕳️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🪱 + 💡 + 🌌 + 🕳️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🪱 + 💡 + 🌌 + 🕳️'},
        'options': {   'uz': ['Svetlyachok', 'Chayon', 'Qirkayoq', "Yorug'lik chuvalchangi (Arachnocampa)"],
                       'ru': ['Светлячок', 'Скорпион', 'Многоножка', 'Светящийся пещерный червь'],
                       'en': ['Firefly', 'Scorpion', 'Centipede', 'Glowworm (Arachnocampa)']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Yorug'lik chuvalchangi (Arachnocampa)",
                              'ru': 'Светящийся пещерный червь',
                              'en': 'Glowworm (Arachnocampa)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Waitomo_glowworm_cave_ceiling.jpg/800px-Waitomo_glowworm_cave_ceiling.jpg',
        'fun_fact': {   'uz': "Yangi Zelandiyaning Vaytomo g'orlarida yashovchi bu lichinkalar shiftda yulduzli osmon "
                              'kabi moviy nur taratib, yopishqoq iplari bilan hasharotlarni tutadi.',
                        'ru': 'Личинки Arachnocampa освещают своды пещер Вайтомо сапфировым светом, привлекая мошек в '
                              'шелковые липкие сети-ловушки.',
                        'en': 'Arachnocampa luminosa larvae illuminate Waitomo Cave ceilings like a galaxy of stars, '
                              'dangling sticky silk fishing lines to ensnare insects.'},
        'aliases': ['yoruglik chuvalchangi', 'пещерный червь', 'glowworm']},
    {   'id': 'nature_emoji_037_bamboo',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🎋 + 🎍 + 🚀 + 📈",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🎋 + 🎍 + 🚀 + 📈',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🎋 + 🎍 + 🚀 + 📈'},
        'options': {   'uz': ['Bambuk', 'Shakarqamish', 'Sekvoya', 'Papirus'],
                       'ru': ['Бамбук', 'Сахарный тростник', 'Секвойя', 'Папирус'],
                       'en': ['Bamboo', 'Sugarcane', 'Redwood', 'Papyrus']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Bambuk', 'ru': 'Бамбук', 'en': 'Bamboo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Bamboo_forest_kyoto.jpg/800px-Bamboo_forest_kyoto.jpg',
        'fun_fact': {   'uz': "Bambuk yer yuzidagi eng tez o'suvchi o'simlik bo'lib, bir sutkada 91 santimetrgacha "
                              "(soatiga qariyb 4 sm) bo'y cho'za oladi.",
                        'ru': 'Бамбук растет со скоростью до 91 см в сутки (около 4 см в час), издавая слышимый скрип '
                              'при стремительном росте стебля.',
                        'en': 'Certain bamboo species can grow up to 91 cm (35 inches) within a single 24-hour period, '
                              'holding the Guinness plant growth record.'},
        'aliases': ['bambuk', 'бамбук', 'bamboo']},
    {   'id': 'nature_emoji_038_saguaro',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌵 + 🏜️ + 👑 + 🇺🇸",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌵 + 🏜️ + 👑 + 🇺🇸',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌵 + 🏜️ + 👑 + 🇺🇸'},
        'options': {   'uz': ['Agava', 'Saguaro kaktusi', 'Aloe', 'Baobab'],
                       'ru': ['Агава', 'Кактус Сагуаро (Карнегия)', 'Алоэ', 'Баобаб'],
                       'en': ['Agave', 'Saguaro Cactus', 'Aloe', 'Baobab']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Saguaro kaktusi', 'ru': 'Кактус Сагуаро (Карнегия)', 'en': 'Saguaro Cactus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Carnegiea_gigantea_saguaro_cactus.jpg/800px-Saguaro_cactus.jpg',
        'fun_fact': {   'uz': "Saguaro kaktusi 200 yilgacha yashaydi va bitta yomg'irli mavsumda o'z tanasiga 3000 "
                              "litrgacha suv jamg'ara oladi.",
                        'ru': 'Гигантский кактус сагуаро весит до 2 тонн после ливня, накапливая тонны влаги в '
                              'гармошкообразном стволе на случай засухи.',
                        'en': 'A mature Carnegiea gigantea can absorb and store over 3,000 liters of water during '
                              'desert rainstorms, weighing several tons.'},
        'aliases': ['saguaro', 'сагуаро', 'saguaro cactus']},
    {   'id': 'nature_emoji_039_baobab',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌳 + 💧 + 🧴 + 🇲🇬",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌳 + 💧 + 🧴 + 🇲🇬',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌳 + 💧 + 🧴 + 🇲🇬'},
        'options': {   'uz': ['Sekvoya', 'Dub', 'Baobab daraxti', 'Evkalipt'],
                       'ru': ['Секвойя', 'Дуб', 'Баобаб', 'Эвкалипт'],
                       'en': ['Giant Sequoia', 'Oak', 'Baobab Tree', 'Eucalyptus']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Baobab daraxti', 'ru': 'Баобаб', 'en': 'Baobab Tree'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Adansonia_grandidieri_baobabs_madagascar.jpg/800px-Baobab_avenue_madagascar.jpg',
        'fun_fact': {   'uz': "Baobabning yo'g'on shishasimon tanasi 120 000 litrgacha suvni shimgich kabi o'zida "
                              "saqlab qurg'oqchilikdan omon chiqadi.",
                        'ru': 'Ствол африканского баобаба может удерживать до 120 000 литров пресной воды, напоминая '
                              'гигантский природный резервуар.',
                        'en': 'Adansonia baobab trunks can swell to store up to 120,000 liters of water inside spongy '
                              'wood cells to endure multi-year droughts.'},
        'aliases': ['baobab', 'баобаб', 'baobab tree']},
    {   'id': 'nature_emoji_040_fly_agaric',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🍄 + ☠️ + 🔴 + ⚪",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🍄 + ☠️ + 🔴 + ⚪',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🍄 + ☠️ + 🔴 + ⚪'},
        'options': {   'uz': ["Oq qo'ziqorin", 'Shampinyon', 'Trilits', "Qizil pashshaxo'r (Muxomor)"],
                       'ru': ['Белый гриб', 'Шампиньон', 'Бледная поганка', 'Красный мухомор'],
                       'en': ['Porcini', 'Button Mushroom', 'Death Cap', 'Fly Agaric (Amanita muscaria)']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Qizil pashshaxo'r (Muxomor)",
                              'ru': 'Красный мухомор',
                              'en': 'Fly Agaric (Amanita muscaria)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Amanita_muscaria_3_vmsp.jpg/800px-Amanita_muscaria_3_vmsp.jpg',
        'fun_fact': {   'uz': "Muxomorning qizil qalpog'idagi oq xollar yosh qo'ziqorinni o'ragan umumiy yopinchiq "
                              'pardaning (volva) qoldiqlari hisoblanadi.',
                        'ru': 'Белые точки на шляпке мухомора — это обрывки защитного покрывала, разрывающегося по '
                              'мере созревания плодового тела гриба.',
                        'en': 'The iconic white warts on Amanita muscaria are fragments of the universal veil torn '
                              'apart as the red pileus expands.'},
        'aliases': ['muxomor', 'мухомор', 'fly agaric', 'amanita muscaria']},
    {   'id': 'nature_emoji_041_bristlecone_pine',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌲 + 🏛️ + ⏳ + 🏔️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌲 + 🏛️ + ⏳ + 🏔️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌲 + 🏛️ + ⏳ + 🏔️'},
        'options': {   'uz': ["Qadimgi qarag'ay (Metuselah)", 'Sekvoya', 'Kedr', 'Lipa'],
                       'ru': ['Остистая сосна (Мафусаил)', 'Секвойя', 'Кедр', 'Липа'],
                       'en': ['Bristlecone Pine (Methuselah)', 'Redwood', 'Cedar', 'Linden']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Qadimgi qarag'ay (Metuselah)",
                              'ru': 'Остистая сосна (Мафусаил)',
                              'en': 'Bristlecone Pine (Methuselah)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Pinus_longaeva_bristlecone_pine.jpg/800px-Bristlecone_pine.jpg',
        'fun_fact': {   'uz': "Kaliforniyaning Oq tog'larida o'suvchi Metuselah qarag'ayi 4850 yoshdan oshgan va u "
                              'Misr piramidalaridan ham qadimiyroqdir.',
                        'ru': 'Сосна Мафусаил проросла около 2832 года до н.э.; ее смолистая плотная древесина '
                              'практически не гниет и устойчива к вредителям.',
                        'en': "Pinus longaeva specimen 'Methuselah' is over 4,850 years old, germinating before the "
                              "construction of Egypt's Great Pyramid."},
        'aliases': ['qaragay', 'metuselah', 'остистая сосна', 'мафусаил', 'bristlecone pine']},
    {   'id': 'nature_emoji_042_giant_sequoia',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌲 + 👑 + 🇺🇸 + 🪵",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌲 + 👑 + 🇺🇸 + 🪵',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌲 + 👑 + 🇺🇸 + 🪵'},
        'options': {   'uz': ['Baobab', 'Ulkan sekvoyadendron (General Sherman)', "Qarag'ay", 'Eman'],
                       'ru': ['Баобаб', 'Секвойядендрон (Генерал Шерман)', 'Сосна', 'Дуб'],
                       'en': ['Baobab', 'Giant Sequoia', 'Pine', 'Oak']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Ulkan sekvoyadendron (General Sherman)',
                              'ru': 'Секвойядендрон (Генерал Шерман)',
                              'en': 'Giant Sequoia'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/General_Sherman_tree_sequoia.jpg/800px-General_Sherman_tree_sequoia.jpg',
        'fun_fact': {   'uz': "General Sherman nomli sekvoya yer yuzidagi eng yirik yakka daraxt bo'lib, uning yog'och "
                              'hajmi 1487 kub metrni tashkil qiladi.',
                        'ru': 'Дерево «Генерал Шерман» весит около 2000 тонн при объеме древесины 1487 м³, являясь '
                              'крупнейшим живым организмом по массе древесины.',
                        'en': 'The General Sherman giant sequoia holds the world record as the largest living stem '
                              'volume at 1,487 cubic meters.'},
        'aliases': ['sekvoya', 'генерал шерман', 'секвойя', 'giant sequoia']},
    {   'id': 'nature_emoji_043_mimosa_pudica',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌿 + 🏃 + 🫣 + 👆",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌿 + 🏃 + 🫣 + 👆',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌿 + 🏃 + 🫣 + 👆'},
        'options': {   'uz': ['Bambuk', 'Kaktus', 'Uychi mimoza (Mimosa pudica)', 'Lotos'],
                       'ru': ['Бамбук', 'Кактус', 'Стыдливая мимоза', 'Лотос'],
                       'en': ['Bamboo', 'Cactus', 'Sensitive Plant (Mimosa pudica)', 'Lotus']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Uychi mimoza (Mimosa pudica)',
                              'ru': 'Стыдливая мимоза',
                              'en': 'Sensitive Plant (Mimosa pudica)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Mimosa_pudica_folding_leaves.jpg/800px-Mimosa_pudica_folding_leaves.jpg',
        'fun_fact': {   'uz': "Mimoza bargiga qo'l tekkizilganda hujayralardagi kaliy va suv tezda chiqib ketib, "
                              'barglar soniyalar ichida yopilib osilib qoladi.',
                        'ru': 'При механическом касании мимоза мгновенно сбрасывает тургорное давление в сочленениях '
                              'черешков, складывая листочки.',
                        'en': 'Mimosa pudica undergoes rapid seismonastic leaf folding within seconds of mechanical '
                              'touch via potassium ion efflux.'},
        'aliases': ['mimoza', 'uychi mimoza', 'стыдливая мимоза', 'мимоза', 'mimosa pudica']},
    {   'id': 'nature_emoji_044_pitcher_plant',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌿 + 🥩 + 🏺 + 🪰",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌿 + 🥩 + 🏺 + 🪰',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌿 + 🥩 + 🏺 + 🪰'},
        'options': {   'uz': ['Rosyanka', 'Muxomor', 'Kaktus', "Nepentes (Ko'zasimon o'simlik)"],
                       'ru': ['Росянка', 'Мухомор', 'Кактус', 'Непентес (Кувшиночник)'],
                       'en': ['Sundew', 'Fly Agaric', 'Cactus', 'Pitcher Plant (Nepenthes)']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Nepentes (Ko'zasimon o'simlik)",
                              'ru': 'Непентес (Кувшиночник)',
                              'en': 'Pitcher Plant (Nepenthes)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Nepenthes_rajah_pitcher_plant.jpg/800px-Nepenthes_rajah_pitcher_plant.jpg',
        'fun_fact': {   'uz': "Nepenthes rajah ko'zalariga 3 litrgacha ovqat hazm qilish suyuqligi sig'adi va unga "
                              "ba'zan qurbaqalar hamda mayda kalamushlar tushib qoladi.",
                        'ru': 'Кувшинчики Nepenthes rajah на Борнео вмещают до 3,5 литра жидкости и способны '
                              'переваривать не только насекомых, но и мышей.',
                        'en': 'Nepenthes rajah urns hold up to 3.5 liters of enzymatic digestive fluid, occasionally '
                              'trapping small frogs, lizards, and rodents.'},
        'aliases': ['nepentes', 'непентес', 'кувшиночник', 'pitcher plant', 'nepenthes']},
    {   'id': 'nature_emoji_045_flying_fish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐟 + 🪂 + 🌊 + ✈️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐟 + 🪂 + 🌊 + ✈️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐟 + 🪂 + 🌊 + ✈️'},
        'options': {   'uz': ['Uchar baliq (Exocoetidae)', 'Qilichbaliq', 'Kambala', 'Skumbriya'],
                       'ru': ['Летучая рыба', 'Меч-рыба', 'Камбала', 'Скумбрия'],
                       'en': ['Flying Fish', 'Swordfish', 'Flounder', 'Mackerel']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Uchar baliq (Exocoetidae)', 'ru': 'Летучая рыба', 'en': 'Flying Fish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Exocoetidae_flying_fish_glide.jpg/800px-Exocoetidae_flying_fish_glide.jpg',
        'fun_fact': {   'uz': 'Uchar baliq dumi bilan suvni soniyasiga 70 marta urib, suvdan otilib chiqadi va keng '
                              'qanotsimon suzgichlari yordamida havoda 400 metrgacha planirlab uchadi.',
                        'ru': 'Летучие рыбы глиссируют над волнами со скоростью 60 км/ч на высоте до 6 метров, '
                              'спасаясь от хищных тунцов и дельфинов.',
                        'en': 'Flying fish taxi across wave crests with caudal fin beats at 70 Hz, launching into '
                              'aerodynamic glides covering up to 400 meters.'},
        'aliases': ['uchar baliq', 'летучая рыба', 'flying fish']},
    {   'id': 'nature_emoji_046_swordfish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐟 + ⚔️ + ⚡ + 🌊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐟 + ⚔️ + ⚡ + 🌊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐟 + ⚔️ + ⚡ + 🌊'},
        'options': {   'uz': ['Akula', 'Qilichbaliq (Xiphias gladius)', 'Karp', 'Treska'],
                       'ru': ['Акула', 'Меч-рыба', 'Карп', 'Треска'],
                       'en': ['Shark', 'Swordfish', 'Carp', 'Cod']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qilichbaliq (Xiphias gladius)', 'ru': 'Меч-рыба', 'en': 'Swordfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Xiphias_gladius_swordfish_specimen.jpg/800px-Swordfish.jpg',
        'fun_fact': {   'uz': "Qilichbaliq o'zining yassi qilichsimon burni bilan o'ljani sanchmaydi, balki baliqlar "
                              "to'dasi ichida qilichdek siltab ularni mayib qiladi.",
                        'ru': 'Меч-рыба глушит кальмаров и макрель рубящими ударами острого рострума, после чего '
                              'спокойно заглатывает добычу.',
                        'en': 'Swordfish use their sharp flat bill like a broadsword to slash and stun schooling squid '
                              'and mackerel rather than spearing them.'},
        'aliases': ['qilichbaliq', 'меч-рыба', 'swordfish']},
    {   'id': 'nature_emoji_047_box_jellyfish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? \U0001fabc + 📦 + ☠️ + "
                              '🌊',
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? \U0001fabc + 📦 + ☠️ '
                              '+ 🌊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? \U0001fabc + 📦 + ☠️ + '
                              '🌊'},
        'options': {   'uz': ['Moviy meduza', 'Aktiniya', 'Qutisimon meduza (Morska osa)', 'Polip'],
                       'ru': ['Аурелия', 'Актиния', 'Морская оса (Кубомедуза)', 'Гидра'],
                       'en': ['Moon Jellyfish', 'Sea Anemone', 'Box Jellyfish (Chironex)', 'Hydra']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Qutisimon meduza (Morska osa)',
                              'ru': 'Морская оса (Кубомедуза)',
                              'en': 'Box Jellyfish (Chironex)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Chironex_fleckeri_box_jellyfish.jpg/800px-Chironex_fleckeri_box_jellyfish.jpg',
        'fun_fact': {   'uz': "Kubomeduzaning 24 ta ko'zi bo'lib, ulardan 4 tasida haqiqiy linza va to'r parda mavjud, "
                              'u shunchaki oqimda oqmay, maqsadli suza oladi.',
                        'ru': 'Кубомедуза обладает 24 сложными глазами с роговицей и сетчаткой, ориентируясь на '
                              'мангровые заросли и свет солнца.',
                        'en': 'Box jellyfish boast 24 sophisticated eyes, including complex lens-bearing rhopalia '
                              'capable of genuine image formation.'},
        'aliases': ['qutisimon meduza', 'морская оса', 'box jellyfish']},
    {   'id': 'nature_emoji_048_walrus',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦭 + 🦷🦷 + ❄️ + 🧊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦭 + 🦷🦷 + ❄️ + 🧊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦭 + 🦷🦷 + ❄️ + 🧊'},
        'options': {   'uz': ['Tyulen', 'Kalan', 'Beluxa', 'Morj'],
                       'ru': ['Нерпа', 'Калан', 'Белуха', 'Морж'],
                       'en': ['Ringed Seal', 'Sea Otter', 'Beluga', 'Walrus']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Morj', 'ru': 'Морж', 'en': 'Walrus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Walrus_skin_folds_macro.jpg/800px-Walrus_skin_folds_macro.jpg',
        'fun_fact': {   'uz': "Morj o'zining 1 metrli ulkan qoziq tishlari yordamida muz ustiga chiqadi va dengiz "
                              'tubidagi mollyuskalarni qidiradi.',
                        'ru': 'Бивни моржа служат ледорубами при вылезании на льдины («ходящие зубами») и оружием в '
                              'турнирных боях самцов.',
                        'en': 'Walruses use their meter-long tusks to haul their 1.5-ton bodies onto pack ice floes, '
                              "earning the scientific name Odobenus ('tooth-walker')."},
        'aliases': ['morj', 'морж', 'walrus']},
    {   'id': 'nature_emoji_049_sea_otter',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦦 + 🌊 + 🪨 + 🦪",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦦 + 🌊 + 🪨 + 🦪',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦦 + 🌊 + 🪨 + 🦪'},
        'options': {   'uz': ['Dengiz qunduzi (Kalan)', 'Oddiy qunduz', 'Tyulen', 'Norka'],
                       'ru': ['Калан (Морская выдра)', 'Речной бобр', 'Тюлень', 'Норка'],
                       'en': ['Sea Otter', 'River Beaver', 'Harbor Seal', 'Mink']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Dengiz qunduzi (Kalan)', 'ru': 'Калан (Морская выдра)', 'en': 'Sea Otter'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Sea_otter_fur_density_macro.jpg/800px-Sea_otter_fur_density_macro.jpg',
        'fun_fact': {   'uz': 'Kalanlar dengiz tipratikani va qisqichbaqalarni tosh ustiga urib chaqish uchun tosh '
                              'qurollaridan foydalanadigan kam sonli hayvonlardan biridir.',
                        'ru': 'Калан плавает на спине, положив плоский камень на грудь, и разбивает о него твердые '
                              'панцири моллюсков и морских ежей.',
                        'en': 'Sea otters float on their backs using rocks balanced on their chests as anvils to crack '
                              'open sea urchins and abalone shells.'},
        'aliases': ['kalan', 'dengiz qunduzi', 'калан', 'sea otter']},
    {   'id': 'nature_emoji_050_skunk',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦨 + 💨 + 🦨 + 👃🤢",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦨 + 💨 + 🦨 + 👃🤢',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦨 + 💨 + 🦨 + 👃🤢'},
        'options': {   'uz': ['Yenot', "Yo'l-yo'l skuns", "Bo'rsiq", 'Possum'],
                       'ru': ['Енот', 'Полосатый скунс', 'Барсук', 'Опоссум'],
                       'en': ['Raccoon', 'Striped Skunk', 'Badger', 'Opossum']},
        'correct_index': 1,
        'correct_answer': {'uz': "Yo'l-yo'l skuns", 'ru': 'Полосатый скунс', 'en': 'Striped Skunk'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Mephitis_mephitis_striped_skunk.jpg/800px-Mephitis_mephitis_striped_skunk.jpg',
        'fun_fact': {   'uz': 'Skunsning anal bezlaridagi oltingugurtli tiollar 3 metr masofagacha purkaladi va '
                              "yirtqichni bir necha kunga ko'r va hid sezmas qilib qo'yishi mumkin.",
                        'ru': 'Струя секрета скунса содержит тиолы с запахом тухлых яиц и чеснока, поражая цель на '
                              'расстоянии до 3-5 метров.',
                        'en': 'A striped skunk accurately sprays volatile sulfuric butyl mercaptans up to 3 meters, '
                              'causing temporary blindness and intense nausea.'},
        'aliases': ['skuns', 'скунс', 'striped skunk', 'skunk']},
    {   'id': 'nature_emoji_051_bison',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦬 + 🇺🇸 + 🌾 + 🦬",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦬 + 🇺🇸 + 🌾 + 🦬',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦬 + 🇺🇸 + 🌾 + 🦬'},
        'options': {   'uz': ['Buloqa', "Yovvoyi qo'tos", 'Amerika bizoni', 'Antilopa'],
                       'ru': ['Зубр', 'Дикий як', 'Американский бизон', 'Антилопа'],
                       'en': ['European Bison', 'Wild Yak', 'American Bison', 'Wildebeest']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Amerika bizoni', 'ru': 'Американский бизон', 'en': 'American Bison'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/American_bison_kansas.jpg/800px-American_bison_kansas.jpg',
        'fun_fact': {   'uz': 'Bizon 1 tonna tosh bossa-da, soatiga 55 km tezlikda yugurib, 1.8 metr balandlikdagi '
                              "to'siqlardan sakrab o'ta oladi.",
                        'ru': 'Несмотря на тонну веса, бизон легко перепрыгивает двухметровые заборы и разгоняется '
                              'быстрее скаковой лошади.',
                        'en': 'Weighing up to 1,000 kg, American bison can sprint at 55 km/h (35 mph) and jump '
                              'vertical obstacles up to 1.8 meters high.'},
        'aliases': ['bizon', 'бизон', 'american bison']},
    {   'id': 'nature_emoji_052_llama',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦙 + 🏔️ + 🇵🇪 + 🦙",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦙 + 🏔️ + 🇵🇪 + 🦙',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦙 + 🏔️ + 🇵🇪 + 🦙'},
        'options': {   'uz': ['Alpaka', 'Tuya', 'Vikunya', 'Lama (Llama)'],
                       'ru': ['Альпака', 'Верблюд', 'Викунья', 'Лама'],
                       'en': ['Alpaca', 'Camel', 'Vicuña', 'Llama']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Lama (Llama)', 'ru': 'Лама', 'en': 'Llama'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Lama_glama_peru.jpg/800px-Lama_glama_peru.jpg',
        'fun_fact': {   'uz': "Lama xafa bo'lganda yoki xavf sezganda oshqozonidagi yarim hazm bo'lgan o't sharbatini "
                              '3 metr masofagacha dushmanga qarab tupuradi.',
                        'ru': 'Раздраженная лама метко плюется содержимым своего первого преджелудка на расстояние до '
                              'трех метров.',
                        'en': 'When agitated, a llama accurately regurgitates and spits green acidic stomach contents '
                              "up to 3 meters into an intruder's face."},
        'aliases': ['lama', 'лама', 'llama']},
    {   'id': 'nature_emoji_053_alpaca',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦙 + 🧶 + 🇵🇪 + 🧣",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦙 + 🧶 + 🇵🇪 + 🧣',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦙 + 🧶 + 🇵🇪 + 🧣'},
        'options': {   'uz': ['Alpaka', 'Lama', 'Vikunya', "Qo'y"],
                       'ru': ['Альпака', 'Лама', 'Викунья', 'Овца'],
                       'en': ['Alpaca', 'Llama', 'Vicuña', 'Sheep']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Alpaka', 'ru': 'Альпака', 'en': 'Alpaca'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Alpaca_fleece_fiber_macro.jpg/800px-Alpaca_fleece_fiber_macro.jpg',
        'fun_fact': {   'uz': "Alpaka lamadan kichikroq bo'lib, faqat o'zining mayin gipoallergen yungi uchun "
                              'parvarish qilinadi.',
                        'ru': 'Шерсть альпаки в 7 раз теплее овечьей, не колется и насчитывает 22 природных оттенка от '
                              'чисто белого до черного.',
                        'en': 'Alpacas were bred by the Incas specifically for their fleece, which is hypoallergenic, '
                              'flame-resistant, and hollow-cored.'},
        'aliases': ['alpaka', 'альпака', 'alpaca']},
    {   'id': 'nature_emoji_054_reindeer',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦌 + 🎅 + ❄️ + 🛷",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦌 + 🎅 + ❄️ + 🛷',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦌 + 🎅 + ❄️ + 🛷'},
        'options': {   'uz': ['Maral', "Shimol bug'usi (Karibu)", 'Los', 'Kiyik'],
                       'ru': ['Благородный олень', 'Северный олень (Карибу)', 'Лось', 'Косуля'],
                       'en': ['Red Deer', 'Reindeer (Caribou)', 'Moose', 'Roe Deer']},
        'correct_index': 1,
        'correct_answer': {   'uz': "Shimol bug'usi (Karibu)",
                              'ru': 'Северный олень (Карибу)',
                              'en': 'Reindeer (Caribou)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Rangifer_tarandus_reindeer.jpg/800px-Rangifer_tarandus_reindeer.jpg',
        'fun_fact': {   'uz': "Shimol bug'usi — urg'ochilari ham har yili shox chiqaradigan yagona bug'u turidir; "
                              "uning ko'zlari qishda ultrabinafsha nurlarini ko'rish uchun ko'k rangga o'zgaradi.",
                        'ru': 'Зимой глаза северного оленя меняют цвет с золотого на синий, усиливая чувствительность '
                              'к ультрафиолету в полярную ночь.',
                        'en': 'Reindeer are the only deer species where females grow antlers; in polar winters, their '
                              'tapetum lucidum shifts from gold to deep blue.'},
        'aliases': ['shimol bugusi', 'karibu', 'северный олень', 'карибу', 'reindeer', 'caribou']},
    {   'id': 'nature_emoji_055_leafcutter_ant',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐜 + 🍃 + 🍄 + 🚜",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐜 + 🍃 + 🍄 + 🚜',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐜 + 🍃 + 🍄 + 🚜'},
        'options': {   'uz': ["O'rmon chumolisi", 'Termit', 'Bargkesar chumoli', 'Ari'],
                       'ru': ['Рыжий лесной муравей', 'Термит', 'Муравей-листорез (Atta)', 'Оса'],
                       'en': ['Wood Ant', 'Termite', 'Leafcutter Ant', 'Wasp']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Bargkesar chumoli', 'ru': 'Муравей-листорез (Atta)', 'en': 'Leafcutter Ant'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Atta_cephalotes_leafcutter_ant.jpg/800px-Atta_cephalotes_leafcutter_ant.jpg',
        'fun_fact': {   'uz': 'Bargkesar chumolilar barglarni yemaydi; ular barglarni chaynab yer ostidagi ulkan '
                              "maxsus zamburug' (qo'ziqorin) fermalarini o'stiradi.",
                        'ru': 'Муравьи-листорезы изобрели сельское хозяйство 50 млн лет назад: они удобряют листьями '
                              'подземные сады грибов Leucoagaricus.',
                        'en': 'Leafcutter ants do not eat leaves; they mulch vegetation into compost to cultivate '
                              'subterranean monocultures of Leucoagaricus fungi.'},
        'aliases': ['bargkesar chumoli', 'муравей-листорез', 'листорез', 'leafcutter ant']},
    {   'id': 'nature_emoji_056_queen_bee',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐝 + 🍯 + 👑 + 🥚",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐝 + 🍯 + 👑 + 🥚',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐝 + 🍯 + 👑 + 🥚'},
        'options': {   'uz': ['Ishchi asalari', 'Erkak ari (Truten)', 'Qovoqari', 'Ona asalari (Matka)'],
                       'ru': ['Рабочая пчела', 'Трутень', 'Шмель', 'Пчелиная матка'],
                       'en': ['Worker Bee', 'Drone Bee', 'Bumblebee', 'Queen Bee']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Ona asalari (Matka)', 'ru': 'Пчелиная матка', 'en': 'Queen Bee'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Apis_mellifera_queen_surrounded.jpg/800px-Queen_bee_in_colony.jpg',
        'fun_fact': {   'uz': "Ona asalari sutkasiga 2000 tagacha tuxum qo'yadi va ona suti (qirollik jele) bilan "
                              'oziqlangani sababli oddiy ishchi asalarilardan 40 baravar uzoq (5 yilgacha) yashaydi.',
                        'ru': 'Матка откладывает до 2000 яиц в день, что превышает ее собственный вес, и живет до 5 '
                              'лет благодаря питанию маточным молочком.',
                        'en': 'A queen bee can lay 2,000 eggs per day and lives up to 5 years exclusively nurtured on '
                              'royal jelly secreted by nurse workers.'},
        'aliases': ['ona asalari', 'matka', 'пчелиная матка', 'queen bee']},
    {   'id': 'nature_emoji_057_puffin',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐦 + 🐧 + 🏝️ + 🐟",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐦 + 🐧 + 🏝️ + 🐟',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐦 + 🐧 + 🏝️ + 🐟'},
        'options': {   'uz': ['Tupik qushi (Atlantika tupigi)', 'Pingvin', 'Albatros', 'Chayka'],
                       'ru': ['Атлантический тупик', 'Пингвин', 'Альбатрос', 'Чайка'],
                       'en': ['Atlantic Puffin', 'Penguin', 'Albatross', 'Seagull']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Tupik qushi (Atlantika tupigi)',
                              'ru': 'Атлантический тупик',
                              'en': 'Atlantic Puffin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Fratercula_arctica_atlantic_puffin.jpg/800px-Atlantic_puffin.jpg',
        'fun_fact': {   'uz': "Tupik tumshug'idagi maxsus tishchalar yordamida bir vaqtning o'zida tumshug'ida 60 "
                              'tagacha mayda baliqni qisib ushlab uya tomon ucha oladi.',
                        'ru': 'Благодаря зазубринам на небе тупик удерживает поперек клюва до 60 мелких песчанок '
                              'одновременно, не роняя их под водой.',
                        'en': "A puffin's grooved tongue and spiny palate allow it to cross-lock dozens of sandeels "
                              'sideways in its bill while continuing to hunt.'},
        'aliases': ['tupik', 'тупик', 'атлантический тупик', 'puffin', 'atlantic puffin']},
    {   'id': 'nature_emoji_058_deathstalker',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦂 + 🏜️ + ☠️ + 🌕",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦂 + 🏜️ + ☠️ + 🌕',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦂 + 🏜️ + ☠️ + 🌕'},
        'options': {   'uz': ['Imperator chayoni', 'Sariq chayon (Deathstalker)', 'Tarantul', 'Falanga'],
                       'ru': ['Императорский скорпион', 'Жёлтый скорпион (Смертельный охотник)', 'Тарантул', 'Фаланга'],
                       'en': ['Emperor Scorpion', 'Deathstalker Scorpion', 'Tarantula', 'Camel Spider']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Sariq chayon (Deathstalker)',
                              'ru': 'Жёлтый скорпион (Смертельный охотник)',
                              'en': 'Deathstalker Scorpion'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Leiurus_quinquestriatus_deathstalker.jpg/800px-Deathstalker_scorpion.jpg',
        'fun_fact': {   'uz': "Ushbu chayonning zahari dunyodagi eng qimmat suyuqliklardan biri bo'lib (litri 10 "
                              'million dollar), undagi xlorotoksin moddasi miya saratonini davolashda ishlatiladi.',
                        'ru': 'Яд желтого скорпиона стоит около 10 млн долларов за литр; хлоротоксин из его яда '
                              'связывается исключительно с клетками опухолей мозга.',
                        'en': 'Deathstalker scorpion venom contains chlorotoxin, used in molecular imaging to '
                              'selectively light up malignant brain tumor cells.'},
        'aliases': ['sariq chayon', 'желтый скорпион', 'deathstalker', 'deathstalker scorpion']},
    {   'id': 'nature_emoji_059_black_widow',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🕷️ + ⏳ + 🔴 + ☠️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🕷️ + ⏳ + 🔴 + ☠️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🕷️ + ⏳ + 🔴 + ☠️'},
        'options': {   'uz': ['Tarantul', 'Krestovik', "Qora beva o'rgimchak (Karakurt)", "Hayvon o'rgimchagi"],
                       'ru': ['Тарантул', 'Крестовик', 'Чёрная вдова (Каракурт)', 'Птицеед'],
                       'en': ['Tarantula', 'Orb-weaver', 'Black Widow Spider', 'Wolf Spider']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Qora beva o'rgimchak (Karakurt)",
                              'ru': 'Чёрная вдова (Каракурт)',
                              'en': 'Black Widow Spider'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Latrodectus_mactans_black_widow.jpg/800px-Black_widow_spider.jpg',
        'fun_fact': {   'uz': 'Qora bevaning qornidagi qizil qumsoat naqshi uning kuchli neyrotoksini (latrotoksin) '
                              'haqida ogohlantiradi; zahar kuchli mushak spazmlarini chaqiradi.',
                        'ru': 'Красные песочные часы на черном брюшке каракурта предупреждают о яде латротоксине, '
                              'который в 15 раз токсичнее яда гремучей змеи.',
                        'en': "The red hourglass on the underside of a black widow's abdomen signals potent "
                              'alpha-latrotoxins that stimulate massive acetylcholine release.'},
        'aliases': ['qora beva', 'karakurt', 'черная вдова', 'каракурт', 'black widow']},
    {   'id': 'nature_emoji_060_locust',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦗 + 🦗 + 🌾 + 🌪️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦗 + 🦗 + 🌾 + 🌪️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦗 + 🦗 + 🌾 + 🌪️'},
        'options': {   'uz': ['Chigirtka', 'Ninachi', "Qo'ng'iz", "Cho'l chigirtkasi (Sarancha)"],
                       'ru': ['Кузнечик', 'Стрекоза', 'Жук', 'Пустынная саранча'],
                       'en': ['Grasshopper', 'Dragonfly', 'Beetle', 'Desert Locust']},
        'correct_index': 3,
        'correct_answer': {'uz': "Cho'l chigirtkasi (Sarancha)", 'ru': 'Пустынная саранча', 'en': 'Desert Locust'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Schistocerca_gregaria_desert_locust.jpg/800px-Desert_locust.jpg',
        'fun_fact': {   'uz': "Cho'l chigirtkasi to'dasi milliardlab hasharotlardan iborat bo'lib, bir kunda butun bir "
                              'shahar aholisiga yetadigan oziq-ovqat ekinlarini yeb bitiradi.',
                        'ru': 'Рой саранчи площадью 1 кв. км насчитывает 40-80 млн особей и съедает за сутки столько '
                              'же пищи, сколько 35 000 человек.',
                        'en': 'A desert locust swarm can span hundreds of square kilometers and consume the food '
                              'supply of 35,000 people in a single day.'},
        'aliases': ['sarancha', 'chigirtka', 'саранча', 'desert locust', 'locust']},
    {   'id': 'nature_emoji_061_carrier_pigeon',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐦 + 🕊️ + ✉️ + 🧭",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐦 + 🕊️ + ✉️ + 🧭',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐦 + 🕊️ + ✉️ + 🧭'},
        'options': {   'uz': ['Pochta kaptari (Xabarchi)', "Qaldirg'och", 'Burgut', 'Boyqush'],
                       'ru': ['Почтовый голубь', 'Ласточка', 'Орел', 'Сова'],
                       'en': ['Homing Pigeon (Carrier Pigeon)', 'Swallow', 'Eagle', 'Owl']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Pochta kaptari (Xabarchi)',
                              'ru': 'Почтовый голубь',
                              'en': 'Homing Pigeon (Carrier Pigeon)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Columba_livia_homing_pigeon.jpg/800px-Homing_pigeon.jpg',
        'fun_fact': {   'uz': "Pochta kaptarlari tumshug'idagi mayda magnitit kristallari va quyosh yo'nalishi orqali "
                              'Yerning magnit maydonini his qilib, 1000 km naridagi uyini topib boradi.',
                        'ru': 'Почтовые голуби ориентируются по магнитному полю Земли и инфразвуку, возвращаясь в свою '
                              'голубятню за сотни километров.',
                        'en': 'Homing pigeons navigate over 1,000 km using cryptochrome photopigments and magnetite in '
                              "their beaks to sense Earth's geomagnetic lines."},
        'aliases': ['pochta kaptari', 'kaptar', 'почтовый голубь', 'голубь', 'carrier pigeon', 'homing pigeon']},
    {   'id': 'nature_emoji_062_bald_eagle',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦅 + 🦅 + 🇺🇸 + 🐟",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦅 + 🦅 + 🇺🇸 + 🐟',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦅 + 🦅 + 🇺🇸 + 🐟'},
        'options': {   'uz': ['Lochin', 'Oqbosh burgut (Orlan)', 'Boyqush', 'Quriy'],
                       'ru': ['Сокол', 'Белоголовый орлан', 'Сова', 'Ястреб'],
                       'en': ['Falcon', 'Bald Eagle', 'Owl', 'Hawk']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Oqbosh burgut (Orlan)', 'ru': 'Белоголовый орлан', 'en': 'Bald Eagle'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Bald_eagle_eye_and_cere_macro.jpg/800px-Bald_eagle_eye_and_cere_macro.jpg',
        'fun_fact': {   'uz': "Oqbosh burgut AQShning milliy ramzi bo'lib, uning uyasi 3 metr kenglikda va 2 tonna "
                              "og'irlikda bo'lishi mumkin (dunyodagi eng katta qush uyasi).",
                        'ru': 'Гнездо белоголового орлана — самое крупное древесное гнездо в мире; рекордное весило '
                              'почти 3 тонны при глубине 4 метра.',
                        'en': 'Bald eagles build the largest tree nests of any animal, with the largest measured at '
                              '2.9 meters wide, 6 meters deep, and weighing nearly 3 tons.'},
        'aliases': ['oqbosh burgut', 'орлан', 'белоголовый орлан', 'bald eagle']},
    {   'id': 'nature_emoji_063_indian_peafowl',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦚 + 🦚 + 🌈 + 👁️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦚 + 🦚 + 🌈 + 👁️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦚 + 🦚 + 🌈 + 👁️'},
        'options': {   'uz': ["Qirg'ovul", 'Jannat qushi', 'Hind tovus (Tovus)', "To'ti"],
                       'ru': ['Фазан', 'Райская птица', 'Обыкновенный (индийский) павлин', 'Попугай'],
                       'en': ['Pheasant', 'Bird-of-paradise', 'Indian Peafowl', 'Parrot']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Hind tovus (Tovus)', 'ru': 'Обыкновенный (индийский) павлин', 'en': 'Indian Peafowl'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Peacock_feather_detail.jpg/800px-Peacock_feather_detail.jpg',
        'fun_fact': {   'uz': 'Tovus dumi deb ataladigan ajoyib qism aslida dum emas, balki dum usti qoplovchi '
                              "patlaridir; dumi esa patlar ostida kichkina bo'lib turadi.",
                        'ru': 'Роскошный «веер» павлина — это не хвост, а удлиненные перья надхвостья, поддерживаемые '
                              'коротким жестким настоящим хвостом.',
                        'en': "The peacock's spectacular train is not its tail, but hyper-elongated upper tail covert "
                              'feathers erected by stiff underlying rectrices.'},
        'aliases': ['tovus', 'павлин', 'индийский павлин', 'peafowl', 'peacock']},
    {   'id': 'nature_emoji_064_budgerigar',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦜 + 🇦🇺 + 🟡 + 🟢",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦜 + 🇦🇺 + 🟡 + 🟢',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦜 + 🇦🇺 + 🟡 + 🟢'},
        'options': {   'uz': ['Kakadu', 'Ara', 'Korella', "To'lqinsimon to'ti"],
                       'ru': ['Какаду', 'Ара', 'Корелла', 'Волнистый попугайчик'],
                       'en': ['Cockatoo', 'Macaw', 'Cockatiel', 'Budgerigar']},
        'correct_index': 3,
        'correct_answer': {'uz': "To'lqinsimon to'ti", 'ru': 'Волнистый попугайчик', 'en': 'Budgerigar'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Melopsittacus_undulatus_budgerigar.jpg/800px-Budgerigar.jpg',
        'fun_fact': {   'uz': "To'lqinsimon to'tilar yovvoyi tabiatda faqat yashil-sariq rangda bo'ladi; ularning "
                              'yonoqlaridagi tuklar ultrabinafsha nurlarida jilvalanadi.',
                        'ru': 'В дикой природе Австралии все волнистые попугайчики имеют зеленый защитный окрас с '
                              'флуоресцентной шапочкой на голове.',
                        'en': 'Wild Australian budgerigars are exclusively green and yellow, displaying fluorescent '
                              'yellow crown feathers visible to prospective mates.'},
        'aliases': ['tolqinsimon toti', "to'ti", 'волнистый попугайчик', 'попугайчик', 'budgerigar']},
    {   'id': 'nature_emoji_065_dungeness_crab',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦀 + 🌊 + 🥢 + 🛡️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦀 + 🌊 + 🥢 + 🛡️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦀 + 🌊 + 🥢 + 🛡️'},
        'options': {   'uz': ['Dungeness krabi', 'Langust', 'Omar', 'Krevetka'],
                       'ru': ['Дадженесский краб', 'Лангуст', 'Омар', 'Креветка'],
                       'en': ['Dungeness Crab', 'Spiny Lobster', 'American Lobster', 'Shrimp']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Dungeness krabi', 'ru': 'Дадженесский краб', 'en': 'Dungeness Crab'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Metacarcinus_magister_dungeness_crab.jpg/800px-Dungeness_crab.jpg',
        'fun_fact': {   'uz': "Bu krab o'zining mustahkam xitin qobig'ini har yili tashlab (molting), yangi kattaroq "
                              "sovut o'stiradi.",
                        'ru': 'Во время линьки краб полностью сбрасывает старый жесткий экзоскелет, включая хитиновую '
                              'выстилку желудка и жабр.',
                        'en': 'Dungeness crabs molt their entire calcified carapace, extracting soft tissue from the '
                              'old shell before expanding in seawater.'},
        'aliases': ['krab', 'dungeness krabi', 'краб', 'dungeness crab']},
    {   'id': 'nature_emoji_066_wild_boar',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐗 + 🐗 + 🌲 + 🌿",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐗 + 🐗 + 🌲 + 🌿',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐗 + 🐗 + 🌲 + 🌿'},
        'options': {   'uz': ["Uy cho'chqasi", "Yovvoyi to'ng'iz (Qobon)", 'Begemot', 'Pekari'],
                       'ru': ['Свинья', 'Дикий кабан (Вепрь)', 'Бегемот', 'Пекари'],
                       'en': ['Domestic Pig', 'Wild Boar', 'Hippo', 'Peccary']},
        'correct_index': 1,
        'correct_answer': {'uz': "Yovvoyi to'ng'iz (Qobon)", 'ru': 'Дикий кабан (Вепрь)', 'en': 'Wild Boar'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Sus_scrofa_wild_boar_forest.jpg/800px-Wild_boar.jpg',
        'fun_fact': {   'uz': "Qobonning qoziq tishlari umr bo'yi o'sadi va pastki tishlari yuqorisi bilan ishqalanib, "
                              "ustara kabi doim o'tkirlanib turadi.",
                        'ru': 'Нижние клыки секача достигают 12 см и самозатачиваются о верхние резцы при каждом '
                              'жевательном движении челюсти.',
                        'en': "A wild boar's lower tusks grow continuously and rub against upper grinding teeth to "
                              'maintain razor-sharp cutting edges.'},
        'aliases': ['qobon', 'tongiz', 'кабан', 'дикий кабан', 'вепрь', 'wild boar']},
    {   'id': 'nature_emoji_067_sacred_lotus',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🪷 + 🧘 + 🌊 + 🪷",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🪷 + 🧘 + 🌊 + 🪷',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🪷 + 🧘 + 🌊 + 🪷'},
        'options': {   'uz': ['Suv nilufari', 'Bambuk', 'Muqaddas nilufar (Lotos)', 'Mimoza'],
                       'ru': ['Кувшинка', 'Бамбук', 'Лотос орехоносный', 'Мимоза'],
                       'en': ['Water Lily', 'Bamboo', 'Sacred Lotus (Nelumbo nucifera)', 'Mimosa']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Muqaddas nilufar (Lotos)',
                              'ru': 'Лотос орехоносный',
                              'en': 'Sacred Lotus (Nelumbo nucifera)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Nelumbo_nucifera_lotus_flower.jpg/800px-Lotus_flower.jpg',
        'fun_fact': {   'uz': "Lotos barglari 'lotos effekti'ga ega: uning yuzasidagi mikroskopik mum ustunchalari suv "
                              "tomchilarini va changni o'ziga yopishtirmay yuvib tushiradi.",
                        'ru': '«Эффект лотоса» объясняется наноструктурой воскового слоя листьев, с которых капли воды '
                              'скатываются, забирая всю грязь.',
                        'en': "Nelumbo nucifera leaves exhibit extreme superhydrophobicity ('lotus effect') via "
                              'nanoscale epicuticular wax crystals that self-clean.'},
        'aliases': ['lotos', 'nilufar', 'лотос', 'священный лотос', 'lotus', 'sacred lotus']},
    {   'id': 'nature_emoji_068_cherry_blossom',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌸 + 🇯🇵 + 🍃 + 🎎",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌸 + 🇯🇵 + 🍃 + 🎎',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌸 + 🇯🇵 + 🍃 + 🎎'},
        'options': {   'uz': ['Lotos', 'Raffleziya', 'Mimoza', 'Sakura (Gilos guli)'],
                       'ru': ['Лотос', 'Раффлезия', 'Мимоза', 'Сакура (Японская вишня)'],
                       'en': ['Lotus', 'Rafflesia', 'Mimosa', 'Cherry Blossom (Sakura)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Sakura (Gilos guli)',
                              'ru': 'Сакура (Японская вишня)',
                              'en': 'Cherry Blossom (Sakura)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cherry_blossoms_sakura_tokyo.jpg/800px-Cherry_blossoms_sakura.jpg',
        'fun_fact': {   'uz': "Yaponiyada sakuraning gullashi bor-yo'g'i 1-2 hafta davom etadi va u hayotning "
                              "go'zalligi hamda o'tkinchiligini ifodalovchi qadimiy milliy ramzdir.",
                        'ru': 'Цветение сакуры символизирует в синтоизме мимолетность и хрупкость бытия, собирая '
                              'миллионы людей на традицию ханами.',
                        'en': 'Sakura blossoms bloom for only 7–14 days in spring, celebrated throughout Japan during '
                              "centuries-old 'Hanami' viewing festivals."},
        'aliases': ['sakura', 'gilos guli', 'сакура', 'японская вишня', 'cherry blossom', 'sakura']},
    {   'id': 'nature_emoji_069_edelweiss',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌾 + 🏔️ + 🐑 + 🇨🇭",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌾 + 🏔️ + 🐑 + 🇨🇭',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌾 + 🏔️ + 🐑 + 🇨🇭'},
        'options': {   'uz': ['Edelveys guli', 'Lotos', 'Atirgul', 'Lola'],
                       'ru': ['Эдельвейс альпийский', 'Лотос', 'Альпийская роза', 'Тюльпан'],
                       'en': ['Edelweiss', 'Lotus', 'Alpine Rose', 'Tulip']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Edelveys guli', 'ru': 'Эдельвейс альпийский', 'en': 'Edelweiss'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Leontopodium_nivale_edelweiss.jpg/800px-Edelweiss_flower.jpg',
        'fun_fact': {   'uz': "Edelveys guli mayin oq momiq bilan qoplangan bo'lib, bu momiq uni Alp tog'laridagi "
                              'kuchli quyosh ultrabinafshasi va sovuqdan himoya qiladi.',
                        'ru': 'Белый войлочный пух на лепестках эдельвейса поглощает ультрафиолетовое излучение на '
                              'высоте 3000 метров над уровнем моря.',
                        'en': 'Edelweiss bracts are cloaked in dense woolly hairs composed of silica microfibers that '
                              'block harmful alpine UV radiation.'},
        'aliases': ['edelveys', 'эдельвейс', 'edelweiss']},
    {   'id': 'nature_emoji_070_sunflower',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌻 + ☀️ + 🌻 + 🐝",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌻 + ☀️ + 🌻 + 🐝',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌻 + ☀️ + 🌻 + 🐝'},
        'options': {   'uz': ['Lotos', 'Kungaboqar', 'Sakura', 'Mimoza'],
                       'ru': ['Лотос', 'Подсолнечник масличный', 'Сакура', 'Мимоза'],
                       'en': ['Lotus', 'Sunflower', 'Sakura', 'Mimosa']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Kungaboqar', 'ru': 'Подсолнечник масличный', 'en': 'Sunflower'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Helianthus_annuus_sunflower.jpg/800px-Sunflower_field.jpg',
        'fun_fact': {   'uz': "Yosh kungaboqar guli quyosh yo'nalishi bo'ylab sharqdan g'arbga buriladi "
                              "(geliotropizm); uning markazidagi urug'lar esa Fibonachchi spiralini hosil qiladi.",
                        'ru': 'Молодые подсолнухи поворачиваются за солнцем (гелиотропизм), а расположение семечек '
                              'подчиняется строгой золотой спирали Фибоначчи.',
                        'en': 'Young sunflowers track the Sun from east to west (heliotropism), packing their disc '
                              'florets into logarithmic Fibonacci spirals.'},
        'aliases': ['kungaboqar', 'подсолнух', 'подсолнечник', 'sunflower']},
    {   'id': 'nature_emoji_071_lionfish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦁 + 🐟 + 🪡 + ☠️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦁 + 🐟 + 🪡 + ☠️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦁 + 🐟 + 🪡 + ☠️'},
        'options': {   'uz': ['Fugu', 'Murena', 'Qanotdor baliq (Krylatka)', 'Skumbriya'],
                       'ru': ['Фугу', 'Мурена', 'Крылатка-зебра', 'Скумбрия'],
                       'en': ['Pufferfish', 'Moray Eel', 'Red Lionfish', 'Mackerel']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Qanotdor baliq (Krylatka)', 'ru': 'Крылатка-зебра', 'en': 'Red Lionfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Pterois_volitans_fin_spines_macro.jpg/800px-Pterois_volitans_fin_spines_macro.jpg',
        'fun_fact': {   'uz': "Krylatkaning yelpig'ichsimon suzgichlaridagi 18 ta ignasida kuchli neyrotoksin bo'lib, "
                              'marjon riflarida suzadi.',
                        'ru': 'Каждый луч спинного плавника крылатки вооружен ядовитой иглой, вызывающей паралич мышц '
                              'у хищников.',
                        'en': 'Pterois volitans carries 18 venomous dorsal and anal spines capable of delivering '
                              'excruciating neuromuscular pain.'},
        'aliases': ['krylatka', 'qanotdor baliq', 'крылатка', 'lionfish']},
    {   'id': 'nature_emoji_072_axolotl',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦎 + 🎀 + 👶 + 💧",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦎 + 🎀 + 👶 + 💧',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦎 + 🎀 + 👶 + 💧'},
        'options': {   'uz': ['Triton', 'Salamandra', 'Qurbaqa', 'Aksolotl'],
                       'ru': ['Тритон', 'Саламандра', 'Лягушка', 'Мексиканский аксолотль'],
                       'en': ['Newt', 'Salamander', 'Frog', 'Axolotl']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Aksolotl', 'ru': 'Мексиканский аксолотль', 'en': 'Axolotl'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Axolotl_external_gills_macro.jpg/800px-Axolotl_external_gills_macro.jpg',
        'fun_fact': {   'uz': "Aksolotl neoteniya holatida yashaydi (lichinka bosqichida ko'payadi) va u oyoqlarini, "
                              "yuragini va hatto miyasining bir qismini to'liq qayta o'stira oladi.",
                        'ru': 'Аксолотль способен полностью регенерировать утраченные лапы, жабры, участки сердца и '
                              'спинного мозга без рубцов.',
                        'en': 'Axolotls exhibit neoteny and possess extraordinary regenerative capacity, regrowing '
                              'entire limbs, heart tissue, and sections of the central nervous system.'},
        'aliases': ['aksolotl', 'аксолотль', 'axolotl']},
    {   'id': 'nature_emoji_073_cuttlefish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦑 + 🎨 + 🎭 + 👁️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦑 + 🎨 + 🎭 + 👁️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦑 + 🎨 + 🎭 + 👁️'},
        'options': {   'uz': ['Siyohbaliq (Karakatitsa)', 'Sakkizoyoq', 'Kalmar', 'Meduza'],
                       'ru': ['Каракатица', 'Осьминог', 'Кальмар', 'Медуза'],
                       'en': ['Cuttlefish', 'Octopus', 'Squid', 'Jellyfish']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Siyohbaliq (Karakatitsa)', 'ru': 'Каракатица', 'en': 'Cuttlefish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Cuttlefish_skin_texture_papillae.jpg/800px-Cuttlefish_skin_texture_papillae.jpg',
        'fun_fact': {   'uz': "Karakatitsaning qorachig'i 'W' shaklida bo'lib, u ko'r bo'lsa ham terisi bilan "
                              "atrof-muhit yorug'ligini sezib rangi va 3D shaklini o'zgartiradi.",
                        'ru': 'Каракатица имеет W-образный зрачок и способна менять цвет и текстуру кожи даже будучи '
                              'слепой благодаря фоторецепторам в коже.',
                        'en': 'Cuttlefish sport unique W-shaped pupils and dermal opsin photopigments that allow the '
                              'skin to sense light and camouflage independently.'},
        'aliases': ['siyohbaliq', 'karakatitsa', 'каракатица', 'cuttlefish']},
    {   'id': 'nature_emoji_074_seahorse',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐴 + 🌊 + 👝 + 🐟",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐴 + 🌊 + 👝 + 🐟',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐴 + 🌊 + 👝 + 🐟'},
        'options': {   'uz': ['Ignabaliq', 'Dengiz oti', 'Krab', 'Meduza'],
                       'ru': ['Рыба-игла', 'Морской конёк', 'Краб', 'Медуза'],
                       'en': ['Pipefish', 'Seahorse', 'Crab', 'Jellyfish']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Dengiz oti', 'ru': 'Морской конёк', 'en': 'Seahorse'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Seahorse_bony_rings_macro.jpg/800px-Seahorse_bony_rings_macro.jpg',
        'fun_fact': {   'uz': "Dengiz otlarida erkagi bolalarini homilador bo'lib dunyoga keltiradi: urg'ochisi "
                              'tuxumlarni erkakning qorin xaltasiga joylaydi.',
                        'ru': 'Морские коньки — единственные животные, у которых беременеют и рожают детенышей именно '
                              'самцы.',
                        'en': 'Seahorses are the only animal group where males experience true pregnancy, carrying '
                              'developing embryos inside a ventral brood pouch.'},
        'aliases': ['dengiz oti', 'морской конек', 'морской конёк', 'seahorse']},
    {   'id': 'nature_emoji_075_starfish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? ⭐ + 🌊 + 🌟 + 🐚",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? ⭐ + 🌊 + 🌟 + 🐚',
                        'en': 'Which fascinating animal or plant is represented by these emojis? ⭐ + 🌊 + 🌟 + 🐚'},
        'options': {   'uz': ['Dengiz tipratikani', 'Dengiz bodringi', 'Dengiz yulduzi', 'Meduza'],
                       'ru': ['Морской еж', 'Голотурия', 'Морская звезда', 'Медуза'],
                       'en': ['Sea Urchin', 'Sea Cucumber', 'Sea Star (Starfish)', 'Jellyfish']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Dengiz yulduzi', 'ru': 'Морская звезда', 'en': 'Sea Star (Starfish)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Starfish_skin_ossicles_macro.jpg/800px-Starfish_skin_ossicles_macro.jpg',
        'fun_fact': {   'uz': "Dengiz yulduzining qoni bo'lmaydi; uning tanasida dengiz suvi tomirlar bo'ylab "
                              "harakatlanadi va o'ljani yeyish uchun oshqozonini tashqariga chiqaradi.",
                        'ru': 'У морских звезд нет крови: по сосудам циркулирует морская вода, а желудок они '
                              'выворачивают наружу для переваривания моллюсков.',
                        'en': 'Sea stars pump filtered seawater through a hydraulic water vascular system and evert '
                              'their cardiac stomach to digest prey externally.'},
        'aliases': ['dengiz yulduzi', 'морская звезда', 'starfish', 'sea star']},
    {   'id': 'nature_emoji_076_sea_urchin',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦔 + 🌊 + 🪡 + 🔘",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦔 + 🌊 + 🪡 + 🔘',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦔 + 🌊 + 🪡 + 🔘'},
        'options': {   'uz': ['Dengiz yulduzi', 'Ofiura', 'Aktiniya', 'Dengiz tipratikani'],
                       'ru': ['Морская звезда', 'Офиура', 'Актиния', 'Морской ёж'],
                       'en': ['Sea Star', 'Brittle Star', 'Anemone', 'Sea Urchin']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Dengiz tipratikani', 'ru': 'Морской ёж', 'en': 'Sea Urchin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Sea_urchin_spines_macro.jpg/800px-Sea_urchin_spines_macro.jpg',
        'fun_fact': {   'uz': "Dengiz tipratikanining 5 ta tishdan iborat maxsus og'iz apparati 'Arastu fonari' deb "
                              "ataladi va toshlardagi suvo'tlarini qirishga xizmat qiladi.",
                        'ru': 'Челюстной аппарат морского ежа называется «аристотелевым фонарем» и состоит из 5 '
                              'самозатачивающихся известковых зубов.',
                        'en': "Sea urchins graze rocky substrate using 'Aristotle's lantern', a pyramidal jaw "
                              'structure of five self-sharpening calcite teeth.'},
        'aliases': ['dengiz tipratikani', 'морской еж', 'морской ёж', 'sea urchin']},
    {   'id': 'nature_emoji_077_pufferfish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐡 + 🎈 + 🪡 + ☠️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐡 + 🎈 + 🪡 + ☠️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐡 + 🎈 + 🪡 + ☠️'},
        'options': {   'uz': ['Sharbaliq (Fugu)', 'Kambala', 'Skumbriya', 'Morona'],
                       'ru': ['Рыба-фугу (Иглобрюх)', 'Камбала', 'Скумбрия', 'Морена'],
                       'en': ['Pufferfish', 'Flounder', 'Mackerel', 'Moray']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Sharbaliq (Fugu)', 'ru': 'Рыба-фугу (Иглобрюх)', 'en': 'Pufferfish'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Pufferfish_erected_spines_macro.jpg/800px-Pufferfish_erected_spines_macro.jpg',
        'fun_fact': {   'uz': "Sharbaliq tanasidagi tetrodotoksin sianiddan 1200 baravar kuchli zahar bo'lib, unga "
                              'qarshi dori (antidot) hali topilmagan.',
                        'ru': 'Яд фугу тетродотоксин в 1200 раз токсичнее цианистого калия; японские повара учатся '
                              'готовить ее не менее 3 лет для получения лицензии.',
                        'en': 'Pufferfish contain lethal concentrations of tetrodotoxin in their ovaries and liver, '
                              '1,200 times deadlier than potassium cyanide.'},
        'aliases': ['fugu', 'sharbaliq', 'рыба-фугу', 'иглобрюх', 'pufferfish']},
    {   'id': 'nature_emoji_078_whale_shark',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐋 + 🦈 + 🦐 + 🌊",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐋 + 🦈 + 🦐 + 🌊',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐋 + 🦈 + 🦐 + 🌊'},
        'options': {   'uz': ['Oq akula', 'Kit akulasi', "Ko'k kit", 'Manta'],
                       'ru': ['Белая акула', 'Китовая акула', 'Синий кит', 'Манта'],
                       'en': ['Great White Shark', 'Whale Shark', 'Blue Whale', 'Manta Ray']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Kit akulasi', 'ru': 'Китовая акула', 'en': 'Whale Shark'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Rhincodon_typus_whale_shark_skin.jpg/800px-Rhincodon_typus_whale_shark_skin.jpg',
        'fun_fact': {   'uz': "Kit akulasi dunyodagi eng katta baliq (uzunligi 18–20 metr) bo'lsa-da, u faqat "
                              'mikroskopik plankton va mayda qisqichbaqalar bilan oziqlanadi.',
                        'ru': 'Китовая акула — крупнейшая рыба планеты (до 20 метров), абсолютно безобидная для '
                              'человека и фильтрующая криль через жаберные решета.',
                        'en': 'Growing up to 18 meters in length, the docile whale shark filters up to 6,000 liters of '
                              'seawater per hour for zooplankton.'},
        'aliases': ['kit akulasi', 'китовая акула', 'whale shark']},
    {   'id': 'nature_emoji_079_hammerhead_shark',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🔨 + 🦈 + 🌊 + 👁️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🔨 + 🦈 + 🌊 + 👁️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🔨 + 🦈 + 🌊 + 👁️'},
        'options': {   'uz': ['Oq akula', 'Manta', "Bolg'abosh akula", 'Morona'],
                       'ru': ['Белая акула', 'Манта', 'Акула-молот', 'Мурена'],
                       'en': ['Great White Shark', 'Manta Ray', 'Hammerhead Shark', 'Moray Eel']},
        'correct_index': 2,
        'correct_answer': {'uz': "Bolg'abosh akula", 'ru': 'Акула-молот', 'en': 'Hammerhead Shark'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Sphyrna_mokarran_hammerhead.jpg/800px-Hammerhead_shark.jpg',
        'fun_fact': {   'uz': "Bolg'asimon kengaygan boshidagi Lorenzini ampulalari akulaga qum ostida yashiringan "
                              'skatlarning eng nozik elektr maydonini sezishga imkon beradi.',
                        'ru': 'Т-образная голова молотоголовой акулы усеяна ампулами Лоренцини, работающими как '
                              'высокочувствительный металлоискатель биополей.',
                        'en': 'The broad cephalofoil head of the hammerhead shark expands the sensory surface of '
                              'ampullae of Lorenzini to detect electric fields of hidden rays.'},
        'aliases': ['bolgabosh akula', 'акула-молот', 'акула молот', 'hammerhead shark']},
    {   'id': 'nature_emoji_080_manta_ray',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦅 + 🌊 + 🦇 + "
                              '\U0001fabd',
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦅 + 🌊 + 🦇 + '
                              '\U0001fabd',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦅 + 🌊 + 🦇 + '
                              '\U0001fabd'},
        'options': {   'uz': ['Akula', 'Skat', 'Kit', 'Manta (Dengiz iblisi)'],
                       'ru': ['Акула', 'Хвостокол', 'Кит', 'Гигантский морской дьявол (Манта)'],
                       'en': ['Shark', 'Stingray', 'Whale', 'Giant Manta Ray']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Manta (Dengiz iblisi)',
                              'ru': 'Гигантский морской дьявол (Манта)',
                              'en': 'Giant Manta Ray'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Manta_alfredi_ventral_spotting_macro.jpg/800px-Manta_ray.jpg',
        'fun_fact': {   'uz': "Manta barcha baliqlar orasida eng katta miyaga ega bo'lib, o'z aksini ko'zguda taniy "
                              'oladigan baliqlardan biridir.',
                        'ru': 'Манта обладает самым крупным мозгом среди рыб относительно массы тела и способна '
                              'узнавать свое отражение в зеркале.',
                        'en': 'Manta rays possess the largest brain-to-body mass ratio of any cold-blooded fish and '
                              'pass mirror self-recognition cognitive tests.'},
        'aliases': ['manta', 'манта', 'морской дьявол', 'manta ray']},
    {   'id': 'nature_emoji_081_moray_eel',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐍 + 🐟 + 🕳️ + 🦷",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐍 + 🐟 + 🕳️ + 🦷',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐍 + 🐟 + 🕳️ + 🦷'},
        'options': {   'uz': ['Murena', 'Ilonbaliq', 'Akula', 'Som'],
                       'ru': ['Мурена', 'Угорь', 'Акула', 'Сом'],
                       'en': ['Moray Eel', 'Conger Eel', 'Shark', 'Catfish']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Murena', 'ru': 'Мурена', 'en': 'Moray Eel'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Moray_eel_skin_macro.jpg/800px-Moray_eel.jpg',
        'fun_fact': {   'uz': "Murenaning tomog'ida ikkinchi juft harakatchan jag'i (faringeal jag') bo'lib, xuddi "
                              "'O'zga sayyoralik' filmidagi maxluqdek o'ljani tomoqqa tortadi.",
                        'ru': 'Мурена обладает второй глоточной челюстью, которая выдвигается вперед, захватывает '
                              'жертву и утягивает ее в пищевод.',
                        'en': 'Moray eels deploy a secondary set of muscular pharyngeal jaws that thrust forward to '
                              'drag prey backward into the esophagus.'},
        'aliases': ['murena', 'мурена', 'moray eel']},
    {   'id': 'nature_emoji_082_electric_eel',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? ⚡ + 🐍 + 🐟 + 🔋",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? ⚡ + 🐍 + 🐟 + 🔋',
                        'en': 'Which fascinating animal or plant is represented by these emojis? ⚡ + 🐍 + 🐟 + 🔋'},
        'options': {   'uz': ['Murena', 'Elektr ilonbaliq', 'Som baliq', 'Akula'],
                       'ru': ['Мурена', 'Электрический угорь', 'Сом', 'Акула'],
                       'en': ['Moray Eel', 'Electric Eel', 'Catfish', 'Shark']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Elektr ilonbaliq', 'ru': 'Электрический угорь', 'en': 'Electric Eel'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Electrophorus_electricus_eel.jpg/800px-Electric_eel.jpg',
        'fun_fact': {   'uz': "Elektr ilonbaliq tanasining 80% qismi elektr hosil qiluvchi a'zolardan iborat bo'lib, u "
                              'suv yuzasiga chiqib 10 daqiqada bir havodan nafas oladi.',
                        'ru': 'Электрический угорь — двоякодышащая рыба: он дышит воздухом, поднимаясь к поверхности, '
                              'иначе он утонет в воде.',
                        'en': 'Electric eels are obligate air-breathers, surfacing every 10 minutes to gulp '
                              'atmospheric oxygen using vascularized buccal cavities.'},
        'aliases': ['elektr ilonbaliq', 'электрический угорь', 'electric eel']},
    {   'id': 'nature_emoji_083_clownfish',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🤡 + 🐟 + 🪸 + 🧡",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🤡 + 🐟 + 🪸 + 🧡',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🤡 + 🐟 + 🪸 + 🧡'},
        'options': {   'uz': ['Zolotoy ribka', 'Xirurg baliq', 'Masxaraboz baliq (Nemo)', 'Guppi'],
                       'ru': ['Золотая рыбка', 'Рыба-хирург', 'Рыба-клоун (Амфиприон)', 'Гуппи'],
                       'en': ['Goldfish', 'Blue Tang', 'Clownfish (Ocellaris)', 'Guppy']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Masxaraboz baliq (Nemo)',
                              'ru': 'Рыба-клоун (Амфиприон)',
                              'en': 'Clownfish (Ocellaris)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Amphiprion_ocellaris_skin_macro.jpg/800px-Clownfish.jpg',
        'fun_fact': {   'uz': "Barcha masxaraboz baliqlar erkak bo'lib tug'iladi; agar to'dadagi bosh urg'ochi baliq "
                              "o'lsa, eng yirik erkak jinsini urg'ochiga o'zgartiradi (ketma-ket germafroditizm).",
                        'ru': 'Все рыбы-клоуны рождаются самцами; если доминантная самка погибает, крупнейший самец '
                              'трансформируется в самку.',
                        'en': 'Clownfish are sequential protandrous hermaphrodites; if the breeding female dies, the '
                              'largest male permanently transitions into a fertile female.'},
        'aliases': ['masxaraboz baliq', 'amfiprion', 'рыба-клоун', 'clownfish', 'nemo']},
    {   'id': 'nature_emoji_084_toco_toucan',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦜 + 🍌 + 🌈 + 🌴",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦜 + 🍌 + 🌈 + 🌴',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦜 + 🍌 + 🌈 + 🌴'},
        'options': {   'uz': ['Kakadu', 'Qarqara', 'Pelikan', 'Tukan (Toko tukan)'],
                       'ru': ['Какаду', 'Цапля', 'Пеликан', 'Большой тукан (Токо)'],
                       'en': ['Cockatoo', 'Heron', 'Pelican', 'Toco Toucan']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Tukan (Toko tukan)', 'ru': 'Большой тукан (Токо)', 'en': 'Toco Toucan'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Toco_toucan_beak_macro.jpg/800px-Toco_toucan.jpg',
        'fun_fact': {   'uz': "Tukanning yorqin tumshug'i nafaqat mevalarni uzish, balki issiq tropikda tanadagi "
                              "ortiqcha issiqlikni tarqatuvchi kuchli radiator vazifasini o'taydi.",
                        'ru': 'Огромный клюв тукана пронизан кровеносными сосудами и рассеивает до 400% тепловыделения '
                              'тела в покое.',
                        'en': "A toucan's bill acts as a thermal window, altering blood flow through superficial "
                              'vascular beds to dump heat.'},
        'aliases': ['tukan', 'тукан', 'большой тукан', 'toucan', 'toco toucan']},
    {   'id': 'nature_emoji_085_greater_flamingo',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦩 + 🩰 + 💖 + 🦐",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦩 + 🩰 + 💖 + 🦐',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦩 + 🩰 + 💖 + 🦐'},
        'options': {   'uz': ['Katta flamingo', 'Oqqush', 'Pelikan', 'Turna'],
                       'ru': ['Обыкновенный (розовый) фламинго', 'Лебедь', 'Пеликан', 'Журавль'],
                       'en': ['Greater Flamingo', 'Swan', 'Pelican', 'Crane']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Katta flamingo', 'ru': 'Обыкновенный (розовый) фламинго', 'en': 'Greater Flamingo'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flamingo_feathers_close_up.jpg/800px-Flamingo.jpg',
        'fun_fact': {   'uz': 'Flamingo bir oyoqda turganda deyarli hech qanday mushak kuchi sarflamaydi, chunki uning '
                              "bo'g'imlari maxsus mexanizm orqali qulflanadi.",
                        'ru': 'Фламинго стоит на одной ноге абсолютно пассивно: гравитация замыкает коленный сустав '
                              'без малейшего мышечного напряжения.',
                        'en': 'Flamingos balance on one leg with zero active muscle engagement, locked in place by a '
                              'passive musculoskeletal stay apparatus.'},
        'aliases': ['flamingo', 'фламинго', 'greater flamingo']},
    {   'id': 'nature_emoji_086_scarlet_macaw',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦜 + 🔴 + 🟡 + 🔵",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦜 + 🔴 + 🟡 + 🔵',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦜 + 🔴 + 🟡 + 🔵'},
        'options': {   'uz': ['Kakadu', "Qizil Ara to'tisi", 'Jako', 'Lori'],
                       'ru': ['Какаду', 'Красный ара', 'Жако', 'Лори'],
                       'en': ['Cockatoo', 'Scarlet Macaw', 'African Grey', 'Lori']},
        'correct_index': 1,
        'correct_answer': {'uz': "Qizil Ara to'tisi", 'ru': 'Красный ара', 'en': 'Scarlet Macaw'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Scarlet_macaw_feather_texture.jpg/800px-Scarlet_macaw.jpg',
        'fun_fact': {   'uz': "Ara to'tisi 75 yildan ortiq yashay oladi va Amazonka daryosi sohilidagi loyli qoyalarni "
                              'yeb, zaharli mevalardagi toksinlarni zararsizlantiradi.',
                        'ru': 'Ара съедают глину на речных обрывах Амазонки, чтобы минералы нейтрализовали токсины и '
                              'алкалоиды незрелых тропических семян.',
                        'en': 'Scarlet macaws practice geophagy, ingesting Amazonian sodium-rich clay licks to '
                              'neutralize dietary alkaloids from unripe rainforest seeds.'},
        'aliases': ['ara', 'qizil ara', 'красный ара', 'scarlet macaw']},
    {   'id': 'nature_emoji_087_barn_owl',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦉 + 👻 + 🤫 + 🌙",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦉 + 👻 + 🤫 + 🌙',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦉 + 👻 + 🤫 + 🌙'},
        'options': {   'uz': ['Filin', 'Kukuruza boyqushi', 'Sipuxa boyqushi (Ombor boyqushi)', "Qarg'a"],
                       'ru': ['Филин', 'Сыч', 'Обыкновенная сипуха', 'Ворона'],
                       'en': ['Eagle Owl', 'Little Owl', 'Barn Owl', 'Crow']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Sipuxa boyqushi (Ombor boyqushi)', 'ru': 'Обыкновенная сипуха', 'en': 'Barn Owl'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Owl_feather_serrations_macro.jpg/800px-Barn_owl.jpg',
        'fun_fact': {   'uz': "Sipuxaning yurak shaklidagi yuzi tovush to'lqinlarini quloqlarga yo'naltiruvchi sun'iy "
                              "yo'ldosh antennasi kabi ishlaydi; u mutlaq qorong'uda sichqonni tovushidan topadi.",
                        'ru': 'Сердцевидный лицевой диск сипухи фокусирует звуки мышиного шуршания прямо в '
                              'асимметричные ушные отверстия.',
                        'en': 'The heart-shaped facial disc of the barn owl channels high-frequency rustling sounds '
                              'into asymmetric ear canals for 3D acoustic targeting.'},
        'aliases': ['sipuxa', 'boyqush', 'сипуха', 'barn owl']},
    {   'id': 'nature_emoji_088_peregrine_falcon',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦅 + ⚡ + 🎯 + 🏎️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦅 + ⚡ + 🎯 + 🏎️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦅 + ⚡ + 🎯 + 🏎️'},
        'options': {   'uz': ['Burgut', 'Quriy', 'Lochincha', 'Sapsan (Lochin)'],
                       'ru': ['Беркут', 'Ястреб', 'Чеглок', 'Сапсан'],
                       'en': ['Golden Eagle', 'Sparrowhawk', 'Hobby', 'Peregrine Falcon']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Sapsan (Lochin)', 'ru': 'Сапсан', 'en': 'Peregrine Falcon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Falco_peregrinus_head.jpg/800px-Peregrine_falcon.jpg',
        'fun_fact': {   'uz': "Sapsan sho'ng'iyotganida o'ljasini tirnog'i bilan shunday kuch bilan uradiki, "
                              'qurbonining boshi havodayoq uzilib ketishi mumkin.',
                        'ru': 'Удар когтей сапсана при пикировании со скоростью 350 км/ч мгновенно ломает шею или '
                              'отрывает голову голубя на лету.',
                        'en': "The impact of a peregrine falcon's clenched foot strike at 350 km/h instantly breaks "
                              'the neck of flying prey mid-air.'},
        'aliases': ['sapsan', 'lochin', 'сапсан', 'peregrine falcon']},
    {   'id': 'nature_emoji_089_kiwi_bird',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🥝 + 🐦 + 🇳🇿 + 🕳️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🥝 + 🐦 + 🇳🇿 + 🕳️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🥝 + 🐦 + 🇳🇿 + 🕳️'},
        'options': {   'uz': ['Kivi qushi (Yangi Zelandiya)', 'Dodo', 'Kazuar', 'Keklik'],
                       'ru': ['Северный киви', 'Додо', 'Казуар', 'Кеклик'],
                       'en': ['Kiwi Bird', 'Dodo', 'Cassowary', 'Partridge']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Kivi qushi (Yangi Zelandiya)', 'ru': 'Северный киви', 'en': 'Kiwi Bird'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Apteryx_mantelli_kiwi_bird.jpg/800px-Kiwi_bird.jpg',
        'fun_fact': {   'uz': "Kivining burni teshiklari tumshug'ining uchida joylashgan yer yuzidagi yagona qushdir; "
                              'u qurtlarni hid bilish orqali yer tagidan qidiradi.',
                        'ru': 'Киви — единственная птица в мире с ноздрями на самом кончике длинного клюва, '
                              'вынюхивающая червей в лесной подстилке.',
                        'en': 'The kiwi is the only avian species with nostrils located at the tip of its bill, '
                              'sniffing out subterranean worms by scent.'},
        'aliases': ['kivi', 'kivi qushi', 'киви', 'птица киви', 'kiwi bird']},
    {   'id': 'nature_emoji_090_tasmanian_devil',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 😈 + 🦷 + 🥩 + 🇦🇺",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 😈 + 🦷 + 🥩 + 🇦🇺',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 😈 + 🦷 + 🥩 + 🇦🇺'},
        'options': {   'uz': ["Xaltali bo'ri", 'Tasmaniya iblisi', 'Vombat', 'Koala'],
                       'ru': ['Сумчатый волк', 'Тасманийский дьявол', 'Вомбат', 'Коала'],
                       'en': ['Thylacine', 'Tasmanian Devil', 'Wombat', 'Koala']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Tasmaniya iblisi', 'ru': 'Тасманийский дьявол', 'en': 'Tasmanian Devil'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Sarcophilus_harrisii_tasmanian_devil.jpg/800px-Tasmanian_devil.jpg',
        'fun_fact': {   'uz': "Tasmaniya iblisi jahli chiqqanda quloqlari qizarib ketadi, badbo'y hid taratadi va "
                              "dahshatli qichqiriq bilan boshqalarni qo'rqitadi.",
                        'ru': 'При стрессе уши тасманийского дьявола становятся ярко-красными, он источает сильный '
                              'запах и издает пронзительный визг.',
                        'en': "When agitated, a Tasmanian devil's ears flush red with blood and it unleashes a foul "
                              'odor accompanied by chilling screeching vocalizations.'},
        'aliases': ['tasmaniya iblisi', 'тасманийский дьявол', 'tasmanian devil']},
    {   'id': 'nature_emoji_091_wombat',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐻 + 🕳️ + 🧱 + 💩",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐻 + 🕳️ + 🧱 + 💩',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐻 + 🕳️ + 🧱 + 💩'},
        'options': {   'uz': ['Koala', 'Possum', 'Vombat', 'Pangolin'],
                       'ru': ['Коала', 'Опоссум', 'Обыкновенный вомбат', 'Панголин'],
                       'en': ['Koala', 'Opossum', 'Common Wombat', 'Pangolin']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Vombat', 'ru': 'Обыкновенный вомбат', 'en': 'Common Wombat'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Vombatus_ursinus_wombat.jpg/800px-Wombat.jpg',
        'fun_fact': {   'uz': "Vombat yer yuzida axlati kub (to'rtburchak g'isht) shaklida bo'lgan yagona hayvondir; "
                              'bu kubiklar toshlardan pastga dumalab ketmaydi.',
                        'ru': 'Вомбаты — единственные животные с кубическим пометом, который они складывают на камнях '
                              'для метки территории, чтобы он не скатывался.',
                        'en': 'Wombats are the only known animals that produce cubic feces, shaped by asymmetric '
                              'intestinal contractions to mark territory on rocks.'},
        'aliases': ['vombat', 'вомбат', 'wombat']},
    {   'id': 'nature_emoji_092_sugar_glider',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐿️ + 🪂 + 🍯 + 🍬",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐿️ + 🪂 + 🍯 + 🍬',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐿️ + 🪂 + 🍯 + 🍬'},
        'options': {   'uz': ['Uchar sincob', "Ko'rshapalak", 'Lori', 'Shakarli uchar sincob (Possum)'],
                       'ru': ['Белка-летяга', 'Летучая мышь', 'Лори', 'Сахарный летающий поссум'],
                       'en': ['Flying Squirrel', 'Bat', 'Slow Loris', 'Sugar Glider']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Shakarli uchar sincob (Possum)',
                              'ru': 'Сахарный летающий поссум',
                              'en': 'Sugar Glider'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Sugar_glider_fur_patagium_macro.jpg/800px-Sugar_glider.jpg',
        'fun_fact': {   'uz': "Shakarli possum shirin evkalipt shirasi va gullar nektarini yaxshi ko'radi, uning "
                              "ko'zlari esa tunda ko'rish uchun ulkan sharsimon shaklda rivojlangan.",
                        'ru': 'Сахарный поссум питается сладким соком акаций и нектаром, а летательная перепонка '
                              'позволяет ему преодолевать 50 метров по воздуху.',
                        'en': 'Sugar gliders feed on sweet sap and flower nectar, gliding between tall trees with '
                              'remarkable steerable agility.'},
        'aliases': ['shakarli sincob', 'shakarli possum', 'сахарный поссум', 'sugar glider']},
    {   'id': 'nature_emoji_093_raccoon',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦝 + 🦹 + 🗑️ + 🧼",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦝 + 🦹 + 🗑️ + 🧼',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦝 + 🦹 + 🗑️ + 🧼'},
        'options': {   'uz': ['Yenot (Yenot-poloskun)', 'Skuns', "Bo'rsiq", 'Qunduz'],
                       'ru': ['Енот-полоскун', 'Скунс', 'Барсук', 'Бобр'],
                       'en': ['Common Raccoon', 'Skunk', 'Badger', 'Beaver']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Yenot (Yenot-poloskun)', 'ru': 'Енот-полоскун', 'en': 'Common Raccoon'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Procyon_lotor_raccoon.jpg/800px-Raccoon.jpg',
        'fun_fact': {   'uz': "Yenot o'zining sezgir panjalaridagi nerv oxirlarini yumshatish va narsalarni yaxshiroq "
                              'his qilish uchun ovqatini doim suvda yuvadi.',
                        'ru': 'Енот полощет еду не из гигиены, а потому что влага в разы повышает чувствительность '
                              'тактильных нервных рецепторов на лапках.',
                        'en': 'Raccoons douse food in water to soften the horny skin of their paws, significantly '
                              'increasing tactile sensitivity when inspecting objects.'},
        'aliases': ['yenot', 'енот', 'енот-полоскун', 'raccoon']},
    {   'id': 'nature_emoji_094_red_panda',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🦊 + 🐼 + 🎋 + 🍎",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🦊 + 🐼 + 🎋 + 🍎',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🦊 + 🐼 + 🎋 + 🍎'},
        'options': {   'uz': ['Ulkan panda', 'Qizil panda (Kichik panda)', 'Yenot', 'Sincob'],
                       'ru': ['Большая панда', 'Малая (красная) панда', 'Енот', 'Белка'],
                       'en': ['Giant Panda', 'Red Panda', 'Raccoon', 'Squirrel']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qizil panda (Kichik panda)', 'ru': 'Малая (красная) панда', 'en': 'Red Panda'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Red_Panda_fur_detail.jpg/800px-Red_panda.jpg',
        'fun_fact': {   'uz': "Qizil panda aslida ayiq emas, balki alohida Ailuridae oilasining yagona a'zosi bo'lib, "
                              "uning dumida 12 ta qizg'ish halqa bo'ladi.",
                        'ru': 'Красная панда не родственник большой панды, а представитель собственного древнего '
                              'семейства, использующий хвост как теплое одеяло.',
                        'en': 'The red panda is not a bear, but the sole surviving member of the ancient family '
                              'Ailuridae, wrapping its ringed tail around itself in snow.'},
        'aliases': ['qizil panda', 'малая панда', 'красная панда', 'red panda']},
    {   'id': 'nature_emoji_095_wolverine',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐻 + 🦡 + ❄️ + ⚔️",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐻 + 🦡 + ❄️ + ⚔️',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐻 + 🦡 + ❄️ + ⚔️'},
        'options': {   'uz': ["Bo'rsiq", "Asalxo'r", 'Rosomaxa', "Bo'ri"],
                       'ru': ['Барсук', 'Медоед', 'Росомаха', 'Волк'],
                       'en': ['Badger', 'Honey Badger', 'Wolverine', 'Wolf']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Rosomaxa', 'ru': 'Росомаха', 'en': 'Wolverine'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Wolverine_frost_resistant_fur_macro.jpg/800px-Wolverine.jpg',
        'fun_fact': {   'uz': "Rosomaxa o'zidan 5 baravar katta bo'lgan kiyik va loslarni qor qatlamida quvib yetib, "
                              'ulkan panjalari bilan changallaydi.',
                        'ru': 'Широкие лапы росомахи действуют как снегоступы, позволяя ей без труда догонять тяжелых '
                              'лосей и оленей по глубокому снегу.',
                        'en': 'Wolverines sport broad, snowshoe-like paws with non-retractable claws, easily '
                              'traversing deep snow to take down adult caribou and moose.'},
        'aliases': ['rosomaxa', 'росомаха', 'wolverine']},
    {   'id': 'nature_emoji_096_snow_leopard',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐆 + ❄️ + 🏔️ + 👻",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐆 + ❄️ + 🏔️ + 👻',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐆 + ❄️ + 🏔️ + 👻'},
        'options': {   'uz': ['Gepard', 'Qoplon', 'Silovsin', "Qor qoploni (Ilvirs / Tog' arvohi)"],
                       'ru': ['Гепард', 'Леопард', 'Рысь', 'Снежный барс (Ирбис)'],
                       'en': ['Cheetah', 'Leopard', 'Lynx', 'Snow Leopard']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Qor qoploni (Ilvirs / Tog' arvohi)",
                              'ru': 'Снежный барс (Ирбис)',
                              'en': 'Snow Leopard'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Snow_leopard_fur_macro.jpg/800px-Snow_leopard.jpg',
        'fun_fact': {   'uz': "Ilvirs o'zining 1 metrli qalin dumini sakrash paytida rul sifatida va uxlab yotganida "
                              "burni va og'zini sovuqdan to'suvchi ro'mol sifatida ishlatadi.",
                        'ru': 'Ирбис совершает прыжки до 15 метров над горными пропастями, балансируя толстым пушистым '
                              'хвостом, которым греется в мороз.',
                        'en': 'Snow leopards can leap 15 meters across mountain gorges, wrapping their meter-long '
                              'bushy tail around their face during sleep.'},
        'aliases': ['ilvirs', 'qor qoploni', 'ирбис', 'снежный барс', 'snow leopard']},
    {   'id': 'nature_emoji_097_cheetah',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐆 + ⚡ + 🏎️ + 💨",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐆 + ⚡ + 🏎️ + 💨',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐆 + ⚡ + 🏎️ + 💨'},
        'options': {   'uz': ['Gepard', 'Qoplon', 'Yaguar', 'Puma'],
                       'ru': ['Гепард', 'Леопард', 'Ягуар', 'Пума'],
                       'en': ['Cheetah', 'Leopard', 'Jaguar', 'Cougar']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Gepard', 'ru': 'Гепард', 'en': 'Cheetah'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cheetah_fur_macro.jpg/800px-Cheetah.jpg',
        'fun_fact': {   'uz': 'Gepardning tirnoqlari boshqa mushuklar kabi ichkariga kirmaydi; ular yerga shpovka kabi '
                              "botib, tez yugurishda tortishni ta'minlaydi.",
                        'ru': 'Когти гепарда полувтяжные, как шипы на бутсах спринтера, обеспечивая надежное сцепление '
                              'с грунтом на виражах.',
                        'en': "Unlike other felids, a cheetah's semi-retractable claws function like athletic running "
                              'cleats to maintain traction during high-speed turns.'},
        'aliases': ['gepard', 'гепард', 'cheetah']},
    {   'id': 'nature_emoji_098_giant_sequoia_tree',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🌲 + 🏛️ + 🇺🇸 + 🪵",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🌲 + 🏛️ + 🇺🇸 + 🪵',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🌲 + 🏛️ + 🇺🇸 + 🪵'},
        'options': {   'uz': ["Qarag'ay", 'Ulkan sekvoya (Mamont daraxti)', 'Baobab', 'Bambuk'],
                       'ru': ['Сосна', 'Гигантская секвойя (Мамонтово дерево)', 'Баобаб', 'Бамбук'],
                       'en': ['Pine', 'Giant Sequoia Tree', 'Baobab', 'Bamboo']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Ulkan sekvoya (Mamont daraxti)',
                              'ru': 'Гигантская секвойя (Мамонтово дерево)',
                              'en': 'Giant Sequoia Tree'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/General_Sherman_tree_sequoia.jpg/800px-Giant_sequoia.jpg',
        'fun_fact': {   'uz': "Sekvoya po'stlog'i 60 santimetrgacha qalinlikda bo'lib, uning tarkibidagi tannidlar "
                              "daraxtni o'rmon yong'inlaridan to'liq asraydi.",
                        'ru': 'Кора секвойи толщиной более полуметра пропитана танинами и не горит в огне, защищая '
                              '3000-летние деревья от пожаров.',
                        'en': 'Giant sequoia bark is up to 60 cm thick and fire-resistant, insulated with tannic acids '
                              'that protect against catastrophic crown fires.'},
        'aliases': ['sekvoya', 'мамont daraxti', 'секвойя', 'мамонтово дерево', 'giant sequoia']},
    {   'id': 'nature_emoji_099_cassowary',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐦 + 👑 + 🥊 + 🔪",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐦 + 👑 + 🥊 + 🔪',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐦 + 👑 + 🥊 + 🔪'},
        'options': {   'uz': ['Tuyaqush', 'Emu', 'Janubiy kazuar', 'Kivi'],
                       'ru': ['Страус', 'Эму', 'Шлемоносный казуар', 'Киви'],
                       'en': ['Ostrich', 'Emu', 'Southern Cassowary', 'Kiwi']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Janubiy kazuar', 'ru': 'Шлемоносный казуар', 'en': 'Southern Cassowary'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Casuarius_casuarius_head_casque.jpg/800px-Cassowary.jpg',
        'fun_fact': {   'uz': "Kazuar boshidagi shoxsimon kaskasi bilan o'rmon shoxlarini yorib o'tadi va uning 12 sm "
                              "lik pichoqdek o'tkir o'rta tirnog'i eng xavfli quroldir.",
                        'ru': 'Книга рекордов Гиннесса называет казуара самой опасной птицей в мире из-за '
                              'кинжаловидных когтей длиной 12 см.',
                        'en': "Dubbed the world's most dangerous bird by Guinness, the southern cassowary kicks with "
                              '12-cm dagger-like inner claws.'},
        'aliases': ['kazuar', 'казуар', 'шлемоносный казуар', 'cassowary']},
    {   'id': 'nature_emoji_100_poison_dart_frog',
        'sub_mode': 'nature_emoji',
        'question': {   'uz': "Ushbu emojilar qaysi qiziqarli jonzot yoki o'simlikni ifodalaydi? 🐸 + ☠️ + 🏹 + 🎨",
                        'ru': 'Какое удивительное животное или растение зашифровано в этих эмодзи? 🐸 + ☠️ + 🏹 + 🎨',
                        'en': 'Which fascinating animal or plant is represented by these emojis? 🐸 + ☠️ + 🏹 + 🎨'},
        'options': {   'uz': ['Qurbaqa', 'Aksolotl', 'Salamandra', 'Zaharli daraxtbaqa (Drevolaz)'],
                       'ru': ['Жаба', 'Аксалотль', 'Саламандра', 'Ужасный листолаз (Ядовитая лягушка)'],
                       'en': ['Toad', 'Axolotl', 'Salamander', 'Golden Poison Frog']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Zaharli daraxtbaqa (Drevolaz)',
                              'ru': 'Ужасный листолаз (Ядовитая лягушка)',
                              'en': 'Golden Poison Frog'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Dendrobates_tinctorius_skin_macro.jpg/800px-Poison_frog.jpg',
        'fun_fact': {   'uz': "Uzunligi atigi 5 santimetr bo'lgan sariq barglarning terisidagi zahar 10 000 ta "
                              "sichqonni yoki 10-20 nafar katta odamni o'ldirishga kifoya qiladi.",
                        'ru': 'Яда одной крошечной золотистой лягушки Phyllobates terribilis достаточно, чтобы '
                              'отправить на тот свет 10-20 взрослых людей.',
                        'en': 'Phyllobates terribilis secretes enough lethal batrachotoxin alkaloid through its skin '
                              'to kill 10 to 20 adult humans.'},
        'aliases': ['drevolaz', 'zaharli baqa', 'листолаз', 'древолаз', 'poison dart frog', 'golden poison frog']},
    {   'id': 'nature_anatomy_001_smallest_bone',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson tanasidagi eng kichik suyak qaysi (uzunligi atigi 3 mm)?',
                        'ru': 'Какая кость является самой маленькой в теле человека (длина всего около 3 мм)?',
                        'en': 'Which is the smallest bone in the human body (measuring only about 3 mm)?'},
        'options': {   'uz': [   "Uzangi suyagi (Stapes / O'rta quloq)",
                                 "Bolg'acha (Malleus)",
                                 'Sandoncha (Incus)',
                                 'Burun suyagi'],
                       'ru': ['Стремечко (в среднем ухе)', 'Молоточек', 'Наковальня', 'Носовая кость'],
                       'en': [   'Stapes (Stirrup bone in middle ear)',
                                 'Malleus (Hammer)',
                                 'Incus (Anvil)',
                                 'Nasal bone']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Uzangi suyagi (Stapes / O'rta quloq)",
                              'ru': 'Стремечко (в среднем ухе)',
                              'en': 'Stapes (Stirrup bone in middle ear)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Stapes_middle_ear_macro.jpg/800px-Stapes_bone.jpg',
        'fun_fact': {   'uz': "Uzangi suyagi o'rta quloqda joylashgan bo'lib, uning vazni atigi 3 milligrammni tashkil "
                              "etadi va u nog'ora pardasidagi tovush tebranishlarini ichki quloqqa uzatadi.",
                        'ru': 'Стремечко весит около 3 мг и передает звуковые колебания от наковальни к овальному окну '
                              'улитки внутреннего уха.',
                        'en': 'The stapes bone in the middle ear weighs only 3 milligrams and transmits sound '
                              "vibrations from the incus to the cochlea's oval window."},
        'aliases': ['uzangi', 'uzangi suyagi', 'стремечко', 'stapes', 'stirrup']},
    {   'id': 'nature_anatomy_002_longest_strongest_bone',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson skeletidagi eng uzun va eng baquvvat suyak qaysi?',
                        'ru': 'Какая кость в скелете человека является самой длинной и прочной?',
                        'en': 'Which is the longest and strongest bone in the human skeleton?'},
        'options': {   'uz': ['Katta boldir suyagi', 'Son suyagi (Femur)', 'Yelka suyagi', "Qovurg'a"],
                       'ru': ['Большеберцовая кость', 'Бедренная кость', 'Плечевая кость', 'Ребро'],
                       'en': ['Tibia (Shin bone)', 'Femur (Thigh bone)', 'Humerus', 'Rib']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Son suyagi (Femur)', 'ru': 'Бедренная кость', 'en': 'Femur (Thigh bone)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Human_femur_bone.jpg/800px-Human_femur.jpg',
        'fun_fact': {   'uz': "Son suyagi inson bo'yining taxminan 27% ini tashkil qiladi va u beton kabi 1.5–2 "
                              "tonnagacha bo'lgan og'irlik bosimiga chiday oladi.",
                        'ru': 'Бедренная кость выдерживает нагрузку на сжатие до 1,5–2 тонн, что прочнее '
                              'железобетонной балки аналогичного веса.',
                        'en': "The femur accounts for roughly 27% of a person's height and can support vertical "
                              'compression loads up to 1,500–2,000 kg.'},
        'aliases': ['son suyagi', 'femur', 'бедренная кость', 'femur']},
    {   'id': 'nature_anatomy_003_only_floating_bone',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tanasidagi boshqa birorta ham suyak bilan bo'g'im hosil qilmaydigan yagona suyak "
                              'qaysi?',
                        'ru': 'Какая единственная кость в теле человека не сочленена ни с одной другой костью скелета?',
                        'en': 'Which is the only bone in the human body that does not articulate with any other bone?'},
        'options': {   'uz': ["To'sh suyagi", 'Kurak suyagi', 'Til osti suyagi (Hyoid)', 'Dumsuyuq'],
                       'ru': ['Грудина', 'Лопатка', 'Подъязычная кость', 'Копчик'],
                       'en': ['Sternum', 'Scapula', 'Hyoid bone', 'Coccyx']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Til osti suyagi (Hyoid)', 'ru': 'Подъязычная кость', 'en': 'Hyoid bone'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Hyoid_bone_human.jpg/800px-Hyoid_bone.jpg',
        'fun_fact': {   'uz': 'Til osti suyagi tomoqda boylamlar va mushaklar orqali osilib turadi; u insonning aniq '
                              "nutq so'zlashi va yutishida hal qiluvchi rol o'ynaydi.",
                        'ru': 'Подъязычная кость имеет подковообразную форму, подвешена на связках в области гортани и '
                              'обеспечивает артикуляцию речи.',
                        'en': 'The horseshoe-shaped hyoid bone is suspended in the throat purely by muscles and '
                              'ligaments, essential for vocal articulation and swallowing.'},
        'aliases': ['til osti suyagi', 'hyoid', 'подъязычная кость', 'hyoid bone']},
    {   'id': 'nature_anatomy_004_total_bones_adult',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Voyaga yetgan sog'lom inson tanasida nechta suyak mavjud?",
                        'ru': 'Сколько костей насчитывает скелет взрослого здорового человека?',
                        'en': 'How many bones are there in an adult human skeleton?'},
        'options': {   'uz': ['300 ta', '180 ta', '248 ta', '206 ta'],
                       'ru': ['300 костей', '180 костей', '248 костей', '206 костей'],
                       'en': ['300 bones', '180 bones', '248 bones', '206 bones']},
        'correct_index': 3,
        'correct_answer': {'uz': '206 ta', 'ru': '206 костей', 'en': '206 bones'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Human_skeleton_front_en.svg/800px-Human_skeleton.jpg',
        'fun_fact': {   'uz': "Chaqaloq tug'ilganda 270–300 tagacha suyak bilan dunyoga keladi; o'sish jarayonida "
                              "ko'plab mayda suyaklar bir-biri bilan birikib 206 taga tushadi.",
                        'ru': 'Младенцы рождаются примерно с 300 костями, но по мере роста часть костей черепа, таза и '
                              'позвоночника срастаются в единые структуры.',
                        'en': 'Humans are born with ~300 bones, many of which fuse together during childhood and '
                              'adolescence to form the 206 bones of adulthood.'},
        'aliases': ['206', '206 ta', '206 костей', '206 bones']},
    {   'id': 'nature_anatomy_005_strongest_muscle_pressure',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Tishlash va bosim kuchi bo'yicha inson tanasidagi eng baquvvat mushak qaysi?",
                        'ru': 'Какая мышца человека развивает наибольшую силу давления относительно своего размера?',
                        'en': 'Which muscle in the human body can exert the greatest pressure force relative to its '
                              'size?'},
        'options': {   'uz': ['Chaynov mushagi (Masseter)', 'Katta dumba mushagi', 'Biceps', "Son to'rtboshli mushagi"],
                       'ru': [   'Жевательная мышца (Массетер)',
                                 'Большая ягодичная мышца',
                                 'Бицепс',
                                 'Четырехглавая мышца бедра'],
                       'en': ['Masseter (Jaw muscle)', 'Gluteus maximus', 'Biceps brachii', 'Quadriceps femoris']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Chaynov mushagi (Masseter)',
                              'ru': 'Жевательная мышца (Массетер)',
                              'en': 'Masseter (Jaw muscle)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Masseter_muscle_head.jpg/800px-Masseter_muscle.jpg',
        'fun_fact': {   'uz': "Chaynov mushaklari jag' tishlarida 90–100 kg gacha bosim kuchini hosil qila oladi; "
                              "rekord ko'rsatkich esa 442 kg ni tashkil etgan.",
                        'ru': 'Жевательные мышцы способны смыкать коренные зубы с усилием до 100 кг, а рекордсмен '
                              'Ричард Хоффман развил усилие в 442 кг.',
                        'en': 'The masseter can contract to produce bite forces exceeding 90–100 kg on molars, holding '
                              'the Guinness record for human bite pressure.'},
        'aliases': ['chaynov mushagi', 'masseter', 'жевательная мышца', 'массетер', 'masseter']},
    {   'id': 'nature_anatomy_006_largest_muscle_volume',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tanasidagi massasi va hajmi bo'yicha eng katta mushak qaysi?",
                        'ru': 'Какая мышца в теле человека является самой большой по массе и объему?',
                        'en': 'Which is the largest muscle in the human body by volume and mass?'},
        'options': {   'uz': [   'Keng orqa mushagi',
                                 'Katta dumba mushagi (Gluteus maximus)',
                                 "Son to'rtboshli mushagi",
                                 "Ko'krak katta mushagi"],
                       'ru': [   'Широчайшая мышца спины',
                                 'Большая ягодичная мышца',
                                 'Квадрицепс',
                                 'Большая грудная мышца'],
                       'en': ['Latissimus dorsi', 'Gluteus maximus', 'Quadriceps', 'Pectoralis major']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Katta dumba mushagi (Gluteus maximus)',
                              'ru': 'Большая ягодичная мышца',
                              'en': 'Gluteus maximus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Gluteus_maximus_anatomy.jpg/800px-Gluteus_maximus.jpg',
        'fun_fact': {   'uz': 'Katta dumba mushagi odamning ikki oyoqda tik turishi, qomatni saqlashi va zinadan '
                              "ko'tarilishida asosiy kuchni ta'minlaydi.",
                        'ru': 'Большая ягодичная мышца развилась в процессе прямохождения и удерживает туловище в '
                              'вертикальном положении при ходьбе и беге.',
                        'en': 'Gluteus maximus evolved specifically for bipedalism, maintaining erect posture and '
                              'powering hip extension during running.'},
        'aliases': ['dumba mushagi', 'gluteus maximus', 'большая ягодичная мышца', 'gluteus']},
    {   'id': 'nature_anatomy_007_smallest_muscle',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson tanasidagi eng kichik mushak qaysi (uzunligi atigi 1 mm)?',
                        'ru': 'Какая мышца является самой крошечной в теле человека (длина чуть более 1 мм)?',
                        'en': 'Which is the smallest muscle in the human body (measuring barely over 1 mm in length)?'},
        'options': {   'uz': [   'Qorachiq mushagi',
                                 'Kiprik mushagi',
                                 'Uzangi mushagi (Stapedius)',
                                 "Soch ko'taruvchi mushak"],
                       'ru': ['Мышца зрачка', 'Ресничная мышца', 'Стременная мышца', 'Мышца, поднимающая волос'],
                       'en': ['Pupillary sphincter', 'Ciliary muscle', 'Stapedius muscle', 'Arrector pili']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Uzangi mushagi (Stapedius)', 'ru': 'Стременная мышца', 'en': 'Stapedius muscle'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Stapedius_middle_ear_muscle.jpg/800px-Stapedius.jpg',
        'fun_fact': {   'uz': "Uzangi mushagi quloqqa to'satdan juda baland tovush urilganda uzangi suyagini tortib "
                              "qotiradi va eshitish nervlarini kar bo'lishdan saqlaydi.",
                        'ru': 'Стременная мышца сокращается при громких звуках, демпфируя вибрацию стремечка и защищая '
                              'внутреннее ухо от акустической травмы.',
                        'en': 'The stapedius muscle dampens excess vibration of the stapes bone during loud sounds to '
                              'protect inner ear hair cells from acoustic trauma.'},
        'aliases': ['uzangi mushagi', 'stapedius', 'стременная мышца', 'stapedius muscle']},
    {   'id': 'nature_anatomy_008_hardest_substance_body',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tanasidagi eng qattiq to'qima (substansiya) nima?",
                        'ru': 'Какое вещество в теле человека является самым твердым (тверже костей)?',
                        'en': 'Which substance in the human body is the hardest (harder than structural bone)?'},
        'options': {   'uz': ['Son suyagi', 'Tirnoq', 'Bosh suyagi', 'Tish emali (Tooth enamel)'],
                       'ru': ['Кость бедра', 'Ногти', 'Кости черепа', 'Зубная эмаль'],
                       'en': ['Femur bone', 'Nails', 'Cranial bone', 'Tooth enamel']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Tish emali (Tooth enamel)', 'ru': 'Зубная эмаль', 'en': 'Tooth enamel'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tooth_enamel_microstructure.jpg/800px-Tooth_enamel.jpg',
        'fun_fact': {   'uz': "Tish emalining 96% qismi gidroksiapatit mineral kristallaridan iborat bo'lib, uning "
                              'qattiqligi Moos shkalasida 5 ga teng.',
                        'ru': 'Эмаль зубов на 96% состоит из минерала гидроксиапатита кальция, превосходя по твердости '
                              'сталь и железо.',
                        'en': 'Tooth enamel is 96% crystalline hydroxyapatite mineral, reaching 5 on the Mohs '
                              'scale—harder than structural steel.'},
        'aliases': ['tish emali', 'emal', 'зубная эмаль', 'эмаль', 'tooth enamel', 'enamel']},
    {   'id': 'nature_anatomy_009_largest_internal_organ',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson organizmidagi eng katta ichki a'zo va eng yirik bez qaysi?",
                        'ru': 'Какой внутренний орган является самым крупным и тяжелым в организме человека?',
                        'en': 'Which internal organ is the largest and heaviest inside the human body?'},
        'options': {   'uz': ['Jigar (Liver)', "O'pka", 'Miya', 'Oshqozon'],
                       'ru': ['Печень', 'Легкие', 'Головной мозг', 'Желудок'],
                       'en': ['Liver', 'Lungs', 'Brain', 'Stomach']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Jigar (Liver)', 'ru': 'Печень', 'en': 'Liver'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Human_liver_anatomy.jpg/800px-Liver.jpg',
        'fun_fact': {   'uz': 'Jigar taxminan 1.5 kg tosh bosadi va u organizmda 500 dan ortiq hayotiy kimyoviy '
                              'funksiyalarni, jumladan toksinlarni tozalashni bajaradi.',
                        'ru': 'Печень взрослого человека весит около 1,5 кг, выполняя более 500 жизненно важных '
                              'биохимических функций одновременно.',
                        'en': 'The human liver weighs approximately 1.5 kg and performs over 500 vital metabolic '
                              'functions, including detoxifying blood and bile synthesis.'},
        'aliases': ['jigar', 'печень', 'liver']},
    {   'id': 'nature_anatomy_010_largest_organ_total',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tanasining umumiy maydoni va og'irligi bo'yicha mutlaq eng katta a'zosi nima?",
                        'ru': 'Какой орган является самым большим по площади и общей массе во всем теле человека?',
                        'en': 'Which is the absolute largest organ of the human body by surface area and total '
                              'weight?'},
        'options': {   'uz': ['Jigar', 'Teri (Skin)', 'Ichaklar', 'Miya'],
                       'ru': ['Печень', 'Кожа', 'Кишечник', 'Головной мозг'],
                       'en': ['Liver', 'Skin (Integumentary system)', 'Intestines', 'Brain']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Teri (Skin)', 'ru': 'Кожа', 'en': 'Skin (Integumentary system)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Human_skin_layers.jpg/800px-Skin_layers.jpg',
        'fun_fact': {   'uz': "Katta odam terisining umumiy maydoni taxminan 2 kvadrat metrni, og'irligi esa tana "
                              'vaznining 15% ini (3.5–4 kg) tashkil etadi.',
                        'ru': 'Кожа взрослого человека имеет площадь около 2 м² и весит до 4 кг, являясь мощным '
                              'барьером от микробов и обезвоживания.',
                        'en': 'Human skin covers roughly 2 square meters of surface area and accounts for about 15% of '
                              'total body weight (3.5–4 kg).'},
        'aliases': ['teri', 'кожа', 'skin']},
    {   'id': 'nature_anatomy_011_red_blood_cell_lifespan',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson qonidagi qizil qon tanachalari (eritrotsitlar) o'rtacha necha kun yashaydi?",
                        'ru': 'Какова средняя продолжительность жизни эритроцита в кровеносном русле человека?',
                        'en': 'What is the average lifespan of a human red blood cell (erythrocyte) in circulation?'},
        'options': {   'uz': ['30 kun', '365 kun', '120 kun (taxminan 4 oy)', '7 kun'],
                       'ru': ['30 дней', '365 дней', '120 дней (около 4 месяцев)', '7 дней'],
                       'en': ['30 days', '365 days', '120 days (around 4 months)', '7 days']},
        'correct_index': 2,
        'correct_answer': {   'uz': '120 kun (taxminan 4 oy)',
                              'ru': '120 дней (около 4 месяцев)',
                              'en': '120 days (around 4 months)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Red_blood_cells_erythrocytes.jpg/800px-Erythrocytes.jpg',
        'fun_fact': {   'uz': 'Eritrotsitlar har soniyada 2-3 million donadan yangilanadi; qarigan eritrotsitlar taloq '
                              'va jigarda parchalanib qayta ishlanadi.',
                        'ru': 'Каждую секунду костный мозг производит более 2 миллионов новых эритроцитов взамен '
                              'разрушенных в селезенке.',
                        'en': 'Bone marrow produces ~2.4 million erythrocytes per second to replace aged cells '
                              'recycled by macrophage phagocytosis in the spleen.'},
        'aliases': ['120 kun', '120', '120 дней', '120 days']},
    {   'id': 'nature_anatomy_012_total_blood_vessels_length',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Bitta katta odam tanasidagi barcha qon tomirlarining (kapillyarlar, venalar, '
                              'arteriyalar) umumiy uzunligi qancha?',
                        'ru': 'Какова суммарная длина всех кровеносных сосудов в теле одного взрослого человека?',
                        'en': 'What is the approximate total combined length of all blood vessels in a single adult '
                              'human body?'},
        'options': {   'uz': ['10 000 kilometr', '40 000 kilometr', '1 million kilometr', 'Qariyb 100 000 kilometr'],
                       'ru': [   '10 000 километров',
                                 '40 000 километров',
                                 '1 миллион километров',
                                 'Около 100 000 километров'],
                       'en': [   '10,000 kilometers',
                                 '40,000 kilometers',
                                 '1,000,000 kilometers',
                                 'Around 100,000 kilometers']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Qariyb 100 000 kilometr',
                              'ru': 'Около 100 000 километров',
                              'en': 'Around 100,000 kilometers'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Circulatory_System_en.svg/800px-Circulatory_system.jpg',
        'fun_fact': {   'uz': "Inson qon tomirlarini bitta chiziqqa ulasa, ular Yer sharini ekvator bo'ylab 2.5 marta "
                              'aylantirib chiqishga yetadi.',
                        'ru': 'Если вытянуть все сосуды человека в одну линию, ими можно обернуть Землю по экватору '
                              'два с половиной раза.',
                        'en': 'If laid end to end, the capillaries, veins, and arteries of one human would stretch '
                              'roughly 100,000 km—encircling Earth 2.5 times.'},
        'aliases': ['100 000 km', '100000 km', '100000', '100 000 километров', '100,000 km']},
    {   'id': 'nature_anatomy_013_universal_red_cell_donor',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Qaysi qon guruhi har qanday boshqa qon guruhiga quyish mumkin bo'lgan 'universal donor' "
                              'eritrotsitlariga ega?',
                        'ru': 'Какая группа крови является «универсальным донором» эритроцитарной массы для всех '
                              'людей?',
                        'en': 'Which blood group is designated as the universal red blood cell donor for '
                              'transfusions?'},
        'options': {   'uz': ['O (I) rezus manfiy (O Rh-)', 'AB (IV) musbat', 'A (II) manfiy', 'B (III) musbat'],
                       'ru': [   'I группа резус-отрицательная (O Rh-)',
                                 'IV группа резус-положительная (AB Rh+)',
                                 'II группа (A Rh-)',
                                 'III группа (B Rh+)'],
                       'en': [   'O negative (O Rh-)',
                                 'AB positive (AB Rh+)',
                                 'A negative (A Rh-)',
                                 'B positive (B Rh+)']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'O (I) rezus manfiy (O Rh-)',
                              'ru': 'I группа резус-отрицательная (O Rh-)',
                              'en': 'O negative (O Rh-)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Blood_group_compatibility.svg/800px-Blood_groups.jpg',
        'fun_fact': {   'uz': "O manfiy qon guruhida A va B agglyutinogenlar hamda Rh oqsili bo'lmagani sababli, qabul "
                              'qiluvchining immuniteti ularga hujum qilmaydi.',
                        'ru': 'На мембране эритроцитов группы O (I) Rh- нет антигенов A, B и резус-фактора, поэтому '
                              'они не вызывают агглютинации у реципиентов.',
                        'en': 'Type O-negative red blood cells lack A, B, and Rh surface antigens, allowing emergency '
                              'transfusion into patients of any blood type.'},
        'aliases': ['o manfiy', 'o rh-', '1-guruh', 'i группа', 'o negative', 'o-']},
    {   'id': 'nature_anatomy_014_universal_plasma_donor',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Qon plazmasi bo'yicha har qanday bemorga mos keluvchi 'universal plazma donori' qaysi "
                              'qon guruhi hisoblanadi?',
                        'ru': 'Плазма какой группы крови является универсальной для переливания любому человеку?',
                        'en': 'Which blood type serves as the universal plasma donor, free from anti-A and anti-B '
                              'antibodies?'},
        'options': {   'uz': ['O (I) manfiy', 'AB (IV) musbat / AB', 'A (II)', 'B (III)'],
                       'ru': ['I группа (O)', 'IV группа (AB)', 'II группа (A)', 'III группа (B)'],
                       'en': ['O negative', 'AB positive / AB', 'Type A', 'Type B']},
        'correct_index': 1,
        'correct_answer': {'uz': 'AB (IV) musbat / AB', 'ru': 'IV группа (AB)', 'en': 'AB positive / AB'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Blood_group_compatibility.svg/800px-Blood_groups.jpg',
        'fun_fact': {   'uz': "AB guruhi plazmasida A va B antitanachalari umuman bo'lmaydi, shuning uchun uning "
                              'plazmasini istalgan qon guruhiga quyish xavfsizdir.',
                        'ru': 'Плазма группы AB не содержит естественных агглютининов анти-А и анти-В, что исключает '
                              'разрушение эритроцитов больного.',
                        'en': 'Type AB blood plasma contains neither anti-A nor anti-B antibodies, making it '
                              'universally safe for transfusion to any recipient.'},
        'aliases': ['ab', 'ab musbat', '4-guruh', 'iv группа', 'ab positive', 'ab plasma']},
    {   'id': 'nature_anatomy_015_heart_daily_output',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson yuragi bir sutka davomida tana bo'ylab qancha litr qon haydaydi?",
                        'ru': 'Сколько примерно литров крови перекачивает сердце взрослого человека за одни сутки?',
                        'en': 'Approximately how many liters of blood does an adult human heart pump in a single '
                              '24-hour day?'},
        'options': {   'uz': ['500 litr', '2000 litr', 'Taxminan 7000–7500 litr', '50 000 litr'],
                       'ru': ['500 литров', '2000 литров', 'Около 7000–7500 литров', '50 000 литров'],
                       'en': ['500 liters', '2,000 liters', 'Around 7,000–7,500 liters', '50,000 liters']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Taxminan 7000–7500 litr',
                              'ru': 'Около 7000–7500 литров',
                              'en': 'Around 7,000–7,500 liters'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Diagram_of_the_human_heart_%28cropped%29.svg/800px-Heart_diagram.jpg',
        'fun_fact': {   'uz': 'Yurak har zarbada 70 ml qon chiqaradi; bu 1 kunda qariyb 7500 litrni, butun umr '
                              'davomida esa 200 million litrdan ortiqni tashkil qiladi.',
                        'ru': 'За 70 лет жизни сердце совершает более 2,5 миллиардов ударов и перекачивает объем '
                              'крови, достаточный для наполнения 80 олимпийских бассейнов.',
                        'en': 'At ~70 ml per beat and 100,000 beats daily, the heart pumps ~7,500 liters (2,000 '
                              'gallons) every day, totaling ~200 million liters over a lifetime.'},
        'aliases': ['7500 litr', '7000 litr', '7500', '7500 литров', '7,500 liters']},
    {   'id': 'nature_anatomy_016_oxygen_binding_protein',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Eritrotsitlar tarkibidagi temir tutuvchi va kislorod tashuvchi asosiy murakkab oqsil '
                              'nima?',
                        'ru': 'Какой железосодержащий белок в эритроцитах связывает кислород и придает крови красный '
                              'цвет?',
                        'en': 'Which iron-containing metalloprotein in red blood cells binds oxygen and imparts red '
                              'coloration to blood?'},
        'options': {   'uz': ['Mioglobin', 'Fibrinogen', 'Albumin', 'Gemoglobin'],
                       'ru': ['Миоглобин', 'Фибриноген', 'Альбумин', 'Гемоглобин'],
                       'en': ['Myoglobin', 'Fibrinogen', 'Albumin', 'Hemoglobin']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Gemoglobin', 'ru': 'Гемоглобин', 'en': 'Hemoglobin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Hemoglobin_molecule_3d.jpg/800px-Hemoglobin.jpg',
        'fun_fact': {   'uz': 'Bitta gemoglobin molekulasi 4 ta kislorod molekulasini biriktira oladi; har bir '
                              "eritrotsitda 270 millionta gemoglobin molekulasi bo'ladi.",
                        'ru': 'Каждый эритроцит содержит около 270 миллионов молекул гемоглобина, способных переносить '
                              'свыше миллиарда молекул кислорода.',
                        'en': 'A single erythrocyte contains ~270 million hemoglobin molecules, each bearing four '
                              'iron-heme groups binding up to four O2 molecules.'},
        'aliases': ['gemoglobin', 'гемоглобин', 'hemoglobin']},
    {   'id': 'nature_anatomy_017_blood_clotting_cells',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Qon tomirlari shikastlanganda qon ivishini ta'minlab qon ketishini to'xtatuvchi "
                              'yadrosiz hujayra plastinkalari nima deb ataladi?',
                        'ru': 'Какие форменные элементы крови отвечают за свертывание крови и закупорку поврежденных '
                              'сосудов?',
                        'en': 'Which cell fragments circulate in blood and aggregate to form clots, stopping blood '
                              'loss after vascular injury?'},
        'options': {   'uz': ['Trombotsitlar (Qon plastinkalari)', 'Leykotsitlar', 'Eritrotsitlar', 'Monotsitlar'],
                       'ru': ['Тромбоциты (кровяные пластинки)', 'Лейкоциты', 'Эритроциты', 'Моноциты'],
                       'en': ['Platelets (Thrombocytes)', 'Leukocytes', 'Erythrocytes', 'Monocytes']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Trombotsitlar (Qon plastinkalari)',
                              'ru': 'Тромбоциты (кровяные пластинки)',
                              'en': 'Platelets (Thrombocytes)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Platelet_thrombocyte_activation_sem.jpg/800px-Platelets.jpg',
        'fun_fact': {   'uz': "Trombotsitlar qizil suyak ko'migidagi ulkan megakariotsit hujayralarining bo'linib "
                              'uzilgan parchalaridir; ularning umri 7-10 kun davom etadi.',
                        'ru': 'Тромбоциты образуются отщеплением от гигантских клеток мегакариоцитов и мгновенно '
                              'активируются, выбрасывая фибринные нити.',
                        'en': 'Platelets are anucleate fragments shed from bone marrow megakaryocytes that rapidly '
                              'polymerize fibrinogen into fibrin nets to seal wounds.'},
        'aliases': ['trombotsitlar', 'trombotsit', 'тромбоциты', 'platelets', 'thrombocytes']},
    {   'id': 'nature_anatomy_018_natural_pacemaker',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson yuragining elektr impulslarini avtomatik ravishda boshqaruvchi 'tabiiy ritm "
                              "yetakchisi' (peysmeyker) qaysi?",
                        'ru': 'Какой узел проводящей системы сердца является естественным водителем ритма '
                              '(пейсмейкером)?',
                        'en': "Which intrinsic node in the cardiac conduction system acts as the heart's natural "
                              'pacemaker?'},
        'options': {   'uz': [   'Atrioventrikulyar tugun (AV)',
                                 'Sinoatrial tugun (SA tuguni / Kis-Flak tuguni)',
                                 'Gis tutami',
                                 'Purkinye tolalari'],
                       'ru': [   'Атриовентрикулярный узел',
                                 'Синусно-предсердный узел (Синоатриальный)',
                                 'Пучок Гиса',
                                 'Волокна Пуркинье'],
                       'en': [   'Atrioventricular node (AV)',
                                 'Sinoatrial node (SA node)',
                                 'Bundle of His',
                                 'Purkinje fibers']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Sinoatrial tugun (SA tuguni / Kis-Flak tuguni)',
                              'ru': 'Синусно-предсердный узел (Синоатриальный)',
                              'en': 'Sinoatrial node (SA node)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cardiac_conduction_system_en.svg/800px-SA_node.jpg',
        'fun_fact': {   'uz': "Sinoatrial tugun o'ng bo'lmacha devorida joylashgan bo'lib, daqiqasiga 60–80 marta "
                              'avtonom elektr impulslarini ishlab chiqaradi.',
                        'ru': 'Синоатриальный узел состоит из специализированных пейсмейкерных клеток, генерирующих '
                              'потенциалы действия без участия мозга.',
                        'en': 'The sinoatrial node in the right atrium initiates rhythmic action potentials via '
                              'hyperpolarization-activated cyclic nucleotide-gated channels.'},
        'aliases': [   'sa tuguni',
                       'sinoatrial tugun',
                       'синусный узел',
                       'синоатриальный узел',
                       'sinoatrial node',
                       'sa node']},
    {   'id': 'nature_anatomy_019_longest_nerve',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson tanasidagi eng uzun va eng qalin nerv qaysi (bel qismidan oyoq barmoqlarigacha '
                              'boradi)?',
                        'ru': 'Какой нерв является самым длинным и толстым в теле человека (идет от поясницы до '
                              'стопы)?',
                        'en': 'Which is the longest and widest single nerve in the human body, running from the lower '
                              'back down to the foot?'},
        'options': {   'uz': ['Sayyor nerv (Vagus)', 'Yelka nervi', 'Sedalish nervi (Sciatic nerve)', 'Femoral nerv'],
                       'ru': ['Блуждающий нерв', 'Лучевой нерв', 'Седалищный нерв', 'Бедренный нерв'],
                       'en': ['Vagus nerve', 'Radial nerve', 'Sciatic nerve', 'Femoral nerve']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Sedalish nervi (Sciatic nerve)', 'ru': 'Седалищный нерв', 'en': 'Sciatic nerve'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nervus_ischiadicus_sciatic.jpg/800px-Sciatic_nerve.jpg',
        'fun_fact': {   'uz': "Sedalish nervi qalinligi odamning bosh barmog'idek keladi va uning yallig'lanishi "
                              "'ishiomiya' (radikulit) og'rig'iga sabab bo'ladi.",
                        'ru': 'Седалищный нерв толщиной с большой палец руки иннервирует мышцы бедра, голени и стопы.',
                        'en': 'The sciatic nerve is roughly as thick as a human thumb, carrying sensory and motor '
                              'fibers from spinal roots L4 through S3.'},
        'aliases': ['sedalish nervi', 'sedalishe', 'седалищный нерв', 'sciatic nerve', 'sciatic']},
    {   'id': 'nature_anatomy_020_wandering_cranial_nerve',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Kalladan boshlanib qorin bo'shlig'igacha cho'ziluvchi va yurak, o'pka hamda oshqozonni "
                              'boshqaruvchi 10-bosh miya nervi qaysi?',
                        'ru': 'Какой 10-й черепной нерв называется «блуждающим» и контролирует работу сердца, легких и '
                              'пищеварения?',
                        'en': "Which tenth cranial nerve is known as the 'wandering nerve', regulating heart rate, "
                              'lungs, and digestive organs?'},
        'options': {   'uz': ["Ko'rish nervi", 'Uch shoxli nerv', 'Yuz nervi', 'Sayyor nerv (Vagus nervi)'],
                       'ru': ['Зрительный нерв', 'Тройничный нерв', 'Лицевой нерв', 'Блуждающий нерв (Nervus vagus)'],
                       'en': ['Optic nerve', 'Trigeminal nerve', 'Facial nerve', 'Vagus nerve (Cranial nerve X)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Sayyor nerv (Vagus nervi)',
                              'ru': 'Блуждающий нерв (Nervus vagus)',
                              'en': 'Vagus nerve (Cranial nerve X)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Vagus_nerve_cranial_X.jpg/800px-Vagus_nerve.jpg',
        'fun_fact': {   'uz': "Vagus nervi parasimpatik asab tizimining asosiy magistrali bo'lib, tinchlanganda yurak "
                              'urishini sekinlashtiradi va ichaklar harakatini faollashtiradi.',
                        'ru': 'Блуждающий нерв является главным кабелем парасимпатической нервной системы («отдыхай и '
                              'переваривай»), связывая мозг с внутренними органами.',
                        'en': 'The vagus nerve (CN X) represents 75% of parasympathetic outflow, modulating heart '
                              'rate, peristalsis, and the gut-brain axis.'},
        'aliases': ['vagus', 'sayyor nerv', 'блуждающий нерв', 'vagus nerve']},
    {   'id': 'nature_anatomy_021_neurons_count_brain',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson bosh miyasida taxminan nechta neyron (asab hujayrasi) mavjud?',
                        'ru': 'Сколько примерно нейронов насчитывает кора и подкорковые структуры головного мозга '
                              'человека?',
                        'en': 'Approximately how many neurons are there in an adult human brain?'},
        'options': {   'uz': ['Taxminan 86 milliard', '10 milliard', '500 milliard', '1 trillion'],
                       'ru': ['Около 86 миллиардов', '10 миллиардов', '500 миллиардов', '1 триллион'],
                       'en': ['Around 86 billion', '10 billion', '500 billion', '1 trillion']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Taxminan 86 milliard', 'ru': 'Около 86 миллиардов', 'en': 'Around 86 billion'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Human_brain_neurons_cortex.jpg/800px-Brain_neurons.jpg',
        'fun_fact': {   'uz': "Suzana Erkulano-Xuzel tadqiqotlariga ko'ra inson miyasida roppa-rosa 86 milliard neyron "
                              'va shuncha miqdorda gliya hujayralari bor.',
                        'ru': 'Каждый из 86 миллиардов нейронов образует до 10 000 синаптических связей, создавая '
                              'триллионы путей передачи информации.',
                        'en': "Dr. Suzana Herculano-Houzel's isotropic fractionator method verified ~86 billion "
                              'neurons and ~85 billion non-neuronal glial cells in the human brain.'},
        'aliases': ['86 milliard', '86', '86 миллиардов', '86 billion']},
    {   'id': 'nature_anatomy_022_brain_oxygen_consumption',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Bosh miya inson tana vaznining atigi 2% ini tashkil qilsa-da, tana energiyasi va '
                              "kislorodining qancha foizini iste'mol qiladi?",
                        'ru': 'Какой процент кислорода и глюкозы потребляет мозг, составляя всего 2% от массы тела '
                              'человека?',
                        'en': 'What percentage of total resting oxygen and glucose does the human brain consume '
                              'despite being only 2% of body mass?'},
        'options': {   'uz': ['5%', 'Taxminan 20%', '50%', '75%'],
                       'ru': ['5%', 'Около 20%', '50%', '75%'],
                       'en': ['5%', 'Around 20%', '50%', '75%']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Taxminan 20%', 'ru': 'Около 20%', 'en': 'Around 20%'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/PET_brain_metabolism_glucose.jpg/800px-Brain_glucose.jpg',
        'fun_fact': {   'uz': "Miya dam olayotganda ham 10-15 vatt quvvatdagi elektr energiyasini iste'mol qiladi; "
                              'uning asosiy qismi natriy-kaliy nasoslarini ishlatishga ketadi.',
                        'ru': 'Мозг сжигает пятую часть всей энергии тела даже во сне, поддерживая ионные градиенты на '
                              'клеточных мембранах.',
                        'en': 'The brain consumes ~20% of resting metabolic energy and oxygen (equivalent to a 15-watt '
                              'bulb), primarily powering Na+/K+-ATPase pumps.'},
        'aliases': ['20%', '20 foiz', '20 процентов', '20 percent']},
    {   'id': 'nature_anatomy_023_memory_consolidation_region',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Bosh miyada qisqa muddatli xotirani uzoq muddatli xotiraga aylantiruvchi (dengiz oti '
                              "shaklidagi) a'zo nima?",
                        'ru': 'Какая подкорковая структура мозга в форме морского конька отвечает за консолидацию '
                              'памяти и пространственную навигацию?',
                        'en': 'Which seahorse-shaped brain structure is critically responsible for consolidating '
                              'short-term memory into long-term storage?'},
        'options': {   'uz': ['Bodomsimon tana (Amigdala)', 'Miyacha', 'Gippokamp (Hippocampus)', 'Talamus'],
                       'ru': ['Миндалевидное тело (Амигдала)', 'Мозжечок', 'Гиппокамп', 'Таламус'],
                       'en': ['Amygdala', 'Cerebellum', 'Hippocampus', 'Thalamus']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Gippokamp (Hippocampus)', 'ru': 'Гиппокамп', 'en': 'Hippocampus'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Hippocampus_brain_mri.jpg/800px-Hippocampus.jpg',
        'fun_fact': {   'uz': 'Gippokamp har kecha chuqur uyqu paytida kungi voqealarni tahlil qilib, ularni miya '
                              "po'stlog'iga uzoq muddatli xotira sifatida muhrlaydi.",
                        'ru': 'Гиппокамп критически необходим для формирования новых воспоминаний; при его повреждении '
                              'человек теряет способность запоминать новые события.',
                        'en': 'The hippocampus replays episodic events during slow-wave sleep, coordinating '
                              'neocortical synaptic consolidation.'},
        'aliases': ['gippokamp', 'гиппокамп', 'hippocampus']},
    {   'id': 'nature_anatomy_024_motor_coordination_region',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Harakatlar aniqligi, muvozanat va tanani fazoda tutishni boshqaruvchi bosh miya bo'limi "
                              'qaysi?',
                        'ru': 'Какой отдел головного мозга отвечает за координацию движений, мышечный тонус и '
                              'сохранение равновесия?',
                        'en': 'Which brain structure coordinates voluntary motor precision, posture, and fine dynamic '
                              'balance?'},
        'options': {   'uz': ['Gipotalamus', "Ko'prik (Pons)", 'Uzunchoq miya', 'Miyacha (Cerebellum)'],
                       'ru': ['Гипоталамус', 'Мост мозга', 'Продолговатый мозг', 'Мозжечок'],
                       'en': ['Hypothalamus', 'Pons', 'Medulla oblongata', 'Cerebellum']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Miyacha (Cerebellum)', 'ru': 'Мозжечок', 'en': 'Cerebellum'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cerebellum_human_brain.jpg/800px-Cerebellum.jpg',
        'fun_fact': {   'uz': 'Miyacha butun miya hajmining 10% ini tashkil qilsa-da, unda barcha neyronlarning 50% '
                              "dan ortig'i (Purkinye hujayralari) jamlangan.",
                        'ru': 'В мозжечке сосредоточено более половины всех нейронов головного мозга, обрабатывающих '
                              'обратную связь от мышц и вестибулярного аппарата.',
                        'en': "The cerebellum contains over 50% of the brain's total neurons packed into densely "
                              'arborized Purkinje and granule cell networks.'},
        'aliases': ['miyacha', 'мозжечок', 'cerebellum']},
    {   'id': 'nature_anatomy_025_fastest_nerve_conduction_speed',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Miyelinlangan qalin asab tolalari bo'ylab asab impulslarining maksimal tarqalish "
                              'tezligi qancha?',
                        'ru': 'С какой максимальной скоростью передаются нервные импульсы по миелинизированным '
                              'волокнам человека?',
                        'en': 'What is the maximum propagation speed of nerve impulses along thick myelinated '
                              'alpha-motor axons?'},
        'options': {   'uz': [   'Sekundiga 100–120 metr (soatiga 400 km)',
                                 'Sekundiga 1 metr',
                                 'Sekundiga 10 metr',
                                 "Yorug'lik tezligida"],
                       'ru': [   '100–120 метров в секунду (до 430 км/ч)',
                                 '1 метр в секунду',
                                 '10 метров в секунду',
                                 'Со скоростью света'],
                       'en': ['100–120 meters per second (~430 km/h)', '1 m/s', '10 m/s', 'Speed of light']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Sekundiga 100–120 metr (soatiga 400 km)',
                              'ru': '100–120 метров в секунду (до 430 км/ч)',
                              'en': '100–120 meters per second (~430 km/h)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Myelin_sheath_saltatory_conduction.jpg/800px-Myelin_conduction.jpg',
        'fun_fact': {   'uz': "Miyelin qobig'i bilan o'ralgan tolalarda impuls Ranye tugunlari bo'ylab sakrab-sakrab "
                              "(saltator) o'tadi, bu esa tezlikni 120 m/s ga yetkazadi.",
                        'ru': 'Благодаря перехватам Ранвье на миелиновой оболочке потенциал действия скачет '
                              'сальтаторно со скоростью гоночного болида Formula 1.',
                        'en': 'Saltatory conduction jumping across Nodes of Ranvier accelerates action potential '
                              'velocities up to 120 m/s in A-alpha motor fibers.'},
        'aliases': ['120 m/s', '100-120 m/s', '120 м/с', '120 m/s']},
    {   'id': 'nature_anatomy_026_pleasure_reward_neurotransmitter',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson miyasida rag'batlantirish, qoniqish, lazzat va motivatsiyani boshqaruvchi asosiy "
                              'neyromediator nima?',
                        'ru': 'Какой нейромедиатор называют главным «веществом мотивации и вознаграждения» в мозге '
                              'человека?',
                        'en': 'Which neurotransmitter acts as the primary driver of motivation, anticipation, '
                              'reinforcement, and reward in the brain?'},
        'options': {   'uz': ['Serotonin', 'Dofamin (Dopamine)', 'GABA (GAMK)', 'Asetilxolin'],
                       'ru': ['Серотонин', 'Дофамин', 'ГАМК', 'Ацетилхолин'],
                       'en': ['Serotonin', 'Dopamine', 'GABA', 'Acetylcholine']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Dofamin (Dopamine)', 'ru': 'Дофамин', 'en': 'Dopamine'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Dopamine_chemical_structure.svg/800px-Dopamine.jpg',
        'fun_fact': {   'uz': "Dofamin kutilgan mukofot oldidan ajralib, odamda harakat qilishga ishtiyoq uyg'otadi; "
                              "uning yetishmovchiligi Parkinson kasalligiga sabab bo'ladi.",
                        'ru': 'Дофамин вырабатывается в черной субстанции и вентральной области покрышки, подталкивая '
                              'нас к достижению целей и обучению.',
                        'en': 'Synthesized in the substantia nigra and ventral tegmental area, dopamine regulates '
                              'mesolimbic incentive salience and motor initiation.'},
        'aliases': ['dofamin', 'дофамин', 'dopamine']},
    {   'id': 'nature_anatomy_027_mood_sleep_neurotransmitter',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Kayfiyat, umumiy xotirjamlik, ishtaha va uyqu fazalarini boshqaruvchi 'baxt gormoni' "
                              'nima?',
                        'ru': 'Какой нейромедиатор регулирует настроение, сон, аппетит и часто называется гормоном '
                              'хорошего самочувствия?',
                        'en': 'Which monoamine neurotransmitter predominantly regulates mood, emotional wellbeing, '
                              'appetite, and circadian cycles?'},
        'options': {   'uz': ['Dofamin', 'Adrenalin', 'Serotonin', 'Glutamat'],
                       'ru': ['Дофамин', 'Адреналин', 'Серотонин', 'Глутамат'],
                       'en': ['Dopamine', 'Adrenaline', 'Serotonin', 'Glutamate']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Serotonin', 'ru': 'Серотонин', 'en': 'Serotonin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Serotonin_molecule_ball_and_stick.jpg/800px-Serotonin.jpg',
        'fun_fact': {   'uz': 'Qiziqarli tomoni shundaki, inson tanasidagi serotoninning 90% qismi miyada emas, balki '
                              'ichak shilliq qavatidagi enteroxromaffin hujayralarida ishlab chiqariladi.',
                        'ru': 'Около 90% всего серотонина синтезируется в кишечнике энтерохромаффинными клетками для '
                              'регуляции перистальтики.',
                        'en': "Over 90% of the body's serotonin is produced in the gastrointestinal tract by "
                              'enterochromaffin cells, linking gut health to mental mood.'},
        'aliases': ['serotonin', 'серотонин', 'serotonin']},
    {   'id': 'nature_anatomy_028_only_avascular_tissue_air_oxygen',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tanasidagi tomirlarsiz bo'lib, kislorodni qondan emas, bevosita tashqi havodan "
                              "oluvchi yagona to'qima nima?",
                        'ru': 'Какая ткань человеческого тела не имеет кровеносных сосудов и поглощает кислород '
                              'напрямую из окружающего воздуха?',
                        'en': 'Which transparent tissue in the human body has zero blood vessels and absorbs oxygen '
                              'directly from atmospheric air?'},
        'options': {   'uz': ["Ko'z gavhari", 'Kiprik', 'Quloq suprasi', "Ko'z shox pardasi (Rogovitsa / Cornea)"],
                       'ru': ['Хрусталик', 'Ресница', 'Ушная раковина', 'Роговица глаза'],
                       'en': ['Lens', 'Eyelash', 'Ear pinna', 'Cornea of the eye']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Ko'z shox pardasi (Rogovitsa / Cornea)",
                              'ru': 'Роговица глаза',
                              'en': 'Cornea of the eye'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Human_cornea_anatomy.jpg/800px-Cornea.jpg',
        'fun_fact': {   'uz': "Ko'z shox pardasi to'liq shaffof bo'lishi uchun unda tomirlar bo'lmaydi; u ko'z yoshi "
                              'suyuqligi va havo orqali nafas oladi.',
                        'ru': 'Прозрачность роговицы возможна лишь благодаря полному отсутствию капилляров; кислород '
                              'диффундирует прямо из слезной пленки.',
                        'en': 'To maintain optical transparency, the cornea is completely avascular, obtaining oxygen '
                              'via diffusion from ambient air dissolved in tears.'},
        'aliases': ['shox parda', 'rogovitsa', 'роговица', 'cornea']},
    {   'id': 'nature_anatomy_029_retina_color_photoreceptors',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Ko'z to'r pardasida yorug'lik ranglarini (qizil, yashil, ko'k) ajratishga mas'ul "
                              "bo'lgan kolbamasimon hujayralar nima deb ataladi?",
                        'ru': 'Какие фоторецепторы сетчатки глаза отвечают за цветное дневное зрение человека?',
                        'en': 'Which photoreceptor cells in the human retina are responsible for high-acuity color '
                              'vision in daylight?'},
        'options': {   'uz': [   'Kolbachalar (Konuslar / Cones)',
                                 'Tayoqchalar (Rods)',
                                 'Gagliyalar',
                                 'Bipolyar hujayralar'],
                       'ru': ['Колбочки', 'Палочки', 'Ганглиозные клетки', 'Биполярные клетки'],
                       'en': ['Cones (Cone cells)', 'Rods', 'Ganglion cells', 'Bipolar cells']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Kolbachalar (Konuslar / Cones)', 'ru': 'Колбочки', 'en': 'Cones (Cone cells)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Rods_and_cones_sem_retina.jpg/800px-Retina_cones.jpg',
        'fun_fact': {   'uz': "To'r pardada 6 millionta kolbacha bo'lib, ular fovea deb ataluvchi sariq dog'da zich "
                              "to'plangan; tayoqchalar esa 120 millionta bo'lib tungi qora-oq ko'rishni ta'minlaydi.",
                        'ru': 'Сетчатка содержит около 6 млн колбочек трех типов (L, M, S), позволяющих различать до '
                              '10 миллионов цветовых оттенков.',
                        'en': 'The retina contains ~6 million cones (S, M, and L types for trichromatic vision) '
                              'concentrated in the fovea centralis.'},
        'aliases': ['kolbachalar', 'konuslar', 'колбочки', 'cones', 'cone cells']},
    {   'id': 'nature_anatomy_030_night_vision_photoreceptors',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Xira va tungi yorug'likda narsalarning oq-qora shaklini ilg'ab oluvchi va rodopsin "
                              'saqlovchi fotoretseptorlar nima?',
                        'ru': 'Какие клетки сетчатки содержат пигмент родопсин и обеспечивают сумеречное и ночное '
                              'зрение?',
                        'en': 'Which retinal photoreceptors contain the pigment rhodopsin and provide monochrome night '
                              'and peripheral vision?'},
        'options': {   'uz': [   'Kolbachalar',
                                 'Tayoqchalar (Rods / Palochkalar)',
                                 'Amakrin hujayralar',
                                 'Goryizontal hujayralar'],
                       'ru': ['Колбочки', 'Палочки', 'Амакриновые клетки', 'Горизонтальные клетки'],
                       'en': ['Cones', 'Rods (Rod cells)', 'Amacrine cells', 'Horizontal cells']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Tayoqchalar (Rods / Palochkalar)', 'ru': 'Палочки', 'en': 'Rods (Rod cells)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Rods_and_cones_sem_retina.jpg/800px-Retina_rods.jpg',
        'fun_fact': {   'uz': "Tayoqchalar shu qadar sezgirki, ular hatto bitta foton yorug'lik zarrasini ham ilg'ay "
                              'oladi; ularning ishlashi uchun A vitamini zarur.',
                        'ru': 'Палочки в 1000 раз чувствительнее к свету, чем колбочки, и позволяют видеть контуры '
                              'предметов при свете звезд.',
                        'en': 'Rod cells contain rhodopsin and can trigger an electrical response to a single photon, '
                              'powering scotopic night vision.'},
        'aliases': ['tayoqchalar', 'palochkalar', 'палочки', 'rods', 'rod cells']},
    {   'id': 'nature_anatomy_031_stomach_acid_ph',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Normal holatda inson oshqozon shirasi (xlorid kislotasi) qanday pH ko'rsatkichiga ega?",
                        'ru': 'Каков нормальный уровень кислотности (pH) желудочного сока взрослого человека натощак?',
                        'en': 'What is the normal resting pH level of concentrated gastric juice (hydrochloric acid) '
                              'in the human stomach?'},
        'options': {   'uz': ['pH 4.5 – 5.0', 'pH 7.0', 'pH 1.5 – 2.0', 'pH 8.5'],
                       'ru': ['pH 4,5 – 5,0', 'pH 7,0', 'pH 1,5 – 2,0', 'pH 8,5'],
                       'en': ['pH 4.5 – 5.0', 'pH 7.0', 'pH 1.5 – 2.0', 'pH 8.5']},
        'correct_index': 2,
        'correct_answer': {'uz': 'pH 1.5 – 2.0', 'ru': 'pH 1,5 – 2,0', 'en': 'pH 1.5 – 2.0'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Human_stomach_mucosa_hcl.jpg/800px-Stomach_acid.jpg',
        'fun_fact': {   'uz': 'Oshqozon kislotasi temir pichoqni ham eritib yuboradigan darajada kuchli; oshqozon '
                              "devori o'zini o'zi hazm qilmasligi uchun har bir necha kunda shilliq qavat to'liq "
                              'yangilanadi.',
                        'ru': 'Соляная кислота желудка убивает бактерии и активирует пепсин; толстый слой слизи '
                              'защищает стенки от самопереваривания.',
                        'en': 'Stomach acid operates at pH 1.5–2.0 using concentrated hydrochloric acid, buffered by '
                              'bicarbonate-rich mucus that renews every few days.'},
        'aliases': ['ph 1.5', '1.5-2.0', 'ph 1.5-2.0', '1.5']},
    {   'id': 'nature_anatomy_032_small_intestine_length',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Voyaga yetgan inson ingichka ichagining o'rtacha uzunligi qancha?",
                        'ru': 'Какова средняя длина тонкого кишечника взрослого человека?',
                        'en': 'What is the average length of the small intestine in an adult human?'},
        'options': {   'uz': ['1–2 metr', '15 metr', '25 metr', 'Taxminan 6–7 metr'],
                       'ru': ['1–2 метра', '15 метров', '25 метров', 'Около 6–7 метров'],
                       'en': ['1–2 meters', '15 meters', '25 meters', 'Around 6–7 meters (20–22 feet)']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Taxminan 6–7 metr', 'ru': 'Около 6–7 метров', 'en': 'Around 6–7 meters (20–22 feet)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Small_intestine_anatomy_human.jpg/800px-Small_intestine.jpg',
        'fun_fact': {   'uz': "Ingichka ichakdagi millionlab vorsinkalar (tukchalar) yoyib chiqilsa, uning so'rish "
                              'yuzasi tennis korti maydonidek (250 m²) kengayadi.',
                        'ru': 'Благодаря микроворсинкам реальная всасывающая площадь тонкой кишки достигает размеров '
                              'теннисного корта.',
                        'en': 'Though 6–7 meters long, microscopic villi and microvilli give the small intestine an '
                              'internal absorptive surface of ~250 square meters.'},
        'aliases': ['6-7 metr', '6 metr', '7 metr', '6-7 метров', '6-7 meters']},
    {   'id': 'nature_anatomy_033_liver_regeneration_capacity',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson jigari o'zining necha foizi saqlanib qolganda ham bir necha oy ichida to'liq "
                              "avvalgi hajmiga qayta o'sib yetisha oladi?",
                        'ru': 'Какой минимальный остаток печени (в процентах) способен полностью регенерировать до '
                              'исходного размера органа?',
                        'en': 'What minimum fraction of healthy liver tissue can regenerate back to full original mass '
                              'within months?'},
        'options': {   'uz': ["Bor-yo'g'i 25% (to'rtdan bir qismi)", '50%', '75%', '90%'],
                       'ru': ['Всего 25% (четверть органа)', '50%', '75%', '90%'],
                       'en': ['Only 25% (one quarter)', '50%', '75%', '90%']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Bor-yo'g'i 25% (to'rtdan bir qismi)",
                              'ru': 'Всего 25% (четверть органа)',
                              'en': 'Only 25% (one quarter)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Human_liver_anatomy.jpg/800px-Liver_regeneration.jpg',
        'fun_fact': {   'uz': "Jigar inson tanasidagi to'liq qayta tiklanish (regeneratsiya) qobiliyatiga ega yagona "
                              "ichki organdir; gepatotsitlar bo'linib yetishmayotgan qismini to'ldiradi.",
                        'ru': 'Гепатоциты способны возобновлять клеточное деление: даже если удалить 75% печени, '
                              'оставшаяся часть вырастет заново за пару месяцев.',
                        'en': 'The liver is unique among human visceral organs in compensatory hyperplasia; as little '
                              'as 25% remaining tissue regrows to full size.'},
        'aliases': ['25%', '25 foiz', '25 процентов', '25 percent']},
    {   'id': 'nature_anatomy_034_kidney_functional_unit',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Buyrakning qonni filtrlovchi va siydik hosil qiluvchi asosiy mikroskopik strukturaviy '
                              'birligi nima deb ataladi?',
                        'ru': 'Как называется основная структурно-функциональная фильтрующая единица почки?',
                        'en': 'What is the basic functional, microscopic blood-filtering unit of the human kidney?'},
        'options': {   'uz': ['Neyron', 'Nefron (Nephron)', 'Alveola', 'Vorsinka'],
                       'ru': ['Нейрон', 'Нефрон', 'Альвеола', 'Ворсинка'],
                       'en': ['Neuron', 'Nephron', 'Alveolus', 'Villus']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Nefron (Nephron)', 'ru': 'Нефрон', 'en': 'Nephron'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Kidney_nephron_diagram.svg/800px-Nephron.jpg',
        'fun_fact': {   'uz': "Har bir inson buyragida taxminan 1 millionta nefron bo'lib, ular kuniga 180 litr "
                              'suyuqlikni filtrlaydi va 1.5 litr siydik ajratadi.',
                        'ru': 'В двух почках человека работает около 2 миллионов нефронов, очищающих весь объем крови '
                              'организма до 60 раз за сутки.',
                        'en': 'Each human kidney houses ~1 million nephrons composed of glomeruli and renal tubules, '
                              'filtering 180 liters of primary filtrate daily.'},
        'aliases': ['nefron', 'нефрон', 'nephron']},
    {   'id': 'nature_anatomy_035_kidneys_daily_blood_filtration',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Insonning ikkita buyragi bir kunda o'rtacha necha litr qon plazmasini filtrlaydi?",
                        'ru': 'Какой колоссальный объем первичного фильтрата (жидкости) фильтруют почки человека за 24 '
                              'часа?',
                        'en': 'How many liters of fluid do the kidneys filter from blood circulation every 24 hours?'},
        'options': {   'uz': ['15 litr', '50 litr', 'Taxminan 180 litr', '500 litr'],
                       'ru': ['15 литров', '50 литров', 'Около 180 литров', '500 литров'],
                       'en': ['15 liters', '50 liters', 'Around 180 liters', '500 liters']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Taxminan 180 litr', 'ru': 'Около 180 литров', 'en': 'Around 180 liters'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kidney_cross_section_macro.jpg/800px-Kidneys.jpg',
        'fun_fact': {   'uz': 'Buyraklar 180 litr birlamchi siydik hosil qilsa-da, uning 99% qismi qonga qayta '
                              "so'riladi (reabsorbsiya) va tashqariga 1.5 litr chiqariladi.",
                        'ru': 'Из 180 литров первичного фильтрата канальцы реабсорбируют обратно 99% воды, сахаров и '
                              'солей, выводя около 1,5 литра вторичной мочи.',
                        'en': 'Kidneys generate ~180 liters of glomerular filtrate daily, reabsorbing 99% of water and '
                              'electrolytes back into peritubular capillaries.'},
        'aliases': ['180 litr', '180', '180 литров', '180 liters']},
    {   'id': 'nature_anatomy_036_insulin_producing_cells',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Qondagi shakar (glyukoza) miqdorini pasaytiruvchi insulin gormonini me'da osti bezining "
                              'qaysi hujayralari ishlab chiqaradi?',
                        'ru': 'Какие клетки островков Лангерганса поджелудочной железы вырабатывают гормон инсулин?',
                        'en': 'Which specific endocrine cells within the pancreatic islets of Langerhans synthesize '
                              'and secrete insulin?'},
        'options': {   'uz': ['Alfa-hujayralar', 'Delta-hujayralar', 'T-hujayralar', 'Beta-hujayralar (β-cells)'],
                       'ru': ['Альфа-клетки', 'Дельта-клетки', 'Т-лимфоциты', 'Бета-клетки'],
                       'en': ['Alpha cells', 'Delta cells', 'T-cells', 'Beta cells (β-cells)']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Beta-hujayralar (β-cells)', 'ru': 'Бета-клетки', 'en': 'Beta cells (β-cells)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Islets_of_Langerhans_beta_cells.jpg/800px-Beta_cells.jpg',
        'fun_fact': {   'uz': "Beta-hujayralar glyukoza ko'payganda insulin ajratib, jigarga shakarni glikogen "
                              "sifatida saqlashni buyuradi; 1-tur qandli diabetda ular nobud bo'ladi.",
                        'ru': 'При разрушении бета-клеток иммунной системой развивается сахарный диабет 1-го типа, '
                              'требующий инъекций инсулина.',
                        'en': 'Pancreatic beta cells sense elevated blood glucose via GLUT2 transporters, secreting '
                              'insulin to stimulate cellular glucose uptake.'},
        'aliases': ['beta hujayralar', 'beta-hujayralar', 'бета-клетки', 'beta cells', 'beta']},
    {   'id': 'nature_anatomy_037_glucagon_producing_cells',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Qonda shakar miqdori pasayganda jigar glikogenini shakarga parchalab qon shakarini '
                              'oshiruvchi glyukagon gormonini qaysi hujayralar ishlab chiqaradi?',
                        'ru': 'Какие клетки поджелудочной железы вырабатывают глюкагон для повышения сахара в крови '
                              'при голоде?',
                        'en': 'Which pancreatic endocrine cells secrete glucagon to mobilize glycogen stores and raise '
                              'blood glucose during fasting?'},
        'options': {   'uz': ['Alfa-hujayralar (α-cells)', 'Beta-hujayralar', 'Nefronlar', 'Gepatotsitlar'],
                       'ru': ['Альфа-клетки', 'Бета-клетки', 'Нефроны', 'Гепатоциты'],
                       'en': ['Alpha cells (α-cells)', 'Beta cells', 'Nephrons', 'Hepatocytes']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Alfa-hujayralar (α-cells)', 'ru': 'Альфа-клетки', 'en': 'Alpha cells (α-cells)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Islets_of_Langerhans_beta_cells.jpg/800px-Alpha_cells.jpg',
        'fun_fact': {   'uz': 'Alfa-hujayralar insulinning aksi sifatida ishlaydi; och qolganda jigar zaxiralaridan '
                              'glyukozani qonga chiqaradi.',
                        'ru': 'Глюкагон альфа-клеток стимулирует расщепление гликогена в печени, предотвращая опасную '
                              'для мозга гипогликемию.',
                        'en': 'Pancreatic alpha cells release glucagon in response to hypoglycemia, triggering hepatic '
                              'glycogenolysis and gluconeogenesis.'},
        'aliases': ['alfa hujayralar', 'альфа-клетки', 'alpha cells', 'alpha']},
    {   'id': 'nature_anatomy_038_saliva_digestive_enzyme',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Odam so'lagi tarkibida bo'lib, og'iz bo'shlig'idayoq murakkab uglevodlarni (kraxmalni) "
                              'parchalashni boshlovchi ferment nima?',
                        'ru': 'Какой фермент слюны начинает расщепление сложных углеводов (крахмала) прямо в ротовой '
                              'полости?',
                        'en': 'Which enzyme in human saliva initiates the chemical breakdown of dietary starch into '
                              'maltose inside the mouth?'},
        'options': {   'uz': ['Pepsin', 'Amilaza (Ptialin)', 'Tripsin', 'Lipaza'],
                       'ru': ['Пепсин', 'Амилаза (Птиалин)', 'Трипсин', 'Липаза'],
                       'en': ['Pepsin', 'Amylase (Ptyalin)', 'Trypsin', 'Lipase']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Amilaza (Ptialin)', 'ru': 'Амилаза (Птиалин)', 'en': 'Amylase (Ptyalin)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Salivary_gland_human_head.jpg/800px-Salivary_amylase.jpg',
        'fun_fact': {   'uz': "Nonni uzoq vaqt chaynasangiz shirin ta'm sezasiz; bunga amilazaning kraxmalni shakarga "
                              'aylantirishi sababdir.',
                        'ru': 'Если долго жевать кусок хлеба, он покажется сладким, так как амилаза слюны расщепляет '
                              'крахмал на простые сахара.',
                        'en': 'Salivary alpha-amylase cleaves internal alpha-1,4-glycosidic bonds in starch molecules, '
                              'generating sweet-tasting maltose and dextrins.'},
        'aliases': ['amilaza', 'ptialin', 'амилаза', 'птиалин', 'amylase', 'ptyalin']},
    {   'id': 'nature_anatomy_039_peristalsis_movement',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Qizilo'ngach va ichaklarda ovqat massasini pastga qarab suruvchi to'lqinsimon avtomatik "
                              'mushak qisqarishlari nima deb ataladi?',
                        'ru': 'Как называются волнообразные мышечные сокращения стенок пищевода и кишечника, '
                              'продвигающие пищу?',
                        'en': 'What is the term for the wave-like involuntary muscle contractions that propel food '
                              'boluses through the digestive tract?'},
        'options': {   'uz': ['Diffuziya', 'Osmos', 'Peristaltika', 'Filtratsiya'],
                       'ru': ['Диффузия', 'Осмос', 'Перистальтика', 'Фильтрация'],
                       'en': ['Diffusion', 'Osmosis', 'Peristalsis', 'Filtration']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Peristaltika', 'ru': 'Перистальтика', 'en': 'Peristalsis'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Peristalsis_diagram_esophagus.gif/800px-Peristalsis.gif',
        'fun_fact': {   'uz': 'Peristaltika tufayli odam oyoqlarini tepaga qilib teskari osilib tursa ham, ovqat va '
                              'suv baribir oshqozonga yetib boradi.',
                        'ru': 'Благодаря перистальтике астронавты в невесомости могут глотать пищу, а человек может '
                              'пить воду, стоя на голове.',
                        'en': 'Peristalsis relies on alternating longitudinal and circular smooth muscle contractions '
                              'driven by the enteric nervous system, independent of gravity.'},
        'aliases': ['peristaltika', 'перистальтика', 'peristalsis']},
    {   'id': 'nature_anatomy_040_bile_storage_organ',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Jigar tomonidan ishlab chiqarilgan o't suyuqligi (safro) qaysi a'zoda to'planadi va "
                              'quyultiriladi?',
                        'ru': 'В каком полом органе накапливается и концентрируется желчь, вырабатываемая печенью?',
                        'en': 'In which sac-like organ is hepatic bile stored and concentrated between meals before '
                              'release into the duodenum?'},
        'options': {   'uz': ['Oshqozon osti bezi', 'Taloq', 'Appendiks', "O't pufagi (Gallbladder)"],
                       'ru': ['Поджелудочная железа', 'Селезенка', 'Аппендикс', 'Желчный пузырь'],
                       'en': ['Pancreas', 'Spleen', 'Appendix', 'Gallbladder']},
        'correct_index': 3,
        'correct_answer': {'uz': "O't pufagi (Gallbladder)", 'ru': 'Желчный пузырь', 'en': 'Gallbladder'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Gallbladder_and_bile_ducts.jpg/800px-Gallbladder.jpg',
        'fun_fact': {   'uz': "O't pufagi yog'li ovqat ichakka tushganda o't suyuqligini siqib chiqarib, yog'larni "
                              'mikroskopik tomchilarga parchalaydi (emulsiya qiladi).',
                        'ru': 'Желчный пузырь концентрирует желчь в 5-10 раз, выбрасывая ее через холедох при '
                              'поступлении жиров в двенадцатиперстную кишку.',
                        'en': 'The gallbladder concentrates liver bile up to tenfold, contracting under '
                              'cholecystokinin (CCK) stimulation to emulsify dietary lipids.'},
        'aliases': ['ot pufagi', "o't pufagi", 'желчный пузырь', 'gallbladder']},
    {   'id': 'nature_anatomy_041_lungs_alveoli_surface_area',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "O'pkadagi 300–500 millionta mayda pufakchalar (alveolalar) yoyib chiqilsa, ularning "
                              "umumiy maydoni nimaga teng bo'ladi?",
                        'ru': 'Чему примерно равна суммарная дыхательная поверхность альвеол легких человека в '
                              'расправленном виде?',
                        'en': 'Approximately what surface area do the 300–500 million alveoli of the human lungs cover '
                              'when fully expanded?'},
        'options': {   'uz': [   'Katta tennis korti maydoniga (~70–100 m²)',
                                 'Oftobparast bargiga (1 m²)',
                                 'Futbol maydoniga (7000 m²)',
                                 'Stol yuzasiga (2 m²)'],
                       'ru': [   'Площади теннисного корта (~70–100 м²)',
                                 'Оконному стеклу (1 м²)',
                                 'Футбольному полю (7000 м²)',
                                 'Обеденному столу (2 м²)'],
                       'en': [   'A full tennis court (~70–100 m²)',
                                 'A window pane (1 m²)',
                                 'A football field (7,000 m²)',
                                 'A dining table (2 m²)']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Katta tennis korti maydoniga (~70–100 m²)',
                              'ru': 'Площади теннисного корта (~70–100 м²)',
                              'en': 'A full tennis court (~70–100 m²)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Alveoli_lungs_sem_macro.jpg/800px-Alveoli.jpg',
        'fun_fact': {   'uz': "Alveolalarning qalinligi atigi bitta hujayradan iborat bo'lib, kislorod kapillyarlarga "
                              "o'ta tez diffuziya bo'lishini ta'minlaydi.",
                        'ru': 'Стенка альвеолы тоньше мыльного пузыря, что позволяет газам диффундировать в кровь за '
                              'долю секунды.',
                        'en': 'Human alveolar surface area spans 70–100 m² across a blood-air barrier just 0.2 to 0.5 '
                              'micrometers thick.'},
        'aliases': ['tennis korti', '70 m2', '100 m2', 'теннисный корт', 'tennis court']},
    {   'id': 'nature_anatomy_042_primary_breathing_muscle',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Tinch holatda nafas olish jarayonining 75% ini ta'minlovchi asosiy gumbazsimon mushak "
                              'nima?',
                        'ru': 'Какая куполообразная мышца является главной дыхательной мышцей человека, разделяя '
                              'грудную и брюшную полости?',
                        'en': 'Which dome-shaped skeletal muscle is the primary driver of quiet inspiration, '
                              'separating thoracic and abdominal cavities?'},
        'options': {   'uz': ["Qovurg'alararo mushaklar", 'Diafragma', "Qorin to'g'ri mushagi", 'Trapetsiya mushagi'],
                       'ru': ['Межреберные мышцы', 'Диафрагма', 'Прямая мышца живота', 'Трапециевидная мышца'],
                       'en': ['Intercostal muscles', 'Diaphragm', 'Rectus abdominis', 'Trapezius']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Diafragma', 'ru': 'Диафрагма', 'en': 'Diaphragm'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Diaphragm_muscle_human.jpg/800px-Diaphragm.jpg',
        'fun_fact': {   'uz': "Diafragma qisqarganda pastga tushadi, ko'krak qafasidagi bosim pasayadi va tashqi havo "
                              "vakuum orqali o'pkaga o'z-o'zidan so'riladi.",
                        'ru': 'При сокращении диафрагма уплощается, создавая отрицательное давление в плевральной '
                              'полости для вдоха.',
                        'en': 'Contraction of the diaphragm flattens its central tendon downward, expanding thoracic '
                              'volume and driving passive atmospheric inflow.'},
        'aliases': ['diafragma', 'диафрагма', 'diaphragm']},
    {   'id': 'nature_anatomy_043_choking_prevention_flap',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Yutinganda hiqildoqqa ovqat tushishining oldini olib nafas yo'lini yopuvchi elastik "
                              "tog'ay nima?",
                        'ru': 'Какой эластичный хрящевой клапан закрывает вход в гортань во время глотания, защищая '
                              'трахею от пищи?',
                        'en': 'Which flexible cartilaginous flap folds backward over the laryngeal inlet during '
                              'swallowing to prevent choking?'},
        'options': {   'uz': [   "Qalqonsimon tog'ay",
                                 'Uvula (Kichik tilcha)',
                                 "Hiqildoq usti tog'ayi (Epiglottis)",
                                 "Uzuksimon tog'ay"],
                       'ru': ['Щитовидный хрящ', 'Язычок', 'Надгортанник', 'Перстневидный хрящ'],
                       'en': ['Thyroid cartilage', 'Palatine uvula', 'Epiglottis', 'Cricoid cartilage']},
        'correct_index': 2,
        'correct_answer': {'uz': "Hiqildoq usti tog'ayi (Epiglottis)", 'ru': 'Надгортанник', 'en': 'Epiglottis'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Epiglottis_larynx_anatomy.jpg/800px-Epiglottis.jpg',
        'fun_fact': {   'uz': "Har safar ovqat yoki suv yutganingizda epiglottis nafas yo'lini toshdek yopadi; agar u "
                              "kechiksa, odam 'chaynab tiqilib qoladi'.",
                        'ru': 'Надгортанник опускается как люк, направляя пищевой комок в пищевод и предотвращая '
                              'асфиксию.',
                        'en': 'The leaf-shaped epiglottis folds over the glottis during deglutition, directing food '
                              'into the esophagus and safeguarding the trachea.'},
        'aliases': ['epiglottis', 'hiqildoq usti', 'надгортанник', 'epiglottis']},
    {   'id': 'nature_anatomy_044_voice_box_organ',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Ovoz paychalari joylashgan va inson nutqini shakllantiruvchi 'ovoz qutisi' a'zosi nima?",
                        'ru': 'Какой орган дыхательной системы содержит голосовые связки и образует кадык (адамово '
                              'яблоко)?',
                        'en': "Which cartilaginous organ houses the vocal folds and forms the external Adam's apple in "
                              'the neck?'},
        'options': {   'uz': ['Halqum (Farinks)', 'Traxeya', 'Bronx', 'Hiqildoq (Larynx)'],
                       'ru': ['Глотка (Фаринкс)', 'Трахея', 'Бронх', 'Гортань (Ларинкс)'],
                       'en': ['Pharynx', 'Trachea', 'Bronchus', 'Larynx (Voice box)']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Hiqildoq (Larynx)', 'ru': 'Гортань (Ларинкс)', 'en': 'Larynx (Voice box)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Larynx_vocal_cords_macro.jpg/800px-Larynx.jpg',
        'fun_fact': {   'uz': "Hiqildoqdagi ovoz paychalari orqali havo o'tganda ular sekundiga 100 dan 1000 "
                              'martagacha tebranib, tovush hosil qiladi.',
                        'ru': 'Натяжение голосовых связок гортани мышцами меняет высоту звука, превращая выдыхаемый '
                              'воздух в голос.',
                        'en': 'Intrinsic laryngeal muscles modulate the tension and glottal aperture of the vocal '
                              'folds to produce phonation.'},
        'aliases': ['hiqildoq', 'гортань', 'ларинкс', 'larynx', 'voice box']},
    {   'id': 'nature_anatomy_045_master_endocrine_gland',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Boshqa barcha ichki sekretsiya bezlari (qalqonsimon bez, buyrak usti bezi) faoliyatini '
                              "boshqaruvchi 'bosh bez' qaysi?",
                        'ru': 'Какая железа у основания мозга считается «дирижером» всей эндокринной системы человека?',
                        'en': "Which pea-sized gland at the base of the brain is hailed as the 'master endocrine "
                              "gland' of the human body?"},
        'options': {   'uz': [   'Gipofiz (Pituitary gland)',
                                 'Qalqonsimon bez',
                                 'Epifiz (Shishasimon bez)',
                                 'Buyrak usti bezi'],
                       'ru': ['Гипофиз', 'Щитовидная железа', 'Эпифиз (Шишковидная)', 'Надпочечники'],
                       'en': ['Pituitary gland (Hypophysis)', 'Thyroid gland', 'Pineal gland', 'Adrenal glands']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Gipofiz (Pituitary gland)', 'ru': 'Гипофиз', 'en': 'Pituitary gland (Hypophysis)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Pituitary_gland_brain_location.jpg/800px-Pituitary.jpg',
        'fun_fact': {   'uz': "Gipofiz no'xatdek kichik bo'lsa-da, bo'y o'sish gormoni (somatotropin) va boshqa "
                              "a'zolarni faollashtiruvchi 9 xil gormon ishlab chiqaradi.",
                        'ru': 'Гипофиз лежит в турецком седле черепа и управляет ростом, обменом веществ и '
                              'репродуктивной системой через тропные гормоны.',
                        'en': 'Nestled in the sella turcica, the pituitary gland secretes tropic hormones regulating '
                              'growth, thyroid output, and adrenal cortisol.'},
        'aliases': ['gipofiz', 'гипофиз', 'pituitary gland', 'pituitary']},
    {   'id': 'nature_anatomy_046_circadian_rhythm_hormone',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Epifiz (shishasimon bez) tomonidan zulmatda ishlab chiqariladigan va uyqu-uyg'onish "
                              'ritmini boshqaruvchi asosiy gormon nima?',
                        'ru': 'Какой гормон вырабатывается шишковидной железой в темноте и регулирует циклы сна и '
                              'бодрствования?',
                        'en': 'Which hormone is synthesized by the pineal gland in response to darkness to regulate '
                              'sleep-wake circadian rhythm?'},
        'options': {   'uz': ['Kortizol', 'Melatonin', 'Insulin', 'Oksitotsin'],
                       'ru': ['Кортизол', 'Мелатонин', 'Инсулин', 'Окситоцин'],
                       'en': ['Cortisol', 'Melatonin', 'Insulin', 'Oxytocin']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Melatonin', 'ru': 'Мелатонин', 'en': 'Melatonin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Pineal_gland_melatonin_cycle.jpg/800px-Melatonin.jpg',
        'fun_fact': {   'uz': "Smartfon va televizor ekranlarining ko'k nuri ko'z orqali epifizga tushganda melatonin "
                              "sintezini to'xtatadi va uyqusizlik keltirib chiqaradi.",
                        'ru': 'Синий свет гаджетов подавляет синтез мелатонина через супрахиазматическое ядро, '
                              'обманывая мозг ощущением полудня.',
                        'en': 'Retinal melanopsin ganglion cells sensing blue light inhibit pineal melatonin synthesis '
                              'via suprachiasmatic nucleus signaling.'},
        'aliases': ['melatonin', 'мелатонин', 'melatonin']},
    {   'id': 'nature_anatomy_047_fight_or_flight_hormone',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Xavf paytida 'qoch yoki jang qil' reaksiyasini yoqib, yurak urishini tezlashtiruvchi va "
                              'qorachiqlarni kengaytiruvchi gormon nima?',
                        'ru': 'Какой гормон надпочечников мгновенно запускает реакцию «бей или беги» при внезапном '
                              'испуге или угрозе?',
                        'en': "Which adrenal medulla hormone triggers the classic 'fight-or-flight' acute sympathetic "
                              'stress response?'},
        'options': {   'uz': ['Tiroksin', 'Melatonin', 'Adrenalin (Epinefrin)', 'Paratgormon'],
                       'ru': ['Тироксин', 'Мелатонин', 'Адреналин (Эпинефрин)', 'Паратгормон'],
                       'en': ['Thyroxine', 'Melatonin', 'Adrenaline (Epinephrine)', 'Parathyroid hormone']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Adrenalin (Epinefrin)',
                              'ru': 'Адреналин (Эпинефрин)',
                              'en': 'Adrenaline (Epinephrine)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Adrenal_glands_adrenaline_macro.jpg/800px-Adrenaline.jpg',
        'fun_fact': {   'uz': "Adrenalin qonni darhol mushaklarga yo'naltiradi, glyukozani qonga chiqaradi va "
                              'organizmni jismoniy kurashga shay qiladi.',
                        'ru': 'Адреналин расширяет бронхи, ускоряет пульс и сужает сосуды кожи, мобилизуя все запасы '
                              'энергии организма за доли секунды.',
                        'en': 'Secreted by the adrenal medulla, epinephrine binds adrenergic receptors to dilate '
                              'bronchioles and shunts blood to skeletal muscles.'},
        'aliases': ['adrenalin', 'epinefrin', 'адреналин', 'эпинефрин', 'adrenaline', 'epinephrine']},
    {   'id': 'nature_anatomy_048_t_cell_training_organ',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson immunitetining asosiy kurashchilari bo'lgan T-limfotsitlar qaysi ko'krak bezi "
                              "a'zosida 'o'qitiladi' va voyaga yetadi?",
                        'ru': 'В каком органе грудной клетки происходит созревание и «обучение» Т-лимфоцитов иммунной '
                              'системы?',
                        'en': 'Which lymphoid organ located behind the sternum trains and matures adaptive '
                              'T-lymphocytes during childhood?'},
        'options': {   'uz': ['Taloq', 'Jigar', 'Appendiks', 'Timus (Ayrisimon bez)'],
                       'ru': ['Селезенка', 'Печень', 'Аппендикс', 'Тимус (Вилочковая железа)'],
                       'en': ['Spleen', 'Liver', 'Appendix', 'Thymus gland']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Timus (Ayrisimon bez)', 'ru': 'Тимус (Вилочковая железа)', 'en': 'Thymus gland'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Thymus_gland_human.jpg/800px-Thymus.jpg',
        'fun_fact': {   'uz': "Timus o'z organizmining hujayralariga hujum qiladigan xavfli T-hujayralarni 98% gacha "
                              "saralab yo'q qiladi (musbat va manfiy seleksiya).",
                        'ru': 'В тимусе 98% развивающихся Т-клеток бракуются и уничтожаются методом апоптоза, '
                              'предотвращая аутоиммунные атаки.',
                        'en': 'The thymus mediates positive and negative selection, eliminating autoreactive T-cell '
                              'clones before release into the bloodstream.'},
        'aliases': ['timus', 'ayrisimon bez', 'тимус', 'вилочковая железа', 'thymus', 'thymus gland']},
    {   'id': 'nature_anatomy_049_blood_filtering_lymphoid_organ',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Qondagi eskirgan qizil qon tanachalarini (eritrotsitlar) tutib filtrlovchi va qon '
                              "zaxirasini saqlovchi a'zo qaysi?",
                        'ru': 'Какой орган брюшной полости называют «кладбищем эритроцитов» за фильтрацию и утилизацию '
                              'старых клеток крови?',
                        'en': "Which abdominal organ acts as the primary blood filter and erythrocyte 'graveyard', "
                              'recycling iron and storing platelets?'},
        'options': {   'uz': ['Taloq (Spleen)', "O't pufagi", 'Buyrak', "Me'da osti bezi"],
                       'ru': ['Селезёнка', 'Желчный пузырь', 'Почка', 'Поджелудочная железа'],
                       'en': ['Spleen', 'Gallbladder', 'Kidney', 'Pancreas']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Taloq (Spleen)', 'ru': 'Селезёнка', 'en': 'Spleen'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Spleen_human_anatomy.jpg/800px-Spleen.jpg',
        'fun_fact': {   'uz': 'Taloqdagi makrofaglar har kuni 200 milliarddan ortiq eskirgan eritrotsitlarni '
                              'parchalaydi va undagi temirni yangi qon uchun qonga qaytaradi.',
                        'ru': 'Красная пульпа селезенки проверяет гибкость эритроцитов, пропуская их через узкие '
                              'синусоиды, а белая пульпа синтезирует антитела.',
                        'en': 'The splenic red pulp tests erythrocyte deformability through the cords of Billroth, '
                              'recycling heme iron from senescent cells.'},
        'aliases': ['taloq', 'селезенка', 'селезёнка', 'spleen']},
    {   'id': 'nature_anatomy_050_metabolism_regulator_gland',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Bo'yinda kapalak shaklida joylashgan va butun tana metabolizmi (moddalar almashinuvi) "
                              'tezligini boshqaruvchi bez qaysi?',
                        'ru': 'Какая железа в форме бабочки на передней поверхности шеи регулирует скорость основного '
                              'обмена веществ?',
                        'en': 'Which butterfly-shaped gland straddling the trachea regulates basal metabolic rate via '
                              'iodine-containing hormones?'},
        'options': {   'uz': ['Paratiroid bez', 'Qalqonsimon bez (Thyroid)', 'Gipofiz', 'Timus'],
                       'ru': ['Паращитовидная железа', 'Щитовидная железа', 'Гипофиз', 'Тимус'],
                       'en': ['Parathyroid gland', 'Thyroid gland', 'Pituitary gland', 'Thymus']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Qalqonsimon bez (Thyroid)', 'ru': 'Щитовидная железа', 'en': 'Thyroid gland'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Thyroid_gland_neck.jpg/800px-Thyroid.jpg',
        'fun_fact': {   'uz': 'Qalqonsimon bez tiroksin (T4) va triyodtironin (T3) gormonlarini ishlab chiqarish uchun '
                              'oziq-ovqatdagi yod elementiga muhtojdir.',
                        'ru': 'Гормоны щитовидной железы Т3 и Т4 контролируют температуру тела, частоту сердцебиения и '
                              'скорость сжигания калорий.',
                        'en': 'The thyroid gland concentrates dietary iodide to synthesize T3 and T4, governing '
                              'mitochondrial respiration throughout all tissues.'},
        'aliases': ['qalqonsimon bez', 'щитовидная железа', 'щитовидка', 'thyroid', 'thyroid gland']},
    {   'id': 'nature_anatomy_051_chromosomes_human_somatic',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Sog'lom insonning oddiy tana (somatik) hujayrasida nechta xromosoma mavjud?",
                        'ru': 'Сколько хромосом насчитывает нормальный диплоидный кариотип соматической клетки '
                              'человека?',
                        'en': 'How many total chromosomes are contained in the nucleus of a normal human diploid '
                              'somatic cell?'},
        'options': {   'uz': ['23 ta', '48 ta', '46 ta (23 juft)', '92 ta'],
                       'ru': ['23 хромосомы', '48 хромосом', '46 хромосом (23 пары)', '92 хромосомы'],
                       'en': ['23 chromosomes', '48 chromosomes', '46 chromosomes (23 pairs)', '92 chromosomes']},
        'correct_index': 2,
        'correct_answer': {'uz': '46 ta (23 juft)', 'ru': '46 хромосом (23 пары)', 'en': '46 chromosomes (23 pairs)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Human_karyotype_46_chromosomes.jpg/800px-Human_karyotype.jpg',
        'fun_fact': {   'uz': "46 ta xromosomaning 23 tasi onadan, 23 tasi otadan o'tadi; 23-juft esa jinsni "
                              'belgilaydi (XX — ayol, XY — erkak).',
                        'ru': 'Кариотип человека состоит из 22 пар аутосом и одной пары половых хромосом (XX или XY).',
                        'en': 'Human diploid cells contain 22 pairs of autosomes and one pair of sex chromosomes, '
                              'totaling 46 chromosomes.'},
        'aliases': ['46', '46 ta', '23 juft', '46 хромосом', '46 chromosomes']},
    {   'id': 'nature_anatomy_052_cellular_powerhouse_organelle',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Hujayra ichida oziq moddalardan universal energiya molekulasi — ATF ishlab chiqaruvchi '
                              "'energiya stansiyasi' organellasi nima?",
                        'ru': 'Какую клеточную органеллу называют «энергетической станцией клетки» за синтез молекул '
                              'АТФ?',
                        'en': "Which double-membraned organelle is dubbed the 'powerhouse of the cell' for "
                              'synthesizing ATP via oxidative phosphorylation?'},
        'options': {   'uz': ['Ribosoma', 'Lizosoma', 'Golji apparati', 'Mitoxondriya'],
                       'ru': ['Рибосома', 'Лизосома', 'Комплекс Гольджи', 'Митохондрия'],
                       'en': ['Ribosome', 'Lysosome', 'Golgi apparatus', 'Mitochondria']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Mitoxondriya', 'ru': 'Митохондрия', 'en': 'Mitochondria'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Mitochondria_cell_powerhouse_macro.jpg/800px-Mitochondria.jpg',
        'fun_fact': {   'uz': "Mitoxondriyalar qadimda alohida bakteriya bo'lgan; shu sababli ularning o'z shaxsiy "
                              "DNKsi bo'lib, u faqat onadan farzandga o'tadi.",
                        'ru': 'Митохондрии имеют собственную кольцевую ДНК и передаются исключительно по материнской '
                              'линии.',
                        'en': 'Mitochondria evolved via endosymbiosis and contain their own circular mitochondrial DNA '
                              '(mtDNA), inherited maternally.'},
        'aliases': ['mitoxondriya', 'митохондрия', 'mitochondria']},
    {   'id': 'nature_anatomy_053_protein_synthesis_organelle',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Genetik RNK ko'rsatmasi bo'yicha aminokislotalardan oqsil molekulalarini yig'uvchi "
                              'mikroskopik tuzilma nima?',
                        'ru': 'Какая внутриклеточная структура осуществляет трансляцию и синтез белков из аминокислот '
                              'по матрице иРНК?',
                        'en': 'Which ribonucleoprotein cellular complex reads messenger RNA codons to synthesize '
                              'proteins from amino acids?'},
        'options': {   'uz': ['Ribosoma', 'Sentriola', 'Lizosoma', 'Vakuola'],
                       'ru': ['Рибосома', 'Центриоль', 'Лизосома', 'Вакуоль'],
                       'en': ['Ribosome', 'Centriole', 'Lysosome', 'Vacuole']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Ribosoma', 'ru': 'Рибосома', 'en': 'Ribosome'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ribosome_translation_protein_synthesis.jpg/800px-Ribosome.jpg',
        'fun_fact': {   'uz': "Bitta tirik hujayrada 10 milliontagacha ribosoma bo'lishi mumkin; ular har soniyada "
                              'minglab yangi oqsillarni ishlab chiqaradi.',
                        'ru': 'Рибосома соединяет аминокислоты со скоростью до 20 штук в секунду, формируя третичную '
                              'структуру функциональных белков.',
                        'en': 'Ribosomes translate mRNA transcripts at rates of up to 20 amino acids per second, '
                              'forming peptide bonds via peptidyl transferase.'},
        'aliases': ['ribosoma', 'рибосома', 'ribosome']},
    {   'id': 'nature_anatomy_054_cellular_waste_digestive_organelle',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Hujayra ichidagi eskirgan qismlar, bakteriyalar va chiqindilarni hazm qiluvchi '
                              "kislotali fermentlarga boy 'chiqindi utilizatori' nima?",
                        'ru': 'Какая органелла содержит пищеварительные ферменты и отвечает за аутофагию и расщепление '
                              'клеточных отходов?',
                        'en': 'Which acidic cytoplasmic organelle contains hydrolytic enzymes that digest cellular '
                              'debris and foreign pathogens?'},
        'options': {   'uz': ['Peroksisoma', 'Lizosoma', 'Plastida', 'Ribosoma'],
                       'ru': ['Пероксисома', 'Лизосома', 'Пластида', 'Рибосома'],
                       'en': ['Peroxisome', 'Lysosome', 'Plastid', 'Ribosome']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Lizosoma', 'ru': 'Лизосома', 'en': 'Lysosome'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Lysosome_autophagy_cell.jpg/800px-Lysosome.jpg',
        'fun_fact': {   'uz': 'Lizosomalar autofagiya jarayonida eskirgan hujayra qismlarini qayta ishlab yangi '
                              'energiya beradi; bu kashfiyot uchun 2016-yilda Nobel mukofoti berilgan.',
                        'ru': 'Лизосомы расщепляют бактерии, вирусы и дефектные белки кислыми гидролазами при pH около '
                              '4,5-5,0.',
                        'en': 'Lysosomes maintain an acidic lumen (pH ~4.5) driven by proton pumps to degrade '
                              'macromolecules via autophagy and phagocytosis.'},
        'aliases': ['lizosoma', 'лизосома', 'lysosome']},
    {   'id': 'nature_anatomy_055_total_dna_length_per_cell',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Bitta inson hujayrasi yadrosidagi barcha 46 ta xromosoma DNK iplarini yozib ulasa, '
                              "uning umumiy uzunligi qancha bo'ladi?",
                        'ru': 'Какова суммарная длина нитей ДНК, упакованных в ядре всего одной диплоидной клетки '
                              'человека?',
                        'en': 'What is the total combined physical length of all DNA strands uncoiled from a single '
                              'human diploid cell nucleus?'},
        'options': {   'uz': ['2 millimetr', '20 santimetr', 'Taxminan 2 metr', '200 metr'],
                       'ru': ['2 миллиметра', '20 сантиметров', 'Около 2 метров', '200 метров'],
                       'en': ['2 millimeters', '20 centimeters', 'Around 2 meters (6.5 feet)', '200 meters']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Taxminan 2 metr', 'ru': 'Около 2 метров', 'en': 'Around 2 meters (6.5 feet)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/DNA_double_helix_nucleosome_packaging.jpg/800px-DNA_packaging.jpg',
        'fun_fact': {   'uz': "2 metrlik DNK mikroskopik yadroga sig'ishi uchun u giston oqsillari atrofiga g'altak "
                              "kabi 10 000 baravar zichlikda o'raladi.",
                        'ru': 'Если сложить ДНК всех клеток одного человека, эта нить дотянется от Земли до Плутона и '
                              'обратно несколько раз.',
                        'en': 'Two meters of genomic DNA are packed into a 6-micrometer nucleus by wrapping around '
                              'histone octamers into chromatin fibers.'},
        'aliases': ['2 metr', '2 метра', '2 meters', '2m']},
    {   'id': 'nature_anatomy_056_hearing_organ_corti',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Ichki quloqda tovush tebranishlarini asab impulslariga aylantiruvchi qabul qiluvchi '
                              "eshitish a'zosi nima deb ataladi?",
                        'ru': 'Какой спиральный орган внутреннего уха содержит слуховые рецепторы и превращает '
                              'механические колебания в нервные импульсы?',
                        'en': 'Which fluid-filled spiral structure in the inner ear houses the Organ of Corti to '
                              'transduce sound waves into neural signals?'},
        'options': {   'uz': [   'Yarim doira kanallari',
                                 "Nog'ora pardasi",
                                 'Evstaxiy nayi',
                                 "Chig'anoq (Ulitka / Cochlea)"],
                       'ru': [   'Полукружные каналы',
                                 'Барабанная перепонка',
                                 'Евстахиева труба',
                                 'Улитка (Кортиев орган)'],
                       'en': [   'Semicircular canals',
                                 'Tympanic membrane',
                                 'Eustachian tube',
                                 'Cochlea (Organ of Corti)']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Chig'anoq (Ulitka / Cochlea)",
                              'ru': 'Улитка (Кортиев орган)',
                              'en': 'Cochlea (Organ of Corti)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cochlea_cross_section_inner_ear.jpg/800px-Cochlea.jpg',
        'fun_fact': {   'uz': "Chig'anoq ichidagi 16 000 dan 20 000 tagacha mayda eshituv tuk hujayralari turli "
                              "chastotalarni ajratadi; ular bir marta nobud bo'lsa qayta o'smaydi.",
                        'ru': 'Волосковые клетки кортиева органа колеблются в эндолимфе, передавая сигналы по '
                              'слуховому нерву в височную кору мозга.',
                        'en': 'The cochlea uses stereocilia deflection along the basilar membrane tonotopic map to '
                              'convert 20–20,000 Hz sound waves into nerve action potentials.'},
        'aliases': ['chiganoq', 'ulitka', 'улитка', 'кортиев орган', 'cochlea']},
    {   'id': 'nature_anatomy_057_dynamic_balance_canals',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Boshning harakatini va tananing fazodagi 3D muvozanatini sezuvchi ichki quloqdagi a'zo "
                              'nima?',
                        'ru': 'Какие три взаимоперпендикулярных канала внутреннего уха отвечают за восприятие углового '
                              'ускорения и вращения головы?',
                        'en': 'Which three fluid-filled, mutually perpendicular inner ear canals detect angular '
                              'rotation and rotational equilibrium?'},
        'options': {   'uz': ['Yarim doirasimon kanallar', "Chig'anoq", "Nog'ora bo'shlig'i", 'Eshitish suyagi'],
                       'ru': ['Полукружные каналы', 'Улитка', 'Барабанная полость', 'Слуховая труба'],
                       'en': ['Semicircular canals', 'Cochlea', 'Tympanic cavity', 'Eustachian tube']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Yarim doirasimon kanallar', 'ru': 'Полукружные каналы', 'en': 'Semicircular canals'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Semicircular_canals_vestibular_system.jpg/800px-Semicircular_canals.jpg',
        'fun_fact': {   'uz': "Uchta yarim doira kanallari fazodagi X, Y va Z o'qlari bo'yicha suyuqlik (endolimfa) "
                              "harakatini ilg'ab, ko'z va tanani muvozanatda saqlaydi.",
                        'ru': 'Купула внутри полукружных каналов отклоняется при движении эндолимфы, мгновенно '
                              'информируя мозжечок о поворотах головы.',
                        'en': 'The three semicircular canals house cristae ampullares embedded in gelatinous cupulae, '
                              'transducing pitch, roll, and yaw rotations.'},
        'aliases': ['yarim doira kanallari', 'полукружные каналы', 'semicircular canals']},
    {   'id': 'nature_anatomy_058_skin_dead_cell_shedding_rate',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tanasi har bir daqiqada o'rtacha nechta o'lik teri hujayrasini to'kib tashlaydi?",
                        'ru': 'Сколько примерно мертвых ороговевших клеток эпидермиса человек сбрасывает каждую '
                              'минуту?',
                        'en': 'Approximately how many dead epidermal skin cells does a healthy human body shed every '
                              'single minute?'},
        'options': {   'uz': ['100 hujayra', '30 000 – 40 000 hujayra', '500 000 hujayra', '5 million hujayra'],
                       'ru': ['100 клеток', '30 000 – 40 000 клеток', '500 000 клеток', '5 миллионов клеток'],
                       'en': ['100 cells', '30,000 to 40,000 cells', '500,000 cells', '5 million cells']},
        'correct_index': 1,
        'correct_answer': {   'uz': '30 000 – 40 000 hujayra',
                              'ru': '30 000 – 40 000 клеток',
                              'en': '30,000 to 40,000 cells'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Desquamation_skin_stratum_corneum_sem.jpg/800px-Skin_shedding.jpg',
        'fun_fact': {   'uz': "Odam 1 yilda taxminan 4 kg o'lik teri to'kadi; uylardagi changning katta qismi aynan "
                              "to'kilgan teri parchalaridan iborat bo'ladi.",
                        'ru': 'За год человек теряет около 4 кг отмершей кожи; она составляет до 70% состава обычной '
                              'домашней пыли.',
                        'en': 'Desquamation sloughs off ~30,000–40,000 keratinocytes per minute, amounting to nearly 4 '
                              'kilograms of dead skin dust shed annually.'},
        'aliases': ['30000', '40000', '30 000', '30,000']},
    {   'id': 'nature_anatomy_059_primary_skin_pigment',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson terisi, sochi va ko'z qorachig'iga rang beruvchi va ultrabinafsha nurlanishidan "
                              'himoyalovchi pigment nima?',
                        'ru': 'Какой пигмент определяет цвет кожи, волос и глаз человека, защищая ДНК ядер от '
                              'ультрафиолетового излучения?',
                        'en': 'Which bio-pigment synthesised by melanocytes dictates human skin, hair, and eye '
                              'coloration while shielding DNA from UV radiation?'},
        'options': {   'uz': ['Keratin', 'Karotin', 'Melanin', 'Gemoglobin'],
                       'ru': ['Кератин', 'Каротин', 'Меланин', 'Гемоглобин'],
                       'en': ['Keratin', 'Carotene', 'Melanin', 'Hemoglobin']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Melanin', 'ru': 'Меланин', 'en': 'Melanin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Melanocyte_melanin_synthesis.jpg/800px-Melanin.jpg',
        'fun_fact': {   'uz': 'Quyoshga toblanganda melanositlar teri hujayralari yadrosi ustiga soyabon kabi '
                              "joylashuvchi melanin pigmentini ko'proq ishlab chiqaradi.",
                        'ru': 'Меланосомы формируют защитные «шапочки» над ядрами кератиноцитов, поглощая более 99% '
                              'вредного УФ-излучения.',
                        'en': 'Melanosomes transfer melanin granules to keratinocytes, clustering above nuclei like '
                              'miniature parasols to absorb mutative UV photons.'},
        'aliases': ['melanin', 'меланин', 'melanin']},
    {   'id': 'nature_anatomy_060_structural_protein_nails_hair',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Soch, tirnoq va terining tashqi shox qavatini tashkil etuvchi pishiq suv o'tkazmas tola "
                              'oqsil nima?',
                        'ru': 'Какой прочный волокнистый белок является основой волос, ногтей и верхнего рогового слоя '
                              'кожи?',
                        'en': 'Which tough fibrous structural protein forms the bulk of human hair, fingernails, and '
                              'the outermost stratum corneum?'},
        'options': {   'uz': ['Kollagen', 'Elastin', 'Fibrin', 'Keratin'],
                       'ru': ['Коллаген', 'Эластин', 'Фибрин', 'Кератин'],
                       'en': ['Collagen', 'Elastin', 'Fibrin', 'Keratin']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Keratin', 'ru': 'Кератин', 'en': 'Keratin'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Alpha_keratin_hair_structure.jpg/800px-Keratin.jpg',
        'fun_fact': {   'uz': "Keratindagi oltingugurt atomlari o'rtasidagi disulfid ko'priklari tirnoq va sochlarga "
                              "mustahkamlik beradi; soch kuyganda badbo'y hid aynan oltingugurtdandir.",
                        'ru': 'Дисульфидные связи цистеина в кератине делают волосы и ногти упругими и устойчивыми к '
                              'механическому истиранию.',
                        'en': 'Cysteine disulfide bonds between alpha-keratin helices provide mechanical rigidity and '
                              'water-insolubility to hair and nails.'},
        'aliases': ['keratin', 'кератин', 'keratin']},
    {   'id': 'nature_anatomy_061_collarbone_scientific_name',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Yelkani to'sh suyagi bilan bog'lab turuvchi va eng ko'p sinadigan suyak — o'mrov suyagi "
                              'tibbiyotda nima deb ataladi?',
                        'ru': 'Как называется ключица в анатомической терминологии — самая часто ломающаяся кость '
                              'человека?',
                        'en': 'What is the medical anatomical name for the collarbone—the most frequently fractured '
                              'bone in the human body?'},
        'options': {   'uz': [   "Klavikula (Clavicle / O'mrov suyagi)",
                                 'Skapula (Kurak)',
                                 "Sternum (To'sh)",
                                 'Humerus (Yelka)'],
                       'ru': ['Ключица (Clavicula)', 'Лопатка', 'Грудина', 'Плечевая кость'],
                       'en': ['Clavicle (Collarbone)', 'Scapula', 'Sternum', 'Humerus']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Klavikula (Clavicle / O'mrov suyagi)",
                              'ru': 'Ключица (Clavicula)',
                              'en': 'Clavicle (Collarbone)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Human_clavicle_bone.jpg/800px-Clavicle.jpg',
        'fun_fact': {   'uz': "O'mrov suyagi inson embrionida eng birinchi bo'lib suyaklanishni (rivojlanishni) "
                              'boshlaydigan suyak hisoblanadi.',
                        'ru': 'Ключица — единственная длинная трубчатая кость, расположенная горизонтально, и первая '
                              'кость, начинающая окостенение у плода.',
                        'en': 'The clavicle is the first bone to begin ossification in the human embryo (week 5) and '
                              'the last to complete fusion (~age 25).'},
        'aliases': ['omrov suyagi', 'klavikula', 'ключица', 'clavicle', 'collarbone']},
    {   'id': 'nature_anatomy_062_kneecap_scientific_name',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Tizza bo'g'imini himoyalovchi va tizzaning old qismida joylashgan kosacha (chanoqcha) "
                              'suyagi nima deb ataladi?',
                        'ru': 'Как называется надколенник (коленная чашечка) — крупнейшая сесамовидная кость человека?',
                        'en': 'What is the anatomical name for the kneecap—the largest sesamoid bone in the human '
                              'body?'},
        'options': {   'uz': ['Menisk', 'Patella (Tizza kosachasi)', 'Fibula', 'Tibia'],
                       'ru': ['Мениск', 'Надколенник (Patella)', 'Малоберцовая кость', 'Большеберцовая кость'],
                       'en': ['Meniscus', 'Patella (Kneecap)', 'Fibula', 'Tibia']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Patella (Tizza kosachasi)', 'ru': 'Надколенник (Patella)', 'en': 'Patella (Kneecap)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Patella_human_anatomy.jpg/800px-Patella.jpg',
        'fun_fact': {   'uz': "Patella to'rtboshli son mushagi payi ichida joylashgan bo'lib, bo'g'im richag kuchini "
                              "30% dan ko'proqqa oshiradi.",
                        'ru': 'Надколенник увеличивает плечо силы четырехглавой мышцы бедра, облегчая разгибание ноги '
                              'в коленном суставе.',
                        'en': 'The patella articulates with the femoral trochlear groove, acting as a fulcrum to '
                              'increase quadriceps mechanical leverage by 30%.'},
        'aliases': ['patella', 'tizza kosachasi', 'надколенник', 'patella', 'kneecap']},
    {   'id': 'nature_anatomy_063_ribs_count_human',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Sog'lom inson ko'krak qafasida nechta qovurg'a (necha juft) mavjud?",
                        'ru': 'Сколько всего ребер (сколько пар) насчитывает нормальная грудная клетка человека?',
                        'en': 'How many total ribs (pairs) form the standard human rib cage?'},
        'options': {   'uz': ['20 ta (10 juft)', '28 ta (14 juft)', '24 ta (12 juft)', '32 ta'],
                       'ru': ['20 ребер (10 пар)', '28 ребер (14 пар)', '24 ребра (12 пар)', '32 ребра'],
                       'en': ['20 ribs (10 pairs)', '28 ribs (14 pairs)', '24 ribs (12 pairs)', '32 ribs']},
        'correct_index': 2,
        'correct_answer': {'uz': '24 ta (12 juft)', 'ru': '24 ребра (12 пар)', 'en': '24 ribs (12 pairs)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Human_rib_cage_anterior.jpg/800px-Rib_cage.jpg',
        'fun_fact': {   'uz': "Dastlabki 7 jufti haqiqiy qovurg'alar, 8-10 soxta, oxirgi 11 va 12-jufti esa suzuvchi "
                              "(old tomondan birikmagan) qovurg'alar deb ataladi.",
                        'ru': 'У мужчин и женщин одинаковое число ребер: 7 пар истинных, 3 пары ложных и 2 пары '
                              'колеблющихся.',
                        'en': 'Humans possess 12 pairs of ribs (7 true, 3 false, and 2 floating), identical in count '
                              'between males and females.'},
        'aliases': ['24 qovurga', '12 juft', '24 ребра', '12 пар', '24 ribs', '12 pairs']},
    {   'id': 'nature_anatomy_064_cervical_vertebrae_count',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Insonning bo'yin umurtqa pog'onasida nechta bo'yin umurtqasi (cervical vertebrae) bor?",
                        'ru': 'Сколько шейных позвонков насчитывает позвоночник человека (столько же, сколько у '
                              'жирафа)?',
                        'en': 'How many cervical vertebrae comprise the human neck spine (identical in number to a '
                              'giraffe)?'},
        'options': {   'uz': ['5 ta', '10 ta', '12 ta', '7 ta umurtqa'],
                       'ru': ['5 позвонков', '10 позвонков', '12 позвонков', '7 позвонков'],
                       'en': ['5 vertebrae', '10 vertebrae', '12 vertebrae', '7 vertebrae']},
        'correct_index': 3,
        'correct_answer': {'uz': '7 ta umurtqa', 'ru': '7 позвонков', 'en': '7 vertebrae'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Cervical_vertebrae_human.jpg/800px-Cervical_spine.jpg',
        'fun_fact': {   'uz': "Birinchi bo'yin umurtqasi 'Atlant' (bosh suyagini ushlab turuvchi), ikkinchisi esa "
                              "'Epistrofey' (boshning burilish o'qi) deb ataladi.",
                        'ru': 'Первый шейный позвонок C1 называется атлантом, а второй C2 — осевым (аксисом), '
                              'обеспечивая вращение головы.',
                        'en': 'The cervical spine contains exactly 7 vertebrae (C1 Atlas through C7), consistent '
                              'across nearly all mammalian species.'},
        'aliases': ['7 ta', '7', '7 позвонков', '7 vertebrae']},
    {   'id': 'nature_anatomy_065_thickest_tendon',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson tanasidagi eng baquvvat va eng qalin pay qaysi (boldir mushaklarini tovon '
                              'suyagiga ulaydi)?',
                        'ru': 'Какое сухожилие является самым мощным, толстым и прочным в теле человека?',
                        'en': 'Which is the strongest, thickest, and most resilient tendon in the human body?'},
        'options': {   'uz': ['Axill payi (Achilles tendon)', 'Tizza payi', 'Biceps payi', 'Kaft payi'],
                       'ru': [   'Ахиллово сухожилие (пяточное)',
                                 'Связка надколенника',
                                 'Сухожилие бицепса',
                                 'Ладонный апоневроз'],
                       'en': [   'Achilles tendon (Calcaneal tendon)',
                                 'Patellar tendon',
                                 'Biceps tendon',
                                 'Palmar aponeurosis']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Axill payi (Achilles tendon)',
                              'ru': 'Ахиллово сухожилие (пяточное)',
                              'en': 'Achilles tendon (Calcaneal tendon)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Achilles_tendon_calcaneal.jpg/800px-Achilles_tendon.jpg',
        'fun_fact': {   'uz': "Axill payi yugurish va sakrashda 1 tonnagacha bo'lgan kuchlanish kuchiga bardosh bera "
                              'oladi.',
                        'ru': 'Ахиллово сухожилие выдерживает нагрузку на разрыв более 400–500 кг, запасая упругую '
                              'энергию при беге.',
                        'en': 'The Achilles tendon connects gastrocnemius and soleus muscles to the calcaneus, '
                              'withstanding tensile loads up to 10 times body weight.'},
        'aliases': ['axill payi', 'axilles payi', 'ахиллово сухожилие', 'achilles tendon']},
    {   'id': 'nature_anatomy_066_synovial_fluid_purpose',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson bo'g'imlarining yengil va ishqalanishsiz harakatlanishini ta'minlovchi 'bo'g'im "
                              "moyi' suyuqligi nima deb ataladi?",
                        'ru': 'Какая вязкая жидкость смазывает суставные хрящи, предотвращая их трение и износ?',
                        'en': 'What is the viscous non-Newtonian fluid that lubricates articulating joint surfaces to '
                              'minimize cartilage friction?'},
        'options': {   'uz': ['Qon plazmasi', 'Sinovial suyuqlik', 'Limfa', 'Orqa miya suyuqligi'],
                       'ru': ['Плазма крови', 'Синовиальная жидкость', 'Лимфа', 'Спинномозговая жидкость'],
                       'en': ['Blood plasma', 'Synovial fluid', 'Lymph', 'Cerebrospinal fluid']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Sinovial suyuqlik', 'ru': 'Синовиальная жидкость', 'en': 'Synovial fluid'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Synovial_joint_diagram_human.jpg/800px-Synovial_joint.jpg',
        'fun_fact': {   'uz': "Sinovial suyuqlik gialuron kislotasiga boy bo'lib, uning ishqalanish koeffitsiyenti muz "
                              'ustidagi muzdan 5 baravar silliqroqdir.',
                        'ru': 'Коэффициент трения в синовиальном суставе человека ниже, чем у конька на идеальном '
                              'гладком льду.',
                        'en': 'Rich in hyaluronic acid and lubricin, synovial fluid provides boundary lubrication with '
                              'a friction coefficient as low as 0.001.'},
        'aliases': ['sinovial suyuqlik', 'синовиальная жидкость', 'synovial fluid']},
    {   'id': 'nature_anatomy_067_cerebrospinal_fluid_purpose',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Miyani kalla suyagi ichida zarbalardan himoyalovchi va uni suzib turishiga imkon '
                              'beruvchi suyuqlik nima?',
                        'ru': 'Какая прозрачная жидкость омывает головной и спинной мозг, амортизируя удары и питая '
                              'нейроны?',
                        'en': 'Which clear protective fluid bathes and cushions the brain and spinal cord within the '
                              'subarachnoid space?'},
        'options': {   'uz': ['Limfa', 'Gialuron', 'Orqa miya suyuqligi (Likvor / CSF)', 'Endolimfa'],
                       'ru': ['Лимфа', 'Гиалурон', 'Спинномозговая жидкость (Ликвор)', 'Эндолимфа'],
                       'en': ['Lymph', 'Hyaluronan', 'Cerebrospinal fluid (CSF)', 'Endolymph']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Orqa miya suyuqligi (Likvor / CSF)',
                              'ru': 'Спинномозговая жидкость (Ликвор)',
                              'en': 'Cerebrospinal fluid (CSF)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Cerebrospinal_fluid_ventricles_mri.jpg/800px-CSF.jpg',
        'fun_fact': {   'uz': "Likvor tufayli 1.5 kg og'irlikdagi inson miyasi kalla suyagi ichida xuddi 50 grammdek "
                              'yengil suzib turadi (Arximed qonuni).',
                        'ru': 'Благодаря выталкивающей силе ликвора эффективный вес мозга снижается с 1500 граммов до '
                              '50 граммов, защищая сосуды основания от сдавления.',
                        'en': 'Cerebrospinal fluid buoyancy reduces the net effective mass of the 1,500-gram human '
                              'brain to merely ~50 grams, preventing self-crushing.'},
        'aliases': [   'likvor',
                       'orqa miya suyuqligi',
                       'ликвор',
                       'спинномозговая жидкость',
                       'cerebrospinal fluid',
                       'csf']},
    {   'id': 'nature_anatomy_068_taste_modalities_count',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tili retseptorlari tomonidan rasman tan olinadigan asosiy ta'mlar soni nechta?",
                        'ru': 'Сколько базовых вкусовых модальностей различают вкусовые сосочки языка человека?',
                        'en': 'How many distinct primary taste modalities are recognized by human gustatory taste '
                              'receptors?'},
        'options': {   'uz': ['4 ta', '6 ta', '10 ta', "5 ta (shirin, sho'r, nordon, achchiq, umami)"],
                       'ru': [   '4 вкуса',
                                 '6 вкусов',
                                 '10 вкусов',
                                 '5 вкусов (сладкий, соленый, кислый, горький, умами)'],
                       'en': ['4 tastes', '6 tastes', '10 tastes', '5 tastes (sweet, sour, salty, bitter, umami)']},
        'correct_index': 3,
        'correct_answer': {   'uz': "5 ta (shirin, sho'r, nordon, achchiq, umami)",
                              'ru': '5 вкусов (сладкий, соленый, кислый, горький, умами)',
                              'en': '5 tastes (sweet, sour, salty, bitter, umami)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tongue_taste_buds_papillae_macro.jpg/800px-Taste_buds.jpg',
        'fun_fact': {   'uz': "Beshinchi ta'm — 'umami' (go'shtli-oqsilli ta'm) 1908-yilda yapon kimyogari Kikunae "
                              'Ikeda tomonidan kashf qilingan va glutamat retseptorlari orqali seziladi.',
                        'ru': 'Старый миф о «карте языка» неверен: все пять базовых вкусов воспринимаются рецепторами '
                              'по всей поверхности языка.',
                        'en': 'Human taste buds detect five basic modalities across the entire tongue: sweet (sugars), '
                              'sour (H+ ions), salty (Na+ ions), bitter, and savory umami (glutamate).'},
        'aliases': ['5 ta', '5', '5 вкусов', '5 tastes', 'umami']},
    {   'id': 'nature_anatomy_069_mitochondrial_dna_inheritance',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Mitoxondriya DNKsi (mtDNK) inson bolasiga kimdan meros bo'lib o'tadi?",
                        'ru': 'По какой родительской линии передается митохондриальная ДНК всем детям человека?',
                        'en': 'Through which parental lineage is mitochondrial DNA (mtDNA) exclusively passed down to '
                              'offspring?'},
        'options': {   'uz': [   'Faqat onadan (Onaning tuxum hujayrasi orqali)',
                                 'Faqat otadan',
                                 'Ikkala ota-onadan teng',
                                 'Tasodifiy ravishda'],
                       'ru': [   'Исключительно по материнской линии',
                                 'Исключительно по отцовской линии',
                                 'От обоих родителей поровну',
                                 'Случайным образом'],
                       'en': [   'Exclusively from the mother (Maternal lineage)',
                                 'Exclusively from father',
                                 'Equally from both parents',
                                 'Randomly']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Faqat onadan (Onaning tuxum hujayrasi orqali)',
                              'ru': 'Исключительно по материнской линии',
                              'en': 'Exclusively from the mother (Maternal lineage)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Mitochondrial_DNA_maternal_inheritance.jpg/800px-Mtdna_inheritance.jpg',
        'fun_fact': {   'uz': "Urug'lanishda spermatozoidning mitoxondriyalari tuxum hujayra ichiga kirmaydi yoki yo'q "
                              "qilinadi; shu sababli olimlar barcha odamlarning kelib chiqishini 'Mitoxondrial Momo "
                              "Havo' orqali kuzatadilar.",
                        'ru': 'Сперматозоид теряет свои митохондрии при оплодотворении, поэтому мтДНК позволяет '
                              'отследить прямую женскую родословную человечества.',
                        'en': 'Sperm mitochondria are ubiquitinated and destroyed upon oocyte fertilization, ensuring '
                              'strict uniparental maternal inheritance of mtDNA.'},
        'aliases': ['onadan', 'faqat onadan', 'по материнской линии', 'материнская линия', 'maternal', 'mother']},
    {   'id': 'nature_anatomy_070_universal_cellular_energy_currency',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Insonning har bir hujayrasida kimyoviy energiyani saqlovchi va sarflovchi universal '
                              "'energiya valyutasi' molekulasi nima?",
                        'ru': 'Какая молекула служит универсальной разменной энергетической валютой во всех живых '
                              'клетках человека?',
                        'en': 'Which molecule serves as the universal chemical energy currency powering metabolic '
                              'processes in all human cells?'},
        'options': {   'uz': ['DNK', 'ATF (Adenozintrifosfat / ATP)', 'Glyukoza', 'RNK'],
                       'ru': ['ДНК', 'АТФ (Аденозинтрифосфат)', 'Глюкоза', 'РНК'],
                       'en': ['DNA', 'ATP (Adenosine triphosphate)', 'Glucose', 'RNA']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'ATF (Adenozintrifosfat / ATP)',
                              'ru': 'АТФ (Аденозинтрифосфат)',
                              'en': 'ATP (Adenosine triphosphate)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/ATP_chemical_structure_spacefill.jpg/800px-ATP_molecule.jpg',
        'fun_fact': {   'uz': "Katta odam organizmi bir kunda o'z tana vazniga teng miqdorda (50–70 kg) ATF "
                              'molekulasini sintezlaydi va sarflaydi; har bir molekula soniyasiga minglab marta '
                              'aylanadi.',
                        'ru': 'Организм человека ежедневно синтезирует и расходует количество молекул АТФ, примерно '
                              'равное собственной массе тела.',
                        'en': 'An adult synthesizes and hydrolyzes their own body weight in ATP (~50–70 kg) daily, '
                              'driving active transport and macromolecule assembly.'},
        'aliases': ['atf', 'atp', 'атф', 'adenozintrifosfat', 'adenosine triphosphate']},
    {   'id': 'nature_anatomy_071_macrophages_phagocytosis',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Begona bakteriyalar, viruslar va o'lik hujayralarni o'z ichiga yutib hazm qiluvchi "
                              'ulkan oq qon hujayralari nima?',
                        'ru': 'Какие крупные белые клетки иммунной системы захватывают и пожирают чужеродные бактерии '
                              'путем фагоцитоза?',
                        'en': 'Which large innate immune cells engulf and digest cellular debris, foreign pathogens, '
                              'and microbes via phagocytosis?'},
        'options': {   'uz': ['Eritrotsitlar', 'Trombotsitlar', 'Makrofaglar', 'Neyronlar'],
                       'ru': ['Эритроциты', 'Тромбоциты', 'Макрофаги', 'Нейроны'],
                       'en': ['Erythrocytes', 'Platelets', 'Macrophages', 'Neurons']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Makrofaglar', 'ru': 'Макрофаги', 'en': 'Macrophages'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Macrophage_engulfing_bacteria_sem.jpg/800px-Macrophage.jpg',
        'fun_fact': {   'uz': "Makrofag yunoncha 'katta yebto'ymas' degan ma'noni anglatadi; u bir vaqtning o'zida 100 "
                              'tagacha bakteriyani yutib yuborishga qodir.',
                        'ru': 'Макрофаги патрулируют все ткани, первыми встречая инфекцию и представляя антигены '
                              'Т-лимфоцитам.',
                        'en': 'Macrophages differentiate from circulating monocytes to patrol tissues, phagocytosing '
                              'up to 100 bacteria per cell.'},
        'aliases': ['makrofaglar', 'макрофаги', 'macrophages', 'macrophage']},
    {   'id': 'nature_anatomy_072_b_cells_antibodies',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Maxsus himoya oqsillari — antitanachalar (antitelolar) ishlab chiqaruvchi limfotsitlar '
                              'qaysi?',
                        'ru': 'Какие клетки иммунной системы созревают в плазматические клетки и вырабатывают '
                              'специфические защитные антитела (иммуноглобулины)?',
                        'en': 'Which lymphocytes mature into plasma cells to synthesize specific antigen-targeting '
                              'antibodies (immunoglobulins)?'},
        'options': {   'uz': ['T-killerlar', 'Eritrotsitlar', 'Trombotsitlar', 'B-limfotsitlar (B-cells)'],
                       'ru': ['Т-киллеры', 'Эритроциты', 'Тромбоциты', 'B-лимфоциты'],
                       'en': ['T-killer cells', 'Erythrocytes', 'Platelets', 'B-lymphocytes (B-cells)']},
        'correct_index': 3,
        'correct_answer': {'uz': 'B-limfotsitlar (B-cells)', 'ru': 'B-лимфоциты', 'en': 'B-lymphocytes (B-cells)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/B_cell_antibody_production.jpg/800px-B_cells.jpg',
        'fun_fact': {   'uz': 'B-limfotsitlarning plazma hujayrasi sekundiga 2000 tagacha antitanacha ishlab chiqaradi '
                              'va ular immunitet xotirasini shakllantiradi.',
                        'ru': 'Каждая активированная плазматическая В-клетка выбрасывает в кровоток до 2000 молекул '
                              'антител в секунду.',
                        'en': 'Activated B-lymphocytes differentiate into plasma cells pumping out ~2,000 antibody '
                              'molecules per second to neutralize antigens.'},
        'aliases': ['b-limfotsitlar', 'b limfotsitlar', 'в-лимфоциты', 'b-cells', 'b cells']},
    {   'id': 'nature_anatomy_073_largest_artery',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Yurakning chap qorinchasidan chiqib butun tanaga kislorodli qon tarqatuvchi eng yo'g'on "
                              'bosh arteriya qaysi?',
                        'ru': 'Какая артерия является самой крупной и толстой в организме человека, отходя прямо от '
                              'левого желудочка сердца?',
                        'en': 'Which is the largest and thickest high-pressure artery in the human body, arising from '
                              'the left ventricle?'},
        'options': {   'uz': ['Aorta', "O'pka arteriyasi", 'Uyqu arteriyasi', 'Son arteriyasi'],
                       'ru': ['Аорта', 'Легочная артерия', 'Сонная артерия', 'Бедренная артерия'],
                       'en': ['Aorta', 'Pulmonary artery', 'Carotid artery', 'Femoral artery']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Aorta', 'ru': 'Аорта', 'en': 'Aorta'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Aorta_human_anatomy.jpg/800px-Aorta.jpg',
        'fun_fact': {   'uz': "Aortaning diametri 2.5–3 santimetr bo'lib, uning elastik devorlari yurakdan otilib "
                              "chiquvchi yuqori bosimli qon to'lqinini yutadi.",
                        'ru': 'Диаметр аорты у взрослого сопоставим с садовым шлангом (около 2,5–3 см), выдерживая '
                              'огромное давление пульсовой волны.',
                        'en': 'The ascending aorta measures ~2.5–3 cm in diameter with thick elastic walls that expand '
                              'during systole to buffer pulse pressure (Windkessel effect).'},
        'aliases': ['aorta', 'аорта', 'aorta']},
    {   'id': 'nature_anatomy_074_largest_veins',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Tanadan kislorodsiz qonni to'plab yurakning o'ng bo'lmachasiga quyuvchi eng katta vena "
                              'qon tomirlari qaysi?',
                        'ru': 'Какие вены являются самыми крупными в теле человека, возвращая обедненную кислородом '
                              'кровь в правое предсердие?',
                        'en': 'Which are the largest veins in the human body, returning deoxygenated systemic blood '
                              'back into the right atrium?'},
        'options': {   'uz': [   "O'pka venalari",
                                 'Kavak venalar (Yuqori va pastki kavak vena)',
                                 "Bo'yinturuq venasi",
                                 'Darvoza venasi'],
                       'ru': [   'Легочные вены',
                                 'Полые вены (Верхняя и нижняя полая вена)',
                                 'Яремная вена',
                                 'Воротная вена'],
                       'en': ['Pulmonary veins', 'Vena cava (Superior and Inferior)', 'Jugular vein', 'Portal vein']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Kavak venalar (Yuqori va pastki kavak vena)',
                              'ru': 'Полые вены (Верхняя и нижняя полая вена)',
                              'en': 'Vena cava (Superior and Inferior)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Vena_cava_inferior_superior.jpg/800px-Vena_cava.jpg',
        'fun_fact': {   'uz': "Pastki kavak vena tana pastki qismidan butun qonni yuqoriga yurakka ko'taradi va uning "
                              'ichki diametri 3 sm ga yetadi.',
                        'ru': 'Нижняя полая вена — самый широкий венозный сосуд тела, собирающий кровь от ног, таза и '
                              'органов брюшной полости.',
                        'en': 'The inferior vena cava is the largest diameter vein in the body, carrying desaturated '
                              'blood from lower extremities back to the heart.'},
        'aliases': ['kavak vena', 'полая вена', 'vena cava']},
    {   'id': 'nature_anatomy_075_left_vs_right_lung_difference',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Insonning chap o'pkasi o'ng o'pkasidan nimasi bilan farq qiladi?",
                        'ru': 'Чем левое легкое человека анатомически отличается от правого легкого?',
                        'en': 'How does the human left lung differ anatomically from the right lung?'},
        'options': {   'uz': [   "Chap o'pka kattaroq",
                                 "Chap o'pkada alveola bo'lmaydi",
                                 "Chap o'pka 2 ta bo'lakdan iborat (o'ng o'pka esa 3 ta bo'lakli)",
                                 "Farqi yo'q"],
                       'ru': [   'Левое легкое больше правого',
                                 'В левом легком нет альвеол',
                                 'В левом легком 2 доли, а в правом — 3 доли',
                                 'Они полностью одинаковы'],
                       'en': [   'Left lung is larger',
                                 'Left lung lacks alveoli',
                                 'Left lung has 2 lobes, right has 3 lobes',
                                 'They are identical']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Chap o'pka 2 ta bo'lakdan iborat (o'ng o'pka esa 3 ta bo'lakli)",
                              'ru': 'В левом легком 2 доли, а в правом — 3 доли',
                              'en': 'Left lung has 2 lobes, right has 3 lobes'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Human_lungs_lobes.jpg/800px-Lungs_lobes.jpg',
        'fun_fact': {   'uz': "Yurak ko'krak qafasining chap tomoniga biroz egilgani tufayli chap o'pkada yurak "
                              "o'ymasi (cardiac notch) bor va u o'ng o'pkadan 10% kichikroqdir.",
                        'ru': 'Сердечная вырезка оставляет меньше места в левой половине груди, поэтому левое легкое '
                              'имеет 2 доли вместо трех.',
                        'en': 'Due to the asymmetrical placement of the heart, the left lung has only superior and '
                              'inferior lobes, weighing ~10% less than the trilobed right lung.'},
        'aliases': ['2 bolakli', '2 доли', 'two lobes', '2 lobes']},
    {   'id': 'nature_anatomy_076_olfactory_receptors_diversity',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson burnidagi hid bilish retseptorlari taxminan nechta turli xil hidlarni ajrata '
                              'oladi?',
                        'ru': 'Сколько различных запахов способна различить обонятельная система человека по '
                              'современным исследованиям?',
                        'en': 'According to modern sensory research, roughly how many distinct scents can the human '
                              'olfactory system discriminate?'},
        'options': {   'uz': ['1000 ta', '10 000 ta', '100 000 ta', '1 trilliondan ortiq hidni'],
                       'ru': ['1000 запахов', '10 000 запахов', '100 000 запахов', 'Более 1 триллиона запахов'],
                       'en': ['1,000 scents', '10,000 scents', '100,000 scents', 'Over 1 trillion scents']},
        'correct_index': 3,
        'correct_answer': {   'uz': '1 trilliondan ortiq hidni',
                              'ru': 'Более 1 триллиона запахов',
                              'en': 'Over 1 trillion scents'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Olfactory_receptors_nasal_epithelium.jpg/800px-Olfactory.jpg',
        'fun_fact': {   'uz': '2014-yilda Rokfeller universiteti olimlari inson burni taxminan 400 turdagi hid '
                              "retseptorlari kombinatsiyasi orqali 1 trilliondan ortiq xushbo'y va badbo'y hidlarni "
                              'taniy olishini isbotlashdi.',
                        'ru': 'Исследования лаборатории Лесли Воссхолл доказали, что комбинаторный код обоняния '
                              'человека распознает свыше триллиона стимулов.',
                        'en': 'Research at Rockefeller University established that human olfactory receptors process '
                              'combinatorial scent mixtures to differentiate over 1 trillion distinct odors.'},
        'aliases': ['1 trillion', 'триллион', 'trillion', '1 trillion scents']},
    {   'id': 'nature_anatomy_077_blind_spot_cause',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Ko'z to'r pardasida hech narsa ko'rinmaydigan 'ko'r dog' (blind spot) paydo bo'lishiga "
                              "nima sabab bo'ladi?",
                        'ru': 'Чем обусловлено существование физиологического «слепого пятна» на сетчатке глаза '
                              'человека?',
                        'en': "What anatomical feature causes the physiological 'blind spot' in human retinal vision?"},
        'options': {   'uz': [   "Ko'rish nervi chiqish joyida fotoretseptorlar yo'qligi",
                                 "Ko'zning shikastlanishi",
                                 'Kipriklar soyasi',
                                 "Ko'z qorachig'i aksi"],
                       'ru': [   'Отсутствием фоторецепторов в месте выхода зрительного нерва',
                                 'Травмой роговицы',
                                 'Тенью от ресниц',
                                 'Бликом зрачка'],
                       'en': [   'Absence of photoreceptors where the optic nerve exits',
                                 'Corneal injury',
                                 'Eyelash shadow',
                                 'Pupil reflection']},
        'correct_index': 0,
        'correct_answer': {   'uz': "Ko'rish nervi chiqish joyida fotoretseptorlar yo'qligi",
                              'ru': 'Отсутствием фоторецепторов в месте выхода зрительного нерва',
                              'en': 'Absence of photoreceptors where the optic nerve exits'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Blind_spot_optic_disc_fundus.jpg/800px-Blind_spot.jpg',
        'fun_fact': {   'uz': "Ko'rish nervi to'r pardadan chiqadigan disk sohasida (optik disk) tayoqcha va "
                              "kolbachalar bo'lmaydi; bosh miya bu bo'shliqni atrof tasviri bilan o'zi to'ldirib "
                              "ko'rsatadi.",
                        'ru': 'Мозг автоматически дорисовывает недостающую картинку в зоне слепого пятна на основе '
                              'окружающего визуального контекста.',
                        'en': 'The optic disc lacks rods and cones because axonal fibers converge to form the optic '
                              'nerve, creating a physiological scotoma filled in by cortical interpolation.'},
        'aliases': ['kor dog', 'слепое пятно', 'blind spot', 'optic disc']},
    {   'id': 'nature_anatomy_078_pupil_constriction_muscle',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Kuchli yorug'lik tushganda qorachiqni kichraytiruvchi (toraytiruvchi) ko'z rangdor "
                              'pardasi mushagi qaysi?',
                        'ru': 'Какая кольцевая мышца радужки сужает зрачок при ярком освещении (сфинктер зрачка)?',
                        'en': 'Which smooth muscle sphincter of the iris constricts the pupil in response to bright '
                              'light?'},
        'options': {   'uz': [   'Qorachiq kengaytiruvchisi',
                                 'Qorachiq sfinkteri (Sphincter pupillae)',
                                 'Siliar mushak',
                                 "To'g'ri ko'z mushagi"],
                       'ru': ['Дилататор зрачка', 'Сфинктер зрачка', 'Цилиарная мышца', 'Прямая мышца глаза'],
                       'en': [   'Dilator pupillae',
                                 'Sphincter pupillae (Pupillary sphincter)',
                                 'Ciliary muscle',
                                 'Rectus muscle']},
        'correct_index': 1,
        'correct_answer': {   'uz': 'Qorachiq sfinkteri (Sphincter pupillae)',
                              'ru': 'Сфинктер зрачка',
                              'en': 'Sphincter pupillae (Pupillary sphincter)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Iris_pupil_constriction_macro.jpg/800px-Pupil_constriction.jpg',
        'fun_fact': {   'uz': "Qorachiq sfinkteri parasimpatik nervlar orqali boshqariladi va ko'z to'r pardasini "
                              "haddan tashqari ko'p yorug'likdan saqlaydi.",
                        'ru': 'Сфинктер сужает зрачок до 1,5 мм на солнце, а дилататор расширяет его до 8 мм в '
                              'темноте.',
                        'en': 'Innervated by parasympathetic postganglionic fibers via the oculomotor nerve (CN III), '
                              'the pupillary sphincter constricts the aperture to protect the retina.'},
        'aliases': ['qorachiq sfinkteri', 'сфинктер зрачка', 'sphincter pupillae', 'pupillary sphincter']},
    {   'id': 'nature_anatomy_079_appendix_true_function',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Uzoq vaqt keraksiz rudiment hisoblangan ko'richak o'simtasi (appendiks) aslida qanday "
                              'muhim vazifani bajaradi?',
                        'ru': 'Какую важную функцию выполняет аппендикс, который долгое время ошибочно считали '
                              'бесполезным рудиментом?',
                        'en': 'What vital physiological role does the vermiform appendix serve, formerly dismissed as '
                              'a useless vestigial structure?'},
        'options': {   'uz': [   "Ovqat hazm qiluvchi asosiy a'zo",
                                 'Qon filtrlovchi bez',
                                 "Foydali ichak bakteriyalari zaxira 'boshpanasi' va immun a'zosi",
                                 "Hech qanday foydasi yo'q"],
                       'ru': [   'Главный орган пищеварения',
                                 'Орган кроветворения',
                                 'Служит безопасным резервуаром для полезной микрофлоры кишечника',
                                 'Абсолютно бесполезен'],
                       'en': [   'Primary digestive organ',
                                 'Blood-filtering gland',
                                 'Safe-house reservoir for beneficial gut microbiome',
                                 'No biological function']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Foydali ichak bakteriyalari zaxira 'boshpanasi' va immun a'zosi",
                              'ru': 'Служит безопасным резервуаром для полезной микрофлоры кишечника',
                              'en': 'Safe-house reservoir for beneficial gut microbiome'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Vermiform_appendix_caecum.jpg/800px-Appendix.jpg',
        'fun_fact': {   'uz': "Kuchli ichketish yoki antibiotiklardan so'ng ichak mikroflorasi nobud bo'lganda, "
                              'appendiks ichida omon qolgan foydali bakteriyalar ichakni qayta tiklaydi.',
                        'ru': 'Аппендикс содержит огромное количество лимфоидной ткани и перезаселяет кишечник '
                              'полезными бактериями после диареи.',
                        'en': 'The appendix acts as a protected biofilm sanctuary that repopulates the colonic '
                              'commensal microbiota following enteric diarrheal purging.'},
        'aliases': ['appendiks', 'korichak osimtalari', 'аппендикс', 'appendix']},
    {   'id': 'nature_anatomy_080_hair_greying_cause',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson qariganda sochlarning oqarishiga (kulrang bo'lishiga) nima sabab bo'ladi?",
                        'ru': 'Что является биохимической причиной поседения волос при старении человека?',
                        'en': 'What biochemical mechanism causes human hair to lose its color and turn grey or white '
                              'with aging?'},
        'options': {   'uz': [   'Sochga havo pufakchalari kirishi',
                                 'Qon aylanishining buzilishi',
                                 'Bosh suyagi bosimi',
                                 "Soch ildizida melanin pigmenti ishlab chiqarilishining to'xtashi"],
                       'ru': [   'Попадание пузырьков воздуха',
                                 'Нарушение притока крови',
                                 'Сдавливание черепом',
                                 'Истощение меланоцитов и накопление перекиси водорода в фолликулах'],
                       'en': [   'Air bubbles in hair shaft',
                                 'Impaired scalp blood flow',
                                 'Cranial pressure',
                                 'Depletion of stem cell melanocytes and hydrogen peroxide buildup']},
        'correct_index': 3,
        'correct_answer': {   'uz': "Soch ildizida melanin pigmenti ishlab chiqarilishining to'xtashi",
                              'ru': 'Истощение меланоцитов и накопление перекиси водорода в фолликулах',
                              'en': 'Depletion of stem cell melanocytes and hydrogen peroxide buildup'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Gray_hair_follicle_melanocyte.jpg/800px-Gray_hair.jpg',
        'fun_fact': {   'uz': "Soch follikulasidagi melanosit ildiz hujayralari vaqt o'tishi bilan kamayadi va "
                              "follikulada to'planib qolgan vodorod peroksidi (H2O2) melaninni oqartirib yuboradi.",
                        'ru': 'С возрастом фермент каталаза перестает разрушать естественную перекись водорода в '
                              'фолликуле, и она обесцвечивает волосы изнутри.',
                        'en': 'Exhaustion of melanocyte stem cells and loss of catalase enzymes allow endogenous '
                              'hydrogen peroxide to bleach hair shafts from within.'},
        'aliases': ['soch oqarishi', 'melanosit', 'поседение', 'меланин', 'hair greying', 'gray hair']},
    {   'id': 'nature_anatomy_081_sweat_glands_count',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson terisida tanani sovutishga xizmat qiluvchi jami nechta ter bezi mavjud?',
                        'ru': 'Сколько примерно потовых желез (эккриновых и апокриновых) насчитывает кожа человека?',
                        'en': 'Approximately how many sweat glands (eccrine and apocrine) are embedded across human '
                              'skin?'},
        'options': {   'uz': ['Taxminan 2–4 millionta', '50 000 ta', '100 000 ta', '50 millionta'],
                       'ru': ['Около 2–4 миллионов', '50 000 желез', '100 000 желез', '50 миллионов желез'],
                       'en': ['Around 2–4 million', '50,000 glands', '100,000 glands', '50 million glands']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Taxminan 2–4 millionta', 'ru': 'Около 2–4 миллионов', 'en': 'Around 2–4 million'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Eccrine_sweat_gland_micrograph.jpg/800px-Sweat_glands.jpg',
        'fun_fact': {   'uz': "Kaftlarda va tovonlarda har santimetr kvadratiga 600–700 tagacha ter bezi to'g'ri "
                              'keladi; issiq kunda odam 10 litrgacha ter ajratishi mumkin.',
                        'ru': 'На ладонях и подошвах плотность потовых желез максимальна; испарение пота спасает '
                              'человека от теплового удара при нагрузках.',
                        'en': 'Human skin contains 2 to 4 million eccrine glands, concentrated highest on palms and '
                              'soles at up to 700 glands per square centimeter.'},
        'aliases': ['2-4 million', 'ter bezlari', 'потовые железы', 'sweat glands']},
    {   'id': 'nature_anatomy_082_normal_body_temperature',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson tanasining an'anaviy normal o'rtacha ichki harorati qancha deb hisoblanadi?",
                        'ru': 'Какова общепринятая стандартная нормальная температура тела здорового человека?',
                        'en': 'What is the universally accepted standard average internal resting core human body '
                              'temperature?'},
        'options': {   'uz': ['35.0 °C', '36.6 °C (98.6 °F)', '37.8 °C', '38.2 °C'],
                       'ru': ['35,0 °C', '36,6 °C (98,6 °F)', '37,8 °C', '38,2 °C'],
                       'en': ['35.0 °C', '36.6 °C (98.6 °F)', '37.8 °C', '38.2 °C']},
        'correct_index': 1,
        'correct_answer': {'uz': '36.6 °C (98.6 °F)', 'ru': '36,6 °C (98,6 °F)', 'en': '36.6 °C (98.6 °F)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Body_temperature_thermometer.jpg/800px-Body_temp.jpg',
        'fun_fact': {   'uz': 'Tana haroratini bosh miyadagi gipotalamus boshqaradi; kechasi u 36.0 °C gacha tushishi, '
                              "kechga tomon esa 37.2 °C gacha ko'tarilishi tabiiy fiziologik holatdir.",
                        'ru': 'Гипоталамус работает как внутренний термостат тела, поддерживая температуру для '
                              'оптимальной скорости ферментативных реакций.',
                        'en': 'Regulated by the preoptic area of the hypothalamus, core body temperature fluctuates '
                              'circadianly between ~36.1 °C and ~37.2 °C.'},
        'aliases': ['36.6', '36.6 c', '36,6', '36.6 c']},
    {   'id': 'nature_anatomy_083_resting_heart_rate_normal',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Sog'lom katta yoshli insonning tinch holatdagi normal yurak urish tezligi (puls) "
                              'qancha?',
                        'ru': 'Какова нормальная частота сердечных сокращений (пульс) взрослого человека в состоянии '
                              'покоя?',
                        'en': 'What is the standard resting heart rate range for a healthy, relaxed adult human?'},
        'options': {   'uz': ['30 – 50 zarba', '110 – 140 zarba', 'Daqiqasiga 60 – 100 zarba', '150 – 180 zarba'],
                       'ru': ['30 – 50 ударов', '110 – 140 ударов', '60 – 100 ударов в минуту', '150 – 180 ударов'],
                       'en': ['30 to 50 bpm', '110 to 140 bpm', '60 to 100 beats per minute', '150 to 180 bpm']},
        'correct_index': 2,
        'correct_answer': {   'uz': 'Daqiqasiga 60 – 100 zarba',
                              'ru': '60 – 100 ударов в минуту',
                              'en': '60 to 100 beats per minute'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Radial_pulse_check.jpg/800px-Pulse.jpg',
        'fun_fact': {   'uz': "Professional sportchilarda yurak mushagi baquvvat bo'lgani uchun tinch holatda puls "
                              'daqiqasiga 40–50 tagacha (bradikardiya) tushishi mumkin.',
                        'ru': 'У тренированных атлетов пульс покоя может составлять 40 ударов в минуту за счет '
                              'увеличенного ударного объема левого желудочка.',
                        'en': 'Resting heart rates range normally from 60 to 100 bpm; endurance athletes often display '
                              'physiologic bradycardia down to 40 bpm.'},
        'aliases': ['60-100', '60-100 zarba', '60-100 ударов', '60 to 100 bpm']},
    {   'id': 'nature_anatomy_084_blood_volume_adult',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "O'rtacha 70 kg vaznli katta odam tanasida taxminan necha litr qon aylanadi?",
                        'ru': 'Сколько примерно литров крови циркулирует в теле взрослого человека весом 70 кг?',
                        'en': 'Approximately how many liters of total blood circulate throughout the body of an '
                              'average 70-kg adult?'},
        'options': {   'uz': ['2 litr', '10 litr', '15 litr', 'Taxminan 5 litr (tana vaznining 7-8% i)'],
                       'ru': ['2 литра', '10 литров', '15 литров', 'Около 5 литров (7–8% массы тела)'],
                       'en': ['2 liters', '10 liters', '15 liters', 'Around 5 liters (7–8% of body weight)']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Taxminan 5 litr (tana vaznining 7-8% i)',
                              'ru': 'Около 5 литров (7–8% массы тела)',
                              'en': 'Around 5 liters (7–8% of body weight)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Blood_donation_bag.jpg/800px-Blood_volume.jpg',
        'fun_fact': {   'uz': "Inson 5 litr qonidan 10-15% qismini yo'qotishga bardosh beradi; 30-40% dan ortiq qon "
                              "yo'qotilishi esa hayot uchun xavflidir.",
                        'ru': 'Объем циркулирующей крови составляет около 5 литров, из которых около 55% приходится на '
                              'плазму и 45% — на форменные элементы.',
                        'en': 'Total blood volume averages roughly 5 liters (women ~4.5 L, men ~5.5 L), consisting of '
                              '~55% plasma and ~45% formed elements.'},
        'aliases': ['5 litr', '5 литров', '5 liters', '5l']},
    {   'id': 'nature_anatomy_085_mitral_valve_location',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Yurakning chap bo'lmachasi bilan chap qorinchasi o'rtasida joylashgan ikki tavaqali "
                              'klapan nima deb ataladi?',
                        'ru': 'Как называется двустворчатый клапан, расположенный между левым предсердием и левым '
                              'желудочком сердца?',
                        'en': 'What is the medical name for the bicuspid heart valve located between the left atrium '
                              'and left ventricle?'},
        'options': {   'uz': [   'Mitral klapan (Bikuspidal klapan)',
                                 'Trikuspidal klapan',
                                 'Aorta klapani',
                                 "O'pka klapani"],
                       'ru': [   'Митральный клапан (Двустворчатый)',
                                 'Трехстворчатый клапан (Трикуспидальный)',
                                 'Аортальный клапан',
                                 'Клапан легочного ствола'],
                       'en': ['Mitral valve (Bicuspid valve)', 'Tricuspid valve', 'Aortic valve', 'Pulmonary valve']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Mitral klapan (Bikuspidal klapan)',
                              'ru': 'Митральный клапан (Двустворчатый)',
                              'en': 'Mitral valve (Bicuspid valve)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Mitral_valve_heart_anatomy.jpg/800px-Mitral_valve.jpg',
        'fun_fact': {   'uz': "Mitral klapanning shakli katolik yepiskoplarining bosh kiyimi (mitra)ga o'xshagani "
                              'uchun unga shunday nom berilgan.',
                        'ru': 'Митральный клапан выдерживает максимальное гидродинамическое давление во время систолы '
                              'левого желудочка.',
                        'en': "Named for its resemblance to a bishop's ceremonial miter headdress, the mitral valve "
                              'prevents backflow into the pulmonary circulation.'},
        'aliases': ['mitral klapan', 'митральный клапан', 'mitral valve', 'bicuspid valve']},
    {   'id': 'nature_anatomy_086_cranial_nerves_count',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson bosh suyagi asosidan to'g'ridan-to'g'ri chiquvchi bosh miya nervlari nechta "
                              'juftdan iborat?',
                        'ru': 'Сколько пар черепных нервов отходит непосредственно от ствола головного мозга человека?',
                        'en': 'How many pairs of cranial nerves emerge directly from the human brainstem and base of '
                              'the brain?'},
        'options': {   'uz': ['10 juft', '12 juft', '24 juft', '31 juft'],
                       'ru': ['10 пар', '12 пар', '24 пары', '31 пара'],
                       'en': ['10 pairs', '12 pairs', '24 pairs', '31 pairs']},
        'correct_index': 1,
        'correct_answer': {'uz': '12 juft', 'ru': '12 пар', 'en': '12 pairs'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/12_cranial_nerves_human_brain.jpg/800px-Cranial_nerves.jpg',
        'fun_fact': {   'uz': "12 juft nervlar hid bilish (I), ko'rish (II), ko'z harakati (III, IV, VI), eshitish "
                              "(VIII) va boshqa a'zolarni to'g'ridan-to'g'ri boshqaradi.",
                        'ru': 'Спинной мозг дает начало 31 паре спинномозговых нервов, а головной мозг — ровно 12 '
                              'парам черепно-мозговых нервов.',
                        'en': 'The 12 pairs of cranial nerves innervate head and neck structures, with the vagus nerve '
                              '(CN X) descending through thorax and abdomen.'},
        'aliases': ['12 juft', '12 пар', '12 pairs', '12']},
    {   'id': 'nature_anatomy_087_spinal_nerves_count',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson orqa miyasidan umurtqalararo teshiklar orqali chiquvchi orqa miya nervlari nechta '
                              'juft?',
                        'ru': 'Сколько пар спинномозговых нервов отходит от сегментов спинного мозга человека?',
                        'en': 'How many bilateral pairs of spinal nerves originate along the segments of the human '
                              'spinal cord?'},
        'options': {   'uz': ['12 juft', '24 juft', '31 juft', '46 juft'],
                       'ru': ['12 пар', '24 пары', '31 пара', '46 пар'],
                       'en': ['12 pairs', '24 pairs', '31 pairs', '46 pairs']},
        'correct_index': 2,
        'correct_answer': {'uz': '31 juft', 'ru': '31 пара', 'en': '31 pairs'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Spinal_cord_segments_nerves.jpg/800px-Spinal_nerves.jpg',
        'fun_fact': {   'uz': "31 juft nerv tarkibi: 8 ta bo'yin, 12 ta ko'krak, 5 ta bel, 5 ta dumg'aza va 1 ta dum "
                              'nervlaridan iborat.',
                        'ru': 'Спинномозговые нервы образуют нервные сплетения (шейное, плечевое, поясничное), '
                              'управляя мышцами конечностей.',
                        'en': 'The 31 spinal nerve pairs comprise 8 cervical, 12 thoracic, 5 lumbar, 5 sacral, and 1 '
                              'coccygeal pair.'},
        'aliases': ['31 juft', '31 пара', '31 pairs', '31']},
    {   'id': 'nature_anatomy_088_forearm_two_bones',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson bilagini (tirsakdan bilakkacha) tashkil etuvchi ikkita suyak qaysi?',
                        'ru': 'Какие две кости формируют скелет предплечья человека?',
                        'en': 'Which two long parallel bones constitute the skeletal anatomy of the human forearm?'},
        'options': {   'uz': [   'Katta va kichik boldir',
                                 'Son va tovon',
                                 'Yelka va kurak',
                                 'Bilak va tirsak suyagi (Radius va Ulna)'],
                       'ru': [   'Большеберцовая и малоберцовая',
                                 'Бедренная и пяточная',
                                 'Плечевая и лопатка',
                                 'Лучевая и локтевая кости'],
                       'en': ['Tibia and Fibula', 'Femur and Calcaneus', 'Humerus and Scapula', 'Radius and Ulna']},
        'correct_index': 3,
        'correct_answer': {   'uz': 'Bilak va tirsak suyagi (Radius va Ulna)',
                              'ru': 'Лучевая и локтевая кости',
                              'en': 'Radius and Ulna'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Radius_and_ulna_bones_human.jpg/800px-Forearm_bones.jpg',
        'fun_fact': {   'uz': 'Radius suyagi tirsak suyagi atrofida aylana oladi; bu mexanizm kaftni pastga '
                              '(pronatsiya) va yuqoriga (supinatsiya) burish imkonini beradi.',
                        'ru': 'Вращение лучевой кости вокруг локтевой обеспечивает супинацию и пронацию кисти руки.',
                        'en': 'The radius pivots around the ulna at proximal and distal radioulnar joints, enabling '
                              'pronation and supination movements of the hand.'},
        'aliases': ['radius va ulna', 'bilak va tirsak', 'лучевая и локтевая', 'radius and ulna']},
    {   'id': 'nature_anatomy_089_lower_leg_two_bones',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson boldirini (tizzadan to'piqqacha) tashkil etuvchi ikkita suyak qaysi?",
                        'ru': 'Какие две параллельные кости образуют скелет голени человека?',
                        'en': 'Which two parallel bones comprise the skeletal structure of the human lower leg (shin '
                              'and calf)?'},
        'options': {   'uz': [   'Katta va kichik boldir suyagi (Tibia va Fibula)',
                                 'Radius va Ulna',
                                 'Son va Patella',
                                 'Klavikula va Skapula'],
                       'ru': [   'Большеберцовая и малоберцовая кости',
                                 'Лучевая и локтевая',
                                 'Бедренная и надколенник',
                                 'Ключица и лопатка'],
                       'en': ['Tibia and Fibula', 'Radius and Ulna', 'Femur and Patella', 'Clavicle and Scapula']},
        'correct_index': 0,
        'correct_answer': {   'uz': 'Katta va kichik boldir suyagi (Tibia va Fibula)',
                              'ru': 'Большеберцовая и малоберцовая кости',
                              'en': 'Tibia and Fibula'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tibia_and_fibula_bones_human.jpg/800px-Shin_bones.jpg',
        'fun_fact': {   'uz': "Katta boldir suyagi (Tibia) tana og'irligining 90% ini ko'taradi; kichik boldir suyagi "
                              "(Fibula) esa to'piq bo'g'imini barqarorlashtiradi.",
                        'ru': 'Большеберцовая кость несет на себе почти всю массу тела человека, а малоберцовая служит '
                              'местом прикрепления мышц стопы.',
                        'en': 'The robust tibia supports over 90% of compressive axial body weight, while the slender '
                              'fibula stabilizes the lateral ankle mortise.'},
        'aliases': ['tibia va fibula', 'boldir suyaklari', 'большеберцовая и малоберцовая', 'tibia and fibula']},
    {   'id': 'nature_anatomy_090_primary_bone_mineral',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson suyaklarining mustahkamligi va qattiqligini ta'minlovchi asosiy mineral element "
                              'nima?',
                        'ru': 'Какой минеральный элемент составляет основу костной ткани и содержится в теле на 99% '
                              'именно в костях?',
                        'en': 'Which essential chemical element accounts for 99% of total body mineral stores, '
                              'sequestered primarily in bone matrix?'},
        'options': {   'uz': ['Temir', 'Kalsiy (va Fosfor)', 'Kaliy', 'Natriy'],
                       'ru': ['Железо', 'Кальций (и фосфор)', 'Калий', 'Натрий'],
                       'en': ['Iron', 'Calcium (and phosphorus)', 'Potassium', 'Sodium']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Kalsiy (va Fosfor)', 'ru': 'Кальций (и фосфор)', 'en': 'Calcium (and phosphorus)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Bone_matrix_calcium_hydroxyapatite.jpg/800px-Bone_calcium.jpg',
        'fun_fact': {   'uz': 'Inson tanasidagi 1 kg dan ortiq kalsiyning 99% qismi suyaklar va tishlarda '
                              'gidroksiapatit shaklida saqlanadi.',
                        'ru': 'Кости служат динамическим резервуаром кальция: если его не хватает в крови для сердца, '
                              'он вымывается из скелета.',
                        'en': 'Over 1 kg of elemental calcium is stored within skeletal hydroxyapatite, regulated by '
                              'parathyroid hormone and calcitonin.'},
        'aliases': ['kalsiy', 'кальций', 'calcium']},
    {   'id': 'nature_anatomy_091_red_bone_marrow_hematopoiesis',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Eritrotsitlar, leykotsitlar va trombotsitlar — barcha qon hujayralari qayerda hosil '
                              "bo'ladi?",
                        'ru': 'В каком кроветворном органе внутри губчатых костей образуются все клетки крови '
                              '(гемопоэз)?',
                        'en': 'In which spongy skeletal tissue are all red cells, white cells, and platelets '
                              'manufactured via hematopoiesis?'},
        'options': {   'uz': ['Sariq suyak iligi', 'Taloq', "Qizil suyak ko'migi (Red bone marrow)", 'Jigar'],
                       'ru': ['Желтый костный мозг', 'Селезенка', 'Красный костный мозг', 'Печень'],
                       'en': ['Yellow bone marrow', 'Spleen', 'Red bone marrow', 'Liver']},
        'correct_index': 2,
        'correct_answer': {   'uz': "Qizil suyak ko'migi (Red bone marrow)",
                              'ru': 'Красный костный мозг',
                              'en': 'Red bone marrow'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Bone_marrow_hematopoiesis_stem_cells.jpg/800px-Bone_marrow.jpg',
        'fun_fact': {   'uz': "Qizil suyak ko'migidagi gematopoetik ildiz hujayralari har kuni 200 milliarddan ortiq "
                              'yangi qon hujayralarini ishlab chiqaradi.',
                        'ru': 'Красный костный мозг взрослого весит около 2,6 кг и расположен в плоских костях таза, '
                              'ребрах и грудине.',
                        'en': 'Adult red bone marrow weighs ~2.6 kg, generating ~500 billion blood cells daily from '
                              'pluripotent hematopoietic stem cells.'},
        'aliases': ['qizil suyak komigi', 'suyak komigi', 'костный мозг', 'красный костный мозг', 'bone marrow']},
    {   'id': 'nature_anatomy_092_blood_ph_level',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson arterial qonining normal kislota-ishqor muvozanati (pH ko'rsatkichi) qancha "
                              "bo'lishi kerak?",
                        'ru': 'Каков строго поддерживаемый физиологический уровень pH артериальной крови здорового '
                              'человека?',
                        'en': 'What is the tightly regulated physiological pH range of arterial human blood?'},
        'options': {   'uz': ['pH 6.0 – 6.5', 'pH 7.0 (neytral)', 'pH 8.0 – 8.5', 'pH 7.35 – 7.45'],
                       'ru': ['pH 6,0 – 6,5', 'pH 7,0 (нейтральный)', 'pH 8,0 – 8,5', 'pH 7,35 – 7,45'],
                       'en': ['pH 6.0 – 6.5', 'pH 7.0 (neutral)', 'pH 8.0 – 8.5', 'pH 7.35 – 7.45']},
        'correct_index': 3,
        'correct_answer': {'uz': 'pH 7.35 – 7.45', 'ru': 'pH 7,35 – 7,45', 'en': 'pH 7.35 – 7.45'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Blood_gas_arterial_ph_scale.jpg/800px-Blood_ph.jpg',
        'fun_fact': {   'uz': "Qon pH ko'rsatkichi 6.8 dan pastga yoki 7.8 dan yuqoriga chiqsa, oqsillar "
                              "denaturatsiyasi tufayli hayot uchun o'lim xavfi tug'iladi.",
                        'ru': 'Буферные системы крови (бикарбонатная и гемоглобиновая) удерживают pH крови в узком '
                              'диапазоне 7,35–7,45.',
                        'en': 'Arterial blood pH is held between 7.35 and 7.45 by bicarbonate, phosphate, and plasma '
                              'protein buffering systems.'},
        'aliases': ['ph 7.4', 'ph 7.35', '7.35-7.45', 'ph 7.35-7.45']},
    {   'id': 'nature_anatomy_093_total_body_water_fraction',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Voyaga yetgan inson tana massasining necha foizi suvdan iborat?',
                        'ru': 'Какой процент массы тела взрослого человека составляет вода?',
                        'en': 'What percentage of total adult human body mass is water?'},
        'options': {   'uz': ['Taxminan 60%', '30%', '85%', '95%'],
                       'ru': ['Около 60%', '30%', '85%', '95%'],
                       'en': ['Around 60%', '30%', '85%', '95%']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Taxminan 60%', 'ru': 'Около 60%', 'en': 'Around 60%'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Body_water_percentage_distribution.jpg/800px-Body_water.jpg',
        'fun_fact': {   'uz': "Inson miyasi va yuragi 73% suvdan, o'pka 83% suvdan, hatto qattiq suyaklar ham 31% "
                              'suvdan tashkil topgan.',
                        'ru': 'Около двух третей всей воды находится внутри клеток (интрацеллюлярно), а одна треть — '
                              'во внеклеточной жидкости и плазме.',
                        'en': "Total body water comprises ~60% of an adult male's weight (~42 L), split into "
                              'intracellular (~28 L) and extracellular fluid (~14 L).'},
        'aliases': ['60%', '60 foiz', '60 процентов', '60 percent']},
    {   'id': 'nature_anatomy_094_adult_permanent_teeth_count',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Voyaga yetgan insonning to'liq tish formulasida (aql tishlari bilan birga) nechta "
                              "doimiy tish bo'ladi?",
                        'ru': 'Сколько постоянных зубов насчитывает полная зубная формула взрослого человека (включая '
                              'зубы мудрости)?',
                        'en': 'How many permanent teeth are present in a complete adult human dentition (including '
                              'wisdom teeth)?'},
        'options': {   'uz': ['28 ta tish', '32 ta tish', '36 ta tish', '20 ta tish'],
                       'ru': ['28 зубов', '32 зуба', '36 зубов', '20 зубов'],
                       'en': ['28 teeth', '32 teeth', '36 teeth', '20 teeth']},
        'correct_index': 1,
        'correct_answer': {'uz': '32 ta tish', 'ru': '32 зуба', 'en': '32 teeth'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Adult_permanent_dentition_32.jpg/800px-Human_teeth.jpg',
        'fun_fact': {   'uz': '32 ta tish tarkibi: 8 ta kesuvchi, 4 ta qoziq tish, 8 ta kichik oziq tish (premolyar) '
                              'va 12 ta katta oziq tish (molyar)dan iborat.',
                        'ru': 'У детей вырастает 20 молочных зубов, которые затем сменяются 32 постоянными зубами.',
                        'en': 'Adult dentition consists of 32 permanent teeth: 8 incisors, 4 canines, 8 premolars, and '
                              '12 molars (including 4 third molars).'},
        'aliases': ['32 tish', '32', '32 зуба', '32 teeth']},
    {   'id': 'nature_anatomy_095_cornea_optical_power',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Inson ko'zining umumiy optik sindirish kuchining (taxminan 60 dioptriya) asosiy 2/3 "
                              "qismi qaysi tuzilmaga to'g'ri keladi?",
                        'ru': 'Какая часть глаза обеспечивает две трети всей оптической силы преломления света (около '
                              '43 диоптрий из 60)?',
                        'en': "Which refractive structure provides approximately two-thirds of the human eye's total "
                              'optical power (~43 diopters)?'},
        'options': {   'uz': ['Gavhar (Lens)', 'Shishasimon tana', 'Shox parda (Cornea)', "To'r parda"],
                       'ru': ['Хрусталик', 'Стекловидное тело', 'Роговица', 'Сетчатка'],
                       'en': ['Crystalline Lens', 'Vitreous humor', 'Cornea', 'Retina']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Shox parda (Cornea)', 'ru': 'Роговица', 'en': 'Cornea'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cornea_refraction_optics.jpg/800px-Cornea_optics.jpg',
        'fun_fact': {   'uz': "Gavhar faqat fokuslashni (akkomodatsiya) boshqaradi, yorug'likning asosiy sinishi havo "
                              'va shox parda chegarasida yuz beradi.',
                        'ru': 'Хрусталик добавляет лишь около 15–20 диоптрий для фокусировки, тогда как роговица '
                              'обеспечивает стабильные 43 диоптрии.',
                        'en': 'The cornea provides ~43 diopters of fixed converging refractive power due to the large '
                              'refractive index difference between air and tissue.'},
        'aliases': ['shox parda', 'rogovitsa', 'роговица', 'cornea']},
    {   'id': 'nature_anatomy_096_hemophilia_clotting_disorder',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Qon ivishi omili (VIII omil) yetishmovchiligi tufayli qon ketishi to'xtamaydigan irsiy "
                              'genetik kasallik nima deb ataladi?',
                        'ru': 'Как называется наследственное заболевание, при котором кровь теряет способность '
                              'свертываться из-за дефицита факторов VIII или IX?',
                        'en': 'What is the hereditary X-linked genetic disorder characterized by deficiency in blood '
                              'clotting factor VIII, preventing coagulation?'},
        'options': {   'uz': ['Anemiya', 'Leykoz', 'Trombotsitopeniya', 'Gemofiliya'],
                       'ru': ['Анемия', 'Лейкоз', 'Тромбоцитопения', 'Гемофилия'],
                       'en': ['Anemia', 'Leukemia', 'Thrombocytopenia', 'Hemophilia (Hemophilia A)']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Gemofiliya', 'ru': 'Гемофилия', 'en': 'Hemophilia (Hemophilia A)'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Hemophilia_inheritance_x_linked.jpg/800px-Hemophilia.jpg',
        'fun_fact': {   'uz': "Gemofiliya X xromosomasiga bog'langan retsessiv gen orqali o'tadi va asosan erkaklarda "
                              "uchraydi; u tarixda qirollik oilalari orqali mashhur bo'lgan.",
                        'ru': 'Гемофилией А страдали многие потомки королевы Виктории, включая цесаревича Алексея в '
                              'России.',
                        'en': 'Hemophilia A is an X-linked recessive disorder impairing factor VIII synthesis, leading '
                              'to prolonged bleeding into weight-bearing joints.'},
        'aliases': ['gemofiliya', 'гемофилия', 'hemophilia']},
    {   'id': 'nature_anatomy_097_skin_dermis_layer',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Epidermis ostida joylashgan, kollagen tolalari, qon tomirlari, asab oxirlari va ter '
                              "bezlarini o'z ichiga olgan 'chin teri' qatlami nima?",
                        'ru': 'Какой слой кожи расположен под эпидермисом и содержит кровеносные сосуды, коллаген, '
                              'волосяные луковицы и рецепторы?',
                        'en': 'Which structural skin layer beneath the epidermis houses vascular beds, collagen '
                              'networks, nerve endings, and hair follicles?'},
        'options': {   'uz': ['Derma (Chin teri)', 'Epidermis', "Gipoderma (Yog' qatlami)", 'Kutikula'],
                       'ru': [   'Дерма (собственно кожа)',
                                 'Эпидермис',
                                 'Гиподерма (подкожно-жировая клетчатка)',
                                 'Кутикула'],
                       'en': ['Dermis', 'Epidermis', 'Hypodermis (Subcutis)', 'Cuticle']},
        'correct_index': 0,
        'correct_answer': {'uz': 'Derma (Chin teri)', 'ru': 'Дерма (собственно кожа)', 'en': 'Dermis'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Human_skin_layers.jpg/800px-Dermis.jpg',
        'fun_fact': {   'uz': 'Derma qatlamidagi I va III turdagi kollagen tolalari teriga elastiklik va mustahkamlik '
                              "beradi; yosh o'tishi bilan kollagen kamayishi ajinlarni keltirib chiqaradi.",
                        'ru': 'Дерма образована сосочковым и сетчатым слоями, обеспечивая механическую прочность кожи '
                              'и питание эпидермиса.',
                        'en': 'The dermis is a dense irregular connective tissue matrix rich in elastin and collagen '
                              'type I, anchoring cutaneous sensory mechanoreceptors.'},
        'aliases': ['derma', 'chin teri', 'дерма', 'dermis']},
    {   'id': 'nature_anatomy_098_cortisol_stress_hormone',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Buyrak usti bezining po'stloq qismidan ajralib chiquvchi, surunkali stress va "
                              'metabolizmni boshqaruvchi asosiy steroid gormon nima?',
                        'ru': 'Какой стероидный гормон коры надпочечников называют главным «гормоном хронического '
                              'стресса»?',
                        'en': 'Which glucocorticoid steroid hormone secreted by the adrenal cortex regulates chronic '
                              'stress, immune suppression, and gluconeogenesis?'},
        'options': {   'uz': ['Adrenalin', 'Kortizol (Cortisol)', 'Aldosteron', 'Insulin'],
                       'ru': ['Адреналин', 'Кортизол', 'Альдостерон', 'Инсулин'],
                       'en': ['Adrenaline', 'Cortisol', 'Aldosterone', 'Insulin']},
        'correct_index': 1,
        'correct_answer': {'uz': 'Kortizol (Cortisol)', 'ru': 'Кортизол', 'en': 'Cortisol'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cortisol_steroid_structure.jpg/800px-Cortisol.jpg',
        'fun_fact': {   'uz': "Kortizol ertalab uyg'onganda eng yuqori darajaga chiqadi va odamni tetiklashtiradi; "
                              'doimiy ortiqcha kortizol esa immunitetni zaiflashtiradi.',
                        'ru': 'Кортизол повышает уровень глюкозы в крови за счет распада белков и подавляет '
                              'воспалительные реакции организма.',
                        'en': 'Cortisol follows a diurnal rhythm peaking shortly after awakening (cortisol awakening '
                              'response), mobilizing glucose and downregulating cytokines.'},
        'aliases': ['kortizol', 'кортизол', 'cortisol']},
    {   'id': 'nature_anatomy_099_smallest_structural_unit_life',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': 'Inson tanasidagi hayotning eng kichik mustaqil tirik strukturaviy va funksional birligi '
                              'nima?',
                        'ru': 'Что является наименьшей живой структурно-функциональной единицей строения и '
                              'жизнедеятельности человеческого организма?',
                        'en': 'What is the smallest independent living structural and functional unit composing the '
                              'human body?'},
        'options': {   'uz': ['Molekula', 'Organ', 'Hujayra (Cell)', "To'qima"],
                       'ru': ['Молекула', 'Орган', 'Клетка', 'Ткань'],
                       'en': ['Molecule', 'Organ', 'Cell', 'Tissue']},
        'correct_index': 2,
        'correct_answer': {'uz': 'Hujayra (Cell)', 'ru': 'Клетка', 'en': 'Cell'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Animal_cell_structure_en.svg/800px-Cell.jpg',
        'fun_fact': {   'uz': "Inson tanasida taxminan 30–37 trillionta hujayra mavjud bo'lib, ularning 200 dan ortiq "
                              'ixtisoslashgan turlari (neyronlar, miotsitlar, eritrotsitlar) faoliyat yuritadi.',
                        'ru': 'Организм человека состоит примерно из 37 триллионов клеток, координируемых нервной и '
                              'гуморальной системами.',
                        'en': 'The adult human body comprises ~37 trillion eukaryotic cells organized across more than '
                              '200 distinct specialized cell phenotypes.'},
        'aliases': ['hujayra', 'клетка', 'cell']},
    {   'id': 'nature_anatomy_100_liver_bile_synthesis',
        'sub_mode': 'human_anatomy',
        'question': {   'uz': "Yog'larni hazm qilishda qatnashuvchi safro (o't suyuqligi) qaysi a'zoda sintezlanadi?",
                        'ru': 'В каком жизненно важном органе непрерывно синтезируется желчь, расщепляющая жиры?',
                        'en': 'In which vital organ is digestive bile continuously synthesized before storage in the '
                              'gallbladder?'},
        'options': {   'uz': ["O't pufagi", 'Oshqozon', 'Taloq', 'Jigar (Liver)'],
                       'ru': ['Желчный пузырь', 'Желудок', 'Селезенка', 'Печень'],
                       'en': ['Gallbladder', 'Stomach', 'Spleen', 'Liver']},
        'correct_index': 3,
        'correct_answer': {'uz': 'Jigar (Liver)', 'ru': 'Печень', 'en': 'Liver'},
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Human_liver_anatomy.jpg/800px-Liver_bile.jpg',
        'fun_fact': {   'uz': "Odam jigari har kuni 800 dan 1000 ml gacha safro ishlab chiqaradi va uni o't yo'llari "
                              'orqali chiqaradi.',
                        'ru': 'Гепатоциты печени синтезируют около 1 литра желчи в сутки, эмульгирующей пищевые '
                              'липиды.',
                        'en': 'Hepatocytes synthesize 800–1,000 ml of bile daily from cholesterol and bile acids, '
                              'facilitating lipid emulsification in the small intestine.'},
        'aliases': ['jigar', 'печень', 'liver']}]

NATURE_BY_ID: Dict[str, Dict[str, Any]] = {item["id"]: item for item in NATURE_DATA}
NATURE_BY_SUBMODE: Dict[str, List[Dict[str, Any]]] = {}
for item in NATURE_DATA:
    NATURE_BY_SUBMODE.setdefault(item["sub_mode"], []).append(item)


def get_nature_item_by_id(item_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a nature game item by its unique ID."""
    return NATURE_BY_ID.get(item_id)


def get_random_nature_items(count: int = 1, sub_mode: Optional[str] = None) -> List[Dict[str, Any]]:
    """Sample random nature questions without replacement, optionally filtered by sub_mode."""
    pool = NATURE_BY_SUBMODE.get(sub_mode, NATURE_DATA) if sub_mode else NATURE_DATA
    if not pool:
        return []
    return random.sample(pool, min(count, len(pool)))


def get_nature_items_by_submode(sub_mode: str) -> List[Dict[str, Any]]:
    """Retrieve all nature game items for a specific sub-mode."""
    return NATURE_BY_SUBMODE.get(sub_mode, [])


def get_random_nature_item(sub_mode: Optional[str] = None) -> Dict[str, Any]:
    """Get a single random nature item, optionally filtered by sub-mode."""
    pool = NATURE_BY_SUBMODE.get(sub_mode, NATURE_DATA) if sub_mode else NATURE_DATA
    return random.choice(pool)


def search_nature_by_alias(query: str) -> Optional[Dict[str, Any]]:
    """Find a nature item matching user input across aliases or multilingual answers."""
    q = query.strip().lower()
    if not q:
        return None
    for item in NATURE_DATA:
        if q in item.get("aliases", []):
            return item
        for val in item.get("correct_answer", {}).values():
            if q == val.lower():
                return item
    return None

