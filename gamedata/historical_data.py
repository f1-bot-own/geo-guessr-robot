# -*- coding: utf-8 -*-
"""
GeoGuru Game Dataset: Historical Figures Database.
Contains 111 world-famous historical figures, thinkers, scholars, monarchs, conquerors, and scientists.
Features extensive coverage of Central Asian thinkers (Amir Temur, Alisher Navoiy, Ibn Sino, Mirzo Ulug'bek, Beruniy, Al-Xorazmiy, Bobur, Jaloliddin Manguberdi)
and global icons (Alexander, Caesar, Napoleon, Einstein, Newton, Da Vinci, Socrates, Aristotle, Genghis Khan, Confucius, Lincoln, Churchill, Gandhi, and more).
"""
import random

HISTORICAL_FIGURES = [
    {
        "id": "amir_temur",
        "name": {
            "uz": "Amir Temur",
            "ru": "Амир Темур (Тамерлан)",
            "en": "Amir Timur (Tamerlane)"
        },
        "era": {
            "uz": "XIV–XV asrlar (O'rta asrlar)",
            "ru": "XIV–XV века (Средневековье)",
            "en": "14th–15th century (Middle Ages)"
        },
        "field": {
            "uz": "Davlat arbobi, buyuk sarkarda, Temuriylar saltanati asoschisi",
            "ru": "Полководец, основатель империи Тимуридов",
            "en": "Conqueror, military commander, founder of Timurid Empire"
        },
        "country": {
            "uz": "Temuriylar davlati / O'zbekiston",
            "ru": "Империя Тимуридов / Узбекистан",
            "en": "Timurid Empire / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Timur_reconstruction03.jpg/640px-Timur_reconstruction03.jpg",
        "aliases": [
            "amir temur",
            "temur",
            "tamerlan",
            "tamerlane",
            "амир темур",
            "темур",
            "тамерлан",
            "sohibqiron"
        ],
        "fun_fact": {
            "uz": "Hayoti davomida biror marta ham jangda mag'lub bo'lmagan buyuk sarkarda bo'lib, Samarqandni jahonning eng go'zal poytaxtiga aylantirgan.",
            "ru": "Великий полководец, не проигравший ни одного сражения, превратил Самарканд в столицу науки и архитектуры.",
            "en": "Undefeated military genius whose vast empire stretched from India to the Mediterranean; made Samarkand a gem of Islamic architecture."
        }
    },
    {
        "id": "alisher_navoiy",
        "name": {
            "uz": "Alisher Navoiy",
            "ru": "Алишер Навои",
            "en": "Alisher Navoiy (Ali-Shir Nava'i)"
        },
        "era": {
            "uz": "XV asr (Temuriylar uyg'onish davri)",
            "ru": "XV век (Темуридский ренессанс)",
            "en": "15th century (Timurid Renaissance)"
        },
        "field": {
            "uz": "Buyuk shoir, mutafakkir, davlat arbobi, o'zbek adabiy tili asoschisi",
            "ru": "Поэт, мыслитель, основоположник узбекской классической литературы",
            "en": "Poet, thinker, statesman, founder of Uzbek classical literature"
        },
        "country": {
            "uz": "Temuriylar davlati / O'zbekiston",
            "ru": "Империя Тимуридов / Узбекистан",
            "en": "Timurid Empire / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Mystics_in_a_garden.jpg/640px-Mystics_in_a_garden.jpg",
        "aliases": [
            "alisher navoiy",
            "navoiy",
            "алишер навои",
            "навои",
            "nizomiddin mir alisher",
            "nava'i",
            "ali-shir navai"
        ],
        "fun_fact": {
            "uz": "Turkiy tilda birinchi bo'lib mashhur 'Xamsa' (besh doston) asarini yozgan va turkiy tilning boyligini dunyoga isbotlagan.",
            "ru": "Первым создал великую «Пятерицу» (Хамсу) на тюркском языке, доказав его исключительное поэтическое богатство.",
            "en": "Composed the monumental Khamsa (Quintet) in Turkic, proving Turkic equal in literary stature to Persian."
        }
    },
    {
        "id": "mirzo_ulugbek",
        "name": {
            "uz": "Mirzo Ulug'bek",
            "ru": "Мирзо Улугбек",
            "en": "Mirzo Ulugh Beg"
        },
        "era": {
            "uz": "XV asr (Temuriylar davri)",
            "ru": "XV век",
            "en": "15th century"
        },
        "field": {
            "uz": "Buyuk astronom, matematik olim, Temuriy hukmdor",
            "ru": "Астроном, математик, правитель Самарканда",
            "en": "Astronomer, mathematician, ruler of Samarkand"
        },
        "country": {
            "uz": "Temuriylar davlati / O'zbekiston",
            "ru": "Империя Тимуридов / Узбекистан",
            "en": "Timurid Empire / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Ulugh_Beg%2C_Timurid_painting_1425-50.jpg/640px-Ulugh_Beg%2C_Timurid_painting_1425-50.jpg",
        "aliases": [
            "mirzo ulug'bek",
            "ulug'bek",
            "ulugbek",
            "улугбек",
            "мирзо улугбек",
            "muhammad tarag'ay"
        ],
        "fun_fact": {
            "uz": "Samarqandda ulkan rasadxona qurib, teleskopsiz 1018 ta yulduz koordinatalarini o'ta yuqori aniqlikda o'lchagan ('Ziji Ko'ragoniy').",
            "ru": "Построил обсерваторию в Самарканде и составил звездный каталог из 1018 звезд с поразительной точностью без телескопа.",
            "en": "Built a landmark observatory in Samarkand, cataloging 1,018 stars with astounding accuracy centuries before modern telescopes."
        }
    },
    {
        "id": "ibn_sino",
        "name": {
            "uz": "Abu Ali ibn Sino (Avitsenna)",
            "ru": "Абу Али ибн Сина (Авиценна)",
            "en": "Avicenna (Ibn Sina)"
        },
        "era": {
            "uz": "X–XI asrlar (Sharq uyg'onish davri)",
            "ru": "X–XI века (Золотой век ислама)",
            "en": "10th–11th century (Islamic Golden Age)"
        },
        "field": {
            "uz": "Tibbiyot va falsafa dahosi, 'Tibbiyot qonunlari' muallifi",
            "ru": "Врач, философ, автор «Канона врачебной науки»",
            "en": "Physician, polymath, philosopher, author of The Canon of Medicine"
        },
        "country": {
            "uz": "Somoniylar / Buxoro / O'zbekiston",
            "ru": "Государство Саманидов / Бухара",
            "en": "Samanid Empire / Bukhara"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Avicenna_Bust%2C_left_profile_%28cropped%29.jpg/640px-Avicenna_Bust%2C_left_profile_%28cropped%29.jpg",
        "aliases": [
            "ibn sino",
            "avitsenna",
            "avicenna",
            "abu ali ibn sino",
            "ибн сина",
            "авиценна"
        ],
        "fun_fact": {
            "uz": "Uning 'Tib qonunlari' asari 500 yildan ortiq vaqt davomida Yevropa universitetlarida asosiy tibbiyot darsligi bo'lib xizmat qilgan.",
            "ru": "Его фундаментальный труд «Канон врачебной науки» был главным медицинским учебником в университетах Европы свыше 500 лет.",
            "en": "His 14-volume medical encyclopedia 'The Canon of Medicine' was Europe's standard medical textbook for more than 500 years."
        }
    },
    {
        "id": "al_xorazmiy",
        "name": {
            "uz": "Muhammad al-Xorazmiy",
            "ru": "Мухаммад аль-Хорезми",
            "en": "Muhammad ibn Musa al-Khwarizmi"
        },
        "era": {
            "uz": "VIII–IX asrlar (Islom oltin davri)",
            "ru": "VIII–IX века",
            "en": "8th–9th century"
        },
        "field": {
            "uz": "Algebra va algoritm asoschisi, buyuk matematik va astronom",
            "ru": "Основоположник алгебры и алгоритмов, математик и географ",
            "en": "Father of algebra, creator of algorithms, mathematician"
        },
        "country": {
            "uz": "Xorazm / Abbosiylar / O'zbekiston",
            "ru": "Хорезм / Халифат Аббасидов",
            "en": "Khwarazm / Abbasid Caliphate"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Madrid_-_Ciudad_Universitaria%2C_Monumento_a_Muhammad_al-Juarismi_%28cropped%29.jpg/640px-Madrid_-_Ciudad_Universitaria%2C_Monumento_a_Muhammad_al-Juarismi_%28cropped%29.jpg",
        "aliases": [
            "al-xorazmiy",
            "xorazmiy",
            "al-khwarizmi",
            "khwarizmi",
            "аль-хорезми",
            "хорезми",
            "algoritmi"
        ],
        "fun_fact": {
            "uz": "Zamonaviy 'Algebra' so'zi uning 'Al-Jabr' kitobidan, 'Algoritm' tushunchasi esa olimning ismi (Al-Xorazmiy)dan kelib chiqqan.",
            "ru": "От названия его книги «Аль-джабр» произошло слово «алгебра», а от латинизации его имени — понятие «алгоритм».",
            "en": "The terms 'Algebra' (from his book Al-Jabr) and 'Algorithm' (from the Latin transliteration of his name) honor his foundational discoveries."
        }
    },
    {
        "id": "beruniy",
        "name": {
            "uz": "Abu Rayhon Beruniy",
            "ru": "Абу Райхан Беруни",
            "en": "Abu Rayhan al-Biruni"
        },
        "era": {
            "uz": "X–XI asrlar",
            "ru": "X–XI века",
            "en": "10th–11th century"
        },
        "field": {
            "uz": "Qomusiy olim, Yer radiusini o'lchagan astronom, geolog va antropolog",
            "ru": "Ученый-энциклопедист, астроном, вычислил радиус Земли",
            "en": "Universal polymath, measured Earth's radius, astronomer and geodesist"
        },
        "country": {
            "uz": "Xorazm / G'aznaviylar / O'zbekiston",
            "ru": "Хорезм / Газневидское государство",
            "en": "Khwarazm / Ghaznavid Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Biruni-russian.jpg/640px-Biruni-russian.jpg",
        "aliases": [
            "beruniy",
            "abu rayhon beruniy",
            "al-biruni",
            "biruni",
            "беруни",
            "абу райхан беруни"
        ],
        "fun_fact": {
            "uz": "Kolumbdan 500 yil oldin Tinch okeani ortida noma'lum qit'a (Amerika) mavjudligini ilmiy asoslab bergan va Yer radiusini 99% aniqlikda hisoblagan.",
            "ru": "За 500 лет до Колумба предсказал существование Америки и вычислил радиус Земли с точностью до 99% от современных данных.",
            "en": "Calculated the radius of the Earth with 99% precision and theorized the existence of the American continent five centuries before Columbus."
        }
    },
    {
        "id": "bobur",
        "name": {
            "uz": "Zahiriddin Muhammad Bobur",
            "ru": "Захириддин Мухаммад Бабур",
            "en": "Zahir al-Din Muhammad Babur"
        },
        "era": {
            "uz": "XV–XVI asrlar",
            "ru": "XV–XVI века",
            "en": "15th–16th century"
        },
        "field": {
            "uz": "Boburiylar sulolasi asoschisi, sarkarda, 'Boburnoma' muallifi, shoir",
            "ru": "Основатель империи Великих Моголов в Индии, поэт и автор «Бабур-наме»",
            "en": "Founder of the Mughal Empire in India, author of Baburnama, poet"
        },
        "country": {
            "uz": "Farg'ona / Boburiylar saltanati / O'zbekiston",
            "ru": "Империя Великих Моголов / Узбекистан",
            "en": "Mughal Empire / Fergana / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Humayun_and_Babur_%28Late_Shah_Jahan_Album%29_Babur_detail.jpg/640px-Humayun_and_Babur_%28Late_Shah_Jahan_Album%29_Babur_detail.jpg",
        "aliases": [
            "bobur",
            "zahiriddin muhammad bobur",
            "babur",
            "бабур",
            "захириддин бабур"
        ],
        "fun_fact": {
            "uz": "Hindistonda 300 yildan ortiq hukmronlik qilgan qudratli Boburiylar saltanatiga asos solgan va jahon adabiyoti durdonasi 'Boburnoma'ni yozgan.",
            "ru": "Основал империю Великих Моголов, правившую Индией более трех веков, и написал мемуары мирового значения «Бабур-наме».",
            "en": "Descendant of Timur and Genghis Khan who founded the Mughal Empire in India and wrote the autobiography Baburnama."
        }
    },
    {
        "id": "jaloliddin_manguberdi",
        "name": {
            "uz": "Jaloliddin Manguberdi",
            "ru": "Джалаладдин Мангуберди",
            "en": "Jalal al-Din Mangburni"
        },
        "era": {
            "uz": "XIII asr",
            "ru": "XIII век",
            "en": "13th century"
        },
        "field": {
            "uz": "Xorazmshoh, Chingizxonga qarshi mardonavor kurashgan milliy qahramon",
            "ru": "Последний хорезмшах, национальный герой, сражавшийся с Чингисханом",
            "en": "Last Khwarazmshah, legendary hero who resisted Genghis Khan"
        },
        "country": {
            "uz": "Xorazmshohlar davlati / O'zbekiston",
            "ru": "Государство Хорезмшахов / Узбекистан",
            "en": "Khwarazmian Empire / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/OUZBEKISTAN%2C_25_Som_%C3%A0_l%27effigie_de_Jaloliddin_Manguberdi_%28portrait%29.jpg/640px-OUZBEKISTAN%2C_25_Som_%C3%A0_l%27effigie_de_Jaloliddin_Manguberdi_%28portrait%29.jpg",
        "aliases": [
            "jaloliddin manguberdi",
            "manguberdi",
            "джалаладдин мангуберди",
            "мангуберди",
            "jalal ad-din"
        ],
        "fun_fact": {
            "uz": "Sind daryosi jangida o'z oti bilan baland qoyadan daryoga sakrab dushmandan qutulgan; hatto Chingizxon uning jasoratiga qoyil qolgan.",
            "ru": "Поразил Чингисхана своим бесстрашием в битве на реке Инд, бросившись на коне с отвесной скалы в бурные воды.",
            "en": "Famed for leaping on horseback off a cliff into the raging Indus River under fire, prompting Genghis Khan to praise his unmatched bravery."
        }
    },
    {
        "id": "imom_buxoriy",
        "name": {
            "uz": "Imom al-Buxoriy",
            "ru": "Имам аль-Бухари",
            "en": "Imam al-Bukhari"
        },
        "era": {
            "uz": "IX asr",
            "ru": "IX век",
            "en": "9th century"
        },
        "field": {
            "uz": "Hadis ilmining buyuk sultoni, 'Sahihul Buxoriy' muallifi",
            "ru": "Великий исламский богослов, составитель «Сахих аль-Бухари»",
            "en": "Foremost Islamic hadith scholar, compiler of Sahih al-Bukhari"
        },
        "country": {
            "uz": "Buxoro / Abbosiylar / O'zbekiston",
            "ru": "Бухара / Арабский халифат",
            "en": "Bukhara / Abbasid Caliphate"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Imam_al-Bukhari_center.jpg/640px-Imam_al-Bukhari_center.jpg",
        "aliases": [
            "imom al-buxoriy",
            "imom buxoriy",
            "al-bukhari",
            "buxoriy",
            "имам аль-бухари",
            "бухари"
        ],
        "fun_fact": {
            "uz": "600 mingdan ortiq hadisni yoddan bilgan va islom olamida Qur'ondan keyingi eng ishonchli manba hisoblangan 'Sahih' to'plamini tuzgan.",
            "ru": "Знал наизусть свыше 600 тысяч хадисов, его сборник признан мусульманским миром второй по значимости книгой после Корана.",
            "en": "Memorized over 600,000 hadiths and authored Sahih al-Bukhari, universally regarded by Sunnis as the most authentic hadith compilation."
        }
    },
    {
        "id": "imom_termiziy",
        "name": {
            "uz": "Imom at-Termiziy",
            "ru": "Имам ат-Тирмизи",
            "en": "Imam al-Tirmidhi"
        },
        "era": {
            "uz": "IX asr",
            "ru": "IX век",
            "en": "9th century"
        },
        "field": {
            "uz": "Yirik muhaddis, 'Sunani Termiziy' va 'Shamoili Muhammadiyya' muallifi",
            "ru": "Выдающийся хадисовед, автор «Сунан ат-Тирмизи»",
            "en": "Master hadith scholar, author of Jami al-Tirmidhi and Shama'il"
        },
        "country": {
            "uz": "Termiz / Abbosiylar / O'zbekiston",
            "ru": "Термез / Арабский халифат",
            "en": "Termez / Abbasid Caliphate"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Grave_of_Isa_al-Tirmidhi_inside_his_Tomb.jpg/640px-Grave_of_Isa_al-Tirmidhi_inside_his_Tomb.jpg",
        "aliases": [
            "imom termiziy",
            "at-termiziy",
            "termiziy",
            "tirmidhi",
            "ат-тирмизи",
            "тирмизи"
        ],
        "fun_fact": {
            "uz": "Payg'ambar Muhammad (s.a.v.)ning shaxsiyati va hayot tarziga bag'ishlangan 'Shamoili Muhammadiyya' bebaho asari bilan butun olamga tanilgan.",
            "ru": "Автор классического труда «Аш-Шамаиль аль-Мухаммадийя», подробно описывающего облик и характер пророка Мухаммада.",
            "en": "Author of the definitive 'Shama'il Muhammadiyyah', documenting the detailed physical description and character of Prophet Muhammad."
        }
    },
    {
        "id": "ahmad_fargoniy",
        "name": {
            "uz": "Ahmad al-Farg'oniy (Alfraganus)",
            "ru": "Ахмад аль-Фаргани (Альфраганус)",
            "en": "Alfraganus (Ahmad al-Farghani)"
        },
        "era": {
            "uz": "IX asr",
            "ru": "IX век",
            "en": "9th century"
        },
        "field": {
            "uz": "Astronom, matematik, Nilometr gidrotexnik inshootini yaratgan olim",
            "ru": "Астроном, математик, создатель Ниломера в Каире",
            "en": "Astronomer, mathematician, inventor of the Cairo Nilometer"
        },
        "country": {
            "uz": "Farg'ona / Abbosiylar / O'zbekiston",
            "ru": "Фергана / Халифат Аббасидов",
            "en": "Fergana / Abbasid Caliphate"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b7/CairoRodaAlfraganusMonument.jpg",
        "aliases": [
            "ahmad fargoniy",
            "al-fargoniy",
            "alfraganus",
            "аль-фаргани",
            "фаргани",
            "alfragan"
        ],
        "fun_fact": {
            "uz": "Qohirada Nil daryosi suv sathini o'lchovchi mashhur 'Nilometr' inshootini qurgan va Oydagi kraterlardan biriga uning nomi berilgan.",
            "ru": "Построил в Каире знаменитый Ниломер для прогнозирования паводков Нила, в его честь назван кратер на Луне.",
            "en": "Engineered the Nilometer on Rawda Island in Cairo to measure Nile floods; a lunar crater bears his Latinized name Alfraganus."
        }
    },
    {
        "id": "abu_nasr_forobiy",
        "name": {
            "uz": "Abu Nasr Forobiy (Alpharabius)",
            "ru": "Абу Наср аль-Фараби (Альфарабиус)",
            "en": "Al-Farabi (Alpharabius)"
        },
        "era": {
            "uz": "IX–X asrlar",
            "ru": "IX–X века",
            "en": "9th–10th century"
        },
        "field": {
            "uz": "'Ikkinchi muallim' (Aristoteldan keyin), faylasuf, musiqashunos olim",
            "ru": "«Второй учитель» после Аристотеля, философ, теоретик музыки",
            "en": "'Second Master' after Aristotle, philosopher, musical theorist"
        },
        "country": {
            "uz": "O'tror / Abbosiylar / Markaziy Osiyo",
            "ru": "Отрар / Арабский халифат",
            "en": "Otrar / Abbasid Caliphate"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Alpharabius_in_Liber_Chronicarum_1493_AD.png/640px-Alpharabius_in_Liber_Chronicarum_1493_AD.png",
        "aliases": [
            "forobiy",
            "al-farabi",
            "farabi",
            "аль-фараби",
            "фараби",
            "abu nasr forobiy",
            "muallim soniy"
        ],
        "fun_fact": {
            "uz": "Sharqda Aristoteldan keyin 'Muallimi soniy' (Ikkinchi muallim) deb e'tirof etilgan va 'Katta musiqa kitobi'ni yozgan.",
            "ru": "Удостоился почетного звания «Второй учитель» (после Аристотеля), написал фундаментальную «Большую книгу о музыке».",
            "en": "Known as the 'Second Teacher' (after Aristotle), he preserved Greek logic in Arabic and wrote the seminal 'Great Book of Music'."
        }
    },
    {
        "id": "mahmud_zamaxshariy",
        "name": {
            "uz": "Mahmud az-Zamaxshariy",
            "ru": "Махмуд аз-Замахшари",
            "en": "Mahmud al-Zamakhshari"
        },
        "era": {
            "uz": "XI–XII asrlar",
            "ru": "XI–XII века",
            "en": "11th–12th century"
        },
        "field": {
            "uz": "Arab tili va adabiyotining buyuk bilimdoni, 'Al-Kashshof' tafsiri muallifi",
            "ru": "Выдающийся филолог, теолог, автор тафсира «Аль-Кашшаф»",
            "en": "Foremost linguist of Arabic, theologian, author of Al-Kashshaf"
        },
        "country": {
            "uz": "Xorazm / O'zbekiston",
            "ru": "Хорезм / Государство Сельджуков",
            "en": "Khwarazm / Seljuk Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Abu%27l_Qasim_Mahmud_ibn_%27Umar_al-Zamakhshri_%28d.1144%29%3B_Al-Mufassal%2C_Near_East%2C_Wednesday_13_August_1253.jpg/640px-Abu%27l_Qasim_Mahmud_ibn_%27Umar_al-Zamakhshri_%28d.1144%29%3B_Al-Mufassal%2C_Near_East%2C_Wednesday_13_August_1253.jpg",
        "aliases": [
            "zamaxshariy",
            "al-zamakhshari",
            "замахшари",
            "аз-замахшари",
            "jorulloh"
        ],
        "fun_fact": {
            "uz": "Arab bo'lmasa-da, arab tili grammatikasini shu qadar chuqur tadqiq qilganki, arablar uni 'Jorulloh' (Allohning qo'shnisi) deb hurmat qilishgan.",
            "ru": "Будучи хорезмийцем, создал непревзойденный грамматический труд арабского языка и получил титул «Сосед Аллаха» в Мекке.",
            "en": "A Persian/Khwarazmian scholar whose mastery of Arabic linguistics was so respected in Mecca that he was dubbed 'Jar Allah' (God's Neighbor)."
        }
    },
    {
        "id": "bahouddin_naqshband",
        "name": {
            "uz": "Bahouddin Naqshband",
            "ru": "Бахауддин Накшбанд",
            "en": "Baha-ud-Din Naqshband"
        },
        "era": {
            "uz": "XIV asr",
            "ru": "XIV век",
            "en": "14th century"
        },
        "field": {
            "uz": "Naqshbandiya tasavvuf tariqati asoschisi, buyuk mutasavvif",
            "ru": "Основатель суфийского ордена Накшбандия, духовный наставник",
            "en": "Founder of the Naqshbandi Sufi order, spiritual master"
        },
        "country": {
            "uz": "Buxoro / O'zbekiston",
            "ru": "Бухара / Империя Тимуридов",
            "en": "Bukhara / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Painting_of_Hazrat_Shah_Bahauddin%2C_from_a_manuscript_in_the_collection_of_Rampur_Raza_Library_%28cropped%29.jpg/640px-Painting_of_Hazrat_Shah_Bahauddin%2C_from_a_manuscript_in_the_collection_of_Rampur_Raza_Library_%28cropped%29.jpg",
        "aliases": [
            "bahouddin naqshband",
            "naqshband",
            "накшбанд",
            "бахауддин накшбанд",
            "xojai buzruk"
        ],
        "fun_fact": {
            "uz": "'Dil ba yoru, dast ba kor' (Ko'ngling Allohda, qo'ling mehnatda bo'lsin) degan mashhur hayotiy tamoyilni ilgari surgan.",
            "ru": "Сформулировал мудрое жизненное правило: «Сердце с Богом, рука в труде» (Дил ба ёру, даст ба кор).",
            "en": "Founded the world's most widespread Sufi tariqa and championed the principle 'Heart with God, hands at work'."
        }
    },
    {
        "id": "nodirabegim",
        "name": {
            "uz": "Nodirabegim (Mohlaroyim)",
            "ru": "Надира (Мохлароим)",
            "en": "Nodira (Mohlaroyim)"
        },
        "era": {
            "uz": "XVIII–XIX asrlar",
            "ru": "XVIII–XIX века",
            "en": "18th–19th century"
        },
        "field": {
            "uz": "Klassik o'zbek shoirasi, davlat va madaniyat arbobi",
            "ru": "Классическая узбекская поэтесса, правительница Кокандского ханства",
            "en": "Classical Uzbek poet, stateswoman of Kokand Khanate"
        },
        "country": {
            "uz": "Qo'qon xonligi / O'zbekiston",
            "ru": "Кокандское ханство / Узбекистан",
            "en": "Kokand Khanate / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Painting_of_Heroine_Nodira_by_Shamsroi_Khasanova.jpg/640px-Painting_of_Heroine_Nodira_by_Shamsroi_Khasanova.jpg",
        "aliases": [
            "nodirabegim",
            "nodira",
            "надира",
            "мохлароим",
            "mohlaroyim",
            "komila"
        ],
        "fun_fact": {
            "uz": "Umarxon vafotidan so'ng o'g'li voyaga yetguncha Qo'qon xonligini boshqargan va ko'plab madrasa, kutubxonalar qurdirgan.",
            "ru": "Фактически правила Кокандским ханством после смерти мужа Умархана, покровительствовала науке, искусству и поэзии.",
            "en": "Served as regent of the Kokand Khanate, patronized literature, and authored poignant romantic divans under the pen name Nodira."
        }
    },
    {
        "id": "uvaysiy",
        "name": {
            "uz": "Jahon otin Uvaysiy",
            "ru": "Джахан-атын Увайси",
            "en": "Uvaysiy (Jahonotin)"
        },
        "era": {
            "uz": "XVIII–XIX asrlar",
            "ru": "XVIII–XIX века",
            "en": "18th–19th century"
        },
        "field": {
            "uz": "Sharq she'riyatining yetuk namoyandasi, chiston (jumboq) ustasi",
            "ru": "Поэтесса, мастер жанра поэтических загадок (чистон)",
            "en": "Celebrated poetess, master of the chiston (poetic riddle) genre"
        },
        "country": {
            "uz": "Qo'qon xonligi / Marg'ilon / O'zbekiston",
            "ru": "Кокандское ханство / Маргилан",
            "en": "Kokand Khanate / Margilan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Painting_of_Heroine_Nodira_by_Shamsroi_Khasanova.jpg",
        "aliases": [
            "uvaysiy",
            "jahon otin uvaysiy",
            "увайси",
            "джахан атын увайси"
        ],
        "fun_fact": {
            "uz": "O'zbek mumtoz adabiyotida murakkab va nafis falsafiy chiston (jumboq-she'r) janrining tengsiz ustasi hisoblangan.",
            "ru": "Считается непревзойденным мастером жанра поэтических загадок (чистон) в классической восточной литературе.",
            "en": "Renowned across Central Asia for elevating the chiston (poetic riddle) into a profound classical literary artform."
        }
    },
    {
        "id": "mahmud_qoshgariy",
        "name": {
            "uz": "Mahmud Qoshg'ariy",
            "ru": "Махмуд аль-Кашгари",
            "en": "Mahmud al-Kashgari"
        },
        "era": {
            "uz": "XI asr",
            "ru": "XI век",
            "en": "11th century"
        },
        "field": {
            "uz": "Turkiy tillar asoschisi, 'Devonu lug'otit turk' ensiklopediyasi muallifi",
            "ru": "Первый тюркский лексикограф, автор «Диван лугат ат-турк»",
            "en": "Pioneering Turkic lexicographer and cartographer"
        },
        "country": {
            "uz": "Qoraxoniylar davlati / Qoshg'ar",
            "ru": "Государство Караханидов / Кашгар",
            "en": "Kara-Khanid Khanate"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/2015-09-11-080312_-_Upal%2C_Mausoleum_des_Uigurischen_Philologen_Muhamad_Al_Kashgari.JPG/640px-2015-09-11-080312_-_Upal%2C_Mausoleum_des_Uigurischen_Philologen_Muhamad_Al_Kashgari.JPG",
        "aliases": [
            "mahmud qoshg'ariy",
            "qoshg'ariy",
            "al-kashgari",
            "махмуд кашгари",
            "кашгари"
        ],
        "fun_fact": {
            "uz": "1074-yilda dunyoda birinchi bo'lib turkiy qabilalar xaritasi va eng qadimiy turkiy qomusiy lug'atni tuzgan.",
            "ru": "Составил первую в мире карту тюркских народов и монументальный сравнительный словарь тюркских наречий.",
            "en": "Produced the first comprehensive dictionary of Turkic languages and the oldest surviving map of Turkic tribal geography."
        }
    },
    {
        "id": "yusuf_xos_hojib",
        "name": {
            "uz": "Yusuf Xos Hojib",
            "ru": "Юсуф Баласагуни",
            "en": "Yusuf Balasaguni (Yusuf Khas Hajib)"
        },
        "era": {
            "uz": "XI asr",
            "ru": "XI век",
            "en": "11th century"
        },
        "field": {
            "uz": "Faylasuf, shoir, 'Qutadg'u bilig' (Baxtga eltuvchi bilim) muallifi",
            "ru": "Философ, мыслитель, автор дидактической поэмы «Кутадгу билиг»",
            "en": "Philosopher, statesman, author of Kutadgu Bilig (Wisdom of Royal Glory)"
        },
        "country": {
            "uz": "Qoraxoniylar davlati / Bolasog'un",
            "ru": "Государство Караханидов / Баласагун",
            "en": "Kara-Khanid Khanate / Balasagun"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Y%C5%ABsuf_Balasaguni_on_1000_som_note.jpg/640px-Y%C5%ABsuf_Balasaguni_on_1000_som_note.jpg",
        "aliases": [
            "yusuf xos hojib",
            "balasaguni",
            "юсуф баласагуни",
            "юсуф хос хаджиб",
            "qutadg'u bilig"
        ],
        "fun_fact": {
            "uz": "Davlatni odil va oqilona boshqarishga bag'ishlangan turkiy tildagi eng birinchi buyuk falsafiy-axloqiy asar muallifi.",
            "ru": "Написал первое этико-политическое наставление правителям на тюркском языке — «Благодатное знание» (Кутадгу билиг).",
            "en": "Authored Kutadgu Bilig (1069), the first major philosophical and political mirrors-for-princes treatise in a Turkic language."
        }
    },
    {
        "id": "chingiz_aytmatov",
        "name": {
            "uz": "Chingiz Aytmatov",
            "ru": "Чингиз Айтматов",
            "en": "Chinghiz Aitmatov"
        },
        "era": {
            "uz": "XX asr (Zamonaviy davr)",
            "ru": "XX век (Современная эпоха)",
            "en": "20th century (Contemporary)"
        },
        "field": {
            "uz": "Jahon adabiyotining ulkan yozuvchisi, diplomat, mutafakkir",
            "ru": "Всемирно известный писатель, философ, дипломат",
            "en": "World-renowned novelist, philosopher, and diplomat"
        },
        "country": {
            "uz": "Qirg'iziston / Markaziy Osiyo",
            "ru": "Кыргызстан / Центральная Азия",
            "en": "Kyrgyzstan / Central Asia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Tschingis_Ajtmatow.jpg/640px-Tschingis_Ajtmatow.jpg",
        "aliases": [
            "chingiz aytmatov",
            "aytmatov",
            "айтматов",
            "чингиз айтматов",
            "chinghiz aitmatov"
        ],
        "fun_fact": {
            "uz": "'Jamila', 'Asrga tatigulik kun', 'Qiyomat' asarlari orqali xalqaro miqyosda 'mankurt' tushunchasini jahon madaniyatiga kiritgan.",
            "ru": "Автор шедевров «Джамиля», «Плаха» и «И дольше века длится день», ввел в мировой обиход понятие «манкурт».",
            "en": "Central Asian literary giant translated into over 150 languages; coined the universally recognized concept of the 'mankurt'."
        }
    },
    {
        "id": "abdulla_qodiriy",
        "name": {
            "uz": "Abdulla Qodiriy",
            "ru": "Абдулла Кадыри",
            "en": "Abdulla Qodiriy"
        },
        "era": {
            "uz": "XX asr boshi (Jadidlar davri)",
            "ru": "Начало XX века (Эпоха джадидизма)",
            "en": "Early 20th century (Jadid era)"
        },
        "field": {
            "uz": "O'zbek romanchiligi asoschisi, jadid adibi, 'O'tkan kunlar' muallifi",
            "ru": "Основоположник узбекского романа, автор «Минувших дней»",
            "en": "Founder of the Uzbek novel, Jadid author of Bygone Days"
        },
        "country": {
            "uz": "O'zbekiston",
            "ru": "Узбекистан",
            "en": "Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Stamps_of_Uzbekistan%2C_2004-07.jpg",
        "aliases": [
            "abdulla qodiriy",
            "qodiriy",
            "кадыри",
            "абдулла кадыри",
            "julqunboy"
        ],
        "fun_fact": {
            "uz": "1922-yilda birinchi o'zbek romani — 'O'tkan kunlar'ni yozib, milliy nasrchilikda yangi davr ochgan.",
            "ru": "Автор первого романа в истории узбекской литературы — «Минувшие дни» (1922), шедевра национальной прозы.",
            "en": "Penned 'Bygone Days' (1922), the first novel in Uzbek literature, immortalizing Otabek and Kumush."
        }
    },
    {
        "id": "cholpon",
        "name": {
            "uz": "Abdulhamid Cho'lpon",
            "ru": "Чулпан (Абдулхамид Сулейман)",
            "en": "Abdulhamid Cho'lpon"
        },
        "era": {
            "uz": "XX asr boshi (Jadidchilik harakati)",
            "ru": "Начало XX века",
            "en": "Early 20th century"
        },
        "field": {
            "uz": "Otashin jadid shoiri, yozuvchi, tarjimon, 'Kecha va kunduz' muallifi",
            "ru": "Поэт-джадид, драматург, автор романа «Ночь и день»",
            "en": "Jadid poet, novelist, translator, author of Night and Day"
        },
        "country": {
            "uz": "O'zbekiston",
            "ru": "Узбекистан",
            "en": "Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Abdulhamid_Cholpon.jpg/330px-Abdulhamid_Cholpon.jpg",
        "aliases": [
            "cho'lpon",
            "cholpon",
            "чулпан",
            "abdulhamid cho'lpon"
        ],
        "fun_fact": {
            "uz": "'Ko'ngil' va erkinlik kuychisi bo'lib, Shekspirning 'Hamlet' asarini o'zbek tiliga yuksak mahorat bilan tarjima qilgan.",
            "ru": "Певец свободы и человеческой души, блестяще перевел «Гамлета» Шекспира на узбекский язык.",
            "en": "Lyrical poet of freedom and national awakening whose translation of Shakespeare's Hamlet into Uzbek is celebrated as a masterpiece."
        }
    },
    {
        "id": "fitrat",
        "name": {
            "uz": "Abdurauf Fitrat",
            "ru": "Абдурауф Фитрат",
            "en": "Abdurauf Fitrat"
        },
        "era": {
            "uz": "XX asr boshi (Jadidlar davri)",
            "ru": "Начало XX века (Джадидизм)",
            "en": "Early 20th century (Jadidism)"
        },
        "field": {
            "uz": "Jadidchilik yetakchisi, qomusiy olim, dramaturg va ma'rifatparvar",
            "ru": "Лидер джадидского движения, ученый-филолог, драматург",
            "en": "Leader of Jadid movement, polymath, playwright and reformer"
        },
        "country": {
            "uz": "Buxoro / O'zbekiston",
            "ru": "Бухара / Узбекистан",
            "en": "Bukhara / Uzbekistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Uzbek_Abdurauf_Fitrat_stamp.jpg/640px-Uzbek_Abdurauf_Fitrat_stamp.jpg",
        "aliases": [
            "abdurauf fitrat",
            "fitrat",
            "фитрат",
            "абдурауф фитрат"
        ],
        "fun_fact": {
            "uz": "Istanbulda tahsil olib, Buxoro xalq respublikasining ta'lim va tashqi ishlar vaziri bo'lgan, o'zbek musiqashunosligi asoschilaridan.",
            "ru": "Один из лидеров младобухарцев, министр Бухарской народной республики, автор фундаментальных трудов по шашмакому.",
            "en": "Studied in Istanbul, led the Young Bukharans reformist movement, and published pioneering treatises on Central Asian classical Shashmaqam."
        }
    },
    {
        "id": "ibn_battuta",
        "name": {
            "uz": "Ibn Battuta",
            "ru": "Ибн Баттута",
            "en": "Ibn Battuta"
        },
        "era": {
            "uz": "XIV asr (O'rta asrlar)",
            "ru": "XIV век",
            "en": "14th century"
        },
        "field": {
            "uz": "Buyuk sayyoh, geograf, 117 ming km masofani kezib chiqqan tadqiqotchi",
            "ru": "Великий путешественник, исследователь средневекового мира",
            "en": "Greatest medieval traveler, explorer, author of the Rihla"
        },
        "country": {
            "uz": "Marokash / Mag'rib",
            "ru": "Марокко",
            "en": "Morocco"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Handmade_oil_painting_reproduction_of_Ibn_Battuta_in_Egypt%2C_a_painting_by_Hippolyte_Leon_Benett..jpg/640px-Handmade_oil_painting_reproduction_of_Ibn_Battuta_in_Egypt%2C_a_painting_by_Hippolyte_Leon_Benett..jpg",
        "aliases": [
            "ibn battuta",
            "ибн баттута",
            "ibn batuta"
        ],
        "fun_fact": {
            "uz": "30 yil davomida deyarli butun islom olami, Xitoy, Oltin O'rda va Markaziy Osiyo (Buxoro, Samarqand) bo'ylab 117 000 km sayohat qilgan.",
            "ru": "За 30 лет странствий преодолел более 117 000 километров, посетив Китай, Индию, Самарканд, Бухару и Африку.",
            "en": "Traveled more than 73,000 miles across 44 modern countries over 30 years, far surpassing Marco Polo's expeditions."
        }
    },
    {
        "id": "al_gazoliy",
        "name": {
            "uz": "Abu Homid al-G'azoliy",
            "ru": "Абу Хамид аль-Газали",
            "en": "Al-Ghazali (Algazel)"
        },
        "era": {
            "uz": "XI–XII asrlar",
            "ru": "XI–XII века",
            "en": "11th–12th century"
        },
        "field": {
            "uz": "'Hujjatul Islom', buyuk mutafakkir, faylasuf va teolog",
            "ru": "«Довод ислама», философ, теолог и суфий",
            "en": "'Proof of Islam', philosopher, jurist, theologian and mystic"
        },
        "country": {
            "uz": "Xuroson / Saljuqiylar davlati",
            "ru": "Хорасан / Сельджукская империя",
            "en": "Khorasan / Seljuk Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Al-Ghaz%C4%81l%C4%AB%2C_Sayr_mulhimah_min_al-Sharq_wa-al-Gharb.png/640px-Al-Ghaz%C4%81l%C4%AB%2C_Sayr_mulhimah_min_al-Sharq_wa-al-Gharb.png",
        "aliases": [
            "al-g'azoliy",
            "al-ghazali",
            "ghazali",
            "аль-газали",
            "газали",
            "hujjatul islom"
        ],
        "fun_fact": {
            "uz": "'Ihyou ulumiddin' (Diniy ilmlarni tiriltirish) asari bilan islom falsafasi va tasavvufini uyg'unlashtirgan daho.",
            "ru": "Автор фундаментального труда «Возрождение религиозных наук», соединивший ортодоксальный ислам и суфизм.",
            "en": "Bridged Islamic orthodoxy and Sufism through his magnum opus 'The Revival of the Religious Sciences'."
        }
    },
    {
        "id": "aleksandr_makedonskiy",
        "name": {
            "uz": "Aleksandr Makedonskiy (Iskandar Zulqarnayn)",
            "ru": "Александр Македонский",
            "en": "Alexander the Great"
        },
        "era": {
            "uz": "Miloddan avvalgi IV asr (Antik davr)",
            "ru": "IV век до н.э. (Античность)",
            "en": "4th century BC (Antiquity)"
        },
        "field": {
            "uz": "Qadimgi dunyoning eng buyuk sarkardasi va imperatori",
            "ru": "Полководец, царь Македонии, создатель мировой державы",
            "en": "King of Macedonia, undefeated conqueror, builder of ancient empire"
        },
        "country": {
            "uz": "Qadimgi Makedoniya / Gretsiya",
            "ru": "Древняя Македония",
            "en": "Ancient Macedonia / Greece"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Alexander_Mosaic_detail_of_Alexander_the_Great_%283x4_cropped%29.jpg/640px-Alexander_Mosaic_detail_of_Alexander_the_Great_%283x4_cropped%29.jpg",
        "aliases": [
            "aleksandr makedonskiy",
            "iskandar",
            "iskandar zulqarnayn",
            "alexander the great",
            "александр македонский",
            "александр великий"
        ],
        "fun_fact": {
            "uz": "Aristotelning shogirdi bo'lib, 30 yoshiga qadar Gretsiyadan Hindistongacha bo'lgan hududni zabt etgan va birorta jangda yengilmagan.",
            "ru": "Ученик Аристотеля, к 30 годам создал крупнейшую империю древности от Греции до Индии, не проиграв ни одного сражения.",
            "en": "Tutored by Aristotle, he forged one of history's largest empires from Greece to northwestern India without a single defeat."
        }
    },
    {
        "id": "yuliy_sezar",
        "name": {
            "uz": "Yuliy Sezar",
            "ru": "Юлий Цезарь",
            "en": "Julius Caesar"
        },
        "era": {
            "uz": "Miloddan avvalgi I asr (Rim respublikasi)",
            "ru": "I век до н.э. (Римская республика)",
            "en": "1st century BC (Roman Republic)"
        },
        "field": {
            "uz": "Rim diktatori, lashkarboshi, Rim imperiyasiga yo'l ochgan davlat arbobi",
            "ru": "Диктатор Рима, полководец, писатель",
            "en": "Dictator of Rome, general, key figure in transition to Roman Empire"
        },
        "country": {
            "uz": "Qadimgi Rim",
            "ru": "Древний Рим",
            "en": "Ancient Rome"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Retrato_de_Julio_C%C3%A9sar_%2826724093101%29_%28cropped%29.jpg/640px-Retrato_de_Julio_C%C3%A9sar_%2826724093101%29_%28cropped%29.jpg",
        "aliases": [
            "yuliy sezar",
            "sezar",
            "julius caesar",
            "caesar",
            "юлий цезарь",
            "цезарь"
        ],
        "fun_fact": {
            "uz": "Galliyani zabt etgan, bugungi quyosh taqvimimiz asoschisi ('Yulian taqvimi') bo'lgan va miloddan avvalgi 44-yilda fitnachilar tomonidan o'ldirilgan.",
            "ru": "Завоевал Галлию, создал Юлианский календарь, которым мы пользуемся по сей день, и был убит в Сенате.",
            "en": "Conquered Gaul, reformed the calendar (the Julian calendar), and was assassinated on the Ides of March 44 BC."
        }
    },
    {
        "id": "napoleon_bonapart",
        "name": {
            "uz": "Napoleon Bonapart",
            "ru": "Наполеон I Бонапарт",
            "en": "Napoleon Bonaparte"
        },
        "era": {
            "uz": "XVIII–XIX asrlar",
            "ru": "XVIII–XIX века",
            "en": "18th–19th century"
        },
        "field": {
            "uz": "Fransuzlar imperatori, buyuk harbiy strateg, Fuqarolik kodeksi muallifi",
            "ru": "Император французов, полководец, автор Кодекса Наполеона",
            "en": "Emperor of the French, military strategist, creator of Napoleonic Code"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project.jpg/640px-Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project.jpg",
        "aliases": [
            "napoleon bonapart",
            "napoleon",
            "наполеон",
            "наполеон бонапарт",
            "bonaparte"
        ],
        "fun_fact": {
            "uz": "Deyarli butun kontinental Yevropani bo'ysundirgan va butun dunyo zamonaviy huquq tizimiga asos bo'lgan Fuqarolik Kodeksini yaratgan.",
            "ru": "Покорил большую часть континентальной Европы и создал Гражданский кодекс, легший в основу правовых систем десятков стран.",
            "en": "Master of military tactics who dominated European affairs and established the Napoleonic Code, foundational to civil law."
        }
    },
    {
        "id": "chingizxon",
        "name": {
            "uz": "Chingizxon (Temuchin)",
            "ru": "Чингисхан (Темуджин)",
            "en": "Genghis Khan (Temüjin)"
        },
        "era": {
            "uz": "XII–XIII asrlar",
            "ru": "XII–XIII века",
            "en": "12th–13th century"
        },
        "field": {
            "uz": "Tarixdagi eng yirik uzluksiz imperiya asoschisi, sarkarda",
            "ru": "Основатель крупнейшей в истории континентальной империи",
            "en": "Founder and First Great Khan of the Mongol Empire"
        },
        "country": {
            "uz": "Mo'g'ullar imperiyasi",
            "ru": "Монгольская империя",
            "en": "Mongol Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/YuanEmperorAlbumGenghisPortrait.jpg/640px-YuanEmperorAlbumGenghisPortrait.jpg",
        "aliases": [
            "chingizxon",
            "chingiz xon",
            "genghis khan",
            "чингисхан",
            "temujin",
            "temuchin"
        ],
        "fun_fact": {
            "uz": "Tarqoq ko'chmanchi qabilalarni birlashtirib, Tinch okeanidan Sharqiy Yevropagacha cho'zilgan tarixdagi eng yirik quruqlik imperiyasini barpo etgan.",
            "ru": "Объединил кочевые племена и создал самую большую в истории сухопутную империю от Китая до Дуная.",
            "en": "United nomadic tribes to forge the contiguous Mongol Empire stretching from the Sea of Japan to Eastern Europe."
        }
    },
    {
        "id": "buyuk_kir",
        "name": {
            "uz": "Buyuk Kir II (Kavush)",
            "ru": "Кир II Великий",
            "en": "Cyrus the Great"
        },
        "era": {
            "uz": "Miloddan avvalgi VI asr",
            "ru": "VI век до н.э.",
            "en": "6th century BC"
        },
        "field": {
            "uz": "Axamoniylar imperiyasi asoschisi, inson huquqlari ilk deklaratsiyasi muallifi",
            "ru": "Основатель первой Персидской империи, автор «Цилиндра Кира»",
            "en": "Founder of the Achaemenid Empire, author of Cyrus Cylinder"
        },
        "country": {
            "uz": "Axamoniylar imperiyasi (Qadimgi Eron)",
            "ru": "Держава Ахеменидов (Древняя Персия)",
            "en": "Achaemenid Empire (Ancient Persia)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Cyrus_II_%28The_Great%29_%28cropped%29.jpg/640px-Cyrus_II_%28The_Great%29_%28cropped%29.jpg",
        "aliases": [
            "buyuk kir",
            "kir",
            "cyrus the great",
            "cyrus",
            "кир великий",
            "кир",
            "cyrus ii"
        ],
        "fun_fact": {
            "uz": "Bobilni zabt etgach, yahudiylarni asirlikdan ozod qilgan; uning silindr-yozuvi tarixdagi inson huquqlarining ilk deklaratsiyasi deb hisoblanadi.",
            "ru": "Освободил иудеев из Вавилонского пленения; глиняный Цилиндр Кира называют первой декларацией прав человека.",
            "en": "Freed the Jewish exiles in Babylon and created the Cyrus Cylinder, hailed as the world's earliest charter of human rights."
        }
    },
    {
        "id": "oktavian_avgust",
        "name": {
            "uz": "Oktavian Avgust",
            "ru": "Октавиан Август",
            "en": "Augustus (Caesar Augustus)"
        },
        "era": {
            "uz": "Miloddan avvalgi I asr – Milodiy I asr",
            "ru": "I век до н.э. – I век н.э.",
            "en": "63 BC – 14 AD"
        },
        "field": {
            "uz": "Rim imperiyasining birinchi imperatori, Pax Romana asoschisi",
            "ru": "Первый римский император, основатель эпохи «Римского мира»",
            "en": "First Roman Emperor, founder of the Principate and Pax Romana"
        },
        "country": {
            "uz": "Rim imperiyasi",
            "ru": "Римская империя",
            "en": "Roman Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Augustus_of_Prima_Porta.jpg/640px-Augustus_of_Prima_Porta.jpg",
        "aliases": [
            "oktavian avgust",
            "avgust",
            "augustus",
            "caesar augustus",
            "октавиан август",
            "август"
        ],
        "fun_fact": {
            "uz": "Rimni g'ishtdan qabul qilib, uni marmarga aylantirganini aytgan va 200 yillik 'Pax Romana' (Rim tinchligi) davrini boshlab bergan.",
            "ru": "Превратил Рим из кирпичного города в мраморный и начал двухвековую эпоху процветания Pax Romana.",
            "en": "Famously boasted he found Rome a city of brick and left it a city of marble, launching the 200-year Pax Romana."
        }
    },
    {
        "id": "kleopatra",
        "name": {
            "uz": "Kleopatra VII",
            "ru": "Клеопатра VII",
            "en": "Cleopatra VII"
        },
        "era": {
            "uz": "Miloddan avvalgi I asr (Antik davr)",
            "ru": "I век до н.э.",
            "en": "1st century BC"
        },
        "field": {
            "uz": "Qadimgi Misrning so'nggi faol hukmdori va malikasi",
            "ru": "Последняя царица эллинистического Египта",
            "en": "Last active ruler of Ptolemaic Kingdom of Egypt"
        },
        "country": {
            "uz": "Qadimgi Misr (Ptolemeylar sulolasi)",
            "ru": "Эллинистический Египет",
            "en": "Ptolemaic Egypt"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kleopatra-VII.-Altes-Museum-Berlin1.jpg/640px-Kleopatra-VII.-Altes-Museum-Berlin1.jpg",
        "aliases": [
            "kleopatra",
            "cleopatra",
            "клеопатра",
            "kleopatra vii"
        ],
        "fun_fact": {
            "uz": "To'qqizta tilni mukammal bilgan, falsafa va diplomatiyani chuqur egallagan afsonaviy Misr malikasi.",
            "ru": "Говорила более чем на девяти языках, была блестящим дипломатом и союзницей Юлия Цезаря и Марка Антония.",
            "en": "Highly educated polyglot fluent in at least nine languages who formed alliances with Julius Caesar and Mark Antony."
        }
    },
    {
        "id": "karl_buyuk",
        "name": {
            "uz": "Karl Buyuk (Sharlemann)",
            "ru": "Карл Великий",
            "en": "Charlemagne (Charles the Great)"
        },
        "era": {
            "uz": "VIII–IX asrlar",
            "ru": "VIII–IX века",
            "en": "8th–9th century"
        },
        "field": {
            "uz": "Franklar qiroli, Rimliklar imperatori, 'Yevropa otasi'",
            "ru": "Король франков, первый император Запада, «Отец Европы»",
            "en": "King of the Franks, Emperor of the Romans, 'Father of Europe'"
        },
        "country": {
            "uz": "Franklar imperiyasi (G'arbiy Yevropa)",
            "ru": "Франкское королевство / Империя Запада",
            "en": "Frankish Empire / Holy Roman Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Charlemagne_denier_Mayence_812_814.jpg/640px-Charlemagne_denier_Mayence_812_814.jpg",
        "aliases": [
            "karl buyuk",
            "charlemagne",
            "карл великий",
            "шарлемань"
        ],
        "fun_fact": {
            "uz": "G'arbiy Rim qulaganidan so'ng Markaziy va G'arbiy Yevropani qayta birlashtirgan va Karolinglar uyg'onish davrini boshlagan.",
            "ru": "Объединил большую часть Западной и Центральной Европы впервые со времен падения Римской империи.",
            "en": "United Western and Central Europe for the first time since the classical Roman Empire, sparking the Carolingian Renaissance."
        }
    },
    {
        "id": "salohiddin_ayyubiy",
        "name": {
            "uz": "Salohiddin Ayyubiy",
            "ru": "Саладин (Салах ад-Дин)",
            "en": "Saladin (Salah al-Din)"
        },
        "era": {
            "uz": "XII asr",
            "ru": "XII век",
            "en": "12th century"
        },
        "field": {
            "uz": "Ayyubiylar sultoni, Quddusni ozod qilgan mashhur lashkarboshi",
            "ru": "Султан Египта и Сирии, отвоевавший Иерусалим у крестоносцев",
            "en": "First Sultan of Egypt and Syria, chivalrous warrior who took Jerusalem"
        },
        "country": {
            "uz": "Ayyubiylar saltanati / Misr / Suriya",
            "ru": "Султанат Айюбидов / Египет",
            "en": "Ayyubid Sultanate / Egypt"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Al-Nasir_I_Salah_al-Din_Yusuf_%28Saladin%29._AH_564-589_%281169-1193_CE%29_%C3%86_Dirham_%2830.1mm%2C_13.28_g%2C_6h%29._Without_mint-name._Dated_AH_586_%28AD_1190-91%29._Sultan_sitting_facing%2C_cross-legged%2C_on_high-backed_throne_%28obverse%29.jpg/640px-thumbnail.jpg",
        "aliases": [
            "salohiddin ayyubiy",
            "saladin",
            "саладин",
            "салах ад-дин",
            "salah ad-din"
        ],
        "fun_fact": {
            "uz": "1187-yilda Hittin jangida salibchilarni mag'lub etib Quddusni qaytarib olgan; o'zining saxiy va olijanob xulqi bilan hattoki dushmanlari hurmatini qozongan.",
            "ru": "Отвоевал Иерусалим у крестоносцев в 1187 году и снискал легендарное уважение в Европе за благородство и милосердие к побежденным.",
            "en": "Recaptured Jerusalem from the Crusaders in 1187 and became an archetype of chivalry and generosity even among European adversaries."
        }
    },
    {
        "id": "sulaymon_qonuniy",
        "name": {
            "uz": "Sulton Sulaymon Qonuniy",
            "ru": "Сулейман I Великолепный (Кануни)",
            "en": "Suleiman the Magnificent"
        },
        "era": {
            "uz": "XVI asr (Usmonlilar oltin davri)",
            "ru": "XVI век (Золотой век Османской империи)",
            "en": "16th century (Ottoman Golden Age)"
        },
        "field": {
            "uz": "Usmonlilar sultoni, qonunshunos hukmdor, imperiyani cho'qqiga olib chiqqan monarx",
            "ru": "Десятый султан Османской империи, законодатель и завоеватель",
            "en": "10th Ottoman Sultan, Caliph, legislator and conqueror"
        },
        "country": {
            "uz": "Usmonlilar imperiyasi",
            "ru": "Османская империя",
            "en": "Ottoman Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/EmperorSuleiman.jpg/640px-EmperorSuleiman.jpg",
        "aliases": [
            "sulaymon qonuniy",
            "suleiman the magnificent",
            "сулейман великолепный",
            "сулейман кануни",
            "sultan suleyman"
        ],
        "fun_fact": {
            "uz": "Usmonlilar imperiyasini 46 yil boshqargan va uning davrida imperiya Yevropa, Osiyo va Afrikada qudratining eng yuksak cho'qqisiga chiqqan.",
            "ru": "Правил 46 лет, возглавил золотой век Османской империи, лично руководил тринадцатью военными походами.",
            "en": "Longest-reigning Ottoman sultan (46 years) whose fleet dominated the Mediterranean and armies reached the gates of Vienna."
        }
    },
    {
        "id": "fotih_sulton_mehmet",
        "name": {
            "uz": "Fotih Sulton Mehmet II",
            "ru": "Мехмед II Фатих (Завоеватель)",
            "en": "Mehmed the Conqueror (Mehmed II)"
        },
        "era": {
            "uz": "XV asr",
            "ru": "XV век",
            "en": "15th century"
        },
        "field": {
            "uz": "Konstantinopolni zabt etgan sulton, sarkarda va davlat arbobi",
            "ru": "Османский султан, завоевавший Константинополь в 1453 году",
            "en": "Ottoman Sultan who conquered Constantinople in 1453"
        },
        "country": {
            "uz": "Usmonlilar imperiyasi",
            "ru": "Османская империя",
            "en": "Ottoman Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Bellini%2C_Gentile_-_Sultan_Mehmet_II.jpg/640px-Bellini%2C_Gentile_-_Sultan_Mehmet_II.jpg",
        "aliases": [
            "fotih sulton mehmet",
            "mehmed ii",
            "mehmet fotih",
            "мехмед фатих",
            "мехмед ii"
        ],
        "fun_fact": {
            "uz": "21 yoshida kemalarni quruqlik orqali Oltin Shox qo'ltig'iga tushirib, ming yillik Vizantiya imperiyasini yakunlagan (1453).",
            "ru": "В 21 год взял неприступный Константинополь, перетащив корабли по суше, и положил конец Византийской империи.",
            "en": "At just age 21, he breached the Theodosian Walls of Constantinople by dragging ships overland, bringing an end to Byzantium."
        }
    },
    {
        "id": "pyotr_birinchi",
        "name": {
            "uz": "Buyuk Pyotr I",
            "ru": "Пётр I Великий",
            "en": "Peter the Great"
        },
        "era": {
            "uz": "XVII–XVIII asrlar",
            "ru": "XVII–XVIII века",
            "en": "17th–18th century"
        },
        "field": {
            "uz": "Butunrossiya Birinchi Imperatori, Rossiyani Yevropalashtirgan islohotchi",
            "ru": "Первый Император Всероссийский, основатель Санкт-Петербурга",
            "en": "First Emperor of All Russia, modernizer, founder of Saint Petersburg"
        },
        "country": {
            "uz": "Rossiya imperiyasi",
            "ru": "Российская империя",
            "en": "Russian Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Inconnu_d%27apr%C3%A8s_J.-M._Nattier%2C_Portrait_de_Pierre_Ier_%28mus%C3%A9e_de_l%E2%80%99Ermitage%29.jpg/640px-Inconnu_d%27apr%C3%A8s_J.-M._Nattier%2C_Portrait_de_Pierre_Ier_%28mus%C3%A9e_de_l%E2%80%99Ermitage%29.jpg",
        "aliases": [
            "pyotr birinchi",
            "buyuk pyotr",
            "peter the great",
            "петр первый",
            "петр великий",
            "петр 1"
        ],
        "fun_fact": {
            "uz": "Boltiq bo'yida Sankt-Peterburg shahrini qurdirdi, dengiz flotiga asos soldi va Rossiyani jahon qudratiga aylantirdi.",
            "ru": "«Прорубил окно в Европу», создал регулярный флот и армию, заложил Санкт-Петербург в 1703 году.",
            "en": "Founded Saint Petersburg in 1703, established the Imperial Russian Navy, and reformed Russia into a major European empire."
        }
    },
    {
        "id": "yekaterina_ikkinchi",
        "name": {
            "uz": "Yekaterina II Buyuk",
            "ru": "Екатерина II Великая",
            "en": "Catherine the Great"
        },
        "era": {
            "uz": "XVIII asr (Ma'rifatparvarlik davri)",
            "ru": "XVIII век (Эпоха Просвещения)",
            "en": "18th century (Age of Enlightenment)"
        },
        "field": {
            "uz": "Rossiya imperatori, Qrim va Yangi Rossiyani qo'shib olgan hukmdor",
            "ru": "Императрица Всероссийская, присоединила Крым и Новороссию",
            "en": "Empress of All Russia, longest-ruling female leader of Russia"
        },
        "country": {
            "uz": "Rossiya imperiyasi",
            "ru": "Российская империя",
            "en": "Russian Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Catherine_II_after_Roslin%2C_Rokotov_%281780s%2C_Kunsthistorisches_Museum%29.jpg/640px-Catherine_II_after_Roslin%2C_Rokotov_%281780s%2C_Kunsthistorisches_Museum%29.jpg",
        "aliases": [
            "yekaterina ikkinchi",
            "yekaterina buyuk",
            "catherine the great",
            "екатерина великая",
            "екатерина ii"
        ],
        "fun_fact": {
            "uz": "Volter va Didro bilan xat yozishgan, Ermitaj muzeyiga asos solgan va Qora dengiz bo'ylarini imperiyaga qo'shgan.",
            "ru": "Вела переписку с Вольтером, основала Эрмитаж и правила Россией 34 года, значительно расширив ее границы.",
            "en": "Corresponded with Voltaire and Diderot, founded the Hermitage Museum, and brought the Crimea into the Russian Empire."
        }
    },
    {
        "id": "akbarshoh",
        "name": {
            "uz": "Akbarshoh Buyuk",
            "ru": "Акбар I Великий",
            "en": "Akbar the Great"
        },
        "era": {
            "uz": "XVI–XVII asrlar",
            "ru": "XVI–XVII века",
            "en": "16th–17th century"
        },
        "field": {
            "uz": "Boburiy hukmdor, barcha dinlarga bag'rikenglik siyosatini yurgizgan monarx",
            "ru": "Падишах Империи Великих Моголов, реформатор и покровитель искусств",
            "en": "Third Mughal Emperor, known for religious tolerance and expansion"
        },
        "country": {
            "uz": "Boburiylar saltanati / Hindiston",
            "ru": "Империя Великих Моголов / Индия",
            "en": "Mughal Empire / India"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Govardhan._Akbar_With_Lion_and_Calf_ca._1630%2C_Metmuseum_%28cropped%29.jpg/640px-Govardhan._Akbar_With_Lion_and_Calf_ca._1630%2C_Metmuseum_%28cropped%29.jpg",
        "aliases": [
            "akbarshoh",
            "akbar the great",
            "акбар великий",
            "акбаршах",
            "jaloliddin akbar"
        ],
        "fun_fact": {
            "uz": "Boburning nabirasi bo'lib, Hindistonda barcha dinlar tengligini joriy qilgan va 'Sulhi kull' (Umumiy tinchlik) tamoyilini o'rnatgan.",
            "ru": "Внук Бабура, объединил большую часть Индийского субконтинента и провозгласил политику религиозной веротерпимости.",
            "en": "Tripled the Mughal Empire in size and wealth, abolishing the jizya tax on non-Muslims and welcoming multi-faith debates."
        }
    },
    {
        "id": "qirolicha_viktoriya",
        "name": {
            "uz": "Qirolicha Viktoriya",
            "ru": "Королева Виктория",
            "en": "Queen Victoria"
        },
        "era": {
            "uz": "XIX asr (Viktoriya davri)",
            "ru": "XIX век (Викторианская эпоха)",
            "en": "19th century (Victorian era)"
        },
        "field": {
            "uz": "Buyuk Britaniya qirolichasi va Hindiston imperatori ayoli",
            "ru": "Королева Великобритании, правительница глобальной империи",
            "en": "Queen of the United Kingdom and Empress of India"
        },
        "country": {
            "uz": "Britaniya imperiyasi",
            "ru": "Британская империя",
            "en": "British Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Queen_Victoria_by_Bassano.jpg/640px-Queen_Victoria_by_Bassano.jpg",
        "aliases": [
            "qirolicha viktoriya",
            "viktoriya",
            "queen victoria",
            "королева виктория",
            "виктория"
        ],
        "fun_fact": {
            "uz": "63 yil hukmronlik qilgan; uning davrida Britaniya imperiyasi 'quyosh botmaydigan saltanat' deb atalgan va sanoat inqilobi cho'qqisiga chiqqan.",
            "ru": "Ее 63-летнее правление ознаменовало расцвет Британской империи, над которой «никогда не заходило солнце».",
            "en": "Her 63-year reign oversaw the apex of the Industrial Revolution and unprecedented global expansion of the British Empire."
        }
    },
    {
        "id": "qirolicha_yelizaveta_birinchi",
        "name": {
            "uz": "Qirolicha Yelizaveta I",
            "ru": "Елизавета I",
            "en": "Elizabeth I"
        },
        "era": {
            "uz": "XVI–XVII asrlar (Yelizaveta davri)",
            "ru": "XVI–XVII века (Золотой век Англии)",
            "en": "16th–17th century (Elizabethan era)"
        },
        "field": {
            "uz": "Angliya qirolichasi, Ispan Armadasini yenggan 'Bokira qirolicha'",
            "ru": "Королева Англии, разгромившая Непобедимую армаду",
            "en": "Queen of England and Ireland, defeated the Spanish Armada"
        },
        "country": {
            "uz": "Angliya",
            "ru": "Англия",
            "en": "England"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Darnley_stage_3.jpg/640px-Darnley_stage_3.jpg",
        "aliases": [
            "yelizaveta i",
            "elizabeth i",
            "елизавета 1",
            "елизавета i",
            "bokira qirolicha"
        ],
        "fun_fact": {
            "uz": "1588-yilda qudratli Ispan Armadasini tor-mor etgan va uning davrida Shekspir ingliz teatrini jahon cho'qqisiga olib chiqqan.",
            "ru": "Разгромила испанскую «Непобедимую армаду» в 1588 году; в ее эпоху творил Уильям Шекспир.",
            "en": "Defeated the Spanish Armada in 1588, ushering in the golden age of English drama and naval exploration."
        }
    },
    {
        "id": "janna_dark",
        "name": {
            "uz": "Janna d'Ark (Orlean qizi)",
            "ru": "Жанна д’Арк (Орлеанская дева)",
            "en": "Joan of Arc"
        },
        "era": {
            "uz": "XV asr (Yuz yillik urush)",
            "ru": "XV век (Столетняя война)",
            "en": "15th century (Hundred Years' War)"
        },
        "field": {
            "uz": "Fransiya milliy qahramoni, Orleanni qutqargan qiz-sarkarda",
            "ru": "Национальная героиня Франции, снявшая осаду Орлеана",
            "en": "National heroine of France, saint, commander in Hundred Years' War"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Joan_of_Arc_miniature_graded.jpg/640px-Joan_of_Arc_miniature_graded.jpg",
        "aliases": [
            "janna d'ark",
            "joan of arc",
            "жанна д'арк",
            "жанна дарк",
            "orlean qizi"
        ],
        "fun_fact": {
            "uz": "17 yoshli dehqon qizi bo'la turib fransuz armiyasiga boshchilik qilgan va inglizlar qamalidagi Orlean shahrini ozod qilgan.",
            "ru": "В 17 лет возглавила французские войска, сняла многомесячную осаду Орлеана и переломила ход Столетней войны.",
            "en": "Peasant teenager who claimed divine guidance, lifted the Siege of Orléans in nine days, and turned the tide of the Hundred Years' War."
        }
    },
    {
        "id": "ramses_ikkinchi",
        "name": {
            "uz": "Ramses II Buyuk",
            "ru": "Рамсес II Великий",
            "en": "Ramesses the Great (Ramesses II)"
        },
        "era": {
            "uz": "Miloddan avvalgi XIII asr (Yangi podsholik)",
            "ru": "XIII век до н.э. (Новое царство)",
            "en": "13th century BC (New Kingdom)"
        },
        "field": {
            "uz": "Misrning eng buyuk fir'avni, Abu-Simbel ibodatxonasini qurdirgan hukmdor",
            "ru": "Фараон Древнего Египта, строитель храмов Абу-Симбела",
            "en": "Pharaoh of the 19th Dynasty, monumental builder of ancient Egypt"
        },
        "country": {
            "uz": "Qadimgi Misr",
            "ru": "Древний Египет",
            "en": "Ancient Egypt"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Ramses_II_British_Museum.jpg/640px-Ramses_II_British_Museum.jpg",
        "aliases": [
            "ramses ii",
            "ramses",
            "ramesses ii",
            "рамсес",
            "рамсес ii",
            "ramzes"
        ],
        "fun_fact": {
            "uz": "Misrni 66 yil boshqargan, Abu-Simbel va Karnakdagi ulkan ibodatxonalarni qurdirgan hamda tarixdagi ilk tinchlik bitimini (Xettlar bilan) imzolagan.",
            "ru": "Правил Египтом 66 лет, построил гигантские храмы Абу-Симбела и заключил древнейший дошедший до нас мирный договор.",
            "en": "Ruled Egypt for 66 years, erected Abu Simbel, and concluded the oldest surviving recorded peace treaty with the Hittites."
        }
    },
    {
        "id": "hammurapi",
        "name": {
            "uz": "Hammurapi",
            "ru": "Хаммурапи",
            "en": "Hammurabi"
        },
        "era": {
            "uz": "Miloddan avvalgi XVIII asr",
            "ru": "XVIII век до н.э.",
            "en": "18th century BC"
        },
        "field": {
            "uz": "Bobil shohi, insoniyat tarixidagi ilk yozma qonunlar to'plami muallifi",
            "ru": "Царь Вавилона, создатель свода законов Хаммурапи",
            "en": "King of Babylon, author of the Code of Hammurabi"
        },
        "country": {
            "uz": "Bobil podsholigi (Mesopotamiya)",
            "ru": "Вавилонское царство (Месопотамия)",
            "en": "Babylon (Mesopotamia)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/F0182_Louvre_Code_Hammourabi_Bas-relief_Sb8_rwk.jpg/640px-F0182_Louvre_Code_Hammourabi_Bas-relief_Sb8_rwk.jpg",
        "aliases": [
            "hammurapi",
            "hammurabi",
            "хаммурапи"
        ],
        "fun_fact": {
            "uz": "Qora bazalt toshga o'yilgan 282 ta moddadan iborat qonunlar majmuasi ('Ko'zga ko'z, tishga tish') insoniyatning ilk huquqiy yodgorligidir.",
            "ru": "Создал один из древнейших сводов законов в истории, высеченный на черной базальтовой стеле («Око за око, зуб за зуб»).",
            "en": "Enacted the Code of Hammurabi inscribed on a black diorite stele, establishing the famed principle 'an eye for an eye'."
        }
    },
    {
        "id": "ashoka",
        "name": {
            "uz": "Ashoka Buyuk",
            "ru": "Ашока Великий",
            "en": "Ashoka the Great"
        },
        "era": {
            "uz": "Miloddan avvalgi III asr",
            "ru": "III век до н.э.",
            "en": "3rd century BC"
        },
        "field": {
            "uz": "Hind imperatori, buddizmni butun Osiyo bo'ylab yoygan tinchliksevar monarx",
            "ru": "Император Индии, распространитель буддизма и ненасилия",
            "en": "Maurya Emperor, patron of Buddhism and champion of non-violence"
        },
        "country": {
            "uz": "Maurya imperiyasi (Hindiston)",
            "ru": "Империя Маурьев (Индия)",
            "en": "Maurya Empire (Ancient India)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Ashoka%27s_visit_to_the_Ramagrama_stupa_Sanchi_Stupa_1_Southern_gateway.jpg/640px-Ashoka%27s_visit_to_the_Ramagrama_stupa_Sanchi_Stupa_1_Southern_gateway.jpg",
        "aliases": [
            "ashoka",
            "ashoka buyuk",
            "ашока",
            "ашока великий"
        ],
        "fun_fact": {
            "uz": "Kalinga urushidagi qirg'inlardan dahshatga tushib zo'ravonlikdan voz kechgan va buddizmni butun dunyoga tarqatgan; uning 'Sherli kapiteli' Hindiston gerbi bo'ldi.",
            "ru": "После кровопролитной войны раскаялся, принял буддизм и провозгласил ненасилие; его Стелла с львами — герб Индии.",
            "en": "Renounced warfare after the brutal Kalinga War, converted to Buddhism, and commissioned the Ashoka Lion Capital—modern India's national emblem."
        }
    },
    {
        "id": "qin_shi_huang",
        "name": {
            "uz": "Sin Shixuandi",
            "ru": "Цинь Шихуанди",
            "en": "Qin Shi Huang"
        },
        "era": {
            "uz": "Miloddan avvalgi III asr",
            "ru": "III век до н.э.",
            "en": "3rd century BC"
        },
        "field": {
            "uz": "Yaxlit Xitoyning birinchi imperatori, Buyuk Xitoy devorini birlashtirgan hukmdor",
            "ru": "Первый император единого Китая, строитель Великой стены",
            "en": "First Emperor of unified China, commissioner of Terracotta Army"
        },
        "country": {
            "uz": "Sin imperiyasi (Xitoy)",
            "ru": "Империя Цинь (Китай)",
            "en": "Qin Dynasty (Ancient China)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/QinShiHuang19century.jpg/640px-QinShiHuang19century.jpg",
        "aliases": [
            "qin shi huang",
            "sin shixuandi",
            "цинь шихуан",
            "цинь шихуанди"
        ],
        "fun_fact": {
            "uz": "Tarqoq yetti podsholikni birlashtirib birinchi Xitoy imperiyasiga asos solgan va o'zi bilan birga ko'milgan afsonaviy 'Terrakota armiyasi'ni yaratgan.",
            "ru": "Объединил враждующие царства Китая, стандартизировал иероглифы и создал многотысячную Терракотовую армию.",
            "en": "Unified China's warring states into a single empire, began the Great Wall, and was buried with the Terracotta Army."
        }
    },
    {
        "id": "attila",
        "name": {
            "uz": "Attila (Xunlar yetakchisi)",
            "ru": "Аттила (вождь гуннов)",
            "en": "Attila the Hun"
        },
        "era": {
            "uz": "V asr",
            "ru": "V век",
            "en": "5th century"
        },
        "field": {
            "uz": "Xunlar hukmdori, Rim imperiyasini larzaga solgan 'Tangri qamchisi'",
            "ru": "Правитель гуннов, «Бич Божий», гроза Рима и Византии",
            "en": "Ruler of the Huns, 'Flagellum Dei' who challenged Rome"
        },
        "country": {
            "uz": "Xunlar imperiyasi",
            "ru": "Гуннская держава",
            "en": "Hunnic Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Eugene_Ferdinand_Victor_Delacroix_Attila_fragment.jpg/640px-Eugene_Ferdinand_Victor_Delacroix_Attila_fragment.jpg",
        "aliases": [
            "attila",
            "аттила",
            "attila the hun",
            "tangri qamchisi"
        ],
        "fun_fact": {
            "uz": "Yevropada 'Tangri qamchisi' (Flagellum Dei) deb atalgan va o'z davrida Sharqiy hamda G'arbiy Rim imperiyalarini birdek bo'ysundirgan.",
            "ru": "Прозван европейцами «Бичом Божьим», создал державу от Рейна до Волги и держал в страхе обе Римские империи.",
            "en": "Feared across Europe as the 'Scourge of God', ruling an empire from the Rhine to the Volga that besieged both Romes."
        }
    },
    {
        "id": "gannibal_barka",
        "name": {
            "uz": "Gannibal Barka",
            "ru": "Ганнибал Барка",
            "en": "Hannibal Barca"
        },
        "era": {
            "uz": "Miloddan avvalgi III–II asrlar",
            "ru": "III–II века до н.э.",
            "en": "3rd–2nd century BC"
        },
        "field": {
            "uz": "Karfagen sarkardasi, harbiy strategiya dahosi, Kanna jangi g'olibi",
            "ru": "Карфагенский полководец, величайший военный тактик древности",
            "en": "Carthaginian general, master tactician who marched war elephants over the Alps"
        },
        "country": {
            "uz": "Karfagen",
            "ru": "Карфаген",
            "en": "Carthage"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Hannibal_Barca_bust_from_Capua_photo.jpg/640px-Hannibal_Barca_bust_from_Capua_photo.jpg",
        "aliases": [
            "gannibal",
            "gannibal barka",
            "hannibal",
            "hannibal barca",
            "ганнибал",
            "ганнибал барка"
        ],
        "fun_fact": {
            "uz": "Jangovar fillar bilan birga Alp tog'larini qordan oshib o'tib, Miloddan avvalgi 216-yilda Kanna jangida Rim armiyasini to'liq qirib tashlagan.",
            "ru": "Пересек Альпы с боевыми слонами и окружил вдвое превосходящую римскую армию в легендарной битве при Каннах.",
            "en": "Marched war elephants across the Alps into Italy and orchestrated the textbook encirclement victory at Cannae (216 BC)."
        }
    },
    {
        "id": "mark_avreliy",
        "name": {
            "uz": "Mark Avreliy",
            "ru": "Марк Аврелий",
            "en": "Marcus Aurelius"
        },
        "era": {
            "uz": "II asr (Pax Romana)",
            "ru": "II век",
            "en": "2nd century AD"
        },
        "field": {
            "uz": "Rim imperatori, stoisizm falsafasi namoyandasi, 'Mulohazalar' muallifi",
            "ru": "Римский император, философ-стоик, автор «Размышлений»",
            "en": "Roman Emperor, Stoic philosopher, author of Meditations"
        },
        "country": {
            "uz": "Rim imperiyasi",
            "ru": "Римская империя",
            "en": "Roman Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/MSR-ra-61-b-1-DM.jpg/640px-MSR-ra-61-b-1-DM.jpg",
        "aliases": [
            "mark avreliy",
            "marcus aurelius",
            "марк аврелий"
        ],
        "fun_fact": {
            "uz": "Taxtdagi faylasuf deb atalgan; harbiy yurishlar chodirida o'zi uchun yozgan 'Mulohazalar' (Meditations) asari stoisizmning eng mashhur kitobidir.",
            "ru": "«Философ на троне», управлявший империей из военного походного шатра и написавший шедевр стоицизма «Наедине с собой».",
            "en": "The quintessential 'philosopher king' whose personal journal 'Meditations' remains one of the world's most read Stoic texts."
        }
    },
    {
        "id": "simon_bolivar",
        "name": {
            "uz": "Simon Bolivar",
            "ru": "Симон Боливар",
            "en": "Simón Bolívar"
        },
        "era": {
            "uz": "XVIII–XIX asrlar",
            "ru": "XVIII–XIX века",
            "en": "18th–19th century"
        },
        "field": {
            "uz": "'El Libertador' (Xaloskor), Janubiy Amerikani Ispaniyadan ozod qilgan yetakchi",
            "ru": "«Освободитель» Южной Америки от испанского владычества",
            "en": "'El Libertador', liberator of northern South America from Spain"
        },
        "country": {
            "uz": "Venesuela / Janubiy Amerika",
            "ru": "Венесуэла / Южная Америка",
            "en": "Venezuela / Gran Colombia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Sim%C3%B3n_Bol%C3%ADvar._Toro_Moreno%2C_Luis._1922%2C_Legislative_Palace%2C_La_Paz.png/640px-Sim%C3%B3n_Bol%C3%ADvar._Toro_Moreno%2C_Luis._1922%2C_Legislative_Palace%2C_La_Paz.png",
        "aliases": [
            "simon bolivar",
            "bolivar",
            "боливар",
            "симон боливар",
            "el libertador"
        ],
        "fun_fact": {
            "uz": "Venesuela, Kolumbiya, Ekvador, Peru va Boliviya davlatlarini Ispaniya mustamlakasidan ozod qilgan; Boliviya davlati uning sharafiga nomlangan.",
            "ru": "Освободил от испанцев территорию шести современных государств; страна Боливия названа в его честь.",
            "en": "Liberated six South American nations from Spanish rule; both Bolivia and the Venezuelan currency are named in his honor."
        }
    },
    {
        "id": "mahatma_gandi",
        "name": {
            "uz": "Mahatma Gandi",
            "ru": "Махатма Ганди",
            "en": "Mahatma Gandhi"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "Hindiston milliy ozodlik yetakchisi, 'Satyagraxa' (zo'ravonliksiz kurash) asoschisi",
            "ru": "Лидер национально-освободительного движения Индии, идеолог ненасилия",
            "en": "Leader of Indian independence, pioneer of Satyagraha (non-violent resistance)"
        },
        "country": {
            "uz": "Hindiston",
            "ru": "Индия",
            "en": "India"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Mahatma-Gandhi%2C_studio%2C_1931.jpg/640px-Mahatma-Gandhi%2C_studio%2C_1931.jpg",
        "aliases": [
            "mahatma gandi",
            "gandi",
            "gandhi",
            "махатма ганди",
            "ганди",
            "mohandas gandhi"
        ],
        "fun_fact": {
            "uz": "Zo'ravonliksiz qarshilik (Satyagraxa) falsafasi orqali dunyodagi eng qudratli Britaniya imperiyasidan Hindiston mustaqilligini qo'lga kiritgan.",
            "ru": "Добился независимости Индии от Британской империи исключительно мирными протестами и бойкотами (Сатьяграха).",
            "en": "Employed nonviolent resistance to lead India to independence, inspiring civil rights movements across the globe."
        }
    },
    {
        "id": "martin_lyuter_king",
        "name": {
            "uz": "Martin Lyuter King (kichik)",
            "ru": "Мартин Лютер Кинг",
            "en": "Martin Luther King Jr."
        },
        "era": {
            "uz": "XX asr (1950–1960-yillar)",
            "ru": "XX век",
            "en": "20th century"
        },
        "field": {
            "uz": "Fuqarolik huquqlari himoyachisi, 'I Have a Dream' nutqi muallifi, Nobel sohibi",
            "ru": "Лидер движения за гражданские права чернокожих в США",
            "en": "Civil rights leader, author of 'I Have a Dream', Nobel Peace Prize laureate"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Martin_Luther_King%2C_Jr._and_Lyndon_Johnson_%28cropped%29.jpg/640px-Martin_Luther_King%2C_Jr._and_Lyndon_Johnson_%28cropped%29.jpg",
        "aliases": [
            "martin lyuter king",
            "martin luther king",
            "king",
            "мартин лютер кинг",
            "mlk"
        ],
        "fun_fact": {
            "uz": "1963-yilda Vashingtonda 'Mening orzuim bor' (I Have a Dream) tarixiy nutqini so'zlagan va 35 yoshida eng yosh Nobel Tinchlik mukofoti sohibi bo'lgan.",
            "ru": "Произнес бессмертную речь «У меня есть мечта» в 1963 году и добился отмены расовой сегрегации в США.",
            "en": "Delivered the historic 1963 'I Have a Dream' speech at the Lincoln Memorial and won the Nobel Peace Prize at age 35."
        }
    },
    {
        "id": "ona_tereza",
        "name": {
            "uz": "Ona Tereza (Avliyo Tereza)",
            "ru": "Мать Тереза",
            "en": "Mother Teresa"
        },
        "era": {
            "uz": "XX asr",
            "ru": "XX век",
            "en": "20th century"
        },
        "field": {
            "uz": "Insonparvarlik timsoli, xalqaro xayriya ordeni asoschisi, Nobel mukofoti sohibi",
            "ru": "Католическая монахиня, лауреат Нобелевской премии мира, символ милосердия",
            "en": "Humanitarian, Catholic nun, founder of Missionaries of Charity, Nobel laureate"
        },
        "country": {
            "uz": "Shimoliy Makedoniya / Hindiston",
            "ru": "Индия / Северная Македония",
            "en": "India / North Macedonia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Mother_Teresa_1.jpg/640px-Mother_Teresa_1.jpg",
        "aliases": [
            "ona tereza",
            "mother teresa",
            "мать тереза",
            "тереза она"
        ],
        "fun_fact": {
            "uz": "Kalkuttada umidsiz va og'ir kasal insonlarga butun umrini bag'ishlab, 1979-yilda Nobel Tinchlik mukofotiga sazovor bo'lgan.",
            "ru": "Посвятила жизнь служению бедным и умирающим в Калькутте, основав монашескую конгрегацию в 130 странах мира.",
            "en": "Devoted 45 years to caring for the poor and dying in Kolkata; awarded the 1979 Nobel Peace Prize and canonized as a saint."
        }
    },
    {
        "id": "sokrat",
        "name": {
            "uz": "Sokrat",
            "ru": "Сократ",
            "en": "Socrates"
        },
        "era": {
            "uz": "Miloddan avvalgi V asr (Klassik Gretsiya)",
            "ru": "V век до н.э.",
            "en": "5th century BC (Classical Greece)"
        },
        "field": {
            "uz": "G'arb falsafasining asoschisi, etika va dialektika dahosi",
            "ru": "Основатель западной философии, создатель метода сократического диалога",
            "en": "Founder of Western philosophy, Socratic method"
        },
        "country": {
            "uz": "Qadimgi Afina / Gretsiya",
            "ru": "Древние Афины / Греция",
            "en": "Ancient Athens / Greece"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Socrates_Louvre.jpg/640px-Socrates_Louvre.jpg",
        "aliases": [
            "sokrat",
            "socrates",
            "сократ"
        ],
        "fun_fact": {
            "uz": "O'zidan hech qanday yozma meros qoldirmagan ('Men bilamanki, hech narsani bilmayman'); ta'limotini shogirdi Platon yozib qoldirgan.",
            "ru": "Не оставил ни строчки сочинений («Я знаю, что ничего не знаю»), его учение известно благодаря диалогам Платона.",
            "en": "Wrote nothing down, famously declaring 'I know that I know nothing'; his ideas were recorded by Plato and Xenophon."
        }
    },
    {
        "id": "platon",
        "name": {
            "uz": "Platon (Aflotun)",
            "ru": "Платон",
            "en": "Plato"
        },
        "era": {
            "uz": "Miloddan avvalgi V–IV asrlar",
            "ru": "V–IV века до н.э.",
            "en": "5th–4th century BC"
        },
        "field": {
            "uz": "Afina akademiyasi asoschisi, idealistik falsafa dahosi, 'Davlat' asari muallifi",
            "ru": "Философ, основатель Академии в Афинах, автор «Государства»",
            "en": "Philosopher, founder of the Academy, author of The Republic"
        },
        "country": {
            "uz": "Qadimgi Afina / Gretsiya",
            "ru": "Древние Афины / Греция",
            "en": "Ancient Athens / Greece"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Plato_Silanion_Musei_Capitolini_MC1377.png/640px-Plato_Silanion_Musei_Capitolini_MC1377.png",
        "aliases": [
            "platon",
            "aflotun",
            "plato",
            "платон"
        ],
        "fun_fact": {
            "uz": "G'arb dunyosidagi ilk oliy ta'lim maskani — mashhur Afina akademiyasiga asos solgan va g'oyalar olami ta'limotini yaratgan.",
            "ru": "Основал первую в западном мире Академию, где учился Аристотель, автор теории идей и мифа о пещере.",
            "en": "Founded the Academy in Athens, the Western world's first institution of higher learning, and wrote The Republic."
        }
    },
    {
        "id": "aristotel",
        "name": {
            "uz": "Aristotel (Arastu)",
            "ru": "Аристотель",
            "en": "Aristotle"
        },
        "era": {
            "uz": "Miloddan avvalgi IV asr",
            "ru": "IV век до н.э.",
            "en": "4th century BC"
        },
        "field": {
            "uz": "'Birinchi muallim', mantiq fani asoschisi, qomusiy donishmand",
            "ru": "«Первый учитель», основоположник формальной логики и естествознания",
            "en": "'The First Teacher', polymath, father of formal logic and biology"
        },
        "country": {
            "uz": "Qadimgi Gretsiya / Makedoniya",
            "ru": "Древняя Греция",
            "en": "Ancient Greece"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Aristotle_Altemps_Inv8575.jpg/640px-Aristotle_Altemps_Inv8575.jpg",
        "aliases": [
            "aristotel",
            "arastu",
            "aristotle",
            "аристотель"
        ],
        "fun_fact": {
            "uz": "Sharqda 'Muallimi avval' (Birinchi o'qituvchi) deb ulug'langan, Aleksandr Makedonskiyga ustozlik qilgan va mantiq fanini yaratgan.",
            "ru": "Был наставником Александра Македонского, заложил основы логики, физики, биологии, этики и политики.",
            "en": "Tutor to Alexander the Great; his encyclopedic works laid the foundations of logic, physics, biology, and politics for millennia."
        }
    },
    {
        "id": "konfutsiy",
        "name": {
            "uz": "Konfutsiy (Kun-szi)",
            "ru": "Конфуций",
            "en": "Confucius"
        },
        "era": {
            "uz": "Miloddan avvalgi VI–V asrlar",
            "ru": "VI–V века до н.э.",
            "en": "6th–5th century BC"
        },
        "field": {
            "uz": "Xitoyning buyuk mutafakkiri, Konfutsiychilik ta'limoti asoschisi",
            "ru": "Философ, основатель конфуцианства, морально-этический учитель Китая",
            "en": "Philosopher, politician, founder of Confucianism"
        },
        "country": {
            "uz": "Qadimgi Xitoy (Lu podsholigi)",
            "ru": "Древний Китай",
            "en": "Ancient China (Lu state)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Confucius%2C_fresco_from_a_Western_Han_tomb_of_Dongping_County%2C_Shandong_province%2C_China_%28cropped%29.jpg/640px-Confucius%2C_fresco_from_a_Western_Han_tomb_of_Dongping_County%2C_Shandong_province%2C_China_%28cropped%29.jpg",
        "aliases": [
            "konfutsiy",
            "confucius",
            "конфуций",
            "kun-szi",
            "kong fuzi"
        ],
        "fun_fact": {
            "uz": "'O'zingga ravo ko'rmagan narsani boshqalarga ham qilma' oltin qoidasini shakllantirgan va Sharqiy Osiyo tamaddunining axloqiy poydevorini qurgan.",
            "ru": "Сформулировал золотое правило этики («Не делай человеку того, чего не желаешь себе»), определившее культуру Восточной Азии.",
            "en": "Championed family loyalty, ancestor veneration, and the Golden Rule: 'Do not do to others what you do not want done to yourself'."
        }
    },
    {
        "id": "lao_szi",
        "name": {
            "uz": "Lao Szi",
            "ru": "Лао-цзы",
            "en": "Laozi (Lao Tzu)"
        },
        "era": {
            "uz": "Miloddan avvalgi VI asr",
            "ru": "VI век до н.э.",
            "en": "6th century BC"
        },
        "field": {
            "uz": "Daosizm falsafasi asoschisi, 'Dao de szin' asari muallifi",
            "ru": "Основатель даосизма, автор канона «Дао Дэ Цзин»",
            "en": "Founder of Taoism, author of the Tao Te Ching"
        },
        "country": {
            "uz": "Qadimgi Xitoy",
            "ru": "Древний Китай",
            "en": "Ancient China"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Laozi_%28Chinese_characters%29.svg/640px-Laozi_%28Chinese_characters%29.svg.png",
        "aliases": [
            "lao szi",
            "lao-szi",
            "laozi",
            "lao tzu",
            "лао-цзы",
            "лао цзы"
        ],
        "fun_fact": {
            "uz": "U-vey (tabiiy harakatsizlik va uyg'unlik) konsepsiyasini yaratgan; 'Ming chaqirimlik yo'l birinchi qadamdan boshlanadi' hikmatining muallifi.",
            "ru": "Автор мудрости: «Путь в тысячу ли начинается с первого шага», основатель концепции недеяния (У-вэй).",
            "en": "Author of the Daoist foundational classic Tao Te Ching and the immortal proverb: 'A journey of a thousand miles begins with a single step'."
        }
    },
    {
        "id": "sun_szi",
        "name": {
            "uz": "Sun Szi",
            "ru": "Сунь-цзы",
            "en": "Sun Tzu"
        },
        "era": {
            "uz": "Miloddan avvalgi V asr",
            "ru": "V век до н.э.",
            "en": "5th century BC"
        },
        "field": {
            "uz": "Harbiy strategiya dahosi, 'Urush san'ati' asari muallifi",
            "ru": "Военный стратег и философ, автор трактата «Искусство войны»",
            "en": "Military general, strategist, author of The Art of War"
        },
        "country": {
            "uz": "Qadimgi Xitoy (U podsholigi)",
            "ru": "Древний Китай",
            "en": "Ancient China (Wu state)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/cf/%E5%90%B4%E5%8F%B8%E9%A9%AC%E5%AD%99%E6%AD%A6.jpg",
        "aliases": [
            "sun szi",
            "sun tzu",
            "сунь-цзы",
            "сунь цзы",
            "sunzi"
        ],
        "fun_fact": {
            "uz": "'Urush san'atining oliy cho'qqisi — dushmanga qarshi jang qilmasdan g'alaba qozonishdir' degan eng mashhur harbiy qoidani yozgan.",
            "ru": "Его книга «Искусство войны» остается главным мировым бестселлером по стратегии в военном деле и бизнесе.",
            "en": "Authored 'The Art of War', declaring that 'the supreme art of war is to subdue the enemy without fighting'."
        }
    },
    {
        "id": "rene_dekart",
        "name": {
            "uz": "Rene Dekart",
            "ru": "Рене Декарт",
            "en": "René Descartes"
        },
        "era": {
            "uz": "XVII asr",
            "ru": "XVII век",
            "en": "17th century"
        },
        "field": {
            "uz": "Zamonaviy falsafa va ratsionalizm otasi, koordinatalar tizimini yaratgan matematik",
            "ru": "Основатель философии Нового времени, создатель декартовой системы координат",
            "en": "Father of modern Western philosophy and Cartesian coordinate system"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg/640px-Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg",
        "aliases": [
            "rene dekart",
            "dekart",
            "descartes",
            "декарт",
            "рене декарт"
        ],
        "fun_fact": {
            "uz": "'Fikr qilyapmanmi, demak mavjudman' (Cogito, ergo sum) tamoyilini va maktablarda o'qitiladigan koordinatalar tekisligini yaratgan.",
            "ru": "Автор бессмертного афоризма «Мыслю, следовательно, существую» (Cogito ergo sum) и декартовых координат.",
            "en": "Coined the bedrock rationalist proposition 'Cogito, ergo sum' ('I think, therefore I am') and invented Cartesian geometry."
        }
    },
    {
        "id": "immanuil_kant",
        "name": {
            "uz": "Immanuil Kant",
            "ru": "Иммануил Кант",
            "en": "Immanuel Kant"
        },
        "era": {
            "uz": "XVIII asr (Ma'rifatparvarlik)",
            "ru": "XVIII век (Просвещение)",
            "en": "18th century (Enlightenment)"
        },
        "field": {
            "uz": "Klassik nemis falsafasi asoschisi, 'Sof aql tanqidi' muallifi",
            "ru": "Основоположник немецкой классической философии, автор «Критики чистого разума»",
            "en": "Central Enlightenment philosopher, author of Critique of Pure Reason"
        },
        "country": {
            "uz": "Prussiya / Germaniya",
            "ru": "Кёнигсберг / Германия",
            "en": "Prussia / Germany"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Immanuel_Kant_-_Gemaelde_1.jpg/640px-Immanuel_Kant_-_Gemaelde_1.jpg",
        "aliases": [
            "immanuil kant",
            "kant",
            "кант",
            "иммануил кант"
        ],
        "fun_fact": {
            "uz": "Hayoti davomida o'z shahri Kenigsbergdan 15 km dan ortiq uzoqqa chiqmagan, ammo olamshumul 'Kategorik imperativ' axloq qoidasini yaratgan.",
            "ru": "Никогда не покидал родной Кёнигсберг, сформулировал знаменитый категорический императив морали.",
            "en": "Never traveled more than 10 miles from Königsberg, yet revolutionized epistemology and moral philosophy via the Categorical Imperative."
        }
    },
    {
        "id": "karl_marks",
        "name": {
            "uz": "Karl Marks",
            "ru": "Карл Маркс",
            "en": "Karl Marx"
        },
        "era": {
            "uz": "XIX asr",
            "ru": "XIX век",
            "en": "19th century"
        },
        "field": {
            "uz": "Marksizm asoschisi, iqtisodchi, faylasuf, 'Kapital' muallifi",
            "ru": "Философ, экономист, автор «Капитала» и «Манифеста компартии»",
            "en": "Philosopher, political economist, author of Das Kapital and The Communist Manifesto"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Germany"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Karl_Marx_by_John_Jabez_Edwin_Mayall_1875_-_Restored.png/640px-Karl_Marx_by_John_Jabez_Edwin_Mayall_1875_-_Restored.png",
        "aliases": [
            "karl marks",
            "marks",
            "marx",
            "маркс",
            "карл маркс"
        ],
        "fun_fact": {
            "uz": "Uning 'Kapital' asari va iqtisodiy sinfiy kurash nazariyasi XX asr davomida dunyo siyosatini butunlay o'zgartirib yubordi.",
            "ru": "Автор «Капитала», чьи экономические и социально-политические идеи определили историю всего XX века.",
            "en": "Authored Das Kapital; his theories on capital, labour, and historical materialism profoundly shaped the course of the 20th century."
        }
    },
    {
        "id": "jaloliddin_rumiy",
        "name": {
            "uz": "Mavlono Jaloliddin Rumiy",
            "ru": "Джалаладдин Руми",
            "en": "Jalal al-Din Muhammad Rumi"
        },
        "era": {
            "uz": "XIII asr",
            "ru": "XIII век",
            "en": "13th century"
        },
        "field": {
            "uz": "Buyuk so'fiy shoir, mutafakkir, 'Masnaviyi ma'naviy' muallifi",
            "ru": "Великий персидский поэт-суфий, автор «Маснави»",
            "en": "Sufi mystic, poet of divine love, author of the Masnavi"
        },
        "country": {
            "uz": "Balx / Qunyo / Saljuqiylar",
            "ru": "Балх / Конья",
            "en": "Balkh / Konya (Seljuk Sultanate)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/%D9%85%D9%88%D9%84%D8%A7%D9%86%D8%A7_%D8%A7%D8%AB%D8%B1_%D8%AD%D8%B3%DB%8C%D9%86_%D8%A8%D9%87%D8%B2%D8%A7%D8%AF_%28cropped%29.jpg/640px-%D9%85%D9%88%D9%84%D8%A7%D9%86%D8%A7_%D8%A7%D8%AB%D8%B1_%D8%AD%D8%B3%DB%8C%D9%86_%D8%A8%D9%87%D8%B2%D8%A7%D8%AF_%28cropped%29.jpg",
        "aliases": [
            "rumiy",
            "jaloliddin rumiy",
            "mavlono rumiy",
            "rumi",
            "руми",
            "джалаладдин руми"
        ],
        "fun_fact": {
            "uz": "'Masnaviy' asari butun insoniyatni mehr-muhabbat va bag'rikenglikka chorlaydi; bugungi kunda ham AQSH va Yevropada eng ko'p o'qiladigan shoir.",
            "ru": "Автор грандиозной поэмы «Маснави», сегодня является одним из самых читаемых поэтов в мире, символом универсальной любви.",
            "en": "His 26,000-verse spiritual masterpiece 'Masnavi' transcended cultures, making him one of the best-selling poets worldwide today."
        }
    },
    {
        "id": "albert_eynshteyn",
        "name": {
            "uz": "Albert Eynshteyn",
            "ru": "Альберт Эйнштейн",
            "en": "Albert Einstein"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "Nisbiylik nazariyasi asoschisi, zamonaviy fizika dahosi, Nobel sohibi",
            "ru": "Создатель теории относительности, нобелевский лауреат по физике",
            "en": "Theoretical physicist, developer of theory of relativity, Nobel laureate"
        },
        "country": {
            "uz": "Germaniya / Shveytsariya / AQSH",
            "ru": "Германия / США",
            "en": "Germany / Switzerland / United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Albert_Einstein_Head_cleaned.jpg/640px-Albert_Einstein_Head_cleaned.jpg",
        "aliases": [
            "albert eynshteyn",
            "eynshteyn",
            "einstein",
            "эйнштейн",
            "альберт эйнштейн"
        ],
        "fun_fact": {
            "uz": "E=mc² mashhur formulasini yaratgan va fotoeffekt qonunini kashf etgani uchun 1921-yilda fizika bo'yicha Nobel mukofotini olgan.",
            "ru": "Сформулировал легендарную формулу E=mc² и совершил революцию в понимании пространства и времени.",
            "en": "Formulated the equation E=mc² and received the 1921 Nobel Prize in Physics for his discovery of the law of the photoelectric effect."
        }
    },
    {
        "id": "isaak_nyuton",
        "name": {
            "uz": "Isaak Nyuton",
            "ru": "Исаак Ньютон",
            "en": "Isaac Newton"
        },
        "era": {
            "uz": "XVII–XVIII asrlar",
            "ru": "XVII–XVIII века",
            "en": "17th–18th century"
        },
        "field": {
            "uz": "Klassik mexanika va gravitatsiya qonuni asoschisi, fizik va matematik",
            "ru": "Создатель классической механики, закона всемирного тяготения и дифференциального исчисления",
            "en": "Physicist, mathematician, discoverer of gravity and laws of motion"
        },
        "country": {
            "uz": "Angliya",
            "ru": "Англия",
            "en": "England"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Portrait_of_Sir_Isaac_Newton%2C_1689_%28brightened%29.jpg/640px-Portrait_of_Sir_Isaac_Newton%2C_1689_%28brightened%29.jpg",
        "aliases": [
            "isaak nyuton",
            "nyuton",
            "newton",
            "ньютон",
            "исаак ньютон"
        ],
        "fun_fact": {
            "uz": "Uning boshiga olma tushishi haqidagi rivoyat butun olam tortishish qonunining ramziga aylangan; 'Tabiat falsafasining matematik asoslari' kitobini yozgan.",
            "ru": "Открыл закон всемирного тяготения и три закона движения, заложив фундамент всей классической физики.",
            "en": "Published Principia Mathematica (1687), formulating the laws of motion and universal gravitation that dominated physics for centuries."
        }
    },
    {
        "id": "galiley_galiley",
        "name": {
            "uz": "Galiley Galiley",
            "ru": "Галилео Галилей",
            "en": "Galileo Galilei"
        },
        "era": {
            "uz": "XVI–XVII asrlar",
            "ru": "XVI–XVII века",
            "en": "16th–17th century"
        },
        "field": {
            "uz": "Zamonaviy astronomiya va fizika otasi, teleskopni kashf etgan olim",
            "ru": "Отец наблюдательной астрономии и современной физики",
            "en": "Astronomer, physicist, polymath, father of observational astronomy"
        },
        "country": {
            "uz": "Italiya (Florensiya)",
            "ru": "Италия",
            "en": "Italy"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Galileo_Galilei_%281564-1642%29_RMG_BHC2700.tiff/lossy-page1-330px-Galileo_Galilei_%281564-1642%29_RMG_BHC2700.tiff.jpg",
        "aliases": [
            "galiley galiley",
            "galiley",
            "galileo",
            "галилей",
            "галилео галилей"
        ],
        "fun_fact": {
            "uz": "Yupiterning to'rtta eng yirik yo'ldoshini teleskop orqali kashf etgan va Yer Quyosh atrofida aylanishini isbotlagan ('Baribir u aylanadi!').",
            "ru": "Открыл спутники Юпитера и фазы Венеры; защищал гелиоцентрическую систему («И все-таки она вертится!»).",
            "en": "Pioneered the telescope for astronomy, discovering Jupiter's four largest moons and championing Copernican heliocentrism."
        }
    },
    {
        "id": "nikolay_kopernik",
        "name": {
            "uz": "Nikolay Kopernik",
            "ru": "Николай Коперник",
            "en": "Nicolaus Copernicus"
        },
        "era": {
            "uz": "XV–XVI asrlar",
            "ru": "XV–XVI века",
            "en": "15th–16th century"
        },
        "field": {
            "uz": "Geliotsentrik nazariya (Quyosh markazda) asoschisi, astronom",
            "ru": "Астроном, создатель гелиоцентрической системы мира",
            "en": "Astronomer who formulated heliocentric model of the solar system"
        },
        "country": {
            "uz": "Polsha",
            "ru": "Польша",
            "en": "Poland"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Nikolaus_Kopernikus_MOT.jpg/640px-Nikolaus_Kopernikus_MOT.jpg",
        "aliases": [
            "nikolay kopernik",
            "kopernik",
            "copernicus",
            "коперник",
            "николай коперник"
        ],
        "fun_fact": {
            "uz": "Yer koinot markazi degan ming yillik tushunchani inkor etib, Yer va boshqa sayyoralar Quyosh atrofida aylanishini ilmiy isbotlagan.",
            "ru": "Совершил коперниканскую революцию, доказав, что Земля и другие планеты вращаются вокруг Солнца.",
            "en": "Initiated the Scientific Revolution by proposing that the Sun, rather than Earth, was at the center of the universe."
        }
    },
    {
        "id": "charlz_darvin",
        "name": {
            "uz": "Charlz Darvin",
            "ru": "Чарльз Дарвин",
            "en": "Charles Darwin"
        },
        "era": {
            "uz": "XIX asr",
            "ru": "XIX век",
            "en": "19th century"
        },
        "field": {
            "uz": "Evolutsiya nazariyasi asoschisi, biolog, 'Turlarning kelib chiqishi' muallifi",
            "ru": "Создатель эволюционной теории, биолог и натуралист",
            "en": "Naturalist, geologist, biologist, architect of the theory of evolution"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Charles_Darwin_seated_crop.jpg/640px-Charles_Darwin_seated_crop.jpg",
        "aliases": [
            "charlz darvin",
            "darvin",
            "darwin",
            "дарвин",
            "чарльз дарвин"
        ],
        "fun_fact": {
            "uz": "'Bigl' kemasidagi 5 yillik jahon sayohati asosida tabiiy tanlanish orqali turlarning evolutsiyasi qonunini kashf etgan.",
            "ru": "Обосновал теорию естественного отбора на основе пятилетнего кругосветного плавания на корабле «Бигль».",
            "en": "Circumnavigated the globe aboard HMS Beagle, gathering observations that formed his landmark 1859 work 'On the Origin of Species'."
        }
    },
    {
        "id": "nikola_tesla",
        "name": {
            "uz": "Nikola Tesla",
            "ru": "Никола Тесла",
            "en": "Nikola Tesla"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "O'zgaruvchan tok (AC) tizimi ixtirochisi, elektrotexnika dahosi",
            "ru": "Изобретатель переменного тока, радиосвязи и электродвигателя",
            "en": "Inventor, electrical engineer, pioneer of alternating current (AC)"
        },
        "country": {
            "uz": "Serbiya / AQSH",
            "ru": "Сербия / США",
            "en": "Serbia / United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Tesla_circa_1890.jpeg/640px-Tesla_circa_1890.jpeg",
        "aliases": [
            "nikola tesla",
            "tesla",
            "тесла",
            "никола тесла"
        ],
        "fun_fact": {
            "uz": "O'zgaruvchan tok, radioto'lqinlar, simsiz energiya uzatish va induksion motorni kashf etib, zamonaviy dunyo elektr ta'minotiga poydevor qo'ygan.",
            "ru": "Создал систему переменного тока, питающую современный мир, электродвигатель и радиоуправление.",
            "en": "Patented the AC induction motor and polyphase transmission system, defeating Edison's direct current in the 'War of the Currents'."
        }
    },
    {
        "id": "tomas_edison",
        "name": {
            "uz": "Tomas Edison",
            "ru": "Томас Эдисон",
            "en": "Thomas Edison"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "Buyuk ixtirochi va tadbirkor, General Electric asoschisi",
            "ru": "Изобретатель и бизнесмен, основатель General Electric",
            "en": "Inventor and industrialist, held 1,093 US patents"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Thomas_Edison2.jpg/640px-Thomas_Edison2.jpg",
        "aliases": [
            "tomas edison",
            "edison",
            "эдисон",
            "томас эдисон"
        ],
        "fun_fact": {
            "uz": "Hayoti davomida 1093 ta patent olgan va birinchi bo'lib amaliy elektr lampasi hamda ovoz yozuvchi fonografni yaratgan.",
            "ru": "Получил более 1000 патентов, создал первую звукозапись на фонографе и коммерческую лампу накаливания.",
            "en": "Averaged a patent every 10–12 days during his prime, pioneering industrial research labs and the phonograph."
        }
    },
    {
        "id": "mariya_kyuri",
        "name": {
            "uz": "Mariya Sklodovskaya-Kyuri",
            "ru": "Мария Склодовская-Кюри",
            "en": "Marie Curie"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "Radioaktivlik kashfiyotchisi, poloniy va radiy elementlarini topgan olima",
            "ru": "Физик и химик, первооткрыватель полония и радия, дважды лауреат Нобеля",
            "en": "Physicist and chemist, pioneer in radioactivity, two-time Nobel laureate"
        },
        "country": {
            "uz": "Polsha / Fransiya",
            "ru": "Польша / Франция",
            "en": "Poland / France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Marie_Curie_c._1920s.jpg/640px-Marie_Curie_c._1920s.jpg",
        "aliases": [
            "mariya kyuri",
            "marie curie",
            "kyuri",
            "мария кюри",
            "кюри",
            "sklodovskaya-kyuri"
        ],
        "fun_fact": {
            "uz": "Dunyo tarixida ikkita turli fan sohasi (Fizika va Kimyo) bo'yicha Nobel mukofotini olgan yagona inson.",
            "ru": "Единственная женщина в истории, удостоенная двух Нобелевских премий в двух разных научных областях — физике и химии.",
            "en": "The first woman to win a Nobel Prize and the only person to win Nobel Prizes in two different scientific fields (Physics and Chemistry)."
        }
    },
    {
        "id": "dmitriy_mendeleyev",
        "name": {
            "uz": "Dmitriy Mendeleyev",
            "ru": "Дмитрий Менделеев",
            "en": "Dmitri Mendeleev"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "Kimyoviy elementlar davriy jadvali asoschisi, kimyogar va qomusiy olim",
            "ru": "Создатель Периодической таблицы химических элементов",
            "en": "Chemist, creator of the Periodic Table of Chemical Elements"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Dmitri_Mendeleev.jpg/640px-Dmitri_Mendeleev.jpg",
        "aliases": [
            "dmitriy mendeleyev",
            "mendeleyev",
            "mendeleev",
            "менделеев",
            "дмитрий менделеев"
        ],
        "fun_fact": {
            "uz": "Kimyoviy elementlar davriy qonunini yaratib, o'sha paytda hali kashf etilmagan elementlarning xossalarini oldindan aytib bergan.",
            "ru": "Открыл Периодический закон и с абсолютной точностью предсказал свойства еще не открытых тогда химических элементов.",
            "en": "Formulated the Periodic Law and used it to accurately predict the properties of elements that were yet to be discovered."
        }
    },
    {
        "id": "lui_paster",
        "name": {
            "uz": "Lui Paster",
            "ru": "Луи Пастер",
            "en": "Louis Pasteur"
        },
        "era": {
            "uz": "XIX asr",
            "ru": "XIX век",
            "en": "19th century"
        },
        "field": {
            "uz": "Mikrobiologiya otasi, pasterizatsiya va quturishga qarshi vaksina ixtirochisi",
            "ru": "Основоположник микробиологии, создатель вакцин против бешенства и пастеризации",
            "en": "Microbiologist, chemist, invented pasteurization and rabies vaccine"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Louis_Pasteur%2C_foto_av_Paul_Nadar%2C_Crisco_edit.jpg/640px-Louis_Pasteur%2C_foto_av_Paul_Nadar%2C_Crisco_edit.jpg",
        "aliases": [
            "lui paster",
            "paster",
            "louis pasteur",
            "пастер",
            "луи пастер"
        ],
        "fun_fact": {
            "uz": "Kasalliklarning mikroblar tufayli kelib chiqishini isbotlagan, oziq-ovqatlarni zararsizlantirish (pasterizatsiya) va vaksinalarni yaratgan.",
            "ru": "Доказал микробную природу инфекций, создал вакцины от сибирской язвы и бешенства, спас миллионы жизней.",
            "en": "Revolutionized medicine by proving germ theory, developing pasteurization, and creating the first rabies and anthrax vaccines."
        }
    },
    {
        "id": "aleksandr_fleming",
        "name": {
            "uz": "Aleksandr Fleming",
            "ru": "Александр Флеминг",
            "en": "Alexander Fleming"
        },
        "era": {
            "uz": "XX asr",
            "ru": "XX век",
            "en": "20th century"
        },
        "field": {
            "uz": "Penitsillin (birinchi antibiotik) kashfiyotchisi, Nobel mukofoti sohibi",
            "ru": "Первооткрыватель пенициллина — первого в мире антибиотика",
            "en": "Biologist, pharmacologist, discoverer of penicillin"
        },
        "country": {
            "uz": "Shotlandiya / Buyuk Britaniya",
            "ru": "Шотландия / Великобритания",
            "en": "Scotland / United Kingdom"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Synthetic_Production_of_Penicillin_TR1468.jpg/640px-Synthetic_Production_of_Penicillin_TR1468.jpg",
        "aliases": [
            "aleksandr fleming",
            "fleming",
            "флеминг",
            "александр флеминг",
            "alexander fleming"
        ],
        "fun_fact": {
            "uz": "1928-yilda tasodifan mog'or zamburug'i bakteriyalarni yo'q qilayotganini payqab, millionlab insonlar hayotini saqlab qolgan penitsillinni kashf etgan.",
            "ru": "Случайно открыл пенициллин, заметив плесень, убивающую бактерии в чашке Петри, что спасло свыше 200 млн жизней.",
            "en": "Serendipitously discovered penicillin in 1928 when mold contaminated a Petri dish, sparking the antibiotic revolution."
        }
    },
    {
        "id": "alan_tyuring",
        "name": {
            "uz": "Alan Tyuring",
            "ru": "Алан Тьюринг",
            "en": "Alan Turing"
        },
        "era": {
            "uz": "XX asr",
            "ru": "XX век",
            "en": "20th century"
        },
        "field": {
            "uz": "Zamonaviy kompyuter va sun'iy intellekt otasi, 'Enigma' shifrini buzgan matematik",
            "ru": "Отец теоретической информатики и искусственного интеллекта, взломал «Энигму»",
            "en": "Father of computer science and artificial intelligence, cracked Enigma"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Alan_turing_header.jpg/640px-Alan_turing_header.jpg",
        "aliases": [
            "alan tyuring",
            "tyuring",
            "turing",
            "тьюринг",
            "алан тьюринг",
            "alan turing"
        ],
        "fun_fact": {
            "uz": "Ikkinchi jahon urushida natsistlarning 'Enigma' shifrini buzib, urushni 2 yilga qisqartirgan va Tyuring mashinasi konsepsiyasini yaratgan.",
            "ru": "Взломал нацистский шифратор «Энигма», приблизив победу во Второй мировой, создал тест Тьюринга для проверки ИИ.",
            "en": "Cracked the Nazi Enigma naval ciphers at Bletchley Park and formulated the concept of universal computing (Turing Machine)."
        }
    },
    {
        "id": "stiven_xoking",
        "name": {
            "uz": "Stiven Xoking",
            "ru": "Стивен Хокинг",
            "en": "Stephen Hawking"
        },
        "era": {
            "uz": "XX–XXI asrlar",
            "ru": "XX–XXI века",
            "en": "20th–21st century"
        },
        "field": {
            "uz": "Nazariy fizik, qora tuynuklar va kosmologiya tadqiqotchisi",
            "ru": "Физик-теоретик, исследователь черных дыр и автор «Краткой истории времени»",
            "en": "Theoretical physicist, cosmologist, author of A Brief History of Time"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Stephen_Hawking.StarChild.jpg",
        "aliases": [
            "stiven xoking",
            "xoking",
            "hawking",
            "хокинг",
            "стивен хокинг",
            "stephen hawking"
        ],
        "fun_fact": {
            "uz": "Og'ir kasallik tufayli to'liq falaj bo'lishiga qaramay, kompyuter nutqi orqali 'Koinotning qisqacha tarixi' xalqaro bestsellerini yozgan.",
            "ru": "Несмотря на полный паралич, сделал фундаментальные открытия в квантовой гравитации и написал мировой бестселлер.",
            "en": "Discovered Hawking radiation from black holes and wrote 'A Brief History of Time', communicating solely via a speech synthesizer."
        }
    },
    {
        "id": "arximed",
        "name": {
            "uz": "Arximed",
            "ru": "Архимед",
            "en": "Archimedes"
        },
        "era": {
            "uz": "Miloddan avvalgi III asr",
            "ru": "III век до н.э.",
            "en": "3rd century BC"
        },
        "field": {
            "uz": "Qadimgi dunyoning buyuk matematigi, fizigi, gidrostatika va richag qonunlari asoschisi",
            "ru": "Величайший математик и инженер древности, создатель гидростатики",
            "en": "Ancient Greek mathematician, physicist, engineer, discovered buoyancy"
        },
        "country": {
            "uz": "Qadimgi Gretsiya / Sirakuza",
            "ru": "Древняя Греция / Сиракузы",
            "en": "Ancient Greece / Syracuse"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Domenico-Fetti_Archimedes_1620.jpg/640px-Domenico-Fetti_Archimedes_1620.jpg",
        "aliases": [
            "arximed",
            "archimedes",
            "архимед",
            "evrika"
        ],
        "fun_fact": {
            "uz": "Vannada suvga tushganda jismlarning suvdan siqib chiqarilish qonunini kashf qilib, yalong'och holda 'Evrika!' (Topdim!) deb baqirib ko'chaga yugurgan.",
            "ru": "Открыл закон гидростатики в ванне с криком «Эврика!», создал боевые катапульты и зеркала для сожжения вражеского флота.",
            "en": "Discovered the principle of buoyancy (shouting 'Eureka!') and pioneered formulas for the volume of a sphere and parabolic segments."
        }
    },
    {
        "id": "yoxann_gutenberg",
        "name": {
            "uz": "Iogann Gutenberg",
            "ru": "Иоганн Гутенберг",
            "en": "Johannes Gutenberg"
        },
        "era": {
            "uz": "XV asr (Uyg'onish davri)",
            "ru": "XV век (Ренессанс)",
            "en": "15th century (Renaissance)"
        },
        "field": {
            "uz": "Kitob bosish dastgohi va qo'rg'oshin harflar ixtirochisi",
            "ru": "Изобретатель европейского книгопечатания подвижными литерами",
            "en": "Inventor of movable-type mechanical printing press"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Holy Roman Empire (Germany)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Mainz_Gutenbergdenkmal_2016_%28cropped%29.jpg/640px-Mainz_Gutenbergdenkmal_2016_%28cropped%29.jpg",
        "aliases": [
            "gutenberg",
            "iogann gutenberg",
            "johannes gutenberg",
            "гутенберг",
            "иоганн гутенберг"
        ],
        "fun_fact": {
            "uz": "1450-yillarda qo'zg'aluvchan metall harflar bilan kitob chop etishni kashf qilib, insoniyat tarixida axborot inqilobiga asos solgan.",
            "ru": "Его изобретение книгопечатного пресса произвело величайшую революцию в распространении знаний в истории человечества.",
            "en": "Introduced mechanical movable type printing to Europe, triggering the Renaissance and the Scientific Revolution."
        }
    },
    {
        "id": "aleksandr_bell",
        "name": {
            "uz": "Aleksandr Bell",
            "ru": "Александр Грейам Белл",
            "en": "Alexander Graham Bell"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "Telefon ixtirochisi, aloqa texnologiyalari kashfiyotchisi",
            "ru": "Изобретатель первого коммерческого телефона",
            "en": "Inventor of the first practical telephone, co-founder of AT&T"
        },
        "country": {
            "uz": "Shotlandiya / AQSH",
            "ru": "Шотландия / США",
            "en": "Scotland / United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Alexander_Graham_Bell_1895_NPG_77_363.jpg/640px-Alexander_Graham_Bell_1895_NPG_77_363.jpg",
        "aliases": [
            "aleksandr bell",
            "bell",
            "alexander graham bell",
            "белл",
            "александр белл"
        ],
        "fun_fact": {
            "uz": "1876-yilda birinchi bo'lib telefonni patentlagan va 'Janob Uotson, bu yerga keling, siz menga keraksiz' degan ilk so'zlarni sim orqali uzatgan.",
            "ru": "Запатентовал телефон в 1876 году; первая фраза по телефону: «Мистер Ватсон, идите сюда, вы мне нужны».",
            "en": "Patented the first practical telephone in 1876 and co-founded American Telephone and Telegraph Company (AT&T)."
        }
    },
    {
        "id": "leonardo_da_vinchi",
        "name": {
            "uz": "Leonardo da Vinchi",
            "ru": "Леонардо да Винчи",
            "en": "Leonardo da Vinci"
        },
        "era": {
            "uz": "XV–XVI asrlar (Uyg'onish davri)",
            "ru": "XV–XVI века (Высокое Возрождение)",
            "en": "15th–16th century (High Renaissance)"
        },
        "field": {
            "uz": "Uyg'onish davri dahosi, 'Mona Liza' va 'So'nggi kechlik' rassomi, ixtirochi",
            "ru": "Художник, ученый, изобретатель, автор «Моны Лизы»",
            "en": "High Renaissance polymath, painter of Mona Lisa and The Last Supper, inventor"
        },
        "country": {
            "uz": "Italiya (Florensiya)",
            "ru": "Италия (Флоренция)",
            "en": "Italy (Florence)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Francesco_Melzi_-_Portrait_of_Leonardo_%28colour_correction%29.png/640px-Francesco_Melzi_-_Portrait_of_Leonardo_%28colour_correction%29.png",
        "aliases": [
            "leonardo da vinchi",
            "da vinchi",
            "leonardo",
            "leonardo da vinci",
            "леонардо да винчи",
            "да винчи"
        ],
        "fun_fact": {
            "uz": "'Mona Liza' va 'So'nggi kechlik' durdonalarini chizgan, vertolyot, parashyut va suv osti kemalarining ilk eskizlarini yaratgan.",
            "ru": "Написал «Мону Лизу» и «Тайную вечерю», опередил время, спроектировав прообразы вертолета, танка и парашюта.",
            "en": "Painted the Mona Lisa and The Last Supper while conceptualizing flying machines, armored vehicles, and concentrated solar power."
        }
    },
    {
        "id": "mikelandjelo",
        "name": {
            "uz": "Mikelandjelo Buonarroti",
            "ru": "Микеланджело Буонарроти",
            "en": "Michelangelo Buonarroti"
        },
        "era": {
            "uz": "XV–XVI asrlar (Uyg'onish davri)",
            "ru": "XV–XVI века (Ренессанс)",
            "en": "15th–16th century (Renaissance)"
        },
        "field": {
            "uz": "Buyuk haykaltarosh va rassom, 'Dovud' haykali va Sikstin kapellasi muallifi",
            "ru": "Скульптор, художник, автор статуи «Давид» и росписи Сикстинской капеллы",
            "en": "Sculptor, painter, architect, creator of David and Sistine Chapel ceiling"
        },
        "country": {
            "uz": "Italiya (Florensiya / Rim)",
            "ru": "Италия (Рим / Флоренция)",
            "en": "Italy (Florence / Rome)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Michelangelo_Daniele_da_Volterra_%28dettaglio%29.jpg/640px-Michelangelo_Daniele_da_Volterra_%28dettaglio%29.jpg",
        "aliases": [
            "mikelandjelo",
            "michelangelo",
            "микеланджело",
            "микеланджело буонарроти"
        ],
        "fun_fact": {
            "uz": "Rimda Sikstin kapellasi shiftini chalqancha yotgan holda 4 yil davomida yolg'iz o'zi chizgan va 5 metrlik 'Dovud' marmar haykalini yo'ngan.",
            "ru": "В одиночку расписал потолок Сикстинской капеллы площадью 500 кв. метров и изваял шедевр эпохи Возрождения — статую Давида.",
            "en": "Sculpted David and the Pietà before age thirty, then painted the 5,000-square-foot Sistine Chapel ceiling over four grueling years."
        }
    },
    {
        "id": "uilyam_shekspir",
        "name": {
            "uz": "Uilyam Shekspir",
            "ru": "Уильям Шекспир",
            "en": "William Shakespeare"
        },
        "era": {
            "uz": "XVI–XVII asrlar (Yelizaveta davri)",
            "ru": "XVI–XVII века",
            "en": "16th–17th century"
        },
        "field": {
            "uz": "Jahon dramaturgiyasi sultoni, 'Gamlet' va 'Romeo va Julyetta' muallifi",
            "ru": "Величайший англоязычный драматург, автор «Гамлета» и «Ромео и Джульетты»",
            "en": "Playwright, poet, author of Hamlet and Romeo and Juliet"
        },
        "country": {
            "uz": "Angliya",
            "ru": "Англия",
            "en": "England"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/William_Shakespeare_by_John_Taylor%2C_edited.jpg/640px-William_Shakespeare_by_John_Taylor%2C_edited.jpg",
        "aliases": [
            "uilyam shekspir",
            "shekspir",
            "shakespeare",
            "шекспир",
            "уильям шекспир"
        ],
        "fun_fact": {
            "uz": "Ingliz tiliga 1700 dan ortiq yangi so'zlarni kiritgan va uning pyesalari dunyoning har bir yirik tiliga tarjima qilingan.",
            "ru": "Обогатил английский язык более чем 1700 новыми словами, признан величайшим драматургом в истории человечества.",
            "en": "Widely regarded as the greatest writer in the English language, creating iconic tragedies including Hamlet, Othello, King Lear, and Macbeth."
        }
    },
    {
        "id": "aleksandr_pushkin",
        "name": {
            "uz": "Aleksandr Pushkin",
            "ru": "Александр Пушкин",
            "en": "Alexander Pushkin"
        },
        "era": {
            "uz": "XIX asr (Oltin asr)",
            "ru": "XIX век (Золотой век русской поэзии)",
            "en": "19th century (Golden Age of Russian Poetry)"
        },
        "field": {
            "uz": "Zamonaviy rus adabiy tili asoschisi, daho shoir va yozuvchi",
            "ru": "Основоположник современного русского литературного языка, поэт",
            "en": "Founder of modern Russian literature, poet, author of Eugene Onegin"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Orest_Kiprensky_-_%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%D0%BF%D0%BE%D1%8D%D1%82%D0%B0_%D0%90.%D0%A1.%D0%9F%D1%83%D1%88%D0%BA%D0%B8%D0%BD%D0%B0_-_Google_Art_Project.jpg/640px-Orest_Kiprensky_-_%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%D0%BF%D0%BE%D1%8D%D1%82%D0%B0_%D0%90.%D0%A1.%D0%9F%D1%83%D1%88%D0%BA%D0%B8%D0%BD%D0%B0_-_Google_Art_Project.jpg",
        "aliases": [
            "pushkin",
            "aleksandr pushkin",
            "пушкин",
            "александр пушкин"
        ],
        "fun_fact": {
            "uz": "'Yevgeniy Onegin', 'Kapitan qizi' asarlarini yozgan, rus adabiy tilini yangi cho'qqiga ko'targan va 37 yoshida dueldan vafot etgan.",
            "ru": "Создатель современного русского языка, автор романа в стихах «Евгений Онегин», трагически погиб на дуэли в 37 лет.",
            "en": "Considered Russia's greatest poet and the founder of modern Russian literature, tragically killed in a duel at age 37."
        }
    },
    {
        "id": "lev_tolstoy",
        "name": {
            "uz": "Lev Tolstoy",
            "ru": "Лев Толстой",
            "en": "Leo Tolstoy"
        },
        "era": {
            "uz": "XIX–XX asrlar",
            "ru": "XIX–XX века",
            "en": "19th–20th century"
        },
        "field": {
            "uz": "Jahon adabiyotining ulug' mutafakkiri, 'Urush va tinchlik' muallifi",
            "ru": "Великий писатель, мыслитель, автор «Войны и мира» и «Анны Карениной»",
            "en": "Master of realistic fiction, author of War and Peace and Anna Karenina"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Leo_Tolstoy_1908_Portrait_%283x4_cropped%29.jpg/640px-Leo_Tolstoy_1908_Portrait_%283x4_cropped%29.jpg",
        "aliases": [
            "lev tolstoy",
            "tolstoy",
            "толстой",
            "лев толстой",
            "leo tolstoy"
        ],
        "fun_fact": {
            "uz": "Uning 'Urush va tinchlik' hamda 'Anna Karenina' romanlari barcha davrlarning eng buyuk asarlari qatorida turadi; Gandi bilan yozishmalar olib borgan.",
            "ru": "Автор эпопеи «Война и мир», оказал огромное влияние на Махатму Ганди своей философией ненасильственного сопротивления злу.",
            "en": "Penned masterpieces 'War and Peace' and 'Anna Karenina'; his moral philosophy of nonviolent resistance directly inspired Mahatma Gandhi."
        }
    },
    {
        "id": "fyodor_dostoyevskiy",
        "name": {
            "uz": "Fyodor Dostoyevskiy",
            "ru": "Фёдор Достоевский",
            "en": "Fyodor Dostoevsky"
        },
        "era": {
            "uz": "XIX asr",
            "ru": "XIX век",
            "en": "19th century"
        },
        "field": {
            "uz": "Inson ruhiyati bilimdoni, 'Jinoyat va jazo' hamda 'Aka-uka Karamazovlar' muallifi",
            "ru": "Великий писатель-психолог, автор «Преступления и наказания»",
            "en": "Novelist, psychological explorer, author of Crime and Punishment"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Vasily_Perov_-_%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%D0%A4.%D0%9C.%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_-_Google_Art_Project.jpg/640px-Vasily_Perov_-_%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%D0%A4.%D0%9C.%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_-_Google_Art_Project.jpg",
        "aliases": [
            "dostoyevskiy",
            "fyodor dostoyevskiy",
            "достоевский",
            "федор достоевский",
            "dostoevsky"
        ],
        "fun_fact": {
            "uz": "O'lim jazosiga hukm qilinib, so'nggi daqiqalarda afv etilgan; inson ichki kechinmalarini chuqur tahlil qilgan eng buyuk psixologik adib.",
            "ru": "Пережил инсценировку смертной казни перед отправкой на каторгу, исследовал глубочайшие бездны человеческой души.",
            "en": "Survived a mock execution before a firing squad; explored human psychology, existentialism, and faith in Crime and Punishment."
        }
    },
    {
        "id": "volfgang_motsart",
        "name": {
            "uz": "Volfgang Amadey Motsart",
            "ru": "Вольфганг Амадей Моцарт",
            "en": "Wolfgang Amadeus Mozart"
        },
        "era": {
            "uz": "XVIII asr (Klassitsizm)",
            "ru": "XVIII век (Венский классицизм)",
            "en": "18th century (Classical era)"
        },
        "field": {
            "uz": "Musiqa dahosi, kompozitor, 600 dan ortiq simfoniya va operalar muallifi",
            "ru": "Музыкальный вундеркинд, классический композитор",
            "en": "Prolific classical composer, prodigy, author of 600+ musical masterworks"
        },
        "country": {
            "uz": "Avstriya (Zaltsburg / Vena)",
            "ru": "Австрия (Зальцбург / Вена)",
            "en": "Austria (Salzburg / Vienna)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/The_Mozart_Family_-_Wolfgang_Amadeus_Mozart_headshot.jpg/640px-The_Mozart_Family_-_Wolfgang_Amadeus_Mozart_headshot.jpg",
        "aliases": [
            "motsart",
            "volfgang motsart",
            "mozart",
            "моцарт",
            "вольфганг моцарт"
        ],
        "fun_fact": {
            "uz": "4 yoshidan fortepianoda ijro etgan, 5 yoshida ilk asarlarini yaratgan va atigi 35 yillik umrida 600 dan ortiq nodir durdonalar qoldirgan.",
            "ru": "Вундеркинд, сочинявший музыку с пяти лет, создал более 600 бессмертных произведений во всех музыкальных жанрах своего времени.",
            "en": "Child prodigy composing by age five; created over 600 works including masterpieces The Marriage of Figaro, Don Giovanni, and Requiem."
        }
    },
    {
        "id": "lyudvig_betxoven",
        "name": {
            "uz": "Lyudvig van Betxoven",
            "ru": "Людвиг ван Бетховен",
            "en": "Ludwig van Beethoven"
        },
        "era": {
            "uz": "XVIII–XIX asrlar",
            "ru": "XVIII–XIX века",
            "en": "18th–19th century"
        },
        "field": {
            "uz": "Buyuk kompozitor, 9-simfoniya ('Quvonch qasidasi') va 'Oy sonatasi' muallifi",
            "ru": "Великий композитор, автор 9-й симфонии и «Лунной сонаты»",
            "en": "Virtuoso pianist and composer, bridge between Classical and Romantic eras"
        },
        "country": {
            "uz": "Germaniya / Avstriya",
            "ru": "Германия / Австрия",
            "en": "Germany / Austria"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Beethoven.jpg/640px-Beethoven.jpg",
        "aliases": [
            "betxoven",
            "lyudvig betxoven",
            "beethoven",
            "бетховен",
            "людвиг ван бетховен"
        ],
        "fun_fact": {
            "uz": "Eshitish qobiliyatini butunlay yo'qotganidan keyin ham dunyoga mashhur 9-simfoniya va Yevropa Ittifoqi madhiyasi bo'lgan 'Quvonch qasidasi'ni yaratgan.",
            "ru": "Написал свою грандиозную Девятую симфонию («Ода к радости»), будучи абсолютно глухим.",
            "en": "Composed his triumphant Ninth Symphony with the immortal 'Ode to Joy' when completely deaf, conducting by feeling vibrations."
        }
    },
    {
        "id": "xristofor_kolumb",
        "name": {
            "uz": "Xristofor Kolumb",
            "ru": "Христофор Колумб",
            "en": "Christopher Columbus"
        },
        "era": {
            "uz": "XV–XVI asrlar (Buyuk geografik kashfiyotlar)",
            "ru": "XV–XVI века (Эпоха Великих открытий)",
            "en": "15th–16th century (Age of Discovery)"
        },
        "field": {
            "uz": "Dengizchi sayyoh, 1492-yilda Amerikani kashf etgan ekspeditsiya rahbari",
            "ru": "Мореплаватель, открывший Америку для Европы в 1492 году",
            "en": "Explorer and navigator who opened the Americas to European exploration"
        },
        "country": {
            "uz": "Genuya (Italiya) / Ispaniya",
            "ru": "Испания / Генуя",
            "en": "Genoa / Spain"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Portrait_of_a_Man%2C_Said_to_be_Christopher_Columbus.jpg/640px-Portrait_of_a_Man%2C_Said_to_be_Christopher_Columbus.jpg",
        "aliases": [
            "kolumb",
            "xristofor kolumb",
            "columbus",
            "колумб",
            "христофор колумб"
        ],
        "fun_fact": {
            "uz": "1492-yilda Atlantika okeanini kesib o'tib Amerikaga yetib borgan, biroq umrining oxirigacha Hindistonga yangi dengiz yo'lini ochdim deb ishongan.",
            "ru": "Совершил четыре экспедиции через Атлантику в Новый Свет, до конца жизни веря, что приплыл в Индию.",
            "en": "Completed four trans-Atlantic voyages opening the New World, famously sailing on the Santa María, Pinta, and Niña."
        }
    },
    {
        "id": "ferdinand_magellan",
        "name": {
            "uz": "Ferdinand Magellan",
            "ru": "Фернан Магеллан",
            "en": "Ferdinand Magellan"
        },
        "era": {
            "uz": "XVI asr (Buyuk geografik kashfiyotlar)",
            "ru": "XVI век",
            "en": "16th century"
        },
        "field": {
            "uz": "Dunyoni birinchi bo'lib aylanib chiqqan dengiz sayohati yetakchisi",
            "ru": "Мореплаватель, возглавивший первое кругосветное плавание",
            "en": "Explorer who led the first expedition to circumnavigate the globe"
        },
        "country": {
            "uz": "Portugaliya / Ispaniya",
            "ru": "Португалия / Испания",
            "en": "Portugal / Spain"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Ferdinand_Magellan.jpg/640px-Ferdinand_Magellan.jpg",
        "aliases": [
            "magellan",
            "ferdinand magellan",
            "магеллан",
            "фернан магеллан"
        ],
        "fun_fact": {
            "uz": "Uning boshchiligidagi ekspeditsiya Yer sharini birinchi marta aylanib chiqib, Yerning sharsimon ekanligini amalda to'liq isbotlagan.",
            "ru": "Его экспедиция первой обогнула земной шар через пролив Магеллана, окончательно доказав шарообразность Земли.",
            "en": "Organized the Spanish expedition to the East Indies that resulted in the first recorded circumnavigation of the Earth."
        }
    },
    {
        "id": "marko_polo",
        "name": {
            "uz": "Marko Polo",
            "ru": "Марко Поло",
            "en": "Marco Polo"
        },
        "era": {
            "uz": "XIII–XIV asrlar",
            "ru": "XIII–XIV века",
            "en": "13th–14th century"
        },
        "field": {
            "uz": "Venetsiyalik sayyoh, Buyuk Ipak yo'li bo'ylab Xitoygacha sayohat qilgan savdogar",
            "ru": "Купец и путешественник, описавший Азию и Китай в «Книге чудес света»",
            "en": "Venetian merchant, explorer, author of The Travels of Marco Polo"
        },
        "country": {
            "uz": "Venetsiya respublikasi / Italiya",
            "ru": "Венеция / Италия",
            "en": "Venice / Italy"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Frontispice_%C3%A9dition_de_Nuremberg_1477_%28cropped%29.png/640px-Frontispice_%C3%A9dition_de_Nuremberg_1477_%28cropped%29.png",
        "aliases": [
            "marko polo",
            "polo",
            "марко поло",
            "поло",
            "marco polo"
        ],
        "fun_fact": {
            "uz": "Buyuk Ipak yo'li orqali Xitoyga (Xubilayxon saroyiga) yetib borib, Yevropaga qog'oz pul, porox va chinnilar haqida birinchi ma'lumotlarni olib kelgan.",
            "ru": "Прожил в Китае при дворе Хубилай-хана 17 лет и познакомил европейцев с порохом, компасом и бумажными деньгами.",
            "en": "Spent 17 years at the court of Kublai Khan, introducing medieval Europe to paper money, coal, and the riches of Asia."
        }
    },
    {
        "id": "yuriy_gagarin",
        "name": {
            "uz": "Yuriy Gagarin",
            "ru": "Юрий Гагарин",
            "en": "Yuri Gagarin"
        },
        "era": {
            "uz": "XX asr (Koinot davri)",
            "ru": "XX век (Космическая эра)",
            "en": "20th century (Space Age)"
        },
        "field": {
            "uz": "Koinotga parvoz qilgan tarixdagi birinchi inson, kosmonavt",
            "ru": "Первый человек в космосе, лётчик-космонавт СССР",
            "en": "First human in space, pilot and cosmonaut"
        },
        "country": {
            "uz": "SSSR / Rossiya",
            "ru": "СССР / Россия",
            "en": "Soviet Union / Russia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Yuri_Gagarin_with_awards_%28cropped%29_2.jpg/640px-Yuri_Gagarin_with_awards_%28cropped%29_2.jpg",
        "aliases": [
            "yuriy gagarin",
            "gagarin",
            "гагарин",
            "юрий гагарин",
            "yuri gagarin"
        ],
        "fun_fact": {
            "uz": "1961-yil 12-aprelda 'Vostok-1' kemasida 'Poyexali!' so'zi bilan koinotga ko'tarilib, 108 daqiqa ichida Yer sharini aylanib chiqqan.",
            "ru": "12 апреля 1961 года на корабле «Восток-1» совершил первый в истории человечества орбитальный космический полет.",
            "en": "Became the first human in outer space on April 12, 1961, orbiting Earth aboard Vostok 1 for 108 minutes."
        }
    },
    {
        "id": "nil_armstrong",
        "name": {
            "uz": "Nil Armstrong",
            "ru": "Нил Армстронг",
            "en": "Neil Armstrong"
        },
        "era": {
            "uz": "XX asr (Oy dasturi)",
            "ru": "XX век (Лунная программа)",
            "en": "20th century (Moon landing)"
        },
        "field": {
            "uz": "Oy sathiga qadam qo'ygan tarixdagi birinchi inson, astronavt",
            "ru": "Первый человек, ступивший на поверхность Луны, астронавт NASA",
            "en": "First person to walk on the Moon, astronaut, aerospace engineer"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Neil_Armstrong_pose.jpg/640px-Neil_Armstrong_pose.jpg",
        "aliases": [
            "nil armstrong",
            "armstrong",
            "армстронг",
            "нил армстронг",
            "neil armstrong"
        ],
        "fun_fact": {
            "uz": "1969-yil 20-iyulda 'Apollon-11' missiyasida Oyga qadam qo'yib: 'Bu inson uchun kichik bir qadam, insoniyat uchun esa ulkan sakrashdir' degan.",
            "ru": "Ступив на Луну 20 июля 1969 года, произнес: «Это один маленький шаг для человека, но гигантский скачок для всего человечества».",
            "en": "First human to walk on the Moon (July 20, 1969), speaking the immortal line: 'That's one small step for [a] man, one giant leap for mankind.'"
        }
    },
    {
        "id": "gerodot",
        "name": {
            "uz": "Gerodot",
            "ru": "Геродот",
            "en": "Herodotus"
        },
        "era": {
            "uz": "Miloddan avvalgi V asr",
            "ru": "V век до н.э.",
            "en": "5th century BC"
        },
        "field": {
            "uz": "'Tarix otasi', birinchi tizimli tarixiy asarlar muallifi",
            "ru": "«Отец истории», автор первого фундаментального трактата «История»",
            "en": "'Father of History', author of The Histories"
        },
        "country": {
            "uz": "Qadimgi Gretsiya / Galikarnas",
            "ru": "Древняя Греция",
            "en": "Ancient Greece / Halicarnassus"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Marble_bust_of_Herodotos_MET_DT11742_%28cropped%29.jpg/640px-Marble_bust_of_Herodotos_MET_DT11742_%28cropped%29.jpg",
        "aliases": [
            "gerodot",
            "herodotus",
            "геродот"
        ],
        "fun_fact": {
            "uz": "Sitseron tomonidan 'Tarix otasi' deb nomlangan; Gretsiya-Fors urushlari va O'rta Osiyo xalqlari (massagetlar, Tomaris) haqida ilk ma'lumotlarni yozgan.",
            "ru": "Назван Цицероном «отцом истории», описал подвиг скифов и царицы Томирис, а также греко-персидские войны.",
            "en": "Dubbed 'The Father of History' by Cicero; his 'Histories' provide the earliest systematic account of Greco-Persian wars and Central Asian Scythians."
        }
    },
    {
        "id": "gomer",
        "name": {
            "uz": "Gomer",
            "ru": "Гомер",
            "en": "Homer"
        },
        "era": {
            "uz": "Miloddan avvalgi VIII asr",
            "ru": "VIII век до н.э.",
            "en": "8th century BC"
        },
        "field": {
            "uz": "Qadimgi epik shoir, 'Iliada' va 'Odisseya' dostonlari muallifi",
            "ru": "Легендарный эпический поэт, автор «Илиады» и «Одиссеи»",
            "en": "Legendary author of the Iliad and the Odyssey"
        },
        "country": {
            "uz": "Qadimgi Gretsiya (Ioniya)",
            "ru": "Древняя Греция",
            "en": "Ancient Greece"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Homer_At_the_British_Museum_2024_%283x4_cropped%29.jpg/640px-Homer_At_the_British_Museum_2024_%283x4_cropped%29.jpg",
        "aliases": [
            "gomer",
            "homer",
            "гомер"
        ],
        "fun_fact": {
            "uz": "Ko'zi ojiz afsonaviy dostonchi bo'lib, uning Troya urushi haqidagi 'Iliada' va 'Odisseya' dostonlari Yevropa adabiyotining tamal toshidir.",
            "ru": "Слепой сказитель, создавший величайшие эпосы человечества «Илиаду» и «Одиссею», давшие начало античной литературе.",
            "en": "Revered as the greatest epic poet of antiquity; the Iliad and Odyssey are the central foundational texts of Western literature."
        }
    },
    {
        "id": "shoh_jahon",
        "name": {
            "uz": "Shoh Jahon",
            "ru": "Шах-Джахан",
            "en": "Shah Jahan"
        },
        "era": {
            "uz": "XVII asr",
            "ru": "XVII век",
            "en": "17th century"
        },
        "field": {
            "uz": "Boburiy hukmdor, Toj Mahal mo''jizasini barpo etgan me'morlik homiysi",
            "ru": "Падишах Империи Великих Моголов, создатель Тадж-Махала",
            "en": "Mughal Emperor, commissioned the Taj Mahal and Peacock Throne"
        },
        "country": {
            "uz": "Boburiylar saltanati / Hindiston",
            "ru": "Империя Великих Моголов / Индия",
            "en": "Mughal Empire / India"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/%27Jujhar_Singh_Bundela_Kneels_in_Submission_to_Shah_Jahan%27%2C_painted_by_Bichitr%2C_c._1630%2C_Chester_Beatty_Library_%28cropped2%29.jpg/640px-%27Jujhar_Singh_Bundela_Kneels_in_Submission_to_Shah_Jahan%27%2C_painted_by_Bichitr%2C_c._1630%2C_Chester_Beatty_Library_%28cropped2%29.jpg",
        "aliases": [
            "shoh jahon",
            "shah jahan",
            "шах-джахан",
            "шах джахан"
        ],
        "fun_fact": {
            "uz": "Suyukli rafiqasi Mumtoz Mahal xotirasiga jahonning 7 yangi mo''jizasidan biri bo'lgan oq marmarli Toj Mahal maqbarasini qurdirgan.",
            "ru": "Построил шедевр мировой архитектуры — мавзолей Тадж-Махал в Агре в память о любимой жене Мумтаз-Махал.",
            "en": "Commissioned the Taj Mahal in Agra as a mausoleum for his favorite wife Mumtaz Mahal, as well as the Peacock Throne."
        }
    },
    {
        "id": "konstantin_buyuk",
        "name": {
            "uz": "Buyuk Konstantin I",
            "ru": "Константин I Великий",
            "en": "Constantine the Great"
        },
        "era": {
            "uz": "IV asr",
            "ru": "IV век",
            "en": "4th century AD"
        },
        "field": {
            "uz": "Rim imperatori, nasroniylikni qonuniylashtirgan, Konstantinopol asoschisi",
            "ru": "Римский император, сделал христианство государственной религией, основал Константинополь",
            "en": "Roman Emperor, legalized Christianity (Edict of Milan), founded Constantinople"
        },
        "country": {
            "uz": "Rim imperiyasi",
            "ru": "Римская империя",
            "en": "Roman Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Constantine_I_The_Great%2C_Colossal_bronze_statue_fragments%2C_Capitoline_Museums.jpg/640px-Constantine_I_The_Great%2C_Colossal_bronze_statue_fragments%2C_Capitoline_Museums.jpg",
        "aliases": [
            "konstantin buyuk",
            "constantine the great",
            "константин великий",
            "константин 1"
        ],
        "fun_fact": {
            "uz": "Milodiy 313-yilda Milan edikti bilan nasroniylik ta'qibiga chek qo'ygan va poytaxtni yangi shahar Konstantinopolga ko'chirgan.",
            "ru": "Основал Константинополь (будущую столицу Византии) и Миланским эдиктом 313 года узаконил христианство.",
            "en": "Issued the Edict of Milan in 313 legalizing Christianity and transferred the imperial capital to Constantinople."
        }
    },
    {
        "id": "yustinian_birinchi",
        "name": {
            "uz": "Yustinian I Buyuk",
            "ru": "Юстиниан I Великий",
            "en": "Justinian I (Justinian the Great)"
        },
        "era": {
            "uz": "VI asr",
            "ru": "VI век",
            "en": "6th century"
        },
        "field": {
            "uz": "Vizantiya imperatori, Ayasofya ibodatxonasini qurdirgan va Rim huquqi kodeksini tuzgan hukmdor",
            "ru": "Византийский император, создатель кодекса Юстиниана и собора Святой Софии",
            "en": "Byzantine Emperor, builder of Hagia Sophia, author of Corpus Juris Civilis"
        },
        "country": {
            "uz": "Vizantiya imperiyasi",
            "ru": "Византийская империя",
            "en": "Byzantine Empire"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Mosaic_of_Justinianus_I_-_Basilica_San_Vitale_%28Ravenna%29.jpg/640px-Mosaic_of_Justinianus_I_-_Basilica_San_Vitale_%28Ravenna%29.jpg",
        "aliases": [
            "yustinian",
            "yustinian i",
            "justinian i",
            "юстиниан",
            "юстиниан 1"
        ],
        "fun_fact": {
            "uz": "Konstantinopolda muazzam Ayasofya (Muqaddas Sofiya) soborini qurdirdi va zamonaviy fuqarolik huquqi asosi bo'lgan 'Yustinian kodeksi'ni tuzdirdi.",
            "ru": "Построил величайший собор Святой Софии в Константинополе и систематизировал римское право (Corpus Juris Civilis).",
            "en": "Constructed the Hagia Sophia and ordered the codification of Roman law into the Corpus Juris Civilis, the backbone of modern civil law."
        }
    },
    {
        "id": "martin_lyuter",
        "name": {
            "uz": "Martin Lyuter",
            "ru": "Мартин Лютер",
            "en": "Martin Luther"
        },
        "era": {
            "uz": "XVI asr (Reformatsiya)",
            "ru": "XVI век (Реформация)",
            "en": "16th century (Reformation)"
        },
        "field": {
            "uz": "Protestant Reformatsiyasi asoschisi, teolog, Injilni nemis tiliga tarjima qilgan",
            "ru": "Инициатор Реформации, основатель протестантизма, переводчик Библии",
            "en": "Leader of Protestant Reformation, theologian, translated Bible into German"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия / Священная Римская империя",
            "en": "Germany (Holy Roman Empire)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Lucas_Cranach_d.%C3%84._-_Martin_Luther%2C_1528_%28Veste_Coburg%29.jpg/640px-Lucas_Cranach_d.%C3%84._-_Martin_Luther%2C_1528_%28Veste_Coburg%29.jpg",
        "aliases": [
            "martin lyuter",
            "martin luther",
            "мартин лютер"
        ],
        "fun_fact": {
            "uz": "1517-yilda Vittenberg cherkovi eshigiga o'zining '95 tezis'ini qoqib qo'yib, butun Yevropa tarixini o'zgartirgan Reformatsiyani boshlab berdi.",
            "ru": "Прибил свои «95 тезисов» к дверям церкви в Виттенберге в 1517 году, положив начало Реформации и протестантизму.",
            "en": "Nailed his 95 Theses to the Wittenberg castle church door in 1517, igniting the Protestant Reformation across Europe."
        }
    },
    {
        "id": "nikkolo_makiavelli",
        "name": {
            "uz": "Nikkolo Makiavelli",
            "ru": "Никколо Макиавелли",
            "en": "Niccolò Machiavelli"
        },
        "era": {
            "uz": "XV–XVI asrlar (Uyg'onish davri)",
            "ru": "XV–XVI века (Возрождение)",
            "en": "15th–16th century (Renaissance)"
        },
        "field": {
            "uz": "Zamonaviy siyosatshunoslik otasi, diplomat, 'Hukmdor' (Il Principe) asari muallifi",
            "ru": "Политолог, философ, автор трактата «Государь»",
            "en": "Diplomat, political theorist, author of The Prince"
        },
        "country": {
            "uz": "Florensiya respublikasi / Italiya",
            "ru": "Флоренция / Италия",
            "en": "Florence / Italy"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Portrait_of_Niccol%C3%B2_Machiavelli_by_Santi_di_Tito.jpg/640px-Portrait_of_Niccol%C3%B2_Machiavelli_by_Santi_di_Tito.jpg",
        "aliases": [
            "makiavelli",
            "nikkolo makiavelli",
            "machiavelli",
            "макиавелли",
            "никколо макиавелли"
        ],
        "fun_fact": {
            "uz": "'Hukmdor' (Il Principe) asarida real siyosat mexanizmlarini birinchi bo'lib oshkora ochib bergan; 'Maqsad vositani oqlaydi' qarashining namoyandasi.",
            "ru": "Основоположник реалистической политологии, автор трактата «Государь», где описал законы завоевания и удержания власти.",
            "en": "Father of modern political philosophy whose realist treatise 'The Prince' analyzed how leaders acquire and maintain power."
        }
    },
    {
        "id": "iogann_bax",
        "name": {
            "uz": "Iogann Sebastyan Bax",
            "ru": "Иоганн Себастьян Бах",
            "en": "Johann Sebastian Bach"
        },
        "era": {
            "uz": "XVII–XVIII asrlar (Barokko davri)",
            "ru": "XVII–XVIII века (Эпоха барокко)",
            "en": "17th–18th century (Baroque era)"
        },
        "field": {
            "uz": "Barokko musiqasining eng buyuk kompozitori va organ ijrochisi",
            "ru": "Величайший композитор эпохи барокко, органист и педагог",
            "en": "Baroque composer, organist, creator of Brandenburg Concertos"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Germany (Holy Roman Empire)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Johann_Sebastian_Bach.jpg/640px-Johann_Sebastian_Bach.jpg",
        "aliases": [
            "bax",
            "iogann sebastyan bax",
            "bach",
            "бах",
            "иоганн себастьян бах"
        ],
        "fun_fact": {
            "uz": "1000 dan ortiq polifonik musiqiy asarlar yaratgan; musiqada matematik uyg'unlik va polifoniya cho'qqisi hisoblanadi.",
            "ru": "Создал более 1000 произведений во всех жанрах барокко; его музыка считается абсолютной вершиной полифонии.",
            "en": "Composed over 1,000 works of staggering polyphonic complexity, celebrated today as the pinnacle of Western musical composition."
        }
    },
    {
        "id": "iogann_gyote",
        "name": {
            "uz": "Iogann Volfgang fon Gyote",
            "ru": "Иоганн Вольфганг фон Гёте",
            "en": "Johann Wolfgang von Goethe"
        },
        "era": {
            "uz": "XVIII–XIX asrlar",
            "ru": "XVIII–XIX века",
            "en": "18th–19th century"
        },
        "field": {
            "uz": "Nemis adabiyoti dahosi, 'Faust' tragediyasi muallifi, mutafakkir va tabiatshunos",
            "ru": "Великий немецкий поэт, мыслитель, автор трагедии «Фауст»",
            "en": "Polymath, poet, playwright, novelist, author of Faust"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Germany"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Goethe_%28Stieler_1828%29.jpg/640px-Goethe_%28Stieler_1828%29.jpg",
        "aliases": [
            "gyote",
            "iogann gyote",
            "goethe",
            "гёте",
            "иоганн вольфганг гёте"
        ],
        "fun_fact": {
            "uz": "O'zining shoh asari 'Faust' tragediyasini yozish uchun 60 yildan ortiq vaqt sarflagan va Sharq she'riyatiga bag'ishlab 'G'arbu Sharq devoni'ni yaratgan.",
            "ru": "Писал трагедию «Фауст» на протяжении 60 лет; вдохновлялся восточной поэзией Хафиза в своем «Западно-восточном диване».",
            "en": "Spent six decades composing Faust; celebrated Persian poet Hafez in his monumental poetic collection 'West-Eastern Divan'."
        }
    },
    {
        "id": "dante_aligyeri",
        "name": {
            "uz": "Dante Aligyeri",
            "ru": "Данте Алигьери",
            "en": "Dante Alighieri"
        },
        "era": {
            "uz": "XIII–XIV asrlar",
            "ru": "XIII–XIV века",
            "en": "13th–14th century"
        },
        "field": {
            "uz": "Italiyan adabiy tili otasi, 'Ilohiy komediya' (Do'zax, A'rof, Jannat) muallifi",
            "ru": "Отец итальянского литературного языка, автор «Божественной комедии»",
            "en": "Father of the Italian language, poet, author of Divine Comedy"
        },
        "country": {
            "uz": "Florensiya / Italiya",
            "ru": "Флоренция / Италия",
            "en": "Florence / Italy"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Bargello_-_Kapelle_Fresko_2a.jpg/640px-Bargello_-_Kapelle_Fresko_2a.jpg",
        "aliases": [
            "dante",
            "dante aligyeri",
            "данте",
            "данте алигьери",
            "divine comedy"
        ],
        "fun_fact": {
            "uz": "'Ilohiy komediya' asarini lotin emas, xalq so'zlashadigan toskana shevasida yozib, zamonaviy italyan tiliga asos solgan.",
            "ru": "Написал «Божественную комедию» на народном тосканском диалекте вместо латыни, создав современный итальянский язык.",
            "en": "Pioneered vernacular literature with his masterpiece 'The Divine Comedy', establishing the Tuscan dialect as standard Italian."
        }
    },
    {
        "id": "migel_servantes",
        "name": {
            "uz": "Migel de Servantes",
            "ru": "Мигель де Сервантес",
            "en": "Miguel de Cervantes"
        },
        "era": {
            "uz": "XVI–XVII asrlar (Ispan oltin asri)",
            "ru": "XVI–XVII века (Золотой век Испании)",
            "en": "16th–17th century (Spanish Golden Age)"
        },
        "field": {
            "uz": "Zamonaviy roman janri asoschisi, 'Don Kixot' muallifi",
            "ru": "Великий испанский писатель, автор «Дон Кихота»",
            "en": "Novelist, poet, playwright, author of Don Quixote"
        },
        "country": {
            "uz": "Ispaniya",
            "ru": "Испания",
            "en": "Spain"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Cervantes_J%C3%A1uregui.jpg/640px-Cervantes_J%C3%A1uregui.jpg",
        "aliases": [
            "servantes",
            "migel servantes",
            "cervantes",
            "сервантес",
            "мигель де сервантес",
            "don kixot"
        ],
        "fun_fact": {
            "uz": "Uning 'Don Kixot' romani dunyo tarixida Injildan keyin eng ko'p tillarga tarjima qilingan va chop etilgan kitob hisoblanadi.",
            "ru": "Его роман «Дон Кихот» признан первым современным европейским романом и второй по тиражу книгой в мире после Библии.",
            "en": "Authored 'Don Quixote', widely regarded as the first modern novel and the most translated book in history after the Bible."
        }
    },
    {
        "id": "vinsent_van_gog",
        "name": {
            "uz": "Vinsent van Gog",
            "ru": "Винсент ван Гог",
            "en": "Vincent van Gogh"
        },
        "era": {
            "uz": "XIX asr (Postimpressionizm)",
            "ru": "XIX век (Постимпрессионизм)",
            "en": "19th century (Post-Impressionism)"
        },
        "field": {
            "uz": "Postimpressionist rassom, 'Yulduzli tun' va 'Kungaboqarlar' muallifi",
            "ru": "Художник-постимпрессионист, создатель «Звездной ночи»",
            "en": "Post-Impressionist painter, creator of The Starry Night and Sunflowers"
        },
        "country": {
            "uz": "Niderlandiya / Fransiya",
            "ru": "Нидерланды / Франция",
            "en": "Netherlands / France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg/640px-Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg",
        "aliases": [
            "van gog",
            "vinsent van gog",
            "van gogh",
            "ван гог",
            "винсент ван гог"
        ],
        "fun_fact": {
            "uz": "Tirikligida deyarli hech bir rasmini sota olmagan qashshoq rassom, bugun esa uning 'Yulduzli tun' kartinasi yuzlab million dollarga baholanadi.",
            "ru": "При жизни продал лишь считанные картины и умер в нищете, а сегодня его «Звёздная ночь» и «Подсолнухи» — мировые сокровища живописи.",
            "en": "Created over 2,100 artworks in just a decade; sold almost none in his lifetime, yet painted immortal masterpieces like The Starry Night."
        }
    },
    {
        "id": "pablo_pikasso",
        "name": {
            "uz": "Pablo Pikasso",
            "ru": "Пабло Пикассо",
            "en": "Pablo Picasso"
        },
        "era": {
            "uz": "XX asr (Kubizm / Modernizm)",
            "ru": "XX век (Кубизм)",
            "en": "20th century (Cubism)"
        },
        "field": {
            "uz": "Kubizm yo'nalishi asoschisi, XX asr tasviriy san'atining buyuk novatori",
            "ru": "Основоположник кубизма, величайший новатор живописи XX века",
            "en": "Painter, sculptor, co-founder of Cubism, creator of Guernica"
        },
        "country": {
            "uz": "Ispaniya / Fransiya",
            "ru": "Испания / Франция",
            "en": "Spain / France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Pablo_picasso_1.jpg/640px-Pablo_picasso_1.jpg",
        "aliases": [
            "pikasso",
            "pablo pikasso",
            "picasso",
            "пикассо",
            "пабло пикассо"
        ],
        "fun_fact": {
            "uz": "Urush dahshatlarini aks ettirgan 'Gernika' kartinasi va 'Tinchlik kaptari' ramzini yaratgan XX asrning eng sermahsul rassomi.",
            "ru": "Создал всемирно известную антивоенную картину «Герника» и символ движения за мир — Голубя мира.",
            "en": "Co-founded the Cubist movement and created the anti-war masterpiece 'Guernica' as well as the universal Dove of Peace symbol."
        }
    },
    {
        "id": "rembrandt",
        "name": {
            "uz": "Rembrandt van Reyn",
            "ru": "Рембрандт ван Рейн",
            "en": "Rembrandt van Rijn"
        },
        "era": {
            "uz": "XVII asr (Golland oltin davri)",
            "ru": "XVII век (Золотой век Голландии)",
            "en": "17th century (Dutch Golden Age)"
        },
        "field": {
            "uz": "Yorug'lik va soya ustasi, 'Tungi qorovul' asari rassomi",
            "ru": "Мастер светотени, величайший живописец «Золотого века» Голландии",
            "en": "Dutch Golden Age master painter and printmaker, creator of The Night Watch"
        },
        "country": {
            "uz": "Niderlandiya",
            "ru": "Нидерланды",
            "en": "Netherlands (Dutch Republic)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Rembrandt_van_Rijn_-_Self-Portrait_-_Google_Art_Project.jpg/640px-Rembrandt_van_Rijn_-_Self-Portrait_-_Google_Art_Project.jpg",
        "aliases": [
            "rembrandt",
            "rembrandt van reyn",
            "рембрандт",
            "рембрандт ван рейн"
        ],
        "fun_fact": {
            "uz": "Moybo'yoq kartinalarida yorug'lik va soyani qo'llash san'atining eng buyuk ustasi bo'lib, 'Tungi qorovul' asarini yaratgan.",
            "ru": "Непревзойденный виртуоз светотени, автор грандиозного группового портрета «Ночной дозор».",
            "en": "Master of chiaroscuro (light and shadow) who captured profound human emotion in masterpieces like The Night Watch."
        }
    },
    {
        "id": "viktor_gyugo",
        "name": {
            "uz": "Viktor Gyugo",
            "ru": "Виктор Гюго",
            "en": "Victor Hugo"
        },
        "era": {
            "uz": "XIX asr (Romantizm)",
            "ru": "XIX век (Романтизм)",
            "en": "19th century (Romanticism)"
        },
        "field": {
            "uz": "Buyuk fransuz yozuvchisi, 'Xo'rlanganlar' va 'Parij Bibi Maryam ibodatxonasi' muallifi",
            "ru": "Классик французской литературы, автор «Отверженных» и «Собора Парижской Богоматери»",
            "en": "Novelist, poet, dramatist, author of Les Misérables and The Hunchback of Notre-Dame"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Victor_Hugo_by_%C3%89tienne_Carjat_1876_-_full.jpg/640px-Victor_Hugo_by_%C3%89tienne_Carjat_1876_-_full.jpg",
        "aliases": [
            "viktor gyugo",
            "gyugo",
            "hugo",
            "victor hugo",
            "гюго",
            "виктор гюго"
        ],
        "fun_fact": {
            "uz": "'Parij Bibi Maryam ibodatxonasi' romani orqali vayron bo'layotgan tarixiy gotika soborini buzilishdan saqlab qolgan.",
            "ru": "Своим романом «Собор Парижской Богоматери» спас исторический шедевр готики от сноса и инициировал его реставрацию.",
            "en": "His novel 'The Hunchback of Notre-Dame' sparked a preservation movement that saved the cathedral from demolition."
        }
    },
    {
        "id": "pyotr_chaykovskiy",
        "name": {
            "uz": "Pyotr Chaykovskiy",
            "ru": "Пётр Ильич Чайковский",
            "en": "Pyotr Ilyich Tchaikovsky"
        },
        "era": {
            "uz": "XIX asr (Romantizm)",
            "ru": "XIX век",
            "en": "19th century"
        },
        "field": {
            "uz": "Afsonaviy kompozitor, 'Oqqush ko'li', 'Qarsildoq' va 'Uyqudagi go'zal' baletlari muallifi",
            "ru": "Великий композитор, автор балетов «Лебединое озеро», «Щелкунчик» и 6 симфоний",
            "en": "Composer, creator of Swan Lake, The Nutcracker, and 1812 Overture"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Tchaikovsky_by_Reutlinger_%28cropped%29.jpg/640px-Tchaikovsky_by_Reutlinger_%28cropped%29.jpg",
        "aliases": [
            "chaykovskiy",
            "pyotr chaykovskiy",
            "tchaikovsky",
            "чайковский",
            "петр чайковский"
        ],
        "fun_fact": {
            "uz": "Uning 'Oqqush ko'li' va 'Qarsildoq' baletlari jahon teatrlarida eng ko'p sahnalashtiriladigan durdona musiqalardir.",
            "ru": "Создал самые исполняемые в истории балеты — «Лебединое озеро» и новогодний шедевр «Щелкунчик».",
            "en": "Composed the world's most performed ballets, Swan Lake and The Nutcracker, beloved across generations worldwide."
        }
    },
    {
        "id": "spartak",
        "name": {
            "uz": "Spartak",
            "ru": "Спартак",
            "en": "Spartacus"
        },
        "era": {
            "uz": "Miloddan avvalgi I asr",
            "ru": "I век до н.э.",
            "en": "1st century BC"
        },
        "field": {
            "uz": "Gladiator, Qadimgi Rimdagi eng yirik qullar qo'zg'oloni yetakchisi",
            "ru": "Гладиатор, предводитель крупнейшего восстания рабов в Древнем Риме",
            "en": "Gladiator, leader of the major slave uprising against the Roman Republic"
        },
        "country": {
            "uz": "Frakiya / Qadimgi Rim",
            "ru": "Фракия / Древний Рим",
            "en": "Thrace / Ancient Rome"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/%CE%A3%CF%80%CE%AC%CF%81%CF%84%CE%B1%CE%BA%CE%BF%CF%82_Spartacus%2CEspartaco_marble_statue_in_Louvre_%22%CE%9C%CE%B1%CE%B9%CE%B4%CE%BF%CE%B9_clan_-Meadow%22_slave_macedon-greek.jpg/640px-%CE%A3%CF%80%CE%AC%CF%81%CF%84%CE%B1%CE%BA%CE%BF%CF%82_Spartacus%2CEspartaco_marble_statue_in_Louvre_%22%CE%9C%CE%B1%CE%B9%CE%B4%CE%BF%CE%B9_clan_-Meadow%22_slave_macedon-greek.jpg",
        "aliases": [
            "spartak",
            "spartacus",
            "спартак"
        ],
        "fun_fact": {
            "uz": "Kapuyadagi gladiatorlar maktabidan 70 kishi bilan qochib, 120 000 kishilik ulkan armiya to'plagan va bir necha bor Rim legionlarini tor-mor qilgan.",
            "ru": "Бежал из школы гладиаторов и собрал армию в 120 000 повстанцев, громившую лучшие легионы Рима на протяжении двух лет.",
            "en": "Escaped a gladiatorial ludus to lead a 120,000-strong rebellion that defeated numerous Roman armies in the Third Servile War."
        }
    },
    {
        "id": "abraham_lincoln",
        "name": {
            "uz": "Avraam Linkoln",
            "ru": "Авраам Линкольн",
            "en": "Abraham Lincoln"
        },
        "era": {
            "uz": "XIX asr",
            "ru": "XIX век",
            "en": "19th century"
        },
        "field": {
            "uz": "AQSHning 16-Prezidenti, davlat arbobi, quldorlikni bekor qilgan",
            "ru": "16-й Президент США, национальный герой, освободитель рабов",
            "en": "16th US President, preserved the Union, abolished slavery"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg/330px-Abraham_Lincoln_O-77_matte_collodion_print.jpg",
        "aliases": [
            "linkoln",
            "avraam linkoln",
            "линкольн",
            "авраам линкольн",
            "lincoln",
            "abraham lincoln"
        ],
        "fun_fact": {
            "uz": "AQSH fuqarolar urushida davlat yaxlitligini saqlab qolgan va 'Ozodlik deklaratsiyasi' orqali qullikni butunlay bekor qilgan.",
            "ru": "Сохранил единство США в ходе Гражданской войны и законодательно отменил рабство.",
            "en": "Led the United States through its Civil War, preserved the Union, and issued the Emancipation Proclamation."
        }
    },
    {
        "id": "winston_churchill",
        "name": {
            "uz": "Uinston Cherchill",
            "ru": "Уинстон Черчилль",
            "en": "Winston Churchill"
        },
        "era": {
            "uz": "XX asr",
            "ru": "XX век",
            "en": "20th century"
        },
        "field": {
            "uz": "Buyuk Britaniya Bosh vaziri, davlat arbobi, adabiyot bo'yicha Nobel sovrindori",
            "ru": "Премьер-министр Великобритании, военный лидер, лауреат Нобелевской премии",
            "en": "British Prime Minister, wartime leader, Nobel laureate"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Sir_Winston_Churchill_-_19086236948_%28restored%29.jpg/330px-Sir_Winston_Churchill_-_19086236948_%28restored%29.jpg",
        "aliases": [
            "cherchill",
            "uinston cherchill",
            "черчилль",
            "уинстон черчилль",
            "churchill",
            "winston churchill"
        ],
        "fun_fact": {
            "uz": "Ikkinchi jahon urushida fashizmga qarshi buyuk kurash yetakchilaridan biri bo'lgan va o'tkir nutqlari bilan xalqini ilhomlantirgan.",
            "ru": "Возглавлял Великобританию во Второй мировой войне и вдохновлял нацию своими легендарными речами.",
            "en": "Led the United Kingdom to victory in World War II and was renowned for his inspiring wartime speeches."
        }
    },
    {
        "id": "george_washington",
        "name": {
            "uz": "Jorj Vashington",
            "ru": "Джордж Вашингтон",
            "en": "George Washington"
        },
        "era": {
            "uz": "XVIII asr",
            "ru": "XVIII век",
            "en": "18th century"
        },
        "field": {
            "uz": "AQSHning birinchi Prezidenti, Mustaqillik urushi bosh qo'mondoni",
            "ru": "Первый Президент США, главнокомандующий в войне за независимость",
            "en": "First President of the United States, military general, Founding Father"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg/640px-Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg",
        "aliases": [
            "vashington",
            "jorj vashington",
            "вашингтон",
            "джордж вашингтон",
            "washington",
            "george washington"
        ],
        "fun_fact": {
            "uz": "AQSH Mustaqillik urushida Kontinental armiyaga boshchilik qilgan va mamlakatning 'Otasi' deb e'zozlanadi.",
            "ru": "Главнокомандующий Континентальной армией, первый всенародно избранный президент США.",
            "en": "Led the Continental Army to victory in the American Revolutionary War and served as first US President."
        }
    }
]

HISTORICAL_BY_ID = {h["id"]: h for h in HISTORICAL_FIGURES}

def get_historical_figure_by_id(figure_id: str) -> dict | None:
    """Retrieve historical figure data dictionary by unique string ID."""
    return HISTORICAL_BY_ID.get(figure_id)

def get_random_historical_figures(count: int = 4, exclude_id: str | None = None) -> list[dict]:
    """Return a random sample of historical figures, optionally excluding a specific ID."""
    pool = [h for h in HISTORICAL_FIGURES if h["id"] != exclude_id] if exclude_id else HISTORICAL_FIGURES
    return random.sample(pool, min(count, len(pool)))

def search_historical_by_alias(alias: str) -> dict | None:
    """Case-insensitive search by name or alias."""
    norm = alias.strip().lower()
    for h in HISTORICAL_FIGURES:
        if norm in h["aliases"] or any(norm == v.lower() for v in h["name"].values()):
            return h
    return None
