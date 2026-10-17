# -*- coding: utf-8 -*-
"""
Generator for Black Box questions: Part 1 (1 to 125).
"""
import json
import os

ITEMS_1_TO_65 = [
    # 1: Ko'zgu
    (
        "Ko'zgu", "Зеркало", "Mirror",
        ["Shisha qadah", "Surat ramkasi", "Teleskop"],
        ["Стеклянный бокал", "Фоторамка", "Телескоп"],
        ["Glass goblet", "Picture frame", "Telescope"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum qadimgi Misr va Xitoyda sayqallangan bronzadan yasalgan. Xalq e'tiqodlariga ko'ra, vampirlar unda o'z aksini ko'ra olmaydi, Lewis Carroll asarida esa Alisa uning ortidagi mo''jizalar olamiga tushib qoladi. Qora qutidagi buyumni toping.",
        "Внимание, чёрный ящик! В древности этот предмет изготавливали из полированной бронзы. Согласно поверьям, вампиры не отражаются в нём, а героиня Льюиса Кэрролла Алиса шагнула сквозь него в Зазеркалье. Что лежит в чёрном ящике?",
        "Attention, black box! In ancient times, this object was made of polished bronze. In folklore, vampires cast no reflection in it, and Lewis Carroll's Alice stepped through it into Wonderland. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/5/52/Mirror.jpg",
        "Ilk shisha oynalar 13-asrda Venetsiyaning Murano orolida yaratilgan bo'lib, oyna yasash siri davlat siri sifatida qattiq qo'riqlangan.",
        "Венецианские зеркала с острова Мурано ценились баснословно дорого, а мастерам под страхом смерти запрещалось раскрывать секрет амальгамы.",
        "Venetian glassmakers on the island of Murano were forbidden under pain of death from leaving Venice to protect the secret of mirror-making.",
        ["ko'zgu", "oyna", "zerkalo", "mirror", "зеркало"]
    ),
    # 2: Kompas
    (
        "Kompas", "Компас", "Compass",
        ["Usturlob", "Qumsoat", "Barometr"],
        ["Астролябия", "Песочные часы", "Барометр"],
        ["Astrolabe", "Hourglass", "Barometer"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutida qadimgi Xitoyning Xan sulolasi davrida kashf etilgan to'rt buyuk ixtironing biri joylashgan. U dastlab qoshiqsimon magnit toshdan yasalgan bo'lib, 'janubga ko'rsatkich' deb nomlangan. Buyuk geografik kashfiyotlar aynan shu buyum tufayli amalga oshgan. Qora qutida nima bor?",
        "Внимание, чёрный ящик! В нём находится одно из четырёх великих изобретений Древнего Китая эпохи Хань. Изначально он имел форму магнитной ложки и назывался 'указателем юга'. Именно благодаря ему состоялись Великие географические открытия. Что в чёрном ящике?",
        "Attention, black box! Inside is one of the Four Great Inventions of Ancient China. Originally shaped like a magnetized spoon on a bronze plate, it was known as the 'south-pointer'. It enabled the Age of Discovery. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/8/8e/2016_Busola.JPG",
        "Kompas ignasi Yerning geografik emas, magnit qutbiga yo'naladi, bu farq magnit og'ishi deb ataladi.",
        "Стрелка компаса указывает не на истинный географический, а на магнитный полюс Земли.",
        "A compass needle aligns with Earth's magnetic field lines rather than true geographic north.",
        ["kompas", "compass", "компас", "qutbnoma"]
    ),
    # 3: Ko'zoynak
    (
        "Ko'zoynak", "Очки", "Eyeglasses",
        ["Lupa", "Mikroskop", "Teleskop"],
        ["Лупа", "Микроскоп", "Телескоп"],
        ["Magnifying glass", "Microscope", "Telescope"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi ushbu buyum ilk bor 13-asr oxirida Italiyada paydo bo'lgan. Uning yaratilishida Ibn al-Haysamning optika bo'yicha kashfiyotlari muhim rol o'ynagan. Petrarxa qarigan chog'ida ushbu buyum yordamida o'qishda davom etganini yozgan. Qora qutidagi buyumni ayting.",
        "Внимание, чёрный ящик! Этот предмет появился в Италии в конце XIII века на основе трудов арабского учёного Ибн аль-Хайсама. Поэт Петрарка писал, что в старости этот предмет вернул ему возможность читать. Что лежит в чёрном ящике?",
        "Attention, black box! Invented in late 13th-century Italy based on Ibn al-Haytham's optics, this device allowed the elderly poet Petrarch to continue reading manuscripts. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/1/1b/Square_sunglasses.jpg",
        "Dastlabki ko'zoynaklar quloqqa ilinadigan bandlarga ega bo'lmagan — ular burun ustiga qistirib taqilgan.",
        "Первые очки не имели дужек — их удерживали на носу (пенсне) или подносили к глазам за ручку (лорнет).",
        "Early spectacles lacked ear temples and had to be balanced on the nose or held on a stick.",
        ["ko'zoynak", "kozoynak", "ochki", "eyeglasses", "glasses", "spectacles", "очки"]
    ),
    # 4: Qumsoat
    (
        "Qumsoat", "Песочные часы", "Hourglass",
        ["Suv soati", "Mexanik soat", "Quyosh soati"],
        ["Водяные часы", "Механические часы", "Солнечные часы"],
        ["Water clock", "Mechanical clock", "Sundial"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum o'rta asrlarda dengiz kemalarida tezlik va vaqtni o'lchashda ajralmas vosita bo'lgan. Uning ichidagi mayda zarralar hech qachon muzlab qolmaydi va gravitatsiya tufayli bir maromda pastga to'kiladi. Vaqt o'tishi va o'lim ramzi bo'lgan buyumni toping.",
        "Внимание, чёрный ящик! В Средневековье этот предмет был незаменим на кораблях для замера скорости лагом и вахт. Вещество внутри него не замерзает и сыплется с постоянной скоростью под действием гравитации. Что лежит в чёрном ящике?",
        "Attention, black box! Essential aboard sailing ships to measure nautical watches and speed, this item contains a substance that flows steadily under gravity and never freezes. An enduring symbol of time, what is in the box?",
        "https://upload.wikimedia.org/wikipedia/commons/9/9e/Half-hour_sand_glass_MET_ES268.jpg",
        "Dengiz kemalarida qumsoat ichiga qovurilgan tuxum po'chog'i yoki marmar kukuni solingan, chunki oddiy qum dengiz namligida ivib qolishi mumkin edi.",
        "На кораблях в песочные часы часто засыпали порошок из мрамора или толчёной скорлупы, чтобы избежать слипания от влажности.",
        "Nautical hourglasses often used powdered marble or pulverized eggshell to prevent clumping from maritime moisture.",
        ["qumsoat", "qum soati", "hourglass", "sandglass", "песочные часы"]
    ),
    # 5: Shaxmat shohi
    (
        "Shaxmat shohi", "Шахматный король", "Chess King",
        ["Shaxmat vaziri", "Shaxmat ruxi", "Shaxmat oti"],
        ["Шахматный ферзь", "Шахматная ладья", "Шахматный конь"],
        ["Chess Queen", "Chess Rook", "Chess Knight"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu buyum 64 katakli maydondagi eng oliy, ammo yurishi eng cheklangan figuralardan biridir. O'yinning nomi forschadan tarjima qilinganda aynan shu buyumning 'ojiz qolishi' yoki o'limini bildiradi. Qora qutida nima bor?",
        "Внимание, чёрный ящик! Этот предмет — ключевая, но весьма ограниченная в манёврах фигура на 64-клеточном поле. Само название игры переводится с персидского как гибель или бессилие этой фигуры. Что в чёрном ящике?",
        "Attention, black box! Inside is the most crucial yet vulnerable piece on a 64-square battlefield. The name of the ancient game translates from Persian as 'the king is helpless'. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/4/42/Chess_klt45.svg",
        "'Shaxmat' so'zi forscha 'Shoh mot' — ya'ni 'Shoh ojiz qoldi' degan ma'nodan kelib chiqqan.",
        "Слово 'шахматы' происходит от персидского 'шах мат', что означает 'властитель повержен'.",
        "The word 'checkmate' originates from the Persian phrase 'Shah mat', meaning 'the King is helpless'.",
        ["shaxmat shohi", "shoh", "chess king", "king", "шахматный король", "король"]
    ),
    # 6: Sovun
    (
        "Sovun", "Мыло", "Soap",
        ["Shampun", "Parfyum", "Tish pastasi"],
        ["Шампунь", "Духи", "Зубная паста"],
        ["Shampoo", "Perfume", "Toothpaste"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu moddani qadimgi bobilliklar miloddan avvalgi 2800-yillarda yog' va kulni qaynatib tayyorlashgan. Rim afsonasiga ko'ra, u Sapo tog'idagi qurbonlik hayvonlari yog'ining yomg'ir suvi bilan daryoga oqishi natijasida kashf qilingan. Gigiyena inqilobiga sabab bo'lgan buyumni toping.",
        "Внимание, чёрный ящик! В Древнем Вавилоне за 2800 лет до н.э. этот продукт варили из жира и древесной золы. Легенда связывает его латинское название с горой Сапо в Риме. Без него была бы невозможна современная гигиена. Что в чёрном ящике?",
        "Attention, black box! Made by Babylonians around 2800 BC by boiling animal fats with wood ash, legend ties its Latin name to Mount Sapo. The bedrock of human hygiene, what is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/9/9b/Handmade_soap_cropped_and_simplified.jpg",
        "Sovun molekulalarining bir uchi suvni (gidrofil), ikkinchi uchi yog'ni (gidrofob) o'ziga tortadi, bu esa mikroblarni yuvib ketish imkonini beradi.",
        "Молекулы мыла гидрофильны с одного конца и гидрофобны с другого, что позволяет им связывать жир и смывать бактерии водой.",
        "Soap molecules possess a hydrophilic head and hydrophobic tail, trapping lipid-coated bacteria and washing them away with water.",
        ["sovun", "milo", "soap", "мыло"]
    ),
    # 7: Gugurt
    (
        "Gugurt", "Спички", "Matches",
        ["Zajigalka", "Chaqmoqtosh", "Sham"],
        ["Зажигалка", "Кремень", "Свеча"],
        ["Lighter", "Flint", "Candle"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi buyum 1826-yilda ingliz kimyogari John Walker tomonidan tasodifan ixtiro qilingan. U kimyoviy moddani yog'och cho'pga surkab aralashtirayotganida ishqalanishdan olov paydo bo'lgan. Qora qutida nima bor?",
        "Внимание, чёрный ящик! В 1826 году английский аптекарь Джон Уокер случайно изобрёл этот предмет, когда палочка с химикатами вспыхнула от трения о пол. Что лежит в чёрном ящике?",
        "Attention, black box! In 1826, English chemist John Walker accidentally invented this item when a wooden stick coated with chemicals scraped across the floor and ignited. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/6/60/Friction_d%27une_allumette.jpg",
        "Dastlabki gugurtlar xavfli oq fosfordan tayyorlangan. Zamonaviy 'xavfsiz gugurt'ni shved kimyogari Johan Lundström 1855-yilda qizil fosfor yordamida yaratgan.",
        "Шведские 'безопасные спички' заменили смертельно опасный белый фосфор красным, за что Швеция стала мировым лидером их производства.",
        "Early matches used toxic white phosphorus before Swedish chemist Johan Lundström developed safety matches with red phosphorus in 1855.",
        ["gugurt", "spichka", "spichki", "matches", "match", "спички", "спичка"]
    ),
    # 8: Pochta markasi
    (
        "Pochta markasi", "Почтовая марка", "Postage stamp",
        ["Konvert", "Otkritka", "Kvitansiya"],
        ["Конверт", "Открытка", "Квитанция"],
        ["Envelope", "Postcard", "Receipt"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu kichkina qog'oz parchasi 1840-yilda Buyuk Britaniyada Rowland Hill islohoti natijasida paydo bo'lgan. Unda qirolicha Viktoriyaning tasviri bo'lgan va u 'Qora penni' nomi bilan tarixga kirgan. Qora qutidagi buyum nima?",
        "Внимание, чёрный ящик! Этот миниатюрный бумажный знак появился в Великобритании в 1840 году благодаря Роуленду Хиллу. На нём был профиль королевы Виктории, и он вошёл в историю под именем 'Чёрный пенни'. Что лежит в чёрном ящике?",
        "Attention, black box! Introduced in Great Britain in 1840 through Rowland Hill's postal reform, this small paper receipt featured Queen Victoria's profile and was dubbed the 'Penny Black'. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/b/b6/Nicaragua1_1913.jpg",
        "Buyuk Britaniya dunyoda markalarida o'z davlati nomini yozmaydigan yagona mamlakatdir, chunki u birinchi bo'lib markani joriy qilgan.",
        "Великобритания — единственная страна мира, освобождённая от обязанности указывать своё название на марках, так как она выпустила их первой.",
        "The United Kingdom is the only country exempt from printing its name on postage stamps because it was the first to issue them.",
        ["pochta markasi", "marka", "postage stamp", "stamp", "почтовая марка", "марка"]
    ),
    # 9: Sham
    (
        "Sham", "Свеча", "Candle",
        ["Kerosin chiroq", "Mash'al", "Fonar"],
        ["Керосиновая лампа", "Факел", "Фонарь"],
        ["Kerosene lamp", "Torch", "Lantern"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi buyum asrlar davomida asalari mumi yoki hayvon yog'idan yasalgan. Michael Faraday London Qirollik institutida Rojdestvo ma'ruzalarida aynan shu buyumning yonishi misolida kimyo va fizikaning barcha qonuniyatlarini tushuntirib bergan. Qora qutida nima bor?",
        "Внимание, чёрный ящик! На протяжении тысячелетий этот предмет делали из пчелиного воска или сала. Майкл Фарадей прочитал знаменитый курс лекций 'История свечи', объяснив на его примере все законы химии и горения. Что в чёрном ящике?",
        "Attention, black box! Made for millennia from beeswax or tallow, Michael Faraday used this humble illumination source to explain all core chemical and physical laws in 'The Chemical History of a Candle'. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/a/aa/LA2_Skultuna_kontorsljusstake.jpg",
        "O'rta asrlarda cherkovlarda faqat sof asalari mumi shamlari ishlatilgan, oddiy xalq esa tutaydigan va hid chiqaradigan hayvon yog'i shamlaridan foydalangan.",
        "В старину восковые свечи были роскошью знати и церквей, а бедняки жгли коптящие сальные свечи из животного жира.",
        "Paraffin wax, discovered in 1830 from petroleum, revolutionized candle-making by providing an odorless, clean-burning, inexpensive fuel.",
        ["sham", "svecha", "candle", "свеча"]
    ),
    # 10: Choy
    (
        "Choy", "Чай", "Tea",
        ["Qahva", "Kakao", "Maté"],
        ["Кофе", "Какао", "Мате"],
        ["Coffee", "Cocoa", "Mate"],
        "Hurmatli bilimdonlar, diqqat qiling: rivoyatga ko'ra, miloddan avvalgi 2737-yilda Xitoy imperatori Shen Nung qaynayotgan suv solingan qozonga shamol olib kelgan yovvoyi daraxt barglari tushishi natijasida bu ichimlikni kashf etgan. 1773-yilda Bostonda bo'lib o'tgan 'ichimlik ziyofati' esa Amerika inqilobining boshlanishiga turtki bo'lgan. Qora qutida nima bor?",
        "Внимание, чёрный ящик! По преданию, в 2737 году до н.э. китайский император Шэнь-нун случайно открыл этот напиток, когда листья упали в кипящий котёл. А в 1773 году с 'чаепития' в Бостоне началась Американская революция. Что в чёрном ящике?",
        "Attention, black box! According to Chinese legend, Emperor Shennong discovered this drink in 2737 BC when wild leaves fell into boiling water. In 1773, a famous 'Party' involving this commodity in Boston harbor sparked the American Revolution. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/d/d3/Longjing_tea_steeping_in_gaiwan.jpg",
        "Qora, yashil, oq va ulun choylari bir xil o'simlik — Camellia sinensis barglaridan tayyorlanadi, farq faqat fermentatsiya darajasida.",
        "Все виды чая (чёрный, зелёный, белый, улун) собирают с одного и того же растения — Camellia sinensis, отличие лишь в ферментации.",
        "All true teas (black, green, white, oolong) come from the same plant species, Camellia sinensis; the differences stem entirely from processing and oxidation.",
        ["choy", "chay", "tea", "чай"]
    ),
    # 11: Qahva donasi
    (
        "Qahva donasi", "Кофейное зерно", "Coffee bean",
        ["Makkajo'xori donasi", "Kashan yong'og'i", "Kofe kukuni"],
        ["Кукурузное зерно", "Кешью", "Растворимый кофе"],
        ["Corn kernel", "Cashew", "Cocoa bean"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu o'simlik mevasining tetiklashtiruvchi xususiyatini 9-asrda Efiopiyada Kaldi ismli cho'pon o'z echkilarining bu buta mevasini yegach g'ayritabiiy sakray boshlaganidan bilib qolgan. Yaman orqali butun dunyoga tarqalgan ushbu mahsulotni toping.",
        "Внимание, чёрный ящик! Тонизирующие свойства этого растения открыл в IX веке эфиопский пастух Калди, заметив, что его козы скачут без устали, наевшись красных ягод. Через суфийские обители Йемена продукт покорил мир. Что лежит в чёрном ящике?",
        "Attention, black box! The stimulating effects of this plant were noticed in 9th-century Ethiopia by the goatherd Kaldi, whose goats danced energized after eating red berries. Spreading via Yemeni Sufi monasteries, it conquered the world. What is in the box?",
        "https://upload.wikimedia.org/wikipedia/commons/c/c5/Roasted_coffee_beans.jpg",
        "Botanika nuqtai nazaridan qahva donasi aslida loviya yoki dukkakli emas, balki qahva mevasining (gilosining) danagidir.",
        "С ботанической точки зрения кофейные зерна — вовсе не бобы, а косточки внутри красных ягод кофейного дерева.",
        "Botanically, coffee beans are not true beans, but rather the pitted seeds of the red fruit known as coffee cherries.",
        ["qahva donasi", "qahva", "kofe", "coffee bean", "coffee", "кофейное зерно", "кофе"]
    ),
    # 12: Ipak
    (
        "Ipak", "Шёлк", "Silk",
        ["Paxta tolasi", "Zig'ir mato", "Jun"],
        ["Хлопковая нить", "Льняная ткань", "Шерсть"],
        ["Cotton fiber", "Linen fabric", "Wool"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi bu qimmatbaho matoning tayyorlanish sirini qadimgi Xitoyda oshkor qilgan kishi o'lim jazosiga hukm qilingan. Afsonaga ko'ra, imperatritsa Ley Szu choy ichib o'tirganida chashkaga tut daraxtidan pilla tushib erigan va nafis ip hosil bo'lgan. Qora qutida nima bor?",
        "Внимание, чёрный ящик! В Древнем Китае за разглашение секрета изготовления этого материала карали смертной казнью. По легенде, императрица Лэй Цзу пила чай в саду, когда кокон упал в горячую чашку и распустился тончайшей нитью. Что в чёрном ящике?",
        "Attention, black box! In ancient China, revealing the secret production of this fabric was punishable by death. Legend says Empress Leizu discovered it when a cocoon fell into her hot tea and unwound into lustrous fibers. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/2/2e/Silk_raw_01a.jpg",
        "Bitta ipak pillasidan 1000 metrgacha uzluksiz ipak tolasi ajratib olinishi mumkin.",
        "Из одного кокона шелкопряда можно размотать непрерывную шёлковую нить длиной до километра.",
        "A single silkworm cocoon can yield a continuous thread of raw silk measuring up to 900–1,000 meters in length.",
        ["ipak", "sholk", "silk", "шёлк", "шелк"]
    ),
    # 13: Paxta
    (
        "Paxta", "Хлопок", "Cotton",
        ["Zig'ir", "Ipak", "Sintetik tola"],
        ["Лён", "Шёлк", "Синтепон"],
        ["Linen", "Silk", "Synthetic fiber"],
        "Hurmatli bilimdonlar, diqqat qiling: qadimgi yunon tarixchisi Gerodot Hindistonda 'daraxtlarda qo'y juni o'sadi, mahalliy xalq undan kiyim to'qiydi' deb hayratlangan. O'zbekistonda u azaldan 'oq oltin' deb ulug'langan. Qora qutida nima bor?",
        "Внимание, чёрный ящик! Древнегреческий историк Геродот писал об Индии, что там 'на деревьях растёт шерсть, превосходящая овечью, из которой ткут одежды'. В Центральной Азии его называют 'белым золотом'. Что в чёрном ящике?",
        "Attention, black box! The Greek historian Herodotus marveled that in India, 'trees produce a wool excelling in beauty that of sheep, which locals weave into clothes.' In Uzbekistan, it is called 'white gold.' What is in the box?",
        "https://upload.wikimedia.org/wikipedia/commons/8/83/Cotton_plant.jpg",
        "Paxta tolasi deyarli 90% sof sellyulozadan iborat bo'lib, u suvni o'z og'irligidan 27 baravar ko'p shimib olish qobiliyatiga ega.",
        "Волокно хлопка состоит из чистой целлюлозы почти на 90% и способно впитывать влагу в объёме, в 27 раз превышающем собственный вес.",
        "Cotton is nearly 90% pure cellulose, making it exceptionally soft, breathable, and capable of absorbing 27 times its weight in water.",
        ["paxta", "oq oltin", "xlopok", "cotton", "хлопок"]
    ),
    # 14: Taqa
    (
        "Taqa", "Подкова", "Horseshoe",
        ["Egar", "Jilov", "Uzangi"],
        ["Седло", "Уздечка", "Стремя"],
        ["Saddle", "Bridle", "Stirrup"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi temir buyum ot tuyog'ini toshloq yo'llarda yemirilishdan saqlash uchun o'ylab topilgan. Ko'plab xalqlarda, agar u yo'ldan topilsa yoki eshik tepasiga osilsa, xonadonga omad va baxt keltiradi deb ishoniladi. Qora qutida nima bor?",
        "Внимание, чёрный ящик! Этот металлический предмет защищает копыта коней от стирания. Во многих культурах существует поверье, что найденный на дороге и прибитый над дверью, он приносит в дом удачу и счастье. Что в чёрном ящике?",
        "Attention, black box! Invented to protect horses' hooves from wear on rocky terrain, folklore worldwide holds that finding one and hanging it above a door brings prosperity and good fortune. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/a/a2/Horseshoe_old.jpg",
        "Taqa eshikka uchlari yuqoriga qaratib osilsa, go'yo kosadek omadni to'playdi, uchlari pastga qarasa, yovuz kuchlardan himoya qiladi deb hisoblangan.",
        "По поверью, подкову вешают концами вверх, чтобы дом был 'полной чашей', или концами вниз — чтобы отгонять зло.",
        "Tradition states a horseshoe hung ends up holds good luck inside like a cup, while hung ends down pours protection over the doorway.",
        ["taqa", "podkova", "horseshoe", "подкова"]
    ),
    # 15: Qo'ng'iroq
    (
        "Qo'ng'iroq", "Колокольчик", "Bell",
        ["Baraban", "Truba", "Dovul"],
        ["Барабан", "Труба", "Гонг"],
        ["Drum", "Trumpet", "Gong"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi ushbu musiqa va signal vositasi maktablarda dars boshlanishi va tugashini bildiradi. Fiziolog Ivan Pavlov o'zining shartli reflekslar bo'yicha mashhur tajribalarida aynan shu buyum tovushidan foydalangan. Qora qutidagi buyumni toping.",
        "Внимание, чёрный ящик! Этот предмет оповещает школьников о начале урока, а академик Иван Павлов в своих классических опытах по изучению условных рефлексов у собак использовал именно его звучание. Что лежит в чёрном ящике?",
        "Attention, black box! Announcing the start and end of classes in schools, physiologist Ivan Pavlov used the acoustic chime of this object in his seminal conditioned reflex experiments with dogs. What is in the box?",
        "https://upload.wikimedia.org/wikipedia/commons/9/9f/Small_brass_bell.jpg",
        "Moskva Kremlidagi 'Podsho qo'ng'iroq' (Tsar-kolokol) dunyodagi eng og'ir (200 tonnadan ortiq) qo'ng'iroq bo'lib, u biror marta ham chalinmagan.",
        "Царь-колокол в Московском Кремле весит свыше 200 тонн и является самым большим в мире, однако в него никогда не звонили.",
        "The Tsar Bell in the Moscow Kremlin, weighing over 200 metric tons, is the largest bell in the world, though it was cracked before ever ringing.",
        ["qo'ng'iroq", "qongiroq", "kolokol", "kolokolchik", "bell", "колокол", "колокольчик"]
    ),
    # 16: Termometr
    (
        "Termometr", "Термометр", "Thermometer",
        ["Barometr", "Gigrometr", "Tonometr"],
        ["Барометр", "Гигрометр", "Тонометр"],
        ["Barometer", "Hygrometer", "Sphygmomanometer"],
        "Hurmatli bilimdonlar, diqqat qiling: qora qutidagi o'lchov asbobining ilk prototipini 1592-yilda Galileo Galiley 'termoskop' nomi bilan yaratgan. Keyinchalik Daniel Farengeyt va Anders Selsiy unga o'z shkalalarini kiritishgan. Kasal bo'lganimizda haroratni o'lchaydigan asbobni toping.",
        "Внимание, чёрный ящик! Прообраз этого прибора под названием 'термоскоп' создал Галилео Галилей в 1592 году. Позже Фаренгейт и Цельсий создали для него шкалы. Мы берем его в руки при первой простуде. Что в чёрном ящике?",
        "Attention, black box! Galileo Galilei devised its earliest prototype, the thermoscope, in 1592. Later calibrated by Fahrenheit and Celsius with numerical scales, we reach for it at the first sign of fever. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/6/67/Mercury_thermometer.jpg",
        "Selsiy dastlab o'z shkalasida suvning qaynash haroratini 0 daraja, muzlashini esa 100 daraja deb belgilagan edi; uning o'limidan keyin shkala teskarisiga o'girilgan.",
        "Изначально Цельсий назначил 0 градусов точке кипения воды, а 100 градусов — точке замерзания льда. Лишь позже шкалу перевернули.",
        "Anders Celsius originally set 0 degrees as the boiling point of water and 100 degrees as the freezing point; it was inverted after his death.",
        ["termometr", "gradusnik", "thermometer", "термометр", "градусник"]
    ),
    # 17: Kalit
    (
        "Kalit", "Ключ", "Key",
        ["Qulf", "Zanjir", "Muhr"],
        ["Замок", "Цепь", "Печать"],
        ["Lock", "Chain", "Seal"],
        "Hurmatli bilimdonlar, diqqat qiling: qadimgi Rimda ikki yuzli xudo Yanus aynan shu buyum bilan tasvirlangan. Rim papasi va Vatikan gerbida uning tilla va kumush rangli ikkita nusxasi tasvirlangan bo'lib, ular jannat eshiklarini ochuvchi ramz hisoblanadi. Qora qutida nima bor?",
        "Внимание, чёрный ящик! В Древнем Риме двуликий бог Янус изображался держащим этот предмет. На гербе Ватикана скрещены два таких предмета (золотой и серебряный), символизирующие власть отверзать врата Небес. Что в чёрном ящике?",
        "Attention, black box! In ancient Rome, the two-faced god Janus held this item. On the coat of arms of the Vatican, two of them—one gold and one silver—represent the authority to unlock the Kingdom of Heaven. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/7/71/Antique_key.jpg",
        "Qadimgi Misrda kalitlar yog'ochdan yasalgan bo'lib, uzunligi yarim metrgacha yetgan va ularni yelkada ko'tarib yurishgan.",
        "В Древнем Египте ключи делали из дерева и они достигали полуметра в длину, поэтому их носили на плече.",
        "Ancient Egyptian wooden pin tumbler keys were so massive (often up to two feet long) that servants carried them over their shoulders.",
        ["kalit", "klyuch", "key", "ключ"]
    ),
    # 18: Avtoruchka
    (
        "Avtoruchka", "Перьевая ручка", "Fountain pen",
        ["Qalam", "Bo'r", "Marker"],
        ["Карандаш", "Мел", "Маркер"],
        ["Pencil", "Chalk", "Marker"],
        "Hurmatli bilimdonlar, diqqat qiling: 1884-yilda sug'urta agenti Lewis Waterman muhim shartnomani imzolash paytida siyoh to'kilib ketib, mijozni boy bergach, siyohni o'zida saqlaydigan va kapillyar naychali ushbu yozuv asbobini patentlagan. Qora qutidagi buyumni toping.",
        "Внимание, чёрный ящик! В 1884 году страховой маклер Льюис Уотерман упустил выгодный контракт из-за потекших чернил, после чего запатентовал этот надёжный пишущий инструмент с капиллярным резервуаром. Что в чёрном ящике?",
        "Attention, black box! In 1884, after losing a lucrative client due to a leaky quill ruining an insurance contract, Lewis Waterman patented this reliable writing instrument featuring a capillary feed reservoir. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/6/64/Fountain_pen_writing.jpg",
        "1943-yilda venger jurnalisti Laslo Biro avtoruchkaning yanada qulayroq turi — sharikli ruchkani (avtoruchka muqobilini) yaratdi.",
        "В 1943 году венгерский журналист Ласло Биро изобрёл шариковую ручку, чернила в которой не сохли и не вытекали в самолётах.",
        "The ballpoint pen was later perfected by László Bíró in 1938 to prevent smudging and leakage at high atmospheric flight altitudes.",
        ["avtoruchka", "ruchka", "fountain pen", "pen", "перьевая ручка", "ручка"]
    ),
    # 19: Qalam
    (
        "Qalam", "Карандаш", "Pencil",
        ["Ruchka", "Bo'yoq cho'tkasi", "Sirkul"],
        ["Ручка", "Кисть", "Циркуль"],
        ["Pen", "Paintbrush", "Compass"],
        "Hurmatli bilimdonlar, diqqat qiling: 1564-yilda Angliyaning Kamberlend grafligida qora rangli g'alati ma'dan koni topiladi. Cho'ponlar dastlab undan qo'ylarni belgilashda foydalanishgan. Keyinchalik u yog'och qobiqqa o'ralib, dunyodagi eng mashhur yozuv va chizmachilik quroliga aylandi. Qora qutida nima bor?",
        "Внимание, чёрный ящик! В 1564 году в Англии пастухи нашли месторождение графита и метили им овец. Позже стержень заключили в деревянную оболочку, создав самый популярный инструмент для рисунка и письма. Что в чёрном ящике?",
        "Attention, black box! In 1564 in Cumberland, England, shepherds discovered pure graphite and used it to mark their sheep. Encased in wooden slats, it became the world's most ubiquitous drawing instrument. What is in the box?",
        "https://upload.wikimedia.org/wikipedia/commons/b/b2/Yellow_pencil.jpg",
        "Bitta oddiy qalam bilan taxminan 56 kilometr uzunlikdagi uzluksiz chiziq chizish yoki 45 000 ta so'z yozish mumkin.",
        "Одним стандартным карандашом можно провести линию длиной около 56 километров или написать около 45 тысяч слов.",
        "A typical pencil holds enough graphite to draw a continuous line 35 miles (56 km) long or write approximately 45,000 words.",
        ["qalam", "karandash", "pencil", "карандаш"]
    ),
    # 20: O'chirg'ich
    (
        "O'chirg'ich", "Ластик", "Eraser",
        ["Qalamtarosh", "Skrepka", "Yelim"],
        ["Точилка", "Скрепка", "Клей"],
        ["Sharpener", "Paper clip", "Glue"],
        "Hurmatli bilimdonlar, diqqat qiling: 1770-yilda kislorodni kashf etgan ingliz olimi Joseph Priestley tabiiy kauchuk parchasi qog'ozdagi qalam izlarini non uvoqlariga qaraganda ancha yaxshi o'chirishini aniqlagan. Ingliz tilida bu buyum 'rubber' deb ataladi. Qora qutidagi buyum nima?",
        "Внимание, чёрный ящик! В 1770 году химик Джозеф Пристли обнаружил, что кусочек натурального каучука стирает графит с бумаги гораздо лучше хлебного мякиша. В Великобритании этот предмет так и назвали — 'rubber'. Что в чёрном ящике?",
        "Attention, black box! In 1770, chemist Joseph Priestley noticed that a piece of natural coagulated rubber rubbed pencil marks off paper far better than stale breadcrumbs. What is in the black box?",
        "https://upload.wikimedia.org/wikipedia/commons/9/93/Rubber_erasers.jpg",
        "O'chirg'ich kashf etilgunga qadar butun dunyoda qalam izlarini o'chirish uchun xamir yoki qotgan oq non bo'laklari ishlatilgan.",
        "До изобретения ластика для стирания карандашных записей использовали мякиш свежего белого хлеба.",
        "Before rubber erasers were discovered, students and draftsmen routinely used rolled-up chunks of crustless white bread.",
        ["o'chirg'ich", "ochirgich", "lastik", "eraser", "rubber", "ластик"]
    )
]

print(f"Loaded {len(ITEMS_1_TO_65)} items in 1..20 block.")
