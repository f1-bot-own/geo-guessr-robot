# -*- coding: utf-8 -*-
"""
Builder for Black Box questions (zakovat_001 to zakovat_125).
"""
import json
import os

BLACK_BOX_DATA = [
    # 1: Ko'zgu / Зеркало / Mirror
    {
        "uz": "Ko'zgu", "ru": "Зеркало", "en": "Mirror",
        "distractors_uz": ["Shisha qadah", "Surat ramkasi", "Teleskop"],
        "distractors_ru": ["Стеклянный бокал", "Фоторамка", "Телескоп"],
        "distractors_en": ["Glass goblet", "Picture frame", "Telescope"],
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum qadimgi Misr va Xitoyda sayqallangan bronzadan yasalgan. Xalq e'tiqodlariga ko'ra, vampirlar unda o'z aksini ko'ra olmaydi, Lewis Carroll asarida esa Alisa uning ortidagi mo''jizalar olamiga tushib qoladi. Qora qutidagi buyumni toping.",
        "q_ru": "Внимание, чёрный ящик! В древности этот предмет изготавливали из полированной бронзы. Согласно поверьям, вампиры не отражаются в нём, а героиня Льюиса Кэрролла Алиса шагнула сквозь него в Зазеркалье. Что лежит в чёрном ящике?",
        "q_en": "Attention, black box! In ancient times, this object was made of polished bronze. In folklore, vampires cast no reflection in it, and Lewis Carroll's Alice stepped through it into Wonderland. What is in the black box?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Mirror.jpg",
        "fun_fact_uz": "Ilk shisha oynalar 13-asrda Venetsiyaning Murano orolida yaratilgan bo'lib, oyna yasash siri davlat siri sifatida qattiq qo'riqlangan.",
        "fun_fact_ru": "Венецианские зеркала с острова Мурано ценились баснословно дорого, а мастерам под страхом смерти запрещалось раскрывать секрет амальгамы.",
        "fun_fact_en": "Venetian glassmakers on the island of Murano were forbidden under pain of death from leaving Venice to protect the secret of mirror-making.",
        "aliases": ["ko'zgu", "oyna", "zerkalo", "mirror", "зеркало"]
    },
    # 2: Kompas / Компас / Compass
    {
        "uz": "Kompas", "ru": "Компас", "en": "Compass",
        "distractors_uz": ["Usturlob", "Qumsoat", "Barometr"],
        "distractors_ru": ["Астролябия", "Песочные часы", "Барометр"],
        "distractors_en": ["Astrolabe", "Hourglass", "Barometer"],
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutida qadimgi Xitoyning Xan sulolasi davrida kashf etilgan to'rt buyuk ixtironing biri joylashgan. U dastlab qoshiqsimon magnit toshdan yasalgan bo'lib, 'janubga ko'rsatkich' deb nomlangan. Buyuk geografik kashfiyotlar aynan shu buyum tufayli amalga oshgan. Qora qutida nima bor?",
        "q_ru": "Внимание, чёрный ящик! В нём находится одно из четырёх великих изобретений Древнего Китая эпохи Хань. Изначально он имел форму магнитной ложки и назывался 'указателем юга'. Именно благодаря ему состоялись Великие географические открытия. Что в чёрном ящике?",
        "q_en": "Attention, black box! Inside is one of the Four Great Inventions of Ancient China. Originally shaped like a magnetized spoon on a bronze plate, it was known as the 'south-pointer'. It enabled the Age of Discovery. What is in the black box?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8e/2016_Busola.JPG",
        "fun_fact_uz": "Kompas ignasi Yerning geografik emas, magnit qutbiga yo'naladi, bu farq magnit og'ishi deb ataladi.",
        "fun_fact_ru": "Стрелка компаса указывает не на истинный географический, а на магнитный полюс Земли.",
        "fun_fact_en": "A compass needle aligns with Earth's magnetic field lines rather than true geographic north.",
        "aliases": ["kompas", "compass", "компас", "qutbnoma"]
    },
    # 3: Ko'zoynak / Очки / Eyeglasses
    {
        "uz": "Ko'zoynak", "ru": "Очки", "en": "Eyeglasses",
        "distractors_uz": ["Lupa", "Mikroskop", "Teleskop"],
        "distractors_ru": ["Лупа", "Микроскоп", "Телескоп"],
        "distractors_en": ["Magnifying glass", "Microscope", "Telescope"],
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi ushbu buyum ilk bor 13-asr oxirida Italiyada paydo bo'lgan. Uning yaratilishida Ibn al-Haysamning optika bo'yicha kashfiyotlari muhim rol o'ynagan. Petrarxa qarigan chog'ida ushbu buyum yordamida o'qishda davom etganini yozgan. Qora qutidagi buyumni ayting.",
        "q_ru": "Внимание, чёрный ящик! Этот предмет появился в Италии в конце XIII века на основе трудов арабского учёного Ибн аль-Хайсама. Поэт Петрарка писал, что в старости этот предмет вернул ему возможность читать. Что лежит в чёрном ящике?",
        "q_en": "Attention, black box! Invented in late 13th-century Italy based on Ibn al-Haytham's optics, this device allowed the elderly poet Petrarch to continue reading manuscripts. What is in the black box?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Square_sunglasses.jpg",
        "fun_fact_uz": "Dastlabki ko'zoynaklar quloqqa ilinadigan bandlarga ega bo'lmagan — ular burun ustiga qistirib taqilgan.",
        "fun_fact_ru": "Первые очки не имели дужек — их удерживали на носу (пенсне) или подносили к глазам за ручку (лорнет).",
        "fun_fact_en": "Early spectacles lacked ear temples and had to be balanced on the nose or held on a stick.",
        "aliases": ["ko'zoynak", "kozoynak", "ochki", "eyeglasses", "glasses", "spectacles", "очки"]
    },
    # 4: Qumsoat / Песочные часы / Hourglass
    {
        "uz": "Qumsoat", "ru": "Песочные часы", "en": "Hourglass",
        "distractors_uz": ["Suv soati", "Mexanik soat", "Quyosh soati"],
        "distractors_ru": ["Водяные часы", "Механические часы", "Солнечные часы"],
        "distractors_en": ["Water clock", "Mechanical clock", "Sundial"],
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum o'rta asrlarda dengiz kemalarida tezlik va vaqtni o'lchashda ajralmas vosita bo'lgan. Uning ichidagi mayda zarralar hech qachon muzlab qolmaydi va gravitatsiya tufayli bir maromda pastga to'kiladi. Vaqt o'tishi va o'lim ramzi bo'lgan buyumni toping.",
        "q_ru": "Внимание, чёрный ящик! В Средневековье этот предмет был незаменим на кораблях для замера скорости лагом и вахт. Вещество внутри него не замерзает и сыплется с постоянной скоростью под действием гравитации. Что лежит в чёрном ящике?",
        "q_en": "Attention, black box! Essential aboard sailing ships to measure nautical watches and speed, this item contains a substance that flows steadily under gravity and never freezes. An enduring symbol of time, what is in the box?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Half-hour_sand_glass_MET_ES268.jpg",
        "fun_fact_uz": "Dengiz kemalarida qumsoat ichiga qovurilgan tuxum po'chog'i yoki marmar kukuni solingan, chunki oddiy qum dengiz namligida ivib qolishi mumkin edi.",
        "fun_fact_ru": "На кораблях в песочные часы часто засыпали порошок из мрамора или толчёной скорлупы, чтобы избежать слипания от влажности.",
        "fun_fact_en": "Nautical hourglasses often used powdered marble or pulverized eggshell to prevent clumping from maritime moisture.",
        "aliases": ["qumsoat", "qum soati", "hourglass", "sandglass", "песочные часы"]
    },
    # 5: Shaxmat shohi / Шахматный король / Chess King
    {
        "uz": "Shaxmat shohi", "ru": "Шахматный король", "en": "Chess King",
        "distractors_uz": ["Shaxmat vaziri", "Shaxmat ruxi", "Shaxmat oti"],
        "distractors_ru": ["Шахматный ферзь", "Шахматная ладья", "Шахматный конь"],
        "distractors_en": ["Chess Queen", "Chess Rook", "Chess Knight"],
        "q_uz": "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum 64 katakli maydondagi eng oliy, ammo yurishi eng cheklangan figuralardan biridir. O'yinning nomi forschadan tarjima qilinganda aynan shu buyumning 'ojiz qolishi' yoki o'limini bildiradi. Qora qutida nima bor?",
        "q_ru": "Внимание, чёрный ящик! Этот предмет — ключевая, но весьма ограниченная в манёврах фигура на 64-клеточном поле. Само название игры переводится с персидского как гибель или бессилие этой фигуры. Что в чёрном ящике?",
        "q_en": "Attention, black box! Inside is the most crucial yet vulnerable piece on a 64-square battlefield. The name of the ancient game translates from Persian as 'the king is helpless'. What is in the black box?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Chess_klt45.svg",
        "fun_fact_uz": "'Shaxmat' so'zi forscha 'Shoh mot' — ya'ni 'Shoh ojiz qoldi' degan ma'nodan kelib chiqqan.",
        "fun_fact_ru": "Слово 'шахматы' происходит от персидского 'шах мат', что означает 'властитель повержен'.",
        "fun_fact_en": "The word 'checkmate' originates from the Persian phrase 'Shah mat', meaning 'the King is helpless'.",
        "aliases": ["shaxmat shohi", "shoh", "chess king", "king", "шахматный король", "король"]
    }
]

print("Script template ready.")
