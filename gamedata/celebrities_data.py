# -*- coding: utf-8 -*-
"""
Celebrities Database for GeoGuru Telegram Bot (Who Is This? Mode).
Contains 120 world-renowned stars across sports, cinema, music, and tech.
Each entry includes multilingual names, category, nationality, high-res Wikimedia image,
comprehensive chat-answering aliases, and fascinating fun facts.
"""

import random
from typing import Optional, List, Dict, Any

CELEBRITIES: List[Dict[str, Any]] = [
    {
        "id": "cristiano_ronaldo",
        "name": {"uz": "Krishtianu Ronaldu", "ru": "Криштиану Роналду", "en": "Cristiano Ronaldo"},
        "category": "sport",
        "country": {"uz": "Portugaliya", "ru": "Португалия", "en": "Portugal"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Cristiano_Ronaldo_Croatia_v_Portugal_2_July_2026-075_%28cropped%29.jpg/960px-Cristiano_Ronaldo_Croatia_v_Portugal_2_July_2026-075_%28cropped%29.jpg",
        "aliases": ["ronaldo", "cr7", "cristiano", "ronaldu", "криштиану роналду", "роналду", "криро", "krishtianu ronaldu"],
        "fun_fact": {"uz": "Ronaldu tarixdagi rasmiy o'yinlarda 900 dan ortiq gol urgan birinchi futbolchidir.", "ru": "Роналду — первый футболист в истории, забивший более 900 официальных голов за карьеру.", "en": "Ronaldo is the first player in football history to score over 900 official career goals."}
    },
    {
        "id": "lionel_messi",
        "name": {"uz": "Lionel Messi", "ru": "Лионель Месси", "en": "Lionel Messi"},
        "category": "sport",
        "country": {"uz": "Argentina", "ru": "Аргентина", "en": "Argentina"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Leo_Messi_Argentina_v_Egypt_7_July_2026-1.jpg/960px-Leo_Messi_Argentina_v_Egypt_7_July_2026-1.jpg",
        "aliases": ["messi", "leo messi", "lionel messi", "месси", "лео месси", "лионель месси", "la pulga"],
        "fun_fact": {"uz": "Messi rekord darajadagi 8 ta 'Oltin to'p' (Ballon d'Or) sohibidir.", "ru": "Месси является рекордсменом по числу выигранных «Золотых мячей» — 8 наград.", "en": "Messi holds the all-time record with 8 Ballon d'Or awards."}
    },
    {
        "id": "kylian_mbappe",
        "name": {"uz": "Kilian Mbappe", "ru": "Килиан Мбаппе", "en": "Kylian Mbappé"},
        "category": "sport",
        "country": {"uz": "Fransiya", "ru": "Франция", "en": "France"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Kylian_Mbappe_France_v_Senegal_16_June_2026-391_%28cropped%29.jpg/960px-Kylian_Mbappe_France_v_Senegal_16_June_2026-391_%28cropped%29.jpg",
        "aliases": ["mbappe", "kylian mbappe", "мбаппе", "килиан мбаппе", "kilian mbappe"],
        "fun_fact": {"uz": "2022 yilgi Jahon chempionati finalida het-trik qayd etgan tarixdagi ikkinchi futbolchi.", "ru": "Стал вторым игроком в истории, оформившим хет-трик в финале чемпионата мира по футболу (2022).", "en": "Became only the second player in history to score a hat-trick in a World Cup final (2022)."}
    },
    {
        "id": "neymar",
        "name": {"uz": "Neymar", "ru": "Неймар", "en": "Neymar Jr"},
        "category": "sport",
        "country": {"uz": "Braziliya", "ru": "Бразилия", "en": "Brazil"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Neymar_Junior_Brazil_V_Morocco_13_June_2026-40.jpg/960px-Neymar_Junior_Brazil_V_Morocco_13_June_2026-40.jpg",
        "aliases": ["neymar", "neymar jr", "неймар", "неймар джуниор", "neymar junior"],
        "fun_fact": {"uz": "Neymar Braziliya milliy terma jamoasi tarixidagi eng yaxshi to'purar hisoblanadi (Peleni ortda qoldirgan).", "ru": "Неймар — лучший бомбардир в истории сборной Бразилии, превзошедший рекорд легендарного Пеле.", "en": "Neymar is Brazil's all-time top goalscorer, surpassing the legendary Pelé."}
    },
    {
        "id": "pele",
        "name": {"uz": "Pele", "ru": "Пеле", "en": "Pelé"},
        "category": "sport",
        "country": {"uz": "Braziliya", "ru": "Бразилия", "en": "Brazil"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Pele_con_brasil_%28cropped%29.jpg",
        "aliases": ["pele", "пеле", "o rei", "edson arantes do nascimento"],
        "fun_fact": {"uz": "Tarixda uch karra Jahon chempioni bo'lgan yagona futbolchi (1958, 1962, 1970).", "ru": "Единственный футболист в истории, трижды становившийся чемпионом мира как игрок (1958, 1962, 1970).", "en": "The only football player in history to win three FIFA World Cups as a player (1958, 1962, 1970)."}
    },
    {
        "id": "diego_maradona",
        "name": {"uz": "Diyego Maradona", "ru": "Диего Марадона", "en": "Diego Maradona"},
        "category": "sport",
        "country": {"uz": "Argentina", "ru": "Аргентина", "en": "Argentina"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/48/Argentina_celebrando_copa_%28cropped%29.jpg",
        "aliases": ["maradona", "diego maradona", "марадона", "диего марадона", "el pibe de oro"],
        "fun_fact": {"uz": "1986 yilgi JCHda Angliyaga qarshi afsonaviy 'Xudoning qo'li' va 'Asr goli'ni urgan.", "ru": "В четвертьфинале ЧМ-1986 против Англии забил легендарные голы «Рука Бога» и «Гол столетия».", "en": "Scored the legendary 'Hand of God' and 'Goal of the Century' against England in the 1986 World Cup."}
    },
    {
        "id": "zinedine_zidane",
        "name": {"uz": "Zinedin Zidan", "ru": "Зинедин Зидан", "en": "Zinedine Zidane"},
        "category": "sport",
        "country": {"uz": "Fransiya", "ru": "Франция", "en": "France"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Zinedine_Zidane_by_Tasnim_03.jpg",
        "aliases": ["zidane", "zizou", "зидан", "зинедин зидан", "зизу", "zinedin zidan"],
        "fun_fact": {"uz": "Real Madrid bosh murabbiyi sifatida ketma-ket 3 marta UEFA Chempionlar Ligasini yutgan.", "ru": "В качестве тренера «Реал Мадрид» выиграл Лигу чемпионов УЕФА 3 раза подряд.", "en": "Won three consecutive UEFA Champions League titles as manager of Real Madrid."}
    },
    {
        "id": "ronaldinho",
        "name": {"uz": "Ronaldinyo", "ru": "Роналдиньо", "en": "Ronaldinho"},
        "category": "sport",
        "country": {"uz": "Braziliya", "ru": "Бразилия", "en": "Brazil"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Ronaldinho_in_2019.jpg",
        "aliases": ["ronaldinho", "ronaldinho gaucho", "роналдиньо", "роналдинью", "ronaldinyo"],
        "fun_fact": {"uz": "Santiyago Bernabeu stadionida 'Real Madrid' muxlislari oyoqqa turib olqishlagan kam sonli 'Barselona' futbolchilaridan biri.", "ru": "Один из немногих игроков «Барселоны», которому стоя аплодировали трибуны «Сантьяго Бернабеу» в Мадриде.", "en": "One of the few Barcelona players to receive a standing ovation from Real Madrid fans at the Santiago Bernabéu."}
    },
    {
        "id": "erling_haaland",
        "name": {"uz": "Erling Xoland", "ru": "Эрлинг Холанн", "en": "Erling Haaland"},
        "category": "sport",
        "country": {"uz": "Norvegiya", "ru": "Норвегия", "en": "Norway"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Erling_Haaland_Morocco_v_Norway_7_June_2026-51.jpg/960px-Erling_Haaland_Morocco_v_Norway_7_June_2026-51.jpg",
        "aliases": ["haaland", "erling haaland", "холанд", "холанн", "эрлинг холанд", "xoland", "erling xoland"],
        "fun_fact": {"uz": "Premyer-liganing debyut mavsumidayoq 36 ta gol urib, liga tarixidagi mutlaq rekordni o'rnatdi.", "ru": "В дебютном сезоне АПЛ забил 36 голов, побив исторический рекорд результативности лиги за один сезон.", "en": "Broke the all-time Premier League single-season scoring record with 36 goals in his debut season."}
    },
    {
        "id": "karim_benzema",
        "name": {"uz": "Karim Benzema", "ru": "Карим Бензема", "en": "Karim Benzema"},
        "category": "sport",
        "country": {"uz": "Fransiya", "ru": "Франция", "en": "France"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Karim_Benzema_Pick.jpg/960px-Karim_Benzema_Pick.jpg",
        "aliases": ["benzema", "karim benzema", "бензема", "карим бензема", "kb9"],
        "fun_fact": {"uz": "2022 yilda 'Real Madrid' safidagi ajoyib mavsumi uchun 'Oltin to'p' sovrinini qo'lga kiritgan.", "ru": "Обладатель «Золотого мяча» 2022 года после феерического сезона в составе мадридского «Реала».", "en": "Won the 2022 Ballon d'Or after a spectacular season leading Real Madrid to Champions League glory."}
    },
    {
        "id": "luka_modric",
        "name": {"uz": "Luka Modrich", "ru": "Лука Модрич", "en": "Luka Modrić"},
        "category": "sport",
        "country": {"uz": "Xorvatiya", "ru": "Хорватия", "en": "Croatia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Luka_Modric_Croatia_v_Portugal_2_July_2026-055.jpg/960px-Luka_Modric_Croatia_v_Portugal_2_July_2026-055.jpg",
        "aliases": ["modric", "luka modric", "модрич", "лука модрич", "modrich"],
        "fun_fact": {"uz": "2018 yilda Ronaldu va Messi gegemonligini to'xtatib, 'Oltin to'p'ni qo'lga kiritgan.", "ru": "В 2018 году прервал десятилетнее доминирование Месси и Роналду, завоевав «Золотой мяч».", "en": "Broke the decade-long Messi-Ronaldo duopoly by winning the Ballon d'Or in 2018."}
    },
    {
        "id": "robert_lewandowski",
        "name": {"uz": "Robert Levandovski", "ru": "Роберт Левандовский", "en": "Robert Lewandowski"},
        "category": "sport",
        "country": {"uz": "Polsha", "ru": "Польша", "en": "Poland"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Robert_Lewandowski_NYCFC_v_Chicago_25_July_2026-383.jpg/960px-Robert_Lewandowski_NYCFC_v_Chicago_25_July_2026-383.jpg",
        "aliases": ["lewandowski", "lewa", "левандовски", "левандовский", "роберт левандовски", "levandovski"],
        "fun_fact": {"uz": "Bir o'yinda zaxiradan tushib, 9 daqiqa ichida 5 ta gol urib Ginnes rekordini o'rnatgan.", "ru": "Забил 5 голов всего за 9 минут после выхода на замену за «Баварию», установив мировой рекорд.", "en": "Scored 5 goals in just 9 minutes as a substitute for Bayern Munich, setting a Guinness World Record."}
    },
    {
        "id": "david_beckham",
        "name": {"uz": "Devid Bekhem", "ru": "Дэвид Бекхэм", "en": "David Beckham"},
        "category": "sport",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/73/David_Beckham_UNICEF_%28cropped2%29.jpg",
        "aliases": ["beckham", "david beckham", "бекхэм", "дэвид бекхэм", "bekhem", "devid bekhem"],
        "fun_fact": {"uz": "Jarimadan zarbalar ustasi bo'lgan Bekhem hozirda AQShning 'Inter Mayami' klubi egasidir.", "ru": "Мастер штрафных ударов, Бекхэм сейчас является совладельцем футбольного клуба «Интер Майами».", "en": "Renowned for his bending free-kicks, Beckham is now co-owner of MLS club Inter Miami."}
    },
    {
        "id": "zlatan_ibrahimovic",
        "name": {"uz": "Zlatan Ibrahimovich", "ru": "Златан Ибрагимович", "en": "Zlatan Ibrahimović"},
        "category": "sport",
        "country": {"uz": "Shvetsiya", "ru": "Швеция", "en": "Sweden"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Zlatan_Ibrahimovi%C4%87_nyc.jpg/960px-Zlatan_Ibrahimovi%C4%87_nyc.jpg",
        "aliases": ["zlatan", "ibrahimovic", "ибрагимович", "златан", "златан ибрагимович", "ibra", "ibroximovich"],
        "fun_fact": {"uz": "Zlatan to'rt xil o'n yillikda (1990, 2000, 2010, 2020) gol urgan kam sonli futbolchilardan.", "ru": "Забивал голы на профессиональном уровне в четырёх разных десятилетиях (1990-е, 2000-е, 2010-е, 2020-е).", "en": "Has scored professional goals across four different decades (1990s, 2000s, 2010s, 2020s)."}
    },
    {
        "id": "thierry_henry",
        "name": {"uz": "Tyerri Anri", "ru": "Тьерри Анри", "en": "Thierry Henry"},
        "category": "sport",
        "country": {"uz": "Fransiya", "ru": "Франция", "en": "France"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Thierry_Henry_%2851649035951%29_%28cropped%29.jpg/960px-Thierry_Henry_%2851649035951%29_%28cropped%29.jpg",
        "aliases": ["henry", "thierry henry", "анри", "тьерри анри", "anri"],
        "fun_fact": {"uz": "Londonning 'Arsenal' klubi tarixidagi eng yaxshi to'purar bo'lib, uning stadioni yonida haykali o'rnatilgan.", "ru": "Лучший бомбардир в истории лондонского «Арсенала», у стадиона клуба ему воздвигнута бронзовая статуя.", "en": "Arsenal's all-time record goalscorer, commemorated with a bronze statue outside Emirates Stadium."}
    },
    {
        "id": "andres_iniesta",
        "name": {"uz": "Andres Inyesta", "ru": "Андрес Иньеста", "en": "Andrés Iniesta"},
        "category": "sport",
        "country": {"uz": "Ispaniya", "ru": "Испания", "en": "Spain"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Andr%C3%A9s_Iniesta_Argentina_v_Spain_19_July_2026-034_%28cropped%29.jpg/960px-Andr%C3%A9s_Iniesta_Argentina_v_Spain_19_July_2026-034_%28cropped%29.jpg",
        "aliases": ["iniesta", "andres iniesta", "иньеста", "андрес иньеста", "don andres"],
        "fun_fact": {"uz": "2010 yilgi JCH finalining 116-daqiqasida gol urib, Ispaniyaga ilk Jahon chempionligini keltirgan.", "ru": "Забил победный гол на 116-й минуте финала ЧМ-2010, принеся Испании первый титул чемпионов мира.", "en": "Scored the 116th-minute winning goal in the 2010 World Cup final to give Spain its first title."}
    },
    {
        "id": "gianluigi_buffon",
        "name": {"uz": "Janluiji Buffon", "ru": "Джанлуиджи Буффон", "en": "Gianluigi Buffon"},
        "category": "sport",
        "country": {"uz": "Italiya", "ru": "Италия", "en": "Italy"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Norway_Italy_-_June_2025_A_44_%28Gianluigi_Buffon%29.jpg/960px-Norway_Italy_-_June_2025_A_44_%28Gianluigi_Buffon%29.jpg",
        "aliases": ["buffon", "gigi buffon", "gianluigi buffon", "буффон", "джанлуиджи буффон", "джиджи буффон"],
        "fun_fact": {"uz": "Italiya terma jamoasi safida rekord darajadagi 176 ta o'yin o'tkazgan afsonaviy darvozabon.", "ru": "Рекордсмен сборной Италии по сыгранным матчам (176 игр), чемпион мира 2006 года.", "en": "Holds the record for the most appearances for the Italian national team (176 caps) and won the 2006 World Cup."}
    },
    {
        "id": "mohamed_salah",
        "name": {"uz": "Muhammad Saloh", "ru": "Мохаммед Салах", "en": "Mohamed Salah"},
        "category": "sport",
        "country": {"uz": "Misr", "ru": "Египет", "en": "Egypt"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Mohamed_Salah_Argentina_v_Egypt_7_July_2026-163_%28cropped%29.jpg/960px-Mohamed_Salah_Argentina_v_Egypt_7_July_2026-163_%28cropped%29.jpg",
        "aliases": ["salah", "mo salah", "mohamed salah", "салах", "мо салах", "мохаммед салах", "saloh"],
        "fun_fact": {"uz": "Liverpul safida Premyer-ligada eng ko'p gol urgan afrikalik futbolchi hisoblanadi.", "ru": "Лучший африканский бомбардир в истории английской Премьер-лиги.", "en": "The highest-scoring African player in Premier League history, breaking numerous Liverpool records."}
    },
    {
        "id": "kevin_de_bruyne",
        "name": {"uz": "Kevin De Bryuyne", "ru": "Кевин Де Брёйне", "en": "Kevin De Bruyne"},
        "category": "sport",
        "country": {"uz": "Belgiya", "ru": "Бельгия", "en": "Belgium"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Kevin_De_Bruyne_USMNT_v_Belgium_Mar_28_2026-64_%28cropped%29.jpg/960px-Kevin_De_Bruyne_USMNT_v_Belgium_Mar_28_2026-64_%28cropped%29.jpg",
        "aliases": ["de bruyne", "kdb", "kevin de bruyne", "де брёйне", "де брюйне", "кевин де брейне", "де бруйне"],
        "fun_fact": {"uz": "Premyer-ligada eng tez 100 ta assist (golli uzatma) qayd etgan futbolchi hisoblanadi.", "ru": "Быстрее всех игроков в истории английской Премьер-лиги достиг отметки в 100 голевых передач.", "en": "Fastest player in Premier League history to reach 100 assists."}
    },
    {
        "id": "jude_bellingham",
        "name": {"uz": "Jud Bellingem", "ru": "Джуд Беллингем", "en": "Jude Bellingham"},
        "category": "sport",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Jude_Bellingham_England_v_Ghana_23_June_2026-061_%28cropped%29.jpg/960px-Jude_Bellingham_England_v_Ghana_23_June_2026-061_%28cropped%29.jpg",
        "aliases": ["bellingham", "jude bellingham", "беллингем", "джуд беллингем", "bellingem"],
        "fun_fact": {"uz": "Real Madrid safidagi debyut mavsumidayoq La Liga va Chempionlar Ligasini yutib, eng yaxshi o'yinchi deb topildi.", "ru": "В дебютном сезоне за «Реал Мадрид» выиграл Ла Лигу и Лигу чемпионов, став лучшим игроком чемпионата Испании.", "en": "Won La Liga and the Champions League in his debut season at Real Madrid, winning Player of the Season."}
    },
    {
        "id": "muhammad_ali",
        "name": {"uz": "Muhammad Ali", "ru": "Мухаммед Али", "en": "Muhammad Ali"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Muhammad_Ali_NYWTS.jpg/960px-Muhammad_Ali_NYWTS.jpg",
        "aliases": ["muhammad ali", "ali", "cassius clay", "мухаммед али", "али", "кассиус клей", "the greatest"],
        "fun_fact": {"uz": "'Kapalakdek uch, aridek chaq' shiori bilan boks tarixidagi eng buyuk afsonaga aylandi.", "ru": "Известен фразой «Порхай как бабочка, жаль как пчела», признан величайшим боксёром всех времён.", "en": "Famous for the phrase 'Float like a butterfly, sting like a bee', widely considered the greatest boxer in history."}
    },
    {
        "id": "mike_tyson",
        "name": {"uz": "Mayk Tayson", "ru": "Майк Тайсон", "en": "Mike Tyson"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Mike_Tyson_Photo_Op_GalaxyCon_Austin_2023.jpg",
        "aliases": ["mike tyson", "tyson", "iron mike", "майк тайсон", "тайсон", "железный майк", "mayk tayson"],
        "fun_fact": {"uz": "20 yoshida boks bo'yicha og'ir vaznda tarixdagi eng yosh jahon chempioniga aylangan.", "ru": "В возрасте 20 лет стал самым молодым чемпионом мира в тяжёлом весе в истории бокса.", "en": "Became the youngest heavyweight boxing champion in history at the age of 20."}
    },
    {
        "id": "usain_bolt",
        "name": {"uz": "Usayn Bolt", "ru": "Усэйн Болт", "en": "Usain Bolt"},
        "category": "sport",
        "country": {"uz": "Yamayka", "ru": "Ямайка", "en": "Jamaica"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Usain_Bolt_smiling_Berlin_2009.JPG",
        "aliases": ["usain bolt", "bolt", "lightning bolt", "усэйн болт", "болт", "усейн болт", "usayn bolt"],
        "fun_fact": {"uz": "100 metrni 9.58 soniyada yugurib o'tib, jahon rekordini o'rnatgan sayyoradagi eng tezkor inson.", "ru": "Обладатель мирового рекорда в беге на 100 метров (9,58 секунды), признан быстрейшим человеком планеты.", "en": "The fastest person in history, holding the world record for the 100 metres at 9.58 seconds."}
    },
    {
        "id": "michael_jordan",
        "name": {"uz": "Maykl Jordan", "ru": "Майкл Джордан", "en": "Michael Jordan"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Michael_jordan_admad_rashad_%2851276390562%29_%28cropped%29.jpg/960px-Michael_jordan_admad_rashad_%2851276390562%29_%28cropped%29.jpg",
        "aliases": ["michael jordan", "jordan", "mj", "air jordan", "майкл джордан", "джордан", "эм джей", "maykl jordan"],
        "fun_fact": {"uz": "Chikago Bullz bilan 6 marta NBA chempioni bo'lgan va Air Jordan brendiga asos solgan.", "ru": "Выиграл 6 чемпионатов НБА с «Чикаго Буллз» и создал всемирно известный бренд Air Jordan.", "en": "Won 6 NBA championships with the Chicago Bulls and created the iconic Air Jordan brand."}
    },
    {
        "id": "lebron_james",
        "name": {"uz": "Lebron Jeyms", "ru": "Леброн Джеймс", "en": "LeBron James"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/LeBron_James_%2851959977144%29_%28cropped2%29.jpg/960px-LeBron_James_%2851959977144%29_%28cropped2%29.jpg",
        "aliases": ["lebron james", "lebron", "king james", "леброн джеймс", "леброн", "кинг джеймс", "lebron jeyms"],
        "fun_fact": {"uz": "Kareem Abdul-Jabbarni ortda qoldirib, NBA tarixidagi eng ko'p ochko to'plagan basketbolchiga aylandi.", "ru": "Стал лучшим бомбардиром в истории НБА по набранным очкам, превзойдя рекорд Карима Абдул-Джаббара.", "en": "The all-time leading scorer in NBA history, surpassing Kareem Abdul-Jabbar."}
    },
    {
        "id": "kobe_bryant",
        "name": {"uz": "Kobi Brayant", "ru": "Коби Брайант", "en": "Kobe Bryant"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Kobe_Bryant_Dec_2014.jpg/960px-Kobe_Bryant_Dec_2014.jpg",
        "aliases": ["kobe bryant", "kobe", "black mamba", "коби брайант", "коби", "блэк мамба", "kobi brayant"],
        "fun_fact": {"uz": "Bir o'yinda 81 ochko to'plagan va 'Los-Anjeles Leykers' safida 5 marta NBA chempioni bo'lgan.", "ru": "Набрал 81 очко в одной игре НБА и завоевал 5 чемпионских перстней с «Лос-Анджелес Лейкерс».", "en": "Scored 81 points in a single NBA game and won 5 championships with the Los Angeles Lakers."}
    },
    {
        "id": "stephen_curry",
        "name": {"uz": "Stefen Karri", "ru": "Стефен Карри", "en": "Stephen Curry"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Stephen_Curry%2C_Olympic_Games_2024_%28cropped%29.jpg",
        "aliases": ["stephen curry", "steph curry", "curry", "стефен карри", "стеф карри", "карри", "stefen karri"],
        "fun_fact": {"uz": "Uch ochkolik tashlashlari bilan zamonaviy basketbol o'yinini butunlay o'zgartirgan afsona.", "ru": "Революционизировал мировой баскетбол своими рекордными трехочковыми бросками.", "en": "Revolutionized basketball with his extraordinary three-point shooting, holding the all-time NBA 3-pointer record."}
    },
    {
        "id": "khabib_nurmagomedov",
        "name": {"uz": "Habib Nurmagomedov", "ru": "Хабиб Нурмагомедов", "en": "Khabib Nurmagomedov"},
        "category": "sport",
        "country": {"uz": "Rossiya", "ru": "Россия", "en": "Russia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Khabib_nurmagomedov.jpg/960px-Khabib_nurmagomedov.jpg",
        "aliases": ["khabib nurmagomedov", "khabib", "the eagle", "хабиб нурмагомедов", "хабиб", "habib nurmagomedov", "habib"],
        "fun_fact": {"uz": "MMA faoliyatini 29 ta g'alaba va 0 ta mag'lubiyat bilan yakunlab, UFC yengil vazn chempioni sifatida ketgan.", "ru": "Завершил карьеру в ММА непобеждённым с рекордом 29-0 в статусе чемпиона UFC в лёгком весе.", "en": "Retired undefeated from MMA with an unprecedented 29-0 record as UFC Lightweight Champion."}
    },
    {
        "id": "conor_mcgregor",
        "name": {"uz": "Konor Makgregor", "ru": "Конор Макгрегор", "en": "Conor McGregor"},
        "category": "sport",
        "country": {"uz": "Irlandiya", "ru": "Ирландия", "en": "Ireland"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Conor_McGregor_2025.jpeg/960px-Conor_McGregor_2025.jpeg",
        "aliases": ["conor mcgregor", "mcgregor", "the notorious", "конор макгрегор", "макгрегор", "конор", "konor makgregor"],
        "fun_fact": {"uz": "Bir vaqtning o'zida ikkita turli vazn toifasida UFC chempioni bo'lgan birinchi jangchi.", "ru": "Первый боец в истории UFC, удерживавший чемпионские пояса в двух весовых категориях одновременно.", "en": "The first fighter in UFC history to hold championship titles in two weight divisions simultaneously."}
    },
    {
        "id": "roger_federer",
        "name": {"uz": "Rojer Federer", "ru": "Роджер Федерер", "en": "Roger Federer"},
        "category": "sport",
        "country": {"uz": "Shveysariya", "ru": "Швейцария", "en": "Switzerland"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Roger_Federer_2015_%28cropped%29.jpg/960px-Roger_Federer_2015_%28cropped%29.jpg",
        "aliases": ["roger federer", "federer", "роджер федерер", "федерер", "rojer federer"],
        "fun_fact": {"uz": "Uimbldon turnirini 8 marta yutgan va 237 hafta davomida ketma-ket dunyoning birinchi raqamli raketkasi bo'lgan.", "ru": "Выиграл Уимблдон рекордные 8 раз и непрерывно оставался первой ракеткой мира на протяжении 237 недель.", "en": "Won 8 Wimbledon titles and held the world No. 1 ranking for a record 237 consecutive weeks."}
    },
    {
        "id": "rafael_nadal",
        "name": {"uz": "Rafael Nadal", "ru": "Рафаэль Надаль", "en": "Rafael Nadal"},
        "category": "sport",
        "country": {"uz": "Ispaniya", "ru": "Испания", "en": "Spain"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Rafael_Nadal_en_2024_%28cropped%29.jpg/960px-Rafael_Nadal_en_2024_%28cropped%29.jpg",
        "aliases": ["rafael nadal", "nadal", "rafa", "рафаэль надаль", "надаль", "рафа", "king of clay"],
        "fun_fact": {"uz": "'Tuproq kort qiroli' — Roland Garros (Fransiya Ochiq chempionati) turnirini fantastik 14 marta yutgan.", "ru": "«Король грунта» — выиграл турнир Большого шлема «Ролан Гаррос» рекордные 14 раз.", "en": "Known as the 'King of Clay', having won the French Open an astounding 14 times."}
    },
    {
        "id": "novak_djokovic",
        "name": {"uz": "Novak Jokovich", "ru": "Новак Джокович", "en": "Novak Djokovic"},
        "category": "sport",
        "country": {"uz": "Serbiya", "ru": "Сербия", "en": "Serbia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Novak_Djokovic_Paris_2024_Olympic_Games_%28cropped%29.jpg/960px-Novak_Djokovic_Paris_2024_Olympic_Games_%28cropped%29.jpg",
        "aliases": ["novak djokovic", "djokovic", "nole", "новак джокович", "джокович", "ноле", "jokovich"],
        "fun_fact": {"uz": "Katta Dubulg'a turnirlarini 24 marta yutib, erkaklar o'rtasida mutlaq rekordchi bo'ldi.", "ru": "Рекордсмен по числу титулов Большого шлема в мужском одиночном разряде (24 титула).", "en": "Holds the all-time men's record with 24 Grand Slam singles titles and Olympic gold."}
    },
    {
        "id": "serena_williams",
        "name": {"uz": "Serena Uilyams", "ru": "Серена Уильямс", "en": "Serena Williams"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Serena-Smiling-2020.png/960px-Serena-Smiling-2020.png",
        "aliases": ["serena williams", "serena", "серена уильямс", "серена вильямс", "серена", "serena uilyams"],
        "fun_fact": {"uz": "Ochiq erada 23 ta Katta Dubulg'a yakkalik unvoniga ega eng buyuk ayol tennischidir.", "ru": "Завоевала 23 титула Большого шлема в одиночном разряде, рекорд в Открытой эре.", "en": "Won 23 Grand Slam singles titles, the most by any player in the Open Era."}
    },
    {
        "id": "michael_phelps",
        "name": {"uz": "Maykl Felps", "ru": "Майкл Фелпс", "en": "Michael Phelps"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Michael_Phelps_Rio_Olympics_2016.jpg/960px-Michael_Phelps_Rio_Olympics_2016.jpg",
        "aliases": ["michael phelps", "phelps", "майкл фелпс", "фелпс", "maykl felps"],
        "fun_fact": {"uz": "Olimpiya o'yinlarida 23 ta oltin (jami 28 ta medal) yutib, Olimpiada tarixidagi eng sovrindor sportchi bo'lgan.", "ru": "Самый титулованный спортсмен в истории Олимпийских игр: 23 золотые медали (всего 28 наград).", "en": "The most decorated Olympian of all time, winning 23 Olympic gold medals (28 total)."}
    },
    {
        "id": "lewis_hamilton",
        "name": {"uz": "Lyuis Hemilton", "ru": "Льюис Хэмилтон", "en": "Lewis Hamilton"},
        "category": "sport",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Prime_Minister_Keir_Starmer_meets_Sir_Lewis_Hamilton_%2854566928382%29_%28cropped%29.jpg/960px-Prime_Minister_Keir_Starmer_meets_Sir_Lewis_Hamilton_%2854566928382%29_%28cropped%29.jpg",
        "aliases": ["lewis hamilton", "hamilton", "льюис хэмилтон", "хэмилтон", "хамильтон", "lyuis hemilton"],
        "fun_fact": {"uz": "Formula-1 bo'yicha 7 karra jahon chempioni va 100 dan ortiq Gran-pri g'olibi bo'lgan birinchi poygachi.", "ru": "Семикратный чемпион мира Формулы-1 и первый гонщик, одержавший более 100 побед в Гран-при.", "en": "Seven-time Formula One World Champion and the first driver to surpass 100 Grand Prix wins."}
    },
    {
        "id": "max_verstappen",
        "name": {"uz": "Maks Ferstappen", "ru": "Макс Ферстаппен", "en": "Max Verstappen"},
        "category": "sport",
        "country": {"uz": "Niderlandiya", "ru": "Нидерланды", "en": "Netherlands"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/2024-08-25_Motorsport%2C_Formel_1%2C_Gro%C3%9Fer_Preis_der_Niederlande_2024_STP_3973_by_Stepro_%28medium_crop%29.jpg/960px-2024-08-25_Motorsport%2C_Formel_1%2C_Gro%C3%9Fer_Preis_der_Niederlande_2024_STP_3973_by_Stepro_%28medium_crop%29.jpg",
        "aliases": ["max verstappen", "verstappen", "макс ферстаппен", "ферстаппен", "maks ferstappen"],
        "fun_fact": {"uz": "Formula-1 da 17 yoshida debyut qilib, tarixdagi eng yosh F1 poygachisi va g'olibiga aylangan.", "ru": "Самый молодой гонщик и победитель Гран-при в истории Формулы-1 (дебютировал в 17 лет).", "en": "The youngest driver to start a Formula One race and win a Grand Prix, debuting at age 17."}
    },
    {
        "id": "michael_schumacher",
        "name": {"uz": "Mixael Shumaxer", "ru": "Михаэль Шумахер", "en": "Michael Schumacher"},
        "category": "sport",
        "country": {"uz": "Germaniya", "ru": "Германия", "en": "Germany"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Michael_Schumacher%2C_September_2005.jpg",
        "aliases": ["michael schumacher", "schumacher", "schumi", "михаэль шумахер", "шумахер", "шуми", "mixael shumaxer"],
        "fun_fact": {"uz": "Ferrari bilan ketma-ket 5 marta va jami 7 marta F1 jahon chempioni bo'lgan afsona.", "ru": "Семикратный чемпион мира Формулы-1, выигравший 5 титулов подряд за рулём Ferrari.", "en": "Legendary seven-time Formula One World Champion, who won 5 consecutive titles with Ferrari."}
    },
    {
        "id": "tiger_woods",
        "name": {"uz": "Tayger Vuds", "ru": "Тайгер Вудс", "en": "Tiger Woods"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/President_Donald_Trump_hosts_a_reception_honoring_Black_History_Month_%2854341713089%29_%28cropped%29.jpg",
        "aliases": ["tiger woods", "woods", "тайгер вудс", "вудс", "tayger vuds"],
        "fun_fact": {"uz": "Golf bo'yicha 15 ta yirik 'Major' turniri g'olibi va tarixdagi eng muvaffaqiyatli golfchi.", "ru": "Выиграл 15 крупных турниров «Мэйджор» и признан одним из величайших игроков в гольф всех времён.", "en": "Won 15 major golf championships and is widely regarded as one of the greatest golfers ever."}
    },
    {
        "id": "shaquille_oneal",
        "name": {"uz": "Shakil O'Nil", "ru": "Шакил О’Нил", "en": "Shaquille O'Neal"},
        "category": "sport",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/TechCrunch_Disrupt_2023_-_Day_1_%28cropped%29.jpg/960px-TechCrunch_Disrupt_2023_-_Day_1_%28cropped%29.jpg",
        "aliases": ["shaquille o'neal", "shaq", "shaquille oneal", "шакил о'нил", "шак", "шакил онил", "shakil onil"],
        "fun_fact": {"uz": "2.16 metr bo'yli va 147 kg og'irlikdagi Shak NBA tarixidagi eng jismoniy ustun markaziy o'yinchi bo'lgan.", "ru": "Один из самых доминирующих центровых в истории НБА при росте 216 см и весе почти 150 кг.", "en": "One of the most dominant centers in NBA history, standing 7 ft 1 in and weighing nearly 330 lbs."}
    },
    {
        "id": "manny_pacquiao",
        "name": {"uz": "Menni Pakyao", "ru": "Мэнни Пакьяо", "en": "Manny Pacquiao"},
        "category": "sport",
        "country": {"uz": "Filippin", "ru": "Филиппины", "en": "Philippines"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Former_senator_Manny_Pacquiao_speaks_in_event_%2810-01-2025%29_%28cropped%29.jpg",
        "aliases": ["manny pacquiao", "pacquiao", "pacman", "мэнни пакьяо", "пакьяо", "пакман", "menni pakyao"],
        "fun_fact": {"uz": "Sakkiz xil vazn toifasida jahon chempioni bo'lgan boks tarixidagi yagona inson.", "ru": "Единственный боксёр в истории, становившийся чемпионом мира в восьми различных весовых категориях.", "en": "The only eight-division world champion in the history of boxing."}
    },
    {
        "id": "wayne_rooney",
        "name": {"uz": "Ueyn Runi", "ru": "Уэйн Руни", "en": "Wayne Rooney"},
        "category": "sport",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Wayne_Rooney_%2850121495731%29_%28cropped%29.jpg",
        "aliases": ["wayne rooney", "rooney", "уэйн руни", "руни", "ueyn runi"],
        "fun_fact": {"uz": "'Manchester Yunayted' tarixidagi eng yaxshi to'purar (253 ta gol) bo'lgan sermahsul hujumchi.", "ru": "Лучший бомбардир в истории клуба «Манчестер Юнайтед» (253 забитых мяча).", "en": "Manchester United's all-time record goalscorer with 253 goals across all competitions."}
    },
    {
        "id": "harry_kane",
        "name": {"uz": "Harri Keyn", "ru": "Харри Кейн", "en": "Harry Kane"},
        "category": "sport",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Harry_Kane_England_v_Ghana_23_June_2026-024_%28cropped%29.jpg/960px-Harry_Kane_England_v_Ghana_23_June_2026-024_%28cropped%29.jpg",
        "aliases": ["harry kane", "kane", "харри кейн", "гарри кейн", "кейн", "harri keyn"],
        "fun_fact": {"uz": "Angliya terma jamoasi va 'Tottenxem' klubi tarixidagi eng yaxshi to'purar hisoblanadi.", "ru": "Лучший бомбардир в истории сборной Англии и клуба «Тоттенхэм Хотспур».", "en": "The all-time highest goalscorer for both England national team and Tottenham Hotspur."}
    },
    {
        "id": "leonardo_dicaprio",
        "name": {"uz": "Leonardo Di Kaprio", "ru": "Леонардо Ди Каприо", "en": "Leonardo DiCaprio"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2d/LeoPTABFI191125-28_%28cropped%29.jpg",
        "aliases": ["leonardo dicaprio", "dicaprio", "леонардо ди каприо", "дикаприо", "лео дикаприо", "leonardo di kaprio"],
        "fun_fact": {"uz": "'Titanik', 'Muqaddima' kabi durdonalar yulduzi bo'lib, 2016 yilda 'Omon qolgan' filmi uchun Oskar oldi.", "ru": "Звезда фильмов «Титаник» и «Начало», в 2016 году получил заветный «Оскар» за фильм «Выживший».", "en": "Star of 'Titanic' and 'Inception', won his long-awaited Academy Award for 'The Revenant' in 2016."}
    },
    {
        "id": "tom_cruise",
        "name": {"uz": "Tom Kruz", "ru": "Том Круз", "en": "Tom Cruise"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Tom_Cruise_at_53rd_Saturn_Awards_2026-01.jpg/960px-Tom_Cruise_at_53rd_Saturn_Awards_2026-01.jpg",
        "aliases": ["tom cruise", "cruise", "том круз", "круз", "tom kruz"],
        "fun_fact": {"uz": "'Uddalab bo'lmas topshiriq' filmlaridagi eng xavfli kaskadyorlik tryuklarini dublyorsiz o'zi bajaradi.", "ru": "Известен тем, что самостоятельно выполняет сложнейшие трюки в серии фильмов «Миссия невыполнима».", "en": "Famous for performing his own dangerous stunts in the 'Mission: Impossible' film franchise."}
    },
    {
        "id": "brad_pitt",
        "name": {"uz": "Bred Pitt", "ru": "Брэд Питт", "en": "Brad Pitt"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Brad_Pitt-69858.jpg/960px-Brad_Pitt-69858.jpg",
        "aliases": ["brad pitt", "pitt", "брэд питт", "питт", "bred pitt"],
        "fun_fact": {"uz": "'Jangari klub', 'Troya' yulduzi, ham aktyor, ham prodyuser sifatida 2 marta Oskar mukofotiga sazovor bo'lgan.", "ru": "Звезда фильмов «Бойцовский клуб» и «Троя», дважды лауреат премии «Оскар» (как продюсер и актёр).", "en": "Starred in 'Fight Club' and 'Troy', winning Academy Awards both as a producer and supporting actor."}
    },
    {
        "id": "keanu_reeves",
        "name": {"uz": "Kianu Rivz", "ru": "Киану Ривз", "en": "Keanu Reeves"},
        "category": "cinema",
        "country": {"uz": "Kanada", "ru": "Канада", "en": "Canada"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Keanu_Reeves_at_TIFF_2025_02_%28Cropped%29.jpg/960px-Keanu_Reeves_at_TIFF_2025_02_%28Cropped%29.jpg",
        "aliases": ["keanu reeves", "reeves", "neo", "john wick", "киану ривз", "ривз", "нео", "джон уик", "kianu rivz"],
        "fun_fact": {"uz": "'Matritsa'dagi Neo va 'Jon Uik' rollari bilan tanilgan Gollivudning eng samimiy va saxiy yulduzlaridan biri.", "ru": "Исполнитель ролей Нео в «Матрице» и Джона Уика, известен своей скромностью и благотворительностью.", "en": "Famed for playing Neo in 'The Matrix' and John Wick, renowned for his philanthropy and humble lifestyle."}
    },
    {
        "id": "jackie_chan",
        "name": {"uz": "Jeki Chan", "ru": "Джеки Чан", "en": "Jackie Chan"},
        "category": "cinema",
        "country": {"uz": "Gonkong", "ru": "Гонконг", "en": "Hong Kong"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Jackie_Chan.jpg",
        "aliases": ["jackie chan", "chan", "джеки чан", "чан", "jeki chan"],
        "fun_fact": {"uz": "150 dan ortiq filmlarda suratga tushgan va akrobatik jang san'atini komediya bilan birlashtirgan afsona.", "ru": "Снялся в более чем 150 фильмах, совместив боевые искусства с непревзойденной комедийной акробатикой.", "en": "Has starred in over 150 films, pioneering acrobatic martial arts comedy and performing his own stunts."}
    },
    {
        "id": "johnny_depp",
        "name": {"uz": "Jonni Depp", "ru": "Джонни Депп", "en": "Johnny Depp"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/21/Johnny_Depp_2020.jpg",
        "aliases": ["johnny depp", "depp", "jack sparrow", "джонни депп", "депп", "капитан джек воробей", "jonni depp"],
        "fun_fact": {"uz": "'Karib dengizi qaroqchilari' filmidagi afsonaviy Kapitan Jek Chittak (Jack Sparrow) obrazi muallifi.", "ru": "Создал культовый образ Капитана Джека Воробья в киносаге «Пираты Карибского моря».", "en": "Created the iconic character Captain Jack Sparrow in the blockbuster 'Pirates of the Caribbean' series."}
    },
    {
        "id": "robert_downey_jr",
        "name": {"uz": "Robert Dauni Jr", "ru": "Роберт Дауни-младший", "en": "Robert Downey Jr."},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/RobertDowneyJr-byPhilipRomano7_%28cropped%29.jpg/960px-RobertDowneyJr-byPhilipRomano7_%28cropped%29.jpg",
        "aliases": ["robert downey jr", "downey jr", "iron man", "роберт дауни младший", "дауни младший", "железный человек", "rdj"],
        "fun_fact": {"uz": "Marvel kinoolamida 'Temir odam' (Iron Man) rolini o'ynagan va 'Oppengeymer' uchun Oskar mukofotini qo'lga kiritgan.", "ru": "Сыграл Железного Человека в киновселенной Marvel и получил премию «Оскар» за роль в «Оппенгеймере».", "en": "Portrayed Tony Stark / Iron Man in the Marvel Cinematic Universe and won an Oscar for 'Oppenheimer'."}
    },
    {
        "id": "will_smith",
        "name": {"uz": "Uill Smit", "ru": "Уилл Смит", "en": "Will Smith"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/TechCrunch_Disrupt_San_Francisco_2019_-_Day_1_%2848834070763%29_%28cropped%29.jpg/960px-TechCrunch_Disrupt_San_Francisco_2019_-_Day_1_%2848834070763%29_%28cropped%29.jpg",
        "aliases": ["will smith", "fresh prince", "уилл смит", "смит", "uill smit"],
        "fun_fact": {"uz": "'Qora libosli odamlar' va 'Baxt ortidan quvib' filmlari yulduzi, 2022 yilda Oskar mukofoti sohibi bo'ldi.", "ru": "Звезда фильмов «Люди в чёрном» и «В погоне за счастьем», обладатель премии «Оскар» 2022 года.", "en": "Starred in 'Men in Black' and 'The Pursuit of Happyness', winning the Best Actor Oscar in 2022."}
    },
    {
        "id": "christopher_nolan",
        "name": {"uz": "Kristofer Nolan", "ru": "Кристофер Нолан", "en": "Christopher Nolan"},
        "category": "cinema",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/ChristopherNolan-byPhilipRomano_%28cropped%29.jpg/960px-ChristopherNolan-byPhilipRomano_%28cropped%29.jpg",
        "aliases": ["christopher nolan", "nolan", "кристофер нолан", "нолан", "kristofer nolan"],
        "fun_fact": {"uz": "'Interstellar', 'Muqaddima' va 'Qora Ritsar' trilogiyasining rejissyori, CGI o'rniga amaliy effektlarni yoqtiradi.", "ru": "Режиссёр фильмов «Интерстеллар», «Начало» и трилогии «Тёмный рыцарь», отдающий предпочтение реальным съёмкам.", "en": "Visionary director of 'Interstellar', 'Inception', and 'Oppenheimer', known for using practical effects."}
    },
    {
        "id": "quentin_tarantino",
        "name": {"uz": "Kventin Tarantino", "ru": "Квентин Тарантино", "en": "Quentin Tarantino"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Quentin_Tarantino_by_Gage_Skidmore.jpg/960px-Quentin_Tarantino_by_Gage_Skidmore.jpg",
        "aliases": ["quentin tarantino", "tarantino", "квентин тарантино", "тарантино", "kventin tarantino"],
        "fun_fact": {"uz": "'Kriminal asar' (Pulp Fiction) va 'Boshsiz chavandozlar' muallifi, o'z filmlarini 10 taga yetkazib faoliyatini tugatishini aytgan.", "ru": "Создатель «Криминального чтива» и «Джанго освобождённого», пообещавший снять ровно 10 фильмов за карьеру.", "en": "Director of 'Pulp Fiction' and 'Django Unchained', famous for nonlinear storytelling and brilliant dialogue."}
    },
    {
        "id": "steven_spielberg",
        "name": {"uz": "Stiven Spilberg", "ru": "Стивен Спилберг", "en": "Steven Spielberg"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/MKr25402_Steven_Spielberg_%28Berlinale_2023%29_%283x4_cropped%29.jpg/960px-MKr25402_Steven_Spielberg_%28Berlinale_2023%29_%283x4_cropped%29.jpg",
        "aliases": ["steven spielberg", "spielberg", "стивен спилберг", "спилберг", "stiven spilberg"],
        "fun_fact": {"uz": "Kino tarixidagi eng kassabop rejissyor ('Yura davri bog'i', 'Shindler ro'yxati', 'Jag'lar').", "ru": "Самый коммерчески успешный режиссёр в истории кино («Парк Юрского периода», «Список Шиндлера», «Челюсти»).", "en": "The highest-grossing film director in history ('Jurassic Park', 'Schindler's List', 'Jaws')."}
    },
    {
        "id": "arnold_schwarzenegger",
        "name": {"uz": "Arnold Shvarsenegger", "ru": "Арнольд Шварценеггер", "en": "Arnold Schwarzenegger"},
        "category": "cinema",
        "country": {"uz": "Avstriya", "ru": "Австрия", "en": "Austria"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Arnold_Schwarzenegger_-_Austrian_World_Summit_2026_BHO-2906.jpg/960px-Arnold_Schwarzenegger_-_Austrian_World_Summit_2026_BHO-2906.jpg",
        "aliases": ["arnold schwarzenegger", "schwarzenegger", "terminator", "arnie", "арнольд шварценеггер", "шварценеггер", "терминатор", "арни"],
        "fun_fact": {"uz": "7 karra 'Janob Olimpiya' bodibilding chempioni, 'Terminator' yulduzi va Kaliforniya gubernatori bo'lgan.", "ru": "7-кратный «Мистер Олимпия», культовый Терминатор и 38-й губернатор штата Калифорния.", "en": "7-time Mr. Olympia bodybuilder, Hollywood superstar in 'The Terminator', and 38th Governor of California."}
    },
    {
        "id": "sylvester_stallone",
        "name": {"uz": "Silvestr Stallone", "ru": "Сильвестр Сталлоне", "en": "Sylvester Stallone"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/12/P20251206DT-0472_%283x4_cropped_on_Stallone_with_moderate_headroom%29.jpg",
        "aliases": ["sylvester stallone", "stallone", "rambo", "rocky", "сильвестр сталлоне", "сталлоне", "рэмбо", "рокки", "silvestr stallone"],
        "fun_fact": {"uz": "'Rokki' filmi ssenariysini 3 kunda yozgan va film 3 ta Oskar mukofotiga sazovor bo'lgan.", "ru": "Написал сценарий к фильму «Рокки» всего за три дня, картина выиграла три премии «Оскар».", "en": "Wrote the screenplay for 'Rocky' in just three days, leading the film to win three Oscars."}
    },
    {
        "id": "morgan_freeman",
        "name": {"uz": "Morgan Friman", "ru": "Морган Фримен", "en": "Morgan Freeman"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Morgan_Freeman_at_The_Pentagon_on_2_August_2023_-_230802-D-PM193-3363_%28cropped%29.jpg/960px-Morgan_Freeman_at_The_Pentagon_on_2_August_2023_-_230802-D-PM193-3363_%28cropped%29.jpg",
        "aliases": ["morgan freeman", "freeman", "морган фримен", "фримен", "морган фриман", "morgan friman"],
        "fun_fact": {"uz": "O'zining chuqur va sehrli ovozi bilan mashhur bo'lib, filmlarda Xudo obrazini bir necha bor gavdalantirgan.", "ru": "Знаменит своим глубоким узнаваемым голосом, неоднократно играл роль Бога в кинематографе.", "en": "Known for his calm, resonant voice and iconic performance in 'The Shawshank Redemption'."}
    },
    {
        "id": "denzel_washington",
        "name": {"uz": "Denzel Vashington", "ru": "Дензел Вашингтон", "en": "Denzel Washington"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Denzel_Washington_at_the_2025_Cannes_Film_Festival.jpg/960px-Denzel_Washington_at_the_2025_Cannes_Film_Festival.jpg",
        "aliases": ["denzel washington", "denzel", "дензел вашингтон", "вашингтон", "denzel vashington"],
        "fun_fact": {"uz": "Ikki karra Oskar mukofoti sohibi bo'lgan Gollivudning eng hurmatli dramatik aktyorlaridan biri.", "ru": "Двукратный обладатель премии «Оскар», один из самых уважаемых актёров современного кинематографа.", "en": "Two-time Academy Award winner regarded as one of the greatest actors of the 21st century."}
    },
    {
        "id": "tom_hanks",
        "name": {"uz": "Tom Xenks", "ru": "Том Хэнкс", "en": "Tom Hanks"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TomHanksPrincEdw031223_%2811_of_41%29_%28cropped%29.jpg/960px-TomHanksPrincEdw031223_%2811_of_41%29_%28cropped%29.jpg",
        "aliases": ["tom hanks", "hanks", "forrest gump", "том хэнкс", "хэнкс", "форрест гамп", "tom xenks"],
        "fun_fact": {"uz": "'Filadelfiya' va 'Forrest Gamp' filmlari uchun ketma-ket 2 yil eng yaxshi aktyor Oskarini olgan kam sonli yulduz.", "ru": "Выиграл две премии «Оскар» подряд за лучшую мужскую роль («Филадельфия» и «Форрест Гамп»).", "en": "Won back-to-back Academy Awards for Best Actor for 'Philadelphia' (1993) and 'Forrest Gump' (1994)."}
    },
    {
        "id": "al_pacino",
        "name": {"uz": "Al Pachino", "ru": "Аль Пачино", "en": "Al Pacino"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Al_Pacino_-_Killing_Castro_-_Q%26A_-_Tribeca_2026_-_by_%40JJxFile-23_%28cropped%29.jpg/960px-Al_Pacino_-_Killing_Castro_-_Q%26A_-_Tribeca_2026_-_by_%40JJxFile-23_%28cropped%29.jpg",
        "aliases": ["al pacino", "pacino", "godfather", "scarface", "аль пачино", "пачино", "крестный отец", "лицо со шрамом"],
        "fun_fact": {"uz": "'Cho'qintirgan ota' filmidagi Maykl Korleone va 'Chandiqli yuz'dagi Toni Montana rollari bilan afsonaga aylangan.", "ru": "Сыграл Майкла Корлеоне в «Крёстном отце» и Тони Монтану в «Лице со шрамом».", "en": "Immortalized as Michael Corleone in 'The Godfather' and Tony Montana in 'Scarface'."}
    },
    {
        "id": "robert_de_niro",
        "name": {"uz": "Robert De Niro", "ru": "Роберт Де Ниро", "en": "Robert De Niro"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Robert_de_Niro_Cannes_Film_Festival_%283x4_cropped%29.jpg/960px-Robert_de_Niro_Cannes_Film_Festival_%283x4_cropped%29.jpg",
        "aliases": ["robert de niro", "de niro", "роберт де ниро", "де ниро", "robert de niro"],
        "fun_fact": {"uz": "'Quturgan buqa' (Raging Bull) filmi uchun 27 kg semirib, aktyorlik mahorati me'yorlarini yangilagan.", "ru": "Набрал 27 кг для роли боксёра в фильме «Бешеный бык», завоевав премию «Оскар».", "en": "Famously gained 60 pounds to play Jake LaMotta in 'Raging Bull', winning the Academy Award."}
    },
    {
        "id": "christian_bale",
        "name": {"uz": "Kristian Beyl", "ru": "Кристиан Бэйл", "en": "Christian Bale"},
        "category": "cinema",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Christian_Bale-7837.jpg/960px-Christian_Bale-7837.jpg",
        "aliases": ["christian bale", "bale", "batman", "кристиан бэйл", "бэйл", "бэтмен", "kristian beyl"],
        "fun_fact": {"uz": "Rollari uchun tana vaznini keskin o'zgartirishi bilan mashhur (Masalan: 'Mashinist' va 'Betmen').", "ru": "Известен экстремальными физическими трансформациями ради ролей в кино («Машинист», «Бэтмен»).", "en": "Known for his extreme physical transformations, dropping to 120 lbs for 'The Machinist' before bulking for 'Batman'."}
    },
    {
        "id": "cillian_murphy",
        "name": {"uz": "Killian Myorfi", "ru": "Киллиан Мёрфи", "en": "Cillian Murphy"},
        "category": "cinema",
        "country": {"uz": "Irlandiya", "ru": "Ирландия", "en": "Ireland"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Cillian_Murphy_at_the_London_premier_of_Steve_in_September_2025_%28cropped%29.jpg",
        "aliases": ["cillian murphy", "oppenheimer", "thomas shelby", "киллиан мёрфи", "мерфи", "киллиан мерфи", "томас шелби"],
        "fun_fact": {"uz": "'O'tkir soyabonlar' serialida Tomas Shelbi va 'Oppengeymer' filmidagi roli bilan Oskar mukofotiga loyiq ko'rildi.", "ru": "Звезда сериала «Острые козырьки» (Томас Шелби), завоевал премию «Оскар» за роль создателя атомной бомбы в «Оппенгеймере».", "en": "Starred as Thomas Shelby in 'Peaky Blinders' and won the Best Actor Oscar for 'Oppenheimer'."}
    },
    {
        "id": "joaquin_phoenix",
        "name": {"uz": "Xoakin Feniks", "ru": "Хоакин Феникс", "en": "Joaquin Phoenix"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Joaquin_Phoenix-64908_%28cropped%29.jpg/960px-Joaquin_Phoenix-64908_%28cropped%29.jpg",
        "aliases": ["joaquin phoenix", "phoenix", "joker", "хоакин феникс", "феникс", "джокер", "xoakin feniks"],
        "fun_fact": {"uz": "2019 yilda 'Joker' filmi bosh qahramoni roli uchun Oskar sovrindori bo'ldi.", "ru": "Завоевал премию «Оскар» за главную роль в психологическом триллере «Джокер» (2019).", "en": "Won the Academy Award for Best Actor for his haunting performance in 'Joker' (2019)."}
    },
    {
        "id": "heath_ledger",
        "name": {"uz": "Hit Lejer", "ru": "Хит Леджер", "en": "Heath Ledger"},
        "category": "cinema",
        "country": {"uz": "Avstraliya", "ru": "Австралия", "en": "Australia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Heath_Ledger_%282%29.jpg/960px-Heath_Ledger_%282%29.jpg",
        "aliases": ["heath ledger", "ledger", "joker", "хит леджер", "леджер", "hit lejer"],
        "fun_fact": {"uz": "'Qora Ritsar' filmidagi afsonaviy Joker roli uchun vafotidan so'ng Oskar mukofoti bilan taqdirlangan.", "ru": "Посмертно удостоен премии «Оскар» за незабываемое воплощение Джокера в «Тёмном рыцаре».", "en": "Posthumously awarded the Academy Award for his defining portrayal of the Joker in 'The Dark Knight'."}
    },
    {
        "id": "hugh_jackman",
        "name": {"uz": "Xyu Jekman", "ru": "Хью Джекман", "en": "Hugh Jackman"},
        "category": "cinema",
        "country": {"uz": "Avstraliya", "ru": "Австралия", "en": "Australia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Hugh_Jackman_Is_This_Thing_On-68_%28cropped%29.jpg/960px-Hugh_Jackman_Is_This_Thing_On-68_%28cropped%29.jpg",
        "aliases": ["hugh jackman", "wolverine", "хью джекман", "джекман", "росомаха", "xyu jekman"],
        "fun_fact": {"uz": "X-Men franchizasida Rosomaxa (Wolverine) obrazini 24 yildan ortiq davomida ijro etib Ginnes rekordiga kirdi.", "ru": "Исполнял роль Росомахи на протяжении более двух десятилетий, установив мировой рекорд.", "en": "Held the Guinness World Record for the longest career as a live-action Marvel superhero as Wolverine."}
    },
    {
        "id": "ryan_reynolds",
        "name": {"uz": "Rayan Reynolds", "ru": "Райан Рейнольдс", "en": "Ryan Reynolds"},
        "category": "cinema",
        "country": {"uz": "Kanada", "ru": "Канада", "en": "Canada"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Deadpool_2_Japan_Premiere_Red_Carpet_Ryan_Reynolds_%28cropped%29.jpg/960px-Deadpool_2_Japan_Premiere_Red_Carpet_Ryan_Reynolds_%28cropped%29.jpg",
        "aliases": ["ryan reynolds", "deadpool", "райан рейнольдс", "рейнольдс", "дэдпул", "rayan reynolds"],
        "fun_fact": {"uz": "'Deadpool' filmi yulduzi bo'lib, o'tkir yumori va muvaffaqiyatli biznes loyihalari bilan tanilgan.", "ru": "Звезда блокбастера «Дэдпул», прославившийся своим искромётным юмором и продюсерскими проектами.", "en": "Star and producer of 'Deadpool', known for his quick wit and co-ownership of Wrexham AFC."}
    },
    {
        "id": "chris_hemsworth",
        "name": {"uz": "Kris Xemsvort", "ru": "Крис Хемсворт", "en": "Chris Hemsworth"},
        "category": "cinema",
        "country": {"uz": "Avstraliya", "ru": "Австралия", "en": "Australia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Chris_Hemsworth_-_Crime_101.jpg/960px-Chris_Hemsworth_-_Crime_101.jpg",
        "aliases": ["chris hemsworth", "thor", "крис хемсворт", "хемсворт", "тор", "kris xemsvort"],
        "fun_fact": {"uz": "Marvel kinoolamida Mjolnir bolg'asini ko'targan Qudratli Momaqaldiroq xudosi — Tor rolini o'ynagan.", "ru": "Исполнитель роли могучего бога грома Тора в супергеройских блокбастерах Marvel.", "en": "Rose to international superstardom playing Thor in the Marvel Cinematic Universe."}
    },
    {
        "id": "dwayne_johnson",
        "name": {"uz": "Dueyn Jonson", "ru": "Дуэйн Джонсон", "en": "Dwayne Johnson"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Dwayne_Johnson-1764_%284x5_cropped_with_moderate_headroom%29.jpg/960px-Dwayne_Johnson-1764_%284x5_cropped_with_moderate_headroom%29.jpg",
        "aliases": ["dwayne johnson", "the rock", "rock", "дуэйн джонсон", "скала", "джонсон", "dueyn jonson"],
        "fun_fact": {"uz": "'The Rock' (Qoya) laqabi bilan WWE resling yulduzidan dunyoning eng ko'p haq to'lanadigan aktyorlaridan biriga aylandi.", "ru": "Прошёл путь от легенды реслинга «Скалы» до самого высокооплачиваемого актёра Голливуда.", "en": "Transitioned from wrestling megastar 'The Rock' to one of Hollywood's highest-paid box office draws."}
    },
    {
        "id": "jason_statham",
        "name": {"uz": "Jeyson Stetxem", "ru": "Джейсон Стэйтем", "en": "Jason Statham"},
        "category": "cinema",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Jason_Statham_2018.jpg",
        "aliases": ["jason statham", "statham", "джейсон стэтхэм", "стэтхем", "стэйтем", "стетхэм", "jeyson stetxem"],
        "fun_fact": {"uz": "Kino olamiga kirib kelishdan oldin Britaniya milliy terma jamoasi safida suvga sakrash sporti bilan professional shug'ullangan.", "ru": "До съёмок в кино на протяжении 12 лет входил в состав сборной Великобритании по прыжкам в воду.", "en": "Was a professional diver on Britain's National Diving Squad for 12 years before becoming an action hero."}
    },
    {
        "id": "scarlett_johansson",
        "name": {"uz": "Skarlett Yoxansson", "ru": "Скарлетт Йоханссон", "en": "Scarlett Johansson"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Scarlett_Johansson-8588.jpg/960px-Scarlett_Johansson-8588.jpg",
        "aliases": ["scarlett johansson", "johansson", "black widow", "скарлетт йоханссон", "йоханссон", "черная вдова", "skarlett yoxansson"],
        "fun_fact": {"uz": "Marvel filmlarida 'Qora beva' (Black Widow) rolini o'ynagan va kinolari jami 14 milliard dollardan ortiq mablag' to'plagan.", "ru": "Исполнительница роли Чёрной вдовы в Marvel, фильмы с её участием собрали более 14 миллиардов долларов.", "en": "Played Black Widow in Marvel; films featuring her have grossed over $14 billion worldwide."}
    },
    {
        "id": "angelina_jolie",
        "name": {"uz": "Anjelina Joli", "ru": "Анджелина Джоли", "en": "Angelina Jolie"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Angelina_Jolie-643531_%28cropped%29.jpg/960px-Angelina_Jolie-643531_%28cropped%29.jpg",
        "aliases": ["angelina jolie", "jolie", "lara croft", "анджелина джоли", "джоли", "anjelina joli"],
        "fun_fact": {"uz": "Lara Kroft va Malefisenta rollari bilan mashhur Oskar sohibasi hamda BMTning maxsus elchisi.", "ru": "Обладательница премии «Оскар», звезда «Лары Крофт» и «Малефисенты», посол доброй воли ООН.", "en": "Academy Award winner famous for Lara Croft and 'Maleficent', as well as extensive UNHCR humanitarian work."}
    },
    {
        "id": "emma_watson",
        "name": {"uz": "Emma Uotson", "ru": "Эмма Уотсон", "en": "Emma Watson"},
        "category": "cinema",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Emma_Watson_2013.jpg",
        "aliases": ["emma watson", "hermione", "эмма уотсон", "гермиона", "гермиона грейнджер", "emma uotson"],
        "fun_fact": {"uz": "Garri Potter haqidagi barcha 8 ta filmda donishmand Germiona Greyndjer rolini gavdalantirgan.", "ru": "Сыграла Гермиону Грейнджер во всех восьми фильмах саги о Гарри Поттере.", "en": "Portrayed Hermione Granger in all eight 'Harry Potter' films, rising to global fame as a child."}
    },
    {
        "id": "natalie_portman",
        "name": {"uz": "Natali Portman", "ru": "Натали Портман", "en": "Natalie Portman"},
        "category": "cinema",
        "country": {"uz": "Isroil", "ru": "Израиль", "en": "Israel"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/NataliePortman.jpg/960px-NataliePortman.jpg",
        "aliases": ["natalie portman", "portman", "padme", "натали портман", "портман", "natali portman"],
        "fun_fact": {"uz": "'Qora oqqush' filmidagi balerina roli uchun Oskar mukofotiga sazovor bo'lgan Garvard universiteti bitiruvchisi.", "ru": "Выпускница Гарвардского университета и обладательница премии «Оскар» за главную роль в «Чёрном лебеде».", "en": "Harvard psychology graduate who won the Best Actress Oscar for 'Black Swan'."}
    },
    {
        "id": "margot_robbie",
        "name": {"uz": "Margo Robbi", "ru": "Марго Робби", "en": "Margot Robbie"},
        "category": "cinema",
        "country": {"uz": "Avstraliya", "ru": "Австралия", "en": "Australia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Margot_Robbie_Wuthering_Heights_premiere_%28cropped%29.jpg/960px-Margot_Robbie_Wuthering_Heights_premiere_%28cropped%29.jpg",
        "aliases": ["margot robbie", "barbie", "harley quinn", "марго робби", "робби", "барби", "харли квинн", "margo robbi"],
        "fun_fact": {"uz": "'Uoll-strit bo'risi', 'Harli Kvinn' va 2023 yilgi rekordchi 'Barbi' filmidagi bosh roli bilan olamshumul yulduzga aylandi.", "ru": "Исполнительница культовой роли Барби (2023) и Харли Квинн, номинантка на премию «Оскар».", "en": "Brought Harley Quinn to life and starred in the $1.4 billion phenomenon 'Barbie' (2023)."}
    },
    {
        "id": "zendaya",
        "name": {"uz": "Zendaya", "ru": "Зендея", "en": "Zendaya"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Zendaya-byPhilipRomano.jpg/960px-Zendaya-byPhilipRomano.jpg",
        "aliases": ["zendaya", "zendaya coleman", "зендея", "зендая", "zendeya"],
        "fun_fact": {"uz": "'Eyforiya' serialidagi roli uchun Emmi mukofotini qo'lga kiritgan tarixdagi eng yosh aktrisa bo'ldi.", "ru": "Стала самой молодой обладательницей премии «Эмми» за лучшую женскую роль в драме («Эйфория»).", "en": "Became the youngest two-time winner of the Primetime Emmy Award for Lead Actress in a Drama ('Euphoria')."}
    },
    {
        "id": "jennifer_lawrence",
        "name": {"uz": "Jennifer Lourens", "ru": "Дженнифер Лоуренс", "en": "Jennifer Lawrence"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Die_My_Love_-_Cannes_2025_02_%28cropped%29.png",
        "aliases": ["jennifer lawrence", "katniss", "дженнифер лоуренс", "лоуренс", "jennifer lourens"],
        "fun_fact": {"uz": "'Ochlik o'yinlari' trilogiyasidagi Ketniss Everdin roli va 'Mening sevgilim — jinni' filmi uchun 22 yoshida Oskar oldi.", "ru": "В 22 года получила «Оскар» за фильм «Мой парень — псих», звезда саги «Голодные игры».", "en": "Won an Oscar at age 22 for 'Silver Linings Playbook' and led the blockbuster 'Hunger Games' franchise."}
    },
    {
        "id": "rowan_atkinson",
        "name": {"uz": "Rouen Atkinson", "ru": "Роуэн Аткинсон", "en": "Rowan Atkinson"},
        "category": "cinema",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Rowan_Atkinson%2C_2011.jpg",
        "aliases": ["rowan atkinson", "mr bean", "bean", "роуэн аткинсон", "мистер бин", "бин", "rouen atkinson", "mister bin"],
        "fun_fact": {"uz": "Dunyodagi eng sevimli komik obrazlardan biri — 'Mister Bin' yaratuvchisi va Oksford universiteti muhandislik magistri.", "ru": "Создатель легендарного мистера Бина, обладатель магистерской степени по электротехнике Оксфордского университета.", "en": "Created the globally beloved character Mr. Bean, holding an Electrical Engineering master's degree from Oxford."}
    },
    {
        "id": "jim_carrey",
        "name": {"uz": "Jim Kerri", "ru": "Джим Керри", "en": "Jim Carrey"},
        "category": "cinema",
        "country": {"uz": "Kanada", "ru": "Канада", "en": "Canada"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Jim_Carrey_2020_%28cropped2%29.jpg",
        "aliases": ["jim carrey", "carrey", "the mask", "джим керри", "керри", "маска", "эйс вентура", "jim kerri"],
        "fun_fact": {"uz": "'Maska', 'Eys Ventura' va 'Tryuman shousi' kabi filmlarda betakror yuz mimikasi bilan tanilgan buyuk komik.", "ru": "Мастер непревзойдённой пластической мимики, звезда фильмов «Маска», «Эйс Вентура» и «Шоу Трумана».", "en": "Renowned for his energetic slapstick performances in 'The Mask', 'Ace Ventura', and 'The Truman Show'."}
    },
    {
        "id": "charlie_chaplin",
        "name": {"uz": "Charli Chaplin", "ru": "Чарли Чаплин", "en": "Charlie Chaplin"},
        "category": "cinema",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Charlie_Chaplin_portrait_Getty_1739411952.jpg/960px-Charlie_Chaplin_portrait_Getty_1739411952.jpg",
        "aliases": ["charlie chaplin", "chaplin", "чарли чаплин", "чаплин", "charli chaplin"],
        "fun_fact": {"uz": "Ovozsiz kino davrining eng buyuk yulduzi, 'Kichik daydi' (The Tramp) obrazi bilan jahon madaniyatiga kirdi.", "ru": "Величайший комик эпохи немого кино, создатель бессмертного образа бродяги Чарли.", "en": "The towering icon of the silent film era through his screen persona, 'The Tramp'."}
    },
    {
        "id": "bruce_lee",
        "name": {"uz": "Bryus Li", "ru": "Брюс Ли", "en": "Bruce Lee"},
        "category": "cinema",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Bruce_Lee_as_Chen_Zhen_%284x5_cropped%29.jpg/960px-Bruce_Lee_as_Chen_Zhen_%284x5_cropped%29.jpg",
        "aliases": ["bruce lee", "lee", "брюс ли", "ли", "bryus li"],
        "fun_fact": {"uz": "Sharqona jang san'atini butun dunyoga tanitgan va Jeet Kune Do uslubiga asos solgan afsonaviy usta.", "ru": "Популяризировал восточные единоборства на Западе и создал боевое искусство джит кун-до.", "en": "Martial arts icon and pop culture pioneer who founded the philosophy of Jeet Kune Do."}
    },
    {
        "id": "michael_jackson",
        "name": {"uz": "Maykl Jekson", "ru": "Майкл Джексон", "en": "Michael Jackson"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Michael_Jackson_1983_%283x4_cropped%29_%28contrast%29.jpg/960px-Michael_Jackson_1983_%283x4_cropped%29_%28contrast%29.jpg",
        "aliases": ["michael jackson", "mj", "king of pop", "майкл джексон", "джексон", "король поп-музыки", "maykl jekson"],
        "fun_fact": {"uz": "'Pop qiroli'ning 'Thriller' albomi 70 milliondan ortiq sotilib, insoniyat tarixidagi eng ko'p sotilgan albom hisoblanadi.", "ru": "Его альбом «Thriller» разошёлся тиражом более 70 млн копий, став самым продаваемым в истории музыки.", "en": "'The King of Pop', whose landmark 1982 album 'Thriller' remains the best-selling album of all time."}
    },
    {
        "id": "eminem",
        "name": {"uz": "Eminem", "ru": "Эминем", "en": "Eminem"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Eminem_2021_Color_Corrected.jpg/960px-Eminem_2021_Color_Corrected.jpg",
        "aliases": ["eminem", "slim shady", "marshall mathers", "эминем", "слим шейди"],
        "fun_fact": {"uz": "'Rap God' qo'shig'ida 9.6 soniyada 97 ta so'z aytib, tarixdagi eng tezkor rep Ginnes rekordini o'rnatgan.", "ru": "В треке «Rap God» произнёс 97 слов за 9,6 секунды, установив мировой рекорд скорости читки.", "en": "In 'Rap God', he recited 97 words in just 9.6 seconds, setting a Guinness World Record."}
    },
    {
        "id": "freddie_mercury",
        "name": {"uz": "Freddi Merkyuri", "ru": "Фредди Меркьюри", "en": "Freddie Mercury"},
        "category": "music",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Freddie_Mercury_performing_in_New_Haven%2C_CT%2C_November_1977.jpg/960px-Freddie_Mercury_performing_in_New_Haven%2C_CT%2C_November_1977.jpg",
        "aliases": ["freddie mercury", "mercury", "queen", "фредди меркьюри", "меркьюри", "квин", "freddi merkyuri"],
        "fun_fact": {"uz": "Queen guruhining afsonaviy vokalisti, 'Bohemian Rhapsody' va 'We Are the Champions' qo'shiqlari muallifi.", "ru": "Вокалист группы Queen с уникальным 4-октавным голосом, автор шедевра «Bohemian Rhapsody».", "en": "Iconic frontman of Queen possessing a legendary four-octave vocal range, writer of 'Bohemian Rhapsody'."}
    },
    {
        "id": "shakira",
        "name": {"uz": "Shakira", "ru": "Шакира", "en": "Shakira"},
        "category": "music",
        "country": {"uz": "Kolumbiya", "ru": "Колумбия", "en": "Colombia"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/2023-11-16_Gala_de_los_Latin_Grammy%2C_03_%28cropped%2902.jpg/960px-2023-11-16_Gala_de_los_Latin_Grammy%2C_03_%28cropped%2902.jpg",
        "aliases": ["shakira", "шакира"],
        "fun_fact": {"uz": "2010 yilgi JCH rasmiy madhiyasi 'Waka Waka' va 'Hips Don't Lie' xitlari bilan Lotin Amerikasi musiqasi malikasi.", "ru": "Колумбийская певица, исполнительница всемирных суперхитов «Whenever, Wherever» и гимна ЧМ-2010 «Waka Waka».", "en": "Colombian superstar known as the 'Queen of Latin Music', whose 2010 anthem 'Waka Waka' became a global phenomenon."}
    },
    {
        "id": "beyonce",
        "name": {"uz": "Beyonse", "ru": "Бейонсе", "en": "Beyoncé"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Beyonc%C3%A9_-_Tottenham_Hotspur_Stadium_-_1st_June_2023_%2810_of_118%29_%2852946364598%29_%28best_crop%29.jpg",
        "aliases": ["beyonce", "queen bey", "бейонсе", "бейонс", "beyonse"],
        "fun_fact": {"uz": "32 ta Gremmi mukofoti bilan musiqa tarixida eng ko'p Gremmi yutgan san'atkor hisoblanadi.", "ru": "Рекордсменка в истории музыки по количеству выигранных премий «Грэмми» (32 награды).", "en": "The most awarded artist in Grammy history, having won an unprecedented 32 Grammy Awards."}
    },
    {
        "id": "taylor_swift",
        "name": {"uz": "Teylor Svift", "ru": "Тейлор Свифт", "en": "Taylor Swift"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Taylor_Swift_at_the_2023_MTV_Video_Music_Awards_%283%29.png/960px-Taylor_Swift_at_the_2023_MTV_Video_Music_Awards_%283%29.png",
        "aliases": ["taylor swift", "swift", "тейлор свифт", "свифт", "teylor svift"],
        "fun_fact": {"uz": "Tarixda 'Yil albomi' nominatsiyasida 4 marta Gremmi yutgan yagona xonanda, The Eras Tour bilan rekord qo'ydi.", "ru": "Единственная исполнительница в истории, четырежды побеждавшая в номинации «Альбом года» на «Грэмми».", "en": "The only artist to win Album of the Year at the Grammys four times; her Eras Tour is the highest-grossing in history."}
    },
    {
        "id": "rihanna",
        "name": {"uz": "Rianna", "ru": "Рианна", "en": "Rihanna"},
        "category": "music",
        "country": {"uz": "Barbados", "ru": "Барбадос", "en": "Barbados"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Rihanna_Fenty_2018.png",
        "aliases": ["rihanna", "riri", "рианна", "рири", "rianna"],
        "fun_fact": {"uz": "Barbados milliy qahramoni va Fenty Beauty imperiyasiga asos solgan milliarder xonanda.", "ru": "Национальный герой Барбадоса и основательница глобального бьюти-бренда Fenty Beauty.", "en": "National Hero of Barbados and billionaire businesswoman behind the beauty brand Fenty Beauty."}
    },
    {
        "id": "drake",
        "name": {"uz": "Dreyk", "ru": "Дрейк", "en": "Drake"},
        "category": "music",
        "country": {"uz": "Kanada", "ru": "Канада", "en": "Drake"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Drake_at_The_Carter_Effect_2017_%2836818935200%29_%28cropped%29.jpg",
        "aliases": ["drake", "champagnepapi", "дрейк", "aubrey graham"],
        "fun_fact": {"uz": "Billboard Hot 100 chartida eng ko'p qo'shig'i (300 dan ortiq) chiqqan tarixdagi mutlaq rekordchi.", "ru": "Абсолютный рекордсмен чарта Billboard Hot 100 по числу вошедших композиций (более 300 треков).", "en": "Holds the record for the most charted songs in the history of the Billboard Hot 100 (over 300 songs)."}
    },
    {
        "id": "the_weeknd",
        "name": {"uz": "The Weeknd", "ru": "The Weeknd", "en": "The Weeknd"},
        "category": "music",
        "country": {"uz": "Kanada", "ru": "Канада", "en": "Canada"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/The_Weeknd_Portrait_by_Brian_Ziff.jpg/960px-The_Weeknd_Portrait_by_Brian_Ziff.jpg",
        "aliases": ["the weeknd", "abel tesfaye", "weeknd", "уикенд", "зэ уикенд", "зе викенд"],
        "fun_fact": {"uz": "'Blinding Lights' xiti Billboard Hot 100 tarixidagi barcha davrlarning eng muvaffaqiyatli qo'shig'i deb topildi.", "ru": "Его хит «Blinding Lights» стал самой успешной песней в истории чарта Billboard Hot 100.", "en": "His global hit 'Blinding Lights' was ranked the No. 1 Greatest Hot 100 Song of All Time by Billboard."}
    },
    {
        "id": "bruno_mars",
        "name": {"uz": "Bruno Mars", "ru": "Бруно Марс", "en": "Bruno Mars"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/BrunoMars24KMagicWorldTourLive_%28cropped%29.jpg/960px-BrunoMars24KMagicWorldTourLive_%28cropped%29.jpg",
        "aliases": ["bruno mars", "бруно марс", "peter hernandez"],
        "fun_fact": {"uz": "'Uptown Funk', 'Just the Way You Are' xitlari bilan 15 ta Gremmi yutgan vokal va raqs ustasi.", "ru": "Обладатель 15 премий «Грэмми», прославившийся суперхитами «Uptown Funk» и «Grenade».", "en": "15-time Grammy winner celebrated for retro showmanship and chart-topping hits like 'Uptown Funk'."}
    },
    {
        "id": "ed_sheeran",
        "name": {"uz": "Ed Shiran", "ru": "Эд Ширан", "en": "Ed Sheeran"},
        "category": "music",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/03/Ed_Sheeran_2022_%283x4_crop%29.jpg",
        "aliases": ["ed sheeran", "sheeran", "эд ширан", "ширан", "ed shiran"],
        "fun_fact": {"uz": "'Shape of You' qo'shig'i Spotify platformasida 4 milliarddan ortiq tinglangan birinchi qo'shiq bo'ldi.", "ru": "Его трек «Shape of You» стал первой песней, преодолевшей отметку в 4 миллиарда прослушиваний на Spotify.", "en": "'Shape of You' became the first song in Spotify history to surpass 4 billion streams."}
    },
    {
        "id": "justin_bieber",
        "name": {"uz": "Jastin Biber", "ru": "Джастин Бибер", "en": "Justin Bieber"},
        "category": "music",
        "country": {"uz": "Kanada", "ru": "Канада", "en": "Canada"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6c/P20260719DT-1213_President_Donald_J._Trump_and_First_Lady_Melania_Trump_attend_the_FIFA_World_Cup_Final_%28cropped_2%29.jpg",
        "aliases": ["justin bieber", "bieber", "джастин бибер", "бибер", "jastin biber"],
        "fun_fact": {"uz": "YouTube orqali 13 yoshida kashf etilgan Biber Spotify platformasida oylik 100 million tinglovchiga yetgan birinchi san'atkordir.", "ru": "Открытый через YouTube в юном возрасте, Бибер стал первым артистом, набравшим 100 млн слушателей в месяц на Spotify.", "en": "Discovered on YouTube at age 13, became the first artist in Spotify history to cross 100 million monthly listeners."}
    },
    {
        "id": "adele",
        "name": {"uz": "Adel", "ru": "Адель", "en": "Adele"},
        "category": "music",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Adele_2016.jpg/960px-Adele_2016.jpg",
        "aliases": ["adele", "адель", "adel"],
        "fun_fact": {"uz": "'Someone Like You' va 'Hello' qo'shiqlari muallifi, 16 ta Gremmi va 'Skyfall' filmi uchun Oskar sovrindori.", "ru": "Исполнительница баллад «Rolling in the Deep» и «Hello», обладательница 16 «Грэмми» и «Оскара».", "en": "Soulful British vocalist behind 'Rolling in the Deep' and 'Hello', with 16 Grammys and an Oscar for 'Skyfall'."}
    },
    {
        "id": "billie_eilish",
        "name": {"uz": "Billi Aylish", "ru": "Билли Айлиш", "en": "Billie Eilish"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c7/BillieEilishO2140725-39_-_54665577407_%28cropped%29.jpg",
        "aliases": ["billie eilish", "eilish", "билли айлиш", "айлиш", "billi aylish"],
        "fun_fact": {"uz": "22 yoshidayoq ikkita Oskar mukofotini qo'lga kiritgan tarixdagi eng yosh shaxs bo'ldi.", "ru": "Стала самым молодым человеком в истории, выигравшим две премии «Оскар» к возрасту 22 лет.", "en": "Became the youngest person in history to win two Academy Awards at just 22 years of age."}
    },
    {
        "id": "lady_gaga",
        "name": {"uz": "Ledi Gaga", "ru": "Леди Гага", "en": "Lady Gaga"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Lady_Gaga_at_Joe_Biden%27s_inauguration_%28cropped_5%29.jpg/960px-Lady_Gaga_at_Joe_Biden%27s_inauguration_%28cropped_5%29.jpg",
        "aliases": ["lady gaga", "gaga", "леди гага", "гага", "stefani germanotta", "ledi gaga"],
        "fun_fact": {"uz": "'Bad Romance', 'Poker Face' va 'Shallow' xitlari orqali 13 ta Gremmi, Oskar va 'Oltin globus'ni qo'lga kiritdi.", "ru": "Звезда поп-музыки и кино, обладательница 13 премий «Грэмми» и премии «Оскар» за песню «Shallow».", "en": "Iconic performer with 13 Grammys and an Oscar for 'Shallow', renowned for theatrical style reinventions."}
    },
    {
        "id": "madonna",
        "name": {"uz": "Madonna", "ru": "Мадонна", "en": "Madonna"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/MadonnaO2171023_%2897_of_133%29_%2853269593787%29_%28cropped%29.jpg/960px-MadonnaO2171023_%2897_of_133%29_%2853269593787%29_%28cropped%29.jpg",
        "aliases": ["madonna", "мадонна", "queen of pop"],
        "fun_fact": {"uz": "Ginnes rekordlar kitobiga ko'ra 300 milliondan ortiq yozuv sotgan tarixdagi eng muvaffaqiyatli ayol san'atkor.", "ru": "Книга рекордов Гиннесса признала её самой продаваемой исполнительницей всех времён (более 300 млн копий).", "en": "Certified by Guinness World Records as the best-selling female recording artist of all time."}
    },
    {
        "id": "elvis_presley",
        "name": {"uz": "Elvis Presli", "ru": "Элвис Пресли", "en": "Elvis Presley"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Elvis_Presley_promoting_Jailhouse_Rock.jpg/960px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",
        "aliases": ["elvis presley", "elvis", "king of rock", "элвис пресли", "элвис", "elvis presli"],
        "fun_fact": {"uz": "'Rok-n-roll qiroli' XX asr musiqasida inqilob qilib, 500 milliondan ortiq plastinka sotgan.", "ru": "«Король рок-н-ролла», изменивший облик мировой популярной музыки в середине XX века.", "en": "The 'King of Rock and Roll', universally recognized as one of the most significant cultural figures of the 20th century."}
    },
    {
        "id": "bob_marley",
        "name": {"uz": "Bob Marli", "ru": "Боб Марли", "en": "Bob Marley"},
        "category": "music",
        "country": {"uz": "Yamayka", "ru": "Ямайка", "en": "Jamaica"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Bob_Marley_circa_1976_%28cropped%29.jpg/960px-Bob_Marley_circa_1976_%28cropped%29.jpg",
        "aliases": ["bob marley", "marley", "боб марли", "марли", "bob marli"],
        "fun_fact": {"uz": "Reggi musiqasini butun dunyoga tanitgan va tinchlik, mehr-oqibat ramziga aylangan buyuk musiqachi.", "ru": "Пионер стиля регги, превративший ямайскую музыку во всемирное культурное движение за мир и свободу.", "en": "Pioneered reggae music and became a global symbol of Jamaican culture, unity, and peace."}
    },
    {
        "id": "tupac_shakur",
        "name": {"uz": "Tupak Shakur", "ru": "Тупак Шакур", "en": "Tupac Shakur"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Tupac_Shakur_in_1995.jpg",
        "aliases": ["tupac", "2pac", "tupac shakur", "makaveli", "тупак", "2пак", "тупак шакур", "tupak shakur"],
        "fun_fact": {"uz": "Rep tarixidagi eng nufuzli va hurmatga sazovor shoir-ijrochilardan biri (75 milliondan ortiq albom sotgan).", "ru": "Один из величайших рэперов всех времён, чьи поэтические тексты поднимали острые социальные темы.", "en": "Widely considered one of the most influential and poetic hip-hop artists of all time."}
    },
    {
        "id": "snoop_dogg",
        "name": {"uz": "Snup Dogg", "ru": "Снуп Догг", "en": "Snoop Dogg"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Snoop_Dogg%2C_WrestleMania_XL_%28cropped%29_%28cropped%29.jpg",
        "aliases": ["snoop dogg", "snoop", "снуп догг", "снуп дог", "calvin broadus", "snup dogg"],
        "fun_fact": {"uz": "G'arbiy sohil repi afsonasi, Dr. Dre bilan 'Doggystyle' albomini chiqarib dunyoga mashhur bo'lgan.", "ru": "Легенда хип-хопа Западного побережья, известный своим расслабленным стилем и дружбой с Dr. Dre.", "en": "West Coast rap icon whose 1993 debut album 'Doggystyle' debuted at number one on the Billboard 200."}
    },
    {
        "id": "fifty_cent",
        "name": {"uz": "50 Cent", "ru": "50 Cent", "en": "50 Cent"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Curtis_%2250_Cent%22_Jackson_visits_Barksdale_AFB_%285%29_%28cropped%29.jpg/960px-Curtis_%2250_Cent%22_Jackson_visits_Barksdale_AFB_%285%29_%28cropped%29.jpg",
        "aliases": ["50 cent", "fifty cent", "curtis jackson", "50 цент", "фифти цент", "фифти"],
        "fun_fact": {"uz": "'Get Rich or Die Tryin' albomi bilan tanilgan, 9 ta o'q jarohatidan omon qolgan rep yulduzi.", "ru": "Выжил после девяти огнестрельных ранений и выпустил мультиплатиновый альбом «Get Rich or Die Tryin'».", "en": "Survived nine gunshot wounds to become a hip-hop megastar with his debut 'Get Rich or Die Tryin''."}
    },
    {
        "id": "kanye_west",
        "name": {"uz": "Kanye Uest", "ru": "Канье Уэст", "en": "Kanye West"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Kanye_West_at_the_2009_Tribeca_Film_Festival_%28crop_2%29.jpg/960px-Kanye_West_at_the_2009_Tribeca_Film_Festival_%28crop_2%29.jpg",
        "aliases": ["kanye west", "kanye", "ye", "канье уэст", "канье вест", "йе", "kanye uest"],
        "fun_fact": {"uz": "24 ta Gremmi mukofotiga sazovor bo'lgan va Yeezy moda brendini yaratgan innovator prodyuser.", "ru": "Обладатель 24 премий «Грэмми» и создатель революционной модной линии кроссовок Yeezy.", "en": "24-time Grammy winner widely celebrated for redefining hip-hop production and creating the Yeezy brand."}
    },
    {
        "id": "post_malone",
        "name": {"uz": "Post Maloun", "ru": "Пост Малоун", "en": "Post Malone"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Post_Malone_July_2021_%28cropped%29.jpg/960px-Post_Malone_July_2021_%28cropped%29.jpg",
        "aliases": ["post malone", "пост малон", "пост малоун", "austin post", "post maloun"],
        "fun_fact": {"uz": "'Sunflower' va 'Rockstar' treklari bilan RIAA tomonidan rekord darajadagi olmos (diamond) sertifikatlar olgan.", "ru": "Поставил рекорд по числу синглов с бриллиантовым статусом в США («Sunflower», «Rockstar»).", "en": "Holds the record for the most RIAA Diamond-certified singles in music history, including 'Sunflower'."}
    },
    {
        "id": "dua_lipa",
        "name": {"uz": "Dua Lipa", "ru": "Дуа Липа", "en": "Dua Lipa"},
        "category": "music",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Dua_Lipa-69798_%28cropped%29.jpg/960px-Dua_Lipa-69798_%28cropped%29.jpg",
        "aliases": ["dua lipa", "дуа липа", "дува липа"],
        "fun_fact": {"uz": "'Future Nostalgia' albomi bilan zamonaviy disko-pop janrini qayta tiriltirgan uch karra Gremmi sohibasi.", "ru": "Трёхкратная обладательница «Грэмми», возродившая моду на диско-поп альбомом «Future Nostalgia».", "en": "Three-time Grammy winner who revitalized disco-pop with her smash album 'Future Nostalgia'."}
    },
    {
        "id": "ariana_grande",
        "name": {"uz": "Ariana Grande", "ru": "Ариана Гранде", "en": "Ariana Grande"},
        "category": "music",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Ariana_Grande_promoting_Wicked_%282024%29.jpg",
        "aliases": ["ariana grande", "grande", "ариана гранде", "гранде", "ariana grande"],
        "fun_fact": {"uz": "4 oktavali qudratli vokal egasi, bir vaqtning o'zida Billboard Hot 100 ning birinchi 3 pog'onasini egallagan ikkinchi ijrochi.", "ru": "Обладает диапазоном в 4 октавы, повторила рекорд The Beatles, заняв первые три строчки Billboard Hot 100 одновременно.", "en": "Possesses a four-octave vocal range and matched The Beatles by occupying the top 3 spots of Billboard Hot 100."}
    },
    {
        "id": "elton_john",
        "name": {"uz": "Elton Jon", "ru": "Элтон Джон", "en": "Elton John"},
        "category": "music",
        "country": {"uz": "Buyuk Britaniya", "ru": "Великобритания", "en": "United Kingdom"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/61/EltonDocBFILFF101024_%284_of_17%29_%28cropped%29.jpg",
        "aliases": ["elton john", "элтон джон", "сэр элтон джон", "elton jon"],
        "fun_fact": {"uz": "Malika Diana xotirasiga bag'ishlangan 'Candle in the Wind 1997' qo'shig'i 33 million nusxada sotilib, tarixdagi eng ko'p sotilgan singl bo'ldi.", "ru": "Его сингл «Candle in the Wind 1997» в память о принцессе Диане разошёлся тиражом более 33 млн экземпляров.", "en": "His 1997 tribute to Princess Diana, 'Candle in the Wind', is the best-selling physical single in history."}
    },
    {
        "id": "celine_dion",
        "name": {"uz": "Selin Dion", "ru": "Селин Дион", "en": "Celine Dion"},
        "category": "music",
        "country": {"uz": "Kanada", "ru": "Канада", "en": "Canada"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f5/C%C3%A9line_Dion_2012.jpg",
        "aliases": ["celine dion", "селин дион", "selin dion"],
        "fun_fact": {"uz": "'Titanik' filmining afsonaviy 'My Heart Will Go On' saundtreki orqali jahon sahnasini zabt etgan.", "ru": "Исполнительница бессмертной темы к фильму «Титаник» — «My Heart Will Go On», продала более 200 млн альбомов.", "en": "Sold over 200 million albums worldwide, famed for the timeless 'Titanic' theme 'My Heart Will Go On'."}
    },
    {
        "id": "andrea_bocelli",
        "name": {"uz": "Andrea Bochelli", "ru": "Андреа Бочелли", "en": "Andrea Bocelli"},
        "category": "music",
        "country": {"uz": "Italiya", "ru": "Италия", "en": "Italy"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/AndreaBocelliMar10.jpg/960px-AndreaBocelliMar10.jpg",
        "aliases": ["andrea bocelli", "bocelli", "андреа бочелли", "бочелли", "andrea bochelli"],
        "fun_fact": {"uz": "12 yoshida ko'rish qobiliyatini yo'qotgan bo'lsa-da, dunyoning eng mashhur opera va klassik estrada tenoriga aylandi.", "ru": "Потерял зрение в 12 лет, но стал самым популярным классическим и оперным тенором в мире.", "en": "Blind since age 12, has sold over 75 million records as the world's most beloved classical-crossover tenor."}
    },
    {
        "id": "elon_musk",
        "name": {"uz": "Ilon Mask", "ru": "Илон Маск", "en": "Elon Musk"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Elon_Musk_-_54820081119_%28cropped%29.jpg/960px-Elon_Musk_-_54820081119_%28cropped%29.jpg",
        "aliases": ["elon musk", "musk", "tesla", "spacex", "илон маск", "маск", "ilon mask"],
        "fun_fact": {"uz": "Tesla, SpaceX asoschisi, qayta ishlatiladigan raketalar va elektromobillar inqilobchisi.", "ru": "Основатель SpaceX и глава Tesla, сделавший многоразовые космические ракеты и электромобили массовыми.", "en": "Founder of SpaceX and CEO of Tesla, revolutionizing electric vehicles and private space exploration."}
    },
    {
        "id": "steve_jobs",
        "name": {"uz": "Stiv Jobs", "ru": "Стив Джобс", "en": "Steve Jobs"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Steve_Jobs_Headshot_2010_%28cropped_4%29.jpg/960px-Steve_Jobs_Headshot_2010_%28cropped_4%29.jpg",
        "aliases": ["steve jobs", "jobs", "apple", "стив джобс", "джобс", "stiv jobs"],
        "fun_fact": {"uz": "Apple hammuassisi, iPhone, iPad va Macintosh kompyuterlari orqali texnologiya olamini tubdan o'zgartirgan daho.", "ru": "Сооснователь Apple, навсегда изменивший мир мобильных технологий выпуском iPhone и iPad.", "en": "Co-founder of Apple who transformed personal computing, music, and phones with the Mac, iPod, and iPhone."}
    },
    {
        "id": "bill_gates",
        "name": {"uz": "Bill Geyts", "ru": "Билл Гейтс", "en": "Bill Gates"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Bill_Gates_at_the_European_Commission_-_P067383-987995_%28cropped%29_5.jpg/960px-Bill_Gates_at_the_European_Commission_-_P067383-987995_%28cropped%29_5.jpg",
        "aliases": ["bill gates", "gates", "microsoft", "билл гейтс", "гейтс", "bill geyts"],
        "fun_fact": {"uz": "Microsoft asoschisi va Windows tizimi yaratuvchisi, uzoq yillar davomida dunyoning eng boy odami bo'lgan.", "ru": "Основатель корпорации Microsoft, создатель операционной системы Windows и филантроп.", "en": "Co-founder of Microsoft and creator of Windows, who led the personal computer revolution."}
    },
    {
        "id": "mark_zuckerberg",
        "name": {"uz": "Mark Sukerberg", "ru": "Марк Цукерберг", "en": "Mark Zuckerberg"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/12/P20260929DT-1655_%2855561811540%29_%28cropped_2%29.jpg",
        "aliases": ["mark zuckerberg", "zuckerberg", "meta", "facebook", "марк цукерберг", "цукерберг", "mark sukerberg"],
        "fun_fact": {"uz": "Garvard yotoqxonasida Facebook'ga asos solgan va 23 yoshida tarixdagi eng yosh o'zini o'zi milliarder qilgan shaxsga aylangan.", "ru": "Основал Facebook в общежитии Гарварда и стал самым молодым миллиардером в истории в возрасте 23 лет.", "en": "Founded Facebook in his Harvard dorm room and became the world's youngest self-made billionaire at age 23."}
    },
    {
        "id": "jeff_bezos",
        "name": {"uz": "Jeff Bezos", "ru": "Джефф Безос", "en": "Jeff Bezos"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/260202-D-PM193-2205_SECWAR_Arsenal_of_Freedom_Tour_-_Florida_%283x4_cropped_on_Bezos_and_rotated%29.jpg/960px-260202-D-PM193-2205_SECWAR_Arsenal_of_Freedom_Tour_-_Florida_%283x4_cropped_on_Bezos_and_rotated%29.jpg",
        "aliases": ["jeff bezos", "bezos", "amazon", "джефф безос", "безос", "dzheff bezos"],
        "fun_fact": {"uz": "Amazon kompaniyasiga o'z garajida onlayn kitob do'koni sifatida asos solgan va uni global savdo gigantiga aylantirgan.", "ru": "Основал Amazon в собственном гараже как книжный онлайн-магазин, построив крупнейшую торговую империю.", "en": "Founded Amazon in his garage as an online bookstore, building it into the world's largest online retailer."}
    },
    {
        "id": "pavel_durov",
        "name": {"uz": "Pavel Durov", "ru": "Павел Дуров", "en": "Pavel Durov"},
        "category": "tech",
        "country": {"uz": "BAA", "ru": "ОАЭ", "en": "United Arab Emirates"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/44/Pavel_Durov_sitting_portrait_%28cropped%29.jpg",
        "aliases": ["pavel durov", "durov", "telegram", "vk", "павел дуров", "дуров"],
        "fun_fact": {"uz": "Telegram messenjeri va VKontakte ijtimoiy tarmog'i asoschisi, shaxsiy daxlsizlik va erkinlik tarafdori.", "ru": "Создатель мессенджера Telegram и социальной сети ВКонтакте, защитник конфиденциальности данных.", "en": "Founder of Telegram and VKontakte, known as a staunch advocate for privacy and freedom of speech."}
    },
    {
        "id": "sam_altman",
        "name": {"uz": "Sem Altman", "ru": "Сэм Альтман", "en": "Sam Altman"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Meeting_with_Masayoshi_Son_and_Sam_Altman_%28February_3%2C_2025%29_%283x4_cropped_on_Altman%29.jpg",
        "aliases": ["sam altman", "altman", "openai", "chatgpt", "сэм альтман", "альтман", "sem altman"],
        "fun_fact": {"uz": "OpenAI bosh direktori bo'lib, ChatGPT va generativ sun'iy intellekt inqilobining asosiy yetakchisi.", "ru": "Генеральный директор OpenAI, стоящий во главе революции искусственного интеллекта и ChatGPT.", "en": "CEO of OpenAI and prominent leader of the generative artificial intelligence boom with ChatGPT."}
    },
    {
        "id": "jensen_huang",
        "name": {"uz": "Jensen Xuang", "ru": "Дженсен Хуанг", "en": "Jensen Huang"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Jen-Hsun_Huang_2025.jpg",
        "aliases": ["jensen huang", "huang", "nvidia", "дженсен хуанг", "хуанг", "jensen xuang"],
        "fun_fact": {"uz": "Nvidia asoschisi va rahbari, o'zining charm kurtkasi va SI grafik chiplari inqilobi bilan mashhur.", "ru": "Сооснователь и бессменный глава Nvidia, превративший компанию в триллионного лидера эпохи ИИ.", "en": "Co-founder and CEO of Nvidia, turning GPUs into the computational backbone of modern AI."}
    },
    {
        "id": "tim_cook",
        "name": {"uz": "Tim Kuk", "ru": "Тим Кук", "en": "Tim Cook"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Tim_Cook_in_New_York_City_-_2026_%28cropped%29.jpg/960px-Tim_Cook_in_New_York_City_-_2026_%28cropped%29.jpg",
        "aliases": ["tim cook", "cook", "apple", "тим кук", "кук", "tim kuk"],
        "fun_fact": {"uz": "2011 yildan buyon Apple bosh direktori bo'lib, kompaniya kapitallashuvini 3 trillion dollarga yetkazdi.", "ru": "Возглавил Apple в 2011 году и сделал её первой компанией в мире с капитализацией более 3 триллионов долларов.", "en": "CEO of Apple since 2011, making Apple the first public company to reach a $3 trillion valuation."}
    },
    {
        "id": "sundar_pichai",
        "name": {"uz": "Sundar Pichai", "ru": "Сундар Пичаи", "en": "Sundar Pichai"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Sundar_Pichai_-_2023_%28cropped%29.jpg",
        "aliases": ["sundar pichai", "pichai", "google", "сундар пичаи", "пичаи"],
        "fun_fact": {"uz": "Google Chrome brauzerini yaratishga boshchilik qilgan va Alphabet hamda Google bosh direktori bo'ldi.", "ru": "Руководил созданием Google Chrome, а затем стал генеральным директором Google и холдинга Alphabet.", "en": "Led the development of Google Chrome before rising to become CEO of Alphabet and Google."}
    },
    {
        "id": "larry_page",
        "name": {"uz": "Larri Peyj", "ru": "Ларри Пейдж", "en": "Larry Page"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Larry_Page_in_the_European_Parliament%2C_17.06.2009_%28cropped_2%29.jpg",
        "aliases": ["larry page", "page", "google", "ларри пейдж", "пейдж", "larri peyj"],
        "fun_fact": {"uz": "Sergey Brin bilan birga Stenfordda Google qidiruv tizimiga va PageRank algoritmi asosiga asos soldi.", "ru": "Сооснователь Google, разработавший вместе с Сергеем Брином революционный алгоритм PageRank.", "en": "Co-founder of Google who co-invented the PageRank search ranking algorithm at Stanford."}
    },
    {
        "id": "warren_buffett",
        "name": {"uz": "Uorren Baffet", "ru": "Уоррен Баффетт", "en": "Warren Buffett"},
        "category": "tech",
        "country": {"uz": "AQSH", "ru": "США", "en": "United States"},
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Warren_Buffett_at_the_2015_SelectUSA_Investment_Summit_%28cropped%29.jpg",
        "aliases": ["warren buffett", "buffett", "berkshire", "уоррен баффетт", "баффетт", "uorren baffet"],
        "fun_fact": {"uz": "'Omaxa donishmandi' laqabli tarixdagi eng muvaffaqiyatli investor, Berkshire Hathaway rahbari.", "ru": "«Оракул из Омахи», признан самым успешным и легендарным инвестором в мировой истории.", "en": "The 'Oracle of Omaha', widely considered the greatest long-term investor in history."}
    },
]

CELEBRITIES_BY_ID: Dict[str, Dict[str, Any]] = {c["id"]: c for c in CELEBRITIES}


def get_celebrity_by_id(cid: str) -> Optional[Dict[str, Any]]:
    """Retrieve a celebrity entry by its unique string identifier."""
    return CELEBRITIES_BY_ID.get(cid)


def get_random_celebrities(count: int = 1, category: Optional[str] = None) -> List[Dict[str, Any]]:
    """Sample random celebrities without replacement, optionally filtered by category."""
    pool = CELEBRITIES
    if category:
        pool = [c for c in pool if c.get("category") == category]
    if not pool:
        return []
    return random.sample(pool, min(count, len(pool)))


def search_celebrity_by_alias(query: str) -> Optional[Dict[str, Any]]:
    """Find a celebrity matching a user input string across aliases or names."""
    q = query.strip().lower()
    if not q:
        return None
    for c in CELEBRITIES:
        if q in c.get("aliases", []):
            return c
        for val in c.get("name", {}).values():
            if q == val.lower():
                return c
    return None
