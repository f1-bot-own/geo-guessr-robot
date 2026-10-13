"""
Dedicated Street Views and Map Panoramas Database for GeoGuessr Mode.
Features 55+ locations across all continents: Americas, Europe, Asia, Africa, Oceania.
Each location includes:
- Country ISO code and multilingual names (EN, RU, UZ)
- Geographic coordinates (lat, lng)
- Region / Street / Panorama title
- GeoGuessr meta clues (driving side, road markings, vegetation, architectural hints)
- Google Maps link for inspection after round completion
- High-resolution reliable image URL
"""

import random
from typing import List, Dict, Any, Optional, Set

STREETVIEWS: List[Dict[str, Any]] = [
    # ==================== NORTH & SOUTH AMERICA ====================
    {
        "id": "sv_us_times_square",
        "country_code": "us",
        "country_name": {"en": "United States", "ru": "США", "uz": "AQSH"},
        "location": {"en": "Times Square, New York City", "ru": "Таймс-сквер, Нью-Йорк", "uz": "Tayms-skver, Nyu-York"},
        "lat": 40.7580,
        "lng": -73.9855,
        "image_url": "https://images.unsplash.com/photo-1534430480872-3498386e7856?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Dense urban canyon, minimal deciduous street trees", "ru": "Городской каньон, минимум уличных деревьев", "uz": "Zich osmono'par binolar, kam sonli shahar daraxtlari"},
            "road_markings": {"en": "Yellow center dividing lines, white crosswalk bars, yellow cabs", "ru": "Желтая разделительная полоса, белые пешеходные полосы, желтые такси", "uz": "Sariq ajratuvchi chiziq, oq piyodalar yo'lagi, sariq taksilar"},
            "hint": {"en": "Dense skyscraper billboard canyon, yellow taxi cabs, traffic moves on the right.", "ru": "Каньон из небоскребов с яркими экранами, желтые такси, правостороннее движение.", "uz": "Yorqin reklama ekranlari bilan to'la osmono'par binolar, sariq taksilar va o'ng harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=40.758,-73.9855"
    },
    {
        "id": "sv_us_golden_gate",
        "country_code": "us",
        "country_name": {"en": "United States", "ru": "США", "uz": "AQSH"},
        "location": {"en": "Golden Gate Bridge Highway, San Francisco", "ru": "Шоссе моста Золотые Ворота, Сан-Франциско", "uz": "Oltin Darvoza ko'prigi trassasi, San-Fransisko"},
        "lat": 37.8199,
        "lng": -122.4783,
        "image_url": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Coastal chaparral, eucalyptus and cypress groves", "ru": "Прибрежные кустарники, эвкалипты и кипарисы", "uz": "Sohil bo'yi butalari, evkalipt va sarv daraxtlari"},
            "road_markings": {"en": "Movable zipper barrier, white dashed lane lines, green overhead highway signs", "ru": "Подвижный разделитель, белая пунктирная разметка, зеленые щиты шоссе", "uz": "Ko'chma ajratuvchi, oq chiziqlar, yashil yo'l belgilari"},
            "hint": {"en": "World-famous international orange suspension bridge tower with Pacific coastal fog.", "ru": "Оранжевые башни легендарного подвесного моста с тихоокеанским туманом.", "uz": "Mashhur to'q sariq osma ko'prik minoralari va Tinch okeani tumanlari."}
        },
        "maps_url": "https://www.google.com/maps?q=37.8199,-122.4783"
    },
    {
        "id": "sv_us_route66_arizona",
        "country_code": "us",
        "country_name": {"en": "United States", "ru": "США", "uz": "AQSH"},
        "location": {"en": "Historic Route 66, Arizona Desert", "ru": "Историческая трасса 66, пустыня Аризоны", "uz": "Tarixiy 66-yo'nalish, Arizona sahrosi"},
        "lat": 35.2828,
        "lng": -113.5658,
        "image_url": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Arid scrub, saguaro cacti, creosote bushes", "ru": "Засушливый кустарник, кактусы сагуаро, креозотовые кусты", "uz": "Quruq cho'l butalari, saguaro kaktuslari"},
            "road_markings": {"en": "Double solid yellow center lines, white dashed outer shoulder lines", "ru": "Двойная сплошная желтая линия по центру, белые обочины", "uz": "Markazda qo'shaloq sariq chiziq, oq chekka chiziqlar"},
            "hint": {"en": "Expansive arid desert horizon, double yellow center lines, classic southwestern scenery.", "ru": "Бескрайняя пустыня, двойная желтая разделительная линия, ландшафт юго-запада США.", "uz": "Cheksiz cho'l manzarasi, o'rtada qo'shaloq sariq chiziq va o'ng harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=35.2828,-113.5658"
    },
    {
        "id": "sv_ca_banff_highway",
        "country_code": "ca",
        "country_name": {"en": "Canada", "ru": "Канада", "uz": "Kanada"},
        "location": {"en": "Icefields Parkway, Banff National Park", "ru": "Айсфилдс Паркуэй, национальный парк Банф", "uz": "Muzliklar trassasi, Banff milliy bog'i"},
        "lat": 51.4968,
        "lng": -115.9281,
        "image_url": "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Subalpine coniferous boreal pine and spruce forest", "ru": "Субальпийский хвойный лес, сосны и ели", "uz": "Subalp ignabargli qarag'ay va qoraqarag'ay o'rmonlari"},
            "road_markings": {"en": "Single or double yellow centerlines, wide paved shoulders", "ru": "Желтая осевая линия, широкие асфальтированные обочины", "uz": "Sariq o'q chizig'i, keng asfaltlangan chetlar"},
            "hint": {"en": "Majestic snow-capped Rocky Mountains flanked by dense pine forests and clean asphalt.", "ru": "Величественные заснеженные Скалистые горы среди сосновых лесов.", "uz": "Qorli qoyali tog'lar, qalin qarag'ayzorlar va tekis asfalt trassa."}
        },
        "maps_url": "https://www.google.com/maps?q=51.4968,-115.9281"
    },
    {
        "id": "sv_ca_toronto_yonge",
        "country_code": "ca",
        "country_name": {"en": "Canada", "ru": "Канада", "uz": "Kanada"},
        "location": {"en": "Yonge-Dundas Square, Toronto", "ru": "Площадь Йонг-Дандас, Торонто", "uz": "Yonge-Dundas maydoni, Toronto"},
        "lat": 43.6561,
        "lng": -79.3802,
        "image_url": "https://images.unsplash.com/photo-1517090504586-fde19ea6066f?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Temperate northeastern maple and oak street landscaping", "ru": "Умеренные клены и дубы вдоль улиц", "uz": "Shahar ko'chalaridagi chinor va eman daraxtlari"},
            "road_markings": {"en": "White stop bars, yellow center dividing lines, streetcar street tracks", "ru": "Белые стоп-линии, желтая осевая, трамвайные пути на дороге", "uz": "Oq to'xtash chiziqlari, sariq o'q chizig'i, tramvay relslari"},
            "hint": {"en": "Commercial downtown hub with streetcar tracks and bilingual/English transit signs.", "ru": "Оживленный даунтаун с трамвайными путями и характерными канадскими знаками.", "uz": "Tramvay relslari bo'lgan zamonaviy markaz va Kanada shahar ko'rinishi."}
        },
        "maps_url": "https://www.google.com/maps?q=43.6561,-79.3802"
    },
    {
        "id": "sv_mx_reforma_cdmx",
        "country_code": "mx",
        "country_name": {"en": "Mexico", "ru": "Мексика", "uz": "Meksika"},
        "location": {"en": "Paseo de la Reforma, Mexico City", "ru": "Пасео-де-ла-Реформа, Мехико", "uz": "Paseo de la Reforma, Mexiko"},
        "lat": 19.4270,
        "lng": -99.1677,
        "image_url": "https://images.unsplash.com/photo-1585464231875-d9ef1f5ad396?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Subtropical palms, jacaranda trees, ash trees", "ru": "Субтропические пальмы, цветущая жакаранда, ясени", "uz": "Subtropik palma va binafsharang gullaydigan jakaranda daraxtlari"},
            "road_markings": {"en": "White lane dashes, red dedicated Metrobús lanes, pedestrian roundabouts", "ru": "Белые полосы, красные полосы для Метробуса, круговые развязки", "uz": "Oq chiziqlar, qizil avtobus yo'laklari, aylanma chorrahalar"},
            "hint": {"en": "Grand boulevard featuring the golden Angel of Independence column and palm trees.", "ru": "Широкий бульвар с золотым Ангелом независимости и рядами пальм.", "uz": "Oltin Mustaqillik Farishtasi monumenti va palma daraxtlari bilan mashhur xiyobon."}
        },
        "maps_url": "https://www.google.com/maps?q=19.427,-99.1677"
    },
    {
        "id": "sv_mx_cancun_kukulcan",
        "country_code": "mx",
        "country_name": {"en": "Mexico", "ru": "Мексика", "uz": "Meksika"},
        "location": {"en": "Boulevard Kukulcan, Cancun", "ru": "Бульвар Кукулькан, Канкун", "uz": "Kukulcan xiyoboni, Kankun"},
        "lat": 21.1350,
        "lng": -86.7450,
        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Tropical coconut palms, bougainvillea, mangroves", "ru": "Кокосовые пальмы, бугенвиллея, мангры", "uz": "Tropik kokos palmalari va dengiz sohili o'simliklari"},
            "road_markings": {"en": "White painted curbs, manicured grassy median strip", "ru": "Белые бордюры, ухоженная разделительная полоса с газоном", "uz": "Oq bo'yalgan bordyurlar, yam-yashil ajratuvchi maysazor"},
            "hint": {"en": "Caribbean seaside strip with coconut palms, turquoise water, resort architecture.", "ru": "Карибская прибрежная зона с кокосовыми пальмами и курортными отелями.", "uz": "Karib dengizi sohili, tropik palmalar va zamonaviy kurort mehmonxonalari."}
        },
        "maps_url": "https://www.google.com/maps?q=21.135,-86.745"
    },
    {
        "id": "sv_br_copacabana",
        "country_code": "br",
        "country_name": {"en": "Brazil", "ru": "Бразилия", "uz": "Braziliya"},
        "location": {"en": "Avenida Atlântica, Copacabana, Rio de Janeiro", "ru": "Авенида Атлантика, Копакабана, Рио-де-Жанейро", "uz": "Atlantika xiyoboni, Kopakabana, Rio-de-Janeyro"},
        "lat": -22.9711,
        "lng": -43.1822,
        "image_url": "https://images.unsplash.com/photo-1516306580123-e6e52b1b7b5f?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Atlantic forest coastal palms, almond trees", "ru": "Прибрежные пальмы атлантического леса, миндальные деревья", "uz": "Tropik Atlantika o'rmon palmalari va bodom daraxtlari"},
            "road_markings": {"en": "Iconic black and white wavy Portuguese mosaic pavement (calçadão)", "ru": "Черно-белая волнистая мозаичная плитка на широкой набережной", "uz": "Mashhur qora va oq to'lqinsimon mozaikali piyodalar yo'lagi"},
            "hint": {"en": "Legendary wave-patterned black and white promenade facing Atlantic waves.", "ru": "Знаменитая черно-белая волнистая набережная вдоль песчаного пляжа.", "uz": "Dengiz sohilidagi mashhur to'lqinsimon qora-oq plitkali xiyobon."}
        },
        "maps_url": "https://www.google.com/maps?q=-22.9711,-43.1822"
    },
    {
        "id": "sv_br_paulista",
        "country_code": "br",
        "country_name": {"en": "Brazil", "ru": "Бразилия", "uz": "Braziliya"},
        "location": {"en": "Avenida Paulista, São Paulo", "ru": "Авенида Паулиста, Сан-Паулу", "uz": "Paulista xiyoboni, San-Paulu"},
        "lat": -23.5615,
        "lng": -46.6559,
        "image_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Tropical park trees, Trianon park Atlantic rainforest reserve", "ru": "Тропические деревья парка Трианон, влажный лес", "uz": "Tropik park daraxtlari va yashil maydonlar"},
            "road_markings": {"en": "Central red cycle lane, wide sidewalks with Portuguese stone patterns", "ru": "Красная велодорожка по центру, тротуары с геометрической плиткой", "uz": "Markaziy qizil velosiped yo'lagi va keng piyodalar yo'li"},
            "hint": {"en": "Towering financial avenue with red central bike lane and distinct radio antennas.", "ru": "Финансовый проспект с красной велодорожкой и телевышками на крышах.", "uz": "Tomlarida teleradio antennalari va markazida qizil velo-yo'lagi bo'lgan ulkan ko'cha."}
        },
        "maps_url": "https://www.google.com/maps?q=-23.5615,-46.6559"
    },
    {
        "id": "sv_ar_9dejulio",
        "country_code": "ar",
        "country_name": {"en": "Argentina", "ru": "Аргентина", "uz": "Argentina"},
        "location": {"en": "Avenida 9 de Julio & Obelisk, Buenos Aires", "ru": "Авенида 9 июля и Обелиск, Буэнос-Айрес", "uz": "9-Iyul xiyoboni va Obelisk, Buenos-Ayres"},
        "lat": -34.6037,
        "lng": -58.3816,
        "image_url": "https://images.unsplash.com/photo-1589553416260-f586c8f1514f?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Pampas urban trees, tipa trees, purple jacarandas", "ru": "Деревья пампасов, типы, цветущие жакаранды", "uz": "Tipa va binafsharang jakaranda daraxtlari"},
            "road_markings": {"en": "Massive 16-lane roadway with dedicated center Metrobus lanes", "ru": "Широчайшая 16-полосная магистраль с выделенными линиями автобусов", "uz": "Dunyodagi eng keng 16 qatorli yo'l va markaziy Metrobus yo'laklari"},
            "hint": {"en": "One of the widest avenues in the world centered on an iconic white obelisk monument.", "ru": "Широчайший проспект мира с огромным белым обелиском по центру.", "uz": "Dunyodagi eng keng xiyobonlardan biri va uning markazidagi oq obelisk."}
        },
        "maps_url": "https://www.google.com/maps?q=-34.6037,-58.3816"
    },
    {
        "id": "sv_ar_patagonia_ruta40",
        "country_code": "ar",
        "country_name": {"en": "Argentina", "ru": "Аргентина", "uz": "Argentina"},
        "location": {"en": "Ruta Nacional 40, Santa Cruz, Patagonia", "ru": "Национальная трасса 40, Патагония", "uz": "Milliy 40-trassa, Patagoniya"},
        "lat": -49.3315,
        "lng": -72.8864,
        "image_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Patagonian steppe tuft grass, low wind-swept shrubs", "ru": "Патагонская степь, низкие кустарники, желтая сухая трава", "uz": "Patagoniya dashti, sariq quruq o'tlar va shamolga chidamli butalar"},
            "road_markings": {"en": "White dashed centerlines, unpaved gravel shoulders with Andean peaks in distance", "ru": "Белая прерывистая разметка, гравийные обочины, пики Анд на горизонте", "uz": "Oq uzuq-yuluq chiziq, shag'al chekkalar va uzoqda And tog'lari"},
            "hint": {"en": "Windy Patagonian steppe highway with distant jagged Andean peaks.", "ru": "Пустынная степная дорога Патагонии на фоне острых вершин Анд.", "uz": "Cheksiz dasht bo'ylab ketgan uzoq trassa va gorizontdagi qorli And cho'qqilari."}
        },
        "maps_url": "https://www.google.com/maps?q=-49.3315,-72.8864"
    },
    {
        "id": "sv_cl_costanera_santiago",
        "country_code": "cl",
        "country_name": {"en": "Chile", "ru": "Чили", "uz": "Chili"},
        "location": {"en": "Avenida Providencia & Gran Torre, Santiago", "ru": "Авенида Провиденсия, Сантьяго", "uz": "Providencia xiyoboni, Santyago"},
        "lat": -33.4172,
        "lng": -70.6067,
        "image_url": "https://images.unsplash.com/photo-1519999482648-25049ddd37b1?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Mediterranean scrub, palms and poplars with backdrop of snowcapped Andes", "ru": "Средиземноморская растительность, пальмы, тополя у подножия Анд", "uz": "O'rta yer dengizi iqlimidagi butalar va qorli And tog'lari etagi"},
            "road_markings": {"en": "White lane dashes, red cycle paths, modern urban LED traffic signals", "ru": "Белая разметка, красные велодорожки, современные светофоры", "uz": "Oq yo'l chiziqlari, qizil velosiped yo'li va zamonaviy svetoforlar"},
            "hint": {"en": "Tallest skyscraper in South America towering beneath the towering snow-capped Andes.", "ru": "Высочайший небоскреб Южной Америки на фоне гигантских снежных Анд.", "uz": "Janubiy Amerikadagi eng baland osmono'par bino va orqa fondagi ulkan And tog'lari."}
        },
        "maps_url": "https://www.google.com/maps?q=-33.4172,-70.6067"
    },
    {
        "id": "sv_cl_atacama_highway",
        "country_code": "cl",
        "country_name": {"en": "Chile", "ru": "Чили", "uz": "Chili"},
        "location": {"en": "Ruta 5 Norte, Atacama Desert", "ru": "Трасса 5 Норте, пустыня Атакама", "uz": "5-Shimoliy trassa, Atakama sahrosi"},
        "lat": -23.8634,
        "lng": -69.1328,
        "image_url": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Hyper-arid desert, virtually zero vegetation", "ru": "Экстремально засушливая пустыня, полное отсутствие растений", "uz": "O'ta quruq sahro, o'simliklar deyarli yo'q"},
            "road_markings": {"en": "White broken centerline, yellow edge markings, white kilometer posts", "ru": "Белая прерывистая по центру, желтые края, белые километровые столбики", "uz": "Oq o'q chizig'i, sariq chetlar va oq kilometr belgilari"},
            "hint": {"en": "The driest non-polar desert on Earth, reddish-brown stony soil under cobalt blue sky.", "ru": "Самая сухая пустыня на Земле с красно-коричневой каменистой почвой.", "uz": "Yer yuzidagi eng quruq sahro, qizg'ish toshli tuproq va moviy osmon."}
        },
        "maps_url": "https://www.google.com/maps?q=-23.8634,-69.1328"
    },
    {
        "id": "sv_co_bogota_carrera7",
        "country_code": "co",
        "country_name": {"en": "Colombia", "ru": "Колумбия", "uz": "Kolumbiya"},
        "location": {"en": "Carrera 7, Downtown Bogotá", "ru": "Каррера 7, центр Боготы", "uz": "7-Karrera ko'chasi, Bogota markazi"},
        "lat": 4.6097,
        "lng": -74.0817,
        "image_url": "https://images.unsplash.com/photo-1583531352515-8884af319dc1?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "High-altitude tropical Andean flora, eucalyptus, wax palms", "ru": "Высокогорная флора Анд, эвкалипты, восковые пальмы", "uz": "Baland tog'li And o'simliklari, evkalipt va sarv daraxtlari"},
            "road_markings": {"en": "Pedestrianized patterned red brick paving, yellow license plates on vehicles", "ru": "Пешеходная зона из красного кирпича, желтые номерные знаки машин", "uz": "Qizil g'ishtli piyodalar yo'lagi, avtomobillarda sariq davlat raqamlari"},
            "hint": {"en": "High mountain capital plateau with red brick towers and distinct yellow car license plates.", "ru": "Высокогорная столица с красно-кирпичными зданиями и желтыми номерами авто.", "uz": "Qizil g'ishtli binolar va avtomobillarning sariq davlat raqamlari bilan mashhur poytaxt."}
        },
        "maps_url": "https://www.google.com/maps?q=4.6097,-74.0817"
    },
    {
        "id": "sv_pe_lima_miraflores",
        "country_code": "pe",
        "country_name": {"en": "Peru", "ru": "Перу", "uz": "Peru"},
        "location": {"en": "Malecón de Miraflores, Lima", "ru": "Малекон Мирафлорес, Лима", "uz": "Miraflores sohili, Lima"},
        "lat": -12.1220,
        "lng": -77.0298,
        "image_url": "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Coastal desert green strip with manicured palms and coastal park lawns", "ru": "Зеленая полоса прибрежных парков, пальмы вдоль обрыва", "uz": "Tinch okeani bo'yidagi qoyali sohil parklari va palmazorlar"},
            "road_markings": {"en": "White lane markings, cliffside highway below (Circuito de Playas)", "ru": "Белая разметка, внизу у океана скоростная трасса Circuito de Playas", "uz": "Qoya tepasidagi xiyobon va pastdagi okean bo'yi trassasi"},
            "hint": {"en": "High coastal cliff overlooking the Pacific Ocean with paragliders and green parks.", "ru": "Высокий обрыв над Тихим океаном с парками и видом на пляжи.", "uz": "Tinch okeani ustidagi baland qoyalar va ko'kalamzorlashtirilgan xiyobon."}
        },
        "maps_url": "https://www.google.com/maps?q=-12.122,-77.0298"
    },

    # ==================== EUROPE ====================
    {
        "id": "sv_fr_champs_elysees",
        "country_code": "fr",
        "country_name": {"en": "France", "ru": "Франция", "uz": "Fransiya"},
        "location": {"en": "Avenue des Champs-Élysées, Paris", "ru": "Елисейские поля, Париж", "uz": "Yelisey maydonlari, Parij"},
        "lat": 48.8698,
        "lng": 2.3075,
        "image_url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Precisely pruned plane trees lining wide avenues", "ru": "Аккуратно подстриженные платаны вдоль широких тротуаров", "uz": "Tartibli qirqilgan chinor daraxtlari"},
            "road_markings": {"en": "White dashed lane markings, blue European license plates with F stripe", "ru": "Белая прерывистая разметка, номера с синей полосой F", "uz": "Oq chiziqlar, mashinalarda 'F' belgili ko'k Yevropa davlat raqamlari"},
            "hint": {"en": "Grand avenue with Haussmannian limestone facades leading to the Arc de Triomphe.", "ru": "Широкий бульвар с османовскими зданиями из светлого камня, ведущий к Триумфальной арке.", "uz": "Triumfal arkaga olib boruvchi go'zal xiyobon va mashhur Usmon me'morchiligi."}
        },
        "maps_url": "https://www.google.com/maps?q=48.8698,2.3075"
    },
    {
        "id": "sv_fr_nice_promenade",
        "country_code": "fr",
        "country_name": {"en": "France", "ru": "Франция", "uz": "Fransiya"},
        "location": {"en": "Promenade des Anglais, Nice", "ru": "Английская набережная, Ницца", "uz": "Ingliz qirg'og'i, Nitssa"},
        "lat": 43.6950,
        "lng": 7.2650,
        "image_url": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Mediterranean palm trees (Phoenix canariensis) along pebble beach", "ru": "Финиковые пальмы вдоль галечного пляжа лазурного берега", "uz": "O'rta yer dengizi xurmo palmalari va toshli sohil"},
            "road_markings": {"en": "Blue cycle lane markings, wide light-colored pedestrian promenade", "ru": "Синяя велополоса, светлая широкая пешеходная набережная", "uz": "Ko'k velosiped yo'lagi va ochiq rangli keng piyodalar yo'li"},
            "hint": {"en": "French Riviera seafront avenue lined with Canary Island date palms and blue Mediterranean sea.", "ru": "Лазурный берег с канарскими пальмами и синими стульями на набережной.", "uz": "Moviy qirg'oq bo'ylab ketgan palma daraxtli xiyobon va O'rta yer dengizi."}
        },
        "maps_url": "https://www.google.com/maps?q=43.695,7.265"
    },
    {
        "id": "sv_de_berlin_unterdenlinden",
        "country_code": "de",
        "country_name": {"en": "Germany", "ru": "Германия", "uz": "Germaniya"},
        "location": {"en": "Unter den Linden & Brandenburg Gate, Berlin", "ru": "Унтер-ден-Линден и Бранденбургские ворота, Берлин", "uz": "Unter den Linden va Brandenburg darvozasi, Berlin"},
        "lat": 52.5169,
        "lng": 13.3889,
        "image_url": "https://images.unsplash.com/photo-1560969184-10fe8719e047?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Linden (lime) trees lining central pedestrian promenade", "ru": "Липовые деревья вдоль центрального пешеходного бульвара", "uz": "Markaziy piyodalar xiyoboni bo'ylab jo'ka (lipa) daraxtlari"},
            "road_markings": {"en": "White lane markings, Ampelmännchen pedestrian traffic signals", "ru": "Белая разметка, знаменитые светофоры с человечком Ампельман", "uz": "Oq chiziqlar va mashhur shlyapali odamcha (Ampelmännchen) svetoforlari"},
            "hint": {"en": "Historic boulevard leading directly to the neoclassical Brandenburg Gate.", "ru": "Исторический бульвар, ведущий к Бранденбургским воротам.", "uz": "Brandenburg darvozasiga olib boruvchi tarixiy jo'ka daraxtli xiyobon."}
        },
        "maps_url": "https://www.google.com/maps?q=52.5169,13.3889"
    },
    {
        "id": "sv_de_autobahn_bavaria",
        "country_code": "de",
        "country_name": {"en": "Germany", "ru": "Германия", "uz": "Germaniya"},
        "location": {"en": "Autobahn A8 near Chiemsee, Bavaria", "ru": "Автобан А8 у озера Кимзе, Бавария", "uz": "A8 Avtobani, Bavariya"},
        "lat": 47.8122,
        "lng": 11.9542,
        "image_url": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Bavarian spruce forests and green Alpine foothills pastures", "ru": "Баварские еловые леса и сочные альпийские луга", "uz": "Bavariya archazorlari va yashil alp maysazorlari"},
            "road_markings": {"en": "Blue motorway signs, solid white edge lines, no general speed limit signs", "ru": "Синие указатели автобана, белая сплошная по краю, немецкие знаки", "uz": "Moviy avtoban ko'rsatkichlari, sifatli beton-asfalt yo'l"},
            "hint": {"en": "Pristine German highway with blue exit signs against a backdrop of Bavarian Alps.", "ru": "Немецкий скоростной автобан с синими указателями на фоне Альп.", "uz": "Moviy belgili nemis avtobani va orqa fondagi Bavariya tog'lari."}
        },
        "maps_url": "https://www.google.com/maps?q=47.8122,11.9542"
    },
    {
        "id": "sv_gb_london_westminster",
        "country_code": "gb",
        "country_name": {"en": "United Kingdom", "ru": "Великобритания", "uz": "Buyuk Britaniya"},
        "location": {"en": "Westminster Bridge & Big Ben, London", "ru": "Вестминстерский мост и Биг-Бен, Лондон", "uz": "Vestminster ko'prigi va Big Ben, London"},
        "lat": 51.5007,
        "lng": -0.1246,
        "image_url": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "English plane trees along Thames Embankment", "ru": "Платаны вдоль набережной Темзы", "uz": "Temza qirg'og'idagi chinor daraxtlari"},
            "road_markings": {"en": "Double red/yellow curb lines, white zig-zag pedestrian crossing lines, red double-decker buses", "ru": "Зигзагообразная белая разметка у переходов, красные двухэтажные автобусы", "uz": "O'tish joylaridagi oq zigzag chiziqlar, qizil ikki qavatli avtobuslar"},
            "hint": {"en": "Left-hand traffic, red double-decker buses, and Elizabeth Tower (Big Ben).", "ru": "Левостороннее движение, красные даблдекеры и башня Биг-Бен.", "uz": "Chap tomonlama harakat, mashhur qizil ikki qavatli avtobuslar va Big Ben."}
        },
        "maps_url": "https://www.google.com/maps?q=51.5007,-0.1246"
    },
    {
        "id": "sv_gb_edinburgh_royalmile",
        "country_code": "gb",
        "country_name": {"en": "United Kingdom", "ru": "Великобритания", "uz": "Buyuk Britaniya"},
        "location": {"en": "Royal Mile, Old Town Edinburgh, Scotland", "ru": "Королевская Миля, Эдинбург, Шотландия", "uz": "Qirollik mili, Edinburg, Shotlandiya"},
        "lat": 55.9505,
        "lng": -3.1895,
        "image_url": "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Maritime temperate stone urban setting, minimal foliage", "ru": "Суровые шотландские каменные фасады без зелени", "uz": "Tarixiy tosh binolar va qadimiy ko'chalar"},
            "road_markings": {"en": "Cobblestone roadway, yellow no-parking curb lines, left-hand traffic", "ru": "Булыжная мостовая, желтые линии у бордюра, движение слева", "uz": "Tosh terilgan ko'cha (bruschatka), sariq chekka chiziqlar, chap harakat"},
            "hint": {"en": "Dark cobblestone streets lined by medieval stone tenements, left-side driving.", "ru": "Брусчатая улица со старинными каменными домами и левосторонним движением.", "uz": "Shotlandiyaning toshli qadimiy ko'chalari va chap tomonlama harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=55.9505,-3.1895"
    },
    {
        "id": "sv_it_rome_fori_imperiali",
        "country_code": "it",
        "country_name": {"en": "Italy", "ru": "Италия", "uz": "Italiya"},
        "location": {"en": "Via dei Fori Imperiali, Rome", "ru": "Виа деи Фори Империали, Рим", "uz": "Fori Imperiali ko'chasi, Rim"},
        "lat": 41.8925,
        "lng": 12.4853,
        "image_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Iconic umbrella stone pine trees (Pinus pinea) and Italian cypresses", "ru": "Знаменитые римские пинии в форме зонтиков и стройные кипарисы", "uz": "Soyabonsimon pinus qarag'aylari va sarv daraxtlari"},
            "road_markings": {"en": "Dark basalt cobblestones (sanpietrini), white painted lane dividers", "ru": "Черная базальтовая брусчатка санпьетрини, белая разметка", "uz": "Qora bazalt toshli yo'l (sanpietrini) va oq chiziqlar"},
            "hint": {"en": "Ancient Roman forum ruins flanked by towering umbrella pine trees toward the Colosseum.", "ru": "Римские руины среди высоких зонтичных сосен-пиний с видом на Колизей.", "uz": "Soyabonsimon qarag'aylar orasidagi qadimiy Rim xarobalari va Kolizey manzarasi."}
        },
        "maps_url": "https://www.google.com/maps?q=41.8925,12.4853"
    },
    {
        "id": "sv_es_madrid_granvia",
        "country_code": "es",
        "country_name": {"en": "Spain", "ru": "Испания", "uz": "Ispaniya"},
        "location": {"en": "Gran Vía, Madrid", "ru": "Гран-Виа, Мадрид", "uz": "Gran Via ko'chasi, Madrid"},
        "lat": 40.4200,
        "lng": -3.7058,
        "image_url": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Planted plane trees in sidewalk grates", "ru": "Одиночные платаны в решетках на широких тротуарах", "uz": "Piyodalar yo'lagidagi panjarali daraxtlar"},
            "road_markings": {"en": "White lane dashes, red dedicated bus/taxi lane surface", "ru": "Белые полосы, выделенная полоса для такси и автобусов", "uz": "Oq chiziqlar, maxsus avtobus va taksi yo'laklari"},
            "hint": {"en": "Grand ornate early 20th-century eclectic Spanish facades, blue Spanish street signs.", "ru": "Пышные исторические здания начала XX века и белые такси с красной диагональной полосой.", "uz": "Madridning mashhur 20-asr boshidagi hashamatli binolari va oq taksilari."}
        },
        "maps_url": "https://www.google.com/maps?q=40.42,-3.7058"
    },
    {
        "id": "sv_nl_amsterdam_damrak",
        "country_code": "nl",
        "country_name": {"en": "Netherlands", "ru": "Нидерланды", "uz": "Niderlandiya"},
        "location": {"en": "Damrak Canal Street, Amsterdam", "ru": "Дамрак, Амстердам", "uz": "Damrak kanali ko'chasi, Amsterdam"},
        "lat": 52.3738,
        "lng": 4.8972,
        "image_url": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Canal-side deciduous elms and lindens", "ru": "Вязы и липы вдоль набережной канала", "uz": "Kanal bo'yidagi daraxtlar"},
            "road_markings": {"en": "Red asphalt designated cycle tracks (fietspad), shark-teeth give-way road markings", "ru": "Красные асфальтовые велодорожки, треугольная разметка 'зубы акулы'", "uz": "Qizil asfaltli velosiped yo'laklari va 'akula tishlari' uchburchak yo'l belgilari"},
            "hint": {"en": "Narrow brick canal houses with hoist hooks, ubiquitous red bicycle lanes, canal water.", "ru": "Узкие кирпичные дома с крюками на крышах вдоль канала и красные велодорожки.", "uz": "Qizil g'ishtli tor uylar, kanal suvi va hamma joyda qizil velosiped yo'laklari."}
        },
        "maps_url": "https://www.google.com/maps?q=52.3738,4.8972"
    },
    {
        "id": "sv_no_atlantic_road",
        "country_code": "no",
        "country_name": {"en": "Norway", "ru": "Норвегия", "uz": "Norvegiya"},
        "location": {"en": "Atlanterhavsveien (Atlantic Ocean Road), Averøy", "ru": "Атлантическая дорога, Аверёй", "uz": "Atlantika yo'li (Atlanterhavsveien), Averoy"},
        "lat": 63.0167,
        "lng": 7.3556,
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Coastal tundra heath, moss, lichens, barren coastal rocks", "ru": "Прибрежная тундра, вереск, мох, скалы без деревьев", "uz": "Shimoliy sohil qoyalari, mox va daraxtsiz ochiq manzaralar"},
            "road_markings": {"en": "Dashed white centerline, yellow road marker posts in winter, cantilever bridges", "ru": "Белая пунктирная осевая линия, изогнутые мосты над волнами океана", "uz": "Oq o'q chizig'i, okean ustidagi egri ko'priklar"},
            "hint": {"en": "Curved roller-coaster style cantilever bridge hopping between rocky islets in the North Atlantic.", "ru": "Знаменитый изогнутый мост над бурными волнами Северной Атлантики.", "uz": "Shimoliy Atlantika toshli orollari uzra o'tgan mashhur egri ko'prik."}
        },
        "maps_url": "https://www.google.com/maps?q=63.0167,7.3556"
    },
    {
        "id": "sv_se_stockholm_kungsgatan",
        "country_code": "se",
        "country_name": {"en": "Sweden", "ru": "Швеция", "uz": "Shvetsiya"},
        "location": {"en": "Kungsgatan & Kungstornen, Stockholm", "ru": "Кунгсгатан, Стокгольм", "uz": "Kungsgatan ko'chasi, Stokgolm"},
        "lat": 59.3361,
        "lng": 18.0686,
        "image_url": "https://images.unsplash.com/photo-1509356843151-3e7d96241e11?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Boreal birch and pine nearby, pristine Nordic urban trees", "ru": "Березы и северные хвойные деревья", "uz": "Shimoliy qayin va qarag'ay daraxtlari"},
            "road_markings": {"en": "White lane stripes, yellow background warning road signs, clean stone curbs", "ru": "Белая разметка, желтые дорожные знаки предупреждения, скандинавский стиль", "uz": "Sariq fonli skandinavcha ogohlantirish belgilari va toza tosh bordyurlar"},
            "hint": {"en": "Nordic street with early 20th-century twin towers and distinct yellow-backed warning signs.", "ru": "Шведская улица с башнями-близнецами Кунгсторнен и желтыми дорожными знаками.", "uz": "Shvetsiyaning mashhur egizak minoralari va sariq fonli yo'l belgilari."}
        },
        "maps_url": "https://www.google.com/maps?q=59.3361,18.0686"
    },
    {
        "id": "sv_ch_zurich_bahnhofstrasse",
        "country_code": "ch",
        "country_name": {"en": "Switzerland", "ru": "Швейцария", "uz": "Shveysariya"},
        "location": {"en": "Bahnhofstrasse, Zurich", "ru": "Банхофштрассе, Цюрих", "uz": "Banhofshtrasse, Syurix"},
        "lat": 47.3717,
        "lng": 8.5397,
        "image_url": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Precisely pruned linden trees lining pedestrian shopping street", "ru": "Аккуратные липы вдоль элегантной пешеходной улицы", "uz": "Tartibli lipa daraxtlari"},
            "road_markings": {"en": "Cobblestone and tram tracks, absence of overhead wire clutter, Swiss cross plaques", "ru": "Трамвайные рельсы на пешеходной мостовой, швейцарские флаги", "uz": "Tramvay relslari, tosh terilgan yo'lak va Shveysariya bayroqlari"},
            "hint": {"en": "Immaculate avenue with sleek blue-and-white VBZ trams, luxury watch boutiques, Swiss flags.", "ru": "Безупречная улица с сине-белыми трамваями и витринами швейцарских часов.", "uz": "Ko'k-oq rangli zamonaviy tramvaylar, soat do'konlari va Shveysariya bayroqlari."}
        },
        "maps_url": "https://www.google.com/maps?q=47.3717,8.5397"
    },
    {
        "id": "sv_gr_athens_syntagma",
        "country_code": "gr",
        "country_name": {"en": "Greece", "ru": "Греция", "uz": "Gretsiya"},
        "location": {"en": "Syntagma Square & Hellenic Parliament, Athens", "ru": "Площадь Синтагма, Афины", "uz": "Sintagma maydoni, Afina"},
        "lat": 37.9753,
        "lng": 23.7361,
        "image_url": "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Bitter orange trees, olive trees, oleander, Mediterranean cypresses", "ru": "Горькие апельсиновые деревья, олеандры, оливы", "uz": "Achchiq apelsin daraxtlari, zaytun va sarvlar"},
            "road_markings": {"en": "White lane dashes, yellow taxis, Greek script road signs", "ru": "Белая разметка, желтые такси, дорожные указатели на греческом алфавите", "uz": "Oq chiziqlar, sariq taksilar, yunon alifbosidagi yo'l belgilari"},
            "hint": {"en": "Greek alphabet road signage, yellow cabs, orange trees in front of neoclassical parliament.", "ru": "Указатели с греческими буквами, желтые такси и цитрусовые деревья.", "uz": "Yunon yozuvidagi yo'l belgilari, sariq taksilar va parlament maydoni."}
        },
        "maps_url": "https://www.google.com/maps?q=37.9753,23.7361"
    },
    {
        "id": "sv_is_ring_road_vik",
        "country_code": "is",
        "country_name": {"en": "Iceland", "ru": "Исландия", "uz": "Islandiya"},
        "location": {"en": "Route 1 (Ring Road) near Vík í Mýrdal", "ru": "Кольцевая дорога (Трасса 1) близ Вика", "uz": "1-halqa yo'li, Vik shaharchasi yaqinida"},
        "lat": 63.4186,
        "lng": -19.0060,
        "image_url": "https://images.unsplash.com/photo-1504893524553-b855bce32c67?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Lush green summer moss, lupine flowers, volcanic black sand, zero trees", "ru": "Зеленый вулканический мох, синие люпины, черный песок, полное отсутствие деревьев", "uz": "Vulkanik qora qumlar, yashil mox va binafsharang lyupin gullari, daraxtlar yo'q"},
            "road_markings": {"en": "Yellow road edge marker stakes with reflectors, narrow two-lane asphalt", "ru": "Желтые столбики со светоотражателями по обочинам, узкая двухполоска", "uz": "Yo'l chetidagi sariq ustunchalar, tor ikki qatorli sifatli asfalt"},
            "hint": {"en": "Bright yellow road-side marker stakes, black volcanic soil, vibrant green moss, no trees.", "ru": "Желтые вешки по краям дороги, черная лава, зеленый мох и отсутствие деревьев.", "uz": "Yo'l chetidagi sariq belgilovchi ustunchalar, qora vulqon tuprog'i va daraxtsiz manzara."}
        },
        "maps_url": "https://www.google.com/maps?q=63.4186,-19.006"
    },
    {
        "id": "sv_pl_warsaw_krakowskie",
        "country_code": "pl",
        "country_name": {"en": "Poland", "ru": "Польша", "uz": "Polsha"},
        "location": {"en": "Krakowskie Przedmieście, Warsaw", "ru": "Краковское предместье, Варшава", "uz": "Krakowskie Przedmiescie ko'chasi, Varshava"},
        "lat": 52.2430,
        "lng": 21.0150,
        "image_url": "https://images.unsplash.com/photo-1519197924294-4ba991a11128?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Central European lindens and maples along stone sidewalks", "ru": "Липы и клены вдоль тротуаров из гранита", "uz": "Jo'ka va chinor daraxtlari"},
            "road_markings": {"en": "Granite paving stones, yellow and blue Warsaw municipal buses", "ru": "Гранитная брусчатка, желто-красные городские автобусы", "uz": "Granit toshli yo'l, sariq-qizil shahar avtobuslari"},
            "hint": {"en": "Historic Royal Route in Poland paved with granite, lined by Baroque and Classical palaces.", "ru": "Королевский тракт в Варшаве с гранитным покрытием и барочными фасадами.", "uz": "Varshavadagi granit toshli Qirollik yo'li va tarixiy saroylar."}
        },
        "maps_url": "https://www.google.com/maps?q=52.243,21.015"
    },
    {
        "id": "sv_pt_lisbon_liberdade",
        "country_code": "pt",
        "country_name": {"en": "Portugal", "ru": "Португалия", "uz": "Portugaliya"},
        "location": {"en": "Avenida da Liberdade, Lisbon", "ru": "Авенида да Либердаде, Лиссабон", "uz": "Ozodlik xiyoboni (Avenida da Liberdade), Lissabon"},
        "lat": 38.7205,
        "lng": -9.1460,
        "image_url": "https://images.unsplash.com/photo-1588614959060-4d144f28b207?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Mature plane trees, palm trees, subtropical garden kiosks", "ru": "Тенистые платаны и пальмы, киоски в садах", "uz": "Sokin chinorlar va palma daraxtlari"},
            "road_markings": {"en": "Intricate black-and-white calçada portuguesa mosaic stone pavement patterns", "ru": "Знаменитая португальская мозаика кальсада на тротуарах", "uz": "Oq-qora toshlardan terilgan portugal mozaikasi (calcada)"},
            "hint": {"en": "Lush boulevard with black-and-white mosaic pedestrian sidewalks and yellow trams nearby.", "ru": "Тенистый бульвар со знаменитой португальской мозаикой на тротуарах.", "uz": "Oq-qora naqshli toshli piyodalar yo'lagi va sarvqomat chinorlar bilan mashhur xiyobon."}
        },
        "maps_url": "https://www.google.com/maps?q=38.7205,-9.146"
    },

    # ==================== ASIA ====================
    {
        "id": "sv_jp_tokyo_shibuya",
        "country_code": "jp",
        "country_name": {"en": "Japan", "ru": "Япония", "uz": "Yaponiya"},
        "location": {"en": "Shibuya Scramble Crossing, Tokyo", "ru": "Перекресток Сибуя, Токио", "uz": "Shibuya chorrahasi, Tokio"},
        "lat": 35.6595,
        "lng": 139.7005,
        "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Minimal urban foliage, ginkgo trees on main avenues", "ru": "Минимум зелени, деревья гинкго на проспектах", "uz": "Ginkgo daraxtlari va neon chiroqlar"},
            "road_markings": {"en": "Massive diagonal zebra crossing, overhead cantilever Japanese signs with kanji", "ru": "Огромный диагональный пешеходный переход, японские дорожные указатели с иероглифами", "uz": "Katta diagonal piyodalar yo'lagi, yaponcha iyeroglifli belgilar"},
            "hint": {"en": "World's busiest scramble crossing, kanji road signs, traffic driving strictly on the left.", "ru": "Самый оживленный перекресток в мире, японские иероглифы и левостороннее движение.", "uz": "Dunyodagi eng gavjum piyodalar chorrahasi, yaponcha yozuvlar va chap harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=35.6595,139.7005"
    },
    {
        "id": "sv_jp_osaka_dotonbori",
        "country_code": "jp",
        "country_name": {"en": "Japan", "ru": "Япония", "uz": "Yaponiya"},
        "location": {"en": "Dotonbori Canal Street, Osaka", "ru": "Улица Дотонбори, Осака", "uz": "Dotonbori kanali ko'chasi, Osaka"},
        "lat": 34.6687,
        "lng": 135.5013,
        "image_url": "https://images.unsplash.com/photo-1590559899731-a382839e5549?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Dense canal promenade, potted shrubs outside izakayas", "ru": "Набережная канала, фонари, изакаи", "uz": "Kanal bo'yi ko'chasi va restoranlar"},
            "road_markings": {"en": "Pedestrian canal walkways with yellow tactile paving for the blind", "ru": "Желтая тактильная плитка для незрячих, японские неоновые вывески", "uz": "Sariq taktil yo'laklar, yaponcha neon yozuvlari"},
            "hint": {"en": "Famous canal street with giant mechanical crabs and glowing Glico running man billboard.", "ru": "Знаменитая улица с гигантским крабом и светящимися рекламными щитами в Японии.", "uz": "Katta harakatlanuvchi qisqichbaqa va yorqin reklama peshtaxtalari bilan mashhur ko'cha."}
        },
        "maps_url": "https://www.google.com/maps?q=34.6687,135.5013"
    },
    {
        "id": "sv_kr_seoul_gangnam",
        "country_code": "kr",
        "country_name": {"en": "South Korea", "ru": "Южная Корея", "uz": "Janubiy Koreya"},
        "location": {"en": "Teheran-ro, Gangnam, Seoul", "ru": "Тегеран-ро, Каннам, Сеул", "uz": "Tegeran-ro ko'chasi, Gangnam, Seul"},
        "lat": 37.5000,
        "lng": 127.0365,
        "image_url": "https://images.unsplash.com/photo-1538485399081-7191377e8241?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Potted ginkgo trees and pine trees along modern wide granite sidewalks", "ru": "Деревья гинкго и аккуратные сосны на гранитных тротуарах", "uz": "Ginkgo va qarag'ay daraxtlari bilan bezatilgan granit yo'laklar"},
            "road_markings": {"en": "Blue bus lane lines in center, Hangul road paint and Korean signage", "ru": "Синяя полоса для автобусов по центру, надписи на хангыле на асфальте", "uz": "Markaziy ko'k avtobus yo'lagi va asfaltda koreyscha hangul yozuvlari"},
            "hint": {"en": "High-tech skyscraper boulevard with blue bus lanes, Hangul writing, right-side driving.", "ru": "Широкий хай-тек проспект с корейскими надписями хангыль и синими автобусными полосами.", "uz": "Ko'k avtobus yo'laklari, koreyscha hangul yozuvlari va osmono'par binolar."}
        },
        "maps_url": "https://www.google.com/maps?q=37.5,127.0365"
    },
    {
        "id": "sv_th_bangkok_sukhumvit",
        "country_code": "th",
        "country_name": {"en": "Thailand", "ru": "Таиланд", "uz": "Tailand"},
        "location": {"en": "Sukhumvit Road under BTS Skytrain, Bangkok", "ru": "Улица Сукхумвит под эстакадой скайтрейна, Бангкок", "uz": "Sukxumvit ko'chasi, Skytrain ostida, Bangkok"},
        "lat": 13.7380,
        "lng": 100.5600,
        "image_url": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Tropical banyan trees, palms, lush hanging roadside plants", "ru": "Тропические баньяны, пальмы, буйная зелень", "uz": "Tropik banyan va palma daraxtlari"},
            "road_markings": {"en": "Elevated concrete Skytrain pillars, pink taxis, Thai script signage", "ru": "Бетонные опоры надземного метро, ярко-розовые такси, тайский шрифт", "uz": "Yer usti metrosi beton ustunlari, pushti taksilar va tay yozuvlari"},
            "hint": {"en": "Elevated concrete rail bridge overhead, bright pink taxis, distinctive Thai script, left-hand traffic.", "ru": "Эстакада метро над дорогой, ярко-розовые такси, тайские буквы и левостороннее движение.", "uz": "Yo'l ustidagi metro ko'prigi, pushti rangli taksilar va tay yozuvlari."}
        },
        "maps_url": "https://www.google.com/maps?q=13.738,100.56"
    },
    {
        "id": "sv_sg_marina_bay",
        "country_code": "sg",
        "country_name": {"en": "Singapore", "ru": "Сингапур", "uz": "Singapur"},
        "location": {"en": "Marina Boulevard & Bayfront, Singapore", "ru": "Марина Бульвар, Сингапур", "uz": "Marina bulvari, Singapur"},
        "lat": 1.2838,
        "lng": 103.8591,
        "image_url": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Pristine lush equatorial rainforest trees, rain trees with fern-covered trunks", "ru": "Идеально подстриженные тропические дождевые деревья с папоротниками", "uz": "Mukammal parvarishlangan tropik daraxtlar va yashil maysazorlar"},
            "road_markings": {"en": "Yellow zig-zag lines near pedestrian crossings, Electronic Road Pricing (ERP) gantries", "ru": "Желтые зигзагообразные линии у переходов, рамки системы ERP", "uz": "Sariq zigzag chiziqlar va elektron to'lov (ERP) arkalari"},
            "hint": {"en": "World-famous hotel with three towers supporting a boat rooftop, ultra-clean streets, left-side traffic.", "ru": "Ультрачистые улицы, отель из трех башен с кораблем на крыше и левостороннее движение.", "uz": "Dunyodagi eng toza ko'chalar, tomi kemasimon mashhur 3 minorali mehmonxona."}
        },
        "maps_url": "https://www.google.com/maps?q=1.2838,103.8591"
    },
    {
        "id": "sv_my_kl_bukit_bintang",
        "country_code": "my",
        "country_name": {"en": "Malaysia", "ru": "Малайзия", "uz": "Malayziya"},
        "location": {"en": "Jalan Bukit Bintang, Kuala Lumpur", "ru": "Джалан Букит Бинтанг, Куала-Лумпур", "uz": "Jalan Bukit Bintang ko'chasi, Kuala-Lumpur"},
        "lat": 3.1466,
        "lng": 101.7115,
        "image_url": "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Tropical equatorial palms and lush ficus trees", "ru": "Экваториальные пальмы и фикусы", "uz": "Tropik palma va fikus daraxtlari"},
            "road_markings": {"en": "Monorail overhead guideway pillars, red pedestrian crossings, black license plates with white letters", "ru": "Эстакада монорельса, черные автомобильные номера с белыми буквами", "uz": "Monorels ustunlari, oq harfli qora avtomobil raqamlari"},
            "hint": {"en": "Elevated single-beam monorail, black license plates with white text, left-hand traffic.", "ru": "Монорельс над улицей, черные автомобильные номера и левостороннее движение.", "uz": "Ko'cha ustidagi monorels yo'li, qora davlat raqamlari va chap harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=3.1466,101.7115"
    },
    {
        "id": "sv_id_jakarta_thamrin",
        "country_code": "id",
        "country_name": {"en": "Indonesia", "ru": "Индонезия", "uz": "Indoneziya"},
        "location": {"en": "Jalan M.H. Thamrin & Bundaran HI, Jakarta", "ru": "Джалан Тамрин и Бундаран HI, Джакарта", "uz": "Jalan Thamrin va Bundaran HI, Jakarta"},
        "lat": -6.1934,
        "lng": 106.8236,
        "image_url": "https://images.unsplash.com/photo-1579202673506-ca3ce28943ef?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Tropical royal palms, frangipani, dense tropical foliage", "ru": "Королевские пальмы, франжипани, тропическая зелень", "uz": "Qirollik palmalari va tropik gulzorlar"},
            "road_markings": {"en": "Separated TransJakarta red bus lanes, massive circular fountain roundabout", "ru": "Красные полосы TransJakarta, круговой фонтан с монументом", "uz": "Maxsus TransJakarta qizil yo'laklari, katta aylanma favvora"},
            "hint": {"en": "Massive circular fountain with Welcome Monument, TransJakarta busway, left-hand drive.", "ru": "Огромный круглый фонтан с монументом 'Добро пожаловать' и левостороннее движение.", "uz": "Markaziy aylanma favvora, maxsus avtobus yo'laklari va chap tomonlama harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=-6.1934,106.8236"
    },
    {
        "id": "sv_uz_tashkent_amirtimur",
        "country_code": "uz",
        "country_name": {"en": "Uzbekistan", "ru": "Узбекистан", "uz": "O'zbekiston"},
        "location": {"en": "Amir Timur Square & Hotel Uzbekistan, Tashkent", "ru": "Сквер Амира Темура и гостиница «Узбекистан», Ташкент", "uz": "Amir Temur xiyoboni va 'O'zbekiston' mehmonxonasi, Toshkent"},
        "lat": 41.3111,
        "lng": 69.2797,
        "image_url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Plane trees (chinor), oaks, poplars along central radial avenues", "ru": "Вековые чинары, дубы, тополя вокруг сквера", "uz": "Asriy chinorlar, eman va terak daraxtlari"},
            "road_markings": {"en": "Wide asphalt avenues, white zebra crossings, white Chevrolet cars (Cobalt, Gentra)", "ru": "Широкие проспекты, белая разметка, множество белых автомобилей Chevrolet", "uz": "Keng asfalt ko'chalar, oq chiziqlar va ko'plab oq rangli Chevrolet avtomobillari"},
            "hint": {"en": "Iconic modernist hotel facade with Islamic lattice screen (panjara), white Chevrolet cars.", "ru": "Знаменитая модернистская гостиница с восточной решеткой-панджарой и белые авто Chevrolet.", "uz": "Sharqona panjarali mashhur mehmonxona, chinorlar va oq rangli Chevrolet mashinalari."}
        },
        "maps_url": "https://www.google.com/maps?q=41.3111,69.2797"
    },
    {
        "id": "sv_uz_samarkand_boulevard",
        "country_code": "uz",
        "country_name": {"en": "Uzbekistan", "ru": "Узбекистан", "uz": "O'zbekiston"},
        "location": {"en": "University Boulevard, Samarkand", "ru": "Университетский бульвар, Самарканд", "uz": "Universitet xiyoboni, Samarqand"},
        "lat": 39.6542,
        "lng": 66.9597,
        "image_url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Towering century-old plane trees forming complete shaded canopy", "ru": "Вековые тенистые чинары, образующие зеленый свод", "uz": "Yashil gumbaz hosil qilgan asriy chinor daraxtlari"},
            "road_markings": {"en": "Two parallel roadways separated by wide tree-lined park promenade", "ru": "Две полосы движения, разделенные широким тенистым парком", "uz": "O'rtada keng daraxtzor xiyobon bo'lgan ikki tomonlama yo'l"},
            "hint": {"en": "Grand historic tree-lined boulevard in ancient Silk Road city with massive plane trees.", "ru": "Тенистый университетский бульвар древнего города Шелкового пути с гигантскими чинарами.", "uz": "Ipak yo'lining qadimiy shahridagi ulkan chinorli soyabon xiyobon."}
        },
        "maps_url": "https://www.google.com/maps?q=39.6542,66.9597"
    },
    {
        "id": "sv_kz_astana_nurzhol",
        "country_code": "kz",
        "country_name": {"en": "Kazakhstan", "ru": "Казахстан", "uz": "Qozog'iston"},
        "location": {"en": "Nurzhol Boulevard & Baiterek, Astana", "ru": "Водно-зеленый бульвар Нуржол и Байтерек, Астана", "uz": "Nurjol xiyoboni va Boyterak, Ostona"},
        "lat": 51.1283,
        "lng": 71.4305,
        "image_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Steppe-adapted pines and birches in futuristic landscaped park", "ru": "Степные сосны и березы в футуристическом парке", "uz": "Dasht qarag'aylari va qayinlar bilan bezatilgan futuristik park"},
            "road_markings": {"en": "Multi-lane wide grid avenues, futuristic Kazakh modern architecture", "ru": "Широкие многополосные проспекты, футуристическая архитектура", "uz": "Keng shohko'chalar va zamonaviy osmono'par binolar"},
            "hint": {"en": "Futuristic white observation tower with golden sphere rising over a vast steppe capital.", "ru": "Белая башня с золотым шаром на вершине посреди футуристической столицы в степи.", "uz": "Tepasida oltin shari bo'lgan mashhur oq minora va keng shohko'cha."}
        },
        "maps_url": "https://www.google.com/maps?q=51.1283,71.4305"
    },
    {
        "id": "sv_in_mumbai_marinedrive",
        "country_code": "in",
        "country_name": {"en": "India", "ru": "Индия", "uz": "Hindiston"},
        "location": {"en": "Marine Drive, Mumbai", "ru": "Марин-Драйв, Мумбаи", "uz": "Marine Drive qirg'og'i, Mumbay"},
        "lat": 18.9432,
        "lng": 72.8230,
        "image_url": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Tropical coastal palms along sea promenade", "ru": "Прибрежные пальмы вдоль Аравийского моря", "uz": "Arabiston dengizi sohilidagi palma daraxtlari"},
            "road_markings": {"en": "Concrete tetrapod sea wall defense, yellow-and-black painted curbs, left-hand traffic", "ru": "Бетонные тетраподы у воды, желто-черные бордюры, левостороннее движение", "uz": "To'lqin qaytaruvchi beton tetrapodlar, sariq-qora bordyurlar, chap harakat"},
            "hint": {"en": "Famous C-shaped bay boulevard known as the 'Queen's Necklace', left-side driving, black-and-yellow taxis.", "ru": "Бульвар в форме полумесяца ('Ожерелье королевы'), черно-желтые такси, левостороннее движение.", "uz": "Yarimoysimon mashhur sohil xiyoboni, qora-sariq taksilar va chap harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=18.9432,72.823"
    },
    {
        "id": "sv_tr_istanbul_istiklal",
        "country_code": "tr",
        "country_name": {"en": "Turkey", "ru": "Турция", "uz": "Turkiya"},
        "location": {"en": "İstiklal Avenue & Nostalgic Tram, Istanbul", "ru": "Улица Истикляль и ностальгический трамвай, Стамбул", "uz": "Istiqlol ko'chasi va retro tramvay, Istanbul"},
        "lat": 41.0340,
        "lng": 28.9780,
        "image_url": "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Dense Mediterranean historic urban canyon, hanging decorative flower baskets", "ru": "Плотная городская застройка, османская и европейская архитектура", "uz": "Zich tarixiy Usmoniy va Yevropa uslubidagi binolar"},
            "road_markings": {"en": "Pedestrianized stone cobbles, single vintage red tram track in center", "ru": "Пешеходная каменная мостовая с одной колеей красного трамвая", "uz": "Piyodalar tosh yo'li va markazdan o'tgan bitta qizil retro-tramvay izi"},
            "hint": {"en": "Vibrant pedestrian street with iconic vintage red tram, late Ottoman facades.", "ru": "Оживленная пешеходная улица с красным ретро-трамваем в Стамбуле.", "uz": "Mashhur qizil retro tramvayi va gavjum piyodalar bilan to'la Istanbul ko'chasi."}
        },
        "maps_url": "https://www.google.com/maps?q=41.034,28.978"
    },
    {
        "id": "sv_ae_dubai_sheikhzayed",
        "country_code": "ae",
        "country_name": {"en": "United Arab Emirates", "ru": "ОАЭ", "uz": "BAA"},
        "location": {"en": "Sheikh Zayed Road, Dubai", "ru": "Шоссе шейха Зайда, Дубай", "uz": "Shayx Zayd shohko'chasi, Dubay"},
        "lat": 25.2048,
        "lng": 55.2708,
        "image_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Irrigated date palms, desert petunias along median strips", "ru": "Финиковые пальмы с капельным поливом на фоне пустыни", "uz": "Tomchilatib sug'oriladigan xurmo palmalari va gullar"},
            "road_markings": {"en": "14-lane mega highway, elevated gold Dubai Metro tracks, Salik toll gantries", "ru": "14-полосная магистраль, золотые станции надземного метро Дубая", "uz": "14 qatorli ulkan trassa, tilla rangli metro bekatlari va zamonaviy binolar"},
            "hint": {"en": "Mega multi-lane highway flanked by glittering futuristic supertall skyscrapers and gold metro stations.", "ru": "Многополосный автобан среди футуристических супернебоскребов в Персидском заливе.", "uz": "Osmono'par oynavand binolar orasidan o'tgan ulkan zamonaviy shohko'cha."}
        },
        "maps_url": "https://www.google.com/maps?q=25.2048,55.2708"
    },
    {
        "id": "sv_mn_ulaanbaatar_peace",
        "country_code": "mn",
        "country_name": {"en": "Mongolia", "ru": "Монголия", "uz": "Mo'g'uliston"},
        "location": {"en": "Peace Avenue & Sukhbaatar Square, Ulaanbaatar", "ru": "Проспект Мира и площадь Сухэ-Батора, Улан-Батор", "uz": "Tinchlik xiyoboni va Suxbaatar maydoni, Ulan-Bator"},
        "lat": 47.9188,
        "lng": 106.9176,
        "image_url": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Hardy Siberian larches, steppe grasses, mountainous backdrop", "ru": "Сибирские лиственницы на фоне сопок", "uz": "Sibir tilog'ochi va dasht tepaliklari orqa fonda"},
            "road_markings": {"en": "White lane markings, mix of left-hand and right-hand drive import cars (Prius)", "ru": "Белая разметка, огромное количество гибридов Toyota Prius", "uz": "Oq yo'l chiziqlari va ko'p sonli Toyota Prius avtomobillari"},
            "hint": {"en": "Vast central square with colossal Genghis Khan bronze monument against rolling steppe hills.", "ru": "Гигантская центральная площадь с памятником Чингисхану на фоне степных сопок.", "uz": "Chingizxon haykali joylashgan ulkan maydon va tog' etagidagi shahar."}
        },
        "maps_url": "https://www.google.com/maps?q=47.9188,106.9176"
    },

    # ==================== AFRICA ====================
    {
        "id": "sv_za_capetown_longstreet",
        "country_code": "za",
        "country_name": {"en": "South Africa", "ru": "ЮАР", "uz": "Janubiy Afrika"},
        "location": {"en": "Long Street & Table Mountain, Cape Town", "ru": "Лонг-стрит и Столовая гора, Кейптаун", "uz": "Long Street va Stol tog'i, Keyptaun"},
        "lat": -33.9249,
        "lng": 18.4174,
        "image_url": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Cape fynbos, silver trees, Mediterranean coastal flora", "ru": "Капский финбос, серебряное дерево, средиземноморская растительность", "uz": "Kap florasi, kumush daraxtlar va sohil bo'yi butalari"},
            "road_markings": {"en": "White center lines, Victorian wrought-iron verandas, left-hand traffic", "ru": "Викторианские чугунные балконы, белая разметка, левостороннее движение", "uz": "Viktoriya uslubidagi temir balkonlar, chap tomonlama harakat"},
            "hint": {"en": "Victorian wrought-iron balconies with flat-topped Table Mountain rising in the background, left driving.", "ru": "Викторианские балконы с кованым железом на фоне плоской вершины Столовой горы.", "uz": "Temir balkonli rang-barang binolar, orqa fondagi mashhur Stol tog'i va chap harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=-33.9249,18.4174"
    },
    {
        "id": "sv_ke_nairobi_kenyatta",
        "country_code": "ke",
        "country_name": {"en": "Kenya", "ru": "Кения", "uz": "Keniya"},
        "location": {"en": "Kenyatta Avenue, Nairobi", "ru": "Проспект Кеньятта, Найроби", "uz": "Kenyatta shohko'chasi, Nayrobi"},
        "lat": -1.2864,
        "lng": 36.8172,
        "image_url": "https://images.unsplash.com/photo-1489493887464-892be6d1daae?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Jacaranda trees with violet blossoms, bougainvillea, acacia trees", "ru": "Фиолетовые цветущие жакаранды, акации, бугенвиллея", "uz": "Binafsharang gullaydigan jakaranda va akatsiya daraxtlari"},
            "road_markings": {"en": "White lane markings, colorful customized Matatu minibuses, left-hand drive", "ru": "Ярко расписанные маршрутки 'матату', левостороннее движение", "uz": "Rang-barang bezatilgan 'Matatu' mikroavtobuslari va chap harakat"},
            "hint": {"en": "Left-hand traffic, colorful customized Matatu buses, jacaranda trees in East Africa.", "ru": "Левостороннее движение, красочные маршрутки матату и цветущие деревья в Восточной Африке.", "uz": "Sharqiy Afrikadagi chap tomonlama harakat va bezatilgan Matatu mikroavtobuslari."}
        },
        "maps_url": "https://www.google.com/maps?q=-1.2864,36.8172"
    },
    {
        "id": "sv_eg_cairo_tahrir",
        "country_code": "eg",
        "country_name": {"en": "Egypt", "ru": "Египет", "uz": "Misr"},
        "location": {"en": "Tahrir Square & Egyptian Museum, Cairo", "ru": "Площадь Тахрир и Египетский музей, Каир", "uz": "Tahrir maydoni va Qohira muzeyi, Qohira"},
        "lat": 30.0444,
        "lng": 31.2357,
        "image_url": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Date palms, ficus, arid Nile desert atmosphere", "ru": "Финиковые пальмы, фикусы вдоль набережной Нила", "uz": "Nil bo'yidagi xurmo palmalari va fikus daraxtlari"},
            "road_markings": {"en": "Roundabout with ancient pharaonic obelisk, white and black taxi cabs", "ru": "Круговая развязка с древнеегипетским обелиском, белые такси", "uz": "Qadimgi fir'avn obeliski o'rnatilgan aylanma maydon, oq taksilar"},
            "hint": {"en": "Huge roundabout with genuine ancient obelisk in front of dusty pink Egyptian museum.", "ru": "Огромная площадь с древним обелиском перед розовым Египетским музеем.", "uz": "Qadimgi Misr obeliski va pushti rangli tarixiy muzey joylashgan mashhur maydon."}
        },
        "maps_url": "https://www.google.com/maps?q=30.0444,31.2357"
    },
    {
        "id": "sv_ma_casablanca_mohammed5",
        "country_code": "ma",
        "country_name": {"en": "Morocco", "ru": "Марокко", "uz": "Marokash"},
        "location": {"en": "Boulevard Mohammed V & Tramway, Casablanca", "ru": "Бульвар Мохаммеда V, Касабланка", "uz": "Muhammad V bulvari va tramvay, Kasablanka"},
        "lat": 33.5951,
        "lng": -7.6186,
        "image_url": "https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Tall date palms, Mediterranean ficus, Moorish courtyard gardens", "ru": "Высокие финиковые пальмы, мавританские мотивы", "uz": "Baland xurmo palmalari va mag'ribiy me'morchilik"},
            "road_markings": {"en": "Sleek modern red tram tracks, Art Deco mixed with Moorish white architecture", "ru": "Современные трамвайные пути, белые здания в стиле ар-деко и неомавританском стиле", "uz": "Zamonaviy tramvay yo'li, oq rangli art-deko va sharqona binolar"},
            "hint": {"en": "Modern tram line flanked by whitewashed Art Deco and Neo-Moorish architecture, Arabic signs.", "ru": "Трамвайная линия среди белых зданий в марокканском стиле с арабскими вывесками.", "uz": "Oq rangli mag'ribiy binolar orasidan o'tgan zamonaviy tramvay yo'li va arabcha yozuvlar."}
        },
        "maps_url": "https://www.google.com/maps?q=33.5951,-7.6186"
    },
    {
        "id": "sv_ng_lagos_broadstreet",
        "country_code": "ng",
        "country_name": {"en": "Nigeria", "ru": "Нигерия", "uz": "Nigeriya"},
        "location": {"en": "Broad Street & Marina, Lagos Island", "ru": "Брод-стрит и Марина, Лагос", "uz": "Brod-strit va Marina, Lagos oroli"},
        "lat": 6.4531,
        "lng": 3.3958,
        "image_url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Tropical humid rainforest palms, mangrove coastlines", "ru": "Тропические пальмы влажного гвинейского побережья", "uz": "Gvineya qo'ltig'i bo'yidagi tropik o'simliklar"},
            "road_markings": {"en": "Yellow Danfo commercial minibuses with black stripes, right-hand drive", "ru": "Желтые микроавтобусы 'данфо' с черными полосами, оживленное движение", "uz": "Qora chiziqli sariq 'Danfo' mikroavtobuslari, gavjum harakat"},
            "hint": {"en": "Distinctive yellow commercial Danfo minibuses with black stripes in West Africa's largest metropolis.", "ru": "Желтые микроавтобусы данфо с двумя черными полосами в крупнейшем городе Западной Африки.", "uz": "Qora chiziqli sariq Danfo mikroavtobuslari bilan mashhur G'arbiy Afrika megapolisi."}
        },
        "maps_url": "https://www.google.com/maps?q=6.4531,3.3958"
    },
    {
        "id": "sv_sn_dakar_corniche",
        "country_code": "sn",
        "country_name": {"en": "Senegal", "ru": "Сенегал", "uz": "Senegal"},
        "location": {"en": "Corniche Ouest & African Renaissance Monument, Dakar", "ru": "Корниш-Уэст и Монумент африканского возрождения, Дакар", "uz": "Corniche Ouest va Afrika uyg'onishi monumenti, Dakar"},
        "lat": 14.6928,
        "lng": -17.4467,
        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "right",
        "clues": {
            "driving_side": {"en": "Right", "ru": "Правостороннее", "uz": "O'ng"},
            "vegetation": {"en": "Sahelian acacia, coastal baobabs, palms along Atlantic beaches", "ru": "Сахельские акации, баобабы, пальмы у океана", "uz": "Sahel akatsiyalari, baobablar va sohil bo'yi palmalari"},
            "road_markings": {"en": "Yellow-and-black painted Car Rapide minibuses, coastal highway curves", "ru": "Красочные микроавтобусы 'кар рапид', шоссе вдоль Атлантики", "uz": "Rangli 'Car Rapide' avtobuslari, Atlantika sohili bo'ylab trassa"},
            "hint": {"en": "Colossal bronze African Renaissance statue overlooking the westernmost tip of Africa.", "ru": "Колоссальный бронзовый монумент на холме над Атлантическим океаном.", "uz": "Afrikaning eng g'arbiy nuqtasidagi baland tepalikda qad rostlagan ulkan bronza monument."}
        },
        "maps_url": "https://www.google.com/maps?q=14.6928,-17.4467"
    },

    # ==================== OCEANIA ====================
    {
        "id": "sv_au_sydney_georgest",
        "country_code": "au",
        "country_name": {"en": "Australia", "ru": "Австралия", "uz": "Avstraliya"},
        "location": {"en": "George Street & Sydney Town Hall, Sydney", "ru": "Джордж-стрит и ратуша Сиднея, Сидней", "uz": "Jorj-strit va shahar ratushasi, Sidney"},
        "lat": -33.8732,
        "lng": 151.2069,
        "image_url": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Eucalyptus gums, Moreton Bay fig trees, London planes in urban pedestrian zones", "ru": "Эвкалипты, фикусы залива Мортон на фоне викторианской архитектуры", "uz": "Evkalipt va yirik sohil fikuslari"},
            "road_markings": {"en": "Pedestrianized light rail corridor, red tram lane markings, left-hand drive", "ru": "Пешеходная зона со скоростным трамваем, левостороннее движение", "uz": "Piyodalar va tramvay yo'lagi, chap tomonlama harakat"},
            "hint": {"en": "Sleek red light rail trams sliding past Victorian sandstone architecture, left-side driving.", "ru": "Красные современные трамваи среди викторианских зданий из песчаника, левостороннее движение.", "uz": "Qizil zamonaviy tramvaylar, Viktoriya davri tosh binolari va chap harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=-33.8732,151.2069"
    },
    {
        "id": "sv_au_great_ocean_road",
        "country_code": "au",
        "country_name": {"en": "Australia", "ru": "Австралия", "uz": "Avstraliya"},
        "location": {"en": "Great Ocean Road near Twelve Apostles, Victoria", "ru": "Великая океанская дорога у Двенадцати апостолов, Виктория", "uz": "Buyuk okean yo'li, 12 havoriy qoyalari yaqinida, Viktoriya"},
        "lat": -38.6806,
        "lng": 143.3917,
        "image_url": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Coastal heathland, eucalyptus scrub, tea tree shrubs", "ru": "Прибрежные эвкалиптовые заросли, чайные деревья", "uz": "Evkalipt butalari va sohil bo'yi choy daraxtlari"},
            "road_markings": {"en": "White dashed centerline, yellow guideposts with reflectors, left-hand driving", "ru": "Белая пунктирная разметка, желтые столбики-катафоты, левостороннее движение", "uz": "Oq o'q chizig'i, reflektorli sariq yo'l ustunchalari, chap harakat"},
            "hint": {"en": "World-famous coastal cliff highway winding past dramatic limestone stacks in the Southern Ocean.", "ru": "Живописная океанская дорога вдоль известняковых скал в Южном океане, движение слева.", "uz": "Janubiy okeandagi ulkan ohaktosh qoyalar bo'ylab ketgan mashhur sohil yo'li, chap harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=-38.6806,143.3917"
    },
    {
        "id": "sv_nz_auckland_queenst",
        "country_code": "nz",
        "country_name": {"en": "New Zealand", "ru": "Новая Зеландия", "uz": "Yangi Zelandiya"},
        "location": {"en": "Queen Street & Sky Tower, Auckland", "ru": "Куин-стрит и Скай-Тауэр, Окленд", "uz": "Queen Street va Sky Tower, Oklend"},
        "lat": -36.8485,
        "lng": 174.7633,
        "image_url": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?auto=format&fit=crop&w=1200&q=80",
        "driving_side": "left",
        "clues": {
            "driving_side": {"en": "Left", "ru": "Левостороннее", "uz": "Chap"},
            "vegetation": {"en": "Pohutukawa trees (New Zealand Christmas trees), subtropical nikau palms", "ru": "Деревья похутукава, пальмы никау", "uz": "Poxutukava daraxtlari va nikau palmalari"},
            "road_markings": {"en": "White painted lane markings, red bus lanes, green pedestrian cycle boxes, left-hand drive", "ru": "Белая разметка, красные полосы для автобусов, левостороннее движение", "uz": "Oq chiziqlar, qizil avtobus yo'laklari, chap tomonlama harakat"},
            "hint": {"en": "Prominent 328-meter needle Sky Tower overlooking a hilly harbor city with left-hand traffic.", "ru": "328-метровая игла телебашни Скай-Тауэр над портовым городом, левостороннее движение.", "uz": "328 metrlik ninasimon Sky Tower minorasi va chap tomonlama harakat."}
        },
        "maps_url": "https://www.google.com/maps?q=-36.8485,174.7633"
    }
]

def get_streetview(sv_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a street view entry by its unique identifier."""
    for sv in STREETVIEWS:
        if sv["id"] == sv_id:
            return sv
    return None

def get_random_streetview(exclude_codes: Optional[Set[str]] = None) -> Dict[str, Any]:
    """Retrieve a random street view, optionally excluding already visited country codes."""
    if exclude_codes:
        pool = [sv for sv in STREETVIEWS if sv["country_code"] not in exclude_codes]
        if pool:
            return random.choice(pool)
    return random.choice(STREETVIEWS)
