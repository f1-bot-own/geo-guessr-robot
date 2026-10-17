# -*- coding: utf-8 -*-
"""
Builder script for Part 1: Black Box (Qora quti) - 125 questions.
"""
import json

RAW_BLACK_BOX = [
    {
        "item_uz": "Ko'zgu (Oyna)",
        "item_ru": "Зеркало",
        "item_en": "Mirror",
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutida shunday bir buyum borki, u qadimgi Xitoy va Misrda sayqallangan bronzadan yasalgan. Xalq e'tiqodlariga ko'ra, vampirlar unda o'z aksini ko'ra olmaydi, Lewis Carroll asarida esa Alisa uning ortidagi mo''jizalar olamiga tushib qoladi. Qora qutidagi buyumni toping.",
        "q_ru": "Внимание, чёрный ящик! В древности этот предмет изготавливали из полированной бронзы и серебра. Согласно поверьям, вампиры не отражаются в нём, а героиня Льюиса Кэрролла Алиса шагнула сквозь него в удивительный мир. Что лежит в чёрном ящике?",
        "q_en": "Attention, black box! In ancient China and Egypt, this item was crafted from polished bronze. In folklore, vampires cast no reflection in it, and Lewis Carroll's Alice stepped through it into a wonderland. What is in the black box?",
        "distractors_uz": ["Shisha qadah", "Surat ramkasi", "Teleskop"],
        "distractors_ru": ["Стеклянный бокал", "Фоторамка", "Телескоп"],
        "distractors_en": ["Glass goblet", "Picture frame", "Telescope"],
        "correct_pos": 0,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Mirror.jpg",
        "fun_fact_uz": "Ilk shisha oynalar 13-asrda Venetsiyaning Murano orolida yaratilgan bo'lib, oyna yasash siri davlat siri sifatida qattiq qo'riqlangan.",
        "fun_fact_ru": "Венецианские зеркала с острова Мурано ценились на вес золота, а мастерам-стеклодувам под страхом смерти запрещалось покидать республику.",
        "fun_fact_en": "Venetian glassmakers on the island of Murano were forbidden under pain of death from leaving Venice to protect the secret of mirror-making.",
        "aliases": ["ko'zgu", "oyna", "zerkalo", "mirror", "зеркало", "айна"]
    },
    {
        "item_uz": "Kompas",
        "item_ru": "Компас",
        "item_en": "Compass",
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutida qadimgi Xitoyning Xan sulolasi davrida kashf etilgan to'rt buyuk ixtironing biri joylashgan. U dastlab qoshiqsimon magnit toshdan yasalgan bo'lib, 'janubga ko'rsatkich' deb nomlangan. Buyuk geografik kashfiyotlar aynan shu buyum tufayli amalga oshgan. Qora qutida nima bor?",
        "q_ru": "Внимание, чёрный ящик! В нём находится одно из четырёх великих изобретений Древнего Китая эпохи Хань. Изначально он имел форму магнитной ложки и назывался 'указателем юга'. Именно благодаря ему состоялись Великие географические открытия. Что в чёрном ящике?",
        "q_en": "Attention, black box! Inside is one of the Four Great Inventions of Ancient China. Originally shaped like a magnetized spoon on a bronze plate, it was known as the 'south-pointer'. It enabled the Age of Discovery. What is in the black box?",
        "distractors_uz": ["Usturlob", "Qumsoat", "Barometr"],
        "distractors_ru": ["Астролябия", "Песочные часы", "Барометр"],
        "distractors_en": ["Astrolabe", "Hourglass", "Barometer"],
        "correct_pos": 1,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8e/2016_Busola.JPG",
        "fun_fact_uz": "Kompas ignasi geografik shimoliy qutbga emas, balki Yerning magnit qutbiga yo'naladi, bu farq magnit og'ishi deb ataladi.",
        "fun_fact_ru": "Стрелка компаса указывает не на географический, а на магнитный полюс Земли, который постоянно смещается.",
        "fun_fact_en": "A compass needle points to the Earth's magnetic north pole rather than true geographic north, an angle known as magnetic declination.",
        "aliases": ["kompas", "compass", "компас", "qutbnoma"]
    },
    {
        "item_uz": "Ko'zoynak",
        "item_ru": "Очки",
        "item_en": "Eyeglasses (Spectacles)",
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi ushbu buyum ilk bor 13-asr oxirida Italiyada paydo bo'lgan. Uning yaratilishida Ibn al-Haysamning optika bo'yicha ilmiy kashfiyotlari muhim rol o'ynagan. Petrarxa qarigan chog'ida ushbu buyum yordamida o'qishda davom etganini faxr bilan yozgan. Qora qutidagi buyumni ayting.",
        "q_ru": "Внимание, чёрный ящик! Этот предмет появился в Италии в конце XIII века на основе трудов арабского учёного Ибн аль-Хайсама. Поэт Петрарка писал, что в старости этот предмет вернул ему возможность читать. Что лежит в чёрном ящике?",
        "q_en": "Attention, black box! Invented in late 13th-century Italy using the optical principles discovered by Ibn al-Haytham, this device allowed the elderly poet Petrarch to continue reading manuscripts. What is in the black box?",
        "distractors_uz": ["Lupa", "Mikroskop", "Teleskop"],
        "distractors_ru": ["Лупа", "Микроскоп", "Телескоп"],
        "distractors_en": ["Magnifying glass", "Microscope", "Telescope"],
        "correct_pos": 2,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Square_sunglasses.jpg",
        "fun_fact_uz": "Dastlabki ko'zoynaklar quloqqa ilinadigan bandlarga ega bo'lmagan — ular burun ustiga qistirib taqilgan yoki qo'lda ushlab turilgan (lornet).",
        "fun_fact_ru": "Первые очки не имели заушников — их зажимали на переносице (пенсне) или держали в руке на рукоятке (лорнет).",
        "fun_fact_en": "Early eyeglasses had no temples to go over ears; they were balanced on the nose (pince-nez) or held by a handle (lorgnette).",
        "aliases": ["ko'zoynak", "kozoynak", "ochki", "eyeglasses", "glasses", "spectacles", "очки"]
    },
    {
        "item_uz": "Qumsoat",
        "item_ru": "Песочные часы",
        "item_en": "Hourglass",
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum o'rta asrlarda dengiz kemalarida tezlik va masofani o'lchashda (lag bilan birga) ajralmas vosita bo'lgan. Uning ichidagi modda hech qachon qotib qolmaydi va gravitatsiya tufayli bir maromda pastga oqadi. O'lim va vaqt o'tishi timsoli bo'lgan ushbu buyumni toping.",
        "q_ru": "Внимание, чёрный ящик! В Средневековье этот предмет был незаменим на кораблях для замера скорости лагом и вахтенного времени. Вещество внутри него не замерзает и течёт с постоянной скоростью под действием гравитации. Что лежит в чёрном ящике?",
        "q_en": "Attention, black box! Essential aboard sailing ships to measure speed with a chip log and nautical watches, this item contains a substance that flows steadily under gravity and never freezes. An allegory for mortality and time, what is in the box?",
        "distractors_uz": ["Suv soati", "Mexanik soat", "Quyosh soati"],
        "distractors_ru": ["Водяные часы", "Механические часы", "Солнечные часы"],
        "distractors_en": ["Water clock", "Mechanical clock", "Sundial"],
        "correct_pos": 3,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Half-hour_sand_glass_MET_ES268.jpg",
        "fun_fact_uz": "Dengiz qumsoatlarida odatda maydalangan marmar kukuni yoki qovurilgan tuxum po'chog'i ishlatilgan, chunki oddiy qum namlikda yopishib qolishi mumkin edi.",
        "fun_fact_ru": "На кораблях в песочные часы часто засыпали порошок из мрамора или толчёной яичной скорлупы, так как обычный песок слипался от влаги.",
        "fun_fact_en": "Nautical hourglasses often used powdered marble or pulverized eggshells rather than sand to prevent clumping from sea moisture.",
        "aliases": ["qumsoat", "qum soati", "hourglass", "sandglass", "песочные часы"]
    },
    {
        "item_uz": "Shaxmat shohi",
        "item_ru": "Шахматный король",
        "item_en": "Chess King",
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu narsa 64 katakli maydondagi eng muhim, ammo eng kuchsiz harakatlanuvchi figuralardan biridir. O'yinning nomi forschadan tarjima qilinganda aynan shu buyumning 'o'limi' yoki ojizligini bildiradi. Qora qutida nima bor?",
        "q_ru": "Внимание, чёрный ящик! Этот предмет — самая важная, но при этом весьма ограниченная в движениях фигура на 64-клеточном поле. Само название древней игры переводится с персидского как смерть или бессилие этой фигуры. Что в чёрном ящике?",
        "q_en": "Attention, black box! Inside is the most crucial yet vulnerable piece on a 64-square battlefield. The very name of the ancient game translates from Persian as 'the ruler is helpless or dead'. What is in the black box?",
        "distractors_uz": ["Shaxmat vaziri", "Shaxmat otasi (Rux)", "Shaxmat piyodasi"],
        "distractors_ru": ["Шахматный ферзь", "Шахматная ладья", "Шахматная пешка"],
        "distractors_en": ["Chess Queen", "Chess Rook", "Chess Pawn"],
        "correct_pos": 0,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Chess_klt45.svg",
        "fun_fact_uz": "'Shaxmat' so'zi forscha 'Shoh mot' — ya'ni 'Shoh ojiz qoldi' yoki 'Shoh vafot etdi' degan ma'noni anglatadi.",
        "fun_fact_ru": "Фраза 'Шах и мат' происходит от персидского 'Шах мат', что буквально означает 'правитель беспомощен' или 'правитель мёртв'.",
        "fun_fact_en": "The term 'checkmate' derives from Persian 'Shah mat', meaning 'the king is helpless' or 'the king is dead'.",
        "aliases": ["shaxmat shohi", "shoh", "chess king", "king", "шахматный король", "король"]
    }
]
print(f"Loaded {len(RAW_BLACK_BOX)} items in test.")
