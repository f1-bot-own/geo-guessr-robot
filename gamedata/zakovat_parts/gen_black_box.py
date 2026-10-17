# -*- coding: utf-8 -*-
"""
Full generator for 125 Black Box (Qora quti) questions.
Produces zakovat_001 to zakovat_125.
"""
import json
import os

RAW_ITEMS = [
    # 1: Ko'zgu
    {
        "target": ("Ko'zgu", "Зеркало", "Mirror"),
        "distractors": [
            ("Shisha qadah", "Стеклянный бокал", "Glass goblet"),
            ("Surat ramkasi", "Фоторамка", "Picture frame"),
            ("Teleskop", "Телескоп", "Telescope")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum qadimgi Misr va Xitoyda sayqallangan bronzadan yasalgan. Xalq e'tiqodlariga ko'ra, vampirlar unda aks etmaydi, Lewis Carroll asarida Alisa u orqali boshqa olamga o'tadi. Qora qutida nima bor?",
            "Внимание, чёрный ящик! В древности этот предмет делали из полированной бронзы. Вампиры в нём не отражаются, а Алиса шагнула сквозь него в Зазеркалье. Что лежит в чёрном ящике?",
            "Attention, black box! Made of polished bronze in antiquity; folklore states vampires cast no reflection in it, and Alice stepped through it into Wonderland. What is in the black box?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Mirror.jpg",
        "fact": (
            "Ilk shisha oynalar 13-asrda Venetsiyaning Murano orolida yaratilgan bo'lib, oyna siri davlat siri sifatida qattiq qo'riqlangan.",
            "Секрет венецианских зеркал охранялся под страхом смертной казни на острове Мурано.",
            "Venetian mirror-making secrets were guarded under pain of death on the island of Murano."
        ),
        "aliases": ["ko'zgu", "oyna", "zerkalo", "mirror", "зеркало"]
    },
    # 2: Kompas
    {
        "target": ("Kompas", "Компас", "Compass"),
        "distractors": [
            ("Usturlob", "Астролябия", "Astrolabe"),
            ("Qumsoat", "Песочные часы", "Hourglass"),
            ("Barometr", "Барометр", "Barometer")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: qora qutida qadimgi Xitoyning 4 buyuk ixtirosidan biri joylashgan. U dastlab magnit toshdan qoshiq shaklida yasalgan bo'lib, 'janub ko'rsatkich' deb nomlangan. Buyuk geografik kashfiyotlarga sabab bo'lgan buyumni toping.",
            "Внимание, чёрный ящик! В нём одно из четырёх великих изобретений Китая, изначально имевшее форму магнитной ложки и называвшееся 'указатель юга'. Что в чёрном ящике?",
            "Attention, black box! Inside is one of the Four Great Inventions of China, originally a magnetized spoon indicating south that enabled global sea exploration. What is it?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8e/2016_Busola.JPG",
        "fact": (
            "Kompas ignasi Yerning geografik emas, magnit qutbiga yo'naladi, bu farq magnit og'ishi deb ataladi.",
            "Стрелка компаса указывает на магнитный, а не географический полюс Земли.",
            "A compass needle points to magnetic north rather than true geographic north."
        ),
        "aliases": ["kompas", "compass", "компас", "qutbnoma"]
    },
    # 3: Ko'zoynak
    {
        "target": ("Ko'zoynak", "Очки", "Eyeglasses"),
        "distractors": [
            ("Lupa", "Лупа", "Magnifying glass"),
            ("Mikroskop", "Микроскоп", "Microscope"),
            ("Teleskop", "Телескоп", "Telescope")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu optik vosita 13-asr oxirida Italiyada Ibn al-Haysam asarlariga tayanib yaratilgan bo'lib, keksa olimlarga kitob mutolaa qilish imkonini qaytargan. Qora qutida nima bor?",
            "Внимание, чёрный ящик! Этот оптический прибор появился в Италии в XIII веке на основе трудов Ибн аль-Хайсама и вернул учёным возможность читать. Что лежит в чёрном ящике?",
            "Attention, black box! Invented in late 13th-century Italy using Ibn al-Haytham's optics, this device allowed scholars to continue reading in old age. What is in the black box?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Square_sunglasses.jpg",
        "fact": (
            "Dastlabki ko'zoynaklarda quloqqa ilinadigan bandlar bo'lmagan, ular faqat burunga qistirib taqilgan.",
            "Первые очки не имели заушников и удерживались исключительно на переносице.",
            "Early spectacles had no ear temples and were pinched onto the bridge of the nose."
        ),
        "aliases": ["ko'zoynak", "kozoynak", "ochki", "eyeglasses", "glasses", "spectacles", "очки"]
    },
    # 4: Qumsoat
    {
        "target": ("Qumsoat", "Песочные часы", "Hourglass"),
        "distractors": [
            ("Suv soati", "Водяные часы", "Water clock"),
            ("Mexanik soat", "Механические часы", "Mechanical clock"),
            ("Quyosh soati", "Солнечные часы", "Sundial")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum o'rta asrlarda dengiz kemalarida tezlik va vaqtni o'lchashda ishlatilgan. Uning ichidagi modda muzlamaydi va bir maromda pastga oqadi. Vaqt va o'lim ramzi bo'lgan buyumni toping.",
            "Внимание, чёрный ящик! Этот предмет был незаменим на кораблях для замера вахт; вещество внутри не замерзает и сыплется равномерно. Что лежит в чёрном ящике?",
            "Attention, black box! Essential aboard sailing ships to track nautical watches, this item contains a substance that never freezes and flows steadily under gravity. What is it?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Half-hour_sand_glass_MET_ES268.jpg",
        "fact": (
            "Kemalarda qumsoat ichiga marmar kukuni yoki tuxum po'chog'i solingan, chunki oddiy qum namda yopishib qolar edi.",
            "В корабельные часы засыпали порошок мрамора или скорлупы, чтобы избежать слипания от влажности.",
            "Nautical hourglasses often used marble dust or powdered eggshells to prevent damp clumping."
        ),
        "aliases": ["qumsoat", "qum soati", "hourglass", "sandglass", "песочные часы"]
    },
    # 5: Shaxmat shohi
    {
        "target": ("Shaxmat shohi", "Шахматный король", "Chess King"),
        "distractors": [
            ("Shaxmat vaziri", "Шахматный ферзь", "Chess Queen"),
            ("Shaxmat ruxi", "Шахматная ладья", "Chess Rook"),
            ("Shaxmat oti", "Шахматный конь", "Chess Knight")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum 64 katakli maydondagi eng muhim, ammo yurishi eng cheklangan figura hisoblanadi. O'yin nomi forschadan uning ojiz qolishi deb tarjima qilinadi. Qora qutida nima bor?",
            "Внимание, чёрный ящик! Главная, но ограниченная в движениях фигура на 64 клетках; само название игры переводится с персидского как её поражение. Что в чёрном ящике?",
            "Attention, black box! Inside is the most crucial yet vulnerable piece on a 64-square battlefield. The name of the ancient game translates from Persian as 'the king is helpless'. What is it?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Chess_klt45.svg",
        "fact": (
            "'Shaxmat' so'zi forscha 'Shoh mot' — ya'ni 'Shoh ojiz qoldi' degan ma'nodan kelib chiqqan.",
            "Слово 'шахматы' происходит от персидского 'шах мат' — властитель повержен.",
            "The term checkmate derives from Persian 'Shah mat', meaning 'the King is helpless'."
        ),
        "aliases": ["shaxmat shohi", "shoh", "chess king", "king", "шахматный король", "король"]
    },
    # 6: Sovun
    {
        "target": ("Sovun", "Мыло", "Soap"),
        "distractors": [
            ("Shampun", "Шампунь", "Shampoo"),
            ("Parfyum", "Духи", "Perfume"),
            ("Tish pastasi", "Зубная паста", "Toothpaste")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu moddani miloddan avvalgi 2800-yilda Bobilda yog' va kuldan tayyorlashgan. Rim afsonasi uning nomini Sapo tog'i bilan bog'laydi. Gigiyenaning asosi bo'lgan vositani toping.",
            "Внимание, чёрный ящик! Продукт, сваренный в Вавилоне из жира и золы; легенда связывает его название с римской горой Сапо. Что лежит в чёрном ящике?",
            "Attention, black box! Boiled in ancient Babylon from animal fats and wood ash, legend ties its name to Mount Sapo. The bedrock of hygiene, what is in the box?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Handmade_soap_cropped_and_simplified.jpg",
        "fact": (
            "Sovun molekulasining bir uchi gidrofil (suvsevar), ikkinchi uchi gidrofob (yog'sevar) bo'lib, kirlarni yuvadi.",
            "Молекулы мыла гидрофильны с одного конца и гидрофобны с другого, что позволяет им связывать жир с водой.",
            "Soap molecules have hydrophilic heads and lipophilic tails that trap grease and wash clean."
        ),
        "aliases": ["sovun", "milo", "soap", "мыло"]
    },
    # 7: Gugurt
    {
        "target": ("Gugurt", "Спички", "Matches"),
        "distractors": [
            ("Zajigalka", "Зажигалка", "Lighter"),
            ("Chaqmoqtosh", "Кремень", "Flint"),
            ("Sham", "Свеча", "Candle")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: 1826-yilda ingliz dorishunosi John Walker tomonidan tasodifan kashf etilgan, ishqalanish natijasida yonuvchi kimyoviy boshli yog'och cho'p qora qutida joylashgan. Qora qutida nima bor?",
            "Внимание, чёрный ящик! В 1826 году химик Джон Уокер случайно изобрёл этот предмет, вспыхивающий от трения о шероховатую поверхность. Что в чёрном ящике?",
            "Attention, black box! Accidentally invented in 1826 by English pharmacist John Walker when a friction-coated stick scraped across stone and ignited. What is in the black box?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/60/Friction_d%27une_allumette.jpg",
        "fact": (
            "Shvetsiyada xavfsiz gugurt yaratilgan bo'lib, unda zaharli oq fosfor o'rniga qizil fosfor ishlatilgan.",
            "Шведские безопасные спички заменили ядовитый белый фосфор красным.",
            "Swedish safety matches replaced lethal white phosphorus with harmless red phosphorus."
        ),
        "aliases": ["gugurt", "spichka", "spichki", "matches", "match", "спички"]
    },
    # 8: Pochta markasi
    {
        "target": ("Pochta markasi", "Почтовая марка", "Postage stamp"),
        "distractors": [
            ("Konvert", "Конверт", "Envelope"),
            ("Otkritka", "Открытка", "Postcard"),
            ("Kvitansiya", "Квитанция", "Receipt")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: 1840-yilda Buyuk Britaniyada Rowland Hill islohoti natijasida paydo bo'lgan 'Qora penni' deb nomlangan qog'oz belgisi qora qutida. Qora qutidagi buyumni toping.",
            "Внимание, чёрный ящик! Клейкий знак почтовой оплаты 1840 года, вошедший в историю как 'Чёрный пенни'. Что лежит в чёрном ящике?",
            "Attention, black box! Introduced in Britain in 1840 under Rowland Hill as the 'Penny Black', transforming communications. What is in the black box?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Nicaragua1_1913.jpg",
        "fact": (
            "Buyuk Britaniya dunyoda markasida o'z davlati nomini yozmaydigan yagona davlatdir.",
            "Великобритания — единственная страна, не указывающая своё название на почтовых марках.",
            "Great Britain is the only country exempt from printing its name on its postage stamps."
        ),
        "aliases": ["pochta markasi", "marka", "postage stamp", "stamp", "почтовая марка", "марка"]
    },
    # 9: Sham
    {
        "target": ("Sham", "Свеча", "Candle"),
        "distractors": [
            ("Kerosin chiroq", "Керосиновая лампа", "Kerosene lamp"),
            ("Mash'al", "Факел", "Torch"),
            ("Fonar", "Фонарь", "Lantern")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: Michael Faraday uning yonishi misolida tabiatning barcha fizik va kimyoviy qonuniyatlarini tushuntirib bergan, qadimda mum va yog'dan yasalgan yoritish vositasini toping.",
            "Внимание, чёрный ящик! Источник света, на примере горения которого Майкл Фарадей объяснил фундаментальные законы природы в знаменитых рождественских лекциях. Что в чёрном ящике?",
            "Attention, black box! The illumination source whose combustion Michael Faraday used to illustrate all core chemical laws in famous lectures. What is in the black box?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/aa/LA2_Skultuna_kontorsljusstake.jpg",
        "fact": (
            "1830-yilda neftdan parafin ajratib olingach, shamlar arzonlashdi va tutun chiqarmaydigan bo'ldi.",
            "Парафин, полученный из нефти в 1830 году, сделал свечи дешёвыми и некоптящими.",
            "Paraffin wax discovered in 1830 made candles affordable and virtually soot-free."
        ),
        "aliases": ["sham", "svecha", "candle", "свеча"]
    },
    # 10: Choy
    {
        "target": ("Choy", "Чай", "Tea"),
        "distractors": [
            ("Qahva", "Кофе", "Coffee"),
            ("Kakao", "Какао", "Cocoa"),
            ("Maté", "Мате", "Mate")
        ],
        "q": (
            "Hurmatli bilimdonlar, diqqat qiling: miloddan avvalgi 2737-yilda Xitoy imperatori Shen Nung qaynayotgan suviga daraxt barglari tushishi bilan kashf etgan, 1773-yilda Bostonda inqilobga sabab bo'lgan o'simlik barglari qora qutida. Bu nima?",
            "Внимание, чёрный ящик! Листья растения, открытые императором Шэнь-нуном в кипящей воде; протест из-за них в Бостоне в 1773 году дал старт Американской революции. Что в чёрном ящике?",
            "Attention, black box! Discovered when wild leaves drifted into Emperor Shennong's boiling kettle; its taxation catalyzed the Boston Tea Party in 1773. What is in the box?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Longjing_tea_steeping_in_gaiwan.jpg",
        "fact": (
            "Qora, yashil, oq choylar barchasi bitta o'simlik — Camellia sinensis barglaridan tayyorlanadi.",
            "Все виды чая получают с одного растения — Camellia sinensis, отличие лишь в ферментации.",
            "Black, green, and white teas all come from the same single plant species, Camellia sinensis."
        ),
        "aliases": ["choy", "chay", "tea", "чай"]
    }
]

print(f"Base items count: {len(RAW_ITEMS)}")
