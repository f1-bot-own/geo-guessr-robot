# -*- coding: utf-8 -*-
"""
World Logos & Brands Database for GeoGuru Telegram Bot (Guess The Logo Mode).
Contains 120 globally recognized brands and crests across tech, automotive,
fashion, top football clubs, and food & beverage.
Each entry includes multilingual names, category, country code, clean high-resolution logo,
comprehensive chat-answering aliases, and engaging fun facts.
"""

import random
from typing import Optional, List, Dict, Any

LOGOS: List[Dict[str, Any]] = [
    {
        "id": "apple",
        "name": {"uz": "Apple", "ru": "Apple", "en": "Apple"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/960px-Apple_logo_black.svg.png",
        "aliases": ["apple", "epl", "эппл", "appl", "айфон", "iphone"],
        "fun_fact": {"uz": "Apple logotipidagi tishlangan olma gilos yoki pomidor bilan adashtirmaslik uchun ataylab shunday chizilgan.", "ru": "Надкусанное яблоко в логотипе Apple было придумано дизайнером Робом Яновым, чтобы его не путали с вишней.", "en": "The bite in the Apple logo was designed by Rob Janoff so people wouldn't confuse it with a cherry or tomato."}
    },
    {
        "id": "google",
        "name": {"uz": "Google", "ru": "Google", "en": "Google"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/960px-Google_2015_logo.svg.png",
        "aliases": ["google", "gugl", "гугл"],
        "fun_fact": {"uz": "Google nomi 'Googol' — 1 raqamidan keyin 100 ta nol keladigan ulkan son nomining noto'g'ri yozilishidan kelib chiqqan.", "ru": "Название Google произошло от числа 'гугол' (единица со 100 нулями) из-за опечатки основателей.", "en": "The name Google originated from a misspelling of 'googol', the number 1 followed by 100 zeros."}
    },
    {
        "id": "microsoft",
        "name": {"uz": "Microsoft", "ru": "Microsoft", "en": "Microsoft"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Microsoft_logo_%282012%29.svg/960px-Microsoft_logo_%282012%29.svg.png",
        "aliases": ["microsoft", "maykrosoft", "майкрософт", "микрософт", "ms"],
        "fun_fact": {"uz": "Microsoft logotipidagi to'rtta rangli kvadrat Windows, Office, Xbox va Bing mahsulotlarini ifodalaydi.", "ru": "Четыре цветных квадрата в логотипе Microsoft символизируют ключевые продукты: Windows, Office, Xbox и Bing.", "en": "The four colored squares in the Microsoft logo represent its core products: Windows, Office, Xbox, and Bing."}
    },
    {
        "id": "telegram",
        "name": {"uz": "Telegram", "ru": "Telegram", "en": "Telegram"},
        "category": "tech",
        "country_code": "ae",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/960px-Telegram_logo.svg.png",
        "aliases": ["telegram", "telegra", "телеграм", "телеграмм", "телега", "tg"],
        "fun_fact": {"uz": "Telegramning qog'oz samolyot ramzi erkinlik, tezlik va chegaralarsiz muloqotni aks ettiradi.", "ru": "Логотип бумажного самолётика Telegram олицетворяет лёгкость, скорость и свободу общения без цензуры.", "en": "Telegram's paper plane emblem represents lightness, speed, and unrestricted freedom of communication."}
    },
    {
        "id": "instagram",
        "name": {"uz": "Instagram", "ru": "Instagram", "en": "Instagram"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/960px-Instagram_logo_2022.svg.png",
        "aliases": ["instagram", "insta", "инстаграм", "инста", "ig"],
        "fun_fact": {"uz": "Instagram dastlab 'Burbn' deb atalgan va 2012 yilda Facebook tomonidan 1 milliard dollarga sotib olingan.", "ru": "Изначально приложение называлось Burbn, а в 2012 году Facebook купил его за рекордный 1 миллиард долларов.", "en": "Originally called Burbn, Instagram was acquired by Facebook in 2012 for $1 billion with only 13 employees."}
    },
    {
        "id": "youtube",
        "name": {"uz": "YouTube", "ru": "YouTube", "en": "YouTube"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/960px-YouTube_full-color_icon_%282017%29.svg.png",
        "aliases": ["youtube", "yutub", "ютуб", "ютубчик", "yt"],
        "fun_fact": {"uz": "YouTube'dagi birinchi video 'Me at the zoo' bo'lib, 2005 yil aprel oyida Javad Karim tomonidan yuklangan.", "ru": "Первым видео на YouTube стал ролик «Me at the zoo», загруженный сооснователем Джаведом Каримом в апреле 2005 года.", "en": "The first video uploaded to YouTube was 'Me at the zoo' by co-founder Jawed Karim on April 23, 2005."}
    },
    {
        "id": "tiktok",
        "name": {"uz": "TikTok", "ru": "TikTok", "en": "TikTok"},
        "category": "tech",
        "country_code": "cn",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/TikTok_logo.svg/960px-TikTok_logo.svg.png",
        "aliases": ["tiktok", "tik tok", "тикток", "тик ток", "tt"],
        "fun_fact": {"uz": "Xitoyda TikTok 'Douyin' deb ataladi va uning logotipi kontsert sahnasidagi elektr musiqiy notani eslatadi.", "ru": "В Китае приложение известно как Douyin, а его логотип стилизован под вибрирующую музыкальную ноту.", "en": "Known as Douyin in China, TikTok's logo represents a vibrant musical note with digital glitch effects."}
    },
    {
        "id": "netflix",
        "name": {"uz": "Netflix", "ru": "Netflix", "en": "Netflix"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Netflix_2015_logo.svg/960px-Netflix_2015_logo.svg.png",
        "aliases": ["netflix", "netfliks", "нетфликс"],
        "fun_fact": {"uz": "Netflix 1997 yilda pochta orqali DVD disklarni ijaraga beruvchi xizmat sifatida ish boshlagan.", "ru": "Netflix начинал в 1997 году как служба доставки DVD-дисков по почте в красных конвертах.", "en": "Netflix started in 1997 as a DVD-by-mail rental service before pioneering global video streaming."}
    },
    {
        "id": "tesla",
        "name": {"uz": "Tesla", "ru": "Tesla", "en": "Tesla"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Tesla_Motors.svg/960px-Tesla_Motors.svg.png",
        "aliases": ["tesla", "тесла"],
        "fun_fact": {"uz": "Tesla logotipidagi 'T' harfi elektr motorining ko'ndalang kesimini (rotor qismini) ifodalaydi.", "ru": "Буква «T» в логотипе Tesla схематически изображает поперечное сечение ротора электродвигателя.", "en": "The 'T' in Tesla's logo represents a cross-section of an electric motor rotor."}
    },
    {
        "id": "samsung",
        "name": {"uz": "Samsung", "ru": "Samsung", "en": "Samsung"},
        "category": "tech",
        "country_code": "kr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Samsung_logo.svg/960px-Samsung_logo.svg.png",
        "aliases": ["samsung", "samusng", "самсунг"],
        "fun_fact": {"uz": "Koreys tilida 'Samsung' so'zi 'uch yulduz' degan ma'noni anglatadi va abadiy qudratni bildiradi.", "ru": "Название Samsung переводится с корейского как «три звезды», символизируя нечто большое и вечное.", "en": "Samsung means 'three stars' in Korean, chosen to represent something vast, numerous, and eternal."}
    },
    {
        "id": "spotify",
        "name": {"uz": "Spotify", "ru": "Spotify", "en": "Spotify"},
        "category": "tech",
        "country_code": "se",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Spotify_icon.svg/960px-Spotify_icon.svg.png",
        "aliases": ["spotify", "spotifay", "спотифай", "спотик"],
        "fun_fact": {"uz": "Shvetsiyada asos solingan Spotify logotipidagi uchta to'lqinli chiziq musiqiy to'lqinlarni ifodalaydi.", "ru": "Три звуковые волны в зелёном круге логотипа Spotify олицетворяют потоковую передачу музыки.", "en": "Founded in Sweden, Spotify's logo features three curved lines representing sound waves and music streaming."}
    },
    {
        "id": "amazon",
        "name": {"uz": "Amazon", "ru": "Amazon", "en": "Amazon"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/960px-Amazon_logo.svg.png",
        "aliases": ["amazon", "amozon", "амазон"],
        "fun_fact": {"uz": "Amazon logotipidagi sariq o'q 'A' harfidan 'Z' harfiga yo'naltirilgan bo'lib, hamma narsa borligini va tabassumni bildiradi.", "ru": "Стрелка в логотипе Amazon соединяет буквы 'A' и 'Z', символизируя, что в магазине есть всё от А до Я, а также улыбку покупателя.", "en": "The yellow arrow in the Amazon logo points from 'A' to 'Z', meaning they sell everything from A to Z with a customer smile."}
    },
    {
        "id": "facebook",
        "name": {"uz": "Facebook", "ru": "Facebook", "en": "Facebook"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Facebook_Logo_2023.png/960px-Facebook_Logo_2023.png",
        "aliases": ["facebook", "fb", "meta", "фейсбук", "фб"],
        "fun_fact": {"uz": "Facebook'ning ko'k rangda bo'lishining sababi Mark Sukerbergning qizil-yashil daltonik bo'lganidir.", "ru": "Синий цвет Facebook был выбран потому, что Марк Цукерберг страдает дейтеранопией (дальтонизмом на красно-зелёные цвета).", "en": "Facebook is blue because Mark Zuckerberg has red-green color blindness, and blue is the color he sees best."}
    },
    {
        "id": "twitter",
        "name": {"uz": "Twitter", "ru": "Twitter", "en": "Twitter"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/960px-Logo_of_Twitter.svg.png",
        "aliases": ["twitter", "x", "tvitter", "твиттер", "икс"],
        "fun_fact": {"uz": "Twitter'ning afsonaviy ko'k qushchasi 'Larri' deb atalgan (basketbolchi Larri Byord sharafiga).", "ru": "Знаменитую синюю птичку Twitter звали «Ларри» — в честь легендарного баскетболиста Ларри Бёрда.", "en": "Twitter's original blue bird icon was named 'Larry the Bird' after NBA legend Larry Bird."}
    },
    {
        "id": "whatsapp",
        "name": {"uz": "WhatsApp", "ru": "WhatsApp", "en": "WhatsApp"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/960px-WhatsApp.svg.png",
        "aliases": ["whatsapp", "vatsap", "ватсап", "вацап", "вотсап", "wa"],
        "fun_fact": {"uz": "WhatsApp nomi inglizcha 'What's up?' ('Nima gap?') so'zlashuv iborasidan olingan.", "ru": "Название WhatsApp — это игра слов от популярного английского приветствия «What's up?» («Как дела?»).", "en": "The name WhatsApp is a clever play on the casual greeting 'What's up?' and 'App'."}
    },
    {
        "id": "linkedin",
        "name": {"uz": "LinkedIn", "ru": "LinkedIn", "en": "LinkedIn"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/LinkedIn_2021.svg/960px-LinkedIn_2021.svg.png",
        "aliases": ["linkedin", "linked in", "линкедин", "линкедин"],
        "fun_fact": {"uz": "Dunyodagi eng yirik professional ish tarmog'i bo'lib, 1 milliarddan ortiq a'zoga ega.", "ru": "Крупнейшая в мире профессиональная деловая сеть, объединяющая более 1 миллиарда специалистов.", "en": "The world's largest professional networking platform, with over 1 billion registered members worldwide."}
    },
    {
        "id": "pinterest",
        "name": {"uz": "Pinterest", "ru": "Pinterest", "en": "Pinterest"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Pinterest_Logo.svg/960px-Pinterest_Logo.svg.png",
        "aliases": ["pinterest", "пинтерест"],
        "fun_fact": {"uz": "Pinterest logotipidagi 'P' harfi doskaga qadaladigan nina (pin) shaklida yaratilgan.", "ru": "Буква «P» в логотипе Pinterest стилизована под канцелярскую кнопку-булавку (pin).", "en": "The letter 'P' in Pinterest's logo is subtly designed to resemble a pushpin."}
    },
    {
        "id": "snapchat",
        "name": {"uz": "Snapchat", "ru": "Snapchat", "en": "Snapchat"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Snapchat_logo.svg/960px-Snapchat_logo.svg.png",
        "aliases": ["snapchat", "snepchat", "снэпчат", "снапчат", "snap"],
        "fun_fact": {"uz": "Snapchat'ning arvoh ko'rinishidagi maskoti 'Ghostface Chillah' deb ataladi.", "ru": "Белое привидение на жёлтом фоне логотипа Snapchat зовут Ghostface Chillah (в честь рэпера из Wu-Tang Clan).", "en": "Snapchat's ghost mascot is officially named 'Ghostface Chillah', inspired by Ghostface Killah of Wu-Tang Clan."}
    },
    {
        "id": "reddit",
        "name": {"uz": "Reddit", "ru": "Reddit", "en": "Reddit"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/Reddit_logo_2023.svg/960px-Reddit_logo_2023.svg.png",
        "aliases": ["reddit", "реддит"],
        "fun_fact": {"uz": "Reddit'ning to'q qizil ko'zli o'zga sayyoralik ramzi 'Snoo' deb nomlangan.", "ru": "Маскота Reddit — забавного инопланетянина с антенной — зовут Snoo (сокращение от 'What's new?').", "en": "The alien mascot of Reddit is officially named 'Snoo', short for 'What's new?'."}
    },
    {
        "id": "discord",
        "name": {"uz": "Discord", "ru": "Discord", "en": "Discord"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Discord_Color_Text_Logo_%282015-2021%29.svg/960px-Discord_Color_Text_Logo_%282015-2021%29.svg.png",
        "aliases": ["discord", "diskord", "дискорд", "дс"],
        "fun_fact": {"uz": "Discord logotipidagi geympad ko'rinishidagi maskot 'Clyde' deb ataladi.", "ru": "Маскота-робота в виде игрового геймпада на логотипе Discord зовут Клайд (Clyde).", "en": "The friendly smiling gamepad robot mascot in the Discord logo is officially named Clyde."}
    },
    {
        "id": "twitch",
        "name": {"uz": "Twitch", "ru": "Twitch", "en": "Twitch"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Twitch_logo.svg/960px-Twitch_logo.svg.png",
        "aliases": ["twitch", "tvich", "твич"],
        "fun_fact": {"uz": "Twitch logotipidagi ikki ko'zli suhbat buluti 'Glitch' deb ataladi.", "ru": "Символ чата с двумя прямоугольными глазами на логотипе стриминга Twitch называется Glitch.", "en": "The iconic purple chat bubble with eyes in the Twitch logo is officially known as 'Glitch'."}
    },
    {
        "id": "sony",
        "name": {"uz": "Sony", "ru": "Sony", "en": "Sony"},
        "category": "tech",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Sony_logo.svg/960px-Sony_logo.svg.png",
        "aliases": ["sony", "soni", "сони"],
        "fun_fact": {"uz": "Sony nomi lotincha 'sonus' (ovoz) va yaponcha 'sonny boy' (chaqqon yigit) so'zlarining uyg'unligidan paydo bo'lgan.", "ru": "Название Sony происходит от латинского слова 'sonus' (звук) и популярного сленга 'sonny boy' (смышлёный парень).", "en": "The name Sony comes from the Latin 'sonus' (sound) and the 1950s American slang 'sonny boy'."}
    },
    {
        "id": "nintendo",
        "name": {"uz": "Nintendo", "ru": "Nintendo", "en": "Nintendo"},
        "category": "tech",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Nintendo.svg/960px-Nintendo.svg.png",
        "aliases": ["nintendo", "нинтендо"],
        "fun_fact": {"uz": "Nintendo 1889 yilda Kiotoda yapon o'yin kartalari (hanafuda) ishlab chiqaruvchi korxona sifatida tashkil etilgan.", "ru": "Nintendo была основана в Киото ещё в 1889 году как фабрика по производству игральных карт ханафуда.", "en": "Nintendo was founded in Kyoto in 1889 as a handmade hanafuda playing cards company."}
    },
    {
        "id": "playstation",
        "name": {"uz": "PlayStation", "ru": "PlayStation", "en": "PlayStation"},
        "category": "tech",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/PlayStation_logo_and_wordmark.svg/960px-PlayStation_logo_and_wordmark.svg.png",
        "aliases": ["playstation", "ps", "ps5", "плейстейшн", "сони плейстейшн"],
        "fun_fact": {"uz": "PlayStation geympadidagi ramzlar ma'noga ega: Uchburchak — nigoh, Kvadrat — menyu/qog'oz, Doira va X — Ha va Yo'q.", "ru": "Символы на геймпаде PlayStation имеют смысл: Треугольник — направление взгляда, Квадрат — документ/меню, Круг и Крест — «Да» и «Нет».", "en": "PlayStation controller buttons were designed with meaning: Triangle for viewpoint, Square for document/menu, Circle and Cross for Yes/No."}
    },
    {
        "id": "xbox",
        "name": {"uz": "Xbox", "ru": "Xbox", "en": "Xbox"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Xbox_one_logo.svg/960px-Xbox_one_logo.svg.png",
        "aliases": ["xbox", "x-box", "иксбокс", "хбокс"],
        "fun_fact": {"uz": "Dastlab konsol Microsoft DirectX texnologiyasi sharafiga 'DirectX Box' deb nomlangan, keyin Xbox deb qisqartirilgan.", "ru": "Консоль изначально называлась «DirectX Box» в честь графической технологии Microsoft DirectX.", "en": "Xbox was originally named 'DirectX Box', referencing Microsoft's DirectX graphics technology."}
    },
    {
        "id": "intel",
        "name": {"uz": "Intel", "ru": "Intel", "en": "Intel"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Intel_logo_2023.svg/960px-Intel_logo_2023.svg.png",
        "aliases": ["intel", "intil", "интел"],
        "fun_fact": {"uz": "Intel nomi 'Integrated Electronics' (Integrallashgan elektronika) so'zlarining qisqartmasidir.", "ru": "Название Intel образовано сокращением от «Integrated Electronics» (интегральная электроника).", "en": "Intel is a portmanteau of the words 'Integrated Electronics'."}
    },
    {
        "id": "nvidia",
        "name": {"uz": "Nvidia", "ru": "Nvidia", "en": "Nvidia"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Nvidia_logo.svg/960px-Nvidia_logo.svg.png",
        "aliases": ["nvidia", "invidia", "энвидиа", "нвидиа", "видеокарта"],
        "fun_fact": {"uz": "Nvidia nomi lotincha 'invidia' (hasad) so'zidan kelib chiqqan bo'lib, 'barchaning havasi keladigan tezlik' degan ma'noni anglatadi.", "ru": "Название Nvidia происходит от латинского слова 'invidia' (зависть), отсюда же зелёный фирменный цвет «зелёной зависти».", "en": "Nvidia comes from the Latin word 'invidia' (envy), inspiring its signature 'green with envy' branding."}
    },
    {
        "id": "amd",
        "name": {"uz": "AMD", "ru": "AMD", "en": "AMD"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/AMD_Logo.svg/960px-AMD_Logo.svg.png",
        "aliases": ["amd", "амд", "ryzen", "radeon"],
        "fun_fact": {"uz": "AMD 'Advanced Micro Devices' nomining qisqartmasi bo'lib, 1969 yilda Silikon vodiysida tashkil topgan.", "ru": "Аббревиатура AMD расшифровывается как «Advanced Micro Devices», компания была создана ещё в 1969 году.", "en": "AMD stands for 'Advanced Micro Devices', founded in Silicon Valley in 1969."}
    },
    {
        "id": "dell",
        "name": {"uz": "Dell", "ru": "Dell", "en": "Dell"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Dell_logo_2016.svg/960px-Dell_logo_2016.svg.png",
        "aliases": ["dell", "del", "делл"],
        "fun_fact": {"uz": "Maykl Dell 19 yoshida Texas universiteti yotoqxonasida 1000 dollar sarmoya bilan kompaniyani boshlagan.", "ru": "Майкл Делл основал компанию в 19 лет в комнате университетского общежития со стартовым капиталом всего $1000.", "en": "Michael Dell founded the computer giant at age 19 from his University of Texas dorm room with just $1,000."}
    },
    {
        "id": "hp",
        "name": {"uz": "HP", "ru": "HP", "en": "HP"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/HP_logo_2012.svg/960px-HP_logo_2012.svg.png",
        "aliases": ["hp", "hewlett packard", "эйчпи", "хп"],
        "fun_fact": {"uz": "Asoschilar Bill Xyulett va Deyv Pakkard kompaniya nomida kimning familiyasi birinchi turishini tanga tashlab hal qilishgan.", "ru": "Основатели Билл Хьюлетт и Дэйв Паккард бросили монетку, чтобы решить, чья фамилия будет стоять первой в названии.", "en": "Founders Bill Hewlett and Dave Packard flipped a coin to decide whether the company would be HP or PH."}
    },
    {
        "id": "lenovo",
        "name": {"uz": "Lenovo", "ru": "Lenovo", "en": "Lenovo"},
        "category": "tech",
        "country_code": "cn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Lenovo_logo_2015.svg/960px-Lenovo_logo_2015.svg.png",
        "aliases": ["lenovo", "леново", "thinkpad"],
        "fun_fact": {"uz": "Dunyodagi eng yirik shaxsiy kompyuter ishlab chiqaruvchisi bo'lib, 2005 yilda IBM PC biznesini sotib olgan.", "ru": "Крупнейший в мире производитель персональных компьютеров, выкупивший подразделение IBM PC в 2005 году.", "en": "The world's largest PC manufacturer, which acquired IBM's personal computer division in 2005."}
    },
    {
        "id": "xiaomi",
        "name": {"uz": "Xiaomi", "ru": "Xiaomi", "en": "Xiaomi"},
        "category": "tech",
        "country_code": "cn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Xiaomi_logo_%282021-%29.svg/960px-Xiaomi_logo_%282021-%29.svg.png",
        "aliases": ["xiaomi", "mi", "сяоми", "ксиоми", "шаоми"],
        "fun_fact": {"uz": "Xitoycha 'Xiaomi' so'zi 'mayda guruch' degan ma'noni anglatadi va kamtarlikni ifodalaydi.", "ru": "Слово «Xiaomi» переводится с китайского как «маленькое пшено» или «просо», символизируя скромность и упорный труд.", "en": "Xiaomi literally translates to 'little rice' in Chinese, representing a Buddhist philosophy of starting small."}
    },
    {
        "id": "huawei",
        "name": {"uz": "Huawei", "ru": "Huawei", "en": "Huawei"},
        "category": "tech",
        "country_code": "cn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Huawei_wordmark.svg/960px-Huawei_wordmark.svg.png",
        "aliases": ["huawei", "хуавей", "хуавэй"],
        "fun_fact": {"uz": "Huawei logotipi qizil xrizantema guli yaproqlarini va doimiy yuksalishni bildiradi.", "ru": "Лепестки на красном логотипе Huawei символизируют соцветие хризантемы и непрерывное развитие.", "en": "The petals of the Huawei logo resemble a blooming chrysanthemum flower and spreading rays of sunlight."}
    },
    {
        "id": "uber",
        "name": {"uz": "Uber", "ru": "Uber", "en": "Uber"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Uber_logo_2018.svg/960px-Uber_logo_2018.svg.png",
        "aliases": ["uber", "yuber", "юбер", "убер"],
        "fun_fact": {"uz": "Uber g'oyasi 2008 yilda Parijda qorli oqshomda taksi topa olmagan asoschilarning boshiga kelgan.", "ru": "Идея Uber родилась снежным вечером в Париже в 2008 году, когда основатели не смогли поймать такси.", "en": "Uber was conceived on a snowy winter evening in Paris in 2008 when the founders couldn't find a cab."}
    },
    {
        "id": "airbnb",
        "name": {"uz": "Airbnb", "ru": "Airbnb", "en": "Airbnb"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Airbnb_Logo.svg/960px-Airbnb_Logo.svg.png",
        "aliases": ["airbnb", "эйрбнб", "эирбнб"],
        "fun_fact": {"uz": "Aslida 'AirBed & Breakfast' nomi bilan ochilgan bo'lib, dastlab mehmonlarga shishiriladigan havo matrasi ijaraga berilgan.", "ru": "Название расшифровывается как «AirBed & Breakfast» (надувной матрас и завтрак), с аренды которого основатели и начинали.", "en": "Short for 'AirBed & Breakfast', started when the founders rented out an air mattress in their living room."}
    },
    {
        "id": "wikipedia",
        "name": {"uz": "Vikipediya", "ru": "Википедия", "en": "Wikipedia"},
        "category": "tech",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/960px-Wikipedia-logo-v2.svg.png",
        "aliases": ["wikipedia", "википедия", "vikipediya", "wiki"],
        "fun_fact": {"uz": "Vikipediyaning boshqotirma shari turli tillardagi alifbo harflari bilan to'ldirilgan va hali tugallanmagan bilimlarni anglatadi.", "ru": "Пазл-сфера логотипа Википедии состоит из фрагментов с глифами разных письменностей мира, показывая незавершённость сбора знаний.", "en": "The unfinished puzzle globe logo of Wikipedia symbolizes that knowledge is always expanding and never complete."}
    },
    {
        "id": "bmw",
        "name": {"uz": "BMW", "ru": "BMW", "en": "BMW"},
        "category": "auto",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/BMW.svg/960px-BMW.svg.png",
        "aliases": ["bmw", "beemve", "bimmer", "бмв", "бумер"],
        "fun_fact": {"uz": "BMW logotipidagi ko'k va oq ranglar Bavariya bayrog'ining rasmiy ranglaridir.", "ru": "Синий и белый секторы в эмблеме BMW взяты из официального флага Баварии.", "en": "The blue and white quarters in the BMW badge represent the Bavarian state flag."}
    },
    {
        "id": "mercedes_benz",
        "name": {"uz": "Mercedes-Benz", "ru": "Mercedes-Benz", "en": "Mercedes-Benz"},
        "category": "auto",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Mercedes-Logo.svg/960px-Mercedes-Logo.svg.png",
        "aliases": ["mercedes", "mercedes-benz", "benz", "мерседес", "мерс", "мерседес бенц"],
        "fun_fact": {"uz": "Uch nurli yulduz quruqlikda, suvda va havoda dvigatellar ustunligini ifodalaydi.", "ru": "Трёхлучевая звезда Mercedes символизирует превосходство моторов марки на суше, в воде и в воздухе.", "en": "The three-pointed Mercedes star symbolizes motor transport dominance on land, sea, and air."}
    },
    {
        "id": "audi",
        "name": {"uz": "Audi", "ru": "Audi", "en": "Audi"},
        "category": "auto",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Audi-Logo_2016.svg/960px-Audi-Logo_2016.svg.png",
        "aliases": ["audi", "ауди", "4 кольца"],
        "fun_fact": {"uz": "To'rtta halqa 1932 yilda Auto Union konsernini tuzgan to'rtta avtomobil ishlab chiqaruvchisini bildiradi.", "ru": "Четыре кольца Audi символизируют четыре марки, объединившиеся в 1932 году в Auto Union.", "en": "The four interlocking rings represent the four automakers that merged in 1932 to form Auto Union."}
    },
    {
        "id": "ferrari",
        "name": {"uz": "Ferrari", "ru": "Ferrari", "en": "Ferrari"},
        "category": "auto",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Ferrari_wordmark.svg/960px-Ferrari_wordmark.svg.png",
        "aliases": ["ferrari", "феррари", "скакун"],
        "fun_fact": {"uz": "Logotipdagi kishnayotgan qora ot Birinchi jahon urushi italyan uchuvchisi Franchesko Barakka samolyotidan olingan.", "ru": "Гарцующий жеребец взят с фюзеляжа самолёта итальянского аса Первой мировой войны Франческо Баракка.", "en": "The prancing horse was originally painted on the fighter plane of Italian World War I ace Francesco Baracca."}
    },
    {
        "id": "lamborghini",
        "name": {"uz": "Lamborghini", "ru": "Lamborghini", "en": "Lamborghini"},
        "category": "auto",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Lamborghini_Logo.svg/960px-Lamborghini_Logo.svg.png",
        "aliases": ["lamborghini", "lambo", "ламборгини", "ламба"],
        "fun_fact": {"uz": "Asoschi Ferruchcho Lamborgini burji Buqa bo'lgani sababli qudratli jangovar buqa ramzini tanlagan.", "ru": "Ферруччо Ламборгини выбрал разъярённого быка эмблемой, так как сам родился под знаком Тельца и любил корриду.", "en": "Ferruccio Lamborghini chose a raging bull as the logo because his zodiac sign was Taurus."}
    },
    {
        "id": "porsche",
        "name": {"uz": "Porsche", "ru": "Porsche", "en": "Porsche"},
        "category": "auto",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Porsche-Automarken-Logo.jpg",
        "aliases": ["porsche", "porshe", "порше", "порш"],
        "fun_fact": {"uz": "Porsche gerbida Shtutgart shahrining qora oti va Vyurtemberg qirolligining kiyik shohlari tasvirlangan.", "ru": "Герб Porsche объединяет скачущего коня из герба Штутгарта и оленьи рога королевства Вюртемберг.", "en": "The Porsche crest combines the black horse from Stuttgart's coat of arms with the stag antlers of Württemberg."}
    },
    {
        "id": "toyota",
        "name": {"uz": "Toyota", "ru": "Toyota", "en": "Toyota"},
        "category": "auto",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Toyota_carlogo.svg/960px-Toyota_carlogo.svg.png",
        "aliases": ["toyota", "тойота", "тайота"],
        "fun_fact": {"uz": "Toyota logotipidagi kesishgan uchta ellips xaridor yuragi, mahsulot yuragi va cheksiz imkoniyatlarni anglatadi.", "ru": "Три овала в логотипе Toyota символизируют сердце клиента, сердце продукта и безграничные инновации.", "en": "The three overlapping ellipses of Toyota symbolize the union of the customer's heart and the company's spirit."}
    },
    {
        "id": "honda",
        "name": {"uz": "Honda", "ru": "Honda", "en": "Honda"},
        "category": "auto",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Honda_logo.svg/960px-Honda_logo.svg.png",
        "aliases": ["honda", "хонда"],
        "fun_fact": {"uz": "Honda dunyodagi eng yirik ichki yonuv dvigatellari va mototsikllar ishlab chiqaruvchisidir.", "ru": "Honda является крупнейшим в мире производителем мотоциклов и двигателей внутреннего сгорания.", "en": "Honda is the world's largest manufacturer of motorcycles and internal combustion engines."}
    },
    {
        "id": "ford",
        "name": {"uz": "Ford", "ru": "Ford", "en": "Ford"},
        "category": "auto",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ford_Motor_Company_Logo.svg/960px-Ford_Motor_Company_Logo.svg.png",
        "aliases": ["ford", "форд"],
        "fun_fact": {"uz": "Genri Ford 1913 yilda birinchi konveyer liniyasini joriy qilib, avtomobil ishlab chiqarishni inqilobiy darajada tezlashtirgan.", "ru": "Генри Форд совершил промышленную революцию, внедрив первую в мире движущуюся сборочную линию в 1913 году.", "en": "Henry Ford revolutionized manufacturing by introducing the world's first moving assembly line in 1913."}
    },
    {
        "id": "chevrolet",
        "name": {"uz": "Chevrolet", "ru": "Chevrolet", "en": "Chevrolet"},
        "category": "auto",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Chevrolet-logo.png/960px-Chevrolet-logo.png",
        "aliases": ["chevrolet", "chevy", "шевроле", "шеви"],
        "fun_fact": {"uz": "O'zbekistonda eng mashhur avtomobil brendlaridan biri bo'lgan Chevy logotipi kapalak-galstuk (bowtie) deb ataladi.", "ru": "Знаменитый золотой крест Chevrolet официально называется «галстук-бабочка» (bowtie).", "en": "The famous Chevrolet emblem is globally recognized as the iconic 'bowtie' logo."}
    },
    {
        "id": "hyundai",
        "name": {"uz": "Hyundai", "ru": "Hyundai", "en": "Hyundai"},
        "category": "auto",
        "country_code": "kr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Hyundai_Motor_Company_logo.svg/960px-Hyundai_Motor_Company_logo.svg.png",
        "aliases": ["hyundai", "хендай", "хёндэ", "хюндай"],
        "fun_fact": {"uz": "Yotiq 'H' harfi aslida mijoz va kompaniya vakilining bir-biri bilan qo'l berib ko'rishayotganini ifodalaydi.", "ru": "Наклонная буква «H» символизирует рукопожатие двух людей: довольного клиента и представителя компании.", "en": "The slanted 'H' in Hyundai's logo represents two people (the client and the company) shaking hands."}
    },
    {
        "id": "volkswagen",
        "name": {"uz": "Volkswagen", "ru": "Volkswagen", "en": "Volkswagen"},
        "category": "auto",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Volkswagen_logo_2019.svg/960px-Volkswagen_logo_2019.svg.png",
        "aliases": ["volkswagen", "vw", "фольксваген"],
        "fun_fact": {"uz": "Nemis tilida 'Volkswagen' so'zi to'g'ridan-to'g'ri 'Xalq avtomobili' deb tarjima qilinadi.", "ru": "В переводе с немецкого языка название марки буквально означает «народный автомобиль».", "en": "The name Volkswagen literally translates to 'people's car' in German."}
    },
    {
        "id": "nissan",
        "name": {"uz": "Nissan", "ru": "Nissan", "en": "Nissan"},
        "category": "auto",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Nissan_2020_logo.svg/960px-Nissan_2020_logo.svg.png",
        "aliases": ["nissan", "ниссан"],
        "fun_fact": {"uz": "Nissan nomi 'Nihon Sangyo' (Yaponiya sanoati) so'zlarining qisqartmasidan kelib chiqqan.", "ru": "Название Nissan образовано от сокращения японских слов «Nippon Sangyo» (промышленность Японии).", "en": "The name Nissan is an abbreviation for 'Nippon Sangyo' (Japan Industries)."}
    },
    {
        "id": "mazda",
        "name": {"uz": "Mazda", "ru": "Mazda", "en": "Mazda"},
        "category": "auto",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Mazda_logo_1992.svg/960px-Mazda_logo_1992.svg.png",
        "aliases": ["mazda", "мазда"],
        "fun_fact": {"uz": "Mazda nomi qadimgi nur va donolik xudosi Axura Mazda nomidan olingan.", "ru": "Название бренда восходит к Ахура Мазде — древнеперсидскому божеству света, мудрости и гармонии.", "en": "Mazda was named after Ahura Mazda, the ancient Persian god of light, wisdom, and harmony."}
    },
    {
        "id": "subaru",
        "name": {"uz": "Subaru", "ru": "Subaru", "en": "Subaru"},
        "category": "auto",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Subaru_logo.svg/960px-Subaru_logo.svg.png",
        "aliases": ["subaru", "субару"],
        "fun_fact": {"uz": "Subaru logotipidagi oltita yulduz Yulduz turkumi — Pleyadalar (yaponcha Subaru) yulduzlaridir.", "ru": "Шесть звёзд на эмблеме Subaru соответствуют скоплению Плеяды в созвездии Тельца.", "en": "The six stars in the Subaru logo represent the Pleiades star cluster, known as Subaru in Japan."}
    },
    {
        "id": "mitsubishi",
        "name": {"uz": "Mitsubishi", "ru": "Mitsubishi", "en": "Mitsubishi"},
        "category": "auto",
        "country_code": "jp",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Mitsubishi_logo.svg/960px-Mitsubishi_logo.svg.png",
        "aliases": ["mitsubishi", "мицубиси", "митсубиси"],
        "fun_fact": {"uz": "Mitsubishi nomi yapon tilida 'uchta olmos' (Mitsu — uch, Hishi — olmos/romb) degan ma'noni bildiradi.", "ru": "Название Mitsubishi переводится с японского как «три ромба» или «три бриллианта».", "en": "Mitsubishi translates to 'three diamonds' (mitsu meaning three, and hishi meaning water chestnut or diamond shape)."}
    },
    {
        "id": "kia",
        "name": {"uz": "Kia", "ru": "Kia", "en": "Kia"},
        "category": "auto",
        "country_code": "kr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c4/KIA-Logo-1994-2012.png",
        "aliases": ["kia", "киа"],
        "fun_fact": {"uz": "Koreys tilida 'Kia' — 'Osiyodan yuksalish' (Ki — yuksalmoq, A — Osiyo) ma'nosini anglatadi.", "ru": "Название Kia образовано от иероглифов 'Ki' (восходить) и 'A' (Азия), означая «Восходящий из Азии».", "en": "Kia roughly translates from Sino-Korean characters as 'rising out of the Orient / Asia'."}
    },
    {
        "id": "volvo",
        "name": {"uz": "Volvo", "ru": "Volvo", "en": "Volvo"},
        "category": "auto",
        "country_code": "se",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Volvo_logo.svg/960px-Volvo_logo.svg.png",
        "aliases": ["volvo", "вольво"],
        "fun_fact": {"uz": "Volvo 1959 yilda uch nuqtali xavfsizlik kamarini ixtiro qilib, patentini butun insoniyat hayotini saqlash uchun tekinga ochib bergan.", "ru": "Volvo изобрела трёхточечный ремень безопасности в 1959 году и открыла патент для всех автопроизводителей бесплатно.", "en": "Volvo invented the 3-point seatbelt in 1959 and gave the patent away for free to save lives worldwide."}
    },
    {
        "id": "land_rover",
        "name": {"uz": "Land Rover", "ru": "Land Rover", "en": "Land Rover"},
        "category": "auto",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Land_Rover_logo_black.svg/960px-Land_Rover_logo_black.svg.png",
        "aliases": ["land rover", "range rover", "ленд ровер", "рендж ровер"],
        "fun_fact": {"uz": "Dastlabki Land Rover avtomobili Ikkinchi jahon urushidan qolgan samolyot alyuminiyidan yasalgan.", "ru": "Первый Land Rover 1948 года собирался из авиационного алюминия, оставшегося после Второй мировой войны.", "en": "The first Land Rover in 1948 was built using surplus post-WWII aircraft aluminum."}
    },
    {
        "id": "jaguar",
        "name": {"uz": "Jaguar", "ru": "Jaguar", "en": "Jaguar"},
        "category": "auto",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Jaguar_1979_logo.svg/960px-Jaguar_1979_logo.svg.png",
        "aliases": ["jaguar", "ягуар"],
        "fun_fact": {"uz": "Britaniyaning afsonaviy hashamatli avtomobil brendi sakrayotgan yirtqich mushuk — Yaguar timsoliga ega.", "ru": "Символ британской марки — прыгающий ягуар («Leaper»), олицетворяющий грацию, мощь и скорость.", "en": "The iconic jumping cat hood ornament is affectionately known in the UK as 'The Leaper'."}
    },
    {
        "id": "bentley",
        "name": {"uz": "Bentley", "ru": "Bentley", "en": "Bentley"},
        "category": "auto",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Bentley_%28Logo_2025%29.svg/960px-Bentley_%28Logo_2025%29.svg.png",
        "aliases": ["bentley", "бентли"],
        "fun_fact": {"uz": "Bentley logotipidagi qanotlarda chap va o'ng tomonda har xil sonli patlar bor (masalan, 10 va 11 ta).", "ru": "Крылья на эмблеме Bentley асимметричны: количество перьев на левом и правом крыле часто различается для защиты от подделок.", "en": "The wings on the Bentley 'Winged B' badge are subtly asymmetrical to deter counterfeiting."}
    },
    {
        "id": "rolls_royce",
        "name": {"uz": "Rolls-Royce", "ru": "Rolls-Royce", "en": "Rolls-Royce"},
        "category": "auto",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Rolls-Royce_Motor_Cars_logo.svg/960px-Rolls-Royce_Motor_Cars_logo.svg.png",
        "aliases": ["rolls-royce", "rolls royce", "роллс-ройс", "ролс ройс", "rr"],
        "fun_fact": {"uz": "Rolls-Royce kapotidagi qanotli ayol haykalchasi 'Ekstaz ruhi' (Spirit of Ecstasy) deb ataladi.", "ru": "Знаменитая фигурка на капоте Rolls-Royce называется «Дух экстаза» (Spirit of Ecstasy).", "en": "The iconic hood ornament figurine on a Rolls-Royce is known worldwide as the 'Spirit of Ecstasy'."}
    },
    {
        "id": "aston_martin",
        "name": {"uz": "Aston Martin", "ru": "Aston Martin", "en": "Aston Martin"},
        "category": "auto",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Aston_Martin_wordmark.svg/960px-Aston_Martin_wordmark.svg.png",
        "aliases": ["aston martin", "астон мартин"],
        "fun_fact": {"uz": "Agent 007 Jeyms Bondning eng sevimli avtomobili, ayniqsa afsonaviy DB5 modeli bilan dunyoga mashhur.", "ru": "Культовая марка секретного агента 007 Джеймса Бонда, прославленная спорткаром DB5.", "en": "Famous as the quintessential car of secret agent James Bond 007 since the 1964 film 'Goldfinger'."}
    },
    {
        "id": "maserati",
        "name": {"uz": "Maserati", "ru": "Maserati", "en": "Maserati"},
        "category": "auto",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Maserati_logo_2.svg/960px-Maserati_logo_2.svg.png",
        "aliases": ["maserati", "мазерати", "трезубец"],
        "fun_fact": {"uz": "Maserati logotipidagi uch tishli nayza Bolonyadagi mashhur Neptun favvorasidan olingan.", "ru": "Трезубец на эмблеме Maserati взят со статуи Нептуна на Пьяцца Маджоре в итальянской Болонье.", "en": "Maserati's trident logo was inspired by the Fountain of Neptune in Bologna's Piazza Maggiore."}
    },
    {
        "id": "bugatti",
        "name": {"uz": "Bugatti", "ru": "Bugatti", "en": "Bugatti"},
        "category": "auto",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Bugatti_logo.svg/960px-Bugatti_logo.svg.png",
        "aliases": ["bugatti", "бугатти", "верон", "широн"],
        "fun_fact": {"uz": "Bugatti Veyron va Chiron 400 km/soatdan ortiq tezlikda harakatlanadigan dunyoning eng tezkor giperkarlaridir.", "ru": "Гиперкары Bugatti Veyron и Chiron разгоняются свыше 400 км/ч и оснащены двигателями W16 с 4 турбинами.", "en": "Bugatti's Veyron and Chiron broke production car speed barriers, exceeding 400 km/h with quad-turbo W16 engines."}
    },
    {
        "id": "peugeot",
        "name": {"uz": "Peugeot", "ru": "Peugeot", "en": "Peugeot"},
        "category": "auto",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Peugeot_Logo.svg/960px-Peugeot_Logo.svg.png",
        "aliases": ["peugeot", "пежо"],
        "fun_fact": {"uz": "Peugeot dastlab 1810 yilda qahva maydalagich va po'lat arra ishlab chiqarish bilan boshlangan, arslon ramzi esa arra tishlarining o'tkirligini bildirgan.", "ru": "До выпуска автомобилей Peugeot производила кофемолки и пилы, а лев символизировал остроту лезвий.", "en": "Peugeot began in 1810 making coffee mills and saws; the lion originally symbolized the strength of saw teeth."}
    },
    {
        "id": "renault",
        "name": {"uz": "Renault", "ru": "Renault", "en": "Renault"},
        "category": "auto",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Renault_logo.svg/960px-Renault_logo.svg.png",
        "aliases": ["renault", "рено"],
        "fun_fact": {"uz": "Renault romb ko'rinishidagi logotipini birinchi marta 1925 yilda avtomobil signaliga moslashtirish uchun o'rnatgan.", "ru": "Знаменитый ромб Renault впервые появился на капотах в 1925 году, скрывая отверстие клаксона.", "en": "Renault's diamond logo was introduced in 1925 to fit over the horn mounted in the center of the grille."}
    },
    {
        "id": "nike",
        "name": {"uz": "Nike", "ru": "Nike", "en": "Nike"},
        "category": "fashion",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Logo_NIKE.svg/960px-Logo_NIKE.svg.png",
        "aliases": ["nike", "nayk", "найк", "swoosh"],
        "fun_fact": {"uz": "Mashhur 'Swoosh' belgisi talaba Kerolin Devidson tomonidan atigi 35 dollarga chizib berilgan.", "ru": "Знаменитый логотип «Swoosh» был нарисован студенткой Кэролин Дэвидсон всего за $35 в 1971 году.", "en": "The iconic Nike 'Swoosh' was designed in 1971 by graphic design student Carolyn Davidson for just $35."}
    },
    {
        "id": "adidas",
        "name": {"uz": "Adidas", "ru": "Adidas", "en": "Adidas"},
        "category": "fashion",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/960px-Adidas_Logo.svg.png",
        "aliases": ["adidas", "adas", "адидас", "3 полоски"],
        "fun_fact": {"uz": "Adidas nomi asoschisi Adolf Dassler sharafiga ('Adi' + 'Das') qo'yilgan.", "ru": "Название марки происходит от имени и фамилии её основателя Адольфа Дасслера («Ади» + «Дас»).", "en": "The name Adidas comes from the nickname and surname of founder Adolf Dassler ('Adi' + 'Das')."}
    },
    {
        "id": "puma",
        "name": {"uz": "Puma", "ru": "Puma", "en": "Puma"},
        "category": "fashion",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/d/da/Puma_complete_logo.svg/960px-Puma_complete_logo.svg.png",
        "aliases": ["puma", "пума"],
        "fun_fact": {"uz": "Puma asoschisi Rudolf Dassler Adidas asoschisi Adolf Dasslerning tug'ishgan akasi bo'lgan.", "ru": "Основатель Puma Рудольф Дасслер был родным братом Адольфа Дасслера, создателя Adidas.", "en": "Puma founder Rudolf Dassler was the older brother of Adolf Dassler, the founder of rival brand Adidas."}
    },
    {
        "id": "reebok",
        "name": {"uz": "Reebok", "ru": "Reebok", "en": "Reebok"},
        "category": "fashion",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Reebok_2019_logo.svg/960px-Reebok_2019_logo.svg.png",
        "aliases": ["reebok", "рибок"],
        "fun_fact": {"uz": "Reebok nomi Afrika antilopasi 'rhebok' so'zidan olingan.", "ru": "Название компании происходит от африканской серой косули-антилопы (rhebok).", "en": "Reebok is named after the grey rhebok, a fast African antelope."}
    },
    {
        "id": "under_armour",
        "name": {"uz": "Under Armour", "ru": "Under Armour", "en": "Under Armour"},
        "category": "fashion",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Under_armour_logo.svg/960px-Under_armour_logo.svg.png",
        "aliases": ["under armour", "under armor", "андер армор", "ua"],
        "fun_fact": {"uz": "Logotipdagi kesishgan chiziqlar bir vaqtning o'zida 'U' va 'A' harflarini hosil qiladi.", "ru": "Эмблема Under Armour сочетает в себе пересечение букв «U» сверху и «A» снизу.", "en": "The interlocking Under Armour logo elegantly combines the 'U' on top and the 'A' underneath."}
    },
    {
        "id": "new_balance",
        "name": {"uz": "New Balance", "ru": "New Balance", "en": "New Balance"},
        "category": "fashion",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/New_Balance_logo.svg/960px-New_Balance_logo.svg.png",
        "aliases": ["new balance", "nb", "нью баланс"],
        "fun_fact": {"uz": "Asoschi Uilyam Rayli hovlidagi tovuqlarning uch tirnoqli panjalari mukammal muvozanat saqlashini ko'rib ushbu poyabzalni kashf qilgan.", "ru": "Идея идеального баланса подошвы пришла основателю после наблюдения за тем, как курицы стоят на трех лапках.", "en": "The founder was inspired by chickens in his yard, noticing their three-clawed feet provided perfect balance."}
    },
    {
        "id": "gucci",
        "name": {"uz": "Gucci", "ru": "Gucci", "en": "Gucci"},
        "category": "fashion",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Gucci_Logo.svg/960px-Gucci_Logo.svg.png",
        "aliases": ["gucci", "гуччи"],
        "fun_fact": {"uz": "Gucci'ning ikkita tutashgan 'G' logotipi asoschi Guchcho Guchchi sharafiga yaratilgan.", "ru": "Культовый логотип из двух переплетённых букв «G» посвящён основателю модного дома Гуччо Гуччи.", "en": "The famous interlocking double-G logo honors the Italian founder, Guccio Gucci."}
    },
    {
        "id": "chanel",
        "name": {"uz": "Chanel", "ru": "Chanel", "en": "Chanel"},
        "category": "fashion",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/9/92/Chanel_logo_interlocking_cs.svg/960px-Chanel_logo_interlocking_cs.svg.png",
        "aliases": ["chanel", "шанель", "coco chanel"],
        "fun_fact": {"uz": "Koko Shanel tomonidan yaratilgan 'Kichik qora libos' va 'Chanel No. 5' atri ayollar modasini tubdan yangiladi.", "ru": "Создала легендарное «маленькое чёрное платье» и духи Chanel № 5, ставшие эталоном элегантности.", "en": "Coco Chanel revolutionized women's fashion with the 'little black dress' and timeless fragrance Chanel No. 5."}
    },
    {
        "id": "louis_vuitton",
        "name": {"uz": "Louis Vuitton", "ru": "Louis Vuitton", "en": "Louis Vuitton"},
        "category": "fashion",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Louis_Vuitton_logo_and_wordmark.svg/960px-Louis_Vuitton_logo_and_wordmark.svg.png",
        "aliases": ["louis vuitton", "lv", "луи виттон", "луи вюиттон"],
        "fun_fact": {"uz": "LV monogrammasi 1896 yilda soxtalashtirishdan himoyalanish uchun maxsus ishlab chiqilgan.", "ru": "Фирменная монограмма LV была создана Жоржем Виттоном в 1896 году для защиты чемоданов от подделок.", "en": "The iconic LV monogram canvas was created in 1896 by Georges Vuitton to prevent counterfeiting of travel trunks."}
    },
    {
        "id": "prada",
        "name": {"uz": "Prada", "ru": "Prada", "en": "Prada"},
        "category": "fashion",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Prada-Logo.svg/960px-Prada-Logo.svg.png",
        "aliases": ["prada", "прада"],
        "fun_fact": {"uz": "Prada 1919 yilda Italiya Qirollik xonadonining rasmiy yetkazib beruvchisi deb e'lon qilingan.", "ru": "В 1919 году Prada стала официальным поставщиком итальянского королевского двора Савойской династии.", "en": "Prada was appointed as an official supplier to the Italian Royal Household in 1919."}
    },
    {
        "id": "versace",
        "name": {"uz": "Versace", "ru": "Versace", "en": "Versace"},
        "category": "fashion",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Versace_old_logo.svg/960px-Versace_old_logo.svg.png",
        "aliases": ["versace", "версаче"],
        "fun_fact": {"uz": "Versace logotipidagi Meduza Gorgona odamlarni o'zining sehrli go'zalligi bilan maftun etish ramzidir.", "ru": "Джанни Версаче выбрал голову Медузы Ронданини, так как она гипнотизировала и влюбляла в себя без оглядки.", "en": "Gianni Versace chose Medusa because people fell hopelessly in love with her and could not look away."}
    },
    {
        "id": "dior",
        "name": {"uz": "Dior", "ru": "Dior", "en": "Christian Dior"},
        "category": "fashion",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Dior_Logo.svg/960px-Dior_Logo.svg.png",
        "aliases": ["dior", "christian dior", "диор", "кристиан диор"],
        "fun_fact": {"uz": "1947 yilda Kristian Dior yaratgan 'New Look' to'plami urushdan keyingi ayollar modasida inqilob qildi.", "ru": "В 1947 году Кристиан Диор перевернул мир моды коллекцией «New Look», вернувшей женщинам утончённость.", "en": "Christian Dior's 1947 'New Look' revolutionized post-war fashion with ultra-feminine silhouettes."}
    },
    {
        "id": "hermes",
        "name": {"uz": "Hermès", "ru": "Hermès", "en": "Hermès"},
        "category": "fashion",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Herm%C3%A8s.svg/960px-Herm%C3%A8s.svg.png",
        "aliases": ["hermes", "эрмес", "гермес"],
        "fun_fact": {"uz": "Mashhur Birkin va Kelly sumkalarini qo'lda tayyorlash uchun mohir usta kamida 18-24 soat mehnat qiladi.", "ru": "Каждая культовая сумка Birkin создаётся вручную одним мастером на протяжении до 24 часов.", "en": "Each iconic Hermès Birkin handbag is handcrafted by a single artisan, taking up to 24 hours of meticulous work."}
    },
    {
        "id": "armani",
        "name": {"uz": "Giorgio Armani", "ru": "Giorgio Armani", "en": "Giorgio Armani"},
        "category": "fashion",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Armani_logo.svg/960px-Armani_logo.svg.png",
        "aliases": ["armani", "giorgio armani", "армани", "джорджо армани"],
        "fun_fact": {"uz": "Armani qadimgi qattiq kostyumlardan yelka qo'shimchalarini olib tashlab, erkin va nafis 'deconstructed' uslubni yaratdi.", "ru": "Джорджо Армани совершил революцию в мужской моде, убрав жёсткие подплечники и создав мягкий силуэт.", "en": "Giorgio Armani revolutionized menswear by removing rigid padding to create the relaxed, elegant jacket."}
    },
    {
        "id": "dolce_gabbana",
        "name": {"uz": "Dolce & Gabbana", "ru": "Dolce & Gabbana", "en": "Dolce & Gabbana"},
        "category": "fashion",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Dolce_%26_Gabbana.svg/960px-Dolce_%26_Gabbana.svg.png",
        "aliases": ["dolce & gabbana", "dolce and gabbana", "d&g", "дольче габбана", "д энд джи"],
        "fun_fact": {"uz": "Italiyalik dizaynerlar Domeniko Dolche va Stefano Gabbana tomonidan Milanda asos solingan hashamatli brend.", "ru": "Итальянский дом моды, основанный Доменико Дольче и Стефано Габбана, черпает вдохновение в культуре Сицилии.", "en": "Founded in Milan by Domenico Dolce and Stefano Gabbana, heavily inspired by timeless Sicilian tradition."}
    },
    {
        "id": "balenciaga",
        "name": {"uz": "Balenciaga", "ru": "Balenciaga", "en": "Balenciaga"},
        "category": "fashion",
        "country_code": "es",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Balenciaga_Logo.svg/960px-Balenciaga_Logo.svg.png",
        "aliases": ["balenciaga", "баленсиага"],
        "fun_fact": {"uz": "Ispaniyalik Kristobal Balenciaga tomonidan asos solingan, Kristian Dior uni 'barchamizning ustozimiz' deb atagan.", "ru": "Основатель марки Кристобаль Баленсиага был признан Кристианом Диором «учителем всех остальных кутюрье».", "en": "Founded in Spain by Cristóbal Balenciaga, whom Christian Dior called 'the master of us all'."}
    },
    {
        "id": "zara",
        "name": {"uz": "Zara", "ru": "Zara", "en": "Zara"},
        "category": "fashion",
        "country_code": "es",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Zara_Logo.svg/960px-Zara_Logo.svg.png",
        "aliases": ["zara", "зара"],
        "fun_fact": {"uz": "Zara yangi kiyim dizaynini chizilganidan boshlab atigi 15 kunda do'kon peshtaxtasiga yetkazib bera oladi.", "ru": "Zara способна разработать новый дизайн одежды и выставить его в магазины всего за 15 дней.", "en": "Zara can take a new garment from design sketch to retail store shelves in just 15 days."}
    },
    {
        "id": "hm",
        "name": {"uz": "H&M", "ru": "H&M", "en": "H&M"},
        "category": "fashion",
        "country_code": "se",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/H%26M-Logo.svg/960px-H%26M-Logo.svg.png",
        "aliases": ["h&m", "hm", "эйч энд эм", "хм"],
        "fun_fact": {"uz": "H&M nomi 'Hennes & Mauritz' qisqartmasi bo'lib, shved tilida 'Hennes' — 'Uning uchun' (ayol uchun) deganidir.", "ru": "Название H&M расшифровывается как Hennes & Mauritz (по-шведски 'Hennes' означает «Для неё»).", "en": "H&M stands for 'Hennes & Mauritz' ('Hennes' meaning 'Hers' in Swedish)."}
    },
    {
        "id": "calvin_klein",
        "name": {"uz": "Calvin Klein", "ru": "Calvin Klein", "en": "Calvin Klein"},
        "category": "fashion",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Calvin_Klein_logo.svg/960px-Calvin_Klein_logo.svg.png",
        "aliases": ["calvin klein", "ck", "кельвин кляйн", "кляйн"],
        "fun_fact": {"uz": "1980 yillarda o'z logotipi tushirilgan djinsi va ichki kiyimlari bilan Amerika modasida burilish yasagan.", "ru": "Совершил революцию в американской моде в 1980-х годах культовыми дизайнерскими джинсами и нижним бельём.", "en": "Pioneered designer jeans and iconic logo underwear in the 1980s, redefining minimalist American fashion."}
    },
    {
        "id": "rolex",
        "name": {"uz": "Rolex", "ru": "Rolex", "en": "Rolex"},
        "category": "fashion",
        "country_code": "ch",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Rolex_wordmark_logo.svg/960px-Rolex_wordmark_logo.svg.png",
        "aliases": ["rolex", "ролекс", "часы"],
        "fun_fact": {"uz": "Rolex 1926 yilda 'Oyster' nomli dunyodagi birinchi suv o'tkazmaydigan qo'l soatini yaratgan.", "ru": "Rolex создал первые в мире полностью водонепроницаемые наручные часы «Oyster» ещё в 1926 году.", "en": "Rolex created the world's first waterproof wristwatch, the legendary 'Oyster', in 1926."}
    },
    {
        "id": "real_madrid",
        "name": {"uz": "Real Madrid", "ru": "Реал Мадрид", "en": "Real Madrid"},
        "category": "football",
        "country_code": "es",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/960px-Real_Madrid_CF.svg.png",
        "aliases": ["real madrid", "real", "реал мадрид", "реал", "сливочные", "los blancos"],
        "fun_fact": {"uz": "UEFA Chempionlar Ligasini rekord darajadagi 15 marta yutgan tarixdagi eng sovrindor klub.", "ru": "Самый титулованный клуб в истории европейского футбола, выигравший Лигу чемпионов рекордные 15 раз.", "en": "The most decorated club in European football history, having won a record 15 Champions League titles."}
    },
    {
        "id": "barcelona",
        "name": {"uz": "Barselona", "ru": "Барселона", "en": "FC Barcelona"},
        "category": "football",
        "country_code": "es",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/960px-FC_Barcelona_%28crest%29.svg.png",
        "aliases": ["barcelona", "barca", "fc barcelona", "barsa", "барселона", "барса", "сине-гранатовые", "blaugrana"],
        "fun_fact": {"uz": "Klub shiori 'Més que un club' ('Klubdan ham ortiqroq') Kataloniya o'ziga xosligini ifodalaydi.", "ru": "Девиз клуба «Més que un club» («Больше, чем клуб») подчеркивает его статус символа Каталонии.", "en": "The club motto 'Més que un club' ('More than a club') represents Catalan cultural identity."}
    },
    {
        "id": "atletico_madrid",
        "name": {"uz": "Atletiko Madrid", "ru": "Атлетико Мадрид", "en": "Atlético de Madrid"},
        "category": "football",
        "country_code": "es",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Atletico_Madrid_Logo_2024.svg/960px-Atletico_Madrid_Logo_2024.svg.png",
        "aliases": ["atletico madrid", "atletico", "атлетико мадрид", "атлетико", "матрасники", "colchoneros"],
        "fun_fact": {"uz": "Klub gerbidagi ayiq va qulupnay daraxti Madrid shahrining rasmiy ramzidan olingan.", "ru": "Медведь и земляничное дерево на эмблеме «Атлетико» взяты с официального герба города Мадрид.", "en": "The bear and strawberry tree on Atlético's crest are taken from the official coat of arms of Madrid."}
    },
    {
        "id": "manchester_united",
        "name": {"uz": "Manchester Yunayted", "ru": "Манчестер Юнайтед", "en": "Manchester United"},
        "category": "football",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Manchester_United_FC_crest.svg/960px-Manchester_United_FC_crest.svg.png",
        "aliases": ["manchester united", "man united", "mufc", "манчестер юнайтед", "мю", "красные дьяволы", "red devils"],
        "fun_fact": {"uz": "Ser Aleks Fergyuson qo'l ostida klub 26 yil ichida 38 ta sovrin, jumladan 13 ta Premyer-liga kubogini yutgan.", "ru": "Под руководством сэра Алекса Фергюсона клуб завоевал 38 трофеев за 26 лет, включая 13 титулов АПЛ.", "en": "Under Sir Alex Ferguson, Manchester United won 38 major trophies in 26 years, including 13 Premier League titles."}
    },
    {
        "id": "manchester_city",
        "name": {"uz": "Manchester Siti", "ru": "Манчестер Сити", "en": "Manchester City"},
        "category": "football",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/960px-Manchester_City_FC_badge.svg.png",
        "aliases": ["manchester city", "man city", "mcfc", "манчестер сити", "мс", "горожане", "citizens"],
        "fun_fact": {"uz": "2017/18 yilgi mavsumda 100 ochko to'plab, Premyer-liga tarixida 'Centurions' laqabini oldi.", "ru": "В сезоне 2017/18 набрал 100 очков за сезон в АПЛ, установив вечный рекорд Премьер-лиги («Стобалльники»).", "en": "Became the first team in Premier League history to reach 100 points in a single season (2017–18)."}
    },
    {
        "id": "liverpool",
        "name": {"uz": "Liverpul", "ru": "Ливерпуль", "en": "Liverpool FC"},
        "category": "football",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/960px-Liverpool_FC.svg.png",
        "aliases": ["liverpool", "liverpool fc", "lfc", "ливерпуль", "мерсисайдцы", "красные"],
        "fun_fact": {"uz": "'You'll Never Walk Alone' qo'shig'i klub madhiyasiga aylangan va har bir o'yindan oldin Enfildda birgalikda kuylanadi.", "ru": "Песня «You'll Never Walk Alone» стала гимном клуба и исполняется десятками тысяч болельщиков на «Энфилде».", "en": "The anthem 'You'll Never Walk Alone' is famously sung before every home match by the Anfield Kop."}
    },
    {
        "id": "arsenal",
        "name": {"uz": "Arsenal", "ru": "Arsenal", "en": "Arsenal FC"},
        "category": "football",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/960px-Arsenal_FC.svg.png",
        "aliases": ["arsenal", "arsenal fc", "gunners", "арсенал", "канониры"],
        "fun_fact": {"uz": "2003/04 yilgi mavsumda birorta ham mag'lubiyatsiz chempion bo'lib, 'Yengilmaslar' (The Invincibles) laqabini olgan.", "ru": "В сезоне 2003/04 стал чемпионом Англии без единого поражения за 38 туров («Непобедимые»).", "en": "Went through the entire 2003–04 Premier League season undefeated, earning the historic nickname 'The Invincibles'."}
    },
    {
        "id": "chelsea",
        "name": {"uz": "Chelsi", "ru": "Челси", "en": "Chelsea FC"},
        "category": "football",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/960px-Chelsea_FC.svg.png",
        "aliases": ["chelsea", "chelsea fc", "blues", "челси", "аристократы", "синие"],
        "fun_fact": {"uz": "UEFAning barcha uchta asosiy klub turnirlarini (Chempionlar Ligasi, Yevropa Ligasi, Kubok egalari kubogi) yutgan birinchi London klubi.", "ru": "Первый лондонский клуб, выигравший Лигу чемпионов УЕФА (в 2012 и 2021 годах).", "en": "The first London club to win the UEFA Champions League, lifting the trophy in 2012 and 2021."}
    },
    {
        "id": "tottenham",
        "name": {"uz": "Tottenxem", "ru": "Тоттенхэм Хотспур", "en": "Tottenham Hotspur"},
        "category": "football",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Tottenham_Hotspur.svg/960px-Tottenham_Hotspur.svg.png",
        "aliases": ["tottenham", "spurs", "tottenham hotspur", "тоттенхэм", "шпоры"],
        "fun_fact": {"uz": "Klub logotipidagi jangovar xo'roz qadimgi ritsar ser Garri Xotspur jangovar xo'rozlariga ishoradir.", "ru": "Бойцовый петух на футбольном мяче — символ сэра Гарри Хотспура, в честь которого назван клуб.", "en": "The cockerel standing on a football commemorates Sir Henry Percy (Harry Hotspur) and his prized fighting cocks."}
    },
    {
        "id": "bayern_munich",
        "name": {"uz": "Bavariya", "ru": "Бавария Мюнхен", "en": "FC Bayern Munich"},
        "category": "football",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg/960px-FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg.png",
        "aliases": ["bayern munich", "bayern", "bayern munchen", "бавария", "бавария мюнхен", "мюнхен"],
        "fun_fact": {"uz": "Germaniya Bundesligasini ketma-ket 11 marta yutib, Yevropa top-5 ligalarida rekord o'rnatgan.", "ru": "Выиграла 11 чемпионских титулов Бундеслиги подряд (2013–2023), рекорд среди топ-5 лиг Европы.", "en": "Won an unprecedented 11 consecutive Bundesliga titles between 2013 and 2023."}
    },
    {
        "id": "borussia_dortmund",
        "name": {"uz": "Borussiya Dortmund", "ru": "Боруссия Дортмунд", "en": "Borussia Dortmund"},
        "category": "football",
        "country_code": "de",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/960px-Borussia_Dortmund_logo.svg.png",
        "aliases": ["borussia dortmund", "dortmund", "bvb", "боруссия дортмунд", "боруссия", "бвб", "шмели"],
        "fun_fact": {"uz": "Vestfalenstadiondagi 25 000 muxlis sig'adigan mashhur janubiy tribuna 'Sariq devor' (Die Gelbe Wand) deb ataladi.", "ru": "Южная трибуна стадиона в Дортмунде вмещает 25 000 стоячих мест и известна как легендарная «Жёлтая стена».", "en": "Home to the famous 'Yellow Wall' (Die Gelbe Wand), the largest free-standing grandstand in European football."}
    },
    {
        "id": "juventus",
        "name": {"uz": "Yuventus", "ru": "Ювентус", "en": "Juventus FC"},
        "category": "football",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Juventus_FC_-_logo_black_%28Italy%2C_2020%29.svg/960px-Juventus_FC_-_logo_black_%28Italy%2C_2020%29.svg.png",
        "aliases": ["juventus", "juve", "ювентус", "юве", "старая синьора", "бьянконери"],
        "fun_fact": {"uz": "'Keksa senyora' (La Vecchia Signora) laqabli Turin klubi Italiya A Seriyasini rekord darajadagi 36 marta yutgan.", "ru": "«Старая Синьора» является рекордсменом Италии по числу выигранных чемпионских титулов Серии А (36 раз).", "en": "Known as 'The Old Lady' (La Vecchia Signora), Juventus has won a record 36 Serie A league titles."}
    },
    {
        "id": "ac_milan",
        "name": {"uz": "Milan", "ru": "Милан", "en": "AC Milan"},
        "category": "football",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Logo_of_AC_Milan.svg/960px-Logo_of_AC_Milan.svg.png",
        "aliases": ["ac milan", "milan", "rossoneri", "милан", "ас милан", "россонери"],
        "fun_fact": {"uz": "UEFA Chempionlar Ligasini 7 marta yutgan bo'lib, bu borada Yevropada faqat 'Real Madrid'dan keyin ikkinchi o'rinda turadi.", "ru": "Выиграл Лигу чемпионов 7 раз, уступая по этому показателю только мадридскому «Реалу».", "en": "Has won the European Cup / Champions League 7 times, second only to Real Madrid."}
    },
    {
        "id": "inter_milan",
        "name": {"uz": "Inter Milan", "ru": "Интер Милан", "en": "Inter Milan"},
        "category": "football",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Inter_Milano_2021_logo_with_one_star.svg/960px-Inter_Milano_2021_logo_with_one_star.svg.png",
        "aliases": ["inter milan", "inter", "internazionale", "интер", "интер милан", "нерадзурри"],
        "fun_fact": {"uz": "Italiya A Seriyasidan hech qachon quyi ligaga tushib ketmagan yagona Italiya klubi.", "ru": "Единственный клуб в истории итальянского футбола, никогда не вылетавший из высшего дивизиона (Серии А).", "en": "The only Italian club that has never been relegated from the top flight of Italian football (Serie A)."}
    },
    {
        "id": "roma",
        "name": {"uz": "Roma", "ru": "Рома", "en": "AS Roma"},
        "category": "football",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/AS_Roma_logo_%282017%29.svg/960px-AS_Roma_logo_%282017%29.svg.png",
        "aliases": ["roma", "as roma", "рома", "ас рома", "волки", "джаллоросси"],
        "fun_fact": {"uz": "Gerbida Rim asoschilari Romul va Remni emizayotgan afsonaviy Bo'ri tasvirlangan.", "ru": "На гербе клуба изображена капитолийская волчица, вскармливающая младенцев Ромула и Рема — основателей Рима.", "en": "The crest depicts the Capitoline She-Wolf nursing Romulus and Remus, the mythical founders of Rome."}
    },
    {
        "id": "psg",
        "name": {"uz": "PSJ", "ru": "ПСЖ", "en": "Paris Saint-Germain"},
        "category": "football",
        "country_code": "fr",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Paris_Saint-Germain_F.C..svg/960px-Paris_Saint-Germain_F.C..svg.png",
        "aliases": ["psg", "paris saint-germain", "пари сен-жермен", "псж", "париж"],
        "fun_fact": {"uz": "Klub logotipida Parijning ramzi Eyfel minorasi va uning ostida qirol Lyudovik XIV beshigi tasvirlangan.", "ru": "В центре эмблемы клуба изображена Эйфелева башня, а под ней — колыбель короля Людовика XIV.", "en": "The crest features the Eiffel Tower and the fleur-de-lis cradle of King Louis XIV born in Saint-Germain-en-Laye."}
    },
    {
        "id": "ajax",
        "name": {"uz": "Ayaks", "ru": "Аякс", "en": "AFC Ajax"},
        "category": "football",
        "country_code": "nl",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/7/79/Ajax_Amsterdam.svg/960px-Ajax_Amsterdam.svg.png",
        "aliases": ["ajax", "afc ajax", "аякс"],
        "fun_fact": {"uz": "Yoxan Kroyff va 'Total futbol' vatani bo'lib, klub logotipidagi qadimgi yunon qahramoni Ayaks chizgisi roppa-rosa 11 ta chiziqdan iborat.", "ru": "Портрет греческого героя Аякса на логотипе нарисован ровно 11 линиями — по числу игроков на футбольном поле.", "en": "The drawing of Greek hero Ajax on the crest is composed of exactly 11 lines, representing the 11 players."}
    },
    {
        "id": "benfica",
        "name": {"uz": "Benfika", "ru": "Бенфика", "en": "SL Benfica"},
        "category": "football",
        "country_code": "pt",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/SL_Benfica_logo.svg/960px-SL_Benfica_logo.svg.png",
        "aliases": ["benfica", "sl benfica", "бенфика", "орлы"],
        "fun_fact": {"uz": "Klub ramzi burgut bo'lib, har bir uy uchrashuvidan oldin 'Estádio da Luz' stadioni uzra haqiqiy burgut parvoz qiladi.", "ru": "Перед каждым домашним матчем на стадионе «Эштадиу да Луж» над трибунами запускают живого орла по имени Витория.", "en": "Before every home game at the Estádio da Luz, a real bald eagle named Vitória flies around the stadium."}
    },
    {
        "id": "porto",
        "name": {"uz": "Portu", "ru": "Порту", "en": "FC Porto"},
        "category": "football",
        "country_code": "pt",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/FC_Porto.svg/960px-FC_Porto.svg.png",
        "aliases": ["porto", "fc porto", "порту", "драконы"],
        "fun_fact": {"uz": "2004 yilda Joze Mourinyo boshchiligida kutilmaganda UEFA Chempionlar Ligasini yutgan.", "ru": "В 2004 году под руководством молодого Жозе Моуринью сенсационно выиграл Лигу чемпионов УЕФА.", "en": "Famously won the 2004 UEFA Champions League under young manager José Mourinho."}
    },
    {
        "id": "galatasaray",
        "name": {"uz": "Galatasaroy", "ru": "Галатасарай", "en": "Galatasaray SK"},
        "category": "football",
        "country_code": "tr",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Galatasaray_Sports_Club_Logo.svg/960px-Galatasaray_Sports_Club_Logo.svg.png",
        "aliases": ["galatasaray", "галатасарай", "сарай"],
        "fun_fact": {"uz": "2000 yilda UEFA Kubogi va UEFA Superkubogini yutib, Yevropa kubogini qo'lga kiritgan yagona Turkiya klubi bo'ldi.", "ru": "Единственный турецкий клуб, выигравший еврокубок — Кубок УЕФА и Суперкубок УЕФА в 2000 году.", "en": "The only Turkish club to win a major European trophy, capturing the UEFA Cup and Super Cup in 2000."}
    },
    {
        "id": "coca_cola",
        "name": {"uz": "Coca-Cola", "ru": "Coca-Cola", "en": "Coca-Cola"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Coca-Cola_logo.svg/960px-Coca-Cola_logo.svg.png",
        "aliases": ["coca-cola", "coca cola", "coke", "кока-кола", "кола"],
        "fun_fact": {"uz": "Coca-Cola qizil-oq ranglari zamonaviy Santa-Klaus obrazining butun dunyo bo'ylab shakllanishiga sabab bo'lgan.", "ru": "Именно рекламные кампании Coca-Cola 1930-х годов популяризировали привычный образ Санта-Клауса в красно-белом костюме.", "en": "Coca-Cola's 1930s holiday advertising largely popularized the modern image of Santa Claus in a red suit."}
    },
    {
        "id": "pepsi",
        "name": {"uz": "Pepsi", "ru": "Pepsi", "en": "Pepsi"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Pepsi_2023.svg/960px-Pepsi_2023.svg.png",
        "aliases": ["pepsi", "pepsi-cola", "пепси"],
        "fun_fact": {"uz": "1893 yilda kashf qilingan ichimlik dastlab oshqozon hazmini yaxshilash uchun 'Brad's Drink' deb atalgan.", "ru": "Изначально напиток назывался «Brad's Drink» в честь создателя-фармацевта Калеба Брэдэма.", "en": "Originally invented in 1893 as 'Brad's Drink' by pharmacist Caleb Bradham to aid digestion."}
    },
    {
        "id": "mcdonalds",
        "name": {"uz": "McDonald's", "ru": "McDonald's", "en": "McDonald's"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/960px-McDonald%27s_Golden_Arches.svg.png",
        "aliases": ["mcdonald's", "mcdonalds", "maccas", "макдоналдс", "макдак", "мак"],
        "fun_fact": {"uz": "McDonald's oltin arkalari (Golden Arches) dunyodagi eng taniqli ramzlardan biri bo'lib, xalqaro 'Big Mac Index' iqtisodiy o'lchoviga ega.", "ru": "Журнал The Economist создал знаменитый «Индекс Биг-Мака» на основе цен в ресторанах McDonald's для оценки валют мира.", "en": "The Golden Arches are so ubiquitous that The Economist uses the 'Big Mac Index' to compare purchasing power across global currencies."}
    },
    {
        "id": "starbucks",
        "name": {"uz": "Starbucks", "ru": "Starbucks", "en": "Starbucks"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/960px-Starbucks_Corporation_Logo_2011.svg.png",
        "aliases": ["starbucks", "старбакс", "кофе"],
        "fun_fact": {"uz": "Starbucks logotipidagi dengiz qizi qadimgi dengiz afsonalaridagi ikki dumli sirena hisoblanadi.", "ru": "Существо на зелёном логотипе Starbucks — это двухвостая сирена из средневековой мифологии.", "en": "The figure on the Starbucks logo is a twin-tailed siren from 16th-century Norse mythology."}
    },
    {
        "id": "kfc",
        "name": {"uz": "KFC", "ru": "KFC", "en": "KFC"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/KFC_logo.svg/960px-KFC_logo.svg.png",
        "aliases": ["kfc", "kentucky fried chicken", "кфс", "курица"],
        "fun_fact": {"uz": "Polkovnik Sandersning 11 xil o't va ziravorlardan iborat mashhur tovuq retsepti AQShdagi eng sirli tijorat sirlaridan biridir.", "ru": "Секретный рецепт панировки полковника Сандерса из 11 трав и специй хранится в сейфе штаб-квартиры в Луисвилле.", "en": "Colonel Sanders' secret blend of 11 herbs and spices is stored in a computerized vault in Louisville, Kentucky."}
    },
    {
        "id": "burger_king",
        "name": {"uz": "Burger King", "ru": "Burger King", "en": "Burger King"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Burger_King_2020.svg/960px-Burger_King_2020.svg.png",
        "aliases": ["burger king", "бургер кинг", "бк", "воппер"],
        "fun_fact": {"uz": "Burger King o'zining 'Whopper' burgerini ochiq olovda qovurilgan go'sht (flame-grilled) bilan tayyorlashi bilan mashhur.", "ru": "Фирменное блюдо Burger King — воппер — готовится из котлеты, обжаренной на настоящем открытом огне.", "en": "Burger King is famous for flame-grilling its burger patties rather than frying them on a flat griddle."}
    },
    {
        "id": "subway",
        "name": {"uz": "Subway", "ru": "Subway", "en": "Subway"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Subway_2016_logo.svg/960px-Subway_2016_logo.svg.png",
        "aliases": ["subway", "сабвей", "саб"],
        "fun_fact": {"uz": "Filiallar soni bo'yicha dunyodagi eng yirik restoranlar tarmog'i (100 dan ortiq davlatda 37 000 dan ko'p nuqta).", "ru": "По числу заведений Subway превосходит McDonald's: более 37 000 точек в 100 странах мира.", "en": "Subway operates more restaurant locations globally than McDonald's, spanning over 100 countries."}
    },
    {
        "id": "pizza_hut",
        "name": {"uz": "Pizza Hut", "ru": "Pizza Hut", "en": "Pizza Hut"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Pizza_Hut_classic_logo.svg/960px-Pizza_Hut_classic_logo.svg.png",
        "aliases": ["pizza hut", "пицца хат", "пицца"],
        "fun_fact": {"uz": "Pizza Hut 2001 yilda Xalqaro koinot stansiyasiga pitsa yetkazib bergan birinchi kompaniyaga aylangan.", "ru": "В 2001 году Pizza Hut стала первой компанией в истории, доставившей пиццу космонавтам на Международную космическую станцию.", "en": "In 2001, Pizza Hut became the first company to deliver a pizza to astronauts aboard the International Space Station."}
    },
    {
        "id": "dominos",
        "name": {"uz": "Domino's Pizza", "ru": "Domino's Pizza", "en": "Domino's Pizza"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Domino%27s_pizza_logo.svg/960px-Domino%27s_pizza_logo.svg.png",
        "aliases": ["domino's", "dominos pizza", "доминос", "доминос пицца"],
        "fun_fact": {"uz": "Domino toshidagi uchta nuqta kompaniyaning dastlab ochilgan birinchi 3 ta filialini anglatadi.", "ru": "Три точки на костяшке домино в логотипе символизируют первые три пиццерии, открытые основателями.", "en": "The three dots on the domino in the logo represent the first three stores opened by the founders."}
    },
    {
        "id": "red_bull",
        "name": {"uz": "Red Bull", "ru": "Red Bull", "en": "Red Bull"},
        "category": "food",
        "country_code": "at",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Logo_of_Red_bull.svg/960px-Logo_of_Red_bull.svg.png",
        "aliases": ["red bull", "ред булл", "редбул", "энергетик"],
        "fun_fact": {"uz": "'Red Bull sizga qanot beradi' shiori bilan mashhur brend Tailanddagi 'Krating Daeng' ichimligidan ilhomlangan.", "ru": "Австрийский энергетик был вдохновлён тайским напитком Krating Daeng («Красный гаур/бык»).", "en": "Inspired by the Thai energy drink Krating Daeng, Red Bull became a global marketing powerhouse sponsoring extreme sports."}
    },
    {
        "id": "heineken",
        "name": {"uz": "Heineken", "ru": "Heineken", "en": "Heineken"},
        "category": "food",
        "country_code": "nl",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Heineken_logo.svg/960px-Heineken_logo.svg.png",
        "aliases": ["heineken", "хайнекен", "хейнекен"],
        "fun_fact": {"uz": "Heineken logotipidagi 'e' harflari kulib turgan inson chehrasini eslatishi uchun bir oz orqaga egilgan.", "ru": "Буквы «e» в логотипе Heineken слегка наклонены назад, чтобы казалось, будто они весело улыбаются.", "en": "The letters 'e' in the Heineken logo are tilted backwards to give the impression of a smiling face."}
    },
    {
        "id": "nestle",
        "name": {"uz": "Nestlé", "ru": "Nestlé", "en": "Nestlé"},
        "category": "food",
        "country_code": "ch",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Nestl%C3%A9.svg/960px-Nestl%C3%A9.svg.png",
        "aliases": ["nestle", "nestlé", "нестле"],
        "fun_fact": {"uz": "Dunyodagi eng yirik oziq-ovqat va ichimliklar kompaniyasi bo'lib, uning logotipidagi uya qush bolalarini oziqlantirayotgan mehrli onani ifodalaydi.", "ru": "Крупнейший в мире производитель продуктов питания, чья эмблема с птичьим гнездом символизирует материнскую заботу и семью.", "en": "The world's largest food and beverage company; its bird's nest logo reflects founder Henri Nestlé's family crest and maternal nurturing."}
    },
    {
        "id": "nutella",
        "name": {"uz": "Nutella", "ru": "Nutella", "en": "Nutella"},
        "category": "food",
        "country_code": "it",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Nutella_logo.svg/960px-Nutella_logo.svg.png",
        "aliases": ["nutella", "нутелла"],
        "fun_fact": {"uz": "Har yili ishlab chiqariladigan Nutella bankalarini yer ekvatori bo'ylab 1.8 marta o'rash mumkin.", "ru": "Количество банок Nutella, производимых за год, может обернуть Землю вокруг экватора почти дважды.", "en": "The amount of Nutella produced worldwide each year could circle the globe nearly twice."}
    },
    {
        "id": "kitkat",
        "name": {"uz": "KitKat", "ru": "KitKat", "en": "KitKat"},
        "category": "food",
        "country_code": "gb",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/KitKat_US_logo.svg/960px-KitKat_US_logo.svg.png",
        "aliases": ["kitkat", "kit kat", "киткат", "кит кат"],
        "fun_fact": {"uz": "Yaponiyada KitKat 'Kitto Katsu' ('Albatta g'alaba qozonasan') deb jaranglagani uchun imtihon topshiruvchilarga omad keltiruvchi sovg'a hisoblanadi.", "ru": "В Японии выпущено более 300 уникальных вкусов KitKat (включая васаби и сакэ), так как название созвучно фразе «Обязательно победишь!».", "en": "In Japan, KitKat sounds like 'Kitto Katsu' ('surely win'), making it an immensely popular good-luck charm for students."}
    },
    {
        "id": "oreo",
        "name": {"uz": "Oreo", "ru": "Oreo", "en": "Oreo"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Oreo_Logo_2014.svg/960px-Oreo_Logo_2014.svg.png",
        "aliases": ["oreo", "орео", "печенье"],
        "fun_fact": {"uz": "Oreo XXI asrda dunyoda eng ko'p sotilgan pechenye bo'lib, 100 dan ortiq mamlakatda har yili 40 milliard dona sotiladi.", "ru": "Oreo — самое продаваемое печенье XXI века: ежегодно в мире съедается более 40 миллиардов штук.", "en": "Oreo is the best-selling cookie brand in the world, with over 40 billion cookies consumed annually."}
    },
    {
        "id": "pringles",
        "name": {"uz": "Pringles", "ru": "Pringles", "en": "Pringles"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Pringles_2021.svg/960px-Pringles_2021.svg.png",
        "aliases": ["pringles", "принглс", "чипсы"],
        "fun_fact": {"uz": "Pringles qutisini kashf qilgan Fred Bor vafot etgach, uning vasiyatiga binoan xoki Pringles qutisiga solib ko'milgan.", "ru": "Создатель знаменитой цилиндрической банки Pringles Фред Бор завещал похоронить часть своего праха в банке из-под чипсов.", "en": "Fred Baur, who designed the iconic cylindrical Pringles can, had part of his ashes buried in one per his will."}
    },
    {
        "id": "lays",
        "name": {"uz": "Lay's", "ru": "Lay's", "en": "Lay's"},
        "category": "food",
        "country_code": "us",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Lay%27s_logo_2019.svg/960px-Lay%27s_logo_2019.svg.png",
        "aliases": ["lay's", "lays", "лейз", "лейс", "чипсы"],
        "fun_fact": {"uz": "Lay's dunyoda birinchi bo'lib televizorda reklama qilingan kartoshka chipslari hisoblanadi (1944 yilda).", "ru": "Lay's стали первыми картофельными чипсами в истории, рекламировавшимися на телевидении (ещё в 1944 году).", "en": "Lay's was the first snack food brand to advertise on commercial television back in 1944."}
    },
]

LOGOS_BY_ID: Dict[str, Dict[str, Any]] = {l["id"]: l for l in LOGOS}


def get_logo_by_id(lid: str) -> Optional[Dict[str, Any]]:
    """Retrieve a logo entry by its unique string identifier."""
    return LOGOS_BY_ID.get(lid)


def get_random_logos(count: int = 1, category: Optional[str] = None) -> List[Dict[str, Any]]:
    """Sample random logos without replacement, optionally filtered by category."""
    pool = LOGOS
    if category:
        pool = [l for l in pool if l.get("category") == category]
    if not pool:
        return []
    return random.sample(pool, min(count, len(pool)))


def search_logo_by_alias(query: str) -> Optional[Dict[str, Any]]:
    """Find a logo matching a user input string across aliases or names."""
    q = query.strip().lower()
    if not q:
        return None
    for l in LOGOS:
        if q in l.get("aliases", []):
            return l
        for val in l.get("name", {}).values():
            if q == val.lower():
                return l
    return None
