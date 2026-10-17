# -*- coding: utf-8 -*-
"""
GeoGuru Game Dataset: History, Ancient Civilizations, Empires & Artifacts.
Contains 400 rich multilingual questions across 4 engaging sub-modes:
1. timeline (100 items): Chronological historical ordering (which landmark event occurred earliest).
2. empire_maps (100 items): Identifying historic empires, realms, and boundaries from maps.
3. who_am_i (100 items): Identifying legendary rulers, commanders, and figures from 3 progressive clues.
4. artifacts (100 items): World-famous archaeological relics, ancient coins, armor, and treasures.
"""
import random
from typing import Optional, List, Dict, Any

HISTORY_DATA: List[Dict[str, Any]] = [{'id': 'hist_time_001',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Shumer mixxat yozuvining paydo bo'lishi (~mil. avv. 3400)",
                     'Misrdagi Xufu (Xeops) piramidasi qurilishi (~mil. avv. 2560)',
                     "Xammurapi qonunlari to'plamining e'lon qilinishi (~mil. avv. 1754)",
                     'Afsonaviy Troya urushi (~mil. avv. 1200)'],
              'ru': ['Возникновение шумерской клинописи (~3400 до н.э.)',
                     'Строительство пирамиды Хеопса в Египте (~2560 до н.э.)',
                     'Издание Законов царя Хаммурапи (~1754 до н.э.)',
                     'Троянская война (~1200 до н.э.)'],
              'en': ['Emergence of Sumerian cuneiform writing (~3400 BC)',
                     "Construction of Khufu's Great Pyramid (~2560 BC)",
                     'Enactment of the Code of Hammurabi (~1754 BC)',
                     'The Trojan War (~1200 BC)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Shumer mixxat yozuvining paydo bo'lishi (~mil. avv. 3400)",
                     'ru': 'Возникновение шумерской клинописи (~3400 до н.э.)',
                     'en': 'Emergence of Sumerian cuneiform writing (~3400 BC)'},
  'image_url': None,
  'fun_fact': {'uz': 'Shumer mixxat yozuvi insoniyat tarixidagi eng qadimgi yozuv turi hisoblanib, dastlab loy '
                     'taxtachalarga qamish tayoqchalar yordamida yozilgan.',
               'ru': 'Шумерская клинопись считается древнейшей системой письменности: знаки выдавливались тростниковой '
                     'палочкой на мягкой глине.',
               'en': 'Sumerian cuneiform is the earliest known writing system in history, written on clay tablets '
                     'using reed styluses.'},
  'aliases': ['shumer', 'mixxat', 'клинопись', 'шумеры', 'cuneiform', 'sumer']},
 {'id': 'hist_time_002',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Afinadagi Parfenon ibodatxonasi qurilishi (mil. avv. 438)',
                     'Stounxendj megalitining qurilishi boshlanishi (~mil. avv. 3000)',
                     'Rimdagi Kolizey amfiteatrining ochilishi (milodiy 80)',
                     'Konstantinopoldagi Ayasofya ibodatxonasining qurilishi (milodiy 537)'],
              'ru': ['Строительство Парфенона в Афинах (438 до н.э.)',
                     'Начало строительства Стоунхенджа (~3000 до н.э.)',
                     'Открытие римского Колизея (80 н.э.)',
                     'Строительство Собора Святой Софии (537 н.э.)'],
              'en': ['Construction of the Parthenon in Athens (438 BC)',
                     'Beginning of Stonehenge construction (~3000 BC)',
                     'Inauguration of the Colosseum in Rome (80 AD)',
                     'Building of Hagia Sophia in Constantinople (537 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Stounxendj megalitining qurilishi boshlanishi (~mil. avv. 3000)',
                     'ru': 'Начало строительства Стоунхенджа (~3000 до н.э.)',
                     'en': 'Beginning of Stonehenge construction (~3000 BC)'},
  'image_url': None,
  'fun_fact': {'uz': "Stounxendj Angliyadagi qadimiy tosh majmua bo'lib, Parfenondan deyarli 2500 yil oldin "
                     'boshlangan.',
               'ru': 'Стоунхендж был заложен более чем за две тысячи лет до классических памятников Древней Греции и '
                     'Рима.',
               'en': 'Stonehenge was begun roughly 2,500 years before the Parthenon was completed in Athens.'},
  'aliases': ['stounxendj', 'stounhendj', 'stonehenge', 'стоунхендж']},
 {'id': 'hist_time_003',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Iskandariya (Misr) shahriga asos solinishi (mil. avv. 331)',
                     'Konstantinopol shahrining tantanali ochilishi (milodiy 330)',
                     'Qadimgi Rim shahriga asos solinishi (mil. avv. 753)',
                     "Bag'dod shahrining barpo etilishi (milodiy 762)"],
              'ru': ['Основание Александрии в Египте (331 до н.э.)',
                     'Основание Константинополя (330 н.э.)',
                     'Легендарное основание Рима Ромулом (753 до н.э.)',
                     'Строительство Багдада халифом Мансуром (762 н.э.)'],
              'en': ['Founding of Alexandria in Egypt (331 BC)',
                     'Inauguration of Constantinople (330 AD)',
                     'Legendary founding of Rome (753 BC)',
                     'Foundation of Baghdad by Caliph Al-Mansur (762 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Qadimgi Rim shahriga asos solinishi (mil. avv. 753)',
                     'ru': 'Легендарное основание Рима Ромулом (753 до н.э.)',
                     'en': 'Legendary founding of Rome (753 BC)'},
  'image_url': None,
  'fun_fact': {'uz': "Afsonaga ko'ra, Rim shahriga mil. avv. 753 yil 21 aprelda bo'ri emizgan Romul va Rem asos "
                     'solgan.',
               'ru': 'Традиционная дата основания Рима — 21 апреля 753 года до н.э., давшая начало римскому календарю '
                     '«от основания города».',
               'en': 'According to legend, Rome was founded on April 21, 753 BC by Romulus, giving birth to the Roman '
                     'Republic and Empire.'},
  'aliases': ['rim', 'rimga asos solinishi', 'основание рима', 'рим', 'founding of rome', 'rome']},
 {'id': 'hist_time_004',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Aleksandr Makedonskiy Persepolni zabt etishi (mil. avv. 330)',
                     "Yuliy Sezarning Rubikon daryosidan o'tishi (mil. avv. 49)",
                     "G'arbiy Rim imperiyasining qulashi (milodiy 476)",
                     'Buyuk Kir II Bobilni zabt etishi (mil. avv. 539)'],
              'ru': ['Захват Персеполя Александром Македонским (330 до н.э.)',
                     'Переход Цезаря через Рубикон (49 до н.э.)',
                     'Падение Западной Римской империи (476 н.э.)',
                     'Завоевание Вавилона Киром Великим (539 до н.э.)'],
              'en': ['Alexander the Great takes Persepolis (330 BC)',
                     'Julius Caesar crosses the Rubicon (49 BC)',
                     'Fall of the Western Roman Empire (476 AD)',
                     'Cyrus the Great conquers Babylon (539 BC)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Buyuk Kir II Bobilni zabt etishi (mil. avv. 539)',
                     'ru': 'Завоевание Вавилона Киром Великим (539 до н.э.)',
                     'en': 'Cyrus the Great conquers Babylon (539 BC)'},
  'image_url': None,
  'fun_fact': {'uz': 'Buyuk Kir II Bobilni egallagach, asirlikdagi yahudiylarni Quddusga qaytargan va tarixda ilk '
                     'inson huquqlari xartiyasi deb tan olingan Kir silindrini yaratgan.',
               'ru': 'Кир Великий освободил плененные народы Вавилона и издал цилиндр, признанный первым биллем о '
                     'правах человека.',
               'en': 'Cyrus conquered Babylon in 539 BC, releasing the Jewish captives and proclaiming tolerance on '
                     'the Cyrus Cylinder.'},
  'aliases': ['kir', 'kir ii', 'bobil', 'кибр', 'вавилон', 'cyrus', 'babylon']},
 {'id': 'hist_time_005',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Marafon jangi — afinaliklar forslar ustidan g'alaba qozonishi (mil. avv. 490)",
                     'Gavgamela jangi — Aleksandr va Doro III jangi (mil. avv. 331)',
                     'Kanna jangi — Gannibal Rim armiyasini qurshab olishi (mil. avv. 216)',
                     'Aksiy dengiz jangi (mil. avv. 31)'],
              'ru': ['Марафонская битва греков с персами (490 до н.э.)',
                     'Битва при Гавгамелах (331 до н.э.)',
                     'Битва при Каннах Ганнибала (216 до н.э.)',
                     'Битва при Акциуме (31 до н.э.)'],
              'en': ['Battle of Marathon (490 BC)',
                     'Battle of Gaugamela (331 BC)',
                     'Battle of Cannae (216 BC)',
                     'Battle of Actium (31 BC)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Marafon jangi — afinaliklar forslar ustidan g'alaba qozonishi (mil. avv. 490)",
                     'ru': 'Марафонская битва греков с персами (490 до н.э.)',
                     'en': 'Battle of Marathon (490 BC)'},
  'image_url': None,
  'fun_fact': {'uz': "Marafon jangidagi g'alaba Afinada demokratiyani saqlab qolgan va zamonaviy marafon yugurishiga "
                     'asos solgan.',
               'ru': 'Победа греков при Марафоне спасла афинскую демократию и вдохновила спортивную марафонскую '
                     'дистанцию.',
               'en': 'The Athenian victory at Marathon in 490 BC turned back the Persian invasion and inspired the '
                     'marathon race.'},
  'aliases': ['marafon', 'marafon jangi', 'марафон', 'марафонская битва', 'battle of marathon', 'marathon']},
 {'id': 'hist_time_006',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Xitoyda Terrakota armiyasining yaratilishi (~mil. avv. 210)',
                     'Giza Buyuk Sfinksining barpo etilishi (~mil. avv. 2500)',
                     "Rimda Trayan ustunining qad ko'tarishi (milodiy 113)",
                     "Buyuk Xitoy devorining Min sulolasi g'ishtli qismlari qurilishi (~milodiy 1400)"],
              'ru': ['Создание Терракотовой армии в Китае (~210 до н.э.)',
                     'Создание Большого сфинкса в Гизе (~2500 до н.э.)',
                     'Колонна Траяна в Риме (113 н.э.)',
                     'Строительство каменной стены Мин (~1400 н.э.)'],
              'en': ['Creation of the Terracotta Army (~210 BC)',
                     'Carving of the Great Sphinx of Giza (~2500 BC)',
                     "Trajan's Column erected in Rome (113 AD)",
                     'Ming-era Great Wall stone masonry (~1400 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Giza Buyuk Sfinksining barpo etilishi (~mil. avv. 2500)',
                     'ru': 'Создание Большого сфинкса в Гизе (~2500 до н.э.)',
                     'en': 'Carving of the Great Sphinx of Giza (~2500 BC)'},
  'image_url': None,
  'fun_fact': {'uz': "Buyuk Sfinks fir'avn Xafra davrida ulkan yaxlit qoyatoshdan yo'nib yasalgan qadimgi dunyo "
                     "mo'jizasidir.",
               'ru': 'Большой сфинкс высечен из монолитной известняковой скалы во времена фараона Хафры около 4500 лет '
                     'назад.',
               'en': 'The Great Sphinx was carved from a single limestone ridge during the reign of Pharaoh Khafre '
                     'around 2500 BC.'},
  'aliases': ['sfinks', 'buyuk sfinks', 'сфинкс', 'sphinx', 'great sphinx']},
 {'id': 'hist_time_007',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Afina va Sparta o'rtasida Peloponnes urushi boshlanishi (mil. avv. 431)",
                     "Rim va Karfagen o'rtasida Birinchi Puni urushi boshlanishi (mil. avv. 264)",
                     "Qadimgi Yunonistonda ilk Olimpiya o'yinlarining o'tkazilishi (mil. avv. 776)",
                     "Spartak boshchiligidagi qullar qo'zg'oloni (mil. avv. 73)"],
              'ru': ['Начало Пелопоннесской войны (431 до н.э.)',
                     'Первая Пуническая война (264 до н.э.)',
                     'Первые античные Олимпийские игры (776 до н.э.)',
                     'Восстание Спартака (73 до н.э.)'],
              'en': ['Start of the Peloponnesian War (431 BC)',
                     'First Punic War begins (264 BC)',
                     'First recorded Ancient Olympic Games (776 BC)',
                     'Spartacus gladiator rebellion (73 BC)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Qadimgi Yunonistonda ilk Olimpiya o'yinlarining o'tkazilishi (mil. avv. 776)",
                     'ru': 'Первые античные Олимпийские игры (776 до н.э.)',
                     'en': 'First recorded Ancient Olympic Games (776 BC)'},
  'image_url': None,
  'fun_fact': {'uz': "Olimpiya o'yinlari paytida butun Elladada muqaddas sulh (ekexeyriya) e'lon qilinib, barcha "
                     "urushlar to'xtatilgan.",
               'ru': 'На время Олимпийских игр в Древней Греции объявлялось священное перемирие, прекращавшее любые '
                     'военные действия.',
               'en': 'During ancient Olympic Games, a sacred truce (ekecheiria) was declared, halting all Greek wars.'},
  'aliases': ['olimpiya', 'olimpiada', 'олимпийские игры', 'olympic games', 'olympics']},
 {'id': 'hist_time_008',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Arastu (Aristotel) vafot etishi (mil. avv. 322)',
                     "Arximedning Sirakuzada o'ldirilishi (mil. avv. 212)",
                     "Rim notig'i Sitseronning qatl etilishi (mil. avv. 43)",
                     'Suqrotning (Sokrat) Afinada qatl etilishi (mil. avv. 399)'],
              'ru': ['Смерть Аристотеля (322 до н.э.)',
                     'Гибель Архимеда в Сиракузах (212 до н.э.)',
                     'Казнь оратора Цицерона (43 до н.э.)',
                     'Казнь философа Сократа в Афинах (399 до н.э.)'],
              'en': ['Death of Aristotle (322 BC)',
                     'Death of Archimedes at Syracuse (212 BC)',
                     'Assassination of Cicero (43 BC)',
                     'Execution of Socrates in Athens (399 BC)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Suqrotning (Sokrat) Afinada qatl etilishi (mil. avv. 399)',
                     'ru': 'Казнь философа Сократа в Афинах (399 до н.э.)',
                     'en': 'Execution of Socrates in Athens (399 BC)'},
  'image_url': None,
  'fun_fact': {'uz': "Suqrot haqiqatni bahslarda izlash (mayevtika) usulini yaratgan va uning g'oyalari Platon hamda "
                     'Arastu orqali jahon falsafasiga singgan.',
               'ru': 'Сократ принял яд цикуты во имя верности закону, став вечным символом философского мужества.',
               'en': 'Socrates was condemned to drink hemlock in 399 BC, choosing integrity over exile or escape.'},
  'aliases': ['suqrot', 'sokrat', 'сократ', 'socrates']},
 {'id': 'hist_time_009',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Ashokaning Kalinga jangi va buddaviylikni qabul qilishi (mil. avv. 261)',
                     'Qin Shixuandi Xitoyni yagona imperiyaga birlashtirishi (mil. avv. 221)',
                     "Buyuk Ipak yo'lining Xan sulolasi tomonidan ochilishi (~mil. avv. 130)",
                     'Sosoniylar saltanatining vujudga kelishi (milodiy 224)'],
              'ru': ['Битва при Калинге и принятие буддизма Ашокой (261 до н.э.)',
                     'Объединение Китая Цинь Шихуанди (221 до н.э.)',
                     'Открытие Шелкового пути династией Хань (~130 до н.э.)',
                     'Возникновение державы Сасанидов (224 н.э.)'],
              'en': ["Ashoka's Kalinga War and embrace of Buddhism (261 BC)",
                     'Qin Shi Huang unifies China (221 BC)',
                     'Han Dynasty opens the Silk Road (~130 BC)',
                     'Rise of the Sasanian Empire (224 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Ashokaning Kalinga jangi va buddaviylikni qabul qilishi (mil. avv. 261)',
                     'ru': 'Битва при Калинге и принятие буддизма Ашокой (261 до н.э.)',
                     'en': "Ashoka's Kalinga War and embrace of Buddhism (261 BC)"},
  'image_url': None,
  'fun_fact': {'uz': "Ashoka Kalingadagi qurbonlar fojiasidan so'ng butun Hindiston bo'ylab tinchlik, mehr-shafqat va "
                     "bag'rikenglik bitiklarini tosh ustunlarga o'yib yozdirgan.",
               'ru': 'Царь Ашока после битвы при Калинге установил каменные эдикты с призывами к миру и уважению ко '
                     'всем живым существам.',
               'en': 'Following the devastation of Kalinga, Emperor Ashoka renounced warfare and inscribed rock edicts '
                     'promoting dharma across India.'},
  'aliases': ['ashoka', 'kalinga', 'ашока', 'ashoka the great']},
 {'id': 'hist_time_010',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Nikeya butunjahon cherkov sobori chaqirilishi (milodiy 325)',
                     "Vezuviy vulqoni otilishi va Pompey vayron bo'lishi (milodiy 79)",
                     'Alarix boshchiligidagi vestgotlar Rimni talashi (milodiy 410)',
                     'Xlodvig Franklar qirolligiga asos solishi (milodiy 481)'],
              'ru': ['Первый Никейский собор (325 н.э.)',
                     'Извержение Везувия и гибель Помпей (79 н.э.)',
                     'Разграбление Рима вестготами Алариха (410 н.э.)',
                     'Основание королевства франков Хлодвигом (481 н.э.)'],
              'en': ['First Council of Nicaea (325 AD)',
                     'Eruption of Vesuvius destroying Pompeii (79 AD)',
                     'Sack of Rome by the Visigoths (410 AD)',
                     'Clovis founds Frankish Kingdom (481 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Vezuviy vulqoni otilishi va Pompey vayron bo'lishi (milodiy 79)",
                     'ru': 'Извержение Везувия и гибель Помпей (79 н.э.)',
                     'en': 'Eruption of Vesuvius destroying Pompeii (79 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Vezuviy kuli Pompey va Gerkulanum shaharlarini shu qadar mukammal saqlaganki, devoriy suratlar, '
                     "nonvoyxonalar va uy-ro'zg'or buyumlari deyarli o'zgarmasdan topilgan.",
               'ru': 'Извержение Везувия запечатало римские города в слое пепла, сохранив фрески, мозаики и даже '
                     'выпеченный хлеб.',
               'en': 'The ash from Mount Vesuvius preserved Pompeii so completely that loaves of bread were found '
                     'intact in carbonized ovens.'},
  'aliases': ['vezuviy', 'pompey', 'везувий', 'помпеи', 'vesuvius', 'pompeii']},
 {'id': 'hist_time_011',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Yarmuk jangi — musulmonlarning Vizantiya ustidan g'alabasi (milodiy 636)",
                     "Talas jangi — arablar va xitoyliklar to'qnashuvi (milodiy 751)",
                     "Hijrat — musulmonlarning Makkadan Madinaga ko'chishi (milodiy 622)",
                     "Buyuk Karlning Rimda imperator deb e'lon qilinishi (milodiy 800)"],
              'ru': ['Битва при Ярмуке против Византии (636 н.э.)',
                     'Таласская битва арабов с Китаем (751 н.э.)',
                     'Хиджра — переселение мусульман из Мекки в Медину (622 н.э.)',
                     'Коронация Карла Великого в Риме (800 н.э.)'],
              'en': ['Battle of Yarmouk (636 AD)',
                     'Battle of Talas (751 AD)',
                     'The Hijrah from Mecca to Medina (622 AD)',
                     'Coronation of Charlemagne (800 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Hijrat — musulmonlarning Makkadan Madinaga ko'chishi (milodiy 622)",
                     'ru': 'Хиджра — переселение мусульман из Мекки в Медину (622 н.э.)',
                     'en': 'The Hijrah from Mecca to Medina (622 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Hijrat yili (622 yil) Islomiy qamariy hijriy taqvimning birinchi yili etib belgilangan.',
               'ru': '622 год стал точкой отсчета мусульманского лунного календаря — Хиджры.',
               'en': "The year 622 AD marks the start of the Islamic lunar calendar following the Prophet's journey to "
                     'Medina.'},
  'aliases': ['hijrat', 'hijra', 'хиджра', 'hijrah']},
 {'id': 'hist_time_012',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Makkaning fath etilishi (milodiy 630)',
                     'Sosoniylar poytaxti Ktesifonning fath etilishi (milodiy 637)',
                     "Toriq ibn Ziyodning Ispaniyaga (Andalusiya) o'tishi (milodiy 711)",
                     "Badr jangi bo'lib o'tishi (milodiy 624)"],
              'ru': ['Взятие Мекки мусульманами (630 н.э.)',
                     'Взятие Ктесифона арабами (637 н.э.)',
                     'Высадка Тарика ибн Зияда в Испании (711 н.э.)',
                     'Битва при Бадре (624 н.э.)'],
              'en': ['Conquest of Mecca (630 AD)',
                     'Capture of Ctesiphon (637 AD)',
                     'Tariq ibn Ziyad lands in Hispania (711 AD)',
                     'Battle of Badr (624 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Badr jangi bo'lib o'tishi (milodiy 624)",
                     'ru': 'Битва при Бадре (624 н.э.)',
                     'en': 'Battle of Badr (624 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Badr jangi ilk musulmonlar tarixidagi eng muhim va hal qiluvchi janglardan biri bo'lgan.",
               'ru': 'Битва при Бадре стала первой крупной победой ранней мусульманской общины.',
               'en': 'The Battle of Badr in 624 was a pivotal victory that solidified early Muslim political '
                     'influence.'},
  'aliases': ['badr', 'badr jangi', 'битва при бадре', 'battle of badr']},
 {'id': 'hist_time_013',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Talas daryosi bo'yidagi mashhur jang (milodiy 751)",
                     'Buyuk Karl Rim papasi tomonidan toj kiyishi (milodiy 800)',
                     'Somoniylar davlatining tashkil topishi (milodiy 819)',
                     'Gastings jangi va Angliyaning normandlar tomonidan zabt etilishi (milodiy 1066)'],
              'ru': ['Битва на реке Талас (751 н.э.)',
                     'Коронация Карла Великого (800 н.э.)',
                     'Основание государства Саманидов (819 н.э.)',
                     'Битва при Гастингсе в Англии (1066 н.э.)'],
              'en': ['Battle of Talas (751 AD)',
                     'Imperial coronation of Charlemagne (800 AD)',
                     'Establishment of the Samanid state (819 AD)',
                     'Battle of Hastings (1066 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Talas daryosi bo'yidagi mashhur jang (milodiy 751)",
                     'ru': 'Битва на реке Талас (751 н.э.)',
                     'en': 'Battle of Talas (751 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Talas jangi Xitoyning Tan sulolasi ekspansiyasini to'xtatgan va eng muhimi, qog'oz ishlab "
                     'chiqarish sirini Samarqand orqali butun dunyoga yoygan.',
               'ru': 'Таласская битва остановила продвижение империи Тан на запад и познакомила исламский мир с '
                     'секретом китайской бумаги через Самарканд.',
               'en': 'The Battle of Talas halted Chinese westward expansion and brought Chinese paper-making knowledge '
                     'to Samarkand.'},
  'aliases': ['talas', 'talas jangi', 'битва на таласе', 'battle of talas']},
 {'id': 'hist_time_014',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Verden shartnomasi bilan Franklar imperiyasining bo'linishi (milodiy 843)",
                     "Buyuk Karlning Rimda imperator deb e'lon qilinishi (milodiy 800)",
                     'Kiyev Rusining xristianlikni qabul qilishi (milodiy 988)',
                     'Birinchi Salib yurishi qatnashchilari Quddusni egallashi (milodiy 1099)'],
              'ru': ['Верденский договор о разделе империи (843 н.э.)',
                     'Коронация Карла Великого в Риме (800 н.э.)',
                     'Крещение Руси князем Владимиром (988 н.э.)',
                     'Взятие Иерусалима крестоносцами (1099 н.э.)'],
              'en': ['Treaty of Verdun partitioning the Empire (843 AD)',
                     'Coronation of Charlemagne as Emperor (800 AD)',
                     'Baptism of Kievan Rus (988 AD)',
                     'First Crusade captures Jerusalem (1099 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Buyuk Karlning Rimda imperator deb e'lon qilinishi (milodiy 800)",
                     'ru': 'Коронация Карла Великого в Риме (800 н.э.)',
                     'en': 'Coronation of Charlemagne as Emperor (800 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Buyuk Karl 800 yil Rojdestvo kuni Papa Lev III tomonidan imperator tojini kiyib, Karolinglar '
                     "uyg'onish davrini boshlab bergan.",
               'ru': 'Папа Лев III короновал Карла Великого на Рождество 800 года, возродив титул императора на '
                     'Западе.',
               'en': "Charlemagne's coronation on Christmas Day 800 AD laid the foundation for medieval Western "
                     'European statehood.'},
  'aliases': ['buyuk karl', 'karl', 'карл великий', 'charlemagne']},
 {'id': 'hist_time_015',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["G'aznaviylar davlatiga asos solinishi (milodiy 977)",
                     "Dandanaqon jangi va Saljuqiylar g'alabasi (milodiy 1040)",
                     'Somoniylar davlatining tashkil topishi (milodiy 819)',
                     'Anushtegin Xorazmshohlar sulolasiga asos solishi (milodiy 1077)'],
              'ru': ['Основание государства Газневидов (977 н.э.)',
                     'Битва при Данданакане сельджуков (1040 н.э.)',
                     'Основание государства Саманидов (819 н.э.)',
                     'Основание династии Хорезмшахов Ануштегином (1077 н.э.)'],
              'en': ['Founding of the Ghaznavid Empire (977 AD)',
                     'Battle of Dandanaqan (1040 AD)',
                     'Founding of the Samanid state (819 AD)',
                     'Anushtegin founds Khwarazmshah dynasty (1077 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Somoniylar davlatining tashkil topishi (milodiy 819)',
                     'ru': 'Основание государства Саманидов (819 н.э.)',
                     'en': 'Founding of the Samanid state (819 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Somoniylar davrida Buxoro jahon ilmi va madaniyatining poytaxtiga aylangan, Ibn Sino va Beruniy '
                     'kabi daho olimlar yetishib chiqqan.',
               'ru': 'При Саманидах Бухара стала одним из величайших интеллектуальных центров мира, подарив '
                     'человечеству Ибн Сину и Рудаки.',
               'en': 'Under the Samanids, Bukhara became a radiant cultural hub of the Islamic Golden Age, home to '
                     'Avicenna and Rudaki.'},
  'aliases': ['somoniylar', 'ismoil somoniy', 'саманиды', 'samanid']},
 {'id': 'hist_time_016',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Kiyev knyazi Vladimirning Rusni cho'qintirishi (milodiy 988)",
                     "Yaroslav Mudriy 'Rus haqiqati' qonunlarini qabul qilishi (milodiy 1016)",
                     "Kalka daryosi bo'yidagi mo'g'ullar bilan jang (milodiy 1223)",
                     'Ryurikning Novgorodga kelishi va Rus davlatchiligiga asos solinishi (milodiy 862)'],
              'ru': ['Крещение Руси князем Владимиром (988 н.э.)',
                     'Создание «Русской Правды» Ярославом Мудрым (1016 н.э.)',
                     'Битва на реке Калке против монголов (1223 н.э.)',
                     'Призвание варягов и правление Рюрика (862 н.э.)'],
              'en': ['Christianization of Kievan Rus (988 AD)',
                     'Yaroslav the Wise codifies Russkaya Pravda (1016 AD)',
                     'Battle of the Kalka River against Mongols (1223 AD)',
                     'Arrival of Rurik founding the Rurikid dynasty (862 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ryurikning Novgorodga kelishi va Rus davlatchiligiga asos solinishi (milodiy 862)',
                     'ru': 'Призвание варягов и правление Рюрика (862 н.э.)',
                     'en': 'Arrival of Rurik founding the Rurikid dynasty (862 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Ryurik sulolasi 862 yildan to 1598 yilgacha, ya'ni Fyodor Ioannovich vafotigacha 700 yildan "
                     'ortiq hukmronlik qilgan.',
               'ru': 'Династия Рюриковичей правила более семи веков — вплоть до конца XVI столетия.',
               'en': 'The Rurikid dynasty ruled from 862 until 1598, encompassing over seven centuries of Eastern '
                     'European history.'},
  'aliases': ['ryurik', 'rus davlatchiligi', 'рюрик', 'призвание варягов', 'rurik']},
 {'id': 'hist_time_017',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Xristian cherkovining pravoslav va katolik bo'lib bo'linishi (Buyuk ajralish) (milodiy 1054)",
                     "Gastings jangi bo'lib o'tishi (milodiy 1066)",
                     'Malazgirt (Manzikert) jangi (milodiy 1071)',
                     "Papa Urban II Klermonda Birinchi Salib yurishini e'lon qilishi (milodiy 1095)"],
              'ru': ['Великая схизма — раскол христианской церкви (1054 н.э.)',
                     'Битва при Гастингсе (1066 н.э.)',
                     'Битва при Манцикерте (1071 н.э.)',
                     'Клермонский собор и призыв к крестовому походу (1095 н.э.)'],
              'en': ['The Great Schism of the Christian Church (1054 AD)',
                     'Battle of Hastings (1066 AD)',
                     'Battle of Manzikert (1071 AD)',
                     'Council of Clermont calling First Crusade (1095 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Xristian cherkovining pravoslav va katolik bo'lib bo'linishi (Buyuk ajralish) (milodiy "
                           '1054)',
                     'ru': 'Великая схизма — раскол христианской церкви (1054 н.э.)',
                     'en': 'The Great Schism of the Christian Church (1054 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "1054 yilda Rim papasi elchilari va Konstantinopol patriarxi bir-birlarini cherkovdan badarg'a "
                     '(anofema) qilishgan.',
               'ru': 'В 1054 году папские легаты и патриарх Михаил Керуларий предали друг друга анафеме, разделив '
                     'католиков и православных.',
               'en': 'In 1054, Rome and Constantinople mutually excommunicated each other, cementing the East-West '
                     'Schism.'},
  'aliases': ['buyuk ajralish', 'cherkov ajralishi', 'великая схизма', 'раскол церкви', 'great schism']},
 {'id': 'hist_time_018',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Salohiddin Ayyubiy Quddusni salibchilardan ozod qilishi (milodiy 1187)',
                     'Gastings jangi — Vilgelm Fathchi Angliyani egallashi (milodiy 1066)',
                     "To'rtinchi Salib yurishida Konstantinopolning talanishi (milodiy 1204)",
                     "Xulogu xonning Bag'dodni zabt etishi va xalifalikning tugashi (milodiy 1258)"],
              'ru': ['Освобождение Иерусалима Саладином (1187 н.э.)',
                     'Битва при Гастингсе — нормандское завоевание Англии (1066 н.э.)',
                     'Разграбление Константинополя крестоносцами (1204 н.э.)',
                     'Падение Багдада под ударами монголов Хулагу (1258 н.э.)'],
              'en': ['Saladin recaptures Jerusalem (1187 AD)',
                     'Battle of Hastings — Norman conquest of England (1066 AD)',
                     'Crusaders sack Constantinople (1204 AD)',
                     'Mongols sack Baghdad ending Caliphate (1258 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Gastings jangi — Vilgelm Fathchi Angliyani egallashi (milodiy 1066)',
                     'ru': 'Битва при Гастингсе — нормандское завоевание Англии (1066 н.э.)',
                     'en': 'Battle of Hastings — Norman conquest of England (1066 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Gastings jangidagi g'alaba natijasida ingliz tiliga minglab fransuzcha so'zlar kirib kelgan va "
                     "ingliz qirolligi tili o'zgargan.",
               'ru': 'Победа Вильгельма Завоевателя при Гастингсе навсегда изменила английский язык, наполнив его '
                     'старофранцузской лексикой.',
               'en': 'The Norman victory at Hastings in 1066 dramatically transformed the English language with an '
                     'influx of French vocabulary.'},
  'aliases': ['gastings', 'gastings jangi', 'битва при гастингсе', 'battle of hastings']},
 {'id': 'hist_time_019',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Sorbonna / Parij universitetiga rasmiy nizom berilishi (milodiy 1200)',
                     'Kembrij universitetiga asos solinishi (milodiy 1209)',
                     "Oksford universitetida ta'lim berish boshlanishi (~milodiy 1096)",
                     'Pragadagi Karl universitetining ochilishi (milodiy 1348)'],
              'ru': ['Учреждение Парижского университета (1200 н.э.)',
                     'Основание Кембриджского университета (1209 н.э.)',
                     'Начало преподавания в Оксфорде (~1096 н.э.)',
                     'Основание Карлова университета в Праге (1348 н.э.)'],
              'en': ['Chartering of the University of Paris (1200 AD)',
                     'Founding of the University of Cambridge (1209 AD)',
                     'Teaching begins at University of Oxford (~1096 AD)',
                     'Founding of Charles University in Prague (1348 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Oksford universitetida ta'lim berish boshlanishi (~milodiy 1096)",
                     'ru': 'Начало преподавания в Оксфорде (~1096 н.э.)',
                     'en': 'Teaching begins at University of Oxford (~1096 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Oksford universiteti ingliz tilidagi dunyoning eng qadimgi universiteti hisoblanadi (1096 yildan '
                     'darslar olib boriladi).',
               'ru': 'Оксфорд — старейший англоязычный университет в мире, непрерывно работающий с конца XI века.',
               'en': 'Oxford is the oldest university in the English-speaking world, with evidence of teaching dating '
                     'back to 1096.'},
  'aliases': ['oksford', 'oksford universiteti', 'оксфорд', 'oxford']},
 {'id': 'hist_time_020',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Mo'g'ullarning Bag'dodni vayron qilishi (milodiy 1258)",
                     'Marko Poloning Xitoyga sayohati boshlanishi (milodiy 1271)',
                     "Angliya va Fransiya o'rtasida Yuz yillik urush boshlanishi (milodiy 1337)",
                     "Angliyada 'Buyuk erkinliklar xartiyasi' (Magna Carta) qabul qilinishi (milodiy 1215)"],
              'ru': ['Монгольское разорение Багдада (1258 н.э.)',
                     'Начало путешествия Марко Поло в Китай (1271 н.э.)',
                     'Начало Столетней войны (1337 н.э.)',
                     'Подписание Великой хартии вольностей в Англии (1215 н.э.)'],
              'en': ['Mongol destruction of Baghdad (1258 AD)',
                     'Marco Polo begins travels to China (1271 AD)',
                     "Outbreak of the Hundred Years' War (1337 AD)",
                     'Signing of Magna Carta in England (1215 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Angliyada 'Buyuk erkinliklar xartiyasi' (Magna Carta) qabul qilinishi (milodiy 1215)",
                     'ru': 'Подписание Великой хартии вольностей в Англии (1215 н.э.)',
                     'en': 'Signing of Magna Carta in England (1215 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Magna Carta qirol hokimiyatini qonun bilan cheklagan tarixiy hujjat bo'lib, zamonaviy "
                     'konstitutsiyaviylikning boshlanishi hisoblanadi.',
               'ru': 'Великая хартия вольностей 1215 года впервые в Европе ограничила власть монарха законом и правами '
                     'подданных.',
               'en': 'Magna Carta, signed in 1215, established that everyone—even the king—is subject to the rule of '
                     'law.'},
  'aliases': ['magna carta', 'buyuk erkinliklar xartiyasi', 'великая хартия вольностей', 'magna karta']},
 {'id': 'hist_time_021',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Temuchinning Buyuk Qurultoyda Chingizxon deb e'lon qilinishi (milodiy 1206)",
                     'Sind daryosi jangi: Jaloliddin Manguberdi jasorati (milodiy 1221)',
                     "Legnitsa va Moxiy janglari: mo'g'ullarning Yevropaga yurishi (milodiy 1241)",
                     "Xulogu xonning Bag'dodni zabt etishi (milodiy 1258)"],
              'ru': ['Провозглашение Темуджина Чингисханом на курултае (1206 н.э.)',
                     'Битва на реке Инд: подвиг Джалолиддина Мангуберди (1221 н.э.)',
                     'Битва при Легнице и вторжение монголов в Европу (1241 н.э.)',
                     'Захват Багдада войском Хулагу (1258 н.э.)'],
              'en': ['Temujin proclaimed Genghis Khan at the Kurultai (1206 AD)',
                     'Battle of the Indus: Jaloliddin Manguberdi (1221 AD)',
                     'Battle of Legnica: Mongols invade Central Europe (1241 AD)',
                     'Hulagu Khan sacks Baghdad (1258 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Temuchinning Buyuk Qurultoyda Chingizxon deb e'lon qilinishi (milodiy 1206)",
                     'ru': 'Провозглашение Темуджина Чингисханом на курултае (1206 н.э.)',
                     'en': 'Temujin proclaimed Genghis Khan at the Kurultai (1206 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "1206 yilda Onon daryosi bo'yidagi qurultoyda barcha mo'g'ul qabilalari birlashtirilib, "
                     'Chingizxon unvoni berilgan.',
               'ru': 'В 1206 году на курултае на реке Онон Темуджин объединил кочевые племена и принял титул '
                     'Чингисхана.',
               'en': 'At the 1206 Kurultai on the Onon River, Temujin unified the steppe tribes and took the title '
                     'Genghis Khan.'},
  'aliases': ['chingizxon', 'chingizxon qurultoy', 'чингисхан', 'курултай', 'genghis khan']},
 {'id': 'hist_time_022',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Muz ustidagi jang (Chud ko'li jangi): Aleksandr Nevskiy g'alabasi (milodiy 1242)",
                     "Jaloliddin Manguberdining Parvon jangi va Sind daryosi bo'yidagi jangi (milodiy 1221)",
                     "Ayn Jolut jangi: mamluklarning mo'g'ullarni to'xtatishi (milodiy 1260)",
                     'Kulikovo jangi (milodiy 1380)'],
              'ru': ['Ледовое побоище на Чудском озере Александра Невского (1242 н.э.)',
                     'Битва при Парване и на реке Инд Джалолиддина Мангуберди (1221 н.э.)',
                     'Битва при Айн-Джалуте мамлюков против монголов (1260 н.э.)',
                     'Куликовская битва (1380 н.э.)'],
              'en': ['Battle on the Ice by Alexander Nevsky (1242 AD)',
                     "Jaloliddin Manguberdi's battles at Parwan and Indus (1221 AD)",
                     'Battle of Ain Jalut (1260 AD)',
                     'Battle of Kulikovo (1380 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Jaloliddin Manguberdining Parvon jangi va Sind daryosi bo'yidagi jangi (milodiy 1221)",
                     'ru': 'Битва при Парване и на реке Инд Джалолиддина Мангуберди (1221 н.э.)',
                     'en': "Jaloliddin Manguberdi's battles at Parwan and Indus (1221 AD)"},
  'image_url': None,
  'fun_fact': {'uz': "Sind daryosi bo'yidagi jangda Jaloliddin o'z oti bilan baland qoyadan shiddatli daryoga "
                     "sakraganida, Chingizxon o'z o'g'illariga: 'Otaga mana shunday o'g'il kerak!' deb xitob qilgan.",
               'ru': 'Подвиг Джалолиддина Мангуберди на реке Инд вызвал восхищение самого Чингисхана, поставившего его '
                     'в пример своим сыновьям.',
               'en': 'Jaloliddin leaped on horseback into the swollen Indus River in 1221, earning the direct '
                     'admiration of Genghis Khan.'},
  'aliases': ['jaloliddin manguberdi', 'manguberdi', 'джалолиддин', 'мангуберди', 'jaloliddin']},
 {'id': 'hist_time_023',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Marko Polo Xubilayxon saroyiga yetib borishi (milodiy 1275)',
                     'Usmon I Usmonli bekligiga asos solishi (~milodiy 1299)',
                     "Ayn Jolut jangi — Qutuz boshchiligidagi mamluklar mo'g'ullarni mag'lub etishi (milodiy 1260)",
                     "Dante 'Ilohiy komediya' asarini yakunlashi (milodiy 1320)"],
              'ru': ['Прибытие Марко Поло ко двору Хубилая (1275 н.э.)',
                     'Основание Османского бейлика Османом I (~1299 н.э.)',
                     'Битва при Айн-Джалуте — победа мамлюков над монголами (1260 н.э.)',
                     'Завершение «Божественной комедии» Данте (1320 н.э.)'],
              'en': ["Marco Polo arrives at Kublai Khan's court (1275 AD)",
                     'Osman I founds the Ottoman principality (~1299 AD)',
                     'Battle of Ain Jalut: Mamluks halt Mongol advance (1260 AD)',
                     'Dante completes the Divine Comedy (1320 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Ayn Jolut jangi — Qutuz boshchiligidagi mamluklar mo'g'ullarni mag'lub etishi (milodiy "
                           '1260)',
                     'ru': 'Битва при Айн-Джалуте — победа мамлюков над монголами (1260 н.э.)',
                     'en': 'Battle of Ain Jalut: Mamluks halt Mongol advance (1260 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Ayn Jolut jangi mo'g'ul qo'shinlarining Yaqin Sharqdagi to'xtovsiz g'alabalariga chek qo'ygan va "
                     'Misrni saqlab qolgan.',
               'ru': 'Битва при Айн-Джалуте в Палестине развеяла миф о непобедимости монгольских туменов в полевом '
                     'сражении.',
               'en': 'Ain Jalut in 1260 was the first permanent defeat of a Mongol army in hand-to-hand field combat, '
                     'saving Cairo.'},
  'aliases': ['ayn jolut', 'ayn jalut', 'айн-джалут', 'battle of ain jalut']},
 {'id': 'hist_time_024',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Qora o'lat (vabo) epidemiyasining Yevropaga kirib kelishi (milodiy 1347)",
                     "Amir Temurning Samarqand taxtiga o'tirishi (milodiy 1370)",
                     'Kulikovo jangi (milodiy 1380)',
                     'Usmon I tomonidan Usmonli davlatiga asos solinishi (~milodiy 1299)'],
              'ru': ['Начало Черной смерти (пандемии чумы) в Европе (1347 н.э.)',
                     'Восшествие Амира Темура на престол в Самарканде (1370 н.э.)',
                     'Куликовская битва (1380 н.э.)',
                     'Основание Османского государства Османом I (~1299 н.э.)'],
              'en': ['Black Death arrives in Europe (1347 AD)',
                     'Amir Timur takes the throne in Samarkand (1370 AD)',
                     'Battle of Kulikovo (1380 AD)',
                     'Founding of the Ottoman state by Osman I (~1299 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Usmon I tomonidan Usmonli davlatiga asos solinishi (~milodiy 1299)',
                     'ru': 'Основание Османского государства Османом I (~1299 н.э.)',
                     'en': 'Founding of the Ottoman state by Osman I (~1299 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Usmon I asos solgan kichik turk bekligi 600 yildan ortiq davom etgan uch qit'ani egallagan buyuk "
                     'saltanatga aylandi.',
               'ru': 'Небольшой бейлик Османа Гази вырос в гигантскую Османскую империю, просуществовавшую более шести '
                     'веков.',
               'en': 'From a tiny Anatolian beylic founded around 1299, the Ottoman Empire grew to span three '
                     'continents for over 600 years.'},
  'aliases': ['usmon gazi', 'usmonli davlati', 'осман i', 'османская империя', 'osman i']},
 {'id': 'hist_time_025',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Qora o'lat (o'lat pandemiyasi) Yevropa va Osiyoda tarqalishi (milodiy 1346-1347)",
                     "Kulikovo jangi: Dmitriy Donskoy Mamay qo'shinini yengishi (milodiy 1380)",
                     'Kosovo maydonidagi jang (milodiy 1389)',
                     "Anqara jangi: Amir Temurning Boyazid I ustidan g'alabasi (milodiy 1402)"],
              'ru': ['Пандемия бубонной чумы («Черная смерть») (1346–1347 н.э.)',
                     'Куликовская битва Дмитрия Донского (1380 н.э.)',
                     'Битва на Косовом поле (1389 н.э.)',
                     'Ангорская битва Амира Темура с Баязидом I (1402 н.э.)'],
              'en': ['Outbreak of the Black Death plague in Europe (1346–1347 AD)',
                     'Battle of Kulikovo (1380 AD)',
                     'Battle of Kosovo (1389 AD)',
                     'Battle of Ankara: Timur defeats Bayezid I (1402 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Qora o'lat (o'lat pandemiyasi) Yevropa va Osiyoda tarqalishi (milodiy 1346-1347)",
                     'ru': 'Пандемия бубонной чумы («Черная смерть») (1346–1347 н.э.)',
                     'en': 'Outbreak of the Black Death plague in Europe (1346–1347 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Qora o'lat Yevropa aholisining uchdan bir qismini (25 milliondan ortiq insonni) nobud qilgan va "
                     "jamiyat tuzilishini butkul o'zgartirgan.",
               'ru': 'Черная смерть унесла жизни от 30% до 60% населения Европы, разрушив феодальную структуру.',
               'en': "The Black Death wiped out roughly one-third of Europe's population between 1347 and 1351."},
  'aliases': ['qora olat', 'vabo', 'черная смерть', 'чума', 'black death', 'plague']},
 {'id': 'hist_time_026',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Terek daryosi bo'yidagi jang: Temurning To'xtamish ustidan g'alabasi (milodiy 1395)",
                     "Amir Temurning Balx va Samarqandda oliy hukmdor deb e'lon qilinishi (milodiy 1370)",
                     'Anqara jangi (milodiy 1402)',
                     "Janna d'Ark Orlean qamalini yorib o'tishi (milodiy 1429)"],
              'ru': ['Битва на реке Терек Темура с Тохтамышем (1395 н.э.)',
                     'Провозглашение Амира Темура верховным эмиром (1370 н.э.)',
                     'Ангорская битва (1402 н.э.)',
                     "Снятие осады Орлеана Жанной д'Арк (1429 н.э.)"],
              'en': ['Battle of the Terek River against Tokhtamysh (1395 AD)',
                     'Amir Timur proclaimed Supreme Ruler in Samarkand (1370 AD)',
                     'Battle of Ankara (1402 AD)',
                     'Joan of Arc lifts the Siege of Orleans (1429 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Amir Temurning Balx va Samarqandda oliy hukmdor deb e'lon qilinishi (milodiy 1370)",
                     'ru': 'Провозглашение Амира Темура верховным эмиром (1370 н.э.)',
                     'en': 'Amir Timur proclaimed Supreme Ruler in Samarkand (1370 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Amir Temur 1370 yilda Samarqandni ulkan saltanat poytaxti qilib tanladi va uni dunyoning eng '
                     "go'zal shahriga aylantirdi.",
               'ru': 'В 1370 году Амир Темур объединил земли Мавераннахра и сделал Самарканд столицей одной из '
                     'величайших империй в истории.',
               'en': 'In 1370, Amir Timur took the reins of power and established Samarkand as the jewel capital of '
                     'Eurasia.'},
  'aliases': ['amir temur', 'temur taxtga otirishi', 'амир темур', 'тамерлан', 'amir timur', 'tamerlane']},
 {'id': 'hist_time_027',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Mirzo Ulug'bek Samarqand rasadxonasini qura boshlashi (milodiy 1424)",
                     'Konstantinopolning Sulton Mehmed II tomonidan zabt etilishi (milodiy 1453)',
                     'Anqara jangi — Amir Temur Usmonli sultoni Boyazid Yildirimni yengishi (milodiy 1402)',
                     'Xristofor Kolumbning Amerikaga ilk suzishi (milodiy 1492)'],
              'ru': ['Начало строительства обсерватории Улугбека (1424 н.э.)',
                     'Падение Константинополя под натиском турок (1453 н.э.)',
                     'Ангорская битва: победа Амира Темура над султаном Баязидом I (1402 н.э.)',
                     'Первая экспедиция Христофора Колумба (1492 н.э.)'],
              'en': ['Mirzo Ulugbek starts Samarkand Observatory (1424 AD)',
                     'Fall of Constantinople to Mehmed II (1453 AD)',
                     'Battle of Ankara: Timur defeats Sultan Bayezid I (1402 AD)',
                     'Christopher Columbus reaches the Americas (1492 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Anqara jangi — Amir Temur Usmonli sultoni Boyazid Yildirimni yengishi (milodiy 1402)',
                     'ru': 'Ангорская битва: победа Амира Темура над султаном Баязидом I (1402 н.э.)',
                     'en': 'Battle of Ankara: Timur defeats Sultan Bayezid I (1402 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Anqara jangidagi Temurning g'alabasi Vizantiya poytaxti Konstantinopolning qulashini roppa-rosa "
                     'yarim asrga (50 yilga) kechiktirgan.',
               'ru': 'Разгром Баязида I войском Темура отсрочил падение Константинополя на целых 50 лет.',
               'en': "Timur's crushing victory at Ankara in 1402 delayed the Ottoman conquest of Constantinople by "
                     'five decades.'},
  'aliases': ['anqara jangi', 'boyazid', 'ангорская битва', 'battle of ankara']},
 {'id': 'hist_time_028',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Gutenberg harakatlanuvchi metall harflar bilan bosma stanokni ixtiro qilishi (~milodiy 1440)',
                     'Konstantinopolning qulashi (milodiy 1453)',
                     "Alisher Navoiy 'Hamsa' asarini yakunlashi (milodiy 1485)",
                     "Mirzo Ulug'bek Samarqand rasadxonasini barpo etishi (milodiy 1424-1428)"],
              'ru': ['Изобретение книгопечатания Иоганном Гутенбергом (~1440 н.э.)',
                     'Взятие Константинополя Мехмедом Завоевателем (1453 н.э.)',
                     'Завершение «Хамсы» Алишером Навои (1485 н.э.)',
                     'Строительство обсерватории Улугбека в Самарканде (1424–1428 н.э.)'],
              'en': ['Gutenberg invents movable type printing press (~1440 AD)',
                     'Fall of Constantinople to Mehmed II (1453 AD)',
                     'Alisher Navoiy completes Hamsa (1485 AD)',
                     "Construction of Mirzo Ulugbek's Observatory (1424–1428 AD)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Mirzo Ulug'bek Samarqand rasadxonasini barpo etishi (milodiy 1424-1428)",
                     'ru': 'Строительство обсерватории Улугбека в Самарканде (1424–1428 н.э.)',
                     'en': "Construction of Mirzo Ulugbek's Observatory (1424–1428 AD)"},
  'image_url': None,
  'fun_fact': {'uz': "Ulug'bek rasadxonasida yulduzlar jadvali (Ziji Jadidi Koragoniy) teleskopsiz tuzilgan bo'lib, "
                     "hisob-kitoblar aniqligi bo'yicha XVII asrgacha tengsiz qolgan.",
               'ru': 'Секстант обсерватории Улугбека позволил составить каталог 1018 звезд с невероятной для XV века '
                     'точностью.',
               'en': "Ulugbek's massive Samarkand sextant catalogued 1,018 stars without a telescope, unmatched until "
                     'Tycho Brahe.'},
  'aliases': ['ulugbek', 'rasadxona', 'улугбек', 'обсерватория улугбека', 'ulugbek observatory']},
 {'id': 'hist_time_029',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Gutenbergning ilk bosma Injil kitobini chop etishi (milodiy 1455)',
                     "Leonardo da Vinchi 'Maxfiy kechlik' freskasini yaratishi (milodiy 1495-1498)",
                     "Vasko da Gama Hindistonga dengiz yo'lini ochishi (milodiy 1498)",
                     'Mikelandjelo Sikstin kapellasi shiftini chizishi (milodiy 1508-1512)'],
              'ru': ['Издание Библии Гутенберга наборным шрифтом (1455 н.э.)',
                     'Создание фрески «Тайная вечеря» Леонардо да Винчи (1495–1498 н.э.)',
                     'Открытие морского пути в Индию Васко да Гамой (1498 н.э.)',
                     'Роспись Сикстинской капеллы Микеланджело (1508–1512 н.э.)'],
              'en': ['Gutenberg prints the 42-Line Bible (1455 AD)',
                     'Leonardo da Vinci paints The Last Supper (1495–1498 AD)',
                     'Vasco da Gama reaches India (1498 AD)',
                     'Michelangelo paints Sistine Chapel ceiling (1508–1512 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Gutenbergning ilk bosma Injil kitobini chop etishi (milodiy 1455)',
                     'ru': 'Издание Библии Гутенберга наборным шрифтом (1455 н.э.)',
                     'en': 'Gutenberg prints the 42-Line Bible (1455 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Gutenberg matbaa stanogi bilimlarning keng omma orasida tarqalishiga turtki bo'lib, Renessans va "
                     'Ilmiy inqilobning poydevorini yaratdi.',
               'ru': 'Библия Гутенберга открыла эру печатного слова, сделав знания доступными миллионам людей.',
               'en': "Gutenberg's movable type Bible democratized literacy, igniting the European Renaissance and "
                     'Scientific Revolution.'},
  'aliases': ['gutenberg', 'gutenberg injili', 'гутенберг', 'библия гутенберга', 'gutenberg bible']},
 {'id': 'hist_time_030',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Ispaniyada Ferdinand va Izabella nikohi bilan davlatning birlashishi (milodiy 1469)',
                     'Konstantinopolning Usmonlilar tomonidan zabt etilishi va Vizantiyaning tugashi (milodiy 1453)',
                     "Ugra daryosi bo'yidagi turish: Rusda tatar-mo'g'ul zulmining tugashi (milodiy 1480)",
                     'Granada amirligining qulashi va Kolumbning birinchi ekspeditsiyasi (milodiy 1492)'],
              'ru': ['Брак Фердинанда и Изабеллы и объединение Испании (1469 н.э.)',
                     'Падение Константинополя и гибель Византийской империи (1453 н.э.)',
                     'Стояние на реке Угре и падение ордынского ига (1480 н.э.)',
                     'Падение Гранады и плавание Колумба (1492 н.э.)'],
              'en': ['Marriage of Ferdinand and Isabella uniting Spain (1469 AD)',
                     'Fall of Constantinople ending Byzantine Empire (1453 AD)',
                     'Great Stand on the Ugra River (1480 AD)',
                     "Fall of Granada and Columbus's first voyage (1492 AD)"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Konstantinopolning Usmonlilar tomonidan zabt etilishi va Vizantiyaning tugashi (milodiy '
                           '1453)',
                     'ru': 'Падение Константинополя и гибель Византийской империи (1453 н.э.)',
                     'en': 'Fall of Constantinople ending Byzantine Empire (1453 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "1453 yil ko'pgina tarixchilar tomonidan O'rta asrlarning tugashi va Yangi davrning boshlanish "
                     'chegarasi deb hisoblanadi.',
               'ru': '1453 год традиционно считается многими историками концом Средневековья и началом Нового времени.',
               'en': 'Many historians treat the Fall of Constantinople in 1453 as the defining transition from the '
                     'Middle Ages to Modern history.'},
  'aliases': ['konstantinopol',
              '1453',
              'падение константинополя',
              'византия',
              'fall of constantinople',
              'constantinople']},
 {'id': 'hist_time_031',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Vasko da Gama Afrikani aylanib Hindistonga yetib borishi (milodiy 1498)',
                     "Martin Lyuter 95 ta tezisni e'lon qilib Reformatsiyani boshlashi (milodiy 1517)",
                     'Xristofor Kolumb kemalari Bagama orollariga (Amerika) yetib borishi (milodiy 1492)',
                     "Magellan ekspeditsiyasi ilk dunyo bo'ylab sayohatni yakunlashi (milodiy 1522)"],
              'ru': ['Васко да Гама приплывает в индийский Каликут (1498 н.э.)',
                     '95 тезисов Мартина Лютера и начало Реформации (1517 н.э.)',
                     'Экспедиция Колумба достигает берегов Америки (1492 н.э.)',
                     'Завершение кругосветного плавания Магеллана (1522 н.э.)'],
              'en': ['Vasco da Gama reaches Calicut in India (1498 AD)',
                     'Martin Luther posts his 95 Theses (1517 AD)',
                     'Columbus reaches the Americas (1492 AD)',
                     "Magellan's expedition completes circumnavigation (1522 AD)"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Xristofor Kolumb kemalari Bagama orollariga (Amerika) yetib borishi (milodiy 1492)',
                     'ru': 'Экспедиция Колумба достигает берегов Америки (1492 н.э.)',
                     'en': 'Columbus reaches the Americas (1492 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Kolumb o'z hayotining oxirigacha Hindistonga yangi yo'l topdim deb hisoblagan, qit'a esa "
                     'keyinchalik Amerigo Vespuchchi nomi bilan atalgan.',
               'ru': 'Колумб до конца жизни полагал, что открыл западный путь в Азию, поэтому коренных жителей назвал '
                     'индейцами.',
               'en': "Columbus died believing he had reached Asia, which is why the Caribbean was termed the 'West "
                     "Indies'."},
  'aliases': ['kolumb', 'amerikani kashf qilish', 'колумб', 'открытие америки', 'columbus']},
 {'id': 'hist_time_032',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Zahiriddin Muhammad Boburning Kobulni egallashi (milodiy 1504)',
                     "Boburning Panipat jangida Ibrohim Lo'diy ustidan g'alaba qozonishi (milodiy 1526)",
                     'Ivan Grozniyning birinchi rus podshosi deb toj kiyishi (milodiy 1547)',
                     "Alisher Navoiy o'zbek tilidagi ilk 'Hamsa' (Besh doston)ni yakunlashi (milodiy 1485)"],
              'ru': ['Взятие Кабула Бабуром (1504 н.э.)',
                     'Битва при Панипате и победа Бабура (1526 н.э.)',
                     'Венчание на царство Ивана Грозного (1547 н.э.)',
                     'Алишер Навои завершает поэму «Хамса» на тюркском языке (1485 н.э.)'],
              'en': ['Babur captures Kabul (1504 AD)',
                     'Babur wins First Battle of Panipat (1526 AD)',
                     'Coronation of Ivan the Terrible as Tsar (1547 AD)',
                     'Alisher Navoiy completes the epic Hamsa (1485 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Alisher Navoiy o'zbek tilidagi ilk 'Hamsa' (Besh doston)ni yakunlashi (milodiy 1485)",
                     'ru': 'Алишер Навои завершает поэму «Хамса» на тюркском языке (1485 н.э.)',
                     'en': 'Alisher Navoiy completes the epic Hamsa (1485 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Navoiy 'Hamsa'ni atigi ikki yilda turkiy (o'zbek) tilida yozib, turkiy tilning forsiy til kabi "
                     'boy va qudratli ekanligini isbotlagan.',
               'ru': 'Навои создал первую «Пятерицу» на староузбекском языке, доказав непревзойденное богатство '
                     'тюркского поэтического слова.',
               'en': 'Navoiy completed the first Turkic Hamsa in 1485, establishing Chagatai Turkic as a supreme '
                     'literary language.'},
  'aliases': ['navoiy', 'alisher navoiy', 'hamsa', 'навои', 'хамса', 'alisher navoi']},
 {'id': 'hist_time_033',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Martin Lyuter 95 tezisni Vittenberg cherkovi eshigiga qoqib qo'yishi (milodiy 1517)",
                     'Ernan Kortesning Atsteklar poytaxti Tenochtlitlanni zabt etishi (milodiy 1521)',
                     "Bobur tomonidan Boburiylar (Buyuk Mo'g'ullar) imperiyasiga asos solinishi (milodiy 1526)",
                     'Fransisko Pisarro Inklar imperiyasini zabt etishi (milodiy 1532)'],
              'ru': ['Мартин Лютер вывешивает 95 тезисов в Виттенберге (1517 н.э.)',
                     'Завоевание империи ацтеков Эрнаном Кортесом (1521 н.э.)',
                     'Основание империи Великих Моголов Бабуром (1526 н.э.)',
                     'Завоевание империи инков Франсиско Писарро (1532 н.э.)'],
              'en': ['Martin Luther posts 95 Theses in Wittenberg (1517 AD)',
                     'Hernan Cortes conquers Aztec Tenochtitlan (1521 AD)',
                     'Babur founds the Mughal Empire in India (1526 AD)',
                     'Francisco Pizarro conquers the Inca Empire (1532 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Martin Lyuter 95 tezisni Vittenberg cherkovi eshigiga qoqib qo'yishi (milodiy 1517)",
                     'ru': 'Мартин Лютер вывешивает 95 тезисов в Виттенберге (1517 н.э.)',
                     'en': 'Martin Luther posts 95 Theses in Wittenberg (1517 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Lyuterning indulgensiyalar sotilishiga qarshi noroziligi butun Yevropada protestantlik diniy '
                     "inqilobiga (Reformatsiyaga) sabab bo'ldi.",
               'ru': 'Выступление Лютера против продажи индульгенций раскололо католический мир и дало начало '
                     'протестантизму.',
               'en': "Luther's attack on papal indulgences in 1517 ignited the Protestant Reformation across Europe."},
  'aliases': ['martin lyuter', 'reformatsiya', 'мартин лютер', 'реформация', 'martin luther', 'reformation']},
 {'id': 'hist_time_034',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Angliya qiroli Genrix VIII Rim katolik cherkovi bilan aloqani uzishi (milodiy 1534)',
                     'Birinchi Panipat jangi — Bobur Hindistonda Boburiylar saltanatiga asos solishi (milodiy 1526)',
                     'Trident soborining ish boshlashi (milodiy 1545)',
                     "Ispan 'Yengilmas armada'sining inglizlar tomonidan tor-mor etilishi (milodiy 1588)"],
              'ru': ['Акт о супрематии Генриха VIII в Англии (1534 н.э.)',
                     'Первая битва при Панипате и основание империи Моголов Бабуром (1526 н.э.)',
                     'Открытие Тридентского собора (1545 н.э.)',
                     'Разгром испанской Непобедимой армады (1588 н.э.)'],
              'en': ['Henry VIII passes Act of Supremacy (1534 AD)',
                     'First Battle of Panipat: Babur founds Mughal Empire (1526 AD)',
                     'Opening of the Council of Trent (1545 AD)',
                     'Defeat of the Spanish Armada (1588 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Birinchi Panipat jangi — Bobur Hindistonda Boburiylar saltanatiga asos solishi (milodiy '
                           '1526)',
                     'ru': 'Первая битва при Панипате и основание империи Моголов Бабуром (1526 н.э.)',
                     'en': 'First Battle of Panipat: Babur founds Mughal Empire (1526 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Bobur Panipat jangida o'tsochar qurollar (to'plar) va 'to'lg'ama' jangovar usulidan mohirona "
                     "foydalanib, o'zidan 5 barobar katta qo'shinni yenggan.",
               'ru': 'Бабур использовал полевую артиллерию и тактику охвата флангов, разгромив стотысячную армию '
                     'делийского султана.',
               'en': 'Babur utilized matchlock muskets, carts, and flanking cavalry at Panipat in 1526 to crush the '
                     'massive Delhi Sultanate army.'},
  'aliases': ['panipat', 'bobur', 'панипат', 'бабур', 'babur', 'battle of panipat']},
 {'id': 'hist_time_035',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Ispan 'Yengilmas armada'sining La-Manshda tor-mor etilishi (milodiy 1588)",
                     'Niderlandiya Ost-Indiya kompaniyasining (VOC) tashkil topishi (milodiy 1602)',
                     "Lepanto dengiz jangi — Muqaddas liga Usmonli flotini to'xtatishi (milodiy 1571)",
                     "Shekspir 'Gamlet' tragediyasini yozishi (~milodiy 1600)"],
              'ru': ['Гибель испанской Непобедимой армады (1588 н.э.)',
                     'Основание Голландской Ост-Индской компании (1602 н.э.)',
                     'Морская битва при Лепанто (1571 н.э.)',
                     'Создание трагедии «Гамлет» Шекспиром (~1600 н.э.)'],
              'en': ['Defeat of the Spanish Armada (1588 AD)',
                     'Chartering of the Dutch East India Company (1602 AD)',
                     'Naval Battle of Lepanto (1571 AD)',
                     'Shakespeare writes Hamlet (~1600 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Lepanto dengiz jangi — Muqaddas liga Usmonli flotini to'xtatishi (milodiy 1571)",
                     'ru': 'Морская битва при Лепанто (1571 н.э.)',
                     'en': 'Naval Battle of Lepanto (1571 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Lepanto jangi eshkakli kemalar (galeralar) o'rtasidagi jahon tarixidagi eng so'nggi yirik dengiz "
                     "jangi bo'lib, unda Servantes ham jang qilgan va yaralangan.",
               'ru': 'В битве при Лепанто участвовал будущий автор «Дон Кихота» Мигель де Сервантес, потерявший в бою '
                     'левую руку.',
               'en': 'Lepanto was the last major naval engagement between rowing galleys; author Miguel de Cervantes '
                     'was wounded in the battle.'},
  'aliases': ['lepanto', 'lepanto jangi', 'лепанто', 'битва при лепанто', 'battle of lepanto']},
 {'id': 'hist_time_036',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Galiley Yupiter yo'ldoshlarini kashf etishi (milodiy 1610)",
                     'Meyflauer kemasida ziyoratchilarning (Pilgrimlar) Amerikaga kelishi (milodiy 1620)',
                     'Shoh Jahon Toj Mahal maqbarasini qura boshlashi (milodiy 1632)',
                     'Jeymstaun — Amerikadagi ilk doimiy ingliz posyolkasiga asos solinishi (milodiy 1607)'],
              'ru': ['Открытие Галилеем спутников Юпитера (1610 н.э.)',
                     'Прибытие отцов-пилигримов на корабле «Мейфлауэр» (1620 н.э.)',
                     'Начало строительства Тадж-Махала Шах-Джаханом (1632 н.э.)',
                     'Основание Джеймстауна — первой английской колонии в Америке (1607 н.э.)'],
              'en': ['Galileo discovers moons of Jupiter (1610 AD)',
                     'Mayflower arrives with Pilgrims (1620 AD)',
                     'Shah Jahan begins building the Taj Mahal (1632 AD)',
                     'Founding of Jamestown, first permanent English colony (1607 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jeymstaun — Amerikadagi ilk doimiy ingliz posyolkasiga asos solinishi (milodiy 1607)',
                     'ru': 'Основание Джеймстауна — первой английской колонии в Америке (1607 н.э.)',
                     'en': 'Founding of Jamestown, first permanent English colony (1607 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Virjiniyadagi Jeymstaun posyolkasi orqali Shimoliy Amerikada ingliz mustamlakachiligi va '
                     'kelajakdagi AQSh davlatchiligi boshlangan.',
               'ru': 'Джеймстаун, названный в честь короля Якова I, стал колыбелью британской колонизации Северной '
                     'Америки.',
               'en': 'Jamestown was established in Virginia in 1607, surviving disease and famine to launch English '
                     'settlement in North America.'},
  'aliases': ['jeymstaun', 'jamestown', 'джеймстаун']},
 {'id': 'hist_time_037',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Galileo Galiley teleskop orqali Yupiterning 4 ta yo'ldoshini kashf etishi (milodiy 1610)",
                     "Yevropada O'ttiz yillik urushning boshlanishi (milodiy 1618)",
                     'Hindistonda Toj Mahal qurilishi boshlanishi (milodiy 1632)',
                     'Vestfaliya tinchlik shartnomasi imzolanishi (milodiy 1648)'],
              'ru': ['Открытие Галилео Галилеем спутников Юпитера через телескоп (1610 н.э.)',
                     'Начало Тридцатилетней войны в Европе (1618 н.э.)',
                     'Строительство Тадж-Махала в Агре (1632 н.э.)',
                     'Подписание Вестфальского мира (1648 н.э.)'],
              'en': ["Galileo observes Jupiter's moons with telescope (1610 AD)",
                     "Outbreak of the Thirty Years' War (1618 AD)",
                     'Construction of Taj Mahal begins (1632 AD)',
                     'Signing of the Peace of Westphalia (1648 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Galileo Galiley teleskop orqali Yupiterning 4 ta yo'ldoshini kashf etishi (milodiy 1610)",
                     'ru': 'Открытие Галилео Галилеем спутников Юпитера через телескоп (1610 н.э.)',
                     'en': "Galileo observes Jupiter's moons with telescope (1610 AD)"},
  'image_url': None,
  'fun_fact': {'uz': "Galiley Yupiter atrofida aylanayotgan yo'ldoshlarni ko'rib, hamma narsa Yer atrofida "
                     'aylanmasligini isbotlagan va Kopernik nazariyasini tasdiqlagan.',
               'ru': 'Открытие спутников Юпитера стало неопровержимым доказательством правоты гелиоцентрической '
                     'системы Коперника.',
               'en': "Galileo's discovery of Io, Europa, Ganymede, and Callisto proved that celestial bodies could "
                     'orbit something other than Earth.'},
  'aliases': ['galiley', 'galileo', 'yupiter', 'галилей', 'галилео']},
 {'id': 'hist_time_038',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Angliya qiroli Karl I ning inqilob davrida qatl etilishi (milodiy 1649)',
                     "Praga defenestratsiyasi va O'ttiz yillik urushning boshlanishi (milodiy 1618)",
                     "London Buyuk yong'ini shahar markazini kul qilishi (milodiy 1666)",
                     'Vena jangi — Usmonlilar qamalining yorib tashlanishi (milodiy 1683)'],
              'ru': ['Казнь короля Карла I в ходе Английской революции (1649 н.э.)',
                     'Пражская дефенестрация и начало Тридцатилетней войны (1618 н.э.)',
                     'Великий лондонский пожар (1666 н.э.)',
                     'Венская битва и разгром османской армии (1683 н.э.)'],
              'en': ['Execution of King Charles I of England (1649 AD)',
                     "Defenestration of Prague starts Thirty Years' War (1618 AD)",
                     'Great Fire of London (1666 AD)',
                     'Battle of Vienna repels Ottoman siege (1683 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Praga defenestratsiyasi va O'ttiz yillik urushning boshlanishi (milodiy 1618)",
                     'ru': 'Пражская дефенестрация и начало Тридцатилетней войны (1618 н.э.)',
                     'en': "Defenestration of Prague starts Thirty Years' War (1618 AD)"},
  'image_url': None,
  'fun_fact': {'uz': "O'ttiz yillik urush Yevropadagi so'nggi yirik diniy urush bo'lib, nemis knyazliklari aholisining "
                     'deyarli uchdan bir qismi qirilib ketgan.',
               'ru': 'Тридцатилетняя война унесла жизни до трети населения германских земель и перекроила карту '
                     'Европы.',
               'en': "The Thirty Years' War devastated Central Europe, reducing German regional populations by up to "
                     '30 percent.'},
  'aliases': ['ottiz yillik urush', 'тридцатилетняя война', 'thirty years war', 'praga']},
 {'id': 'hist_time_039',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Londonda vabo (Buyuk o'lat) tarqalishi (milodiy 1665)",
                     "Isaak Nyuton 'Tabiat falsafasining matematik asoslari' kitobini chop etishi (milodiy 1687)",
                     'Vestfaliya tinchlik shartnomasi imzolanib, milliy suverenitet tizimi yaratilishi (milodiy 1648)',
                     "Pyotr I ning Yevropaga 'Buyuk elchilik' safari (milodiy 1697)"],
              'ru': ['Великая чума в Лондоне (1665 н.э.)',
                     'Исаак Ньютон публикует «Математические начала натуральной философии» (1687 н.э.)',
                     'Вестфальский мир и создание системы суверенных государств (1648 н.э.)',
                     'Великое посольство Петра I в Западную Европу (1697 н.э.)'],
              'en': ['Great Plague of London (1665 AD)',
                     'Newton publishes Principia Mathematica (1687 AD)',
                     'Peace of Westphalia establishes modern state sovereignty (1648 AD)',
                     "Peter the Great's Grand Embassy to Europe (1697 AD)"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Vestfaliya tinchlik shartnomasi imzolanib, milliy suverenitet tizimi yaratilishi (milodiy '
                           '1648)',
                     'ru': 'Вестфальский мир и создание системы суверенных государств (1648 н.э.)',
                     'en': 'Peace of Westphalia establishes modern state sovereignty (1648 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Vestfaliya tinchligi zamonaviy xalqaro munosabatlar tizimiga asos solib, davlatlarning '
                     "mustaqilligi va tengligi tamoyilini o'rnatdi.",
               'ru': 'Вестфальский мир 1648 года заложил основы современного международного права и концепцию '
                     'государственного суверенитета.',
               'en': 'The Peace of Westphalia in 1648 created the concept of nation-state sovereignty that underpins '
                     'global diplomacy today.'},
  'aliases': ['vestfaliya', 'vestfaliya tinchligi', 'вестфальский мир', 'peace of westphalia']},
 {'id': 'hist_time_040',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Vena jangi: Yan Sobeskiy boshchiligidagi qutqaruv (milodiy 1683)',
                     "Angliyada 'Huquqlar to'g'risida bill' qabul qilinishi (milodiy 1689)",
                     'Sankt-Peterburg shahriga asos solinishi (milodiy 1703)',
                     "London Buyuk yong'ini (milodiy 1666)"],
              'ru': ['Венская битва Яна Собеского (1683 н.э.)',
                     'Билль о правах в Англии (1689 н.э.)',
                     'Основание Санкт-Петербурга Петром I (1703 н.э.)',
                     'Великий пожар в Лондоне (1666 н.э.)'],
              'en': ['Battle of Vienna by Jan Sobieski (1683 AD)',
                     'English Bill of Rights enacted (1689 AD)',
                     'Founding of Saint Petersburg (1703 AD)',
                     'The Great Fire of London (1666 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "London Buyuk yong'ini (milodiy 1666)",
                     'ru': 'Великий пожар в Лондоне (1666 н.э.)',
                     'en': 'The Great Fire of London (1666 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "London yong'ini 13 000 dan ortiq uyni va eski Avliyo Pavel soborini yoqib yuborgan, biroq "
                     'shaharni oldingi yildagi vabodan butunlay tozalagan.',
               'ru': 'Великий пожар бушевал 4 дня, уничтожив 87 церквей, но одновременно остановил эпидемию чумы в '
                     'городе.',
               'en': 'The Great Fire burned for 4 days in 1666, destroying 13,200 houses and purging London of the '
                     'bubonic plague.'},
  'aliases': ['london yongini', 'великий пожар в лондоне', 'great fire of london']},
 {'id': 'hist_time_041',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Isaak Nyuton 'Principia' (Butunjahon tortishish qonuni) asarini nashr etishi (milodiy 1687)",
                     'Poltava jangi: Pyotr I shved qiroli Karl XII ni tor-mor qilishi (milodiy 1709)',
                     'Gabriel Farengeyt simobli termometrni ixtiro qilishi (milodiy 1714)',
                     "Jeyms Uatt bug' mashinasini takomillashtirib patentlashi (milodiy 1769)"],
              'ru': ['Исаак Ньютон публикует труд о всемирном тяготении (1687 н.э.)',
                     'Полтавская битва Петра I со шведами (1709 н.э.)',
                     'Изобретение ртутного термометра Фаренгейтом (1714 н.э.)',
                     'Патент паровой машины Джеймса Уатта (1769 н.э.)'],
              'en': ['Isaac Newton publishes Principia Mathematica (1687 AD)',
                     'Battle of Poltava (1709 AD)',
                     'Fahrenheit invents mercury thermometer (1714 AD)',
                     'James Watt patents separate condenser steam engine (1769 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Isaak Nyuton 'Principia' (Butunjahon tortishish qonuni) asarini nashr etishi (milodiy "
                           '1687)',
                     'ru': 'Исаак Ньютон публикует труд о всемирном тяготении (1687 н.э.)',
                     'en': 'Isaac Newton publishes Principia Mathematica (1687 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Nyutonning 'Principia' kitobi klassik mexanikaning 3 ta qonuni va butunjahon tortishish qonunini "
                     "bayon qilib, zamonaviy fizika asosini qo'ydi.",
               'ru': 'Труд Ньютона 1687 года сформулировал законы движения и тяготения, определив развитие науки на '
                     'века вперед.',
               'en': "Newton's Principia stated the three laws of motion and universal gravitation, forming the "
                     'foundation of modern physics.'},
  'aliases': ['nyuton', 'principia', 'ньютон', 'newton']},
 {'id': 'hist_time_042',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Poltava jangi bo'lib o'tishi (milodiy 1709)",
                     "Boltiq bo'yida Sankt-Peterburg shahriga asos solinishi (milodiy 1703)",
                     'Plessi jangi: inglizlarning Bengaliyani zabt etishi (milodiy 1757)',
                     "Boston choyxo'rligi — Amerika mustaqillik urushi debochasi (milodiy 1773)"],
              'ru': ['Полтавская битва (1709 н.э.)',
                     'Основание Санкт-Петербурга на Неве (1703 н.э.)',
                     'Битва при Плесси в Индии (1757 н.э.)',
                     '«Бостонское чаепитие» в Америке (1773 н.э.)'],
              'en': ['Battle of Poltava (1709 AD)',
                     'Founding of Saint Petersburg on the Neva (1703 AD)',
                     'Battle of Plassey in Bengal (1757 AD)',
                     'The Boston Tea Party (1773 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Boltiq bo'yida Sankt-Peterburg shahriga asos solinishi (milodiy 1703)",
                     'ru': 'Основание Санкт-Петербурга на Неве (1703 н.э.)',
                     'en': 'Founding of Saint Petersburg on the Neva (1703 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Sankt-Peterburg botqoqliklar o'rnida Pyotr I tomonidan 'Yevropaga ochilgan darcha' sifatida "
                     "bunyod etilgan va 200 yildan ortiq poytaxt bo'lgan.",
               'ru': 'Санкт-Петербург строился как европейская столица России и «окно в Европу» на отвоеванных у '
                     'Швеции землях.',
               'en': "Peter the Great founded Saint Petersburg in 1703 as a maritime 'window to Europe', replacing "
                     'Moscow as capital.'},
  'aliases': ['peterburg', 'sankt-peterburg', 'петербург', 'санкт-петербург', 'saint petersburg']},
 {'id': 'hist_time_043',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Nodirshohning Dehliga yurishi va Tovus taxtini qo'lga kiritishi (milodiy 1739)",
                     'Yetti yillik urushning boshlanishi (milodiy 1756)',
                     "Nishtad tinchligi va Rossiyaning Imperiya deb e'lon qilinishi (milodiy 1721)",
                     'AQSh Mustaqillik deklaratsiyasining qabul qilinishi (milodiy 1776)'],
              'ru': ['Поход Надир-шаха на Дели и захват Павлиньего трона (1739 н.э.)',
                     'Начало Семилетней войны (1756 н.э.)',
                     'Провозглашение Российской империи Петром I (1721 н.э.)',
                     'Принятие Декларации независимости США (1776 н.э.)'],
              'en': ['Nader Shah invades Delhi taking Peacock Throne (1739 AD)',
                     "Start of the Seven Years' War (1756 AD)",
                     'Peter the Great proclaims the Russian Empire (1721 AD)',
                     'US Declaration of Independence (1776 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Nishtad tinchligi va Rossiyaning Imperiya deb e'lon qilinishi (milodiy 1721)",
                     'ru': 'Провозглашение Российской империи Петром I (1721 н.э.)',
                     'en': 'Peter the Great proclaims the Russian Empire (1721 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Shimoliy urushda Shvetsiya ustidan qozonilgan g'alabadan so'ng Senat Pyotr I ga 'Buyuk' va "
                     "'Butunrossiya imperatori' unvonini bergan.",
               'ru': 'В октябре 1721 года Россия официально стала империей, закрепив статус великой мировой державы.',
               'en': 'In 1721, following victory in the Great Northern War, the Senate declared Peter Emperor, '
                     'establishing the Russian Empire.'},
  'aliases': ['rossiya imperiyasi', 'pyotr i', 'российская империя', 'russian empire']},
 {'id': 'hist_time_044',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Boston choyxo'rligi voqeasi (milodiy 1773)",
                     "AQSh Mustaqillik deklaratsiyasi e'lon qilinishi (milodiy 1776)",
                     "Bastiliya qal'asining egallanishi va Fransiya inqilobi boshlanishi (milodiy 1789)",
                     "Jeyms Uatt alohida kondensatorli bug' dvigateliga patent olishi (milodiy 1769)"],
              'ru': ['Бостонское чаепитие (1773 н.э.)',
                     'Декларация независимости США (1776 н.э.)',
                     'Взятие Бастилии в Париже (1789 н.э.)',
                     'Джеймс Уатт патентует конденсатор для паровой машины (1769 н.э.)'],
              'en': ['Boston Tea Party (1773 AD)',
                     'Declaration of Independence (1776 AD)',
                     'Storming of the Bastille in Paris (1789 AD)',
                     'James Watt patents separate condenser steam engine (1769 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Jeyms Uatt alohida kondensatorli bug' dvigateliga patent olishi (milodiy 1769)",
                     'ru': 'Джеймс Уатт патентует конденсатор для паровой машины (1769 н.э.)',
                     'en': 'James Watt patents separate condenser steam engine (1769 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Uattning bug' mashinasi Sanoat to'ntarilishining yuragi bo'lib, insoniyatni mexanizatsiyalashgan "
                     'davrga olib kirdi.',
               'ru': 'Усовершенствование паровой машины Уаттом стало двигателем Первой промышленной революции.',
               'en': "Watt's 1769 patent vastly increased steam engine efficiency, powering the Industrial "
                     'Revolution.'},
  'aliases': ['uatt', 'bug dvigateli', 'уатт', 'паровая машина', 'james watt', 'steam engine']},
 {'id': 'hist_time_045',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['AQSh Mustaqillik deklaratsiyasining Filadelfiyada qabul qilinishi (milodiy 1776)',
                     'AQSh Konstitutsiyasining ishlab chiqilishi (milodiy 1787)',
                     "Parijda Bastiliya qal'asining shturm qilinishi (milodiy 1789)",
                     'Fransiya qiroli Lyudovik XVI ning gilotinada qatl etilishi (milodiy 1793)'],
              'ru': ['Принятие Декларации независимости США в Филадельфии (1776 н.э.)',
                     'Принятие Конституции США (1787 н.э.)',
                     'Штурм Бастилии (1789 н.э.)',
                     'Казнь Людовика XVI (1793 н.э.)'],
              'en': ['United States Declaration of Independence adopted (1776 AD)',
                     'US Constitution drafted (1787 AD)',
                     'Storming of the Bastille (1789 AD)',
                     'Execution of Louis XVI (1793 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'AQSh Mustaqillik deklaratsiyasining Filadelfiyada qabul qilinishi (milodiy 1776)',
                     'ru': 'Принятие Декларации независимости США в Филадельфии (1776 н.э.)',
                     'en': 'United States Declaration of Independence adopted (1776 AD)'},
  'image_url': None,
  'fun_fact': {'uz': '1776 yil 4 iyulda qabul qilingan Tomas Jefferson qalamiga mansub deklaratsiya har bir insonning '
                     "'hayot, erkinlik va baxtga intilish' huquqini e'lon qildi.",
               'ru': 'Декларация 4 июля 1776 года провозгласила неотъемлемые права человека на жизнь, свободу и '
                     'стремление к счастью.',
               'en': 'Adopted on July 4, 1776, the Declaration declared all men created equal with rights to life, '
                     'liberty, and the pursuit of happiness.'},
  'aliases': ['aqsh mustaqilligi',
              'mustaqillik deklaratsiyasi',
              'декларация независимости сша',
              'declaration of independence']},
 {'id': 'hist_time_046',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Napoleon Bonapartning 18-bryumer to'ntarishi (milodiy 1799)",
                     "Bastiliya qal'asi shturmi va Buyuk Fransuz inqilobining boshlanishi (milodiy 1789)",
                     "Napoleonning Notr-Damda o'zini Fransiya imperatori deb e'lon qilishi (milodiy 1804)",
                     'Trafalgar dengiz jangi va Austerlits jangi (milodiy 1805)'],
              'ru': ['Переворот 18 брюмера Наполеона Бонапарта (1799 н.э.)',
                     'Взятие Бастилии и начало Великой французской революции (1789 н.э.)',
                     'Коронация Наполеона императором в Нотр-Дам (1804 н.э.)',
                     'Трафальгарская битва и Аустерлиц (1805 н.э.)'],
              'en': ["Napoleon's Coup of 18 Brumaire (1799 AD)",
                     'Storming of the Bastille begins French Revolution (1789 AD)',
                     'Napoleon crowns himself Emperor (1804 AD)',
                     'Battle of Trafalgar and Austerlitz (1805 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Bastiliya qal'asi shturmi va Buyuk Fransuz inqilobining boshlanishi (milodiy 1789)",
                     'ru': 'Взятие Бастилии и начало Великой французской революции (1789 н.э.)',
                     'en': 'Storming of the Bastille begins French Revolution (1789 AD)'},
  'image_url': None,
  'fun_fact': {'uz': '1789 yil 14 iyulda Bastiliya qamoqxonasi qulatildi va bu kun Fransiyaning milliy bayramiga '
                     'aylandi.',
               'ru': '14 июля 1789 года падение королевской крепости-тюрьмы Бастилии ознаменовало крах абсолютизма во '
                     'Франции.',
               'en': 'The storming of the Bastille on July 14, 1789 signaled the end of the Ancien Regime and is '
                     'celebrated as Bastille Day.'},
  'aliases': ['bastiliya', 'fransuz inqilobi', 'бастилия', 'французская революция', 'bastille']},
 {'id': 'hist_time_047',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Austerlits jangi ('Uch imperator jangi') (milodiy 1805)",
                     'Borodino jangi va Moskvaga Napoleon kirishi (milodiy 1812)',
                     "Napoleon Bonapart Fransiya imperatori deb e'lon qilinishi (milodiy 1804)",
                     "Vaterloo jangi va Napoleonning uzil-kesil mag'lubiyati (milodiy 1815)"],
              'ru': ['Битва при Аустерлице (1805 н.э.)',
                     'Бородинское сражение (1812 н.э.)',
                     'Провозглашение Наполеона императором французов (1804 н.э.)',
                     'Битва при Ватерлоо (1815 н.э.)'],
              'en': ['Battle of Austerlitz (1805 AD)',
                     'Battle of Borodino (1812 AD)',
                     'Napoleon crowns himself Emperor of the French (1804 AD)',
                     'Battle of Waterloo (1815 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Napoleon Bonapart Fransiya imperatori deb e'lon qilinishi (milodiy 1804)",
                     'ru': 'Провозглашение Наполеона императором французов (1804 н.э.)',
                     'en': 'Napoleon crowns himself Emperor of the French (1804 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Notr-Damdagi toj kiyish marosimida Napoleon imperatorlik tojini Papa qo'lidan olib, o'z qo'llari "
                     "bilan boshiga qo'ygan.",
               'ru': 'Наполеон сам возложил корону себе на голову в соборе Нотр-Дам, подчеркнув, что заслужил власть '
                     'личными победами.',
               'en': 'At Notre-Dame in 1804, Napoleon famously took the crown from Pope Pius VII and placed it on his '
                     'own head.'},
  'aliases': ['napoleon', 'napoleon imperator', 'наполеон', 'коронация наполеона', 'napoleon bonaparte']},
 {'id': 'hist_time_048',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Vena kongressining ochilishi (milodiy 1814)',
                     "Vaterloo jangi: Napoleonning so'nggi mag'lubiyati (milodiy 1815)",
                     'Gretsiyada Usmonlilarga qarshi mustaqillik urushi boshlanishi (milodiy 1821)',
                     "Trafalgar dengiz jangi: admiral Nelsonning g'alabasi (milodiy 1805)"],
              'ru': ['Открытие Венского конгресса (1814 н.э.)',
                     'Битва при Ватерлоо (1815 н.э.)',
                     'Начало греческой войны за независимость (1821 н.э.)',
                     'Трафальгарское морское сражение адмирала Нельсона (1805 н.э.)'],
              'en': ['Opening of the Congress of Vienna (1814 AD)',
                     'Battle of Waterloo (1815 AD)',
                     'Greek War of Independence begins (1821 AD)',
                     "Battle of Trafalgar: Admiral Nelson's victory (1805 AD)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Trafalgar dengiz jangi: admiral Nelsonning g'alabasi (milodiy 1805)",
                     'ru': 'Трафальгарское морское сражение адмирала Нельсона (1805 н.э.)',
                     'en': "Battle of Trafalgar: Admiral Nelson's victory (1805 AD)"},
  'image_url': None,
  'fun_fact': {'uz': "Trafalgar jangida ingliz floti g'alaba qozonib, Napoleonning Buyuk Britaniyaga bostirib kirish "
                     "rejasiga batamom chek qo'ygan.",
               'ru': 'Победа при Трафальгаре утвердила морское господство Британии на целое столетие.',
               'en': 'Trafalgar in October 1805 destroyed the Franco-Spanish fleet, securing British naval supremacy '
                     'for over a century.'},
  'aliases': ['trafalgar', 'trafalgar jangi', 'трафальгар', 'трафальгарская битва', 'battle of trafalgar']},
 {'id': 'hist_time_049',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Vaterloo jangi — Napoleon armiyasining Vellington va Blyuxer tomonidan yengilishi (milodiy 1815)',
                     "Simon Bolivar Buyuk Kolumbiya mustaqilligini e'lon qilishi (milodiy 1819)",
                     "Peterburgda Dekabristlar qo'zg'oloni (milodiy 1825)",
                     "Qirolicha Viktoriya Buyuk Britaniya taxtiga o'tirishi (milodiy 1837)"],
              'ru': ['Битва при Ватерлоо — окончательный разгром Наполеона (1815 н.э.)',
                     'Симон Боливар освобождает Великую Колумбию (1819 н.э.)',
                     'Восстание декабристов в Петербурге (1825 н.э.)',
                     'Восшествие королевы Виктории на британский престол (1837 н.э.)'],
              'en': ['Battle of Waterloo ends the Napoleonic Era (1815 AD)',
                     'Simon Bolivar liberates Gran Colombia (1819 AD)',
                     'Decembrist Revolt in Saint Petersburg (1825 AD)',
                     'Queen Victoria ascends the British throne (1837 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Vaterloo jangi — Napoleon armiyasining Vellington va Blyuxer tomonidan yengilishi (milodiy '
                           '1815)',
                     'ru': 'Битва при Ватерлоо — окончательный разгром Наполеона (1815 н.э.)',
                     'en': 'Battle of Waterloo ends the Napoleonic Era (1815 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Vaterloodagi mag'lubiyatdan so'ng Napoleon Muqaddas Yelena oroliga surgun qilingan va umrining "
                     "oxirigacha o'sha yerda yashagan.",
               'ru': 'После разгрома при Ватерлоо 18 июня 1815 года Наполеон был сослан на далекий остров Святой '
                     'Елены.',
               'en': "Waterloo on June 18, 1815 ended the Hundred Days and led to Napoleon's final exile on Saint "
                     'Helena.'},
  'aliases': ['vaterloo', 'vaterloo jangi', 'ватерлоо', 'битва при ватерлоо', 'waterloo']},
 {'id': 'hist_time_050',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Gretsiya mustaqillik urushi boshlanishi (milodiy 1821)',
                     'Simon Bolivar Boyaka jangida ispanlarni tor-mor etib, Janubiy Amerikani ozod qila boshlashi '
                     '(milodiy 1819)',
                     'Birinchi Afyun (Opium) urushi boshlanishi (milodiy 1839)',
                     "Karl Marks va Engels 'Kommunistik partiya manifesti'ni chop etishi (milodiy 1848)"],
              'ru': ['Греческая война за независимость (1821 н.э.)',
                     'Битва при Бояке и освобождение Новой Гранады Симоном Боливаром (1819 н.э.)',
                     'Начало Первой Опиумной войны в Китае (1839 н.э.)',
                     'Публикация «Манифеста Коммунистической партии» (1848 н.э.)'],
              'en': ['Greek War of Independence begins (1821 AD)',
                     'Simon Bolivar wins Battle of Boyaca liberating South America (1819 AD)',
                     'First Opium War begins in China (1839 AD)',
                     'Publication of the Communist Manifesto (1848 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Simon Bolivar Boyaka jangida ispanlarni tor-mor etib, Janubiy Amerikani ozod qila '
                           'boshlashi (milodiy 1819)',
                     'ru': 'Битва при Бояке и освобождение Новой Гранады Симоном Боливаром (1819 н.э.)',
                     'en': 'Simon Bolivar wins Battle of Boyaca liberating South America (1819 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Simon Bolivar Lotin Amerikasining oltita davlatini (Venesuela, Kolumbiya, Ekvador, Peru, '
                     'Boliviya, Panama) ispan mustamlakasidan ozod qilgan.',
               'ru': 'Симон Боливар получил почетный титул «Освободитель» (El Libertador) за свержение власти '
                     'испанской короны в шести странах.',
               'en': "Known as 'El Libertador', Simon Bolivar led campaigns that won independence for six South "
                     'American nations.'},
  'aliases': ['simon bolivar', 'bolivar', 'симон боливар', 'боливар', 'simon bolivar']},
 {'id': 'hist_time_051',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Samuel Morzening ilk elektr telegraf xabarini jo'natishi (milodiy 1844)",
                     "Kaliforniyada 'Oltin vasvasasi'ning boshlanishi (milodiy 1848)",
                     "Jorj Stefensonning 'Raketa' parovozining poygada g'alaba qozonishi (milodiy 1829)",
                     "Ilk transatlantika telegraf kabelining o'tkazilishi (milodiy 1858)"],
              'ru': ['Первая телеграмма Сэмюэла Морзе (1844 н.э.)',
                     'Золотая лихорадка в Калифорнии (1848 н.э.)',
                     'Победа паровоза «Ракета» Стефенсона в Рейнхильских состязаниях (1829 н.э.)',
                     'Прокладка трансатлантического кабеля связи (1858 н.э.)'],
              'en': ['Samuel Morse sends first telegraph message (1844 AD)',
                     'California Gold Rush begins (1848 AD)',
                     "George Stephenson's Rocket wins the Rainhill Trials (1829 AD)",
                     'First transatlantic telegraph cable (1858 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Jorj Stefensonning 'Raketa' parovozining poygada g'alaba qozonishi (milodiy 1829)",
                     'ru': 'Победа паровоза «Ракета» Стефенсона в Рейнхильских состязаниях (1829 н.э.)',
                     'en': "George Stephenson's Rocket wins the Rainhill Trials (1829 AD)"},
  'image_url': None,
  'fun_fact': {'uz': "Stefensonning 'Raketa' parovozi soatiga 47 km tezlikka erishib, temir yo'l transportining butun "
                     "dunyoga tarqalishiga turtki bo'lgan.",
               'ru': 'Паровоз «Ракета» развил рекордную скорость 47 км/ч, открыв эпоху регулярного железнодорожного '
                     'сообщения.',
               'en': "Stephenson's Rocket reached 29 mph at Rainhill in 1829, establishing steam railways as viable "
                     'transport.'},
  'aliases': ['stefenson', 'raketa parovozi', 'стефенсон', 'ракета паровоз', 'stephenson rocket']},
 {'id': 'hist_time_052',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["AQSh va Meksika o'rtasidagi urushning boshlanishi (milodiy 1846)",
                     "Yevropada 'Xalqlar bahori' inqiloblari (milodiy 1848)",
                     'Qrim urushining boshlanishi (milodiy 1853)',
                     "Samuel Morze ilk elektr telegraf orqali xabar uzatishi: 'Xudoning karomatini qarang' (milodiy "
                     '1844)'],
              'ru': ['Начало Американо-мексиканской войны (1846 н.э.)',
                     '«Весна народов» — революции в Европе (1848 н.э.)',
                     'Начало Крымской войны (1853 н.э.)',
                     'Сэмюэл Морзе отправляет первую официальную телеграмму (1844 н.э.)'],
              'en': ['Outbreak of Mexican-American War (1846 AD)',
                     'Spring of Nations revolutions across Europe (1848 AD)',
                     'Outbreak of the Crimean War (1853 AD)',
                     'Samuel Morse sends first electric telegraph message (1844 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Samuel Morze ilk elektr telegraf orqali xabar uzatishi: 'Xudoning karomatini qarang' "
                           '(milodiy 1844)',
                     'ru': 'Сэмюэл Морзе отправляет первую официальную телеграмму (1844 н.э.)',
                     'en': 'Samuel Morse sends first electric telegraph message (1844 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Morze telegrafi va uning alifbosi (nuqta va tirelar) axborotni masofadan bir zumda uzatish '
                     'orqali telekommunikatsiya inqilobini boshlab berdi.',
               'ru': 'Телеграф Морзе соединил Вашингтон и Балтимор в 1844 году, впервые позволив передавать сообщения '
                     'со скоростью света.',
               'en': "Morse sent 'What hath God wrought' between Washington and Baltimore in 1844, launching instant "
                     'long-distance communication.'},
  'aliases': ['morze', 'telegraf', 'morze alifbosi', 'морзе', 'телеграф', 'morse code', 'telegraph']},
 {'id': 'hist_time_053',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Karl Marks va Fridrix Engels 'Kommunistik partiya manifesti'ni e'lon qilishi (milodiy 1848)",
                     "Florens Naytingeyl Qrim urushida yaradorlarga yordam ko'rsatishi (milodiy 1854)",
                     "Charlz Darvin 'Turlarning kelib chiqishi' asarini chop etishi (milodiy 1859)",
                     'AQShda Fuqarolar urushining boshlanishi (milodiy 1861)'],
              'ru': ['Публикация «Манифеста Коммунистической партии» Марксом и Энгельсом (1848 н.э.)',
                     'Флоренс Найтингейл в госпиталях Крымской войны (1854 н.э.)',
                     'Выход книги Дарвина «Происхождение видов» (1859 н.э.)',
                     'Начало Гражданской войны в США (1861 н.э.)'],
              'en': ['Marx and Engels publish the Communist Manifesto (1848 AD)',
                     'Florence Nightingale serves in Crimean War (1854 AD)',
                     'Charles Darwin publishes On the Origin of Species (1859 AD)',
                     'Outbreak of the American Civil War (1861 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Karl Marks va Fridrix Engels 'Kommunistik partiya manifesti'ni e'lon qilishi (milodiy "
                           '1848)',
                     'ru': 'Публикация «Манифеста Коммунистической партии» Марксом и Энгельсом (1848 н.э.)',
                     'en': 'Marx and Engels publish the Communist Manifesto (1848 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "'Butun dunyo proletarlari, birlashingiz!' shiori bilan yakunlangan ushbu kitob XX asr siyosiy "
                     "tarixiga eng katta ta'sir ko'rsatgan manifestga aylandi.",
               'ru': 'Манифест 1848 года провозгласил классовую борьбу движущей силой истории и вдохновил '
                     'социалистические революции XX века.',
               'en': 'Published in London in February 1848, the Communist Manifesto became one of the most influential '
                     'political texts in history.'},
  'aliases': ['marks', 'kommunistik manifest', 'маркс', 'манифест', 'communist manifesto']},
 {'id': 'hist_time_054',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Rossiya imperiyasida krepostnoylik huquqining bekor qilinishi (milodiy 1861)',
                     "Charlz Darvin 'Turlarning kelib chiqishi' kitobini chop etishi (milodiy 1859)",
                     "Avraam Linkoln quldorlikni bekor qilish to'g'risida proklamatsiya chiqarishi (milodiy 1863)",
                     'Yaponiyada Meydzi inqilobi boshlanishi (milodiy 1868)'],
              'ru': ['Отмена крепостного права в России Александром II (1861 н.э.)',
                     'Издание Чарльзом Дарвином «Происхождения видов» (1859 н.э.)',
                     'Прокламация об освобождении рабов Авраама Линкольна (1863 н.э.)',
                     'Реставрация Мэйдзи в Японии (1868 н.э.)'],
              'en': ['Emancipation of the Serfs in Russia (1861 AD)',
                     'Charles Darwin publishes On the Origin of Species (1859 AD)',
                     'Abraham Lincoln issues Emancipation Proclamation (1863 AD)',
                     'Meiji Restoration begins in Japan (1868 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Charlz Darvin 'Turlarning kelib chiqishi' kitobini chop etishi (milodiy 1859)",
                     'ru': 'Издание Чарльзом Дарвином «Происхождения видов» (1859 н.э.)',
                     'en': 'Charles Darwin publishes On the Origin of Species (1859 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Darvinning tabiiy tanlanish orqali evolyutsiya nazariyasi biologiya fanida inqilob qildi; '
                     'kitobning birinchi 1250 nusxasi birinchi kundayoq sotilib ketgan.',
               'ru': 'Теория эволюции путем естественного отбора перевернула научное представление о происхождении '
                     'жизни на Земле.',
               'en': "Darwin's 1859 book sold out on its first day of publication and revolutionized modern biological "
                     'science.'},
  'aliases': ['darvin', 'turlarning kelib chiqishi', 'дарвин', 'происхождение видов', 'darwin', 'origin of species']},
 {'id': 'hist_time_055',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Yaponiyada imperatorlik hokimiyati tiklanishi (Meydzi davri) (milodiy 1868)',
                     'Suvaysh kanalining xalqaro kemachilik uchun ochilishi (milodiy 1869)',
                     "General Chernyayev qo'shinlari Toshkentni qamal qilib bosib olishi (milodiy 1865)",
                     "Germaniya imperiyasining Versal saroyida e'lon qilinishi (milodiy 1871)"],
              'ru': ['Реставрация Мэйдзи (1868 н.э.)',
                     'Открытие Суэцкого канала (1869 н.э.)',
                     'Штурм и взятие Ташкента войсками генерала Черняева (1865 н.э.)',
                     'Провозглашение Германской империи в Версале (1871 н.э.)'],
              'en': ['Meiji Restoration in Japan (1868 AD)',
                     'Opening of the Suez Canal (1869 AD)',
                     'Tsarist forces under Chernyaev conquer Tashkent (1865 AD)',
                     'Proclamation of the German Empire (1871 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "General Chernyayev qo'shinlari Toshkentni qamal qilib bosib olishi (milodiy 1865)",
                     'ru': 'Штурм и взятие Ташкента войсками генерала Черняева (1865 н.э.)',
                     'en': 'Tsarist forces under Chernyaev conquer Tashkent (1865 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Toshkent mudofaasi qariyb 3 oy davom etgan; Chernyayev Kamolon darvozasi orqali bostirib kirgan '
                     'va keyinchalik Turkiston general-gubernatorligi tashkil etilgan.',
               'ru': 'Захват Ташкента в июне 1865 года открыл путь к созданию Туркестанского генерал-губернаторства '
                     'Российской империи.',
               'en': 'The capture of Tashkent in June 1865 initiated the direct colonial incorporation of Central Asia '
                     'into the Russian Empire.'},
  'aliases': ['toshkent bosib olinishi', 'chernyayev', 'взятие ташкента', 'черняев', 'tashkent 1865']},
 {'id': 'hist_time_056',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Suvaysh kanali ochilishi (milodiy 1869)',
                     'Fransiya-Prussiya urushi va Parij Kommunasi (milodiy 1870-1871)',
                     'Aleksandr Bell telefonni patentlashi (milodiy 1876)',
                     'Yaponiyada Meydzi inqilobi va samuraylar hokimiyatining tugatilishi (milodiy 1868)'],
              'ru': ['Открытие Суэцкого канала (1869 н.э.)',
                     'Франко-прусская война и Парижская коммуна (1870–1871 н.э.)',
                     'Патент на телефон Александра Белла (1876 н.э.)',
                     'Реставрация Мэйдзи — начало модернизации Японии (1868 н.э.)'],
              'en': ['Opening of Suez Canal (1869 AD)',
                     'Franco-Prussian War (1870–1871 AD)',
                     'Alexander Graham Bell patents telephone (1876 AD)',
                     'The Meiji Restoration begins modernization of Japan (1868 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Yaponiyada Meydzi inqilobi va samuraylar hokimiyatining tugatilishi (milodiy 1868)',
                     'ru': 'Реставрация Мэйдзи — начало модернизации Японии (1868 н.э.)',
                     'en': 'The Meiji Restoration begins modernization of Japan (1868 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Meydzi davrida feodal syogunlik ag'darilib, Yaponiya atigi 30 yil ichida Osiyoning eng qudratli "
                     'industrial davlatiga aylandi.',
               'ru': 'Эпоха Мэйдзи покончила с изоляцией сегуната Токугава, превратив феодальную страну в передовую '
                     'мировую державу.',
               'en': 'The 1868 Meiji Restoration ended 250 years of Tokugawa isolation, propelling Japan into rapid '
                     'industrialization.'},
  'aliases': ['meydzi', 'meydzi inqilobi', 'мэйдзи', 'реставрация мэйдзи', 'meiji restoration']},
 {'id': 'hist_time_057',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["O'rta yer va Qizil dengizni tutashtiruvchi Suvaysh kanalining ochilishi (milodiy 1869)",
                     "Parij Kommunasining e'lon qilinishi (milodiy 1871)",
                     'Tomas Edison fonografni (tovush yozuvchi qurilma) ixtiro qilishi (milodiy 1877)',
                     "Berlin konferensiyasida Afrikaning mustamlakalarga bo'linishi (milodiy 1884)"],
              'ru': ['Торжественное открытие Суэцкого канала в Египте (1869 н.э.)',
                     'Провозглашение Парижской коммуны (1871 н.э.)',
                     'Изобретение фонографа Томасом Эдисоном (1877 н.э.)',
                     'Берлинская конференция по разделу Африки (1884 н.э.)'],
              'en': ['Opening of the Suez Canal linking Mediterranean to Red Sea (1869 AD)',
                     'Proclamation of Paris Commune (1871 AD)',
                     'Thomas Edison invents the phonograph (1877 AD)',
                     'Berlin Conference partitions Africa (1884 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "O'rta yer va Qizil dengizni tutashtiruvchi Suvaysh kanalining ochilishi (milodiy 1869)",
                     'ru': 'Торжественное открытие Суэцкого канала в Египте (1869 н.э.)',
                     'en': 'Opening of the Suez Canal linking Mediterranean to Red Sea (1869 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Suvaysh kanali ochilishi Yevropadan Hindistonga bo'lgan dengiz yo'lini qariyb 7000 km ga "
                     "qisqartirdi (Afrikani aylanib o'tish zarurati qolmadi).",
               'ru': 'Суэцкий канал длиной 163 км сократил морской путь из Лондона в Бомбей почти в два раза.',
               'en': 'Opening in November 1869, the Suez Canal eliminated the need to circumnavigate Africa, slashing '
                     'transit distance to India.'},
  'aliases': ['suvaysh', 'suvaysh kanali', 'суэцкий канал', 'suez canal']},
 {'id': 'hist_time_058',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Tomas Edison uzoq yonuvchi cho'g'lanma lampochkani yaratishi (milodiy 1879)",
                     'Aleksandr Grem Bell telefon apparatini patentlashi (milodiy 1876)',
                     'Karl Bens birinchi benzinli avtomobilga patent olishi (milodiy 1886)',
                     'Parijda Eyfel minorasining ochilishi (milodiy 1889)'],
              'ru': ['Томас Эдисон создает лампу накаливания (1879 н.э.)',
                     'Александр Белл получает патент на электрический телефон (1876 н.э.)',
                     'Патент Карла Бенца на бензиновый автомобиль (1886 н.э.)',
                     'Открытие Эйфелевой башни (1889 н.э.)'],
              'en': ['Edison perfects incandescent light bulb (1879 AD)',
                     'Alexander Graham Bell patents the telephone (1876 AD)',
                     'Karl Benz patents first petrol automobile (1886 AD)',
                     'Inauguration of Eiffel Tower in Paris (1889 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Aleksandr Grem Bell telefon apparatini patentlashi (milodiy 1876)',
                     'ru': 'Александр Белл получает патент на электрический телефон (1876 н.э.)',
                     'en': 'Alexander Graham Bell patents the telephone (1876 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Bell telefon orqali aytgan birinchi so'zlar: 'Janob Uotson, bu yerga keling, siz menga "
                     "keraksiz!' bo'lgan.",
               'ru': 'Первая фраза, сказанная Беллом по телефону помощнику Уотсону: «Мистер Ватсон, идите сюда, вы мне '
                     'нужны».',
               'en': "Bell spoke the first telephone words on March 10, 1876: 'Mr. Watson, come here, I want to see "
                     "you.'"},
  'aliases': ['bell', 'telefon', 'grem bell', 'белл', 'телефон', 'graham bell', 'telephone']},
 {'id': 'hist_time_059',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Eyfel minorasi Butunjahon ko'rgazmasi uchun qurilishi (milodiy 1889)",
                     "Afinada zamonaviy birinchi Olimpiya o'yinlarining o'tkazilishi (milodiy 1896)",
                     "Karl Bens birinchi benzinli uch g'ildirakli avtomobilga patent olishi (milodiy 1886)",
                     'Aka-uka Raytlar ilk marta samolyotda parvoz qilishi (milodiy 1903)'],
              'ru': ['Возведение Эйфелевой башни в Париже (1889 н.э.)',
                     'Первые современные Олимпийские игры в Афинах (1896 н.э.)',
                     'Карл Бенц получает патент на первый в мире бензиновый автомобиль (1886 н.э.)',
                     'Первый управляемый полет братьев Райт (1903 н.э.)'],
              'en': ["Eiffel Tower built for Paris World's Fair (1889 AD)",
                     'First modern Olympic Games in Athens (1896 AD)',
                     'Karl Benz patents the first gasoline automobile (1886 AD)',
                     'Wright brothers make first powered flight (1903 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Karl Bens birinchi benzinli uch g'ildirakli avtomobilga patent olishi (milodiy 1886)",
                     'ru': 'Карл Бенц получает патент на первый в мире бензиновый автомобиль (1886 н.э.)',
                     'en': 'Karl Benz patents the first gasoline automobile (1886 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Karl Bensning rafiqasi Berta Bens 1888 yilda eriga aytmasdan dunyodagi ilk 106 kilometrlik uzoq '
                     'masofali avtosayohatni amalga oshirgan.',
               'ru': 'Берта Бенц доказала практичность машины мужа, совершив в 1888 году первый в истории автопробег '
                     'на 106 км.',
               'en': "In 1888, Bertha Benz famously drove the Motorwagen 106 km without her husband's knowledge, "
                     'proving its commercial viability.'},
  'aliases': ['bens', 'avtomobil', 'karl benz', 'бенц', 'первый автомобиль', 'karl benz']},
 {'id': 'hist_time_060',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Zamonaviy Olimpiya o'yinlarining Afinada tiklanishi (milodiy 1896)",
                     'Janubiy Afrikada Angliya-Bur urushi boshlanishi (milodiy 1899)',
                     "Titanik gigant laynerining aysbergga urilib cho'kishi (milodiy 1912)",
                     'Parijda Eyfel minorasining tantanali ochilishi (milodiy 1889)'],
              'ru': ['Возрождение Олимпийских игр в Афинах (1896 н.э.)',
                     'Начало Англо-бурской войны (1899 н.э.)',
                     'Крушение лайнера «Титаник» (1912 н.э.)',
                     'Торжественное открытие Эйфелевой башни в Париже (1889 н.э.)'],
              'en': ['Revival of Olympic Games in Athens (1896 AD)',
                     'Outbreak of the Boer War (1899 AD)',
                     'Sinking of the RMS Titanic (1912 AD)',
                     'Inauguration of the Eiffel Tower in Paris (1889 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Parijda Eyfel minorasining tantanali ochilishi (milodiy 1889)',
                     'ru': 'Торжественное открытие Эйфелевой башни в Париже (1889 н.э.)',
                     'en': 'Inauguration of the Eiffel Tower in Paris (1889 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Eyfel minorasi dastlab 20 yildan so'ng buzib tashlanishi rejalashtirilgan edi, ammo "
                     "radioantennalar o'rnatilgani sababli saqlab qolingan.",
               'ru': 'Эйфелеву башню планировали разобрать через 20 лет после выставки, но ее спасло бурное развитие '
                     'радиосвязи.',
               'en': 'Originally meant to stand for only 20 years, the Eiffel Tower was saved because its height made '
                     'it ideal for radio transmission.'},
  'aliases': ['eyfel', 'eyfel minorasi', 'эйфелева башня', 'eiffel tower']},
 {'id': 'hist_time_061',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Aka-uka Raytlar ilk boshqariladigan motorli samolyot parvozini amalga oshirishi (milodiy 1903)',
                     'Rossiya-Yaponiya urushining boshlanishi (milodiy 1904)',
                     "Eynshteyn Maxsus nisbiylik nazariyasini e'lon qilishi (milodiy 1905)",
                     "Titanik kemasining cho'kishi (milodiy 1912)"],
              'ru': ['Первый в мире управляемый полет братьев Райт на самолете (1903 н.э.)',
                     'Начало Русско-японской войны (1904 н.э.)',
                     'Публикация специальной теории относительности Эйнштейна (1905 н.э.)',
                     'Гибель «Титаника» (1912 н.э.)'],
              'en': ['Wright brothers make first controlled powered flight (1903 AD)',
                     'Outbreak of Russo-Japanese War (1904 AD)',
                     'Einstein publishes Special Relativity (1905 AD)',
                     'Sinking of the Titanic (1912 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Aka-uka Raytlar ilk boshqariladigan motorli samolyot parvozini amalga oshirishi (milodiy '
                           '1903)',
                     'ru': 'Первый в мире управляемый полет братьев Райт на самолете (1903 н.э.)',
                     'en': 'Wright brothers make first controlled powered flight (1903 AD)'},
  'image_url': None,
  'fun_fact': {'uz': '1903 yil 17 dekabrda Orvill Rayt amalga oshirgan birinchi parvoz atigi 12 soniya davom etib, 36 '
                     "metr masofani bosib o'tgan.",
               'ru': 'Первый исторический полет 17 декабря 1903 года в Китти-Хок длился всего 12 секунд и покрыл '
                     'расстояние в 36,5 метров.',
               'en': "Orville Wright's maiden flight lasted just 12 seconds and covered 120 feet, yet launched the era "
                     'of aviation.'},
  'aliases': ['raytlar', 'aka uka raytlar', 'братья райт', 'первый полет', 'wright brothers']},
 {'id': 'hist_time_062',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Titanik transatlantik laynerining cho'kishi (milodiy 1912)",
                     "Albert Eynshteyn o'zining 'Mo'jizaviy yili'da E=mc² formulasini e'lon qilishi (milodiy 1905)",
                     "Sarayevoda Frans Ferdinandning o'ldirilishi va Birinchi jahon urushi (milodiy 1914)",
                     'Rossiyada Oktyabr inqilobi va bolsheviklar hokimiyatga kelishi (milodiy 1917)'],
              'ru': ['Гибель «Титаника» в Атлантике (1912 н.э.)',
                     '«Год чудес» Альберта Эйнштейна и публикация формулы E=mc² (1905 н.э.)',
                     'Убийство эрцгерцога Франца Фердинанда в Сараево (1914 н.э.)',
                     'Октябрьская революция в России (1917 н.э.)'],
              'en': ['Sinking of the Titanic (1912 AD)',
                     'Albert Einstein publishes Annus Mirabilis papers including E=mc² (1905 AD)',
                     'Assassination of Franz Ferdinand (1914 AD)',
                     'October Revolution in Russia (1917 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Albert Eynshteyn o'zining 'Mo'jizaviy yili'da E=mc² formulasini e'lon qilishi (milodiy "
                           '1905)',
                     'ru': '«Год чудес» Альберта Эйнштейна и публикация формулы E=mc² (1905 н.э.)',
                     'en': 'Albert Einstein publishes Annus Mirabilis papers including E=mc² (1905 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "1905 yilda Shveytsariya patent byurosida oddiy xodim bo'lib ishlagan Eynshteyn fizika asoslarini "
                     'larzaga solgan 4 ta maqola chop etgan.',
               'ru': 'Работая скромным клерком в патентном бюро Берна, 26-летний Эйнштейн перевернул представления о '
                     'пространстве, времени и энергии.',
               'en': 'In 1905, while working at the Bern patent office, 26-year-old Einstein published four '
                     'groundbreaking papers altering physics forever.'},
  'aliases': ['eynshteyn', 'nisbiylik nazariyasi', 'эйнштейн', 'теория относительности', 'einstein', 'relativity']},
 {'id': 'hist_time_063',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Birinchi jahon urushining boshlanishi (milodiy 1914)',
                     "Somma daryosi bo'yidagi qonli jang (milodiy 1916)",
                     "Titanik yo'lovchi laynerining aysbergga urilib cho'kishi (milodiy 1912)",
                     'Rossiyada Oktabr inqilobi (milodiy 1917)'],
              'ru': ['Начало Первой мировой войны (1914 н.э.)',
                     'Битва на Сомме (1916 н.э.)',
                     'Крушение гигантского лайнера «Титаник» в Атлантическом океане (1912 н.э.)',
                     'Октябрьская революция (1917 н.э.)'],
              'en': ['Outbreak of World War I (1914 AD)',
                     'Battle of the Somme (1916 AD)',
                     'Sinking of the RMS Titanic on maiden voyage (1912 AD)',
                     'October Revolution in Russia (1917 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Titanik yo'lovchi laynerining aysbergga urilib cho'kishi (milodiy 1912)",
                     'ru': 'Крушение гигантского лайнера «Титаник» в Атлантическом океане (1912 н.э.)',
                     'en': 'Sinking of the RMS Titanic on maiden voyage (1912 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "'Cho'kmas' deb e'lon qilingan Titanik o'zining ilk safaridayoq aysberg bilan to'qnashib, 1500 "
                     "dan ortiq odamning halokatiga sabab bo'ldi.",
               'ru': 'Крушение крупнейшего судна своего времени привело к пересмотру всех правил безопасности на море '
                     'и созданию Международного ледового патруля.',
               'en': 'The sinking of the Titanic in April 1912 led to the establishment of the International Ice '
                     'Patrol and universal life-saving mandates.'},
  'aliases': ['titanik', 'титаник', 'titanic', 'rms titanic']},
 {'id': 'hist_time_064',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Rossiyada Oktyabr inqilobi (milodiy 1917)',
                     'Birinchi jahon urushi sulhining Kompyenda imzolanishi (milodiy 1918)',
                     'Versal tinchlik shartnomasi imzolanishi (milodiy 1919)',
                     'Sarayevo suiqasdi va Birinchi jahon urushining boshlanishi (milodiy 1914)'],
              'ru': ['Октябрьская революция большевиков (1917 н.э.)',
                     'Компьенское перемирие (1918 н.э.)',
                     'Подписание Версальского мирного договора (1919 н.э.)',
                     'Сараевское убийство и начало Первой мировой войны (1914 н.э.)'],
              'en': ['Bolshevik October Revolution (1917 AD)',
                     'Compiègne Armistice ending WWI fighting (1918 AD)',
                     'Signing of Treaty of Versailles (1919 AD)',
                     'Assassination of Franz Ferdinand sparking World War I (1914 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Sarayevo suiqasdi va Birinchi jahon urushining boshlanishi (milodiy 1914)',
                     'ru': 'Сараевское убийство и начало Первой мировой войны (1914 н.э.)',
                     'en': 'Assassination of Franz Ferdinand sparking World War I (1914 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Avstriya-Vengriya taxti vorisi Frans Ferdinandning Gavrilo Prinsip tomonidan otilishi bir oy '
                     'ichida barcha buyuk davlatlarni qamrab olgan jahon urushini keltirib chiqardi.',
               'ru': 'Выстрелы в Сараево 28 июня 1914 года запустили цепную реакцию союзов, ввергнувшую планету в '
                     'первую тотальную войну.',
               'en': 'The assassination of Archduke Franz Ferdinand on June 28, 1914 triggered military mobilizations '
                     'that started World War I.'},
  'aliases': ['birinchi jahon urushi', 'sarayevo suiqasdi', 'первая мировая война', 'world war i', 'ww1']},
 {'id': 'hist_time_065',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Rossiyada Oktyabr qurolli to'ntarishi va bolsheviklar hokimiyatga kelishi (milodiy 1917)",
                     "Mustafo Kamol Otaturk Turkiya Respublikasini e'lon qilishi (milodiy 1923)",
                     'Aleksandr Fleming penitsillinni kashf etishi (milodiy 1928)',
                     'Nyu-York birjasining qulashi (Buyuk depressiya) (milodiy 1929)'],
              'ru': ['Октябрьская революция и захват власти большевиками в Петрограде (1917 н.э.)',
                     'Провозглашение Турецкой Республики Ататюрком (1923 н.э.)',
                     'Открытие пенициллина Александром Флемингом (1928 н.э.)',
                     'Биржевой крах на Уолл-стрит (1929 н.э.)'],
              'en': ['Bolsheviks seize power in the October Revolution (1917 AD)',
                     'Atatürk proclaims Republic of Turkey (1923 AD)',
                     'Alexander Fleming discovers penicillin (1928 AD)',
                     'Wall Street Crash begins Great Depression (1929 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Rossiyada Oktyabr qurolli to'ntarishi va bolsheviklar hokimiyatga kelishi (milodiy 1917)",
                     'ru': 'Октябрьская революция и захват власти большевиками в Петрограде (1917 н.э.)',
                     'en': 'Bolsheviks seize power in the October Revolution (1917 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Lenin boshchiligidagi bolsheviklar Qishki saroyni shturm qilib Muvaqqat hukumatni ag'dardi va "
                     'dunyodagi birinchi sotsialistik davlatni tuzdi.',
               'ru': 'Залп крейсера «Аврора» и штурм Зимнего дворца в октябре 1917 года ознаменовали начало советской '
                     'эпохи.',
               'en': 'In October 1917, Vladimir Lenin and the Bolsheviks overthrew the Russian Provisional Government, '
                     'establishing Soviet rule.'},
  'aliases': ['oktyabr inqilobi', 'lenin', 'октябрьская революция', 'большевики', 'october revolution', 'lenin']},
 {'id': 'hist_time_066',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Aleksandr Fleming penitsillinni kashf qilishi (milodiy 1928)',
                     "Mustafo Kamol Otaturk tomonidan Turkiya Respublikasining e'lon qilinishi (milodiy 1923)",
                     'Uoll-Strit fond birjasi inqirozi (milodiy 1929)',
                     'Gitlerning Germaniya reyxskansleri etib tayinlanishi (milodiy 1933)'],
              'ru': ['Открытие пенициллина Флемингом (1928 н.э.)',
                     'Провозглашение Турецкой Республики Мустафой Кемалем Ататюрком (1923 н.э.)',
                     'Крах на Уолл-стрит («Черный четверг») (1929 н.э.)',
                     'Назначение Гитлера рейхсканцлером Германии (1933 н.э.)'],
              'en': ['Fleming discovers penicillin (1928 AD)',
                     'Mustafa Kemal Atatürk proclaims the Republic of Turkey (1923 AD)',
                     'Wall Street Crash (1929 AD)',
                     'Adolf Hitler appointed Chancellor (1933 AD)']},
  'correct_index': 1,
  'correct_answer': {'uz': "Mustafo Kamol Otaturk tomonidan Turkiya Respublikasining e'lon qilinishi (milodiy 1923)",
                     'ru': 'Провозглашение Турецкой Республики Мустафой Кемалем Ататюрком (1923 н.э.)',
                     'en': 'Mustafa Kemal Atatürk proclaims the Republic of Turkey (1923 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Otaturk sultonlikni bekor qilib poytaxtni Anqaraga ko'chirdi, dunyoviy respublika tuzdi va lotin "
                     'alifbosini joriy etdi.',
               'ru': 'Ататюрк упразднил султанат, перенес столицу в Анкару и провел масштабную модернизацию страны.',
               'en': 'On October 29, 1923, Atatürk proclaimed the secular Republic of Turkey, enacting comprehensive '
                     'modern reforms.'},
  'aliases': ['otaturk', 'turkiya respublikasi', 'ататюрк', 'турецкая республика', 'ataturk']},
 {'id': 'hist_time_067',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Buyuk Depressiyaning boshlanishi (milodiy 1929)',
                     "Mahatma Gandining mashhur 'Tuz yurishi' (milodiy 1930)",
                     'Aleksandr Fleming tomonidan ilk antibiotik — penitsillinning kashf etilishi (milodiy 1928)',
                     'Ispaniyada fuqarolar urushining boshlanishi (milodiy 1936)'],
              'ru': ['Начало Великой депрессии (1929 н.э.)',
                     '«Соляной поход» Махатмы Ганди в Индии (1930 н.э.)',
                     'Открытие первого антибиотика пенициллина Александром Флемингом (1928 н.э.)',
                     'Начало Гражданской войны в Испании (1936 н.э.)'],
              'en': ['Great Depression begins (1929 AD)',
                     "Mahatma Gandhi's Salt March (1930 AD)",
                     'Alexander Fleming discovers penicillin (1928 AD)',
                     'Outbreak of Spanish Civil War (1936 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Aleksandr Fleming tomonidan ilk antibiotik — penitsillinning kashf etilishi (milodiy 1928)',
                     'ru': 'Открытие первого антибиотика пенициллина Александром Флемингом (1928 н.э.)',
                     'en': 'Alexander Fleming discovers penicillin (1928 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Fleming zamburug' (Penicillium notatum) bakteriyalarni yo'q qilayotganini tasodifan payqab "
                     'qolib, tibbiyotda yuz millionlab insonlar hayotini saqlab qolgan dori ixtiro qildi.',
               'ru': 'Случайное открытие плесени, уничтожающей стафилококки, открыло эру антибиотиков и спасло сотни '
                     'миллионов жизней.',
               'en': "Fleming's serendipitous discovery of antibacterial Penicillium mold in 1928 ushered in the era "
                     'of modern antibiotics.'},
  'aliases': ['penitsillin', 'fleming', 'пенициллин', 'флеминг', 'penicillin', 'fleming']},
 {'id': 'hist_time_068',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Ispaniyada fuqarolar urushi boshlanishi (milodiy 1936)',
                     'Fashistlar Germaniyasining Polshaga bostirib kirishi (milodiy 1939)',
                     'Perl-Xarborga yapon aviasiyasi hujumi (milodiy 1941)',
                     "Uoll-Stritdagi 'Qora seshanba' va Buyuk Depressiyaning boshlanishi (milodiy 1929)"],
              'ru': ['Гражданская война в Испании (1936 н.э.)',
                     'Вторжение нацистской Германии в Польшу (1939 н.э.)',
                     'Нападение на Перл-Харбор (1941 н.э.)',
                     'Крах на Нью-Йоркской бирже («Черный вторник») и Великая депрессия (1929 н.э.)'],
              'en': ['Outbreak of the Spanish Civil War (1936 AD)',
                     'Nazi Germany invades Poland (1939 AD)',
                     'Japanese attack on Pearl Harbor (1941 AD)',
                     'Wall Street Crash (Black Tuesday) begins Great Depression (1929 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Uoll-Stritdagi 'Qora seshanba' va Buyuk Depressiyaning boshlanishi (milodiy 1929)",
                     'ru': 'Крах на Нью-Йоркской бирже («Черный вторник») и Великая депрессия (1929 н.э.)',
                     'en': 'Wall Street Crash (Black Tuesday) begins Great Depression (1929 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "1929 yil oktyabrdagi fond bozori qulashi butun dunyo bo'ylab sanoat ishlab chiqarishini 40 "
                     'foizdan ziyod qisqartirdi va ommaviy ishsizlikka olib keldi.',
               'ru': 'Крах Уолл-стрит в октябре 1929 года вызвал тяжелейший мировой экономический кризис XX столетия.',
               'en': 'The October 1929 Wall Street Crash wiped out billions in stock value, plunging the '
                     'industrialized world into the Great Depression.'},
  'aliases': ['uoll strit',
              'buyuk depressiya',
              'уолл-стрит',
              'великая депрессия',
              'wall street crash',
              'great depression']},
 {'id': 'hist_time_069',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Ispaniyada fuqarolar urushining boshlanishi va Franko isyoni (milodiy 1936)',
                     'Germaniyaning Polshaga hujumi va Ikkinchi jahon urushining boshlanishi (milodiy 1939)',
                     'Britaniya uchun havo jangi (milodiy 1940)',
                     'Barbarossa rejasi: fashistlarning SSSRga hujumi (milodiy 1941)'],
              'ru': ['Начало Гражданской войны в Испании и мятеж генерала Франко (1936 н.э.)',
                     'Начало Второй мировой войны (1939 н.э.)',
                     'Битва за Британию (1940 н.э.)',
                     'Нападение Германии на СССР (1941 н.э.)'],
              'en': ['Outbreak of the Spanish Civil War (1936 AD)',
                     'German invasion of Poland starts WWII (1939 AD)',
                     'Battle of Britain (1940 AD)',
                     'Nazi invasion of the Soviet Union (1941 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Ispaniyada fuqarolar urushining boshlanishi va Franko isyoni (milodiy 1936)',
                     'ru': 'Начало Гражданской войны в Испании и мятеж генерала Франко (1936 н.э.)',
                     'en': 'Outbreak of the Spanish Civil War (1936 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Ispaniya fuqarolar urushi Ikkinchi jahon urushining 'bosh repetitsiyasi' deb atalgan; Gernika "
                     "shaharchasining bombardimon qilinishi Pikassoning mashhur kartinasiga ilhom bo'lgan.",
               'ru': 'Гражданская война в Испании 1936–1939 гг. стала полигоном для испытания новой военной техники '
                     'фашистской Германии и СССР.',
               'en': 'The Spanish Civil War (1936-1939) served as a prelude to WWII, witnessing ideological conflict '
                     'and the bombing of Guernica.'},
  'aliases': ['ispan fuqarolar urushi', 'franko', 'гражданская война в испании', 'spanish civil war']},
 {'id': 'hist_time_070',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Yaponiyaning Perl-Xarborga to'satdan hujumi (1941 yil dekabr)",
                     'Germaniyaning Polshaga bostirib kirishi va Ikkinchi jahon urushining boshlanishi (1939 yil 1 '
                     'sentyabr)',
                     "Stalingrad jangida fashist qo'shinlarining taslim bo'lishi (1943 yil fevral)",
                     "Normandiyaga ittifoqchilar qo'shinining tushirilishi (D-Day) (1944 yil 6 iyun)"],
              'ru': ['Атака на Перл-Харбор (декабрь 1941)',
                     'Нападение нацистской Германии на Польшу — начало Второй мировой войны (1939)',
                     'Разгром немецких войск под Сталинградом (февраль 1943)',
                     'Высадка союзников в Нормандии (июнь 1944)'],
              'en': ['Attack on Pearl Harbor (December 1941)',
                     'Germany invades Poland, starting World War II (September 1, 1939)',
                     'Soviet victory at Stalingrad (February 1943)',
                     'D-Day Normandy landings (June 1944)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Germaniyaning Polshaga bostirib kirishi va Ikkinchi jahon urushining boshlanishi (1939 yil '
                           '1 sentyabr)',
                     'ru': 'Нападение нацистской Германии на Польшу — начало Второй мировой войны (1939)',
                     'en': 'Germany invades Poland, starting World War II (September 1, 1939)'},
  'image_url': None,
  'fun_fact': {'uz': "Polshaga hujumdan ikki kun o'tib Buyuk Britaniya va Fransiya Germaniyaga urush e'lon qildi va "
                     'insoniyat tarixidagi eng qonli urush boshlandi.',
               'ru': 'Вторая мировая война продолжалась 6 лет и унесла жизни более 70 миллионов человек.',
               'en': "On September 1, 1939, Hitler's forces launched the Blitzkrieg against Poland, precipitating "
                     "Britain and France's declarations of war."},
  'aliases': ['polshaga hujum',
              'ikkinchi jahon urushi boshlanishi',
              'вторая мировая война',
              'вторжение в польшу',
              'invasion of poland',
              'ww2']},
 {'id': 'hist_time_071',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Miduey dengiz jangi (1942 yil iyun)',
                     'Kursk jangi (1943 yil iyul)',
                     "Perl-Xarbor harbiy bazasiga yapon aviatsiyasining to'satdan hujumi (1941 yil 7 dekabr)",
                     'Xirosima va Nagasakiga atom bombasining tashlanishi (1945 yil avgust)'],
              'ru': ['Битва у атолла Мидуэй (июнь 1942)',
                     'Курская битва (июль 1943)',
                     'Нападение Японии на американскую базу Перл-Харбор (7 декабря 1941)',
                     'Атомная бомбардировка Хиросимы (август 1945)'],
              'en': ['Battle of Midway (June 1942)',
                     'Battle of Kursk (July 1943)',
                     'Japanese attack on Pearl Harbor (December 7, 1941)',
                     'Atomic bombing of Hiroshima (August 1945)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Perl-Xarbor harbiy bazasiga yapon aviatsiyasining to'satdan hujumi (1941 yil 7 dekabr)",
                     'ru': 'Нападение Японии на американскую базу Перл-Харбор (7 декабря 1941)',
                     'en': 'Japanese attack on Pearl Harbor (December 7, 1941)'},
  'image_url': None,
  'fun_fact': {'uz': "Prezident Franklin Ruzvelt Perl-Xarbor hujumi kunini 'tarixda sharmandalik kuni sifatida "
                     "qoladigan sana' deb atagan va AQSh rasman urushga kirgan.",
               'ru': 'Нападение на Перл-Харбор заставило США отказаться от нейтралитета и вступить во Вторую мировую '
                     'войну.',
               'en': "President Roosevelt termed December 7 'a date which will live in infamy' as the US entered World "
                     'War II.'},
  'aliases': ['perl xarbor', 'perl-xarbor', 'перл-харбор', 'pearl harbor']},
 {'id': 'hist_time_072',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Normandiyaga ittifoqchi kuchlarining desanti (D-Day) (1944 yil iyun)',
                     "Yalta (Qrim) konferensiyasining o'tkazilishi (1945 yil fevral)",
                     'BMT tashkilotining San-Fransiskoda tuzilishi (1945 yil iyun)',
                     "Stalingrad jangida Paulus boshchiligidagi 6-nemis armiyasining taslim bo'lishi (1943 yil "
                     'fevral)'],
              'ru': ['Высадка в Нормандии (июнь 1944)',
                     'Ялтинская конференция (февраль 1945)',
                     'Создание ООН в Сан-Франциско (июнь 1945)',
                     'Победа под Сталинградом и капитуляция армии Паулюса (февраль 1943)'],
              'en': ['D-Day Normandy Landings (June 1944)',
                     'Yalta Conference (February 1945)',
                     'Foundation of the United Nations (June 1945)',
                     'Capitulation of German 6th Army at Stalingrad (February 1943)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Stalingrad jangida Paulus boshchiligidagi 6-nemis armiyasining taslim bo'lishi (1943 yil "
                           'fevral)',
                     'ru': 'Победа под Сталинградом и капитуляция армии Паулюса (февраль 1943)',
                     'en': 'Capitulation of German 6th Army at Stalingrad (February 1943)'},
  'image_url': None,
  'fun_fact': {'uz': "Stalingrad jangi Ikkinchi jahon urushining tub burilish nuqtasi bo'lib, fashistlar armiyasi "
                     "o'zining butun elit kuchlarini boy berdi.",
               'ru': 'Сталинградская битва стала переломным моментом всей Второй мировой войны, положив начало '
                     'изгнанию нацистов.',
               'en': 'The Battle of Stalingrad in 1942-1943 was the single largest bloodiest battle in history, '
                     'turning the tide on the Eastern Front.'},
  'aliases': ['stalingrad', 'stalingrad jangi', 'сталинград', 'сталинградская битва', 'battle of stalingrad']},
 {'id': 'hist_time_073',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Normandiyaga ittifoqchilar desanti tushirilishi — 'Overlord' operatsiyasi (D-Day) (1944 yil 6 "
                     'iyun)',
                     "Fashistlar Germaniyasining so'zsiz taslim bo'lishi (G'alaba kuni) (1945 yil may)",
                     'Xirosimaga atom bombasining tashlanishi (1945 yil avgust)',
                     'Inson huquqlari umumjahon deklaratsiyasining qabul qilinishi (1948 yil dekabr)'],
              'ru': ['Высадка союзников в Нормандии — открытие Второго фронта (6 июня 1944)',
                     'Акт о безоговорочной капитуляции Германии (май 1945)',
                     'Атомный удар по Хиросиме (август 1945)',
                     'Всеобщая декларация прав человека (декабрь 1948)'],
              'en': ['Allied D-Day Normandy landings: Operation Overlord (June 6, 1944)',
                     'Unconditional surrender of Nazi Germany (May 1945)',
                     'Atomic bombing of Hiroshima (August 1945)',
                     'Universal Declaration of Human Rights (December 1948)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Normandiyaga ittifoqchilar desanti tushirilishi — 'Overlord' operatsiyasi (D-Day) (1944 "
                           'yil 6 iyun)',
                     'ru': 'Высадка союзников в Нормандии — открытие Второго фронта (6 июня 1944)',
                     'en': 'Allied D-Day Normandy landings: Operation Overlord (June 6, 1944)'},
  'image_url': None,
  'fun_fact': {'uz': "D-Day operatsiyasi tarixdagi eng yirik dengiz desanti bo'lib, bir kunda 156 000 dan ortiq askar "
                     "Normandiya qirg'oqlariga tushirilgan.",
               'ru': 'Операция «Оверлорд» 6 июня 1944 года стала крупнейшей морской десантной операцией в мировой '
                     'военной истории.',
               'en': 'On June 6, 1944, over 156,000 Allied soldiers landed in Normandy across five assault beaches, '
                     "piercing Hitler's Atlantic Wall."},
  'aliases': ['d-day', 'normandiya', 'overlord', 'высадка в нормандии', 'd-day', 'normandy']},
 {'id': 'hist_time_074',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Hindiston va Pokistonning mustaqillikka erishuvi (1947 yil avgust)',
                     'San-Fransiskoda Birlashgan Millatlar Tashkiloti (BMT) Ustavi imzolanishi (1945 yil 26 iyun)',
                     "Isroil davlatining e'lon qilinishi (1948 yil may)",
                     "Xitoy Xalq Respublikasining e'lon qilinishi (1949 yil oktyabr)"],
              'ru': ['Независимость Индии и Пакистана (август 1947)',
                     'Подписание Устава Организации Объединенных Наций (ООН) (26 июня 1945)',
                     'Провозглашение Государства Израиль (май 1948)',
                     'Образование КНР Мао Цзэдуном (октябрь 1949)'],
              'en': ['Independence of India and Pakistan (August 1947)',
                     'Signing of the Charter of the United Nations (June 26, 1945)',
                     'Proclamation of the State of Israel (May 1948)',
                     "Founding of the People's Republic of China (October 1949)"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'San-Fransiskoda Birlashgan Millatlar Tashkiloti (BMT) Ustavi imzolanishi (1945 yil 26 '
                           'iyun)',
                     'ru': 'Подписание Устава Организации Объединенных Наций (ООН) (26 июня 1945)',
                     'en': 'Signing of the Charter of the United Nations (June 26, 1945)'},
  'image_url': None,
  'fun_fact': {'uz': 'BMT jahonda tinchlik va xavfsizlikni saqlash maqsadida 50 ta davlat vakillari tomonidan tuzilgan '
                     "bo'lib, uning birinchi Bosh kotibi Tryugve Li bo'lgan.",
               'ru': 'Устав ООН был подписан представителями 50 государств, положив начало новой эпохе международного '
                     'права.',
               'en': 'The UN Charter was signed on June 26, 1945 in San Francisco to save succeeding generations from '
                     'the scourge of war.'},
  'aliases': ['bmt', 'bmt ustavi', 'оон', 'устав оон', 'united nations', 'un charter']},
 {'id': 'hist_time_075',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['BMT tomonidan Inson huquqlari umumjahon deklaratsiyasining qabul qilinishi (1948 yil dekabr)',
                     "Mao Szedun Pekinda XXR tuzilganini e'lon qilishi (1949 yil oktyabr)",
                     'Hindiston va Pokistonning Britaniya imperiyasidan mustaqillikka erishuvi (1947 yil avgust)',
                     'Koreya urushining boshlanishi (1950 yil iyun)'],
              'ru': ['Принятие Всеобщей декларации прав человека (1948)',
                     'Провозглашение Китайской Народной Республики (1949)',
                     'Провозглашение независимости Индии и Пакистана (август 1947)',
                     'Начало Корейской войны (1950)'],
              'en': ['Adoption of Universal Declaration of Human Rights (1948)',
                     "Mao Zedong proclaims People's Republic of China (1949)",
                     'Independence of India and Pakistan from British rule (August 1947)',
                     'Outbreak of the Korean War (1950)']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Hindiston va Pokistonning Britaniya imperiyasidan mustaqillikka erishuvi (1947 yil avgust)',
                     'ru': 'Провозглашение независимости Индии и Пакистана (август 1947)',
                     'en': 'Independence of India and Pakistan from British rule (August 1947)'},
  'image_url': None,
  'fun_fact': {'uz': "Mahatma Gandi boshchiligidagi 'zo'ravonliksiz kurash' (satyaagraha) Britaniya imperiyasini "
                     'Hindistondan chiqib ketishga majbur qildi.',
               'ru': '15 августа 1947 года «Жемчужина Британской короны» обрела независимость после десятилетий '
                     'ненасильственной борьбы Ганди.',
               'en': "India won independence on August 15, 1947 following decades of Mahatma Gandhi's nonviolent civil "
                     'disobedience.'},
  'aliases': ['hindiston mustaqilligi', 'gandi', 'независимость индии', 'ганди', 'indian independence']},
 {'id': 'hist_time_076',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Uotson va Krik DNK qo'sh spiral tuzilishini kashf etishi (milodiy 1953)",
                     "Yerning birinchi sun'iy yo'ldoshi (Sputnik-1) uchirilishi (milodiy 1957)",
                     'Karib (Kuba) raketa inqirozi (milodiy 1962)',
                     "Koreya urushining boshlanishi: 38-parallel bo'ylab to'qnashuv (1950 yil iyun)"],
              'ru': ['Открытие структуры ДНК Уотсоном и Криком (1953 н.э.)',
                     'Запуск Спутника-1 (1957 н.э.)',
                     'Карибский кризис (1962 н.э.)',
                     'Начало Корейской войны (25 июня 1950)'],
              'en': ['Watson and Crick discover DNA double helix (1953 AD)',
                     'Launch of Sputnik 1 (1957 AD)',
                     'Cuban Missile Crisis (1962 AD)',
                     'Outbreak of the Korean War across the 38th parallel (June 1950)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Koreya urushining boshlanishi: 38-parallel bo'ylab to'qnashuv (1950 yil iyun)",
                     'ru': 'Начало Корейской войны (25 июня 1950)',
                     'en': 'Outbreak of the Korean War across the 38th parallel (June 1950)'},
  'image_url': None,
  'fun_fact': {'uz': "Koreya urushi 1953 yilda sulh bitimi bilan to'xtagan, biroq tinchlik shartnomasi imzolanmagani "
                     'sababli texnik jihatdan bugungi kungacha davom etmoqda.',
               'ru': 'Корейская война закончилась соглашением о перемирии в 1953 году, но мирный договор не подписан '
                     'по сей день.',
               'en': 'The Korean War was paused by the 1953 armistice creating the DMZ, leaving the two nations '
                     'technically at war.'},
  'aliases': ['koreya urushi', 'корейская война', 'korean war']},
 {'id': 'hist_time_077',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Jeyms Uotson va Frensis Krik DNK qo'sh spiral tuzilishini kashf etishi (milodiy 1953)",
                     'Jonas Solk poliomiyelitga qarshi vaksina yaratishi (milodiy 1955)',
                     "SSSR tomonidan fazoga Sputnik-1 sun'iy yo'ldoshi uchirilishi (milodiy 1957)",
                     'Yuriy Gagarinning koinotga ilk parvozi (milodiy 1961)'],
              'ru': ['Открытие структуры двойной спирали ДНК Уотсоном и Криком (1953 н.э.)',
                     'Создание вакцины от полиомиелита Солка (1955 н.э.)',
                     'Запуск первого искусственного спутника Земли (1957 н.э.)',
                     'Полет Юрия Гагарина в космос (1961 н.э.)'],
              'en': ['Watson and Crick discover the DNA double helix structure (1953 AD)',
                     'Jonas Salk develops polio vaccine (1955 AD)',
                     'Soviet Union launches Sputnik 1 (1957 AD)',
                     'Yuri Gagarin becomes first human in space (1961 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Jeyms Uotson va Frensis Krik DNK qo'sh spiral tuzilishini kashf etishi (milodiy 1953)",
                     'ru': 'Открытие структуры двойной спирали ДНК Уотсоном и Криком (1953 н.э.)',
                     'en': 'Watson and Crick discover the DNA double helix structure (1953 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "DNK qo'sh spirali kashfiyoti gen muhandisligi, biotexnologiya va zamonaviy kriminalistika "
                     'fanlarining poydevoriga aylandi.',
               'ru': 'Открытие спирали ДНК в Кембридже стало величайшим биологическим прорывом XX века, расшифровавшим '
                     'код жизни.',
               'en': "Watson, Crick, and Rosalind Franklin's work unveiled the double helix in 1953, cracking the "
                     'fundamental secret of genetic inheritance.'},
  'aliases': ['dnk', 'dnk spirali', 'днк', 'двойная спираль днк', 'dna', 'double helix']},
 {'id': 'hist_time_078',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Yuriy Gagarinning fazoga parvozi (1961 yil aprel)',
                     "SSSR tomonidan Yerning birinchi sun'iy yo'ldoshi 'Sputnik-1' orbitaga chiqarilishi (1957 yil 4 "
                     'oktyabr)',
                     'Berlin devorining qurilishi boshlanishi (1961 yil avgust)',
                     'Karib raketa inqirozi (1962 yil oktyabr)'],
              'ru': ['Полет первого космонавта Юрия Гагарина (апрель 1961)',
                     'Запуск первого в мире искусственного спутника Земли «Спутник-1» (4 октября 1957)',
                     'Начало строительства Берлинской стены (август 1961)',
                     'Карибский ядерный кризис (октябрь 1962)'],
              'en': ["Yuri Gagarin's space flight (April 1961)",
                     'Soviet Union launches Sputnik 1 into orbit (October 4, 1957)',
                     'Construction of Berlin Wall begins (August 1961)',
                     'Cuban Missile Crisis (October 1962)']},
  'correct_index': 1,
  'correct_answer': {'uz': "SSSR tomonidan Yerning birinchi sun'iy yo'ldoshi 'Sputnik-1' orbitaga chiqarilishi (1957 "
                           'yil 4 oktyabr)',
                     'ru': 'Запуск первого в мире искусственного спутника Земли «Спутник-1» (4 октября 1957)',
                     'en': 'Soviet Union launches Sputnik 1 into orbit (October 4, 1957)'},
  'image_url': None,
  'fun_fact': {'uz': "Sputnik-1 ning fazodan yuborgan 'bip-bip' radioto'lqini butun dunyo bo'ylab yangradi va "
                     'insoniyatning Kosmik erasini boshlab berdi.',
               'ru': '«Спутник-1» весом всего 83,6 кг открыл Космическую эру и дал старт космической гонке между СССР '
                     'и США.',
               'en': "Sputnik 1's radio beeps circled Earth every 96 minutes in October 1957, inaugurating the Space "
                     'Age.'},
  'aliases': ['sputnik', 'sputnik 1', 'спутник-1', 'спутник 1', 'sputnik 1']},
 {'id': 'hist_time_079',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Martin Lyuter Kingning 'Menda orzu bor' (I Have a Dream) nutqi (1963 yil avgust)",
                     "Nil Armstrongning Oy sathiga qadam qo'yishi (1969 yil iyul)",
                     "Yuriy Gagarin 'Vostok-1' kemasida insoniyat tarixida ilk bor koinotga uchishi (1961 yil 12 "
                     'aprel)',
                     'Vyetnam urushining Saygon qulashi bilan tugashi (1975 yil aprel)'],
              'ru': ['Речь Мартина Лютера Кинга «У меня есть мечта» (август 1963)',
                     'Высадка Нила Армстронга на Луну (июль 1969)',
                     'Полет Юрия Гагарина на корабле «Восток-1» — первый человек в космосе (12 апреля 1961)',
                     'Падение Сайгона и конец войны во Вьетнаме (апрель 1975)'],
              'en': ["Martin Luther King's 'I Have a Dream' speech (August 1963)",
                     'Neil Armstrong walks on the Moon (July 1969)',
                     'Yuri Gagarin becomes the first human in space aboard Vostok 1 (April 12, 1961)',
                     'Fall of Saigon ending Vietnam War (April 1975)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Yuriy Gagarin 'Vostok-1' kemasida insoniyat tarixida ilk bor koinotga uchishi (1961 yil 12 "
                           'aprel)',
                     'ru': 'Полет Юрия Гагарина на корабле «Восток-1» — первый человек в космосе (12 апреля 1961)',
                     'en': 'Yuri Gagarin becomes the first human in space aboard Vostok 1 (April 12, 1961)'},
  'image_url': None,
  'fun_fact': {'uz': "Gagarin Yer atrofini 108 daqiqada aylanib chiqib: 'Ketdik!' (Poyexali!) so'zi bilan koinot "
                     'zabtkoriga aylandi.',
               'ru': '108 минут полета Юрия Гагарина навсегда изменили мир, сделав 12 апреля Всемирным днем '
                     'космонавтики.',
               'en': "Gagarin's 108-minute orbital flight on April 12, 1961 made him the first human to see Earth from "
                     'orbit.'},
  'aliases': ['gagarin', 'yuriy gagarin', 'гагарин', 'юрий гагарин', 'yuri gagarin', 'vostok 1']},
 {'id': 'hist_time_080',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Martin Lyuter King Vashingtonda mashhur nutq so'zlashi (1963 yil avgust)",
                     "Apollon-11 astronavtlari Oyga qo'nishi (1969 yil iyul)",
                     'Chernobil AESidagi halokat (1986 yil aprel)',
                     'Karib (Kuba) raketa inqirozi — dunyo yadroviy urush yoqasiga kelishi (1962 yil oktyabr)'],
              'ru': ['Марш на Вашингтон Мартина Лютера Кинга (1963)',
                     'Первая высадка человека на Луну (1969)',
                     'Авария на Чернобыльской АЭС (1986)',
                     'Карибский кризис — пик ядерного противостояния СССР и США (октябрь 1962)'],
              'en': ['March on Washington by MLK (1963)',
                     'Apollo 11 Moon landing (1969)',
                     'Chernobyl nuclear catastrophe (1986)',
                     'Cuban Missile Crisis brings world to brink of nuclear war (October 1962)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Karib (Kuba) raketa inqirozi — dunyo yadroviy urush yoqasiga kelishi (1962 yil oktyabr)',
                     'ru': 'Карибский кризис — пик ядерного противостояния СССР и США (октябрь 1962)',
                     'en': 'Cuban Missile Crisis brings world to brink of nuclear war (October 1962)'},
  'image_url': None,
  'fun_fact': {'uz': "Jon Kennedi va Nikita Xrushchev o'rtasidagi maxfiy muzokaralar natijasida sovet raketalari "
                     'Kubadan, AQSh raketalari Turkiyadan olib chiqilgan.',
               'ru': '13 дней в октябре 1962 года держали мир на волоске от глобальной термоядерной катастрофы.',
               'en': 'For 13 tense days in October 1962, the world stood at the precipice of full-scale nuclear '
                     'confrontation.'},
  'aliases': ['karib inqirozi', 'kuba inqirozi', 'карибский кризис', 'cuban missile crisis']},
 {'id': 'hist_time_081',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Nil Armstrong va Bazz Oldrin Oyga qadam qo'yishi — 'Apollon-11' (1969 yil 20 iyul)",
                     'Vyetnam urushining tugashi va Saygonning olinishi (1975 yil aprel)',
                     "Eronda Islom inqilobi va shoh rejimining ag'darilishi (1979 yil)",
                     'Chernobil AES portlashi (1986 yil aprel)'],
              'ru': ['Первая высадка людей на Луну астронавтами «Аполлона-11» (20 июля 1969)',
                     'Окончание войны во Вьетнаме (апрель 1975)',
                     'Исламская революция в Иране (1979)',
                     'Катастрофа на Чернобыльской АЭС (апрель 1986)'],
              'en': ['Neil Armstrong and Buzz Aldrin land on the Moon on Apollo 11 (July 20, 1969)',
                     'End of Vietnam War with Fall of Saigon (April 1975)',
                     'Iranian Islamic Revolution (1979)',
                     'Chernobyl disaster (April 1986)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Nil Armstrong va Bazz Oldrin Oyga qadam qo'yishi — 'Apollon-11' (1969 yil 20 iyul)",
                     'ru': 'Первая высадка людей на Луну астронавтами «Аполлона-11» (20 июля 1969)',
                     'en': 'Neil Armstrong and Buzz Aldrin land on the Moon on Apollo 11 (July 20, 1969)'},
  'image_url': None,
  'fun_fact': {'uz': "Armstrong Oy sathiga qadam qo'yayotib: 'Bu inson uchun kichik bir qadam, ammo insoniyat uchun "
                     "ulkan sakrashdir' deb tarixiy iborani aytgan.",
               'ru': 'Слова Нила Армстронга: «Это один маленький шаг для человека, но гигантский скачок для всего '
                     'человечества» услышали 650 миллионов зрителей.',
               'en': "Neil Armstrong's words on the lunar surface on July 20, 1969 were broadcast live to an estimated "
                     '650 million viewers.'},
  'aliases': ['oyga qonish', 'apollon 11', 'armstrong', 'высадка на луну', 'аполлон-11', 'moon landing', 'apollo 11']},
 {'id': 'hist_time_082',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Eronda Islom inqilobining g'alabasi (1979 yil fevral)",
                     'Saygonning Shimoliy Vyetnam kuchlari tomonidan olinishi va Vyetnam urushining tugashi (1975 yil '
                     'aprel)',
                     "Sovet qo'shinlarining Afg'onistonga kiritilishi (1979 yil dekabr)",
                     'Chernobil AES reaktori portlashi (1986 yil aprel)'],
              'ru': ['Победа Исламской революции в Иране (февраль 1979)',
                     'Падение Сайгона и объединение Вьетнама (30 апреля 1975)',
                     'Ввод советских войск в Афганистан (декабрь 1979)',
                     'Взрыв на Чернобыльской АЭС (апрель 1986)'],
              'en': ['Victory of Islamic Revolution in Iran (February 1979)',
                     'Fall of Saigon ending the Vietnam War (April 30, 1975)',
                     'Soviet invasion of Afghanistan (December 1979)',
                     'Chernobyl nuclear disaster (April 1986)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Saygonning Shimoliy Vyetnam kuchlari tomonidan olinishi va Vyetnam urushining tugashi '
                           '(1975 yil aprel)',
                     'ru': 'Падение Сайгона и объединение Вьетнама (30 апреля 1975)',
                     'en': 'Fall of Saigon ending the Vietnam War (April 30, 1975)'},
  'image_url': None,
  'fun_fact': {'uz': 'Saygon qulashi bilan 20 yil davom etgan qonli Vyetnam urushi yakunlandi va Shimoliy hamda '
                     'Janubiy Vyetnam yagona davlatga birlashdi.',
               'ru': 'Взятие Сайгона 30 апреля 1975 года положило конец почти двадцатилетней войне во Вьетнаме.',
               'en': "The Fall of Saigon on April 30, 1975 concluded the Vietnam War, leading to the country's "
                     'reunification in 1976.'},
  'aliases': ['saygon', 'vyetnam urushi', 'падение сайгона', 'война во вьетнаме', 'fall of saigon', 'vietnam war']},
 {'id': 'hist_time_083',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Berlin devorining qulashi (1989 yil noyabr)',
                     "Tim Berners-Li Butunjahon Internet tarmog'ini (WWW) ixtiro qilishi (milodiy 1989)",
                     "Chernobil atom elektr stansiyasining 4-energoblogida halokat sodir bo'lishi (1986 yil 26 aprel)",
                     'Sovet Ittifoqining (SSSR) rasman parchalanib ketishi (1991 yil dekabr)'],
              'ru': ['Падение Берлинской стены (ноябрь 1989)',
                     'Изобретение Всемирной паутины (WWW) Тимом Бернерсом-Ли (1989)',
                     'Катастрофа на 4-м энергоблоке Чернобыльской АЭС (26 апреля 1986)',
                     'Распад СССР (декабрь 1991)'],
              'en': ['Fall of the Berlin Wall (November 1989)',
                     'Tim Berners-Lee invents World Wide Web (1989)',
                     'Disaster at Chernobyl Nuclear Power Plant Reactor 4 (April 26, 1986)',
                     'Dissolution of the Soviet Union (December 1991)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Chernobil atom elektr stansiyasining 4-energoblogida halokat sodir bo'lishi (1986 yil 26 "
                           'aprel)',
                     'ru': 'Катастрофа на 4-м энергоблоке Чернобыльской АЭС (26 апреля 1986)',
                     'en': 'Disaster at Chernobyl Nuclear Power Plant Reactor 4 (April 26, 1986)'},
  'image_url': None,
  'fun_fact': {'uz': 'Chernobil halokati atom energetikasi tarixidagi eng yirik avariya hisoblanib, Pripyat shahri '
                     'butunlay tashlab ketildi.',
               'ru': 'Авария на Чернобыльской АЭС стала крупнейшей техногенной радиационной катастрофой в истории '
                     'человечества.',
               'en': 'The April 1986 Chernobyl disaster was the worst nuclear disaster in history, releasing massive '
                     'radiation across Europe.'},
  'aliases': ['chernobil', 'chernobyl', 'чернобыль', 'авария в чернобыле', 'chernobyl disaster']},
 {'id': 'hist_time_084',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Nelson Mandelaning 27 yillik qamoqdan ozod etilishi (1990 yil fevral)',
                     "O'zbekiston Respublikasining Mustaqillik e'lon qilishi (1991 yil 1 sentyabr)",
                     "SSSRning rasman faoliyatini to'xtatishi (1991 yil 26 dekabr)",
                     'Berlin devorining qulashi va Germaniyaning birlashishi jarayoni (1989 yil 9 noyabr)'],
              'ru': ['Освобождение Нельсона Манделы из тюрьмы (февраль 1990)',
                     'Провозглашение независимости Узбекистана (1 сентября 1991)',
                     'Официальный роспуск СССР (декабрь 1991)',
                     'Падение Берлинской стены и объединение Германии (9 ноября 1989)'],
              'en': ['Release of Nelson Mandela from prison (February 1990)',
                     'Proclamation of Uzbekistan Independence (September 1, 1991)',
                     'Formal dissolution of USSR (December 1991)',
                     'Fall of the Berlin Wall (November 9, 1989)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Berlin devorining qulashi va Germaniyaning birlashishi jarayoni (1989 yil 9 noyabr)',
                     'ru': 'Падение Берлинской стены и объединение Германии (9 ноября 1989)',
                     'en': 'Fall of the Berlin Wall (November 9, 1989)'},
  'image_url': None,
  'fun_fact': {'uz': "28 yil davomida G'arbiy va Sharqiy Berlinni ajratib turgan 155 kilometrlik devor 'Sovuq urush' "
                     'ramzining qulashini ifodaladi.',
               'ru': '9 ноября 1989 года Берлинская стена пала под напором сотен тысяч граждан, положив конец расколу '
                     'Европы.',
               'en': 'Erected in 1961, the Berlin Wall stood for 28 years before joyful crowds dismantled it on '
                     'November 9, 1989.'},
  'aliases': ['berlin devori',
              'berlin devorining qulashi',
              'берлинская стена',
              'падение берлинской стены',
              'berlin wall']},
 {'id': 'hist_time_085',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Nelson Mandelaning 27 yillik mahbuslikdan so'ng ozodlikka chiqishi (1990 yil 11 fevral)",
                     "O'zbekiston Respublikasining davlat mustaqilligi e'lon qilinishi (1991 yil 1 sentyabr)",
                     "Yevropa Ittifoqini tuzish bo'yicha Maastrixt shartnomasi (milodiy 1992)",
                     "JARda ilk ko'p irqli umumxalq demokratik saylovlari (milodiy 1994)"],
              'ru': ['Освобождение Нельсона Манделы после 27 лет заключения (11 февраля 1990)',
                     'Декларация независимости Республики Узбекистан (1 сентября 1991)',
                     'Маастрихтский договор о создании ЕС (1992)',
                     'Первые нерасовые выборы в ЮАР (1994)'],
              'en': ['Release of Nelson Mandela after 27 years in prison (February 11, 1990)',
                     'Proclamation of Independence of Uzbekistan (September 1, 1991)',
                     'Maastricht Treaty founding European Union (1992)',
                     'First multiracial democratic elections in South Africa (1994)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Nelson Mandelaning 27 yillik mahbuslikdan so'ng ozodlikka chiqishi (1990 yil 11 fevral)",
                     'ru': 'Освобождение Нельсона Манделы после 27 лет заключения (11 февраля 1990)',
                     'en': 'Release of Nelson Mandela after 27 years in prison (February 11, 1990)'},
  'image_url': None,
  'fun_fact': {'uz': "Mandela qamoqdan chiqqach, o'zining sobiq dushmanlariga qasos o'rniga yarashuv va kechirim "
                     "yo'lini taklif qildi va 1993 yilda Tinchlik bo'yicha Nobel mukofotini oldi.",
               'ru': 'Освобождение Манделы положило начало демонтажу режима апартеида в Южно-Африканской Республике.',
               'en': "Mandela's release in 1990 led to the peaceful dismantling of apartheid and his election as "
                     'president in 1994.'},
  'aliases': ['mandela', 'nelson mandela', 'мандела', 'нельсон мандела']},
 {'id': 'hist_time_086',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Yevropa Ittifoqini tashkil etgan Maastrixt shartnomasi imzolanishi (1992 yil fevral)',
                     "O'zbekiston Respublikasining davlat mustaqilligi e'lon qilinishi (1991 yil 31 avgust — 1 "
                     'sentyabr)',
                     'Janubiy Afrikada Mandelaning prezident etib saylanishi (1994 yil)',
                     'Vikipediyaning rasman ishga tushirilishi (2001 yil yanvar)'],
              'ru': ['Подписание Маастрихтского договора (февраль 1992)',
                     'Провозглашение государственной независимости Республики Узбекистан (1 сентября 1991)',
                     'Избрание Манделы президентом ЮАР (1994)',
                     'Запуск свободной энциклопедии Википедия (январь 2001)'],
              'en': ['Signing of the Maastricht Treaty (February 1992)',
                     'Proclamation of the State Independence of the Republic of Uzbekistan (September 1, 1991)',
                     'Nelson Mandela elected President of South Africa (1994)',
                     'Launch of Wikipedia (January 2001)']},
  'correct_index': 1,
  'correct_answer': {'uz': "O'zbekiston Respublikasining davlat mustaqilligi e'lon qilinishi (1991 yil 31 avgust — 1 "
                           'sentyabr)',
                     'ru': 'Провозглашение государственной независимости Республики Узбекистан (1 сентября 1991)',
                     'en': 'Proclamation of the State Independence of the Republic of Uzbekistan (September 1, 1991)'},
  'image_url': None,
  'fun_fact': {'uz': "1991 yil 31 avgustda O'zbekiston Oliy Kengashining navbatdan tashqari sessiyasida mustaqillik "
                     "to'g'risidagi qonun qabul qilindi va 1 sentyabr Mustaqillik kuni deb belgilandi.",
               'ru': '1 сентября 1991 года Узбекистан обрел суверенитет, открыв новую страницу в тысячелетней истории '
                     'своего народа.',
               'en': 'On August 31, 1991, Uzbekistan declared sovereign statehood, celebrated annually on September 1 '
                     'as Independence Day.'},
  'aliases': ['ozbekiston mustaqilligi', 'mustaqillik kuni', 'независимость узбекистана', 'uzbekistan independence']},
 {'id': 'hist_time_087',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Xalqaro Koinot Stansiyasining (XKS) ilk moduli 'Zarya' uchirilishi (1998 yil)",
                     'Yevro valyutasining naqd pulsiz muomalaga kiritilishi (1999 yil)',
                     "Janubiy Afrika Respublikasida ilk bor barcha irqlar qatnashgan saylov o'tkazilishi va "
                     "Mandelaning g'alabasi (1994 yil aprel)",
                     'Vikipediya erkin ensiklopediyasining ochilishi (2001 yil)'],
              'ru': ['Запуск первого модуля МКС «Заря» (1998)',
                     'Введение евро в безналичный оборот (1999)',
                     'Первые всеобщие многорасовые выборы в ЮАР и победа Нельсона Манделы (апрель 1994)',
                     'Запуск Википедии (2001)'],
              'en': ['Launch of first ISS module Zarya (1998)',
                     'Introduction of Euro currency (1999)',
                     'First multiracial democratic elections in South Africa: Mandela elected president (April 1994)',
                     'Launch of Wikipedia (2001)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Janubiy Afrika Respublikasida ilk bor barcha irqlar qatnashgan saylov o'tkazilishi va "
                           "Mandelaning g'alabasi (1994 yil aprel)",
                     'ru': 'Первые всеобщие многорасовые выборы в ЮАР и победа Нельсона Манделы (апрель 1994)',
                     'en': 'First multiracial democratic elections in South Africa: Mandela elected president (April '
                           '1994)'},
  'image_url': None,
  'fun_fact': {'uz': "1994 yilgi saylovlarda qora tanli fuqarolar o'z hayotlarida birinchi marta ovoz berishdi va "
                     "aparteid tuzumi tarixga ko'mildi.",
               'ru': 'Выборы 1994 года мирно завершили эпоху расовой дискриминации и создали «Радужную нацию».',
               'en': 'The 1994 elections saw millions of Black South Africans vote for the first time, ending decades '
                     'of apartheid.'},
  'aliases': ['mandela saylovi', 'jar saylovlari', 'выборы в юар', 'south africa 1994']},
 {'id': 'hist_time_088',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Yevro qog'oz kupyuralari va tangalarining naqd muomalaga chiqishi (2002 yil yanvar)",
                     'Inson genomi loyihasining muvaffaqiyatli yakunlanishi (2003 yil aprel)',
                     "Facebook ijtimoiy tarmog'ining Garvardda ishga tushishi (2004 yil fevral)",
                     "Xalqaro Koinot Stansiyasining (XKS) ilk moduli — 'Zarya' orbitaga chiqarilishi (1998 yil "
                     'noyabr)'],
              'ru': ['Введение наличного евро в обращение (январь 2002)',
                     'Завершение проекта «Геном человека» (апрель 2003)',
                     'Запуск социальной сети Facebook (февраль 2004)',
                     'Запуск функционально-грузового блока «Заря» — начало создания МКС (ноябрь 1998)'],
              'en': ['Euro notes and coins enter physical circulation (January 2002)',
                     'Completion of the Human Genome Project (April 2003)',
                     'Launch of Facebook at Harvard (February 2004)',
                     'Launch of Zarya module, beginning construction of the ISS (November 1998)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Xalqaro Koinot Stansiyasining (XKS) ilk moduli — 'Zarya' orbitaga chiqarilishi (1998 yil "
                           'noyabr)',
                     'ru': 'Запуск функционально-грузового блока «Заря» — начало создания МКС (ноябрь 1998)',
                     'en': 'Launch of Zarya module, beginning construction of the ISS (November 1998)'},
  'image_url': None,
  'fun_fact': {'uz': "XKS insoniyat tarixidagi eng yirik va eng qimmat kosmik xalqaro loyiha bo'lib, 16 ta davlat "
                     'hamkorligida boshqariladi.',
               'ru': 'МКС — крупнейший искусственный спутник Земли, на котором непрерывно живут и работают космонавты '
                     'с 2000 года.',
               'en': 'The ISS has been continuously inhabited since November 2000, representing the greatest '
                     'international engineering feat in space.'},
  'aliases': ['xks', 'xalqaro koinot stansiyasi', 'мкс', 'заря', 'iss', 'international space station']},
 {'id': 'hist_time_089',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Jimmi Ueyls va Larri Sanger tomonidan Vikipediyaning ishga tushirilishi (2001 yil 15 yanvar)',
                     "Inson genomi to'liq o'qib chiqilishi (2003 yil aprel)",
                     "Mark Sukerberg tomonidan Facebook tarmog'i yaratilishi (2004 yil fevral)",
                     'Stiv Jobs ilk iPhone smartfonini taqdim etishi (2007 yil yanvar)'],
              'ru': ['Запуск свободной интернет-энциклопедии Википедия (15 января 2001)',
                     'Расшифровка генома человека (апрель 2003)',
                     'Создание Facebook Марком Цукербергом (февраль 2004)',
                     'Презентация первого iPhone Стивом Джобсом (январь 2007)'],
              'en': ['Launch of Wikipedia by Jimmy Wales and Larry Sanger (January 15, 2001)',
                     'Sequencing of the human genome (April 2003)',
                     'Mark Zuckerberg launches Facebook (February 2004)',
                     'Steve Jobs unveils original iPhone (January 2007)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Jimmi Ueyls va Larri Sanger tomonidan Vikipediyaning ishga tushirilishi (2001 yil 15 '
                           'yanvar)',
                     'ru': 'Запуск свободной интернет-энциклопедии Википедия (15 января 2001)',
                     'en': 'Launch of Wikipedia by Jimmy Wales and Larry Sanger (January 15, 2001)'},
  'image_url': None,
  'fun_fact': {'uz': "Bugungi kunda Vikipediya 300 dan ortiq tilda 60 milliondan ortiq maqolaga ega bo'lib, jahonning "
                     "eng yirik ochiq ma'lumot xazinasidir.",
               'ru': 'Википедия стала крупнейшей и самой популярной энциклопедией в истории человечества, создаваемой '
                     'добровольцами со всего мира.',
               'en': 'Launched on January 15, 2001, Wikipedia now contains over 60 million articles in 300+ '
                     'languages.'},
  'aliases': ['vikipediya', 'википедия', 'wikipedia']},
 {'id': 'hist_time_090',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['CERNda Katta adron kollayderining ishga tushirilishi (2008 yil sentyabr)',
                     'Stiv Jobs tomonidan birinchi iPhone smartfonining ommaga taqdim etilishi (2007 yil 9 yanvar)',
                     "Jahon moliyaviy inqirozining cho'qqisiga chiqishi (2008 yil kuzi)",
                     "Marsga 'Kyuriositi' (Curiosity) marsoxodining muvaffaqiyatli qo'nishi (2012 yil avgust)"],
              'ru': ['Запуск Большого адронного коллайдера в ЦЕРН (сентябрь 2008)',
                     'Стив Джобс представляет первый революционный смартфон iPhone (9 января 2007)',
                     'Мировой финансовый кризис (осень 2008)',
                     'Посадка марсохода Curiosity на Марс (август 2012)'],
              'en': ['Large Hadron Collider begins operation (September 2008)',
                     'Steve Jobs unveils the original Apple iPhone (January 9, 2007)',
                     'Global Financial Crisis peaks (Autumn 2008)',
                     'Curiosity rover lands on Mars (August 2012)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Stiv Jobs tomonidan birinchi iPhone smartfonining ommaga taqdim etilishi (2007 yil 9 '
                           'yanvar)',
                     'ru': 'Стив Джобс представляет первый революционный смартфон iPhone (9 января 2007)',
                     'en': 'Steve Jobs unveils the original Apple iPhone (January 9, 2007)'},
  'image_url': None,
  'fun_fact': {'uz': "Stiv Jobs iPhone taqdimotida uni 'keng ekranli iPod, inqilobiy mobil telefon va internet aloqa "
                     "qurilmasi' deb atagan.",
               'ru': 'Появление iPhone в 2007 году положило начало эре современных сенсорных мобильных устройств и '
                     'мобильного интернета.',
               'en': 'On January 9, 2007, Steve Jobs introduced the iPhone, redefining mobile technology and consumer '
                     'electronics.'},
  'aliases': ['iphone', 'ayfon', 'stiv jobs', 'айфон', 'стив джобс', 'steve jobs']},
 {'id': 'hist_time_091',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Britaniyada Rim imperatori Adrian devorining qurilishi (milodiy 122)',
                     'Yustinian I Konstantinopolda Ayasofya soborini qurdirishi (milodiy 537)',
                     'Qin Shixuandi tomonidan Buyuk Xitoy devorining ilk mudofaa qismlari birlashtirilishi (~mil. avv. '
                     '215)',
                     'Granadada Al-Hamro (Alhambra) saroyining barpo etilishi (milodiy 1333)'],
              'ru': ['Строительство Вала Адриана в Британии (122 н.э.)',
                     'Строительство собора Святой Софии Юстинианом (537 н.э.)',
                     'Строительство первой объединенной Великой Китайской стены императором Цинь (~215 до н.э.)',
                     'Возведение дворца Альгамбра в Гранаде (1333 н.э.)'],
              'en': ["Construction of Hadrian's Wall in Britain (122 AD)",
                     'Justinian builds Hagia Sophia (537 AD)',
                     'Qin Shi Huang begins linking the Great Wall of China (~215 BC)',
                     'Construction of the Alhambra palaces (1333 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Qin Shixuandi tomonidan Buyuk Xitoy devorining ilk mudofaa qismlari birlashtirilishi '
                           '(~mil. avv. 215)',
                     'ru': 'Строительство первой объединенной Великой Китайской стены императором Цинь (~215 до н.э.)',
                     'en': 'Qin Shi Huang begins linking the Great Wall of China (~215 BC)'},
  'image_url': None,
  'fun_fact': {'uz': 'Birinchi Xitoy imperatori Qin Shixuandi xunnular hujumidan himoyalanish uchun shimoliy chegara '
                     'devorlarini yaxlit mudofaa tizimiga birlashtirgan.',
               'ru': 'Император Цинь Шихуанди соединил разрозненные стены северных царств для защиты от кочевников '
                     'хунну.',
               'en': 'Qin Shi Huang linked separate border ramparts around 215 BC to defend unified China against '
                     'Xiongnu incursions.'},
  'aliases': ['buyuk xitoy devori', 'xitoy devori', 'великая китайская стена', 'great wall', 'great wall of china']},
 {'id': 'hist_time_092',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Vilgelm Fathchining Angliyani bosib olishi (milodiy 1066)',
                     'Parij Notr-Dam soborining qurilishi boshlanishi (milodiy 1163)',
                     'Atsteklar tomonidan Tenochtitlan shahriga asos solinishi (milodiy 1325)',
                     'Fotimiylar xalifaligi tomonidan Qohira (Al-Qohira) shahriga asos solinishi (milodiy 969)'],
              'ru': ['Нормандское завоевание Англии (1066 н.э.)',
                     'Начало строительства Нотр-Дам де Пари (1163 н.э.)',
                     'Основание Теночтитлана ацтеками (1325 н.э.)',
                     'Основание Каира фатимидским полководцем Джаухаром (969 н.э.)'],
              'en': ['Norman conquest of England (1066 AD)',
                     'Construction of Notre-Dame begins (1163 AD)',
                     'Founding of Tenochtitlan by the Aztecs (1325 AD)',
                     'Founding of Cairo (Al-Qahira) by the Fatimid Caliphate (969 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Fotimiylar xalifaligi tomonidan Qohira (Al-Qohira) shahriga asos solinishi (milodiy 969)',
                     'ru': 'Основание Каира фатимидским полководцем Джаухаром (969 н.э.)',
                     'en': 'Founding of Cairo (Al-Qahira) by the Fatimid Caliphate (969 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Qohira arabcha 'Al-Qohira' — 'G'olib' yoki 'Zafarli' degan ma'noni anglatadi va Mars "
                     "sayyorasining osmonda ko'rinishi sharafiga nomlangan.",
               'ru': 'Название Каира переводится как «Победоносный», а основанная здесь мечеть Аль-Азхар стала '
                     'старейшим университетом региона.',
               'en': "Cairo ('The Victorious') was established in 969 AD, and the Al-Azhar mosque-university was begun "
                     'shortly after.'},
  'aliases': ['qohira', 'al-qohira', 'каир', 'cairo']},
 {'id': 'hist_time_093',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ['Xorazmshoh Aloviddin Muhammadning Samarqandni poytaxtga aylantirishi (milodiy 1207-1212)',
                     "Mo'g'ullarning Xorazmshohlar davlatiga halokatli bosqini (milodiy 1219-1221)",
                     "Muz ustidagi jang (Chud ko'lida) (milodiy 1242)",
                     'Marko Poloning Pekinga yetib borishi (milodiy 1275)'],
              'ru': ['Хорезмшах Ала ад-Дин Мухаммед делает Самарканд своей столицей (1207–1212 н.э.)',
                     'Вторжение Чингисхана в государство Хорезмшахов (1219–1221 н.э.)',
                     'Ледовое побоище (1242 н.э.)',
                     'Прибытие Марко Поло в Пекин (1275 н.э.)'],
              'en': ['Khwarazmshah Ala ad-Din Muhammad takes Samarkand as capital (1207–1212 AD)',
                     'Mongol invasion of Khwarazm (1219–1221 AD)',
                     'Battle of the Ice (1242 AD)',
                     'Marco Polo reaches Beijing (1275 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Xorazmshoh Aloviddin Muhammadning Samarqandni poytaxtga aylantirishi (milodiy 1207-1212)',
                     'ru': 'Хорезмшах Ала ад-Дин Мухаммед делает Самарканд своей столицей (1207–1212 н.э.)',
                     'en': 'Khwarazmshah Ala ad-Din Muhammad takes Samarkand as capital (1207–1212 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Xorazmshoh Aloviddin Muhammad davrida saltanat Kaspiy dengizidan to Hindistongacha cho'zilgan, "
                     "ammo O'tror fojiasi mo'g'ul bosqiniga sabab bo'lgan.",
               'ru': 'Государство Хорезмшахов перед монгольским нашествием было крупнейшей империей Среднего Востока.',
               'en': 'Under Ala ad-Din Muhammad, Khwarazm reached its peak territorial expanse before the catastrophic '
                     'Mongol invasion of 1219.'},
  'aliases': ['xorazmshoh', 'aloviddin muhammad', 'хорезмшах', 'самарканд', 'khwarazmshah']},
 {'id': 'hist_time_094',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Yevropada 'Qora o'lat' epidemiyasining tarqalishi (milodiy 1347)",
                     "Ibn Battutaning Tangerdan 30 yillik dunyo bo'ylab sayohatini boshlashi (milodiy 1325)",
                     'Amir Temurning 5 yillik yurishi boshlanishi (milodiy 1392)',
                     "Chjen Xe 'Xazina flotiliyasi'ning ilk ekspeditsiyasi (milodiy 1405)"],
              'ru': ['Черная смерть в Европе (1347 н.э.)',
                     'Начало 30-летних странствий великого путешественника Ибн Баттуты (1325 н.э.)',
                     'Пятилетний поход Амира Темура (1392 н.э.)',
                     'Первое плавание китайского адмирала Чжэн Хэ (1405 н.э.)'],
              'en': ['Black Death in Europe (1347 AD)',
                     'Ibn Battuta begins his epic 30-year journey across the known world (1325 AD)',
                     'Amir Timur begins Five-Year Campaign (1392 AD)',
                     "Zheng He's first treasure voyage (1405 AD)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Ibn Battutaning Tangerdan 30 yillik dunyo bo'ylab sayohatini boshlashi (milodiy 1325)",
                     'ru': 'Начало 30-летних странствий великого путешественника Ибн Баттуты (1325 н.э.)',
                     'en': 'Ibn Battuta begins his epic 30-year journey across the known world (1325 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Ibn Battuta 117 000 kilometrdan ortiq masofani bosib o'tib, O'rta Osiyo (Samarqand, Buxoro, "
                     "Urganch), Xitoy, Hindiston va Afrikada bo'lgan.",
               'ru': 'Ибн Баттута преодолел более 117 тысяч километров, оставив подробнейшие описания средневекового '
                     'Мавераннахра, Индии и Китая.',
               'en': 'Ibn Battuta logged roughly 73,000 miles over 30 years, including visits to Samarkand, Bukhara, '
                     'Mecca, and China.'},
  'aliases': ['ibn battuta', 'ибн баттута', 'ibn battuta']},
 {'id': 'hist_time_095',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Janna d'Arkning Ruanda gulxanda yoqilishi (milodiy 1431)",
                     'Konstantinopolning qulashi (milodiy 1453)',
                     "Xitoy admirali Chjen Xe o'zining ulkan 'Xazina kemalari' bilan ilk dengiz sayohatiga chiqishi "
                     '(milodiy 1405)',
                     'Kolumbning Amerikani kashf qilishi (milodiy 1492)'],
              'ru': ["Казнь Жанны д'Арк в Руане (1431 н.э.)",
                     'Падение Константинополя (1453 н.э.)',
                     'Первая морская экспедиция китайского адмирала Чжэн Хэ (1405 н.э.)',
                     'Открытие Америки Колумбом (1492 н.э.)'],
              'en': ['Execution of Joan of Arc in Rouen (1431 AD)',
                     'Fall of Constantinople (1453 AD)',
                     'Admiral Zheng He launches the first Ming treasure fleet expedition (1405 AD)',
                     'Columbus reaches the Americas (1492 AD)']},
  'correct_index': 2,
  'correct_answer': {'uz': "Xitoy admirali Chjen Xe o'zining ulkan 'Xazina kemalari' bilan ilk dengiz sayohatiga "
                           'chiqishi (milodiy 1405)',
                     'ru': 'Первая морская экспедиция китайского адмирала Чжэн Хэ (1405 н.э.)',
                     'en': 'Admiral Zheng He launches the first Ming treasure fleet expedition (1405 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Chjen Xe flotiliyasidagi kemalar uzunligi 120 metrga yetgan bo'lib, Kolumbning 'Santa-Mariya' "
                     "kemasidan 4 barobar katta bo'lgan.",
               'ru': 'Гигантские деревянные джонки Чжэн Хэ бороздили Индийский океан за десятилетия до португальских '
                     'каравелл.',
               'en': 'Zheng He commanded armada vessels over 100 meters long, dwarfing contemporary European ships.'},
  'aliases': ['chjen xe', 'чжэн хэ', 'zheng he']},
 {'id': 'hist_time_096',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Tixo Brage osmonda yangi yulduz (o'ta yangi yulduz) portlashini kuzatishi (milodiy 1572)",
                     'Iogann Kepler sayyoralar harakatining qonunlarini kashf etishi (milodiy 1609)',
                     "Isaak Nyuton butunjahon tortishish qonunini ta'riflashi (milodiy 1687)",
                     "Nikolay Kopernik 'Osmon sferalarining aylanishi haqida' geliotsentrik asarini nashr ettirishi "
                     '(milodiy 1543)'],
              'ru': ['Наблюдение сверхновой звезды Тихо Браге (1572 н.э.)',
                     'Открытие законов движения планет Иоганном Кеплером (1609 н.э.)',
                     'Формулировка закона тяготения Ньютоном (1687 н.э.)',
                     'Публикация труда Николая Коперника о гелиоцентрической системе мира (1543 н.э.)'],
              'en': ['Tycho Brahe observes supernova (1572 AD)',
                     'Kepler publishes laws of planetary motion (1609 AD)',
                     'Newton states universal gravitation (1687 AD)',
                     'Copernicus publishes On the Revolutions of Heavenly Spheres (1543 AD)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Nikolay Kopernik 'Osmon sferalarining aylanishi haqida' geliotsentrik asarini nashr "
                           'ettirishi (milodiy 1543)',
                     'ru': 'Публикация труда Николая Коперника о гелиоцентрической системе мира (1543 н.э.)',
                     'en': 'Copernicus publishes On the Revolutions of Heavenly Spheres (1543 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Kopernik Quyoshni olam markaziga qo'yib, Yer uning atrofida aylanadigan sayyoralardan biri "
                     'ekanini ilmiy asoslab berdi.',
               'ru': 'Коперник «остановил Солнце и сдвинул Землю», положив начало научной революции эпохи Возрождения.',
               'en': 'Copernicus published his heliocentric model on his deathbed in 1543, shifting the center of the '
                     'known cosmos from Earth to the Sun.'},
  'aliases': ['kopernik', 'geliotsentrizm', 'коперник', 'гелиоцентризм', 'copernicus']},
 {'id': 'hist_time_097',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Rossiya, Prussiya va Avstriya tomonidan Polshaning (Rech Pospolita) birinchi bo'lib olinishi "
                     '(milodiy 1772)',
                     'Leksington jangi bilan Amerika mustaqillik urushi boshlanishi (milodiy 1775)',
                     "Fransiyada Bastiliya qal'asining egallanishi (milodiy 1789)",
                     'Vena kongressining boshlanishi (milodiy 1814)'],
              'ru': ['Первый раздел Речи Посполитой между Россией, Пруссией и Австрией (1772 н.э.)',
                     'Битва при Лексингтоне в Америке (1775 н.э.)',
                     'Взятие Бастилии (1789 н.э.)',
                     'Открытие Венского конгресса (1814 н.э.)'],
              'en': ['First Partition of Poland by Russia, Prussia, and Austria (1772 AD)',
                     'Battle of Lexington begins American Revolution (1775 AD)',
                     'Storming of the Bastille (1789 AD)',
                     'Opening of Congress of Vienna (1814 AD)']},
  'correct_index': 0,
  'correct_answer': {'uz': "Rossiya, Prussiya va Avstriya tomonidan Polshaning (Rech Pospolita) birinchi bo'lib "
                           'olinishi (milodiy 1772)',
                     'ru': 'Первый раздел Речи Посполитой между Россией, Пруссией и Австрией (1772 н.э.)',
                     'en': 'First Partition of Poland by Russia, Prussia, and Austria (1772 AD)'},
  'image_url': None,
  'fun_fact': {'uz': "Polsha 1772, 1793 va 1795 yillardagi uchta bo'linish natijasida 123 yil davomida dunyo "
                     "xaritasidan butunlay yo'qolib ketgan.",
               'ru': 'В результате трех разделов Речь Посполитая прекратила существование как суверенное государство '
                     'до 1918 года.',
               'en': 'The First Partition in 1772 initiated the piecemeal division of Poland, erasing it from European '
                     'maps until 1918.'},
  'aliases': ['polsha bolinishi', 'rech pospolita', 'раздел польши', 'partition of poland']},
 {'id': 'hist_time_098',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Jan-Fransua Shampolion Qadimgi Misr ierogliflarini o'qishga muvaffaq bo'lishi (milodiy 1822)",
                     'Napoleonning Misr yurishida Rozetta toshining topilishi (milodiy 1799)',
                     'Genrix Shliman afsonaviy Troya xarobalarini topishi (milodiy 1871)',
                     'Govard Karter Tutanxamon maqbarasini ochishi (milodiy 1922)'],
              'ru': ['Дешифровка египетских иероглифов Жан-Франсуа Шампольоном (1822 н.э.)',
                     'Обнаружение Розеттского камня французскими солдатами в Египте (1799 н.э.)',
                     'Раскопки Трои Генрихом Шлиманом (1871 н.э.)',
                     'Открытие гробницы Тутанхамона Говардом Картером (1922 н.э.)'],
              'en': ['Champollion deciphers hieroglyphs (1822 AD)',
                     'Discovery of the Rosetta Stone in Egypt (1799 AD)',
                     'Heinrich Schliemann discovers Troy (1871 AD)',
                     "Howard Carter discovers Tutankhamun's tomb (1922 AD)"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Napoleonning Misr yurishida Rozetta toshining topilishi (milodiy 1799)',
                     'ru': 'Обнаружение Розеттского камня французскими солдатами в Египте (1799 н.э.)',
                     'en': 'Discovery of the Rosetta Stone in Egypt (1799 AD)'},
  'image_url': None,
  'fun_fact': {'uz': 'Rozetta toshida bitta matn uch tilda (ieroglif, demotik va yunoncha) yozilgani sababli, u '
                     'qadimgi Misr yozuvini ochish kalitiga aylandi.',
               'ru': 'Находка плиты с параллельным греческим и иероглифическим текстом позволила расшифровать '
                     'письменность фараонов.',
               'en': 'Discovered in 1799, the bilingual decree on the Rosetta Stone provided the key that unlocked '
                     'ancient Egyptian hieroglyphs.'},
  'aliases': ['rozetta toshi', 'rozetta', 'розеттский камень', 'rosetta stone']},
 {'id': 'hist_time_099',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Titanik yo'lovchi kemasining cho'kishi (1912 yil aprel)",
                     'Panama kanalining ochilishi (1914 yil avgust)',
                     'Rual Amundsen ekspeditsiyasi Janubiy qutbga yetib borishi (1911 yil dekabr)',
                     'Charlz Lindbergning Atlantika okeani uzra yakka parvozi (1927 yil may)'],
              'ru': ['Гибель «Титаника» (апрель 1912)',
                     'Открытие Панамского канала (август 1914)',
                     'Экспедиция Руаля Амундсена достигает Южного полюса (декабрь 1911)',
                     'Перелет Чарльза Линдберга через Атлантику (май 1927)'],
              'en': ['Sinking of Titanic (April 1912)',
                     'Opening of Panama Canal (August 1914)',
                     "Roald Amundsen's expedition reaches the South Pole (December 1911)",
                     "Lindbergh's solo transatlantic flight (May 1927)"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Rual Amundsen ekspeditsiyasi Janubiy qutbga yetib borishi (1911 yil dekabr)',
                     'ru': 'Экспедиция Руаля Амундсена достигает Южного полюса (декабрь 1911)',
                     'en': "Roald Amundsen's expedition reaches the South Pole (December 1911)"},
  'image_url': None,
  'fun_fact': {'uz': 'Norvegiyalik Amundsen it chanalari yordamida Janubiy qutbga Robert Skottdan 34 kun oldin yetib '
                     'borgan.',
               'ru': '14 декабря 1911 года норвежский флаг впервые взвился на Южном полюсе Земли.',
               'en': 'On December 14, 1911, Roald Amundsen became the first human to stand at the South Pole, beating '
                     'Robert Falcon Scott.'},
  'aliases': ['amundsen', 'janubiy qutb', 'амундсен', 'южный полюс', 'roald amundsen', 'south pole']},
 {'id': 'hist_time_100',
  'sub_mode': 'timeline',
  'question': {'uz': "Ushbu tarixiy voqealardan qaysi biri eng avval (boshqalaridan oldin) sodir bo'lgan?",
               'ru': 'Какое из этих исторических событий произошло раньше остальных?',
               'en': 'Which of these historical events occurred earliest in history?'},
  'options': {'uz': ["Ameliya Erxartning Atlantika uzra ayollar o'rtasida ilk yakka parvozi (1932 yil may)",
                     'Chak Yeger birinchi marta tovush tezligidan tez uchishi (1947 yil oktyabr)',
                     'Yuriy Gagarinning fazoga parvozi (1961 yil aprel)',
                     "Charlz Lindberg 'Spirit of St. Louis' samolyotida Atlantika uzra birinchi to'xtovsiz yakka "
                     'parvozni amalga oshirishi (1927 yil may)'],
              'ru': ['Одиночный перелет Амелии Эрхарт через Атлантику (май 1932)',
                     'Преодоление звукового барьера Чаком Йегером (1947)',
                     'Полет Гагарина в космос (1961)',
                     'Чарльз Линдберг совершает первый беспосадочный одиночный перелет через Атлантику (май 1927)'],
              'en': ["Amelia Earhart's solo transatlantic flight (May 1932)",
                     'Chuck Yeager breaks sound barrier (October 1947)',
                     'Yuri Gagarin orbits Earth (April 1961)',
                     'Charles Lindbergh completes first solo nonstop transatlantic flight (May 1927)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Charlz Lindberg 'Spirit of St. Louis' samolyotida Atlantika uzra birinchi to'xtovsiz yakka "
                           'parvozni amalga oshirishi (1927 yil may)',
                     'ru': 'Чарльз Линдберг совершает первый беспосадочный одиночный перелет через Атлантику (май '
                           '1927)',
                     'en': 'Charles Lindbergh completes first solo nonstop transatlantic flight (May 1927)'},
  'image_url': None,
  'fun_fact': {'uz': 'Lindberg Nyu-Yorkdan Parijgacha 33,5 soat davomida uxlamasdan uchgan va uni Parijda 150 000 '
                     'kishi kutib olgan.',
               'ru': 'Линдберг в одиночку преодолел почти 6000 км над бушующей Атлантикой без автопилота и радиосвязи.',
               'en': 'Lindbergh flew 33.5 hours solo from Long Island to Paris in May 1927, instantly becoming an '
                     'international aviation hero.'},
  'aliases': ['lindberg', 'charlz lindberg', 'линдберг', 'чарльз линдберг', 'lindbergh', 'charles lindbergh']},
 {'id': 'hist_map_001',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Ahamoniylar (Fors) imperiyasi',
                     'Parfiya podsholigi',
                     'Sosoniylar saltanati',
                     'Salavkiylar davlati'],
              'ru': ['Держава Ахеменидов (Персидская империя)',
                     'Парфянское царство',
                     'Государство Сасанидов',
                     'Государство Селевкидов'],
              'en': ['Achaemenid Empire (First Persian Empire)',
                     'Parthian Empire',
                     'Sasanian Empire',
                     'Seleucid Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Ahamoniylar (Fors) imperiyasi',
                     'ru': 'Держава Ахеменидов (Персидская империя)',
                     'en': 'Achaemenid Empire (First Persian Empire)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Achaemenid_Empire_at_its_greatest_extent.png/1024px-Achaemenid_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': "Buyuk Kir va Doro I davrida Ahamoniylar dunyo aholisining qariyb 44 foizini o'z ichiga olgan "
                     "tarixdagi ilk jahon imperiyasi bo'lgan.",
               'ru': 'Империя Ахеменидов при Дарии I простиралась от Египта и Фракии до реки Инд, охватывая до 44% '
                     'населения Земли.',
               'en': "At its peak under Darius I, the Achaemenid Empire ruled over an estimated 44% of the world's "
                     'population.'},
  'aliases': ['ahamoniylar', 'fors imperiyasi', 'ахемениды', 'персидская империя', 'achaemenid', 'persian empire']},
 {'id': 'hist_map_002',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Rim imperiyasi',
                     'Aleksandr Makedonskiy imperiyasi',
                     'Vizantiya imperiyasi',
                     'Salavkiylar davlati'],
              'ru': ['Римская империя',
                     'Империя Александра Македонского',
                     'Византийская империя',
                     'Государство Селевкидов'],
              'en': ['Roman Empire', 'Empire of Alexander the Great', 'Byzantine Empire', 'Seleucid Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Aleksandr Makedonskiy imperiyasi',
                     'ru': 'Империя Александра Македонского',
                     'en': 'Empire of Alexander the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Macedonian_Empire.jpg/1024px-Macedonian_Empire.jpg',
  'fun_fact': {'uz': "Aleksandr atigi 12 yil ichida Yunonistondan Hind daryosigacha bo'lgan hududni zabt etib, "
                     'ellinizm madaniyatini yoydi.',
               'ru': 'Александр Великий создал империю, раскинувшуюся от Балкан до Индии, заложив основы эпохи '
                     'эллинизма.',
               'en': 'Alexander conquered from Greece to the Indus River within twelve years, dying undefeated in '
                     'battle at age 32.'},
  'aliases': ['aleksandr makedonskiy',
              'makedoniya imperiyasi',
              'александр македонский',
              'alexander the great',
              'macedonian empire']},
 {'id': 'hist_map_003',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Franklar imperiyasi',
                     'Muqaddas Rim imperiyasi',
                     'Rim imperiyasi (Trayan davri)',
                     'Karfagen davlati'],
              'ru': ['Франкская империя',
                     'Священная Римская империя',
                     'Римская империя (эпоха Траяна)',
                     'Карфагенская держава'],
              'en': ['Frankish Empire', 'Holy Roman Empire', 'Roman Empire (under Trajan)', 'Carthaginian Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Rim imperiyasi (Trayan davri)',
                     'ru': 'Римская империя (эпоха Траяна)',
                     'en': 'Roman Empire (under Trajan)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Roman_Empire_Trajan_117AD.png/1024px-Roman_Empire_Trajan_117AD.png',
  'fun_fact': {'uz': "Milodiy 117 yilda imperator Trayan davrida Rim imperiyasi o'zining eng katta kengligiga (5 "
                     "million kv km) erishib, O'rta yer dengizini 'Bizning dengiz' (Mare Nostrum) deb atagan.",
               'ru': 'При императоре Траяне в 117 году н.э. Рим охватывал все побережье Средиземного моря, Британию, '
                     'Месопотамию и Дакию.',
               'en': 'In 117 AD, Emperor Trajan pushed Roman borders to their maximum extent, encircling the '
                     'Mediterranean Sea.'},
  'aliases': ['rim imperiyasi', 'римская империя', 'roman empire', 'rome']},
 {'id': 'hist_map_004',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Usmonli imperiyasi',
                     'Lotin imperiyasi',
                     'Venetsiya respublikasi',
                     'Vizantiya (Sharqiy Rim) imperiyasi (Yustinian I davri)'],
              'ru': ['Османская империя',
                     'Латинская империя',
                     'Венецианская республика',
                     'Византийская империя (эпоха Юстиниана I)'],
              'en': ['Ottoman Empire', 'Latin Empire', 'Venetian Republic', 'Byzantine Empire (under Justinian I)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Vizantiya (Sharqiy Rim) imperiyasi (Yustinian I davri)',
                     'ru': 'Византийская империя (эпоха Юстиниана I)',
                     'en': 'Byzantine Empire (under Justinian I)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Byzantine_Empire_555_AD.png/1024px-Byzantine_Empire_555_AD.png',
  'fun_fact': {'uz': 'Yustinian I davrida sarkarda Velisariy Italiya, Shimoliy Afrika va Ispaniya janubini qaytarib '
                     'olib, qadimgi Rim hududlarini qisman tiklagan.',
               'ru': 'При Юстиниане I в 555 году Византия отвоевала Рим, Карфаген и Равенну, вернув значительную часть '
                     'западных владений.',
               'en': "Justinian I's generals Belisarius and Narses recaptured Italy and North Africa, expanding "
                     'Byzantine territory to its height in 555 AD.'},
  'aliases': ['vizantiya', 'sharqiy rim', 'византия', 'византийская империя', 'byzantine', 'byzantine empire']},
 {'id': 'hist_map_005',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["Mo'g'ullar imperiyasi", 'Sin imperiyasi (Xitoy)', 'Rossiya imperiyasi', 'Turk xoqonligi'],
              'ru': ['Монгольская империя', 'Империя Цин', 'Российская империя', 'Тюркский каганат'],
              'en': ['Mongol Empire', 'Qing Empire', 'Russian Empire', 'Turkic Khaganate']},
  'correct_index': 0,
  'correct_answer': {'uz': "Mo'g'ullar imperiyasi", 'ru': 'Монгольская империя', 'en': 'Mongol Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Mongol_Empire_map.gif/1024px-Mongol_Empire_map.gif',
  'fun_fact': {'uz': "Mo'g'ullar saltanati tarixdagi eng ulkan tutash quruqlik imperiyasi bo'lib, Tinch okeanidan to "
                     'Markaziy Yevropagacha 24 million kv km ni egallagan.',
               'ru': 'Монгольская империя была крупнейшим единым континентальным государством в истории, занимая 24 '
                     'млн кв. км.',
               'en': 'The Mongol Empire was the largest contiguous land empire in human history, stretching from the '
                     'Sea of Japan to the Danube.'},
  'aliases': ['mogullar imperiyasi', 'chingizxon saltanati', 'монгольская империя', 'mongol empire']},
 {'id': 'hist_time_map_006',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Xorazmshohlar davlati',
                     'Temuriylar saltanati (Amir Temur davlati)',
                     'Saljuqiylar saltanati',
                     'Safaviylar davlati'],
              'ru': ['Государство Хорезмшахов',
                     'Империя Тимуридов (государство Амира Темура)',
                     'Сельджукская империя',
                     'Государство Сефевидов'],
              'en': ['Khwarazmian Empire', 'Timurid Empire (State of Amir Timur)', 'Seljuk Empire', 'Safavid Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Temuriylar saltanati (Amir Temur davlati)',
                     'ru': 'Империя Тимуридов (государство Амира Темура)',
                     'en': 'Timurid Empire (State of Amir Timur)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Timurid_Empire_1405.png/1024px-Timurid_Empire_1405.png',
  'fun_fact': {'uz': "Amir Temur poytaxt Samarqanddan turib Hindistondan O'rta yer dengizigacha, Volga daryosidan Fors "
                     "ko'rfazigacha bo'lgan hududni boshqargan.",
               'ru': 'Империя Тимуридов со столицей в Самарканде объединяла земли Центральной Азии, Ирана, '
                     'Афганистана, Месопотамии и Кавказа.',
               'en': 'With Samarkand as its magnificent capital, the Timurid Empire stretched from Delhi to the Aegean '
                     'Sea and Moscow borders.'},
  'aliases': ['temuriylar', 'amir temur davlati', 'тимуриды', 'государство темура', 'timurid', 'timurid empire']},
 {'id': 'hist_time_map_007',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Mamluklar sultonligi',
                     'Saljuqiylar saltanati',
                     'Usmonli (Usmoniyya) imperiyasi',
                     'Ayyubiylar davlati'],
              'ru': ['Мамлюкский султанат',
                     'Государство Сельджукидов',
                     'Османская империя (Порта)',
                     'Государство Айюбидов'],
              'en': ['Mamluk Sultanate', 'Seljuk Empire', 'Ottoman Empire', 'Ayyubid Sultanate']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Usmonli (Usmoniyya) imperiyasi', 'ru': 'Османская империя (Порта)', 'en': 'Ottoman Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/OttomanEmpireIn1683.png/1024px-OttomanEmpireIn1683.png',
  'fun_fact': {'uz': '1683 yilda Usmonli imperiyasi Janubi-sharqiy Yevropa, Yaqin Sharq va Shimoliy Afrikani egallab, '
                     'Vena darvozalarigacha yetib borgan.',
               'ru': 'В зените могущества в 1683 году Османская империя владела землями на трех континентах: в Европе, '
                     'Азии и Африке.',
               'en': 'At its territorial peak in 1683, the Ottoman Empire spanned Southeastern Europe, Western Asia, '
                     'and North Africa.'},
  'aliases': ['usmonlilar', 'usmonli imperiyasi', 'османская империя', 'ottoman', 'ottoman empire']},
 {'id': 'hist_time_map_008',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Abbosiylar xalifaligi', 'Fotimiylar xalifaligi', 'Murobitlar davlati', 'Umaviylar xalifaligi'],
              'ru': ['Аббасидский халифат', 'Фатимидский халифат', 'Государство Альморавидов', 'Омейядский халифат'],
              'en': ['Abbasid Caliphate', 'Fatimid Caliphate', 'Almoravid Empire', 'Umayyad Caliphate']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Umaviylar xalifaligi', 'ru': 'Омейядский халифат', 'en': 'Umayyad Caliphate'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Umayyad_Caliphate_750_AD.png/1024px-Umayyad_Caliphate_750_AD.png',
  'fun_fact': {'uz': "Poytaxti Damashq bo'lgan Umaviylar xalifaligi Ispaniyadan (Andalusiya) to Hind daryosi va "
                     'Movarounnahrgacha 11 million kv km hududni birlashtirgan.',
               'ru': 'Омейядский халифат со столицей в Дамаске простирался от Атлантического океана до границ Китая и '
                     'Индии.',
               'en': 'Ruled from Damascus, the Umayyad Caliphate covered over 11 million sq km, from Portugal to the '
                     'borders of China.'},
  'aliases': ['umaviylar', 'umaviylar xalifaligi', 'омейяды', 'омейядский халифат', 'umayyad', 'umayyad caliphate']},
 {'id': 'hist_time_map_009',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["Abbosiylar xalifaligi (Bag'dod)",
                     'Umaviylar xalifaligi',
                     'Fotimiylar xalifaligi',
                     'Ayyubiylar davlati'],
              'ru': ['Аббасидский халифат (Багдад)', 'Омейядский халифат', 'Фатимидский халифат', 'Держава Айюбидов'],
              'en': ['Abbasid Caliphate (Baghdad)', 'Umayyad Caliphate', 'Fatimid Caliphate', 'Ayyubid Sultanate']},
  'correct_index': 0,
  'correct_answer': {'uz': "Abbosiylar xalifaligi (Bag'dod)",
                     'ru': 'Аббасидский халифат (Багдад)',
                     'en': 'Abbasid Caliphate (Baghdad)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Abbasid_Caliphate_at_its_greatest_extent.png/1024px-Abbasid_Caliphate_at_its_greatest_extent.png',
  'fun_fact': {'uz': "Abbosiylar davrida Bag'dodda 'Bayt ul-Hikma' (Donishmandlar uyi) tashkil etilib, Islom oltin "
                     'asrining ilmiy markaziga aylandi.',
               'ru': 'Эпоха Аббасидов со столицей в Багдаде стала золотым веком исламской науки, философии и культуры.',
               'en': 'The Abbasid Caliphate presided over the Islamic Golden Age from Baghdad, patronizing the House '
                     'of Wisdom.'},
  'aliases': ['abbosiylar',
              'abbosiylar xalifaligi',
              'аббасиды',
              'аббасидский халифат',
              'abbasid',
              'abbasid caliphate']},
 {'id': 'hist_time_map_010',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Tohiriylar davlati',
                     'Somoniylar davlati (Buxoro)',
                     'Safforiylar davlati',
                     "G'aznaviylar davlati"],
              'ru': ['Государство Тахиридов',
                     'Государство Саманидов (Бухара)',
                     'Государство Саффаридов',
                     'Государство Газневидов'],
              'en': ['Tahirid Dynasty', 'Samanid Empire (Bukhara)', 'Saffarid Dynasty', 'Ghaznavid Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Somoniylar davlati (Buxoro)',
                     'ru': 'Государство Саманидов (Бухара)',
                     'en': 'Samanid Empire (Bukhara)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Samanid_Dynasty_943_AD.png/1024px-Samanid_Dynasty_943_AD.png',
  'fun_fact': {'uz': 'Ismoil Somoniy asos solgan bu davlat Movarounnahr va Xurosonni birlashtirib, poytaxt Buxoroni '
                     'Sharqning ilm-fan beshigiga aylantirgan.',
               'ru': 'Государство Саманидов со столицей в Бухаре объединяло Мавераннахр и Хорасан, возродив '
                     'персо-таджикскую и тюркскую культуру.',
               'en': 'Under Ismail Samani, the Samanid Empire united Transoxiana and Khorasan, turning Bukhara into an '
                     'illustrious capital.'},
  'aliases': ['somoniylar', 'somoniylar davlati', 'саманиды', 'государство саманидов', 'samanid', 'samanid empire']},
 {'id': 'hist_time_map_011',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Qoraxoniylar davlati',
                     'Saljuqiylar saltanati',
                     'Xorazmshohlar davlati (Anushteginiylar)',
                     "G'uriylar davlati"],
              'ru': ['Караханидское государство',
                     'Сельджукская империя',
                     'Государство Хорезмшахов (Ануштегиниды)',
                     'Государство Гуридов'],
              'en': ['Kara-Khanid Khanate', 'Seljuk Empire', 'Khwarazmian Empire', 'Ghurid Sultanate']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Xorazmshohlar davlati (Anushteginiylar)',
                     'ru': 'Государство Хорезмшахов (Ануштегиниды)',
                     'en': 'Khwarazmian Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Khwarazmian_Empire_1218.png/1024px-Khwarazmian_Empire_1218.png',
  'fun_fact': {'uz': "1218 yilda Aloviddin Muhammad davrida Xorazmshohlar saltanati Orol bo'ylaridan to Fors "
                     "ko'rfazigacha 5 million kv km hududni egallagan.",
               'ru': 'Перед монгольским вторжением в 1219 году держава Хорезмшахов простиралась от Урала до '
                     'Персидского залива.',
               'en': 'By 1218, the Khwarazmian Empire controlled Transoxiana, Iran, and Khorasan, right before the '
                     'Mongol conquest.'},
  'aliases': ['xorazmshohlar',
              'xorazmshohlar davlati',
              'хорезмшахи',
              'государство хорезмшахов',
              'khwarazmian',
              'khwarazm']},
 {'id': 'hist_time_map_012',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Somoniylar davlati',
                     'Dehli sultonligi',
                     "G'uriylar davlati",
                     "G'aznaviylar davlati (Mahmud G'aznaviy)"],
              'ru': ['Государство Саманидов',
                     'Делийский султанат',
                     'Государство Гуридов',
                     'Государство Газневидов (Махмуд Газневи)'],
              'en': ['Samanid Empire', 'Delhi Sultanate', 'Ghurid Sultanate', 'Ghaznavid Empire']},
  'correct_index': 3,
  'correct_answer': {'uz': "G'aznaviylar davlati (Mahmud G'aznaviy)",
                     'ru': 'Государство Газневидов (Махмуд Газневи)',
                     'en': 'Ghaznavid Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Ghaznavid_Empire_at_its_greatest_extent.png/1024px-Ghaznavid_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': "Sulton Mahmud G'aznaviy Hindistonga 17 marta zafarli yurish qilgan va poytaxt G'aznani saroylar "
                     'va olimlar maskaniga aylantirgan (Beruniy shu saroyda ishlagan).',
               'ru': 'Махмуд Газневи первым принял титул султана и распространил власть от Амударьи до северной Индии.',
               'en': 'Mahmud of Ghazni was the first ruler titled Sultan; his empire spanned modern Afghanistan, Iran, '
                     'Pakistan, and Northwest India.'},
  'aliases': ['gaznaviylar', 'mahmud gaznaviy', 'газневиды', 'махмуд газневи', 'ghaznavid', 'ghaznavids']},
 {'id': 'hist_time_map_013',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Buyuk Saljuqiylar saltanati', 'Rum saljuqiylari', 'Usmonli davlati', 'Xorazmshohlar davlati'],
              'ru': ['Великая Сельджукская империя',
                     'Конийский султанат',
                     'Османское государство',
                     'Государство Хорезмшахов'],
              'en': ['Great Seljuk Empire', 'Sultanate of Rum', 'Ottoman State', 'Khwarazmian Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Buyuk Saljuqiylar saltanati',
                     'ru': 'Великая Сельджукская империя',
                     'en': 'Great Seljuk Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Seljuk_Empire_at_its_greatest_extent.png/1024px-Seljuk_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': "Alp Arslon va Malikshoh davrida Saljuqiylar O'rta Osiyodan O'rta yer dengizigacha bo'lgan "
                     "hududni boshqargan, vazir Nizomulmulk esa mashhur 'Siyosatnoma'ni yozgan.",
               'ru': 'Сельджуки разгромили византийцев при Манцикерте в 1071 году и открыли Анатолию для расселения '
                     'тюркских народов.',
               'en': 'Under Alp Arslan and Malik-Shah I, the Seljuks ruled from the Hindu Kush to Anatolia after the '
                     'decisive Battle of Manzikert.'},
  'aliases': ['saljuqiylar', 'buyuk saljuqiylar', 'сельджуки', 'сельджукская империя', 'seljuk', 'seljuk empire']},
 {'id': 'hist_time_map_014',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Dehli sultonligi',
                     "Boburiylar (Buyuk Mo'g'ullar) imperiyasi (Hindiston)",
                     'Marathalar imperiyasi',
                     'Vijayanagara imperiyasi'],
              'ru': ['Делийский султанат',
                     'Империя Великих Моголов (Бабуриды в Индии)',
                     'Империя Маратха',
                     'Империя Виджаянагара'],
              'en': ['Delhi Sultanate', 'Mughal Empire (Baburid India)', 'Maratha Empire', 'Vijayanagara Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': "Boburiylar (Buyuk Mo'g'ullar) imperiyasi (Hindiston)",
                     'ru': 'Империя Великих Моголов (Бабуриды в Индии)',
                     'en': 'Mughal Empire (Baburid India)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Mughal_Empire_1700.png/1024px-Mughal_Empire_1700.png',
  'fun_fact': {'uz': 'Bobur asos solgan va Avrangzeb davrida deyarli butun Hindiston yarimorolini birlashtirgan bu '
                     'saltanat jahon yalpi mahsulotining chorak qismini ishlab chiqargan.',
               'ru': 'Бабуриды объединили почти весь Индостан, создав одну из богатейших империй и построив чудо света '
                     'Тадж-Махал.',
               'en': 'Founded by Babur in 1526, the Mughal Empire ruled almost the entire Indian subcontinent by 1700, '
                     'producing 25% of global GDP.'},
  'aliases': ['boburiylar', 'buyuk mogullar', 'бабуриды', 'великие моголы', 'mughal', 'mughal empire']},
 {'id': 'hist_time_map_015',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["Chig'atoy ulusi", 'Qozon xonligi', "Oltin O'rda (Jo'ji ulusi)", 'Qrim xonligi'],
              'ru': ['Чагатайский улус', 'Казанское ханство', 'Золотая Орда (Улус Джучи)', 'Крымское ханство'],
              'en': ['Chagatai Khanate', 'Khanate of Kazan', 'Golden Horde (Jochid Ulus)', 'Crimean Khanate']},
  'correct_index': 2,
  'correct_answer': {'uz': "Oltin O'rda (Jo'ji ulusi)",
                     'ru': 'Золотая Орда (Улус Джучи)',
                     'en': 'Golden Horde (Jochid Ulus)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Golden_Horde_1389.png/1024px-Golden_Horde_1389.png',
  'fun_fact': {'uz': "Botuxon asos solgan Oltin O'rda poytaxti Saroy-Botu bo'lib, Irtish daryosidan to Dunay "
                     "daryosigacha cho'zilgan.",
               'ru': 'Золотая Орда со столицей в Сарай-Бату на Волге контролировала бескрайние степи Евразии и русские '
                     'княжества.',
               'en': 'Founded by Batu Khan, the Golden Horde dominated the Eurasian steppes from the Danube to Siberia '
                     'from its capital Sarai.'},
  'aliases': ['oltin orda', 'joji ulusi', 'золотая орда', 'улус джучи', 'golden horde']},
 {'id': 'hist_time_map_016',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Qin sulolasi', 'Tan sulolasi', 'Min sulolasi', 'Xan sulolasi (Xitoy)'],
              'ru': ['Династия Цинь', 'Династия Тан', 'Династия Мин', 'Империя Хань (Китай)'],
              'en': ['Qin Dynasty', 'Tang Dynasty', 'Ming Dynasty', 'Han Dynasty (China)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Xan sulolasi (Xitoy)', 'ru': 'Империя Хань (Китай)', 'en': 'Han Dynasty (China)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Han_dynasty_2_AD.png/1024px-Han_dynasty_2_AD.png',
  'fun_fact': {'uz': "Xan sulolasi 400 yildan ortiq hukmronlik qilib, Buyuk Ipak yo'liga asos solgan va bugungi kunda "
                     "ham xitoyliklar o'zlarini 'xan' xalqi deb atashadi.",
               'ru': 'Эпоха Хань заложила основы китайской цивилизации, открыла Шелковый путь и дала имя титульному '
                     'народу Китая.',
               'en': "The Han Dynasty (202 BC - 220 AD) opened the Silk Road and gave its name to China's dominant "
                     'ethnic group, the Han.'},
  'aliases': ['xan sulolasi', 'xitoy xan', 'династия хань', 'империя хань', 'han dynasty']},
 {'id': 'hist_time_map_017',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Tan sulolasi (Xitoyning Oltin davri)', 'Sun sulolasi', 'Yuan sulolasi', 'Min sulolasi'],
              'ru': ['Империя Тан (Золотой век Китая)', 'Империя Сун', 'Империя Юань', 'Империя Мин'],
              'en': ['Tang Dynasty (Golden Age of China)', 'Song Dynasty', 'Yuan Dynasty', 'Ming Dynasty']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Tan sulolasi (Xitoyning Oltin davri)',
                     'ru': 'Империя Тан (Золотой век Китая)',
                     'en': 'Tang Dynasty (Golden Age of China)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Tang_Dynasty_circa_700_CE.png/1024px-Tang_Dynasty_circa_700_CE.png',
  'fun_fact': {'uz': "Poytaxti Chanan (zamonaviy Sian) bo'lgan Tan imperiyasi 1 milliondan ortiq aholiga ega dunyoning "
                     'eng yirik kosmopolit shahriga aylangan.',
               'ru': 'Династия Тан (618–907) считается золотым веком китайской поэзии, живописи и торговли по '
                     'Шелковому пути.',
               'en': "The Tang Dynasty ruled cosmopolitan Chang'an, then the world's largest city, and fostered a "
                     'golden age of Chinese culture.'},
  'aliases': ['tan sulolasi', 'xitoy tan', 'династия тан', 'империя тан', 'tang dynasty']},
 {'id': 'hist_time_map_018',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Xan sulolasi', 'Sun sulolasi (Xitoy)', 'Sin sulolasi', 'Szin sulolasi'],
              'ru': ['Империя Хань', 'Империя Сун (Китай)', 'Империя Цин', 'Империя Цзинь'],
              'en': ['Han Dynasty', 'Song Dynasty (China)', 'Qing Dynasty', 'Jin Dynasty']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Sun sulolasi (Xitoy)', 'ru': 'Империя Сун (Китай)', 'en': 'Song Dynasty (China)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Northern_Song_Dynasty_1111.png/1024px-Northern_Song_Dynasty_1111.png',
  'fun_fact': {'uz': "Sun sulolasi davrida dunyoda ilk bor qog'oz pullar (szyaoszi) muomalaga chiqarilgan, porox va "
                     "magnit kompas keng qo'llanilgan.",
               'ru': 'При династии Сун впервые в мире появились бумажные деньги, распространился порох и компас.',
               'en': 'The Song Dynasty pioneered paper banknotes, permanent standing navies, and the practical use of '
                     'gunpowder and compasses.'},
  'aliases': ['sun sulolasi', 'династия сун', 'империя сун', 'song dynasty']},
 {'id': 'hist_time_map_019',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Yuan sulolasi', 'Sin sulolasi', 'Min sulolasi (Xitoy)', 'Tan sulolasi'],
              'ru': ['Империя Юань', 'Империя Цин', 'Империя Мин (Китай)', 'Империя Тан'],
              'en': ['Yuan Dynasty', 'Qing Dynasty', 'Ming Dynasty (China)', 'Tang Dynasty']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Min sulolasi (Xitoy)', 'ru': 'Империя Мин (Китай)', 'en': 'Ming Dynasty (China)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Ming_Dynasty_circa_1415.png/1024px-Ming_Dynasty_circa_1415.png',
  'fun_fact': {'uz': "Min sulolasi davrida Pekinga poytaxt ko'chirilib, 'Taqiqlangan shahar' saroyi bunyod etildi va "
                     'Buyuk Xitoy devori toshdan mustahkamlandi.',
               'ru': 'Императоры Мин построили Запретный город в Пекине и возвели современный каменный облик Великой '
                     'стены.',
               'en': "The Ming Dynasty constructed Beijing's Forbidden City and rebuilt the Great Wall into the "
                     'stone-faced ramparts seen today.'},
  'aliases': ['min sulolasi', 'династия мин', 'империя мин', 'ming dynasty']},
 {'id': 'hist_time_map_020',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Min sulolasi', 'Yapon imperiyasi', 'Mongol imperiyasi', 'Sin (Manchjur) imperiyasi'],
              'ru': ['Империя Мин', 'Японская империя', 'Монгольская империя', 'Империя Цин (Маньчжурская династия)'],
              'en': ['Ming Dynasty', 'Empire of Japan', 'Mongol Empire', 'Qing Empire (Manchu Dynasty)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Sin (Manchjur) imperiyasi',
                     'ru': 'Империя Цин (Маньчжурская династия)',
                     'en': 'Qing Empire (Manchu Dynasty)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Qing_Empire_circa_1820.png/1024px-Qing_Empire_circa_1820.png',
  'fun_fact': {'uz': "Sin sulolasi Xitoyning so'nggi imperatorlik sulolasi bo'lib (1644-1912), Xitoy, Tibet, Shinjon "
                     "va Mo'g'ulistonni o'z ichiga olgan 13 million kv km ga yetgan.",
               'ru': 'Цин была последней императорской династией Китая, объединившей Маньчжурию, Монголию, Синьцзян и '
                     'Тибет.',
               'en': "The Manchu Qing Dynasty was China's final imperial dynasty, expanding China to its maximum "
                     'extent of over 13 million sq km.'},
  'aliases': ['sin sulolasi', 'manchjur', 'династия цин', 'империя цин', 'qing dynasty', 'qing empire']},
 {'id': 'hist_time_map_021',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["Britaniya imperiyasi ('Quyosh botmaydigan saltanat')",
                     'Ispaniya imperiyasi',
                     'Fransiya mustamlakachilik imperiyasi',
                     'Portugaliya imperiyasi'],
              'ru': ['Британская империя («Империя, над которой никогда не заходит солнце»)',
                     'Испанская империя',
                     'Французская колониальная империя',
                     'Португальская империя'],
              'en': ["British Empire ('The empire on which the sun never sets')",
                     'Spanish Empire',
                     'French Colonial Empire',
                     'Portuguese Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': "Britaniya imperiyasi ('Quyosh botmaydigan saltanat')",
                     'ru': 'Британская империя («Империя, над которой никогда не заходит солнце»)',
                     'en': "British Empire ('The empire on which the sun never sets')"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/The_British_Empire_Anachronous.png/1024px-The_British_Empire_Anachronous.png',
  'fun_fact': {'uz': "Britaniya imperiyasi insoniyat tarixidagi eng yirik imperiya bo'lib, Yer quruqligining 25 "
                     'foizini (35 million kv km) va 400 milliondan ortiq aholini qamrab olgan.',
               'ru': 'Британская империя занимала четверть суши Земли и правила четвертью населения планеты в 1920-х '
                     'годах.',
               'en': 'Covering over 35 million square kilometers at its 1920 peak, the British Empire was the largest '
                     'empire in world history.'},
  'aliases': ['britaniya imperiyasi', 'ingliz imperiyasi', 'британская империя', 'british empire']},
 {'id': 'hist_time_map_022',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Portugaliya imperiyasi', 'Ispaniya imperiyasi', 'Britaniya imperiyasi', 'Gollandiya imperiyasi'],
              'ru': ['Португальская империя',
                     'Испанская колониальная империя',
                     'Британская империя',
                     'Голландская колониальная империя'],
              'en': ['Portuguese Empire', 'Spanish Empire', 'British Empire', 'Dutch Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Ispaniya imperiyasi', 'ru': 'Испанская колониальная империя', 'en': 'Spanish Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Imperio_espa%C3%B1ol_en_su_c%C3%BAspide.png/1024px-Imperio_espa%C3%B1ol_en_su_c%C3%BAspide.png',
  'fun_fact': {'uz': 'XVI-XVIII asrlarda Ispaniya imperiyasi Shimoliy va Janubiy Amerikaning katta qismini, Filippinni '
                     "va Yevropadagi ko'plab hududlarni birlashtirgan ilk global saltanat bo'lgan.",
               'ru': 'Испанская империя владела почти всей Южной и Центральной Америкой, Мексикой, Филиппинами и '
                     'частями Европы.',
               'en': 'The Spanish Empire was among the first global empires, spanning from the Americas to the '
                     'Philippines across two centuries.'},
  'aliases': ['ispan imperiyasi', 'isponiya imperiyasi', 'испанская империя', 'spanish empire']},
 {'id': 'hist_time_map_023',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Sovet Ittifoqi (SSSR)',
                     'Rossiya podsholigi',
                     "Rossiya imperiyasi (1866 yil cho'qqisi)",
                     'Avstriya-Vengriya imperiyasi'],
              'ru': ['СССР',
                     'Русское царство',
                     'Российская империя (территориальный пик 1866 года)',
                     'Австро-Венгерская империя'],
              'en': ['Soviet Union',
                     'Tsardom of Russia',
                     'Russian Empire (at its peak in 1866)',
                     'Austro-Hungarian Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': "Rossiya imperiyasi (1866 yil cho'qqisi)",
                     'ru': 'Российская империя (территориальный пик 1866 года)',
                     'en': 'Russian Empire (at its peak in 1866)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Russian_Empire_1866.png/1024px-Russian_Empire_1866.png',
  'fun_fact': {'uz': "1866 yilda Alyaskani AQShga sotishdan oldin Rossiya imperiyasi uch qit'ani (Yevropa, Osiyo va "
                     'Shimoliy Amerika) qamrab olib, 23,7 million kv km maydonga ega edi.',
               'ru': 'До продажи Аляски в 1867 году Российская империя была единственным государством, владевшим '
                     'землями сразу в Европе, Азии и Америке.',
               'en': 'Before selling Alaska to the US in 1867, the Russian Empire spanned across three continents: '
                     'Europe, Asia, and North America.'},
  'aliases': ['rossiya imperiyasi', 'российская империя', 'russian empire']},
 {'id': 'hist_time_map_024',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Britaniya imperiyasi',
                     'Ispaniya imperiyasi',
                     'Belgiya mustamlakalari',
                     'Fransiya mustamlakachilik imperiyasi'],
              'ru': ['Британская империя',
                     'Испанская империя',
                     'Бельгийские колонии',
                     'Французская колониальная империя'],
              'en': ['British Empire', 'Spanish Empire', 'Belgian Colonial Empire', 'French Colonial Empire']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Fransiya mustamlakachilik imperiyasi',
                     'ru': 'Французская колониальная империя',
                     'en': 'French Colonial Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/French_Empire_evolution.gif/1024px-French_Empire_evolution.gif',
  'fun_fact': {'uz': "Fransiya G'arbiy va Markaziy Afrika, Hindixitoy (Vyetnam, Laos, Kambodja) va Karib orollarini "
                     'egallab, dunyodagi ikkinchi yirik mustamlaka imperiyasiga aylangan.',
               'ru': 'Французская колониальная империя охватывала огромные территории в Западной Африке, Индокитае и '
                     'на островах океанов.',
               'en': "At its height between the World Wars, France controlled roughly 10% of the world's land area, "
                     'centered in West Africa and Indochina.'},
  'aliases': ['fransuz imperiyasi', 'fransiya mustamlakalari', 'французская империя', 'french colonial empire']},
 {'id': 'hist_time_map_025',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Avstriya-Vengriya imperiyasi (Gabsburglar)',
                     'Prussiya qirolligi',
                     'Germaniya imperiyasi',
                     'Muqaddas Rim imperiyasi'],
              'ru': ['Австро-Венгерская империя (монархия Габсбургов)',
                     'Королевство Пруссия',
                     'Германская империя',
                     'Священная Римская империя'],
              'en': ['Austro-Hungarian Empire (Habsburg Monarchy)',
                     'Kingdom of Prussia',
                     'German Empire',
                     'Holy Roman Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Avstriya-Vengriya imperiyasi (Gabsburglar)',
                     'ru': 'Австро-Венгерская империя (монархия Габсбургов)',
                     'en': 'Austro-Hungarian Empire (Habsburg Monarchy)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Austria-Hungary_1914.png/1024px-Austria-Hungary_1914.png',
  'fun_fact': {'uz': "Avstriya-Vengriya ikki markazli monarxiya bo'lib, uning tarkibida 10 dan ortiq millat (nemislar, "
                     'vengerlar, chexlar, polyaklar, ukrainlar, xorvatlar) yashagan.',
               'ru': 'Австро-Венгрия была многонациональной дуалистической монархией в центре Европы, распавшейся в '
                     'результате Первой мировой войны.',
               'en': 'The Austro-Hungarian dual monarchy ruled Central Europe until dissolving at the end of World War '
                     'I in 1918.'},
  'aliases': ['avstriya vengriya', 'avstriya-vengriya', 'австро-венгрия', 'austria-hungary']},
 {'id': 'hist_time_map_026',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Qadimgi Rim imperiyasi',
                     'Muqaddas Rim imperiyasi (Nemis millatining)',
                     'Franklar imperiyasi',
                     'Prussiya qirolligi'],
              'ru': ['Древняя Римская империя',
                     'Священная Римская империя (германской нации)',
                     'Франкская империя',
                     'Королевство Пруссия'],
              'en': ['Ancient Roman Empire', 'Holy Roman Empire', 'Frankish Empire', 'Kingdom of Prussia']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Muqaddas Rim imperiyasi (Nemis millatining)',
                     'ru': 'Священная Римская империя (германской нации)',
                     'en': 'Holy Roman Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Holy_Roman_Empire_circa_1000.png/1024px-Holy_Roman_Empire_circa_1000.png',
  'fun_fact': {'uz': "Otton I tomonidan 962 yilda tuzilgan bu davlat haqida Volter mashhur gapi bilan aytgan: 'U na "
                     "muqaddas, na rimlik va na imperiya edi'.",
               'ru': 'Священная Римская империя просуществовала с 962 по 1806 год, объединяя сотни германских княжеств '
                     'и епископств.',
               'en': 'Founded by Otto I in 962 and abolished by Napoleon in 1806, it was famously neither holy, nor '
                     'Roman, nor an empire.'},
  'aliases': ['muqaddas rim imperiyasi', 'священная римская империя', 'holy roman empire']},
 {'id': 'hist_time_map_027',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Guptalar imperiyasi',
                     'Kushonlar saltanati',
                     'Maurya imperiyasi (Chandragupta va Ashoka)',
                     'Harsha davlati'],
              'ru': ['Империя Гупта',
                     'Кушанское царство',
                     'Империя Маурьев (Чандрагупта и Ашока)',
                     'Государство Харши'],
              'en': ['Gupta Empire', 'Kushan Empire', 'Maurya Empire (Chandragupta and Ashoka)', 'Empire of Harsha']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Maurya imperiyasi (Chandragupta va Ashoka)',
                     'ru': 'Империя Маурьев (Чандрагупта и Ашока)',
                     'en': 'Maurya Empire (Chandragupta and Ashoka)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Maurya_Empire_circa_250_BCE.png/1024px-Maurya_Empire_circa_250_BCE.png',
  'fun_fact': {'uz': "Maurya imperiyasi Hindiston yarimorolini deyarli to'liq birlashtirgan ilk qudratli davlat "
                     "bo'lib, uning poytaxti Pataliputra shahri edi.",
               'ru': 'Империя Маурьев охватила почти весь Индостан в III веке до н.э., распространив буддизм по всей '
                     'Азии.',
               'en': "The Maurya Empire (322-185 BC) was ancient India's largest empire, famously ruled by Buddhist "
                     'convert Emperor Ashoka.'},
  'aliases': ['maurya', 'ashoka davlati', 'маурья', 'империя маурьев', 'maurya empire']},
 {'id': 'hist_time_map_028',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Maurya imperiyasi',
                     'Kushon imperiyasi',
                     'Chola imperiyasi',
                     'Guptalar imperiyasi (Hindistonning Oltin davri)'],
              'ru': ['Империя Маурьев',
                     'Кушанская империя',
                     'Империя Чола',
                     'Империя Гупта (Золотой век древней Индии)'],
              'en': ['Maurya Empire', 'Kushan Empire', 'Chola Empire', 'Gupta Empire (Classical Golden Age of India)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Guptalar imperiyasi (Hindistonning Oltin davri)',
                     'ru': 'Империя Гупта (Золотой век древней Индии)',
                     'en': 'Gupta Empire (Classical Golden Age of India)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Gupta_Empire_circa_400_CE.png/1024px-Gupta_Empire_circa_400_CE.png',
  'fun_fact': {'uz': "Guptalar davrida hind matematigi Aryabxata 'nol' (0) raqamini va pi sonini hisoblagan, mashhur "
                     "'Kamasutra' va Kalidasa asarlari yaratilgan.",
               'ru': 'Эпоха Гуптов (IV–VI вв.) подарила миру индийские цифры, изобретение математического нуля и '
                     'расцвет санскритской литературы.',
               'en': 'The Gupta era (320-550 AD) saw immense scientific breakthroughs including the mathematical '
                     'invention of zero and the decimal system.'},
  'aliases': ['gupta', 'guptalar imperiyasi', 'гупта', 'империя гупта', 'gupta empire']},
 {'id': 'hist_time_map_029',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Inklar imperiyasi (Tavantinsuyu)', 'Atsteklar imperiyasi', 'Mayya davlati', 'Chimu madaniyati'],
              'ru': ['Империя инков (Тауантинсуйу)', 'Империя ацтеков', 'Цивилизация майя', 'Государство Чиму'],
              'en': ['Inca Empire (Tawantinsuyu)', 'Aztec Empire', 'Maya Civilization', 'Chimu Culture']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Inklar imperiyasi (Tavantinsuyu)',
                     'ru': 'Империя инков (Тауантинсуйу)',
                     'en': 'Inca Empire (Tawantinsuyu)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Inca_Empire_map.png/1024px-Inca_Empire_map.png',
  'fun_fact': {'uz': "Inklar And tog'lari bo'ylab 40 000 km dan ortiq mukammal tosh yo'llar qurgan va g'ildirak hamda "
                     'yozuvsiz ulkan imperiyani boshqargan (kipu tugunli ip yozuvidan foydalanishgan).',
               'ru': 'Империя инков протянулась на 4000 км вдоль хребтов Анд, создав шедевры горной архитектуры вроде '
                     'Мачу-Пикчу.',
               'en': "The Inca Empire connected South America's Andes across 40,000 km of roads, managing trade "
                     'without wheels using quipu knots.'},
  'aliases': ['inklar', 'inklar imperiyasi', 'tavantinsuyu', 'инки', 'империя инков', 'inca', 'inca empire']},
 {'id': 'hist_time_map_030',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Mayya sivilizatsiyasi',
                     'Atsteklar imperiyasi (Uchlik ittifoqi)',
                     'Inklar imperiyasi',
                     'Zapoteklar davlati'],
              'ru': ['Города-государства майя',
                     'Империя ацтеков (Тройственный союз)',
                     'Империя инков',
                     'Государство сапотеков'],
              'en': ['Maya Civilization', 'Aztec Empire (Triple Alliance)', 'Inca Empire', 'Zapotec Civilization']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Atsteklar imperiyasi (Uchlik ittifoqi)',
                     'ru': 'Империя ацтеков (Тройственный союз)',
                     'en': 'Aztec Empire (Triple Alliance)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Aztec_Empire_1519.png/1024px-Aztec_Empire_1519.png',
  'fun_fact': {'uz': "Atsteklar poytaxti Tenochtitlan Texkoko ko'li o'rtasidagi orolda barpo etilgan bo'lib, uning "
                     "o'rnida hozirgi Mexiko shahri joylashgan.",
               'ru': 'Столица ацтеков Теночтитлан с населением более 200 000 человек была построена на сваях посреди '
                     'озера Тескоко.',
               'en': "The Aztec capital Tenochtitlan sat on an island in Lake Texcoco and was one of the world's "
                     'largest cities in 1519.'},
  'aliases': ['atsteklar', 'atstek imperiyasi', 'ацтеки', 'империя ацтеков', 'aztec', 'aztec empire']},
 {'id': 'hist_time_map_031',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Songay imperiyasi', 'Gana imperiyasi', 'Mali imperiyasi (Mansa Muso)', 'Kanem-Bornu davlati'],
              'ru': ['Империя Сонгай', 'Империя Гана', 'Империя Мали (Манса Муса)', 'Империя Канем-Борну'],
              'en': ['Songhai Empire', 'Ghana Empire', 'Mali Empire (Mansa Musa)', 'Kanem-Bornu Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Mali imperiyasi (Mansa Muso)',
                     'ru': 'Империя Мали (Манса Муса)',
                     'en': 'Mali Empire (Mansa Musa)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Mali_Empire_1350.png/1024px-Mali_Empire_1350.png',
  'fun_fact': {'uz': 'Mali hukmdori Mansa Muso tarixdagi eng boy inson hisoblanadi; uning Makkaga haj safari paytida '
                     "Qohirada shunchalik ko'p oltin tarqatganki, oltin narxi 12 yilga arzonlab ketgan.",
               'ru': 'Император Манса Муса владел колоссальными золотыми рудниками Сахары и считался богатейшим '
                     'правителем в истории.',
               'en': 'The Mali Empire controlled West African gold routes; ruler Mansa Musa distributed so much gold '
                     "on pilgrimage that Cairo's market deflated."},
  'aliases': ['mali', 'mali imperiyasi', 'mansa muso', 'мали', 'империя мали', 'mali empire']},
 {'id': 'hist_time_map_032',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Mali imperiyasi', 'Benin qirolligi', 'Ashanti davlati', "Songay imperiyasi (G'arbiy Afrika)"],
              'ru': ['Империя Мали', 'Королевство Бенин', 'Империя Ашанти', 'Империя Сонгай (Западная Африка)'],
              'en': ['Mali Empire', 'Kingdom of Benin', 'Ashanti Empire', 'Songhai Empire (West Africa)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Songay imperiyasi (G'arbiy Afrika)",
                     'ru': 'Империя Сонгай (Западная Африка)',
                     'en': 'Songhai Empire (West Africa)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Songhai_Empire_1500.png/1024px-Songhai_Empire_1500.png',
  'fun_fact': {'uz': "Songay poytaxti Gao va ilmiy markazi Timbuktu bo'lib, Sankore universitetida minglab talabalar "
                     "matematika, astronomiya va huquqni o'rgangan.",
               'ru': 'Сонгай был крупнейшим государством в истории Западной Африки со знаменитым научным центром в '
                     'Тимбукту.',
               'en': 'At its zenith around 1500, Songhai dominated the Sahel and housed the famed Sankore University '
                     'in Timbuktu.'},
  'aliases': ['songay', 'songay imperiyasi', 'сонгай', 'империя сонгай', 'songhai', 'songhai empire']},
 {'id': 'hist_time_map_033',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Karfagen dengiz davlati (Gannibal)',
                     'Rim respublikasi',
                     'Numidiya podsholigi',
                     'Finikiya davlatlari'],
              'ru': ['Карфагенская морская держава (Ганнибал)',
                     'Римская республика',
                     'Царство Нумидия',
                     'Финикийские города-государства'],
              'en': ['Carthaginian Empire (Hannibal)',
                     'Roman Republic',
                     'Kingdom of Numidia',
                     'Phoenician city-states']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Karfagen dengiz davlati (Gannibal)',
                     'ru': 'Карфагенская морская держава (Ганнибал)',
                     'en': 'Carthaginian Empire (Hannibal)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Carthaginian_Empire_264_BC.png/1024px-Carthaginian_Empire_264_BC.png',
  'fun_fact': {'uz': "Karfagen O'rta yer dengizining g'arbiy savdosini nazorat qilgan finikiylar koloniyasi bo'lib, "
                     "uchta mashhur Puni urushida Rim bilan to'qnashgan.",
               'ru': 'Карфаген контролировал морскую торговлю Средиземноморья, пока не был разрушен Римом в 146 году '
                     'до н.э.',
               'en': 'Founded by Phoenicians, Carthage commanded Western Mediterranean maritime commerce before '
                     'falling to Rome in 146 BC.'},
  'aliases': ['karfagen', 'gannibal', 'карфаген', 'carthage', 'carthaginian']},
 {'id': 'hist_time_map_034',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Yangi Misr podsholigi',
                     'Ptolemeylar Misr qirolligi (Kleopatra)',
                     'Salavkiylar davlati',
                     'Mamluklar sultonligi'],
              'ru': ['Новое царство Египта',
                     'Эллинистический Египет Птолемеев (Клеопатра)',
                     'Государство Селевкидов',
                     'Мамлюкский султанат'],
              'en': ['New Kingdom of Egypt',
                     'Ptolemaic Kingdom of Egypt (Cleopatra)',
                     'Seleucid Empire',
                     'Mamluk Sultanate']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Ptolemeylar Misr qirolligi (Kleopatra)',
                     'ru': 'Эллинистический Египет Птолемеев (Клеопатра)',
                     'en': 'Ptolemaic Kingdom of Egypt (Cleopatra)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Ptolemaic_Kingdom_300_BC.png/1024px-Ptolemaic_Kingdom_300_BC.png',
  'fun_fact': {'uz': "Ptolemeylar sulolasi yunon millatiga mansub bo'lib, Iskandariya kutubxonasi va Faros mayog'ini "
                     "qurdirgan; sulolaning so'nggi hukmdori Kleopatra VII edi.",
               'ru': 'Птолемеевский Египет со столицей в Александрии стал центром эллинистической науки, подарив миру '
                     'знаменитую Александрийскую библиотеку.',
               'en': 'Ruled by Greco-Macedonian kings descended from Ptolemy I, the kingdom ended with Cleopatra VII '
                     'in 30 BC.'},
  'aliases': ['ptolemeylar', 'ptolemey misri', 'птолемеи', 'египет птолемеев', 'ptolemaic', 'ptolemaic kingdom']},
 {'id': 'hist_time_map_035',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Parfiya podsholigi',
                     'Ptolemeylar podsholigi',
                     'Salavkiylar ellinistik saltanati',
                     'Pont podsholigi'],
              'ru': ['Парфянское царство',
                     'Царство Птолемеев',
                     'Государство Селевкидов (эллинизм)',
                     'Понтийское царство'],
              'en': ['Parthian Empire', 'Ptolemaic Kingdom', 'Seleucid Empire', 'Kingdom of Pontus']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Salavkiylar ellinistik saltanati',
                     'ru': 'Государство Селевкидов (эллинизм)',
                     'en': 'Seleucid Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Seleucid_Empire_circa_200_BCE.png/1024px-Seleucid_Empire_circa_200_BCE.png',
  'fun_fact': {'uz': 'Aleksandr Makedonskiy sarkardasi Salavk I Nikator asos solgan bu ulkan saltanat Suriyadan to '
                     "O'rta Osiyo va Baqtriyagacha cho'zilgan.",
               'ru': 'Держава Селевкидов была крупнейшим эллинистическим осколком империи Александра Македонского в '
                     'Азии.',
               'en': "Founded by Seleucus I Nicator, the Seleucid Empire formed the vast central core of Alexander's "
                     'divided realm in Asia.'},
  'aliases': ['salavkiylar', 'селевкиды', 'государство селевкидов', 'seleucid', 'seleucid empire']},
 {'id': 'hist_time_map_036',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Sosoniylar saltanati',
                     'Kushon imperiyasi',
                     'Ahamoniylar davlati',
                     'Parfiya (Arshakiylar) podsholigi'],
              'ru': ['Держава Сасанидов',
                     'Кушанская империя',
                     'Государство Ахеменидов',
                     'Парфянское царство (Аршакиды)'],
              'en': ['Sasanian Empire', 'Kushan Empire', 'Achaemenid Empire', 'Parthian Empire (Arsacid)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Parfiya (Arshakiylar) podsholigi',
                     'ru': 'Парфянское царство (Аршакиды)',
                     'en': 'Parthian Empire (Arsacid)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Parthian_Empire_at_its_greatest_extent.png/1024px-Parthian_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': "Parfiyalik chavandozlar o'zlarining 'parfiya o'qi' (ot ustida orqaga qarab kamondan o'q uzish) "
                     "taktikasi bilan mashhur bo'lib, Rim legionlarini Karri jangida tor-mor qilgan.",
               'ru': 'Парфяне нанесли сокрушительное поражение римлянам при Каррах в 53 году до н.э., уничтожив армию '
                     'Красса.',
               'en': "The Parthians mastered horseback archery, crushing Marcus Licinius Crassus's Roman legions at "
                     'Carrhae in 53 BC.'},
  'aliases': ['parfiya', 'arshakiylar', 'парфия', 'парфянское царство', 'parthian', 'parthian empire']},
 {'id': 'hist_time_map_037',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Sosoniylar saltanati (Eronshahr)',
                     'Parfiya podsholigi',
                     'Somoniylar davlati',
                     'Saljuqiylar davlati'],
              'ru': ['Государство Сасанидов (Эраншахр)',
                     'Парфянское царство',
                     'Государство Саманидов',
                     'Сельджукское государство'],
              'en': ['Sasanian Empire (Neo-Persian Empire)', 'Parthian Empire', 'Samanid Empire', 'Seljuk State']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Sosoniylar saltanati (Eronshahr)',
                     'ru': 'Государство Сасанидов (Эраншахр)',
                     'en': 'Sasanian Empire (Neo-Persian Empire)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Sasanian_Empire_620_CE.png/1024px-Sasanian_Empire_620_CE.png',
  'fun_fact': {'uz': "Sosoniylar 400 yildan ortiq Rim va Vizantiya bilan kurashgan qadimgi dunyoning so'nggi buyuk "
                     "fors saltanati bo'lib, zardushtiylik davlat dini bo'lgan.",
               'ru': 'Империя Сасанидов была главным геополитическим соперником Рима и Византии на протяжении четырех '
                     'столетий.',
               'en': 'The Sasanian Empire represented the peak of ancient Persian Zoroastrian civilization before the '
                     'Arab conquest in 651 AD.'},
  'aliases': ['sosoniylar', 'eronshahr', 'сасаниды', 'государство сасанидов', 'sasanian', 'sasanian empire']},
 {'id': 'hist_time_map_038',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Eftaliylar davlati',
                     'Kushon imperiyasi (Kanishka I)',
                     'Greko-Baqtriya podsholigi',
                     "Kang' davlati"],
              'ru': ['Государство эфталитов',
                     'Кушанская империя (царь Канишка)',
                     'Греко-Бактрийское царство',
                     'Государство Кангюй'],
              'en': ['Hephthalite Empire', 'Kushan Empire (King Kanishka)', 'Greco-Bactrian Kingdom', 'Kangju State']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Kushon imperiyasi (Kanishka I)',
                     'ru': 'Кушанская империя (царь Канишка)',
                     'en': 'Kushan Empire (King Kanishka)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Kushan_Empire_map.png/1024px-Kushan_Empire_map.png',
  'fun_fact': {'uz': "Kushonlar O'rta Osiyo (Surxondaryo, Dalvarzintepa), Afg'oniston va Shimoliy Hindistonni "
                     "birlashtirib, Buyuk Ipak yo'lining markaziy nazoratchisiga aylangan.",
               'ru': 'Кушанское царство связало Рим, Персию, Индию и Китай, став проводником буддизма в Центральную '
                     'Азию и Китай.',
               'en': 'The Kushan Empire straddled Central and South Asia, synthesizing Hellenistic, Persian, and '
                     'Indian Buddhist cultures.'},
  'aliases': ['kushon', 'kushonlar imperiyasi', 'кушаны', 'кушанское царство', 'kushan', 'kushan empire']},
 {'id': 'hist_time_map_039',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Kushon imperiyasi', 'Turk xoqonligi', "Eftaliylar saltanati ('Oq xunlar')", 'Xioniylar davlati'],
              'ru': ['Кушанская империя',
                     'Тюркский каганат',
                     'Государство эфталитов («Белые гунны»)',
                     'Государство хионитов'],
              'en': ['Kushan Empire', 'Turkic Khaganate', "Hephthalite Empire ('White Huns')", 'Chionite Kingdom']},
  'correct_index': 2,
  'correct_answer': {'uz': "Eftaliylar saltanati ('Oq xunlar')",
                     'ru': 'Государство эфталитов («Белые гунны»)',
                     'en': "Hephthalite Empire ('White Huns')"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Hephthalite_Empire_500_CE.png/1024px-Hephthalite_Empire_500_CE.png',
  'fun_fact': {'uz': "Eftaliylar V-VI asrlarda O'rta Osiyoda yirik davlat barpo etib, Sosoniylar shohi Perozni jangda "
                     'yengishgan.',
               'ru': 'Эфталиты нанесли сокрушительное поражение персидскому царю Перозу и правили землями от Каспия до '
                     'Индии.',
               'en': 'Known as the White Huns, the Hephthalites ruled Central Asia and India in the 5th and 6th '
                     'centuries, defeating the Sasanians.'},
  'aliases': ['eftaliylar', 'oq xunlar', 'эфталиты', 'белые гунны', 'hephthalite', 'white huns']},
 {'id': 'hist_time_map_040',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["G'arbiy Turk xoqonligi",
                     "Uyg'ur xoqonligi",
                     'Xazar xoqonligi',
                     'Birinchi Turk xoqonligi (Bumin va Istami xoqonlar)'],
              'ru': ['Западно-тюркский каганат',
                     'Уйгурский каганат',
                     'Хазарский каганат',
                     'Первый Тюркский каганат (Бумын и Истеми каганы)'],
              'en': ['Western Turkic Khaganate',
                     'Uyghur Khaganate',
                     'Khazar Khaganate',
                     'First Turkic Khaganate (Bumin and Istami)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Birinchi Turk xoqonligi (Bumin va Istami xoqonlar)',
                     'ru': 'Первый Тюркский каганат (Бумын и Истеми каганы)',
                     'en': 'First Turkic Khaganate (Bumin and Istami)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/First_Turkic_Khaganate_576_AD.png/1024px-First_Turkic_Khaganate_576_AD.png',
  'fun_fact': {'uz': "552 yilda asos solingan Turk xoqonligi Sariq dengizdan Qora dengizgacha cho'zilgan bo'lib, "
                     "'turk' etnonimi ilk bor xalqaro davlat nomi sifatida ishlatilgan.",
               'ru': 'Тюркский каганат объединил бескрайние степи Евразии от Маньчжурии до Крыма, утвердив имя тюрков '
                     'на мировой арене.',
               'en': 'Founded in 552 AD, the Göktürk Khaganate stretched from Manchuria to the Black Sea, establishing '
                     'the historic Turkic identity.'},
  'aliases': ['turk xoqonligi', 'birinchi turk xoqonligi', 'тюркский каганат', 'gokturk', 'turkic khaganate']},
 {'id': 'hist_time_map_041',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["G'arbiy Turk xoqonligi (O'n o'q bodun)",
                     'Sharqiy Turk xoqonligi',
                     "Uyg'ur xoqonligi",
                     'Qarluqlar xoqonligi'],
              'ru': ['Западно-тюркский каганат («Десять стрел»)',
                     'Восточно-тюркский каганат',
                     'Уйгурский каганат',
                     'Карлукский каганат'],
              'en': ['Western Turkic Khaganate (Ten Arrows)',
                     'Eastern Turkic Khaganate',
                     'Uyghur Khaganate',
                     'Karluk Yabghu']},
  'correct_index': 0,
  'correct_answer': {'uz': "G'arbiy Turk xoqonligi (O'n o'q bodun)",
                     'ru': 'Западно-тюркский каганат («Десять стрел»)',
                     'en': 'Western Turkic Khaganate (Ten Arrows)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Western_Turkic_Khaganate_circa_600_CE.png/1024px-Western_Turkic_Khaganate_circa_600_CE.png',
  'fun_fact': {'uz': "G'arbiy Turk xoqonligi poytaxti Suyob shahri bo'lib, Movarounnahr, Yettisuv va Kavkazorti "
                     "xalqlarini o'z ichiga olgan.",
               'ru': 'Западно-тюркский каганат со столицей в Суябе контролировал ключевые оазисы Шелкового пути и '
                     'торговые маршруты согдийцев.',
               'en': 'The Western Turkic Khaganate was centered in the Seven Rivers (Semirechye) and controlled the '
                     'main trans-Eurasian trade routes.'},
  'aliases': ['garbiy turk xoqonligi', 'on oq', 'западно-тюркский каганат', 'western turkic khaganate']},
 {'id': 'hist_time_map_042',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["Qirg'iz xoqonligi", "Uyg'ur xoqonligi (O'rxun vodiysi)", 'Xazar xoqonligi', 'Kimak xoqonligi'],
              'ru': ['Кыргызский каганат',
                     'Уйгурский каганат (Орхонский каганат)',
                     'Хазарский каганат',
                     'Кимакский каганат'],
              'en': ['Yenisei Kyrgyz Khaganate',
                     'Uyghur Khaganate (Orkhon Valley)',
                     'Khazar Khaganate',
                     'Kimek Khaganate']},
  'correct_index': 1,
  'correct_answer': {'uz': "Uyg'ur xoqonligi (O'rxun vodiysi)",
                     'ru': 'Уйгурский каганат (Орхонский каганат)',
                     'en': 'Uyghur Khaganate (Orkhon Valley)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Uyghur_Khaganate_800_CE.png/1024px-Uyghur_Khaganate_800_CE.png',
  'fun_fact': {'uz': "Uyg'ur xoqonligi poytaxti Qorabalg'asun bo'lib, bu davlatda moniylik dini rasmiy davlat dini deb "
                     'qabul qilingan va yozma madaniyat rivojlangan.',
               'ru': 'Уйгурский каганат (744–840 гг.) со столицей в Карабалгасуне принял манихейство и развил '
                     'самобытную городскую культуру.',
               'en': 'The Uyghur Khaganate (744-840 AD) made Manichaeism its state religion and built impressive '
                     'walled cities in the Orkhon Valley.'},
  'aliases': ['uygur xoqonligi', 'уйгурский каганат', 'uyghur khaganate']},
 {'id': 'hist_time_map_043',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Moskva buyuk knyazligi',
                     'Novgorod respublikasi',
                     'Qadimgi Kiyev Rusi (Yaroslav Mudriy davri)',
                     'Litva buyuk knyazligi'],
              'ru': ['Великое княжество Московское',
                     'Новгородская республика',
                     'Киевская Русь (эпоха Ярослава Мудрого)',
                     'Великое княжество Литовское'],
              'en': ['Grand Duchy of Moscow',
                     'Novgorod Republic',
                     'Kievan Rus (era of Yaroslav the Wise)',
                     'Grand Duchy of Lithuania']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Qadimgi Kiyev Rusi (Yaroslav Mudriy davri)',
                     'ru': 'Киевская Русь (эпоха Ярослава Мудрого)',
                     'en': 'Kievan Rus (era of Yaroslav the Wise)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Kievan_Rus_en.jpg/1024px-Kievan_Rus_en.jpg',
  'fun_fact': {'uz': "Kiyev Rusi 'Varyaglardan yunonlargacha' savdo yo'lini nazorat qilgan va XI asrda Yevropaning eng "
                     "yirik davlatlaridan biri bo'lgan.",
               'ru': 'Киевская Русь объединила восточнославянские земли от Балтики до Черного моря, приняв православие '
                     'в 988 году.',
               'en': 'Kievan Rus was a medieval federation that flourished along the Dnieper River trade route between '
                     'Scandinavia and Byzantium.'},
  'aliases': ['kiyev rusi', 'qadimgi rus', 'киевская русь', 'kievan rus']},
 {'id': 'hist_time_map_044',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Prussiya qirolligi',
                     'Avstriya imperiyasi',
                     'Shvetsiya imperiyasi',
                     'Rech Pospolita (Polsha-Litva ittifoqi)'],
              'ru': ['Королевство Пруссия',
                     'Австрийская империя',
                     'Шведская империя',
                     'Речь Посполитая (Польско-Литовское государство)'],
              'en': ['Kingdom of Prussia', 'Austrian Empire', 'Swedish Empire', 'Polish-Lithuanian Commonwealth']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Rech Pospolita (Polsha-Litva ittifoqi)',
                     'ru': 'Речь Посполитая (Польско-Литовское государство)',
                     'en': 'Polish-Lithuanian Commonwealth'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Polish-Lithuanian_Commonwealth_at_its_greatest_extent.png/1024px-Polish-Lithuanian_Commonwealth_at_its_greatest_extent.png',
  'fun_fact': {'uz': "1569 yildagi Lyublin uniyasi bilan tuzilgan Rech Pospolita qirol saylanadigan 'Shlyaxetlik "
                     "demokratiyasi' bilan boshqarilgan.",
               'ru': 'Речь Посполитая была крупнейшим государством Европы в XVI–XVII веках с уникальным строем '
                     '«шляхетской демократии».',
               'en': "Formed by the 1569 Union of Lublin, it was one of early modern Europe's largest states, known "
                     'for its noble democracy.'},
  'aliases': ['rech pospolita', 'polsha litva', 'речь посполитая', 'polish lithuanian commonwealth']},
 {'id': 'hist_time_map_045',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Shvetsiya imperiyasi (Buyuk davlat davri — Stormaktstiden)',
                     'Daniya-Norvegiya uniyasi',
                     'Prussiya qirolligi',
                     'Kalmar uniyasi'],
              'ru': ['Шведская империя (эпоха великодержавия — Stormaktstiden)',
                     'Датско-норвежская уния',
                     'Королевство Пруссия',
                     'Кальмарская уния'],
              'en': ['Swedish Empire (Stormaktstiden)', 'Denmark-Norway', 'Kingdom of Prussia', 'Kalmar Union']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Shvetsiya imperiyasi (Buyuk davlat davri — Stormaktstiden)',
                     'ru': 'Шведская империя (эпоха великодержавия — Stormaktstiden)',
                     'en': 'Swedish Empire (Stormaktstiden)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Swedish_Empire_1658.png/1024px-Swedish_Empire_1658.png',
  'fun_fact': {'uz': "Gustav II Adolf davrida Shvetsiya Boltiq dengizini o'zining 'ichki ko'liga' aylantirib, "
                     'Yevropaning eng qudratli harbiy davlatiga aylangan.',
               'ru': 'В XVII веке Швеция доминировала на Балтике, пока не потерпела поражение от России в Северной '
                     'войне.',
               'en': 'During the 17th century, Sweden dominated the Baltic Sea until defeated by Peter the Great in '
                     'the Great Northern War.'},
  'aliases': ['shvetsiya imperiyasi', 'шведская империя', 'швеция', 'swedish empire']},
 {'id': 'hist_time_map_046',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Ispaniya imperiyasi',
                     'Portugaliya mustamlakachilik imperiyasi',
                     'Gollandiya imperiyasi',
                     'Britaniya imperiyasi'],
              'ru': ['Испанская империя',
                     'Португальская колониальная империя',
                     'Голландская империя',
                     'Британская империя'],
              'en': ['Spanish Empire', 'Portuguese Empire', 'Dutch Empire', 'British Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Portugaliya mustamlakachilik imperiyasi',
                     'ru': 'Португальская колониальная империя',
                     'en': 'Portuguese Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Portuguese_Empire_anachronous.png/1024px-Portuguese_Empire_anachronous.png',
  'fun_fact': {'uz': 'Portugaliya Braziliya, Angola, Mozambik, Goa (Hindiston) va Makaoni (Xitoy) birlashtirgan '
                     "birinchi va eng uzoq umr ko'rgan (1415-1999) Yevropa global imperiyasi bo'lgan.",
               'ru': 'Португалия создала первую глобальную империю Нового времени, простиравшуюся от Бразилии до Макао '
                     'и Нагасаки.',
               'en': 'The Portuguese Empire was the first global European maritime empire, lasting nearly six '
                     'centuries from Ceuta (1415) to Macau (1999).'},
  'aliases': ['portugaliya', 'portugaliya imperiyasi', 'португальская империя', 'portuguese empire']},
 {'id': 'hist_time_map_047',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Belgiya mustamlakalari',
                     'Daniya imperiyasi',
                     'Gollandiya (Niderlandiya) mustamlaka imperiyasi',
                     'Portugaliya imperiyasi'],
              'ru': ['Бельгийская империя',
                     'Датская империя',
                     'Голландская колониальная империя',
                     'Португальская империя'],
              'en': ['Belgian Colonial Empire', 'Danish Empire', 'Dutch Colonial Empire', 'Portuguese Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Gollandiya (Niderlandiya) mustamlaka imperiyasi',
                     'ru': 'Голландская колониальная империя',
                     'en': 'Dutch Colonial Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Dutch_Empire_anachronous.png/1024px-Dutch_Empire_anachronous.png',
  'fun_fact': {'uz': "Gollandiya Ost-Indiya kompaniyasi dunyoda ilk bor aksiyalar chiqargan korporatsiya bo'lib, "
                     "hozirgi Indoneziyani to'liq boshqargan.",
               'ru': 'Голландцы доминировали в мировой торговле пряностями XVII века, владея Индонезией, Цейлоном и '
                     'Суринамом.',
               'en': 'The Dutch built a worldwide maritime network in the 17th century powered by the VOC, centered on '
                     'the Dutch East Indies (Indonesia).'},
  'aliases': ['gollandiya', 'gollandiya imperiyasi', 'голландская империя', 'нидерланды', 'dutch empire']},
 {'id': 'hist_time_map_048',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Afshoriylar davlati',
                     'Qojarlar davlati',
                     'Usmonli imperiyasi',
                     'Safaviylar davlati (Shoh Abbos)'],
              'ru': ['Держава Афшаридов',
                     'Государство Каджаров',
                     'Османская империя',
                     'Государство Сефевидов (Шах Аббас I)'],
              'en': ['Afsharid Empire', 'Qajar Empire', 'Ottoman Empire', 'Safavid Empire (Shah Abbas)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Safaviylar davlati (Shoh Abbos)',
                     'ru': 'Государство Сефевидов (Шах Аббас I)',
                     'en': 'Safavid Empire (Shah Abbas)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Safavid_Empire_at_its_greatest_extent.png/1024px-Safavid_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': "Shoh Ismoil I asos solgan Safaviylar davlati poytaxt Isfahonda 'Yarim jahon' (Isfahon nisfi "
                     "jahon) deb atalgan me'moriy mo'jizalarni bunyod etdi.",
               'ru': 'Сефевиды сделали шиизм государственной религией Ирана и построили великолепную столицу в '
                     'Исфахане.',
               'en': "Under Shah Abbas I, the Safavids made Isfahan ('Half the World') one of the most magnificent "
                     'Renaissance-era cultural capitals.'},
  'aliases': ['safaviylar', 'safaviy', 'сефевиды', 'государство сефевидов', 'safavid', 'safavid empire']},
 {'id': 'hist_time_map_049',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Afshoriylar saltanati (Nodirshoh)',
                     'Safaviylar davlati',
                     'Qojarlar davlati',
                     'Boburiylar davlati'],
              'ru': ['Империя Афшаридов (Надир-шах)',
                     'Государство Сефевидов',
                     'Государство Каджаров',
                     'Империя Великих Моголов'],
              'en': ['Afsharid Empire (Nader Shah)', 'Safavid Empire', 'Qajar Empire', 'Mughal Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Afshoriylar saltanati (Nodirshoh)',
                     'ru': 'Империя Афшаридов (Надир-шах)',
                     'en': 'Afsharid Empire (Nader Shah)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Afsharid_Empire_at_its_greatest_extent.png/1024px-Afsharid_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': "Nodirshoh 'Sharqning so'nggi buyuk sarkardasi' va 'Fors Napoleon'i deb atalgan; u Dehlidan "
                     "mashhur Ko'hi Nur olmosi va Tovus taxtini olib ketgan.",
               'ru': 'Надир-шах Афшар завоевал огромные земли от Кавказа до Дели, захватив знаменитый алмаз «Кохинур».',
               'en': "Known as the 'Sword of Persia', Nader Shah conquered Delhi, Oman, and Central Asia, amassing "
                     'unparalleled treasure.'},
  'aliases': ['afshoriylar', 'nodirshoh', 'афшариды', 'надир-шах', 'afsharid', 'nader shah']},
 {'id': 'hist_time_map_050',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Safaviylar davlati', 'Qojarlar davlati (Eron)', 'Zandlar davlati', 'Pahlaviylar sulolasi'],
              'ru': ['Государство Сефевидов', 'Государство Каджаров (Персия)', 'Династия Зенд', 'Династия Пехлеви'],
              'en': ['Safavid Empire', 'Qajar Empire (Persia)', 'Zand Dynasty', 'Pahlavi Dynasty']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Qojarlar davlati (Eron)',
                     'ru': 'Государство Каджаров (Персия)',
                     'en': 'Qajar Empire (Persia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Qajar_Empire_1814.png/1024px-Qajar_Empire_1814.png',
  'fun_fact': {'uz': "Oga Muhammadxon asos solgan Qojarlar sulolasi poytaxtni Tehronga ko'chirgan va Eronni XIX asrdan "
                     '1925 yilgacha boshqargan.',
               'ru': 'Династия Каджаров сделала Тегеран столицей Ирана, ведя противостояние с Российской и Британской '
                     'империями («Большая игра»).',
               'en': "The Qajars designated Tehran as capital and ruled Iran throughout the 19th-century 'Great Game' "
                     'until 1925.'},
  'aliases': ['qojarlar', 'qojar davlati', 'каджары', 'qajar', 'qajar dynasty']},
 {'id': 'hist_map_051',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Boburiylar imperiyasi',
                     'Guptalar imperiyasi',
                     "Dehli sultonligi (Muhammad Tug'luq davri)",
                     "G'aznaviylar davlati"],
              'ru': ['Империя Великих Моголов',
                     'Империя Гупта',
                     'Делийский султанат (эпоха Мухаммада Туглака)',
                     'Государство Газневидов'],
              'en': ['Mughal Empire',
                     'Gupta Empire',
                     'Delhi Sultanate (under Muhammad bin Tughluq)',
                     'Ghaznavid Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': "Dehli sultonligi (Muhammad Tug'luq davri)",
                     'ru': 'Делийский султанат (эпоха Мухаммада Туглака)',
                     'en': 'Delhi Sultanate (under Muhammad bin Tughluq)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Delhi_Sultanate_1330.png/1024px-Delhi_Sultanate_1330.png',
  'fun_fact': {'uz': 'Dehli sultonligi 1206-1526 yillarda Shimoliy va Markaziy Hindistonni boshqargan 5 ta turkiy va '
                     "afg'on sulolalari ittifoqi bo'lgan.",
               'ru': 'Делийский султанат отбил несколько нашествий монголов и распространил исламскую культуру по всей '
                     'Индии.',
               'en': 'The Delhi Sultanate ruled large parts of the subcontinent from 1206 until conquered by Babur in '
                     '1526.'},
  'aliases': ['dehli sultonligi', 'делийский султанат', 'delhi sultanate']},
 {'id': 'hist_map_052',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Maurya imperiyasi',
                     'Pallava podsholigi',
                     'Pandya podsholigi',
                     'Chola imperiyasi (Janubiy Hindiston va dengiz orti)'],
              'ru': ['Империя Маурьев',
                     'Государство Паллавов',
                     'Государство Пандья',
                     'Империя Чола (Южная Индия и морские владения)'],
              'en': ['Maurya Empire',
                     'Pallava Dynasty',
                     'Pandya Dynasty',
                     'Chola Empire (South India and Thalassocracy)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Chola imperiyasi (Janubiy Hindiston va dengiz orti)',
                     'ru': 'Империя Чола (Южная Индия и морские владения)',
                     'en': 'Chola Empire (South India and Thalassocracy)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Chola_Empire_1030.png/1024px-Chola_Empire_1030.png',
  'fun_fact': {'uz': 'Chola imperatori Rajendra I ulkan harbiy-dengiz floti tuzib, Shri-Lanka, Malayziya va '
                     'Indoneziyadagi Shrivijaya davlatini zabt etgan.',
               'ru': 'Тамильская династия Чола создала мощнейший военный флот, контролировавший морские пути '
                     'Индийского океана.',
               'en': 'Under Rajendra Chola I, the Chola navy conquered Sri Lanka and parts of the Indonesian Srivijaya '
                     'Empire in 1025 AD.'},
  'aliases': ['chola', 'chola imperiyasi', 'чола', 'империя чола', 'chola empire']},
 {'id': 'hist_map_053',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Vijayanagara imperiyasi (Xampi)', 'Bahmaniy sultonligi', 'Marathalar davlati', 'Chola davlati'],
              'ru': ['Империя Виджаянагара (Хампи)', 'Бахманидский султанат', 'Империя Маратха', 'Империя Чола'],
              'en': ['Vijayanagara Empire (Hampi)', 'Bahmani Sultanate', 'Maratha Empire', 'Chola Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Vijayanagara imperiyasi (Xampi)',
                     'ru': 'Империя Виджаянагара (Хампи)',
                     'en': 'Vijayanagara Empire (Hampi)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Vijayanagara_Empire_map.png/1024px-Vijayanagara_Empire_map.png',
  'fun_fact': {'uz': "Vijayanagara poytaxti Xampi o'z davrida dunyodagi ikkinchi eng yirik shahar bo'lib, mislsiz tosh "
                     'ibodatxonalar majmuasiga ega edi.',
               'ru': 'Виджаянагара была могущественной индуистской империей юга Индии, противостоявшей деканским '
                     'султанатам.',
               'en': 'Centred on the monumental city of Hampi, Vijayanagara ruled Southern India from 1336 until '
                     '1646.'},
  'aliases': ['vijayanagara', 'xampi', 'виджаянагара', 'хампи', 'vijayanagara empire']},
 {'id': 'hist_map_054',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Shrivijaya imperiyasi',
                     'Majapaxit dengiz imperiyasi (Indoneziya)',
                     'Mataram sultonligi',
                     'Malakka sultonligi'],
              'ru': ['Империя Шривиджая',
                     'Морская империя Маджапахит (Индонезия)',
                     'Султанат Матарам',
                     'Малаккский султанат'],
              'en': ['Srivijaya Empire', 'Majapahit Empire (Indonesia)', 'Mataram Sultanate', 'Malacca Sultanate']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Majapaxit dengiz imperiyasi (Indoneziya)',
                     'ru': 'Морская империя Маджапахит (Индонезия)',
                     'en': 'Majapahit Empire (Indonesia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Majapahit_Empire_map.png/1024px-Majapahit_Empire_map.png',
  'fun_fact': {'uz': 'Gadjah Mada boshchiligidagi Majapaxit Yava, Sumatra, Kalimantan va Malay yarimorolini '
                     'birlashtirib, Indoneziya tarixidagi eng buyuk saltanatga aylandi.',
               'ru': 'Маджапахит объединил сотни островов Малайского архипелага, став золотым веком индонезийской '
                     'истории.',
               'en': 'Under Prime Minister Gajah Mada, Majapahit ruled the Maritime Southeast Asian archipelago in the '
                     '14th century.'},
  'aliases': ['majapaxit', 'majapahit', 'маджапахит', 'majapahit empire']},
 {'id': 'hist_map_055',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Champa davlati', 'Ayuttiya qirolligi', 'Kxmer imperiyasi (Angkor)', 'Pagan podsholigi'],
              'ru': ['Тямпа (Чампа)', 'Королевство Аютия', 'Кхмерская империя (Ангкор)', 'Царство Паган'],
              'en': ['Champa', 'Ayutthaya Kingdom', 'Khmer Empire (Angkor)', 'Pagan Kingdom']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Kxmer imperiyasi (Angkor)',
                     'ru': 'Кхмерская империя (Ангкор)',
                     'en': 'Khmer Empire (Angkor)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Khmer_Empire_900_CE.png/1024px-Khmer_Empire_900_CE.png',
  'fun_fact': {'uz': "Kxmerlar Kambodjada dunyodagi eng yirik diniy inshoot bo'lgan muazzam Angkor Vat ibodatxona "
                     'majmuasini barpo etishgan.',
               'ru': 'Кхмерская империя доминировала в Юго-Восточной Азии и построила колоссальный храмовый комплекс '
                     'Ангкор-Ват.',
               'en': 'The Khmer Empire ruled mainland Southeast Asia from the 9th to 15th centuries, constructing '
                     'iconic Angkor Wat.'},
  'aliases': ['kxmer', 'kxmer imperiyasi', 'angkor', 'кхмерская империя', 'ангкор', 'khmer', 'khmer empire']},
 {'id': 'hist_map_056',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Majapaxit davlati',
                     'Sailendra sulolasi',
                     'Bruney sultonligi',
                     'Shrivijaya talassokratiyasi (Sumatra)'],
              'ru': ['Империя Маджапахит',
                     'Династия Сайлендра',
                     'Султанат Бруней',
                     'Морская империя Шривиджая (Суматра)'],
              'en': ['Majapahit Empire', 'Sailendra Dynasty', 'Bruneian Empire', 'Srivijaya Empire (Sumatra)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Shrivijaya talassokratiyasi (Sumatra)',
                     'ru': 'Морская империя Шривиджая (Суматра)',
                     'en': 'Srivijaya Empire (Sumatra)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Srivijaya_Empire.svg/1024px-Srivijaya_Empire.svg.png',
  'fun_fact': {'uz': "Shrivijaya Malakka bo'g'ozini nazorat qilib, Xitoy va Hindiston o'rtasidagi barcha dengiz ipak "
                     "yo'li savdosini boshqargan.",
               'ru': 'Шривиджая была буддийской морской державой, веками контролировавшей ключевой Малаккский пролив.',
               'en': 'Srivijaya was a powerful maritime Buddhist empire based on Sumatra that dominated the Malacca '
                     'Strait trade.'},
  'aliases': ['shrivijaya', 'srivijaya', 'шривиджая', 'srivijaya empire']},
 {'id': 'hist_map_057',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Fotimiylar xalifaligi (Qohira)',
                     'Mamluklar sultonligi',
                     'Ayyubiylar sultonligi',
                     'Umaviylar xalifaligi'],
              'ru': ['Фатимидский халифат (Каир)', 'Мамлюкский султанат', 'Айюбидский султанат', 'Омейядский халифат'],
              'en': ['Fatimid Caliphate (Cairo)', 'Mamluk Sultanate', 'Ayyubid Sultanate', 'Umayyad Caliphate']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Fotimiylar xalifaligi (Qohira)',
                     'ru': 'Фатимидский халифат (Каир)',
                     'en': 'Fatimid Caliphate (Cairo)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Fatimid_Caliphate_at_its_greatest_extent.png/1024px-Fatimid_Caliphate_at_its_greatest_extent.png',
  'fun_fact': {'uz': 'Fotimiylar Qohira shahriga asos solishgan va 970 yilda dunyodagi eng qadimgi faol '
                     'dorilfununlardan biri Al-Azxar universitetini barpo etishgan.',
               'ru': 'Фатимиды основали Каир и построили мечеть-университет Аль-Азхар, распространив власть на Египет, '
                     'Сирию и Хиджаз.',
               'en': 'The Fatimids founded Cairo in 969 AD, establishing the historic Al-Azhar Mosque and University.'},
  'aliases': ['fotimiylar',
              'fotimiylar xalifaligi',
              'фатимиды',
              'фатимидский халифат',
              'fatimid',
              'fatimid caliphate']},
 {'id': 'hist_map_058',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Usmonli imperiyasi',
                     'Mamluklar sultonligi (Misr va Shom)',
                     'Ayyubiylar davlati',
                     'Fotimiylar davlati'],
              'ru': ['Османская империя',
                     'Мамлюкский султанат (Египет и Сирия)',
                     'Государство Айюбидов',
                     'Государство Фатимидов'],
              'en': ['Ottoman Empire', 'Mamluk Sultanate of Cairo', 'Ayyubid Sultanate', 'Fatimid State']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Mamluklar sultonligi (Misr va Shom)',
                     'ru': 'Мамлюкский султанат (Египет и Сирия)',
                     'en': 'Mamluk Sultanate of Cairo'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Mamluk_Sultanate_1317.png/1024px-Mamluk_Sultanate_1317.png',
  'fun_fact': {'uz': "Mamluklar asosan qipchoq va cherkes kelib chiqishiga ega jangchilardan iborat bo'lib, "
                     "salibchilarni Yaqin Sharqdan batamom haydab chiqargan va mo'g'ullarni to'xtatgan.",
               'ru': 'Мамлюки Египта остановили монгольское наступление при Айн-Джалуте и окончательно изгнали '
                     'крестоносцев из Леванта.',
               'en': 'The soldier-slave caste of Mamluks ruled Egypt and Syria from 1250 to 1517, expelling Crusaders '
                     'and halting Mongols.'},
  'aliases': ['mamluklar', 'mamluk sultonligi', 'мамлюки', 'мамлюкский султанат', 'mamluk', 'mamluk sultanate']},
 {'id': 'hist_map_059',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Muvahhidlar davlati',
                     'Mariniylar sulolasi',
                     'Murobitlar (Almoravidlar) saltanati',
                     'Fotimiylar davlati'],
              'ru': ['Государство Альмохадов',
                     'Династия Маринидов',
                     'Государство Альморавидов (Магриб и Андалусия)',
                     'Государство Фатимидов'],
              'en': ['Almohad Caliphate',
                     'Marinid Sultanate',
                     'Almoravid Dynasty (Maghreb and Andalusia)',
                     'Fatimid Caliphate']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Murobitlar (Almoravidlar) saltanati',
                     'ru': 'Государство Альморавидов (Магриб и Андалусия)',
                     'en': 'Almoravid Dynasty (Maghreb and Andalusia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Almoravid_Empire_at_its_greatest_extent.png/1024px-Almoravid_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': 'Yusuf ibn Toshfin asos solgan Murobitlar davlati Marokash poytaxti Marrakesh shahriga asos '
                     'solgan va Zallaqa jangida ispan xristian qirollarini yenggan.',
               'ru': 'Альморавиды вышли из Сахары, основали Марракеш и объединили Марокко с мусульманской Испанией.',
               'en': 'The Berber Almoravid dynasty founded Marrakesh and united Morocco and Muslim Spain after winning '
                     'the Battle of Sagrajas (1086).'},
  'aliases': ['murobitlar', 'almoravidlar', 'альморавиды', 'almoravid', 'almoravids']},
 {'id': 'hist_map_060',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Murobitlar davlati',
                     'Qurtuba xalifaligi',
                     'Usmonli imperiyasi',
                     'Muvahhidlar (Almohadlar) xalifaligi'],
              'ru': ['Государство Альморавидов',
                     'Кордовский халифат',
                     'Османская империя',
                     'Альмохадский халифат (Магриб и Иберия)'],
              'en': ['Almoravid Empire',
                     'Caliphate of Cordoba',
                     'Ottoman Empire',
                     'Almohad Caliphate (Maghreb and Iberia)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Muvahhidlar (Almohadlar) xalifaligi',
                     'ru': 'Альмохадский халифат (Магриб и Иберия)',
                     'en': 'Almohad Caliphate (Maghreb and Iberia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Almohad_Empire_1200.png/1024px-Almohad_Empire_1200.png',
  'fun_fact': {'uz': 'Muvahhidlar butun Shimoliy Afrikani (Marokash, Jazoir, Tunis, Liviya) va Ispaniyani boshqargan '
                     "yagona berber xalifaligi bo'lgan.",
               'ru': 'Альмохады создали крупнейшую берберскую империю в истории, построив знаменитую башню Хиральда в '
                     'Севилье.',
               'en': 'The Almohad Caliphate unified the entire Maghreb with Andalusia, constructing the famed Giralda '
                     'minaret in Seville.'},
  'aliases': ['muvahhidlar', 'almohadlar', 'альмохады', 'альмохадский халифат', 'almohad', 'almohad caliphate']},
 {'id': 'hist_map_061',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Aksum qirolligi (Efiopiya / Habashiston)',
                     'Kush podsholigi',
                     'Mali imperiyasi',
                     'Songay imperiyasi'],
              'ru': ['Аксумское царство (Эфиопия)', 'Царство Куш', 'Империя Мали', 'Империя Сонгай'],
              'en': ['Kingdom of Aksum (Ethiopia)', 'Kingdom of Kush', 'Mali Empire', 'Songhai Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Aksum qirolligi (Efiopiya / Habashiston)',
                     'ru': 'Аксумское царство (Эфиопия)',
                     'en': 'Kingdom of Aksum (Ethiopia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Kingdom_of_Aksum_map.png/1024px-Kingdom_of_Aksum_map.png',
  'fun_fact': {'uz': "Aksum fors manbalarida Rim, Fors va Xitoy bilan bir qatorda 'dunyodagi to'rtta buyuk imperiyadan "
                     "biri' deb tan olingan va milodiy IV asrda xristianlikni qabul qilgan.",
               'ru': 'Аксум контролировал торговлю на Красном море и чеканил собственные золотые монеты с III века '
                     'н.э.',
               'en': 'The Prophet Mani called Aksum one of the four great powers of the world alongside Rome, Persia, '
                     'and China.'},
  'aliases': ['aksum', 'aksum qirolligi', 'аксум', 'аксумское царство', 'aksum', 'kingdom of aksum']},
 {'id': 'hist_map_062',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Somali sultonligi', 'Efiopiya imperiyasi (Abissiniya)', 'Kongo qirolligi', 'Zanzibar sultonligi'],
              'ru': ['Султанат Адаль', 'Эфиопская империя (Абиссиния)', 'Королевство Конго', 'Занзибарский султанат'],
              'en': ['Adal Sultanate', 'Ethiopian Empire (Abyssinia)', 'Kingdom of Kongo', 'Sultanate of Zanzibar']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Efiopiya imperiyasi (Abissiniya)',
                     'ru': 'Эфиопская империя (Абиссиния)',
                     'en': 'Ethiopian Empire (Abyssinia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Ethiopian_Empire_1896.png/1024px-Ethiopian_Empire_1896.png',
  'fun_fact': {'uz': 'Imperator Menelik II 1896 yilda Adua jangida Italiya armiyasini tor-mor etib, Efiopiyani '
                     "mustamlaka bo'lmagan yagona Afrika davlatiga aylantirgan.",
               'ru': 'Эфиопия отстояла независимость в битве при Адуа в 1896 году, став символом антиколониального '
                     'сопротивления в Африке.',
               'en': 'Ethiopia defeated Italian invaders at Adwa in 1896, preserving its sovereignty throughout the '
                     'Scramble for Africa.'},
  'aliases': ['efiopiya', 'abissiniya', 'эфиопия', 'абиссиния', 'ethiopia', 'abyssinia']},
 {'id': 'hist_map_063',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Aksum qirolligi',
                     'Qadimgi Misr podsholigi',
                     'Kush podsholigi (Nubiya / Meroe)',
                     'Punt mamlakati'],
              'ru': ['Царство Аксум', 'Древний Египет', 'Царство Куш (Нубия / Мероэ)', 'Земля Пунт'],
              'en': ['Kingdom of Aksum', 'Ancient Egypt', 'Kingdom of Kush (Nubia / Meroë)', 'Land of Punt']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Kush podsholigi (Nubiya / Meroe)',
                     'ru': 'Царство Куш (Нубия / Мероэ)',
                     'en': 'Kingdom of Kush (Nubia / Meroë)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Kingdom_of_Kush_map.png/1024px-Kingdom_of_Kush_map.png',
  'fun_fact': {'uz': "Kush podsholari ('Qora fir'avnlar') Misrni zabt etib, mil. avv. VIII asrda 25-sulola sifatida "
                     "butun Nil vodiysini boshqargan; Meroeda Misrdan ko'proq piramidalar mavjud.",
               'ru': 'Цари Куша («черные фараоны») правили Египтом как XXV династия, оставив в Судане более 200 '
                     'пирамид.',
               'en': "Kushite 'Black Pharaohs' ruled Egypt as the 25th Dynasty; Sudan actually contains more ancient "
                     'pyramids than Egypt.'},
  'aliases': ['kush', 'kush podsholigi', 'nubiya', 'куш', 'царство куш', 'нубия', 'kush', 'kingdom of kush']},
 {'id': 'hist_map_064',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Lunda imperiyasi', 'Benin qirolligi', 'Monomotapa davlati', 'Kongo qirolligi (Markaziy Afrika)'],
              'ru': ['Империя Лунда',
                     'Королевство Бенин',
                     'Империя Мономотапа',
                     'Королевство Конго (Центральная Африка)'],
              'en': ['Lunda Empire', 'Kingdom of Benin', 'Kingdom of Mutapa', 'Kingdom of Kongo (Central Africa)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Kongo qirolligi (Markaziy Afrika)',
                     'ru': 'Королевство Конго (Центральная Африка)',
                     'en': 'Kingdom of Kongo (Central Africa)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Kingdom_of_Kongo_1711.png/1024px-Kingdom_of_Kongo_1711.png',
  'fun_fact': {'uz': "Kongo qirolligi 1483 yilda portugallar kelishidan ancha oldin qudratli davlat bo'lib, o'z "
                     "poytaxti Mbanza-Kongoda o'ziga xos temir va to'qimachilik madaniyatini rivojlantirgan.",
               'ru': 'Королевство Конго было развитой централизованной монархией в бассейне реки Конго с XIV по начало '
                     'XX века.',
               'en': 'The Kingdom of Kongo was a centralized monarchy dominating Central Africa from the 14th to the '
                     '19th centuries.'},
  'aliases': ['kongo qirolligi', 'kongo', 'королевство конго', 'конго', 'kingdom of kongo']},
 {'id': 'hist_map_065',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Zulu qirolligi (Shaka Zulu)',
                     'Transvaal respublikasi',
                     'Matabele qirolligi',
                     'Kosa xalqi davlati'],
              'ru': ['Королевство зулусов (Шака Зулу)',
                     'Республика Трансвааль',
                     'Королевство Матабеле',
                     'Государство Коса'],
              'en': ['Zulu Kingdom (Shaka Zulu)',
                     'South African Republic',
                     'Northern Ndebele Kingdom',
                     'Xhosa Kingdom']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Zulu qirolligi (Shaka Zulu)',
                     'ru': 'Королевство зулусов (Шака Зулу)',
                     'en': 'Zulu Kingdom (Shaka Zulu)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Zulu_Kingdom_1879.png/1024px-Zulu_Kingdom_1879.png',
  'fun_fact': {'uz': "Shaka Zulu 'buqa shoxlari' harbiy taktikasi va qisqa nayzani (iklva) ixtiro qilib, Janubiy "
                     'Afrikada yengilmas jangchilar armiyasini tuzdi.',
               'ru': 'Шака реформировал армию зулусов, которая в 1879 году нанесла поражение британским войскам в '
                     'битве при Исандлване.',
               'en': 'Shaka Zulu forged a formidable military kingdom whose warriors famously routed British forces at '
                     'Isandlwana in 1879.'},
  'aliases': ['zulu', 'zulu qirolligi', 'shaka', 'зулусы', 'королевство зулусов', 'zulu kingdom']},
 {'id': 'hist_map_066',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Kongo qirolligi', 'Mutapa imperiyasi (Buyuk Zimbabve)', 'Mali imperiyasi', 'Buganda qirolligi'],
              'ru': ['Королевство Конго',
                     'Империя Мономотапа (Великий Зимбабве)',
                     'Империя Мали',
                     'Королевство Буганда'],
              'en': ['Kingdom of Kongo', 'Kingdom of Mutapa (Great Zimbabwe)', 'Mali Empire', 'Kingdom of Buganda']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Mutapa imperiyasi (Buyuk Zimbabve)',
                     'ru': 'Империя Мономотапа (Великий Зимбабве)',
                     'en': 'Kingdom of Mutapa (Great Zimbabwe)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Mutapa_Empire_1560.png/1024px-Mutapa_Empire_1560.png',
  'fun_fact': {'uz': "Buyuk Zimbabve qalin qorishmasiz tosh devorlardan qurilgan ulkan qasrlar majmuasi bo'lib, oltin "
                     "va fil suyagi savdosi markazi bo'lgan.",
               'ru': 'Империя Мономотапа контролировала золотые прииски между реками Замбези и Лимпопо, торгуя с '
                     'арабами и португальцами.',
               'en': 'Mutapa flourished between the Zambezi and Limpopo rivers, building the monumental stone '
                     'enclosures of Great Zimbabwe.'},
  'aliases': ['mutapa', 'monomotapa', 'buyuk zimbabve', 'мономотапа', 'великий зимбабве', 'mutapa empire']},
 {'id': 'hist_map_067',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Muqaddas Rim imperiyasi',
                     'Vestgotlar qirolligi',
                     'Franklar imperiyasi (Buyuk Karl)',
                     'Ostgotlar qirolligi'],
              'ru': ['Священная Римская империя',
                     'Королевство вестготов',
                     'Империя франков (Карл Великий)',
                     'Королевство остготов'],
              'en': ['Holy Roman Empire',
                     'Visigothic Kingdom',
                     'Frankish Empire (Charlemagne)',
                     'Ostrogothic Kingdom']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Franklar imperiyasi (Buyuk Karl)',
                     'ru': 'Империя франков (Карл Великий)',
                     'en': 'Frankish Empire (Charlemagne)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Charlemagne_empire_814.svg/1024px-Charlemagne_empire_814.svg.png',
  'fun_fact': {'uz': 'Buyuk Karl davrida Franklar davlati Fransiya, Germaniya, Italiya va Niderlandiyani birlashtirib, '
                     "zamonaviy G'arbiy Yevropaga tamal toshini qo'ydi.",
               'ru': 'Империя Карла Великого объединила Западную Европу впервые после падения Рима, став '
                     'прародительницей Франции и Германии.',
               'en': 'Charlemagne united Western Europe for the first time since classical Rome, laying the seeds of '
                     'modern France and Germany.'},
  'aliases': ['franklar imperiyasi', 'buyuk karl davlati', 'империя франков', 'карл великий', 'frankish empire']},
 {'id': 'hist_map_068',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Rim imperiyasi (Trayan)',
                     "G'arbiy Rim imperiyasi",
                     'Karfagen respublikasi',
                     "Rim respublikasi (Yuliy Sezar o'limi payti, mil. avv. 44)"],
              'ru': ['Римская империя (Траян)',
                     'Западная Римская империя',
                     'Карфагенская республика',
                     'Римская республика (на момент гибели Юлия Цезаря, 44 г. до н.э.)'],
              'en': ['Roman Empire (Trajan)',
                     'Western Roman Empire',
                     'Carthaginian Republic',
                     "Roman Republic (at Caesar's death, 44 BC)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Rim respublikasi (Yuliy Sezar o'limi payti, mil. avv. 44)",
                     'ru': 'Римская республика (на момент гибели Юлия Цезаря, 44 г. до н.э.)',
                     'en': "Roman Republic (at Caesar's death, 44 BC)"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Roman_Republic_44_BC.png/1024px-Roman_Republic_44_BC.png',
  'fun_fact': {'uz': 'Senat va Rim xalqi (SPQR) tomonidan boshqarilgan respublika Sezarning Galliyani zabt etishi va '
                     "Fuqarolar urushidan so'ng imperiyaga aylangan.",
               'ru': 'Римская республика просуществовала почти 500 лет, пока убийство Цезаря не открыло путь к '
                     'принципату Августа.',
               'en': 'The Roman Republic dominated the Mediterranean for five centuries before transforming into the '
                     'Roman Empire under Augustus.'},
  'aliases': ['rim respublikasi', 'римская республика', 'spqr', 'roman republic']},
 {'id': 'hist_map_069',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Qadimgi Misr (Yangi podsholik davri, Tutmos III)',
                     'Qadimgi Misr (Qadimgi podsholik)',
                     'Ptolemeylar Misri',
                     'Kush podsholigi'],
              'ru': ['Древний Египет (Новое царство, Тутмос III)',
                     'Древнее царство Египта',
                     'Египет Птолемеев',
                     'Царство Куш'],
              'en': ['Ancient Egypt (New Kingdom, Thutmose III)',
                     'Old Kingdom of Egypt',
                     'Ptolemaic Egypt',
                     'Kingdom of Kush']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Qadimgi Misr (Yangi podsholik davri, Tutmos III)',
                     'ru': 'Древний Египет (Новое царство, Тутмос III)',
                     'en': 'Ancient Egypt (New Kingdom, Thutmose III)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/New_Kingdom_Empire_1450_BCE.png/1024px-New_Kingdom_Empire_1450_BCE.png',
  'fun_fact': {'uz': 'Tutmos III va Ramzes II davrida Misr Furot daryosidan to Sudan (Nubiya) janubigacha hududlarni '
                     "zabt etib, o'zining eng cho'qqisiga chiqqan.",
               'ru': 'В эпоху Нового царства фараоны Тутмос III и Рамсес II создали первую египетскую империю от '
                     'Евфрата до 4-го порога Нила.',
               'en': 'During the New Kingdom (1550-1077 BC), Egypt reached its zenith, extending from the Euphrates to '
                     'the Fourth Cataract of the Nile.'},
  'aliases': ['yangi misr', 'qadimgi misr', 'древний египет', 'новое царство', 'ancient egypt', 'new kingdom egypt']},
 {'id': 'hist_map_070',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Yangi Bobil imperiyasi',
                     'Yangi Ossuriya imperiyasi (Ashurbanipal)',
                     'Xett podsholigi',
                     'Ahamoniylar imperiyasi'],
              'ru': ['Нововавилонское царство',
                     'Новоассирийская империя (Ашшурбанапал)',
                     'Хеттское царство',
                     'Ахеменидская империя'],
              'en': ['Neo-Babylonian Empire',
                     'Neo-Assyrian Empire (Ashurbanipal)',
                     'Hittite Empire',
                     'Achaemenid Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Yangi Ossuriya imperiyasi (Ashurbanipal)',
                     'ru': 'Новоассирийская империя (Ашшурбанапал)',
                     'en': 'Neo-Assyrian Empire (Ashurbanipal)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Neo_Assyrian_Empire_650_BCE.png/1024px-Neo_Assyrian_Empire_650_BCE.png',
  'fun_fact': {'uz': "Ossuriya temir qurollar, qamal mashinalari va dahshatli otliq qo'shinlar bilan Mesopotamiya, "
                     'Suriya va Misrni zabt etgan ilk harbiy superdavlat edi.',
               'ru': 'Новоассирийская империя со столицей в Ниневии создала первую в мире регулярную армию и '
                     'знаменитую глиняную библиотеку Ашшурбанапала.',
               'en': "Centred on Nineveh, the Neo-Assyrian Empire was antiquity's first military superpower, known for "
                     'iron weaponry and siegecraft.'},
  'aliases': ['ossuriya', 'yangi ossuriya', 'ассирия', 'новоассирийская империя', 'assyria', 'neo-assyrian']},
 {'id': 'hist_map_071',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Ossuriya imperiyasi',
                     'Ahamoniylar imperiyasi',
                     'Yangi Bobil (Xaldey) imperiyasi (Navuxodonosor II)',
                     'Mitanni podsholigi'],
              'ru': ['Ассирийская империя',
                     'Империя Ахеменидов',
                     'Нововавилонское (Халдейское) царство (Навуходоносор II)',
                     'Царство Митанни'],
              'en': ['Assyrian Empire',
                     'Achaemenid Empire',
                     'Neo-Babylonian (Chaldean) Empire (Nebuchadnezzar II)',
                     'Mitanni']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Yangi Bobil (Xaldey) imperiyasi (Navuxodonosor II)',
                     'ru': 'Нововавилонское (Халдейское) царство (Навуходоносор II)',
                     'en': 'Neo-Babylonian (Chaldean) Empire (Nebuchadnezzar II)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Neo-Babylonian_Empire_at_its_greatest_extent.png/1024px-Neo-Babylonian_Empire_at_its_greatest_extent.png',
  'fun_fact': {'uz': 'Navuxodonosor II Bobilning mashhur Ishtar darvozasini, Bobil minorasini (Etemenanki) va dunyo '
                     "mo'jizasi bo'lgan 'Semiramida osma bog'lari'ni qurdirgan.",
               'ru': 'Навуходоносор II отстроил Вавилон, возвел Висячие сады Семирамиды и захватил Иерусалим, начав '
                     'Вавилонский плен.',
               'en': 'Nebuchadnezzar II built the Ishtar Gate and the Hanging Gardens of Babylon, dominating '
                     'Mesopotamia until Cyrus took it in 539 BC.'},
  'aliases': ['bobil', 'yangi bobil', 'вавилон', 'нововавилонское царство', 'babylon', 'neo-babylonian']},
 {'id': 'hist_map_072',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Lidiya podsholigi', 'Frigiya podsholigi', 'Urartu podsholigi', 'Xettlar imperiyasi (Xattusa)'],
              'ru': ['Лидийское царство', 'Фригийское царство', 'Царство Урарту', 'Хеттское царство (Хаттуса)'],
              'en': ['Kingdom of Lydia', 'Phrygian Kingdom', 'Kingdom of Urartu', 'Hittite Empire (Hattusa)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Xettlar imperiyasi (Xattusa)',
                     'ru': 'Хеттское царство (Хаттуса)',
                     'en': 'Hittite Empire (Hattusa)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Hittite_Empire_1300_BC.png/1024px-Hittite_Empire_1300_BC.png',
  'fun_fact': {'uz': 'Xettlar Anatoliyada (hozirgi Turkiya) qudratli davlat tuzib, mil. avv. 1274 yilda Kadesh jangida '
                     "Misr fir'avni Ramzes II bilan to'qnashgan va tarixdagi ilk yozma tinchlik shartnomasini tuzgan.",
               'ru': 'Хетты первыми освоили технологию выплавки железа и заключили с Египтом древнейший сохранившийся '
                     'мирный договор после битвы при Кадеше.',
               'en': "The Hittites pioneered ironworking and chariot warfare, signing the world's earliest known peace "
                     'treaty with Ramesses II after Kadesh.'},
  'aliases': ['xettlar', 'xett davlati', 'хетты', 'хеттское царство', 'hittite', 'hittite empire']},
 {'id': 'hist_map_073',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Akkad imperiyasi (Buyuk Sargon)', 'Shumer shahar-davlatlari', 'Elam davlati', 'Bobil davlati'],
              'ru': ['Аккадская империя (Саргон Древний)',
                     'Шумерские города-государства',
                     'Государство Элам',
                     'Вавилонское царство'],
              'en': ['Akkadian Empire (Sargon of Akkad)', 'Sumerian City-States', 'Elam', 'Babylonian Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Akkad imperiyasi (Buyuk Sargon)',
                     'ru': 'Аккадская империя (Саргон Древний)',
                     'en': 'Akkadian Empire (Sargon of Akkad)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Akkadian_Empire_2200_BCE.png/1024px-Akkadian_Empire_2200_BCE.png',
  'fun_fact': {'uz': 'Akkad davlati mil. avv. XXIII asrda barcha Mesopotamiya shaharlarini birlashtirib, insoniyat '
                     'tarixidagi birinchi imperiyaga aylangan.',
               'ru': 'Саргон Древний около 2334 года до н.э. создал первую централизованную империю в истории '
                     'человечества.',
               'en': 'Founded by Sargon the Great around 2334 BC, the Akkadian Empire is regarded by historians as the '
                     'first empire in world history.'},
  'aliases': ['akkad', 'sargon', 'аккад', 'саргон', 'akkad', 'akkadian empire']},
 {'id': 'hist_map_074',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Armaniston qirolligi',
                     'Gruziya qirolligi (Oltin davr, Malika Tamar)',
                     'Trabzon imperiyasi',
                     'Shirvonshohlar davlati'],
              'ru': ['Армянское царство',
                     'Грузинское царство (Золотой век, царица Тамара)',
                     'Трапезундская империя',
                     'Государство Ширваншахов'],
              'en': ['Kingdom of Armenia',
                     'Kingdom of Georgia (Golden Age, Queen Tamar)',
                     'Empire of Trebizond',
                     'Shirvanshah State']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Gruziya qirolligi (Oltin davr, Malika Tamar)',
                     'ru': 'Грузинское царство (Золотой век, царица Тамара)',
                     'en': 'Kingdom of Georgia (Golden Age, Queen Tamar)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Kingdom_of_Georgia_Tamar_era.png/1024px-Kingdom_of_Georgia_Tamar_era.png',
  'fun_fact': {'uz': 'Dovud Quruvchi va Malika Tamar davrida (XI-XIII asrlar) Gruziya Kavkazning eng qudratli '
                     "davlatiga aylanib, Shota Rustaveli o'zining shoh asarini unga bag'ishlagan.",
               'ru': 'Золотой век Грузии при царице Тамаре (1184–1213) ознаменовался расцветом культуры, зодчества и '
                     'поэзией Шоты Руставели.',
               'en': 'Under King David IV and Queen Tamar, medieval Georgia ruled the Caucasus, inspiring Shota '
                     "Rustaveli's epic poetry."},
  'aliases': ['gruziya qirolligi', 'malika tamar', 'грузинское царство', 'царица тамара', 'kingdom of georgia']},
 {'id': 'hist_map_075',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Kilikiya arman podsholigi',
                     'Pont podsholigi',
                     'Buyuk Armaniston qirolligi (Buyuk Tigran II)',
                     'Albaniya (Kavkaz) davlati'],
              'ru': ['Киликийское армянское царство',
                     'Понтийское царство',
                     'Великая Армения (эпоха Тиграна II Великого)',
                     'Кавказская Албания'],
              'en': ['Armenian Kingdom of Cilicia',
                     'Kingdom of Pontus',
                     'Kingdom of Greater Armenia (Tigranes the Great)',
                     'Caucasian Albania']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Buyuk Armaniston qirolligi (Buyuk Tigran II)',
                     'ru': 'Великая Армения (эпоха Тиграна II Великого)',
                     'en': 'Kingdom of Greater Armenia (Tigranes the Great)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Tigranes_great_empire.png/1024px-Tigranes_great_empire.png',
  'fun_fact': {'uz': "Buyuk Tigran II davrida (mil. avv. I asr) davlat Kaspiy, O'rta yer va Qora dengizlar "
                     "oralig'idagi hududlarni egallagan.",
               'ru': 'При Тигране II Великом держава простиралась от Каспийского до Средиземного моря («Армения от '
                     'моря до моря»).',
               'en': 'Under Tigranes II, Greater Armenia stretched from the Mediterranean Sea to the Caspian Sea in '
                     'the 1st century BC.'},
  'aliases': ['armaniston', 'buyuk tigran', 'великая армения', 'тигран великий', 'greater armenia', 'tigranes']},
 {'id': 'hist_map_076',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Ashtarxoniylar davlati',
                     "Qo'qon xonligi",
                     'Xiva xonligi',
                     'Shayboniylar davlati (Buxoro xonligi)'],
              'ru': ['Аштарханиды (Джаниды)',
                     'Кокандское ханство',
                     'Хивинское ханство',
                     'Государство Шейбанидов (Бухарское ханство)'],
              'en': ['Ashtarkhanid Dynasty',
                     'Khanate of Kokand',
                     'Khanate of Khiva',
                     'Shaybanid Khanate (Khanate of Bukhara)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Shayboniylar davlati (Buxoro xonligi)',
                     'ru': 'Государство Шейбанидов (Бухарское ханство)',
                     'en': 'Shaybanid Khanate (Khanate of Bukhara)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Shaybanid_Dynasty_1510.png/1024px-Shaybanid_Dynasty_1510.png',
  'fun_fact': {'uz': "Shayboniyxon 1500 yilda Samarqand va Movarounnahrni egallab, yangi o'zbek davlatchiligiga asos "
                     "solgan va Abdullaxon II davrida qudrati cho'qqisiga chiqqan.",
               'ru': 'Шейбаниды во главе с Мухаммедом Шейбани объединили Мавераннахр и Хорасан, сделав Бухару столицей '
                     'процветающего государства.',
               'en': 'Founded by Muhammad Shaybani in 1500, the Shaybanids ruled Transoxiana, building numerous '
                     'architectural monuments in Bukhara.'},
  'aliases': ['shayboniylar', 'shayboniyxon', 'шейбаниды', 'бухарское ханство', 'shaybanid', 'khanate of bukhara']},
 {'id': 'hist_map_077',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Xiva xonligi (Xorazm davlati)', 'Buxoro amirligi', "Qo'qon xonligi", 'Qozoq xonligi'],
              'ru': ['Хивинское ханство (Государство Хорезм)',
                     'Бухарский эмират',
                     'Кокандское ханство',
                     'Казахское ханство'],
              'en': ['Khanate of Khiva (State of Khwarazm)',
                     'Emirate of Bukhara',
                     'Khanate of Kokand',
                     'Kazakh Khanate']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Xiva xonligi (Xorazm davlati)',
                     'ru': 'Хивинское ханство (Государство Хорезм)',
                     'en': 'Khanate of Khiva (State of Khwarazm)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Khanate_of_Khiva_1800.png/1024px-Khanate_of_Khiva_1800.png',
  'fun_fact': {'uz': "Xiva xonligi poytaxti Ichan Qal'a bo'lib, xonlik Amudaryo etaklari, Qoraqum va Kaspiy bo'ylarini "
                     "o'z ichiga olgan.",
               'ru': 'Хивинское ханство в низовьях Амударьи сохраняло уникальную культуру Хорезма, а его столица '
                     'Ичан-Кала вошла в список ЮНЕСКО.',
               'en': 'The Khanate of Khiva was centered in the ancient oasis of Khwarazm, with its intact walled '
                     'capital Itchan Kala.'},
  'aliases': ['xiva xonligi', 'xiva', 'xorazm xonligi', 'хивинское ханство', 'хива', 'khanate of khiva', 'khiva']},
 {'id': 'hist_map_078',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Buxoro amirligi', "Qo'qon xonligi (Farg'ona vodiysi)", 'Xiva xonligi', 'Qashqar xonligi'],
              'ru': ['Бухарский эмират',
                     'Кокандское ханство (Ферганская долина)',
                     'Хивинское ханство',
                     'Кашгарское ханство'],
              'en': ['Emirate of Bukhara',
                     'Khanate of Kokand (Fergana Valley)',
                     'Khanate of Khiva',
                     'Yarkent Khanate']},
  'correct_index': 1,
  'correct_answer': {'uz': "Qo'qon xonligi (Farg'ona vodiysi)",
                     'ru': 'Кокандское ханство (Ферганская долина)',
                     'en': 'Khanate of Kokand (Fergana Valley)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Kokand_Khanate_1850.png/1024px-Kokand_Khanate_1850.png',
  'fun_fact': {'uz': "Qo'qon xonligi Olimxon va Umarxon davrida Toshkent, Chimkent, Turkiston va Yettisuvni o'z ichiga "
                     'olgan yirik davlatga aylangan.',
               'ru': 'Кокандское ханство контролировало Ферганскую долину, Ташкент и юг современного Казахстана до '
                     'присоединения к России в 1876 году.',
               'en': 'At its peak, the Khanate of Kokand ruled from the Fergana Valley across Tashkent, Shymkent, and '
                     'parts of modern Kyrgyzstan and Kazakhstan.'},
  'aliases': ['qoqon xonligi', 'qoqon', 'кокандское ханство', 'коканд', 'khanate of kokand', 'kokand']},
 {'id': 'hist_map_079',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Xiva xonligi', "Qo'qon xonligi", "Buxoro amirligi (Mang'itlar sulolasi)", "Afg'oniston amirligi"],
              'ru': ['Хивинское ханство',
                     'Кокандское ханство',
                     'Бухарский эмират (династия Мангытов)',
                     'Эмират Афганистан'],
              'en': ['Khanate of Khiva',
                     'Khanate of Kokand',
                     'Emirate of Bukhara (Manghit Dynasty)',
                     'Emirate of Afghanistan']},
  'correct_index': 2,
  'correct_answer': {'uz': "Buxoro amirligi (Mang'itlar sulolasi)",
                     'ru': 'Бухарский эмират (династия Мангытов)',
                     'en': 'Emirate of Bukhara (Manghit Dynasty)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Emirate_of_Bukhara_1868.png/1024px-Emirate_of_Bukhara_1868.png',
  'fun_fact': {'uz': "Shohmurod asos solgan Mang'itlar sulolasi davrida Buxoro hukmdorlari 'amir' (Amir al-mo'minin) "
                     'unvonini olgan va 1920 yilgacha hukmronlik qilgan.',
               'ru': 'Бухарский эмират с центром в священной Бухаре был влиятельным центром исламского образования '
                     'вплоть до падения в 1920 году.',
               'en': 'Ruled by the Manghit dynasty from 1785 to 1920, the Emirate of Bukhara was the predominant state '
                     'in southern Central Asia.'},
  'aliases': ['buxoro amirligi', 'mangitlar', 'бухарский эмират', 'мангыты', 'emirate of bukhara', 'bukhara']},
 {'id': 'hist_map_080',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Genuya respublikasi',
                     'Piza respublikasi',
                     'Ikki Sitsiliya qirolligi',
                     'Venetsiya dengiz respublikasi (Serenissima)'],
              'ru': ['Генуэзская республика',
                     'Пизанская республика',
                     'Королевство Обеих Сицилий',
                     'Венецианская морская республика (Серениссима)'],
              'en': ['Republic of Genoa',
                     'Republic of Pisa',
                     'Kingdom of the Two Sicilies',
                     'Republic of Venice (Most Serene Republic)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Venetsiya dengiz respublikasi (Serenissima)',
                     'ru': 'Венецианская морская республика (Серениссима)',
                     'en': 'Republic of Venice (Most Serene Republic)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Republic_of_Venice_1560.png/1024px-Republic_of_Venice_1560.png',
  'fun_fact': {'uz': "Venetsiya 1100 yildan ortiq davom etgan respublika bo'lib, O'rta yer dengizi va Adriatika "
                     'savdosini, Kipr va Krit orollarini nazorat qilgan.',
               'ru': 'Венецианская республика дожей правила более тысячи лет, владея Критом, Кипром и ключевыми '
                     'портами Средиземноморья.',
               'en': 'Venice flourished as a maritime trading republic for over a millennium (697-1797), ruled by its '
                     'elected Doge.'},
  'aliases': ['venetsiya',
              'venetsiya respublikasi',
              'венецианская республика',
              'венеция',
              'venice',
              'republic of venice']},
 {'id': 'hist_map_081',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Genuya dengiz respublikasi',
                     'Venetsiya respublikasi',
                     'Florensiya respublikasi',
                     'Sardiniya qirolligi'],
              'ru': ['Генуэзская морская республика',
                     'Венецианская республика',
                     'Флорентийская республика',
                     'Сардинское королевство'],
              'en': ['Republic of Genoa', 'Republic of Venice', 'Republic of Florence', 'Kingdom of Sardinia']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Genuya dengiz respublikasi',
                     'ru': 'Генуэзская морская республика',
                     'en': 'Republic of Genoa'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Republic_of_Genoa_1400.png/1024px-Republic_of_Genoa_1400.png',
  'fun_fact': {'uz': 'Genuya Qrimdagi Kafa (Feodosiya) va Qora dengiz portlarini nazorat qilgan; Xristofor Kolumb '
                     "aynan Genuya shahrida tug'ilgan.",
               'ru': 'Генуэзцы владели Корсикой и мощными торговыми факториями в Крыму (Кафа, Судак), ведя '
                     'ожесточенное соперничество с Венецией.',
               'en': "Genoa was Venice's fierce maritime rival, controlling Corsica and major Black Sea trading "
                     'outposts in Crimea like Kaffa.'},
  'aliases': ['genuya', 'genuya respublikasi', 'генуэзская республика', 'генуя', 'republic of genoa', 'genoa']},
 {'id': 'hist_map_082',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Shvetsiya imperiyasi',
                     'Kalmar uniyasi (Daniya, Shvetsiya, Norvegiya birlashmasi)',
                     'Ganza savdo ittifoqi',
                     'Daniya-Norvegiya qirolligi'],
              'ru': ['Шведская империя',
                     'Кальмарская уния (объединение Дании, Норвегии и Швеции)',
                     'Ганзейский союз',
                     'Датско-норвежское королевство'],
              'en': ['Swedish Empire', 'Kalmar Union (Scandinavia)', 'Hanseatic League', 'Denmark-Norway']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Kalmar uniyasi (Daniya, Shvetsiya, Norvegiya birlashmasi)',
                     'ru': 'Кальмарская уния (объединение Дании, Норвегии и Швеции)',
                     'en': 'Kalmar Union (Scandinavia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Kalmar_Union_1400.png/1024px-Kalmar_Union_1400.png',
  'fun_fact': {'uz': '1397 yilda malika Margareta I tomonidan tuzilgan Kalmar uniyasi butun Skandinaviya, Islandiya va '
                     'Grenlandiyani yagona toj ostida birlashtirgan.',
               'ru': 'Кальмарская уния объединила все скандинавские королевства под властью датской королевы Маргариты '
                     'I.',
               'en': 'Formed in 1397, the Kalmar Union united the three Scandinavian kingdoms of Denmark, Norway, and '
                     'Sweden under a single monarch.'},
  'aliases': ['kalmar uniyasi', 'skandinaviya uniyasi', 'кальмарская уния', 'kalmar union']},
 {'id': 'hist_map_083',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Shvetsiya imperiyasi',
                     'Norvegiya qirolligi',
                     'Daniya mustamlakachilik imperiyasi (Grenlandiya, Islandiya)',
                     'Niderlandiya imperiyasi'],
              'ru': ['Шведская империя',
                     'Королевство Норвегия',
                     'Датская колониальная империя (Гренландия, Исландия)',
                     'Нидерландская империя'],
              'en': ['Swedish Empire', 'Kingdom of Norway', 'Danish Colonial Empire', 'Dutch Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Daniya mustamlakachilik imperiyasi (Grenlandiya, Islandiya)',
                     'ru': 'Датская колониальная империя (Гренландия, Исландия)',
                     'en': 'Danish Colonial Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Danish_Empire_map.png/1024px-Danish_Empire_map.png',
  'fun_fact': {'uz': 'Daniya Shimoliy muz okeanidagi Grenlandiya va Farer orollaridan tashqari, Hindistondagi '
                     'Trankebar va Karibdagi Virgin orollariga egalik qilgan.',
               'ru': 'Датская корона владела колониями в Карибском море, факториями в Индии и сохраняет юрисдикцию над '
                     'Гренландией поныне.',
               'en': 'Denmark established trading colonies in India, West Africa, and the Caribbean, maintaining '
                     'sovereignty over Greenland today.'},
  'aliases': ['daniya', 'daniya imperiyasi', 'датская империя', 'дания', 'danish empire']},
 {'id': 'hist_map_084',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Muqaddas Rim imperiyasi',
                     'Prussiya qirolligi',
                     'Veymar respublikasi',
                     'Germaniya imperiyasi (Ikkinchi Reyx, Bismark davri)'],
              'ru': ['Священная Римская империя',
                     'Королевство Пруссия',
                     'Веймарская республика',
                     'Германская империя (Второй рейх, эпоха Бисмарка)'],
              'en': ['Holy Roman Empire',
                     'Kingdom of Prussia',
                     'Weimar Republic',
                     'German Empire (Second Reich, 1871-1918)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Germaniya imperiyasi (Ikkinchi Reyx, Bismark davri)',
                     'ru': 'Германская империя (Второй рейх, эпоха Бисмарка)',
                     'en': 'German Empire (Second Reich, 1871-1918)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/German_Empire_1914.png/1024px-German_Empire_1914.png',
  'fun_fact': {'uz': "Otto fon Bismark 'temir va qon' bilan nemis davlatlarini birlashtirib, 1871 yilda Versal "
                     'saroyida kayzer Vilgelm I ga imperatorlik tojini kiydirgan.',
               'ru': 'Второй рейх объединил разрозненные немецкие земли после победы над Францией в 1871 году, став '
                     'индустриальным гигантом Европы.',
               'en': "Unified under Bismarck in 1871, the German Empire became Europe's leading industrial and "
                     'military power until 1918.'},
  'aliases': ['germaniya imperiyasi',
              'ikkinchi reyx',
              'bismark',
              'германская империя',
              'второй рейх',
              'german empire']},
 {'id': 'hist_map_085',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Birinchi Fransiya imperiyasi (Napoleon Bonapart)',
                     'Ikkinchi Fransiya imperiyasi',
                     'Franklar imperiyasi',
                     'Ispaniya imperiyasi'],
              'ru': ['Первая Французская империя (Наполеон Бонапарт)',
                     'Вторая Французская империя',
                     'Франкская империя',
                     'Испанская империя'],
              'en': ['First French Empire (Napoleon Bonaparte)',
                     'Second French Empire',
                     'Frankish Empire',
                     'Spanish Empire']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Birinchi Fransiya imperiyasi (Napoleon Bonapart)',
                     'ru': 'Первая Французская империя (Наполеон Бонапарт)',
                     'en': 'First French Empire (Napoleon Bonaparte)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/First_French_Empire_1812.png/1024px-First_French_Empire_1812.png',
  'fun_fact': {'uz': "1812 yilda Napoleon butun kontinental Yevropani (Ispaniyadan to Polshagacha) o'ziga bo'ysundirib "
                     'yoki vassal davlatlarga aylantirgan edi.',
               'ru': 'На пике могущества в 1812 году Наполеон контролировал почти всю континентальную Европу до '
                     'рокового похода в Россию.',
               'en': "At its zenith in 1812, Napoleon's French Empire held sway over continental Europe from Madrid to "
                     'Warsaw.'},
  'aliases': ['napoleon imperiyasi',
              'birinchi fransuz imperiyasi',
              'империя наполеона',
              'первая французская империя',
              'napoleonic empire']},
 {'id': 'hist_map_086',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Sin imperiyasi',
                     "Buyuk Yaponiya imperiyasi (1942 yil cho'qqisi)",
                     'Manchjou-go',
                     'Koreya imperiyasi'],
              'ru': ['Империя Цин',
                     'Японская империя (максимальная экспансия 1942 года)',
                     'Маньчжоу-го',
                     'Корейская империя'],
              'en': ['Qing Empire', 'Empire of Japan (at its peak in 1942)', 'Manchukuo', 'Korean Empire']},
  'correct_index': 1,
  'correct_answer': {'uz': "Buyuk Yaponiya imperiyasi (1942 yil cho'qqisi)",
                     'ru': 'Японская империя (максимальная экспансия 1942 года)',
                     'en': 'Empire of Japan (at its peak in 1942)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Empire_of_Japan_1942.png/1024px-Empire_of_Japan_1942.png',
  'fun_fact': {'uz': '1942 yilda Yaponiya Manjuriya, Sharqiy Xitoy, Filippin, Indoneziya, Malayziya, Birma va Tinch '
                     'okeani orollarini egallab, 7,4 million kv km ga kengaygan edi.',
               'ru': 'В 1942 году Японская империя контролировала огромные пространства Восточной Азии и Тихого океана '
                     'под лозунгом «Сферы сопроцветания».',
               'en': 'In 1942, Imperial Japan controlled over 7 million sq km across Southeast Asia and the Pacific '
                     'Ocean.'},
  'aliases': ['yapon imperiyasi',
              'buyuk yaponiya imperiyasi',
              'японская империя',
              'empire of japan',
              'imperial japan']},
 {'id': 'hist_map_087',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Bavariya qirolligi',
                     'Saksoniya qirolligi',
                     'Prussiya qirolligi (Fridrix II Buyuk)',
                     'Avstriya gersogligi'],
              'ru': ['Королевство Бавария',
                     'Королевство Саксония',
                     'Королевство Пруссия (Фридрих II Великий)',
                     'Эрцгерцогство Австрия'],
              'en': ['Kingdom of Bavaria',
                     'Kingdom of Saxony',
                     'Kingdom of Prussia (Frederick the Great)',
                     'Archduchy of Austria']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Prussiya qirolligi (Fridrix II Buyuk)',
                     'ru': 'Королевство Пруссия (Фридрих II Великий)',
                     'en': 'Kingdom of Prussia (Frederick the Great)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Kingdom_of_Prussia_1806.png/1024px-Kingdom_of_Prussia_1806.png',
  'fun_fact': {'uz': "Fridrix II davrida Prussiya qudratli armiyasi tufayli 'Armiyasi bor davlat emas, o'ziga davlat "
                     "qurib olgan armiya' deb atalgan.",
               'ru': 'Пруссия с центром в Берлине славилась железной военной дисциплиной и стала ядром объединения '
                     'Германии в XIX веке.',
               'en': 'Known for strict militarism under Frederick the Great, Prussia drove the unification of Germany '
                     'in the 19th century.'},
  'aliases': ['prussiya', 'prussiya qirolligi', 'пруссия', 'королевство пруссия', 'prussia', 'kingdom of prussia']},
 {'id': 'hist_map_088',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Angliya qirolligi',
                     'Shotlandiya qirolligi',
                     'Birlashgan Qirollik (Irlandiya bilan)',
                     'Buyuk Britaniya qirolligi (1707 yilgi Uniya)'],
              'ru': ['Королевство Англия',
                     'Королевство Шотландия',
                     'Соединенное Королевство',
                     'Королевство Великобритания (Акт об унии 1707 года)'],
              'en': ['Kingdom of England',
                     'Kingdom of Scotland',
                     'United Kingdom',
                     'Kingdom of Great Britain (Union of 1707)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Buyuk Britaniya qirolligi (1707 yilgi Uniya)',
                     'ru': 'Королевство Великобритания (Акт об унии 1707 года)',
                     'en': 'Kingdom of Great Britain (Union of 1707)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Great_Britain_1707.png/1024px-Great_Britain_1707.png',
  'fun_fact': {'uz': "1707 yildagi Uniya to'g'risidagi qonun bilan Angliya va Shotlandiya parlamentlari birlashib, "
                     "rasman 'Buyuk Britaniya' davlati vujudga keldi.",
               'ru': 'Акт об унии 1707 года объединил парламенты Англии и Шотландии, создав единое суверенное '
                     'королевство Великобританию.',
               'en': 'The Acts of Union in 1707 united the Kingdom of England and Kingdom of Scotland into a single '
                     'sovereign realm.'},
  'aliases': ['buyuk britaniya', '1707 uniyasi', 'великобритания', 'королевство великобритания', 'great britain']},
 {'id': 'hist_map_089',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Anju (Plantagenetlar) imperiyasi (Genrix II)',
                     'Fransiya qirolligi (Kapetinglar)',
                     'Burgundiya gersogligi',
                     'Normandiya gersogligi'],
              'ru': ['Анжуйская империя Плантагенетов (Генрих II)',
                     'Королевство Франция (Капетинги)',
                     'Герцогство Бургундия',
                     'Герцогство Нормандия'],
              'en': ['Angevin Empire (Plantagenet Dynasty)',
                     'Kingdom of France',
                     'Duchy of Burgundy',
                     'Duchy of Normandy']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Anju (Plantagenetlar) imperiyasi (Genrix II)',
                     'ru': 'Анжуйская империя Плантагенетов (Генрих II)',
                     'en': 'Angevin Empire (Plantagenet Dynasty)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Angevin_Empire_1190.png/1024px-Angevin_Empire_1190.png',
  'fun_fact': {'uz': "Genrix II va Richard Sheryurak davrida ingliz qirollari Fransiyaning yarmidan ko'pini "
                     '(Normandiya, Akvitaniya, Anju) boshqargan.',
               'ru': 'Анжуйская держава охватывала Англию и западную половину Франции, что привело к многовековой '
                     'борьбе с французской короной.',
               'en': 'Henry II and Richard the Lionheart ruled an empire extending from the Scottish border to the '
                     'Pyrenees.'},
  'aliases': ['anju imperiyasi', 'plantagenetlar', 'анжуйская империя', 'плантагенеты', 'angevin', 'angevin empire']},
 {'id': 'hist_map_090',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["Oltin O'rda", "Chig'atoy ulusi (Markaziy Osiyo)", 'Elxoniylar davlati', 'Qoraqoyunlilar davlati'],
              'ru': ['Золотая Орда', 'Чагатайский улус (Средняя Азия)', 'Государство Хулагуидов', 'Кара-Коюнлу'],
              'en': ['Golden Horde', 'Chagatai Khanate (Central Asia)', 'Ilkhanate', 'Qara Qoyunlu']},
  'correct_index': 1,
  'correct_answer': {'uz': "Chig'atoy ulusi (Markaziy Osiyo)",
                     'ru': 'Чагатайский улус (Средняя Азия)',
                     'en': 'Chagatai Khanate (Central Asia)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Chagatai_Khanate_1300.png/1024px-Chagatai_Khanate_1300.png',
  'fun_fact': {'uz': "Chingizxonning ikkinchi o'g'li Chig'atoyga berilgan bu ulus Movarounnahr, Yettisuv va Sharqiy "
                     "Turkistonni birlashtirgan bo'lib, chig'atoy (eski o'zbek) tili rivojlangan.",
               'ru': 'Чагатайский улус охватывал сердце Центральной Азии, дав название литературному чагатайскому '
                     '(староузбекскому) языку.',
               'en': "Inherited by Genghis Khan's second son Chagatai, this khanate encompassed Central Asia and gave "
                     'rise to the Chagatai literary language.'},
  'aliases': ['chigatoy ulusi', 'chigatoy', 'чагатайский улус', 'чагатай', 'chagatai', 'chagatai khanate']},
 {'id': 'hist_map_091',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Temuriylar saltanati',
                     "Chig'atoy ulusi",
                     'Elxoniylar (Xuloguiylar) davlati',
                     'Saljuqiylar saltanati'],
              'ru': ['Империя Тимуридов',
                     'Чагатайский улус',
                     'Государство Хулагуидов (Ильханат)',
                     'Сельджукская империя'],
              'en': ['Timurid Empire', 'Chagatai Khanate', 'Ilkhanate (Hulagu Dynasty)', 'Seljuk Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Elxoniylar (Xuloguiylar) davlati',
                     'ru': 'Государство Хулагуидов (Ильханат)',
                     'en': 'Ilkhanate (Hulagu Dynasty)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ilkhanate_1300.png/1024px-Ilkhanate_1300.png',
  'fun_fact': {'uz': "Xulogu xon asos solgan bu davlat poytaxti Tabriz bo'lib, Eron, Iroq, Ozarbayjon va Sharqiy "
                     "Anatoliyani egallagan; G'ozonxon davrida Islom davlat diniga aylangan.",
               'ru': 'Ильханат Хулагу со столицей в Тебризе объединял Иран, Ирак и Закавказье, приняв ислам при '
                     'Газан-хане.',
               'en': 'Established by Hulagu Khan, the Ilkhanate encompassed Iran, Iraq, and Azerbaijan, patronizing '
                     'Persian arts from Tabriz.'},
  'aliases': ['elxoniylar', 'xuloguiylar', 'ильханат', 'хулагуиды', 'ilkhanate']},
 {'id': 'hist_map_092',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Sun sulolasi', 'Szin imperiyasi', 'Lyao imperiyasi', "G'arbiy Sya (Tangut imperiyasi)"],
              'ru': ['Империя Сун', 'Империя Цзинь', 'Империя Ляо', 'Западное Ся (Тангутское царство)'],
              'en': ['Song Dynasty', 'Jin Dynasty', 'Liao Dynasty', 'Western Xia (Tangut Empire)']},
  'correct_index': 3,
  'correct_answer': {'uz': "G'arbiy Sya (Tangut imperiyasi)",
                     'ru': 'Западное Ся (Тангутское царство)',
                     'en': 'Western Xia (Tangut Empire)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Western_Xia_1111.png/1024px-Western_Xia_1111.png',
  'fun_fact': {'uz': "Tangutlar Buyuk Ipak yo'lining shimoliy bo'g'inini nazorat qilgan va o'ziga xos murakkab "
                     'iyeroglif yozuvini yaratgan; 1227 yilda Chingizxon ularni tor-mor qilgan.',
               'ru': 'Тангутское государство Западное Ся обладало самобытной письменностью и пало под ударами '
                     'Чингисхана в 1227 году.',
               'en': "The Tangut Western Xia ruled the Hexi Corridor until obliterated by Genghis Khan's Mongols in "
                     '1227.'},
  'aliases': ['garbiy sya', 'tangutlar', 'западное ся', 'тангуты', 'western xia', 'tangut']},
 {'id': 'hist_map_093',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Szin (Chjurjen) imperiyasi (Shimoliy Xitoy)', 'Sun sulolasi', 'Lyao imperiyasi', 'Min sulolasi'],
              'ru': ['Империя Цзинь (чжурчжэни в Северном Китае)', 'Империя Сун', 'Империя Ляо', 'Империя Мин'],
              'en': ['Jin Dynasty (Jurchen Northern China)', 'Song Dynasty', 'Liao Dynasty', 'Ming Dynasty']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Szin (Chjurjen) imperiyasi (Shimoliy Xitoy)',
                     'ru': 'Империя Цзинь (чжурчжэни в Северном Китае)',
                     'en': 'Jin Dynasty (Jurchen Northern China)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Jin_Dynasty_1141.png/1024px-Jin_Dynasty_1141.png',
  'fun_fact': {'uz': 'Chjurjenlar Shimoliy Xitoyni zabt etib, Sun sulolasini janubga chekinishga majbur qilgan; ular '
                     'keyinchalik manchjurlarning ajdodlari hisoblangan.',
               'ru': 'Империя чжурчжэней Цзинь захватила север Китая со столицей в Чжунду (Пекине), предшествуя '
                     'династии Цин.',
               'en': 'The Jurchen Jin Dynasty ruled Northern China from 1115 to 1234, ancestors of the Manchus who '
                     'later founded the Qing.'},
  'aliases': ['szin', 'chjurjenlar', 'цзинь', 'чжурчжэни', 'jin dynasty', 'jurchen']},
 {'id': 'hist_map_094',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Boburiylar davlati', 'Marathalar imperiyasi (Shivaji)', 'Dehli sultonligi', 'Maysur qirolligi'],
              'ru': ['Империя Великих Моголов',
                     'Империя Маратхов (Шиваджи)',
                     'Делийский султанат',
                     'Королевство Майсур'],
              'en': ['Mughal Empire', 'Maratha Empire (Shivaji)', 'Delhi Sultanate', 'Kingdom of Mysore']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Marathalar imperiyasi (Shivaji)',
                     'ru': 'Империя Маратхов (Шиваджи)',
                     'en': 'Maratha Empire (Shivaji)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Maratha_Empire_1760.png/1024px-Maratha_Empire_1760.png',
  'fun_fact': {'uz': 'Chhatrapati Shivaji asos solgan bu konfederatsiya Boburiylarga qarshi partizanlik taktikasi '
                     "bilan kurashib, XVIII asrda Hindistonning asosiy qismida hukmron bo'lgan.",
               'ru': 'Империя Маратхов сокрушила господство Великих Моголов и контролировала большую часть Индии до '
                     'войн с англичанами.',
               'en': 'Founded by Shivaji in 1674, the Hindu Maratha confederacy superseded Mughal power across central '
                     'and northern India.'},
  'aliases': ['marathalar', 'shivaji', 'маратхи', 'империя маратхов', 'maratha', 'maratha empire']},
 {'id': 'hist_map_095',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Marathalar imperiyasi',
                     'Boburiylar davlati',
                     'Sikh imperiyasi (Maharaja Ranjit Singx, Panjob)',
                     'Durroniylar imperiyasi'],
              'ru': ['Империя Маратха',
                     'Империя Великих Моголов',
                     'Сикхская империя (махараджа Ранджит Сингх, Пенджаб)',
                     'Дурранийская империя'],
              'en': ['Maratha Empire',
                     'Mughal Empire',
                     'Sikh Empire (Maharaja Ranjit Singh, Punjab)',
                     'Durrani Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Sikh imperiyasi (Maharaja Ranjit Singx, Panjob)',
                     'ru': 'Сикхская империя (махараджа Ранджит Сингх, Пенджаб)',
                     'en': 'Sikh Empire (Maharaja Ranjit Singh, Punjab)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Sikh_Empire_1839.png/1024px-Sikh_Empire_1839.png',
  'fun_fact': {'uz': 'Ranjit Singx poytaxt Lohurda mustaqil va qudratli davlat tuzib, Panjob, Kashmir va Peshovarni '
                     'birlashtirgan.',
               'ru': 'Сикхское государство со столицей в Лахоре обладало европейски обученной армией и было последним '
                     'покорено британцами в Индии.',
               'en': 'Centered on Lahore under Maharaja Ranjit Singh, the Sikh Empire dominated the Punjab until '
                     'annexed by Britain in 1849.'},
  'aliases': ['sixlar', 'six imperiyasi', 'ranjit singx', 'сикхи', 'сикхская империя', 'sikh empire']},
 {'id': 'hist_map_096',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Sparta davlati',
                     'Afina dengiz ittifoqi',
                     'Epir podsholigi',
                     'Qadimgi Makedoniya qirolligi (Filipp II davri)'],
              'ru': ['Спарта', 'Афинский морской союз', 'Царство Эпир', 'Древняя Македония (эпоха Филиппа II)'],
              'en': ['Sparta', 'Delian League', 'Kingdom of Epirus', 'Ancient Kingdom of Macedonia (Philip II)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Qadimgi Makedoniya qirolligi (Filipp II davri)',
                     'ru': 'Древняя Македония (эпоха Филиппа II)',
                     'en': 'Ancient Kingdom of Macedonia (Philip II)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Kingdom_of_Macedon_336_BC.png/1024px-Kingdom_of_Macedon_336_BC.png',
  'fun_fact': {'uz': 'Filipp II mashhur makedon falangasini va 6 metrlik sarissalarni joriy qilib, butun Yunonistonni '
                     'Korinf ittifoqiga birlashtirgan.',
               'ru': 'Филипп II создал несокрушимую македонскую фалангу, подчинив греческие полисы и подготовив походы '
                     'своего сына Александра.',
               'en': 'Philip II reformed Macedonian infantry into the 18-foot sarissa phalanx, unifying Greece under '
                     'the League of Corinth.'},
  'aliases': ['makedoniya', 'filipp ii', 'македония', 'филипп ii', 'macedon', 'philip ii']},
 {'id': 'hist_map_097',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ["Jung'or xonligi (Oyratlar davlati)", 'Qalmoq xonligi', 'Qozoq xonligi', "Mo'g'uliston xonligi"],
              'ru': ['Джунгарское ханство (Ойратское государство)',
                     'Калмыцкое ханство',
                     'Казахское ханство',
                     'Монгольское ханство'],
              'en': ['Dzungar Khanate (Oirat Mongol State)', 'Kalmyk Khanate', 'Kazakh Khanate', 'Northern Yuan']},
  'correct_index': 0,
  'correct_answer': {'uz': "Jung'or xonligi (Oyratlar davlati)",
                     'ru': 'Джунгарское ханство (Ойратское государство)',
                     'en': 'Dzungar Khanate (Oirat Mongol State)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Dzungar_Khanate_1750.png/1024px-Dzungar_Khanate_1750.png',
  'fun_fact': {'uz': "Jung'or xonligi tarixdagi so'nggi yirik ko'chmanchi dasht imperiyasi bo'lib, Sin imperiyasi "
                     'bilan shiddatli urushlar olib borgan.',
               'ru': 'Джунгары создали последнюю великую кочевую империю Евразии, занимавшую земли современного '
                     'Синьцзяна и Казахстана.',
               'en': 'The Dzungar Khanate was the last nomadic steppe empire in history, falling to the Qing Empire in '
                     'the 1750s.'},
  'aliases': ['jungor', 'jungor xonligi', 'oyratlar', 'джунгары', 'джунгарское ханство', 'dzungar', 'dzungar khanate']},
 {'id': 'hist_map_098',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Volga Bulgariyasi',
                     "Xazar xoqonligi (Volga va Kaspiy bo'yi)",
                     'Pecheneglar ittifoqi',
                     'Avar xoqonligi'],
              'ru': ['Волжская Булгария',
                     'Хазарский каганат (Поволжье и Подонье)',
                     'Печенежский союз',
                     'Аварский каганат'],
              'en': ['Volga Bulgaria', 'Khazar Khaganate (Volga and Caspian Steppes)', 'Pechenegs', 'Avar Khaganate']},
  'correct_index': 1,
  'correct_answer': {'uz': "Xazar xoqonligi (Volga va Kaspiy bo'yi)",
                     'ru': 'Хазарский каганат (Поволжье и Подонье)',
                     'en': 'Khazar Khaganate (Volga and Caspian Steppes)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Khazar_Khaganate_820_CE.png/1024px-Khazar_Khaganate_820_CE.png',
  'fun_fact': {'uz': "Xazarlar poytaxt Itil shahrida Ipak yo'lining shimoliy tarmog'ini nazorat qilgan va hukmdor "
                     'elita iudaizm (yahudiylik) dinini qabul qilgan.',
               'ru': 'Хазарский каганат со столицей в Итиле был могущественным торговым государством, верхушка '
                     'которого приняла иудаизм.',
               'en': 'The semi-nomadic Turkic Khazars controlled the northern trade between Byzantium, the Caliphate, '
                     'and Rus, converting to Judaism.'},
  'aliases': ['xazar xoqonligi', 'xazarlar', 'хазары', 'хазарский каганат', 'khazar', 'khazar khaganate']},
 {'id': 'hist_map_099',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Xunlar imperiyasi',
                     'Venger qirolligi',
                     'Avar xoqonligi (Pannoniya / Markaziy Yevropa)',
                     "Bulg'or podsholigi"],
              'ru': ['Империя гуннов',
                     'Венгерское королевство',
                     'Аварский каганат (Паннония / Центральная Европа)',
                     'Первое Болгарское царство'],
              'en': ['Hunnic Empire',
                     'Kingdom of Hungary',
                     'Avar Khaganate (Pannonian Basin)',
                     'First Bulgarian Empire']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Avar xoqonligi (Pannoniya / Markaziy Yevropa)',
                     'ru': 'Аварский каганат (Паннония / Центральная Европа)',
                     'en': 'Avar Khaganate (Pannonian Basin)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Avar_Khaganate_600_CE.png/1024px-Avar_Khaganate_600_CE.png',
  'fun_fact': {'uz': 'Avarlar Yevropaga temir uzangini olib kelgan va 626 yilda forslar bilan birgalikda '
                     'Konstantinopolni qamal qilgan.',
               'ru': 'Авары господствовали в Дунайском бассейне более двух веков, познакомив Европу со стременем, пока '
                     'не были разбиты Карлом Великим.',
               'en': 'The Avars dominated the Danube basin from 567 to 804 AD, bringing stirrups to Europe before '
                     'defeat by Charlemagne.'},
  'aliases': ['avarlar', 'avar xoqonligi', 'авары', 'аварский каганат', 'avar', 'avar khaganate']},
 {'id': 'hist_map_100',
  'sub_mode': 'empire_maps',
  'question': {'uz': "Xaritada ko'rsatilgan hududlar qaysi buyuk imperiya yoki davlatga tegishli?",
               'ru': 'Территория какой великой империи или государства показана на карте?',
               'en': 'Which great empire or state territory is shown on this map?'},
  'options': {'uz': ['Granada amirligi',
                     'Murobitlar davlati',
                     'Muvahhidlar davlati',
                     'Qurtuba (Kordova) xalifaligi (Andalusiya)'],
              'ru': ['Гранадский эмират',
                     'Государство Альморавидов',
                     'Государство Альмохадов',
                     'Кордовский халифат (Аль-Андалус)'],
              'en': ['Emirate of Granada', 'Almoravid State', 'Almohad State', 'Caliphate of Córdoba (Al-Andalus)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Qurtuba (Kordova) xalifaligi (Andalusiya)',
                     'ru': 'Кордовский халифат (Аль-Андалус)',
                     'en': 'Caliphate of Córdoba (Al-Andalus)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Caliphate_of_Cordoba_1000.png/1024px-Caliphate_of_Cordoba_1000.png',
  'fun_fact': {'uz': 'Abdurahmon III davrida Qurtuba 500 000 aholiga ega Yevropaning eng boy madaniy va ilmiy shahriga '
                     'aylangan (Kordova jome masjidi — Mezquita qurilgan).',
               'ru': 'Кордовский халифат был светочем европейской науки и терпимости в X веке, где сосуществовали '
                     'мусульмане, христиане и иудеи.',
               'en': "Under Abd al-Rahman III, the Caliphate of Córdoba made Islamic Iberia Europe's foremost "
                     'intellectual and cultural powerhouse.'},
  'aliases': ['qurtuba', 'kordova xalifaligi', 'кордовский халифат', 'аль-андалус', 'cordoba', 'caliphate of cordoba']},
 {'id': 'hist_who_001',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 1336 yilda Kesh (Shahrisabz) yaqinidagi Xo'ja Ilg'or qishlog'ida tug'ilganman.\n"
                     "2-maslahat: 'Kuch — adolatdadir' shiorini davlatimning asosiy tamoyili qilib belgilaganman.\n"
                     '3-maslahat: Butun hayotim davomida biror marta ham jangda yengilmagan buyuk Sohibqironman.',
               'ru': 'Подсказка 1: Родился в 1336 году близ Кеша (Шахрисабза).\n'
                     'Подсказка 2: Сделал девизом своего правления «Справедливость — основа государства».\n'
                     'Подсказка 3: Не проиграл ни одного сражения, создал великую империю со столицей в Самарканде.',
               'en': 'Clue 1: Born in 1336 near Shahrisabz in Central Asia.\n'
                     "Clue 2: My royal motto was 'Strength is in Justice'.\n"
                     'Clue 3: Undefeated commander and founder of the Timurid Empire with its capital in Samarkand.'},
  'options': {'uz': ['Amir Temur (Sohibqiron)', 'Chingizxon', "Mirzo Ulug'bek", 'Zahiriddin Muhammad Bobur'],
              'ru': ['Амир Темур (Тамерлан)', 'Чингисхан', 'Мирзо Улугбек', 'Захириддин Мухаммад Бабур'],
              'en': ['Amir Timur (Tamerlane)', 'Genghis Khan', 'Mirzo Ulugbek', 'Babur']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Amir Temur (Sohibqiron)', 'ru': 'Амир Темур (Тамерлан)', 'en': 'Amir Timur (Tamerlane)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Timur_reconstruction03.jpg/640px-Timur_reconstruction03.jpg',
  'fun_fact': {'uz': "Amir Temur Samarqandni jahonning eng go'zal shahriga aylantirgan va uning 'Temur tuzuklari' "
                     "asari davlat boshqaruvi bo'yicha nodir qo'llanmadir.",
               'ru': 'Тамерлан превратил Самарканд в архитектурную жемчужину Востока, возведя соборную мечеть '
                     'Биби-Ханым и мавзолей Гур-Эмир.',
               'en': 'Amir Timur never lost a battle in 35 years of campaigns and codified his statecraft in the '
                     "'Tuzuk-i Timuri'."},
  'aliases': ['amir temur', 'temur', 'tamerlan', 'tamerlane', 'sohibqiron', 'амир темур', 'тамерлан']},
 {'id': 'hist_who_002',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Arastu (Aristotel) mening shaxsiy ustozim bo'lgan va mashhur Bukefal laqabli otim "
                     'bor edi.\n'
                     '2-maslahat: Gordiy tugunini qilichim bilan kesib tashlaganman va Gavgamela jangida forslarni '
                     "mag'lub etganman.\n"
                     '3-maslahat: 32 yoshimda Bobilda vafot etgunimcha Gretsiyadan Hindistongacha ulkan imperiya '
                     'tuzdim.',
               'ru': 'Подсказка 1: Моим учителем был философ Аристотель, а коня звали Буцефал.\n'
                     'Подсказка 2: Разрубил мечом Гордиев узел и сокрушил персидского царя Дария III.\n'
                     'Подсказка 3: Создал гигантскую империю от Греции до реки Инд и умер в Вавилоне в 32 года.',
               'en': 'Clue 1: Tutored by Aristotle, my famed warhorse was Bucephalus.\n'
                     'Clue 2: I cut the Gordian Knot and defeated Darius III at Gaugamela.\n'
                     'Clue 3: I conquered from Greece to India, dying undefeated in Babylon at age 32.'},
  'options': {'uz': ['Yuliy Sezar', 'Aleksandr Makedonskiy (Iskandar Zulqarnayn)', 'Filipp II', 'Pirr'],
              'ru': ['Юлий Цезарь', 'Александр Македонский (Великий)', 'Филипп II', 'Пирр'],
              'en': ['Julius Caesar', 'Alexander the Great', 'Philip II', 'Pyrrhus of Epirus']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Aleksandr Makedonskiy (Iskandar Zulqarnayn)',
                     'ru': 'Александр Македонский (Великий)',
                     'en': 'Alexander the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/AlexanderTheGreat_Bust.jpg/640px-AlexanderTheGreat_Bust.jpg',
  'fun_fact': {'uz': "Aleksandr o'zi zabt etgan hududlarda 70 dan ortiq shaharga o'z nomini (Iskandariya) bergan, "
                     'shulardan eng mashhuri Misrdagi Iskandariyadir.',
               'ru': 'Александр основал свыше 70 городов, названных в его честь Александриями, а также один в честь '
                     'своего коня Буцефала.',
               'en': 'Alexander founded over 70 cities bearing his name, including Alexandria in Egypt and Bucephala '
                     'named for his horse.'},
  'aliases': ['aleksandr', 'aleksandr makedonskiy', 'iskandar', 'александр македонский', 'alexander the great']},
 {'id': 'hist_who_003',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Galliyani zabt etib, 'Veni, vidi, vici' (Keldim, ko'rdim, g'alaba qozondim) deb "
                     'yozganman.\n'
                     "2-maslahat: Rubikon daryosidan o'tayotib 'Qur'a tashlandi' (Alea iacta est) degan mashhur "
                     'iborani aytganman.\n'
                     "3-maslahat: Mil. avv. 44 yil 15 martda Senatda o'z yaqinim Brut va fitnachilar tomonidan 23 "
                     "marta xanjar urib o'ldirilganman.",
               'ru': 'Подсказка 1: Покорил Галлию и произнес крылатые слова «Пришел, увидел, победил».\n'
                     'Подсказка 2: Перешел Рубикон со словами «Жребий брошен», начав гражданскую войну.\n'
                     'Подсказка 3: Был убит заговорщиками в сенате в мартовские иды 44 года до н.э. со словами «И ты, '
                     'Брут?»',
               'en': "Clue 1: Conquered Gaul and famously reported: 'Veni, vidi, vici'.\n"
                     "Clue 2: Crossed the Rubicon declaring 'The die is cast' (Alea iacta est).\n"
                     'Clue 3: Assassinated on the Ides of March in 44 BC by Roman senators including Brutus.'},
  'options': {'uz': ['Oktavian Avgust', 'Mark Antoniy', 'Yuliy Sezar', 'Neron'],
              'ru': ['Октавиан Август', 'Марк Антоний', 'Юлий Цезарь', 'Нерон'],
              'en': ['Augustus', 'Mark Antony', 'Julius Caesar', 'Nero']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Yuliy Sezar', 'ru': 'Юлий Цезарь', 'en': 'Julius Caesar'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Retrato_de_Julio_C%C3%A9sar_%282672409310%29.jpg/640px-Retrato_de_Julio_C%C3%A9sar_%282672409310%29.jpg',
  'fun_fact': {'uz': "Yuliy Sezar Yulian taqvimini joriy qilgan va iyul oyi uning sharafiga 'July' deb atalgan; "
                     "'Kayser' va 'Tsar' unvonlari ham uning nomidan olingan.",
               'ru': 'Имя Цезаря стало титулом монархов (кайзер, царь), а месяц июль назван в честь его дня рождения.',
               'en': 'Caesar reformed the Roman calendar, giving his name to July; the royal titles Kaiser and Czar '
                     'both derive from his name.'},
  'aliases': ['yuliy sezar', 'sezar', 'цезарь', 'юлий цезарь', 'julius caesar', 'caesar']},
 {'id': 'hist_who_004',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Bolalikdagi ismim Temuchin bo'lib, Onon daryosi bo'yida tug'ilganman.\n"
                     "2-maslahat: Ko'chmanchi qabilalarni birlashtirib, 'Buyuk Yasa' qonunlar to'plamini yaratdim.\n"
                     "3-maslahat: Tinch okeanidan Kaspiygacha cho'zilgan tarixdagi eng ulkan quruqlik imperiyasiga "
                     'asos soldim.',
               'ru': 'Подсказка 1: Мое имя при рождении — Темуджин, родился в степях у реки Онон.\n'
                     'Подсказка 2: Создал кодекс законов «Великая Яса» и объединил кочевые народы.\n'
                     'Подсказка 3: Основатель Монгольской империи, величайший завоеватель в истории степей.',
               'en': 'Clue 1: Born Temüjin on the banks of the Onon River.\n'
                     "Clue 2: Promulgated the legal code 'Yassa' and unified nomadic steppe tribes.\n"
                     "Clue 3: Proclaimed Genghis Khan in 1206, founding history's largest contiguous empire."},
  'options': {'uz': ['Botuxon', 'Xubilayxon', "O'qtoyxon", 'Chingizxon (Temuchin)'],
              'ru': ['Батый', 'Хубилай', 'Угэдэй', 'Чингисхан (Темуджин)'],
              'en': ['Batu Khan', 'Kublai Khan', 'Ogedei Khan', 'Genghis Khan (Temüjin)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Chingizxon (Temuchin)', 'ru': 'Чингисхан (Темуджин)', 'en': 'Genghis Khan (Temüjin)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/YuanGenghisKhan.jpg/640px-YuanGenghisKhan.jpg',
  'fun_fact': {'uz': "Chingizxonning dafn qilingan joyi qat'iy sir tutilgan: afsonaga ko'ra, qabr ustidan daryo "
                     'oqizilgan yoki minglab otlar bilan toptalgan.',
               'ru': 'Место захоронения Чингисхана до сих пор остается неразгаданной тайной: всех свидетелей '
                     'погребения умертвили.',
               'en': 'The exact tomb of Genghis Khan has never been discovered; legend says a river was diverted over '
                     'it to conceal its location.'},
  'aliases': ['chingizxon', 'temuchin', 'чингисхан', 'темуджин', 'genghis khan', 'temujin']},
 {'id': 'hist_who_005',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Xorazmshoh Aloviddin Muhammadning to'ng'ich o'g'li bo'lib, yuzimdagi xol sababli "
                     "'Manguberdi' deb atalganman.\n"
                     "2-maslahat: Parvon jangida mo'g'ul qo'shinlarini tor-mor keltirib, ularga ilk qaqshatqich "
                     'zarbani berganman.\n'
                     "3-maslahat: Sind daryosi bo'yidagi jasoratimni ko'rib Chingizxonning o'zi tan bergan o'zbek "
                     'xalqining milliy qahramoniman.',
               'ru': 'Подсказка 1: Старший сын хорезмшаха Ала ад-Дина Мухаммеда, названный «Мангуберди» из-за родинки '
                     'на лице.\n'
                     'Подсказка 2: Нанес сокрушительное поражение монголам в битве при Парване в 1221 году.\n'
                     'Подсказка 3: Прыгнул на коне в бурные воды реки Инд, вызвав искреннее восхищение Чингисхана.',
               'en': 'Clue 1: Eldest son of Khwarazmshah Ala ad-Din Muhammad, nicknamed for a distinctive birthmark.\n'
                     'Clue 2: Inflicted the first major defeat on the Mongols at the Battle of Parwan in 1221.\n'
                     'Clue 3: Leaped into the raging Indus on horseback, earning the respect of his foe Genghis Khan.'},
  'options': {'uz': ['Jaloliddin Manguberdi', 'Najmiddin Kubro', 'Temur Malik', 'Mahmud Torobiy'],
              'ru': ['Джалолиддин Мангуберди', 'Наджмиддин Кубра', 'Темур Малик', 'Махмуд Тороби'],
              'en': ['Jaloliddin Manguberdi', 'Najm al-Din Kubra', 'Temur Malik', 'Mahmud Tarabi']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Jaloliddin Manguberdi', 'ru': 'Джалолиддин Мангуберди', 'en': 'Jaloliddin Manguberdi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Jaloliddin_Manguberdi_monument.jpg/640px-Jaloliddin_Manguberdi_monument.jpg',
  'fun_fact': {'uz': "Jaloliddin 10 yil davomida (1221-1231) mo'g'ul bosqinchilariga qarshi tinimsiz kurashib, ozodlik "
                     'va mardlik timsoliga aylandi.',
               'ru': 'Джалолиддин Мангуберди почитается в Узбекистане как национальный герой, боровшийся за '
                     'независимость родины.',
               'en': 'For a decade, Jaloliddin waged unrelenting resistance against Mongol conquest, celebrated as '
                     "Uzbekistan's hero of liberty."},
  'aliases': ['jaloliddin manguberdi', 'manguberdi', 'джалолиддин мангуберди', 'мангуберди', 'jaloliddin']},
 {'id': 'hist_who_006',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 1483 yilda Andijonda tug'ilganman, 12 yoshimda Farg'ona taxtiga o'tirganman.\n"
                     "2-maslahat: 'Boburnoma' nomli qomusiy memuar asar va nozik g'azallar, ruboiylar yozganman.\n"
                     "3-maslahat: 1526 yilda Panipat jangida g'alaba qozonib, Hindistonda Boburiylar saltanatiga asos "
                     'soldim.',
               'ru': 'Подсказка 1: Родился в Андижане в 1483 году, унаследовал трон Ферганы в 12 лет.\n'
                     'Подсказка 2: Автор всемирно известной автобиографической книги «Бабур-наме» и изящных стихов.\n'
                     'Подсказка 3: Основатель империи Великих Моголов в Индии после победы при Панипате.',
               'en': "Clue 1: Born in Andijan in 1483, ascending Fergana's throne at age twelve.\n"
                     "Clue 2: Penned the celebrated autobiography 'Baburnama' and exquisite lyric poetry.\n"
                     'Clue 3: Founded the Mughal Empire in India after winning the Battle of Panipat in 1526.'},
  'options': {'uz': ['Alisher Navoiy', 'Zahiriddin Muhammad Bobur', "Mirzo Ulug'bek", 'Humoyun Mirzo'],
              'ru': ['Алишер Навои', 'Захириддин Мухаммад Бабур', 'Мирзо Улугбек', 'Хумаюн'],
              'en': ['Alisher Navoi', 'Zahiriddin Muhammad Babur', 'Mirzo Ulugbek', 'Humayun']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Zahiriddin Muhammad Bobur',
                     'ru': 'Захириддин Мухаммад Бабур',
                     'en': 'Zahiriddin Muhammad Babur'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Babur_portrait.jpg/640px-Babur_portrait.jpg',
  'fun_fact': {'uz': 'Bobur nafaqat buyuk sarkarda va davlat arbobi, balki nozik tabiatli shoir, botanik, geograf va '
                     "'Xatti Boburiy' yozuvining ixtirochisi edi.",
               'ru': 'Бабур сочетал талант полководца с даром поэта и натуралиста, подробно описав флору и фауну Индии '
                     'в «Бабур-наме».',
               'en': "Babur was an avid naturalist and poet who invented a script ('Khatt-i Baburi') and detailed "
                     'Asian flora in his memoirs.'},
  'aliases': ['bobur', 'zahiriddin muhammad bobur', 'бабур', 'захириддин бабур', 'babur']},
 {'id': 'hist_who_007',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Amir Temurning suyukli nabirasi bo'lib, 1409 yildan 40 yil Samarqandni boshqardim.\n"
                     '2-maslahat: Registon maydonida birinchi mahobatli madrasani qurdirdim.\n'
                     "3-maslahat: Samarqand rasadxonasini barpo etib, 1018 ta yulduz harakatini o'z ichiga olgan 'Ziji "
                     "Jadidi Ko'ragoniy'ni yaratdim.",
               'ru': 'Подсказка 1: Внук Амира Темура, правивший Самаркандом сорок лет.\n'
                     'Подсказка 2: Построил знаменитое медресе на площади Регистан.\n'
                     'Подсказка 3: Великий астроном, создавший обсерваторию и каталог 1018 звезд «Зидж Гурагони».',
               'en': 'Clue 1: Grandson of Amir Timur, ruling Samarkand for forty years from 1409.\n'
                     'Clue 2: Built the first monumental madrasah on Registan Square.\n'
                     'Clue 3: Famed astronomer-king who built the Samarkand Observatory and charted 1,018 stars.'},
  'options': {'uz': ['Shohruh Mirzo', 'Husayn Boyqaro', "Mirzo Ulug'bek", 'Qozizoda Rumiy'],
              'ru': ['Шахрух Мирзо', 'Хусейн Байкара', 'Мирзо Улугбек', 'Казы-заде ар-Руми'],
              'en': ['Shahrukh Mirza', 'Husayn Bayqara', 'Mirzo Ulugbek', 'Qadi Zada al-Rumi']},
  'correct_index': 2,
  'correct_answer': {'uz': "Mirzo Ulug'bek", 'ru': 'Мирзо Улугбек', 'en': 'Mirzo Ulugbek'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Ulugh_Beg_statue_Samarkand.jpg/640px-Ulugh_Beg_statue_Samarkand.jpg',
  'fun_fact': {'uz': "Ulug'bek hisoblab chiqqan bir yilning davomiyligi (365 kun, 6 soat, 10 daqiqa, 8 soniya) "
                     'zamonaviy hisob-kitobdan atigi 58 soniyaga farq qiladi.',
               'ru': 'Звездный год Улугбека отличался от современных расчетов всего на 58 секунд, что является чудом '
                     'науки XV века.',
               'en': 'Ulugbek calculated the sidereal year with an error of only 58 seconds compared to modern atomic '
                     'clock measurements.'},
  'aliases': ['ulugbek', 'mirzo ulugbek', 'улугбек', 'мирзо улугбек', 'ulugh beg', 'mirzo ulughbeg']},
 {'id': 'hist_who_008',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Ahamoniylar saltanatiga asos solgan forslar shohiman.\n'
                     '2-maslahat: Bobilni mil. avv. 539 yilda egallab, asirlikdagi yahudiylarga Quddusga qaytishga '
                     'ijozat berdim.\n'
                     "3-maslahat: Massagetlar malikasi To'maris bilan jangda halok bo'lganman.",
               'ru': 'Подсказка 1: Основатель державы Ахеменидов, объединивший персов и мидян.\n'
                     'Подсказка 2: Захватил Вавилон и издал глиняный цилиндр с признанием религиозных свобод.\n'
                     'Подсказка 3: Погиб в битве против царицы массагетов Томирис.',
               'en': 'Clue 1: Founder of the First Persian (Achaemenid) Empire.\n'
                     'Clue 2: Conquered Babylon in 539 BC and freed Jewish captives to rebuild their Temple.\n'
                     'Clue 3: Died in battle against the Massagetae warrior Queen Tomyris.'},
  'options': {'uz': ['Doro I', 'Kserks I', 'Kambiz II', 'Buyuk Kir II (Kavush)'],
              'ru': ['Дарий I', 'Ксеркс I', 'Камбис II', 'Кир II Великий'],
              'en': ['Darius the Great', 'Xerxes I', 'Cambyses II', 'Cyrus the Great']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Buyuk Kir II (Kavush)', 'ru': 'Кир II Великий', 'en': 'Cyrus the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Cyrus_the_Great_Olympic_Park.jpg/640px-Cyrus_the_Great_Olympic_Park.jpg',
  'fun_fact': {'uz': "Buyuk Kir qabrida qoldirilgan yozuv: 'Ey inson, men Kirman, forslarga imperiya berganman. Menga "
                     "bu bir parcha tuproqni ko'p ko'rma!' bo'lgan.",
               'ru': 'Гробница Кира Великого в Пасаргадах сохранилась до наших дней и является объектом Всемирного '
                     'наследия ЮНЕСКО.',
               'en': "Cyrus's tomb at Pasargadae was spared by Alexander the Great out of profound respect for his "
                     'statecraft.'},
  'aliases': ['kir', 'kir ii', 'buyuk kir', 'кир великий', 'кир ii', 'cyrus the great', 'cyrus']},
 {'id': 'hist_who_009',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Karfagenlik sarkardaman, bolaligimda Rimga abadiy nafrat saqlashga qasam ichganman.\n'
                     "2-maslahat: Urush fillari bilan qorli Alp tog'larini oshib o'tib, Rim yuragiga kutilmagan zarba "
                     'berdim.\n'
                     "3-maslahat: Kanna jangida (mil. avv. 216) o'zimdan ikki barobar katta Rim armiyasini qopqonga "
                     'tushirib qirib tashladim.',
               'ru': 'Подсказка 1: Полководец Карфагена, давший в детстве «Ганнибалову клятву» вечной вражды к Риму.\n'
                     'Подсказка 2: Совершил беспримерный переход через заснеженные Альпы с боевыми слонами.\n'
                     'Подсказка 3: Одержал легендарную победу при Каннах, окружив вдвое превосходящую римскую армию.',
               'en': 'Clue 1: Carthaginian commander who swore eternal hostility to Rome as a boy.\n'
                     'Clue 2: Marched war elephants across the snowy Alps into the heart of Italy.\n'
                     'Clue 3: Masterminded the ultimate double-envelopment victory at Cannae in 216 BC.'},
  'options': {'uz': ['Gannibal Barka', 'Gamilkar Barka', 'Sitsipion Afrikalik', 'Pirr'],
              'ru': ['Ганнибал Барка', 'Гамилькар Барка', 'Сципион Африканский', 'Пирр'],
              'en': ['Hannibal Barca', 'Hamilcar Barca', 'Scipio Africanus', 'Pyrrhus']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Gannibal Barka', 'ru': 'Ганнибал Барка', 'en': 'Hannibal Barca'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Hannibal_Bust.jpg/640px-Hannibal_Bust.jpg',
  'fun_fact': {'uz': "Gannibalning Kanna jangidagi taktikasi (markazni orqaga chekintirib, qanotlardan o'rab olish) "
                     "bugungi kunda ham barcha harbiy akademiyalarda o'rganiladi.",
               'ru': 'Тактическое окружение римлян при Каннах считается непревзойденной классикой военного искусства.',
               'en': "Hannibal's tactical encirclement at Cannae remains the gold standard of military envelopment "
                     'taught in academies today.'},
  'aliases': ['gannibal', 'gannibal barka', 'ганнибал', 'ганнибал барка', 'hannibal', 'hannibal barca']},
 {'id': 'hist_who_010',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Ayyubiylar sulolasiga asos solgan kurd millatiga mansub buyuk sarkardaman.\n'
                     '2-maslahat: 1187 yilda Xittin jangida salibchilarni tor-mor qildim.\n'
                     "3-maslahat: 88 yillik salibchilar hukmronligidan so'ng Quddusni ozod etdim va dushmanlarimga ham "
                     "marhamat ko'rsatdim.",
               'ru': 'Подсказка 1: Основатель династии Айюбидов, султан Египта и Сирии.\n'
                     'Подсказка 2: Разгромил войско крестоносцев в битве при Хаттине в 1187 году.\n'
                     'Подсказка 3: Отвоевал Иерусалим у крестоносцев, проявив поразительное рыцарское благородство.',
               'en': 'Clue 1: Kurdish founder of the Ayyubid Sultanate ruling Egypt and Syria.\n'
                     'Clue 2: Crushed the Crusader field army at the Horns of Hattin in 1187.\n'
                     'Clue 3: Recaptured Jerusalem after 88 years of Crusader rule, famed for his chivalry.'},
  'options': {'uz': ['Nuriddin Zangiy', 'Salohiddin Ayyubiy (Saladin)', 'Boybars', 'Alp Arslon'],
              'ru': ['Нур ад-Дин Занги', 'Салах ад-Дин (Саладин)', 'Бейбарс', 'Алп-Арслан'],
              'en': ['Nur ad-Din', 'Saladin (Salah ad-Din)', 'Baibars', 'Alp Arslan']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Salohiddin Ayyubiy (Saladin)',
                     'ru': 'Салах ад-Дин (Саладин)',
                     'en': 'Saladin (Salah ad-Din)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Saladin_statue_Damascus.jpg/640px-Saladin_statue_Damascus.jpg',
  'fun_fact': {'uz': 'Salohiddin Quddusni egallagach, xristian aholini qirmasdan, ularga shahar xavfsizligini '
                     "kafolatladi va Richard Sheryurak betob bo'lganida unga meva va tabib yubordi.",
               'ru': 'Саладин прославился в Европе рыцарским милосердием: он не тронул христианских святынь и посылал '
                     'лед больному Ричарду Львиное Сердце.',
               'en': "Saladin spared Jerusalem's Christian population and sent his personal physician and fresh fruit "
                     'to his rival, Richard the Lionheart.'},
  'aliases': ['salohiddin', 'salohiddin ayyubiy', 'саладин', 'салах ад-дин', 'saladin']},
 {'id': 'hist_who_011',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Korsika orolida tug'ilganman va artilleriya zobiti sifatida harbiy faoliyatimni "
                     'boshlaganman.\n'
                     "2-maslahat: Austerlits jangida g'alaba qozonib, butun kontinental Yevropani bo'ysundirdim va "
                     "'Fuqarolik kodeksi'ni tuzdim.\n"
                     "3-maslahat: 1812 yilda Rossiyada chekinishga majbur bo'lib, 1815 yilda Vaterlooda mag'lub "
                     "bo'ldim va Muqaddas Yelena orolida vafot etdim.",
               'ru': 'Подсказка 1: Родился на Корсике, начал военную карьеру офицером-артиллеристом.\n'
                     'Подсказка 2: Создал «Кодекс Наполеона» и разбил армии коалиций при Аустерлице.\n'
                     'Подсказка 3: Французский император, потерпевший крах при Ватерлоо и закончивший дни на острове '
                     'Святой Елены.',
               'en': 'Clue 1: Born in Corsica, rising from an artillery officer to national leadership.\n'
                     'Clue 2: Introduced the Napoleonic Code and won his tactical masterpiece at Austerlitz.\n'
                     'Clue 3: Emperor of France who was finally defeated at Waterloo and exiled to Saint Helena.'},
  'options': {'uz': ['Lyudovik XIV', 'Napoleon III', 'Napoleon Bonapart', 'Gersog Vellington'],
              'ru': ['Людовик XIV', 'Наполеон III', 'Наполеон I Бонапарт', 'Герцог Веллингтон'],
              'en': ['Louis XIV', 'Napoleon III', 'Napoleon Bonaparte', 'Duke of Wellington']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Napoleon Bonapart', 'ru': 'Наполеон I Бонапарт', 'en': 'Napoleon Bonaparte'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project.jpg/640px-Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project.jpg',
  'fun_fact': {'uz': "Napoleon o'zining harbiy g'alabalaridan ko'ra Fuqarolik kodeksini yuqori baholagan: 'Mening "
                     "haqiqiy shon-sharafim 40 ta g'alaba qozongan janglarimda emas, balki hech qachon o'chmaydigan "
                     "Kodeksimdadir'.",
               'ru': 'Наполеон считал своим главным памятником Гражданский кодекс, легший в основу правовых систем '
                     'десятков стран мира.',
               'en': 'Napoleon considered his Civil Code his greatest monument, observing that it would outlive all '
                     'forty of his battlefield victories.'},
  'aliases': ['napoleon', 'napoleon bonapart', 'наполеон', 'наполеон бонапарт', 'napoleon bonaparte']},
 {'id': 'hist_who_012',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Ptolemeylar sulolasidan bo'lgan Misrning so'nggi hukmdoriman.\n"
                     '2-maslahat: Yuliy Sezar va keyinchalik Mark Antoniy bilan siyosiy va shaxsiy ittifoq tuzganman.\n'
                     "3-maslahat: Aksiy jangidagi mag'lubiyatdan so'ng Oktavian qo'liga tushmaslik uchun ilon zahri "
                     'bilan jonimga qasd qildim.',
               'ru': 'Подсказка 1: Последняя царица эллинистического Египта из династии Птолемеев.\n'
                     'Подсказка 2: Очаровала Юлия Цезаря и Марка Антония, борясь за независимость Египта.\n'
                     'Подсказка 3: Покончила с собой после поражения при Акциуме, чтобы не идти пленницей в триумфе '
                     'Октавиана.',
               'en': 'Clue 1: The last active ruler of the Ptolemaic Kingdom of Egypt.\n'
                     'Clue 2: Allied politically and romantically with Julius Caesar and Mark Antony.\n'
                     "Clue 3: Committed suicide following the Battle of Actium rather than parade as Octavian's "
                     'captive.'},
  'options': {'uz': ['Nefertiti', 'Xatshepsut', 'Zenobiya', 'Kleopatra VII Filopator'],
              'ru': ['Нефертити', 'Хатшепсут', 'Зенобия', 'Клеопатра VII Филопатор'],
              'en': ['Nefertiti', 'Hatshepsut', 'Zenobia', 'Cleopatra VII Philopator']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Kleopatra VII Filopator',
                     'ru': 'Клеопатра VII Филопатор',
                     'en': 'Cleopatra VII Philopator'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kleopatra-VII.-Altes-Museum-Berlin1.jpg/640px-Kleopatra-VII.-Altes-Museum-Berlin1.jpg',
  'fun_fact': {'uz': "Kleopatra o'z sulolasida misr tilini o'rgangan yagona hukmdor bo'lib, jami 9 ta xorijiy tilda "
                     "erkin so'zlashgan va chuqur bilimga ega bo'lgan.",
               'ru': 'Клеопатра была блестяще образована, говорила на девяти языках и первой из династии Птолемеев '
                     'выучила древнеегипетский язык.',
               'en': 'Cleopatra spoke at least nine languages and was the only Ptolemaic monarch who bothered to learn '
                     'the Egyptian tongue.'},
  'aliases': ['kleopatra', 'kleopatra vii', 'клеопатра', 'cleopatra']},
 {'id': 'hist_who_013',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Qadimgi Misrning 19-sulolasiga mansub fir'avnman, 66 yil hukmronlik qilganman.\n"
                     "2-maslahat: Mil. avv. 1274 yilda xettlar bilan mashhur Kadesh jangida to'qnashdim.\n"
                     '3-maslahat: Abu-Simbel qoya ibodatxonasini va Luksordagi mahobatli inshootlarni barpo etdim.',
               'ru': 'Подсказка 1: Фараон XIX династии, правивший Древним Египтом рекордные 66 лет.\n'
                     'Подсказка 2: Сражался с хеттами в грандиозной битве при Кадеше.\n'
                     'Подсказка 3: Построил колоссальные храмы Абу-Симбел и заупокойный храм Рамессеум.',
               'en': 'Clue 1: 19th-Dynasty pharaoh who ruled Egypt for an extraordinary 66 years.\n'
                     'Clue 2: Fought the Hittites in the massive chariot clash at Kadesh in 1274 BC.\n'
                     'Clue 3: Commissioned the colossal rock temples of Abu Simbel and the Ramesseum.'},
  'options': {'uz': ['Ramzes II (Buyuk Ramzes)', 'Tutmos III', 'Tutanxamon', 'Exnaton'],
              'ru': ['Рамсес II Великий', 'Тутмос III', 'Тутанхамон', 'Эхнатон'],
              'en': ['Ramesses II (The Great)', 'Thutmose III', 'Tutankhamun', 'Akhenaten']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Ramzes II (Buyuk Ramzes)', 'ru': 'Рамсес II Великий', 'en': 'Ramesses II (The Great)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/RamessesII_AbuSimbel.jpg/640px-RamessesII_AbuSimbel.jpg',
  'fun_fact': {'uz': "Ramzes II ning 100 dan ortiq farzandi bo'lgan va u 90 yoshdan oshib vafot etgan; uning mumiyasi "
                     'bugungi kunda ham Qohira muzeyida mukammal saqlangan.',
               'ru': 'Рамсес II пережил многих своих сыновей и жен, дожив до 90 лет в эпоху, когда средняя '
                     'продолжительность жизни не превышала 30.',
               'en': 'Ramesses II fathered over 100 children and lived into his 90s, leaving more monuments and '
                     'statues than any other pharaoh.'},
  'aliases': ['ramzes', 'ramzes ii', 'рамсес', 'рамсес ii', 'ramesses', 'ramesses the great']},
 {'id': 'hist_who_014',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Mil. avv. XVIII asrda Bobil shohligining oltinchi shohi bo'lganman.\n"
                     '2-maslahat: Mesopotamiyadagi Shumer va Akkad yerlarini birlashtirdim.\n'
                     "3-maslahat: Qora bazalt toshga 'Ko'zga ko'z, tishga tish' tamoyiliga asoslangan 282 ta moddadan "
                     "iborat qonunlarni o'ydirdim.",
               'ru': 'Подсказка 1: Царь Вавилона в XVIII веке до н.э., объединивший Месопотамию.\n'
                     'Подсказка 2: Создал один из первых в истории письменных сводов законов из 282 статей.\n'
                     'Подсказка 3: Автор знаменитого правового принципа талиона: «Око за око, зуб за зуб».',
               'en': 'Clue 1: Sixth king of the First Babylonian Dynasty in the 18th century BC.\n'
                     'Clue 2: Unified Mesopotamia under Babylonian rule from the Persian Gulf to Syria.\n'
                     "Clue 3: Promulgated the 282-law code inscribed on a basalt stele, famed for 'an eye for an "
                     "eye'."},
  'options': {'uz': ['Navuxodonosor II', 'Xammurapi', 'Sargon', 'Gilgamish'],
              'ru': ['Навуходоносор II', 'Хаммурапи', 'Саргон', 'Гильгамеш'],
              'en': ['Nebuchadnezzar II', 'Hammurabi', 'Sargon of Akkad', 'Gilgamesh']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Xammurapi', 'ru': 'Хаммурапи', 'en': 'Hammurabi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Code_of_Hammurabi_stele_Louvre.jpg/640px-Code_of_Hammurabi_stele_Louvre.jpg',
  'fun_fact': {'uz': 'Xammurapi qonunlari stelasining yuqori qismida shoh adolat xudosi Shamashdan qonunlar ramzini '
                     'qabul qilib olayotgani tasvirlangan.',
               'ru': 'Базальтовая стела с Законами Хаммурапи была найдена в 1901 году в Сузах и хранится в Лувре.',
               'en': 'The Code of Hammurabi stele depicts the king receiving the sceptre and ring of justice from the '
                     'sun god Shamash.'},
  'aliases': ['xammurapi', 'хаммурапи', 'hammurabi']},
 {'id': 'hist_who_015',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Qadimgi Hindistondagi Maurya sulolasining uchinchi imperatoriman.\n'
                     "2-maslahat: Kalinga jangi dahshatlaridan so'ng qon to'kishdan voz kechdim.\n"
                     "3-maslahat: Buddaviylikni qabul qilib, butun Osiyo bo'ylab tinchlik tosh ustunlarini (Ashoka "
                     "ediktlari) o'rnatdim.",
               'ru': 'Подсказка 1: Правитель империи Маурьев в Индии в III веке до н.э.\n'
                     'Подсказка 2: После кровавой войны в Калинге отрекся от насилия и принял буддизм.\n'
                     'Подсказка 3: Создал каменные эдикты Дхармы, а его «Львиная капитель» стала гербом Индии.',
               'en': 'Clue 1: Third emperor of the Maurya Dynasty ruling almost all of India.\n'
                     'Clue 2: Renounced warfare following the extreme casualties of the Kalinga War.\n'
                     "Clue 3: Converted to Buddhism, erecting stone pillars; his Lion Capital is India's national "
                     'emblem.'},
  'options': {'uz': ['Chandragupta Maurya', 'Kanishka I', 'Ashoka (Buyuk Ashoka)', 'Samudragupta'],
              'ru': ['Чандрагупта Маурья', 'Канишка I', 'Ашока Великий', 'Самудрагупта'],
              'en': ['Chandragupta Maurya', 'Kanishka I', 'Ashoka the Great', 'Samudragupta']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Ashoka (Buyuk Ashoka)', 'ru': 'Ашока Великий', 'en': 'Ashoka the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ashoka_Pillar_Vaishali.jpg/640px-Ashoka_Pillar_Vaishali.jpg',
  'fun_fact': {'uz': "Ashokaning Sarnathdagi to'rtta sher haykali zamonaviy Hindiston Respublikasining rasmiy gerbiga, "
                     "g'ildiragi (Ashoka Chakra) esa davlat bayrog'iga kiritilgan.",
               'ru': '«Львиная капитель» Ашоки в Сарнатхе и «Колесо Ашоки» (чакра) украшают современный герб и флаг '
                     'Индии.',
               'en': "Ashoka's four-lion capital at Sarnath is India's national emblem, and the Ashoka Chakra wheel "
                     "appears on India's flag."},
  'aliases': ['ashoka', 'buyuk ashoka', 'ашока', 'ашока великий', 'ashoka the great']},
 {'id': 'hist_who_016',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 'Urushayotgan podsholiklar' davriga chek qo'yib, Xitoyni ilk bor yagona imperiyaga "
                     'birlashtirdim.\n'
                     "2-maslahat: Yozuv, o'lchov, tanga va aravaning g'ildirak o'qlarini standartlashtirdim.\n"
                     '3-maslahat: Buyuk Xitoy devorini birlashtirdim va qabrim uchun minglab Terrakota jangchilarini '
                     'yasattirdim.',
               'ru': 'Подсказка 1: Первый император объединенного Китая, основатель династии Цинь.\n'
                     'Подсказка 2: Стандартизировал иероглифическую письменность, монеты и меры веса.\n'
                     'Подсказка 3: Построил Великую Китайскую стену и был похоронен с восьмитысячной Терракотовой '
                     'армией.',
               'en': 'Clue 1: Ended the Warring States period, becoming the first Emperor of a unified China.\n'
                     'Clue 2: Standardized Chinese script, currency, road widths, and units of measurement.\n'
                     'Clue 3: Connected the Great Wall and was entombed with the subterranean Terracotta Army.'},
  'options': {'uz': ['Xan Gaotszu', 'Sun Yatsen', 'Xan Vudi', 'Qin Shixuandi'],
              'ru': ['Хань Гао-цзу', 'Сунь Ятсен', 'У-ди', 'Цинь Шихуанди'],
              'en': ['Emperor Gaozu of Han', 'Sun Yat-sen', 'Emperor Wu of Han', 'Qin Shi Huang']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Qin Shixuandi', 'ru': 'Цинь Шихуанди', 'en': 'Qin Shi Huang'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Qinshihuang.jpg/640px-Qinshihuang.jpg',
  'fun_fact': {'uz': 'Qin Shixuandi mangu hayot eliksirini qidirib simob ichgan va zaharlanib vafot etgan; uning yer '
                     'osti maqbarasida simobdan yasalgan daryolar oqadi degan taxmin bor.',
               'ru': 'Император искал эликсир бессмертия и принимал пилюли с ртутью, что и послужило причиной его '
                     'преждевременной смерти.',
               'en': 'Obsessed with immortality, Qin Shi Huang consumed mercury pills concocted by alchemists, '
                     'hastening his death in 210 BC.'},
  'aliases': ['qin shixuandi', 'tsin shixuandi', 'цинь шихуанди', 'qin shi huang']},
 {'id': 'hist_who_017',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Franklar qiroli bo'lib, Karolinglar sulolasiga mansubman.\n"
                     "2-maslahat: Milodiy 800 yilda Rim papasi Lev III tomonidan G'arbiy Rim imperatori deb toj "
                     'kiydirildim.\n'
                     "3-maslahat: G'arbiy Yevropani birlashtirib, 'Yevropaning otasi' (Pater Europae) deb nom oldim.",
               'ru': 'Подсказка 1: Король франков из династии Каролингов, объединивший Европу.\n'
                     'Подсказка 2: В день Рождества 800 года был коронован папой Львом III как император Запада.\n'
                     'Подсказка 3: Считается «Отцом Европы», заложившим основы Франции и Германии.',
               'en': 'Clue 1: King of the Franks who led the Carolingian Renaissance.\n'
                     'Clue 2: Crowned Emperor of the Romans by Pope Leo III in Rome on Christmas Day 800.\n'
                     "Clue 3: United much of Western Europe, earning the moniker 'Father of Europe' (Pater Europae)."},
  'options': {'uz': ['Buyuk Karl (Karl Velikiy)', 'Xlodvig I', 'Karl Martell', 'Otton I'],
              'ru': ['Карл Великий', 'Хлодвиг I', 'Карл Мартелл', 'Оттон I'],
              'en': ['Charlemagne', 'Clovis I', 'Charles Martel', 'Otto the Great']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Buyuk Karl (Karl Velikiy)', 'ru': 'Карл Великий', 'en': 'Charlemagne'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Charlemagne_Durer.jpg/640px-Charlemagne_Durer.jpg',
  'fun_fact': {'uz': "Buyuk Karl o'qishni bilsa-da, yozishni yaxshi bilmagan; u yostiq ostida doim mum taxtacha "
                     "saqlab, yozishni o'rganishga uringan.",
               'ru': 'Карл Великий свободно говорил на латыни и греческом, но писать так и не научился, несмотря на '
                     'постоянные упражнения.',
               'en': 'Though Charlemagne promoted scholarly learning, he struggled to write, keeping wax tablets under '
                     'his pillow to practice.'},
  'aliases': ['buyuk karl', 'karl velikiy', 'карл великий', 'charlemagne']},
 {'id': 'hist_who_018',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Yuz yillik urush paytida oddiy dehqon qizi bo'lib tug'ilganman.\n"
                     '2-maslahat: Samoviy ovozlarga ergashib, 1429 yilda Orlean shahrining inglizlar qamalini yorib '
                     "o'tdim.\n"
                     "3-maslahat: Inglizlar tomonidan sotib olinib, Ruanda 'jodugar' ayblovi bilan gulxanda tiriklayin "
                     'yoqildim.',
               'ru': 'Подсказка 1: Французская крестьянка, услышавшая голоса святых во время Столетней войны.\n'
                     'Подсказка 2: Возглавила армию и сняла осаду Орлеана, приведя дофина Карла к коронации в Реймсе.\n'
                     'Подсказка 3: Была предана, объявлена еретичкой и сожжена на костре в Руане в возрасте 19 лет.',
               'en': 'Clue 1: Peasant girl who believed she was guided by the archangel Michael.\n'
                     "Clue 2: Lifted the Siege of Orleans in 1429, turning the tide of the Hundred Years' War.\n"
                     'Clue 3: Captured and burned at the stake for heresy in Rouen at age nineteen; later canonized.'},
  'options': {'uz': ['Mariya Antuanetta', "Janna d'Ark (Orlean qizi)", 'Yekaterina Medichi', 'Eleonora Akvitaniyalik'],
              'ru': ['Мария-Антуанетта', "Жанна д'Арк (Орлеанская дева)", 'Екатерина Медичи', 'Алиенора Аквитанская'],
              'en': ['Marie Antoinette',
                     'Joan of Arc (Maid of Orléans)',
                     "Catherine de' Medici",
                     'Eleanor of Aquitaine']},
  'correct_index': 1,
  'correct_answer': {'uz': "Janna d'Ark (Orlean qizi)",
                     'ru': "Жанна д'Арк (Орлеанская дева)",
                     'en': 'Joan of Arc (Maid of Orléans)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Joan_of_arc_miniature_graded.jpg/640px-Joan_of_arc_miniature_graded.jpg',
  'fun_fact': {'uz': "Janna d'Ark o'limidan 25 yil o'tib oqlangan va 1920 yilda Katolik cherkovi tomonidan avliyolar "
                     "safiga qo'shilgan.",
               'ru': "Спустя 500 лет после гибели Жанна д'Арк была канонизирована Римской католической церковью как "
                     'святая покровительница Франции.',
               'en': 'Posthumously retried and declared innocent 25 years after her death, Joan was canonized as a '
                     'Saint in 1920.'},
  'aliases': ['janna dark', 'orlean qizi', 'жанна дарк', 'орлеанская дева', 'joan of arc']},
 {'id': 'hist_who_019',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Usmonli saltanatining 10-sultoni bo'lib, 46 yil taxtda o'tirganman.\n"
                     '2-maslahat: Mohach jangida (1526) Vengriyani zabt etdim va Vena shahrini qamal qildim.\n'
                     "3-maslahat: Me'mor Sinon bilan birga Sulaymoniya masjidini qurdirdim; Hurram Sulton (Roksolana) "
                     'mening suyukli rafiqam edi.',
               'ru': 'Подсказка 1: Десятый султан Османской империи, правивший дольше всех — 46 лет.\n'
                     'Подсказка 2: Разгромил венгров при Мохаче, осаждал Вену и расширил флот на Средиземном море.\n'
                     'Подсказка 3: В Европе прозван «Великолепным», на Востоке — «Кануни» (Законодатель); муж Хюррем '
                     'Султан.',
               'en': 'Clue 1: Tenth and longest-reigning Ottoman Sultan, ruling for 46 years.\n'
                     'Clue 2: Conquered Hungary at Mohács in 1526 and laid siege to Vienna.\n'
                     "Clue 3: Commissioned the Süleymaniye Mosque; known in Europe as 'The Magnificent' and married to "
                     'Hürrem Sultan.'},
  'options': {'uz': ['Mehmed II Fathchi', 'Salim I Yavuz', 'Sulton Sulaymon Qonuniy (Muhtasham)', 'Boyazid I'],
              'ru': ['Мехмед II Фатих', 'Селим I Явуз', 'Султан Сулейман Великолепный (Кануни)', 'Баязид I'],
              'en': ['Mehmed the Conqueror', 'Selim I', 'Suleiman the Magnificent (The Lawgiver)', 'Bayezid I']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Sulton Sulaymon Qonuniy (Muhtasham)',
                     'ru': 'Султан Сулейман Великолепный (Кануни)',
                     'en': 'Suleiman the Magnificent (The Lawgiver)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Suleiman_the_magnificent.jpg/640px-Suleiman_the_magnificent.jpg',
  'fun_fact': {'uz': "Sulaymon Qonuniy saltanat qonunlarini to'liq tizimlashtirgani uchun musulmon olamida 'Qonuniy' "
                     'unvonini olgan va zargarlik hunarini mukammal egallagan.',
               'ru': 'Сулейман I был искусным ювелиром и поэтом, писавшим газели под псевдонимом Мухибби.',
               'en': 'Suleiman was an accomplished goldsmith and wrote celebrated love poetry under the pen name '
                     'Muhibbi.'},
  'aliases': ['sulaymon',
              'sulaymon qonuniy',
              'muhtasham sulaymon',
              'сулейман великолепный',
              'кануни',
              'suleiman the magnificent']},
 {'id': 'hist_who_020',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Romanovlar sulolasiga mansub bo'lib, bo'yim 2 metrdan baland edi.\n"
                     "2-maslahat: Yevropaga 'Buyuk elchilik' bilan borib, Gollandiyada oddiy duradgor bo'lib kema "
                     "qurishni o'rgandim.\n"
                     '3-maslahat: Shvetsiyani Poltava jangida yengib, Sankt-Peterburg shahriga asos soldim va '
                     'Rossiyani imperiyaga aylantirdim.',
               'ru': 'Подсказка 1: Русский царь ростом более двух метров, начавший править в конце XVII века.\n'
                     'Подсказка 2: Побывал в Европе инкогнито под именем урядника Петра Михайлова, учась '
                     'кораблестроению.\n'
                     'Подсказка 3: Победил Карла XII при Полтаве, «прорубил окно в Европу» и основал Санкт-Петербург.',
               'en': 'Clue 1: Over six-foot-seven Romanov monarch who transformed his country in the late 17th '
                     'century.\n'
                     'Clue 2: Traveled incognito to Western Europe to learn shipbuilding as a common carpenter.\n'
                     'Clue 3: Defeated Sweden at Poltava, founded Saint Petersburg, and proclaimed the Russian '
                     'Empire.'},
  'options': {'uz': ['Ivan Grozniy', 'Aleksandr I', 'Nikolay II', 'Pyotr I Buyuk'],
              'ru': ['Иван Грозный', 'Александр I', 'Николай II', 'Петр I Великий'],
              'en': ['Ivan the Terrible', 'Alexander I', 'Nicholas II', 'Peter the Great']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Pyotr I Buyuk', 'ru': 'Петр I Великий', 'en': 'Peter the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Peter_the_Great_by_Paul_Delaroche.jpg/640px-Peter_the_Great_by_Paul_Delaroche.jpg',
  'fun_fact': {'uz': "Pyotr I zodagonlarning soqollarini o'z qo'li bilan qirqqan va soqol qo'yganlardan maxsus 'soqol "
                     "solig'i' joriy qilgan.",
               'ru': 'Петр I ввел знаменитый налог на бороды и заставил бояр сменить традиционную одежду на '
                     'европейские камзолы.',
               'en': 'Peter enacted a famous tax on beards, carrying scissors to personally shear off the whiskers of '
                     'resistant boyars.'},
  'aliases': ['pyotr i', 'pyotr buyuk', 'петр i', 'петр великий', 'peter the great', 'peter i']},
 {'id': 'hist_who_021',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Germaniyada tug'ilgan Sofiya Avgustaman, eri Pyotr III ni ag'darib taxtga "
                     "o'tirganman.\n"
                     "2-maslahat: Volter va Didro kabi ma'rifatparvar faylasuflar bilan doimiy xat yozishganman.\n"
                     "3-maslahat: Qrimni, Qora dengiz bo'ylarini va Polshaning katta qismini Rossiyaga qo'shib olgan "
                     'imperatrisaman.',
               'ru': 'Подсказка 1: Немецкая принцесса София, пришедшая к власти в Петербурге в результате дворцового '
                     'переворота.\n'
                     'Подсказка 2: Вела переписку с Вольтером и Дидро, продвигая «просвещенный абсолютизм».\n'
                     'Подсказка 3: Присоединила Крым, Новороссию и основала города Одессу, Севастополь и '
                     'Екатеринослав.',
               'en': 'Clue 1: German-born princess who seized the imperial throne in a 1762 palace coup.\n'
                     "Clue 2: Corresponded with Voltaire and Diderot as an 'enlightened despot'.\n"
                     "Clue 3: Annexed Crimea and partitioned Poland, reigning during Russia's golden age of nobility."},
  'options': {'uz': ['Yekaterina II Buyuk', 'Yelizaveta Petrovna', 'Anna Ioannovna', 'Mariya Tereziya'],
              'ru': ['Екатерина II Великая', 'Елизавета Петровна', 'Анна Иоанновна', 'Мария Терезия'],
              'en': ['Catherine the Great', 'Elizabeth of Russia', 'Anna of Russia', 'Maria Theresa']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Yekaterina II Buyuk', 'ru': 'Екатерина II Великая', 'en': 'Catherine the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Catherine_II_by_Rokotov_%281763%2C_Hermitage%29.jpg/640px-Catherine_II_by_Rokotov_%281763%2C_Hermitage%29.jpg',
  'fun_fact': {'uz': "Yekaterina II Yevropadagi eng katta san'at asarlari to'plamini sotib olib, mashhur Ermitaj "
                     'muzeyiga asos solgan.',
               'ru': 'Екатерина II положила начало коллекции Эрмитажа в 1764 году, закупив 225 полотен европейских '
                     'художников.',
               'en': 'Catherine founded the State Hermitage Museum in 1764 by purchasing a private collection of 225 '
                     'European masterworks.'},
  'aliases': ['yekaterina ii', 'yekaterina buyuk', 'екатерина ii', 'екатерина великая', 'catherine the great']},
 {'id': 'hist_who_022',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Virjiniyadagi Maunt-Vernon mulkida tug'ilgan plantator va harbiy ofitserman.\n"
                     "2-maslahat: AQSh Mustaqillik urushida Qit'a armiyasining Bosh qo'mondoni bo'lib, Yorktaun "
                     "jangida g'alaba qozondim.\n"
                     "3-maslahat: AQShning birinchi prezidenti bo'ldim va 'Millat otasi' deb nom oldim.",
               'ru': 'Подсказка 1: Виргинский плантатор и главнокомандующий Континентальной армией в войне за '
                     'независимость.\n'
                     'Подсказка 2: Принял капитуляцию британцев при Йорктауне в 1781 году.\n'
                     'Подсказка 3: Первый президент Соединенных Штатов Америки, единогласно избранный коллегией '
                     'выборщиков.',
               'en': 'Clue 1: Virginia planter who served as Commander-in-Chief of the Continental Army.\n'
                     'Clue 2: Forced the British surrender at Yorktown in 1781, winning American independence.\n'
                     'Clue 3: Unanimously elected as the first President of the United States.'},
  'options': {'uz': ['Tomas Jefferson', 'Jorj Vashington', 'Benjamin Franklin', 'Jon Adams'],
              'ru': ['Томас Джефферсон', 'Джордж Вашингтон', 'Бенджамин Франклин', 'Джон Адамс'],
              'en': ['Thomas Jefferson', 'George Washington', 'Benjamin Franklin', 'John Adams']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Jorj Vashington', 'ru': 'Джордж Вашингтон', 'en': 'George Washington'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg/640px-Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg',
  'fun_fact': {'uz': 'Vashington uchinchi muddatga prezidentlikka saylanishdan ixtiyoriy ravishda voz kechib, AQShda '
                     "ikki muddatli prezidentlik an'anasiga asos solgan.",
               'ru': 'Вашингтон отказался от третьего президентского срока, установив вековую демократическую традицию '
                     'добровольной передачи власти.',
               'en': 'Washington voluntarily stepped down after two terms, setting the precedent of peaceful '
                     'democratic succession.'},
  'aliases': ['vashington', 'jorj vashington', 'вашингтон', 'джордж вашингтон', 'george washington']},
 {'id': 'hist_who_023',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Kentukkidagi oddiy yog'och kulbada tug'ilib, o'z kuchi bilan advokat bo'ldim.\n"
                     '2-maslahat: AQSh Fuqarolar urushida Shimoliy shtatlarni boshqarib, qullikni butunlay bekor '
                     'qildim.\n'
                     "3-maslahat: Mashhur Gettisberg nutqini so'zlaganman; 1865 yilda teatrda aktyor Jon But tomonidan "
                     "otib o'ldirildim.",
               'ru': 'Подсказка 1: Выходец из бедной семьи, ставший 16-м президентом США.\n'
                     'Подсказка 2: Сохранил союз штатов в Гражданской войне и издал Прокламацию об освобождении '
                     'рабов.\n'
                     'Подсказка 3: Был смертельно ранен сторонником южан Джоном Бутом в театре Форда в Вашингтоне.',
               'en': 'Clue 1: Born in a Kentucky log cabin, self-educated to become a frontier lawyer.\n'
                     'Clue 2: Led the Union through the Civil War and issued the Emancipation Proclamation.\n'
                     "Clue 3: Delivered the Gettysburg Address and was assassinated by John Wilkes Booth at Ford's "
                     'Theatre.'},
  'options': {'uz': ['Uillis Grant', 'Endryu Jekson', 'Avraam Linkoln', 'Teodor Ruzvelt'],
              'ru': ['Улисс Грант', 'Эндрю Джексон', 'Авраам Линкольн', 'Теодор Рузвельт'],
              'en': ['Ulysses S. Grant', 'Andrew Jackson', 'Abraham Lincoln', 'Theodore Roosevelt']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Avraam Linkoln', 'ru': 'Авраам Линкольн', 'en': 'Abraham Lincoln'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg/640px-Abraham_Lincoln_O-77_matte_collodion_print.jpg',
  'fun_fact': {'uz': "Linkoln AQSh prezidentlari ichida eng novchasi (193 sm) bo'lgan va o'zining baland silindr "
                     'shlyapasi ichida muhim hujjatlar va xatlarni saqlagan.',
               'ru': 'Линкольн был самым высоким президентом США (193 см) и носил в своей знаменитой высокой шляпе '
                     'важные бумаги и законопроекты.',
               'en': "At 6 feet 4 inches, Lincoln was America's tallest president, often storing bills and speeches "
                     'inside his stovepipe hat.'},
  'aliases': ['linkoln', 'avraam linkoln', 'линкольн', 'авраам линкольн', 'abraham lincoln']},
 {'id': 'hist_who_024',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 'Qon, mashaqqat, ko'zyoshi va ter'dan boshqa narsa va'da qila olmayman deganman.\n"
                     '2-maslahat: Ikkinchi jahon urushida Buyuk Britaniya Bosh vaziri sifatida Gitlerga qarshi '
                     'kurashga boshchilik qildim.\n'
                     "3-maslahat: 'V for Victory' ishorasi va og'zimdagi doimiy sigara mening timsolim bo'lgan; 1953 "
                     "yilda Adabiyot bo'yicha Nobel mukofotini oldim.",
               'ru': 'Подсказка 1: Произнес историческую речь о «крови, тяжелом труде, слезах и поте».\n'
                     'Подсказка 2: Премьер-министр Великобритании, сплотивший нацию во время Битвы за Британию против '
                     'нацистов.\n'
                     'Подсказка 3: Лауреат Нобелевской премии по литературе, автор понятия «железный занавес» в '
                     'Фултонской речи.',
               'en': "Clue 1: Promised his nation nothing but 'blood, toil, tears, and sweat' in May 1940.\n"
                     'Clue 2: British Prime Minister who rallied the free world against Nazi Germany in WWII.\n'
                     "Clue 3: Coined the phrase 'Iron Curtain' in 1946 and won the 1953 Nobel Prize in Literature."},
  'options': {'uz': ['Nevil Chemberlen', 'Klement Ettli', 'Franklin Ruzvelt', 'Uinston Cherchill'],
              'ru': ['Невилл Чемберлен', 'Клемент Эттли', 'Франклин Рузвельт', 'Уинстон Черчилль'],
              'en': ['Neville Chamberlain', 'Clement Attlee', 'Franklin D. Roosevelt', 'Winston Churchill']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Uinston Cherchill', 'ru': 'Уинстон Черчилль', 'en': 'Winston Churchill'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Sir_Winston_Churchill_-_1941.jpg/640px-Sir_Winston_Churchill_-_1941.jpg',
  'fun_fact': {'uz': "Cherchill bo'sh vaqtlarida mahoratli rassom bo'lgan va hayoti davomida 500 dan ortiq kartina "
                     'chizgan.',
               'ru': 'Черчилль был плодовитым художником, написавшим более 500 картин под псевдонимом Шарль Морен.',
               'en': 'Churchill was an avid painter who produced over 500 canvases, exhibiting under pseudonyms at the '
                     'Royal Academy.'},
  'aliases': ['cherchill', 'uinston cherchill', 'черчилль', 'уинстон черчилль', 'winston churchill', 'churchill']},
 {'id': 'hist_who_025',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Londonda yuristlikka o'qiganman va Janubiy Afrikada irqiy kamsitishlarga qarshi ilk "
                     'kurashimni boshlaganman.\n'
                     "2-maslahat: 'Satyagraha' — zo'ravonliksiz fuqarolik itoatsizligi falsafasini yaratdim va 'Tuz "
                     "yurishi'ga boshchilik qildim.\n"
                     "3-maslahat: Hindistonni Britaniya mustamlakasidan ozod etib, 'Millat otasi' (Bapu) va 'Buyuk "
                     "qalb' (Mahatma) nomini oldim.",
               'ru': 'Подсказка 1: Начал правозащитную деятельность в Южной Африке, защищая права индийцев.\n'
                     'Подсказка 2: Разработал тактику ненасильственного сопротивления («Сатьяграха») и возглавил '
                     '«Соляной поход».\n'
                     'Подсказка 3: Духовный лидер движения за независимость Индии, прозванный «Великой душой» '
                     '(Махатма).',
               'en': 'Clue 1: Trained as a barrister in London, beginning civil rights work in South Africa.\n'
                     "Clue 2: Developed 'Satyagraha' nonviolent resistance and led the famous 1930 Salt March.\n"
                     "Clue 3: Revered as the Father of the Nation in India, honored with the title 'Mahatma' (Great "
                     'Soul).'},
  'options': {'uz': ['Mahatma Gandi (Mohandas Karamchand Gandi)',
                     'Javaharlal Neru',
                     'Subxas Chandra Bos',
                     'Rabindranat Tagor'],
              'ru': ['Махатма Ганди', 'Джавахарлал Неру', 'Субхас Чандра Бос', 'Рабиндранат Тагор'],
              'en': ['Mahatma Gandhi', 'Jawaharlal Nehru', 'Subhas Chandra Bose', 'Rabindranath Tagore']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Mahatma Gandi (Mohandas Karamchand Gandi)', 'ru': 'Махатма Ганди', 'en': 'Mahatma Gandhi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Mahatma-Gandhi%2C_studio%2C_1931.jpg/640px-Mahatma-Gandhi%2C_studio%2C_1931.jpg',
  'fun_fact': {'uz': "Rabindranat Tagor unga ilk bor 'Mahatma' (Buyuk qalb) unvonini bergan; Gandi har kuni o'z "
                     "qo'llari bilan urchiqda ip yigirgan.",
               'ru': 'Ганди носил простую домотканую одежду (дхоти) и ежедневно прял пряжу на ручной прялке, призывая '
                     'к бойкоту британских товаров.',
               'en': 'Gandhi spun his own yarn daily on a charkha, promoting khadi homespun cloth to boycott imported '
                     'British textiles.'},
  'aliases': ['gandi', 'mahatma gandi', 'ганди', 'махатма ганди', 'mahatma gandhi']},
 {'id': 'hist_who_026',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Janubiy Afrikadagi irqiy kamsitish (aparteid) rejimiga qarshi kurashganman.\n'
                     "2-maslahat: Robben orolidagi qamoqxonada va boshqa qamoqlarda 27 yil mahbuslikda o'tirdim.\n"
                     "3-maslahat: 1994 yilda JARning ilk qora tanli prezidenti bo'lib saylandim va Tinchlik bo'yicha "
                     'Nobel mukofoti oldim.',
               'ru': 'Подсказка 1: Борец против режима расовой сегрегации (апартеида) в ЮАР.\n'
                     'Подсказка 2: Провел 27 лет в тюрьмах, став всемирным символом стойкости и прощения.\n'
                     'Подсказка 3: Первый чернокожий президент Южно-Африканской Республики и нобелевский лауреат мира.',
               'en': 'Clue 1: Anti-apartheid revolutionary in South Africa.\n'
                     'Clue 2: Imprisoned for 27 years, mostly on Robben Island, as Prisoner 46664.\n'
                     "Clue 3: Elected South Africa's first Black president in 1994 and awarded the Nobel Peace Prize."},
  'options': {'uz': ['Desmond Tutu', 'Nelson Mandela (Madiba)', 'Kofi Annan', 'Patris Lumumba'],
              'ru': ['Десмонд Туту', 'Нельсон Мандела (Мадиба)', 'Кофи Аннан', 'Патрис Лумумба'],
              'en': ['Desmond Tutu', 'Nelson Mandela (Madiba)', 'Kofi Annan', 'Patrice Lumumba']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Nelson Mandela (Madiba)',
                     'ru': 'Нельсон Мандела (Мадиба)',
                     'en': 'Nelson Mandela (Madiba)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Nelson_Mandela_1994.jpg/640px-Nelson_Mandela_1994.jpg',
  'fun_fact': {'uz': "Mandela ozodlikka chiqqach, qasos olish o'rniga 'Haqiqat va yarashuv komissiyasi'ni tuzib, "
                     'Janubiy Afrikada fuqarolar urushining oldini oldi.',
               'ru': 'Мандела пригласил на свою президентскую инаугурацию тюремного надзирателя, показав пример '
                     'национального примирения.',
               'en': 'Mandela invited his former Robben Island prison guard as an honored VIP guest to his '
                     'presidential inauguration in 1994.'},
  'aliases': ['mandela', 'nelson mandela', 'madiba', 'мандела', 'нельсон мандела', 'nelson mandela']},
 {'id': 'hist_who_027',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Chanakkale (Gallipoli) jangida (1915) Usmonli qo'shinlariga qo'mondonlik qilib "
                     "ittifoqchilarni to'xtatdim.\n"
                     '2-maslahat: Usmonli saltanati parchalanib ketgach, Turkiya mustaqillik urushiga rahbarlik '
                     'qildim.\n'
                     "3-maslahat: 1923 yilda zamonaviy dunyoviy Turkiya Respublikasiga asos soldim va 'Turklar otasi' "
                     '(Otaturk) nomini oldim.',
               'ru': 'Подсказка 1: Национальный герой битвы при Галлиполи (Чанаккале) 1915 года.\n'
                     'Подсказка 2: Возглавил войну за независимость Турции против интервентов Антанты.\n'
                     'Подсказка 3: Первый президент Турецкой Республики, отменивший халифат и внедривший латинский '
                     'алфавит.',
               'en': 'Clue 1: Hero of the Gallipoli campaign in 1915 defending the Dardanelles.\n'
                     'Clue 2: Led the Turkish War of Independence against Allied occupation.\n'
                     "Clue 3: Founded the modern secular Republic of Turkey in 1923, bestowed the surname 'Atatürk'."},
  'options': {'uz': ['Ismat Inonyu', 'Enver Posho', 'Mustafo Kamol Otaturk', 'Abdulhamid II'],
              'ru': ['Исмет Инёню', 'Энвер-паша', 'Мустафа Кемаль Ататюрк', 'Абдул-Хамид II'],
              'en': ['İsmet İnönü', 'Enver Pasha', 'Mustafa Kemal Atatürk', 'Abdul Hamid II']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Mustafo Kamol Otaturk', 'ru': 'Мустафа Кемаль Ататюрк', 'en': 'Mustafa Kemal Atatürk'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Ataturk1930s.jpg/640px-Ataturk1930s.jpg',
  'fun_fact': {'uz': "Otaturk poytaxtni Istanbuldan Anqaraga ko'chirgan, ayollarga saylov huquqini ko'plab Yevropa "
                     "davlatlaridan oldin bergan va lotin alifbosini shaxsan taxtada xalqqa o'rgatgan.",
               'ru': 'Ататюрк предоставил турецким женщинам избирательные права раньше, чем во Франции и Швейцарии.',
               'en': 'Atatürk personally toured Anatolia with a blackboard and chalk to teach the new Turkish Latin '
                     'alphabet to citizens.'},
  'aliases': ['otaturk', 'mustafo kamol', 'ататюрк', 'мустафа кемаль', 'ataturk', 'mustafa kemal']},
 {'id': 'hist_who_028',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Qadimgi Xitoyda Vu podsholigida sarkarda va harbiy strateg bo'lib xizmat qilganman.\n"
                     "2-maslahat: 'Dushmaningni va o'zingni bilsang, yuzta jangda ham xavf ostida qolmaysan' degan "
                     'mashhur qoidani yaratdim.\n'
                     "3-maslahat: Harbiy san'at bo'yicha dunyodagi eng mashhur qo'llanma bo'lgan 'Urush san'ati' "
                     '(Binfa) kitobining muallifiman.',
               'ru': 'Подсказка 1: Древнекитайский полководец и военный теоретик VI века до н.э.\n'
                     'Подсказка 2: Сформулировал закон: «Если знаешь себя и врага, не проиграешь и в сотне битв».\n'
                     'Подсказка 3: Автор древнейшего и самого известного в мире трактата «Искусство войны».',
               'en': 'Clue 1: Ancient Chinese military general and strategist from the state of Wu.\n'
                     "Clue 2: Wrote: 'If you know the enemy and know yourself, you need not fear the result of a "
                     "hundred battles'.\n"
                     "Clue 3: Author of 'The Art of War', the most influential military treatise in history."},
  'options': {'uz': ['Konfutsiy', 'Lao Tszi', 'Shan Yan', 'Sun Tszi (Sun Szi)'],
              'ru': ['Конфуций', 'Лао-цзы', 'Шан Ян', 'Сунь-цзы'],
              'en': ['Confucius', 'Laozi', 'Shang Yang', 'Sun Tzu']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Sun Tszi (Sun Szi)', 'ru': 'Сунь-цзы', 'en': 'Sun Tzu'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Sun_Tzu.jpg/640px-Sun_Tzu.jpg',
  'fun_fact': {'uz': "Sun Tszi ta'limotiga ko'ra, eng buyuk g'alaba — birorta ham jang qilmasdan va qon to'kmasdan "
                     "dushmanning rejalarini buzish orqali erishilgan g'alabadir.",
               'ru': 'Сунь-цзы утверждал: «Лучшая война — разбить замыслы противника, а не воевать на поле боя».',
               'en': "Sun Tzu's supreme principle was: 'The supreme art of war is to subdue the enemy without "
                     "fighting.'"},
  'aliases': ['sun tszi', 'sun szi', 'urush sanati', 'сунь-цзы', 'искусство войны', 'sun tzu', 'art of war']},
 {'id': 'hist_who_029',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Mil. avv. VI asrda Lu podsholigida tug'ilgan qadimgi Xitoy mutafakkiriman.\n"
                     "2-maslahat: 'O'zingga ravo ko'rmagan narsani boshqalarga ham ravo ko'rma' oltin qoidasini "
                     "targ'ib qilganman.\n"
                     '3-maslahat: Butun Sharqiy Osiyo sivilizatsiyasi, davlat boshqaruvi va axloq poydevoriga aylangan '
                     "konfutsiylik ta'limoti asoschisiman.",
               'ru': 'Подсказка 1: Древнекитайский мудрец, живший в эпоху Весен и Осеней в царстве Лу.\n'
                     'Подсказка 2: Сформулировал золотое правило этики: «Не делай другим того, чего не желаешь себе».\n'
                     'Подсказка 3: Создатель конфуцианства — учения о сыновней почтительности, ритуале и благородном '
                     'муже.',
               'en': 'Clue 1: Ancient Chinese sage and teacher born in the State of Lu around 551 BC.\n'
                     "Clue 2: Advocated the golden rule: 'Do not do unto others what you do not want done to "
                     "yourself'.\n"
                     'Clue 3: Founder of Confucianism, the ethical and philosophical foundation of East Asian '
                     'civilization.'},
  'options': {'uz': ['Konfutsiy (Kun Tszi)', 'Lao Tszi', 'Men Tszi', 'Chjuan Tszi'],
              'ru': ['Конфуций (Кун-цзы)', 'Лао-цзы', 'Мэн-цзы', 'Чжуан-цзы'],
              'en': ['Confucius (Kong Fuzi)', 'Laozi', 'Mencius', 'Zhuangzi']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Konfutsiy (Kun Tszi)', 'ru': 'Конфуций (Кун-цзы)', 'en': 'Confucius (Kong Fuzi)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Confucius_Tang_Dynasty.jpg/640px-Confucius_Tang_Dynasty.jpg',
  'fun_fact': {'uz': "Uning shogirdlari tomonidan to'plangan 'Lun Yuy' (Suhbatlar va mulohazalar) kitobi 2000 yildan "
                     "ortiq vaqt davomida Xitoyda davlat xizmatiga imtihon topshirishning asosiy manbasi bo'lgan.",
               'ru': 'Сборник изречений Конфуция «Лунь Юй» веками оставался главным каноническим текстом для сдачи '
                     'экзаменов на государственные должности в Китае.',
               'en': "The Analects ('Lunyu'), compiled by Confucius's disciples, served as the mandatory curriculum "
                     'for Chinese civil service exams for over two millennia.'},
  'aliases': ['konfutsiy', 'kun tszi', 'конфуций', 'кун-цзы', 'confucius']},
 {'id': 'hist_who_030',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Afinaning ko'cha va maydonlarida odamlar bilan savol-javob orqali haqiqatni izlagan "
                     'qadimgi yunon faylasufiman.\n'
                     "2-maslahat: 'Men hech narsani bilmasligimni bilaman, boshqalar esa buni ham bilishmaydi' degan "
                     'hikmat muallifiman.\n'
                     "3-maslahat: O'z ortimdan hech qanday kitob qoldirmaganman; mil. avv. 399 yilda sud hukmi bilan "
                     "sikut (zahar) ichib halok bo'ldim.",
               'ru': 'Подсказка 1: Афинский мудрец, искавший истину в диалогах с гражданами на городской площади '
                     '(агоре).\n'
                     'Подсказка 2: Сформулировал парадокс мудрости: «Я знаю, что ничего не знаю, но другие не знают и '
                     'этого».\n'
                     'Подсказка 3: Был приговорен судом к смерти за «непочитание богов» и принял чашу с ядом цикуты.',
               'en': 'Clue 1: Classical Athenian philosopher who walked the Agora questioning citizens on virtue and '
                     'justice.\n'
                     "Clue 2: Famously declared: 'I know that I know nothing'.\n"
                     "Clue 3: Left no written texts, executed by drinking hemlock in 399 BC; immortalized in Plato's "
                     'dialogues.'},
  'options': {'uz': ['Aflotun (Platon)', 'Suqrot (Sokrat)', 'Arastu (Aristotel)', 'Diogen'],
              'ru': ['Платон', 'Сократ', 'Аристотель', 'Диоген'],
              'en': ['Plato', 'Socrates', 'Aristotle', 'Diogenes']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Suqrot (Sokrat)', 'ru': 'Сократ', 'en': 'Socrates'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Socrate_du_Louvre.jpg/640px-Socrate_du_Louvre.jpg',
  'fun_fact': {'uz': "Suqrot o'z usulini onasining doyalik kasbiga qiyoslab 'mayevtika' (fikr tug'dirish san'ati) deb "
                     'atagan.',
               'ru': 'Метод Сократа (майевтика) заключался в рождении истины через серию наводящих вопросов в диалоге.',
               'en': "Socrates called his method 'maieutics' (intellectual midwifery), coaxing latent truth from his "
                     'conversation partners.'},
  'aliases': ['suqrot', 'sokrat', 'сократ', 'socrates']},
 {'id': 'hist_who_031',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Suqrotning eng mashhur shogirdi bo'lib, Afinada dunyodagi ilk oliy ta'lim dargohi — "
                     'Akademiyaga asos solganman.\n'
                     "2-maslahat: 'G'or to'g'risida afsona' va 'G'oyalar (eydoslar) dunyosi' falsafasini yaratdim.\n"
                     "3-maslahat: Ideal davlat tuzilishi haqidagi mashhur 'Davlat' (Politeya) asarini yozganman.",
               'ru': 'Подсказка 1: Ученик Сократа, основавший первую Академию в оливковой роще близ Афин.\n'
                     'Подсказка 2: Автор знаменитого мифа о пещере и учения о мире вечных идей (эйдосов).\n'
                     'Подсказка 3: Создал фундаментальный диалог «Государство» об идеальном полисе под властью '
                     'философов.',
               'en': "Clue 1: Socrates' foremost student who founded the Academy in Athens.\n"
                     'Clue 2: Formulated the Theory of Forms (Ideas) and the famous Allegory of the Cave.\n'
                     "Clue 3: Penned the 'Republic', outlining an ideal society governed by philosopher-kings."},
  'options': {'uz': ['Suqrot', 'Arastu', 'Aflotun (Platon)', 'Pifagor'],
              'ru': ['Сократ', 'Аристотель', 'Платон', 'Пифагор'],
              'en': ['Socrates', 'Aristotle', 'Plato', 'Pythagoras']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Aflotun (Platon)', 'ru': 'Платон', 'en': 'Plato'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Plato_Silanion_Musei_Capitolini_MC1377.jpg/640px-Plato_Silanion_Musei_Capitolini_MC1377.jpg',
  'fun_fact': {'uz': "Platon uning asl ismi emas, balki keng yelkasi tufayli berilgan laqab bo'lgan (yunoncha 'platos' "
                     '— keng, keng yelkali demakdir).',
               'ru': '«Платон» — это прозвище, означающее «широкоплечий», данное ему борцовским тренером; настоящее '
                     'имя — Аристокл.',
               'en': "Plato's real name was Aristocles; 'Plato' was a wrestling nickname referring to his broad "
                     'shoulders.'},
  'aliases': ['aflotun', 'platon', 'платон', 'plato']},
 {'id': 'hist_who_032',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Platon Akademiyasida 20 yil ta'lim olib, keyinchalik Afinada o'z maktabim — Likeyga "
                     '(Litsey) asos soldim.\n'
                     '2-maslahat: Aleksandr Makedonskiyga 3 yil davomida ustozlik qilganman.\n'
                     "3-maslahat: Mantiq, biologiya, fizika, metafizika va axloq fanlariga asos solgan 'Birinchi "
                     "muallim'man (Muallimi avval).",
               'ru': 'Подсказка 1: Ученик Платона, основавший Ликей (Лицей) в Афинах и школу перипатетиков.\n'
                     'Подсказка 2: Был наставником и личным учителем юного Александра Македонского.\n'
                     'Подсказка 3: Отец формальной логики и классификатор наук, названный на Востоке «Первым '
                     'учителем».',
               'en': 'Clue 1: Student of Plato who founded the Lyceum and Peripatetic school in Athens.\n'
                     'Clue 2: Served as personal tutor to young Alexander the Great.\n'
                     "Clue 3: Father of formal logic, biology, and rhetoric; known in Islamic philosophy as 'The First "
                     "Teacher'."},
  'options': {'uz': ['Aflotun', 'Suqrot', 'Forobiy', 'Arastu (Aristotel)'],
              'ru': ['Платон', 'Сократ', 'Аль-Фараби', 'Аристотель'],
              'en': ['Plato', 'Socrates', 'Al-Farabi', 'Aristotle']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Arastu (Aristotel)', 'ru': 'Аристотель', 'en': 'Aristotle'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Aristotle_Altemps_Inv8575.jpg/640px-Aristotle_Altemps_Inv8575.jpg',
  'fun_fact': {'uz': "Arastu o'z ustoziga hurmat saqlagan holda: 'Platon mening do'stim, ammo haqiqat undan ham "
                     "azizroq' (Amicus Plato, sed magis amica veritas) degan mashhur so'zni aytgan.",
               'ru': 'Крылатая фраза «Платон мне друг, но истина дороже» принадлежит Аристотелю, спорившему с теорией '
                     'идей своего учителя.',
               'en': "Aristotle coined the adage 'Plato is dear to me, but dearer still is truth' when critiquing his "
                     "teacher's philosophy."},
  'aliases': ['arastu', 'aristotel', 'muallimi avval', 'аристотель', 'первый учитель', 'aristotle']},
 {'id': 'hist_who_033',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Sitsiliyaning Sirakuza shahrida yashagan qadimgi yunon olimi va muhandisiman.\n'
                     "2-maslahat: Vanna qabul qilayotib gidrostatika qonunini kashf etdim va 'Evrika!' (Topdim!) deb "
                     'baqirdim.\n'
                     "3-maslahat: 'Menga tayanch nuqtasini bering, men Yerni joyidan qo'zg'ataman' degan dastak "
                     'qonunining muallifiman.',
               'ru': 'Подсказка 1: Великий математик, механик и инженер из сицилийского города Сиракузы.\n'
                     'Подсказка 2: Открыл закон гидростатики в ванне и с криком «Эврика!» выбежал на улицу.\n'
                     'Подсказка 3: Сформулировал закон рычага: «Дайте мне точку опоры, и я переверну Землю».',
               'en': 'Clue 1: Ancient Greek mathematician, physicist, and engineer from Syracuse, Sicily.\n'
                     "Clue 2: Discovered the buoyancy principle in a bath, famously shouting 'Eureka!'.\n"
                     "Clue 3: Mastered levers and pulleys, stating: 'Give me a place to stand, and I shall move the "
                     "Earth'."},
  'options': {'uz': ['Arximed', 'Evklid', 'Pifagor', 'Geron'],
              'ru': ['Архимед', 'Евклид', 'Пифагор', 'Герон Александрийский'],
              'en': ['Archimedes', 'Euclid', 'Pythagoras', 'Hero of Alexandria']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Arximed', 'ru': 'Архимед', 'en': 'Archimedes'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Domenico-Fetti_Archimedes_1620.jpg/640px-Domenico-Fetti_Archimedes_1620.jpg',
  'fun_fact': {'uz': "Rim askari Sirakuzani bosib olganda, Arximed qumga chizayotgan geometrik shakllarini to'xtatmay: "
                     "'Doiralarimga tegmang!' deganida o'ldirilgan.",
               'ru': 'По легенде, последними словами Архимеда римскому легионеру были: «Не трогай мои чертежи!».',
               'en': "According to legend, Archimedes was killed by a Roman soldier after demanding: 'Do not disturb "
                     "my circles!'"},
  'aliases': ['arximed', 'evrika', 'архимед', 'эврика', 'archimedes', 'eureka']},
 {'id': 'hist_who_034',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 980 yilda Buxoro yaqinidagi Afshona qishlog'ida tug'ilganman, 17 yoshimda Somoniylar "
                     'amirini davolaganman.\n'
                     "2-maslahat: 'Kitob ash-Shifo' (Davolash kitobi) va falsafiy ensiklopediyalarni yaratdim.\n"
                     "3-maslahat: 600 yil davomida Yevropa va Sharqda tibbiyotning asosiy darsligi bo'lgan 'Tib "
                     "qonunlari' (Al-Qonun fit-Tibb) asarining muallifiman.",
               'ru': 'Подсказка 1: Родился в 980 году в селении Афшана близ Бухары, исцелил эмира Саманидов в 17 лет.\n'
                     'Подсказка 2: Автор грандиозной философской энциклопедии «Книга исцеления».\n'
                     'Подсказка 3: Написал «Канон врачебной науки», остававшийся главным медицинским учебником Европы '
                     'более 500 лет.',
               'en': 'Clue 1: Born in 980 AD near Bukhara, curing the Samanid Emir of an illness at age 17.\n'
                     "Clue 2: Authored the philosophical encyclopedia 'The Book of Healing'.\n"
                     "Clue 3: Wrote 'The Canon of Medicine', which remained the standard medical textbook across "
                     'Europe and Asia for six centuries.'},
  'options': {'uz': ['Abu Rayhon Beruniy', 'Abu Ali ibn Sino (Avitsenna)', 'Al-Xorazmiy', 'Ar-Roziy'],
              'ru': ['Абу Райхан Беруни', 'Абу Али ибн Сина (Авиценна)', 'Аль-Хорезми', 'Ар-Рази'],
              'en': ['Abu Rayhan al-Biruni', 'Ibn Sina (Avicenna)', 'Al-Khwarizmi', 'Al-Razi']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Abu Ali ibn Sino (Avitsenna)',
                     'ru': 'Абу Али ибн Сина (Авиценна)',
                     'en': 'Ibn Sina (Avicenna)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Avicenna_portrait.jpg/640px-Avicenna_portrait.jpg',
  'fun_fact': {'uz': "Ibn Sino kasalliklar ko'zga ko'rinmas mikroblar (suv va havodagi zarralar) orqali yuqishini "
                     "birinchi bo'lib bashorat qilgan va karantin usulini joriy etgan.",
               'ru': 'Ибн Сина первым научно описал механизм передачи инфекций через воздух и воду, предвосхитив '
                     'открытие микробов.',
               'en': 'Avicenna hypothesized that diseases spread through unseen airborne particles, pioneering '
                     'quarantine practices.'},
  'aliases': ['ibn sino', 'avitsenna', 'ибн сина', 'авиценна', 'avicenna', 'ibn sina']},
 {'id': 'hist_who_035',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 973 yilda Qadimgi Xorazmning Kot shahrida tug'ilgan qomusiy allomaman.\n"
                     "2-maslahat: Sulton Mahmud G'aznaviy saroyida yashab, Hindiston fani, dini va an'analari haqida "
                     "'Hindiston' asarini yozdim.\n"
                     '3-maslahat: Yerning radiusini (6339 km) mislsiz aniqlikda hisobladim va Kolumbdan 500 yil oldin '
                     "G'arbiy yarimsharda noma'lum quruqlik (Amerika) borligini bashorat qildim.",
               'ru': 'Подсказка 1: Родился в древней столице Хорезма Кяте в 973 году.\n'
                     'Подсказка 2: Автор энциклопедического труда «Индия» и фундаментального «Канона Масуда» по '
                     'астрономии.\n'
                     'Подсказка 3: Рассчитал радиус Земли с точностью до 0,1% и предсказал существование американского '
                     'континента.',
               'en': 'Clue 1: Born in 973 in Kath, Khwarazm, mastering astronomy, physics, and history.\n'
                     "Clue 2: Wrote the monumental anthropological treatise 'Indica' on Indian science and culture.\n"
                     "Clue 3: Calculated Earth's radius to within 1% of the modern value and deduced an inhabited "
                     'landmass in the Western Hemisphere.'},
  'options': {'uz': ['Ibn Sino', "Al-Farg'oniy", 'Abu Rayhon Beruniy', "Mirzo Ulug'bek"],
              'ru': ['Ибн Сина', 'Аль-Фергани', 'Абу Райхан Беруни', 'Мирзо Улугбек'],
              'en': ['Avicenna', 'Al-Farghani', 'Abu Rayhan al-Biruni', 'Mirzo Ulugbek']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Abu Rayhon Beruniy', 'ru': 'Абу Райхан Беруни', 'en': 'Abu Rayhan al-Biruni'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Al-Biruni_statue_Tehran.jpg/640px-Al-Biruni_statue_Tehran.jpg',
  'fun_fact': {'uz': "Beruniy 150 dan ortiq fundamental ilmiy asar yozgan bo'lib, mineralogiya, geodeziya va qiyosiy "
                     'dinshunoslik fanlarining otasi hisoblanadi.',
               'ru': 'Беруни сконструировал первый в исламском мире рельефный глобус и точно определил удельный вес '
                     'десятков металлов и минералов.',
               'en': "Al-Biruni built the Islamic world's first relief globe and determined specific gravities of "
                     'minerals with stunning accuracy.'},
  'aliases': ['beruniy', 'abu rayhon beruniy', 'беруни', 'абу райхан беруни', 'al-biruni', 'biruni']},
 {'id': 'hist_who_036',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 783 yilda Xorazmda tug'ilganman, Bag'doddagi 'Bayt ul-Hikma' (Donishmandlar uyi) "
                     "mudiri bo'lganman.\n"
                     "2-maslahat: 'Al-Jabr val-Muqobala' asarim orqali butun dunyoga 'Algebra' fanini tuhfa qildim.\n"
                     "3-maslahat: Hind raqamlari va 'nol' (0)ni dunyoga yoydim; mening lotincha ismimdan 'Algoritm' "
                     "atamasi paydo bo'ldi.",
               'ru': 'Подсказка 1: Родился в Хорезме, руководил Домом мудрости («Байт аль-Хикма») в Багдаде.\n'
                     'Подсказка 2: Автор книги «Аль-джебр ва-ль-мукабала», давшей начало науке алгебре.\n'
                     'Подсказка 3: Познакомил мир с десятичной позиционной системой и нулем; мое имя породило термин '
                     '«алгоритм».',
               'en': "Clue 1: Born in Khwarazm around 780 AD, serving as director of Baghdad's House of Wisdom.\n"
                     "Clue 2: Authored 'Al-Kitab al-mukhtasar fi hisab al-jabr wal-muqabala', giving birth to "
                     'algebra.\n'
                     'Clue 3: Introduced Hindu-Arabic numerals and zero to the West; my Latinized name gave rise to '
                     "'algorithm'."},
  'options': {'uz': ["Al-Farg'oniy", 'Ibn Sino', 'Umar Xayyom', 'Muhammad ibn Muso al-Xorazmiy'],
              'ru': ['Аль-Фергани', 'Ибн Сина', 'Омар Хайям', 'Мухаммад аль-Хорезми'],
              'en': ['Al-Farghani', 'Avicenna', 'Omar Khayyam', 'Muhammad ibn Musa al-Khwarizmi']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Muhammad ibn Muso al-Xorazmiy',
                     'ru': 'Мухаммад аль-Хорезми',
                     'en': 'Muhammad ibn Musa al-Khwarizmi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Al-Khwarizmi_statue_Khiva.jpg/640px-Al-Khwarizmi_statue_Khiva.jpg',
  'fun_fact': {'uz': "Al-Xorazmiyning 'Al-Jabr' so'zi bugungi kunda barcha tillarda (Algebra) ishlatiladi, uning nomi "
                     "esa kompyuter dasturlashining yuragi bo'lgan 'Algoritm' so'ziga asos bo'lgan.",
               'ru': 'Слова «алгебра» и «алгоритм» вошли во все мировые языки благодаря трактатам великого математика '
                     'из Хорезма.',
               'en': "Modern computer science literally runs on 'algorithms', a term directly derived from "
                     "al-Khwarizmi's Latin name 'Algoritmi'."},
  'aliases': ['al-xorazmiy', 'xorazmiy', 'al xorazmiy', 'аль-хорезми', 'хорезми', 'al-khwarizmi', 'khwarizmi']},
 {'id': 'hist_who_037',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Farg'ona vodiysi (Quva)da tug'ilgan IX asr buyuk astronomi va matematikiman.\n"
                     "2-maslahat: Qohirada Nil daryosi suvi sathini o'lchovchi 'Nilomer' (Miqyos an-Nil) gidrotexnik "
                     'inshootini yaratdim.\n'
                     "3-maslahat: 'Astronomiya asoslari' (Kitob fi usul ilm an-nujum) asarim Dante 'Ilohiy "
                     "komediya'sida va Yevropa universitetlarida asosiy darslik bo'lgan.",
               'ru': 'Подсказка 1: Великий астроном IX века, уроженец Ферганской долины (Кувы).\n'
                     'Подсказка 2: Построил знаменитый ниломер на острове Рода в Каире, действовавший более тысячи '
                     'лет.\n'
                     'Подсказка 3: Его труды по астрономии изучались в университетах средневековой Европы под именем '
                     'Альфраганус.',
               'en': 'Clue 1: 9th-century astronomer and engineer born in the Fergana Valley.\n'
                     'Clue 2: Engineered the monumental Nilometer on Roda Island in Cairo to measure the annual Nile '
                     'floods.\n'
                     'Clue 3: Known in medieval Europe as Alfraganus, his astronomical texts directly influenced Dante '
                     'Alighieri.'},
  'options': {'uz': ["Ahmad al-Farg'oniy (Alfraganus)", 'Al-Xorazmiy', 'Beruniy', 'Ibn Sino'],
              'ru': ['Ахмад аль-Фергани (Альфраганус)', 'Аль-Хорезми', 'Беруни', 'Ибн Сина'],
              'en': ['Ahmad al-Farghani (Alfraganus)', 'Al-Khwarizmi', 'Al-Biruni', 'Avicenna']},
  'correct_index': 0,
  'correct_answer': {'uz': "Ahmad al-Farg'oniy (Alfraganus)",
                     'ru': 'Ахмад аль-Фергани (Альфраганус)',
                     'en': 'Ahmad al-Farghani (Alfraganus)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Al-Farghani_monument_Fergana.jpg/640px-Al-Farghani_monument_Fergana.jpg',
  'fun_fact': {'uz': "Al-Farg'oniy 861 yilda qurgan Nilomer inshooti o'zining mustahkamligi va muhandislik aniqligi "
                     "bilan XX asrgacha — Asvon to'g'oni qurilguniga qadar benuqson xizmat qilgan.",
               'ru': 'Каирский ниломер Аль-Фергани исправно измерял уровень воды в Ниле вплоть до постройки Асуанской '
                     'плотины в XX веке.',
               'en': "Farghani's Nilometer in Cairo measured the Nile flood accurately for over a thousand years until "
                     'the Aswan High Dam.'},
  'aliases': ['al-fargoniy', 'fargoniy', 'alfraganus', 'аль-фергани', 'фергани', 'al-farghani', 'farghani']},
 {'id': 'hist_who_038',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 810 yilda Buxoroda tug'ilganman, bolalikdanoq yuz minglab hadislarni yod bilganman.\n"
                     "2-maslahat: Butun Islom olamini 16 yil kezib, 600 mingdan ortiq hadis to'pladim.\n"
                     "3-maslahat: Qur'oni Karimdan keyingi ikkinchi muqaddas manba deb tan olingan 'Al-Jome' as-Sahih' "
                     "(Sahihul Buxoriy) hadislar to'plamini tuzdim.",
               'ru': 'Подсказка 1: Родился в Бухаре в 810 году, обладал феноменальной памятью.\n'
                     'Подсказка 2: Путешествовал 16 лет по Багдаду, Мекке и Медине, собирая и проверяя предания.\n'
                     'Подсказка 3: Автор канонического свода достоверных хадисов «Сахих аль-Бухари», почитаемого во '
                     'всем исламском мире.',
               'en': 'Clue 1: Islamic scholar born in Bukhara in 810 AD with photographic memory.\n'
                     'Clue 2: Spent 16 years traveling across the Middle East vetting over 600,000 prophetic '
                     'traditions.\n'
                     "Clue 3: Compiled 'Sahih al-Bukhari', revered as the most authentic Islamic text after the Holy "
                     'Quran.'},
  'options': {'uz': ['Imom Termiziy', 'Imom al-Buxoriy (Muhammad ibn Ismoil)', 'Imom Moturidiy', 'Imom Muslim'],
              'ru': ['Имам ат-Тирмизи', 'Имам аль-Бухари (Мухаммад аль-Бухари)', 'Имам аль-Матуриди', 'Имам Муслим'],
              'en': ['Imam at-Tirmidhi', 'Imam al-Bukhari', 'Imam al-Maturidi', 'Imam Muslim']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Imom al-Buxoriy (Muhammad ibn Ismoil)',
                     'ru': 'Имам аль-Бухари (Мухаммад аль-Бухари)',
                     'en': 'Imam al-Bukhari'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Imam_Bukhari_Complex_Samarkand.jpg/640px-Imam_Bukhari_Complex_Samarkand.jpg',
  'fun_fact': {'uz': "Imom Buxoriy har bir hadisni o'z kitobiga kiritishdan oldin g'usl qilib, ikki rakat namoz o'qib, "
                     "uning sahihligiga to'liq ishonch hosil qilgan.",
               'ru': 'Мемориальный комплекс имама аль-Бухари расположен в селении Хартанг под Самаркандом, где великий '
                     'мухаддис закончил земные дни.',
               'en': 'Before committing any single Hadith to his Sahih, Imam Bukhari performed ritual ablution and '
                     "prayed two rak'ahs."},
  'aliases': ['imom buxoriy', 'al-buxoriy', 'buxoriy', 'имам аль-бухари', 'аль-бухари', 'imam al-bukhari', 'bukhari']},
 {'id': 'hist_who_039',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Tursda tug'ilganman, Saljuqiylar sultonlari Alp Arslon va Malikshohning bosh vaziri "
                     "bo'lganman.\n"
                     "2-maslahat: Bag'dod, Nishopur va Isfahonda dunyoga mashhur 'Nizomiya' dorilfununlariga asos "
                     'soldim.\n'
                     "3-maslahat: Davlat boshqaruvi va podshohlar siyosati bo'yicha nodir qo'llanma bo'lgan "
                     "'Siyosatnoma' (Siyar al-Muluk) asarini yozganman.",
               'ru': 'Подсказка 1: Великий визирь сельджукских султанов Алп-Арслана и Мелик-шаха в XI веке.\n'
                     'Подсказка 2: Создал первую в исламском мире сеть высших учебных заведений — медресе «Низамия».\n'
                     'Подсказка 3: Автор знаменитого политического трактата «Сиясат-наме» («Книга о правлении»).',
               'en': 'Clue 1: 11th-century Persian Grand Vizier to Seljuk Sultans Alp Arslan and Malik-Shah I.\n'
                     "Clue 2: Founded the prestigious network of higher learning colleges known as the 'Nizamiyya'.\n"
                     "Clue 3: Authored the classic manual of Islamic statecraft and governance, the 'Siyasatnama'."},
  'options': {'uz': ["Mahmud G'aznaviy", 'Hasan Sabboh', 'Nizomulmulk (Abu Ali Hasan)', 'Ibn Sino'],
              'ru': ['Махмуд Газневи', 'Хасан ибн Саббах', 'Низам аль-Мульк', 'Ибн Сина'],
              'en': ['Mahmud of Ghazni', 'Hassan-i Sabbah', 'Nizam al-Mulk', 'Avicenna']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Nizomulmulk (Abu Ali Hasan)', 'ru': 'Низам аль-Мульк', 'en': 'Nizam al-Mulk'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Nizam_al-Mulk_tomb_Isfahan.jpg/640px-Nizam_al-Mulk_tomb_Isfahan.jpg',
  'fun_fact': {'uz': 'Nizomulmulk 1092 yilda Makka safariga ketayotganida Hasan Sabboh boshchiligidagi hashshoshiylar '
                     "(assasinlar) fitnasi qurboni bo'lgan.",
               'ru': 'Низам аль-Мульк пал жертвой убийцы-исмаилита (ассасина), став первой громкой жертвой тайного '
                     'ордена Хасана ибн Саббаха.',
               'en': 'Nizam al-Mulk was assassinated in 1092 by an Assassin operative disguised as a Sufi dervish.'},
  'aliases': ['nizomulmulk', 'siyosatnoma', 'низам аль-мульк', 'сиясат-наме', 'nizam al-mulk']},
 {'id': 'hist_who_040',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Buyuk Saljuqiylar saltanatining ikkinchi sultoni bo'lib, 'Mard sher' laqabini "
                     'olganman.\n'
                     '2-maslahat: 1071 yilda Malazgirt (Manzikert) jangida Vizantiya imperatori Roman IV Diogenni '
                     'asirga oldim.\n'
                     "3-maslahat: Ushbu g'alaba bilan turkiy xalqlarga Onado'li (Turkiya) eshiklarini abadiy ochib "
                     'berdim.',
               'ru': 'Подсказка 1: Второй султан государства Сельджукидов, чье тюркское имя переводится как «Храбрый '
                     'лев».\n'
                     'Подсказка 2: Одержал историческую победу над византийцами при Манцикерте в 1071 году, пленив '
                     'императора Романа IV.\n'
                     'Подсказка 3: Открыл Анатолию для расселения тюркских народов и создания будущей Турции.',
               'en': "Clue 1: Second Sultan of the Great Seljuk Empire, whose Turkic name means 'Courageous Lion'.\n"
                     'Clue 2: Defeated and captured Byzantine Emperor Romanos IV Diogenes at the Battle of Manzikert '
                     'in 1071.\n'
                     'Clue 3: His historic victory permanently opened Anatolia to Turkic settlement.'},
  'options': {'uz': ["To'g'rulbek", 'Malikshoh', 'Sulton Sanjar', 'Alp Arslon (Muhammad ibn Dovud)'],
              'ru': ['Тогрул-бек', 'Мелик-шах', 'Султан Санджар', 'Алп-Арслан (Султан сельджуков)'],
              'en': ['Tughril', 'Malik-Shah I', 'Ahmad Sanjar', 'Alp Arslan (The Heroic Lion)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Alp Arslon (Muhammad ibn Dovud)',
                     'ru': 'Алп-Арслан (Султан сельджуков)',
                     'en': 'Alp Arslan (The Heroic Lion)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Alp_Arslan_statue.jpg/640px-Alp_Arslan_statue.jpg',
  'fun_fact': {'uz': 'Malazgirt jangida oq kafan kiyib jangga kirgan Alp Arslon asirga tushgan Vizantiya imperatorini '
                     'sharaf bilan kutib olgan va uni ozod qilgan.',
               'ru': 'Алп-Арслан перед битвой надел белые одежды, символизирующие саван, и поклялся погибнуть за веру.',
               'en': 'At Manzikert, Alp Arslan wore white robes as a shroud, treating the captive Roman Emperor with '
                     'magnanimous nobility.'},
  'aliases': ['alp arslon', 'malazgirt', 'алп-арслан', 'алпарслан', 'alp arslan']},
 {'id': 'hist_who_041',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Miloddan avvalgi VI asrda Orol va Kaspiy bo'yida yashagan jasur massagetlar "
                     'malikasiman.\n'
                     '2-maslahat: Ahamoniylar shohi Buyuk Kir II ning qonli bosqiniga qarshi xalqimni erkinlik uchun '
                     'boshladim.\n'
                     "3-maslahat: Kir II ni jangda tor-mor etib: 'Qonga to'ymagan eding, endi to'yguningcha ich!' deb "
                     "uning boshini qon to'ldirilgan meshga soldirdim.",
               'ru': 'Подсказка 1: Царица кочевого народа массагетов в степях Центральной Азии в VI веке до н.э.\n'
                     'Подсказка 2: Отвергла предложение персидского царя Кира II о браке и вступила с ним в '
                     'смертельную схватку.\n'
                     'Подсказка 3: Разгромила персидскую армию и бросила отрубленную голову Кира в мех с кровью.',
               'en': 'Clue 1: 6th-century BC warrior Queen of the pastoral Massagetae of Central Asia.\n'
                     'Clue 2: Resisted invasion by Cyrus the Great after he captured and caused the death of her son '
                     'Spargapises.\n'
                     'Clue 3: Decisively defeated Cyrus in battle, plunging his severed head into a wine-skin of human '
                     'blood.'},
  'options': {'uz': ["To'maris (Malika Tomiris)", 'Zarina', 'Boudikka', 'Zenobiya'],
              'ru': ['Царица Томирис', 'Царица Зарина', 'Боудикка', 'Зенобия'],
              'en': ['Queen Tomyris', 'Queen Zarinaea', 'Boudica', 'Zenobia']},
  'correct_index': 0,
  'correct_answer': {'uz': "To'maris (Malika Tomiris)", 'ru': 'Царица Томирис', 'en': 'Queen Tomyris'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tomyris_Cyrus_Rubens.jpg/640px-Tomyris_Cyrus_Rubens.jpg',
  'fun_fact': {'uz': "Geredotning yozishicha, To'maris va Kir II o'rtasidagi to'qnashuv qadimgi dunyo varvarlari "
                     "o'rtasidagi eng shafqatsiz va qonli jang bo'lgan.",
               'ru': 'Историк Геродот описал битву Томирис с Киром Великим как самое жестокое сражение античного мира.',
               'en': 'Herodotus called the battle between Tomyris and Cyrus the fiercest ever fought between non-Greek '
                     'peoples.'},
  'aliases': ['tomiris', 'tomaris', 'malika tomiris', 'томирис', 'царица томирис', 'tomyris']},
 {'id': 'hist_who_042',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Mil. avv. IV asrda yashagan jasur so'g'd sarkardasiman.\n"
                     "2-maslahat: Aleksandr Makedonskiy qo'shinlariga qarshi So'g'diyona va Baqtriyada 3 yil davomida "
                     '(mil. avv. 329-327) partizanlik urushini olib bordim.\n'
                     "3-maslahat: Politimet (Zarafshon) daryosi bo'yida Aleksandrning eng sara sarkardalari boshliq "
                     "makedon qo'shinini to'liq tor-mor qildim.",
               'ru': 'Подсказка 1: Согдийский военачальник IV века до н.э., возглавивший восстание против македонян.\n'
                     'Подсказка 2: Вел успешную партизанскую войну против войск Александра Македонского в '
                     'Мавераннахре.\n'
                     'Подсказка 3: Уничтожил греческий отряд на реке Политимет (Зеравшан) — единственное поражение '
                     'войск Александра.',
               'en': 'Clue 1: Sogdian military chieftain who led a widespread uprising against Alexander the Great.\n'
                     'Clue 2: Waged a three-year guerilla campaign across Sogdiana and Bactria (329-327 BC).\n'
                     'Clue 3: Wiped out an entire Macedonian division at the Battle of the Polytimetus River.'},
  'options': {'uz': ['Oksiat', 'Spitamen', 'Bess', 'Muqanna'],
              'ru': ['Оксиарт', 'Спитамен', 'Бесс', 'Муканна'],
              'en': ['Oxyartes', 'Spitamenes', 'Bessus', 'Muqanna']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Spitamen', 'ru': 'Спитамен', 'en': 'Spitamenes'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Spitamenes_monument_Samarkand.jpg/640px-Spitamenes_monument_Samarkand.jpg',
  'fun_fact': {'uz': 'Spitamenning qizi Apama Aleksandrning eng yaqin safdoshi Salavk I Nikatorga turmushga chiqqan va '
                     'qudratli Salavkiylar sulolasining onasiga aylangan.',
               'ru': 'Дочь Спитамена Апама вышла замуж за Селевка I Никатора и стала прародительницей династии '
                     'Селевкидов.',
               'en': "Spitamenes's daughter Apama married Seleucus I Nicator, becoming the ancestral mother of the "
                     'Seleucid Dynasty.'},
  'aliases': ['spitamen', 'spitamenes', 'спитамен']},
 {'id': 'hist_who_043',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Asl ismim Hoshim ibn Hakim bo'lib, Merv yaqinida tug'ilganman.\n"
                     "2-maslahat: Yuzimga yashil ipak niqob (yopinchiq) taqib yurganim sababli 'Muqanna' (Niqobdor) "
                     'nomini oldim.\n'
                     "3-maslahat: Movarounnahrda Abbosiylar xalifaligiga qarshi 'Oq kiyimlilar' qo'zg'oloniga "
                     '(776-783) rahbarlik qildim.',
               'ru': 'Подсказка 1: Настоящее имя — Хашим ибн Хаким, уроженец Мерва.\n'
                     'Подсказка 2: Носил шелковое покрывало на лице, за что получил прозвище аль-Муканна '
                     '(«закутанный»).\n'
                     'Подсказка 3: Предводитель восстания «людей в белых одеждах» в Согде против Арабского халифата.',
               'en': 'Clue 1: Born Hashim ibn Hakim near Merv in 8th-century Central Asia.\n'
                     "Clue 2: Wore a golden mask or silk veil over his face, earning the epithet 'Al-Muqanna' (The "
                     'Veiled One).\n'
                     "Clue 3: Led the massive 'White Raiment' rebellion against the Abbasid Caliphate in Transoxiana."},
  'options': {'uz': ['Abu Muslim', 'Bobak', 'Muqanna (Hoshim ibn Hakim)', 'Rofe ibn Lays'],
              'ru': ['Абу Муслим', 'Бабек', 'Муканна («Покрытый покрывалом»)', 'Рафи ибн Лейс'],
              'en': ['Abu Muslim', 'Babak Khorramdin', 'Al-Muqanna (The Veiled Prophet)', 'Rafi ibn al-Layth']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Muqanna (Hoshim ibn Hakim)',
                     'ru': 'Муканна («Покрытый покрывалом»)',
                     'en': 'Al-Muqanna (The Veiled Prophet)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Muqanna_rebellion_miniature.jpg/640px-Muqanna_rebellion_miniature.jpg',
  'fun_fact': {'uz': "Muqanna Sanom qal'asi qamalida dushman qo'liga tushmaslik uchun o'zini yonayotgan olovli "
                     "tandirga tashlab halok bo'lgan deb rivoyat qilinadi.",
               'ru': 'Легенда гласит, что при падении крепости Санам Муканна бросился в раскаленную печь, чтобы '
                     'исчезнуть и утвердить миф о своем божественном вознесении.',
               'en': 'According to legend, when his fortress of Sanam was breached, Muqanna threw himself into a fiery '
                     'furnace to leave no mortal remains.'},
  'aliases': ['muqanna', 'oq kiyimlilar', 'hoshim ibn hakim', 'муканна', 'al-muqanna']},
 {'id': 'hist_who_044',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: G'aznaviylar davlatining eng buyuk hukmdori bo'lib, X asr oxirida taxtga o'tirdim.\n"
                     "2-maslahat: Islom tarixida birinchi bo'lib rasman 'Sulton' unvonini qabul qildim.\n"
                     '3-maslahat: Hindistonga 17 marta harbiy yurish qilib, Somnat ibodatxonasini zabt etdim va '
                     "Beruniyni G'azna saroyiga jalb qildim.",
               'ru': 'Подсказка 1: Правитель державы Газневидов (998–1030), сделавший столицу Газни центром науки.\n'
                     'Подсказка 2: Первый правитель в исламской истории, принявший титул султана от халифа Багдада.\n'
                     'Подсказка 3: Совершил 17 победоносных походов в Северную Индию, захватив колоссальные богатства '
                     'храма Сомнатх.',
               'en': 'Clue 1: Most prominent ruler of the Ghaznavid Empire from 998 to 1030.\n'
                     "Clue 2: First ruler in Islamic history to carry the official sovereign title of 'Sultan'.\n"
                     'Clue 3: Launched 17 expeditions into Northern India, sacking Somnath and patronizing polymath '
                     'al-Biruni.'},
  'options': {'uz': ['Sabuktegin', 'Alptigin', "Mas'ud G'aznaviy", "Sulton Mahmud G'aznaviy"],
              'ru': ['Себук-тегин', 'Алп-тегин', 'Масуд Газневи', 'Султан Махмуд Газневи'],
              'en': ['Sabuktigin', 'Alptigin', "Mas'ud I of Ghazni", 'Mahmud of Ghazni']},
  'correct_index': 3,
  'correct_answer': {'uz': "Sulton Mahmud G'aznaviy", 'ru': 'Султан Махмуд Газневи', 'en': 'Mahmud of Ghazni'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Mahmud_of_Ghazni_miniature.jpg/640px-Mahmud_of_Ghazni_miniature.jpg',
  'fun_fact': {'uz': "Mahmud G'aznaviy o'z saroyiga 400 dan ortiq shoir va olimlarni to'plagan; Firdavsiy o'zining "
                     "shoh 'Shohnoma' dostonini aynan unga taqdim etgan.",
               'ru': 'При дворе Махмуда в Газни работали величайшие умы эпохи, включая автора поэмы «Шахнаме» Фирдоуси '
                     'и ученого-энциклопедиста Беруни.',
               'en': 'Mahmud assembled over 400 poets at his court, including Ferdowsi who dedicated the epic '
                     "'Shahnameh' to him."},
  'aliases': ['mahmud gaznaviy', 'gaznaviy', 'махмуд газневи', 'газневи', 'mahmud of ghazni']},
 {'id': 'hist_who_045',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Somoniylar sulolasining eng qudratli amiri bo'lib, Buxoroni poytaxtga aylantirdim.\n"
                     "2-maslahat: 900 yilda Balx yaqinida Amr ibn Lays qo'shinini tor-mor etib, Movarounnahr va "
                     'Xurosonni yagona mustaqil davlatga birlashtirdim.\n'
                     "3-maslahat: 'Buxoroning devori menman' deb shahar atrofiga mudofaa devori qurdirmaganman; "
                     "Buxorodagi mashhur pishiq g'ishtli maqbaram saqlanib qolgan.",
               'ru': 'Подсказка 1: Основатель сильного централизованного государства Саманидов в Средней Азии.\n'
                     'Подсказка 2: Разгромил Саффаридов и объединил Мавераннахр и Хорасан под властью Бухары.\n'
                     'Подсказка 3: Говорил: «Пока я жив, я сам — стена Бухары»; его кирпичный мавзолей IX века — '
                     'шедевр архитектуры.',
               'en': 'Clue 1: Greatest Amir of the Samanid dynasty who united Transoxiana and Khorasan.\n'
                     'Clue 2: Defeated the Saffarids at Balkh in 900 AD, making Bukhara a flourishing capital.\n'
                     "Clue 3: Famously declared 'As long as I live, I am the wall of Bukhara'; his brick mausoleum "
                     'still stands intact.'},
  'options': {'uz': ['Ismoil Somoniy', 'Nasr I Somoniy', 'Ahmad Somoniy', 'Asad ibn Somon'],
              'ru': ['Исмаил Самани', 'Наср I', 'Ахмад Самани', 'Асад ибн Саман'],
              'en': ['Ismail Samani', 'Nasr I', 'Ahmad Samani', 'Asad ibn Saman']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Ismoil Somoniy', 'ru': 'Исмаил Самани', 'en': 'Ismail Samani'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Samanid_Mausoleum_Bukhara.jpg/640px-Samanid_Mausoleum_Bukhara.jpg',
  'fun_fact': {'uz': "Buxorodagi Ismoil Somoniy maqbarasi O'rta Osiyoda pishiq g'ishtdan qurilgan va bugungi kungacha "
                     "to'liq saqlanib qolgan eng qadimgi me'moriy yodgorlikdir.",
               'ru': 'Мавзолей Саманидов в Бухаре — древнейший сохранившийся шедевр кирпичной исламской архитектуры в '
                     'Центральной Азии.',
               'en': 'The Samanid Mausoleum in Bukhara is the earliest surviving monument of Islamic brick '
                     'architecture in Central Asia.'},
  'aliases': ['ismoil somoniy', 'somoniy', 'исмаил самани', 'самани', 'ismail samani']},
 {'id': 'hist_who_046',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Ozarbayjon va Eron tog'larida Abbosiylar xalifaligiga qarshi kurashgan ozodlik "
                     'yetakchisiman.\n'
                     "2-maslahat: 'Xurramiylar' (Qizil kiyimlilar) harakatiga 20 yildan ortiq boshchilik qildim.\n"
                     "3-maslahat: O'tib bo'lmas Bazz qal'asidan turib arab xalifalari qo'shinlariga ketma-ket "
                     'qaqshatqich zarbalar berdim.',
               'ru': 'Подсказка 1: Вождь антиарабского освободительного движения хуррамитов в Азербайджане и Иране.\n'
                     'Подсказка 2: На протяжении более 20 лет успешно сдерживал натиск армий халифата из крепости '
                     'Базз.\n'
                     'Подсказка 3: Национальный герой, казненный в Самарре в 838 году, но не склонивший головы.',
               'en': 'Clue 1: Persian/Azerbaijani military leader who spearheaded the Khurramite uprising against the '
                     'Abbasids.\n'
                     'Clue 2: Held the mountain fortress of Badd against imperial armies for over two decades.\n'
                     'Clue 3: Celebrated as a fearless champion of national independence who died defiantly in 838 '
                     'AD.'},
  'options': {'uz': ['Muqanna', 'Bobak Xurramiy (Bobak)', 'Abu Muslim', 'Afshin'],
              'ru': ['Муканна', 'Бабек (вождь хуррамитов)', 'Абу Муслим', 'Афшин'],
              'en': ['Muqanna', 'Babak Khorramdin', 'Abu Muslim', 'Afshin']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Bobak Xurramiy (Bobak)', 'ru': 'Бабек (вождь хуррамитов)', 'en': 'Babak Khorramdin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Babak_Khorramdin_Castle.jpg/640px-Babak_Khorramdin_Castle.jpg',
  'fun_fact': {'uz': "Bobak qatl etilayotganda kesilgan qo'li qonini yuziga surtib: 'Dushmanlarim qon yo'qotishdan "
                     "oqargan yuzimni qo'rqdi deb o'ylamasin' degan.",
               'ru': 'Перед казнью Бабек омыл лицо собственной кровью, чтобы враги не подумали, что он побледнел от '
                     'страха.',
               'en': 'At his execution, Babak smeared his face with his own blood so his enemies would not think he '
                     'had paled from fear.'},
  'aliases': ['bobak', 'bobak xurramiy', 'бабек', 'хуррамиты', 'babak', 'babak khorramdin']},
 {'id': 'hist_who_047',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Oddiy cho'pon oilasidan chiqib, Afshoriylar sulolasiga asos solgan fors "
                     'hukmdoriman.\n'
                     "2-maslahat: 'Sharq Napoleoni' va 'Osiyo qahramoni' deb atalgan harbiy dahoman.\n"
                     "3-maslahat: 1739 yilda Dehlini egallab, Boburiylar xazinasidan 'Ko'hi Nur' va 'Daryoyi Nur' "
                     "olmoslarini, shuningdek 'Tovus taxti'ni qo'lga kiritdim.",
               'ru': 'Подсказка 1: Выходец из скромного тюркского племени афшаров, ставший шахиншахом Персии.\n'
                     'Подсказка 2: Европейские историки прозвали меня «Мечом Персии» и «Наполеоном Востока» за '
                     'блестящую тактику.\n'
                     'Подсказка 3: Разграбил Дели в 1739 году, увезя в Иран Павлиний трон и легендарный алмаз '
                     '«Кохинур».',
               'en': "Clue 1: Brilliant Turkic military commander who founded Iran's Afsharid dynasty.\n"
                     "Clue 2: Known as the 'Sword of Persia' and the 'Napoleon of Asia' for his unmatched tactical "
                     'mobility.\n'
                     'Clue 3: Sacked Delhi in 1739, carrying off the Peacock Throne and the Koh-i-Noor and '
                     'Daria-i-Noor diamonds.'},
  'options': {'uz': ['Shoh Abbos I', 'Shoh Ismoil I', 'Nodirshoh Afshor', 'Karimxon Zand'],
              'ru': ['Шах Аббас I', 'Шах Исмаил I', 'Надир-шах Афшар', 'Карим-хан Зенд'],
              'en': ['Shah Abbas I', 'Shah Ismail I', 'Nader Shah Afshar', 'Karim Khan Zand']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Nodirshoh Afshor', 'ru': 'Надир-шах Афшар', 'en': 'Nader Shah Afshar'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Nader_Shah_portrait.jpg/640px-Nader_Shah_portrait.jpg',
  'fun_fact': {'uz': "Nodirshoh Dehlidan olib kelgan boyliklar shunchalik ko'p ediki, u o'z davlatida soliqlarni "
                     'ketma-ket 3 yilga butunlay bekor qilgan.',
               'ru': 'Богатств, захваченных Надир-шахом в Индии, было так много, что он освободил жителей Персии от '
                     'налогов на три года.',
               'en': "Nader Shah's plunder from Delhi was so staggering that he suspended all taxation in Persia for "
                     'three continuous years.'},
  'aliases': ['nodirshoh', 'nodirshoh afshor', 'надир-шах', 'надир шах', 'nader shah']},
 {'id': 'hist_who_048',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Boburiylar sulolasining beshinchi hukmdori bo'lib, 'Dunyo podshohi' unvonini "
                     'olganman.\n'
                     "2-maslahat: Dehlidagi mashhur Qizil qal'a (Lal Qila) va Jome masjidini barpo ettirdim.\n"
                     "3-maslahat: Suyukli rafiqam Mumtoz Mahal xotirasiga oq marmardan dunyo mo'jizasi — Toj Mahal "
                     'maqbarasini qurdirdim.',
               'ru': 'Подсказка 1: Пятый император Великих Моголов, чье имя означает «Повелитель мира».\n'
                     'Подсказка 2: Построил Красный форт и Соборную мечеть в Дели в период наивысшего расцвета '
                     'архитектуры.\n'
                     'Подсказка 3: Создал шедевр мировой архитектуры — мавзолей Тадж-Махал в память о любимой жене '
                     'Мумтаз-Махал.',
               'en': "Clue 1: Fifth Mughal Emperor of India whose regnal name translates to 'King of the World'.\n"
                     'Clue 2: Built the Red Fort and Jama Masjid in Delhi during the golden age of Mughal '
                     'architecture.\n'
                     'Clue 3: Commissioned the world wonder Taj Mahal in Agra as an eternal mausoleum for his wife '
                     'Mumtaz Mahal.'},
  'options': {'uz': ['Akbarshoh', 'Jahongirshoh', 'Avrangzeb', 'Shoh Jahon (Boburiy podshoh)'],
              'ru': ['Акбар Великий', 'Джахангир', 'Аурангзеб', 'Шах-Джахан (правитель Моголов)'],
              'en': ['Akbar the Great', 'Jahangir', 'Aurangzeb', 'Shah Jahan']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Shoh Jahon (Boburiy podshoh)', 'ru': 'Шах-Джахан (правитель Моголов)', 'en': 'Shah Jahan'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Shah_Jahan_on_a_terrace.jpg/640px-Shah_Jahan_on_a_terrace.jpg',
  'fun_fact': {'uz': "Shoh Jahon umrining so'nggi 8 yilini o'z o'g'li Avrangzeb tomonidan Agra qal'asiga qamab "
                     "qo'yilgan holda, derazadan Toj Mahalga termulib o'tkazgan.",
               'ru': 'Свергнутый сыном Аурангзебом, Шах-Джахан провел последние годы в заключении в форте Агры, глядя '
                     'на Тадж-Махал.',
               'en': 'Imprisoned in Agra Fort by his son Aurangzeb, Shah Jahan spent his final eight years gazing '
                     'across the river at the Taj Mahal.'},
  'aliases': ['shoh jahon', 'shohjahon', 'toj mahal qurdirgan', 'шах-джахан', 'шахджахан', 'shah jahan']},
 {'id': 'hist_who_049',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Boburning nabirasi bo'lib, 13 yoshimda taxtga o'tirganman va 49 yil hukmronlik "
                     'qilganman.\n'
                     "2-maslahat: Hindularga nisbatan 'jizya' solig'ini bekor qildim va dinlararo bag'rikenglik "
                     'siyosatini (Sulhi kul) yuritdim.\n'
                     "3-maslahat: Barcha dinlarni birlashtiruvchi 'Dini ilohiy' ta'limotini yaratdim va Boburiylar "
                     'imperiyasi hududini uch barobar kengaytirdim.',
               'ru': 'Подсказка 1: Внук Бабура, унаследовавший трон Моголов в 13 лет и правивший полвека.\n'
                     'Подсказка 2: Отменил налог на немусульман (джизью), привлекал индусов к управлению и женился на '
                     'раджпутской принцессе.\n'
                     'Подсказка 3: Создал синкретическую религию «Дин-и илахи» («Божественная вера») во имя '
                     'религиозного мира.',
               'en': 'Clue 1: Grandson of Babur who ascended the Mughal throne at thirteen and ruled for nearly 50 '
                     'years.\n'
                     "Clue 2: Abolished the jizya tax on non-Muslims and promoted universal tolerance ('Sulh-i-kul').\n"
                     'Clue 3: Expanded Mughal borders across most of the Indian subcontinent and introduced the '
                     "syncretic faith 'Din-i Ilahi'."},
  'options': {'uz': ['Jaloliddin Muhammad Akbar (Akbarshoh)', 'Bobur', 'Humoyun', 'Shoh Jahon'],
              'ru': ['Акбар I Великий', 'Бабур', 'Хумаюн', 'Шах-Джахан'],
              'en': ['Akbar the Great', 'Babur', 'Humayun', 'Shah Jahan']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Jaloliddin Muhammad Akbar (Akbarshoh)', 'ru': 'Акбар I Великий', 'en': 'Akbar the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Akbar_holding_court.jpg/640px-Akbar_holding_court.jpg',
  'fun_fact': {'uz': "Akbarshoh o'qish va yozishni bilmagan (disleksiyadan aziyat chekgan), ammo har kuni unga "
                     "kitoblar o'qib berilgan va u 24 000 jildlik ulkan kutubxona to'plagan.",
               'ru': 'Не умея читать из-за дислексии, Акбар обладал феноменальной памятью и собрал крупнейшую '
                     'библиотеку в 24 000 рукописей.',
               'en': 'Though illiterate due to severe dyslexia, Akbar amassed an imperial library of 24,000 volumes, '
                     'having texts read aloud to him daily.'},
  'aliases': ['akbar', 'akbarshoh', 'akbar buyuk', 'акбар великий', 'акбар', 'akbar the great']},
 {'id': 'hist_who_050',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Abbosiylar xalifaligining beshinchi xalifasi bo'lib, VIII asr oxirida Bag'dodni "
                     'boshqarganman.\n'
                     "2-maslahat: Bag'dodda ilm-fan markazi bo'lgan 'Bayt ul-Hikma' (Donishmandlar uyi)ga asos "
                     'solishni boshladim.\n'
                     "3-maslahat: 'Ming bir kecha' ertaklarining markaziy qahramoniman; Buyuk Karlga mexanik soat va "
                     "oq fil sovg'a yuborganman.",
               'ru': 'Подсказка 1: Пятый халиф из династии Аббасидов, правивший Багдадом в период наивысшего расцвета '
                     '(786–809).\n'
                     'Подсказка 2: Главный исторический персонаж сказок «Тысяча и одна ночь», гулявший инкогнито по '
                     'улицам ночного города.\n'
                     'Подсказка 3: Отправил императору Карлу Великому посольство с дарами, включая водяные часы и '
                     'белого слона Абуль-Аббаса.',
               'en': 'Clue 1: Fifth Abbasid Caliph whose 786-809 reign marked the golden zenith of Baghdad.\n'
                     "Clue 2: Immortalized as the nocturnal wandering caliph in the 'One Thousand and One Nights'.\n"
                     'Clue 3: Established the foundations of the House of Wisdom and sent Charlemagne a water clock '
                     'and an albino elephant.'},
  'options': {'uz': ['Al-Mansur', 'Horun ar-Rashid', "Al-Ma'mun", 'Al-Mutavakkil'],
              'ru': ['Аль-Мансур', 'Харун ар-Рашид', 'Аль-Мамун', 'Аль-Мутаваккиль'],
              'en': ['Al-Mansur', 'Harun al-Rashid', "Al-Ma'mun", 'Al-Mutawakkil']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Horun ar-Rashid', 'ru': 'Харун ар-Рашид', 'en': 'Harun al-Rashid'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Harun_al-Rashid_receiving_delegation.jpg/640px-Harun_al-Rashid_receiving_delegation.jpg',
  'fun_fact': {'uz': "Horun ar-Rashid tunda oddiy savdogar libosini kiyib, vaziri Ja'far Barmakiy bilan birga Bag'dod "
                     'bozorlarini aylanib odamlar dardini eshitgan.',
               'ru': 'Харун ар-Рашид переодевался в платье простолюдина и инкогнито бродил по ночному Багдаду, чтобы '
                     'лично узнавать нужды горожан.',
               'en': 'Harun famously donned merchant disguises to wander the night markets of Baghdad with his vizier '
                     'Jafar.'},
  'aliases': ['horun ar-rashid', 'horun ar rashid', 'харун ар-рашид', 'харун ар рашид', 'harun al-rashid']},
 {'id': 'hist_who_051',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Umaviylar xalifaligining berber millatiga mansub sarkardasiman.\n'
                     "2-maslahat: 711 yilda kemalarda Shimoliy Afrikadan Ispaniyaga o'tib, kemalarimni yoqishga buyruq "
                     'berganman.\n'
                     "3-maslahat: Qadimgi Kalpe qoyasi mening nomim bilan 'Jabal at-Toriq' (Gibraltar) deb atalgan.",
               'ru': 'Подсказка 1: Полководец Омейядов берберского происхождения, начавший завоевание Испании в 711 '
                     'году.\n'
                     'Подсказка 2: По легенде, приказал сжечь корабли после высадки, отрезав войску путь к '
                     'отступлению.\n'
                     'Подсказка 3: В честь меня названа Гибралтарская скала — «Джабаль ат-Тарик» («Гора Тарика»).',
               'en': 'Clue 1: Berber Muslim general who led the 711 AD conquest of Visigothic Hispania.\n'
                     "Clue 2: Famously burned his landing boats, telling his army: 'The sea is behind you, and the "
                     "enemy is before you'.\n"
                     "Clue 3: The Rock of Gibraltar is named in his honor ('Jabal Tariq' meaning Mount of Tariq)."},
  'options': {'uz': ['Muso ibn Nusayr', 'Yusuf ibn Toshfin', 'Toriq ibn Ziyod', 'Abdurahmon I'],
              'ru': ['Муса ибн Нусайр', 'Юсуф ибн Ташфин', 'Тарик ибн Зияд', 'Абд ар-Рахман I'],
              'en': ['Musa ibn Nusayr', 'Yusuf ibn Tashfin', 'Tariq ibn Ziyad', 'Abd al-Rahman I']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Toriq ibn Ziyod', 'ru': 'Тарик ибн Зияд', 'en': 'Tariq ibn Ziyad'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tariq_ibn_Ziyad_Gibraltar.jpg/640px-Tariq_ibn_Ziyad_Gibraltar.jpg',
  'fun_fact': {'uz': 'Toriq ibn Ziyod Gvadalete jangida vestgotlar qiroli Roderixni tor-mor qilib, Pireney '
                     'yarimorolida 800 yillik Andalusiya madaniyatini boshlab berdi.',
               'ru': 'Победа Тарика при Гвадалете положила начало восьми векам мусульманского присутствия в Испании '
                     '(Аль-Андалус).',
               'en': "Tariq's victory at Guadalete initiated nearly eight centuries of Moorish culture in Islamic "
                     'Iberia (Al-Andalus).'},
  'aliases': ['toriq', 'toriq ibn ziyod', 'gibraltar', 'тарик ибн зияд', 'гибралтар', 'tariq ibn ziyad']},
 {'id': 'hist_who_052',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Islom tarixidagi eng yirik sarkarda bo'lib, hayotimda 50 dan ortiq jangda hech "
                     'qachon yengilmaganman.\n'
                     "2-maslahat: Payg'ambar Muhammad (s.a.v.) menga 'Sayfulloh' (Allohning qilichi) degan faxriy nom "
                     'berganlar.\n'
                     '3-maslahat: 636 yilda Yarmuk jangida Vizantiyaning 100 minglik armiyasini tor-mor etdim.',
               'ru': 'Подсказка 1: Выдающийся полководец раннего ислама, не потерпевший ни одного поражения в десятках '
                     'битв.\n'
                     'Подсказка 2: Получил почетное прозвище «Сейфуллах» («Меч Аллаха») за бесстрашие и тактический '
                     'гений.\n'
                     'Подсказка 3: Одержал решающую победу над Византией при Ярмуке, решившую судьбу Сирии и '
                     'Палестины.',
               'en': 'Clue 1: Legendary early Islamic commander undefeated in over 50 pitched battles.\n'
                     "Clue 2: Bestowed the title 'Sayf Allah al-Maslul' (The Drawn Sword of God) by Prophet Muhammad.\n"
                     'Clue 3: Masterminded the historic encirclement victory over Byzantine forces at Yarmouk in 636 '
                     'AD.'},
  'options': {'uz': ['Amr ibn Os', "Sa'd ibn Abu Vaqqos", 'Abu Ubayda', 'Xolid ibn Valid (Sayfulloh)'],
              'ru': ['Амр ибн аль-Ас', 'Саад ибн Абу Ваккас', 'Абу Убайда', 'Халид ибн аль-Валид (Сейфуллах)'],
              'en': ['Amr ibn al-As', "Sa'd ibn Abi Waqqas", 'Abu Ubaidah', 'Khalid ibn al-Walid (Sword of Allah)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Xolid ibn Valid (Sayfulloh)',
                     'ru': 'Халид ибн аль-Валид (Сейфуллах)',
                     'en': 'Khalid ibn al-Walid (Sword of Allah)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Khalid_ibn_Walid_Mosque.jpg/640px-Khalid_ibn_Walid_Mosque.jpg',
  'fun_fact': {'uz': 'Xolid ibn Valid vafot etayotganda butun tanasida jarohatsiz bir qarich ham joy qolmaganini, ammo '
                     "to'shakda vafot etayotganidan afsusdaligini aytgan.",
               'ru': 'На теле полководца не было места без следов ран от мечей и копий, но он умер в своей постели в '
                     'Хомсе в 642 году.',
               'en': 'On his deathbed in Homs, Khalid wept that despite bearing wounds across his entire body, he was '
                     'dying peacefully in bed.'},
  'aliases': ['xolid ibn valid', 'sayfulloh', 'халид ибн аль-валид', 'меч аллаха', 'khalid ibn al-walid']},
 {'id': 'hist_who_053',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Rim sarkardasi bo'lib, Karfagenga qarshi Ikkinchi Puni urushida armiyaga boshchilik "
                     'qildim.\n'
                     '2-maslahat: Mil. avv. 202 yilda Zama jangida afsonaviy Gannibal Barka ustidan hal qiluvchi '
                     "g'alabaga erishdim.\n"
                     "3-maslahat: Ushbu g'alabadan so'ng Rim Senati menga 'Afrikalik' (Afrikanus) faxriy unvonini "
                     'berdi.',
               'ru': 'Подсказка 1: Римский полководец, изучивший тактику Ганнибала и применивший ее против него '
                     'самого.\n'
                     'Подсказка 2: Разгромил войска Карфагена в битве при Заме в 202 году до н.э., завершив Вторую '
                     'Пуническую войну.\n'
                     'Подсказка 3: Первый римлянин, получивший триумфальное прозвище по имени покоренного континента — '
                     '«Африканский».',
               'en': 'Clue 1: Roman general and statesman during the Second Punic War.\n'
                     "Clue 2: Neutralized Hannibal's war elephants and crushed the Carthaginian army at Zama in 202 "
                     'BC.\n'
                     "Clue 3: Awarded the agnomen 'Africanus' to commemorate his decisive conquest."},
  'options': {'uz': ['Sitsipion Afrikalik (Publiy Korneliy)', 'Yuliy Sezar', 'Katon Katta', 'Fabiy Maksim'],
              'ru': ['Сципион Африканский', 'Юлий Цезарь', 'Катон Старший', 'Фабий Максим'],
              'en': ['Scipio Africanus', 'Julius Caesar', 'Cato the Elder', 'Fabius Maximus']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Sitsipion Afrikalik (Publiy Korneliy)',
                     'ru': 'Сципион Африканский',
                     'en': 'Scipio Africanus'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Scipio_Africanus_Bust_Naples.jpg/640px-Scipio_Africanus_Bust_Naples.jpg',
  'fun_fact': {'uz': "Sitsipion o'z vatandoshlarining noshukurligidan ranjib, o'z qabriga: 'Noshukur vatan, sen hatto "
                     "mening suyaklarimga ham ega bo'lolmaysan!' deb yozdirgan.",
               'ru': 'Разочарованный политическими нападками сограждан, Сципион завещал выбить на надгробии: '
                     '«Неблагодарное отечество, ты не получишь моих костей».',
               'en': 'Bitter over accusations from political rivals, Scipio withdrew from Rome, ordering inscribed on '
                     "his tomb: 'Ungrateful fatherland, you shall not have my bones'."},
  'aliases': ['sitsipion', 'sitsipion afrikalik', 'сципион', 'сципион африканский', 'scipio', 'scipio africanus']},
 {'id': 'hist_who_054',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Frakiyalik jangchi bo'lib, Kapuyadagi gladiatorlar maktabida qul qilib "
                     'saqlanganman.\n'
                     "2-maslahat: Mil. avv. 73 yilda oshxona pichoqlari bilan qochib, Vezuviy vulqoni cho'qqisida "
                     "qo'zg'olon boshladim.\n"
                     "3-maslahat: Rim imperiyasini larzaga solgan 120 ming kishilik qullar qo'zg'olonining afsonaviy "
                     'yetakchisiman.',
               'ru': 'Подсказка 1: Фракиец, попавший в римский плен и ставший гладиатором в Капуе.\n'
                     'Подсказка 2: Сбежал с товарищами на гору Везувий и возглавил крупнейшее восстание рабов в '
                     'древней истории.\n'
                     'Подсказка 3: Два года громил консульские армии Рима, став символом борьбы угнетенных за свободу.',
               'en': 'Clue 1: Thracian gladiator trained in the ludus of Lentulus Batiatus in Capua.\n'
                     'Clue 2: Escaped with 70 gladiators, taking refuge on Mount Vesuvius to launch a rebellion.\n'
                     'Clue 3: Led over 100,000 escaped slaves during the Third Servile War against Rome (73-71 BC).'},
  'options': {'uz': ['Kriks', 'Spartak', 'Enomay', 'Krass'],
              'ru': ['Крикс', 'Спартак', 'Эномай', 'Красс'],
              'en': ['Crixus', 'Spartacus', 'Oenomaus', 'Marcus Licinius Crassus']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Spartak', 'ru': 'Спартак', 'en': 'Spartacus'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Spartacus_Foyatier_Louvre.jpg/640px-Spartacus_Foyatier_Louvre.jpg',
  'fun_fact': {'uz': "Spartak armiyasi rimliklar tomonidan mag'lub etilgach, 6000 nafar asir qul Rimdan Kapuyagacha "
                     "bo'lgan Appiy yo'li bo'ylab xochga mixlangan.",
               'ru': 'После гибели Спартака в бою Марк Красс распял шесть тысяч пленных повстанцев вдоль Аппиевой '
                     'дороги.',
               'en': "Following Spartacus's final defeat in 71 BC, Crassus crucified 6,000 captured slaves along the "
                     '200 km Appian Way.'},
  'aliases': ['spartak', 'спартак', 'spartacus']},
 {'id': 'hist_who_055',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Yuliy Sezarning jiyani va asrab olgan o'g'li bo'lib, Aksiy jangida Mark Antoniyni "
                     'yengdim.\n'
                     "2-maslahat: Rim respublikasiga barham berib, 200 yillik 'Rim tinchligi' (Pax Romana) davrini "
                     'boshlab berdim.\n'
                     "3-maslahat: Rim tarixidagi birinchi imperator (Princeps) bo'ldim; avgust oyi mening sharafimga "
                     'atalgan.',
               'ru': 'Подсказка 1: Внучатый племянник и наследник Юлия Цезаря, победивший Антония и Клеопатру.\n'
                     'Подсказка 2: Первый римский император (принцепс), установивший эпоху «Римского мира» (Pax '
                     'Romana).\n'
                     'Подсказка 3: Говорил, что «принял Рим глиняным, а оставил мраморным»; месяц август назван в его '
                     'честь.',
               'en': 'Clue 1: Great-nephew and adopted heir of Julius Caesar, defeating Antony and Cleopatra at '
                     'Actium.\n'
                     "Clue 2: Founded the Principate, inaugurating two centuries of peace known as 'Pax Romana'.\n"
                     "Clue 3: First Roman Emperor, boasting he 'found Rome a city of brick and left it a city of "
                     "marble'; August is named for him."},
  'options': {'uz': ['Yuliy Sezar', 'Tiberiy', 'Oktavian Avgust', 'Mark Antoniy'],
              'ru': ['Юлий Цезарь', 'Тиберий', 'Октавиан Август', 'Марк Антоний'],
              'en': ['Julius Caesar', 'Tiberius', 'Augustus (Octavian)', 'Mark Antony']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Oktavian Avgust', 'ru': 'Октавиан Август', 'en': 'Augustus (Octavian)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Statue-Augustus.jpg/640px-Statue-Augustus.jpg',
  'fun_fact': {'uz': "Avgust 41 yil imperatorlik qilgan bo'lib, o'lim to'shagida do'stlariga: 'Agar men hayot "
                     "komediyasida rolimni yaxshi o'ynagan bo'lsam, qarsak chaling!' degan.",
               'ru': 'Последними словами Августа к друзьям были: «Коль хорошо сыграли мы комедию, похлопайте и '
                     'проводите нас аплодисментами».',
               'en': "On his deathbed in 14 AD, Augustus famously asked his friends: 'Have I played my part well in "
                     "the comedy of life? Then applaud as I exit.'"},
  'aliases': ['oktavian', 'avgust', 'oktavian avgust', 'октавиан август', 'август', 'augustus', 'octavian']},
 {'id': 'hist_who_056',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Rimning 'Besh yaxshi imperatori'ning so'nggisi bo'lib, 161-180 yillarda hukmronlik "
                     'qilganman.\n'
                     "2-maslahat: Dunay bo'yida german qabilalariga qarshi harbiy chodirda stoisizm falsafasiga oid "
                     'shaxsiy kundaligimni yozdim.\n'
                     "3-maslahat: 'O'z-o'zim bilan' (Meditations) asari muallifi bo'lgan 'Taxtdagi faylasuf'man.",
               'ru': 'Подсказка 1: Римский император из династии Антонинов, последний из «Пяти хороших императоров».\n'
                     'Подсказка 2: Провел годы в военных походах на Дунае, сдерживая варваров во время Маркоманских '
                     'войн.\n'
                     'Подсказка 3: Философ-стоик на троне, автор бессмертной книги размышлений «К самому себе».',
               'en': "Clue 1: Last of the 'Five Good Emperors' of Rome, ruling from 161 to 180 AD.\n"
                     'Clue 2: Wrote his Stoic journal in military tents while campaigning along the frozen Danube.\n'
                     "Clue 3: Renowned as the 'Philosopher Emperor', author of the enduring classic 'Meditations'."},
  'options': {'uz': ['Seneka', 'Epiktet', 'Antonin Piy', 'Mark Avreliy'],
              'ru': ['Сенека', 'Эпиктет', 'Антонин Пий', 'Марк Аврелий'],
              'en': ['Seneca', 'Epictetus', 'Antoninus Pius', 'Marcus Aurelius']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Mark Avreliy', 'ru': 'Марк Аврелий', 'en': 'Marcus Aurelius'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Marcus_Aurelius_Louvre.jpg/640px-Marcus_Aurelius_Louvre.jpg',
  'fun_fact': {'uz': 'Mark Avreliyning Kapitoliy maydonidagi bronza otliq haykali xristianlar uni xatolik bilan '
                     "Konstantin deb o'ylaganlari tufayli O'rta asrlarda eritib yuborilmay saqlanib qolgan yagona "
                     'antik otliq haykaldir.',
               'ru': 'Конная статуя Марка Аврелия на Капитолии в Риме — единственная сохранившаяся античная конная '
                     'бронзовая скульптура.',
               'en': "His equestrian bronze on Rome's Capitoline Hill survived the Middle Ages only because Christians "
                     'mistook him for Constantine.'},
  'aliases': ['mark avreliy', 'марк аврелий', 'marcus aurelius']},
 {'id': 'hist_who_057',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Milviy ko'prigi jangida (312) osmonda xoch belgisini ko'rib, 'Bu nishon bilan "
                     "g'alaba qozonasan' degan vahiy olganman.\n"
                     '2-maslahat: 313 yilda Milan edikti bilan xristianlikka erkinlik berdim va xristianlikni qabul '
                     "qilgan ilk Rim imperatori bo'ldim.\n"
                     "3-maslahat: 330 yilda imperiya poytaxtini Bosfor bo'yiga ko'chirib, o'z nomim bilan "
                     'Konstantinopol deb atadim.',
               'ru': 'Подсказка 1: Перед битвой у Мульвийского моста увидел в небе крест с надписью «Сим победиши».\n'
                     'Подсказка 2: Издал Миланский эдикт в 313 году, прекративший гонения на христиан в Римской '
                     'империи.\n'
                     'Подсказка 3: Основал новую столицу на Босфоре — Константинополь («Второй Рим»).',
               'en': "Clue 1: Fought at the Milvian Bridge in 312 AD under the sign of the cross ('In hoc signo "
                     "vinces').\n"
                     'Clue 2: Issued the Edict of Milan in 313, ending Christian persecution, and became the first '
                     'Christian emperor.\n'
                     'Clue 3: Dedicated the new imperial capital of Nova Roma on the Bosphorus in 330, naming it '
                     'Constantinople.'},
  'options': {'uz': ['Buyuk Konstantin I', 'Yustinian I', 'Feodosiy I', 'Diokletian'],
              'ru': ['Константин I Великий', 'Юстиниан I', 'Феодосий I', 'Диоклетиан'],
              'en': ['Constantine the Great', 'Justinian I', 'Theodosius I', 'Diocletian']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Buyuk Konstantin I', 'ru': 'Константин I Великий', 'en': 'Constantine the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Constantine_the_Great_York.jpg/640px-Constantine_the_Great_York.jpg',
  'fun_fact': {'uz': "Konstantin 325 yilda Birinchi Butunjahon Nikeya soborini chaqirib, xristianlik e'tiqodi "
                     "qoidalarini (Nikeya e'tiqod ramzi) rasmiylashtirdi.",
               'ru': 'Константин Великий созвал Первый Вселенский собор в Никее, установив догматы христианской '
                     'церкви.',
               'en': 'Constantine convened the First Ecumenical Council at Nicaea in 325 AD, formulating the Nicene '
                     'Creed.'},
  'aliases': ['konstantin', 'buyuk konstantin', 'константин великий', 'константин i', 'constantine the great']},
 {'id': 'hist_who_058',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Bolqonlik oddiy dehqon oilasida tug'ilib, amakisi Yustin orqali Vizantiya taxtiga "
                     "o'tirganman.\n"
                     "2-maslahat: Rim qonunlarini tizimlashtirib, 'Fuqarolik huquqi to'plami' (Corpus Juris Civilis)ni "
                     'yaratdim.\n'
                     "3-maslahat: Konstantinopolda muazzam Ayasofya (Muqaddas Sofiya) soborini qurdirdim va 'Sulaymon, "
                     "men sendan o'zdim!' deb xitob qildim.",
               'ru': 'Подсказка 1: Византийский император VI века, отвоевавший Рим, Карфаген и Равенну у варваров.\n'
                     'Подсказка 2: Создал монументальный свод римского права «Кодекс Юстиниана», ставший фундаментом '
                     'права Европы.\n'
                     'Подсказка 3: Построил грандиозный собор Святой Софии в Константинополе, воскликнув: «Я превзошел '
                     'тебя, Соломон!»',
               'en': 'Clue 1: 6th-century Byzantine Emperor whose generals Belisarius and Narses recaptured Italy and '
                     'North Africa.\n'
                     "Clue 2: Codified centuries of Roman jurisprudence into the 'Corpus Juris Civilis' (Code of "
                     'Justinian).\n'
                     "Clue 3: Built Hagia Sophia in Constantinople, famously exclaiming upon its completion: 'Solomon, "
                     "I have surpassed thee!'"},
  'options': {'uz': ['Buyuk Konstantin', 'Yustinian I Buyuk', 'Irakliy I', 'Vasiliy II'],
              'ru': ['Константин Великий', 'Юстиниан I Великий', 'Ираклий I', 'Василий II Болгаробойца'],
              'en': ['Constantine the Great', 'Justinian I', 'Heraclius', 'Basil II']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Yustinian I Buyuk', 'ru': 'Юстиниан I Великий', 'en': 'Justinian I'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Justinian555AD.jpg/640px-Justinian555AD.jpg',
  'fun_fact': {'uz': "532 yilda 'Nika' qo'zg'oloni paytida Yustinian qochishga shaylanganda, uning rafiqasi Teodora: "
                     "'Imperatorlik libosi eng yaxshi kafandir' deb uni shaharda qolishga undagan.",
               'ru': 'Императрица Феодора спасла трон Юстиниана во время восстания «Ника», заявив, что пурпур власти — '
                     'лучший саван.',
               'en': 'During the Nika riots in 532, Empress Theodora dissuaded Justinian from fleeing, declaring '
                     'imperial purple a noble burial shroud.'},
  'aliases': ['yustinian', 'yustinian i', 'юстиниан', 'юстиниан i', 'justinian', 'justinian i']},
 {'id': 'hist_who_059',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Konstantinopol hippodromida aktrisa va raqqosa bo'lib, keyinchalik imperator "
                     'Yustinian I ning rafiqasiga aylanganman.\n'
                     "2-maslahat: 532 yilgi 'Nika' qo'zg'oloni paytida erimni qochishdan to'xtatib, taxtni saqlab "
                     'qoldim.\n'
                     '3-maslahat: Vizantiyada ayollar huquqlarini (ajrashish, mulk egaligi, bolalarni vasiylik qilish) '
                     'qonun bilan himoya qilgan buyuk imperatrisaman.',
               'ru': 'Подсказка 1: Бывшая цирковая артистка, ставшая супругой и соправительницей византийского '
                     'императора Юстиниана I.\n'
                     'Подсказка 2: Проявила железную волю в восстании «Ника», сказав мужу: «Царская порфира — '
                     'прекрасный саван».\n'
                     'Подсказка 3: Первая правительница, законодательно закрепившая права женщин на развод и имущество '
                     'в Римском праве.',
               'en': 'Clue 1: Former actress and circus performer who became Empress of the Byzantine Empire alongside '
                     'Justinian I.\n'
                     'Clue 2: Saved the imperial throne during the bloody Nika riots of 532 through her sheer '
                     'defiance.\n'
                     "Clue 3: Championed legal reforms expanding women's rights regarding divorce, child custody, and "
                     'property ownership.'},
  'options': {'uz': ['Malika Irina', 'Kleopatra', 'Malika Feodora (Teodora)', 'Zenobiya'],
              'ru': ['Императрица Ирина', 'Клеопатра', 'Императрица Феодора', 'Зенобия'],
              'en': ['Empress Irene', 'Cleopatra', 'Empress Theodora', 'Zenobia']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Malika Feodora (Teodora)', 'ru': 'Императрица Феодора', 'en': 'Empress Theodora'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Theodora_mosaic_Ravenna.jpg/640px-Theodora_mosaic_Ravenna.jpg',
  'fun_fact': {'uz': 'Ravennadagi San-Vitale bazilikasidagi mozaikada Teodora boshida zumrad toji va orqasida nimb '
                     '(ziyo) bilan tasvirlangan.',
               'ru': 'Знаменитая мозаика в базилике Сан-Витале в Равенне увековечила Феодору в роскошных императорских '
                     'одеждах с нимбом святой.',
               'en': "The stunning 6th-century mosaic in Ravenna's Basilica of San Vitale portrays Theodora in regal "
                     'purple clutching a jewel-encrusted chalice.'},
  'aliases': ['teodora',
              'feodora',
              'malika teodora',
              'феодора',
              'императрица феодора',
              'theodora',
              'empress theodora']},
 {'id': 'hist_who_060',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: V asrda yashagan xunlarning eng qudratli hukmdoriman.\n'
                     "2-maslahat: Rim va Vizantiyaga birdek dahshat solib, xristianlar tomonidan 'Tangrining qamchisi' "
                     '(Flagellum Dei) deb atalganman.\n'
                     "3-maslahat: 451 yilda Katalaun maydonlarida ('Xalqlar jangi') Rim sarkardasi Aetsiy va "
                     "vestgotlar bilan to'qnashdim.",
               'ru': 'Подсказка 1: Вождь гуннов в V веке, объединивший племена от Волги до Рейна.\n'
                     'Подсказка 2: Европейцы прозвали меня «Бич Божий» (Flagellum Dei), считая карой за грехи.\n'
                     'Подсказка 3: Сражался против римлян и вестготов на Каталаунских полях в 451 году («Битва '
                     'народов»).',
               'en': 'Clue 1: Supreme ruler of the Huns who united tribal federations from the Volga to the Rhine.\n'
                     "Clue 2: Feared across the Roman world, earning the fearsome title 'Scourge of God' (Flagellum "
                     'Dei).\n'
                     'Clue 3: Clashed with Roman general Aetius and Visigothic king Theodoric at the Battle of the '
                     'Catalaunian Plains in 451 AD.'},
  'options': {'uz': ['Balamber', 'Rua', 'Alarix', "Attila ('Tangrining qamchisi')"],
              'ru': ['Баламбер', 'Руа', 'Аларих', 'Аттила («Бич Божий»)'],
              'en': ['Balamber', 'Rugila', 'Alaric', "Attila the Hun ('Flagellum Dei')"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Attila ('Tangrining qamchisi')",
                     'ru': 'Аттила («Бич Божий»)',
                     'en': "Attila the Hun ('Flagellum Dei')"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Attila_the_Hun_Delacroix.jpg/640px-Attila_the_Hun_Delacroix.jpg',
  'fun_fact': {'uz': "Attila 453 yilda o'z to'y kechasida kutilmaganda vafot etgan; u uch qavatli (oltin, kumush va "
                     "temir) tobutda daryo tubiga ko'milgan va qabr siri saqlanishi uchun ko'mganlar o'ldirilgan.",
               'ru': 'По легенде, Аттила был похоронен на дне реки Тиса в трех гробах — железном, серебряном и '
                     'золотом, а могильщиков предали мечу.',
               'en': 'According to Priscus, Attila was buried secretly in a triple coffin of iron, silver, and gold '
                     'diverted beneath a riverbed.'},
  'aliases': ['attila', 'tangrining qamchisi', 'аттила', 'бич божий', 'attila the hun']},
 {'id': 'hist_who_061',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Merovinglar sulolasiga mansub franklar yetakchisiman.\n'
                     '2-maslahat: 486 yilda Suasson jangida oxirgi Rim noibini yengib Galliyani egalladim.\n'
                     '3-maslahat: 496 yilda katolik xristianlikni qabul qilib, Fransiya davlatchiligiga tamal toshini '
                     "qo'ydim.",
               'ru': 'Подсказка 1: Вождь салических франков из династии Меровингов.\n'
                     'Подсказка 2: Разбил римлян при Суассоне и объединил франкские племена.\n'
                     'Подсказка 3: Принял крещение в Реймсе в 496 году, став основателем Франкского королевства.',
               'en': 'Clue 1: First King of the Franks who united all Frankish tribes under Merovingian rule.\n'
                     'Clue 2: Defeated the last Roman governor Syagrius at Soissons in 486.\n'
                     'Clue 3: Converted to Catholicism at Reims around 496 AD, laying the foundation for France.'},
  'options': {'uz': ['Xlodvig I', 'Karl Martell', 'Pipin Pakana', 'Xilderik I'],
              'ru': ['Хлодвиг I', 'Карл Мартелл', 'Пипин Короткий', 'Хильдерик I'],
              'en': ['Clovis I', 'Charles Martel', 'Pepin the Short', 'Childeric I']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Xlodvig I', 'ru': 'Хлодвиг I', 'en': 'Clovis I'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Clovis_Ier.jpg/640px-Clovis_Ier.jpg',
  'fun_fact': {'uz': "Fransiya qirollarining an'anaviy 'Lui' (Louis) ismi aynan qadimgi nemischa 'Xlodvig' (Jangda "
                     'dovruqli) ismidan kelib chiqqan.',
               'ru': 'Имя Хлодвиг трансформировалось во французском языке в имя Людовик (Луи), которое носили 18 '
                     'королей Франции.',
               'en': "The name 'Louis', borne by 18 kings of France, is the French evolution of the Germanic name "
                     "'Clovis'."},
  'aliases': ['xlodvig', 'xlodvig i', 'хлодвиг', 'clovis', 'clovis i']},
 {'id': 'hist_who_062',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Normandiya gersogi bo'lib, La-Mansh bo'g'ozidan o'tib Angliyaga bostirib kirdim.\n"
                     '2-maslahat: 1066 yilda Gastings jangida anglosaks qiroli Garold II ni yengdim.\n'
                     "3-maslahat: Angliyada birinchi umumxalq yer va mulk ro'yxati — 'Qiyomat kitobi'ni (Domesday "
                     'Book) tuzdirdim va London Tauerini qurdirdim.',
               'ru': 'Подсказка 1: Герцог Нормандии, высадившийся с флотом на побережье Англии в 1066 году.\n'
                     'Подсказка 2: Одержал победу в битве при Гастингсе, где погиб король Гарольд II.\n'
                     'Подсказка 3: Коронован в Вестминстерском аббатстве, построил Тауэр и составил «Книгу Страшного '
                     'суда».',
               'en': 'Clue 1: Duke of Normandy who launched the 1066 Norman Conquest of England.\n'
                     'Clue 2: Defeated Anglo-Saxon King Harold Godwinson at the Battle of Hastings.\n'
                     'Clue 3: Commissioned the Domesday Book land survey and founded the Tower of London.'},
  'options': {'uz': ['Garold Godvinson', 'Vilgelm I Fathchi (Bosqinchi)', 'Eduard Tavbakor', 'Genrix I'],
              'ru': ['Гарольд II Годвинсон', 'Вильгельм I Завоеватель', 'Эдуард Исповедник', 'Генрих I'],
              'en': ['Harold Godwinson', 'William the Conqueror', 'Edward the Confessor', 'Henry I']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Vilgelm I Fathchi (Bosqinchi)',
                     'ru': 'Вильгельм I Завоеватель',
                     'en': 'William the Conqueror'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/William_the_Conqueror_Bayeux.jpg/640px-William_the_Conqueror_Bayeux.jpg',
  'fun_fact': {'uz': "Vilgelm o'z hayotining oxirigacha ingliz tilini o'rgana olmagan bo'lsa-da, uning davridan "
                     "boshlab ingliz tili normand-fransuzcha so'zlar bilan boyidi.",
               'ru': 'Вильгельм так и не овладел английским языком, но именно нормандское завоевание сформировало '
                     'современный английский.',
               'en': 'William never learned to speak English, yet his conquest permanently altered the language, '
                     'introducing Anglo-Norman French vocabulary.'},
  'aliases': ['vilgelm', 'vilgelm fathchi', 'вильгельм завоеватель', 'william the conqueror']},
 {'id': 'hist_who_063',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Plantagenetlar sulolasiga mansub Angliya qiroliman, ammo hayotimning atigi 6 oyini '
                     "Angliyada o'tkazganman.\n"
                     '2-maslahat: Uchinchi Salib yurishida (1189-1192) Akkra va Arsuf janglarida qahramonlik '
                     "ko'rsatdim.\n"
                     '3-maslahat: Musulmon sarkardasi Salohiddin Ayyubiy bilan tengma-teng kurashgan afsonaviy '
                     'ritsarlik timsoliman.',
               'ru': 'Подсказка 1: Английский король, говоривший по-французски и почти не живший в Англии.\n'
                     'Подсказка 2: Предводитель Третьего крестового похода, взявший Акру и победивший при Арсуфе.\n'
                     'Подсказка 3: Прозван «Львиное Сердце» за бесстрашие; вел рыцарское противостояние с Саладином.',
               'en': 'Clue 1: King of England who spoke Occitan and spent barely six months of his reign in England.\n'
                     'Clue 2: Commanded the Third Crusade, winning victories at Acre and Arsuf.\n'
                     "Clue 3: Renowned as 'Coeur de Lion' (Lionheart) for his battlefield bravery against Saladin."},
  'options': {'uz': ['Genrix II', 'Ioann Yersiz', 'Richard I Sheryurak', 'Eduard I'],
              'ru': ['Генрих II', 'Иоанн Безземельный', 'Ричард I Львиное Сердце', 'Эдуард I'],
              'en': ['Henry II', 'King John', 'Richard the Lionheart (Coeur de Lion)', 'Edward I']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Richard I Sheryurak',
                     'ru': 'Ричард I Львиное Сердце',
                     'en': 'Richard the Lionheart (Coeur de Lion)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Richard_I_tomb_Fontevraud.jpg/640px-Richard_I_tomb_Fontevraud.jpg',
  'fun_fact': {'uz': "Richard Fransiyadagi kichik Shalyu qal'asi qamalida oddiy kamonchining yelkasiga otgan "
                     "zaharlangan o'qidan vafot etgan.",
               'ru': 'Непобедимый рыцарь погиб от случайного арбалетного болта при осаде крошечного замка Шалю во '
                     'Франции.',
               'en': 'Richard was fatally struck by a crossbow bolt fired by a lone defender during the siege of the '
                     'minor castle of Châlus.'},
  'aliases': ['richard sheryurak', 'sheryurak', 'ричард львиное сердце', 'richard the lionheart', 'lionheart']},
 {'id': 'hist_who_064',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Gogenshtaufenlar sulolasidan bo'lgan Muqaddas Rim imperatoriman.\n"
                     '2-maslahat: Italiya shaharlariga qarshi 6 marta yurish qilib, Legnano jangida Lombardiya ligasi '
                     "bilan to'qnashdim.\n"
                     "3-maslahat: Qizil soqolim uchun 'Barbarossa' laqabini olganman; Uchinchi Salib yurishida Salef "
                     "daryosidan o'tayotib cho'kib ketdim.",
               'ru': 'Подсказка 1: Император Священной Римской империи из династии Гогенштауфенов.\n'
                     'Подсказка 2: Вел долгую войну с североитальянскими городами Ломбардской лиги и папой римским.\n'
                     'Подсказка 3: Получил прозвище Барбаросса («Рыжебородый»); утонул во время Третьего крестового '
                     'похода в Киликии.',
               'en': 'Clue 1: Hohenstaufen Holy Roman Emperor who spent decades fighting the Lombard League in Italy.\n'
                     "Clue 2: Nicknamed 'Barbarossa' (Redbeard) by the northern Italian cities he subdued.\n"
                     'Clue 3: Drowned while crossing the Saleph River in Cilicia during the Third Crusade in 1190.'},
  'options': {'uz': ['Fridrix II', 'Genrix IV', 'Otton I', 'Fridrix I Barbarossa (Qizilsoqol)'],
              'ru': ['Фридрих II Гогенштауфен', 'Генрих IV', 'Оттон I', 'Фридрих I Барбаросса'],
              'en': ['Frederick II', 'Henry IV', 'Otto I', 'Frederick I Barbarossa']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Fridrix I Barbarossa (Qizilsoqol)',
                     'ru': 'Фридрих I Барбаросса',
                     'en': 'Frederick I Barbarossa'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Frederick_Barbarossa_miniature.jpg/640px-Frederick_Barbarossa_miniature.jpg',
  'fun_fact': {'uz': "Nemis xalq afsonalariga ko'ra, Barbarossa o'lmagan, balki Kifxoyzer tog'i g'orida uxlab yotibdi "
                     "va Germaniya birlashishi uchun uyg'onadi.",
               'ru': 'По немецкой легенде, Барбаросса спит в пещере горы Кифхойзер за каменным столом в ожидании часа '
                     'возрождения величия страны.',
               'en': 'German folklore told that Barbarossa was asleep beneath the Kyffhäuser mountain, awaiting the '
                     'day to awaken and restore Germany.'},
  'aliases': ['barbarossa', 'fridrix barbarossa', 'барбаросса', 'фридрих барбаросса', 'frederick barbarossa']},
 {'id': 'hist_who_065',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Fransiyaning boy Akvitaniya gersogligi merosxo'ri bo'lganman.\n"
                     '2-maslahat: Tarixda ham Fransiya qirolichasi (Lyudovik VII xotini), ham Angliya qirolichasi '
                     "(Genrix II xotini) bo'lgan yagona ayolman.\n"
                     "3-maslahat: Qirol Richard Sheryurak va Ioann Yersizning onasiman; O'rta asr ritsarlik madaniyati "
                     "va trubadurlarning homiysi bo'ldim.",
               'ru': 'Подсказка 1: Богатейшая наследница Аквитании, определившая геополитику Европы XII века.\n'
                     'Подсказка 2: Единственная в истории женщина, успевшая побывать королевой сначала Франции, а '
                     'затем Англии.\n'
                     'Подсказка 3: Мать королей Ричарда Львиное Сердце и Иоанна Безземельного, покровительница '
                     'трубадуров.',
               'en': 'Clue 1: Duchess of Aquitaine in her own right, controlling vast wealthy lands in southwestern '
                     'France.\n'
                     'Clue 2: The only woman in history to wear the crowns of both France (queen to Louis VII) and '
                     'England (queen to Henry II).\n'
                     'Clue 3: Mother of Kings Richard the Lionheart and John; patroness of troubadours and courtly '
                     'love.'},
  'options': {'uz': ['Eleonora Akvitaniyalik (Aliyenora)',
                     'Mariya Tyudor',
                     'Izabella Kastiliyalik',
                     'Yekaterina Medichi'],
              'ru': ['Алиенора Аквитанская (Элеонора)', 'Мария Тюдор', 'Изабелла Кастильская', 'Екатерина Медичи'],
              'en': ['Eleanor of Aquitaine', 'Mary I of England', 'Isabella of Castile', "Catherine de' Medici"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Eleonora Akvitaniyalik (Aliyenora)',
                     'ru': 'Алиенора Аквитанская (Элеонора)',
                     'en': 'Eleanor of Aquitaine'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Eleanor_of_Aquitaine_tomb.jpg/640px-Eleanor_of_Aquitaine_tomb.jpg',
  'fun_fact': {'uz': "Eleonora o'g'li Richard bilan birga Ikkinchi Salib yurishida shaxsan qurol ko'tarib Yaqin "
                     "Sharqqa borgan jasur ayol bo'lgan.",
               'ru': 'Алиенора лично отправилась во Второй крестовый поход во главе отряда аквитанских рыцарей.',
               'en': 'Eleanor accompanied her husband King Louis VII on the Second Crusade, riding at the head of '
                     'Aquitanian vassals.'},
  'aliases': ['eleonora', 'aliyenora', 'алиенора аквитанская', 'элеонора', 'eleanor of aquitaine']},
 {'id': 'hist_who_066',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Aragon qiroli Ferdinand II bilan turmush qurib, Ispaniyani yagona davlatga '
                     'birlashtirdim.\n'
                     '2-maslahat: 1492 yilda Rekonkistani yakunlab, Granada amirligini zabt etdim.\n'
                     "3-maslahat: Xristofor Kolumbning Amerikaga ilk ekspeditsiyasini o'z mablag'larim (shaxsiy "
                     'javohirlarim) hisobidan moliyalashtirdim.',
               'ru': 'Подсказка 1: Королева Кастилии, чей брак с Фердинандом Арагонским объединил Испанию.\n'
                     'Подсказка 2: Завершила Реконкисту в 1492 году взятием Гранады и изгнанием мавров.\n'
                     'Подсказка 3: Поверила Христофору Колумбу и профинансировала его экспедицию, открывшую Новый '
                     'Свет.',
               'en': 'Clue 1: Queen of Castile whose marriage to Ferdinand II of Aragon united Spain.\n'
                     'Clue 2: Completed the Reconquista in January 1492 with the surrender of Muslim Granada.\n'
                     "Clue 3: Sponsored and financed Christopher Columbus's 1492 voyage to the New World."},
  'options': {'uz': ['Xuan I Telba', 'Izabella I Kastiliyalik (Katolik Izabella)', 'Yelizaveta I', 'Mariya I'],
              'ru': ['Хуана Безумная', 'Изабелла I Кастильская', 'Елизавета I', 'Мария I Тюдор'],
              'en': ['Joanna of Castile', 'Isabella I of Castile', 'Elizabeth I', 'Mary I']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Izabella I Kastiliyalik (Katolik Izabella)',
                     'ru': 'Изабелла I Кастильская',
                     'en': 'Isabella I of Castile'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Isabella_of_Castile_portrait.jpg/640px-Isabella_of_Castile_portrait.jpg',
  'fun_fact': {'uz': "Izabella va Ferdinandga Papa Aleksandr VI tomonidan 'Katolik monarxlari' (Los Reyes Catolicos) "
                     'unvoni berilgan.',
               'ru': 'Папа Римский даровал Изабелле и Фердинанду титул «Католические короли», ставший официальным '
                     'титулом испанских монархов.',
               'en': "Pope Alexander VI conferred the title 'The Catholic Monarchs' upon Isabella and Ferdinand in "
                     '1494.'},
  'aliases': ['izabella', 'izabella i', 'изабелла кастильская', 'isabella of castile', 'isabella i']},
 {'id': 'hist_who_067',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Genrix VIII va Anna Boleynning qizi bo'lib, Tyudorlar sulolasining so'nggi "
                     'vakiliman.\n'
                     "2-maslahat: Hech qachon turmushga chiqmaganman va 'Men Angliya bilan nikoh qurganman' deganman.\n"
                     "3-maslahat: 1588 yilda Ispan 'Yengilmas armada'sini yengdim; mening 44 yillik hukmronligim "
                     "'Oltin asr' deb ataldi.",
               'ru': 'Подсказка 1: Дочь Генриха VIII и Анны Болейн, последний монарх династии Тюдоров.\n'
                     'Подсказка 2: Отказалась выходить замуж, заявив: «Я обручена со своим королевством» '
                     '(Королева-дева).\n'
                     'Подсказка 3: Разгромила испанскую Непобедимую армаду в 1588 году; эпоха расцвета театра '
                     'Шекспира.',
               'en': 'Clue 1: Daughter of Henry VIII and Anne Boleyn, the last monarch of the House of Tudor.\n'
                     "Clue 2: Known as 'The Virgin Queen' for never marrying, declaring herself wedded to England.\n"
                     'Clue 3: Defeated the Spanish Armada in 1588, presiding over the golden age of Shakespeare.'},
  'options': {'uz': ['Mariya I Tyudor', 'Mariya Styuart', 'Yelizaveta I (Qirolicha-Bokira)', 'Qirolicha Viktoriya'],
              'ru': ['Мария I Кровавая', 'Мария Стюарт', 'Елизавета I (Королева-дева)', 'Королева Виктория'],
              'en': ['Mary I of England',
                     'Mary, Queen of Scots',
                     'Elizabeth I of England (The Virgin Queen)',
                     'Queen Victoria']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Yelizaveta I (Qirolicha-Bokira)',
                     'ru': 'Елизавета I (Королева-дева)',
                     'en': 'Elizabeth I of England (The Virgin Queen)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Darnley_stage_3.jpg/640px-Darnley_stage_3.jpg',
  'fun_fact': {'uz': "Yelizaveta I davrida Amerikadagi birinchi ingliz koloniyasi uning sharafiga 'Virjiniya' (Bokira "
                     'ayol yeri) deb atalgan.',
               'ru': 'Американский штат Виргиния назван в честь Елизаветы I («Королевы-девы» — The Virgin Queen).',
               'en': "The American colony and state of Virginia was named in honour of Elizabeth I, the 'Virgin "
                     "Queen'."},
  'aliases': ['yelizaveta i', 'qirolicha yelizaveta', 'елизавета i', 'королева-дева', 'elizabeth i', 'virgin queen']},
 {'id': 'hist_who_068',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Atigi 6 kunlik chaqaloqligimda Shotlandiya toji menga meros qolgan.\n'
                     '2-maslahat: Fransiya qiroli Fransisk II bilan nikoh orqali qisqa vaqt Fransiya qirolichasi ham '
                     "bo'lganman.\n"
                     "3-maslahat: Angliya taxtiga da'vogarlik qildim; jiyanim Yelizaveta I buyrug'i bilan 1587 yilda "
                     'Foderingey qasrida boshim tanamdan judo qilindi.',
               'ru': 'Подсказка 1: Стала королевой Шотландии в возрасте всего шести дней от роду.\n'
                     'Подсказка 2: Супруга французского короля Франциска II, претендовавшая на английский престол.\n'
                     'Подсказка 3: Была заключена в тюрьму Елизаветой I на 19 лет и казнена на плахе в замке '
                     'Фотерингей.',
               'en': 'Clue 1: Ascended the Scottish throne when barely six days old.\n'
                     'Clue 2: Queen consort of France through her marriage to Francis II.\n'
                     'Clue 3: Imprisoned for 19 years and executed by beheading on orders of Elizabeth I in 1587.'},
  'options': {'uz': ['Yelizaveta I', 'Mariya Tyudor', 'Jeyn Grey', 'Mariya Styuart (Shotlandiya qirolichasi)'],
              'ru': ['Елизавета I', 'Мария Тюдор', 'Джейн Грей', 'Мария Стюарт (королева Шотландии)'],
              'en': ['Elizabeth I', 'Mary I of England', 'Lady Jane Grey', 'Mary, Queen of Scots']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Mariya Styuart (Shotlandiya qirolichasi)',
                     'ru': 'Мария Стюарт (королева Шотландии)',
                     'en': 'Mary, Queen of Scots'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Mary_Queen_of_Scots_blours.jpg/640px-Mary_Queen_of_Scots_blours.jpg',
  'fun_fact': {'uz': "Mariya Styuart qatl etilgan bo'lsa-da, uning o'g'li Yakov (Jeyms I) Yelizaveta o'limidan so'ng "
                     "Angliya va Shotlandiyaning birinchi umumiy qiroli bo'ldi.",
               'ru': 'Сын Марии Стюарт Яков VI стал королем Англии (как Яков I), объединив под своей короной Англию и '
                     'Шотландию.',
               'en': 'Though Mary was beheaded, her son James VI of Scotland inherited the English throne in 1603 as '
                     'James I.'},
  'aliases': ['mariya styuart', 'мария стюарт', 'mary queen of scots', 'mary stuart']},
 {'id': 'hist_who_069',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Angliya qiroli bo'lib, o'g'il farzand ko'rish ilinjida ketma-ket 6 marta "
                     'uylanganman.\n'
                     '2-maslahat: Rim papasi ajrashishimga ruxsat bermagach, 1534 yilda Katolik cherkovi bilan aloqani '
                     'uzdim va Anglikan cherkovini tuzdim.\n'
                     "3-maslahat: Xotinlarimning taqdiri mashhur ingliz qofiyasi bilan eslanadi: 'Ajrashdi, boshini "
                     "kesdi, vafot etdi, ajrashdi, boshini kesdi, omon qoldi'.",
               'ru': 'Подсказка 1: Английский монарх эпохи Возрождения, прославившийся своими шестью браками.\n'
                     'Подсказка 2: Порвал с папским Римом, провел Реформацию и провозгласил себя главой Англиканской '
                     'церкви.\n'
                     'Подсказка 3: Казнил двух своих жен — Анну Болейн и Екатерину Говард — по обвинению в измене.',
               'en': 'Clue 1: Renaissance Tudor monarch famed for having six marriages in pursuit of a male heir.\n'
                     'Clue 2: Broke with the papacy in 1534, creating the Church of England with himself as Supreme '
                     'Head.\n'
                     "Clue 3: His wives' fates are remembered by: 'Divorced, beheaded, died; divorced, beheaded, "
                     "survived'."},
  'options': {'uz': ['Genrix VIII Tyudor', 'Genrix VII', 'Eduard VI', 'Yakov I'],
              'ru': ['Генрих VIII Тюдор', 'Генрих VII', 'Эдуард VI', 'Яков I'],
              'en': ['Henry VIII of England', 'Henry VII', 'Edward VI', 'James I']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Genrix VIII Tyudor', 'ru': 'Генрих VIII Тюдор', 'en': 'Henry VIII of England'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/After_Hans_Holbein_the_Younger_-_Portrait_of_Henry_VIII_-_Google_Art_Project.jpg/640px-After_Hans_Holbein_the_Younger_-_Portrait_of_Henry_VIII_-_Google_Art_Project.jpg',
  'fun_fact': {'uz': "Genrix VIII yoshligida musiqachi va shoir bo'lgan; mashhur 'Greensleeves' xalq kuyini unga "
                     'nisbat berishadi.',
               'ru': 'Генрих VIII сочинял музыку и стихи; ему традиционно приписывают авторство баллады «Зеленые '
                     'рукава» (Greensleeves).',
               'en': 'Henry was an accomplished lutenist, jouster, and composer, widely associated with the ballad '
                     "'Greensleeves'."},
  'aliases': ['genrix viii', 'genrix 8', 'генрих viii', 'генрих 8', 'henry viii']},
 {'id': 'hist_who_070',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Fransiya taxtida 72 yil (1643-1715) o'tirib, Yevropa tarixidagi eng uzoq hukmronlik "
                     'qilgan monarxman.\n'
                     "2-maslahat: 'Davlat — bu menman!' (L'État, c'est moi) degan mutlaq monarxiya tamoyilining "
                     'timsoliman.\n'
                     "3-maslahat: Parij yaqinida o'z qudratim ramzi bo'lgan muhtasham Versal saroyi va bog'larini "
                     'barpo qildirdim.',
               'ru': 'Подсказка 1: Французский монарх из династии Бурбонов, правивший 72 года — дольше всех в истории '
                     'Европы.\n'
                     "Подсказка 2: Автор знаменитого афоризма абсолютной власти: «Государство — это я!» (L'État, c'est "
                     'moi).\n'
                     'Подсказка 3: Прозван «Королем-солнце»; превратил охотничий замок Версаль в пышнейшую резиденцию '
                     'мира.',
               'en': 'Clue 1: Bourbon monarch who reigned for 72 years and 110 days, the longest verified reign of any '
                     'sovereign.\n'
                     "Clue 2: Epitomized absolute monarchy, famously asserting 'L'État, c'est moi' (I am the State).\n"
                     "Clue 3: Known as 'The Sun King' (Le Roi Soleil), transforming Versailles into the epicentre of "
                     'European court life.'},
  'options': {'uz': ['Lyudovik XVI', "Lyudovik XIV ('Quyosh-qirol')", 'Lyudovik XV', 'Kardinal Rishelye'],
              'ru': ['Людовик XVI', 'Людовик XIV («Король-солнце»)', 'Людовик XV', 'Кардинал Ришелье'],
              'en': ['Louis XVI', 'Louis XIV (The Sun King)', 'Louis XV', 'Cardinal Richelieu']},
  'correct_index': 1,
  'correct_answer': {'uz': "Lyudovik XIV ('Quyosh-qirol')",
                     'ru': 'Людовик XIV («Король-солнце»)',
                     'en': 'Louis XIV (The Sun King)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Louis_XIV_of_France.jpg/640px-Louis_XIV_of_France.jpg',
  'fun_fact': {'uz': "Lyudovik XIV baletni juda sevgan va saroy tomoshalarida o'zi Quyosh qiyofasida raqsga tushgani "
                     "uchun 'Quyosh-qirol' nomini olgan.",
               'ru': 'Людовик XIV обожал балет и лично танцевал в придворных постановках в образе Аполлона — бога '
                     'Солнца.',
               'en': 'Louis loved ballet and danced in lavish court spectacles dressed as Apollo, cementing his '
                     "nickname 'The Sun King'."},
  'aliases': ['lyudovik xiv', 'quyosh qirol', 'людовик xiv', 'король-солнце', 'louis xiv', 'sun king']},
 {'id': 'hist_who_071',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Shvetsiya qiroli bo'lib, o'z mamlakatimni Buyuk Yevropa harbiy davlatiga "
                     'aylantirdim.\n'
                     "2-maslahat: Yengil to'plar, intizomli mushketyorlar va otliqlar hamkorligiga asoslangan "
                     "zamonaviy umumqo'shin taktikasiga asos soldim.\n"
                     "3-maslahat: O'ttiz yillik urushda protestantlar himoyachisi sifatida 1632 yilda Lyutsen jangida "
                     "g'alaba qozonib, o'sha jangda halok bo'ldim.",
               'ru': 'Подсказка 1: Король Швеции из династии Васа, прозванный «Отцом современной войны».\n'
                     'Подсказка 2: Создал регулярную армию нового типа с легкой полевой артиллерией и стрелковыми '
                     'шеренгами.\n'
                     'Подсказка 3: Возглавил протестантов в Тридцатилетней войне («Северный лев»); погиб в битве при '
                     'Лютцене в 1632 году.',
               'en': "Clue 1: Swedish King from the House of Vasa, regarded as the 'Father of Modern Warfare'.\n"
                     'Clue 2: Pioneered mobile field artillery, flexible fire doctrines, and aggressive combined '
                     'arms.\n'
                     "Clue 3: The 'Lion of the North' who turned the tide of the Thirty Years' War before dying in the "
                     'fog at Lützen in 1632.'},
  'options': {'uz': ['Karl XII', 'Gustav III', "Gustav II Adolf ('Shimol arsloni')", 'Albrext fon Vallenshteyn'],
              'ru': ['Карл XII', 'Густав III', 'Густав II Адольф («Северный лев»)', 'Альбрехт фон Валленштейн'],
              'en': ['Charles XII',
                     'Gustav III',
                     'Gustavus Adolphus (The Lion of the North)',
                     'Albrecht von Wallenstein']},
  'correct_index': 2,
  'correct_answer': {'uz': "Gustav II Adolf ('Shimol arsloni')",
                     'ru': 'Густав II Адольф («Северный лев»)',
                     'en': 'Gustavus Adolphus (The Lion of the North)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Gustav_II_Adolf_portrait.jpg/640px-Gustav_II_Adolf_portrait.jpg',
  'fun_fact': {'uz': 'Napoleon Bonapart Gustav Adolfni Aleksandr, Sezar va Gannibal bilan bir qatorda dunyo tarixidagi '
                     'eng buyuk 7 ta sarkardadan biri deb hisoblagan.',
               'ru': 'Наполеон ставил военный гений Густава Адольфа в один ряд с Александром Македонским, Цезарем и '
                     'Ганнибалом.',
               'en': 'Napoleon Bonaparte counted Gustavus Adolphus among the eight greatest military commanders of all '
                     'time.'},
  'aliases': ['gustav adolf', 'gustav ii adolf', 'густав адольф', 'густав ii адольф', 'gustavus adolphus']},
 {'id': 'hist_who_072',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Venesuelaning Karakas shahrida boy aristokrat oilasida tug'ilganman.\n"
                     "2-maslahat: Rimdagi Muqaddas tog'da Janubiy Amerikani Ispaniya zulmidan ozod etishga qasam "
                     'ichdim.\n'
                     '3-maslahat: Venesuela, Kolumbiya, Ekvador, Peru va Panamani ozod qilib, Buyuk Kolumbiyaga asos '
                     "soldim; Boliviya davlati mening nomimga qo'yildi.",
               'ru': 'Подсказка 1: Креол-аристократ из Каракаса, посвятивший жизнь борьбе за независимость Южной '
                     'Америки.\n'
                     'Подсказка 2: Дал знаменитую клятву на Авентинском холме в Риме сокрушить власть испанской '
                     'короны.\n'
                     'Подсказка 3: «Освободитель» (El Libertador), в честь которого названа страна Боливия и валюта '
                     'Венесуэлы.',
               'en': 'Clue 1: Aristocratic Venezuelan military leader who pledged to free South America from Spanish '
                     'rule.\n'
                     'Clue 2: Led dramatic campaigns across the Andes, serving as President of Gran Colombia.\n'
                     "Clue 3: Revered as 'El Libertador' across six nations; the country of Bolivia is named in his "
                     'honor.'},
  'options': {'uz': ['Xose de San-Martin',
                     "Bernardo O'Xiggins",
                     'Fransisko de Miranda',
                     "Simon Bolivar ('Ozodlik keltiruvchi')"],
              'ru': ['Хосе де Сан-Мартин',
                     "Бернардо О'Хиггинс",
                     'Франсиско де Миранда',
                     'Симон Боливар («Освободитель»)'],
              'en': ['José de San Martín',
                     "Bernardo O'Higgins",
                     'Francisco de Miranda',
                     "Simón Bolívar ('The Liberator')"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Simon Bolivar ('Ozodlik keltiruvchi')",
                     'ru': 'Симон Боливар («Освободитель»)',
                     'en': "Simón Bolívar ('The Liberator')"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Simon_Bolivar_portrait.jpg/640px-Simon_Bolivar_portrait.jpg',
  'fun_fact': {'uz': "Bolivar 123 000 km dan ortiq masofani otda bosib o'tgan — bu Aleksandr Makedonskiy va Napoleon "
                     "bosib o'tgan masofadan ko'pdir.",
               'ru': 'Боливар верхом преодолел более 120 тысяч километров во время походов через Анды — больше, чем '
                     'любой европейский завоеватель.',
               'en': 'Bolívar rode over 75,000 miles on horseback during his liberation campaigns—more than Napoleon '
                     'and Alexander combined.'},
  'aliases': ['simon bolivar', 'bolivar', 'симон боливар', 'боливар', 'simon bolivar']},
 {'id': 'hist_who_073',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Argentinalik harbiy qo'mondon bo'lib, Janubiy Amerikaning janubiy qismini ozod "
                     'etishga boshchilik qildim.\n'
                     "2-maslahat: 1817 yilda And tog'larini 4000 metr balandlikdan otliq armiyam bilan oshib o'tib, "
                     'Chilini ozod qildim.\n'
                     "3-maslahat: Peru mustaqilligini e'lon qilib, o'zimni 'Peru himoyachisi' (Protector del Perú) deb "
                     "e'lon qildim.",
               'ru': 'Подсказка 1: Аргентинский генерал, один из главных лидеров борьбы за независимость испанских '
                     'колоний.\n'
                     'Подсказка 2: Совершил беспрецедентный переход через заснеженные Анды в 1817 году и освободил '
                     'Чили.\n'
                     'Подсказка 3: Объявил независимость Перу в Лиме в 1821 году, приняв титул «Протектора свободы».',
               'en': 'Clue 1: Argentine general who led the southern independence campaigns against the Spanish '
                     'Empire.\n'
                     'Clue 2: Marched the Army of the Andes over 4,000-meter passes in 1817 to liberate Chile.\n'
                     "Clue 3: Proclaimed the independence of Peru in Lima in 1821, serving as 'Protector of Peru'."},
  'options': {'uz': ['Xose de San-Martin', 'Simon Bolivar', "Bernardo O'Xiggins", 'Migel Idalgo'],
              'ru': ['Хосе де Сан-Мартин', 'Симон Боливар', "Бернардо О'Хиггинс", 'Мигель Идальго'],
              'en': ['José de San Martín', 'Simón Bolívar', "Bernardo O'Higgins", 'Miguel Hidalgo']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Xose de San-Martin', 'ru': 'Хосе де Сан-Мартин', 'en': 'José de San Martín'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Jose_de_San_Martin_portrait.jpg/640px-Jose_de_San_Martin_portrait.jpg',
  'fun_fact': {'uz': "1822 yilda Guayakil uchrashuvida Bolivar bilan yakkama-yakka suhbatdan so'ng, San-Martin "
                     'ixtiyoriy ravishda barcha lavozimlaridan voz kechib Yevropaga ketgan.',
               'ru': 'После исторической встречи с Боливаром в Гуаякиле Сан-Мартин добровольно ушел из политики, чтобы '
                     'избежать соперничества.',
               'en': 'After the mysterious 1822 Guayaquil Conference with Bolívar, San Martín gracefully resigned '
                     'command and exiled himself to France.'},
  'aliases': ['san martin', 'xose de san martin', 'сан-мартин', 'хосе де сан-мартин', 'san martin']},
 {'id': 'hist_who_074',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Gaitida (San-Domingo) qora tanli qul oilasida tug'ilib, 50 yoshimda inqilobga "
                     'boshchilik qildim.\n'
                     "2-maslahat: Tarixdagi birinchi va yagona muvaffaqiyatli qullar qo'zg'oloni — Gaiti inqilobini "
                     'boshqardim.\n'
                     "3-maslahat: 'Qora Napoleon' deb atalganman; Fransiya, Buyuk Britaniya va Ispaniya armiyalarini "
                     'oroldan haydab chiqarganman.',
               'ru': 'Подсказка 1: Родился рабом на сахарных плантациях французской колонии Сан-Доминго (Гаити).\n'
                     'Подсказка 2: Возглавил Гаитянскую революцию — единственное в мировой истории победоносное '
                     'восстание рабов.\n'
                     'Подсказка 3: «Черный Наполеон», создавший свободную конституцию и разгромивший европейские '
                     'интервентские армии.',
               'en': 'Clue 1: Born an enslaved coachman in Saint-Domingue who rose to lead the Haitian Revolution.\n'
                     'Clue 2: Orchestrated the only successful slave revolt in modern world history.\n'
                     "Clue 3: Famed as the 'Black Napoleon' who outmaneuvered French, British, and Spanish empires to "
                     'build a free society.'},
  'options': {'uz': ['Jan-Jak Dessalin', 'Tussen-Luvertyur (Fransua-Dominik)', 'Anri Kristof', 'Patris Lumumba'],
              'ru': ['Жан-Жак Дессалин', 'Туссен-Лувертюр', 'Анри Кристоф', 'Патрис Лумумба'],
              'en': ['Jean-Jacques Dessalines', 'Toussaint Louverture', 'Henri Christophe', 'Patrice Lumumba']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Tussen-Luvertyur (Fransua-Dominik)', 'ru': 'Туссен-Лувертюр', 'en': 'Toussaint Louverture'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Toussaint_Louverture_portrait.jpg/640px-Toussaint_Louverture_portrait.jpg',
  'fun_fact': {'uz': 'Gaiti inqilobi natijasida Gaiti 1804 yilda dunyodagi qora tanlilar boshqargan birinchi mustaqil '
                     'respublikaga aylandi.',
               'ru': 'Победа восстания Туссена привела к созданию в 1804 году Республики Гаити — первого независимого '
                     'государства Латинской Америки.',
               'en': "Louverture's rebellion led Haiti to become the world's first free Black republic and the second "
                     'independent nation in the Americas.'},
  'aliases': ['tussen luvertyur', 'luvertyur', 'туссен-лувертюр', 'toussaint louverture']},
 {'id': 'hist_who_075',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Janubiy Afrikada kichik zulu qabilasining noqonuniy tug'ilgan o'g'li edim.\n"
                     "2-maslahat: Janubiy Afrika harbiy taktikasini o'zgartirib, qisqa nayza (iklva) va 'buqa "
                     "shoxlari' qamal usulini yaratdim.\n"
                     "3-maslahat: Tarqoq klanlarni birlashtirib, qudratli Zulu qirolligiga asos soldim va 'Qora "
                     "Napoleon' deb nom oldim.",
               'ru': 'Подсказка 1: Правитель зулусов в начале XIX века, превративший небольшое племя в военную '
                     'империю.\n'
                     'Подсказка 2: Вооружил воинов короткими копьями и разработал тактику охвата врага «рогами '
                     'буйвола».\n'
                     'Подсказка 3: Создатель державы зулусов, эпоха завоеваний которого известна как Мфекане («Великое '
                     'рассеяние»).',
               'en': 'Clue 1: 19th-century monarch who transformed the Zulu from a minor clan into a formidable '
                     'southern African empire.\n'
                     "Clue 2: Revolutionized tribal warfare with the stabbing spear (iklwa) and the 'buffalo horns' "
                     'battle formation.\n'
                     'Clue 3: Forged the Zulu Empire, initiating the transformative period known as the Mfecane.'},
  'options': {'uz': ['Dingane', 'Ketshvayo', 'Shaka Zulu (Shaka kaSenzangaxona)', 'Mosheshve I'],
              'ru': ['Дингане', 'Кетчвайо', 'Шака Зулу', 'Мошвешве I'],
              'en': ['Dingane', 'Cetshwayo', 'Shaka Zulu', 'Moshoeshoe I']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Shaka Zulu (Shaka kaSenzangaxona)', 'ru': 'Шака Зулу', 'en': 'Shaka Zulu'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Shaka_Zulu_sketch.jpg/640px-Shaka_Zulu_sketch.jpg',
  'fun_fact': {'uz': "Shaka o'z askarlarining tezkorligini oshirish uchun poyabzal kiyishni taqiqlab, qattiq tikanlar "
                     'ustida yalangoyoq yugurish mashqini joriy qilgan.',
               'ru': 'Шака заставлял воинов ходить босиком, чтобы развивать поразительную скорость марша — до 80 '
                     'километров в день.',
               'en': 'Shaka banned sandals, forcing his impis (warriors) to march barefoot across thorn fields, '
                     'covering up to 50 miles a day.'},
  'aliases': ['shaka', 'shaka zulu', 'шака', 'шака зулу', 'shaka zulu']},
 {'id': 'hist_who_076',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: XIV asrda G'arbiy Afrikadagi Mali imperiyasini boshqargan musulmon hukmdoriman.\n"
                     "2-maslahat: 1324 yilda 60 ming kishilik karvon va o'nlab tonna oltin bilan Makkaga haj safariga "
                     'bordim.\n'
                     "3-maslahat: Qohirada shunchalik ko'p oltin tarqatdimki, jahon oltin bozori izdan chiqdi; "
                     'tarixdagi eng boy inson deb tan olinganman.',
               'ru': 'Подсказка 1: Десятый манса (верховный правитель) империи Мали в XIV веке.\n'
                     'Подсказка 2: Совершил паломничество в Мекку в 1324 году со свитой из десятков тысяч людей и '
                     'караваном верблюдов с золотом.\n'
                     'Подсказка 3: Признан экономистами богатейшим человеком всех времен (состояние свыше 400 '
                     'миллиардов долларов в пересчете).',
               'en': 'Clue 1: 14th-century tenth Mansa of the Mali Empire across the West African Sahel.\n'
                     'Clue 2: Undertook a legendary 1324 Hajj to Mecca accompanied by 60,000 attendants laden with '
                     'gold.\n'
                     'Clue 3: Distributed so much gold in Cairo that it caused a regional currency crisis; widely '
                     'rated the wealthiest individual in history.'},
  'options': {'uz': ['Sundjata Keyta', 'Sonni Ali', 'Askiya Muhammad', 'Mansa Muso (Mali imperatori)'],
              'ru': ['Сундиата Кейта', 'Сонни Али', 'Аския Мохаммад', 'Манса Муса (правитель Мали)'],
              'en': ['Sundiata Keita', 'Sonni Ali', 'Askia the Great', 'Mansa Musa (Emperor of Mali)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Mansa Muso (Mali imperatori)',
                     'ru': 'Манса Муса (правитель Мали)',
                     'en': 'Mansa Musa (Emperor of Mali)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Mansa_Musa_Catalan_Atlas.jpg/640px-Mansa_Musa_Catalan_Atlas.jpg',
  'fun_fact': {'uz': "1375 yildagi mashhur Kataloniya atlasida Mansa Muso taxtda qo'lida katta oltin quymasi ushlab "
                     "o'tirgan holda tasvirlangan.",
               'ru': 'На знаменитом Каталанском атласе 1375 года Манса Муса изображен в золотой короне с золотым '
                     'слитком в руке.',
               'en': 'On the 1375 Catalan Atlas map, Mansa Musa is depicted holding a glittering golden orb, embodying '
                     'African prosperity to Europe.'},
  'aliases': ['mansa muso', 'mansa musa', 'манса муса', 'mansa musa']},
 {'id': 'hist_who_077',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Bolalikda shol bo'lib tug'ilib, oyoqqa turgan va qabilasini birlashtirgan afsonaviy "
                     "g'arbiy afrikalik qahramonman.\n"
                     "2-maslahat: 1235 yilda Kirina jangida zolim Sumanguru Kanteni mag'lub etdim.\n"
                     "3-maslahat: Buyuk Mali imperiyasiga asos soldim; mening tarixim 'Sher-qirol' (The Lion King) "
                     "dostoniga asos bo'lgan.",
               'ru': 'Подсказка 1: Основатель империи Мали, который в детстве не мог ходить, но преодолел недуг силой '
                     'духа.\n'
                     'Подсказка 2: Разбил правителя сосо Сумаоро Канте в решающей битве при Кирине в 1235 году.\n'
                     'Подсказка 3: Создал конституцию «Курукан Фуга» (одну из первых в мире) и прозван «Царем-львом» '
                     '(прототип Короля Льва).',
               'en': 'Clue 1: Founder of the Mali Empire who overcame childhood paralysis to become a legendary '
                     'warrior.\n'
                     'Clue 2: Defeated the Sosso sorcerer-king Soumaoro Kanté at the Battle of Kirina in 1235.\n'
                     'Clue 3: Proclaimed the Kouroukan Fouga charter of rights; his life inspired the West African '
                     "Epic of Sundiata and 'The Lion King'."},
  'options': {'uz': ["Sundjata Keyta ('Sher-qirol')", 'Mansa Muso', 'Sonni Ali', 'Samori Ture'],
              'ru': ['Сундиата Кейта («Царь-лев»)', 'Манса Муса', 'Сонни Али', 'Самори Туре'],
              'en': ['Sundiata Keita (The Lion King)', 'Mansa Musa', 'Sonni Ali', 'Samori Ture']},
  'correct_index': 0,
  'correct_answer': {'uz': "Sundjata Keyta ('Sher-qirol')",
                     'ru': 'Сундиата Кейта («Царь-лев»)',
                     'en': 'Sundiata Keita (The Lion King)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Sundiata_Keita_statue_Mali.jpg/640px-Sundiata_Keita_statue_Mali.jpg',
  'fun_fact': {'uz': "Sundjata e'lon qilgan Kurukan Fuqa nizomi inson huquqlari, ayollar mavqei va ijtimoiy totuvlikni "
                     'belgilab bergan ilk xartiyalardan biri hisoblanadi.',
               'ru': 'Хартия Курукан Фуга, провозглашенная Сундиатой в 1235 году, включена ЮНЕСКО в список '
                     'нематериального культурного наследия.',
               'en': "Sundiata's 1235 Kouroukan Fouga charter established early provisions for human rights, gender "
                     'respect, and social peace.'},
  'aliases': ['sundjata keyta', 'sundiata', 'сундидиата кейта', 'сундиата', 'sundiata keita']},
 {'id': 'hist_who_078',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Yangi Misr podsholigining 18-sulolasiga mansub hukmdorman.\n'
                     "2-maslahat: Rasmiy marosimlarda soxta erkaklar soqoli taqib, o'zimni to'laqonli fir'avn deb "
                     "e'lon qilgan ilk ayollardanman.\n"
                     '3-maslahat: Deyr al-Bahridagi mahobatli qoya ibodatxonasini qurdirdim va Punt mamlakatiga '
                     "mashhur savdo ekspeditsiyasini jo'natdim.",
               'ru': 'Подсказка 1: Вторая подтвержденная женщина-фараон в истории Древнего Египта (XVIII династия).\n'
                     'Подсказка 2: Изображалась в мужском царском одеянии с накладной церемониальной бородкой '
                     'фараона.\n'
                     'Подсказка 3: Построила уникальный террасный заупокойный храм в Дейр-эль-Бахри и снарядила '
                     'экспедицию в страну Пунт.',
               'en': "Clue 1: Second historically confirmed female pharaoh, reigning over Egypt's prosperous 18th "
                     'Dynasty.\n'
                     'Clue 2: Depicted in regal statues wearing the royal kilt and ceremonial pharaonic false beard.\n'
                     'Clue 3: Commissioned the monumental mortuary temple at Deir el-Bahari and a famed naval trade '
                     'expedition to Punt.'},
  'options': {'uz': ['Kleopatra VII', "Xatshepsut (Fir'avn ayol)", 'Nefertiti', 'Teya'],
              'ru': ['Клеопатра VII', 'Хатшепсут (женщина-фараон)', 'Нефертити', 'Тия'],
              'en': ['Cleopatra VII', 'Hatshepsut', 'Nefertiti', 'Tiye']},
  'correct_index': 1,
  'correct_answer': {'uz': "Xatshepsut (Fir'avn ayol)", 'ru': 'Хатшепсут (женщина-фараон)', 'en': 'Hatshepsut'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Hatshepsut_statue_Met.jpg/640px-Hatshepsut_statue_Met.jpg',
  'fun_fact': {'uz': "Uning o'gay o'g'li Tutmos III taxtga o'tirgach, uning barcha haykallari va devoriy yozuvlarini "
                     "o'chirib tashlashga buyruq bergan.",
               'ru': 'После смерти Хатшепсут ее пасынок Тутмос III пытался стереть память о мачехе, уничтожая ее '
                     'картуши со стен храмов.',
               'en': 'Her successor Thutmose III attempted to expunge her memory from Egyptian records, chiseled her '
                     'images off temple walls.'},
  'aliases': ['xatshepsut', 'hatshepsut', 'хатшепсут']},
 {'id': 'hist_who_079',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Qadimgi Misr fir'avni Exnatonning (Amenxotep IV) bosh xotini bo'lganman.\n"
                     "2-maslahat: Erim bilan birga ko'p xudolilikni taqiqlab, yagona Quyosh diski — Aten dinini joriy "
                     'qildik.\n'
                     "3-maslahat: Lyudvig Borxardt tomonidan Amarnada topilgan va Berlinda saqlanuvchi go'zal ohaktosh "
                     'byustim butun dunyoga mashhur.',
               'ru': 'Подсказка 1: Главная царская супруга фараона-реформатора Эхнатона в XIV веке до н.э.\n'
                     'Подсказка 2: Участвовала в религиозной революции, установившей культ единого бога солнца Атона.\n'
                     'Подсказка 3: Автор знаменитого бюста работы скульптора Тутмоса, хранящегося в Новом музее '
                     'Берлина.',
               'en': "Clue 1: Great Royal Wife of Pharaoh Akhenaten during Egypt's Amarna period.\n"
                     'Clue 2: Co-ruled during the religious transition that established the monolatrist worship of the '
                     'sun disk Aten.\n'
                     'Clue 3: Celebrated for the iconic painted stucco-coated limestone bust sculpted by Thutmose, now '
                     'in Berlin.'},
  'options': {'uz': ['Xatshepsut', 'Kleopatra', 'Nefertiti (Malika Nefertiti)', 'Nefertari'],
              'ru': ['Хатшепсут', 'Клеопатра', 'Нефертити', 'Нефертари'],
              'en': ['Hatshepsut', 'Cleopatra', 'Nefertiti', 'Nefertari']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Nefertiti (Malika Nefertiti)', 'ru': 'Нефертити', 'en': 'Nefertiti'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Nofretete_Neues_Museum.jpg/640px-Nofretete_Neues_Museum.jpg',
  'fun_fact': {'uz': "Nefertiti ismi misrcha 'Go'zal ayol keldi' degan ma'noni anglatadi va u qadimgi dunyo go'zallik "
                     'etaloni hisoblanadi.',
               'ru': 'Имя Нефертити переводится с древнеегипетского как «Прекрасная пришла»; ее бюст считается '
                     'эталоном женской красоты.',
               'en': "Her name translates to 'A beautiful woman has come'; the 1912 discovery of her Amarna bust "
                     'turned her into a global icon of beauty.'},
  'aliases': ['nefertiti', 'нефертити', 'nefertiti']},
 {'id': 'hist_who_080',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 9 yoshimda fir'avn bo'lib, ota-bobolarimning an'anaviy dinini va Amun kultini qayta "
                     'tikladim.\n'
                     '2-maslahat: Atigi 19 yoshimda sirli sabablar bilan vafot etdim.\n'
                     '3-maslahat: 1922 yilda Govard Karter tomonidan Podshohlar vodiysida deyarli daxlsiz saqlangan '
                     'oltin niqobli maqbaram topildi.',
               'ru': 'Подсказка 1: Фараон XVIII династии, взошедший на трон в 9-летнем возрасте и вернувший культ '
                     'Амона.\n'
                     'Подсказка 2: Правил всего десять лет и скоропостижно скончался около 1323 года до н.э.\n'
                     'Подсказка 3: Сенсационное открытие его неразграбленной гробницы Говардом Картером в 1922 году '
                     'потрясло мир.',
               'en': 'Clue 1: 18th-Dynasty pharaoh who ascended the throne at age eight or nine, restoring Amun '
                     'worship.\n'
                     'Clue 2: Reigned for approximately a decade before dying mysteriously around age eighteen or '
                     'nineteen.\n'
                     'Clue 3: Discovered intact in the Valley of the Kings by Howard Carter in 1922 with his solid '
                     'gold death mask.'},
  'options': {'uz': ['Ramzes II', 'Exnaton', 'Seti I', "Tutanxamon (Bola-fir'avn)"],
              'ru': ['Рамсес II', 'Эхнатон', 'Сети I', 'Тутанхамон'],
              'en': ['Ramesses II', 'Akhenaten', 'Seti I', 'Tutankhamun (King Tut)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Tutanxamon (Bola-fir'avn)", 'ru': 'Тутанхамон', 'en': 'Tutankhamun (King Tut)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tutankhamun_mask_Cairo.jpg/640px-Tutankhamun_mask_Cairo.jpg',
  'fun_fact': {'uz': "Tutanxamonning sof oltindan yasalgan dafn niqobi 10,23 kg og'irlikda bo'lib, qadimgi dunyo "
                     "zargarlik san'atining eng qimmatbaho durdonasidir.",
               'ru': 'Погребальная маска Тутанхамона весит более 10 килограммов чистейшего золота, инкрустированного '
                     'лазуритом и бирюзой.',
               'en': "King Tut's solid gold funerary mask weighs over 10 kilograms (22 lbs) and is inlaid with "
                     'semi-precious lapis lazuli.'},
  'aliases': ['tutanxamon', 'king tut', 'тутанхамон', 'tutankhamun']},
 {'id': 'hist_who_081',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Afina davlatining strateg va yetakchisi bo'lib, mil. avv. V asrda 30 yildan ortiq "
                     "demokratik islohotlar o'tkazdim.\n"
                     "2-maslahat: Meni davrim 'Afinaning Oltin asri' yoki 'Perikl asri' deb nomlandi.\n"
                     '3-maslahat: Afina Akropolida buyuk Parfenon ibodatxonasi qurilishini tashkillashtirdim va '
                     'haykaltarosh Fidiyga homiylik qildim.',
               'ru': 'Подсказка 1: Афинский государственный деятель и полководец, создатель классической афинской '
                     'демократии.\n'
                     'Подсказка 2: Эпоха его правления в V веке до н.э. названа «Золотым веком Афин».\n'
                     'Подсказка 3: Инициатор строительства Парфенона, Пропилей и статуи Афины работы Фидия на '
                     'Акрополе.',
               'en': 'Clue 1: Prominent statesman, orator, and general of Athens during its classical zenith.\n'
                     "Clue 2: Championed Athenian democracy, presiding over the 'Golden Age of Pericles'.\n"
                     'Clue 3: Commissioned the monumental rebuilding of the Acropolis, including the Parthenon.'},
  'options': {'uz': ['Perikl', 'Solon', 'Femistokl', 'Alkiviad'],
              'ru': ['Перикл', 'Солон', 'Фемистокл', 'Алкивиад'],
              'en': ['Pericles', 'Solon', 'Themistocles', 'Alcibiades']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Perikl', 'ru': 'Перикл', 'en': 'Pericles'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Pericles_bust_British_Museum.jpg/640px-Pericles_bust_British_Museum.jpg',
  'fun_fact': {'uz': "Perikl har doim dubulg'a kiyib tasvirlangan, chunki uning boshi g'ayritabiiy cho'ziq bo'lib, u "
                     'bundan uyalgan.',
               'ru': 'Перикла изображали во всех бюстах в коринфском шлеме, чтобы скрыть необычно вытянутую форму '
                     'черепа.',
               'en': 'Ancient busts invariably depict Pericles wearing a Corinthian helmet pushed back, masking his '
                     'unusually elongated head.'},
  'aliases': ['perikl', 'перикл', 'pericles']},
 {'id': 'hist_who_082',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Qadimgi Spartaning Agiadlar sulolasiga mansub 17-qiroliman.\n'
                     '2-maslahat: Mil. avv. 480 yilda Fors podshohi Kserks I ning son-sanoqsiz armiyasiga tor Termopil '
                     'darasida qarshi turdim.\n'
                     "3-maslahat: 300 nafar spartalik jangchim bilan o'limga tik qarab, Yunoniston erkinligi uchun "
                     "qurbon bo'ldim.",
               'ru': 'Подсказка 1: Царь Спарты из рода Агиадов, воспитанный в суровых традициях спартанского '
                     'воспитания (агогэ).\n'
                     'Подсказка 2: На требование Ксеркса сдать оружие ответил лаконично: «Приди и возьми» (Молон '
                     'лабе).\n'
                     'Подсказка 3: Пал смертью храбрых в Фермопильском ущелье в 480 году до н.э. вместе с отрядом из '
                     '300 спартанцев.',
               'en': 'Clue 1: Agiad king of Sparta trained in the rigorous warrior agoge system.\n'
                     "Clue 2: Replied 'Molon labe' (Come and take them) when Persian King Xerxes demanded his "
                     'weapons.\n'
                     'Clue 3: Heroically led the immortal last stand of the 300 Spartans at the Battle of Thermopylae '
                     'in 480 BC.'},
  'options': {'uz': ['Lisandr', 'Leonid I (Sparta qiroli)', 'Agesilay II', 'Pavsaniy'],
              'ru': ['Лисандр', 'Леонид I (царь Спарты)', 'Агесилай II', 'Павсаний'],
              'en': ['Lysander', 'Leonidas I (King of Sparta)', 'Agesilaus II', 'Pausanias']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Leonid I (Sparta qiroli)',
                     'ru': 'Леонид I (царь Спарты)',
                     'en': 'Leonidas I (King of Sparta)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Leonidas_Thermopylae_monument.jpg/640px-Leonidas_Thermopylae_monument.jpg',
  'fun_fact': {'uz': "Termopil jangida halok bo'lgan spartaliklar qabriga: 'Ey musofir, Spartaga xabar ber: biz uning "
                     "qonunlariga sodiq qolib, shu yerda yotibmiz' degan bitik yozilgan.",
               'ru': 'На монументе у Фермопил выбита бессмертная эпитафия поэта Симонида: «Путник, пойди возвести '
                     'нашим гражданам в Лакедемоне: здесь мы легли, костьми законы исполнив».',
               'en': "The epitaph at Thermopylae reads: 'Go tell the Spartans, stranger passing by, that here, "
                     "obedient to their laws, we lie.'"},
  'aliases': ['leonid', 'leonid i', '300 spartalik', 'леонид', 'царь леонид', 'leonidas', '300 spartans']},
 {'id': 'hist_who_083',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Afina davlat arbobi bo'lib, shaharni himoya qilish uchun kuchli dengiz floti "
                     '(triyeralar) qurishni taklif qilganman.\n'
                     "2-maslahat: 'Yog'och devorlar' Afinani qutqaradi degan bashoratni kemalar deb to'g'ri talqin "
                     'qildim.\n'
                     '3-maslahat: Mil. avv. 480 yilda Salamin dengiz jangida forslarning bahaybat flotini tor '
                     "bo'g'ozda aldab qopqonga tushirdim va g'alaba qozondim.",
               'ru': 'Подсказка 1: Афинский архонт и стратег, убедивший сограждан построить мощный флот из 200 триер.\n'
                     'Подсказка 2: Истолковал пророчество Дельфийского оракула о «деревянных стенах» как спасительный '
                     'морской флот.\n'
                     'Подсказка 3: Создатель триумфа в морской битве при Саламине, спасший греческую цивилизацию от '
                     'персидского ига.',
               'en': 'Clue 1: Athenian politician and general who convinced Athens to construct a 200-trireme battle '
                     'fleet.\n'
                     "Clue 2: Interpreted the Delphic Oracle's prophecy of 'wooden walls' as naval wooden hulls.\n"
                     'Clue 3: Lured the superior Persian fleet into the narrows of Salamis in 480 BC, winning a '
                     'decisive victory.'},
  'options': {'uz': ['Perikl', 'Miltiad', 'Femistokl (Afinalik)', 'Aristid'],
              'ru': ['Перикл', 'Мильтиад', 'Фемистокл (Афины)', 'Аристид'],
              'en': ['Pericles', 'Miltiades', 'Themistocles', 'Aristides']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Femistokl (Afinalik)', 'ru': 'Фемистокл (Афины)', 'en': 'Themistocles'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Themistocles_bust_Ostia.jpg/640px-Themistocles_bust_Ostia.jpg',
  'fun_fact': {'uz': "G'alabadan so'ng hasadgo'y afinaliklar uni ostrakizm (sopol parchasiga ism yozib quvg'in qilish) "
                     'orqali shahardan haydab yuborishgan.',
               'ru': 'Несмотря на спасение родины, сограждане подвергли Фемистокла остракизму и изгнали из Афин.',
               'en': 'Despite saving Greece, Themistocles was ostracized by envious Athenian voters and spent his '
                     'final years in Asia Minor.'},
  'aliases': ['femistokl', 'salamin jangi', 'фемистокл', 'themistocles']},
 {'id': 'hist_who_084',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Bolaligimda duduqlanib gapirganman, ovozimni kuchaytirish uchun og'zimga mayda "
                     "toshlar solib dengiz to'lqinlari shovqinida nutq so'zlaganman.\n"
                     "2-maslahat: Qadimgi Yunonistonning eng buyuk notig'i (ritori) darajasiga ko'tarildim.\n"
                     "3-maslahat: Makedoniya qiroli Filipp II ga qarshi olovli nutqlar ('Filippikalar') so'zlab, Afina "
                     'erkinligini himoya qildim.',
               'ru': 'Подсказка 1: В юности страдал косноязычием и слабым голосом, тренируя речь с камешками во рту на '
                     'берегу шумящего моря.\n'
                     'Подсказка 2: Стал непревзойденным оратором Древней Греции, образцом риторического мастерства.\n'
                     'Подсказка 3: Автор знаменитых гневных речей («Филиппик») против царя Филиппа Македонского.',
               'en': 'Clue 1: Overcame a severe childhood speech impediment by practicing declamation with pebbles in '
                     'his mouth.\n'
                     'Clue 2: Acclaimed as the greatest orator of classical antiquity.\n'
                     "Clue 3: Delivered the impassioned 'Philippics' against Philip II of Macedon to preserve Athenian "
                     'liberty.'},
  'options': {'uz': ['Sitseron', 'Isokrat', 'Eshin', 'Demosfen'],
              'ru': ['Цицерон', 'Исократ', 'Эсхин', 'Демосфен'],
              'en': ['Cicero', 'Isocrates', 'Aeschines', 'Demosthenes']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Demosfen', 'ru': 'Демосфен', 'en': 'Demosthenes'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Demosthenes_statue_Louvre.jpg/640px-Demosthenes_statue_Louvre.jpg',
  'fun_fact': {'uz': 'Demosfen nutq mashqlariga butun diqqatini qaratish uchun sochini yarmini qirdirib tashlagan, '
                     "toki ko'chaga chiqa olmay uyda shug'ullansin.",
               'ru': 'Чтобы не отвлекаться от занятий ораторским искусством, Демосфен выбривал половину головы и '
                     'месяцами сидел взаперти.',
               'en': 'To discipline himself to stay home and study rhetoric, Demosthenes shaved half his head so he '
                     'was too embarrassed to go outside.'},
  'aliases': ['demosfen', 'filippikalar', 'демосфен', 'филиппики', 'demosthenes']},
 {'id': 'hist_who_085',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Rim Respublikasining eng mashhur notig'i, huquqshunosi va faylasufiman.\n"
                     "2-maslahat: Mil. avv. 63 yilda konsul bo'lib, Katilina fitnasini fosh qildim va 'O tempora, o "
                     "mores!' (Ey zamonlar, ey axloqlar!) deb xitob qildim.\n"
                     "3-maslahat: Respublikani diktaturadan himoya qildim; Mark Antoniy buyrug'i bilan qatl etildim.",
               'ru': 'Подсказка 1: Римский оратор, философ и государственный деятель, эталон латинского языка.\n'
                     'Подсказка 2: Будучи консулом в 63 году до н.э., раскрыл заговор Катилины со словами: «О времена, '
                     'о нравы!» (O tempora, o mores!).\n'
                     'Подсказка 3: До последнего защищал республиканский строй, произнеся «Филиппики» против Марка '
                     'Антония.',
               'en': "Clue 1: Rome's greatest orator, lawyer, and philosopher whose writings set the standard for "
                     'classical Latin.\n'
                     "Clue 2: As consul in 63 BC, thwarted the Catiline Conspiracy, lamenting: 'O tempora, o mores!'.\n"
                     "Clue 3: Championed the dying Roman Republic, executed on Mark Antony's orders in 43 BC."},
  'options': {'uz': ['Mark Tulliy Sitseron', 'Seneka', 'Katon Kichik', 'Kvintilian'],
              'ru': ['Марк Туллий Цицерон', 'Сенека', 'Катон Младший', 'Квинтилиан'],
              'en': ['Marcus Tullius Cicero', 'Seneca the Younger', 'Cato the Younger', 'Quintilian']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Mark Tulliy Sitseron', 'ru': 'Марк Туллий Цицерон', 'en': 'Marcus Tullius Cicero'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cicero_bust_Capitoline.jpg/640px-Cicero_bust_Capitoline.jpg',
  'fun_fact': {'uz': "Sitseron lotin tiliga falsafiy atamalarni kiritgan (masalan, 'humanitas', 'natura') va uning "
                     "asarlari Uyg'onish davriga kuchli ta'sir ko'rsatgan.",
               'ru': 'Гуманисты эпохи Возрождения считали слог Цицерона непревзойденной вершиной европейской '
                     'словесности.',
               'en': "Petrarch's rediscovery of Cicero's letters in 1345 is widely considered the spark of the "
                     'Renaissance.'},
  'aliases': ['sitseron', 'mark tulliy sitseron', 'цицерон', 'марк туллий цицерон', 'cicero']},
 {'id': 'hist_who_086',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Ispaniyada tug'ilgan birinchi provinsiyalik Rim imperatoriman.\n"
                     '2-maslahat: Dakiya (Ruminiya) va Parfiyani zabt etib, Rim imperiyasi chegaralarini tarixdagi eng '
                     'ulkan kengligiga (117 yil) yetkazdim.\n'
                     "3-maslahat: Rim Senati tomonidan rasman 'Eng yaxshi hukmdor' (Optimus Princeps) unvoni bilan "
                     'taqdirlanganman; Rimda mashhur ustunim bor.',
               'ru': 'Подсказка 1: Первый римский император родом из провинции (Испании).\n'
                     'Подсказка 2: Покорил Дакию и победил Парфию, расширив границы империи до максимума за всю ее '
                     'историю.\n'
                     'Подсказка 3: Получил от сената почетный титул «Наилучший принцепс» (Optimus Princeps); в Риме '
                     'стоит моя колонна.',
               'en': 'Clue 1: First Roman emperor born outside Italy, hailing from Hispania Baetica.\n'
                     'Clue 2: Conquered Dacia and pushed across Mesopotamia to the Persian Gulf, achieving the '
                     "Empire's maximum territorial extent in 117 AD.\n"
                     "Clue 3: Honored by the Senate with the official title 'Optimus Princeps' (Best Ruler); "
                     "commemorated by Trajan's Column."},
  'options': {'uz': ['Adrian', 'Trayan (Mark Ulpiy Nerva)', 'Mark Avreliy', 'Neron'],
              'ru': ['Адриан', 'Траян (Марк Ульпий Нерва Траян)', 'Марк Аврелий', 'Нерон'],
              'en': ['Hadrian', 'Trajan (Optimus Princeps)', 'Marcus Aurelius', 'Nero']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Trayan (Mark Ulpiy Nerva)',
                     'ru': 'Траян (Марк Ульпий Нерва Траян)',
                     'en': 'Trajan (Optimus Princeps)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Trajan_statue_Glyptothek.jpg/640px-Trajan_statue_Glyptothek.jpg',
  'fun_fact': {'uz': "Keyingi barcha Rim imperatorlari taxtga o'tirayotganda Senat ularga: 'Avgustdan baxtliroq, "
                     "Trayandan yaxshiroq bo'l!' (Felicior Augusto, melior Traiano) deb tilak bildirgan.",
               'ru': 'Традиционное пожелание новым императорам гласило: «Будь счастливее Августа и лучше Траяна».',
               'en': "Subsequent Roman emperors were inaugurated with the prayer: 'Be more fortunate than Augustus and "
                     "better than Trajan'."},
  'aliases': ['trayan', 'trayan ustuni', 'траян', 'колонна траяна', 'trajan']},
 {'id': 'hist_who_087',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: XV asrda Valaxiya (zamonaviy Ruminiya) knyazi bo'lganman.\n"
                     "2-maslahat: Dushmanlarim va jinoyatchilarni qoziqqa o'tqazishdek shafqatsiz usuli bilan 'Sepesh' "
                     '(Qoziqli) laqabini oldim.\n'
                     '3-maslahat: Usmonli sultoni Mehmed II ga qarshi partizanlik urushini olib bordim; mening laqabim '
                     "Brem Stokerning 'Drakula' asariga asos bo'ldi.",
               'ru': 'Подсказка 1: Господарь Валахии в XV веке, боровшийся за независимость от Османской империи.\n'
                     'Подсказка 2: Прозван Цепеш («Колосажатель») за жестокие публичные казни врагов и предателей.\n'
                     'Подсказка 3: Носил родовое прозвище Дракула («Сын дракона»), послужившее прототипом знаменитого '
                     'литературного вампира.',
               'en': 'Clue 1: 15th-century Prince of Wallachia who led guerilla resistance against the Ottoman '
                     'Empire.\n'
                     "Clue 2: Notorious for his terrifying favorite method of mass execution, earning the moniker 'The "
                     "Impaler' (Țepeș).\n"
                     "Clue 3: His patronymic 'Dracula' (Son of the Dragon) was adapted by Bram Stoker for his famous "
                     'vampire novel.'},
  'options': {'uz': ['Ivan Grozniy', 'Stefan Buyuk', 'Vlad III Sepesh (Drakula / Qoziqli Vlad)', 'Mixay Jasur'],
              'ru': ['Иван Грозный', 'Стефан Великий', 'Влад III Цепеш (Дракула / Колосажатель)', 'Михай Храбрый'],
              'en': ['Ivan the Terrible',
                     'Stephen the Great',
                     'Vlad the Impaler (Vlad III Dracula)',
                     'Michael the Brave']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Vlad III Sepesh (Drakula / Qoziqli Vlad)',
                     'ru': 'Влад III Цепеш (Дракула / Колосажатель)',
                     'en': 'Vlad the Impaler (Vlad III Dracula)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Vlad_Tepes_Ambras.jpg/640px-Vlad_Tepes_Ambras.jpg',
  'fun_fact': {'uz': "Ruminiyada Vlad Sepesh vahshiy monstr emas, balki qattiqqo'l qonun himoyachisi va Usmonli "
                     'bosqiniga qarshi kurashgan milliy qahramon hisoblanadi.',
               'ru': 'В румынском фольклоре Влад Цепеш почитается как справедливый защитник простых людей и '
                     'непримиримый борец с коррупцией.',
               'en': 'In Romanian national memory, Vlad is celebrated not as a monster but as a heroic defender of '
                     'sovereignty and ruthless opponent of corruption.'},
  'aliases': ['drakula', 'vlad sepesh', 'qoziqli vlad', 'дракула', 'влад цепеш', 'vlad the impaler', 'dracula']},
 {'id': 'hist_who_088',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 1547 yilda Moskva Uspenskiy soborida birinchi bo'lib rasman 'Butun Rossiya podshosi' "
                     '(Tsar) deb toj kiydim.\n'
                     '2-maslahat: Qozon va Astraxon xonliklarini bosib olib, Sibirni zabt etishni boshladim; '
                     "'Oprichnina' qatag'onini o'tkazdim.\n"
                     "3-maslahat: Qizil maydondagi Vasiliy Blajenniy soborini qurdirdim; g'azab ustida o'z o'g'lim "
                     "Ivanni o'ldirib qo'ydim.",
               'ru': 'Подсказка 1: Первый венчанный русский царь из династии Рюриковичей (1547).\n'
                     'Подсказка 2: Покорил Казанское и Астраханское ханства, создал опричнину и Судебник 1550 года.\n'
                     'Подсказка 3: Построил собор Василия Блаженного на Красной площади; в припадке гнева смертельно '
                     'ранил собственного сына.',
               'en': 'Clue 1: First crowned Tsar of All Russia in 1547, reigning for over five decades.\n'
                     'Clue 2: Conquered the Khanates of Kazan and Astrakhan and unleashed the ruthless Oprichnina '
                     'police state.\n'
                     "Clue 3: Commissioned Saint Basil's Cathedral on Red Square; fatally struck his own eldest son in "
                     'a fit of rage.'},
  'options': {'uz': ['Ivan III Buyuk', 'Boris Godunov', 'Pyotr I', 'Ivan IV Grozniy (Dahshatli Ivan)'],
              'ru': ['Иван III Великий', 'Борис Годунов', 'Петр I', 'Иван IV Грозный'],
              'en': ['Ivan the Great', 'Boris Godunov', 'Peter the Great', 'Ivan the Terrible']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ivan IV Grozniy (Dahshatli Ivan)', 'ru': 'Иван IV Грозный', 'en': 'Ivan the Terrible'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ivan_the_Terrible_Vasnetsov.jpg/640px-Ivan_the_Terrible_Vasnetsov.jpg',
  'fun_fact': {'uz': "Afsonaga ko'ra, Ivan Grozniy Vasiliy Blajenniy sobori me'morlari Barma va Postnik boshqa hech "
                     "qachon bunday go'zal bino qurmasliklari uchun ularning ko'zlarini ko'r qilgan.",
               'ru': 'Мрачная легенда гласит, что царь велел ослепить зодчих собора Василия Блаженного, чтобы они не '
                     'повторили этот шедевр.',
               'en': "Apocryphal lore claims Ivan blinded the architects of Saint Basil's Cathedral so they could "
                     'never duplicate its kaleidoscopic beauty.'},
  'aliases': ['ivan grozniy', 'ivan iv', 'иван грозный', 'иван iv', 'ivan the terrible']},
 {'id': 'hist_who_089',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Yaponiyani birlashtirgan uch buyuk sarkardaning uchinchisiman.\n'
                     "2-maslahat: 1600 yilda mashhur Sekigahara jangida g'alaba qozonib, butun Yaponiya ustidan to'la "
                     "nazorat o'rnatdim.\n"
                     "3-maslahat: Tokugava syogunligiga asos soldim va poytaxtni Edoga (hozirgi Tokio) ko'chirdim; "
                     'mening sulolam 250 yildan ortiq hukmronlik qildi.',
               'ru': 'Подсказка 1: Третий великий объединитель феодальной Японии.\n'
                     'Подсказка 2: Одержал решающую победу в исторической битве при Сэкигахаре в 1600 году.\n'
                     'Подсказка 3: Основатель сёгуната Токугава, перенесший столицу в Эдо (современный Токио) и '
                     'правивший 250 лет мирного периода.',
               'en': "Clue 1: Third of the 'Three Great Unifiers' of Japan after Nobunaga and Hideyoshi.\n"
                     'Clue 2: Won the epochal Battle of Sekigahara in 1600, subjugating rival daimyo factions.\n'
                     'Clue 3: Established the Tokugawa Shogunate, moving the capital to Edo (Tokyo) and ushering in '
                     '250 years of peace.'},
  'options': {'uz': ['Tokugava Ieyasu', 'Oda Nobunaga', 'Toyotomi Xideyosi', 'Minamoto no Yoritomo'],
              'ru': ['Токугава Иэясу', 'Ода Нобунага', 'Тоётоми Хидэёси', 'Минамото-но Ёритомо'],
              'en': ['Tokugawa Ieyasu', 'Oda Nobunaga', 'Toyotomi Hideyoshi', 'Minamoto no Yoritomo']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Tokugava Ieyasu', 'ru': 'Токугава Иэясу', 'en': 'Tokugawa Ieyasu'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tokugawa_Ieyasu_portrait.jpg/640px-Tokugawa_Ieyasu_portrait.jpg',
  'fun_fact': {'uz': "Yapon maqolida aytilishicha: 'Nobunaga pirojnoye tayyorladi, Xideyosi pishirdi, Ieyasu esa uni "
                     "yeb qo'ydi'.",
               'ru': 'Японская поговорка гласит: «Нобунага месил глину национального пирога, Хидэёси испек его, а '
                     'Иэясу съел».',
               'en': "A famous Japanese proverb summarizes the unifiers: 'Nobunaga mixed the dough, Hideyoshi baked "
                     "the pie, and Ieyasu ate it'."},
  'aliases': ['tokugava', 'tokugava ieyasu', 'токугава', 'токугава иэясу', 'tokugawa', 'tokugawa ieyasu']},
 {'id': 'hist_who_090',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Yaponiyadagi 'Sengoku' (Urushayotgan viloyatlar) davrining eng shafqatsiz va novator "
                     'daymyosiman.\n'
                     "2-maslahat: 1575 yilda Nagasino jangida ilk bor o'tsochar qurollar (arkebuza)dan uch qatorli "
                     "uzluksiz o'q otish taktikasini qo'llab g'alaba qozondim.\n"
                     "3-maslahat: Yaponiyani birlashtirishni birinchi bo'lib boshladim; 1582 yilda o'z sarkardam Aketi "
                     'Mitsuxide xiyonati sababli Xonnodzi ibodatxonasida seppuku (harakiri) qildim.',
               'ru': 'Подсказка 1: Первый из трех великих объединителей Японии эпохи Сэнгоку.\n'
                     'Подсказка 2: Массово вооружил армию огнестрельным оружием, разгромив элитную конницу Такеды при '
                     'Нагасино.\n'
                     'Подсказка 3: Погиб в Киото в горящем храме Хонно-дзи в результате внезапного мятежа своего '
                     'генерала Акэти Мицухидэ.',
               'en': "Clue 1: First of Japan's Three Great Unifiers, rising from Owari Province in the Sengoku "
                     'period.\n'
                     'Clue 2: Revolutionized samurai combat at Nagashino (1575) by deploying matchlock arquebus '
                     'volleys in rotating ranks.\n'
                     'Clue 3: Betrayed by his vassal Akechi Mitsuhide in 1582, committing seppuku inside burning '
                     'Honno-ji temple in Kyoto.'},
  'options': {'uz': ['Tokugava Ieyasu', 'Oda Nobunaga', 'Toyotomi Xideyosi', 'Takeda Singen'],
              'ru': ['Токугава Иэясу', 'Ода Нобунага', 'Тоётоми Хидэёси', 'Такэда Сингэн'],
              'en': ['Tokugawa Ieyasu', 'Oda Nobunaga', 'Toyotomi Hideyoshi', 'Takeda Shingen']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Oda Nobunaga', 'ru': 'Ода Нобунага', 'en': 'Oda Nobunaga'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Oda_Nobunaga_portrait.jpg/640px-Oda_Nobunaga_portrait.jpg',
  'fun_fact': {'uz': "Oda Nobunaganing shaxsiy muhri 'Tenka Fubu' — 'Butun mamlakat qurol kuchi bilan bo'ysundirilsin' "
                     'degan shiorni aks ettirgan.',
               'ru': 'Девизом Нобунаги было «Тэнка Фубу» — «Военное владычество над всей Поднебесной».',
               'en': "Nobunaga's personal seal carried the motto 'Tenka Fubu' ('All the realm under military rule')."},
  'aliases': ['oda nobunaga', 'nobunaga', 'ода нобунага', 'нобунага', 'oda nobunaga']},
 {'id': 'hist_who_091',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Oddiy dehqon oilasida tug'ilib, Oda Nobunaganing sandallarini ko'tarib yuruvchi "
                     'xizmatkoridan boshlaganman.\n'
                     "2-maslahat: Dehqonlardan barcha qurollarni tortib oluvchi 'Qilich ovi' (Katanagari) qonunini "
                     "chiqardim va ulug'vor Osaka qasrini qurdirdim.\n"
                     "3-maslahat: Butun Yaponiyani birlashtirib, 'Kampaku' (Bosh vazir/Regent) bo'ldim va Koreyaga "
                     'ikki marta harbiy yurish qildim.',
               'ru': 'Подсказка 1: Выходец из низов крестьянства, поднявшийся до фактического правителя Японии.\n'
                     'Подсказка 2: Построил неприступный замок в Осаке и провел «охоту за мечами», разоружив '
                     'крестьян.\n'
                     'Подсказка 3: Объединил страну после гибели Нобунаги и предпринял масштабное вторжение в Корею '
                     '(Имджинская война).',
               'en': 'Clue 1: Peasant-born general who rose from a lowly sandal-bearer to rule all of feudal Japan.\n'
                     'Clue 2: Built the grand Osaka Castle and enacted the Great Sword Hunt disarming all '
                     'non-samurai.\n'
                     'Clue 3: Completed the unification of Japan as Kampaku and launched the Imjin Wars into Korea.'},
  'options': {'uz': ['Oda Nobunaga', 'Tokugava Ieyasu', 'Toyotomi Xideyosi', 'Date Masamune'],
              'ru': ['Ода Нобунага', 'Токугава Иэясу', 'Тоётоми Хидэёси', 'Датэ Масамунэ'],
              'en': ['Oda Nobunaga', 'Tokugawa Ieyasu', 'Toyotomi Hideyoshi', 'Date Masamune']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Toyotomi Xideyosi', 'ru': 'Тоётоми Хидэёси', 'en': 'Toyotomi Hideyoshi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Toyotomi_Hideyoshi_portrait.jpg/640px-Toyotomi_Hideyoshi_portrait.jpg',
  'fun_fact': {'uz': "Xideyosi choy marosimining buyuk ishqibozi bo'lib, sof oltindan yasalgan ko'chma oltin choyxona "
                     'yaratgan.',
               'ru': 'Хидэёси построил знаменитую Золотую чайную комнату, стены и утварь которой были покрыты чистым '
                     'золотом.',
               'en': 'Hideyoshi commissioned a portable Golden Tea Room lined with solid gold leaf to host the Grand '
                     'Kitano Tea Ceremony.'},
  'aliases': ['xideyosi', 'toyotomi xideyosi', 'тоётоми хидэёси', 'хидэёси', 'toyotomi hideyoshi']},
 {'id': 'hist_who_092',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Koreyaning Choson sulolasiga mansub to'rtinchi qiroliman (1418-1450).\n"
                     "2-maslahat: Ilm-fan markazi 'Zodagonlar xonasi'ni (Jiphyeonjeon) tashkil etib, quyosh soatlari "
                     "va yomg'ir o'lchagichlarni ixtiro qildirdim.\n"
                     "3-maslahat: Oddiy xalq oson o'qiy olishi uchun 28 harfli milliy koreys fonetik alifbosi — "
                     "'Hangil'ni (Hangul) shaxsan ixtiro qildim.",
               'ru': 'Подсказка 1: Четвертый правитель корейской династии Чосон, признанный величайшим монархом в '
                     'истории Кореи.\n'
                     'Подсказка 2: Развил астрономию, медицину и создал первый в мире стандартизированный дождемер '
                     '(чхыгуги).\n'
                     'Подсказка 3: Создал национальный корейский алфавит хангыль («Хунмин чоным»), чтобы каждый '
                     'гражданин мог научиться грамоте.',
               'en': "Clue 1: Fourth monarch of Korea's Joseon Dynasty who reigned from 1418 to 1450.\n"
                     "Clue 2: Promoted scientific advancements including the world's first standardized rain gauge "
                     '(cheugugi).\n'
                     "Clue 3: Personally designed and introduced the phonetic Korean alphabet 'Hangul' in 1443 to "
                     'overcome illiteracy.'},
  'options': {'uz': ['Txejo', 'Yonsangun', 'Chonjo', 'Buyuk Sejon (Qirol Sejon)'],
              'ru': ['Тхэджо', 'Ёнсан-гун', 'Чонджо', 'Седжон Великий (ван Чосона)'],
              'en': ['Taejo of Joseon',
                     'Yeonsangun of Joseon',
                     'Jeongjo of Joseon',
                     'Sejong the Great (King of Joseon)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Buyuk Sejon (Qirol Sejon)',
                     'ru': 'Седжон Великий (ван Чосона)',
                     'en': 'Sejong the Great (King of Joseon)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Statue_of_King_Sejong_Seoul.jpg/640px-Statue_of_King_Sejong_Seoul.jpg',
  'fun_fact': {'uz': "Hangil alifbosi harflarining shakli inson tovush chiqarayotganda og'iz, til va tomoq holatini "
                     'takrorlaydi va dunyodagi eng ilmiy mukammal alifbo hisoblanadi.',
               'ru': 'Хангыль считается лингвистами самым совершенным и логичным алфавитом мира: форма букв имитирует '
                     'положение органов речи при звуке.',
               'en': "Linguists praise Hangul as the world's most scientifically designed alphabet; consonant shapes "
                     'mimic the vocal organs pronouncing them.'},
  'aliases': ['sejon', 'buyuk sejon', 'hangil', 'седжон', 'седжон великий', 'хангыль', 'sejong the great', 'hangul']},
 {'id': 'hist_who_093',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Koreya tarixidagi eng buyuk dengiz qo'mondoni va milliy qahramonman.\n"
                     "2-maslahat: Zirhli temir qoplamali va to'plar bilan jihozlangan 'Toshbaqa-kemalar'ni (Gobukson) "
                     'yaratdim.\n'
                     '3-maslahat: 1597 yilgi Myonnyan dengiz jangida atigi 13 ta kema bilan 133 ta yapon harbiy '
                     'kemasini tor-mor etdim.',
               'ru': 'Подсказка 1: Легендарный корейский флотоводец времен Имджинской войны с Японией.\n'
                     'Подсказка 2: Сконструировал первые в мире броненосные «корабли-черепахи» (кобуксоны), изрыгавшие '
                     'дым и ядра.\n'
                     'Подсказка 3: В битве в проливе Мёнрян с 13 кораблями разгромил вражеский флот из 133 боевых '
                     'судов, не потеряв ни одного своего.',
               'en': 'Clue 1: Celebrated Korean naval commander who remained undefeated throughout the Imjin War.\n'
                     "Clue 2: Innovated and deployed armored 'Turtle Ships' (Geobukseon) equipped with spiked roofs "
                     'and cannons.\n'
                     "Clue 3: Achieved one of naval history's greatest miracles at Myeongnyang (1597), routing 133 "
                     'Japanese ships with only 13 vessels.'},
  'options': {'uz': ['Admiral I Sun Sin', 'Sejon', 'Kvon Yul', 'Kim Si Min'],
              'ru': ['Адмирал Ли Сунсин', 'Седжон', 'Квон Юль', 'Ким Си Мин'],
              'en': ['Admiral Yi Sun-sin', 'King Sejong', 'Kwon Yul', 'Kim Si-min']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Admiral I Sun Sin', 'ru': 'Адмирал Ли Сунсин', 'en': 'Admiral Yi Sun-sin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Yi_Sun-sin_statue_Seoul.jpg/640px-Yi_Sun-sin_statue_Seoul.jpg',
  'fun_fact': {'uz': "I Sun Sin o'zining so'nggi jangi — Noryang jangida yapon o'qidan yaralangach: 'Mening o'limimni "
                     "bildirmang, jangni davom ettiring!' deb buyruq bergan.",
               'ru': 'Умирая от ранения в последней битве при Норянге, адмирал приказал племяннику: «Битва в разгаре. '
                     'Бейте в барабан и не говорите о моей смерти».',
               'en': "Mortally wounded at the Battle of Noryang in 1598, his dying words were: 'The battle is at its "
                     "height; do not announce my death.'"},
  'aliases': ['i sun sin',
              'admiral i sun sin',
              'toshbaqa kema',
              'ли сунсин',
              'адмирал ли сунсин',
              'yi sun-sin',
              'turtle ship']},
 {'id': 'hist_who_094',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Usmonli saltanatining yettinchi sultoni bo'lib, atigi 21 yoshimda tarixni "
                     "o'zgartirdim.\n"
                     "2-maslahat: Katta to'plar quydirib, kemalarni tunda quruqlik (yog'langan g'o'lalar) orqali Oltin "
                     "Shox qo'ltig'iga tushirdim.\n"
                     '3-maslahat: 1453 yil 29 mayda Konstantinopolni zabt etib, 1100 yillik Vizantiya imperiyasiga '
                     "chek qo'ydim va 'Fotih' (Fathchi) nomini oldim.",
               'ru': 'Подсказка 1: Османский султан, взошедший на трон в юности и свободно говоривший на семи языках.\n'
                     'Подсказка 2: Приказал перетащить боевые корабли по суше на бревнах в бухту Золотой Рог в обход '
                     'цепи.\n'
                     'Подсказка 3: 29 мая 1453 года штурмом взял неприступный Константинополь, положив конец '
                     'Византийской империи.',
               'en': 'Clue 1: Seventh Ottoman Sultan who changed the course of world history at age twenty-one.\n'
                     'Clue 2: Transported galleys overland on greased logs into the Golden Horn to bypass Byzantine '
                     'sea chains.\n'
                     'Clue 3: Captured Constantinople on May 29, 1453, ending the Byzantine Empire and earning the '
                     "cognomen 'The Conqueror' (Fatih)."},
  'options': {'uz': ['Sulaymon Qonuniy', 'Sulton Mehmed II Fathchi (Fotih)', 'Salim I', 'Murod II'],
              'ru': ['Сулейман Великолепный', 'Султан Мехмед II Фатих (Завоеватель)', 'Селим I', 'Мурад II'],
              'en': ['Suleiman the Magnificent', 'Mehmed II the Conqueror (Fatih)', 'Selim I', 'Murad II']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Sulton Mehmed II Fathchi (Fotih)',
                     'ru': 'Султан Мехмед II Фатих (Завоеватель)',
                     'en': 'Mehmed II the Conqueror (Fatih)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Gentile_Bellini_-_Portrait_of_Sultan_Mehmet_II_-_National_Gallery.jpg/640px-Gentile_Bellini_-_Portrait_of_Sultan_Mehmet_II_-_National_Gallery.jpg',
  'fun_fact': {'uz': "Mehmed II Konstantinopolni zabt etgach, o'zini 'Qaysari Rum' (Rim imperatori) deb e'lon qilgan "
                     'va shaharni imperiya poytaxtiga aylantirgan.',
               'ru': 'Взяв византийскую столицу, Мехмед принял титул «Кайзер-и Рум» (Цезарь Рима), считая Османскую '
                     'империю преемницей Рима.',
               'en': "After taking Constantinople, Mehmed II claimed the title 'Kayser-i Rum' (Caesar of Rome), "
                     'viewing his empire as the successor to Rome.'},
  'aliases': ['mehmed ii',
              'fotih',
              'mehmed fathchi',
              'мехмед ii',
              'мехмед фатих',
              'mehmed the conqueror',
              'mehmed ii']},
 {'id': 'hist_who_095',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Usmonlilarning to'rtinchi sultoni bo'lib, qo'shinlarni favqulodda tezkor "
                     "harakatlantirganim uchun 'Yildirim' (Chaqmoq) laqabini olganman.\n"
                     '2-maslahat: 1396 yilda Nikopol jangida salibchilarning birlashgan Yevropa armiyasini tor-mor '
                     'etdim.\n'
                     "3-maslahat: 1402 yilda Anqara jangida Amir Temur bilan to'qnashdim va mag'lub bo'lib asirga "
                     'tushdim.',
               'ru': 'Подсказка 1: Четвертый султан Османской империи, прозванный за стремительность маневров '
                     '«Молниеносным» (Йылдырым).\n'
                     'Подсказка 2: Наголову разгромил объединенное европейское рыцарское войско в битве при Никополе в '
                     '1396 году.\n'
                     'Подсказка 3: Был разбит и взят в плен Амиром Темуром в грандиозной Ангорской битве 1402 года.',
               'en': "Clue 1: Fourth Ottoman Sultan nicknamed 'The Thunderbolt' (Yıldırım) for his blistering "
                     'battlefield mobility.\n'
                     'Clue 2: Annihilated a major European Crusader army at the Battle of Nicopolis in 1396.\n'
                     'Clue 3: Clashed with Amir Timur at the Battle of Ankara in 1402, where he was defeated and '
                     'captured.'},
  'options': {'uz': ['Murod I', 'Usmon I', "Sulton Boyazid I Yildirim ('Chaqmoq')", 'Mehmed I'],
              'ru': ['Мурад I', 'Осман I', 'Султан Баязид I Молниеносный (Йылдырым)', 'Мехмед I'],
              'en': ['Murad I', 'Osman I', 'Bayezid I (The Thunderbolt)', 'Mehmed I']},
  'correct_index': 2,
  'correct_answer': {'uz': "Sulton Boyazid I Yildirim ('Chaqmoq')",
                     'ru': 'Султан Баязид I Молниеносный (Йылдырым)',
                     'en': 'Bayezid I (The Thunderbolt)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Bayezid_I_miniature.jpg/640px-Bayezid_I_miniature.jpg',
  'fun_fact': {'uz': "Amir Temur Boyazidni asir olgach, unga izzat-ikrom ko'rsatgan va o'z chodirida oliy martabali "
                     'mehmon sifatida kutib olgan.',
               'ru': 'Легенда о том, что Темур держал Баязида в железной клетке, была опровергнута историками: к '
                     'султану относились с подобающими почестями.',
               'en': 'Western myths claimed Timur kept Bayezid in an iron cage, but historical accounts show Timur '
                     'treated the captured Sultan with royal dignity.'},
  'aliases': ['boyazid',
              'boyazid yildirim',
              'chaqmoq boyazid',
              'баязид молниеносный',
              'баязид i',
              'bayezid i',
              'yildirim']},
 {'id': 'hist_who_096',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Usmonli saltanatining to'qqizinchi sultoni bo'lib, o'zining qat'iyatliligi bilan "
                     "'Yavuz' (Qahrli) laqabini olganman.\n"
                     '2-maslahat: Choldiron jangida (1514) Safaviylar shohi Ismoil I ni yengdim.\n'
                     '3-maslahat: Mamluklarni tor-mor etib, Misr, Suriya va muqaddas Makka hamda Madinani egalladim; '
                     "birinchi Usmonli xalifasi bo'ldim.",
               'ru': 'Подсказка 1: Османский правитель, за восемь лет правления утроивший территорию империи.\n'
                     'Подсказка 2: Разбил персидского шаха Исмаила I при Чалдыране с помощью сокрушительного '
                     'артиллерийского огня.\n'
                     'Подсказка 3: Покорил державу мамлюков в Египте и Сирии в 1517 году, приняв титул халифа всех '
                     'мусульман.',
               'en': 'Clue 1: Ninth Ottoman Sultan who tripled the size of the empire in just eight relentless years '
                     '(1512-1520).\n'
                     'Clue 2: Defeated Shah Ismail I of the Safavids at Chaldiran in 1514 with concentrated field '
                     'artillery.\n'
                     'Clue 3: Conquered Mamluk Egypt and the Levant in 1517, assuming custody of Mecca and Medina as '
                     'the first Ottoman Caliph.'},
  'options': {'uz': ['Sulaymon Qonuniy', 'Boyazid II', 'Mehmed II', "Sulton Salim I Yavuz ('Qahrli')"],
              'ru': ['Сулейман Великолепный', 'Баязид II', 'Мехмед II', 'Султан Селим I Грозный (Явуз)'],
              'en': ['Suleiman the Magnificent', 'Bayezid II', 'Mehmed II', 'Selim I (The Grim / The Resolute)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Sulton Salim I Yavuz ('Qahrli')",
                     'ru': 'Султан Селим I Грозный (Явуз)',
                     'en': 'Selim I (The Grim / The Resolute)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Yavuz_Sultan_Selim.jpg/640px-Yavuz_Sultan_Selim.jpg',
  'fun_fact': {'uz': "Salim I Makka va Madinani egallagach, o'zini 'ikki muqaddas shahar hukmdori' emas, balki 'Xodimi "
                     "al-Haramayn' (Ikki muqaddas shahar xizmatkori) deb atagan.",
               'ru': 'Селим I отказался от титула владыки Мекки и Медины, назвав себя скромно «служителем обоих '
                     'священных городов».',
               'en': "Rather than claiming dominion, Selim adopted the humble title 'Khadim al-Haramayn' (Servant of "
                     'the Two Holy Sanctuaries).'},
  'aliases': ['salim i', 'yavuz', 'salim yavuz', 'селим явуз', 'селим i', 'selim i', 'selim the grim']},
 {'id': 'hist_who_097',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Chingizxonning nabirasi bo'lib, Mo'g'ullar imperiyasining beshinchi Buyuk xoni "
                     "bo'ldim.\n"
                     "2-maslahat: Xitoydagi Janubiy Sun sulolasini to'liq zabt etib, butun Xitoyni birlashtirdim va "
                     'Yuan sulolasiga asos soldim.\n'
                     "3-maslahat: Poytaxt Xonbaliqqa (Pekin) asos soldim; venetsiyalik sayyoh Marko Poloni o'z "
                     'saroyimda 17 yil xizmatda saqladim.',
               'ru': 'Подсказка 1: Внук Чингисхана, ставший пятым Великим ханом Монгольской империи.\n'
                     'Подсказка 2: Завоевал империю Сун, объединил Китай и основал монгольскую династию Юань.\n'
                     'Подсказка 3: Перенес столицу в Ханбалык (современный Пекин) и принимал при дворе венецианца '
                     'Марко Поло.',
               'en': 'Clue 1: Grandson of Genghis Khan who reigned as fifth Khagan of the Mongol Empire.\n'
                     'Clue 2: Conquered the Song Dynasty, becoming the first non-Han emperor to conquer and rule all '
                     'of China under the Yuan Dynasty.\n'
                     'Clue 3: Rebuilt Beijing as his imperial capital Dadu and famously hosted Venetian traveler Marco '
                     'Polo.'},
  'options': {'uz': ['Xubilayxon (Yuan imperatori)', 'Munke xon', 'Hulogu xon', 'Botuxon'],
              'ru': ['Хубилай (основатель династии Юань)', 'Мунке', 'Хулагу', 'Батый'],
              'en': ['Kublai Khan', 'Möngke Khan', 'Hulagu Khan', 'Batu Khan']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Xubilayxon (Yuan imperatori)',
                     'ru': 'Хубилай (основатель династии Юань)',
                     'en': 'Kublai Khan'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/YuanEmperorAlbumKhubilaiPortrait.jpg/640px-YuanEmperorAlbumKhubilaiPortrait.jpg',
  'fun_fact': {'uz': 'Xubilayxon Yaponiyani zabt etish uchun 1274 va 1281 yillarda ikkita ulkan flot yuborgan, biroq '
                     "'Kamikadze' (Ilohiy shamol) to'foni har ikkala flotni ham dengizda yo'q qilgan.",
               'ru': 'Обе морские армады Хубилая, отправленные на завоевание Японии, были разбиты священными тайфунами '
                     '«камикадзе».',
               'en': "Kublai's massive invasion fleets sent to conquer Japan in 1274 and 1281 were both destroyed by "
                     "the legendary 'Kamikaze' typhoons."},
  'aliases': ['xubilay', 'xubilayxon', 'хубилай', 'хубилай хан', 'kublai khan']},
 {'id': 'hist_who_098',
  'sub_mode': 'who_am_i',
  'question': {'uz': '1-maslahat: Oddiy temirchi oilasidan chiqqan Chingizxon va Botuxonning eng bosh harbiy strategi '
                     "bo'lganman.\n"
                     "2-maslahat: 32 ta davlatni zabt etgan, 65 ta maydon jangida g'alaba qozonib biror marta mag'lub "
                     "bo'lmagan tarixdagi eng muvaffaqiyatli sarkardaman.\n"
                     '3-maslahat: Kalka jangi (1223), Shayo jangi (Moxi) va Legnitsada Yevropa ritsarlarini bir '
                     "vaqtning o'zida bir necha yuz kilometr masofada muvofiqlashtirib tor-mor qilganman.",
               'ru': 'Подсказка 1: Величайший полководец Чингисхана и Батыя, выходец из рода урянхайцев.\n'
                     'Подсказка 2: Покорил 32 народа, выиграл 65 генеральных сражений и ни разу не потерпел '
                     'поражения.\n'
                     'Подсказка 3: Автор гениального плана одновременного разгрома европейских армий при Легнице и на '
                     'реке Шайо в 1241 году.',
               'en': 'Clue 1: Primary military strategist of Genghis Khan and Batu Khan, hailing from the Uriankhai '
                     'clan.\n'
                     'Clue 2: Conquered more territory than any other commander in history, winning 65 pitched battles '
                     'across 32 nations.\n'
                     'Clue 3: Coordinated the simultaneous destruction of Polish, German, and Hungarian armies across '
                     '500 miles at Legnica and Mohi in 1241.'},
  'options': {'uz': ["Jebe no'yon", 'Subutoy Bahodir (Subudoy)', 'Muqali', 'Jelme'],
              'ru': ['Джэбэ', 'Субэдэй (Субудай-багатур)', 'Мухали', 'Джэлмэ'],
              'en': ['Jebe', 'Subutai (Subutai Bahadur)', 'Muqali', 'Jelme']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Subutoy Bahodir (Subudoy)',
                     'ru': 'Субэдэй (Субудай-багатур)',
                     'en': 'Subutai (Subutai Bahadur)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Subutai_miniature.jpg/640px-Subutai_miniature.jpg',
  'fun_fact': {'uz': "Subutoy keksayganida shu qadar semiz bo'lganki, otga o'tira olmagan va qo'shinlarni maxsus "
                     'aravada yurib mohirona boshqargan.',
               'ru': 'В преклонном возрасте Субэдэй уже не мог держаться в седле из-за тучности и руководил войсками '
                     'из крытой повозки.',
               'en': 'In old age, Subutai grew too heavy to mount a horse and commanded his blitzkrieg offensives '
                     'riding in a specialized cart.'},
  'aliases': ['subutoy', 'subudoy', 'субэдэй', 'субудай', 'subutai']},
 {'id': 'hist_who_099',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: 'Bigl' (HMS Beagle) kemasida 5 yillik dunyo bo'ylab ilmiy sayohatga chiqqan ingliz "
                     'tabiatshunosiman.\n'
                     "2-maslahat: Galapagos orollaridagi vyuroklar (qushlar) va toshbaqalarni o'rganib tirik "
                     "organizmlarning o'zgarishini kuzatdim.\n"
                     "3-maslahat: 1859 yilda 'Turlarning kelib chiqishi' asarim bilan tabiiy tanlanish orqali biologik "
                     'evolyutsiya nazariyasiga asos soldim.',
               'ru': 'Подсказка 1: Английский натуралист, совершивший пятилетнее кругосветное плавание на корабле '
                     '«Бигль».\n'
                     'Подсказка 2: Исследовал уникальную фауну Галапагосских островов, заметив адаптацию вьюрков.\n'
                     'Подсказка 3: Создатель научной теории эволюции путем естественного отбора, изложенной в труде '
                     '«Происхождение видов» (1859).',
               'en': 'Clue 1: English naturalist who undertook a transformative five-year voyage on HMS Beagle.\n'
                     'Clue 2: Studied finches, mockingbirds, and giant tortoises on the Galápagos Islands.\n'
                     "Clue 3: Formulated the theory of biological evolution by natural selection in 'On the Origin of "
                     "Species' (1859)."},
  'options': {'uz': ['Gregor Mendel', 'Jan-Batist Lamark', 'Charlz Darvin', 'Alfred Uolles'],
              'ru': ['Грегор Мендель', 'Жан-Батист Ламарк', 'Чарльз Дарвин', 'Альфред Уоллес'],
              'en': ['Gregor Mendel', 'Jean-Baptiste Lamarck', 'Charles Darwin', 'Alfred Russel Wallace']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Charlz Darvin', 'ru': 'Чарльз Дарвин', 'en': 'Charles Darwin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Charles_Darwin_seated_crop.jpg/640px-Charles_Darwin_seated_crop.jpg',
  'fun_fact': {'uz': "Darvin o'z nazariyasini cherkov va jamiyat reaksiyasidan qo'rqib, 20 yildan ortiq vaqt davomida "
                     "e'lon qilmay yashirib yurgan.",
               'ru': 'Дарвин медлил с публикацией своей теории более 20 лет, опасаясь религиозного и общественного '
                     'скандала.',
               'en': 'Darwin hesitated for over two decades to publish his findings until Alfred Russel Wallace '
                     'independently arrived at the same idea.'},
  'aliases': ['darvin', 'charlz darvin', 'дарвин', 'чарльз дарвин', 'darwin', 'charles darwin']},
 {'id': 'hist_who_0100',
  'sub_mode': 'who_am_i',
  'question': {'uz': "1-maslahat: Venetsiyalik savdogar oilasida tug'ilganman, 17 yoshimda otam va amakim bilan "
                     "Sharqqa yo'l oldim.\n"
                     "2-maslahat: Ipak yo'li orqali O'rta Osiyo va Xitoyga yetib borib, Xubilayxon saroyida 17 yil "
                     'xizmat qildim.\n'
                     "3-maslahat: Genuya qamoqxonasida Rustichanoga o'z sayohatlarimni aytib berdim va Yevropani Osiyo "
                     "boyliklari bilan tanishtirgan 'Dunyo mo'jizalari kitobi'ni yaratdim.",
               'ru': 'Подсказка 1: Венецианский купец и путешественник, отправившийся в Китай по Шелковому пути в 1271 '
                     'году.\n'
                     'Подсказка 2: Провел 17 лет при дворе великого хана Хубилая, исполняя его дипломатические '
                     'поручения.\n'
                     'Подсказка 3: Находясь в генуэзской тюрьме, надиктовал Рустикелло знаменитую «Книгу о '
                     'разнообразии мира».',
               'en': 'Clue 1: Venetian merchant adventurer who embarked on a 24-year journey to Asia along the Silk '
                     'Road.\n'
                     'Clue 2: Served in the inner administration and diplomatic corps of Mongol Emperor Kublai Khan '
                     'for 17 years.\n'
                     "Clue 3: Dictated his astonishing memoirs 'The Travels of Marco Polo' to Rustichello da Pisa "
                     'while imprisoned in Genoa.'},
  'options': {'uz': ['Ibn Battuta', 'Vasko da Gama', 'Afanasiy Nikitin', 'Marko Polo'],
              'ru': ['Ибн Баттута', 'Васко да Гама', 'Афанасий Никитин', 'Марко Поло'],
              'en': ['Ibn Battuta', 'Vasco da Gama', 'Afanasy Nikitin', 'Marco Polo']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Marko Polo', 'ru': 'Марко Поло', 'en': 'Marco Polo'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Marco_Polo_mosaic.jpg/640px-Marco_Polo_mosaic.jpg',
  'fun_fact': {'uz': "Marko Polo o'lim to'shagida kitobidagi 'uydirmalar'dan tavba qilishni so'rashganida: 'Men "
                     "ko'rganlarimning hatto yarmini ham aytib berolmadim!' deb javob bergan.",
               'ru': 'На смертном одре Марко Поло ответил скептикам: «Я не рассказал и половины того, что видел своими '
                     'глазами».',
               'en': "Urged on his deathbed to recant his 'tall tales', Marco Polo famously replied: 'I did not write "
                     "half of what I saw.'"},
  'aliases': ['marko polo', 'марко поло', 'marco polo']},
 {'id': 'hist_art_001',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Rozetta toshi', 'Xammurapi qonunlari stelasi', 'Behistun qoyatosh yozuvi', 'Palermo toshi'],
              'ru': ['Розеттский камень', 'Стела законов Хаммурапи', 'Бехистунская надпись', 'Палермский камень'],
              'en': ['Rosetta Stone', 'Code of Hammurabi Stele', 'Behistun Inscription', 'Palermo Stone']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Rozetta toshi', 'ru': 'Розеттский камень', 'en': 'Rosetta Stone'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/23/Rosetta_Stone.JPG',
  'fun_fact': {'uz': 'Rozetta toshida bitta matn uch tilda (qadimgi misr iyerogliflari, demotik yozuv va qadimgi yunon '
                     "tili) bitilgani tufayli Jan-Fransua Shampolyon qadimgi Misr yozuvini o'qishga muvaffaq bo'lgan.",
               'ru': 'Благодаря параллельному тексту на трёх языках Жан-Франсуа Шампольон в 1822 году расшифровал '
                     'древнеегипетские иероглифы.',
               'en': 'Carved in 196 BC with three scripts (hieroglyphic, demotic, and Ancient Greek), it allowed '
                     'Jean-Francois Champollion to decipher Egyptian hieroglyphs.'},
  'aliases': ['rozetta toshi', 'rozetta', 'розеттский камень', 'rosetta stone', 'rosetta']},
 {'id': 'hist_art_002',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Agamemnon oltin niqobi',
                     'Tutanxamonning oltin dafn niqobi',
                     'Psusennes I oltin niqobi',
                     'Sipanning oltin niqobi'],
              'ru': ['Маска Агамемнона',
                     'Золотая погребальная маска Тутанхамона',
                     'Золотая маска Псусеннеса I',
                     'Золотая маска Сипана'],
              'en': ['Mask of Agamemnon',
                     'Gold Mask of Tutankhamun',
                     'Mask of Psusennes I',
                     'Mask of the Lord of Sipan']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Tutanxamonning oltin dafn niqobi',
                     'ru': 'Золотая погребальная маска Тутанхамона',
                     'en': 'Gold Mask of Tutankhamun'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/38/Tutankhamun_mask_macro.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 1323 yilda yasalgan ushbu 10 kg dan ortiq sof oltin, lapis-lazul va qimmatbaho '
                     'toshlardan iborat niqob 1922 yilda Govard Karter tomonidan topilgan.',
               'ru': 'Маска весом более 10 кг чистого золота, инкрустированная лазуритом и сердоликом, была обнаружена '
                     'Говардом Картером в неразграбленной гробнице KV62.',
               'en': 'Discovered by Howard Carter in 1922, this iconic 10.2 kg solid gold funerary mask rested '
                     'directly over the mummified face of King Tut.'},
  'aliases': ['tutanxamon niqobi',
              'tutanxamon',
              'маска тутанхамона',
              'тутанхамон',
              'tutankhamun mask',
              'mask of tutankhamun']},
 {'id': 'hist_art_003',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Trundxolm quyosh aravachasi',
                     'Ur qirollik aravachasi',
                     'Amudaryo xazinasi oltin aravachasi',
                     'Monteleone aravasi'],
              'ru': ['Солнечная повозка из Трундхольма',
                     'Колесница из царских гробниц Ура',
                     'Золотая колесница из Амударьинского клада (Сокровищ Окса)',
                     'Колесница из Монтелеоне'],
              'en': ['Trundholm Sun Chariot',
                     'Chariot of the Royal Tombs of Ur',
                     'Gold Chariot of the Oxus Treasure',
                     'Monteleone Chariot']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Amudaryo xazinasi oltin aravachasi',
                     'ru': 'Золотая колесница из Амударьинского клада (Сокровищ Окса)',
                     'en': 'Gold Chariot of the Oxus Treasure'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/34/Gold_chariot%2C_Oxus_treasure.jpg',
  'fun_fact': {'uz': 'Amudaryoning yuqori oqimi (Qubodiyon/Taxti Sangin)da topilgan bu mil. avv. V-IV asrlarga oid '
                     'Baqtriya-Ahamoniylar durdonasi hozirda Britaniya muzeyida saqlanadi.',
               'ru': 'Найдена на берегах Амударьи (Окса) в древней Бактрии; модель четвёрки лошадей с возницей и '
                     'вельможей выполнена из чистого золота.',
               'en': 'Discovered near the Amu Darya river in ancient Bactria, this 5th-4th century BC miniature gold '
                     'chariot is a crown jewel of the British Museum.'},
  'aliases': ['amudaryo xazinasi', 'oxus treasure', 'амударьинский клад', 'сокровища окса', 'oxus chariot']},
 {'id': 'hist_art_004',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Nabopolasar silindri', 'Kipr kuranti', 'Mixxat xronikasi', 'Buyuk Kir silindri'],
              'ru': ['Цилиндр Набопаласара', 'Кипрская призма', 'Вавилонская хроника', 'Цилиндр Кира Великого'],
              'en': ['Nabopolassar Cylinder', 'Prism of Sennacherib', 'Babylonian Chronicle', 'Cyrus Cylinder']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Buyuk Kir silindri', 'ru': 'Цилиндр Кира Великого', 'en': 'Cyrus Cylinder'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/77/Cyrus_Cylinder_front.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 539 yilda Bobilni zabt etgan Kir II buyrug'i bilan yozilgan bu gil silindr "
                     "ko'plab tarixchilar tomonidan insoniyat tarixidagi ilk inson huquqlari deklaratsiyasi deb "
                     'ataladi.',
               'ru': 'Глиняный цилиндр с клинописным указом царя Кира II Великого 539 г. до н.э., часто называемый '
                     'первой в мире декларацией прав человека.',
               'en': 'Issued in 539 BC after the conquest of Babylon, this baked clay cylinder proclaimed freedom of '
                     'religion and return of displaced peoples.'},
  'aliases': ['kir silindri', 'buyuk kir silindri', 'цилиндр кира', 'cyrus cylinder']},
 {'id': 'hist_art_005',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Sian terrakota armiyasi haykallari',
                     'Xan sulolasi terrakota chavandozlari',
                     'Min sulolasi tosh haykallari',
                     'Sanxingdui bronza askarlari'],
              'ru': ['Терракотовая армия императора Цинь Шихуанди',
                     'Терракотовые всадники династии Хань',
                     'Каменные стражи гробниц Мин',
                     'Бронзовые фигуры Саньсиндуй'],
              'en': ['Terracotta Army of Qin Shi Huang',
                     'Han Dynasty Terracotta Cavalry',
                     'Ming Dynasty Stone Guardians',
                     'Sanxingdui Bronze Figures']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Sian terrakota armiyasi haykallari',
                     'ru': 'Терракотовая армия императора Цинь Шихуанди',
                     'en': 'Terracotta Army of Qin Shi Huang'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Terracotta_Army%2C_View_of_Pit_1.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 210-209 yillarda yaratilgan 8000 dan ortiq askar, 520 ot va 130 aravadan iborat '
                     "armiyada har bir jangchining yuzi betakror va o'ziga xos qilib ishlangan.",
               'ru': 'Комплекс насчитывает более 8000 полноразмерных терракотовых воинов, причём ни одно из лиц солдат '
                     'не повторяется.',
               'en': "Buried with China's first Emperor Qin Shi Huang in 210-209 BC to protect him in the afterlife; "
                     'each of the 8,000+ clay soldiers has unique facial features.'},
  'aliases': ['terrakota armiyasi',
              'terrakota',
              'терракотовая армия',
              'цинь шихуанди',
              'terracotta army',
              'qin shi huang']},
 {'id': 'hist_art_006',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Ur-Nammu qonunlari lavhasi',
                     'Xammurapi qonunlari stelasi',
                     'Lipit-Ishtar lavhasi',
                     'Mesha stelasi'],
              'ru': ['Законы Ур-Намму',
                     'Базальтовая стела с Законами Хаммурапи',
                     'Законы Липит-Иштара',
                     'Стела царя Меша'],
              'en': ['Code of Ur-Nammu', 'Stele of the Code of Hammurabi', 'Code of Lipit-Ishtar', 'Mesha Stele']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Xammurapi qonunlari stelasi',
                     'ru': 'Базальтовая стела с Законами Хаммурапи',
                     'en': 'Stele of the Code of Hammurabi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/ca/Code_of_Hammurabi_stele_Louvre_Sb8.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 1754 yilda qora diorit (bazalt) toshga o'yib yozilgan 282 ta moddadan iborat "
                     'ushbu kodeks yuqori qismida shoh Xammurapining quyosh xudosi Shamashdan qonunlarni qabul qilishi '
                     'tasvirlangan.',
               'ru': 'На вершине чёрной базальтовой стелы царь Вавилона Хаммурапи получает свод законов из 282 статей '
                     'непосредственно от бога солнца и справедливости Шамаша.',
               'en': 'Carved into a 2.25-meter black diorite stele around 1754 BC, featuring 282 laws including the '
                     "famous principle of 'an eye for an eye'."},
  'aliases': ['xammurapi qonunlari', 'xammurapi', 'законы хаммурапи', 'code of hammurabi', 'hammurabi stele']},
 {'id': 'hist_art_007',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Aleksandriya astrolabiyasi',
                     "Geron bug' turbinasi (eolipil)",
                     'Antikitera mexanizmi',
                     'Arximed soati'],
              'ru': ['Александрийская астролябия', 'Эолипил Герона', 'Антикитерский механизм', 'Часы Архимеда'],
              'en': ['Alexandrian Astrolabe', 'Aeolipile of Hero', 'Antikythera Mechanism', 'Archimedes Water Clock']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Antikitera mexanizmi', 'ru': 'Антикитерский механизм', 'en': 'Antikythera Mechanism'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/eb/NAMA_Machine_d%27Anticyth%C3%A8re_1.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 150-100 yillarda qadimgi Yunonistonda yasalgan ushbu bronza tishli g'ildiraklar "
                     'tizimi quyosh, oy va sayyoralar harakatini hisoblaydigan dunyodagi ilk analog kompyuter '
                     'sanaladi.',
               'ru': 'Древнегреческое устройство с десятками бронзовых шестерён для расчёта движения небесных тел и '
                     'затмений — древнейший аналоговый компьютер.',
               'en': 'Salvaged from an ancient shipwreck near Greece, this 2nd-century BC complex geared mechanism is '
                     "widely regarded as the world's oldest analog computer."},
  'aliases': ['antikitera mexanizmi', 'antikitera', 'антикитерский механизм', 'antikythera mechanism', 'antikythera']},
 {'id': 'hist_art_008',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Nag-Xammadi kutubxonasi',
                     'Sinay kodeksi',
                     'Elefantina papiruslari',
                     "O'lik dengiz (Qumron) qo'lyozmalari"],
              'ru': ['Библиотека Наг-Хаммади',
                     'Синайский кодекс',
                     'Элефантинские папирусы',
                     'Свитки Мёртвого моря (Кумранские рукописи)'],
              'en': ['Nag Hammadi Library',
                     'Codex Sinaiticus',
                     'Elephantine Papyri',
                     'Dead Sea Scrolls (Qumran Caves Scrolls)']},
  'correct_index': 3,
  'correct_answer': {'uz': "O'lik dengiz (Qumron) qo'lyozmalari",
                     'ru': 'Свитки Мёртвого моря (Кумранские рукописи)',
                     'en': 'Dead Sea Scrolls (Qumran Caves Scrolls)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Dead_Sea_Scroll_-_part_of_Isaiah_Scroll_%28Isa_b%29.jpg',
  'fun_fact': {'uz': "1947 yilda cho'pon bolalar tomonidan Qumron g'orlaridagi sopol ko'zalarda topilgan pergament va "
                     "papirus o'ramlari Injilning eng qadimgi saqlanib qolgan qo'lyozmalari hisoblanadi.",
               'ru': 'Обнаружены бедуинскими пастухами в глиняных кувшинах в пещерах Кумрана в 1947 году; содержат '
                     'древнейшие библейские манускрипты на иврите и арамейском.',
               'en': 'Discovered in 1947 in jars within Judean Desert caves, these ancient Jewish manuscripts include '
                     'the oldest known surviving copies of biblical texts.'},
  'aliases': ["o'lik dengiz qo'lyozmalari",
              "qumron qo'lyozmalari",
              'свитки мёртвого моря',
              'кумранские рукописи',
              'dead sea scrolls',
              'qumran']},
 {'id': 'hist_art_009',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Agamemnonning oltin niqobi',
                     'Tutanxamon oltin niqobi',
                     'Shilman oltin gulchambari',
                     'Trebenishte oltin niqobi'],
              'ru': ['Золотая погребальная маска Агамемнона',
                     'Маска Тутанхамона',
                     'Золотая диадема Шлимана',
                     'Золотая маска из Требениште'],
              'en': ['Mask of Agamemnon', 'Mask of Tutankhamun', "Schliemann's Diadem", 'Trebenishte Gold Mask']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Agamemnonning oltin niqobi',
                     'ru': 'Золотая погребальная маска Агамемнона',
                     'en': 'Mask of Agamemnon'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c2/MaskAgamemnon.jpg',
  'fun_fact': {'uz': "Genrix Shliman 1876 yilda Mikenada qazishma o'tkazib uni Gomer dostonidagi shoh Agamemnonga "
                     "tegishli deb e'lon qilgan, ammo niqob aslida Troya urushidan 300 yil avvalroqqa tegishli.",
               'ru': 'Найдена Генрихом Шлиманом в Микенах в 1876 году. Хотя Шлиман приписал её герою «Илиады», маска '
                     'датируется XVI веком до н.э. — на 300 лет старше Троянской войны.',
               'en': "Unearthed at Mycenae by Heinrich Schliemann in 1876; although attributed to Homer's King "
                     'Agamemnon, it predates the Trojan War by three centuries.'},
  'aliases': ['agamemnon niqobi', 'agamemnon', 'маска агамемнона', 'mask of agamemnon', 'agamemnon mask']},
 {'id': 'hist_art_010',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Lessel Venerasi', 'Villendorf Venerasi', 'Brasempuy xonimi', 'Xoxle-Fels Venerasi'],
              'ru': ['Венера Лоссельская', 'Венера Виллендорфская', 'Венера Брассемпуйская', 'Венера из Холе-Фельс'],
              'en': ['Venus of Laussel', 'Venus of Willendorf', 'Venus of Brassempouy', 'Venus of Hohle Fels']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Villendorf Venerasi', 'ru': 'Венера Виллендорфская', 'en': 'Venus of Willendorf'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/50/Venus_of_Willendorf_frontview.jpg',
  'fun_fact': {'uz': "Avstriyadagi Villendorf qishlog'idan topilgan, bo'yi bor-yo'g'i 11 sm bo'lgan bu ohaktosh "
                     "haykalcha miloddan avvalgi 25 000 yillarga, ya'ni paleolit davriga tegishli.",
               'ru': 'Статуэтка из известняка высотой 11 см, найденная в Австрии, была высечена около 25 000 лет назад '
                     'и олицетворяет палеолитический культ плодородия.',
               'en': 'Discovered in Austria in 1908, this 11-cm limestone figurine dates to roughly 25,000 BC, '
                     'representing Paleolithic fertility symbolism.'},
  'aliases': ['villendorf venerasi', 'villendorf', 'венера виллендорфская', 'venus of willendorf']},
 {'id': 'hist_art_011',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Kserks barcha xalqlar darvozasi',
                     'Arslonlar darvozasi (Mikena)',
                     'Bobil Ishtar darvozasi',
                     'Milet bozor darvozasi'],
              'ru': ['Ворота всех наций',
                     'Львиные ворота в Микенах',
                     'Ворота Иштар в Вавилоне',
                     'Рыночные ворота Милета'],
              'en': ['Gate of All Nations',
                     'Lion Gate of Mycenae',
                     'Ishtar Gate of Babylon',
                     'Market Gate of Miletus']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Bobil Ishtar darvozasi', 'ru': 'Ворота Иштар в Вавилоне', 'en': 'Ishtar Gate of Babylon'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Ishtar_Gate_at_Berlin_Museum.jpg',
  'fun_fact': {'uz': 'Shoh Navuxodonosor II davrida (mil. avv. 575 y.) sirlangan moviy koshinlar, ajdaho (mushxushshu) '
                     'va yovvoyi buqalar tasviri bilan bezatilgan Bobilning asosiy darvozasi hozir Berlindagi Pergamon '
                     'muzeyida qayta tiklangan.',
               'ru': 'Возведены в 575 году до н.э. царём Навуходоносором II из глазурованного синего кирпича с '
                     'барельефами драконов-сиррушей и быков.',
               'en': 'Constructed in 575 BC by Nebuchadnezzar II using vibrant blue glazed bricks and bas-relief '
                     "dragons (mušḫuššu); reconstructed in Berlin's Pergamon Museum."},
  'aliases': ['ishtar darvozasi', 'ishtar', 'bobil darvozasi', 'ворота иштар', 'вавилон', 'ishtar gate', 'babylon']},
 {'id': 'hist_art_012',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Qirg'iylar stelasi", "Naram-Sin g'alaba stelasi", 'Gudea haykali', "Ur bayrog'i (Ur standarti)"],
              'ru': ['Стела коршунов', 'Стела царя Нарам-Сина', 'Статуя Гудеа', 'Штандарт войны и мира из Ура'],
              'en': ['Stele of the Vultures', 'Victory Stele of Naram-Sin', 'Statue of Gudea', 'Standard of Ur']},
  'correct_index': 3,
  'correct_answer': {'uz': "Ur bayrog'i (Ur standarti)", 'ru': 'Штандарт войны и мира из Ура', 'en': 'Standard of Ur'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Standard_of_ur.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 2600 yillarga oid Shumerning Ur shohona qabrlaridan topilgan ushbu yog'och quti "
                     "mozaikasida 'Urush' va 'Tinchlik' sahnalari sadaf, qizil ohaktosh va lazurit bilan ishlangan.",
               'ru': 'Шумерский артефакт XXVI века до н.э. из лазурита, перламутра и красного известняка, изображающий '
                     'сцены «Войны» с одной стороны и «Мира» с другой.',
               'en': 'Dating to 2600 BC, this hollow wooden box from Sumer features elaborate shell and lapis lazuli '
                     "mosaics depicting scenes of 'War' and 'Peace'."},
  'aliases': ['ur standarti', "ur bayrog'i", 'штандарт ура', 'standard of ur', 'ur']},
 {'id': 'hist_art_013',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Narmer paletkasi', "Jebil al-Aroq pichog'i", 'Ovchilar paletkasi', 'Bultuq stelasi'],
              'ru': ['Палетка фараона Нармера',
                     'Нож из Гебель эль-Арака',
                     'Палетка охотников',
                     'Стела царя Змея (Джета)'],
              'en': ['Narmer Palette', 'Gebel el-Arak Knife', 'Hunters Palette', 'Stele of Djet']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Narmer paletkasi', 'ru': 'Палетка фараона Нармера', 'en': 'Narmer Palette'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/eb/NarmerPalette_ROM.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 3100 yillarga oid ushbu tosh lavha Yuqori va Quyi Misrning birlashtirilishi '
                     "hamda fir'avn Narmer (Menes)ning g'alabasini aks ettirgan eng qadimgi tarixiy hujjatdir.",
               'ru': 'Древнейший исторический документ Египта (ок. 3100 до н.э.), символизирующий объединение Верхнего '
                     'и Нижнего царств фараоном Нармером.',
               'en': 'Carved siltstone plate from c. 3100 BC documenting the unification of Upper and Lower Egypt '
                     'under King Narmer, wearing both historic crowns.'},
  'aliases': ['narmer paletkasi', 'narmer', 'палетка нармера', 'narmer palette']},
 {'id': 'hist_art_014',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Vendal dubulg'asi",
                     "Satton-Xu dafn dubulg'asi",
                     "Koppengeyt dubulg'asi",
                     "Benti-Grange dubulg'asi"],
              'ru': ['Вендельский шлем',
                     'Шлем из кургана Саттон-Ху',
                     'Шлем из Коппергейта (Йорк)',
                     'Шлем из Бенти-Грейндж'],
              'en': ['Vendel Helmet', 'Sutton Hoo Helmet', 'Coppergate Helmet', 'Benty Grange Helmet']},
  'correct_index': 1,
  'correct_answer': {'uz': "Satton-Xu dafn dubulg'asi", 'ru': 'Шлем из кургана Саттон-Ху', 'en': 'Sutton Hoo Helmet'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/03/Sutton_Hoo_helmet_2012.jpg',
  'fun_fact': {'uz': '1939 yilda Angliyaning Suffolk grafligidagi anglo-sakson kemasi qabridan topilgan VII asrga oid '
                     "temir va bronza dubulg'a yuz qismidagi ajdaho va qanotlar tasviri bilan mashhur.",
               'ru': 'Англосаксонский шлем начала VII века из погребального корабля в Суффолке. Маска шлема образует '
                     'фигуру летящего дракона.',
               'en': 'Unearthed in 1939 from an Anglo-Saxon ship burial in Suffolk, this 7th-century crested helmet '
                     'features a face mask in the shape of a flying dragon.'},
  'aliases': ["satton xu dubulg'asi", 'satton xu', 'шлем саттон-ху', 'саттон-ху', 'sutton hoo helmet', 'sutton hoo']},
 {'id': 'hist_art_015',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Karl Buyuk shaxmati',
                     'San-Jeneviev shaxmati',
                     'Lyuis oroli shaxmat donalari',
                     'Nisapur shaxmat donalari'],
              'ru': ['Шахматы Карла Великого',
                     'Шахматы Сен-Женевьев',
                     'Шахматные фигуры с острова Льюис',
                     'Нишапурские шахматы'],
              'en': ['Charlemagne Chessmen', 'Sainte-Genevieve Chessmen', 'Lewis Chessmen', 'Nishapur Chessmen']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Lyuis oroli shaxmat donalari',
                     'ru': 'Шахматные фигуры с острова Льюис',
                     'en': 'Lewis Chessmen'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Lewis_chessmen_collection.jpg',
  'fun_fact': {'uz': "XII asr oxirida morj tishi va kit suyagidan Norvegiyada o'yib yasalgan ushbu 78 ta shaxmat "
                     'donasi 1831 yilda Shotlandiyaning Lyuis orolidagi qumtepalardan topilgan.',
               'ru': 'Изготовлены в Норвегии в конце XII века из моржового клыка и зубов кита; найдены на шотландском '
                     'острове Льюис в 1831 году.',
               'en': "Carved in Norway around 1150-1200 AD from walrus ivory and whales' teeth, discovered in 1831 on "
                     'the Isle of Lewis in Scotland.'},
  'aliases': ['lyuis shaxmati', 'lyuis donalari', 'шахматы льюис', 'остров льюис', 'lewis chessmen', 'isle of lewis']},
 {'id': 'hist_art_016',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Kleopatra byusti', 'Xatshepsut haykali', 'Tiye byusti', 'Nefertiti byusti'],
              'ru': ['Бюст Клеопатры', 'Статуя Хатшепсут', 'Головка царицы Тии', 'Бюст царицы Нефертити'],
              'en': ['Bust of Cleopatra', 'Statue of Hatshepsut', 'Head of Queen Tiye', 'Bust of Nefertiti']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Nefertiti byusti', 'ru': 'Бюст царицы Нефертити', 'en': 'Bust of Nefertiti'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/1f/Nofretete_Neues_Museum.jpg',
  'fun_fact': {'uz': "Haykaltarosh Tutmos tomonidan mil. avv. 1345 yilda ohaktosh va ganchdan ishlangan fir'avn "
                     'Exnaton rafiqasi Nefertitining bu byusti Berlindagi Yangi muzeyda saqlanadi.',
               'ru': 'Создан в 1345 году до н.э. придворным скульптором Тутмосом в Амарне; одно из самых копируемых '
                     'произведений искусства Древнего Египта.',
               'en': 'Crafted in 1345 BC by sculptor Thutmose in Amarna, this painted stucco-coated limestone bust of '
                     "Pharaoh Akhenaten's Great Royal Wife resides in Berlin."},
  'aliases': ['nefertiti byusti', 'nefertiti', 'бюст нефертити', 'нефертити', 'bust of nefertiti', 'nefertiti bust']},
 {'id': 'hist_art_017',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Fest diski (Krit)', "Krit chig'anoq muhri", 'Nebra osmon diski', 'Piskokefalo plitasi'],
              'ru': ['Фестский диск (Крит)',
                     'Критская цилиндрическая печать',
                     'Небесный диск из Небры',
                     'Табличка из Пискокефало'],
              'en': ['Phaistos Disc (Crete)', 'Minoan Seal Stone', 'Nebra Sky Disc', 'Piskokephalo Tablet']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Fest diski (Krit)', 'ru': 'Фестский диск (Крит)', 'en': 'Phaistos Disc (Crete)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/07/Phaistos_Disc_Side_A.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi II ming yillikka oid pishirilgan gil diskda spiral bo'ylab muhrlangan 241 ta "
                     "noma'lum belgi bo'lib, uning yozuvi hanuz to'liq shifrlanmagan.",
               'ru': 'Терракотовый диск минойской эпохи (ок. 1700 до н.э.) со спиральной надписью из штампованных '
                     'иероглифических знаков, не расшифрован по сей день.',
               'en': 'Discovered at the Minoan palace of Phaistos in Crete, this fired clay disc features 241 stamped '
                     'hieroglyphic symbols spiraling toward the center.'},
  'aliases': ['fest diski', 'фестский диск', 'phaistos disc', 'phaistos']},
 {'id': 'hist_art_018',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Rampurva buqa kapiteli',
                     'Ashokaning Arslon kapiteli (Sarnatx)',
                     'Sanchi darvozasi arslonlari',
                     'Lauriya-Nandangarh ustuni'],
              'ru': ['Капитель быка из Рампурвы',
                     'Львиная капитель Ашоки в Сарнатхе',
                     'Львы ворот Санчи',
                     'Колонна Лаурия-Нандангарх'],
              'en': ['Bull Capital of Rampurva',
                     'Lion Capital of Ashoka (Sarnath)',
                     'Lions of Sanchi Gate',
                     'Lauriya Nandangarh Capital']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Ashokaning Arslon kapiteli (Sarnatx)',
                     'ru': 'Львиная капитель Ашоки в Сарнатхе',
                     'en': 'Lion Capital of Ashoka (Sarnath)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Sarnath_Lion_Capital_of_Ashoka.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 250 yilda Budda ilk bor va'z aytgan joy — Sarnatxda imperator Ashoka tomonidan "
                     "o'rnatilgan ushbu 4 arslonli haykal bugungi kunda Hindistonning milliy gerbi hisoblanadi.",
               'ru': 'Высечена из песчаника около 250 года до н.э. при императоре Ашоке; четыре льва спиной к спине '
                     'стали государственным гербом Республики Индия.',
               'en': "Carved around 250 BC under Mauryan Emperor Ashoka at the site of Buddha's first sermon; its four "
                     'back-to-back Asiatic lions serve as the National Emblem of India.'},
  'aliases': ['ashoka kapiteli',
              'arslon kapiteli',
              'львиная капитель ашоки',
              'lion capital of ashoka',
              'ashoka pillar']},
 {'id': 'hist_art_019',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Yunus va kit gobeleni',
                     'Klod de Melen gilami',
                     'Bayyo gobeleni (Bayyo gilami)',
                     'Gildesxaym matosi'],
              'ru': ['Шпалера из Апокалипсиса в Анже',
                     'Шпалера «Дама с единорогом»',
                     'Гобелен (ковёр) из Байё',
                     'Хильдесхаймский ковёр'],
              'en': ['Apocalypse Tapestry of Angers',
                     'The Lady and the Unicorn Tapestry',
                     'Bayeux Tapestry',
                     'Hildesheim Carpet']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Bayyo gobeleni (Bayyo gilami)', 'ru': 'Гобелен (ковёр) из Байё', 'en': 'Bayeux Tapestry'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/69/Odo_bayeux_tapestry.png',
  'fun_fact': {'uz': "Uzunligi qariyb 70 metr bo'lgan ushbu XI asr kashtado'zlik asarida 1066 yildagi Vilgelm "
                     'Fotihning Angliyani zabt etishi va Gastings jangi batafsil tasvirlangan.',
               'ru': 'Вышитое полотно длиной почти 70 метров, созданное в конце XI века, иллюстрирует нормандское '
                     'завоевание Англии и битву при Гастингсе 1066 года.',
               'en': 'Nearly 70 meters long, this 11th-century embroidered linen cloth vividly depicts events leading '
                     'up to the Norman Conquest of England and the Battle of Hastings in 1066.'},
  'aliases': ['bayyo gobeleni', 'bayyo gilami', 'гобелен из байё', 'ковёр из байё', 'bayeux tapestry', 'bayeux']},
 {'id': 'hist_art_020',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Fuchai nayzasi', 'Qin imperatori qilichi', 'Chanoqlik qilich', 'Goujian qilichi (Xitoy)'],
              'ru': ['Копьё Фучая', 'Меч первого императора Цинь', 'Клинок Чжао', 'Меч Гоуцзяня (древний Китай)'],
              'en': ['Spear of Fuchai', 'Sword of Qin Shi Huang', 'Blade of Zhao', 'Sword of Goujian (Ancient China)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Goujian qilichi (Xitoy)',
                     'ru': 'Меч Гоуцзяня (древний Китай)',
                     'en': 'Sword of Goujian (Ancient China)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/63/Sword_of_Goujian_2011_02.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi V asrga oid ushbu bronza qilich 1965 yilda nam qabrdan topilganida 2500 yil '
                     "o'tganiga qaramay birorta ham zang dog'i bo'lmagan va qog'ozni osonlikcha kesgan.",
               'ru': 'Бронзовый меч V века до н.э. правителя царства Юэ. Пролежав более двух тысячелетий в сырой '
                     'гробнице, клинок не покрылся ржавчиной и сохранил бритвенную остроту.',
               'en': 'Cast in the 5th century BC with high tin content and chrome-plated rust resistance, this Yue '
                     'King sword was found unscratched and razor-sharp after 2,500 years.'},
  'aliases': ['goujian qilichi', 'меч гоуцзяня', 'гоуцзянь', 'sword of goujian', 'goujian']},
 {'id': 'hist_art_021',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Trundxolm quyosh aravachasi (Daniya)',
                     'Oxus oltin aravachasi',
                     'Strettveg qurbonlik aravasi',
                     'Dejbiyerg aravasi'],
              'ru': ['Солнечная повозка из Трундхольма',
                     'Колесница из Амударьинского клада',
                     'Культовая повозка из Штреттвега',
                     'Повозка из Дейбьерга'],
              'en': ['Trundholm Sun Chariot (Denmark)', 'Oxus Gold Chariot', 'Strettweg Cult Wagon', 'Dejbjerg Wagon']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Trundxolm quyosh aravachasi (Daniya)',
                     'ru': 'Солнечная повозка из Трундхольма',
                     'en': 'Trundholm Sun Chariot (Denmark)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Solvognen-cropped.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 1400 yillarga oid bronza va zarhal quyosh diskini tortib borayotgan ot haykali '
                     'Shimoliy Yevropa bronza davri mifologiyasining eng nodir yodgorligidir.',
               'ru': 'Бронзовая фигура лошади, везущей позолоченный солнечный диск на колёсах (ок. 1400 г. до н.э.), '
                     'отражает верования скандинавов бронзового века.',
               'en': 'Dating to c. 1400 BC, this bronze and gilded horse drawing a sun disc demonstrates Nordic Bronze '
                     'Age solar worship beliefs.'},
  'aliases': ['trundxolm aravachasi',
              'quyosh aravachasi',
              'солнечная повозка',
              'трундхольм',
              'trundholm sun chariot',
              'trundholm']},
 {'id': 'hist_art_022',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Shilikti oltin kiyimi',
                     "Issiq 'Oltin odami' (Sak jangchisi libosi)",
                     'Arjon oltin skifi',
                     'Paziriq chavandozi'],
              'ru': ['Шиликтинский золотой человек',
                     '«Золотой человек» из кургана Иссык',
                     'Царь из кургана Аржан-2',
                     'Всадник из Пазырыка'],
              'en': ['Shilikti Golden Man',
                     'Golden Warrior of Issyk (Saka Golden Man)',
                     'Arzhan-2 Golden King',
                     'Pazyryk Horseman']},
  'correct_index': 1,
  'correct_answer': {'uz': "Issiq 'Oltin odami' (Sak jangchisi libosi)",
                     'ru': '«Золотой человек» из кургана Иссык',
                     'en': 'Golden Warrior of Issyk (Saka Golden Man)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b2/Altyn_Adam.jpg',
  'fun_fact': {'uz': "1969 yilda Qozog'istonning Issiq qo'rg'onidan topilgan mil. avv. V-IV asrlarga oid yosh sak "
                     'jangchisining 4000 dan ortiq nafis oltin bezaklar bilan qoplangan tantanali libosi.',
               'ru': 'Захоронение сакского воина IV–III вв. до н.э. в доспехах из более чем 4000 золотых пластин в '
                     'характерном скифо-сибирском зверином стиле.',
               'en': "Excavated in 1969 from a Saka kurgan in Kazakhstan, the 4th-century BC warrior's suit comprises "
                     'over 4,000 intricate animal-style gold plaques.'},
  'aliases': ['oltin odam', 'issiq oltin odami', 'золотой человек', 'иссык', 'golden warrior', 'issyk golden man']},
 {'id': 'hist_art_023',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Tilla-tepa xazinasi',
                     "Mirzako'l xazinasi",
                     'Dalvarzintepa oltin xazinasi (Kushan davri)',
                     'Qoratepa oltin idishi'],
              'ru': ['Золото Тилля-тепе (Бактрийское золото)',
                     'Мирзакульский клад',
                     'Золотой клад Дальверзинтепа (Кушанское царство)',
                     'Сосуд из Каратепа'],
              'en': ['Tillya Tepe Gold',
                     'Mirzakul Hoard',
                     'Dalverzintepa Gold Hoard (Kushan Empire)',
                     'Kara Tepe Vessel']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Dalvarzintepa oltin xazinasi (Kushan davri)',
                     'ru': 'Золотой клад Дальверзинтепа (Кушанское царство)',
                     'en': 'Dalverzintepa Gold Hoard (Kushan Empire)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Dalverzin_Tepe_treasure.jpg',
  'fun_fact': {'uz': '1972 yilda Surxondaryo viloyatining Dalvarzintepa qadimiy shahar xarobalaridan topilgan 36 kg '
                     "sof oltindan iborat bu xazina Kushon imperiyasi zargarlik san'atining eng buyuk yodgorligidir.",
               'ru': 'Найден в 1972 году археологом Э. Ртвеладзе в Сурхандарье (Узбекистан); клад весом около 36 кг '
                     'чистого золота I века н.э. содержит уникальные кушанские слитки и украшения.',
               'en': 'Discovered in 1972 at Dalverzin Tepe in Surkhandarya, Uzbekistan; weighing ~36 kg of pure gold, '
                     'it is the largest ancient gold hoard found in Central Asia.'},
  'aliases': ['dalvarzintepa',
              'dalvarzintepa oltin xazinasi',
              'дальверзинтепа',
              'dalverzin tepe',
              'dalverzintepa gold']},
 {'id': 'hist_art_024',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Afrosiyob elchilar zali',
                     'Panjikent devoriy rasmlari',
                     "Tuproqqal'a zali suratlari",
                     'Varaxsha saroyi devoriy suratlari (Fil ustida qoplonlar bilan jang)'],
              'ru': ['Зал послов в Афрасиабе',
                     'Пенджикентские росписи',
                     'Росписи Топрак-калы',
                     'Фрески дворца Варахша (Битва со зверями на слонах)'],
              'en': ['Afrasiab Ambassador Hall',
                     'Panjakent Murals',
                     'Toprak-Kala Wall Paintings',
                     'Varakhsha Palace Murals (Elephant and Leopard Hunt)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Varaxsha saroyi devoriy suratlari (Fil ustida qoplonlar bilan jang)',
                     'ru': 'Фрески дворца Варахша (Битва со зверями на слонах)',
                     'en': 'Varakhsha Palace Murals (Elephant and Leopard Hunt)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/14/Varakhsha_fresco.jpg',
  'fun_fact': {'uz': "Buxoro vohasidagi Buxorxudotlar qarorgohi bo'lgan Varaxsha saroyidan (VII-VIII asrlar) topilgan "
                     "qizil fondagi mashhur suratda oq fil ustida o'tirib qoplonlar va yirtqichlarga qarshi jang "
                     'qilayotgan shohona qahramon tasvirlangan.',
               'ru': 'Шедевр согдийского искусства VII–VIII вв. из резиденции бухархудатов Варахша: охота на леопардов '
                     'и фантастических хищников верхом на белых боевых слонах.',
               'en': '7th-8th century Sogdian masterwork from the Varakhsha residence near Bukhara, showing heroes '
                     'mounted on painted war elephants spearing leopards against a red backdrop.'},
  'aliases': ['varaxsha', 'varaxsha suratlari', 'варахша', 'фрески варахши', 'varakhsha murals']},
 {'id': 'hist_art_025',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Afrosiyob elchilar zali devoriy suratlari (Samarqand)',
                     'Balaliqtepa devoriy suratlari',
                     'Varaxsha devoriy suratlari',
                     'Qoratepa budda freskalari'],
              'ru': ['Настенные росписи Зала послов в Афрасиабе (Самарканд)',
                     'Росписи Балалык-тепе',
                     'Росписи Варахши',
                     'Буддийские фрески Каратепа'],
              'en': ['Afrasiab Murals of the Ambassadors (Samarkand)',
                     'Balalyk Tepe Paintings',
                     'Varakhsha Wall Paintings',
                     'Kara Tepe Murals']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Afrosiyob elchilar zali devoriy suratlari (Samarqand)',
                     'ru': 'Настенные росписи Зала послов в Афрасиабе (Самарканд)',
                     'en': 'Afrasiab Murals of the Ambassadors (Samarkand)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Afrasiab_mural_-_Korean_ambassadors.jpg',
  'fun_fact': {'uz': "Samarqand hukmdori Varxuman (VII asr o'rtalari) saroyidan topilgan ushbu so'g'd devoriy "
                     "suratlarida Xitoy, Koreya (Koguryo), Chag'oniyon va Tibetdan kelgan elchilar delegatsiyalari "
                     'tasvirlangan.',
               'ru': 'Росписи середины VII века во дворце царя Вархумана на городище Афрасиаб запечатлели послов из '
                     'Китая, Кореи (Когурё), Чаганиана и Тибета на празднике Навруз.',
               'en': "Mid-7th century Sogdian royal murals from King Varkhuman's palace at Afrasiab, showing "
                     'diplomatic missions from Tang China, Korea (Goguryeo), Chaganian, and Tibet.'},
  'aliases': ['afrosiyob suratlari',
              'afrosiyob elchilar zali',
              'афрасиаб',
              'росписи афрасиаба',
              'afrasiab murals',
              'afrasiyab']},
 {'id': 'hist_art_026',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Senet taxtasi (Qadimgi Misr)',
                     "Ur shohona o'yini taxtasi (Qadimgi Shumer)",
                     "Mehen ilon o'yini",
                     "Ellik sakkiz katak o'yini"],
              'ru': ['Египетский сенет',
                     'Царская игра Ура (древнейшая настольная игра)',
                     'Игра мехен',
                     'Игра «Пятьдесят восемь дырочек»'],
              'en': ['Senet (Ancient Egypt)',
                     'Royal Game of Ur (Ancient Sumerian Board Game)',
                     'Mehen Snake Game',
                     'Hounds and Jackals']},
  'correct_index': 1,
  'correct_answer': {'uz': "Ur shohona o'yini taxtasi (Qadimgi Shumer)",
                     'ru': 'Царская игра Ура (древнейшая настольная игра)',
                     'en': 'Royal Game of Ur (Ancient Sumerian Board Game)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Royal_Game_of_Ur%2C_British_Museum.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 2600 yillarga oid Shumerning Ur shahridan topilgan sadaf, lazurit va qizil '
                     "ohaktoshdan yasalgan bu taxta insoniyat tarixidagi eng qadimiy stol o'yinlaridan biridir.",
               'ru': 'Шумерская настольная игра для двух игроков возрастом более 4500 лет; правила игры удалось '
                     'реконструировать по клинописной табличке вавилонского астронома.',
               'en': 'Dating to roughly 2600 BC from the Royal Cemetery at Ur, its original rules were deciphered from '
                     'a 2nd-century BC cuneiform clay tablet by Irving Finkel.'},
  'aliases': ["ur o'yini", "ur shohona o'yini", 'царская игра ура', 'игра ура', 'royal game of ur', 'game of ur']},
 {'id': 'hist_art_027',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Lindisfarn Injili',
                     'Darrou kitobi',
                     'Kells kitobi (Kells Injili)',
                     'Giyas kodeksi (Iblis Injili)'],
              'ru': ['Евангелие из Линдисфарна',
                     'Книга из Дарроу',
                     'Келлская книга (Книга Колумбы)',
                     'Гигантский кодекс'],
              'en': ['Lindisfarne Gospels', 'Book of Durrow', 'Book of Kells (Gospel Book)', 'Codex Gigas']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Kells kitobi (Kells Injili)',
                     'ru': 'Келлская книга (Книга Колумбы)',
                     'en': 'Book of Kells (Gospel Book)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ea/KellsFol032vChristEnthroned.jpg',
  'fun_fact': {'uz': 'Taxminan 800 yilda Shotlandiya va Irlandiya rohiblari tomonidan yaratilgan nafis kelt '
                     "illyustratsiyalari va bosh harflari bilan bezatilgan to'rt Injil qo'lyozmasi Dublin Triniti "
                     'kollejida saqlanadi.',
               'ru': 'Иллюминированная рукопись четырёх Евангелий около 800 года; непревзойдённая вершина кельтского '
                     'монастырского миниатюрного искусства.',
               'en': 'Created around 800 AD by Celtic monks, this lavishly illuminated manuscript of the four Gospels '
                     "is Ireland's greatest national cultural treasure at Trinity College Dublin."},
  'aliases': ['kells kitobi', 'kells', 'келлская книга', 'book of kells']},
 {'id': 'hist_art_028',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Fest diski',
                     'Trundxolm quyosh diski',
                     'Kolbaquyosh oltin diski',
                     'Nebra osmon diski (Bronza davri)'],
              'ru': ['Фестский диск', 'Диск из Трундхольма', 'Золотой диск из Брухофера', 'Небесный диск из Небры'],
              'en': ['Phaistos Disc', 'Trundholm Disc', 'Banc Tynddol Sun-disc', 'Nebra Sky Disc']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Nebra osmon diski (Bronza davri)', 'ru': 'Небесный диск из Небры', 'en': 'Nebra Sky Disc'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Nebra_Scheibe.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 1600 yillarga oid Germaniyaning Nebra shahri yaqinidan topilgan bronza va '
                     "oltindan yasalgan bu disk insoniyat tarixidagi osmon va yulduzlar (Pleyada to'dasi)ning eng "
                     'qadimgi aniq tasviridir.',
               'ru': 'Бронзовый диск диаметром 30 см с золотыми аппликациями Солнца, Луны и созвездия Плеяд (ок. 1600 '
                     'г. до н.э.) — старейшее астрономическое изображение небосвода.',
               'en': 'Dating to c. 1600 BC, this 30 cm bronze disc with gold inlays of the Sun, Crescent Moon, and the '
                     'Pleiades cluster is the oldest known concrete depiction of cosmic phenomena.'},
  'aliases': ['nebra diski',
              'nebra osmon diski',
              'диск из небры',
              'небесный диск из небры',
              'nebra sky disc',
              'nebra disc']},
 {'id': 'hist_art_029',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Parfenon marmarlari (Elgin marmarlari)',
                     'Pergamon mehrobi frizlari',
                     'Galikarnas maqbarasi relyeflari',
                     'Bassae ibodatxonasi frizi'],
              'ru': ['Мраморы Парфенона (Мраморы Элгина)',
                     'Фриз Пергамского алтаря',
                     'Рельефы Галикарнасского мавзолея',
                     'Фриз храма Аполлона в Бассах'],
              'en': ['Parthenon Marbles (Elgin Marbles)',
                     'Pergamon Altar Frieze',
                     'Mausoleum at Halicarnassus Reliefs',
                     'Bassae Frieze']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Parfenon marmarlari (Elgin marmarlari)',
                     'ru': 'Мраморы Парфенона (Мраморы Элгина)',
                     'en': 'Parthenon Marbles (Elgin Marbles)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Parthenon_sculptures_at_the_British_Museum.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi V asrda haykaltarosh Fidiy rahbarligida Afina Akropolida yaratilgan ushbu '
                     'haykaltaroshlik kompozitsiyalari XIX asr boshida lord Elgin tomonidan Londonga olib ketilgan va '
                     'Britaniya muzeyida saqlanadi.',
               'ru': 'Коллекция древнегреческих статуй и метоп V века до н.э., созданных под руководством Фидия для '
                     'Парфенона и вывезенных лордом Элгином в Лондон.',
               'en': 'Classical Greek marble sculptures crafted under the supervision of Phidias around 440 BC for the '
                     'Parthenon; removed by Lord Elgin and displayed in the British Museum.'},
  'aliases': ['parfenon marmarlari',
              'elgin marmarlari',
              'мраморы парфенона',
              'мраморы элгина',
              'parthenon marbles',
              'elgin marbles']},
 {'id': 'hist_art_030',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Likurg qadahi', 'Portlend shisha vazasi (Kameya shishasi)', 'Uorren kubogi', 'Marten vazasi'],
              'ru': ['Кубок Ликурга',
                     'Портлендская ваза (двухслойное римское стекло)',
                     'Кубок Уоррена',
                     'Ваза из Мартена'],
              'en': ['Lycurgus Cup', 'Portland Vase (Roman Cameo Glass)', 'Warren Cup', 'Vase of Saint Martin']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Portlend shisha vazasi (Kameya shishasi)',
                     'ru': 'Портлендская ваза (двухслойное римское стекло)',
                     'en': 'Portland Vase (Roman Cameo Glass)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Portland_Vase_BM_Gem4036_n2.jpg',
  'fun_fact': {'uz': "Milodiy I asr boshlariga oid to'q ko'k rangli shisha ustiga oq rangli shisha qatlami tushirilib "
                     "o'yib ishlangan (kameya uslubida) ushbu Rim vazasi shishasozlik san'atining cho'qqisi "
                     'hisoblanadi.',
               'ru': 'Римский сосуд I века н.э. из двухслойного тёмно-синего и белого стекла с рельефными '
                     'мифологическими фигурами; выдающийся образец техники камеи.',
               'en': 'Roman cameo glass vessel dating to AD 1-25; created with violet-blue glass overlaid with carved '
                     'white cameo glass depicting Peleus and Thetis.'},
  'aliases': ['portlend vazasi', 'портлендская ваза', 'portland vase']},
 {'id': 'hist_art_031',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Toltek jangchisi (Atlant)',
                     'Chak-Mool haykali',
                     'Olmeklarning ulkan bazalt tosh boshi',
                     'Paskal tosh niqobi'],
              'ru': ['Атлант из Тулы (тольтеки)',
                     'Скульптура Чак-Мооль',
                     'Колоссальная каменная голова ольмеков',
                     'Нефритовая маска Пакаля'],
              'en': ['Toltec Atlantean Figure', 'Chacmool Sculpture', 'Olmec Colossal Head', 'Jade Mask of Pakal']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Olmeklarning ulkan bazalt tosh boshi',
                     'ru': 'Колоссальная каменная голова ольмеков',
                     'en': 'Olmec Colossal Head'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Olmec_Head_No._1_from_San_Lorenzo.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 1200-900 yillarda qadimgi Meksika o'rmonlarida yashagan olmeklar og'irligi 20 "
                     "tonnagacha keladigan ulkan bazalt xarsanglardan hukmdorlarining dubulg'ali portretlarini yo'nib "
                     'yasaganlar.',
               'ru': 'Высечены из базальтовых валунов цивилизацией ольмеков около 1200–900 гг. до н.э. Каждая голова '
                     'уникальна и изображает могущественного вождя в боевом шлеме.',
               'en': 'Carved from giant basalt boulders between 1200-900 BC in Mesoamerica; each monumental head '
                     'weighs up to 28 tons and portrays an individual Olmec ruler.'},
  'aliases': ['olmek boshi', 'olmek tosh boshi', 'голова ольмеков', 'ольмеки', 'olmec colossal head', 'olmec head']},
 {'id': 'hist_art_032',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Tizok toshi',
                     'Koatlikue haykali',
                     'Koyolshauki tosh diski',
                     'Atstek quyosh toshi (Piedra del Sol)'],
              'ru': ['Камень Тисока',
                     'Монолит Коатликуэ',
                     'Монолит Койольшауки',
                     'Камень Солнца ацтеков (Календарный камень)'],
              'en': ['Stone of Tizoc', 'Coatlicue Statue', 'Coyolxauhqui Stone', 'Aztec Sun Stone (Piedra del Sol)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Atstek quyosh toshi (Piedra del Sol)',
                     'ru': 'Камень Солнца ацтеков (Календарный камень)',
                     'en': 'Aztec Sun Stone (Piedra del Sol)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/23/Monolito_de_la_Piedra_del_Sol.jpg',
  'fun_fact': {'uz': "Og'irligi 24 tonna, diametri 3,6 metr bo'lgan ushbu bazalt monolit 1790 yilda Mexiko shahrida "
                     "topilgan bo'lib, atsteklarning to'rt olam davri va quyosh xudosi Tonatiux tasvirlangan.",
               'ru': 'Базальтовый монолит весом 24 тонны, созданный около 1500 года; отражает космогонию ацтеков с '
                     'четырьмя эпохами творения вокруг бога солнца Тонатиу.',
               'en': "Discovered under Mexico City's central plaza in 1790, this 24-ton basalt monolith represents "
                     'Aztec cosmogony and the creation ages surrounding sun god Tonatiuh.'},
  'aliases': ['atstek quyosh toshi',
              'quyosh toshi',
              'камень солнца',
              'ацтекский календарь',
              'aztec sun stone',
              'piedra del sol']},
 {'id': 'hist_art_033',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Priam xazinasi (Troya oltinlari)', 'Mikena xazinasi', 'Egina xazinasi', 'Varna oltin nekropoli'],
              'ru': ['Клад Приама (Золото Трои)', 'Золото Микен', 'Эгинский клад', 'Варненский некрополь'],
              'en': ["Priam's Treasure (Gold of Troy)",
                     'Mycenaean Gold Hoard',
                     'Aegina Treasure',
                     'Varna Necropolis Gold']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Priam xazinasi (Troya oltinlari)',
                     'ru': 'Клад Приама (Золото Трои)',
                     'en': "Priam's Treasure (Gold of Troy)"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/05/Schliemanns_Frau_mit_Goldschmuck.jpg',
  'fun_fact': {'uz': '1873 yilda Genrix Shliman tomonidan Hisorlik tepaligida topilgan va Troya shohi Priamga tegishli '
                     "deb e'lon qilingan qadimiy oltin diademalar va taqinchoqlar aslida Troya urushidan 1000 yil "
                     'avvalroqqa tegishli.',
               'ru': 'Найден Генрихом Шлиманом в 1873 году на холме Гиссарлык; состоит из тысяч золотых подвесок и '
                     'диадем эпохи ранней бронзы (ок. 2400 до н.э.).',
               'en': 'Uncovered by Heinrich Schliemann at Hisarlik in 1873; the thousands of gold jewelry pieces date '
                     "to the Early Bronze Age (c. 2400 BC), a millennium before Homer's Troy."},
  'aliases': ['priam xazinasi', 'troya oltinlari', 'клад приама', 'золото трои', "priam's treasure", 'gold of troy']},
 {'id': 'hist_art_034',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Buyuk Zimbabve qush haykalchasi',
                     'Mapungubve oltin karkidoni (Janubiy Afrika)',
                     'Benin bronza leopardi',
                     'Ife oltin toji'],
              'ru': ['Птица Зимбабве',
                     'Золотой носорог из Мапунгубве (Южная Африка)',
                     'Бенинский бронзовый леопард',
                     'Корона Ифе'],
              'en': ['Zimbabwe Bird',
                     'Golden Rhinoceros of Mapungubwe (South Africa)',
                     'Benin Bronze Leopard',
                     'Ife Crown']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Mapungubve oltin karkidoni (Janubiy Afrika)',
                     'ru': 'Золотой носорог из Мапунгубве (Южная Африка)',
                     'en': 'Golden Rhinoceros of Mapungubwe (South Africa)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ea/Golden_Rhinoceros_of_Mapungubwe.jpg',
  'fun_fact': {'uz': "XII asrga oid ushbu yog'och asosga yupqa zarhal oltin folga mixlab ishlangan haykalcha o'rta "
                     'asrlarda janubiy Afrikada rivojlangan qudratli qirollik mavjudligining ramzidir.',
               'ru': 'Изготовлен в XII–XIII вв. из тонких пластин золотой фольги на деревянной основе; национальный '
                     'символ древней африканской цивилизации Мапунгубве.',
               'en': 'Crafted around 1200 AD from hammered gold foil over carved wood, it symbolizes political power '
                     'and indigenous civilization in pre-colonial southern Africa.'},
  'aliases': ['mapungubve oltin karkidoni',
              'oltin karkidon',
              'золотой носорог',
              'мапунгубве',
              'golden rhinoceros of mapungubwe']},
 {'id': 'hist_art_035',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['In sulolasi yuzi',
                     'Chjou niqobi',
                     'Sansinduy ulkan bronza niqobi (Xitoy)',
                     'Dian bronza haykali'],
              'ru': ['Бронзовый сосуд династии Шан',
                     'Маска династии Чжоу',
                     'Гигантская бронзовая маска из Саньсиндуй (Китай)',
                     'Бронзовая фигура царства Диань'],
              'en': ['Shang Dynasty Bronze Vessel',
                     'Zhou Dynasty Mask',
                     'Sanxingdui Colossal Bronze Mask (China)',
                     'Dian Bronze Figure']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Sansinduy ulkan bronza niqobi (Xitoy)',
                     'ru': 'Гигантская бронзовая маска из Саньсиндуй (Китай)',
                     'en': 'Sanxingdui Colossal Bronze Mask (China)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/00/Sanxingdui_Mask.jpg',
  'fun_fact': {'uz': "Sichuan provinsiyasidan topilgan mil. avv. XII-XI asrlarga oid bo'rtib chiqqan ko'zlari va ulkan "
                     "quloqlari bo'lgan bu g'aroyib bronza niqob qadimgi Shu sivilizatsiyasining sirli marosim "
                     'buyumidir.',
               'ru': 'Бронзовая маска с гипертрофированными миндалевидными глазами и ушами возрастом более 3000 лет из '
                     'древнего царства Шу в Сычуани.',
               'en': 'Discovered in Sichuan, this 3,000-year-old bronze mask from the mysterious ancient Shu '
                     'civilization features protruding eyes and enormous flared ears.'},
  'aliases': ['sansinduy niqobi', 'sansinduy', 'маска саньсиндуй', 'саньсиндуй', 'sanxingdui mask', 'sanxingdui']},
 {'id': 'hist_art_036',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Hurriy madhiyasi lavhasi',
                     'Delfi Apollon madhiyasi',
                     'Mesomed lavhasi',
                     "Seykilos epitafiyasi (Eng qadimgi to'liq nota yozuvi)"],
              'ru': ['Хурритский гимн № 6',
                     'Дельфийский гимн Аполлону',
                     'Гимн Месомеда',
                     'Эпитафия Сейкила (древнейшая полная запись музыки)'],
              'en': ['Hurrian Hymn to Nikkal',
                     'Delphic Hymn to Apollo',
                     'Hymn of Mesomedes',
                     'Seikilos Epitaph (Oldest Complete Musical Composition)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Seykilos epitafiyasi (Eng qadimgi to'liq nota yozuvi)",
                     'ru': 'Эпитафия Сейкила (древнейшая полная запись музыки)',
                     'en': 'Seikilos Epitaph (Oldest Complete Musical Composition)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/d/d4/Seikilos_stele.jpg',
  'fun_fact': {'uz': "Milodiy I-II asrlarga oid marmar qabrtosh ustiga o'yib yozilgan qisqa qo'shiq va uning ustidagi "
                     "qadimgi yunon nota belgilari dunyoda to'liq saqlanib qolgan eng qadimgi kuy hisoblanadi.",
               'ru': 'Мраморная надгробная стела I–II вв. н.э. из Турции с текстом и древнегреческой буквенной '
                     'нотацией; древнейшее дошедшее до нас законченное музыкальное произведение.',
               'en': 'Carved on a marble tombstone from Hellenistic Asia Minor (1st-2nd century AD), this is the '
                     'oldest surviving complete musical composition, including lyrics and ancient Greek notation.'},
  'aliases': ['seykilos', 'seykilos epitafiyasi', 'эпитафия сейкила', 'seikilos epitaph', 'seikilos']},
 {'id': 'hist_art_037',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Behistun qoyatosh yozuvlari',
                     'Naqshi Rustam yozuvlari',
                     'Pasargada yozuvi',
                     'Ganjnoma yozuvlari'],
              'ru': ['Бехистунская наскальная надпись царя Дария I',
                     'Надписи Накше-Рустам',
                     'Надпись Кира в Пасаргадах',
                     'Ганджнаме'],
              'en': ['Behistun Inscription of Darius the Great',
                     'Naqsh-e Rostam Inscriptions',
                     'Pasargadae Inscription',
                     'Ganjnameh Inscription']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Behistun qoyatosh yozuvlari',
                     'ru': 'Бехистунская наскальная надпись царя Дария I',
                     'en': 'Behistun Inscription of Darius the Great'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Behistun_relief.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 520 yilda Eronning Kirmonshoh qoyasida Doro I buyrug'i bilan uch tilda (qadimgi "
                     "fors, elam va bobil) o'yilgan bu relyef mixxat yozuvini ochishda kalit vazifasini o'tagan.",
               'ru': 'Высечена на скале на высоте 100 метров на трёх языках клинописи; позволила Генри Роулинсону в '
                     '1835–1843 годах расшифровать клинописные системы Ближнего Востока.',
               'en': 'Carved high on a cliff in Iran around 520 BC in Old Persian, Elamite, and Babylonian cuneiform, '
                     'it enabled Henry Rawlinson to decipher ancient cuneiform.'},
  'aliases': ['behistun yozuvlari',
              'behistun',
              'бехистунская надпись',
              'бехистун',
              'behistun inscription',
              'behistun']},
 {'id': 'hist_art_038',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Gudea stelasi', "Qirg'iylar stelasi (Shumer)", "Naram-Sin g'alaba stelasi", 'Ur-Nanshe relyefi'],
              'ru': ['Стела Гудеа',
                     'Стела коршунов (правителя Лагаша Эанатума)',
                     'Стела победы царя Нарам-Сина',
                     'Рельеф Ур-Нанше'],
              'en': ['Stele of Gudea',
                     'Stele of the Vultures (Sumerian King Eannatum)',
                     'Victory Stele of Naram-Sin',
                     'Relief of Ur-Nanshe']},
  'correct_index': 1,
  'correct_answer': {'uz': "Qirg'iylar stelasi (Shumer)",
                     'ru': 'Стела коршунов (правителя Лагаша Эанатума)',
                     'en': 'Stele of the Vultures (Sumerian King Eannatum)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Stele_of_the_Vultures_detail_01a.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 2460 yillarga oid ohaktosh stela Lagash hukmdori Eanatumning Umma ustidan '
                     "g'alabasini aks ettiradi va tarixdagi ilk harbiy hujjatli tasvir sanaladi.",
               'ru': 'Шумерская стела сер. III тыс. до н.э. из Лагаша, изображающая фалангу щитоносцев с копьями и '
                     'коршунов, уносящих головы побеждённых врагов.',
               'en': 'Carved in Sumer around 2460 BC, this limestone stele depicts King Eannatum leading a tight '
                     'phalanx of shielded soldiers, with vultures carrying severed heads of enemies.'},
  'aliases': ["qirg'iylar stelasi", 'стела коршунов', 'stele of the vultures']},
 {'id': 'hist_art_039',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Basa xonimi', 'Ibiza xonimi', 'Elche xonimi (Dama de Elche, Ispaniya)', 'Kabrera Venerasi'],
              'ru': ['Дама из Басы',
                     'Дама из Ибицы',
                     'Дама из Эльче (иберская полихромная скульптура)',
                     'Венера из Кабреры'],
              'en': ['Lady of Baza', 'Lady of Ibiza', 'Lady of Elche (Dama de Elche, Spain)', 'Venus of Cabrera']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Elche xonimi (Dama de Elche, Ispaniya)',
                     'ru': 'Дама из Эльче (иберская полихромная скульптура)',
                     'en': 'Lady of Elche (Dama de Elche, Spain)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/64/Dama_de_Elche.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi IV asrga oid Ispaniyaning Elche shahridan topilgan ushbu iber ohaktosh binosida '
                     "quloqlari ustidagi ulkan g'ildiraksimon zargarlik bezaklari diqqatga sazovordir.",
               'ru': 'Иберский известняковый бюст IV века до н.э. со сложнейшим головным убором и колесовидными '
                     'височными украшениями; шедевр древнеиспанского искусства.',
               'en': 'Carved in the 4th century BC in southeastern Spain, this polychrome limestone bust showcases '
                     'elaborate Iberian headdresses with large coiled wheel ornaments.'},
  'aliases': ['elche xonimi', 'dama de elche', 'дама из эльче', 'lady of elche']},
 {'id': 'hist_art_040',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Portlend vazasi', 'Likurg qadahi', "Beruvild kumush ko'zasi", 'Uorren kumush qadahi (Rim davri)'],
              'ru': ['Портлендская ваза',
                     'Кубок Ликурга',
                     'Бертувильское серебро',
                     'Кубок Уоррена (римский серебряный кубок)'],
              'en': ['Portland Vase', 'Lycurgus Cup', 'Berthouville Treasure', 'Warren Cup (Roman Silver Cup)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Uorren kumush qadahi (Rim davri)',
                     'ru': 'Кубок Уоррена (римский серебряный кубок)',
                     'en': 'Warren Cup (Roman Silver Cup)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/07/Warren_Cup_side_A_BM_GR1999.4-26.1.jpg',
  'fun_fact': {'uz': 'Milodiy I asrga oid Quddus yaqinidan topilgan ushbu kumush sharob idishi Rim nozik '
                     "metallurgiyasi va san'atining yorqin namunasidir.",
               'ru': 'Серебряный кубок эпохи Юлиев-Клавдиев (I век н.э.) с чеканными фигурами в технике репуссе; '
                     'хранится в Британском музее.',
               'en': 'Dating to the Julio-Claudian era (1st century AD), this embossed silver drinking vessel is '
                     'famous for its intricate Classical Roman repoussé work.'},
  'aliases': ['uorren qadahi', 'uorren kubogi', 'кубок уоррена', 'warren cup']},
 {'id': 'hist_art_041',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Uluburun oltin skarabeyi (Nefertiti nomi bitilgan)',
                     'Tutanxamon oltin skarabeyi',
                     'Xatshepsut skarabeyi',
                     'Amenxotep III nikoh skarabeyi'],
              'ru': ['Золотой скарабей царицы Нефертити из кораблекрушения Улубурун',
                     'Пектораль со скарабеем Тутанхамона',
                     'Скарабей Хатшепсут',
                     'Брачный скарабей Аменхотепа III'],
              'en': ['Uluburun Gold Scarab of Nefertiti',
                     'Tutankhamun Pectoral Scarab',
                     'Scarab of Hatshepsut',
                     'Amenhotep III Marriage Scarab']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Uluburun oltin skarabeyi (Nefertiti nomi bitilgan)',
                     'ru': 'Золотой скарабей царицы Нефертити из кораблекрушения Улубурун',
                     'en': 'Uluburun Gold Scarab of Nefertiti'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Nefertiti_Scarab_Uluburun.jpg',
  'fun_fact': {'uz': "Turkiya qirg'oqlarida suv ostidan topilgan mil. avv. XIV asrga oid kema halokati xarobasidan "
                     'chiqqan ushbu noyob oltin skarabey Nefertitining hayotlik davriga oid kam sonli yodgorliklardan '
                     'biridir.',
               'ru': 'Найден в затонувшем около 1300 г. до н.э. финикийском торговом судне у мыса Улубурун; '
                     'единственный в мире золотой скарабей с картушем Нефертити.',
               'en': 'Discovered in the Late Bronze Age Uluburun shipwreck off Turkey, this tiny solid gold scarab '
                     'bears the hieroglyphic cartouche of Queen Nefertiti.'},
  'aliases': ['uluburun skarabeyi', 'nefertiti skarabeyi', 'скарабей улубурун', 'uluburun scarab', 'nefertiti scarab']},
 {'id': 'hist_art_042',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Artemision Zevsi',
                     'Riashe bronza jangchilari haykallari',
                     'Delfi aravakashi',
                     'Attik jangchi haykali'],
              'ru': ['Бронзовая статуя с мыса Артемисион',
                     'Бронзовые воины из Риаче (Древняя Греция)',
                     'Дельфийский возничий',
                     'Марафонский юноша'],
              'en': ['Artemision Bronze', 'Riace Bronzes (Riace Warriors)', 'Charioteer of Delphi', 'Marathon Youth']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Riashe bronza jangchilari haykallari',
                     'ru': 'Бронзовые воины из Риаче (Древняя Греция)',
                     'en': 'Riace Bronzes (Riace Warriors)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Riace_bronzes_Reggio_Calabria.jpg',
  'fun_fact': {'uz': "1972 yilda Italiyaning Riashe qirg'oqlari yaqinida dengiz tubidan topilgan mil. avv. V asrga oid "
                     "ikki yunon jangchisi haykali to'liq saqlangan kam sonli qadimgi yunon bronza asarlaridandir.",
               'ru': 'Две полноразмерные греческие статуи нагих воинов V века до н.э., случайно обнаруженные дайвером '
                     'на дне Ионического моря у города Риаче в 1972 году.',
               'en': 'Two full-size Greek bronze statues of naked bearded warriors dating to c. 460-450 BC, discovered '
                     'on the seabed near Riace Marina in Calabria in 1972.'},
  'aliases': ['riashe jangchilari', 'riashe bronzalari', 'воины из риаче', 'риаче', 'riace bronzes', 'riace warriors']},
 {'id': 'hist_art_043',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Dyurandal qilichi', 'Ekskalibur', 'Juaioz — Buyuk Karlning tojlari qilichi', 'Kolyada qilichi'],
              'ru': ['Меч Дюрандаль', 'Экскалибур', 'Жуайёз — коронационный меч Карла Великого', 'Меч Колада'],
              'en': ['Durendal', 'Excalibur', 'Joyeuse — Coronation Sword of Charlemagne', 'Colada']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Juaioz — Buyuk Karlning tojlari qilichi',
                     'ru': 'Жуайёз — коронационный меч Карла Великого',
                     'en': 'Joyeuse — Coronation Sword of Charlemagne'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/23/Joyeuse_Louvre_MR380.jpg',
  'fun_fact': {'uz': 'Luvr muzeyida saqlanuvchi ushbu afsonaviy qilich asrlar davomida Fransiya qirollarining tojlari '
                     'kiydirish marosimlarida rasmiy davlat ramzi sifatida xizmat qilgan.',
               'ru': 'Легендарный меч («Радостный»), использовавшийся при коронациях французских королей в аббатстве '
                     'Сен-Дени на протяжении столетий.',
               'en': "Preserved in the Louvre, this legendary sword named 'Joyeuse' served in the coronation "
                     'ceremonies of French kings from the 12th to the 19th century.'},
  'aliases': ['juaioz', 'karl buyuk qilichi', 'жуайёз', 'меч карла великого', 'joyeuse', 'charlemagne sword']},
 {'id': 'hist_art_044',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Avliyo Stefan toji', 'Avliyo Eduard toji', 'Avliyo Vatslav toji', 'Lombardiya temir toji'],
              'ru': ['Корона святого Иштвана',
                     'Корона святого Эдуарда',
                     'Корона Святого Вацлава',
                     'Железная корона Ломбардии'],
              'en': ['Holy Crown of Hungary',
                     "St Edward's Crown",
                     'Crown of Saint Wenceslas',
                     'Iron Crown of Lombardy']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Lombardiya temir toji', 'ru': 'Железная корона Ломбардии', 'en': 'Iron Crown of Lombardy'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Couronne_de_fer_Monza.JPG',
  'fun_fact': {'uz': 'Ichki halqasi Iso Masih xochga mixlangan mixlardan biri deb hisoblangan ushbu oltin va '
                     'qimmatbaho toshli toj bilan Karl Buyukdan tortib Napoleon Bonapartgacha Italiya qirollari toj '
                     'kiygan.',
               'ru': 'Внутри короны вкована узкая полоса железа, по легенде изготовленная из гвоздя с Животворящего '
                     'Креста Господня; ею короновался Наполеон Бонапарт.',
               'en': 'Circlet of gold and gems enclosing an iron strip traditionally believed to be beaten from a nail '
                     'of the True Cross; used by Charlemagne and Napoleon.'},
  'aliases': ['lombardiya toji',
              'temir toj',
              'железная корона',
              'железная корона ломбардии',
              'iron crown of lombardy',
              'iron crown']},
 {'id': 'hist_art_045',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Avliyo Vatslav toji (Chexiya qirollik toji)',
                     'Bavariya qirollik toji',
                     'Avstriya imperatorlik toji',
                     'Polsha qirollik toji'],
              'ru': ['Корона Святого Вацлава (корона Чешского королевства)',
                     'Корона королей Баварии',
                     'Австрийская императорская корона',
                     'Корона Болеслава Храброго'],
              'en': ['Crown of Saint Wenceslas (Czech Crown)',
                     'Crown of Bavaria',
                     'Imperial Crown of Austria',
                     'Crown of Boleslaw I']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Avliyo Vatslav toji (Chexiya qirollik toji)',
                     'ru': 'Корона Святого Вацлава (корона Чешского королевства)',
                     'en': 'Crown of Saint Wenceslas (Czech Crown)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Wenzelskrone_Prag.JPG',
  'fun_fact': {'uz': "1346 yilda Muqaddas Rim imperatori Karl IV buyrug'i bilan Chexiya qirollari uchun yasalgan ushbu "
                     "sof oltin toj Praga qal'asidagi Avliyo Vit soborida 7 ta kalitli maxsus xonada saqlanadi.",
               'ru': 'Изготовлена в 1346 году императором Карлом IV из чистого золота, сапфиров, рубинов и изумрудов; '
                     'хранится в соборе Святого Вита за семью замками.',
               'en': 'Commissioned in 1346 by Holy Roman Emperor Charles IV for Bohemian coronations; kept inside St. '
                     'Vitus Cathedral in Prague locked with seven keys.'},
  'aliases': ['avliyo vatslav toji',
              'vatslav toji',
              'корона святого вацлава',
              'crown of saint wenceslas',
              'wenceslas crown']},
 {'id': 'hist_art_046',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Rossiya imperatorlik toji',
                     'Muqaddas Rim imperiyasi imperatorlik toji',
                     'Karl Buyuk shlyapasi',
                     'Vizantiya diadasi'],
              'ru': ['Большая императорская корона России',
                     'Корона Священной Римской империи',
                     'Корона Карла Великого',
                     'Византийская диадема'],
              'en': ['Great Imperial Crown of Russia',
                     'Imperial Crown of the Holy Roman Empire',
                     'Crown of Charlemagne',
                     'Byzantine Imperial Diadem']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Muqaddas Rim imperiyasi imperatorlik toji',
                     'ru': 'Корона Священной Римской империи',
                     'en': 'Imperial Crown of the Holy Roman Empire'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Reichskrone_front.jpg',
  'fun_fact': {'uz': 'X asr oxirida yasalgan sakkizburchak shakldagi ushbu unikal oltin toj emal miniatyuralari va 144 '
                     "ta qimmatbaho tosh bilan bezatilgan bo'lib, hozir Venadagi Xofburg xazinasida saqlanadi.",
               'ru': 'Восьмигранная корона конца X века из восьми шарнирных золотых пластин с эмалями и жемчугом; '
                     'хранится в сокровищнице Хофбурга в Вене.',
               'en': 'Octagonal hoop crown made around 962 AD for Otto I, composed of eight gold plates adorned with '
                     'cloisonné enamel plaques and 144 precious stones.'},
  'aliases': ['muqaddas rim toji',
              'imperatorlik toji',
              'корона священной римской империи',
              'imperial crown',
              'holy roman crown']},
 {'id': 'hist_art_047',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Qozon qalpoqchasi',
                     "Oltin O'rda dubulg'asi",
                     'Monomax qalpoqchasi (Rossiya podsholari toji)',
                     'Monomax barmalari'],
              'ru': ['Шапка Казанская',
                     'Шлем Александра Невского',
                     'Шапка Мономаха (главная регалия русских царей)',
                     'Бармы Мономаха'],
              'en': ['Kazan Cap',
                     'Helmet of Alexander Nevsky',
                     "Monomakh's Cap (Crown of Russian Tsars)",
                     'Monomakh Barmy']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Monomax qalpoqchasi (Rossiya podsholari toji)',
                     'ru': 'Шапка Мономаха (главная регалия русских царей)',
                     'en': "Monomakh's Cap (Crown of Russian Tsars)"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Monomakh_cap_01.jpg',
  'fun_fact': {'uz': 'Moskva Kremli Qurol-aslaha palatasida saqlanuvchi, oltin naqshlar, feruza, yoqut va samur '
                     "mo'ynasi bilan hoshiyalangan bu Sharqona bosh kiyim Pyotr I gacha barcha rus podsholarining "
                     "tojlari bo'lgan.",
               'ru': 'Древнейшая русская регалия из золотых филигранных пластин, собольего меха и драгоценных камней, '
                     'вероятно созданная восточными мастерами в XIV веке.',
               'en': 'Chief regalia of Russian Grand Dukes and Tsars from Ivan the Terrible to Peter the Great; '
                     'crafted from filigree gold plates topped with a cross and edged with sable.'},
  'aliases': ['monomax qalpoqchasi', 'monomax', 'шапка мономаха', 'мономах', "monomakh's cap", 'monomakh']},
 {'id': 'hist_art_048',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Bimaran qutichasi',
                     'Kandahar tosh idishi',
                     'Mir Zakah xazinasi',
                     'Kanishka relikvariy qutichasi (Kushon podsholigi)'],
              'ru': ['Шкатулка из Бимарана',
                     'Кандагарская чаша',
                     'Клад Мир Заках',
                     'Шкатулка Канишки (буддийский реликварий Кушанского царства)'],
              'en': ['Bimaran Casket',
                     'Kandahar Bowl',
                     'Mir Zakah Hoard',
                     'Kanishka Casket (Kushan Buddhist Reliquary)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Kanishka relikvariy qutichasi (Kushon podsholigi)',
                     'ru': 'Шкатулка Канишки (буддийский реликварий Кушанского царства)',
                     'en': 'Kanishka Casket (Kushan Buddhist Reliquary)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/41/KanishkaCasketBritishMuseum.jpg',
  'fun_fact': {'uz': 'Peshovar yaqinidagi Kanishka stupasidan topilgan milodiy 127 yilga oid zarhal mis quticha '
                     "qopqog'ida Budda, Brahma va Indra haykalchalari, yon tomonida esa shoh Kanishka tasviri "
                     'tushirilgan.',
               'ru': 'Позолоченный медный реликварий великого кушанского царя Канишки I с изображением Будды между '
                     'Брахмой и Индрой, найденный близ Пешавара.',
               'en': 'Found near Peshawar in 1908, this gilt bronze reliquary from 127 AD bears an inscription of '
                     'Kushan emperor Kanishka and statuettes of Buddha flanked by Brahma and Indra.'},
  'aliases': ['kanishka qutichasi', 'kanishka relikvariysi', 'шкатулка канишки', 'kanishka casket', 'kanishka']},
 {'id': 'hist_art_049',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Tuproqqal'a saroyi shohona relyeflari (Qadimgi Xorazm)",
                     "Qo'yqirilganqal'a rasmlari",
                     "Ayazqal'a bezaklari",
                     "Jonbosqal'a sopollari"],
              'ru': ['Дворцовые барельефы и скульптуры Топрак-калы (Древний Хорезм)',
                     'Фрески Кой-Крылган-калы',
                     'Украшения Аяз-калы',
                     'Керамика Джанбас-калы'],
              'en': ['Toprak-Kala Palace High Reliefs (Ancient Khwarazm)',
                     'Koy Krylgan Kala Murals',
                     'Ayaz Kala Reliefs',
                     'Djanbas Kala Ceramics']},
  'correct_index': 0,
  'correct_answer': {'uz': "Tuproqqal'a saroyi shohona relyeflari (Qadimgi Xorazm)",
                     'ru': 'Дворцовые барельефы и скульптуры Топрак-калы (Древний Хорезм)',
                     'en': 'Toprak-Kala Palace High Reliefs (Ancient Khwarazm)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Toprak_Kala_clay_statue.jpg',
  'fun_fact': {'uz': "Xorazm arxeologiya-etnografiya ekspeditsiyasi (S.P. Tolstov) tomonidan ochilgan Tuproqqal'a "
                     "shohlar saroyining (mil. II-III asrlar) 'Shohlar zali' va 'Kiyiklar zali'dagi ganch haykallari "
                     'Xorazm madaniyatining nodir yodgorliklaridir.',
               'ru': 'Уникальные глиняные барельефы и скульптуры правителей и богов Хорезма II–III вв. н.э., открытые '
                     'С. Толстовым при раскопках дворца Топрак-кала.',
               'en': 'Discovered by Sergey Tolstov in the royal palace of Toprak-Kala in Karakalpakstan; these 2nd-3rd '
                     'century AD clay high-reliefs portray the ancient kings of Khwarazm.'},
  'aliases': ["tuproqqal'a",
              'tuproqqala relyeflari',
              'топрак-кала',
              'барельефы топрак-калы',
              'toprak kala',
              'toprak-kala']},
 {'id': 'hist_art_050',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Qoratepa monastiri haykallari',
                     'Fayoztepa Budda haykali va triadasining ganch haykali (Termiz)',
                     'Zurmala minorasi relyefi',
                     "Xolchayon ma'buda haykali"],
              'ru': ['Скульптуры монастыря Каратепа',
                     'Скульптурная триада Будды из монастыря Фаязтепа (Термез)',
                     'Рельеф ступы Зурмала',
                     'Скульптура богини из Халчаяна'],
              'en': ['Kara Tepe Monastic Sculptures',
                     'Fayaztepa Buddha Triad Sculpture (Termez, Uzbekistan)',
                     'Zurmala Stupa Relief',
                     'Khalchayan Goddess']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Fayoztepa Budda haykali va triadasining ganch haykali (Termiz)',
                     'ru': 'Скульптурная триада Будды из монастыря Фаязтепа (Термез)',
                     'en': 'Fayaztepa Buddha Triad Sculpture (Termez, Uzbekistan)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Fayaz_Tepe_Buddha_Triad.jpg',
  'fun_fact': {'uz': 'Termiz yaqinidagi I-III asrlarga oid Fayoztepa budda ibodatxonasidan topilgan ushbu mashhur '
                     "triada (Budda va uning ikki rohib shogirdi) ganchdan ishlangan bo'lib, O'zbekiston tarixi davlat "
                     'muzeyida saqlanadi.',
               'ru': 'Известняково-гипсовая триада I–II вв. н.э. из буддийского монастыря Фаязтепа близ Старого '
                     'Термеза — один из шедевров кушанского гандхарского искусства.',
               'en': 'Excavated from the 1st-3rd century AD Buddhist complex at Fayaztepa near Termez, Uzbekistan; '
                     'this gypsum limestone triad depicts Buddha seated beneath the bodhi tree with two monks.'},
  'aliases': ['fayoztepa', 'fayoztepa budda', 'фаязтепа', 'будда фаязтепа', 'fayaztepa', 'fayaz tepe']},
 {'id': 'hist_art_051',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Ximera haykali',
                     'Venetsiya arsloni',
                     "Kapitoliya bo'risi (Rim afsonaviy ramzi)",
                     'Lakon iti haykali'],
              'ru': ['Химера из Ареццо',
                     'Венецианский лев',
                     'Капитолийская волчица (символ Рима)',
                     'Статуя молосской собаки'],
              'en': ['Chimera of Arezzo', 'Venetian Lion', 'Capitoline She-Wolf (Symbol of Rome)', 'Jennings Dog']},
  'correct_index': 2,
  'correct_answer': {'uz': "Kapitoliya bo'risi (Rim afsonaviy ramzi)",
                     'ru': 'Капитолийская волчица (символ Рима)',
                     'en': 'Capitoline She-Wolf (Symbol of Rome)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/6a/She-wolf_suckles_Romulus_and_Remus.jpg',
  'fun_fact': {'uz': "Rim afsonasiga ko'ra shaharga asos solgan egizaklar Romul va Remni emizgan bo'ri tasvirlangan "
                     "bronza haykal; egizaklar haykalchalari XV asrda Antonio del Pollayolo tomonidan qo'shilgan.",
               'ru': 'Бронзовая волчица, вскормившая по легенде основателей Вечного города Ромула и Рема; фигурки '
                     'младенцев добавлены скульптором Поллайоло в эпоху Возрождения.',
               'en': "Depicting the legendary she-wolf nursing Rome's infant founders Romulus and Remus; the twin "
                     'suckling figures were sculpted in the 15th century by Pollaiuolo.'},
  'aliases': ["kapitoliya bo'risi", 'kapitoliya', 'капитолийская волчица', 'capitoline she-wolf', 'capitoline wolf']},
 {'id': 'hist_art_052',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Milos Venerasi', 'Peyoniy Nikasi', 'Afina Parfenos', "Samofrakiya Nikasi (G'alaba ma'budasi)"],
              'ru': ['Венера Милосская', 'Ника Пеония', 'Афина Парфенос', 'Ника Самофракийская (богиня победы)'],
              'en': ['Venus de Milo',
                     'Nike of Paionios',
                     'Athena Parthenos',
                     'Winged Victory of Samothrace (Nike of Samothrace)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Samofrakiya Nikasi (G'alaba ma'budasi)",
                     'ru': 'Ника Самофракийская (богиня победы)',
                     'en': 'Winged Victory of Samothrace (Nike of Samothrace)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Victoire_de_Samothrace_-_Musee_du_Louvre_-_2019.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi II asr boshlarida paros oq marmaridan yo'nilgan ushbu kema burnida qanotlarini "
                     "yoyib turgan ma'buda haykali Luvr muzeyining eng mashhur durdonasidir.",
               'ru': 'Шедевр эллинистической скульптуры II века до н.э. из паросского мрамора; статуя крылатой богини '
                     'победы возвышается на парадной лестнице Лувра.',
               'en': 'Carved from Parian marble in the 2nd century BC to celebrate a naval victory, this headless '
                     'winged goddess dominates the Grand Staircase of the Louvre Museum.'},
  'aliases': ['samofrakiya nikasi',
              'nika',
              'ника самофракийская',
              'крылатая победа',
              'winged victory',
              'nike of samothrace']},
 {'id': 'hist_art_053',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Laokoon va uning o'g'illari haykaltaroshlik guruhi",
                     'Farneze buqasi',
                     'Borgeze gladiator haykali',
                     'Galat va uning xotini'],
              'ru': ['Скульптурная группа «Лаокоон и его сыновья»',
                     'Фарнезский бык',
                     'Боргезский боец',
                     'Самоубийство галла'],
              'en': ['Laocoön and His Sons Sculpture', 'Farnese Bull', 'Borghese Gladiator', 'Ludovisi Gaul']},
  'correct_index': 0,
  'correct_answer': {'uz': "Laokoon va uning o'g'illari haykaltaroshlik guruhi",
                     'ru': 'Скульптурная группа «Лаокоон и его сыновья»',
                     'en': 'Laocoön and His Sons Sculpture'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/17/Laocoon_and_His_Sons_Black_bg.jpg',
  'fun_fact': {'uz': '1506 yilda Rimda topilgan va Mikelanjeloni lol qoldirgan ushbu marmar asar Troya kohini Laokoon '
                     "va uning ikki o'g'lini dengiz mahluqlari bo'g'ib o'ldirayotgan fojiali sahnani ifodalaydi.",
               'ru': 'Найдена в 1506 году в Риме в присутствии Микеланджело; изображает троянского жреца Лаоокона и '
                     'его сыновей, гибнущих в тисках морских змеев.',
               'en': 'Unearthed in Rome in 1506 and admired by Michelangelo, this Hellenistic masterpiece in the '
                     'Vatican depicts the Trojan priest and sons besieged by sea serpents.'},
  'aliases': ['laokoon',
              "laokoon va uning o'g'illari",
              'лаокоон',
              'лаокоон и сыновья',
              'laocoon',
              'laocoon and his sons']},
 {'id': 'hist_art_054',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Diskobol haykali',
                     "Spinario (Oyog'idan tikan sug'urayotgan bola)",
                     "G'oz bilan o'ynayotgan bola",
                     'Delfi aravakashi'],
              'ru': ['Дискобол', 'Спинарио (Мальчик, извлекающий занозу)', 'Мальчик с гусем', 'Дельфийский возничий'],
              'en': ['Discobolus', 'Spinario (Boy with Thorn)', 'Boy with a Goose', 'Charioteer of Delphi']},
  'correct_index': 1,
  'correct_answer': {'uz': "Spinario (Oyog'idan tikan sug'urayotgan bola)",
                     'ru': 'Спинарио (Мальчик, извлекающий занозу)',
                     'en': 'Spinario (Boy with Thorn)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Spinario_Capitoline_MC1186.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi I asrga oid Rim bronza haykali; o'rta asrlardan buyon hech qachon tuproq ostida "
                     "qolmagan va doimiy ko'rgazmada turgan kam sonli qadimgi bronza haykallardan biri.",
               'ru': 'Римская бронзовая статуя мальчика I века до н.э.; одна из крайне редких античных бронз, которая '
                     'никогда не была погребена в земле и всегда стояла на виду.',
               'en': 'Hellenistic-Roman bronze statue from the 1st century BC; one of the very few Classical bronzes '
                     'that never lay buried and remained visible continuously through the Middle Ages.'},
  'aliases': ['spinario', "tikan sug'urayotgan bola", 'спинарио', 'мальчик с занозой', 'boy with thorn']},
 {'id': 'hist_art_055',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Battersea qalqoni',
                     'Xoxdorf oltin qadahi',
                     'Gundestrup kumush qozoni (Keltlar madaniyati)',
                     'Viks krateri'],
              'ru': ['Щит из Баттерси',
                     'Кубок из Хохдорфа',
                     'Котёл из Гундеструпа (кельтский серебряный котёл)',
                     'Кратер из Викса'],
              'en': ['Battersea Shield',
                     'Hochdorf Cauldron',
                     'Gundestrup Cauldron (Celtic Silver Vessel)',
                     'Vix Krater']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Gundestrup kumush qozoni (Keltlar madaniyati)',
                     'ru': 'Котёл из Гундеструпа (кельтский серебряный котёл)',
                     'en': 'Gundestrup Cauldron (Celtic Silver Vessel)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Gundestrupkedlen2.jpg',
  'fun_fact': {'uz': "1891 yilda Daniya torf botqog'idan topilgan mil. avv. I asrga oid ushbu 9 kg sof kumush qozon "
                     'plastinkalarida shoxli kelt xudosi Kernunnos va marosim qurbonliklari tasvirlangan.',
               'ru': 'Серебряный ритуальный котёл I века до н.э. из датского торфяника с барельефами кельтских богов, '
                     'включая рогатого Кернунна в окружении зверей.',
               'en': 'Found in a Danish peat bog in 1891, this 1st-century BC silver vessel displays Celtic mythic '
                     'scenes including the antlered god Cernunnos holding a ram-horned snake.'},
  'aliases': ['gundestrup qozoni', 'gundestrup', 'котёл из гундеструпа', 'гундеструп', 'gundestrup cauldron']},
 {'id': 'hist_art_056',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Uitham qalqoni',
                     'Uondsvort qalqoni',
                     'Satton-Xu qalqoni',
                     'Battersea bronza qalqoni (Temza daryosi)'],
              'ru': ['Щит из Уитхема',
                     'Щит из Уондсворта',
                     'Щит из Саттон-Ху',
                     'Щит из Баттерси (кельтский бронзовый щит)'],
              'en': ['Witham Shield',
                     'Wandsworth Shield',
                     'Sutton Hoo Shield',
                     'Battersea Shield (Celtic Bronze Shield)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Battersea bronza qalqoni (Temza daryosi)',
                     'ru': 'Щит из Баттерси (кельтский бронзовый щит)',
                     'en': 'Battersea Shield (Celtic Bronze Shield)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Battersea_Shield.jpg',
  'fun_fact': {'uz': "1857 yilda London yaqinida Temza tubidan topilgan La-Ten kelt san'ati durdonasi; 27 ta qizil "
                     "shisha emali bilan bezatilgan bo'lib, jangda emas, muqaddas qurbonlik marosimida ishlatilgan.",
               'ru': 'Бронзовый кельтский парадный щит I века до н.э. с 27 заклепками из красной непрозрачной эмали, '
                     'принесённый в дар речным богам Темзы.',
               'en': 'Cast in Celtic La Tène style around 350-50 BC, decorated with red glass paste inlays; retrieved '
                     'from the River Thames where it was deposited as a votive offering.'},
  'aliases': ['battersea qalqoni', 'battersea', 'щит из баттерси', 'баттерси', 'battersea shield']},
 {'id': 'hist_art_057',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Tara to'g'nog'ichi (Qadimgi Irlandiya broshi)",
                     'Xanterston broshi',
                     "Londi to'g'nog'ichi",
                     "Ballinderri to'g'nog'ichi"],
              'ru': ['Брошь из Тары (кельтская фибула)',
                     'Брошь Хантерстона',
                     'Лондисборская фибула',
                     'Брошь Баллиндерри'],
              'en': ['Tara Brooch (Celtic Pseudo-penannular Brooch)',
                     'Hunterston Brooch',
                     'Londesborough Brooch',
                     'Ballinderry Brooch']},
  'correct_index': 0,
  'correct_answer': {'uz': "Tara to'g'nog'ichi (Qadimgi Irlandiya broshi)",
                     'ru': 'Брошь из Тары (кельтская фибула)',
                     'en': 'Tara Brooch (Celtic Pseudo-penannular Brooch)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b3/TaraBrooch_NationalMuseumOfIreland.jpg',
  'fun_fact': {'uz': "Taxminan milodiy 710-750 yillarda Irlandiyada quyma kumush, zarhal, tillakor sim to'r va "
                     "qimmatbaho toshlardan ishlangan bu brosh kelt zargarlik san'atining eng yuksak cho'qqisidir.",
               'ru': 'Шедевр островного кельтского ювелирного искусства VIII века из позолоченного серебра с тончайшей '
                     'филигранью, янтарем и стеклом; хранится в Национальном музее Ирландии.',
               'en': 'Created around 710-750 AD in gilded silver with intricate gold filigree and amber studs; '
                     'epitomizes the peak of early medieval Insular metalwork in Ireland.'},
  'aliases': ['tara broshi', "tara to'g'nog'ichi", 'брошь из тары', 'брошь тара', 'tara brooch']},
 {'id': 'hist_art_058',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Arda kadoshi',
                     'Derrinaflan kumush kadoshi (chalice)',
                     'Tassilo kadoshi',
                     'Guaqqar xazinasi kadoshi'],
              'ru': ['Потир из Арда',
                     'Потир из Дерринафлана (ирландская церковная чаша)',
                     'Потир Тассилона',
                     'Чаша из Гурдона'],
              'en': ['Ardagh Chalice',
                     'Derrynaflan Chalice (Irish Silver Chalice)',
                     'Tassilo Chalice',
                     'Chalice of Gourdon']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Derrinaflan kumush kadoshi (chalice)',
                     'ru': 'Потир из Дерринафлана (ирландская церковная чаша)',
                     'en': 'Derrynaflan Chalice (Irish Silver Chalice)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Derrynaflan_chalice.jpg',
  'fun_fact': {'uz': '1980 yilda Tipperari grafligidagi monastir xarobasidan metall qidiruvchi ixlosmandlar tomonidan '
                     'topilgan IX asrga oid zarhal kumush marosim kosasi.',
               'ru': 'Был найден в 1980 году в руинах аббатства Дерринафлан в Ирландии; серебряный потир IX века с '
                     'янтарными вставками и золотой филигранью.',
               'en': 'Unearthed in 1980 with a metal detector at an island bog monastery in County Tipperary; a '
                     '9th-century liturgical chalice richly ornamented with filigree and amber.'},
  'aliases': ['derrinaflan chalice', 'derrinaflan kosasi', 'потир дерринафлан', 'derrinaflan chalice']},
 {'id': 'hist_art_059',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Kumush kodeks',
                     'Sinay kodeksi',
                     'Giyas kodeksi (Iblis Injili / Codex Gigas)',
                     'Amiatinus kodeksi'],
              'ru': ['Серебряный кодекс',
                     'Синайский кодекс',
                     'Гигантский кодекс (Библия Дьявола / Codex Gigas)',
                     'Амиатинский кодекс'],
              'en': ['Codex Argenteus', 'Codex Sinaiticus', "Codex Gigas (The Devil's Bible)", 'Codex Amiatinus']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Giyas kodeksi (Iblis Injili / Codex Gigas)',
                     'ru': 'Гигантский кодекс (Библия Дьявола / Codex Gigas)',
                     'en': "Codex Gigas (The Devil's Bible)"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Codex_Gigas_devil.jpg',
  'fun_fact': {'uz': 'XIII asrda Chexiya monastirida 160 ta eshak terisidan tayyorlangan 75 kg li dunyodagi eng katta '
                     "o'rta asr qo'lyozmasi bo'lib, uning bir sahifasida butun bo'yli iblis surati chizilgan.",
               'ru': 'Крупнейшая средневековая рукопись в мире весом 75 кг, созданная в начале XIII века; содержит '
                     'полностраничную иллюстрацию Сатаны, породившую легенду о монахе.',
               'en': 'Weighing 75 kg and written on donkey-skin vellum in 13th-century Bohemia, it is the largest '
                     'extant medieval manuscript, famed for a full-page portrait of the Devil.'},
  'aliases': ['giyas kodeksi', 'iblis injili', 'codex gigas', 'библия дьявола', 'гигантский кодекс', 'devils bible']},
 {'id': 'hist_art_060',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Oltin kodeks',
                     'Vatikan kodeksi',
                     'Aleksandriya kodeksi',
                     'Kumush kodeks (Codex Argenteus — Got Injili)'],
              'ru': ['Золотой кодекс',
                     'Ватиканский кодекс',
                     'Александрийский кодекс',
                     'Серебряный кодекс (Codex Argenteus — готская Библия)'],
              'en': ['Codex Aureus',
                     'Codex Vaticanus',
                     'Codex Alexandrinus',
                     'Codex Argenteus (Silver Bible in Gothic)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Kumush kodeks (Codex Argenteus — Got Injili)',
                     'ru': 'Серебряный кодекс (Codex Argenteus — готская Библия)',
                     'en': 'Codex Argenteus (Silver Bible in Gothic)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/78/Codex_Argenteus.jpg',
  'fun_fact': {'uz': 'Milodiy VI asrda binafsharang pergamentga kumush va oltin siyoh bilan got tilida yozilgan ushbu '
                     "nodir qo'lyozma episkop Vulfila tomonidan tarjima qilingan got tilining asosiy manbasidir.",
               'ru': 'Написан серебряными и золотыми чернилами на пурпурном пергаменте для короля остготов Теодориха '
                     'Великого; главный памятник вымершего готского языка.',
               'en': 'Written in silver and gold ink on purple-stained vellum for Ostrogothic King Theodoric the Great '
                     'in the 6th century; the primary surviving text of the Gothic language.'},
  'aliases': ['kumush kodeks', 'codex argenteus', 'серебряный кодекс', 'готская библия', 'silver bible']},
 {'id': 'hist_art_061',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Voynich qo'lyozmasi (Sirli shifrlangan kitob)",
                     'Roxonts kodeksi',
                     'Soyga kitobi',
                     "Ripley o'rami"],
              'ru': ['Рукопись Войнича (неразгаданный иллюстрированный манускрипт)',
                     'Кодекс Рохонци',
                     'Книга Сойги',
                     'Свиток Рипли'],
              'en': ['Voynich Manuscript (Undeciphered Illustrated Codex)',
                     'Rohonc Codex',
                     'Book of Soyga',
                     'Ripley Scroll']},
  'correct_index': 0,
  'correct_answer': {'uz': "Voynich qo'lyozmasi (Sirli shifrlangan kitob)",
                     'ru': 'Рукопись Войнича (неразгаданный иллюстрированный манускрипт)',
                     'en': 'Voynich Manuscript (Undeciphered Illustrated Codex)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/44/Voynich_Manuscript_%28156%29.jpg',
  'fun_fact': {'uz': "XV asr boshlariga oid noma'lum yozuv va til bilan bitilgan, afsonaviy o'simliklar va yulduzlar "
                     "suratlari tushirilgan bu qo'lyozmani dunyoning eng buyuk kriptograflari ham hali shifrlay "
                     'olmagan.',
               'ru': 'Рукопись начала XV века на неизвестном языке с неизвестным алфавитом и рисунками фантастических '
                     'трав, которую столетиями безуспешно пытаются прочесть криптографы мира.',
               'en': 'Carbon-dated to the early 15th century, this illustrated codex written in an unknown writing '
                     "system remains the world's most mysterious undeciphered manuscript."},
  'aliases': ["voynich qo'lyozmasi", 'voynich', 'манускрипт войнича', 'рукопись войнича', 'voynich manuscript']},
 {'id': 'hist_art_062',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Gutenberg Injili',
                     'Dunxuan Olmos sutrasi (Eng qadimgi bosma kitob, 868 y.)',
                     'Dharani matni',
                     'Jikji'],
              'ru': ['Библия Гутенберга',
                     'Алмазная сутра из Дуньхуана (древнейшая точно датированная печатная книга, 868 г.)',
                     'Дхарани-сутра из Пульгукса',
                     'Чикчи'],
              'en': ['Gutenberg Bible',
                     'Dunhuang Diamond Sutra (Oldest Dated Printed Book, 868 AD)',
                     'Dharani Sutra of Bulguksa',
                     'Jikji']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Dunxuan Olmos sutrasi (Eng qadimgi bosma kitob, 868 y.)',
                     'ru': 'Алмазная сутра из Дуньхуана (древнейшая точно датированная печатная книга, 868 г.)',
                     'en': 'Dunhuang Diamond Sutra (Oldest Dated Printed Book, 868 AD)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Diamond_Sutra_woodcut.jpg',
  'fun_fact': {'uz': "Xitoyning Dunxuan Mogao g'orlaridan Aurel Steyn topgan ushbu ksilografiya (yog'och gravyura) "
                     "usulida bosilgan o'ram 868 yil 11 may sanasi ko'rsatilgan dunyodagi eng qadimgi sanali bosma "
                     'kitobdir.',
               'ru': 'Напечатана ксилографическим способом в Китае 11 мая 868 года Ван Цзе; древнейший сохранившийся '
                     'печатный документ в мире с точной датой выпуска.',
               'en': 'Printed with woodblocks on May 11, 868 AD and discovered in the Mogao Caves at Dunhuang; '
                     "universally recognized as the world's earliest dated printed book."},
  'aliases': ['olmos sutra', 'dunxuan sutrasi', 'алмазная сутра', 'diamond sutra', 'dunhuang sutra']},
 {'id': 'hist_art_063',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Oviedo dastro'moli",
                     "Veronika ro'moli",
                     'Turin kafani (Muqaddas plashchanitsa)',
                     'Manopello yuzi'],
              'ru': ['Судариум из Овьедо', 'Плат Вероники', 'Туринская плащаница', 'Лик из Маноппелло'],
              'en': ['Sudarium of Oviedo', 'Veil of Veronica', 'Shroud of Turin', 'Manoppello Image']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Turin kafani (Muqaddas plashchanitsa)',
                     'ru': 'Туринская плащаница',
                     'en': 'Shroud of Turin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/14/Shroud_of_Turin_positive_and_negative_displaying_original_color_tone_360_dpi.jpg',
  'fun_fact': {'uz': "Turin soborida saqlanuvchi 4,4 metrli bu zig'ir matoda xochga mixlangan erkak tanasining old va "
                     "orqa salbiy (negativ) tasviri aks etgan bo'lib, xristian olamining eng bahsli yodgorligidir.",
               'ru': 'Льняное полотно длиной 4,4 м со слабым негативным отпечатком тела распятого человека; хранится в '
                     'соборе святого Иоанна Крестителя в Турине.',
               'en': 'Linen cloth bearing the faint negative image of a crucified man, kept in Turin Cathedral; one of '
                     'the most studied and debated artifacts in religious history.'},
  'aliases': ['turin kafani', 'turin plashchanitsasi', 'туринская плащаница', 'shroud of turin', 'holy shroud']},
 {'id': 'hist_art_064',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Antioxiya nayzasi',
                     'Echmiadzin nayzasi',
                     'Krakov nayzasi',
                     'Taqdir nayzasi (Vena Muqaddas nayzasi / Longin nayzasi)'],
              'ru': ['Антиохийское копьё',
                     'Эчмиадзинское копьё',
                     'Краковское копьё',
                     'Копьё Судьбы (Венское Священное копьё / Копьё Лонгина)'],
              'en': ['Holy Lance of Antioch',
                     'Holy Lance of Echmiadzin',
                     'Krakow Lance',
                     'Holy Lance (Spear of Destiny / Vienna Lance)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Taqdir nayzasi (Vena Muqaddas nayzasi / Longin nayzasi)',
                     'ru': 'Копьё Судьбы (Венское Священное копьё / Копьё Лонгина)',
                     'en': 'Holy Lance (Spear of Destiny / Vienna Lance)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/d/da/Heilige_Lanze_Hofburg.JPG',
  'fun_fact': {'uz': "Rivoyatga ko'ra xochdagi Isoga sanchilgan nayza; Vena Xofburg xazinasida saqlanadigan bu nayzaga "
                     'oltin qoplama ichiga muqaddas mix joylangan deb ishonilgan.',
               'ru': 'Одна из важнейших реликвий Страстей Христовых и атрибут коронации императоров Священной Римской '
                     'империи; хранится в сокровищнице Хофбурга.',
               'en': 'Legendary spear attributed to the Roman soldier Longinus; preserved among Imperial Regalia in '
                     'the Hofburg in Vienna with gold cuff containing a holy relic.'},
  'aliases': ['taqdir nayzasi', 'muqaddas nayza', 'копьё судьбы', 'священное копьё', 'holy lance', 'spear of destiny']},
 {'id': 'hist_art_065',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Uch afsunsharif (maglar) oltin relikvariysi (Kyoln sobori)',
                     'Avliyo Yelizaveta relikvariysi',
                     'Karl Buyuk relikvariysi',
                     'Avliyo Sebaldus qabri'],
              'ru': ['Рака трёх волхвов в Кёльнском соборе',
                     'Рака святой Елизаветы',
                     'Рака Карла Великого',
                     'Гробница святого Себальда'],
              'en': ['Shrine of the Three Kings (Cologne Cathedral)',
                     'Shrine of Saint Elizabeth',
                     'Shrine of Charlemagne',
                     'Shrine of Saint Sebaldus']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Uch afsunsharif (maglar) oltin relikvariysi (Kyoln sobori)',
                     'ru': 'Рака трёх волхвов в Кёльнском соборе',
                     'en': 'Shrine of the Three Kings (Cologne Cathedral)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Dreikoenigenschrein_front.jpg',
  'fun_fact': {'uz': 'Verdenlik Nikolay tomonidan XII asr oxirida Kyoln sobori uchun yasalgan ushbu uch qavatli '
                     "bazilika shaklidagi zarhal oltin sarkofag Yevropadagi eng yirik o'rta asr relikvariysidir.",
               'ru': 'Создана мастером Николаем Верденским около 1190–1225 гг.; грандиозный позолоченный саркофаг в '
                     'виде трёхнефной базилики с мощами библейских волхвов.',
               'en': 'Crafted by Nicholas of Verdun around 1190-1225 in Cologne Cathedral; this triple-basilica gilded '
                     'reliquary holds the reputed bones of the Biblical Magi.'},
  'aliases': ['uch afsunsharif',
              'kyoln relikvariysi',
              'рака трёх волхвов',
              'shrine of the three kings',
              'three kings shrine']},
 {'id': 'hist_art_066',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Trundxolm oltin kosasi',
                     'Gallexus oltin shoxlari (Daniya runik yodgorligi)',
                     'Brakteat xazinasi',
                     'Torsbjerg shoxi'],
              'ru': ['Золотой сосуд Трундхольма',
                     'Золотые рога из Галлехуса (Дания, V век)',
                     'Клад брактеатов из Сковборг',
                     'Рог из Торсберга'],
              'en': ['Trundholm Gold Cup',
                     'Golden Horns of Gallehus (5th-century Danish Gold Horns)',
                     'Skovborg Bracteate Hoard',
                     'Thorsberg Horn']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Gallexus oltin shoxlari (Daniya runik yodgorligi)',
                     'ru': 'Золотые рога из Галлехуса (Дания, V век)',
                     'en': 'Golden Horns of Gallehus (5th-century Danish Gold Horns)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/a/ad/Gallehus-horns.png',
  'fun_fact': {'uz': 'V asrga oid sof oltindan yasalgan va runik yozuvlar hamda mifologik maxluqlar tasvirlangan bu '
                     "ikki shox 1639 va 1734 yillarda topilgan, biroq 1802 yilda o'g'irlanib eritib yuborilgan (hozir "
                     'nusxalari mavjud).',
               'ru': 'Два золотых рога V века с древнейшими скандинавскими руническими надписями; трагически украдены '
                     'и переплавлены ювелиром в 1802 году.',
               'en': 'Discovered in 1639 and 1734 in Jutland, these 5th-century gold horns featured Proto-Norse runes; '
                     'tragically stolen and melted down in 1802, known from detailed casts.'},
  'aliases': ['gallexus shoxlari',
              'gallexus',
              'золотые рога галлехуса',
              'галлехус',
              'horns of gallehus',
              'gallehus horns']},
 {'id': 'hist_art_067',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Yig'layotgan ayollar sarkofagi",
                     'Likiy sarkofagi',
                     'Aleksandr sarkofagi (Sidon shohi Abdalonim qabri)',
                     'Etrusk juftlik sarkofagi'],
              'ru': ['Саркофаг плакальщиц',
                     'Ликийский саркофаг',
                     'Сидонский саркофаг («Саркофаг Александра»)',
                     'Этрусский саркофаг супругов'],
              'en': ['Sarcophagus of the Mourning Women',
                     'Lycian Sarcophagus of Sidon',
                     'Alexander Sarcophagus (Sidon Royal Tomb)',
                     'Etruscan Spouses Sarcophagus']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Aleksandr sarkofagi (Sidon shohi Abdalonim qabri)',
                     'ru': 'Сидонский саркофаг («Саркофаг Александра»)',
                     'en': 'Alexander Sarcophagus (Sidon Royal Tomb)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Alexander_Sarcophagus_Istanbul_Archaeological_Museum.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi IV asr oxirida Sidon (Livan)da oq pentelikon marmaridan yo'nilgan ushbu ajoyib "
                     'sarkofag devorlarida Iskandar Zulqarnaynning forslarga qarshi jangi va sher ovi sahnalari aks '
                     'etgan.',
               'ru': 'Мраморный саркофаг IV века до н.э. из некрополя Сидона; украшен барельефами битвы Александра с '
                     'персами при Иссе; шедевр Стамбульского археологического музея.',
               'en': 'Found in Sidon and displayed in Istanbul, this Hellenistic Pentelic marble sarcophagus is carved '
                     'in high relief with Alexander the Great fighting Persians at Issus.'},
  'aliases': ['aleksandr sarkofagi', 'саркофаг александра', 'сидонский саркофаг', 'alexander sarcophagus']},
 {'id': 'hist_art_068',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Lartia Seyanti sarkofagi',
                     'Amazonkalar sarkofagi',
                     'Tarkviniya tosh sarkofagi',
                     'Er-xotin sarkofagi (Banditachcha etrusk terrakotasi)'],
              'ru': ['Саркофаг Лартии Сейанти',
                     'Саркофаг амазонок',
                     'Саркофаг из Тарквинии',
                     'Саркофаг супругов из Черветери (этрусская терракота)'],
              'en': ['Sarcophagus of Larthia Seianti',
                     'Amazon Sarcophagus',
                     'Tarquinia Sarcophagus',
                     'Sarcophagus of the Spouses (Etruscan Terracotta, Cerveteri)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Er-xotin sarkofagi (Banditachcha etrusk terrakotasi)',
                     'ru': 'Саркофаг супругов из Черветери (этрусская терракота)',
                     'en': 'Sarcophagus of the Spouses (Etruscan Terracotta, Cerveteri)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/ba/Sarcophagus_of_the_Spouses_Louvre_Cp5194.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi VI asr oxiriga oid etrusk terrakota asari bo'lib, unda qabr qopqog'ida "
                     'yonboshlab yotgan va samimiy tabassum qilayotgan er-xotin tasvirlangan (Rim va Luvrda '
                     'saqlanadi).',
               'ru': 'Этрусский терракотовый саркофаг VI века до н.э. из некрополя Бандитачча; супруги пируют вместе '
                     'на смертном одре, что отражает высокий статус женщин в Этрурии.',
               'en': 'Late 6th-century BC Etruscan painted terracotta sarcophagus showing a married couple reclining '
                     'together at a banquet; symbolizes the equal status of women in Etruria.'},
  'aliases': ['er-xotin sarkofagi', 'etrusk sarkofagi', 'саркофаг супругов', 'sarcophagus of the spouses']},
 {'id': 'hist_art_069',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Aretso ximerasi (Etrusk bronza haykali)',
                     "Kapitoliya bo'risi",
                     'Todi Mars haykali',
                     'Volterra soyasi'],
              'ru': ['Химера из Ареццо (этрусская бронзовая статуя)',
                     'Капитолийская волчица',
                     'Марс из Тоди',
                     'Тень вечера (Вольтерра)'],
              'en': ['Chimera of Arezzo (Etruscan Bronze Statue)',
                     'Capitoline She-Wolf',
                     'Mars of Todi',
                     'Evening Shadow']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Aretso ximerasi (Etrusk bronza haykali)',
                     'ru': 'Химера из Ареццо (этрусская бронзовая статуя)',
                     'en': 'Chimera of Arezzo (Etruscan Bronze Statue)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Chimera_di_arezzo_01.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 400 yillarga oid sher tanasi, orqasida echki boshi va dumi o'rnida ilon "
                     'tasvirlangan ushbu dahshatli afsonaviy mahluq bronza haykali 1553 yilda Aretsoda topilgan.',
               'ru': 'Бронзовое чудовище около 400 года до н.э. с телом льва, растущей из спины головой козла и '
                     'хвостом-змеёй; найдена герцогом Козимо I Медичи в Тоскане.',
               'en': "Dating to c. 400 BC, this Etruscan bronze depiction of the mythical beast has a lion's body, a "
                     "goat's head emerging from its spine, and a serpent tail."},
  'aliases': ['aretso ximerasi', 'ximera', 'химера из ареццо', 'химера', 'chimera of arezzo', 'chimera']},
 {'id': 'hist_art_070',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Efroniya krateri',
                     'Fransua vazasi (Qora figurali attik krater)',
                     'Dipilon amforasi',
                     'Ezekiy amforasi'],
              'ru': ['Кратер Евфрония',
                     'Ваза Франсуа (аттический чернофигурный кратер)',
                     'Дипилонская амфора',
                     'Амфора Эксекия'],
              'en': ['Euphronios Krater',
                     'François Vase (Attic Black-Figure Volute Krater)',
                     'Dipylon Amphora',
                     'Exekias Amphora']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Fransua vazasi (Qora figurali attik krater)',
                     'ru': 'Ваза Франсуа (аттический чернофигурный кратер)',
                     'en': 'François Vase (Attic Black-Figure Volute Krater)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Francois_Vase_side_A.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 570 yillarda afinalik kulol Ergotim va rassom Klitiy tomonidan yasalgan bu 66 '
                     'sm lik vaza ustida yunon mifologiyasiga oid 270 dan ortiq odam va hayvon shakllari chizilgan.',
               'ru': 'Шедевр греческой вазописи 570 г. до н.э.; на 6 фризах расписаны более 270 фигур героев Троянской '
                     'войны, подвигов Ахилла и Тесея.',
               'en': 'Created around 570 BC by potter Ergotimos and painter Kleitias; this Attic black-figure krater '
                     'features over 270 figures and 121 inscriptions detailing Greek myths.'},
  'aliases': ['fransua vazasi', 'ваза франсуа', 'francois vase', 'françois vase']},
 {'id': 'hist_art_071',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Kaiseraugst likopchasi',
                     'Sevso lagani',
                     'Mildenxoll katta kumush likopchasi (Okean likopchasi)',
                     'Eskvilin xazinasi likopchasi'],
              'ru': ['Блюдо из Кайзераугста',
                     'Блюдо Севсо',
                     'Великое блюдо океана из Милденхолла (римское серебро)',
                     'Шкатулка Проекты'],
              'en': ['Kaiseraugst Achilles Plate',
                     'Sevso Hunting Plate',
                     'Great Dish of Mildenhall (Oceanus Dish)',
                     'Projecta Casket']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Mildenxoll katta kumush likopchasi (Okean likopchasi)',
                     'ru': 'Великое блюдо океана из Милденхолла (римское серебро)',
                     'en': 'Great Dish of Mildenhall (Oceanus Dish)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Mildenhall_Great_Dish.jpg',
  'fun_fact': {'uz': '1942 yilda Angliyaning Suffolk grafligida traktorchi shudgor qilayotganda topgan IV asrga oid 8 '
                     'kg dan ortiq sof kumush Rim lagani markazida dengiz xudosi Okean yuzi aks ettirilgan.',
               'ru': 'Римское серебряное блюдо IV века весом более 8 кг с изображением морского бога Океана и '
                     'вакхических плясок; центральный экспонат клада Милденхолл в Британском музее.',
               'en': 'Weighing over 8 kg of solid silver, this 4th-century Roman platter was plowed up in Suffolk in '
                     '1942; centered on the horned face of Neptune/Oceanus surrounded by Nereids.'},
  'aliases': ['mildenxoll lagani',
              'mildenxoll likopchasi',
              'блюдо океана',
              'милденхолл',
              'mildenhall dish',
              'oceanus dish']},
 {'id': 'hist_art_072',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Beruvild kumush ko'zasi",
                     'Portlend vazasi',
                     'Tyomis kubogi',
                     'Xoksn xazinasi imperator ayol qalampirdoni'],
              'ru': ['Серебряный кувшин из Бертувиля',
                     'Портлендская ваза',
                     'Кубок из Тёмиса',
                     'Перечница в виде императрицы из клада Хоксне'],
              'en': ['Berthouville Pitcher',
                     'Portland Vase',
                     'Thetford Spoons',
                     'Empress Pepper Pot of the Hoxne Hoard']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Xoksn xazinasi imperator ayol qalampirdoni',
                     'ru': 'Перечница в виде императрицы из клада Хоксне',
                     'en': 'Empress Pepper Pot of the Hoxne Hoard'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Empress_pepper_pot_Hoxne.jpg',
  'fun_fact': {'uz': "1992 yilda Angliyada bolg'a qidirayotgan odam metall qidirgich bilan topgan Rimning eng boy "
                     'xazinasidagi zarhal kumushdan ishlangan imperator ayol qiyofasidagi murchdon.',
               'ru': 'Серебряная солонка-перечница V века в виде бюста знатной римлянки с механизмом регулировки '
                     'помола; жемчужина клада Хоксне из почти 15 000 золотых и серебряных монет.',
               'en': 'A 5th-century hollow silver-gilt statuette of an imperial lady that doubled as an exquisite '
                     'table pepper castor, unearthed with the giant Hoxne Hoard in 1992.'},
  'aliases': ['xoksn qalampirdoni',
              'xoksn xazinasi',
              'перечница хоксне',
              'клад хоксне',
              'hoxne pepper pot',
              'empress pepper pot']},
 {'id': 'hist_art_073',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Paziriq gilami (Dunyodagi eng qadimiy jun gilam)',
                     'Ardabil gilami',
                     "Noin-Ula to'qimasi",
                     'Varaxsha ipak gilami'],
              'ru': ['Пазырыкский ковёр (старейший в мире ворсовый ковёр)',
                     'Ардебильский ковёр',
                     'Ткань из Ноин-Улы',
                     'Шёлковый ковёр Варахши'],
              'en': ["Pazyryk Carpet (World's Oldest Pile Carpet)",
                     'Ardabil Carpet',
                     'Noin-Ula Textile',
                     'Varakhsha Silk Rug']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Paziriq gilami (Dunyodagi eng qadimiy jun gilam)',
                     'ru': 'Пазырыкский ковёр (старейший в мире ворсовый ковёр)',
                     'en': "Pazyryk Carpet (World's Oldest Pile Carpet)"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Pazyryk_carpet.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi V asrga oid Oltoydagi Paziriq muzlagan sak-skif qo'rg'onidan topilgan bu gilam "
                     '2500 yil davomida muz qatlamida chirimasdan mukammal saqlangan va Ermitajda turadi.',
               'ru': 'Ворсовый шерстяной ковёр V века до н.э., законсервированный в вечной мерзлоте алтайского кургана '
                     'Пазырык; шедевр древнего ткачества с изображениями всадников и оленей.',
               'en': 'Preserved intact in permafrost for 2,500 years in the Altai Mountains, this 5th-century BC wool '
                     'pile carpet in the Hermitage depicts horsemen, fallow deer, and griffins.'},
  'aliases': ['paziriq gilami', 'paziriq', 'пазырыкский ковёр', 'пазырык', 'pazyryk carpet', 'pazyryk']},
 {'id': 'hist_art_074',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Kul-Oba oltin ko'zasi",
                     "Tovsta Mogila skif oltin pektorali (ko'krak bezagi)",
                     'Soloxa oltin tarozi',
                     'Chertomlik kumush amforasi'],
              'ru': ['Куль-Обская золотая чаша',
                     'Золотая пектораль из Толстой Могилы (скифский шедевр)',
                     'Золотой гребень из Солохи',
                     'Чертомлыкская амфора'],
              'en': ['Kul-Oba Gold Vase',
                     'Scythian Gold Pectoral of Tovsta Mohyla',
                     'Solokha Golden Comb',
                     'Chertomlyk Amphora']},
  'correct_index': 1,
  'correct_answer': {'uz': "Tovsta Mogila skif oltin pektorali (ko'krak bezagi)",
                     'ru': 'Золотая пектораль из Толстой Могилы (скифский шедевр)',
                     'en': 'Scythian Gold Pectoral of Tovsta Mohyla'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Pectoral_from_Tovsta_Mohyla.jpg',
  'fun_fact': {'uz': "1971 yilda Boris Mozolevskiy tomonidan Ukrainadagi Skif podshosi qo'rg'onidan topilgan mil. avv. "
                     "IV asrga oid 1,15 kg sof oltindan iborat uch yarusli nafis ko'krak nishoni.",
               'ru': 'Найдена археологом Б. Мозолевским в 1971 году; шедевр IV века до н.э. из чистого золота весом '
                     '1,15 кг с ювелирной детализацией скифского быта и сцен терзания зверей.',
               'en': 'Unearthed in 1971 in Ukraine, this 4th-century BC three-tiered solid gold royal breastplate '
                     '(1.15 kg) portrays Scythian pastoral life and mythical animal combat.'},
  'aliases': ['skif pektorali',
              'tovsta mogila pektorali',
              'скифская пектораль',
              'пектораль из толстой могилы',
              'scythian pectoral',
              'tovsta mohyla']},
 {'id': 'hist_art_075',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Al-Mansur qilichi',
                     'Ispaniya Tisona qilichi',
                     "Boabdil qilichi (Granada so'nggi sultoni jinete qilichi)",
                     'Salohiddin qilichi'],
              'ru': ['Меч Аль-Мансура', 'Тисона Сида', 'Меч Боабдиля (последнего эмира Гранады)', 'Сабля Саладина'],
              'en': ['Sword of Almanzor',
                     'Tizona of El Cid',
                     'Sword of Boabdil (Jinete Sword of Last Sultan of Granada)',
                     'Sabre of Saladin']},
  'correct_index': 2,
  'correct_answer': {'uz': "Boabdil qilichi (Granada so'nggi sultoni jinete qilichi)",
                     'ru': 'Меч Боабдиля (последнего эмира Гранады)',
                     'en': 'Sword of Boabdil (Jinete Sword of Last Sultan of Granada)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Espada_jineta_de_Boabdil_%28M.A.N._Madrid%29_01.jpg',
  'fun_fact': {'uz': "1492 yilda Granada qulashi bilan Rekonkista yakunlanganida asir tushgan so'nggi nasriy sulton "
                     'Muhammad XII (Boabdil)ning fil suyagi, emal va oltin bilan bezatilgan shohona qilichi.',
               'ru': 'Парадный меч-хинета конца XV века из слоновой кости, золота и перегородчатой эмали последнего '
                     'мусульманского правителя Гранады Мухаммеда XII (Боабдиля).',
               'en': 'Gilded Nasrid jineta sword belonging to Muhammad XII (Boabdil), the last Muslim ruler of Granada '
                     'who surrendered the Alhambra to Catholic Monarchs in 1492.'},
  'aliases': ['boabdil qilichi', 'boabdil', 'меч боабдиля', 'боабдиль', 'sword of boabdil', 'boabdil']},
 {'id': 'hist_art_076',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Sulton Sulaymon qilichi',
                     'Bobur xanjari',
                     'Nodirshoh xanjari',
                     "To'pqopi zumradli xanjari (Usmoniylar saroy xazinasi)"],
              'ru': ['Меч Сулеймана Великолепного',
                     'Кинжал Бабура',
                     'Кинжал Надир-шаха',
                     'Кинжал Топкапы (изумрудный кинжал османских султанов)'],
              'en': ['Sword of Suleiman',
                     'Dagger of Babur',
                     'Dagger of Nader Shah',
                     'Topkapi Dagger (Emerald Dagger of Ottoman Sultans)']},
  'correct_index': 3,
  'correct_answer': {'uz': "To'pqopi zumradli xanjari (Usmoniylar saroy xazinasi)",
                     'ru': 'Кинжал Топкапы (изумрудный кинжал османских султанов)',
                     'en': 'Topkapi Dagger (Emerald Dagger of Ottoman Sultans)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Topkapi_Dagger.jpg',
  'fun_fact': {'uz': "1746 yilda sulton Mahmud I tomonidan Eron shohi Nodirshohga sovg'a sifatida yasalgan, dastasida "
                     "3 ta ulkan Kolumbiya zumradi o'rnatilgan ushbu xanjar sulton saroyida qolgan (chunki Nodirshoh "
                     "o'ldirilgan edi).",
               'ru': 'Изготовлен в 1746 году для подарка персидскому Надир-шаху, но остался в Стамбуле из-за гибели '
                     'шаха; украшен тремя гигантскими изумрудами и часами в рукояти.',
               'en': 'Commissioned in 1746 by Sultan Mahmud I as a gift for Nader Shah; set with three massive '
                     'emeralds and a watch in the pommel, it remains in Topkapi Palace.'},
  'aliases': ["to'pqopi xanjari", 'zumradli xanjar', 'кинжал топкапы', 'топкапы', 'topkapi dagger']},
 {'id': 'hist_art_077',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Ko'hi Nur olmosi (Buyuk Britaniya tojlari olmosi)",
                     'Orlov olmosi',
                     'Kullinan olmosi',
                     'Regent olmosi'],
              'ru': ['Алмаз «Кохинур» («Гора света»)', 'Алмаз «Орлов»', 'Алмаз «Куллинан»', 'Алмаз «Регент»'],
              'en': ['Koh-i-Noor Diamond (Mountain of Light)', 'Orlov Diamond', 'Cullinan Diamond', 'Regent Diamond']},
  'correct_index': 0,
  'correct_answer': {'uz': "Ko'hi Nur olmosi (Buyuk Britaniya tojlari olmosi)",
                     'ru': 'Алмаз «Кохинур» («Гора света»)',
                     'en': 'Koh-i-Noor Diamond (Mountain of Light)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/69/Koh-i-Noor_glass_replica.jpg',
  'fun_fact': {'uz': 'Hindistonning Golkonda konlaridan topilgan va Boburiylar, Nodirshoh, durroniylar va Panjob '
                     "sikxlari qo'lidan o'tib 1849 yilda qirolicha Viktoriyaga topshirilgan afsonaviy 105 karatli "
                     'rangsiz olmos.',
               'ru': 'Один из известнейших драгоценных камней в истории (105 карат); принадлежал Великим Моголам, '
                     'Надир-шаху и махараджам, пока не стал частью короны королевы Елизаветы.',
               'en': 'Mined in Golconda, India, this famed 105.6-carat diamond passed from the Mughal emperors to '
                     'Nader Shah, Ahmad Shah Durrani, and ultimately the British Crown Jewels.'},
  'aliases': ["ko'hi nur", 'koh-i-noor', 'кохинур', 'кох-и-нур', 'koh-i-noor diamond']},
 {'id': 'hist_art_078',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Ko'hi Nur olmosi",
                     'Daryoyi Nur olmosi («Nur daryosi» — Eron milliy xazinasi)',
                     'Shoh olmosi',
                     'Sansi olmosi'],
              'ru': ['Алмаз Кохинур',
                     'Алмаз «Дерианур» («Море света», сокровищница Ирана)',
                     'Алмаз «Шах»',
                     'Алмаз Санси'],
              'en': ['Koh-i-Noor Diamond',
                     'Darya-ye Noor Diamond (Sea of Light, Iran National Jewels)',
                     'Shah Diamond',
                     'Sancy Diamond']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Daryoyi Nur olmosi («Nur daryosi» — Eron milliy xazinasi)',
                     'ru': 'Алмаз «Дерианур» («Море света», сокровищница Ирана)',
                     'en': 'Darya-ye Noor Diamond (Sea of Light, Iran National Jewels)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Daria-i-noor.jpg',
  'fun_fact': {'uz': "Og'irligi taxminan 182 karat bo'lgan och pushti rangli dunyodagi eng yirik ishlov berilgan "
                     "olmoslardan biri bo'lib, Tehrondagi Markaziy bank xazinasida saqlanadi.",
               'ru': 'Редчайший бледно-розовый бриллиант весом около 182 карат; жемчужина коронных драгоценностей '
                     'Ирана, захваченная Надир-шахом в Индии в 1739 году.',
               'en': 'Weighing roughly 182 carats, this pale pink tabular diamond is one of the rarest and largest cut '
                     'diamonds in the world, housed in the National Jewels of Iran.'},
  'aliases': ['daryoyi nur', 'darya-ye noor', 'дерианур', 'море света', 'darya-i-noor']},
 {'id': 'hist_art_079',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Moviy Oy olmosi',
                     'Vittelsbax olmosi',
                     "Houp olmosi (Mashhur la'nati ko'k brilliant)",
                     'Drezden yashil olmosi'],
              'ru': ['Алмаз «Голубая луна»',
                     'Виттельсбахский голубой алмаз',
                     'Алмаз Хоупа («Проклятый» синий алмаз)',
                     'Дрезденский зелёный бриллиант'],
              'en': ['Blue Moon Diamond',
                     'Wittelsbach-Graff Diamond',
                     'Hope Diamond (Famous Blue Diamond)',
                     'Dresden Green Diamond']},
  'correct_index': 2,
  'correct_answer': {'uz': "Houp olmosi (Mashhur la'nati ko'k brilliant)",
                     'ru': 'Алмаз Хоупа («Проклятый» синий алмаз)',
                     'en': 'Hope Diamond (Famous Blue Diamond)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/30/Hope_Gem.jpg',
  'fun_fact': {'uz': "45,52 karatli to'q ko'k rangli ushbu olmos o'z egalariga kulfat va fojia keltiradi degan "
                     'mish-mishlar bilan mashhur; hozirda Smitson milliy tabiat tarixi muzeyida saqlanadi.',
               'ru': 'Крупнейший глубоко-синий алмаз весом 45,52 карата; овеян легендами о зловещем проклятии, '
                     'постигавшем каждого его владельца со времён Людовика XIV.',
               'en': 'A 45.52-carat deep steely-blue gem mined in India, renowned for its legendary curse that '
                     'supposedly brought misfortune to its historic owners; displayed at the Smithsonian.'},
  'aliases': ['houp olmosi', 'brilliant houp', 'алмаз хоупа', 'алмаз надежды', 'hope diamond']},
 {'id': 'hist_art_080',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Faberje Ko'klam gullari tuxumi",
                     'Faberje Transsibir poyezdi tuxumi',
                     'Faberje Kreml tuxumi',
                     "Faberje imperatorlik 'Toj kiyish' tuxumi (1897 y.)"],
              'ru': ['Яйцо Фаберже «Весенние цветы»',
                     'Яйцо «Транссибирский экспресс»',
                     'Яйцо «Московский Кремль»',
                     'Императорское пасхальное яйцо Фаберже «Коронационное» (1897)'],
              'en': ['Fabergé Spring Flowers Egg',
                     'Fabergé Trans-Siberian Railway Egg',
                     'Fabergé Moscow Kremlin Egg',
                     'Fabergé Imperial Coronation Egg (1897)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Faberje imperatorlik 'Toj kiyish' tuxumi (1897 y.)",
                     'ru': 'Императорское пасхальное яйцо Фаберже «Коронационное» (1897)',
                     'en': 'Fabergé Imperial Coronation Egg (1897)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Imperial_Coronation_egg.jpg',
  'fun_fact': {'uz': 'Nikolay II va Aleksandra Fyodorovnaning toj kiyish marosimi sharafiga Peter Karl Faberje '
                     'tomonidan yasalgan bu oltin tuxum ichida qirolichaning oltin aravachasining kichik miniatyurasi '
                     'yashiringan.',
               'ru': 'Создано в 1897 году в честь коронации Николая II; внутри золотого яйца с желтой эмалью скрыта '
                     'миниатюрная копия коронационной кареты Екатерины II с открывающимися дверцами.',
               'en': 'Presented by Tsar Nicholas II to Empress Alexandra in 1897; contains a 7-cm miniature replica of '
                     "Catherine the Great's 1793 imperial coronation coach with rolling wheels and working doors."},
  'aliases': ['faberje tuxumi',
              'toj kiyish tuxumi',
              'яйцо фаберже',
              'коронационное яйцо',
              'faberge egg',
              'coronation egg']},
 {'id': 'hist_art_081',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Magna Carta (Buyuk erkinlik xartiyasi, 1215 y.)',
                     "Huquqlar to'g'risida bill",
                     'Oksford proviziyalari',
                     'Klarendon konstitutsiyasi'],
              'ru': ['Великая хартия вольностей (Magna Carta, 1215)',
                     'Билль о правах 1689 года',
                     'Оксфордские провизии',
                     'Кларендонские ассизы'],
              'en': ['Magna Carta (The Great Charter of 1215)',
                     'Bill of Rights 1689',
                     'Provisions of Oxford',
                     'Constitutions of Clarendon']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Magna Carta (Buyuk erkinlik xartiyasi, 1215 y.)',
                     'ru': 'Великая хартия вольностей (Magna Carta, 1215)',
                     'en': 'Magna Carta (The Great Charter of 1215)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ee/Magna_Carta_%28British_Library_Cotton_MS_Augustus_II.106%29.jpg',
  'fun_fact': {'uz': '1215 yilda Angliya qiroli Ioann Yersiz isyonkor baronlar bosimi ostida imzolagan ushbu lotincha '
                     'pergament konstitutsiyaviy qonun ustuvorligi va inson erkinliklarining poydevori hisoblanadi.',
               'ru': 'Подписана королём Иоанном Безземельным в Руннимеде под давлением мятежных баронов в 1215 году; '
                     'заложила фундамент верховенства закона и гражданских свобод.',
               'en': 'Agreed to by King John of England at Runnymede in 1215, this parchment charter established that '
                     'everyone, even the king, is subject to the rule of law.'},
  'aliases': ['magna carta', 'buyuk erkinlik xartiyasi', 'великая хартия вольностей', 'great charter']},
 {'id': 'hist_art_082',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Dharmazediy buyuk qo'ng'irog'i",
                     "Podsho qo'ng'irog'i (Tsar-kolokol, Moskva Kremli)",
                     "Min-gun qo'ng'irog'i",
                     "Yongle qo'ng'irog'i"],
              'ru': ['Колокол Дхаммазеди', 'Царь-колокол в Московском Кремле', 'Мингунский колокол', 'Колокол Юнлэ'],
              'en': ['Great Bell of Dhammazede',
                     'Tsar Bell (Tsar Kolokol, Moscow Kremlin)',
                     'Mingun Bell',
                     'Yongle Bell']},
  'correct_index': 1,
  'correct_answer': {'uz': "Podsho qo'ng'irog'i (Tsar-kolokol, Moskva Kremli)",
                     'ru': 'Царь-колокол в Московском Кремле',
                     'en': 'Tsar Bell (Tsar Kolokol, Moscow Kremlin)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/07/Tsar_Bell_in_the_Moscow_Kremlin_01.jpg',
  'fun_fact': {'uz': "1735 yilda quyilgan 200 tonnalik dunyodagi eng katta qo'ng'iroq; 1737 yilgi dahshatli Kreml "
                     "yong'inida sovuq suv sepilishi tufayli uning 11,5 tonnalik bo'lagi sinib tushgan va u biror "
                     'marta ham chalinmagan.',
               'ru': 'Отлит в 1735 году мастерами Моториными; весит свыше 200 тонн. Во время пожара 1737 года треснул '
                     'от воды, от него откололся 11,5-тонный кусок, так ни разу и не зазвонив.',
               'en': 'Cast in 1735 and weighing over 200 metric tons, this Kremlin bell cracked during a 1737 city '
                     'fire when cold water was poured on it, breaking off an 11.5-ton slab before it ever rang.'},
  'aliases': ['tsar kolokol', "podsho qo'ng'irog'i", 'царь-колокол', 'tsar bell']},
 {'id': 'hist_art_083',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Dardanell buyuk to'pi",
                     "Mons Meg to'pi",
                     "Podsho to'pi (Tsar-pushka, Andrey Choxov asari)",
                     "Faule Grete to'pi"],
              'ru': ['Дарданелльская пушка',
                     'Бомбарда Монс Мег',
                     'Царь-пушка в Московском Кремле (мастер Андрей Чохов)',
                     'Ленивая Грета'],
              'en': ['Dardanelles Gun', 'Mons Meg', 'Tsar Cannon (Tsar Pushka, Moscow Kremlin)', 'Faule Grete']},
  'correct_index': 2,
  'correct_answer': {'uz': "Podsho to'pi (Tsar-pushka, Andrey Choxov asari)",
                     'ru': 'Царь-пушка в Московском Кремле (мастер Андрей Чохов)',
                     'en': 'Tsar Cannon (Tsar Pushka, Moscow Kremlin)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Tsar_cannon_in_Moscow_Kremlin.jpg',
  'fun_fact': {'uz': "1586 yilda bronzadan quyilgan 39,3 tonnalik, kalibri 890 mm bo'lgan ushbu gigant to'p Ginnes "
                     "rekordlar kitobiga dunyodagi eng katta kalibrli bombardir to'p sifatida kiritilgan.",
               'ru': 'Отлита из бронзы в 1586 году русским мастером Андреем Чоховым; калибр орудия составляет '
                     'рекордные 890 мм, а масса ствола — 39,3 тонны.',
               'en': 'Cast in bronze in 1586 by master Andrey Chokhov; with an enormous bore caliber of 890 mm and '
                     'weighing 39.3 tons, it is the largest bombard by caliber in history.'},
  'aliases': ['tsar pushka', "podsho to'pi", 'царь-пушка', 'tsar cannon']},
 {'id': 'hist_art_084',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Knid Afroditasi',
                     'Kapitoliya Venerasi',
                     'Kallipiga Venerasi',
                     'Milos Venerasi (Afrodita haykali)'],
              'ru': ['Афродита Книдская',
                     'Венера Капитолийская',
                     'Венера Каллипига',
                     'Венера Милосская (Афродита с острова Милос)'],
              'en': ['Aphrodite of Knidos',
                     'Capitoline Venus',
                     'Venus Kallipygos',
                     'Venus de Milo (Aphrodite of Milos)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Milos Venerasi (Afrodita haykali)',
                     'ru': 'Венера Милосская (Афродита с острова Милос)',
                     'en': 'Venus de Milo (Aphrodite of Milos)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c2/Venus_de_Milo_Louvre_Ma399_n4.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 150-100 yillarda oq marmardan yaratilgan, qo'llari yo'qolgan bu go'zallik va "
                     "sevgi ma'budasi haykali 1820 yilda Milos orolida dehqon tomonidan topilgan va Luvrda turadi.",
               'ru': 'Древнегреческая мраморная статуя богини Афродиты около 130–100 гг. до н.э.; найдена в 1820 году '
                     'греческим крестьянином на острове Милос.',
               'en': 'Ancient Greek marble statue sculpted between 150 and 100 BC; discovered on the Aegean island of '
                     'Milos in 1820, its missing arms have fueled worldwide legend.'},
  'aliases': ['milos venerasi', 'afrodita', 'венера милосская', 'venus de milo']},
 {'id': 'hist_art_085',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Diskobol (Disk uloqtiruvchi atlet — Miron asari)',
                     "Dorifor (Nayza ko'targan jangchi)",
                     "Diadumen (Boshbog' taqqan yigit)",
                     'Apoksiomen (Kurakcha bilan tozalanuvchi atlet)'],
              'ru': ['«Дискобол» (античная статуя атлета работы Мирона)',
                     '«Дорифор» Поликлета',
                     '«Диадумен» Поликлета',
                     '«Апоксиомен» Лисиппа'],
              'en': ['Discobolus of Myron (The Discus Thrower)',
                     'Doryphoros of Polykleitos',
                     'Diadumenos',
                     'Apoxyomenos of Lysippos']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Diskobol (Disk uloqtiruvchi atlet — Miron asari)',
                     'ru': '«Дискобол» (античная статуя атлета работы Мирона)',
                     'en': 'Discobolus of Myron (The Discus Thrower)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/07/Discobolus_Lancellotti_Massimo_Inv126371.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi V asrda haykaltarosh Miron tomonidan yaratilgan bu asar jismoniy harakat '
                     'dinamikasini tosh va metallga muhrlagan antik davrning eng mashhur sport haykalidir.',
               'ru': 'Бронзовый оригинал V века до н.э. работы скульптора Мирона не сохранился, но дошёл в римских '
                     'мраморных копиях; эталон гармонии и движения в древнегреческом искусстве.',
               'en': 'Originally cast in bronze by Athenian sculptor Myron around 460-450 BC, this dynamic athletic '
                     'pose captured in mid-swing is the definitive icon of Olympic ideals.'},
  'aliases': ['diskobol', 'дискобол', 'discobolus', 'discus thrower', 'myron discobolus']},
 {'id': 'hist_art_086',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Borgeze gladiator haykali',
                     "O'layotgan gall jangchisi haykali (Kapitoliya g扰ali)",
                     'Jangchi Termi',
                     'Diskobol'],
              'ru': ['Боргезский борец',
                     '«Умирающий галл» (античная скульптура смертельно раненого кельта)',
                     'Кулачный боец (Термы)',
                     'Дискобол'],
              'en': ['Borghese Gladiator', 'The Dying Gaul (Capitoline Gaul)', 'Boxer at Rest', 'Discobolus']},
  'correct_index': 1,
  'correct_answer': {'uz': "O'layotgan gall jangchisi haykali (Kapitoliya g扰ali)",
                     'ru': '«Умирающий галл» (античная скульптура смертельно раненого кельта)',
                     'en': 'The Dying Gaul (Capitoline Gaul)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Dying_gaul.jpg',
  'fun_fact': {'uz': "Pergam shohi Attal I ning galatlar ustidan qozongan g'alabasini aks ettirgan bu haykalda yarador "
                     "kelt jangchisining bo'ynidagi tork (bo'yinbog') va qahramonona o'limi tasvirlangan.",
               'ru': 'Римская копия эллинистической бронзы III века до н.э. в память о победе царя Аттала I над '
                     'галатами; изображает умирающего кельтского воина с гривной (торком) на шее.',
               'en': 'Hellenistic marble copy of a Pergamon bronze commemorating victory over the Galatians; portrays '
                     'a mortally wounded Celtic warrior collapsing with dignity upon his shield.'},
  'aliases': ["o'layotgan gall", 'dying gaul', 'умирающий галл', 'capitoline gaul']},
 {'id': 'hist_art_087',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Laokoon guruhi',
                     'Farneze Gerkulesi',
                     'Farneze buqasi (Diktaning jazolanishi haykali)',
                     'Paskvino guruhi'],
              'ru': ['Лаокоон и сыновья',
                     'Геркулес Фарнезский',
                     '«Фарнезский бык» (Казнь Дирки, крупнейшая античная мраморная группа)',
                     'Группа Пасквино'],
              'en': ['Laocoon Group',
                     'Farnese Hercules',
                     'Farnese Bull (Punishment of Dirce Marble Group)',
                     'Pasquino Group']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Farneze buqasi (Diktaning jazolanishi haykali)',
                     'ru': '«Фарнезский бык» (Казнь Дирки, крупнейшая античная мраморная группа)',
                     'en': 'Farnese Bull (Punishment of Dirce Marble Group)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/14/Farnese_Bull_side_A_MAN_Napoli_Inv6002.jpg',
  'fun_fact': {'uz': "Neapol milliy arxeologiya muzeyida saqlanuvchi, yaxlit 24 tonnalik marmar bo'lagidan yo'nilgan "
                     'ushbu asar antik dunyodan saqlanib qolgan eng yirik yagona marmar haykaltaroshlik asaridir.',
               'ru': 'Высечена из единой глыбы мрамора весом 24 тонны; обнаружена в термах Каракаллы в 1546 году и '
                     'является самой массивной античной скульптурой, дошедшей до наших дней.',
               'en': 'Carved from a single colossal block of marble weighing 24 tons and excavated at the Baths of '
                     'Caracalla; the largest single intact sculpture recovering antiquity.'},
  'aliases': ['farneze buqasi', 'фарнезский бык', 'farnese bull']},
 {'id': 'hist_art_088',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Diskobol haykali',
                     'Damoksen haykali',
                     'Dorifor haykali',
                     'Borgeze gladiator haykali (Agasiy asari)'],
              'ru': ['Дискобол', 'Статуя Дамоксена', 'Дорифор', '«Боргезский боец» (скульптура воина работы Агасия)'],
              'en': ['Discobolus', 'Statue of Damoxenos', 'Doryphoros', 'Borghese Gladiator (Agasias of Ephesus)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Borgeze gladiator haykali (Agasiy asari)',
                     'ru': '«Боргезский боец» (скульптура воина работы Агасия)',
                     'en': 'Borghese Gladiator (Agasias of Ephesus)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Borghese_Gladiator_Louvre_Ma527_n2.jpg',
  'fun_fact': {'uz': 'Miloddan avvalgi 100 yillarga oid Efeslik Agasiy tomonidan ishlangan bu asar aslida gladiator '
                     "emas, balki chap qo'lidagi qalqon bilan otliq jangchiga qarshi himoyalanayotgan jangchini "
                     'tasvirlaydi.',
               'ru': 'Эллинистическая мраморная статуя около 100 г. до н.э.; изображает не римского гладиатора, а '
                     'пешего греческого воина, отражающего нападение конника.',
               'en': "Signed by Agasias of Ephesus around 100 BC; despite its 17th-century nickname 'Gladiator', it "
                     'actually depicts an infantry swordsman lunging with shield against cavalry.'},
  'aliases': ['borgeze gladiatori',
              'borgeze kurashchisi',
              'боргезский боец',
              'боргезский гладиатор',
              'borghese gladiator']},
 {'id': 'hist_art_089',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Avliyo Mark qanotli arsloni (Venetsiya ramzi)', 'Piza grifoni', 'Brunsvik arsloni', 'Lakon iti'],
              'ru': ['Крылатый лев святого Марка (бронзовый символ Венеции)',
                     'Пизанский грифон',
                     'Брауншвейгский лев',
                     'Молосский пёс'],
              'en': ['Lion of Saint Mark (Winged Bronze Lion of Venice)',
                     'Pisa Griffin',
                     'Brunswick Lion',
                     'Molossian Hound']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Avliyo Mark qanotli arsloni (Venetsiya ramzi)',
                     'ru': 'Крылатый лев святого Марка (бронзовый символ Венеции)',
                     'en': 'Lion of Saint Mark (Winged Bronze Lion of Venice)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/69/Lion_of_Venice_Piazza_San_Marco.jpg',
  'fun_fact': {'uz': 'Venetsiyadagi San-Marko maydonidagi granit ustun ustida turgan bu qadimiy bronza arslon aslida '
                     "mil. avv. IV asrga oid ellinistik yoki sharqona sher-grifon haykali bo'lgan deb taxmin qilinadi.",
               'ru': 'Античная бронзовая статуя, возвышающаяся на колонне площади Сан-Марко в Венеции; вероятно '
                     'происходит из эллинистической Сирии или Киликии.',
               'en': "Perched atop a granite column in Saint Mark's Square, Venice; modern metallurgical analysis "
                     'suggests it was originally cast in the 4th century BC in the Hellenistic Levant.'},
  'aliases': ['venetsiya arsloni',
              'avliyo mark arsloni',
              'лев святого марка',
              'венецианский лев',
              'lion of saint mark',
              'venetian lion']},
 {'id': 'hist_art_090',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Piza sobori eshiklari',
                     '«Jannat darvozalari» (Lorentso Giberti bronza eshigi, Florensiya)',
                     'Verona San-Dzeno eshigi',
                     "Rodenning «Do'zax darvozalari»"],
              'ru': ['Двери собора в Пизе',
                     '«Врата рая» (бронзовые двери баптистерия во Флоренции, Лоренцо Гиберти)',
                     'Бронзовые двери Сан-Дзено',
                     '«Врата ада» Огюста Родена'],
              'en': ['Pisa Cathedral Bronze Doors',
                     'Gates of Paradise (Lorenzo Ghiberti, Florence Baptistery)',
                     'San Zeno Bronze Doors',
                     'The Gates of Hell by Rodin']},
  'correct_index': 1,
  'correct_answer': {'uz': '«Jannat darvozalari» (Lorentso Giberti bronza eshigi, Florensiya)',
                     'ru': '«Врата рая» (бронзовые двери баптистерия во Флоренции, Лоренцо Гиберти)',
                     'en': 'Gates of Paradise (Lorenzo Ghiberti, Florence Baptistery)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/64/Porta_del_Paradiso_originale_Ghiberti.jpg',
  'fun_fact': {'uz': 'Florensiya baptisteriyasi uchun 1425-1452 yillarda yasalgan 10 ta zarhal bronza relyef panelini '
                     "ko'rgan Mikelanjelo: 'Bu eshiklar shunchalik go'zalki, hatto Jannat eshigi bo'lishga munosib' "
                     'deb aytgan.',
               'ru': 'Создавались Гиберти на протяжении 27 лет; Микеланджело воскликнул, что они столь великолепны, '
                     'что достойны служить вратами Рая.',
               'en': 'Created by Lorenzo Ghiberti between 1425 and 1452; Michelangelo declared the gilded relief '
                     'panels so sublime that they were worthy to stand as the Gates of Paradise.'},
  'aliases': ['jannat darvozalari', 'giberti eshiklari', 'врата рая', 'гиберти', 'gates of paradise', 'ghiberti']},
 {'id': 'hist_art_091',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Avliyo Moris relikvariysi',
                     "Karl Buyuk barmog'i",
                     'Avliyo Fua oltin relikvariy haykali (Konk, Fransiya)',
                     'Aaxen relikvariysi'],
              'ru': ['Реликварий святого Маврикия',
                     'Бюст Карла Великого',
                     'Золотой реликварий святой Веры (Сент-Фуа в Конке)',
                     'Аахенский реликварий'],
              'en': ['Reliquary of Saint Maurice',
                     'Bust of Charlemagne',
                     'Reliquary Statue of Saint Foy (Conques, France)',
                     'Aachen Reliquary']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Avliyo Fua oltin relikvariy haykali (Konk, Fransiya)',
                     'ru': 'Золотой реликварий святой Веры (Сент-Фуа в Конке)',
                     'en': 'Reliquary Statue of Saint Foy (Conques, France)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Statue_reliquaire_Sainte_Foy_Conques.jpg',
  'fun_fact': {'uz': "X asrga oid ushbu yog'och asosga tilla qoplab, qadimgi Rim kameyasi va yuzlab qimmatbaho "
                     "javohirlar bilan bezatilgan haykal o'rta asrlarda ziyoratchilar uchun mo''jizakor maskan "
                     "bo'lgan.",
               'ru': 'Шедевр каролингского и романского золотого дела X века в аббатстве Конк; инкрустирован античными '
                     'камеями, драгоценными камнями и хранит мощи мученицы.',
               'en': '10th-century gold and gemstone encrusted wooden statue preserving the skull of child martyr '
                     'Saint Foy; one of the few surviving monumental medieval reliquary statues.'},
  'aliases': ['avliyo fua', 'sainte foy', 'реликварий святой веры', 'сент-фуа', 'reliquary of saint foy']},
 {'id': 'hist_art_092',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Sens billuri',
                     'Sent-Deni billuri',
                     'Eshbern billur qadahi',
                     "Lotar billur medalyoni (Susanna tarixi o'yilgan kvars)"],
              'ru': ['Хрусталь из Санса',
                     'Хрусталь Сен-Дени',
                     'Кубок из горного хрусталя',
                     'Кристалл Лотаря (каролингский резной горный хрусталь)'],
              'en': ['Sens Crystal',
                     'Saint-Denis Crystal',
                     'Ashburnham Rock Crystal',
                     'Lothair Crystal (Carved Rock Crystal of King Lothair II)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Lotar billur medalyoni (Susanna tarixi o'yilgan kvars)",
                     'ru': 'Кристалл Лотаря (каролингский резной горный хрусталь)',
                     'en': 'Lothair Crystal (Carved Rock Crystal of King Lothair II)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Lothair_Crystal_BM_1855%2C1201.1.jpg',
  'fun_fact': {'uz': "IX asr o'rtalarida Lotaringiya qiroli Lotar II buyrug'i bilan tog' billuriga (kvars) intaglio "
                     "uslubida o'yib ishlangan ushbu medalyonda Injildagi begunoh Susanna tarixi aks etgan.",
               'ru': 'Диск из горного хрусталя IX века с вырезанными 8 сценами ветхозаветной истории о Сусанне и '
                     'старцах; создан для каролингского короля Лотаря II.',
               'en': 'Carved from rock crystal in 9th-century Lotharingia, depicting the Biblical story of Susanna in '
                     'eight engraved scenes; made for King Lothair II.'},
  'aliases': ['lotar billuri', 'кристалл лотаря', 'lothair crystal']},
 {'id': 'hist_art_093',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Buyuk Alfred taqinchog'i (Anglo-sakson emal va billur durdonasi)",
                     'Fuller broshi',
                     'Kingston broshi',
                     "Kopland taqinchog'i"],
              'ru': ['Драгоценность короля Альфреда Великого',
                     'Брошь Фуллера',
                     'Кингстонская брошь',
                     'Пендант из Копленда'],
              'en': ['Alfred Jewel (Anglo-Saxon Gold and Enamel Ornament)',
                     'Fuller Brooch',
                     'Kingston Brooch',
                     'Copland Pendant']},
  'correct_index': 0,
  'correct_answer': {'uz': "Buyuk Alfred taqinchog'i (Anglo-sakson emal va billur durdonasi)",
                     'ru': 'Драгоценность короля Альфреда Великого',
                     'en': 'Alfred Jewel (Anglo-Saxon Gold and Enamel Ornament)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4e/AlfredJewel_Ashmolean_AN1836p135-269.jpg',
  'fun_fact': {'uz': "IX asr oxirida yasalgan va qirrasida 'AELFRED MEC HEHT GEWYRCAN' (Alfred meni yasashni buyurdi) "
                     "deb yozilgan bu qimmatbaho buyum kitob o'qishda ko'rsatkich sifatida xizmat qilgan.",
               'ru': 'Создана в конце IX века по заказу короля Альфреда Великого; служила рукоятью указки для чтения '
                     'священных книг (эстела); хранится в Оксфорде.',
               'en': "Inscribed 'AELFRED MEC HEHT GEWYRCAN' (Alfred ordered me to be made), this 9th-century gold and "
                     'cloisonné enamel artifact was the handle of a pointer for reading books.'},
  'aliases': ["alfred taqinchog'i", 'buyuk alfred', 'драгоценность альфреда', 'alfred jewel']},
 {'id': 'hist_art_094',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Tollund odami', 'Lindou odami (Temir davri botqoq mumiyasi)', 'Grauballe odami', 'Yelling odami'],
              'ru': ['Человек из Толлунда',
                     'Человек из Линдоу (болотное тело железного века, Англия)',
                     'Человек из Гроболла',
                     'Человек из Эллинга'],
              'en': ['Tollund Man', 'Lindow Man (Iron Age Bog Body, England)', 'Grauballe Man', 'Elling Woman']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Lindou odami (Temir davri botqoq mumiyasi)',
                     'ru': 'Человек из Линдоу (болотное тело железного века, Англия)',
                     'en': 'Lindow Man (Iron Age Bog Body, England)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/41/Lindow_man_british_museum.jpg',
  'fun_fact': {'uz': "1984 yilda Cheshir botqog'idan torf qazib olish paytida topilgan milodiy I asrga oid bu kelt "
                     'yigitining jasadi torf kislotasi va kislorodsizlik sababli 2000 yil sochi va tirnoqlarigacha '
                     'aynimasdan saqlangan.',
               'ru': 'Обнаружен в торфяном болоте в графстве Чешир в 1984 году; благодаря торфяному дублению '
                     'превосходно сохранились кожа, борода и последняя трапеза кельтского воина.',
               'en': 'Preserved in peat moss since the 1st century AD in Cheshire, England; peat chemistry preserved '
                     'his skin, trimmed beard, and fingernails, revealing evidence of three-fold ritual sacrifice.'},
  'aliases': ['lindou odami', 'человек из линдоу', 'линдоу', 'lindow man']},
 {'id': 'hist_art_095',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Lindou odami',
                     'Grauballe odami',
                     "Tollund odami (Daniya botqoq mo''jizasi, mil. avv. IV asr)",
                     'Boksten odami'],
              'ru': ['Человек из Линдоу',
                     'Человек из Гроболла',
                     'Человек из Толлунда (болотная мумия IV века до н.э., Дания)',
                     'Человек из Бокстена'],
              'en': ['Lindow Man', 'Grauballe Man', 'Tollund Man (4th-century BC Bog Body, Denmark)', 'Bocksten Man']},
  'correct_index': 2,
  'correct_answer': {'uz': "Tollund odami (Daniya botqoq mo''jizasi, mil. avv. IV asr)",
                     'ru': 'Человек из Толлунда (болотная мумия IV века до н.э., Дания)',
                     'en': 'Tollund Man (4th-century BC Bog Body, Denmark)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Tollundmanden.jpg',
  'fun_fact': {'uz': "1950 yilda Daniyaning Yutlandiya botqog'idan topilganida yuzi shunchalik xotirjam va tirikdek "
                     "saqlanganki, mahalliy politsiya uni yaqinda o'ldirilgan odam deb o'ylab tergov boshlagan.",
               'ru': 'Мумия возрастом более 2300 лет с настолько живыми и умиротворёнными чертами лица, что нашедшие '
                     'её датские торфокопы вызвали полицию, приняв за недавнюю жертву убийства.',
               'en': 'Discovered in 1950 in a Danish peat bog; his facial features from the 4th century BC are so '
                     'serene and impeccably preserved that discoverers called the police thinking it was a recent '
                     'murder.'},
  'aliases': ['tollund odami', 'tollund', 'человек из толлунда', 'толлунд', 'tollund man']},
 {'id': 'hist_art_096',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Neolit chaqmoqtosh boltasi',
                     'Bronza boltasi',
                     'Temir davri chopqisi',
                     "O'tsi muz odamining mis boltasi (Eneolit davri, mil. avv. 3300 y.)"],
              'ru': ['Кремнёвый топор из Спиенн',
                     'Кельтский бронзовый кельт',
                     'Железный топор викинга',
                     'Медный топор ледяного человека Этци (энеолит, ок. 3300 до н.э.)'],
              'en': ['Spiennes Flint Axe',
                     'Bronze Palstave Axe',
                     'Viking Bearded Axe',
                     'Copper Axe of Ötzi the Iceman (Chalcolithic, c. 3300 BC)']},
  'correct_index': 3,
  'correct_answer': {'uz': "O'tsi muz odamining mis boltasi (Eneolit davri, mil. avv. 3300 y.)",
                     'ru': 'Медный топор ледяного человека Этци (энеолит, ок. 3300 до н.э.)',
                     'en': 'Copper Axe of Ötzi the Iceman (Chalcolithic, c. 3300 BC)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Kupferbeil_Oetzi.jpg',
  'fun_fact': {'uz': "1991 yilda Alp tog'lari muzligidan topilgan 5300 yillik qadimgi muz odami O'tsining ushbu "
                     "boltasi 99,7 foiz toza misdan quyilgan bo'lib, tarixdagi eng qadimgi to'liq saqlangan yog'och "
                     'dasta va charm tasmali boltadir.',
               'ru': 'Единственный полностью сохранившийся доисторический топор из 99,7% чистой меди с тисовой '
                     'рукоятью и кожаными ремнями возрастом свыше 5300 лет.',
               'en': 'Carried by the 5,300-year-old alpine mummy Ötzi, this is the only prehistoric copper axe '
                     'preserved completely intact with its yew-wood haft and leather lashings.'},
  'aliases': ["o'tsi boltasi", "o'tsi", 'топор этци', 'ледяной человек этци', 'otzi axe', 'oetzi axe']},
 {'id': 'hist_art_097',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Silla podsholigi oltin toji (Koreya milliy durdonasi)',
                     'Bekje qiroli toji',
                     'Koguryo toj bezagi',
                     'Goryo zarhal toji'],
              'ru': ['Золотая корона королевства Силла (Кёнчжу, Корея)',
                     'Корона правителя Пэкче',
                     'Корона Когурё',
                     'Корона Корё'],
              'en': ['Gold Crown of Silla (Gyeongju, Korea)',
                     'Baekje Diadem',
                     'Goguryeo Headdress',
                     'Goryeo Gilded Crown']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Silla podsholigi oltin toji (Koreya milliy durdonasi)',
                     'ru': 'Золотая корона королевства Силла (Кёнчжу, Корея)',
                     'en': 'Gold Crown of Silla (Gyeongju, Korea)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/23/Gold_crown_from_Hwangnamdaechong_Gyeongju.jpg',
  'fun_fact': {'uz': 'V-VI asrlarga oid Koreyaning Kyonju shahridagi ulkan qabrlardan topilgan bu toj daraxt shoxlari '
                     "va bug'u shoxlari shaklidagi sof oltin plitalar hamda osilgan nefrit (magatama) munchoqlari "
                     'bilan yasalgan.',
               'ru': 'Изготовлена в V–VI веках из золотых ветвей в форме священного древа жизни с нефритовыми '
                     'подвесками-гогок; символ шаманской и царской власти правителей Силла.',
               'en': 'Excavated from 5th-6th century royal tumuli in Gyeongju; features stylized tree-and-antler '
                     'shaped gold branches adorned with comma-shaped green jade jewels (gogok).'},
  'aliases': ['silla toji',
              'silla oltin toji',
              'корона силла',
              'золотая корона силла',
              'silla crown',
              'gold crown of silla']},
 {'id': 'hist_art_098',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Kusanagi afsonaviy qilichi',
                     'Yetti shoxli qilich (Chiljido — Bekje qirolligi tuhfasi)',
                     'Goujian qilichi',
                     'Silla qilichi'],
              'ru': ['Меч Кусанаги',
                     'Семизубый меч («Чхильчидо» — клинок царства Пэкче)',
                     'Меч Гоуцзяня',
                     'Меч правителя Силла'],
              'en': ['Kusanagi Sword',
                     'Seven-Branched Sword (Chiljido of Baekje)',
                     'Sword of Goujian',
                     'Silla Double-edged Sword']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Yetti shoxli qilich (Chiljido — Bekje qirolligi tuhfasi)',
                     'ru': 'Семизубый меч («Чхильчидо» — клинок царства Пэкче)',
                     'en': 'Seven-Branched Sword (Chiljido of Baekje)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Seven-Branched_Sword.jpg',
  'fun_fact': {'uz': 'Milodiy 369 yilda Bekje qiroli tomonidan Yaponiya hukmdoriga hadya qilingan 6 ta yon novdasi '
                     "bo'lgan bu g'aroyib temir qilichga oltin harflar bilan 61 ta iyeroglif bitilgan bo'lib, Nara "
                     'ibodatxonasida saqlanadi.',
               'ru': 'Железный меч IV века с шестью ответвлениями и золотой надписью из 61 знака; дипломатический дар '
                     'корейского монарха правителю древней Японии Ямато.',
               'en': 'Forged in 369 AD with six branching wave-like protrusions and 61 gold-inlaid characters; gifted '
                     'by the King of Baekje to the ruler of Yamato Japan, preserved at Isonokami Shrine.'},
  'aliases': ['yetti shoxli qilich',
              'chiljido',
              'семизубый меч',
              'чхильчидо',
              'seven-branched sword',
              'seven branched sword']},
 {'id': 'hist_art_099',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ["Muramasa la'nati qilichi",
                     'Kogarasu Maru',
                     'Xonjo Masamune samuray katanasi (Yaponiya afsonaviy qilichi)',
                     'Kotetsu qilichi'],
              'ru': ['Клинок Мурамасы',
                     'Когарасу Мару',
                     'Хондзё Масамунэ (легендарный японский меч-катана)',
                     'Меч Котэцу'],
              'en': ['Muramasa Katana',
                     'Kogarasu Maru',
                     'Honjo Masamune Katana (Legendary Japanese Sword)',
                     'Kotetsu Sword']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Xonjo Masamune samuray katanasi (Yaponiya afsonaviy qilichi)',
                     'ru': 'Хондзё Масамунэ (легендарный японский меч-катана)',
                     'en': 'Honjo Masamune Katana (Legendary Japanese Sword)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Masamune_tanto.jpg',
  'fun_fact': {'uz': 'XIII-XIV asrlar buyuk yapon ustasi Goro Nyudo Masamune tomonidan soxta qilingan va Tokugava '
                     "syogunlarining rasmiy ramzi bo'lgan bu tengsiz qilich 1945 yilda sirli tarzda g'oyib bo'lgan.",
               'ru': 'Выкован величайшим мечником Японии Масамунэ в начале XIV века; веками передавался от сёгуна к '
                     'сёгуну клана Токугава, но бесследно исчез в декабре 1945 года.',
               'en': 'Forged by master smith Goro Nyudo Masamune in the 14th century, representing the shogunate power '
                     'of the Tokugawa clan; mysteriously lost at the end of World War II in 1945.'},
  'aliases': ['masamune', 'xonjo masamune', 'масамунэ', 'хондзё масамунэ', 'honjo masamune', 'masamune katana']},
 {'id': 'hist_art_100',
  'sub_mode': 'artifacts',
  'question': {'uz': 'Suratda tasvirlangan mashhur qadimiy artefakt / arxeologik yodgorlik qanday nomlanadi?',
               'ru': 'Как называется знаменитый древний артефакт или археологический памятник на фото?',
               'en': 'What is the name of the famous ancient artifact or archaeological relic shown in the photo?'},
  'options': {'uz': ['Oksirinx papiruslari',
                     'Elephantina papiruslari',
                     "Herculaneum ko'mir papirusi",
                     "Derveni papirusi (Yevropadagi eng qadimiy saqlangan qo'lyozma)"],
              'ru': ['Оксиринхские папирусы',
                     'Элефантинские папирусы',
                     'Папирусы из Геркуланума',
                     'Папирус из Дервени (древнейшая сохранившаяся рукопись в Европе)'],
              'en': ['Oxyrhynchus Papyri',
                     'Elephantine Papyri',
                     'Herculaneum Papyri',
                     "Derveni Papyrus (Europe's Oldest Surviving Manuscript)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Derveni papirusi (Yevropadagi eng qadimiy saqlangan qo'lyozma)",
                     'ru': 'Папирус из Дервени (древнейшая сохранившаяся рукопись в Европе)',
                     'en': "Derveni Papyrus (Europe's Oldest Surviving Manuscript)"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Derveni_papyrus.jpg',
  'fun_fact': {'uz': "Miloddan avvalgi 340 yillarga oid kuygan bu o'ram 1962 yilda Saloniki yaqinidagi qabrdan "
                     "topilgan bo'lib, unda qadimgi yunon orfik diniy va falsafiy ta'limotlari bitilgan.",
               'ru': 'Обугленный папирус IV века до н.э., найденный в погребальном костре близ Салоник в Греции; '
                     'древнейший дошедший до наших дней европейский рукописный текст.',
               'en': 'Carbonized scroll discovered in 1962 near Thessaloniki, dated to c. 340 BC; containing '
                     "philosophical commentary on an Orphic theogony, it is Europe's oldest surviving manuscript."},
  'aliases': ['derveni papirusi', 'derveni', 'папирус из дервени', 'derveni papyrus']}]

HISTORY_QUESTIONS: List[Dict[str, Any]] = HISTORY_DATA

HISTORY_BY_ID: Dict[str, Dict[str, Any]] = {item["id"]: item for item in HISTORY_DATA}
HISTORY_BY_SUBMODE: Dict[str, List[Dict[str, Any]]] = {}
for item in HISTORY_DATA:
    HISTORY_BY_SUBMODE.setdefault(item["sub_mode"], []).append(item)
HISTORY_BY_SUB_MODE = HISTORY_BY_SUBMODE


def get_history_item_by_id(item_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a history trivia item by its unique ID."""
    return HISTORY_BY_ID.get(item_id)


def get_history_question_by_id(question_id: str) -> Optional[Dict[str, Any]]:
    """Alias for get_history_item_by_id."""
    return get_history_item_by_id(question_id)


def get_history_items_by_submode(sub_mode: str) -> List[Dict[str, Any]]:
    """Retrieve all history items for a specific sub-mode."""
    return HISTORY_BY_SUBMODE.get(sub_mode, [])


def get_history_questions_by_submode(sub_mode: str) -> List[Dict[str, Any]]:
    """Alias for get_history_items_by_submode."""
    return get_history_items_by_submode(sub_mode)


def get_random_history_items(count: int = 1, sub_mode: Optional[str] = None) -> List[Dict[str, Any]]:
    """Sample random history items without replacement, optionally filtered by sub-mode."""
    pool = HISTORY_BY_SUBMODE.get(sub_mode, HISTORY_DATA) if sub_mode else HISTORY_DATA
    if not pool:
        return []
    return random.sample(pool, min(count, len(pool)))


def get_random_history_questions(count: int = 1, sub_mode: Optional[str] = None) -> List[Dict[str, Any]]:
    """Alias for get_random_history_items."""
    return get_random_history_items(count, sub_mode)


def search_history_by_alias(query: str) -> List[Dict[str, Any]]:
    """Search history items by alias or name match."""
    q = query.lower().strip()
    results = []
    for item in HISTORY_DATA:
        if any(q in alias for alias in item["aliases"]):
            results.append(item)
            continue
        for lang in ["uz", "ru", "en"]:
            if q in item["correct_answer"][lang].lower():
                results.append(item)
                break
    return results
