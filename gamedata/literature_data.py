# -*- coding: utf-8 -*-
"""
GeoGuru Game Dataset: Literature, World & Uzbek Classics, Poetry & Epics.
Contains 400 rich multilingual questions across 4 engaging sub-modes:
1. quotes (100 items): Famous quotes from world and Uzbek literary masterpieces.
2. book_emojis (100 items): Emoji riddles deciphering iconic novels and epics.
3. authors (100 items): Identifying legendary authors and poets from portraits.
4. characters (100 items): Identifying iconic literary protagonists and figures from 3 progressive clues.
"""
import random
from typing import Optional, List, Dict, Any

LITERATURE_DATA: List[Dict[str, Any]] = [{'id': 'lit_q_001',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Bo'lmoq yo bo'lmaslik — mana masala!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Быть или не быть, вот в чём вопрос...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'To be, or not to be, that is the question...'"},
  'options': {'uz': ['Uilyam Shekspir («Hamlet»)',
                     'Uilyam Shekspir («Otello»)',
                     'Uilyam Shekspir («Qirol Lir»)',
                     'Uilyam Shekspir («Makbet»)'],
              'ru': ['Уильям Шекспир («Гамлет»)',
                     'Уильям Шекспир («Отелло»)',
                     'Уильям Шекспир («Король Лир»)',
                     'Уильям Шекспир («Макбет»)'],
              'en': ["William Shakespeare ('Hamlet')",
                     "William Shakespeare ('Othello')",
                     "William Shakespeare ('King Lear')",
                     "William Shakespeare ('Macbeth')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Uilyam Shekspir («Hamlet»)',
                     'ru': 'Уильям Шекспир («Гамлет»)',
                     'en': "William Shakespeare ('Hamlet')"},
  'image_url': None,
  'fun_fact': {'uz': "Shekspirning «Hamlet» tragediyasidagi ushbu monolog shahzoda Hamlet tomonidan hayot va o'lim, "
                     "kurash va taslim bo'lish haqida aytiladi.",
               'ru': 'Знаменитый монолог принца датского Гамлета в третьем акте пьесы Шекспира — один из самых '
                     'цитируемых в мировой драматургии.',
               'en': "Prince Hamlet's soliloquy in Act 3 of Shakespeare's tragedy contemplates mortality and the "
                     'painful uncertainty of existence.'},
  'aliases': ['hamlet', 'shekspir', 'гамлет', 'быть или не быть', 'to be or not to be', 'shakespeare']},
 {'id': 'lit_q_002',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Barcha baxtli oilalar bir-biriga o'xshaydi, har bir baxtsiz oila esa o'zicha baxtsizdir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'All happy families are alike; each unhappy family is unhappy in its own way.'"},
  'options': {'uz': ['Lev Tolstoy («Urush va tinchlik»)',
                     'Lev Tolstoy («Anna Karenina»)',
                     'Fyodor Dostoevskiy («Idiot»)',
                     'Ivan Turgenev («Otalar va bolalar»)'],
              'ru': ['Лев Толстой («Война и мир»)',
                     'Лев Толстой («Анна Каренина»)',
                     'Фёдор Достоевский («Идиот»)',
                     'Иван Тургенев («Отцы и дети»)'],
              'en': ["Leo Tolstoy ('War and Peace')",
                     "Leo Tolstoy ('Anna Karenina')",
                     "Fyodor Dostoevsky ('The Idiot')",
                     "Ivan Turgenev ('Fathers and Sons')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Lev Tolstoy («Anna Karenina»)',
                     'ru': 'Лев Толстой («Анна Каренина»)',
                     'en': "Leo Tolstoy ('Anna Karenina')"},
  'image_url': None,
  'fun_fact': {'uz': 'Lev Tolstoyning «Anna Karenina» romani aynan shu jumlalar bilan boshlanadi va bu ibora falsafada '
                     "'Anna Karenina tamoyili' deb ataladi.",
               'ru': 'Первая фраза романа Льва Толстого «Анна Каренина» (1878) стала афоризмом и дала название '
                     '«принципу Анны Карениной».',
               'en': "The iconic opening line of Tolstoy's 1878 masterpiece formulated what scientists and "
                     "sociologists call the 'Anna Karenina principle'."},
  'aliases': ['anna karenina', 'tolstoy', 'анна каренина', 'толстой', 'happy families']},
 {'id': 'lit_q_003',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Odamiy ersang, demagil odami,\n'
                     "Onikim, yo'q xalq g'amidin g'ami.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Если ты человек — не зови человеком того,\n'
                     'Кто не знает печали о благе народа своего.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'If thou art human, call not him a man,\n"
                     "Who knows no sorrow for his fellow clan.'"},
  'options': {'uz': ['Zahiriddin Muhammad Bobur («Boburnoma»)',
                     'Jaloliddin Rumiy («Masnaviy»)',
                     'Alisher Navoiy («Hayrat ul-abror»)',
                     "Sa'diy Sheroziy («Guliston»)"],
              'ru': ['Захириддин Мухаммад Бабур («Бабур-наме»)',
                     'Джалаладдин Руми («Маснави»)',
                     'Алишер Навои («Смятение праведных»)',
                     'Саади Ширази («Гулистан»)'],
              'en': ["Babur ('Baburnama')",
                     "Jalaluddin Rumi ('Masnavi')",
                     "Alisher Navoi ('Hayrat al-Abrar')",
                     "Saadi Shirazi ('Gulistan')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Alisher Navoiy («Hayrat ul-abror»)',
                     'ru': 'Алишер Навои («Смятение праведных»)',
                     'en': "Alisher Navoi ('Hayrat al-Abrar')"},
  'image_url': None,
  'fun_fact': {'uz': 'Alisher Navoiyning mashhur «Xamsa»sining birinchi dostoni «Hayrat ul-abror»dan olingan bu bayt '
                     'gumanistik tamoyilning oliy ifodasidir.',
               'ru': 'Бессмертное двустишие Алишера Навои из первой поэмы «Хамсы» («Пятерицы») призывает к истинному '
                     'состраданию и служению народу.',
               'en': "Penned by Chagatai poet Alisher Navoi in 1483 in 'Hayrat al-Abrar', this couplet stands as the "
                     'golden rule of humanitarian empathy.'},
  'aliases': ['alisher navoiy', 'navoiy', 'hayrat ul-abror', 'алишер навои', 'навои', 'odamiy ersang']},
 {'id': 'lit_q_004',
  'sub_mode': 'quotes',
  'question': {'uz': "Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n\n«Ulkan Og'a seni kuzatmoqda!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n\n«Большой Брат следит за тобой!»',
               'en': "Which work or author is the source of this famous quote?\n\n'Big Brother is Watching You!'"},
  'options': {'uz': ['Oldos Xaksli («Ajib yangi dunyo»)',
                     "Rey Bredberi («Farengeyt bo'yicha 451 daraja»)",
                     'Yevgeniy Zamyatin («Biz»)',
                     'Jorj Oruell («1984»)'],
              'ru': ['Олдос Хаксли («О дивный новый мир»)',
                     'Рэй Брэдбери («451 градус по Фаренгейту»)',
                     'Евгений Замятин («Мы»)',
                     'Джордж Оруэлл («1984»)'],
              'en': ["Aldous Huxley ('Brave New World')",
                     "Ray Bradbury ('Fahrenheit 451')",
                     "Yevgeny Zamyatin ('We')",
                     "George Orwell ('1984')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jorj Oruell («1984»)', 'ru': 'Джордж Оруэлл («1984»)', 'en': "George Orwell ('1984')"},
  'image_url': None,
  'fun_fact': {'uz': 'Oruellning 1949 yilda yozilgan antiutopik «1984» romanida totalitarizm va ommaviy nazorat ramzi '
                     "bo'lgan partiya dohiysi 'Ulkan Og'a' tasvirlanadi.",
               'ru': 'Лозунг тоталитарной партии Океании из романа-антиутопии Джорджа Оруэлла «1984» стал '
                     'нарицательным символом всевидящего государственного контроля.',
               'en': "The terrifying slogan from Orwell's dystopian masterpiece '1984' has entered global culture to "
                     'describe pervasive surveillance.'},
  'aliases': ['1984', 'oruell', 'orwell', "katta og'a", 'большой брат', 'big brother']},
 {'id': 'lit_q_005',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Sen o'zing qo'lga o'rgatgan har bir jonzot uchun butun umr javobgarsan.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Ты навсегда в ответе за всех, кого приручил.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'You become responsible, forever, for what you have tamed.'"},
  'options': {'uz': ['Antuan de Sent-Ekzyuperi («Kichkina shahzoda»)',
                     'Richard Bax («Jonatan Livingston ismli oqcharloq»)',
                     'Jyul Vern («Sirli orol»)',
                     'Astrid Lindgren («Mittivoy va Karlson»)'],
              'ru': ['Антуан де Сент-Экзюпери («Маленький принц»)',
                     'Ричард Бах («Чайка по имени Джонатан Ливингстон»)',
                     'Жюль Верн («Таинственный остров»)',
                     'Астрид Линдгрен («Малыш и Карлсон»)'],
              'en': ["Antoine de Saint-Exupéry ('The Little Prince')",
                     "Richard Bach ('Jonathan Livingston Seagull')",
                     "Jules Verne ('The Mysterious Island')",
                     "Astrid Lindgren ('Karlsson-on-the-Roof')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Antuan de Sent-Ekzyuperi («Kichkina shahzoda»)',
                     'ru': 'Антуан де Сент-Экзюпери («Маленький принц»)',
                     'en': "Antoine de Saint-Exupéry ('The Little Prince')"},
  'image_url': None,
  'fun_fact': {'uz': "Tulki Kichkina shahzodaga do'stlik mas'uliyatini tushuntirganda aynan shu dono gapni aytadi.",
               'ru': 'Эти слова произносит Лис в философской сказке Экзюпери, раскрывая тайну верности и дружбы.',
               'en': 'The Fox explains this profound truth to the Little Prince on asteroid B-612 regarding love and '
                     'duty.'},
  'aliases': ['kichkina shahzoda', 'ekzyuperi', 'маленький принц', 'экзюпери', 'little prince']},
 {'id': 'lit_q_006',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Modomiki, biz yangi davrga oyoq qo'ydik, bas, biz har bir yo'sunda ham shu yangi davrning "
                     "yangiliklari ketidan ergashmog'imiz... lozimdir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Поскольку мы вступили в новую эпоху, то нам надлежит во всех отношениях следовать новым веяниям '
                     'времени...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Since we have stepped into a new era, we must pursue modern renewals in every possible way...'"},
  'options': {'uz': ["Abdulhamid Cho'lpon («Kecha va kunduz»)",
                     "Abdulla Qodiriy («O'tkan kunlar» romani muqaddimasi)",
                     'Abdurauf Fitrat («Qiyomat»)',
                     "Oybek («Qutlug' qon»)"],
              'ru': ['Абдулхамид Чулпан («Ночь и день»)',
                     'Абдулла Кадыри (предисловие к роману «Минувшие дни»)',
                     'Абдурауф Фитрат («Судный день»)',
                     'Айбек («Священная кровь»)'],
              'en': ["Abdulhamid Cholpon ('Night and Day')",
                     "Abdulla Qadiri (preface to 'Bygone Days')",
                     "Abdurauf Fitrat ('Judgment Day')",
                     "Oybek ('Sacred Blood')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Abdulla Qodiriy («O'tkan kunlar» romani muqaddimasi)",
                     'ru': 'Абдулла Кадыри (предисловие к роману «Минувшие дни»)',
                     'en': "Abdulla Qadiri (preface to 'Bygone Days')"},
  'image_url': None,
  'fun_fact': {'uz': "«O'tkan kunlar» o'zbek adabiyotidagi birinchi romandir; Qodiriy unda Otabek va Kumushbibining "
                     'fojiali sevgisi fonida xonliklar davri tushkunligini ochib bergan.',
               'ru': '«Минувшие дни» — первый в истории узбекский роман, повествующий о любви Атабека и Кумуш на фоне '
                     'феодального кризиса Кокандского ханства.',
               'en': "Written by Abdulla Qadiri between 1922 and 1926, 'Bygone Days' is the groundbreaking first novel "
                     'written in the Uzbek language.'},
  'aliases': ['abdulla qodiriy', "o'tkan kunlar", 'otkan kunlar', 'кадыри', 'минувшие дни']},
 {'id': 'lit_q_007',
  'sub_mode': 'quotes',
  'question': {'uz': "Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n\n«Qo'lyozmalar yonmaydi!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n\n«Рукописи не горят!»',
               'en': "Which work or author is the source of this famous quote?\n\n'Manuscripts don't burn!'"},
  'options': {'uz': ['Boris Pasternak («Doktor Jivago»)',
                     'Vladimir Nabokov («Lolita»)',
                     'Mixail Bulgakov («Usta va Margarita»)',
                     'Mixail Sholoxov («Tinch oqar Don»)'],
              'ru': ['Борис Пастернак («Доктор Живаго»)',
                     'Владимир Набоков («Лолита»)',
                     'Михаил Булгаков («Мастер и Маргарита»)',
                     'Михаил Шолохов («Тихий Дон»)'],
              'en': ["Boris Pasternak ('Doctor Zhivago')",
                     "Vladimir Nabokov ('Lolita')",
                     "Mikhail Bulgakov ('The Master and Margarita')",
                     "Mikhail Sholokhov ('And Quiet Flows the Don')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Mixail Bulgakov («Usta va Margarita»)',
                     'ru': 'Михаил Булгаков («Мастер и Маргарита»)',
                     'en': "Mikhail Bulgakov ('The Master and Margarita')"},
  'image_url': None,
  'fun_fact': {'uz': "Volandning Ustaga qarata aytgan bu so'zlari haqiqiy badiiy asarning abadiyligi va "
                     "o'chmasligining ramzidir.",
               'ru': 'Крылатая фраза Воланда в романе Булгакова символизирует бессмертие подлинного искусства и мысли.',
               'en': "Woland's retort when restoring the Master's burned novel remains one of literature's greatest "
                     'tributes to the immortality of art.'},
  'aliases': ['usta va margarita', 'bulgakov', 'мастер и маргарита', 'булгаков', 'рукописи не горят']},
 {'id': 'lit_q_008',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Inson yengilish uchun yaratilmagan. Uni yo'q qilish mumkin, ammo yengib bo'lmaydi!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Человек не для того создан, чтобы терпеть поражения. Человека можно уничтожить, но его нельзя '
                     'победить!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Man is not made for defeat. A man can be destroyed but not defeated!'"},
  'options': {'uz': ['Ernest Xeminguey («Alvido, qurol!»)',
                     "Jek London («Dengiz bo'risi»)",
                     'German Melvill («Mobi Dik»)',
                     'Ernest Xeminguey («Chol va dengiz»)'],
              'ru': ['Эрнест Хемингуэй («Прощай, оружие!»)',
                     'Джек Лондон («Морской волк»)',
                     'Герман Мелвилл («Моби Дик»)',
                     'Эрнест Хемингуэй («Старик и море»)'],
              'en': ["Ernest Hemingway ('A Farewell to Arms')",
                     "Jack London ('The Sea-Wolf')",
                     "Herman Melville ('Moby-Dick')",
                     "Ernest Hemingway ('The Old Man and the Sea')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ernest Xeminguey («Chol va dengiz»)',
                     'ru': 'Эрнест Хемингуэй («Старик и море»)',
                     'en': "Ernest Hemingway ('The Old Man and the Sea')"},
  'image_url': None,
  'fun_fact': {'uz': "Ushbu asar tufayli Ernest Xeminguey 1954 yilda adabiyot bo'yicha Nobel mukofotiga sazovor "
                     "bo'lgan.",
               'ru': 'Повесть о старике Сантьяго принесла Эрнесту Хемингуэю Нобелевскую премию по литературе 1954 '
                     'года.',
               'en': 'The novella earned Hemingway the Pulitzer Prize in 1953 and contributed directly to his 1954 '
                     'Nobel Prize in Literature.'},
  'aliases': ['chol va dengiz', 'xeminguey', 'старик и море', 'хемингуэй', 'old man and the sea']},
 {'id': 'lit_q_009',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Men titroq jonivormanmi yoki haq-huquqim bormi?!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Тварь ли я дрожащая или право имею?!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Am I a trembling creature or do I have the right?!'"},
  'options': {'uz': ['Fyodor Dostoevskiy («Jinoyat va jazo»)',
                     'Fyodor Dostoevskiy («Aka-uka Karamazovlar»)',
                     'Fyodor Dostoevskiy («Jinlar»)',
                     'Fyodor Dostoevskiy («Idiot»)'],
              'ru': ['Фёдор Достоевский («Преступление и наказание»)',
                     'Фёдор Достоевский («Братья Карамазовы»)',
                     'Фёдор Достоевский («Бесы»)',
                     'Фёдор Достоевский («Идиот»)'],
              'en': ["Fyodor Dostoevsky ('Crime and Punishment')",
                     "Fyodor Dostoevsky ('The Brothers Karamazov')",
                     "Fyodor Dostoevsky ('Demons')",
                     "Fyodor Dostoevsky ('The Idiot')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Fyodor Dostoevskiy («Jinoyat va jazo»)',
                     'ru': 'Фёдор Достоевский («Преступление и наказание»)',
                     'en': "Fyodor Dostoevsky ('Crime and Punishment')"},
  'image_url': None,
  'fun_fact': {'uz': "Rodion Raskolnikov kampir sudxo'rni o'ldirishdan oldin o'z vijdoni va 'o'ta qobiliyatli odamlar' "
                     'nazariyasi bilan kurashganda shunday deydi.',
               'ru': 'Главный этический конфликт Раскольникова между совестью и бесчеловечной теорией '
                     'вседозволенности.',
               'en': "The core moral question that obsesses Rodion Raskolnikov in Dostoevsky's psychological "
                     'masterpiece.'},
  'aliases': ['jinoyat va jazo', 'dostoevskiy', 'преступление и наказание', 'достоевский', 'raskolnikov']},
 {'id': 'lit_q_010',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Ko'ngil, sen bunchalar nega yig'laysan?\n"
                     "Nega to'kilasan ko'zdagi yoshday?..»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Душа, отчего ты плачешь столь безутешно?\n'
                     'Зачем ты таешь, подобно слезам на глазах?..»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Soul, why weepest thou so inconsolably?\n"
                     "Why dost thou pour forth like falling tears?..'"},
  'options': {'uz': ['Usmon Nosir («Yurak»)',
                     "Abdulhamid Cho'lpon («Ko'ngil» she'ri)",
                     "Hamid Olimjon («O'zbekiston»)",
                     "G'afur G'ulom («Sen yetim emassan»)"],
              'ru': ['Усман Насыр («Сердце»)',
                     'Абдулхамид Чулпан (стихотворение «Душа»)',
                     'Хамид Алимджан («Узбекистан»)',
                     'Гафур Гулям («Ты не сирота»)'],
              'en': ["Usmon Nosir ('The Heart')",
                     "Abdulhamid Cholpon ('Ko'ngil' / 'The Soul')",
                     "Hamid Olimjon ('Uzbekistan')",
                     "Ghafur Ghulam ('You Are Not an Orphan')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Abdulhamid Cho'lpon («Ko'ngil» she'ri)",
                     'ru': 'Абдулхамид Чулпан (стихотворение «Душа»)',
                     'en': "Abdulhamid Cholpon ('Ko'ngil' / 'The Soul')"},
  'image_url': None,
  'fun_fact': {'uz': "Cho'lponning «Ko'ngil» she'ri erk va ozodlikka intilish ramzidir; shoir 1938 yilda qatg'on "
                     "qurboni bo'lgan.",
               'ru': 'Шедевр лирики Чулпана выражает вечную тоску по духовной независимости; поэт был необоснованно '
                     'репрессирован в 1938 году.',
               'en': "Cholpon was one of Central Asia's foremost Jadid modernists, executed during the Great Purge in "
                     '1938.'},
  'aliases': ["cho'lpon", 'cholpon', "ko'ngil", 'чулпан', 'душа']},
 {'id': 'lit_q_011',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Bu yerga kiruvchilar, barcha umidlaringizni tark eting!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Оставь надежду, всяк сюда входящий!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Abandon all hope, ye who enter here!'"},
  'options': {'uz': ["Djon Milton («Yo'qotilgan jannat»)",
                     'Iogann Gyote («Faust»)',
                     "Dante Aligyeri («Ilohiy komediya» — Do'zax darvozasi)",
                     'Jovanni Bokkachcho («Dekameron»)'],
              'ru': ['Джон Мильтон («Потерянный рай»)',
                     'Иоганн Гёте («Фауст»)',
                     'Данте Алигьери («Божественная комедия» — Врата Ада)',
                     'Джованни Боккаччо («Декамерон»)'],
              'en': ["John Milton ('Paradise Lost')",
                     "Johann Wolfgang von Goethe ('Faust')",
                     "Dante Alighieri ('Divine Comedy' — Inferno Gates)",
                     "Giovanni Boccaccio ('The Decameron')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Dante Aligyeri («Ilohiy komediya» — Do'zax darvozasi)",
                     'ru': 'Данте Алигьери («Божественная комедия» — Врата Ада)',
                     'en': "Dante Alighieri ('Divine Comedy' — Inferno Gates)"},
  'image_url': None,
  'fun_fact': {'uz': "XIV asr boshlarida yozilgan «Ilohiy komediya»da Do'zax (Inferno) kirish peshtoqiga yozilgan "
                     'dahshatli ogohlantirish.',
               'ru': 'Знаменитая надпись на вратах Ада в третьей песне «Божественной комедии» Данте Алигьери.',
               'en': "Inscribed over the entrance to Hell in Canto III of Dante's 14th-century Italian epic "
                     "'Inferno'."},
  'aliases': ['dante', 'ilohiy komediya', 'данте', 'божественная комедия', 'оставь надежду', 'abandon all hope']},
 {'id': 'lit_q_012',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«To'xta, lahza, naqadar go'zalsan!» (Verweile doch! du bist so schön!)",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Остановись, мгновенье! Ты прекрасно!»',
               'en': "Which work or author is the source of this famous quote?\n\n'Ah, linger on, thou art so fair!'"},
  'options': {'uz': ['Fridrix Shiller («Qaroqchilar»)',
                     "Genrix Geyne («Qo'shiqlar kitobi»)",
                     "Tomas Mann («Sehrli tog'»)",
                     'Iogann Volfgang fon Gyote («Faust»)'],
              'ru': ['Фридрих Шиллер («Разбойники»)',
                     'Генрих Гейне («Книга песен»)',
                     'Томас Манн («Волшебная гора»)',
                     'Иоганн Вольфганг фон Гёте («Фауст»)'],
              'en': ["Friedrich Schiller ('The Robbers')",
                     "Heinrich Heine ('Book of Songs')",
                     "Thomas Mann ('The Magic Mountain')",
                     "Johann Wolfgang von Goethe ('Faust')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Iogann Volfgang fon Gyote («Faust»)',
                     'ru': 'Иоганн Вольфганг фон Гёте («Фауст»)',
                     'en': "Johann Wolfgang von Goethe ('Faust')"},
  'image_url': None,
  'fun_fact': {'uz': "Faust va Mefistofel shartnomasiga ko'ra, agar doktor Faust hayotining biron lahzasidan mutlaq "
                     "qanoat hosil qilib shu so'zni aytsa, uning joni iblisga o'tishi kerak edi.",
               'ru': 'Условие договора между Фаустом и Мефистофелем: если доктор произнесёт эту фразу, Мефистофель '
                     'забирает его душу.',
               'en': "The pivotal wager in Goethe's drama: if Faust ever finds complete contentment and speaks this "
                     'phrase, the devil wins his soul.'},
  'aliases': ['faust', 'gyote', 'фауст', 'гёте', 'остановись мгновенье', 'goethe']},
 {'id': 'lit_q_013',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Eng qorong'u tun ham tugaydi va albatta quyosh chiqadi.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Даже самая тёмная ночь закончится, и солнце взойдёт.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Even the darkest night will end and the sun will rise.'"},
  'options': {'uz': ["Viktor Gyugo («Xo'rlanganlar»)",
                     'Viktor Gyugo («Parij Bibi Maryam ibodatxonasi»)',
                     'Onore de Balzak («Gorio ota»)',
                     'Emil Zolya («Jerminal»)'],
              'ru': ['Виктор Гюго («Отверженные»)',
                     'Виктор Гюго («Собор Парижской Богоматери»)',
                     'Оноре де Бальзак («Отец Горио»)',
                     'Эмиль Золя («Жерминаль»)'],
              'en': ["Victor Hugo ('Les Misérables')",
                     "Victor Hugo ('The Hunchback of Notre-Dame')",
                     "Honoré de Balzac ('Père Goriot')",
                     "Émile Zola ('Germinal')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Viktor Gyugo («Xo'rlanganlar»)",
                     'ru': 'Виктор Гюго («Отверженные»)',
                     'en': "Victor Hugo ('Les Misérables')"},
  'image_url': None,
  'fun_fact': {'uz': "Viktor Gyugoning Jan Valjan taqdiri orqali adolat, mehr-shafqat va insonparvarlikni ulug'lagan "
                     'buyuk fransuz romani.',
               'ru': 'Гимн надежде и всепрощению в монументальном романе Виктора Гюго о судьбе Жана Вальжана.',
               'en': "An uplifting message of hope and redemption from Victor Hugo's epic 1862 historical novel."},
  'aliases': ["xo'rlanganlar", 'gyugo', 'отверженные', 'гюго', 'les miserables', 'victor hugo']},
 {'id': 'lit_q_014',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Barchamiz birimiz uchun, birimiz barchamiz uchun!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n\n«Один за всех, и все за одного!»',
               'en': "Which work or author is the source of this famous quote?\n\n'All for one and one for all!'"},
  'options': {'uz': ['Aleksandr Dyuma («Graf Monte-Kristo»)',
                     'Aleksandr Dyuma («Uch mushketyor»)',
                     'Valter Skott («Ayvengo»)',
                     'Robert Lyuis Stivenson («Xazinalar oroli»)'],
              'ru': ['Александр Дюма («Граф Монте-Кристо»)',
                     'Александр Дюма («Три мушкетёра»)',
                     'Вальтер Скотт («Айвенго»)',
                     'Роберт Льюис Стивенсон («Остров сокровищ»)'],
              'en': ["Alexandre Dumas ('The Count of Monte Cristo')",
                     "Alexandre Dumas ('The Three Musketeers')",
                     "Walter Scott ('Ivanhoe')",
                     "Robert Louis Stevenson ('Treasure Island')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Aleksandr Dyuma («Uch mushketyor»)',
                     'ru': 'Александр Дюма («Три мушкетёра»)',
                     'en': "Alexandre Dumas ('The Three Musketeers')"},
  'image_url': None,
  'fun_fact': {'uz': "D'Artanyan, Atos, Portos va Aramisning sadoqatli birodarlik qasami bo'lib, keyinchalik "
                     'Shveysariya Konfederatsiyasining norasmiy shioriga aylangan.',
               'ru': 'Девиз д’Артаньяна и трёх мушкетёров стал мировым символом верности и взаимовыручки, а также '
                     'девизом Швейцарии.',
               'en': "The legendary motto of d'Artagnan and his musketeer companions, also adopted as the traditional "
                     'motto of Switzerland.'},
  'aliases': ['uch mushketyor', 'dyuma', 'три мушкетера', 'дюма', 'three musketeers', 'all for one']},
 {'id': 'lit_q_015',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Bu zamonlarning eng yaxshisi edi, bu zamonlarning eng yomoni edi...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Это было лучшее из всех времён, это было худшее из всех времён...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'It was the best of times, it was the worst of times...'"},
  'options': {'uz': ['Charlz Dikkens («Oliver Tvist»)',
                     'Charlz Dikkens («Katta umidlar»)',
                     'Charlz Dikkens («Ikki shahar qissasi»)',
                     'Uilyam Tekkerey («Shon-shuhrat yarmarkasi»)'],
              'ru': ['Чарльз Диккенс («Приключения Оливера Твиста»)',
                     'Чарльз Диккенс («Большие надежды»)',
                     'Чарльз Диккенс («Повесть о двух городах»)',
                     'Уильям Теккерей («Ярмарка тщеславия»)'],
              'en': ["Charles Dickens ('Oliver Twist')",
                     "Charles Dickens ('Great Expectations')",
                     "Charles Dickens ('A Tale of Two Cities')",
                     "William Makepeace Thackeray ('Vanity Fair')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Charlz Dikkens («Ikki shahar qissasi»)',
                     'ru': 'Чарльз Диккенс («Повесть о двух городах»)',
                     'en': "Charles Dickens ('A Tale of Two Cities')"},
  'image_url': None,
  'fun_fact': {'uz': 'Fransuz inqilobi davridagi London va Parij voqealarini tasvirlovchi ushbu roman dunyoda 200 '
                     'milliondan ortiq nusxada sotilgan.',
               'ru': 'Культовое начало романа Диккенса 1859 года; книга о событиях Французской революции разошлась '
                     'тиражом свыше 200 млн экземпляров.',
               'en': "The famous antithetical opening line of Dickens's 1859 novel set in London and Paris during the "
                     'French Revolution.'},
  'aliases': ['ikki shahar qissasi', 'dikkens', 'повесть о двух городах', 'диккенс', 'tale of two cities', 'dickens']},
 {'id': 'lit_q_016',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Mehnat — inson qilishga majbur bo'lgan ishdir, o'yin esa — qilishga majbur bo'lmagan ishdir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Работа — это то, что человек обязан делать, а игра — то, чего он делать не обязан.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Work consists of whatever a body is obliged to do, and Play consists of whatever a body is not "
                     "obliged to do.'"},
  'options': {'uz': ['Mark Tven («Geklberri Finn sarguzashtlari»)',
                     'Mark Tven («Shahzoda va gado»)',
                     'O. Genri («Qizil tanlilar dohiysi»)',
                     'Mark Tven («Tom Soyerning sarguzashtlari»)'],
              'ru': ['Марк Твен («Приключения Гекльберри Финна»)',
                     'Марк Твен («Принц и нищий»)',
                     'О. Генри («Вождь краснокожих»)',
                     'Марк Твен («Приключения Тома Сойера»)'],
              'en': ["Mark Twain ('Adventures of Huckleberry Finn')",
                     "Mark Twain ('The Prince and the Pauper')",
                     "O. Henry ('The Ransom of Red Chief')",
                     "Mark Twain ('The Adventures of Tom Sawyer')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Mark Tven («Tom Soyerning sarguzashtlari»)',
                     'ru': 'Марк Твен («Приключения Тома Сойера»)',
                     'en': "Mark Twain ('The Adventures of Tom Sawyer')"},
  'image_url': None,
  'fun_fact': {'uz': "Tom Soyer Polly xolaning devorini oqlash jazosini boshqa bolalarga qimmatbaho 'o'yin' sifatida "
                     "o'tkazib yuborganida muallif shunday xulosaga keladi.",
               'ru': 'Философский вывод Марка Твена после знаменитого эпизода, в котором Том превратил покраску забора '
                     'в желанную привилегию для соседских мальчишек.',
               'en': "Mark Twain's witty commentary on human psychology following the famous fence-whitewashing scene "
                     'in St. Petersburg, Missouri.'},
  'aliases': ['tom soyer', 'mark tven', 'том сойер', 'марк твен', 'tom sawyer', 'mark twain']},
 {'id': 'lit_q_017',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Barcha imkonsiz narsalarni chiqarib tashlaganingizda, qolgan narsa qanchalik aqlbovar qilmas '
                     "bo'lmasin — haqiqatdir!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Когда вы отбросите всё невозможное, то, что останется, каким бы невероятным оно ни казалось, и '
                     'есть истина!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'When you have eliminated the impossible, whatever remains, however improbable, must be the "
                     "truth!'"},
  'options': {'uz': ['Artur Konan Doyl («Sherlok Xolms»)',
                     'Agata Kristi («Erkyul Puaro»)',
                     'Edgar Allan Po («Ogyust Dyupen»)',
                     'Jorj Simenon («Komissar Megre»)'],
              'ru': ['Артур Конан Дойл («Приключения Шерлока Холмса»)',
                     'Агата Кристи («Эркюль Пуаро»)',
                     'Эдгар Аллан По («Огюст Дюпен»)',
                     'Жорж Сименон («Комиссар Мегрэ»)'],
              'en': ["Arthur Conan Doyle ('Sherlock Holmes')",
                     "Agatha Christie ('Hercule Poirot')",
                     "Edgar Allan Poe ('Auguste Dupin')",
                     "Georges Simenon ('Inspector Maigret')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Artur Konan Doyl («Sherlok Xolms»)',
                     'ru': 'Артур Конан Дойл («Приключения Шерлока Холмса»)',
                     'en': "Arthur Conan Doyle ('Sherlock Holmes')"},
  'image_url': None,
  'fun_fact': {'uz': "Sherlok Xolmsning do'sti doktor Vatsonga o'zining deduktiv usulining asosiy tamoyilini "
                     'tushuntirgan mashhur qoidasi.',
               'ru': 'Золотое правило дедуктивного метода великого сыщика Шерлока Холмса, впервые прозвучавшее в '
                     'повести «Знак четырёх».',
               'en': "Sherlock Holmes's defining maxim of deductive reasoning, first appearing in the 1890 novel 'The "
                     "Sign of the Four'."},
  'aliases': ['sherlok xolms', 'konan doyl', 'шерлок холмс', 'конан дойл', 'sherlock holmes', 'conan doyle']},
 {'id': 'lit_q_018',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Boy bo'ydoq kishining albatta xotin qidirayotgani — butun olam tan olgan haqiqatdir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Всепризнанной истиной является то, что состоятельный холостяк непременно должен испытывать '
                     'потребность в жене.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'It is a truth universally acknowledged, that a single man in possession of a good fortune, must "
                     "be in want of a wife.'"},
  'options': {'uz': ['Sharlotta Bronte («Jeyn Eyr»)',
                     "Jeyn Ostin («G'urur va andisha»)",
                     'Emili Bronte («Momaqaldiroqli dovon»)',
                     'Jorj Eliot («Middlemarch»)'],
              'ru': ['Шарлотта Бронте («Джейн Эйр»)',
                     'Джейн Остин («Гордость и предубеждение»)',
                     'Эмили Бронте («Грозовой перевал»)',
                     'Джордж Элиот («Мидлмарч»)'],
              'en': ["Charlotte Brontë ('Jane Eyre')",
                     "Jane Austen ('Pride and Prejudice')",
                     "Emily Brontë ('Wuthering Heights')",
                     "George Eliot ('Middlemarch')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Jeyn Ostin («G'urur va andisha»)",
                     'ru': 'Джейн Остин («Гордость и предубеждение»)',
                     'en': "Jane Austen ('Pride and Prejudice')"},
  'image_url': None,
  'fun_fact': {'uz': "1813 yilda nashr etilgan «G'urur va andisha» romanining boshlang'ich jumlasi ingliz "
                     'adabiyotidagi eng mashhur kinoyali ochilish jumlalaridan biridir.',
               'ru': 'Ироничное первое предложение шедевра Джейн Остин 1813 года задаёт тон всей истории '
                     'взаимоотношений Элизабет Беннет и мистера Дарси.',
               'en': 'One of the most celebrated and ironic opening lines in the English language, setting the social '
                     "satire of Austen's 1813 novel."},
  'aliases': ["g'urur va andisha",
              'jeyn ostin',
              'гордость и предубеждение',
              'джейн остин',
              'pride and prejudice',
              'austen']},
 {'id': 'lit_q_019',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Shunday qilib, biz oqimga qarshi suzamiz, to'xtovsiz o'tmishga uloqtirilayotgan qayiqlar "
                     "yanglig' kurashamiz...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Так мы и плывём вперёд, как лодки против течения, непрестанно сносимые назад, в прошлое...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'So we beat on, boats against the current, borne back ceaselessly into the past.'"},
  'options': {'uz': ['Ernest Xeminguey («Quyosh baribir chiqaveradi»)',
                     "Jon Steynbek («G'azab mevalari»)",
                     'F. Skott Fitsjerald («Buyuk Getsbi»)',
                     'Teodor Drayzer («Amerika fojiasi»)'],
              'ru': ['Эрнест Хемингуэй («Фиеста»)',
                     'Джон Стейнбек («Гроздья гнева»)',
                     'Ф. Скотт Фицджеральд («Великий Гэтсби»)',
                     'Теодор Драйзер («Американская трагедия»)'],
              'en': ["Ernest Hemingway ('The Sun Also Rises')",
                     "John Steinbeck ('The Grapes of Wrath')",
                     "F. Scott Fitzgerald ('The Great Gatsby')",
                     "Theodore Dreiser ('An American Tragedy')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'F. Skott Fitsjerald («Buyuk Getsbi»)',
                     'ru': 'Ф. Скотт Фицджеральд («Великий Гэтсби»)',
                     'en': "F. Scott Fitzgerald ('The Great Gatsby')"},
  'image_url': None,
  'fun_fact': {'uz': "1925 yilda chop etilgan «Buyuk Getsbi» romanining so'nggi jumlasi bo'lib, insonning orzular va "
                     "o'tmish o'rtasidagi cheksiz kurashini aks ettiradi.",
               'ru': 'Финальная строка романа Фицджеральда 1925 года высечена на могильном камне писателя и его '
                     'супруги Зельды в Роквилле.',
               'en': "The haunting closing line of Fitzgerald's 1925 masterpiece about the illusory nature of the "
                     'American Dream, carved on his tombstone.'},
  'aliases': ['buyuk getsbi', 'fitsjerald', 'великий гэтсби', 'фицджеральд', 'great gatsby', 'fitzgerald']},
 {'id': 'lit_q_020',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Qarg'a dedi: 'Hech qachon!' (Nevermore)»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Каркнул Ворон: „Никогда!“ (Nevermore)»',
               'en': "Which work or author is the source of this famous quote?\n\n'Quoth the Raven: Nevermore!'"},
  'options': {'uz': ['Edgar Allan Po («Annabel Li»)',
                     'Sharl Bodler («Yovuzlik gullari»)',
                     'Lord Bayron («Chayld Garold»)',
                     "Edgar Allan Po («Qarg'a» dostoni)"],
              'ru': ['Эдгар Аллан По («Аннабель Ли»)',
                     'Шарль Бодлер («Цветы зла»)',
                     'Лорд Байрон («Паломничество Чайльд-Гарольда»)',
                     'Эдгар Аллан По (поэма «Ворон»)'],
              'en': ["Edgar Allan Poe ('Annabel Lee')",
                     "Charles Baudelaire ('Les Fleurs du mal')",
                     "Lord Byron ('Childe Harold's Pilgrimage')",
                     "Edgar Allan Poe ('The Raven')"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Edgar Allan Po («Qarg'a» dostoni)",
                     'ru': 'Эдгар Аллан По (поэма «Ворон»)',
                     'en': "Edgar Allan Poe ('The Raven')"},
  'image_url': None,
  'fun_fact': {'uz': "1845 yilda e'lon qilingan ushbu doston sevikli yoridan ayrilgan qahramonning qarg'a bilan sirli "
                     "va g'amgin muloqotini ifodalaydi.",
               'ru': 'Знаменитый рефрен мрачной поэмы Эдгара По 1845 года, переведённой на русский язык Бальмонтом и '
                     'Брюсовым.',
               'en': 'First published in January 1845, this ominous refraining croak established Poe as a master of '
                     'macabre atmosphere and musical rhythm.'},
  'aliases': ["qarg'a", 'edgar po', 'ворон', 'эдгар по', 'raven', 'nevermore', 'edgar allan poe']},
 {'id': 'lit_q_021',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Meni Ismoil deb chaqiring.» (Call me Ishmael)',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n\n«Зовите меня Измаил.»',
               'en': "Which work or author is the source of this famous quote?\n\n'Call me Ishmael.'"},
  'options': {'uz': ['German Melvill («Mobi Dik»)',
                     "Jek London («Dengiz bo'risi»)",
                     'Robert Lyuis Stivenson («Xazinalar oroli»)',
                     'Daniyel Defo («Robinzon Kruzo»)'],
              'ru': ['Герман Мелвилл («Моби Дик, или Белый кит»)',
                     'Джек Лондон («Морской волк»)',
                     'Роберт Льюис Стивенсон («Остров сокровищ»)',
                     'Даниэль Дефо («Робинзон Крузо»)'],
              'en': ["Herman Melville ('Moby-Dick')",
                     "Jack London ('The Sea-Wolf')",
                     "Robert Louis Stevenson ('Treasure Island')",
                     "Daniel Defoe ('Robinson Crusoe')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'German Melvill («Mobi Dik»)',
                     'ru': 'Герман Мелвилл («Моби Дик, или Белый кит»)',
                     'en': "Herman Melville ('Moby-Dick')"},
  'image_url': None,
  'fun_fact': {'uz': '1851 yilda nashr etilgan oq kashalot ortidan quvuvchi kapitan Axav va kema jamoasi haqidagi '
                     'romanning afsonaviy birinchi jumlasi.',
               'ru': 'Одно из самых знаменитых первых предложений в мировой литературе, открывающее рассказ о '
                     'гибельной охоте капитана Ахава на белого кита.',
               'en': 'Perhaps the most iconic opening sentence in American literature, inviting the reader aboard the '
                     'ill-fated whaleship Pequod.'},
  'aliases': ['mobi dik', 'melvill', 'моби дик', 'мелвилл', 'moby dick', 'call me ishmael']},
 {'id': 'lit_q_022',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Bugun onam vafot etdi. Yoki kechadir, aniq bilmayman...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Сегодня умерла мама. А может, вчера — не знаю...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Mother died today. Or maybe yesterday, I can't be sure...'"},
  'options': {'uz': ['Alber Kamyu («Vabo»)',
                     'Alber Kamyu («Begona»)',
                     "Jan-Pol Sartr («Ko'ngil aynishi»)",
                     'Frans Kafka («Sud jarayoni»)'],
              'ru': ['Альбер Камю («Чума»)',
                     'Альбер Камю («Посторонний»)',
                     'Жан-Поль Сартр («Тошнота»)',
                     'Франц Кафка («Процесс»)'],
              'en': ["Albert Camus ('The Plague')",
                     "Albert Camus ('The Stranger')",
                     "Jean-Paul Sartre ('Nausea')",
                     "Franz Kafka ('The Trial')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Alber Kamyu («Begona»)',
                     'ru': 'Альбер Камю («Посторонний»)',
                     'en': "Albert Camus ('The Stranger')"},
  'image_url': None,
  'fun_fact': {'uz': "Alber Kamyuning 1942 yilda e'lon qilingan ekzistensialist romani qahramoni Merso o'zining hissiy "
                     'begonalashuvi bilan mashhur.',
               'ru': 'Первая фраза повести Камю «Посторонний», ярко иллюстрирующая философию абсурда и отчуждения '
                     'главного героя Мерсо.',
               'en': "The chilling opening line of Camus's 1942 absurdist classic defining the emotional detachment of "
                     'protagonist Meursault.'},
  'aliases': ['begona', 'kamyu', 'посторонний', 'камю', 'the stranger', 'camus']},
 {'id': 'lit_q_023',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Vasvasadan qutulishning yagona yo'li — unga taslim bo'lishdir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Единственный способ избавиться от искушения — поддаться ему.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'The only way to get rid of a temptation is to yield to it.'"},
  'options': {'uz': ["Oskar Uayld («Jiddiy bo'lish qanchalik muhim»)",
                     'Bernard Shou («Pigmalion»)',
                     'Oskar Uayld («Dorian Greyning portreti»)',
                     'Somerset Moem («Oy va chaqa»)'],
              'ru': ['Оскар Уайльд («Как важно быть серьёзным»)',
                     'Бернард Шоу («Пигмалион»)',
                     'Оскар Уайльд («Портрет Дориана Грея»)',
                     'Сомерсет Моэм («Луна и грош»)'],
              'en': ["Oscar Wilde ('The Importance of Being Earnest')",
                     "George Bernard Shaw ('Pygmalion')",
                     "Oscar Wilde ('The Picture of Dorian Gray')",
                     "W. Somerset Maugham ('The Moon and Sixpence')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Oskar Uayld («Dorian Greyning portreti»)',
                     'ru': 'Оскар Уайльд («Портрет Дориана Грея»)',
                     'en': "Oscar Wilde ('The Picture of Dorian Gray')"},
  'image_url': None,
  'fun_fact': {'uz': 'Lord Genri Uottonning yosh Dorian Greyga estetik lazzatparastlik (gedonizm) haqida bergan '
                     'mashhur paradoksal maslahati.',
               'ru': 'Один из сотен блестящих гедонистических парадоксов лорда Генри Уоттона в единственном '
                     'опубликованном романе Оскара Уайльда (1890).',
               'en': "Lord Henry Wotton's hedonistic philosophy whispering corruption into Dorian Gray's "
                     'impressionable soul.'},
  'aliases': ['dorian grey', 'uayld', 'дориан грей', 'уайльд', 'dorian gray', 'oscar wilde']},
 {'id': 'lit_q_024',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Bir kuni ertalab notinch tushlardan uyg'ongan Gregor Zamza o'zining ulkan hasharotga aylanib "
                     "qolganini ko'rdi.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Проснувшись однажды утром после беспокойного сна, Грегор Замза обнаружил, что он у себя в '
                     'постели превратился в страшное насекомое.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed "
                     "into a gigantic insect.'"},
  'options': {'uz': ['Frans Kafka («Sud jarayoni»)',
                     'Frans Kafka («Qasr»)',
                     "Tomas Mann («Sehrli tog'»)",
                     'Frans Kafka («Evrilish»)'],
              'ru': ['Франц Кафка («Процесс»)',
                     'Франц Кафка («Замок»)',
                     'Томас Манн («Волшебная гора»)',
                     'Франц Кафка («Превращение»)'],
              'en': ["Franz Kafka ('The Trial')",
                     "Franz Kafka ('The Castle')",
                     "Thomas Mann ('The Magic Mountain')",
                     "Franz Kafka ('The Metamorphosis')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Frans Kafka («Evrilish»)',
                     'ru': 'Франц Кафка («Превращение»)',
                     'en': "Franz Kafka ('The Metamorphosis')"},
  'image_url': None,
  'fun_fact': {'uz': "Kafkaning 1915 yilda yozilgan ushbu mashhur hikoyasi insonning yolg'izligi va jamiyatdagi "
                     'begonalashuvini chuqur ramziy tarzda aks ettiradi.',
               'ru': 'Ошеломляющее начало новеллы 1915 года, ставшей метафорой отчуждения, потери идентичности и '
                     'одиночества человека в обществе.',
               'en': "Published in 1915, this grotesque yet mundane premise launched Kafka's reputation as a prophet "
                     'of modern existential alienation.'},
  'aliases': ['evrilish', 'kafka', 'превращение', 'кафка', 'metamorphosis', 'gregor samsa']},
 {'id': 'lit_q_025',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Oradan ko'p yillar o'tib, otuvchi otryad ro'parasida turgan polkovnik Aureliano Buendia otasi "
                     "uni muzni ko'rishga olib borgan o'sha olis oqshomni esladi...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Пройдёт много лет, и полковник Аурелиано Буэндиа, стоя у стены в ожидании расстрела, вспомнит '
                     'тот далёкий вечер, когда отец взял его с собой посмотреть на лёд...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that "
                     "distant afternoon when his father took him to discover ice...'"},
  'options': {'uz': ["Gabriel Garsia Markes («Yolg'izlikning yuz yili»)",
                     'Gabriel Garsia Markes («Vabo davridagi muhabbat»)',
                     'Gabriel Garsia Markes («Patriarx kuzi»)',
                     'Xorxe Luis Borxes («Fiktsiyalar»)'],
              'ru': ['Габриэль Гарсиа Маркес («Сто лет одиночества»)',
                     'Габриэль Гарсиа Маркес («Любовь во время холеры»)',
                     'Габриэль Гарсиа Маркес («Осень патриарха»)',
                     'Хорхе Луис Борхес («Вымышленные истории»)'],
              'en': ["Gabriel García Márquez ('One Hundred Years of Solitude')",
                     "Gabriel García Márquez ('Love in the Time of Cholera')",
                     "Gabriel García Márquez ('The Autumn of the Patriarch')",
                     "Jorge Luis Borges ('Ficciones')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Gabriel Garsia Markes («Yolg'izlikning yuz yili»)",
                     'ru': 'Габриэль Гарсиа Маркес («Сто лет одиночества»)',
                     'en': "Gabriel García Márquez ('One Hundred Years of Solitude')"},
  'image_url': None,
  'fun_fact': {'uz': "Sehrli realizm uslubining cho'qqisi hisoblangan ushbu asar xayoliy Makondo shaharchasi va "
                     'Buendia avlodi tarixi haqidadir.',
               'ru': 'Величайшее начало в литературе магического реализма, открывающее историю шести поколений рода '
                     'Буэндиа в городке Макондо.',
               'en': 'Widely cited as one of the finest opening sentences in 20th-century literature, introducing the '
                     'magic-realist epic of Macondo.'},
  'aliases': ["yolg'izlikning yuz yili",
              'markes',
              'сто лет одиночества',
              'маркес',
              'one hundred years of solitude',
              'marquez']},
 {'id': 'lit_q_026',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Har kimki vafo qilsa, vafo topqusidur,\n'
                     'Har kimki jafo qilsa, jafo topqusidur.\n'
                     "Yaxshi kishi ko'rmag'ay yamonlik hargiz,\n"
                     "Har kimki yamon bo'lsa, jazo topqusidur.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Тот, кто верность хранит, тот верность найдет,\n'
                     'Кто сеет жестокость, к тому горе придет.\n'
                     'Доброму зло не грозит никогда,\n'
                     'Злого же кара и гибель ждет.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'He who keeps faith will find fidelity,\n"
                     'He who sows cruel pain will reap agony.\n'
                     'The righteous shall never encounter ill,\n'
                     "While evil men face retribution still.'"},
  'options': {'uz': ["Alisher Navoiy («Badoyi' ul-vasat»)",
                     'Zahiriddin Muhammad Bobur («Bobur devoni»)',
                     'Lutfiy («Devon»)',
                     'Mashrab («Mabdai nur»)'],
              'ru': ['Алишер Навои («Диван»)',
                     'Захириддин Мухаммад Бабур (рубаи из «Дивана Бабура»)',
                     'Лутфи («Диван»)',
                     'Боборахим Машраб («Диван»)'],
              'en': ["Alisher Navoi ('Divan')",
                     "Zahiriddin Muhammad Babur (rubai from 'Divan of Babur')",
                     "Lutfi ('Divan')",
                     "Mashrab ('Divan')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Zahiriddin Muhammad Bobur («Bobur devoni»)',
                     'ru': 'Захириддин Мухаммад Бабур (рубаи из «Дивана Бабура»)',
                     'en': "Zahiriddin Muhammad Babur (rubai from 'Divan of Babur')"},
  'image_url': None,
  'fun_fact': {'uz': "Bobur Mirzoning ushbu ruboiysi o'zbek adabiyotida ezgulik va yomonlikning muqarrar oqibati "
                     'haqidagi eng mashhur hikmatli bayt hisoblanadi.',
               'ru': 'Одно из самых известных четверостиший Бабура, воспевающее закон справедливости и неизбежности '
                     'воздаяния за содеянное.',
               'en': "Babur's celebrated rubai on cosmic justice and reciprocal karma remains among the most quoted "
                     'verses in Central Asia.'},
  'aliases': ['bobur', 'zahiriddin muhammad bobur', 'бабур', 'har kimki vafo qilsa', 'ruboiy']},
 {'id': 'lit_q_027',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Tarixingdir ming asrlar\n'
                     "Ichra pinhon, o'zbegim,\n"
                     'Senga tengdosh Pomiru\n'
                     "Tiyonshon, o'zbegim.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«В толще тысячелетий скрыта\n'
                     'Твоя история, мой узбек,\n'
                     'Ровесник тебе Памир\n'
                     'И седой Тянь-Шань, мой узбек.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Thy history lies shrouded\n"
                     'Across ten thousand years, my Uzbek,\n'
                     'Ancient as the peaks of Pamir\n'
                     "And white-capped Tian Shan, my Uzbek.'"},
  'options': {'uz': ["Abdulla Oripov («O'zbekiston»)",
                     'Muhammad Yusuf («Vatanim»)',
                     "Erkin Vohidov («O'zbegim» qasidasi)",
                     'Rauf Parfi («Qaytish»)'],
              'ru': ['Абдулла Арипов («Узбекистан»)',
                     'Мухаммад Юсуф («Родина»)',
                     'Эркин Вахидов (поэма-касыда «Узбегим»)',
                     'Рауф Парфи («Возвращение»)'],
              'en': ["Abdulla Oripov ('Uzbekistan')",
                     "Muhammad Yusuf ('My Homeland')",
                     "Erkin Vohidov ('O'zbegim' Ode)",
                     "Rauf Parfi ('The Return')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Erkin Vohidov («O'zbegim» qasidasi)",
                     'ru': 'Эркин Вахидов (поэма-касыда «Узбегим»)',
                     'en': "Erkin Vohidov ('O'zbegim' Ode)"},
  'image_url': None,
  'fun_fact': {'uz': "1968 yilda yozilgan «O'zbegim» qasidasi sovet davri senzurasiga qaramay xalq milliy g'ururini "
                     "uyg'otgan tarixiy she'riy asar bo'ldi.",
               'ru': 'Касыда Эркина Вахидова 1968 года пробудила национальное самосознание и гордость за многовековое '
                     'наследие предков.',
               'en': "Written in 1968 under Soviet restrictions, this sweeping ode celebrated Uzbekistan's "
                     'millennia-long cultural antiquity and historical giants.'},
  'aliases': ['erkin vohidov', "o'zbegim", 'ozbegim', 'эркин вахидов', 'узбегим', 'vohidov']},
 {'id': 'lit_q_028',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Yurtim, seni yelkangda tog'lar tutib turibdi,\n"
                     "Bosh egmagan mag'rur bir viqor tutib turibdi!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Родина моя, горы держат тебя на своих плечах,\n'
                     'Гордое, непокорённое величие венчает твой образ!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Homeland, the mountains hold thee high on their shoulders,\n"
                     "A proud, unbending majesty upholds thy stature!'"},
  'options': {'uz': ["Erkin Vohidov («O'zbegim»)",
                     'Shavkat Rahmon («Hulvo»)',
                     'Halima Xudoyberdiyeva («Muqaddas ayol»)',
                     "Abdulla Oripov («O'zbekiston» qasidasi)"],
              'ru': ['Эркин Вахидов («Узбегим»)',
                     'Шавкат Рахмон («Хульво»)',
                     'Халима Худойбердыева («Святая женщина»)',
                     'Абдулла Арипов (стихотворение «Узбекистан»)'],
              'en': ["Erkin Vohidov ('O'zbegim')",
                     "Shavkat Rahmon ('Hulvo')",
                     "Halima Xudoyberdiyeva ('Sacred Woman')",
                     "Abdulla Oripov ('Uzbekistan' Ode)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Abdulla Oripov («O'zbekiston» qasidasi)",
                     'ru': 'Абдулла Арипов (стихотворение «Узбекистан»)',
                     'en': "Abdulla Oripov ('Uzbekistan' Ode)"},
  'image_url': None,
  'fun_fact': {'uz': "O'zbekiston Qahramoni Abdulla Oripov O'zbekiston Respublikasi Davlat madhiyasi matnining ham "
                     'muallifidir.',
               'ru': 'Герой Узбекистана Абдулла Арипов также является автором текста Государственного гимна Республики '
                     'Узбекистан.',
               'en': 'Hero of Uzbekistan Abdulla Oripov was also the author of the official National Anthem of the '
                     'Republic of Uzbekistan.'},
  'aliases': ['abdulla oripov', "o'zbekiston", 'oripov', 'абдулла арипов', 'арипов', 'узбекистан']},
 {'id': 'lit_q_029',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Onam o'qish-yozishni bilmas edi. Ammo butun umri davomida menga mehr-oqibat va insoniylikdan "
                     'saboq berdi...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Моя мать не умела читать и писать. Но всю жизнь она давала мне великие уроки доброты, '
                     'милосердия и человечности...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'My mother could neither read nor write. Yet all her life she taught me the profoundest lessons "
                     "of kindness, compassion, and humanity...'"},
  'options': {'uz': ["O'tkir Hoshimov («Dunyoning ishlari»)",
                     "O'tkir Hoshimov («Ikki eshik orasi»)",
                     'Said Ahmad («Ufq»)',
                     'Asqad Muxtor («Chinor»)'],
              'ru': ['Уткир Хашимов («Дела земные»)',
                     'Уткир Хашимов («Войти и выйти» / «Между двух дверей»)',
                     'Саид Ахмад («Горизонт»)',
                     'Аскад Мухтар («Чинар»)'],
              'en': ["O'tkir Hoshimov ('Affairs of this World')",
                     "O'tkir Hoshimov ('Between Two Doors')",
                     "Said Ahmad ('The Horizon')",
                     "Asqad Mukhtar ('The Plane Tree')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "O'tkir Hoshimov («Dunyoning ishlari»)",
                     'ru': 'Уткир Хашимов («Дела земные»)',
                     'en': "O'tkir Hoshimov ('Affairs of this World')"},
  'image_url': None,
  'fun_fact': {'uz': "«Dunyoning ishlari» asari adibning o'z onasiga bag'ishlangan lirik qissalar to'plami bo'lib, "
                     "o'zbek onalarining mehr-oqibatini yuksak mahorat bilan tarannum etgan.",
               'ru': 'Трогательная автобиографическая повесть Уткира Хашимова — признанный гимн материнской любви и '
                     'самопожертвованию.',
               'en': "Hoshimov's tender biographical work pays homage to his mother and the enduring devotion of Uzbek "
                     'maternal care.'},
  'aliases': ['dunyoning ishlari', "o'tkir hoshimov", 'дела земные', 'уткир хашимов', 'otkir hoshimov']},
 {'id': 'lit_q_030',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Odam bolasi boshiga qanday kulfat tushmasin, umidini uzmasa, albatta najot topadi.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Какая бы беда ни обрушилась на человека, пока в его сердце жива надежда — спасение обязательно '
                     'придёт.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'No matter what sorrow falls upon human shoulders, so long as hope remains alive, salvation will "
                     "surely arrive.'"},
  'options': {'uz': ["Said Ahmad («Kelinlar qo'zg'oloni»)",
                     'Said Ahmad («Ufq» trilogiyasi)',
                     "Shukur Xolmirzayev («O'n sakkizga kirmagan kim bor»)",
                     "O'tkir Hoshimov («Ikki eshik orasi»)"],
              'ru': ['Саид Ахмад («Бунт невесток»)',
                     'Саид Ахмад (трилогия «Горизонт»)',
                     'Шукур Холмирзаев («Кому не было восемнадцати»)',
                     'Уткир Хашимов («Между двух дверей»)'],
              'en': ["Said Ahmad ('The Revolt of the Daughters-in-Law')",
                     "Said Ahmad ('The Horizon' Trilogy)",
                     "Shukur Kholmirzaev ('Who Was Never Eighteen')",
                     "O'tkir Hoshimov ('Between Two Doors')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Said Ahmad («Ufq» trilogiyasi)',
                     'ru': 'Саид Ахмад (трилогия «Горизонт»)',
                     'en': "Said Ahmad ('The Horizon' Trilogy)"},
  'image_url': None,
  'fun_fact': {'uz': "Said Ahmadning «Ufq» trilogiyasi Ikkinchi jahon urushi va undan keyingi yillarda o'zbek "
                     'xalqining jasorati, fidoiyligi va qalb jarohatlarini haqqoniy tasvirlagan.',
               'ru': 'Масштабная трилогия Саида Ахмада рассказывает о судьбах тыловиков в годы войны и строительстве '
                     'Большого Ферганского канала.',
               'en': "Said Ahmad's monumental trilogy depicts the resilience of ordinary people during World War II "
                     'and the digging of the Great Fergana Canal.'},
  'aliases': ['ufq', 'said ahmad', 'горизонт', 'саид ахмад']},
 {'id': 'lit_q_031',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«O'zim ham xush ko'raman-da, bekorchilikdan ko'ra biror hunarning boshini tutish kerak, deb "
                     "o'yladim...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Я и сам так подумал: чем слоняться без дела, не лучше ли взяться за какое-нибудь ремесло...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'I thought to myself: rather than loafing around, isn't it better to try my hand at an honest "
                     "craft?..'"},
  'options': {'uz': ["G'afur G'ulom («Yodgor»)",
                     "Xudoyberdi To'xtaboyev («Sariq devni minib»)",
                     "G'afur G'ulom («Shum bola» qissasi)",
                     'Abdulla Qahhor («Sinchalak»)'],
              'ru': ['Гафур Гулям («Ядгар»)',
                     'Худайберды Тухтабаев («Верхом на жёлтом диве»)',
                     'Гафур Гулям (повесть «Озорник»)',
                     'Абдулла Каххар («Птичка-невеличка»)'],
              'en': ["Ghafur Ghulam ('Yadgar')",
                     "Khudoyberdi Tukhtabayev ('Riding the Yellow Giant')",
                     "Ghafur Ghulam ('The Mischievous Boy')",
                     "Abdulla Qahhor ('The Little Bird')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "G'afur G'ulom («Shum bola» qissasi)",
                     'ru': 'Гафур Гулям (повесть «Озорник»)',
                     'en': "Ghafur Ghulam ('The Mischievous Boy')"},
  'image_url': None,
  'fun_fact': {'uz': "G'afur G'ulomning «Shum bola» qissasi o'zbek bolalar adabiyotining durdonasi bo'lib, o'tkir "
                     "satira va sho'x sarguzashtlarga boydir.",
               'ru': 'Классическая юмористическая повесть Гафура Гуляма о приключениях смышленого ташкентского '
                     'мальчишки в дореволюционном Туркестане.',
               'en': "Ghafur Ghulam's beloved picaresque tale recounts the humorous adventures and hardships of a "
                     'resourceful young boy in pre-revolutionary Tashkent.'},
  'aliases': ['shum bola', "g'afur g'ulom", 'озорник', 'гафур гулям', 'mischievous boy']},
 {'id': 'lit_q_032',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«So'z gavhari dengiz tubida yotgan dur kabi bebahodir, uni qadrlovchi inson qalbini munavvar "
                     'qiladi.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Жемчужина слова драгоценна, как перл со дна океана; озаряет она сердце того, кто постиг её '
                     'благородную суть.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'The pearl of the word is as priceless as a gem from the ocean floor, illuminating the heart of "
                     "whoever cherishes its grace.'"},
  'options': {'uz': ["Oybek («Qutlug' qon»)",
                     'Pirimqul Qodirov («Yulduzli tunlar»)',
                     "Mirkarim Osim («To'maris»)",
                     'Oybek («Navoiy» romani)'],
              'ru': ['Айбек («Священная кровь»)',
                     'Пиримкул Кадыров («Звёздные ночи»)',
                     'Миркарим Осим («Томирис»)',
                     'Айбек (роман «Навои»)'],
              'en': ["Oybek ('Sacred Blood')",
                     "Pirimqul Qodirov ('Starry Nights')",
                     "Mirkarim Osim ('Tomiris')",
                     "Oybek ('Navoi' Novel)"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Oybek («Navoiy» romani)', 'ru': 'Айбек (роман «Навои»)', 'en': "Oybek ('Navoi' Novel)"},
  'image_url': None,
  'fun_fact': {'uz': "Muso Toshmuhammad o'g'li Oybek 1944 yilda yaratgan «Navoiy» romani buyuk mutafakkir shoir "
                     "Alisher Navoiy hayotiga bag'ishlangan eng sara tarixiy romandir.",
               'ru': 'Роман Айбека «Навои» (1944) — вершина узбекской исторической романистики, глубоко раскрывающая '
                     'образ великого мыслителя Востока.',
               'en': "Published in 1944, Oybek's biographical novel 'Navoi' paints a magnificent panorama of "
                     '15th-century Timurid Herat.'},
  'aliases': ['navoiy romani', 'oybek', 'роман навои', 'айбек', 'oybek navoi']},
 {'id': 'lit_q_033',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Ota yurtdan ayrilmoq — tiriklayin jondan ayrilmoq bilan barobardir.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Покинуть родную землю — всё равно что расстаться с душой при жизни.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'To part from one's native land is like being ripped of one's living soul.'"},
  'options': {'uz': ['Pirimqul Qodirov («Yulduzli tunlar» romani)',
                     'Pirimqul Qodirov («Avlodlar dovoni»)',
                     "Asqad Muxtor («Bo'ronlarda bordek halovat»)",
                     'Mirkarim Osim («Zulmat ichra nur»)'],
              'ru': ['Пиримкул Кадыров (роман «Звёздные ночи» / «Бабур»)',
                     'Пиримкул Кадыров («Перевал поколений»)',
                     'Аскад Мухтар («В бурях есть покой»)',
                     'Миркарим Осим («Свет во тьме»)'],
              'en': ["Pirimqul Qodirov ('Starry Nights' / 'Babur')",
                     "Pirimqul Qodirov ('Pass of Generations')",
                     "Asqad Mukhtar ('Peace in the Tempest')",
                     "Mirkarim Osim ('Light in Darkness')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Pirimqul Qodirov («Yulduzli tunlar» romani)',
                     'ru': 'Пиримкул Кадыров (роман «Звёздные ночи» / «Бабур»)',
                     'en': "Pirimqul Qodirov ('Starry Nights' / 'Babur')"},
  'image_url': None,
  'fun_fact': {'uz': "«Yulduzli tunlar» romani Zahiriddin Muhammad Boburning murakkab va jo'shqin hayot yo'li, "
                     "Farg'onadan Hindistongacha kechgan dramatik kechinmalariga bag'ishlangan.",
               'ru': 'Исторический роман Пиримкула Кадырова проникновенно повествует о драматической судьбе Бабура и '
                     'его неугасимой тоске по Самарканду и Андижану.',
               'en': "Pirimqul Qodirov's acclaimed 1978 novel portrays Babur's youth, military campaigns, and lifelong "
                     'heartache for his native Fergana valley.'},
  'aliases': ['yulduzli tunlar', 'pirimqul qodirov', 'звёздные ночи', 'пиримкул кадыров', 'starry nights']},
 {'id': 'lit_q_034',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Nafsining quliga aylangan inson har qanday ifloslikdan qaytmaydi; vijdon yo'qolgan joyda esa "
                     'faqat shayton bazm quradi.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Человек, ставший рабом своих низменных страстей, способен на любую подлость; там, где гибнет '
                     'совесть, пирует шайтан.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'A man enslaved by his own greed hesitates at no villainy; and where conscience dies, only "
                     "devils rejoice.'"},
  'options': {'uz': ['Tohir Malik («Murdalar gapirmaydilar»)',
                     'Tohir Malik («Shaytanat» romani)',
                     "Tohir Malik («So'nggi o'q»)",
                     'Tohir Malik («Ov»)'],
              'ru': ['Тохир Малик («Мертвецы молчат»)',
                     'Тохир Малик (роман «Шайтанат»)',
                     'Тохир Малик («Последняя пуля»)',
                     'Тохир Малик («Охота»)'],
              'en': ["Tohir Malik ('The Dead Keep Silent')",
                     "Tohir Malik ('Shaytanat')",
                     "Tohir Malik ('The Last Bullet')",
                     "Tohir Malik ('The Hunt')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Tohir Malik («Shaytanat» romani)',
                     'ru': 'Тохир Малик (роман «Шайтанат»)',
                     'en': "Tohir Malik ('Shaytanat')"},
  'image_url': None,
  'fun_fact': {'uz': "Tohir Malikning «Shaytanat» kriminal dramasi o'zbek adabiyotidagi eng mashhur bestseller "
                     "asarlardan biri bo'lib, chuqur ma'naviy-falsafiy saboqlarni beradi.",
               'ru': 'Многотомный детективно-психологический роман Тохира Малика разошёлся рекордными тиражами и был '
                     'успешно экранизирован.',
               'en': "Tohir Malik's multi-volume crime saga explored organized crime and spiritual disintegration in "
                     'late Soviet and post-independence Uzbekistan.'},
  'aliases': ['shaytanat', 'tohir malik', 'шайтанат', 'тохир малик']},
 {'id': 'lit_q_035',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n\n«Haq olinur, berilmas!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Права не даруются, их завоевывают!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Rights are not granted, they are seized!'"},
  'options': {'uz': ['Abdurauf Fitrat («Munozara»)',
                     'Abdurauf Fitrat («Sayha»)',
                     'Abdurauf Fitrat («Hind ixtilochilari» dramasi)',
                     "Mahmudxo'ja Behbudiy («Padarkush»)"],
              'ru': ['Абдурауф Фитрат («Спор»)',
                     'Абдурауф Фитрат («Крик»)',
                     'Абдурауф Фитрат (драма «Индийские мятежники»)',
                     'Махмудходжа Бехбуди («Падаркуш»)'],
              'en': ["Abdurauf Fitrat ('The Dispute')",
                     "Abdurauf Fitrat ('The Cry')",
                     "Abdurauf Fitrat ('Indian Rebels' Drama)",
                     "Mahmudkhoja Behbudi ('The Patricide')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Abdurauf Fitrat («Hind ixtilochilari» dramasi)',
                     'ru': 'Абдурауф Фитрат (драма «Индийские мятежники»)',
                     'en': "Abdurauf Fitrat ('Indian Rebels' Drama)"},
  'image_url': None,
  'fun_fact': {'uz': 'Jadidchilik yetakchisi Abdurauf Fitratning 1923 yilda Berlinda chop etilgan bu mashhur iborasi '
                     'milliy ozodlik harakatining bosh shioriga aylangan.',
               'ru': 'Пламенный призыв лидера джадидов Абдурауфа Фитрата стал символом национального освобождения '
                     'народов Востока.',
               'en': "Fitrat's resounding rallying cry in Berlin in 1923 inspired anti-colonial and reformist "
                     'movements across early 20th-century Central Asia.'},
  'aliases': ['fitrat', 'hind ixtilochilari', 'haq olinur berilmas', 'фитрат', 'индийские мятежники']},
 {'id': 'lit_q_036',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Kuy kuyla, ma'buda, Axillning g'azabi haqida...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Гнев, богиня, воспой Ахиллеса, Пелеева сына...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Sing, O goddess, the anger of Achilles son of Peleus...'"},
  'options': {'uz': ['Gomer («Odisseya»)', 'Vergiliy («Eneida»)', 'Gesiod («Teogoniya»)', 'Gomer («Iliada» dostoni)'],
              'ru': ['Гомер («Одиссея»)', 'Вергилий («Энеида»)', 'Гесиод («Теогония»)', 'Гомер (поэма «Илиада»)'],
              'en': ["Homer ('The Odyssey')", "Virgil ('The Aeneid')", "Hesiod ('Theogony')", "Homer ('The Iliad')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Gomer («Iliada» dostoni)', 'ru': 'Гомер (поэма «Илиада»)', 'en': "Homer ('The Iliad')"},
  'image_url': None,
  'fun_fact': {'uz': 'Qadimgi Yunonistonning eng buyuk eposi «Iliada» aynan shu jumlalar bilan boshlanadi va Troya '
                     "qamalining o'ninchi yilidagi fojialarni kuylaydi.",
               'ru': 'Знаменитый зачин древнегреческого эпоса Гомера VIII века до н.э., задающий главную тему '
                     'Троянской войны.',
               'en': "The monumental opening line of Western literature's oldest surviving epic, establishing the "
                     'tragic wrath of Achilles.'},
  'aliases': ['iliada', 'gomer', 'илиада', 'гомер', 'iliad', 'homer']},
 {'id': 'lit_q_037',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Kuy kuyla, ey Muza, o'sha epchil, ayyor qahramon haqida...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Муза, скажи мне о том многоопытном муже, который, странствуя долго со дня, как святой Илион '
                     'разорил он...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Tell me, O Muse, of that ingenious hero who travelled far and wide after he had sacked the "
                     "famous citadel of Troy...'"},
  'options': {'uz': ['Gomer («Odisseya» dostoni)',
                     'Gomer («Iliada»)',
                     'Ovidiy («Metamorfozalar»)',
                     'Apolloniy Rodoslik («Argonavtika»)'],
              'ru': ['Гомер (поэма «Одиссея»)',
                     'Гомер («Илиада»)',
                     'Овидий («Метаморфозы»)',
                     'Аполлоний Родосский («Аргонавтика»)'],
              'en': ["Homer ('The Odyssey')",
                     "Homer ('The Iliad')",
                     "Ovid ('Metamorphoses')",
                     "Apollonius of Rhodes ('Argonautica')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Gomer («Odisseya» dostoni)',
                     'ru': 'Гомер (поэма «Одиссея»)',
                     'en': "Homer ('The Odyssey')"},
  'image_url': None,
  'fun_fact': {'uz': 'Gomerning ushbu ikkinchi dostoni Itaka shohi Odisseyning Troya urushidan keyin 10 yil davom '
                     'etgan vataniga qaytish mashaqqatlarini tasvirlaydi.',
               'ru': 'Первая песнь поэмы Гомера о десятилетних странствиях хитроумного царя Итаки Одиссея по пути '
                     'домой к Пенелопе.',
               'en': "The invocation opening Homer's epic voyage of Odysseus struggling against monsters, sirens, and "
                     'gods to return home to Ithaca.'},
  'aliases': ['odisseya', 'gomer', 'одиссея', 'гомер', 'odyssey', 'homer']},
 {'id': 'lit_q_038',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Orzulardan voz kechish — telbalikning eng dahshatlisidir; dunyoni boricha emas, qanday bo'lishi "
                     "kerak bo'lsa, shunday ko'rish lozim!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Самое худшее безумие — видеть мир таким, какой он есть, а не таким, каким он должен быть!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Too much sanity may be madness — and maddest of all: to see life as it is, and not as it should "
                     "be!'"},
  'options': {'uz': ["Lope de Vega («Qo'radagi it»)",
                     'Migel de Servantes («Don Kixot»)',
                     'Pedro Kalderon («Hayot — bu tush»)',
                     'Fransua Rable («Gargantyua va Pantagryuel»)'],
              'ru': ['Лопе де Вега («Собака на сене»)',
                     'Мигель де Сервантес («Дон Кихот»)',
                     'Педро Кальдерон («Жизнь есть сон»)',
                     'Франсуа Рабле («Гаргантюа и Пантагрюэль»)'],
              'en': ["Lope de Vega ('The Dog in the Manger')",
                     "Miguel de Cervantes ('Don Quixote')",
                     "Pedro Calderón de la Barca ('Life Is a Dream')",
                     "François Rabelais ('Gargantua and Pantagruel')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Migel de Servantes («Don Kixot»)',
                     'ru': 'Мигель де Сервантес («Дон Кихот»)',
                     'en': "Miguel de Cervantes ('Don Quixote')"},
  'image_url': None,
  'fun_fact': {'uz': "1605 yilda e'lon qilingan La-Manchalik olijanob ritsar Don Kixot va uning qurolbardori Sancho "
                     "Pansa sarguzashtlari jahonning eng ko'p tarjima qilingan asaridir.",
               'ru': 'Роман Сервантеса об идальго Дон Кихоте Ламанчском стал вечным гимном благородному идеализму и '
                     'борьбе с ветряными мельницами.',
               'en': "Cervantes's 1605 masterpiece fundamentally defined modern fiction, celebrating idealism against "
                     'cynical realism.'},
  'aliases': ['don kixot', 'servantes', 'дон кихот', 'сервантес', 'don quixote', 'cervantes']},
 {'id': 'lit_q_039',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Agar dushmaningni bilsang va o'zingni bilsang, yuzlab janglarda ham mag'lubiyat xavfi ostida "
                     'qolmaysan.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Если знаешь врага и знаешь себя, ты победишь в сотне битв без опасности поражения.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'If you know the enemy and know yourself, you need not fear the result of a hundred battles.'"},
  'options': {'uz': ['Konfutsiy («Suhbatlar va mulohazalar»)',
                     'Lao-tszi («Dao De Szin»)',
                     "Sun Tszi («Harb san'ati»)",
                     'Nikkkolo Makiavelli («Hukmdor»)'],
              'ru': ['Конфуций («Беседы и суждения»)',
                     'Лао-цзы («Дао Дэ Цзин»)',
                     'Сунь-цзы («Искусство войны»)',
                     'Никколо Макиавелли («Государь»)'],
              'en': ["Confucius ('Analects')",
                     "Laozi ('Tao Te Ching')",
                     "Sun Tzu ('The Art of War')",
                     "Niccolò Machiavelli ('The Prince')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Sun Tszi («Harb san'ati»)",
                     'ru': 'Сунь-цзы («Искусство войны»)',
                     'en': "Sun Tzu ('The Art of War')"},
  'image_url': None,
  'fun_fact': {'uz': 'Miloddan avvalgi V asrga oid qadimgi Xitoy harbiy risolasi bugungi kunda ham strategiya, '
                     "diplomatiya va boshqaruvning asosiy qo'llanmasidir.",
               'ru': 'Основополагающий постулат трактата Сунь-цзы V века до н.э., изучаемый военными академиями и '
                     'лидерами бизнеса по всему миру.',
               'en': "Dating to roughly the 5th century BC, Sun Tzu's strategic treatise remains timeless required "
                     'reading for commanders and negotiators.'},
  'aliases': ["harb san'ati", 'sun tszi', 'искусство войны', 'сунь-цзы', 'art of war', 'sun tzu']},
 {'id': 'lit_q_040',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Jim bo'l! Sukut — dengizdir, so'z esa — daryo. Dengiz seni chaqirayotganda, daryo bo'lib oqma!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Молчи! Безмолвие — океан, а слова — лишь реки. Когда зовёт тебя океан, не устремляйся в ручей!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Silence is an ocean. Speech is a river. When the ocean is searching for you, don't walk into "
                     "the river!'"},
  'options': {'uz': ['Shams Tabriziy («Maqolot»)',
                     'Farididdin Attor («Mantiq ut-tayr»)',
                     'Hofiz Sheroziy («Devon»)',
                     "Jaloliddin Rumiy («Masnaviyi ma'naviy»)"],
              'ru': ['Шамс Тебризи («Беседы»)',
                     'Фаридаддин Аттар («Язык птиц»)',
                     'Хафиз Ширази («Диван»)',
                     'Джалаладдин Руми («Маснави»)'],
              'en': ["Shams Tabrizi ('Maqalat')",
                     "Farid ud-Din Attar ('The Conference of the Birds')",
                     "Hafez ('Divan')",
                     "Jalaluddin Rumi ('Masnavi')"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Jaloliddin Rumiy («Masnaviyi ma'naviy»)",
                     'ru': 'Джалаладдин Руми («Маснави»)',
                     'en': "Jalaluddin Rumi ('Masnavi')"},
  'image_url': None,
  'fun_fact': {'uz': "Mavlono Rumiyning «Masnaviy» asari tasavvuf falsafasining cho'qqisi bo'lib, 'Qur'onning "
                     "pahlaviycha (forscha) talqini' deb e'tirof etilgan.",
               'ru': 'Джалаладдин Руми — великий суфийский поэт XIII века, чья монументальная поэма «Маснави» '
                     'прославляет божественную любовь и духовную тишину.',
               'en': "Rumi's 13th-century 'Masnavi' is revered across the Islamic and Western world as the summit of "
                     'mystical spiritual philosophy.'},
  'aliases': ['rumiy', 'jaloliddin rumiy', 'masnaviy', 'руми', 'джалаладдин руми', 'маснави']},
 {'id': 'lit_q_041',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Bani odam a'zoyi yakdigarand,\n"
                     'Ki dar ofarinish zi yak gavharand.\n'
                     "Chu uzve ba dard ovarad ro'zgor,\n"
                     'Digar uzvhoro namonad qaror.»\n'
                     "(Odam bolalari bir vujud a'zolaridir...)",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Все племя Адамово — тело одно,\n'
                     'Из праха единого сотворено.\n'
                     'Коль тело одну лишь постигнет беда,\n'
                     'То стонут другие части всегда.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Human beings are members of a whole,\n"
                     'In creation of one essence and soul.\n'
                     'If one member is afflicted with pain,\n'
                     "Other members uneasy will remain.'"},
  'options': {'uz': ["Sa'diy Sheroziy («Guliston»)",
                     "Sa'diy Sheroziy («Bo'ston»)",
                     'Hofiz Sheroziy («Devon»)',
                     'Jomiy («Bahoriston»)'],
              'ru': ['Саади Ширази («Гулистан»)',
                     'Саади Ширази («Бустан»)',
                     'Хафиз Ширази («Диван»)',
                     'Джами («Бахаристан»)'],
              'en': ["Saadi Shirazi ('Gulistan')",
                     "Saadi Shirazi ('Bustan')",
                     "Hafez ('Divan')",
                     "Jami ('Baharistan')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Sa'diy Sheroziy («Guliston»)",
                     'ru': 'Саади Ширази («Гулистан»)',
                     'en': "Saadi Shirazi ('Gulistan')"},
  'image_url': None,
  'fun_fact': {'uz': "Sa'diy Sheroziyning «Guliston» (1258 y.) asaridagi ushbu mashhur she'r BMTning Nyu-Yorkdagi Bosh "
                     'qarorgohi kirish zaliga oltin harflar bilan bitilgan.',
               'ru': 'Эти строки персидского поэта Саади XIII века выбиты золотыми буквами при входе в штаб-квартиру '
                     'ООН в Нью-Йорке.',
               'en': 'Penned by Saadi of Shiraz in 1258, these immortal lines on universal human kinship adorn the '
                     'entrance of the United Nations headquarters.'},
  'aliases': ["sa'diy", 'guliston', 'саади', 'гулистан', 'saadi', 'bani odam']},
 {'id': 'lit_q_042',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Bir ko'za may bo'lsa-yu, yarimta non,\n"
                     "Va bir go'zal yor bilan sahro bo'lsa makon —\n"
                     "O'shal sahro menga jannatdan afzal!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Кувшин вина, кусок лепешки хлеба,\n'
                     'Любимая под сенью чистого неба —\n'
                     'Вот рай земной! Султан в своём дворце\n'
                     'Не знает счастья, равного победе.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'A Book of Verses underneath the Bough,\n"
                     'A Jug of Wine, a Loaf of Bread — and Thou\n'
                     'Beside me singing in the Wilderness —\n'
                     "Oh, Wilderness were Paradise enow!'"},
  'options': {'uz': ["Hofiz Sheroziy (G'azallar)",
                     'Umar Xayyom (Ruboiylar)',
                     'Bobur (Ruboiylar)',
                     'Ibn Sino (Hikmatlar)'],
              'ru': ['Хафиз Ширази (Газели)', 'Омар Хайям (Рубаи)', 'Бабур (Рубаи)', 'Ибн Сина (Четверостишия)'],
              'en': ['Hafez (Ghazals)', 'Omar Khayyam (Rubaiyat)', 'Babur (Rubaiyat)', 'Avicenna (Quatrains)']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Umar Xayyom (Ruboiylar)', 'ru': 'Омар Хайям (Рубаи)', 'en': 'Omar Khayyam (Rubaiyat)'},
  'image_url': None,
  'fun_fact': {'uz': 'XI-XII asrlarda yashagan buyuk matematik, astronom va faylasuf Umar Xayyomning ruboiylari Edvard '
                     "Fitsjerald tarjimasida butun dunyoga mashhur bo'lgan.",
               'ru': 'Знаменитое четверостишие Омара Хайяма, прославленное на Западе классическим переводом Эдварда '
                     'Фицджеральда 1859 года.',
               'en': 'Translated by Edward FitzGerald in 1859, this quatrain became one of the most widely quoted '
                     'poetic stanzas in world literature.'},
  'aliases': ['umar xayyom', 'xayyom', 'ruboiy', 'омар хайям', 'хайям', 'omar khayyam']},
 {'id': 'lit_q_043',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Menga darmon kerakmas, dardimning o'zi davodir,\n"
                     'Majnun holin bilmagan qalb ishqdan judodir...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Мне лекарь не нужен, сама болезнь моя — исцеленье,\n'
                     'Кто не ведал безумства любви, тот не знает спасенья...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Seek not to heal my sorrow, for love's affliction is my remedy;\n"
                     "He who never knew love's madness lives in spiritual poverty...'"},
  'options': {'uz': ['Alisher Navoiy («Layli va Majnun»)',
                     'Fuzuliy («Layli va Majnun»)',
                     'Nizomiy Ganjaviy («Layli va Majnun»)',
                     'Amir Xusrav Dehlaviy («Majnun va Layli»)'],
              'ru': ['Алишер Навои («Лейли и Меджнун»)',
                     'Физули («Лейли и Меджнун»)',
                     'Низами Гянджеви («Лейли и Меджнун»)',
                     'Амир Хосров Дехлеви («Меджнун и Лейли»)'],
              'en': ["Alisher Navoi ('Layla and Majnun')",
                     "Fuzuli ('Layla and Majnun')",
                     "Nizami Ganjavi ('Layla and Majnun')",
                     "Amir Khusrow ('Majnun and Layla')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Nizomiy Ganjaviy («Layli va Majnun»)',
                     'ru': 'Низами Гянджеви («Лейли и Меджнун»)',
                     'en': "Nizami Ganjavi ('Layla and Majnun')"},
  'image_url': None,
  'fun_fact': {'uz': 'XII asrda yashagan Nizomiy Ganjaviy Sharq adabiyotida «Layli va Majnun» afsonasini mustaqil '
                     "doston sifatida birinchi bo'lib qalamga olgan.",
               'ru': 'Низами первым в 1188 году превратил полулегендарную арабскую притчу о любви Кайса и Лейли в '
                     'бессмертную романтическую поэму.',
               'en': 'In 1188, Persian poet Nizami Ganjavi composed the first definitive narrative poem of the tragic '
                     'desert lovers Qays and Layla.'},
  'aliases': ['layli va majnun', 'nizomiy', 'лейли и меджнун', 'низами', 'nizami']},
 {'id': 'lit_q_044',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Yillar o'tib shamol va yomg'irlar qasrlarni yemirar,\n"
                     "Ammo men so'zdan bino etgan bu muhtasham saroyga asrlar ham ziyon yetkaza olmas!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Дворцы и башни рушатся от бурь и непогод,\n'
                     'Но замок слова, возведённый мной, века переживёт!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Buildings of stone crumble before wind and rain,\n"
                     "Yet the palace of verses I have raised shall ever endure without stain!'"},
  'options': {'uz': ['Alisher Navoiy («Saddi Iskandariy»)',
                     'Nizomiy Ganjaviy («Iskandarnoma»)',
                     'Rudakiy («Kalila va Dimna»)',
                     'Abulqosim Firdavsiy («Shohnoma» xotimasi)'],
              'ru': ['Алишер Навои («Вал Искандара»)',
                     'Низами Гянджеви («Искандер-наме»)',
                     'Рудаки («Калила и Димна»)',
                     'Абулькасим Фирдоуси (финал эпопеи «Шахнаме»)'],
              'en': ["Alisher Navoi ('Sadd-i Iskandari')",
                     "Nizami Ganjavi ('Iskandarnama')",
                     "Rudaki ('Kalila and Dimna')",
                     "Ferdowsi (epilogue of 'Shahnameh')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Abulqosim Firdavsiy («Shohnoma» xotimasi)',
                     'ru': 'Абулькасим Фирдоуси (финал эпопеи «Шахнаме»)',
                     'en': "Ferdowsi (epilogue of 'Shahnameh')"},
  'image_url': None,
  'fun_fact': {'uz': 'Firdavsiy 30 yildan ortiq vaqt mobaynida 50 000 dan ziyod baytdan iborat «Shohnoma» eposini '
                     "yozib, qadimgi Eron va Turon tarixini so'z san'atida abadiylashtirgan.",
               'ru': 'Фирдоуси создавал грандиозную эпопею «Шахнаме» более 30 лет, обессмертив историю царей и подвиги '
                     'богатыря Рустама.',
               'en': "Ferdowsi spent over three decades crafting the 50,000 rhyming couplets of the 'Shahnameh' (Book "
                     'of Kings), reviving Persian language and lore.'},
  'aliases': ['shohnoma', 'firdavsiy', 'шахнаме', 'фирдоуси', 'shahnameh', 'ferdowsi']},
 {'id': 'lit_q_045',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Men sizni sevardim: ehtimol sevgim\n'
                     "Qalbimda hali butunlay so'nmagandir...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Я вас любил: любовь ещё, быть может,\n'
                     'В душе моей угасла не совсем...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'I loved you once: and love perhaps is yet\n"
                     "Within my soul not quite extinguished...'"},
  'options': {'uz': ["Aleksandr Pushkin («Men sizni sevardim...» she'ri)",
                     'Aleksandr Pushkin («Yevgeniy Onegin»)',
                     'Mixail Lermontov («Yelkan»)',
                     'Fyodor Tyutchev («Silentium!»)'],
              'ru': ['Александр Пушкин («Я вас любил: любовь ещё, быть может...»)',
                     'Александр Пушкин («Евгений Онегин»)',
                     'Михаил Лермонтов («Парус»)',
                     'Фёдор Тютчев («Silentium!»)'],
              'en': ["Alexander Pushkin ('I Loved You Once')",
                     "Alexander Pushkin ('Eugene Onegin')",
                     "Mikhail Lermontov ('The Sail')",
                     "Fyodor Tyutchev ('Silentium!')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Aleksandr Pushkin («Men sizni sevardim...» she'ri)",
                     'ru': 'Александр Пушкин («Я вас любил: любовь ещё, быть может...»)',
                     'en': "Alexander Pushkin ('I Loved You Once')"},
  'image_url': None,
  'fun_fact': {'uz': '1829 yilda yozilgan ushbu 8 qatorlik lirik durdona buyuk rus shoiri Pushkinning sevgi va '
                     'fidoiylik haqidagi eng yuksak asarlaridan biridir.',
               'ru': 'Восьмистишие Пушкина 1829 года — непревзойдённый шедевр мировой любовной лирики, гимн '
                     'бескорыстному и благородному чувству.',
               'en': 'Written in 1829, this exquisite eight-line lyric stands as one of the most famous declarations '
                     'of noble, selfless love in world literature.'},
  'aliases': ['pushkin', 'men sizni sevardim', 'пушкин', 'я вас любил', 'i loved you once']},
 {'id': 'lit_q_046',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Insonning yuzi ham, kiyimi ham, qalbi ham, fikrlari ham — hamma narsasi go'zal bo'lishi kerak.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«В человеке должно быть всё прекрасно: и лицо, и одежда, и душа, и мысли.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Everything about a human being should be beautiful: the face, the clothes, the soul, and the "
                     "thoughts.'"},
  'options': {'uz': ['Anton Chexov («Chayka»)',
                     "Anton Chexov («Vanya tog'a» pesasi)",
                     'Anton Chexov («Olchazor»)',
                     'Maksim Gorkiy («Tubanlikda»)'],
              'ru': ['Антон Чехов («Чайка»)',
                     'Антон Чехов (пьеса «Дядя Ваня» — доктор Астров)',
                     'Антон Чехов («Вишнёвый сад»)',
                     'Максим Горький («На дне»)'],
              'en': ["Anton Chekhov ('The Seagull')",
                     "Anton Chekhov ('Uncle Vanya' — Dr. Astrov)",
                     "Anton Chekhov ('The Cherry Orchard')",
                     "Maxim Gorky ('The Lower Depths')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Anton Chexov («Vanya tog'a» pesasi)",
                     'ru': 'Антон Чехов (пьеса «Дядя Ваня» — доктор Астров)',
                     'en': "Anton Chekhov ('Uncle Vanya' — Dr. Astrov)"},
  'image_url': None,
  'fun_fact': {'uz': "Anton Chexovning «Vanya tog'a» pesasida doktor Astrov tilidan aytilgan bu jumla insoniy "
                     'barkamollikning qanotli iborasiga aylangan.',
               'ru': 'Слова доктора Астрова во втором действии чеховской драмы «Дядя Ваня» стали всемирно известным '
                     'этико-эстетическим кредо.',
               'en': "Spoken by Dr. Astrov in Act 2 of Chekhov's 1898 play, this line remains an iconic standard of "
                     'holistic human beauty and integrity.'},
  'aliases': ['chexov', "vanya tog'a", 'чехов', 'дядя ваня', 'в человеке все прекрасно', 'uncle vanya']},
 {'id': 'lit_q_047',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Meni tinch qo'ying, nega meni ranjitasiz? Axir men sizning birodaringizman-ku!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Оставьте меня, зачем вы меня обижаете? Ведь я брат твой!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Leave me alone, why do you torment me? Am I not your brother?!'"},
  'options': {'uz': ['Nikolay Gogol («Revizor»)',
                     "Nikolay Gogol («O'lik jonlar»)",
                     'Nikolay Gogol («Shinel» qissasi)',
                     'Nikolay Gogol («Taras Bulba»)'],
              'ru': ['Николай Гоголь («Ревизор»)',
                     'Николай Гоголь («Мёртвые души»)',
                     'Николай Гоголь (повесть «Шинель» — Акакий Акакиевич)',
                     'Николай Гоголь («Тарас Бульба»)'],
              'en': ["Nikolai Gogol ('The Government Inspector')",
                     "Nikolai Gogol ('Dead Souls')",
                     "Nikolai Gogol ('The Overcoat' — Akaky Akakievich)",
                     "Nikolai Gogol ('Taras Bulba')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Nikolay Gogol («Shinel» qissasi)',
                     'ru': 'Николай Гоголь (повесть «Шинель» — Акакий Акакиевич)',
                     'en': "Nikolai Gogol ('The Overcoat' — Akaky Akakievich)"},
  'image_url': None,
  'fun_fact': {'uz': "Kichik xizmatchi Akakiy Akakiyevich Bashmachkinning bu faryodi jahon adabiyotida 'mitti odam' "
                     "dardini ifodalagan eng ta'sirli sahnadir.",
               'ru': 'Пронзительный вопль маленького титулярного советника Акакия Акакиевича, ставший манифестом '
                     'сострадания к «маленькому человеку».',
               'en': "The heart-wrenching plea of Akaky Akakievich in Gogol's 1842 masterpiece, which birthed the "
                     "humanitarian theme of the 'little man'."},
  'aliases': ['shinel', 'gogol', 'шинель', 'гоголь', 'the overcoat']},
 {'id': 'lit_q_048',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Tabiat ibodatxona emas, u ustaxonadir, inson esa unda ishchidir.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Природа не храм, а мастерская, и человек в ней работник.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Nature is not a temple, but a workshop, and man's the workman in it.'"},
  'options': {'uz': ['Ivan Turgenev («Rudin»)',
                     'Ivan Turgenev («Asya»)',
                     'Ivan Goncharov («Oblomov»)',
                     'Ivan Turgenev («Otalar va bolalar» — Bazarov)'],
              'ru': ['Иван Тургенев («Рудин»)',
                     'Иван Тургенев («Ася»)',
                     'Иван Гончаров («Обломов»)',
                     'Иван Тургенев («Отцы и дети» — Евгений Базаров)'],
              'en': ["Ivan Turgenev ('Rudin')",
                     "Ivan Turgenev ('Asya')",
                     "Ivan Goncharov ('Oblomov')",
                     "Ivan Turgenev ('Fathers and Sons' — Bazarov)"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ivan Turgenev («Otalar va bolalar» — Bazarov)',
                     'ru': 'Иван Тургенев («Отцы и дети» — Евгений Базаров)',
                     'en': "Ivan Turgenev ('Fathers and Sons' — Bazarov)"},
  'image_url': None,
  'fun_fact': {'uz': 'Bosh qahramon Yevgeniy Bazarovning pragmatik nigilizmi va tabiatga utilitarian munosabatini '
                     'ifodalagan mashhur fikr.',
               'ru': 'Ключевое кредо нигилиста Евгения Базарова, отвергавшего отвлечённое романтическое любование '
                     'природой ради науки.',
               'en': "Spoken by the iconic nihilist hero Yevgeny Bazarov in Turgenev's 1862 generational confrontation "
                     'novel.'},
  'aliases': ['otalar va bolalar', 'turgenev', 'отцы и дети', 'тургенев', 'bazarov', 'fathers and sons']},
 {'id': 'lit_q_049',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Men butun dunyoni sevishga tayyor edim — meni hech kim tushunmadi: va men nafratlanishni '
                     "o'rgandim.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Я был готов любить весь мир, — меня никто не понял: и я выучился ненавидеть.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'I was ready to love the whole world — no one understood me, so I learned to hate.'"},
  'options': {'uz': ['Mixail Lermontov («Zamonamiz qahramoni» — Pechorin)',
                     'Mixail Lermontov («Mtsiri»)',
                     'Mixail Lermontov («Maskarad»)',
                     'Aleksandr Griboyedov («Aqllilik balosi»)'],
              'ru': ['Михаил Лермонтов («Герой нашего времени» — Печорин)',
                     'Михаил Лермонтов («Мцыри»)',
                     'Михаил Лермонтов («Маскарад»)',
                     'Александр Грибоедов («Горе от ума»)'],
              'en': ["Mikhail Lermontov ('A Hero of Our Time' — Pechorin)",
                     "Mikhail Lermontov ('Mtsyri')",
                     "Mikhail Lermontov ('Masquerade')",
                     "Aleksandr Griboyedov ('Woe from Wit')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Mixail Lermontov («Zamonamiz qahramoni» — Pechorin)',
                     'ru': 'Михаил Лермонтов («Герой нашего времени» — Печорин)',
                     'en': "Mikhail Lermontov ('A Hero of Our Time' — Pechorin)"},
  'image_url': None,
  'fun_fact': {'uz': "Grigoriy Pechorinning malika Meri bilan suhbatdagi iqrori; Lermontov 'ortiqcha odam'ning fojiali "
                     "qalb parchalanishini ko'rsatgan.",
               'ru': 'Исповедь Печорина княжне Мери в Пятигорске, раскрывающая драму разочарованного и лишнего '
                     'человека николаевской эпохи.',
               'en': "Pechorin's cynical confession to Princess Mary in Lermontov's landmark 1840 psychological "
                     'novel.'},
  'aliases': ['zamonamiz qahramoni', 'lermontov', 'герой нашего времени', 'лермонтов', 'pechorin']},
 {'id': 'lit_q_050',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Kitoblarni yoqishdan ko'ra og'irroq jinoyatlar bor. Masalan, ularni o'qimaslik!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Есть преступления хуже, чем сжигать книги. Например — не читать их!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'There are worse crimes than burning books. One of them is not reading them!'"},
  'options': {'uz': ['Rey Bredberi («Mars yilnomalari»)',
                     "Rey Bredberi («Farengeyt bo'yicha 451 daraja»)",
                     'Rey Bredberi («Momaqaymoq vinosi»)',
                     'Oldos Xaksli («Ajib yangi dunyo»)'],
              'ru': ['Рэй Брэдбери («Марсианские хроники»)',
                     'Рэй Брэдбери («451 градус по Фаренгейту»)',
                     'Рэй Брэдбери («Вино из одуванчиков»)',
                     'Олдос Хаксли («О дивный новый мир»)'],
              'en': ["Ray Bradbury ('The Martian Chronicles')",
                     "Ray Bradbury ('Fahrenheit 451')",
                     "Ray Bradbury ('Dandelion Wine')",
                     "Aldous Huxley ('Brave New World')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Rey Bredberi («Farengeyt bo'yicha 451 daraja»)",
                     'ru': 'Рэй Брэдбери («451 градус по Фаренгейту»)',
                     'en': "Ray Bradbury ('Fahrenheit 451')"},
  'image_url': None,
  'fun_fact': {'uz': "Kitoblar taqiqlangan va o't o'chiruvchilar kitoblarni yoqish bilan shug'ullanadigan kelajak "
                     "jamiyati haqidagi ushbu asar ma'naviyatning oliy himoyasidir.",
               'ru': 'Предостережение Рэя Брэдбери в его антиутопии 1953 года об опасности бездумного потребительства '
                     'и утраты культуры чтения.',
               'en': "Ray Bradbury's enduring warning against censorship, anti-intellectualism, and mass indifference "
                     'toward literature.'},
  'aliases': ['451', 'bredberi', 'farengeyt 451', 'рэй брэдбери', '451 градус по фаренгейту', 'fahrenheit 451']},
 {'id': 'lit_q_051',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Farzandlaringiz — sizning farzandlaringiz emas. Ular Hayotning o'z-o'ziga bo'lgan intilishining "
                     "o'g'il-qizlaridir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Ваши дети — это не ваши дети. Они сыновья и дочери тоски Жизни по самой себе.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Your children are not your children. They are the sons and daughters of Life's longing for "
                     "itself.'"},
  'options': {'uz': ['Rabindranat Tagor («Gitanjali»)',
                     'Jaloliddin Rumiy («Fiyhi mo fiyh»)',
                     "Xalil Jibron («Payg'ambar»)",
                     'Amin ar-Rayhoniy («Haramxon qissalari»)'],
              'ru': ['Рабиндранат Тагор («Гитанджали»)',
                     'Джалаладдин Руми («В нём то, что в нём»)',
                     'Халиль Джебран («Пророк»)',
                     'Амин ар-Рейхани («Повести»)'],
              'en': ["Rabindranath Tagore ('Gitanjali')",
                     "Jalaluddin Rumi ('Fihi Ma Fihi')",
                     "Kahlil Gibran ('The Prophet')",
                     "Ameen Rihani ('The Book of Khalid')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Xalil Jibron («Payg'ambar»)",
                     'ru': 'Халиль Джебран («Пророк»)',
                     'en': "Kahlil Gibran ('The Prophet')"},
  'image_url': None,
  'fun_fact': {'uz': "Livanlik buyuk faylasuf-adib Xalil Jibronning 1923 yilda ingliz tilida chop etilgan «Payg'ambar» "
                     'kitobi jahon falsafiy poeziyasining durdonasidir.',
               'ru': 'Поэтический шедевр Халиля Джебрана 1923 года переведён более чем на 100 языков мира и разошёлся '
                     'десятками миллионов тиражей.',
               'en': "Kahlil Gibran's 1923 book of poetic essays remains one of the best-selling books of all time, "
                     'translated into over 100 languages.'},
  'aliases': ['xalil jibron', "payg'ambar", 'халиль джебран', 'пророк', 'kahlil gibran', 'the prophet']},
 {'id': 'lit_q_052',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Qayerdaki aql qo'rquvdan xoli bo'lsa va inson boshi mag'rur ko'tarilsa; qayerdaki bilim barcha "
                     "uchun ozod va ochiq bo'lsa...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Там, где мысль свободна от страха и гордо поднята голова; где знание открыто для всех...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Where the mind is without fear and the head is held high; Where knowledge is free...'"},
  'options': {'uz': ['Rabindranat Tagor («Halokat»)',
                     'Sarojini Naidu («Oltin ostonalar»)',
                     'Aurobindo Gxosh («Savitri»)',
                     "Rabindranat Tagor («Gitanjali» — 35-she'r)"],
              'ru': ['Рабиндранат Тагор («Крушение»)',
                     'Сароджини Найду («Золотой порог»)',
                     'Ауробиндо Гхош («Савитри»)',
                     'Рабиндранат Тагор («Гитанджали» — Жертвопесни)'],
              'en': ["Rabindranath Tagore ('The Wreck')",
                     "Sarojini Naidu ('The Golden Threshold')",
                     "Sri Aurobindo ('Savitri')",
                     "Rabindranath Tagore ('Gitanjali' — Song Offerings)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Rabindranat Tagor («Gitanjali» — 35-she'r)",
                     'ru': 'Рабиндранат Тагор («Гитанджали» — Жертвопесни)',
                     'en': "Rabindranath Tagore ('Gitanjali' — Song Offerings)"},
  'image_url': None,
  'fun_fact': {'uz': "1913 yilda «Gitanjali» to'plami uchun Rabindranat Tagor adabiyot bo'yicha Nobel mukofotini "
                     "qo'lga kiritgan birinchi osiyolik ijodkor bo'ldi.",
               'ru': 'В 1913 году Тагор стал первым неевропейским лауреатом Нобелевской премии по литературе именно за '
                     'этот поэтический сборник.',
               'en': 'In 1913 Tagore became the first non-European Nobel laureate in Literature for his spiritual and '
                     "patriotic 'Gitanjali'."},
  'aliases': ['tagor', 'rabindranat tagor', 'gitanjali', 'тагор', 'рабиндранат тагор', 'гитанджали']},
 {'id': 'lit_q_053',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Meni o'ldirmagan har qanday sinov — meni yanada kuchliroq qiladi!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«То, что меня не убивает, делает меня сильнее!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'What does not kill me makes me stronger!'"},
  'options': {'uz': ["Fridrix Nitsshe («Butlar g'urubi» / «Zardusht tavallosi»)",
                     'Artur Shopengauer («Hayotiy donolik aforizmlari»)',
                     'Immanuil Kant («Sof aql tanqidi»)',
                     'Georq Gegel («Ruh fenomenologiyasi»)'],
              'ru': ['Фридрих Ницше («Сумерки идолов» / «Так говорил Заратустра»)',
                     'Артур Шопенгауэр («Афоризмы житейской мудрости»)',
                     'Иммануил Кант («Критика чистого разума»)',
                     'Георг Гегель («Феноменология духа»)'],
              'en': ["Friedrich Nietzsche ('Twilight of the Idols' / 'Zarathustra')",
                     "Arthur Schopenhauer ('Aphorisms')",
                     "Immanuel Kant ('Critique of Pure Reason')",
                     "Georg Wilhelm Friedrich Hegel ('Phenomenology of Spirit')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Fridrix Nitsshe («Butlar g'urubi» / «Zardusht tavallosi»)",
                     'ru': 'Фридрих Ницше («Сумерки идолов» / «Так говорил Заратустра»)',
                     'en': "Friedrich Nietzsche ('Twilight of the Idols' / 'Zarathustra')"},
  'image_url': None,
  'fun_fact': {'uz': 'Nemis faylasufi Fridrix Nitsshening 1889 yildagi ushbu aforizmi inson ruhiy qudrati va '
                     'toblanishining mashhur timsoliga aylangan.',
               'ru': 'Знаменитый восьмой афоризм Ницше из раздела «Стрелы и изречения» книги «Сумерки идолов» (1889).',
               'en': "Nietzsche's famous maxim from 'Twilight of the Idols' (1889) encapsulating his philosophy of "
                     'resilience and overcoming.'},
  'aliases': ['nitsshe', 'ницше', 'что не убивает', 'what does not kill me', 'nietzsche']},
 {'id': 'lit_q_054',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Hukmdor uchun sevimlilikdan ko'ra, qo'rquv uyg'otmoq ancha xavfsizroqdir, chunki odamlar o'z "
                     "manfaatlariga ko'ra yaxshi ko'radilar...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Для государя куда безопаснее внушать страх, нежели любовь, ибо любовь держится узами '
                     'благодарности, которые люди легко рвут...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'It is much safer to be feared than loved, if one cannot be both...'"},
  'options': {'uz': ['Tomas Gobbs («Leviafan»)',
                     'Nikkolo Makiavelli («Hukmdor» risolasi)',
                     'Jan-Jak Russo («Ijtimoiy shartnoma»)',
                     'Jon Lokk («Hukumat haqida ikki risola»)'],
              'ru': ['Томас Гоббс («Левиафан»)',
                     'Никколо Макиавелли (трактат «Государь»)',
                     'Жан-Жак Руссо («Об общественном договоре»)',
                     'Джон Локк («Два трактата о правлении»)'],
              'en': ["Thomas Hobbes ('Leviathan')",
                     "Niccolò Machiavelli ('The Prince')",
                     "Jean-Jacques Rousseau ('The Social Contract')",
                     "John Locke ('Two Treatises of Government')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Nikkolo Makiavelli («Hukmdor» risolasi)',
                     'ru': 'Никколо Макиавелли (трактат «Государь»)',
                     'en': "Niccolò Machiavelli ('The Prince')"},
  'image_url': None,
  'fun_fact': {'uz': '1513 yilda Florensiyada yozilgan «Hukmdor» (Il Principe) asari real siyosat (realpolitik) va '
                     "davlat boshqaruvining dunyodagi eng mashhur qo'llanmasidir.",
               'ru': 'Трактат Макиавелли 1513 года заложил основы практической политологии эпохи Возрождения и породил '
                     'термин «макиавеллизм».',
               'en': "Machiavelli's 1513 political treatise analyzing power, pragmatism, and statecraft in Renaissance "
                     'Italy.'},
  'aliases': ['hukmdor', 'makiavelli', 'государь', 'макиавелли', 'the prince', 'machiavelli']},
 {'id': 'lit_q_055',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Bolalarni asrang!» (Ehtimol, odam go'shtini yemagan bolalar hali qolgandir...)",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Спасите детей!» (Может быть, ещё есть дети, которые не ели человечины?..)',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Save the children!' (Perhaps there are still children who have not eaten human flesh?..)"},
  'options': {'uz': ['Lu Syun («A-Q haqiqiy tarixi»)',
                     'Lao She («Tuyakash Luotuo Siangzi»)',
                     'Lu Syun («Telba kundaligi»)',
                     'Mo Yan («Qizil gao-lyan»)'],
              'ru': ['Лу Синь («Подлинная история А-Кью»)',
                     'Лао Шэ («Рикша»)',
                     'Лу Синь («Записки сумасшедшего»)',
                     'Мо Янь («Красный гаолян»)'],
              'en': ["Lu Xun ('The True Story of Ah Q')",
                     "Lao She ('Rickshaw Boy')",
                     "Lu Xun ('A Madman's Diary')",
                     "Mo Yan ('Red Sorghum')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Lu Syun («Telba kundaligi»)',
                     'ru': 'Лу Синь («Записки сумасшедшего»)',
                     'en': "Lu Xun ('A Madman's Diary')"},
  'image_url': None,
  'fun_fact': {'uz': "1918 yilda e'lon qilingan ushbu asar zamonaviy Xitoy adabiyotining tamal toshi hisoblanadi; Lu "
                     'Syun unda eski feodal jamiyatning shafqatsizligini qoralaydi.',
               'ru': 'Первый модернистский рассказ на разговорном китайском языке (байхуа) 1918 года, ставший вехой в '
                     'обновлении Китая.',
               'en': "Published in 1918, this seminal story founded modern Chinese literature, using a madman's "
                     'delusions as an allegory for feudal cannibalism.'},
  'aliases': ['lu syun', 'telba kundaligi', 'лу синь', 'записки сумасшедшего', 'lu xun']},
 {'id': 'lit_q_056',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«O'lim hayotning teskarisi emas, balki uning ajralmas bir qismidir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Смерть — это не противоположность жизни, а её неотъемлемая часть.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Death is not the opposite of life, but a part of it.'"},
  'options': {'uz': ['Xaruki Murakami («Sohilda Kafka»)',
                     "Xaruki Murakami («Qo'y ovi»)",
                     "Kadzuo Isiguro («Meni qo'yib yuborma»)",
                     "Xaruki Murakami («Norveg o'rmoni»)"],
              'ru': ['Харуки Мураками («Кафка на пляже»)',
                     'Харуки Мураками («Охота на овец»)',
                     'Кадзуо Исигуро («Не отпускай меня»)',
                     'Харуки Мураками («Норвежский лес»)'],
              'en': ["Haruki Murakami ('Kafka on the Shore')",
                     "Haruki Murakami ('A Wild Sheep Chase')",
                     "Kazuo Ishiguro ('Never Let Me Go')",
                     "Haruki Murakami ('Norwegian Wood')"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Xaruki Murakami («Norveg o'rmoni»)",
                     'ru': 'Харуки Мураками («Норвежский лес»)',
                     'en': "Haruki Murakami ('Norwegian Wood')"},
  'image_url': None,
  'fun_fact': {'uz': "1987 yilda chop etilgan «Norveg o'rmoni» yoshlik xotiralari, ayriliq va sevgining fojiaviy "
                     "go'zalligini tasvirlab, Murakamiga xalqaro shuhrat keltirgan.",
               'ru': 'Роман 1987 года, сделавший Мураками культовым автором; заглавие отсылает к одноимённой песне '
                     'группы The Beatles.',
               'en': "Murakami's 1987 nostalgic masterpiece taking its title from the Beatles song, selling millions "
                     'across Japan and worldwide.'},
  'aliases': ["norveg o'rmoni", 'murakami', 'норвежский лес', 'мураками', 'norwegian wood', 'haruki murakami']},
 {'id': 'lit_q_057',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Florentino Ariza o'z sevgisini ellik bir yil, to'qqiz oy va to'rt kun davomida kutgan edi...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Флорентино Ариса ждал свою любовь пятьдесят один год, девять месяцев и четыре дня...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Florentino Ariza had waited for this moment for fifty-one years, nine months, and four "
                     "days...'"},
  'options': {'uz': ['Gabriel Garsia Markes («Vabo davridagi muhabbat»)',
                     "Gabriel Garsia Markes («Yolg'izlikning yuz yili»)",
                     'Mario Vargas Lyosa («Xola Xuliya va qalamkash»)',
                     'Izabel Alende («Ruhlar uyi»)'],
              'ru': ['Габриэль Гарсиа Маркес («Любовь во время холеры»)',
                     'Габриэль Гарсиа Маркес («Сто лет одиночества»)',
                     'Марио Варгас Льоса («Тётя Хулия и писака»)',
                     'Исабель Альенде («Дом духов»)'],
              'en': ["Gabriel García Márquez ('Love in the Time of Cholera')",
                     "Gabriel García Márquez ('One Hundred Years of Solitude')",
                     "Mario Vargas Llosa ('Aunt Julia and the Scriptwriter')",
                     "Isabel Allende ('The House of the Spirits')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Gabriel Garsia Markes («Vabo davridagi muhabbat»)',
                     'ru': 'Габриэль Гарсиа Маркес («Любовь во время холеры»)',
                     'en': "Gabriel García Márquez ('Love in the Time of Cholera')"},
  'image_url': None,
  'fun_fact': {'uz': "Florentino Ariza va Fermina Dasa o'rtasidagi yarim asrlik sadoqatli muhabbat haqidagi ushbu asar "
                     '1985 yilda yozilgan.',
               'ru': 'Роман Маркеса 1985 года воспевает вечную победу человеческой любви и верности над временем, '
                     'старением и болезнями.',
               'en': "Márquez's 1985 lyrical tribute to undying fidelity and devotion enduring for over half a "
                     'century.'},
  'aliases': ['vabo davridagi muhabbat', 'любовь во время холеры', 'love in the time of cholera', 'florentino ariza']},
 {'id': 'lit_q_058',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«ANANKE (Muqarrar Taqdir) — sobor devoriga qadimgi yunoncha o'yilgan bu so'z barcha fojialarning "
                     'ibtidosi edi...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«ANANKE (Рок) — это греческое слово, нацарапанное на стене собора, породило всю эту скорбную '
                     'книгу...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'ANANKE (Fate) — it was upon this word, engraved in a dark corner of Notre-Dame, that this book "
                     "was founded...'"},
  'options': {'uz': ["Viktor Gyugo («Xo'rlanganlar»)",
                     'Viktor Gyugo («Parij Bibi Maryam ibodatxonasi»)',
                     'Viktor Gyugo («Kulayotgan odam»)',
                     'Prosper Merime («Karmen»)'],
              'ru': ['Виктор Гюго («Отверженные»)',
                     'Виктор Гюго («Собор Парижской Богоматери»)',
                     'Виктор Гюго («Человек, который смеётся»)',
                     'Проспер Мериме («Кармен»)'],
              'en': ["Victor Hugo ('Les Misérables')",
                     "Victor Hugo ('The Hunchback of Notre-Dame')",
                     "Victor Hugo ('The Man Who Laughs')",
                     "Prosper Mérimée ('Carmen')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Viktor Gyugo («Parij Bibi Maryam ibodatxonasi»)',
                     'ru': 'Виктор Гюго («Собор Парижской Богоматери»)',
                     'en': "Victor Hugo ('The Hunchback of Notre-Dame')"},
  'image_url': None,
  'fun_fact': {'uz': "Gyugo sobor xarobaligiga jamoatchilik e'tiborini qaratish va uni buzilishdan saqlab qolish "
                     'maqsadida 1831 yilda ushbu romanni yozgan va sobor qayta tiklangan.',
               'ru': 'Роман Гюго 1831 года спас собор Парижской Богоматери от сноса и положил начало движению за '
                     'сохранение готической архитектуры.',
               'en': 'Hugo wrote the 1831 novel specifically to spearhead the preservation and restoration of the '
                     'crumbling Gothic cathedral.'},
  'aliases': ['notr dam', 'gyugo', 'собор парижской богоматери', 'квазимодо', 'hunchback of notre dame', 'ananke']},
 {'id': 'lit_q_059',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Insoniyatning barcha donoligi ikki so'zda jamlangandir: Kutmoq va Umid qilmoq!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Вся человеческая мудрость заключена в двух словах: Ждать и Надеяться!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'All human wisdom is contained in these two words: Wait and Hope!'"},
  'options': {'uz': ['Aleksandr Dyuma («Uch mushketyor»)',
                     'Onore de Balzak («Shagren terisi»)',
                     'Aleksandr Dyuma («Graf Monte-Kristo» xotimasi)',
                     'Stendal («Qizil va qora»)'],
              'ru': ['Александр Дюма («Три мушкетёра»)',
                     'Оноре де Бальзак («Шагреневая кожа»)',
                     'Александр Дюма («Граф Монте-Кристо» — финал романа)',
                     'Стендаль («Красное и чёрное»)'],
              'en': ["Alexandre Dumas ('The Three Musketeers')",
                     "Honoré de Balzac ('The Wild Ass's Skin')",
                     "Alexandre Dumas ('The Count of Monte Cristo' — finale)",
                     "Stendhal ('The Red and the Black')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Aleksandr Dyuma («Graf Monte-Kristo» xotimasi)',
                     'ru': 'Александр Дюма («Граф Монте-Кристо» — финал романа)',
                     'en': "Alexandre Dumas ('The Count of Monte Cristo' — finale)"},
  'image_url': None,
  'fun_fact': {'uz': "Edmon Dantes Maksimilian Morrelga qoldirgan vidolashuv maktubining so'nggi jumlasi bo'lib, "
                     'romanning bosh falsafasini jamlaydi.',
               'ru': 'Заключительные строки письма Эдмона Дантеса к Максимилиану Моррелю подводят философский итог '
                     'великому роману о возмездии и прощении.',
               'en': 'The final moral advice left by Edmond Dantès in his farewell letter to Maximilien Morrel at the '
                     "end of Dumas's masterpiece."},
  'aliases': ['graf monte-kristo', 'monte kristo', 'граф монте-кристо', 'count of monte cristo', 'wait and hope']},
 {'id': 'lit_q_060',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Dunyoda chin daho paydo bo'lganini bilmoqchimisiz? Barcha nodonlar unga qarshi ittifoq "
                     'tuzganidan buni bilib olasiz!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Когда на свете появляется истинный гений, вы можете узнать его по тому признаку, что все дураки '
                     'объединяются против него!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'When a true genius appears in the world, you may know him by this sign, that the dunces are all "
                     "in confederacy against him!'"},
  'options': {'uz': ['Daniel Defo («Robinzon Kruzo»)',
                     'Volter («Kandid»)',
                     'Lorens Stern («Tristram Shendi»)',
                     'Jonatan Svift («Gulliverning sayohatlari» / «Tafakkur durdonalari»)'],
              'ru': ['Даниэль Дефо («Робинзон Крузо»)',
                     'Вольтер («Кандид»)',
                     'Лоренс Стерн («Тристрам Шенди»)',
                     'Джонатан Свифт («Путешествия Гулливера» / «Размышления»)'],
              'en': ["Daniel Defoe ('Robinson Crusoe')",
                     "Voltaire ('Candide')",
                     "Laurence Sterne ('Tristram Shandy')",
                     "Jonathan Swift ('Gulliver's Travels' / 'Thoughts on Various Subjects')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jonatan Svift («Gulliverning sayohatlari» / «Tafakkur durdonalari»)',
                     'ru': 'Джонатан Свифт («Путешествия Гулливера» / «Размышления»)',
                     'en': "Jonathan Swift ('Gulliver's Travels' / 'Thoughts on Various Subjects')"},
  'image_url': None,
  'fun_fact': {'uz': 'Buyuk ingliz-irland satirigi Jonatan Sviftning ushbu aforizmi Jon Kennedi Tulning mashhur '
                     '«Nodonlar ittifoqi» romaniga nom bergan.',
               'ru': 'Этот афоризм Свифта послужил эпиграфом и дал название знаменитому роману Джона Кеннеди Тула '
                     '«Сговор остолопов».',
               'en': "Swift's blistering aphorism later inspired the title and epigraph of John Kennedy Toole's "
                     "Pulitzer Prize-winning 'A Confederacy of Dunces'."},
  'aliases': ['svift', 'gulliver', 'свифт', 'гулливер', 'swift', 'gullivers travels']},
 {'id': 'lit_q_061',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Xavf-xatardan qo'rqish hissi — xavfning o'zidan o'n ming karra dahshatliroqdir!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Страх перед опасностью в десять тысяч раз ужаснее самой опасности!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Fear of danger is ten thousand times more terrifying and distressing than danger itself!'"},
  'options': {'uz': ['Daniel Defo («Robinzon Kruzo»)',
                     "Jyul Vern («O'n besh yoshli kapitan»)",
                     'Robert Lyuis Stivenson («Xazinalar oroli»)',
                     'Jonatan Svift («Gulliverning sayohatlari»)'],
              'ru': ['Даниэль Дефо («Робинзон Крузо»)',
                     'Жюль Верн («Пятнадцатилетний капитан»)',
                     'Роберт Льюис Стивенсон («Остров сокровищ»)',
                     'Джонатан Свифт («Путешествия Гулливера»)'],
              'en': ["Daniel Defoe ('Robinson Crusoe')",
                     "Jules Verne ('Dick Sand, A Boy Captain')",
                     "Robert Louis Stevenson ('Treasure Island')",
                     "Jonathan Swift ('Gulliver's Travels')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Daniel Defo («Robinzon Kruzo»)',
                     'ru': 'Даниэль Дефо («Робинзон Крузо»)',
                     'en': "Daniel Defoe ('Robinson Crusoe')"},
  'image_url': None,
  'fun_fact': {'uz': '1719 yilda yozilgan kimsasiz orolda 28 yil yashagan Robinzon Kruzo sarguzashtlari inson irodasi '
                     'va mehnatining qudratini tasdiqlagan.',
               'ru': 'Философское размышление Робинзона Крузо на необитаемом острове после обнаружения на песке следа '
                     'босой ноги.',
               'en': "Crusoe's psychological reflection upon discovering a single footprint of a cannibal on the "
                     "island's beach."},
  'aliases': ['robinzon kruzo', 'robinzon', 'defo', 'робинзон крузо', 'дефо', 'robinson crusoe']},
 {'id': 'lit_q_062',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Ehtiyot bo'l: men hech narsadan qo'rqmayman, shuning uchun ham behad qudratliman!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Берегись: я ничего не боюсь, и потому я всесилен!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Beware; for I am fearless, and therefore powerful!'"},
  'options': {'uz': ['Brem Stoker («Drakula»)',
                     'Meri Shelli («Frankenshteyn»)',
                     'Robert Lyuis Stivenson («Doktor Jekil va mister Xayd»)',
                     'Edgar Allan Po («Usherlar xonadonining qulashi»)'],
              'ru': ['Брэм Стокер («Дракула»)',
                     'Мэри Шелли («Франкенштейн, или Современный Прометей»)',
                     'Роберт Льюис Стивенсон («Странная история доктора Джекила и мистера Хайда»)',
                     'Эдгар Аллан По («Падение дома Ашеров»)'],
              'en': ["Bram Stoker ('Dracula')",
                     "Mary Shelley ('Frankenstein')",
                     "Robert Louis Stevenson ('Strange Case of Dr Jekyll and Mr Hyde')",
                     "Edgar Allan Poe ('The Fall of the House of Usher')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Meri Shelli («Frankenshteyn»)',
                     'ru': 'Мэри Шелли («Франкенштейн, или Современный Прометей»)',
                     'en': "Mary Shelley ('Frankenstein')"},
  'image_url': None,
  'fun_fact': {'uz': 'Meri Shelli 1818 yilda atigi 20 yoshida yozgan ushbu roman ilmiy fantastika janrining ilk '
                     'durdonasi hisoblanadi.',
               'ru': 'Слова Чудовища, обращённые к своему создателю Виктору Франкенштейну; роман 1818 года считается '
                     'предтечей научной фантастики.',
               'en': "The Creature's terrifying threat to his creator Victor Frankenstein in Mary Shelley's pioneering "
                     '1818 science-fiction novel.'},
  'aliases': ['frankenshteyn', 'meri shelli', 'франкенштейн', 'мэри шелли', 'frankenstein', 'mary shelley']},
 {'id': 'lit_q_063',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Ularni eshiting: tun bolalarining ovozini! Ular qanday g'aroyib musiqa yaratadilar!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Послушайте их: дети ночи! Какую дивную музыку они создают!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Listen to them, the children of the night. What music they make!'"},
  'options': {'uz': ['Meri Shelli («Frankenshteyn»)',
                     'Jon Polidori («Vampir»)',
                     'Brem Stoker («Drakula»)',
                     'Sheridan Le Fanyu («Karmilla»)'],
              'ru': ['Мэри Шелли («Франкенштейн»)',
                     'Джон Полидори («Вампир»)',
                     'Брэм Стокер («Дракула»)',
                     'Шеридан Ле Фаню («Кармилла»)'],
              'en': ["Mary Shelley ('Frankenstein')",
                     "John William Polidori ('The Vampyre')",
                     "Bram Stoker ('Dracula')",
                     "Sheridan Le Fanu ('Carmilla')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Brem Stoker («Drakula»)', 'ru': 'Брэм Стокер («Дракула»)', 'en': "Bram Stoker ('Dracula')"},
  'image_url': None,
  'fun_fact': {'uz': "Graf Drakula Transilvaniyadagi qasrida Jonatan Xarkerga tunda uvillayotgan bo'rilar to'dasi "
                     "haqida gapirganda shu so'zlarni aytadi.",
               'ru': 'Знаменитая реплика графа Дракулы, обращённая к Джонатану Харкеру в ответ на вой волков под '
                     'стенами замка в Трансильвании.',
               'en': "Count Dracula's iconic welcome to Jonathan Harker at Castle Dracula in Transylvania, referring "
                     'to howling wolves.'},
  'aliases': ['drakula', 'brem stoker', 'дракула', 'брэм стокер', 'dracula', 'bram stoker']},
 {'id': 'lit_q_064',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Men qush emasman va hech qanday to'r meni ushlab turolmaydi; men mustaqil irodaga ega ozod "
                     'insonman!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Я не птица, и никакие сети не удержат меня; я свободный человек с независимой волей!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'I am no bird; and no net ensnares me; I am a free human being with an independent will!'"},
  'options': {'uz': ['Emili Bronte («Momaqaldiroqli dovon»)',
                     'Jeyn Ostin («Emma»)',
                     'Luiza Mey Olkott («Kichik ayollar»)',
                     'Sharlotta Bronte («Jeyn Eyr»)'],
              'ru': ['Эмили Бронте («Грозовой перевал»)',
                     'Джейн Остин («Эмма»)',
                     'Луиза Мэй Олкотт («Маленькие женщины»)',
                     'Шарлотта Бронте («Джейн Эйр»)'],
              'en': ["Emily Brontë ('Wuthering Heights')",
                     "Jane Austen ('Emma')",
                     "Louisa May Alcott ('Little Women')",
                     "Charlotte Brontë ('Jane Eyre')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Sharlotta Bronte («Jeyn Eyr»)',
                     'ru': 'Шарлотта Бронте («Джейн Эйр»)',
                     'en': "Charlotte Brontë ('Jane Eyre')"},
  'image_url': None,
  'fun_fact': {'uz': "Jeyn Eyrning mister Rochesterga o'z erkinligi, qadr-qimmati va tengligi haqida aytgan jasur "
                     "so'zlari ayollar mustaqilligining ramziga aylandi.",
               'ru': 'Гордый ответ гувернантки Джейн Эйр мистеру Рочестеру стал манифестом женского достоинства и '
                     'духовной независимости.',
               'en': "Jane Eyre's passionate assertion of moral and spiritual autonomy to Mr. Rochester in Charlotte "
                     "Brontë's 1847 novel."},
  'aliases': ['jeyn eyr', 'sharlotta bronte', 'джейн эйр', 'бронте', 'jane eyre']},
 {'id': 'lit_q_065',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Bizning qalblarimiz nimadan yaratilgan bo'lmasin, uning qalbi va mening qalbim — bir narsadir!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Из чего бы ни были сотворены наши души, его душа и моя — одно и то же!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Whatever our souls are made of, his and mine are the same!'"},
  'options': {'uz': ['Emili Bronte («Momaqaldiroqli dovon» — Ketrin)',
                     'Sharlotta Bronte («Villett»)',
                     'Dafna dyu Morye («Rebekka»)',
                     'Tomas Hardi («Tess»)'],
              'ru': ['Эмили Бронте («Грозовой перевал» — Кэтрин)',
                     'Шарлотта Бронте («Виллетт»)',
                     'Дафна дю Морье («Ребекка»)',
                     "Томас Гарди («Тэсс из рода д'Эрбервиллей»)"],
              'en': ["Emily Brontë ('Wuthering Heights' — Catherine)",
                     "Charlotte Brontë ('Villette')",
                     "Daphne du Maurier ('Rebecca')",
                     "Thomas Hardy ('Tess of the d'Urbervilles')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Emili Bronte («Momaqaldiroqli dovon» — Ketrin)',
                     'ru': 'Эмили Бронте («Грозовой перевал» — Кэтрин)',
                     'en': "Emily Brontë ('Wuthering Heights' — Catherine)"},
  'image_url': None,
  'fun_fact': {'uz': "Ketrin Ernshoning Xitklifga bo'lgan g'ayritabiiy, yonuvchi va azobli muhabbati haqidagi ushbu "
                     'iqrori ingliz adabiyotining eng yorqin sahifasidir.',
               'ru': 'Признание Кэтрин в её стихийной, всепоглощающей страсти к Хитклиффу в единственном романе Эмили '
                     'Бронте 1847 года.',
               'en': "Catherine Earnshaw's passionate confession of her metaphysical connection to Heathcliff in the "
                     'windswept Yorkshire moors.'},
  'aliases': ['momaqaldiroqli dovon', 'emili bronte', 'грозовой перевал', 'эмили бронте', 'wuthering heights']},
 {'id': 'lit_q_066',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Bu yerda hamma jinnivoy. Men ham jinniman. Sen ham jinnisan. Aks holda bu yerga kelmas eding!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Мы тут все сумасшедшие. Я сумасшедший. Ты сумасшедшая. Иначе ты бы сюда не попала!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'We're all mad here. I'm mad. You're mad. You must be, or you wouldn't have come here!'"},
  'options': {'uz': ["Lyuis Kerroll («Ko'zgular ortida»)",
                     "Lyuis Kerroll («Alisa mo''jizalar mamlakatida» — Cheshir mushugi)",
                     'Jeyms Barri («Piter Pen»)',
                     'Liman Frenk Baum («Oz mamlakati sehrgari»)'],
              'ru': ['Льюис Кэрролл («Алиса в Зазеркалье»)',
                     'Льюис Кэрролл («Алиса в Стране чудес» — Чеширский Кот)',
                     'Джеймс Барри («Питер Пэн»)',
                     'Лаймен Фрэнк Баум («Волшебник страны Оз»)'],
              'en': ["Lewis Carroll ('Through the Looking-Glass')",
                     "Lewis Carroll ('Alice in Wonderland' — Cheshire Cat)",
                     "J.M. Barrie ('Peter Pan')",
                     "L. Frank Baum ('The Wonderful Wizard of Oz')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Lyuis Kerroll («Alisa mo''jizalar mamlakatida» — Cheshir mushugi)",
                     'ru': 'Льюис Кэрролл («Алиса в Стране чудес» — Чеширский Кот)',
                     'en': "Lewis Carroll ('Alice in Wonderland' — Cheshire Cat)"},
  'image_url': None,
  'fun_fact': {'uz': 'Cheshir mushugining Alisaga aytgan paradoksal falsafasi ushbu 1865 yildagi ertakning eng sevimli '
                     'iqtibosidir.',
               'ru': 'Фирменный афоризм улыбающегося Чеширского Кота в разговоре с Алисой на развилке дорог.',
               'en': "The Cheshire Cat's grinning declaration of whimsical absurdism to Alice in Wonderland."},
  'aliases': ['alisa',
              'lyuis kerroll',
              'чеширский кот',
              'алиса в стране чудес',
              'alice in wonderland',
              'cheshire cat']},
 {'id': 'lit_q_067',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Inson mutlaqo zamonaviy bo'lishi shart!» (Il faut être absolument moderne)",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Нужно быть абсолютно современным!»',
               'en': "Which work or author is the source of this famous quote?\n\n'One must be absolutely modern!'"},
  'options': {'uz': ["Pol Verlen («Saturnik she'rlar»)",
                     'Stefan Mallarme («Irod»)',
                     'Artyur Rembo («Jahannamda bir fasl»)',
                     'Giyom Apolliner («Alkogollar»)'],
              'ru': ['Поль Верлен («Сатурнические стихотворения»)',
                     'Стефан Малларме («Иродиада»)',
                     'Артюр Рембо («Одно лето в аду»)',
                     'Гийом Аполлинер («Алкоголи»)'],
              'en': ["Paul Verlaine ('Poèmes saturniens')",
                     "Stéphane Mallarmé ('Hérodiade')",
                     "Arthur Rimbaud ('A Season in Hell')",
                     "Guillaume Apollinaire ('Alcools')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Artyur Rembo («Jahannamda bir fasl»)',
                     'ru': 'Артюр Рембо («Одно лето в аду»)',
                     'en': "Arthur Rimbaud ('A Season in Hell')"},
  'image_url': None,
  'fun_fact': {'uz': "19 yoshida barcha she'rlarini yozib bo'lib adabiyotni tark etgan fransuz daho shoiri Artyur "
                     'Remboning modernizm shioriga aylangan iborasi.',
               'ru': 'Финальный девиз пророческой поэмы в прозе 1873 года бунтарского гения французского символизма '
                     'Артюра Рембо.',
               'en': 'The defining manifesto of modernism proclaimed in 1873 by teenage prodigy Arthur Rimbaud before '
                     'abandoning poetry.'},
  'aliases': ['rembo', 'artyur rembo', 'рембо', 'артюр рембо', 'rimbaud', 'a season in hell']},
 {'id': 'lit_q_068',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Munofiq kitobxon, mening qiyofadoshim, mening qondosh birodarim!» (Hypocrite lecteur, — mon '
                     'semblable, — mon frère!)',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Лицемерный читатель, мой двойник, мой брат!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Hypocrite reader, — my likeness, — my brother!'"},
  'options': {'uz': ["Pol Verlen («So'zsiz romanslar»)",
                     'Artyur Rembo («Tovushlar»)',
                     'Stefan Mallarme («Bir favnning tushdan keyingi oromi»)',
                     'Sharl Bodler («Yovuzlik gullari» muqaddimasi)'],
              'ru': ['Поль Верлен («Романсы без слов»)',
                     'Артюр Рембо («Озарения»)',
                     'Стефан Малларме («Послеполуденный отдых фавна»)',
                     'Шарль Бодлер (предисловие к «Цветам зла»)'],
              'en': ["Paul Verlaine ('Romances sans paroles')",
                     "Arthur Rimbaud ('Illuminations')",
                     "Stéphane Mallarmé ('The Afternoon of a Faun')",
                     "Charles Baudelaire ('The Flowers of Evil' — Preface)"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Sharl Bodler («Yovuzlik gullari» muqaddimasi)',
                     'ru': 'Шарль Бодлер (предисловие к «Цветам зла»)',
                     'en': "Charles Baudelaire ('The Flowers of Evil' — Preface)"},
  'image_url': None,
  'fun_fact': {'uz': "1857 yilda e'lon qilingan va shov-shuvlarga sabab bo'lgan «Yovuzlik gullari» kitobida Bodler "
                     "kitobxonni o'zining ichki qusurlari va g'amiga sherik qiladi.",
               'ru': 'Заключительная строфа вступительного стихотворения «Читателю» скандального сборника 1857 года, '
                     'перевернувшего мировую поэзию.',
               'en': "The provocative closing line of Baudelaire's opening poem 'To the Reader' in his revolutionary "
                     '1857 collection.'},
  'aliases': ['bodler', 'yovuzlik gullari', 'бодлер', 'цветы зла', 'baudelaire', 'flowers of evil']},
 {'id': 'lit_q_069',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Haqiqiy kashfiyot safari yangi yerlarni izlashda emas, balki bor narsalarga yangi nigoh bilan '
                     'boqishdadir.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Истинное путешествие открытий состоит не в поисках новых пейзажей, а в обретении нового '
                     'взгляда.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'The real voyage of discovery consists not in seeking new landscapes, but in having new eyes.'"},
  'options': {'uz': ["Marsel Prust («Yo'qotilgan vaqtni izlab»)",
                     'Andre Jid («Soxta pul yasovchilar»)',
                     'Romen Rollan («Jan-Kristof»)',
                     "Lui-Ferdinand Selin («Tun qa'riga sayohat»)"],
              'ru': ['Марсель Пруст («В поисках утраченного времени»)',
                     'Андре Жид («Фальшивомонетчики»)',
                     'Ромен Роллан («Жан-Кристоф»)',
                     'Луи-Фердинанд Селин («Путешествие на край ночи»)'],
              'en': ["Marcel Proust ('In Search of Lost Time')",
                     "André Gide ('The Counterfeiters')",
                     "Romain Rolland ('Jean-Christophe')",
                     "Louis-Ferdinand Céline ('Journey to the End of the Night')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Marsel Prust («Yo'qotilgan vaqtni izlab»)",
                     'ru': 'Марсель Пруст («В поисках утраченного времени»)',
                     'en': "Marcel Proust ('In Search of Lost Time')"},
  'image_url': None,
  'fun_fact': {'uz': "Marsel Prustning 7 jildlik ushbu monumental asari inson xotirasi, vaqtning oqishi va tuyg'ular "
                     'nozikligini tadqiq etgan psixologik durdonadir.',
               'ru': 'Ключевая мысль монументальной семитомной эпопеи Марселя Пруста о природе памяти, искусства и '
                     'восприятия реальности.',
               'en': "Proust's philosophical observation from his monumental seven-volume modernist exploration of "
                     'involuntary memory and perception.'},
  'aliases': ['prust', "yo'qotilgan vaqtni izlab", 'пруст', 'в поисках утраченного времени', 'proust']},
 {'id': 'lit_q_070',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Ko'pchilik odamlar suzishni o'rganmagunlaricha suvga tushishni istamaydilar. Bu qanday kulgili! "
                     'Axir suzishni bilish uchun suvga tushmoq lozim-ku!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Большинство людей не желает плавать до того, как научится плавать. Какая забавная шутка: ведь '
                     'чтобы научиться плавать, нужно войти в воду!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Most people will not swim before they are able to. Isn't that witty? To learn to swim, you must "
                     "go into the water!'"},
  'options': {'uz': ["German Gesse («Marjonlar o'yini»)",
                     "German Gesse («Cho'l bo'risi»)",
                     'German Gesse («Siddharta»)',
                     "Tomas Mann («Sehrli tog'»)"],
              'ru': ['Герман Гессе («Игра в бисер»)',
                     'Герман Гессе («Степной волк»)',
                     'Герман Гессе («Сиддхартха»)',
                     'Томас Манн («Волшебная гора»)'],
              'en': ["Hermann Hesse ('The Glass Bead Game')",
                     "Hermann Hesse ('Steppenwolf')",
                     "Hermann Hesse ('Siddhartha')",
                     "Thomas Mann ('The Magic Mountain')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "German Gesse («Cho'l bo'risi»)",
                     'ru': 'Герман Гессе («Степной волк»)',
                     'en': "Hermann Hesse ('Steppenwolf')"},
  'image_url': None,
  'fun_fact': {'uz': "1927 yilda yozilgan «Cho'l bo'risi» insonning ichki ma'naviy ikkilanishi va o'zligini topish "
                     "yo'lidagi ruhiy sayohatidir.",
               'ru': 'Культовый роман Германа Гессе 1927 года исследует раскол между буржуазной личностью Гарри '
                     'Галлера и его звериной сущностью.',
               'en': "Hesse's 1927 psychological masterpiece dissecting the dual nature of intellectual Harry Haller "
                     'and his wild, untamed animal soul.'},
  'aliases': ["cho'l bo'risi", 'german gesse', 'степной волк', 'герман гессе', 'steppenwolf', 'hermann hesse']},
 {'id': 'lit_q_071',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Inson faqat o'z shaxsiy hayotini yashab qolmay, o'z davrining ham hayoti bilan yashaydi.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Человек живёт не только своей личной жизнью, но сознательно или бессознательно и жизнью своей '
                     'эпохи.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'A man lives not only his personal life, but consciously or unconsciously also that of his epoch "
                     "and his contemporaries.'"},
  'options': {'uz': ['Tomas Mann («Buddenbroklar»)',
                     "Tomas Mann («Venetsiyada o'lim»)",
                     "Tomas Mann («Sehrli tog'»)",
                     'Robert Muzil («Fazilatlarsiz odam»)'],
              'ru': ['Томас Манн («Будденброки»)',
                     'Томас Манн («Смерть в Венеции»)',
                     'Томас Манн («Волшебная гора»)',
                     'Роберт Музиль («Человек без свойств»)'],
              'en': ["Thomas Mann ('Buddenbrooks')",
                     "Thomas Mann ('Death in Venice')",
                     "Thomas Mann ('The Magic Mountain')",
                     "Robert Musil ('The Man Without Qualities')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Tomas Mann («Sehrli tog'»)",
                     'ru': 'Томас Манн («Волшебная гора»)',
                     'en': "Thomas Mann ('The Magic Mountain')"},
  'image_url': None,
  'fun_fact': {'uz': 'Shveysariya sanatoriysidagi bemorlar hayoti orqali Birinchi jahon urushi arafasidagi Yevropa '
                     'sivilizatsiyasining inqirozi aks ettirilgan.',
               'ru': 'Шедевр интеллектуального романа XX века (1924), принёсший Томасу Манну мировое признание.',
               'en': "Published in 1924, Mann's monumental sanatorium novel served as an intellectual microcosm of "
                     'pre-WWI European civilization.'},
  'aliases': ["sehrli tog'", 'tomas mann', 'волшебная гора', 'томас манн', 'magic mountain', 'thomas mann']},
 {'id': 'lit_q_072',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Xonim bilan gul sotuvchi qiz o'rtasidagi farq — ularning qanday tutishida emas, balki ularga "
                     "boshqalar qanday munosabatda bo'lishidadir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Разница между леди и цветочницей заключается не только в том, как она себя держит, но и в том, '
                     'как к ней относятся окружающие.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'The difference between a lady and a flower girl is not how she behaves, but how she's "
                     "treated.'"},
  'options': {'uz': ['Oskar Uayld («Ideal er»)',
                     'Somerset Moem («Teatr»)',
                     'Jon Golsuorsi («Forsaytlar haqida doston»)',
                     'Jorj Bernard Shou («Pigmalion» — Eliza Dulitl)'],
              'ru': ['Оскар Уайльд («Идеальный муж»)',
                     'Сомерсет Моэм («Театр»)',
                     'Джон Голсуорси («Сага о Форсайтах»)',
                     'Джордж Бернард Шоу («Пигмалион» — Элиза Дулиттл)'],
              'en': ["Oscar Wilde ('An Ideal Husband')",
                     "W. Somerset Maugham ('Theatre')",
                     "John Galsworthy ('The Forsyte Saga')",
                     "George Bernard Shaw ('Pygmalion' — Eliza Doolittle)"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jorj Bernard Shou («Pigmalion» — Eliza Dulitl)',
                     'ru': 'Джордж Бернард Шоу («Пигмалион» — Элиза Дулиттл)',
                     'en': "George Bernard Shaw ('Pygmalion' — Eliza Doolittle)"},
  'image_url': None,
  'fun_fact': {'uz': "Eliza Dulitl professor Xigginsga uning sinfiy kibrini fosh qilib aytgan ushbu so'zlari ijtimoiy "
                     'tenglikning yorqin ifodasidir.',
               'ru': 'Знаменитая реплика преобразившейся Элизы Дулиттл в пятом акте комедии Бернарда Шоу (1912).',
               'en': "Eliza Doolittle's sharp insight on class perception delivered to Colonel Pickering and Professor "
                     'Higgins.'},
  'aliases': ['pigmalion', 'bernard shou', 'пигмалион', 'бернард шоу', 'pygmalion', 'eliza doolittle']},
 {'id': 'lit_q_073',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Agar ayol kishi badiiy asar yozmoqchi bo'lsa, uning puli va o'zining shaxsiy xonasi bo'lishi "
                     'shart.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Если женщина собирается писать прозу, у неё должны быть деньги и собственная комната.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'A woman must have money and a room of her own if she is to write fiction.'"},
  'options': {'uz': ["Virjiniya Vulf («O'zining shaxsiy xonasi»)",
                     'Virjiniya Vulf («Missis Dellouey»)',
                     'Virjiniya Vulf («Mayoqqa»)',
                     'Silviya Plat («Shisha qopqoq ostida»)'],
              'ru': ['Вирджиния Вулф (эссе «Своя комната»)',
                     'Вирджиния Вулф («Миссис Дэллоуэй»)',
                     'Вирджиния Вулф («На маяк»)',
                     'Сильвия Плат («Под стеклянным колпаком»)'],
              'en': ["Virginia Woolf ('A Room of One's Own')",
                     "Virginia Woolf ('Mrs Dalloway')",
                     "Virginia Woolf ('To the Lighthouse')",
                     "Sylvia Plath ('The Bell Jar')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Virjiniya Vulf («O'zining shaxsiy xonasi»)",
                     'ru': 'Вирджиния Вулф (эссе «Своя комната»)',
                     'en': "Virginia Woolf ('A Room of One's Own')"},
  'image_url': None,
  'fun_fact': {'uz': '1929 yilda chop etilgan ushbu esse ayollar adabiyoti va ijodiy erkinlik masalasidagi eng '
                     "ta'sirli nazariy asardir.",
               'ru': 'Эссе 1929 года, ставшее классическим манифестом женской финансовой независимости и творческого '
                     'равноправия.',
               'en': "Woolf's foundational 1929 essay examining women's historical exclusion from education and "
                     'intellectual independence.'},
  'aliases': ['virjiniya vulf',
              "o'zining xonasi",
              'вирджиния вулф',
              'своя комната',
              'virginia woolf',
              'room of ones own']},
 {'id': 'lit_q_074',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Tarix — men undan uyg'onishga behuda urinayotgan dahshatli tushdir.»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«История — это кошмар, от которого я пытаюсь проснуться.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'History is a nightmare from which I am trying to awake.'"},
  'options': {'uz': ['Jeyms Joys («Musavvirning yoshlikdagi shomoyili»)',
                     'Jeyms Joys («Uliss» — Stiven Dedal)',
                     "Jeyms Joys («Finneganning uyg'onishi»)",
                     'Semuel Bekket («Godoni kutib»)'],
              'ru': ['Джеймс Джойс («Портрет художника в юности»)',
                     'Джеймс Джойс («Улисс» — Стивен Дедал)',
                     'Джеймс Джойс («Поминки по Финнегану»)',
                     'Сэмюэл Беккет («В ожидании Годо»)'],
              'en': ["James Joyce ('A Portrait of the Artist as a Young Man')",
                     "James Joyce ('Ulysses' — Stephen Dedalus)",
                     "James Joyce ('Finnegans Wake')",
                     "Samuel Beckett ('Waiting for Godot')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Jeyms Joys («Uliss» — Stiven Dedal)',
                     'ru': 'Джеймс Джойс («Улисс» — Стивен Дедал)',
                     'en': "James Joyce ('Ulysses' — Stephen Dedalus)"},
  'image_url': None,
  'fun_fact': {'uz': '1922 yilda nashr etilgan va 1904 yil 16 iyun kunidagi Dublin hayotini qamrab olgan «Uliss» '
                     "modernistik adabiyotning eng murakkab cho'qqisidir.",
               'ru': 'Слова Стивена Дедала директору школы мистеру Дизи во втором эпизоде модернистского шедевра '
                     'Джойса «Улисс» (1922).',
               'en': "Stephen Dedalus's iconic definition of historical burden during a conversation with Mr. Deasy in "
                     "Joyce's revolutionary 1922 novel."},
  'aliases': ['uliss', 'joys', 'улисс', 'джойс', 'ulysses', 'james joyce']},
 {'id': 'lit_q_075',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Sargardon kezib yurganlarning barchasi ham yo'ldan adashgan emas; yaltiragan har narsa oltin "
                     "bo'lavermaydi...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Не все те бродяги, кто скитается; не всё то золото, что блестит...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'All that is gold does not glitter, / Not all those who wander are lost...'"},
  'options': {'uz': ['J.R.R. Tolkin («Xobbit»)',
                     'J.R.R. Tolkin («Silmarillion»)',
                     "J.R.R. Tolkin («Uzuklar hukmdori» — Aragorn haqidagi she'r)",
                     'K.S. Lyuis («Narniya yilnomalari»)'],
              'ru': ['Дж. Р. Р. Толкин («Хоббит»)',
                     'Дж. Р. Р. Толкин («Сильмариллион»)',
                     'Дж. Р. Р. Толкин («Властелин колец» — стих об Арагорне)',
                     'К. С. Льюис («Хроники Нарнии»)'],
              'en': ["J.R.R. Tolkien ('The Hobbit')",
                     "J.R.R. Tolkien ('The Silmarillion')",
                     "J.R.R. Tolkien ('The Lord of the Rings' — Riddle of Strider)",
                     "C.S. Lewis ('The Chronicles of Narnia')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "J.R.R. Tolkin («Uzuklar hukmdori» — Aragorn haqidagi she'r)",
                     'ru': 'Дж. Р. Р. Толкин («Властелин колец» — стих об Арагорне)',
                     'en': "J.R.R. Tolkien ('The Lord of the Rings' — Riddle of Strider)"},
  'image_url': None,
  'fun_fact': {'uz': "Bilbo Beggins tomonidan bo'lajak qirol Aragorn (Daydi) haqida yozilgan ushbu she'r jahon fentezi "
                     'adabiyotining eng sevimli baytlaridandir.',
               'ru': 'Знаменитое стихотворение Бильбо Бэггинса о страннике Следопыте, истинном наследнике трона '
                     'Гондора Арагорне.',
               'en': "Penned by Bilbo Baggins to identify the Ranger 'Strider' as Aragorn, the rightful heir of "
                     'Isildur.'},
  'aliases': ['uzuklar hukmdori', 'tolkin', 'властелин колец', 'толкин', 'lord of the rings', 'tolkien']},
 {'id': 'lit_q_076',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Jasoratli bo'l, azizim!» (Aslan ovozi)",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Мужайся, милое сердце!» (слова льва Аслана)',
               'en': "Which work or author is the source of this famous quote?\n\n'Courage, dear heart!'"},
  'options': {'uz': ['K.S. Lyuis («Arslon, jodugar va javon»)',
                     'J.K. Rouling («Garri Potter»)',
                     "Filip Pulman («Shimol yog'dusi»)",
                     'K.S. Lyuis («Narniya yilnomalari: Tong yulduzi sayohati»)'],
              'ru': ['К. С. Льюис («Лев, колдунья и платяной шкаф»)',
                     'Дж. К. Роулинг («Гарри Поттер»)',
                     'Филип Пулман («Северное сияние»)',
                     'К. С. Льюис («Хроники Нарнии: Покоритель зари»)'],
              'en': ["C.S. Lewis ('The Lion, the Witch and the Wardrobe')",
                     "J.K. Rowling ('Harry Potter')",
                     "Philip Pullman ('Northern Lights')",
                     "C.S. Lewis ('The Chronicles of Narnia: The Voyage of the Dawn Treader')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'K.S. Lyuis («Narniya yilnomalari: Tong yulduzi sayohati»)',
                     'ru': 'К. С. Льюис («Хроники Нарнии: Покоритель зари»)',
                     'en': "C.S. Lewis ('The Chronicles of Narnia: The Voyage of the Dawn Treader')"},
  'image_url': None,
  'fun_fact': {'uz': "Lyusi Pevensi Zulmat orolida tushkunlikka tushib umidsizlanganida ulug'vor arslon Aslan unga "
                     "ko'rinmasdan pichirlab umid bag'ishlaydi.",
               'ru': 'Великий Лев Аслан нашёптывает эти слова отчаявшейся Люси во тьме Тёмного острова.',
               'en': "Aslan's whispered comfort to Lucy Pevensie when lost in the terrifying darkness around the Dark "
                     'Island.'},
  'aliases': ['narniya', 'lyuis', 'aslan', 'хроники нарнии', 'к.с. льюис', 'chronicles of narnia', 'c.s. lewis']},
 {'id': 'lit_q_077',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Barcha hayvonlar tengdir, ammo ba'zi hayvonlar boshqalariga qaraganda tengroqdir!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Все животные равны, но некоторые животные равнее других!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'All animals are equal, but some animals are more equal than others!'"},
  'options': {'uz': ["Jorj Oruell («Molxona» / «Hayvonlar xo'jaligi»)",
                     'Jorj Oruell («1984»)',
                     'Artur Kestler («Zulmatdagi choshgoh»)',
                     'Oldos Xaksli («Orol»)'],
              'ru': ['Джордж Оруэлл (повесть-притча «Скотный двор»)',
                     'Джордж Оруэлл («1984»)',
                     'Артур Кёстлер («Слепящая тьма»)',
                     'Олдос Хаксли («Остров»)'],
              'en': ["George Orwell ('Animal Farm')",
                     "George Orwell ('1984')",
                     "Arthur Koestler ('Darkness at Noon')",
                     "Aldous Huxley ('Island')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Jorj Oruell («Molxona» / «Hayvonlar xo'jaligi»)",
                     'ru': 'Джордж Оруэлл (повесть-притча «Скотный двор»)',
                     'en': "George Orwell ('Animal Farm')"},
  'image_url': None,
  'fun_fact': {'uz': '1945 yilda yozilgan bu satirik qissada inqilobiy adolat shiorlarining diktatura tomonidan qanday '
                     "buzib talqin qilinishi ko'rsatilgan.",
               'ru': 'Единственная уцелевшая заповедь Скотного двора, наглядно разоблачающая лицемерие тоталитарной '
                     'элиты.',
               'en': "The ultimate corrupted commandment painted on the barn wall in Orwell's 1945 political satire."},
  'aliases': ['molxona', "hayvonlar xo'jaligi", 'oruell', 'скотный двор', 'оруэлл', 'animal farm']},
 {'id': 'lit_q_078',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Balki maxluq tashqarida emasdir... Balki u mahluq — bizning o'zimizdirmiz?!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Может быть, зверь и есть... Может, он внутри нас самих?!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Maybe there is a beast... maybe it's only us?!'"},
  'options': {'uz': ['Jon Steynbek («Sichqonlar va odamlar haqida»)',
                     'Uilyam Golding («Pashshalar tangrisi» — Saymon)',
                     "Jorj Oruell («Bir o'q otilishi»)",
                     'Entoni Byorjess («Murakkab apelsin»)'],
              'ru': ['Джон Стейнбек («О мышах и людях»)',
                     'Уильям Голдинг («Повелитель мух» — Саймон)',
                     'Джордж Оруэлл («Как я стрелял в слона»)',
                     'Энтони Бёрджесс («Заводной апельсин»)'],
              'en': ["John Steinbeck ('Of Mice and Men')",
                     "William Golding ('Lord of the Flies' — Simon)",
                     "George Orwell ('Shooting an Elephant')",
                     "Anthony Burgess ('A Clockwork Orange')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Uilyam Golding («Pashshalar tangrisi» — Saymon)',
                     'ru': 'Уильям Голдинг («Повелитель мух» — Саймон)',
                     'en': "William Golding ('Lord of the Flies' — Simon)"},
  'image_url': None,
  'fun_fact': {'uz': "Kimsasiz orolga tushib qolgan maktab o'quvchilarining yovvoyilashuvi orqali inson tabiati "
                     'tubidagi shafqatsizlikni tadqiq etgan 1954 yilgi mashhur roman.',
               'ru': 'Пророческое прозрение Саймона в романе-притче Голдинга о врождённой склонности человеческой '
                     'природы к жестокости и первобытному хаосу.',
               'en': "Simon's intuitive realization on the deserted island in Golding's 1954 Nobel-winning "
                     'psychological novel.'},
  'aliases': ['pashshalar tangrisi', 'golding', 'повелитель мух', 'голдинг', 'lord of the flies']},
 {'id': 'lit_q_079',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Insonni uning o'rniga o'zingni qo'yib ko'rmaguningcha, uning terisiga kirib sayr "
                     'qilmaguningcha, uni hech qachon tushunolmaysan.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Ты никогда по-настоящему не поймёшь человека, пока не взглянешь на вещи с его точки зрения... '
                     'пока не влезешь в его шкуру и не походишь в ней.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'You never really understand a person until you consider things from his point of view... until "
                     "you climb into his skin and walk around in it.'"},
  'options': {'uz': ['Truman Kapote («Yovvoyi tabiat sukunati»)',
                     "Karson Makkallers («Yurak yolg'iz ovchidir»)",
                     "Harper Li («Kiyikshosharni o'ldirish» — Attikus Finch)",
                     "Uilyam Folkner («Shovqin va g'azab»)"],
              'ru': ['Трумен Капоте («Хладнокровное убийство»)',
                     'Карсон Маккаллерс («Сердце — одинокий охотник»)',
                     'Харпер Ли («Убить пересмешника» — Аттикус Финч)',
                     'Уильям Фолкнер («Шум и ярость»)'],
              'en': ["Truman Capote ('In Cold Blood')",
                     "Carson McCullers ('The Heart Is a Lonely Hunter')",
                     "Harper Lee ('To Kill a Mockingbird' — Atticus Finch)",
                     "William Faulkner ('The Sound and the Fury')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Harper Li («Kiyikshosharni o'ldirish» — Attikus Finch)",
                     'ru': 'Харпер Ли («Убить пересмешника» — Аттикус Финч)',
                     'en': "Harper Lee ('To Kill a Mockingbird' — Atticus Finch)"},
  'image_url': None,
  'fun_fact': {'uz': 'Advokat Attikus Finch qizi Skautga bergan ushbu saboq empatiya, insoniylik va irqiy adolatning '
                     'jahon adabiyotidagi eng mashhur darsidir.',
               'ru': 'Главный этический урок адвоката Аттикуса Финча своей дочери Глазастику в романе 1960 года, '
                     'удостоенном Пулитцеровской премии.',
               'en': "Atticus Finch's classic advice on empathy to his daughter Scout in Harper Lee's Pulitzer "
                     'Prize-winning 1960 novel.'},
  'aliases': ["kiyikshosharni o'ldirish",
              'harper li',
              'убить пересмешника',
              'харпер ли',
              'to kill a mockingbird',
              'atticus finch']},
 {'id': 'lit_q_080',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Men javdarzor chetidagi qoya ustida turib, tubsiz jarlikka qulab tushayotgan bolachalarni tutib '
                     "oluvchi posbon bo'lishni xohlardim...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Я стою на самом краю обрыва над пропастью во ржи и ловлю ребятишек, чтобы они не сорвались...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'I have to catch everybody if they start to go over the cliff — I'd just be the catcher in the "
                     "rye and all.'"},
  'options': {'uz': ['Jon Apdayk («Quyon, yugur»)',
                     "Jek Keruak («Yo'lda»)",
                     'Ken Kizi («Kakkuning uyasi uzra parvoz»)',
                     'J.D. Selinjer («Javdarzordagi xaloskor» — Xolden Kolfild)'],
              'ru': ['Джон Апдайк («Кролик, беги»)',
                     'Джек Керуак («В дороге»)',
                     'Кен Кизи («Над кукушкиным гнездом»)',
                     'Дж. Д. Сэлинджер («Над пропастью во ржи» — Холден Колфилд)'],
              'en': ["John Updike ('Rabbit, Run')",
                     "Jack Kerouac ('On the Road')",
                     "Ken Kesey ('One Flew Over the Cuckoo's Nest')",
                     "J.D. Salinger ('The Catcher in the Rye' — Holden Caulfield)"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'J.D. Selinjer («Javdarzordagi xaloskor» — Xolden Kolfild)',
                     'ru': 'Дж. Д. Сэлинджер («Над пропастью во ржи» — Холден Колфилд)',
                     'en': "J.D. Salinger ('The Catcher in the Rye' — Holden Caulfield)"},
  'image_url': None,
  'fun_fact': {'uz': "1951 yilda nashr etilgan ushbu roman 16 yoshli o'smir Xolden Kolfildning yolg'onlarga to'la "
                     'kattalar dunyosiga qarshi isyonini ifodalaydi.',
               'ru': 'Сокровенная мечта 16-летнего подростка Холдена Колфилда защитить детскую невинность и '
                     'искренность от цинизма взрослых.',
               'en': "Holden Caulfield's heartfelt confession of his solitary desire to preserve childhood innocence "
                     'from falling into adulthood.'},
  'aliases': ['javdarzordagi xaloskor',
              'selinjer',
              'над пропастью во ржи',
              'сэлинджер',
              'catcher in the rye',
              'salinger']},
 {'id': 'lit_q_081',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Yovvoyi tabiatning yagona qonuni: yeng yoki yengil; ye yoki yem bo'l!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Закон добычи и закон дубины и клыка: ешь или съедят тебя; убей или будь убит!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'The law of club and fang: eat or be eaten; kill or be killed!'"},
  'options': {'uz': ["Jek London («Oqso'yloq» / «Ajdodlar chorlovi»)",
                     "Jek London («Dengiz bo'risi»)",
                     'Jek London («Martin Iden»)',
                     "Ernest Seton-Tompson («Yovvoyi yo'rg'a»)"],
              'ru': ['Джек Лондон («Белый Клык» / «Зов предков»)',
                     'Джек Лондон («Морской волк»)',
                     'Джек Лондон («Мартин Иден»)',
                     'Эрнест Сетон-Томпсон («Мустанг-иноходец»)'],
              'en': ["Jack London ('White Fang' / 'The Call of the Wild')",
                     "Jack London ('The Sea-Wolf')",
                     "Jack London ('Martin Eden')",
                     "Ernest Thompson Seton ('Wild Animals I Have Known')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Jek London («Oqso'yloq» / «Ajdodlar chorlovi»)",
                     'ru': 'Джек Лондон («Белый Клык» / «Зов предков»)',
                     'en': "Jack London ('White Fang' / 'The Call of the Wild')"},
  'image_url': None,
  'fun_fact': {'uz': "Jek Londonning Alyaska va Klondayk oltin izlovchilari davrida itlar va bo'rilar hayotini aks "
                     'ettirgan qahramonlik qissalari.',
               'ru': 'Суровый закон северной глуши, сформулированный Джеком Лондоном в его знаменитых северных '
                     'повестях.',
               'en': "Jack London's primal doctrine of wilderness survival in the frozen Yukon and Klondike gold rush "
                     'country.'},
  'aliases': ["oqso'yloq", 'jek london', 'белый клык', 'джек лондон', 'white fang', 'jack london']},
 {'id': 'lit_q_082',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Sovg'a ulashuvchi barcha donishmandlar ichida bu ikki yosh oshiq eng donolari edilar...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Из всех, кто преподносит дары, эти двое были мудрейшими...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Of all who give gifts these two were the wisest...'"},
  'options': {'uz': ["O. Genri («So'nggi yaproq»)",
                     "O. Genri («Sehrgarlarning sovg'alari» — Jim va Della)",
                     'O. Genri («Qizil tanlilar dohiysi»)',
                     'O. Genri («Yashil eshik»)'],
              'ru': ['О. Генри («Последний лист»)',
                     'О. Генри (новелла «Дары волхвов» — Джим и Делла)',
                     'О. Генри («Вождь краснокожих»)',
                     'О. Генри («Зелёная дверь»)'],
              'en': ["O. Henry ('The Last Leaf')",
                     "O. Henry ('The Gift of the Magi' — Jim and Della)",
                     "O. Henry ('The Ransom of Red Chief')",
                     "O. Henry ('The Green Door')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "O. Genri («Sehrgarlarning sovg'alari» — Jim va Della)",
                     'ru': 'О. Генри (новелла «Дары волхвов» — Джим и Делла)',
                     'en': "O. Henry ('The Gift of the Magi' — Jim and Della)"},
  'image_url': None,
  'fun_fact': {'uz': 'Rojdestvo arafasida Jim soatiga zanjir olish uchun sochini sotgan Dellaga taroq oladi, Della esa '
                     "Jimning soatiga zanjir olish uchun o'z sochini sotgan edi.",
               'ru': 'Классическая рождественская новелла 1905 года о самопожертвовании влюблённых супругов ради '
                     'счастья друг друга.',
               'en': "O. Henry's celebrated 1905 twist-ending tale of impoverished young spouses sacrificing their "
                     'greatest treasures for love.'},
  'aliases': ["sehrgarlarning sovg'alari", 'o genri', 'дары волхвов', 'о генри', 'gift of the magi', 'o henry']},
 {'id': 'lit_q_083',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Men o'zimni nishonlayman va o'zimni kuylayman,\n"
                     'Va men nimani qabul qilsam, siz ham shuni qabul qilursiz!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Я славлю себя и воспеваю себя,\n'
                     'И то, что я принимаю, вы примете тоже...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'I celebrate myself, and sing myself,\n"
                     "And what I assume you shall assume...'"},
  'options': {'uz': ["Genri Toro («Uolden, yoki o'rmondagi hayot»)",
                     "Ralf Uoldo Emerson («O'z kuchiga ishonch»)",
                     "Uolt Uitmen («Maysa yaproqlari» — «O'zim haqimda qo'shiq»)",
                     "Gerdert Longfello («Gayavata haqida qo'shiq»)"],
              'ru': ['Генри Торо («Уолден, или Жизнь в лесах»)',
                     'Ральф Уолдо Эмерсон («Доверие к себе»)',
                     'Уолт Уитмен («Листья травы» — «Песня о себе»)',
                     'Генри Лонгфелло («Песнь о Гайавате»)'],
              'en': ["Henry David Thoreau ('Walden')",
                     "Ralph Waldo Emerson ('Self-Reliance')",
                     "Walt Whitman ('Leaves of Grass' — 'Song of Myself')",
                     "Henry Wadsworth Longfellow ('The Song of Hiawatha')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Uolt Uitmen («Maysa yaproqlari» — «O'zim haqimda qo'shiq»)",
                     'ru': 'Уолт Уитмен («Листья травы» — «Песня о себе»)',
                     'en': "Walt Whitman ('Leaves of Grass' — 'Song of Myself')"},
  'image_url': None,
  'fun_fact': {'uz': "1855 yilda chop etilgan «Maysa yaproqlari» erkin vazn (verlibir) orqali Amerika she'riyatida "
                     'inqilob yasadi.',
               'ru': 'Знаменитый зачин американского поэтического манифеста 1855 года, сломавшего все традиционные '
                     'каноны европейского стиха.',
               'en': "The pioneering opening invocation of Whitman's 1855 masterpiece, which reshaped democratic world "
                     'poetry with free verse.'},
  'aliases': ['maysa yaproqlari', 'uitmen', 'листья травы', 'уитмен', 'walt whitman', 'leaves of grass']},
 {'id': 'lit_q_084',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Umid — patlari bor qushga o'xshaydi,\n"
                     "U qalb shoxiga qo'nib, so'zsiz qo'shiq kuylaydi...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Надежда — это оперенье,\n'
                     'Она в душе поёт без слов...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Hope is the thing with feathers\n"
                     'That perches in the soul,\n'
                     "And sings the tune without the words...'"},
  'options': {'uz': ['Kristina Rossetti («Eslash»)',
                     'Elizabet Barrett Brauning («Portugalcha sonetlar»)',
                     'Silviya Plat («Lolalar»)',
                     "Emili Dikinson («Umid — patli jonzot» she'ri)"],
              'ru': ['Кристина Россетти («Помни»)',
                     'Элизабет Барретт Браунинг («Сонеты с португальского»)',
                     'Сильвия Плат («Тюльпаны»)',
                     'Эмили Дикинсон (стихотворение «Надежда — создание с крыльями»)'],
              'en': ["Christina Rossetti ('Remember')",
                     "Elizabeth Barrett Browning ('Sonnets from the Portuguese')",
                     "Sylvia Plath ('Tulips')",
                     "Emily Dickinson ('Hope is the thing with feathers')"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Emili Dikinson («Umid — patli jonzot» she'ri)",
                     'ru': 'Эмили Дикинсон (стихотворение «Надежда — создание с крыльями»)',
                     'en': "Emily Dickinson ('Hope is the thing with feathers')"},
  'image_url': None,
  'fun_fact': {'uz': "Hayotlik chog'ida bor-yo'g'i o'nga yaqin she'ri bosilgan buyuk amerikalik shoira Emili "
                     "Dikinsonning 1800 ga yaqin she'riy merosi vafotidan so'ng topilgan.",
               'ru': 'Одно из самых пронзительных стихотворений затворницы из Амхерста Эмили Дикинсон, ставшее '
                     'символом неиссякаемой надежды.',
               'en': "One of Emily Dickinson's best-loved lyrics, found among roughly 1,800 poems preserved in "
                     'hand-sewn booklets after her death.'},
  'aliases': ['emili dikinson', 'dikinson', 'эмили дикинсон', 'дикинсон', 'emily dickinson', 'hope is the thing']},
 {'id': 'lit_q_085',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Sariq o'rmonda yo'l ikkiga ayrildi,\n"
                     "Va men — kamroq odam yurgan yo'ldan ketdim,\n"
                     'Va barcha farqni mana shu yaratdi!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«В осеннем лесу развилка дорог,\n'
                     'И я выбрал ту, где следов почти не видать,\n'
                     'И это решило всё остальное!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Two roads diverged in a wood, and I —\n"
                     'I took the one less traveled by,\n'
                     "And that has made all the difference.'"},
  'options': {'uz': ["Robert Frost («Tanlanmagan yo'l» she'ri)",
                     "Robert Frost («Qorli oqshomda to'xtash»)",
                     'Uilyam Batler Yeyts («Innisfri oroli»)',
                     "Uolles Stivens («Qora qarg'aga qarashning o'n uch usuli»)"],
              'ru': ['Роберт Фрост (стихотворение «Другая дорога» / «Неизбранная стезя»)',
                     'Роберт Фрост («Остановка в лесу снежным вечером»)',
                     'Уильям Батлер Йейтс («Озёрный остров Иннисфри»)',
                     'Уоллес Стивенс («Тринадцать способов увидеть дрозда»)'],
              'en': ["Robert Frost ('The Road Not Taken')",
                     "Robert Frost ('Stopping by Woods on a Snowy Evening')",
                     "W.B. Yeats ('The Lake Isle of Innisfree')",
                     "Wallace Stevens ('Thirteen Ways of Looking at a Blackbird')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Robert Frost («Tanlanmagan yo'l» she'ri)",
                     'ru': 'Роберт Фрост (стихотворение «Другая дорога» / «Неизбранная стезя»)',
                     'en': "Robert Frost ('The Road Not Taken')"},
  'image_url': None,
  'fun_fact': {'uz': "1916 yilda chop etilgan ushbu she'r inson hayotidagi tanlov va uning taqdirni butkul "
                     "o'zgartiruvchi kuchi haqidagi eng mashhur asardir.",
               'ru': 'Стихотворение 1916 года четырёхкратного пулитцеровского лауреата Роберта Фроста — всемирная '
                     'аллегория жизненного выбора.',
               'en': 'Published in 1916 by four-time Pulitzer laureate Robert Frost, this poem remains an immortal '
                     'cultural metaphor for non-conformity.'},
  'aliases': ['robert frost', "tanlanmagan yo'l", 'роберт фрост', 'неизбранная стезя', 'road not taken', 'frost']},
 {'id': 'lit_q_086',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Stolda sham yonardi, sham yonardi...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Свеча горела на столе,\n'
                     'Свеча горела...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'A candle burned upon the table,\n"
                     "A candle burned...'"},
  'options': {'uz': ['Osip Mandelshtam («Vaqt shovqini»)',
                     "Boris Pasternak («Doktor Jivago» — Yuriy Jivago she'rlari / «Qishki tun»)",
                     'Anna Axmatova («Qahramonsiz doston»)',
                     'Marina Svetayeva («Ajralish»)'],
              'ru': ['Осип Мандельштам («Шум времени»)',
                     'Борис Пастернак («Доктор Живаго» — стихотворение «Зимняя ночь»)',
                     'Анна Ахматова («Поэма без героя»)',
                     'Марина Цветаева («Разлука»)'],
              'en': ["Osip Mandelstam ('The Noise of Time')",
                     "Boris Pasternak ('Doctor Zhivago' — 'Winter Night')",
                     "Anna Akhmatova ('Poem Without a Hero')",
                     "Marina Tsvetaeva ('The Separation')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Boris Pasternak («Doktor Jivago» — Yuriy Jivago she'rlari / «Qishki tun»)",
                     'ru': 'Борис Пастернак («Доктор Живаго» — стихотворение «Зимняя ночь»)',
                     'en': "Boris Pasternak ('Doctor Zhivago' — 'Winter Night')"},
  'image_url': None,
  'fun_fact': {'uz': "1957 yilda Italiyada e'lon qilingan va 1958 yilda Pasternakka Nobel mukofotini keltirgan «Doktor "
                     "Jivago» romanining eng mashhur she'riy satrlari.",
               'ru': 'Бессмертные строки из стихотворения Юрия Живаго «Зимняя ночь», входящего в поэтическую тетрадь в '
                     'финале романа.',
               'en': "The lyrical refrain of Yurii Zhivago's poem 'Winter Night', featured at the conclusion of "
                     "Pasternak's 1957 Nobel Prize novel."},
  'aliases': ['doktor jivago', 'pasternak', 'доктор живаго', 'пастернак', 'свеча горела', 'doctor zhivago']},
 {'id': 'lit_q_087',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Ey sokin Don, bizning aziz otamiz, nega endi loyqa bo'lib oqasan?..»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Ой ты, наш батюшка тихий Дон, что же ты, тихий Дон, мутнёхонек течёшь?..»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'O thou, our father, quiet Don, why dost thou flow so muddied?..'"},
  'options': {'uz': ["Mixail Sholoxov («Ochilgan qo'riq»)",
                     'Mixail Sholoxov («Inson taqdiri»)',
                     'Mixail Sholoxov («Tinch oqar Don» romanining epigrafi)',
                     'Aleksandr Fadeyev («Tor-mor»)'],
              'ru': ['Михаил Шолохов («Поднятая целина»)',
                     'Михаил Шолохов («Судьба человека»)',
                     'Михаил Шолохов (эпиграф к роману «Тихий Дон»)',
                     'Александр Фадеев («Разгром»)'],
              'en': ["Mikhail Sholokhov ('Virgin Soil Upturned')",
                     "Mikhail Sholokhov ('The Fate of a Man')",
                     "Mikhail Sholokhov ('And Quiet Flows the Don' — Epigraph)",
                     "Aleksandr Fadeyev ('The Rout')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Mixail Sholoxov («Tinch oqar Don» romanining epigrafi)',
                     'ru': 'Михаил Шолохов (эпиграф к роману «Тихий Дон»)',
                     'en': "Mikhail Sholokhov ('And Quiet Flows the Don' — Epigraph)"},
  'image_url': None,
  'fun_fact': {'uz': 'Grigoriy Melexov va Aksinya taqdiri fonida Fuqarolar urushining fojiali sahifalarini aks '
                     'ettirgan ushbu roman Sholoxovga 1965 yilda Nobel mukofotini keltirgan.',
               'ru': 'Казачья песня-эпиграф задаёт трагический тон эпопее Шолохова о судьбе Григория Мелехова, '
                     'отмеченной Нобелевской премией 1965 года.',
               'en': "The Cossack song epigraph to Sholokhov's epic saga of Grigory Melekhov, which won the 1965 Nobel "
                     'Prize in Literature.'},
  'aliases': ['tinch oqar don', 'sholoxov', 'тихий дон', 'шолохов', 'quiet flows the don']},
 {'id': 'lit_q_088',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Eslab ko'r, kimning o'g'lisan? Oting nima? Esla, sen Jo'lamonmisan?!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Вспомни, чей ты сын? Как твое имя? Вспомни, ты ведь Жоламан?!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Remember whose son you are! What is your name? Remember, are you not Joolaman?!'"},
  'options': {'uz': ['Chingiz Aytmatov («Oq kema»)',
                     'Chingiz Aytmatov («Kunda»)',
                     'Chingiz Aytmatov («Sarvqomat dilbarim»)',
                     'Chingiz Aytmatov («Asrga tatigulik kun» — Nayman ona va Mankurt)'],
              'ru': ['Чингиз Айтматов («Белый пароход»)',
                     'Чингиз Айтматов («Плаха»)',
                     'Чингиз Айтматов («Тополёк мой в красной косынке»)',
                     'Чингиз Айтматов («И дольше века длится день» — Найман-Ана и манкурт)'],
              'en': ["Chingiz Aitmatov ('The White Steamship')",
                     "Chingiz Aitmatov ('The Scaffold')",
                     "Chingiz Aitmatov ('My Little Poplar in a Red Headscarf')",
                     "Chingiz Aitmatov ('The Day Lasts More Than a Hundred Years' — Mankurt Legend)"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Chingiz Aytmatov («Asrga tatigulik kun» — Nayman ona va Mankurt)',
                     'ru': 'Чингиз Айтматов («И дольше века длится день» — Найман-Ана и манкурт)',
                     'en': "Chingiz Aitmatov ('The Day Lasts More Than a Hundred Years' — Mankurt Legend)"},
  'image_url': None,
  'fun_fact': {'uz': "Aytmatovning ushbu asarida o'z xotirasi va ildizlaridan judo qilingan qul — 'mankurt' "
                     'tushunchasi jahon adabiyotiga kirdi.',
               'ru': 'Крик отчаяния Найман-Аны над сыном, превращённым жуаньжуанями в бездушного манкурта; притча о '
                     'потере исторической памяти.',
               'en': "Nayman-Ana's tragic cry to her amnesiac enslaved son introduced the concept of the 'mankurt' "
                     'into world literature.'},
  'aliases': ['asrga tatigulik kun', 'aytmatov', 'mankurt', 'и дольше века длится день', 'айтматов', 'манкурт']},
 {'id': 'lit_q_089',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "Lui Aragon uni «Dunyodagi eng go'zal muhabbat qissasi» deb atagan asar qaysi?",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     'Какую повесть Луи Арагон назвал «Самой прекрасной историей любви на свете»?',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "Which novella was famously praised by Louis Aragon as 'The most beautiful love story in the "
                     "world'?"},
  'options': {'uz': ['Chingiz Aytmatov («Jamila» qissasi)',
                     'Chingiz Aytmatov («Birinchi muallim»)',
                     'Chingiz Aytmatov («Momo yer»)',
                     'Chingiz Aytmatov («Alvido, Gulsari!»)'],
              'ru': ['Чингиз Айтматов (повесть «Джамиля»)',
                     'Чингиз Айтматов («Первый учитель»)',
                     'Чингиз Айтматов («Материнское поле»)',
                     'Чингиз Айтматов («Прощай, Гульсары!»)'],
              'en': ["Chingiz Aitmatov ('Jamila' Novella)",
                     "Chingiz Aitmatov ('The First Teacher')",
                     "Chingiz Aitmatov ('Mother Earth')",
                     "Chingiz Aitmatov ('Farewell, Gulsary!')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Chingiz Aytmatov («Jamila» qissasi)',
                     'ru': 'Чингиз Айтматов (повесть «Джамиля»)',
                     'en': "Chingiz Aitmatov ('Jamila' Novella)"},
  'image_url': None,
  'fun_fact': {'uz': '1958 yilda yozilgan «Jamila» qissasi yosh rassom Seit xotiralari orqali Jamila va Doniyorning '
                     "jasur muhabbatini ochib beradi va Aytmatovga jahon e'tirofini keltirgan.",
               'ru': 'Французский поэт Луи Арагон лично перевёл «Джамилю» на французский язык в 1959 году, открыв '
                     'талант молодого Айтматова Европе.',
               'en': "Translated into French by Louis Aragon in 1959, 'Jamila' vaulted the young Kyrgyz writer onto "
                     'the global literary stage.'},
  'aliases': ['jamila', 'aytmatov', 'джамиля', 'айтматов', 'jamila aitmatov']},
 {'id': 'lit_q_090',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Sening ikki ertaging bor edi: biri — o'zingniki, boshqasi esa bobong aytib bergan Shoxdor ona "
                     'kiyik ertagi edi...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«У тебя было две сказки: одна своя, другая та, которую рассказывал дед — сказка о Рогатой '
                     'матери-оленихе...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'You had two fairy tales: one was your own, and the other was the one your grandfather told you "
                     "about the Horned Mother Deer...'"},
  'options': {'uz': ['Chingiz Aytmatov («Dengiz yoqalab chopayotgan olapar»)',
                     'Chingiz Aytmatov («Oq kema» qissasi)',
                     'Chingiz Aytmatov («Erta qaytgan turnalar»)',
                     'Chingiz Aytmatov («Kunda»)'],
              'ru': ['Чингиз Айтматов («Пегий пёс, бегущий краем моря»)',
                     'Чингиз Айтматов (повесть «Белый пароход»)',
                     'Чингиз Айтматов («Ранние журавли»)',
                     'Чингиз Айтматов («Плаха»)'],
              'en': ["Chingiz Aitmatov ('Piebald Dog Running Along the Shore')",
                     "Chingiz Aitmatov ('The White Ship' / 'The White Steamship')",
                     "Chingiz Aitmatov ('Early Cranes')",
                     "Chingiz Aitmatov ('The Scaffold')"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Chingiz Aytmatov («Oq kema» qissasi)',
                     'ru': 'Чингиз Айтматов (повесть «Белый пароход»)',
                     'en': "Chingiz Aitmatov ('The White Ship' / 'The White Steamship')"},
  'image_url': None,
  'fun_fact': {'uz': "Orolsiz qolgan bolakayning daryo bo'ylab Oq kemaga yetish orzusi va tabiatning ezgulik ramzi "
                     "bo'lgan kiyik fojiasi tasvirlangan chuqur gumanistik qissa.",
               'ru': 'Пронзительная трагедия чистого детского сердца семилетнего мальчика у озера Иссык-Куль, '
                     'мечтавшего превратиться в рыбу.',
               'en': 'A poignant tragedy about an innocent seven-year-old boy living in the Tien Shan mountains who '
                     'dreams of swimming to the white ship.'},
  'aliases': ['oq kema', 'aytmatov', 'белый пароход', 'айтматов', 'white ship', 'white steamship']},
 {'id': 'lit_q_091',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Inson har qadamda o'z vijdon ko'prigidan o'tadi; bu ko'prikdan yiqilmaslik — hayotning eng oliy "
                     'burchidir.»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Человек на каждом шагу переходит мост собственной совести; не сорваться с этого моста — высший '
                     'долг жизни.»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'At every step in life a man crosses the bridge of his own conscience; not falling from this "
                     "bridge is life's highest duty.'"},
  'options': {'uz': ['Shukur Xolmirzayev («Yovvoyi gul»)',
                     "O'tkir Hoshimov («Ikki eshik orasi»)",
                     "Shukur Xolmirzayev («Qil ko'prik» romani)",
                     "Tog'ay Murod («Ot kishnagan oqshom»)"],
              'ru': ['Шукур Холмирзаев («Дикий цветок»)',
                     'Уткир Хашимов («Между двух дверей»)',
                     'Шукур Холмирзаев (роман «Волосяной мост» / «Мост над бездной»)',
                     'Тогай Мурад («Вечер, когда ржал конь»)'],
              'en': ["Shukur Kholmirzaev ('Wild Flower')",
                     "O'tkir Hoshimov ('Between Two Doors')",
                     "Shukur Kholmirzaev ('Hair-Thin Bridge' Novel)",
                     "Toghay Murad ('The Evening the Horse Neighed')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "Shukur Xolmirzayev («Qil ko'prik» romani)",
                     'ru': 'Шукур Холмирзаев (роман «Волосяной мост» / «Мост над бездной»)',
                     'en': "Shukur Kholmirzaev ('Hair-Thin Bridge' Novel)"},
  'image_url': None,
  'fun_fact': {'uz': "Shukur Xolmirzayev o'zbek nasrida inson ruhiyatining murakkab qirralarini, qishloq odamlari "
                     'hayoti va shafqatsiz haqiqatni yuksak realizm bilan ifodalagan adibdir.',
               'ru': 'Шукур Холмирзаев — признанный мастер узбекской психологической прозы, исследовавший нравственный '
                     'выбор человека.',
               'en': "Kholmirzaev's novel 'Qil ko'prik' (Hair-Thin Bridge) explores the precarious moral choices "
                     'confronting individuals during tumultuous historic changes.'},
  'aliases': ["qil ko'prik", 'shukur xolmirzayev', 'шукур холмирзаев', 'kholmirzaev']},
 {'id': 'lit_q_092',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Men Hoshimjonman! O'sha mashhur sehrli qalpoqcha egasi bo'lgan Hoshimjonman!»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Я Хашимджан! Тот самый Хашимджан, хозяин знаменитой волшебной шапки-невидимки!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'I am Hoshimjon! The very same Hoshimjon who owned the famous magic invisibility cap!'"},
  'options': {'uz': ["Xudoyberdi To'xtaboyev («Shirin qovunlar mamlakati»)",
                     "Xudoyberdi To'xtaboyev («Mungli ko'zlar»)",
                     "G'afur G'ulom («Shum bola»)",
                     "Xudoyberdi To'xtaboyev («Sariq devni minib»)"],
              'ru': ['Худайберды Тухтабаев («Страна сладких дынь»)',
                     'Худайберды Тухтабаев («Печальные глаза»)',
                     'Гафур Гулям («Озорник»)',
                     'Худайберды Тухтабаев (повесть «Верхом на жёлтом диве» / «Волшебная шапка»)'],
              'en': ["Khudoyberdi Tukhtabayev ('Land of Sweet Melons')",
                     "Khudoyberdi Tukhtabayev ('Sorrowful Eyes')",
                     "Ghafur Ghulam ('The Mischievous Boy')",
                     "Khudoyberdi Tukhtabayev ('Riding the Yellow Giant')"]},
  'correct_index': 3,
  'correct_answer': {'uz': "Xudoyberdi To'xtaboyev («Sariq devni minib»)",
                     'ru': 'Худайберды Тухтабаев (повесть «Верхом на жёлтом диве» / «Волшебная шапка»)',
                     'en': "Khudoyberdi Tukhtabayev ('Riding the Yellow Giant')"},
  'image_url': None,
  'fun_fact': {'uz': "1968 yilda yozilgan bu asar dunyoning o'nlab tillariga tarjima qilingan va o'zbek bolalar "
                     'adabiyotining jahon miqyosidagi eng mashhur qahramoni Hoshimjonni yaratgan.',
               'ru': 'Классическая узбекская сказочная повесть Тухтабаева переведена на немецкий, итальянский, '
                     'французский и десятки других языков.',
               'en': "Tukhtabayev's classic 1968 children's novel follows lazy yet ambitious village boy Hoshimjon who "
                     'acquires an invisibility cap.'},
  'aliases': ['sariq devni minib', "xudoyberdi to'xtaboyev", 'верхом на желтом диве', 'тухтабаев', 'hoshimjon']},
 {'id': 'lit_q_093',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Homilador xotinining bittagina anor yeyish orzusini ushaltirish uchun qishloqma-qishloq sarson '
                     'kezgan Turobjon qismati...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Трагическая история бедняка Турабджана, скитавшегося по садам, чтобы исполнить скромное желание '
                     'беременной жены съесть гранат...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'The tragic plight of poor Turobjon, wandering desperately from orchard to orchard to find a "
                     "single pomegranate for his pregnant wife...'"},
  'options': {'uz': ['Abdulla Qahhor («Anor» hikoyasi)',
                     'Abdulla Qahhor («Bemor»)',
                     "Abdulla Qahhor («O'g'ri»)",
                     'Abdulla Qahhor («Dahshat»)'],
              'ru': ['Абдулла Каххар (рассказ «Гранат»)',
                     'Абдулла Каххар («Больная»)',
                     'Абдулла Каххар («Вор»)',
                     'Абдулла Каххар («Ужас»)'],
              'en': ["Abdulla Qahhor ('The Pomegranate' Story)",
                     "Abdulla Qahhor ('The Patient')",
                     "Abdulla Qahhor ('The Thief')",
                     "Abdulla Qahhor ('The Horror')"]},
  'correct_index': 0,
  'correct_answer': {'uz': 'Abdulla Qahhor («Anor» hikoyasi)',
                     'ru': 'Абдулла Каххар (рассказ «Гранат»)',
                     'en': "Abdulla Qahhor ('The Pomegranate' Story)"},
  'image_url': None,
  'fun_fact': {'uz': "O'zbek adabiyotining 'Chexovi' deb atalgan Abdulla Qahhorning «Anor» hikoyasi oddiy xalqning "
                     'ayanchli qashshoqligi va insoniy fojiasini yuksak badiiy qudrat bilan aks ettiradi.',
               'ru': 'Шедевр малой прозы Абдуллы Каххара, обнажающий бесправие и нищету дехкан в дореволюционной '
                     'Средней Азии.',
               'en': 'A masterpiece of the Uzbek short story by Abdulla Qahhor, demonstrating the devastating social '
                     'inequality of the pre-revolutionary era.'},
  'aliases': ['anor', 'abdulla qahhor', 'гранат', 'абдулла каххар', 'qahhor anor']},
 {'id': 'lit_q_094',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Qobil boboning birdan-bir boquvchisi bo'lgan ho'kizi o'g'irlandi. Ammo uni qidirib amaldorlarga "
                     "murojaat qilgani unga ho'kiz yo'qotishdan ham qimmatga tushdi...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«У деда Кабыла украли единственного кормильца — вола. Но хождение по чиновникам обошлось ему '
                     'дороже самого вола...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Old Qobil's sole provider, his ox, was stolen. But appealing to corrupt officials cost him far "
                     "more than losing the ox itself...'"},
  'options': {'uz': ['Abdulla Qahhor («Mayiz yemagan xotin»)',
                     "Abdulla Qahhor («O'g'ri» hikoyasi)",
                     'Abdulla Qahhor («Asror bobo»)',
                     "G'afur G'ulom («Mening o'g'rigina bolam»)"],
              'ru': ['Абдулла Каххар («Жена, не знавшая изюма»)',
                     'Абдулла Каххар (рассказ «Вор»)',
                     'Абдулла Каххар («Дед Асрор»)',
                     'Гафур Гулям («Мой сыночек воришка»)'],
              'en': ["Abdulla Qahhor ('The Wife Who Never Ate Raisins')",
                     "Abdulla Qahhor ('The Thief' Story)",
                     "Abdulla Qahhor ('Grandfather Asror')",
                     "Ghafur Ghulam ('My Little Thief Boy')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Abdulla Qahhor («O'g'ri» hikoyasi)",
                     'ru': 'Абдулла Каххар (рассказ «Вор»)',
                     'en': "Abdulla Qahhor ('The Thief' Story)"},
  'image_url': None,
  'fun_fact': {'uz': "«O'g'ri» hikoyasida poraxo'rlik va amaldorlar zulmi satirik fosh qilinadi; qishloq oqsoqoli, "
                     'ellikboshi va pristav boboni butunlay xonavayron qilishadi.',
               'ru': 'Острая социальная сатира Абдуллы Каххара, в которой истинными ворами оказываются не похитители '
                     'вола, а царские чиновники и волостные.',
               'en': "Qahhor's famous satire exposes how the corrupt colonial bureaucracy plunders impoverished "
                     'villagers worse than any common thief.'},
  'aliases': ["o'g'ri", 'abdulla qahhor', 'вор', 'абдулла каххар', 'the thief']},
 {'id': 'lit_q_095',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Dunyoda odam bo'lib tug'ilish oson, ammo oxirigacha odam bo'lib yashash naqadar qiyin...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«В этом мире легко родиться человеком, но как трудно прожить до конца настоящим Человеком...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'In this world it is easy to be born human, yet how terribly hard it is to live as a true Human "
                     "Being until the end...'"},
  'options': {'uz': ["O'lmas Umarbekov («Fotima va Zuhra»)",
                     "O'lmas Umarbekov («Sevgim — sevgilim»)",
                     "O'lmas Umarbekov («Odam bo'lish qiyin» romani)",
                     'Shukur Xolmirzayev («Bandiy»)'],
              'ru': ['Ульмас Умарбеков («Фатима и Зухра»)',
                     'Ульмас Умарбеков («Любовь моя — радость моя»)',
                     'Ульмас Умарбеков (роман «Трудно быть человеком»)',
                     'Шукур Холмирзаев («Пленник»)'],
              'en': ["O'lmas Umarbekov ('Fatima and Zuhra')",
                     "O'lmas Umarbekov ('My Love, My Beloved')",
                     "O'lmas Umarbekov ('It's Hard to Be a Human Being')",
                     "Shukur Kholmirzaev ('The Captive')"]},
  'correct_index': 2,
  'correct_answer': {'uz': "O'lmas Umarbekov («Odam bo'lish qiyin» romani)",
                     'ru': 'Ульмас Умарбеков (роман «Трудно быть человеком»)',
                     'en': "O'lmas Umarbekov ('It's Hard to Be a Human Being')"},
  'image_url': None,
  'fun_fact': {'uz': '1970 yilda yaratilgan bu asar yoshlarning axloqiy tarbiyasi, vijdon pokligi va xudbinlik '
                     "oqibatlari haqidagi eng ta'sirli o'zbek romanlaridan biridir.",
               'ru': 'Популярнейший роман Ульмаса Умарбекова о становлении личности, нравственной ответственности и '
                     'цене эгоизма.',
               'en': "Umarbekov's 1970 coming-of-age novel explores adolescent moral responsibility, conscience, and "
                     'the tragic consequences of betrayal.'},
  'aliases': ["odam bo'lish qiyin", "o'lmas umarbekov", 'трудно быть человеком', 'ульмас умарбеков']},
 {'id': 'lit_q_096',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Qarag'aylar shovullaydi qoya boshida,\n"
                     'Burgut qanot qoqadi bulut qoshida...\n'
                     'Ona tuproq, sening har bir toshing muqaddas!»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Шумят сосны на вершине скалы,\n'
                     'Бьёт крыльями беркут подле облаков...\n'
                     'О родная земля, священен каждый твой камень!»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Pine trees rustle on the rocky heights,\n"
                     'The golden eagle beats its wings near passing clouds...\n'
                     "O Mother Earth, every stone of thine is sacred!'"},
  'options': {'uz': ['Mirtemir («Zebu zebu»)',
                     'Usmon Nosir («Naxshon»)',
                     'Shuhrat («Oltin zanglamas»)',
                     'Mirtemir («Surat» dostoni)'],
              'ru': ['Миртемир («Зебу-зебу»)',
                     'Усман Насыр («Нахшон»)',
                     'Шухрат («Золото не ржавеет»)',
                     'Миртемир (поэма «Сурат»)'],
              'en': ["Mirtemir ('Zebu-zebu')",
                     "Usmon Nosir ('Nakhshon')",
                     "Shukhrat ('Gold Never Rusts')",
                     "Mirtemir ('Surat' Poem)"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Mirtemir («Surat» dostoni)',
                     'ru': 'Миртемир (поэма «Сурат»)',
                     'en': "Mirtemir ('Surat' Poem)"},
  'image_url': None,
  'fun_fact': {'uz': "O'zbekiston xalq shoiri Mirtemir milliy she'riyatimizda o'ziga xos xalqona til, dostonchilik "
                     "an'anasi va tabiat tasvirining betakror ustasi edi.",
               'ru': 'Народный поэт Узбекистана Миртемир прославился богатым фольклорным языком и глубокой верностью '
                     'родным степям и горам.',
               'en': "People's Poet of Uzbekistan Mirtemir was celebrated for his folksy diction, idiomatic "
                     'authenticity, and passionate nature imagery.'},
  'aliases': ['mirtemir', 'surat', 'миртемир', 'поэма сурат']},
 {'id': 'lit_q_097',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Salqin saharlarda, bodom gulida,\n'
                     'Binafsha labida, yerning tilida,\n'
                     "Har bahor kelganda seni so'roqlab,\n"
                     "Ko'nglim xazon bo'lar mening yo'lingda...»",
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«В прохладных зорях, в цветении миндаля,\n'
                     'На устах фиалок, где поёт земля,\n'
                     'Каждую весну я ищу тебя с тоской,\n'
                     'Сердце осыпается осеннею листвой...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'In the cool dawns, upon the almond blossom,\n"
                     "On the violet's petal, on the speaking earth,\n"
                     'With every spring arriving, searching for thee,\n'
                     "My heart turns to autumn leaves upon thy path...'"},
  'options': {'uz': ["Zulfiya («Bahor keldi seni so'roqlab» — Hamid Olimjonga bag'ishlov)",
                     'Zulfiya («Hulkar»)',
                     "Zulfiya («Qo'ng'iroq»)",
                     'Halima Xudoyberdiyeva («Dorilbaqo»)'],
              'ru': ['Зульфия (стихотворение «Весна пришла, тебя окликнув» — памяти Хамида Алимджана)',
                     'Зульфия («Хулькар»)',
                     'Зульфия («Колокольчик»)',
                     'Халима Худойбердыева («Дорилбако»)'],
              'en': ["Zulfiya ('Spring Has Arrived Calling Thy Name' — Elegy for Hamid Olimjon)",
                     "Zulfiya ('Hulkar')",
                     "Zulfiya ('The Bell')",
                     "Halima Xudoyberdiyeva ('Dorilbaqo')"]},
  'correct_index': 0,
  'correct_answer': {'uz': "Zulfiya («Bahor keldi seni so'roqlab» — Hamid Olimjonga bag'ishlov)",
                     'ru': 'Зульфия (стихотворение «Весна пришла, тебя окликнув» — памяти Хамида Алимджана)',
                     'en': "Zulfiya ('Spring Has Arrived Calling Thy Name' — Elegy for Hamid Olimjon)"},
  'image_url': None,
  'fun_fact': {'uz': "O'zbekiston xalq shoirasi Zulfiyaning bevaqt halok bo'lgan sevikli umr yo'ldoshi Hamid Olimjonga "
                     "bag'ishlagan bu marsiyasi o'zbek sadoqat lirikasining tojidir.",
               'ru': 'Элегия Зульфии 1944 года, посвящённая безвременно погибшему мужу поэту Хамиду Алимджану, стала '
                     'гимном вечной любви и женской верности.',
               'en': "Zulfiya's famous 1944 elegy dedicated to her late husband Hamid Olimjon remains the "
                     'quintessential anthem of fidelity in Uzbek literature.'},
  'aliases': ['zulfiya', "bahor keldi seni so'roqlab", 'зульфия', 'весна пришла', 'hamid olimjon']},
 {'id': 'lit_q_098',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Biz baxtli bo'lamiz, xudo xohlasa,\n"
                     'Xudo xohlamasa, uchrasharmidik...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Мы непременно будем счастливы, если пожелает Аллах,\n'
                     'Разве мы встретились бы, не будь на то Его воли?..»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'We shall be happy, if God wills,\n"
                     "Would we have ever met, if God did not will?..'"},
  'options': {'uz': ["Muhammad Yusuf («Ulug'imsan, Vatanim»)",
                     "Muhammad Yusuf («Biz baxtli bo'lamiz» she'ri)",
                     'Muhammad Yusuf («Erka kiyik»)',
                     'Shavkat Rahmon («Yurak qonim»)'],
              'ru': ['Мухаммад Юсуф («Великая моя Родина»)',
                     'Мухаммад Юсуф (стихотворение «Мы будем счастливы»)',
                     'Мухаммад Юсуф («Баловница газель»)',
                     'Шавкат Рахмон («Кровь сердца»)'],
              'en': ["Muhammad Yusuf ('My Great Homeland')",
                     "Muhammad Yusuf ('We Shall Be Happy' Lyric)",
                     "Muhammad Yusuf ('Pampered Deer')",
                     "Shavkat Rahmon ('Heart's Blood')"]},
  'correct_index': 1,
  'correct_answer': {'uz': "Muhammad Yusuf («Biz baxtli bo'lamiz» she'ri)",
                     'ru': 'Мухаммад Юсуф (стихотворение «Мы будем счастливы»)',
                     'en': "Muhammad Yusuf ('We Shall Be Happy' Lyric)"},
  'image_url': None,
  'fun_fact': {'uz': "O'zbekiston xalq shoiri Muhammad Yusuf xalq qalbiga eng yaqin, samimiy va sodda tilda kuylagan "
                     'sevimli lirik shoir edi.',
               'ru': 'Мухаммад Юсуф — один из самых всенародно любимых узбекских поэтов рубежа XX–XXI веков, чьи стихи '
                     'стали десятками популярных песен.',
               'en': "People's Poet of Uzbekistan Muhammad Yusuf was celebrated for touching every reader's heart with "
                     'plain, tender, and musical lyricism.'},
  'aliases': ['muhammad yusuf', "biz baxtli bo'lamiz", 'мухаммад юсуф', 'yusuf']},
 {'id': 'lit_q_099',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     '«Turkiy tillar, sizda qonim qaynar,\n'
                     'Sizda jaranglaydi ajdodlarim sasi!\n'
                     'Qadim toshlarda bitilgan muqaddas kalom...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«Тюркские языки, в вас закипает моя кровь,\n'
                     'В вас разносится эхо голосов моих предков!\n'
                     'Священное слово, высеченное на древних камнях...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'Turkic tongues, my blood boils in your rhythm,\n"
                     'In you echoes the resounding voice of my ancestors!\n'
                     "The sacred word inscribed on ancient stone steles...'"},
  'options': {'uz': ['Rauf Parfi («Qora devor»)',
                     'Usmon Azim («Baxshiyona»)',
                     'Shavkat Rahmon («Turkiy til» / «Saylanma»)',
                     "Xurshid Davron («Qadimgi Farg'ona»)"],
              'ru': ['Рауф Парфи («Чёрная стена»)',
                     'Усман Азим («Бахши»)',
                     'Шавкат Рахмон (стихотворение «Тюркские языки»)',
                     'Хуршид Даврон («Древняя Фергана»)'],
              'en': ["Rauf Parfi ('Black Wall')",
                     "Usmon Azim ('Bakhshi Song')",
                     "Shavkat Rahmon ('Turkic Tongues' Lyric)",
                     "Khurshid Davron ('Ancient Fergana')"]},
  'correct_index': 2,
  'correct_answer': {'uz': 'Shavkat Rahmon («Turkiy til» / «Saylanma»)',
                     'ru': 'Шавкат Рахмон (стихотворение «Тюркские языки»)',
                     'en': "Shavkat Rahmon ('Turkic Tongues' Lyric)"},
  'image_url': None,
  'fun_fact': {'uz': "Shavkat Rahmon o'zbek she'riyatida milliy ruh, qat'iyat va erksevarlik g'oyalarini otashin "
                     'misralarda ifoda etgan buyuk shoirdir.',
               'ru': 'Шавкат Рахмон — выдающийся поэт бескомпромиссной гражданской лирики, возродивший дух '
                     'древнетюркской воинской чести.',
               'en': 'Shavkat Rahmon was a defining figure of modern Uzbek heroic poetry, passionately invoking '
                     'ancient Orkhon-Yenisey stone inscriptions.'},
  'aliases': ['shavkat rahmon', 'turkiy til', 'шавкат рахмон', 'тюркские языки']},
 {'id': 'lit_q_0100',
  'sub_mode': 'quotes',
  'question': {'uz': 'Quyidagi mashhur iqtibos qaysi asar yoki muallifga tegishli?\n'
                     '\n'
                     "«Ko'zlaringda ko'rdim dunyo dardini,\n"
                     'Sukut — eng muhtasham sasdir bu olamda...»',
               'ru': 'Кому или какому произведению принадлежит знаменитая цитата?\n'
                     '\n'
                     '«В глазах твоих я узрел печаль всего мира,\n'
                     'Безмолвие — самый величественный голос во вселенной...»',
               'en': 'Which work or author is the source of this famous quote?\n'
                     '\n'
                     "'In thine eyes I beheld the sorrow of the whole world,\n"
                     "Silence is the most majestic voice in this universe...'"},
  'options': {'uz': ['Shavkat Rahmon («Yurak»)',
                     'Asqad Muxtor («Poetik xotiralar»)',
                     'Jamol Kamol («Dovon»)',
                     'Rauf Parfi («Sukunat» / «Sabr daraxti»)'],
              'ru': ['Шавкат Рахмон («Сердце»)',
                     'Аскад Мухтар («Поэтические воспоминания»)',
                     'Джамал Камал («Перевал»)',
                     'Рауф Парфи (стихотворение «Безмолвие»)'],
              'en': ["Shavkat Rahmon ('Heart')",
                     "Asqad Mukhtar ('Poetic Memoirs')",
                     "Jamol Kamol ('The Pass')",
                     "Rauf Parfi ('Silence' / 'Tree of Patience')"]},
  'correct_index': 3,
  'correct_answer': {'uz': 'Rauf Parfi («Sukunat» / «Sabr daraxti»)',
                     'ru': 'Рауф Парфи (стихотворение «Безмолвие»)',
                     'en': "Rauf Parfi ('Silence' / 'Tree of Patience')"},
  'image_url': None,
  'fun_fact': {'uz': "O'zbekiston xalq shoiri Rauf Parfi o'zbek she'riyatida modernizm, erkin vazn va sonet janrining "
                     'eng buyuk ustozidir.',
               'ru': 'Рауф Парфи — реформатор узбекского поэтического языка, мастер сонета и глубокой '
                     'философско-экзистенциальной лирики.',
               'en': "People's Poet of Uzbekistan Rauf Parfi transformed contemporary poetry with avant-garde sonnets "
                     'and profound introspective symbolism.'},
  'aliases': ['rauf parfi', 'parfi', 'sukunat', 'рауф парфи', 'парфи']},
 {'id': 'lit_emoji_001',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⚔️🕊️🇷🇺👑',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⚔️🕊️🇷🇺👑',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⚔️🕊️🇷🇺👑'},
  'options': {'uz': ['«Urush va tinchlik» (Lev Tolstoy)',
                     '«Anna Karenina» (Lev Tolstoy)',
                     '«Tinch oqar Don» (Mixail Sholoxov)',
                     '«Poltava» (Aleksandr Pushkin)'],
              'ru': ['«Война и мир» (Лев Толстой)',
                     '«Анна Каренина» (Лев Толстой)',
                     '«Тихий Дон» (Михаил Шолохов)',
                     '«Полтава» (Александр Пушкин)'],
              'en': ["'War and Peace' (Leo Tolstoy)",
                     "'Anna Karenina' (Leo Tolstoy)",
                     "'And Quiet Flows the Don' (Mikhail Sholokhov)",
                     "'Poltava' (Alexander Pushkin)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Urush va tinchlik» (Lev Tolstoy)',
                     'ru': '«Война и мир» (Лев Толстой)',
                     'en': "'War and Peace' (Leo Tolstoy)"},
  'image_url': None,
  'fun_fact': {'uz': "Lev Tolstoy ushbu epopeyani 1863-1869 yillarda yozgan bo'lib, unda 550 dan ortiq personaj va "
                     '1812 yilgi Vatan urushi qatnashchilari tasvirlangan.',
               'ru': 'Грандиозная четырёхтомная эпопея Льва Толстого включает более 550 персонажей и детально '
                     'описывает наполеоновские войны в России.',
               'en': "Tolstoy's four-volume epic incorporates over 550 characters, chronicling the French invasion of "
                     'Russia in 1812.'},
  'aliases': ['urush va tinchlik', 'tolstoy', 'война и мир', 'толстой', 'war and peace']},
 {'id': 'lit_emoji_002',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👴🚣\u200d♂️🎣🦈🌊',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👴🚣\u200d♂️🎣🦈🌊',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👴🚣\u200d♂️🎣🦈🌊'},
  'options': {'uz': ['«Mobi Dik» (German Melvill)',
                     '«Chol va dengiz» (Ernest Xeminguey)',
                     "«Dengiz bo'risi» (Jek London)",
                     '«Suv ostida 20 000 lye» (Jyul Vern)'],
              'ru': ['«Моби Дик» (Герман Мелвилл)',
                     '«Старик и море» (Эрнест Хемингуэй)',
                     '«Морской волк» (Джек Лондон)',
                     '«Двадцать тысяч лье под водой» (Жюль Верн)'],
              'en': ["'Moby-Dick' (Herman Melville)",
                     "'The Old Man and the Sea' (Ernest Hemingway)",
                     "'The Sea-Wolf' (Jack London)",
                     "'Twenty Thousand Leagues Under the Sea' (Jules Verne)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Chol va dengiz» (Ernest Xeminguey)',
                     'ru': '«Старик и море» (Эрнест Хемингуэй)',
                     'en': "'The Old Man and the Sea' (Ernest Hemingway)"},
  'image_url': None,
  'fun_fact': {'uz': "Qariyb 3 oy baliqsiz qolgan qariya Santyagoning ulkan marlin balig'i va akulalar bilan 3 kunlik "
                     'mardona kurashi haqidagi asar.',
               'ru': 'Повесть рассказывает о 84 днях неудач старого кубинского рыбака Сантьяго и его героической битве '
                     'с гигантским марлином в Гольфстриме.',
               'en': 'Santiago struggles for days in the Gulf Stream against a giant marlin and marauding mako sharks, '
                     'proving unconquerable human willpower.'},
  'aliases': ['chol va dengiz', 'xeminguey', 'старик и море', 'хемингуэй', 'old man and the sea']},
 {'id': 'lit_emoji_003',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n💍👰\u200d♂️💔🦂📜',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n💍👰\u200d♂️💔🦂📜',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n💍👰\u200d♂️💔🦂📜'},
  'options': {'uz': ['«Mehrobdan chayon» (Abdulla Qodiriy)',
                     "«Kecha va kunduz» (Cho'lpon)",
                     "«O'tkan kunlar» (Abdulla Qodiriy)",
                     '«Sarvqomat dilbarim» (Chingiz Aytmatov)'],
              'ru': ['«Скорпион из алтаря» (Абдулла Кадыри)',
                     '«Ночь и день» (Чулпан)',
                     '«Минувшие дни» (Абдулла Кадыри)',
                     '«Тополёк мой в красной косынке» (Айтматов)'],
              'en': ["'Scorpion from the Altar' (Abdulla Qadiri)",
                     "'Night and Day' (Cholpon)",
                     "'Bygone Days' (Abdulla Qadiri)",
                     "'My Little Poplar in a Red Headscarf' (Aitmatov)"]},
  'correct_index': 2,
  'correct_answer': {'uz': "«O'tkan kunlar» (Abdulla Qodiriy)",
                     'ru': '«Минувшие дни» (Абдулла Кадыри)',
                     'en': "'Bygone Days' (Abdulla Qadiri)"},
  'image_url': None,
  'fun_fact': {'uz': 'Otabek va Kumushbibining sof muhabbati, rashkchi Zaynab va kundoshlik fojiasi orqali xonliklar '
                     'davri tushkunligi tasvirlangan.',
               'ru': 'Трагическая история любви Атабека и Кумуш, отравленной ядом соперницы Зайнаб, в первом узбекском '
                     'историческом романе.',
               'en': 'The pioneering Uzbek novel depicting the tragic love between Otabek and Kumushbibi amid the '
                     'oppressive social norms of Kokand Khanate.'},
  'aliases': ["o'tkan kunlar", 'otkan kunlar', 'abdulla qodiriy', 'минувшие дни', 'bygone days']},
 {'id': 'lit_emoji_004',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🌹🏰💔🧪☠️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🌹🏰💔🧪☠️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🌹🏰💔🧪☠️'},
  'options': {'uz': ['«Hamlet» (Uilyam Shekspir)',
                     '«Otello» (Uilyam Shekspir)',
                     '«Faust» (Iogann Gyote)',
                     '«Romeo va Juletta» (Uilyam Shekspir)'],
              'ru': ['«Гамлет» (Уильям Шекспир)',
                     '«Отелло» (Уильям Шекспир)',
                     '«Фауст» (Иоганн Гёте)',
                     '«Ромео и Джульетта» (Уильям Шекспир)'],
              'en': ["'Hamlet' (William Shakespeare)",
                     "'Othello' (William Shakespeare)",
                     "'Faust' (Johann Wolfgang von Goethe)",
                     "'Romeo and Juliet' (William Shakespeare)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Romeo va Juletta» (Uilyam Shekspir)',
                     'ru': '«Ромео и Джульетта» (Уильям Шекспир)',
                     'en': "'Romeo and Juliet' (William Shakespeare)"},
  'image_url': None,
  'fun_fact': {'uz': "Veronadagi Montekki va Kapuletti urug'lari dushmanligi qurboni bo'lgan ikki yosh oshiqning "
                     'afsonaviy fojiasi.',
               'ru': 'Бессмертная трагедия Шекспира о двух юных веронских влюблённых из враждующих семейств Монтекки и '
                     'Капулетти.',
               'en': "Shakespeare's celebrated tragedy set in Verona concerning star-crossed lovers from feuding "
                     'Montague and Capulet houses.'},
  'aliases': ['romeo va juletta', 'romeo', 'juletta', 'ромео и джульетта', 'шекспир', 'romeo and juliet']},
 {'id': 'lit_emoji_005',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🛡️🐎💨🌬️🪓',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🛡️🐎💨🌬️🪓',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🛡️🐎💨🌬️🪓'},
  'options': {'uz': ['«Don Kixot» (Migel de Servantes)',
                     '«Ayvengo» (Valter Skott)',
                     '«Uch mushketyor» (Aleksandr Dyuma)',
                     '«Sid» (Pyer Kornel)'],
              'ru': ['«Дон Кихот» (Мигель де Сервантес)',
                     '«Айвенго» (Вальтер Скотт)',
                     '«Три мушкетёра» (Александр Дюма)',
                     '«Сид» (Пьер Корнель)'],
              'en': ["'Don Quixote' (Miguel de Cervantes)",
                     "'Ivanhoe' (Walter Scott)",
                     "'The Three Musketeers' (Alexandre Dumas)",
                     "'Le Cid' (Pierre Corneille)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Don Kixot» (Migel de Servantes)',
                     'ru': '«Дон Кихот» (Мигель де Сервантес)',
                     'en': "'Don Quixote' (Miguel de Cervantes)"},
  'image_url': None,
  'fun_fact': {'uz': "Ritsarlik romanlarini o'qiyverib aqlidan ozgan va shamol tegirmonlarini maxluq deb o'ylab jangga "
                     'kirgan ritsar va uning eshak mingan xizmatkori Sancho Pansa.',
               'ru': 'Идальго Дон Кихот на кляче Росинанте принимает ветряные мельницы за великанов и сражается за '
                     'прекрасную Дульсинею Тобосскую.',
               'en': 'The noble dreamer tilted at windmills astride his steed Rocinante alongside faithful squire '
                     'Sancho Panza.'},
  'aliases': ['don kixot', 'servantes', 'дон кихот', 'сервантес', 'don quixote']},
 {'id': 'lit_emoji_006',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐷🚜🐴🐑🚩',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐷🚜🐴🐑🚩',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐷🚜🐴🐑🚩'},
  'options': {'uz': ['«1984» (Jorj Oruell)',
                     "«Molxona» / «Hayvonlar xo'jaligi» (Jorj Oruell)",
                     "«Shum bola» (G'afur G'ulom)",
                     '«Chayka» (Anton Chexov)'],
              'ru': ['«1984» (Джордж Оруэлл)',
                     '«Скотный двор» (Джордж Оруэлл)',
                     '«Озорник» (Гафур Гулям)',
                     '«Чайка» (Антон Чехов)'],
              'en': ["'1984' (George Orwell)",
                     "'Animal Farm' (George Orwell)",
                     "'The Mischievous Boy' (Ghafur Ghulam)",
                     "'The Seagull' (Anton Chekhov)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Molxona» / «Hayvonlar xo'jaligi» (Jorj Oruell)",
                     'ru': '«Скотный двор» (Джордж Оруэлл)',
                     'en': "'Animal Farm' (George Orwell)"},
  'image_url': None,
  'fun_fact': {'uz': "Fermadagi hayvonlar o'z xo'jayinini haydab chiqarib, 'barcha hayvonlar teng' degan davlat "
                     "tuzishadi, ammo cho'chqalar tez orada diktatorga aylanishadi.",
               'ru': 'Аллегорическая антиутопическая притча о том, как идеалы революции перерождаются в жестокую '
                     'тиранию свиней под предводительством Наполеона.',
               'en': 'Barnyard animals overthrow their human farmer only to see totalitarian pigs under Napoleon '
                     'establish an even harsher tyranny.'},
  'aliases': ['molxona', "hayvonlar xo'jaligi", 'скотный двор', 'oruell', 'animal farm']},
 {'id': 'lit_emoji_007',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐈\u200d⬛🧙\u200d♂️🧹🌕🔥',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '🐈\u200d⬛🧙\u200d♂️🧹🌕🔥',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n'
                     '\n'
                     '🐈\u200d⬛🧙\u200d♂️🧹🌕🔥'},
  'options': {'uz': ['«It yuragi» (Mixail Bulgakov)',
                     '«Oq gvardiya» (Mixail Bulgakov)',
                     '«Usta va Margarita» (Mixail Bulgakov)',
                     '«Qiyomat» (Abdurauf Fitrat)'],
              'ru': ['«Собачье сердце» (Михаил Булгаков)',
                     '«Белая гвардия» (Михаил Булгаков)',
                     '«Мастер и Маргарита» (Михаил Булгаков)',
                     '«Судный день» (Абдурауф Фитрат)'],
              'en': ["'Heart of a Dog' (Mikhail Bulgakov)",
                     "'The White Guard' (Mikhail Bulgakov)",
                     "'The Master and Margarita' (Mikhail Bulgakov)",
                     "'Judgment Day' (Abdurauf Fitrat)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Usta va Margarita» (Mixail Bulgakov)',
                     'ru': '«Мастер и Маргарита» (Михаил Булгаков)',
                     'en': "'The Master and Margarita' (Mikhail Bulgakov)"},
  'image_url': None,
  'fun_fact': {'uz': "Shayton (Voland) va uning dumi qora mushugi Begemot 1930-yillar Moskvada paydo bo'lib kutilmagan "
                     "mo''jizalar ko'rsatishadi.",
               'ru': 'Роман переплетает сатиру на Москву 1930-х с визитом Воланда и кота Бегемота и библейскую историю '
                     'Понтия Пилата и Иешуа Га-Ноцри.',
               'en': 'The devil Woland arrives in Soviet Moscow accompanied by a vodka-drinking giant black cat named '
                     'Behemoth.'},
  'aliases': ['usta va margarita', 'bulgakov', 'мастер и маргарита', 'булгаков', 'master and margarita']},
 {'id': 'lit_emoji_008',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🤴🌹🦊✈️🪐',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🤴🌹🦊✈️🪐',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🤴🌹🦊✈️🪐'},
  'options': {'uz': ['«Jonatan Livingston ismli oqcharloq» (Richard Bax)',
                     "«Alisa mo''jizalar mamlakatida» (Lyuis Kerroll)",
                     '«Mittivoy va Karlson» (Astrid Lindgren)',
                     '«Kichkina shahzoda» (Antuan de Sent-Ekzyuperi)'],
              'ru': ['«Чайка Джонатан Ливингстон» (Ричард Бах)',
                     '«Алиса в Стране чудес» (Льюис Кэрролл)',
                     '«Малыш и Карлсон» (Астрид Линдгрен)',
                     '«Маленький принц» (Антуан де Сент-Экзюпери)'],
              'en': ["'Jonathan Livingston Seagull' (Richard Bach)",
                     "'Alice in Wonderland' (Lewis Carroll)",
                     "'Karlsson-on-the-Roof' (Astrid Lindgren)",
                     "'The Little Prince' (Antoine de Saint-Exupéry)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Kichkina shahzoda» (Antuan de Sent-Ekzyuperi)',
                     'ru': '«Маленький принц» (Антуан де Сент-Экзюпери)',
                     'en': "'The Little Prince' (Antoine de Saint-Exupéry)"},
  'image_url': None,
  'fun_fact': {'uz': 'B-612 asteroididan kelgan oltin sochli shahzoda sahroda samolyoti buzilgan uchuvchi bilan '
                     "uchrashadi va do'stlik sirlarini o'rganadi.",
               'ru': 'Трогательная сказка об обитателе крошечного астероида B-612, любимой розе, встрече с Лисом и '
                     'пилотом в Сахаре.',
               'en': 'A poetical tale of a young prince visiting planets from asteroid B-612, befriending a stranded '
                     'pilot and a wise desert fox.'},
  'aliases': ['kichkina shahzoda', 'ekzyuperi', 'маленький принц', 'the little prince']},
 {'id': 'lit_emoji_009',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐋⚓🪵👴🎯',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐋⚓🪵👴🎯',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐋⚓🪵👴🎯'},
  'options': {'uz': ['«Mobi Dik, yoki Oq kit» (German Melvill)',
                     '«Chol va dengiz» (Ernest Xeminguey)',
                     "«Dengiz bo'risi» (Jek London)",
                     '«Robinzon Kruzo» (Daniel Defo)'],
              'ru': ['«Моби Дик, или Белый кит» (Герман Мелвилл)',
                     '«Старик и море» (Эрнест Хемингуэй)',
                     '«Морской волк» (Джек Лондон)',
                     '«Робинзон Крузо» (Даниэль Дефо)'],
              'en': ["'Moby-Dick; or, The Whale' (Herman Melville)",
                     "'The Old Man and the Sea' (Ernest Hemingway)",
                     "'The Sea-Wolf' (Jack London)",
                     "'Robinson Crusoe' (Daniel Defoe)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Mobi Dik, yoki Oq kit» (German Melvill)',
                     'ru': '«Моби Дик, или Белый кит» (Герман Мелвилл)',
                     'en': "'Moby-Dick; or, The Whale' (Herman Melville)"},
  'image_url': None,
  'fun_fact': {'uz': "Bir oyog'idan ayrilgan kapitan Axav 'Pekod' kit ovlash kemasida afsonaviy oq kashalot Mobi "
                     'Dikdan qasos olishga intiladi.',
               'ru': 'Одноногий капитан Ахав на китобойном судне «Пекод» одержим жаждой мести свирепому белому '
                     'кашалоту Моби Дику.',
               'en': "Captain Ahab obsessively steers the whaleship Pequod across the world's oceans in pursuit of the "
                     'monstrous white sperm whale.'},
  'aliases': ['mobi dik', 'melvill', 'моби дик', 'moby dick', 'white whale']},
 {'id': 'lit_emoji_010',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧛\u200d♂️🦇🩸⚰️🏰',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🧛\u200d♂️🦇🩸⚰️🏰',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧛\u200d♂️🦇🩸⚰️🏰'},
  'options': {'uz': ['«Frankenshteyn» (Meri Shelli)',
                     '«Drakula» (Brem Stoker)',
                     '«Doktor Jekil va mister Xayd» (Stivenson)',
                     '«Karmilla» (Sheridan Le Fanyu)'],
              'ru': ['«Франкенштейн» (Мэри Шелли)',
                     '«Дракула» (Брэм Стокер)',
                     '«Доктор Джекил и мистер Хайд» (Стивенсон)',
                     '«Кармилла» (Шеридан Ле Фаню)'],
              'en': ["'Frankenstein' (Mary Shelley)",
                     "'Dracula' (Bram Stoker)",
                     "'Dr Jekyll and Mr Hyde' (Stevenson)",
                     "'Carmilla' (Sheridan Le Fanu)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Drakula» (Brem Stoker)', 'ru': '«Дракула» (Брэм Стокер)', 'en': "'Dracula' (Bram Stoker)"},
  'image_url': None,
  'fun_fact': {'uz': "1897 yilda yozilgan epistolyar roman bo'lib, Transilvaniyadan Angliyaga ko'chib o'tmoqchi "
                     "bo'lgan qadimgi vampir graf haqida hikoya qiladi.",
               'ru': 'Эпистолярный готический роман 1897 года о графе-вампире из Трансильвании и противостоящем ему '
                     'профессоре Абрахаме Ван Хельсинге.',
               'en': "Bram Stoker's foundational vampire novel told through diary entries, letters, and newspaper "
                     'clippings.'},
  'aliases': ['drakula', 'stoker', 'дракула', 'dracula', 'vampire']},
 {'id': 'lit_emoji_011',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🍸🎷🚘🟢💸',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🍸🎷🚘🟢💸',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🍸🎷🚘🟢💸'},
  'options': {'uz': ["«Boy ota, kambag'al ota» (Robert Kiosaki)",
                     '«Quyosh baribir chiqaveradi» (Xeminguey)',
                     '«Buyuk Getsbi» (F. Skott Fitsjerald)',
                     "«G'azab mevalari» (Jon Steynbek)"],
              'ru': ['«Богатый папа, бедный папа» (Кийосаки)',
                     '«Фиеста» (Эрнест Хемингуэй)',
                     '«Великий Гэтсби» (Ф. Скотт Фицджеральд)',
                     '«Гроздья гнева» (Джон Стейнбек)'],
              'en': ["'Rich Dad Poor Dad' (Robert Kiyosaki)",
                     "'The Sun Also Rises' (Ernest Hemingway)",
                     "'The Great Gatsby' (F. Scott Fitzgerald)",
                     "'The Grapes of Wrath' (John Steinbeck)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Buyuk Getsbi» (F. Skott Fitsjerald)',
                     'ru': '«Великий Гэтсби» (Ф. Скотт Фицджеральд)',
                     'en': "'The Great Gatsby' (F. Scott Fitzgerald)"},
  'image_url': None,
  'fun_fact': {'uz': "Jaz davri Nyu-Yorkida o'z sevgilisi Deyzi Byukenen e'tiborini qozonish uchun dabdabali bazmlar "
                     'beruvchi sirli boy Jey Getsbi taqdiri.',
               'ru': 'Эпоха джаза 1920-х годов: таинственный миллионер Джей Гэтсби устраивает роскошные вечеринки в '
                     'надежде вернуть любовь Дэйзи Бьюкенен.',
               'en': 'Set in Jazz Age Long Island, mysterious tycoon Jay Gatsby gazes yearningly across the bay at the '
                     "green light on Daisy Buchanan's dock."},
  'aliases': ['buyuk getsbi', 'getsbi', 'великий гэтсби', 'гэтсби', 'great gatsby', 'fitzgerald']},
 {'id': 'lit_emoji_012',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🪓👵🪙👮\u200d♂️🇷🇺',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🪓👵🪙👮\u200d♂️🇷🇺',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🪓👵🪙👮\u200d♂️🇷🇺'},
  'options': {'uz': ['«Aka-uka Karamazovlar» (Dostoevskiy)',
                     '«Idiot» (Dostoevskiy)',
                     '«Qiyomat qoyim» (Lev Tolstoy)',
                     '«Jinoyat va jazo» (Fyodor Dostoevskiy)'],
              'ru': ['«Братья Карамазовы» (Достоевский)',
                     '«Идиот» (Достоевский)',
                     '«Воскресение» (Лев Толстой)',
                     '«Преступление и наказание» (Фёдор Достоевский)'],
              'en': ["'The Brothers Karamazov' (Dostoevsky)",
                     "'The Idiot' (Dostoevsky)",
                     "'Resurrection' (Leo Tolstoy)",
                     "'Crime and Punishment' (Fyodor Dostoevsky)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Jinoyat va jazo» (Fyodor Dostoevskiy)',
                     'ru': '«Преступление и наказание» (Фёдор Достоевский)',
                     'en': "'Crime and Punishment' (Fyodor Dostoevsky)"},
  'image_url': None,
  'fun_fact': {'uz': "Talaba Rodion Raskolnikov Peterburgda kampir sudxo'r Alena Ivanovnani bolta bilan qatl etib, "
                     "so'ng qattiq ruhiy azob chekadi.",
               'ru': 'Петербургский студент Родион Раскольников совершает убийство процентщицы топором, переживая '
                     'мучительное нравственное возмездие.',
               'en': 'Penniless student Rodion Raskolnikov murders a pawnbroker with an axe in Saint Petersburg, '
                     'followed by agonizing guilt and spiritual redemption.'},
  'aliases': ['jinoyat va jazo',
              'dostoevskiy',
              'преступление и наказание',
              'достоевский',
              'raskolnikov',
              'crime and punishment']},
 {'id': 'lit_emoji_013',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏝️🥥👣🦜🛶',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏝️🥥👣🦜🛶',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏝️🥥👣🦜🛶'},
  'options': {'uz': ['«Robinzon Kruzo» (Daniel Defo)',
                     '«Sirli orol» (Jyul Vern)',
                     '«Xazinalar oroli» (Stivenson)',
                     '«Kapitan Grant bolalari» (Jyul Vern)'],
              'ru': ['«Робинзон Крузо» (Даниэль Дефо)',
                     '«Таинственный остров» (Жюль Верн)',
                     '«Остров сокровищ» (Стивенсон)',
                     '«Дети капитана Гранта» (Жюль Верн)'],
              'en': ["'Robinson Crusoe' (Daniel Defoe)",
                     "'The Mysterious Island' (Jules Verne)",
                     "'Treasure Island' (Stevenson)",
                     "'In Search of the Castaways' (Jules Verne)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Robinzon Kruzo» (Daniel Defo)',
                     'ru': '«Робинзон Крузо» (Даниэль Дефо)',
                     'en': "'Robinson Crusoe' (Daniel Defoe)"},
  'image_url': None,
  'fun_fact': {'uz': "Kema halokatidan so'ng kimsasiz orolga tushib qolib, 28 yil davomida u yerda hayot kechirgan va "
                     "Juma ismli do'st orttirgan qahramon.",
               'ru': 'Робинзон выживает на необитаемом острове 28 лет, приручает коз, учится печь хлеб и спасает '
                     'дикаря Пятницу.',
               'en': 'Marooned on a tropical desert island for 28 years, Crusoe builds a homestead, bakes pottery, and '
                     'rescues Friday.'},
  'aliases': ['robinzon kruzo', 'robinzon', 'робинзон крузо', 'дефо', 'robinson crusoe']},
 {'id': 'lit_emoji_014',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🔍🕵️\u200d♂️🐕🔥🌫️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '🔍🕵️\u200d♂️🐕🔥🌫️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🔍🕵️\u200d♂️🐕🔥🌫️'},
  'options': {'uz': ["«To'rtlar belgisi» (Konan Doyl)",
                     '«Baskervillar iti» (Artur Konan Doyl)',
                     '«Qirmizi etyud» (Konan Doyl)',
                     '«Sharqiy ekspressdagi qotillik» (Kristi)'],
              'ru': ['«Знак четырёх» (Конан Дойл)',
                     '«Собака Баскервилей» (Артур Конан Дойл)',
                     '«Этюд в багровых тонах» (Конан Дойл)',
                     '«Убийство в Восточном экспрессе» (Кристи)'],
              'en': ["'The Sign of the Four' (Conan Doyle)",
                     "'The Hound of the Baskervilles' (Arthur Conan Doyle)",
                     "'A Study in Scarlet' (Conan Doyle)",
                     "'Murder on the Orient Express' (Agatha Christie)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Baskervillar iti» (Artur Konan Doyl)',
                     'ru': '«Собака Баскервилей» (Артур Конан Дойл)',
                     'en': "'The Hound of the Baskervilles' (Arthur Conan Doyle)"},
  'image_url': None,
  'fun_fact': {'uz': "Devonshir botqoqliklarida og'zidan fosforli olov purkaydigan afsonaviy bahaybat qora it haqidagi "
                     'dahshatli jumboqni Sherlok Xolms va doktor Vatson yechadi.',
               'ru': 'Знаменитая повесть 1902 года о призрачной светящейся собаке, преследующей древний род сэра Генри '
                     'Баскервиля на Гримпенской трясине.',
               'en': 'Sherlock Holmes and Dr. Watson investigate a spectral, phosphorus-glowing hellhound haunting the '
                     'Dartmoor mires.'},
  'aliases': ['baskervillar iti', 'sherlok xolms', 'собака баскервилей', 'шерлок холмс', 'hound of the baskervilles']},
 {'id': 'lit_emoji_015',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👧🐇🕳️🍵👑',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👧🐇🕳️🍵👑',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👧🐇🕳️🍵👑'},
  'options': {'uz': ['«Piter Pen» (Jeyms Barri)',
                     '«Oz mamlakati sehrgari» (Frenk Baum)',
                     "«Alisa mo''jizalar mamlakatida» (Lyuis Kerroll)",
                     "«Sariq devni minib» (To'xtaboyev)"],
              'ru': ['«Питер Пэн» (Джеймс Барри)',
                     '«Волшебник страны Оз» (Фрэнк Баум)',
                     '«Алиса в Стране чудес» (Льюис Кэрролл)',
                     '«Верхом на жёлтом диве» (Тухтабаев)'],
              'en': ["'Peter Pan' (J.M. Barrie)",
                     "'The Wizard of Oz' (L. Frank Baum)",
                     "'Alice's Adventures in Wonderland' (Lewis Carroll)",
                     "'Riding the Yellow Giant' (Tukhtabayev)"]},
  'correct_index': 2,
  'correct_answer': {'uz': "«Alisa mo''jizalar mamlakatida» (Lyuis Kerroll)",
                     'ru': '«Алиса в Стране чудес» (Льюис Кэрролл)',
                     'en': "'Alice's Adventures in Wonderland' (Lewis Carroll)"},
  'image_url': None,
  'fun_fact': {'uz': "Quyon iniga qulab g'aroyib dunyoga tushib qolgan qizcha, Qalpog'i telba bilan choyxo'rlik va "
                     'Yuraklar Qirolichasi sudi.',
               'ru': 'Алиса бежит за Белым Кроликом, падает в кроличью нору, попадает на Безумное чаепитие и встречает '
                     'Червонную Королеву.',
               'en': 'Alice falls down a rabbit hole into a fantasy realm populated by the Mad Hatter, the March Hare, '
                     'and the Queen of Hearts.'},
  'aliases': ['alisa', "alisa mo'jizalar mamlakatida", 'алиса в стране чудес', 'alice in wonderland', 'lewis carroll']},
 {'id': 'lit_emoji_016',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n💍🧙\u200d♂️🌋🧝\u200d♂️👁️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '💍🧙\u200d♂️🌋🧝\u200d♂️👁️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n'
                     '\n'
                     '💍🧙\u200d♂️🌋🧝\u200d♂️👁️'},
  'options': {'uz': ['«Xobbit» (J.R.R. Tolkin)',
                     '«Narniya yilnomalari» (K.S. Lyuis)',
                     '«Garri Potter» (J.K. Rouling)',
                     '«Uzuklar hukmdori» (J.R.R. Tolkin)'],
              'ru': ['«Хоббит» (Толкин)',
                     '«Хроники Нарнии» (К. С. Льюис)',
                     '«Гарри Поттер» (Дж. К. Роулинг)',
                     '«Властелин колец» (Дж. Р. Р. Толкин)'],
              'en': ["'The Hobbit' (Tolkien)",
                     "'The Chronicles of Narnia' (C.S. Lewis)",
                     "'Harry Potter' (J.K. Rowling)",
                     "'The Lord of the Rings' (J.R.R. Tolkien)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Uzuklar hukmdori» (J.R.R. Tolkin)',
                     'ru': '«Властелин колец» (Дж. Р. Р. Толкин)',
                     'en': "'The Lord of the Rings' (J.R.R. Tolkien)"},
  'image_url': None,
  'fun_fact': {'uz': "Frodo Beggins va uning birodarlari Qudrat uzugini Mordorning Orodruin vulqoniga tashlab yo'q "
                     "qilish uchun O'rta Yer bo'ylab xavfli safarga chiqishadi.",
               'ru': 'Хоббит Фродо Бэггинс несёт Кольцо Всевластья к жерлу вулкана Ородруин в Мордоре, чтобы сокрушить '
                     'Тёмного Властелина Саурона.',
               'en': 'Frodo Baggins journeys across Middle-earth to destroy the One Ring in the fires of Mount Doom '
                     'and defeat the Dark Lord Sauron.'},
  'aliases': ['uzuklar hukmdori', 'tolkin', 'властелин колец', 'толкин', 'lord of the rings', 'tolkien']},
 {'id': 'lit_emoji_017',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⚡🧟\u200d♂️🧪🔬🔥',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⚡🧟\u200d♂️🧪🔬🔥',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⚡🧟\u200d♂️🧪🔬🔥'},
  'options': {'uz': ['«Frankenshteyn, yoki Zamonaviy Prometey» (Meri Shelli)',
                     '«Drakula» (Brem Stoker)',
                     '«Doktor Jekil va mister Xayd» (Stivenson)',
                     "«Ko'rinmas odam» (Gerbert Uells)"],
              'ru': ['«Франкенштейн, или Современный Прометей» (Мэри Шелли)',
                     '«Дракула» (Брэм Стокер)',
                     '«Доктор Джекил и мистер Хайд» (Стивенсон)',
                     '«Человек-невидимка» (Герберт Уэллс)'],
              'en': ["'Frankenstein; or, The Modern Prometheus' (Mary Shelley)",
                     "'Dracula' (Bram Stoker)",
                     "'Dr Jekyll and Mr Hyde' (Stevenson)",
                     "'The Invisible Man' (H.G. Wells)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Frankenshteyn, yoki Zamonaviy Prometey» (Meri Shelli)',
                     'ru': '«Франкенштейн, или Современный Прометей» (Мэри Шелли)',
                     'en': "'Frankenstein; or, The Modern Prometheus' (Mary Shelley)"},
  'image_url': None,
  'fun_fact': {'uz': "Olim Viktor Frankenshteyn murdalar a'zolaridan sun'iy odam yaratadi, ammo uning dahshatli "
                     "ko'rinishidan qo'rqib tashlab ketgach, maxluq qasos ola boshlaydi.",
               'ru': 'Молодой учёный оживляет существо из неживой материи с помощью электричества, но порождает '
                     'трагедию отверженности и мести.',
               'en': 'Victor Frankenstein sparks life into a creature stitched from cadavers, unleashing tragedy when '
                     'he abandons his monstrous creation.'},
  'aliases': ['frankenshteyn', 'шелли', 'франкенштейн', 'frankenstein', 'mary shelley']},
 {'id': 'lit_emoji_018',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🚒🔥📚🚫📖',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🚒🔥📚🚫📖',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🚒🔥📚🚫📖'},
  'options': {'uz': ['«1984» (Jorj Oruell)',
                     "«Farengeyt bo'yicha 451 daraja» (Rey Bredberi)",
                     '«Ajib yangi dunyo» (Oldos Xaksli)',
                     '«Biz» (Yevgeniy Zamyatin)'],
              'ru': ['«1984» (Джордж Оруэлл)',
                     '«451 градус по Фаренгейту» (Рэй Брэдбери)',
                     '«О дивный новый мир» (Олдос Хаксли)',
                     '«Мы» (Евгений Замятин)'],
              'en': ["'1984' (George Orwell)",
                     "'Fahrenheit 451' (Ray Bradbury)",
                     "'Brave New World' (Aldous Huxley)",
                     "'We' (Yevgeny Zamyatin)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Farengeyt bo'yicha 451 daraja» (Rey Bredberi)",
                     'ru': '«451 градус по Фаренгейту» (Рэй Брэдбери)',
                     'en': "'Fahrenheit 451' (Ray Bradbury)"},
  'image_url': None,
  'fun_fact': {'uz': "451 daraja farengeyt — qog'ozning o'z-o'zidan yonish haroratidir; Gay Monteg o't o'chiruvchi "
                     "bo'lib kitoblarni yoqish bilan shug'ullanardi.",
               'ru': '451°F — температура воспламенения бумаги; пожарный Гай Монтэг сжигает запрещённые книги, пока не '
                     'начинает читать их тайно.',
               'en': 'Guy Montag is a fireman tasked with incinerating outlawed books, until an encounter with '
                     'Clarisse awakens his curiosity.'},
  'aliases': ['451', 'bredberi', '451 градус по фаренгейту', 'брэдбери', 'fahrenheit 451']},
 {'id': 'lit_emoji_019',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🛏️🪳🚪🍎😔',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🛏️🪳🚪🍎😔',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🛏️🪳🚪🍎😔'},
  'options': {'uz': ['«Sud jarayoni» (Frans Kafka)',
                     '«Qasr» (Frans Kafka)',
                     '«Evrilish» (Frans Kafka)',
                     '«Begona» (Alber Kamyu)'],
              'ru': ['«Процесс» (Франц Кафка)',
                     '«Замок» (Франц Кафка)',
                     '«Превращение» (Франц Кафка)',
                     '«Посторонний» (Альбер Камю)'],
              'en': ["'The Trial' (Franz Kafka)",
                     "'The Castle' (Franz Kafka)",
                     "'The Metamorphosis' (Franz Kafka)",
                     "'The Stranger' (Albert Camus)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Evrilish» (Frans Kafka)',
                     'ru': '«Превращение» (Франц Кафка)',
                     'en': "'The Metamorphosis' (Franz Kafka)"},
  'image_url': None,
  'fun_fact': {'uz': "Sayohat qiluvchi savdogar Gregor Zamza bir tongda ulkan qo'ng'iz-hasharotga aylanib uyg'onadi va "
                     'oilasi uni xonaga qamab, otasi unga olma otadi.',
               'ru': 'Грегор Замза просыпается насекомым; отец швыряет в него яблоко, которое застревает в панцире, '
                     'вызывая смертельное воспаление.',
               'en': 'Traveling salesman Gregor Samsa transforms into a gigantic vermin; his family gradually rejects '
                     'him, his father lodging an apple in his back.'},
  'aliases': ['evrilish', 'kafka', 'превращение', 'кафка', 'metamorphosis']},
 {'id': 'lit_emoji_020',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👦🏃\u200d♂️🍉🎪💰',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👦🏃\u200d♂️🍉🎪💰',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👦🏃\u200d♂️🍉🎪💰'},
  'options': {'uz': ["«Sariq devni minib» (Xudoyberdi To'xtaboyev)",
                     "«Yodgor» (G'afur G'ulom)",
                     "«O'g'ri» (Abdulla Qahhor)",
                     "«Shum bola» (G'afur G'ulom)"],
              'ru': ['«Верхом на жёлтом диве» (Тухтабаев)',
                     '«Ядгар» (Гафур Гулям)',
                     '«Вор» (Абдулла Каххар)',
                     '«Озорник» (Гафур Гулям)'],
              'en': ["'Riding the Yellow Giant' (Tukhtabayev)",
                     "'Yadgar' (Ghafur Ghulam)",
                     "'The Thief' (Abdulla Qahhor)",
                     "'The Mischievous Boy' (Ghafur Ghulam)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Shum bola» (G'afur G'ulom)",
                     'ru': '«Озорник» (Гафур Гулям)',
                     'en': "'The Mischievous Boy' (Ghafur Ghulam)"},
  'image_url': None,
  'fun_fact': {'uz': "Uyidan qochib ketgan sho'x Qoravoyning qalandarlar to'dasi, boylar xonadoni va bozorlarda "
                     'boshdan kechirgan kulgili sarguzashtlari.',
               'ru': 'Приключения ташкентского мальчишки Каравая, убежавшего из дома и сменившего десяток профессий от '
                     'дервиша до батрака.',
               'en': 'The runaway boy Qoravoy uses his wits to survive among charlatans, wandering dervishes, and '
                     'wealthy merchants in old Tashkent.'},
  'aliases': ['shum bola', "g'afur g'ulom", 'озорник', 'гулям', 'mischievous boy']},
 {'id': 'lit_emoji_021',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🌴👵🧬⏳🦋',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🌴👵🧬⏳🦋',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🌴👵🧬⏳🦋'},
  'options': {'uz': ["«Yolg'izlikning yuz yili» (Gabriel Garsia Markes)",
                     '«Vabo davridagi muhabbat» (Markes)',
                     '«Patriarx kuzi» (Markes)',
                     '«Pedro Paramo» (Xuan Rulfo)'],
              'ru': ['«Сто лет одиночества» (Габриэль Гарсиа Маркес)',
                     '«Любовь во время холеры» (Маркес)',
                     '«Осень патриарха» (Маркес)',
                     '«Педро Парамо» (Хуан Рульфо)'],
              'en': ["'One Hundred Years of Solitude' (Gabriel García Márquez)",
                     "'Love in the Time of Cholera' (Marquez)",
                     "'The Autumn of the Patriarch' (Marquez)",
                     "'Pedro Páramo' (Juan Rulfo)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«Yolg'izlikning yuz yili» (Gabriel Garsia Markes)",
                     'ru': '«Сто лет одиночества» (Габриэль Гарсиа Маркес)',
                     'en': "'One Hundred Years of Solitude' (Gabriel García Márquez)"},
  'image_url': None,
  'fun_fact': {'uz': "Xose Arkadio Buendia tomonidan asos solingan Makondo qishlog'i, sariq kapalaklar, yuz yillik "
                     "yomg'irlar va yolg'izlik girdobidagi avlod taqdiri.",
               'ru': 'История городка Макондо и семи поколений семьи Буэндиа, закончившаяся тем, что город стёр с лица '
                     'земли библейский ураган.',
               'en': 'The cyclical, enchanted rise and fall of the mythical town of Macondo and the Buendía lineage '
                     'plagued by solitude and yellow butterflies.'},
  'aliases': ["yolg'izlikning yuz yili", 'markes', 'сто лет одиночества', 'маркес', 'one hundred years of solitude']},
 {'id': 'lit_emoji_022',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⚔️👒🏇🇫🇷💎',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⚔️👒🏇🇫🇷💎',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⚔️👒🏇🇫🇷💎'},
  'options': {'uz': ['«Graf Monte-Kristo» (Dyuma)',
                     '«Uch mushketyor» (Aleksandr Dyuma)',
                     '«Ayvengo» (Valter Skott)',
                     '«Temir niqob» (Dyuma)'],
              'ru': ['«Граф Монте-Кристо» (Дюма)',
                     '«Три мушкетёра» (Александр Дюма)',
                     '«Айвенго» (Вальтер Скотт)',
                     '«Железная маска» (Дюма)'],
              'en': ["'The Count of Monte Cristo' (Dumas)",
                     "'The Three Musketeers' (Alexandre Dumas)",
                     "'Ivanhoe' (Walter Scott)",
                     "'The Man in the Iron Mask' (Dumas)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Uch mushketyor» (Aleksandr Dyuma)',
                     'ru': '«Три мушкетёра» (Александр Дюма)',
                     'en': "'The Three Musketeers' (Alexandre Dumas)"},
  'image_url': None,
  'fun_fact': {'uz': "Gaskoniyalik yosh yigit D'Artanyan Parijga kelib uch qirol mushketyori bilan do'stlashadi va "
                     'qirolicha olmoslarini qutqarishga otlanadi.',
               'ru': "Д'Артаньян и его неразлучные друзья Атос, Портос и Арамис спасают честь королевы Анны "
                     'Австрийской, возвращая её алмазные подвески.',
               'en': "D'Artagnan and comrades Athos, Porthos, and Aramis cross the English Channel to recover Queen "
                     "Anne's diamond studs from Buckingham."},
  'aliases': ['uch mushketyor', 'dyuma', 'три мушкетера', 'дюма', 'three musketeers']},
 {'id': 'lit_emoji_023',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏰⛓️🌊🪙🎭',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏰⛓️🌊🪙🎭',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏰⛓️🌊🪙🎭'},
  'options': {'uz': ['«Uch mushketyor» (Dyuma)',
                     "«Xo'rlanganlar» (Gyugo)",
                     '«Graf Monte-Kristo» (Aleksandr Dyuma)',
                     '«Parij sirlari» (Ejen Syu)'],
              'ru': ['«Три мушкетёра» (Дюма)',
                     '«Отверженные» (Гюго)',
                     '«Граф Монте-Кристо» (Александр Дюма)',
                     '«Парижские тайны» (Эжен Сю)'],
              'en': ["'The Three Musketeers' (Dumas)",
                     "'Les Misérables' (Hugo)",
                     "'The Count of Monte Cristo' (Alexandre Dumas)",
                     "'The Mysteries of Paris' (Eugène Sue)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Graf Monte-Kristo» (Aleksandr Dyuma)',
                     'ru': '«Граф Монте-Кристо» (Александр Дюма)',
                     'en': "'The Count of Monte Cristo' (Alexandre Dumas)"},
  'image_url': None,
  'fun_fact': {'uz': 'Noqonuniy ravishda If qasri zindoniga tashlangan dengizchi Edmon Dantes abba Fariadan xazina '
                     'sirini bilib qochadi va dushmanlaridan qasos oladi.',
               'ru': 'Моряк Эдмон Дантес проводит 14 лет в темнице замка Иф, бежит в мешке для покойников, находит '
                     'сказочный клад и карает своих предателей.',
               'en': "Wrongfully imprisoned sailor Edmond Dantès escapes Château d'If, unearths hidden treasure on the "
                     'Isle of Monte Cristo, and exacts retribution.'},
  'aliases': ['graf monte-kristo', 'monte kristo', 'граф монте-кристо', 'count of monte cristo']},
 {'id': 'lit_emoji_024',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🥖⛓️👮\u200d♂️👧🇫🇷',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '🥖⛓️👮\u200d♂️👧🇫🇷',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🥖⛓️👮\u200d♂️👧🇫🇷'},
  'options': {'uz': ['«Parij Bibi Maryam ibodatxonasi» (Gyugo)',
                     '«Kulayotgan odam» (Gyugo)',
                     '«Gorio ota» (Balzak)',
                     "«Xo'rlanganlar» (Viktor Gyugo)"],
              'ru': ['«Собор Парижской Богоматери» (Гюго)',
                     '«Человек, который смеётся» (Гюго)',
                     '«Отец Горио» (Бальзак)',
                     '«Отверженные» (Виктор Гюго)'],
              'en': ["'The Hunchback of Notre-Dame' (Hugo)",
                     "'The Man Who Laughs' (Hugo)",
                     "'Père Goriot' (Balzac)",
                     "'Les Misérables' (Victor Hugo)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Xo'rlanganlar» (Viktor Gyugo)",
                     'ru': '«Отверженные» (Виктор Гюго)',
                     'en': "'Les Misérables' (Victor Hugo)"},
  'image_url': None,
  'fun_fact': {'uz': "Bitta non o'g'irlagani uchun 19 yil katorgada azob chekkan Jan Valjan, uning izidan qolmaydigan "
                     "qat'iy inspektor Javer va yetim qiz Kozetta taqdiri.",
               'ru': 'Бывший каторжник Жан Вальжан, осуждённый за кражу буханки хлеба, становится праведником и '
                     'спасает маленькую сироту Козетту.',
               'en': 'Ex-convict Jean Valjean seeks redemption while pursued across revolutionary France by the '
                     'fanatical police inspector Javert.'},
  'aliases': ["xo'rlanganlar", 'gyugo', 'отверженные', 'гюго', 'les miserables']},
 {'id': 'lit_emoji_025',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🖼️👴🥀🍷🪞',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🖼️👴🥀🍷🪞',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🖼️👴🥀🍷🪞'},
  'options': {'uz': ['«Dorian Greyning portreti» (Oskar Uayld)',
                     '«Doktor Jekil va mister Xayd» (Stivenson)',
                     '«Faust» (Gyote)',
                     '«Shagren terisi» (Balzak)'],
              'ru': ['«Портрет Дориана Грея» (Оскар Уайльд)',
                     '«Доктор Джекил и мистер Хайд» (Стивенсон)',
                     '«Фауст» (Гёте)',
                     '«Шагреневая кожа» (Бальзак)'],
              'en': ["'The Picture of Dorian Gray' (Oscar Wilde)",
                     "'Dr Jekyll and Mr Hyde' (Stevenson)",
                     "'Faust' (Goethe)",
                     "'The Wild Ass's Skin' (Balzac)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Dorian Greyning portreti» (Oskar Uayld)',
                     'ru': '«Портрет Дориана Грея» (Оскар Уайльд)',
                     'en': "'The Picture of Dorian Gray' (Oscar Wilde)"},
  'image_url': None,
  'fun_fact': {'uz': "Yosh va go'zal Dorian o'rniga uning portreti qariydi va har bir gunohi suratda dahshatli iz "
                     'qoldiradi.',
               'ru': 'Дориан Грей сохраняет вечную юность и красоту, в то время как скрытый на чердаке портрет стареет '
                     'и запечатлевает следы всех его пороков.',
               'en': 'The handsome youth Dorian Gray remains unblemished while his hidden painted portrait bears the '
                     'terrible physical signs of his sins and age.'},
  'aliases': ['dorian grey', 'uayld', 'дориан грей', 'уайльд', 'dorian gray', 'picture of dorian gray']},
 {'id': 'lit_emoji_026',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🔔⛪👹💃🐐',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🔔⛪👹💃🐐',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🔔⛪👹💃🐐'},
  'options': {'uz': ["«Xo'rlanganlar» (Gyugo)",
                     '«Parij Bibi Maryam ibodatxonasi» (Viktor Gyugo)',
                     '«Opera sharpasi» (Gaston Leru)',
                     '«Karmen» (Prosper Merime)'],
              'ru': ['«Отверженные» (Гюго)',
                     '«Собор Парижской Богоматери» (Виктор Гюго)',
                     '«Призрак Оперы» (Гастон Леру)',
                     '«Кармен» (Проспер Мериме)'],
              'en': ["'Les Misérables' (Hugo)",
                     "'The Hunchback of Notre-Dame' (Victor Hugo)",
                     "'The Phantom of the Opera' (Gaston Leroux)",
                     "'Carmen' (Prosper Mérimée)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Parij Bibi Maryam ibodatxonasi» (Viktor Gyugo)',
                     'ru': '«Собор Парижской Богоматери» (Виктор Гюго)',
                     'en': "'The Hunchback of Notre-Dame' (Victor Hugo)"},
  'image_url': None,
  'fun_fact': {'uz': "Sobor qo'ng'iroqchisi xunuk bukri Kvazimodo, sohibjamol lo'li qizi Esmeralda va zolim arxidiakon "
                     "Klod Frollo o'rtasidagi fojia.",
               'ru': 'Трогательная любовь уродливого звонаря Квазимодо к юной цыганке Эсмеральде на фоне величия '
                     'средневекового собора в Париже.',
               'en': 'The deformed bell-ringer Quasimodo passionately defends the gypsy dancer Esmeralda from '
                     'archdeacon Claude Frollo.'},
  'aliases': ['notr dam',
              'kvazimodo',
              'esmeralda',
              'собор парижской богоматери',
              'квазимодо',
              'hunchback of notre dame']},
 {'id': 'lit_emoji_027',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🚢👨\u200d🦱🤏🐎🏝️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🚢👨\u200d🦱🤏🐎🏝️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🚢👨\u200d🦱🤏🐎🏝️'},
  'options': {'uz': ['«Robinzon Kruzo» (Daniel Defo)',
                     '«Baron Myunxauzen sarguzashtlari» (Raspe)',
                     '«Gulliverning sayohatlari» (Jonatan Svift)',
                     '«Yer markaziga sayohat» (Jyul Vern)'],
              'ru': ['«Робинзон Крузо» (Даниэль Дефо)',
                     '«Приключения барона Мюнхгаузена» (Распе)',
                     '«Путешествия Гулливера» (Джонатан Свифт)',
                     '«Путешествие к центру Земли» (Жюль Верн)'],
              'en': ["'Robinson Crusoe' (Daniel Defoe)",
                     "'Baron Munchausen' (Raspe)",
                     "'Gulliver's Travels' (Jonathan Swift)",
                     "'Journey to the Center of the Earth' (Jules Verne)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Gulliverning sayohatlari» (Jonatan Svift)',
                     'ru': '«Путешествия Гулливера» (Джонатан Свифт)',
                     'en': "'Gulliver's Travels' (Jonathan Swift)"},
  'image_url': None,
  'fun_fact': {'uz': 'Kemadosh Lemuel Gulliver mittivoylar yurti Liliputiya, bahaybatlar mamlakati Brobdingneg va '
                     'aqlli otlar yurti Guygngnmlar mamlakatiga tushib qoladi.',
               'ru': 'Острая сатира на человеческое общество: Гулливер попадает к лилипутам, великанам-великанам, '
                     'летающий остров Лапуту и разумных лошадей-гуигнгнмов.',
               'en': "Ship's surgeon Lemuel Gulliver encounters six-inch Lilliputians, giants of Brobdingnag, and the "
                     'noble equine Houyhnhnms.'},
  'aliases': ['gulliver', 'svift', 'гулливер', 'свифт', 'gullivers travels']},
 {'id': 'lit_emoji_028',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧪👨\u200d⚕️➡️👹🦯🇬🇧',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '🧪👨\u200d⚕️➡️👹🦯🇬🇧',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧪👨\u200d⚕️➡️👹🦯🇬🇧'},
  'options': {'uz': ['«Dorian Greyning portreti» (Oskar Uayld)',
                     '«Frankenshteyn» (Meri Shelli)',
                     "«Ko'rinmas odam» (Gerbert Uells)",
                     '«Doktor Jekil va mister Xayd» (Robert Lyuis Stivenson)'],
              'ru': ['«Портрет Дориана Грея» (Оскар Уайльд)',
                     '«Франкенштейн» (Мэри Шелли)',
                     '«Человек-невидимка» (Герберт Уэллс)',
                     '«Странная история доктора Джекила и мистера Хайда» (Стивенсон)'],
              'en': ["'The Picture of Dorian Gray' (Oscar Wilde)",
                     "'Frankenstein' (Mary Shelley)",
                     "'The Invisible Man' (H.G. Wells)",
                     "'Strange Case of Dr Jekyll and Mr Hyde' (Robert Louis Stevenson)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Doktor Jekil va mister Xayd» (Robert Lyuis Stivenson)',
                     'ru': '«Странная история доктора Джекила и мистера Хайда» (Стивенсон)',
                     'en': "'Strange Case of Dr Jekyll and Mr Hyde' (Robert Louis Stevenson)"},
  'image_url': None,
  'fun_fact': {'uz': "Hurmatli shifokor Genri Jekil o'zining yovuz tabiatini ajratib oluvchi zardob ichib, shafqatsiz "
                     'jinoyatchi Edvard Xaydga aylanadi.',
               'ru': 'Викторианская притча о раздвоении личности: добропорядочный доктор Джекил изобретает зелье, '
                     'выпускающее на свободу его злобное эго Хайда.',
               'en': 'A respectable Victorian doctor brews a potion separating his good and evil instincts, '
                     'inadvertently unleashing the depraved Mr. Hyde.'},
  'aliases': ['doktor jekil', 'mister xayd', 'jekil va xayd', 'джекил и хайд', 'dr jekyll and mr hyde']},
 {'id': 'lit_emoji_029',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👓🧣🥼🧪👻',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👓🧣🥼🧪👻',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👓🧣🥼🧪👻'},
  'options': {'uz': ["«Ko'rinmas odam» (Gerbert Uells)",
                     '«Vaqt mashinasi» (Gerbert Uells)',
                     '«Dunyolar jangi» (Gerbert Uells)',
                     '«Amfibiya odam» (Aleksandr Belyayev)'],
              'ru': ['«Человек-невидимка» (Герберт Уэллс)',
                     '«Машина времени» (Герберт Уэллс)',
                     '«Война миров» (Герберт Уэллс)',
                     '«Человек-амфибия» (Александр Беляев)'],
              'en': ["'The Invisible Man' (H.G. Wells)",
                     "'The Time Machine' (H.G. Wells)",
                     "'The War of the Worlds' (H.G. Wells)",
                     "'Amphibian Man' (Alexander Belyaev)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«Ko'rinmas odam» (Gerbert Uells)",
                     'ru': '«Человек-невидимка» (Герберт Уэллс)',
                     'en': "'The Invisible Man' (H.G. Wells)"},
  'image_url': None,
  'fun_fact': {'uz': "Yosh fizik Griffin inson tanasini ko'rinmas qiluvchi apparat va dorini ixtiro qiladi, ammo "
                     'kiyimsiz sovuqda qolib, asta-sekin aqlidan ozadi.',
               'ru': 'Блестящий физик Гриффин открывает способ обесцвечивания крови и тканей, становясь невидимым '
                     'монстром, терроризирующим Англию.',
               'en': 'Brilliant scientist Griffin renders himself invisible, but descends into paranoia and terrorizes '
                     'the Sussex countryside.'},
  'aliases': ["ko'rinmas odam", 'uells', 'человек-невидимка', 'уэллс', 'the invisible man', 'h.g. wells']},
 {'id': 'lit_emoji_030',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏴\u200d☠️🦜🗺️🪙🏝️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '🏴\u200d☠️🦜🗺️🪙🏝️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏴\u200d☠️🦜🗺️🪙🏝️'},
  'options': {'uz': ['«Robinzon Kruzo» (Daniel Defo)',
                     '«Xazinalar oroli» (Robert Lyuis Stivenson)',
                     '«Sirli orol» (Jyul Vern)',
                     '«Kapitan Bloodning adissiyasi» (Rafael Sabatini)'],
              'ru': ['«Робинзон Крузо» (Даниэль Дефо)',
                     '«Остров сокровищ» (Роберт Льюис Стивенсон)',
                     '«Таинственный остров» (Жюль Верн)',
                     '«Одиссея капитана Блада» (Рафаэль Сабатини)'],
              'en': ["'Robinson Crusoe' (Daniel Defoe)",
                     "'Treasure Island' (Robert Louis Stevenson)",
                     "'The Mysterious Island' (Jules Verne)",
                     "'Captain Blood' (Rafael Sabatini)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Xazinalar oroli» (Robert Lyuis Stivenson)',
                     'ru': '«Остров сокровищ» (Роберт Льюис Стивенсон)',
                     'en': "'Treasure Island' (Robert Louis Stevenson)"},
  'image_url': None,
  'fun_fact': {'uz': "Jim Xokins kapitan Flintning xarita topib oladi va 'Ispanola' kemasida bir oyoqli qaroqchi Jon "
                     "Silver bilan xazina izlab yo'lga chiqadi.",
               'ru': 'Юный Джим Хокинс с пиратской картой сокровищ капитана Флинта отправляется в плавание на шхуне '
                     '«Эспаньола» против коварного Джона Сильвера.',
               'en': "Young Jim Hawkins discovers Captain Flint's treasure map, facing mutinous pirates led by "
                     'one-legged cook Long John Silver.'},
  'aliases': ['xazinalar oroli', 'stivenson', 'остров сокровищ', 'стивенсон', 'treasure island']},
 {'id': 'lit_emoji_031',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👦🪵🖌️⛵🪦',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👦🪵🖌️⛵🪦',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👦🪵🖌️⛵🪦'},
  'options': {'uz': ['«Geklberri Finn sarguzashtlari» (Mark Tven)',
                     '«Shahzoda va gado» (Mark Tven)',
                     '«Tom Soyerning sarguzashtlari» (Mark Tven)',
                     '«Oliver Tvist» (Charlz Dikkens)'],
              'ru': ['«Приключения Гекльберри Финна» (Марк Твен)',
                     '«Принц и нищий» (Марк Твен)',
                     '«Приключения Тома Сойера» (Марк Твен)',
                     '«Приключения Оливера Твиста» (Чарльз Диккенс)'],
              'en': ["'Adventures of Huckleberry Finn' (Mark Twain)",
                     "'The Prince and the Pauper' (Mark Twain)",
                     "'The Adventures of Tom Sawyer' (Mark Twain)",
                     "'Oliver Twist' (Charles Dickens)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Tom Soyerning sarguzashtlari» (Mark Tven)',
                     'ru': '«Приключения Тома Сойера» (Марк Твен)',
                     'en': "'The Adventures of Tom Sawyer' (Mark Twain)"},
  'image_url': None,
  'fun_fact': {'uz': "Polly xolaning devorini oqlash jazosini do'stlariga qimmatbaho ermakka aylantirgan sho'x Tom "
                     'Soyer va Gek Finn sarguzashtlari.',
               'ru': 'Том Сойер красит забор тёти Полли, сбегает на необитаемый остров на Миссисипи и находит клад в '
                     'пещере индейца Джо.',
               'en': "Mischievous Tom Sawyer tricks friends into whitewashing Aunt Polly's fence, attends his own "
                     "funeral, and explores McDougal's cave."},
  'aliases': ['tom soyer', 'mark tven', 'том сойер', 'марк твен', 'tom sawyer']},
 {'id': 'lit_emoji_032',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👑🤴🔄👦🏚️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👑🤴🔄👦🏚️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👑🤴🔄👦🏚️'},
  'options': {'uz': ['«Tom Soyerning sarguzashtlari» (Mark Tven)',
                     '«Temir niqob» (Aleksandr Dyuma)',
                     '«Kichkina lord Fontleroy» (Frensis Bernett)',
                     '«Shahzoda va gado» (Mark Tven)'],
              'ru': ['«Приключения Тома Сойера» (Марк Твен)',
                     '«Железная маска» (Александр Дюма)',
                     '«Маленький лорд Фаунтлерой» (Фрэнсис Бернетт)',
                     '«Принц и нищий» (Марк Твен)'],
              'en': ["'The Adventures of Tom Sawyer' (Mark Twain)",
                     "'The Man in the Iron Mask' (Alexandre Dumas)",
                     "'Little Lord Fauntleroy' (Frances Hodgson Burnett)",
                     "'The Prince and the Pauper' (Mark Twain)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Shahzoda va gado» (Mark Tven)',
                     'ru': '«Принц и нищий» (Марк Твен)',
                     'en': "'The Prince and the Pauper' (Mark Twain)"},
  'image_url': None,
  'fun_fact': {'uz': "London xarobasida tug'ilgan Tom Kenti va Angliya taxti vorisi shahzoda Eduard o'xshashliklaridan "
                     'foydalanib kiyimlarini almashtirishadi.',
               'ru': 'Бедный мальчик Том Кенти и будущий король Англии Эдуард VI, похожие как две капли воды, случайно '
                     'меняются местами и судьбами.',
               'en': 'Impoverished London street urchin Tom Canty and Crown Prince Edward Tudor swap clothes and '
                     'experience life on opposite sides of society.'},
  'aliases': ['shahzoda va gado', 'mark tven', 'принц и нищий', 'марк твен', 'prince and the pauper']},
 {'id': 'lit_emoji_033',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🚢🌊🤿🐙⚙️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🚢🌊🤿🐙⚙️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🚢🌊🤿🐙⚙️'},
  'options': {'uz': ['«Suv ostida 20 000 lye» (Jyul Vern)',
                     '«Sirli orol» (Jyul Vern)',
                     '«Kapitan Nemo» (Jyul Vern)',
                     '«Yer markaziga sayohat» (Jyul Vern)'],
              'ru': ['«Двадцать тысяч лье под водой» (Жюль Верн)',
                     '«Таинственный остров» (Жюль Верн)',
                     '«Дети капитана Гранта» (Жюль Верн)',
                     '«Путешествие к центру Земли» (Жюль Верн)'],
              'en': ["'Twenty Thousand Leagues Under the Sea' (Jules Verne)",
                     "'The Mysterious Island' (Jules Verne)",
                     "'In Search of the Castaways' (Jules Verne)",
                     "'Journey to the Center of the Earth' (Jules Verne)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Suv ostida 20 000 lye» (Jyul Vern)',
                     'ru': '«Двадцать тысяч лье под водой» (Жюль Верн)',
                     'en': "'Twenty Thousand Leagues Under the Sea' (Jules Verne)"},
  'image_url': None,
  'fun_fact': {'uz': "Professor Aronaks va uning do'stlari kapitan Nemoning 'Nautilus' suvosti kemasida jahon "
                     'okeanlari tubiga unutilmas ilmiy sayohat qiladilar.',
               'ru': 'Капитан Немо бороздит глубины мирового океана на электрической подлодке «Наутилус», сражаясь с '
                     'гигантскими спрутами.',
               'en': "Professor Aronnax journeys through the deep ocean aboard the enigmatic Captain Nemo's advanced "
                     'submarine Nautilus.'},
  'aliases': ['suv ostida 20000 lye',
              'kapitan nemo',
              'nautilus',
              '20000 лье под водой',
              'капитан немо',
              'twenty thousand leagues']},
 {'id': 'lit_emoji_034',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🇬🇧⏱️🚂🚢🎈',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🇬🇧⏱️🚂🚢🎈',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🇬🇧⏱️🚂🚢🎈'},
  'options': {'uz': ['«Kapitan Grant bolalari» (Jyul Vern)',
                     "«Sakson kunda yer yuzi bo'ylab» (Jyul Vern)",
                     "«O'n besh yoshli kapitan» (Jyul Vern)",
                     '«Gulliverning sayohatlari» (Svift)'],
              'ru': ['«Дети капитана Гранта» (Жюль Верн)',
                     '«Вокруг света за 80 дней» (Жюль Верн)',
                     '«Пятнадцатилетний капитан» (Жюль Верн)',
                     '«Путешествия Гулливера» (Свифт)'],
              'en': ["'In Search of the Castaways' (Jules Verne)",
                     "'Around the World in Eighty Days' (Jules Verne)",
                     "'Dick Sand, A Boy Captain' (Jules Verne)",
                     "'Gulliver's Travels' (Jonathan Swift)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Sakson kunda yer yuzi bo'ylab» (Jyul Vern)",
                     'ru': '«Вокруг света за 80 дней» (Жюль Верн)',
                     'en': "'Around the World in Eighty Days' (Jules Verne)"},
  'image_url': None,
  'fun_fact': {'uz': "Ingliz jentlmeni Fileas Fogg va uning xizmatkori Paspartu Reform-klub a'zolari bilan 80 kunda "
                     "butun dunyoni aylanib chiqishga garov bog'laydilar.",
               'ru': 'Педантичный лондонец Филеас Фогг выигрывает пари благодаря пересечению линии перемены дат при '
                     'движении на восток.',
               'en': 'Phileas Fogg and French valet Passepartout race against the clock to circle the globe in eighty '
                     'days on a £20,000 wager.'},
  'aliases': ['sakson kunda',
              'fileas fogg',
              'вокруг света за 80 дней',
              'жюль верн',
              'around the world in eighty days']},
 {'id': 'lit_emoji_035',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👽🔴🚀👾🦠',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👽🔴🚀👾🦠',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👽🔴🚀👾🦠'},
  'options': {'uz': ['«Vaqt mashinasi» (Gerbert Uells)',
                     "«Ko'rinmas odam» (Gerbert Uells)",
                     '«Dunyolar jangi» (Gerbert Uells)',
                     '«Mars yilnomalari» (Rey Bredberi)'],
              'ru': ['«Машина времени» (Герберт Уэллс)',
                     '«Человек-невидимка» (Герберт Уэллс)',
                     '«Война миров» (Герберт Уэллс)',
                     '«Марсианские хроники» (Рэй Брэдбери)'],
              'en': ["'The Time Machine' (H.G. Wells)",
                     "'The Invisible Man' (H.G. Wells)",
                     "'The War of the Worlds' (H.G. Wells)",
                     "'The Martian Chronicles' (Ray Bradbury)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Dunyolar jangi» (Gerbert Uells)',
                     'ru': '«Война миров» (Герберт Уэллс)',
                     'en': "'The War of the Worlds' (H.G. Wells)"},
  'image_url': None,
  'fun_fact': {'uz': 'Marsliklarning uch oyoqli jangovar mashinalarda Yerga bostirib kirishi va odamlar qurollari '
                     "emas, oddiy Yer mikroblari ularni mag'lub etishi haqidagi asar.",
               'ru': 'Марсиане с тепловыми лучами и чёрным дымом сокрушают армии Британской империи, но гибнут от '
                     'земных бактерий.',
               'en': 'Martian invaders in towering tripod fighting-machines devastate England, until defeated by '
                     'common terrestrial bacteria.'},
  'aliases': ['dunyolar jangi', 'uells', 'война миров', 'уэллс', 'war of the worlds', 'h.g. wells']},
 {'id': 'lit_emoji_036',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⏳🕰️⚙️👤👹',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⏳🕰️⚙️👤👹',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⏳🕰️⚙️👤👹'},
  'options': {'uz': ['«Dunyolar jangi» (Gerbert Uells)',
                     '«Doktor Moro oroli» (Gerbert Uells)',
                     '«Farengeyt 451» (Rey Bredberi)',
                     '«Vaqt mashinasi» (Gerbert Uells)'],
              'ru': ['«Война миров» (Герберт Уэллс)',
                     '«Остров доктора Моро» (Герберт Уэллс)',
                     '«451 градус по Фаренгейту» (Брэдбери)',
                     '«Машина времени» (Герберт Уэллс)'],
              'en': ["'The War of the Worlds' (H.G. Wells)",
                     "'The Island of Doctor Moreau' (H.G. Wells)",
                     "'Fahrenheit 451' (Ray Bradbury)",
                     "'The Time Machine' (H.G. Wells)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Vaqt mashinasi» (Gerbert Uells)',
                     'ru': '«Машина времени» (Герберт Уэллс)',
                     'en': "'The Time Machine' (H.G. Wells)"},
  'image_url': None,
  'fun_fact': {'uz': 'Sayohat qiluvchi olim 802701 yilga borib, insoniyat nozik eloylar va yer ostida yashovchi '
                     "shafqatsiz morloklarga bo'linib ketganini ko'radi.",
               'ru': 'Путешественник во времени переносится в 802 701 год, заставая вырождение человечества на '
                     'беззаботных элоев и подземных хищных морлоков.',
               'en': 'A Victorian scientist travels to AD 802,701, discovering humanity split into the childlike Eloi '
                     'and subterranean cannibal Morlocks.'},
  'aliases': ['vaqt mashinasi', 'uells', 'машина времени', 'уэллс', 'the time machine']},
 {'id': 'lit_emoji_037',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧢🌾🗽🦆🎒',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🧢🌾🗽🦆🎒',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧢🌾🗽🦆🎒'},
  'options': {'uz': ['«Javdarzordagi xaloskor» (J.D. Selinjer)',
                     '«Buyuk Getsbi» (Fitsjerald)',
                     "«Yo'lda» (Jek Keruak)",
                     "«Kiyikshosharni o'ldirish» (Harper Li)"],
              'ru': ['«Над пропастью во ржи» (Дж. Д. Сэлинджер)',
                     '«Великий Гэтсби» (Фицджеральд)',
                     '«В дороге» (Джек Керуак)',
                     '«Убить пересмешника» (Харпер Ли)'],
              'en': ["'The Catcher in the Rye' (J.D. Salinger)",
                     "'The Great Gatsby' (Fitzgerald)",
                     "'On the Road' (Jack Kerouac)",
                     "'To Kill a Mockingbird' (Harper Lee)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Javdarzordagi xaloskor» (J.D. Selinjer)',
                     'ru': '«Над пропастью во ржи» (Дж. Д. Сэлинджер)',
                     'en': "'The Catcher in the Rye' (J.D. Salinger)"},
  'image_url': None,
  'fun_fact': {'uz': 'Qizil ovchi qalpoqchasini kiygan 16 yoshli Xolden Kolfild maktabdan haydalib, Nyu-York '
                     "ko'chalarida aylanadi va Markaziy bog'dagi o'rdaklar qayerga uchib ketishini so'raydi.",
               'ru': 'Холден Колфилд в красной охотничьей шапке бродит по предрождественскому Нью-Йорку, рассуждая о '
                     'фальши взрослых и утках на пруду.',
               'en': 'Red hunting-cap-wearing Holden Caulfield wanders New York City pondering phoniness and where '
                     'Central Park ducks go in winter.'},
  'aliases': ['javdarzordagi xaloskor', 'selinjer', 'над пропастью во ржи', 'сэлинджер', 'catcher in the rye']},
 {'id': 'lit_emoji_038',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐦⚖️👨\u200d⚖️👧🌳',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐦⚖️👨\u200d⚖️👧🌳',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐦⚖️👨\u200d⚖️👧🌳'},
  'options': {'uz': ["«G'azab mevalari» (Jon Steynbek)",
                     "«Kiyikshosharni o'ldirish» (Harper Li)",
                     '«Sichqonlar va odamlar haqida» (Steynbek)',
                     "«Shovqin va g'azab» (Uilyam Folkner)"],
              'ru': ['«Гроздья гнева» (Джон Стейнбек)',
                     '«Убить пересмешника» (Харпер Ли)',
                     '«О мышах и людях» (Джон Стейнбек)',
                     '«Шум и ярость» (Уильям Фолкнер)'],
              'en': ["'The Grapes of Wrath' (John Steinbeck)",
                     "'To Kill a Mockingbird' (Harper Lee)",
                     "'Of Mice and Men' (John Steinbeck)",
                     "'The Sound and the Fury' (William Faulkner)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Kiyikshosharni o'ldirish» (Harper Li)",
                     'ru': '«Убить пересмешника» (Харпер Ли)',
                     'en': "'To Kill a Mockingbird' (Harper Lee)"},
  'image_url': None,
  'fun_fact': {'uz': 'Alabama shtatidagi Meykomb shahrida advokat Attikus Finch begunoh qora tanli Tom Robinsonni '
                     'sudda himoya qiladi; mockingbird (sayroqi qush) begunohlik ramzidir.',
               'ru': 'Адвокат Аттикус Финч защищает в суде чернокожего парня, ложно обвинённого в насилии, преподавая '
                     'детям уроки истинного мужества.',
               'en': 'Lawyer Atticus Finch defends Tom Robinson, a Black man falsely accused of rape, teaching '
                     "children that it's a sin to kill a mockingbird."},
  'aliases': ["kiyikshosharni o'ldirish", 'harper li', 'убить пересмешника', 'харпер ли', 'to kill a mockingbird']},
 {'id': 'lit_emoji_039',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏝️🐚👓🐗🔥',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏝️🐚👓🐗🔥',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏝️🐚👓🐗🔥'},
  'options': {'uz': ['«Robinzon Kruzo» (Daniel Defo)',
                     '«Sirli orol» (Jyul Vern)',
                     '«Pashshalar tangrisi» (Uilyam Golding)',
                     '«Kaptarlar oroli» (Golding)'],
              'ru': ['«Робинзон Крузо» (Даниэль Дефо)',
                     '«Таинственный остров» (Жюль Верн)',
                     '«Повелитель мух» (Уильям Голдинг)',
                     '«Наследники» (Уильям Голдинг)'],
              'en': ["'Robinson Crusoe' (Daniel Defoe)",
                     "'The Mysterious Island' (Jules Verne)",
                     "'Lord of the Flies' (William Golding)",
                     "'The Inheritors' (William Golding)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Pashshalar tangrisi» (Uilyam Golding)',
                     'ru': '«Повелитель мух» (Уильям Голдинг)',
                     'en': "'Lord of the Flies' (William Golding)"},
  'image_url': None,
  'fun_fact': {'uz': "Kimsasiz orolga tushgan bolalar dengiz chig'anog'i (konx) orqali tartib saqlashga harakat "
                     "qiladi, ammo tez orada yovvoyilashib cho'chqa ovlashga o'tadi.",
               'ru': 'Британские школьники на необитаемом острове скатываются к первобытной дикости вокруг насаженной '
                     'на кол головы свиньи.',
               'en': 'Stranded British schoolboys establish order with a conch shell, only to descend into savage '
                     "violence surrounding the pig's head on a stake."},
  'aliases': ['pashshalar tangrisi', 'golding', 'повелитель мух', 'голдинг', 'lord of the flies']},
 {'id': 'lit_emoji_040',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👁️📺🐀📖🚫',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👁️📺🐀📖🚫',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👁️📺🐀📖🚫'},
  'options': {'uz': ['«Molxona» (Jorj Oruell)',
                     '«Farengeyt 451» (Rey Bredberi)',
                     '«Ajib yangi dunyo» (Oldos Xaksli)',
                     '«1984» (Jorj Oruell)'],
              'ru': ['«Скотный двор» (Джордж Оруэлл)',
                     '«451 градус по Фаренгейту» (Брэдбери)',
                     '«О дивный новый мир» (Олдос Хаксли)',
                     '«1984» (Джордж Оруэлл)'],
              'en': ["'Animal Farm' (George Orwell)",
                     "'Fahrenheit 451' (Ray Bradbury)",
                     "'Brave New World' (Aldous Huxley)",
                     "'1984' (George Orwell)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«1984» (Jorj Oruell)', 'ru': '«1984» (Джордж Оруэлл)', 'en': "'1984' (George Orwell)"},
  'image_url': None,
  'fun_fact': {'uz': "Uinston Smit Haqiqat vazirligida tarixni qayta yozish bilan shug'ullanadi, teleskrinlar orqali "
                     'kuzatiladi va 101-xonada kalamushlar bilan qiynoqqa solinadi.',
               'ru': 'Уинстон Смит работает в Министерстве правды, скрытно ведёт дневник и проходит пытки в страшной '
                     'комнате 101.',
               'en': 'Winston Smith toils at the Ministry of Truth altering historical records until betrayed into '
                     'Room 101 by the Thought Police.'},
  'aliases': ['1984', 'oruell', 'уинстон смит', 'orwell', 'nineteen eighty four']},
 {'id': 'lit_emoji_041',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧪💊👶🧬😄',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🧪💊👶🧬😄',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧪💊👶🧬😄'},
  'options': {'uz': ['«Ajib yangi dunyo» (Oldos Xaksli)',
                     '«1984» (Jorj Oruell)',
                     '«Farengeyt 451» (Rey Bredberi)',
                     '«Biz» (Yevgeniy Zamyatin)'],
              'ru': ['«О дивный новый мир» (Олдос Хаксли)',
                     '«1984» (Джордж Оруэлл)',
                     '«451 градус по Фаренгейту» (Брэдбери)',
                     '«Мы» (Евгений Замятин)'],
              'en': ["'Brave New World' (Aldous Huxley)",
                     "'1984' (George Orwell)",
                     "'Fahrenheit 451' (Ray Bradbury)",
                     "'We' (Yevgeny Zamyatin)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Ajib yangi dunyo» (Oldos Xaksli)',
                     'ru': '«О дивный новый мир» (Олдос Хаксли)',
                     'en': "'Brave New World' (Aldous Huxley)"},
  'image_url': None,
  'fun_fact': {'uz': "Kelajakda bolalar probirkalarda kastalarga (alfa, beta, gamma, delta, epsiolon) bo'linib "
                     "yetishtiriladi va muammolardan qochish uchun 'soma' tabletkasi ichiladi.",
               'ru': 'Технократическое общество потребления, где людей выращивают в инкубаторах по кастам, а депрессию '
                     'глушат наркотиком «сома».',
               'en': 'Citizens are genetically bred in test-tube hatcheries into strict castes, conditioned to '
                     "consume, and dosed with euphoric 'soma'."},
  'aliases': ['ajib yangi dunyo', 'xaksli', 'о дивный новый мир', 'хаксли', 'brave new world', 'aldous huxley']},
 {'id': 'lit_emoji_042',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⚖️👨\u200d💼🏛️❓🔪',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⚖️👨\u200d💼🏛️❓🔪',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⚖️👨\u200d💼🏛️❓🔪'},
  'options': {'uz': ['«Evrilish» (Frans Kafka)',
                     '«Sud jarayoni» (Frans Kafka)',
                     '«Qasr» (Frans Kafka)',
                     '«Begona» (Alber Kamyu)'],
              'ru': ['«Превращение» (Франц Кафка)',
                     '«Процесс» (Франц Кафка)',
                     '«Замок» (Франц Кафка)',
                     '«Посторонний» (Альбер Камю)'],
              'en': ["'The Metamorphosis' (Franz Kafka)",
                     "'The Trial' (Franz Kafka)",
                     "'The Castle' (Franz Kafka)",
                     "'The Stranger' (Albert Camus)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Sud jarayoni» (Frans Kafka)',
                     'ru': '«Процесс» (Франц Кафка)',
                     'en': "'The Trial' (Franz Kafka)"},
  'image_url': None,
  'fun_fact': {'uz': 'Bank xodimi Yozef K. bir tongda hibsga olinadi, ammo butun asar davomida unga qanday ayb '
                     "qo'yilgani noma'lumligicha qoladi.",
               'ru': 'Йозеф К. просыпается утром и узнаёт, что арестован, но никакие судебные инстанции так и не '
                     'называют состава его преступления.',
               'en': 'Josef K. is mysteriously arrested on his 30th birthday and prosecuted by an inaccessible, '
                     'labyrinthine bureaucratic authority.'},
  'aliases': ['sud jarayoni', 'kafka', 'процесс', 'кафка', 'the trial', 'josef k']},
 {'id': 'lit_emoji_043',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐀😷🏥🚪⚰️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐀😷🏥🚪⚰️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐀😷🏥🚪⚰️'},
  'options': {'uz': ['«Begona» (Alber Kamyu)',
                     "«Ko'ngil aynishi» (Jan-Pol Sartr)",
                     '«Vabo» (Alber Kamyu)',
                     "«Qizil o'lim niqobi» (Edgar Allan Po)"],
              'ru': ['«Посторонний» (Альбер Камю)',
                     '«Тошнота» (Жан-Поль Сартр)',
                     '«Чума» (Альбер Камю)',
                     '«Маска Красной смерти» (Эдгар По)'],
              'en': ["'The Stranger' (Albert Camus)",
                     "'Nausea' (Jean-Paul Sartre)",
                     "'The Plague' (Albert Camus)",
                     "'The Masque of the Red Death' (Edgar Allan Poe)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Vabo» (Alber Kamyu)', 'ru': '«Чума» (Альбер Камю)', 'en': "'The Plague' (Albert Camus)"},
  'image_url': None,
  'fun_fact': {'uz': 'Jazoirning Oran shahrida vabo epidemiyasi boshlanadi; doktor Bernar Rye va uning safdoshlari '
                     "shafqatsiz o'limga qarshi kurashadilar.",
               'ru': 'Доктор Бернар Риэ организует санитарные дружины в заблокированном чумой алжирском городе Оран; '
                     'роман служит аллегорией Сопротивления.',
               'en': 'Dr. Bernard Rieux leads medical resistance against a deadly bubonic plague outbreak sealing off '
                     'the Algerian port of Oran.'},
  'aliases': ['vabo', 'kamyu', 'чума', 'камю', 'the plague', 'albert camus']},
 {'id': 'lit_emoji_044',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⛵👁️🧜\u200d♀️🐖🏹',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⛵👁️🧜\u200d♀️🐖🏹',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⛵👁️🧜\u200d♀️🐖🏹'},
  'options': {'uz': ['«Iliada» (Gomer)',
                     '«Eneida» (Vergiliy)',
                     '«Argonavtlar» (Apolloniy Rodoslik)',
                     '«Odisseya» (Gomer)'],
              'ru': ['«Илиада» (Гомер)',
                     '«Энеида» (Вергилий)',
                     '«Аргонавтика» (Аполлоний Родосский)',
                     '«Одиссея» (Гомер)'],
              'en': ["'The Iliad' (Homer)",
                     "'The Aeneid' (Virgil)",
                     "'Argonautica' (Apollonius of Rhodes)",
                     "'The Odyssey' (Homer)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Odisseya» (Gomer)', 'ru': '«Одиссея» (Гомер)', 'en': "'The Odyssey' (Homer)"},
  'image_url': None,
  'fun_fact': {'uz': "Itaka shohi Odissey bir ko'zli Siklop Polifem, sehrgar Sirseya va sirenalar sinovlaridan o'tib, "
                     'sadoqatli rafiqasi Penelopa huzuriga qaytadi.',
               'ru': 'Царь Одиссей ослепляет циклопа Полифема, спасается от сирен и Сциллы с Харибдой, возвращаясь на '
                     'родную Итаку спустя 20 лет.',
               'en': 'Odysseus outwits the Cyclops Polyphemus, resists Circe and the Sirens, and strings his great bow '
                     'to reclaim Ithaca.'},
  'aliases': ['odisseya', 'gomer', 'одиссея', 'гомер', 'the odyssey', 'odysseus']},
 {'id': 'lit_emoji_045',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🛡️🐎🔥🏹👑',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🛡️🐎🔥🏹👑',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🛡️🐎🔥🏹👑'},
  'options': {'uz': ['«Iliada» (Gomer)', '«Odisseya» (Gomer)', '«Eneida» (Vergiliy)', '«Shohnoma» (Firdavsiy)'],
              'ru': ['«Илиада» (Гомер)', '«Одиссея» (Гомер)', '«Энеида» (Вергилий)', '«Шахнаме» (Фирдоуси)'],
              'en': ["'The Iliad' (Homer)",
                     "'The Odyssey' (Homer)",
                     "'The Aeneid' (Virgil)",
                     "'Shahnameh' (Ferdowsi)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Iliada» (Gomer)', 'ru': '«Илиада» (Гомер)', 'en': "'The Iliad' (Homer)"},
  'image_url': None,
  'fun_fact': {'uz': "Axill va Agamemnon ixtilofi, Gektor va Axill jangi hamda Troya qamalining so'nggi 50 kunlik "
                     'shiddatli janglari tasvirlangan epos.',
               'ru': 'Эпос Гомера о гневе Ахиллеса, гибели Патрокла, поединке с Гектором и троянском коне.',
               'en': 'The wrath of Achilles, the fall of Trojan hero Hector, and the epic siege of Ilium immortalized '
                     'by Homer.'},
  'aliases': ['iliada', 'gomer', 'илиада', 'гомер', 'the iliad', 'achilles']},
 {'id': 'lit_emoji_046',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🔥👿⛰️🕊️✨',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🔥👿⛰️🕊️✨',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🔥👿⛰️🕊️✨'},
  'options': {'uz': ['«Dekameron» (Bokkachcho)',
                     '«Ilohiy komediya» (Dante Aligyeri)',
                     "«Yo'qotilgan jannat» (Milton)",
                     '«Faust» (Gyote)'],
              'ru': ['«Декамерон» (Боккаччо)',
                     '«Божественная комедия» (Данте Алигьери)',
                     '«Потерянный рай» (Мильтон)',
                     '«Фауст» (Гёте)'],
              'en': ["'The Decameron' (Boccaccio)",
                     "'The Divine Comedy' (Dante Alighieri)",
                     "'Paradise Lost' (John Milton)",
                     "'Faust' (Goethe)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Ilohiy komediya» (Dante Aligyeri)',
                     'ru': '«Божественная комедия» (Данте Алигьери)',
                     'en': "'The Divine Comedy' (Dante Alighieri)"},
  'image_url': None,
  'fun_fact': {'uz': "Dantening shoir Vergiliy va sevikli Beatriche hamrohligida Do'zaxning 9 doirasi, A'rof va Jannat "
                     "bo'ylab qilgan tasavvufiy sayohati.",
               'ru': 'Путешествие Данте через 9 кругов Ада, гору Чистилища и небесные сферы Рая под предводительством '
                     'Вергилия и Беатриче.',
               'en': 'Dante journeys through the nine circles of the Inferno, ascends Mount Purgatory, and reaches '
                     'Paradise guided by Beatrice.'},
  'aliases': ['ilohiy komediya', 'dante', 'божественная комедия', 'данте', 'divine comedy', 'inferno']},
 {'id': 'lit_emoji_047',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n📜✍️🩸😈👧',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n📜✍️🩸😈👧',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n📜✍️🩸😈👧'},
  'options': {'uz': ['«Ilohiy komediya» (Dante)',
                     '«Shagren terisi» (Balzak)',
                     '«Faust» (Iogann Volfgang fon Gyote)',
                     '«Qaroqchilar» (Shiller)'],
              'ru': ['«Божественная комедия» (Данте)',
                     '«Шагреневая кожа» (Бальзак)',
                     '«Фауст» (Иоганн Вольфганг фон Гёте)',
                     '«Разбойники» (Шиллер)'],
              'en': ["'The Divine Comedy' (Dante)",
                     "'The Wild Ass's Skin' (Balzac)",
                     "'Faust' (Johann Wolfgang von Goethe)",
                     "'The Robbers' (Friedrich Schiller)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Faust» (Iogann Volfgang fon Gyote)',
                     'ru': '«Фауст» (Иоганн Вольфганг фон Гёте)',
                     'en': "'Faust' (Johann Wolfgang von Goethe)"},
  'image_url': None,
  'fun_fact': {'uz': "Doktor Faust abadiy yoshlik va cheksiz bilim evaziga o'z qoni bilan Mefistofelga jonini sotadi "
                     'va Margaritani (Gretxen) sevib qoladi.',
               'ru': 'Доктор Фауст подписывает кровью договор с Мефистофелем, стремясь познать полноту бытия, что '
                     'приводит к гибели Гретхен.',
               'en': 'Dr. Heinrich Faust trades his soul to Mephistopheles for worldly pleasure, endless wisdom, and '
                     "youth, leading to Gretchen's tragedy."},
  'aliases': ['faust', 'gyote', 'фауст', 'гёте', 'faust goethe', 'mephistopheles']},
 {'id': 'lit_emoji_048',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👧🧕🔒👵😭',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👧🧕🔒👵😭',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👧🧕🔒👵😭'},
  'options': {'uz': ["«O'tkan kunlar» (Abdulla Qodiriy)",
                     '«Mehrobdan chayon» (Abdulla Qodiriy)',
                     "«Qutlug' qon» (Oybek)",
                     "«Kecha va kunduz» (Abdulhamid Cho'lpon)"],
              'ru': ['«Минувшие дни» (Абдулла Кадыри)',
                     '«Скорпион из алтаря» (Кадыри)',
                     '«Священная кровь» (Айбек)',
                     '«Ночь и день» (Абдулхамид Чулпан)'],
              'en': ["'Bygone Days' (Abdulla Qadiri)",
                     "'Scorpion from the Altar' (Qadiri)",
                     "'Sacred Blood' (Oybek)",
                     "'Night and Day' (Abdulhamid Cholpon)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Kecha va kunduz» (Abdulhamid Cho'lpon)",
                     'ru': '«Ночь и день» (Абдулхамид Чулпан)',
                     'en': "'Night and Day' (Abdulhamid Cholpon)"},
  'image_url': None,
  'fun_fact': {'uz': "Beg'ubor Zebi qizning keksaygan amaldor Mingboshiga to'rtinchi xotin qilib majburlab uzatilishi "
                     'va uning fojiali qismati tasvirlangan jadidchilik romani.',
               'ru': 'Трагедия юной поэтичной Зебихон, насильно выданной замуж четвёртой женой за сластолюбивого '
                     'Мингбаши Акбарали.',
               'en': "Cholpon's masterpiece portrays the innocent village girl Zebi, forced to become the fourth wife "
                     'of the corrupt district chief Akbarali.'},
  'aliases': ['kecha va kunduz', "cho'lpon", 'ночь и день', 'чулпан', 'night and day', 'zebi']},
 {'id': 'lit_emoji_049',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🦂🕌📿💔👑',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🦂🕌📿💔👑',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🦂🕌📿💔👑'},
  'options': {'uz': ['«Mehrobdan chayon» (Abdulla Qodiriy)',
                     "«O'tkan kunlar» (Abdulla Qodiriy)",
                     "«Qutlug' qon» (Oybek)",
                     '«Dahshat» (Abdulla Qahhor)'],
              'ru': ['«Скорпион из алтаря» (Абдулла Кадыри)',
                     '«Минувшие дни» (Абдулла Кадыри)',
                     '«Священная кровь» (Айбек)',
                     '«Ужас» (Абдулла Каххар)'],
              'en': ["'Scorpion from the Altar' (Abdulla Qadiri)",
                     "'Bygone Days' (Abdulla Qadiri)",
                     "'Sacred Blood' (Oybek)",
                     "'The Horror' (Abdulla Qahhor)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Mehrobdan chayon» (Abdulla Qodiriy)',
                     'ru': '«Скорпион из алтаря» (Абдулла Кадыри)',
                     'en': "'Scorpion from the Altar' (Abdulla Qadiri)"},
  'image_url': None,
  'fun_fact': {'uz': "Mirzo Anvar va Ra'noning sevgisi hamda xon saroyidagi munofiq dinpeshvolar (Domla Shahobiddin) "
                     'fitnalari fosh etilgan roman.',
               'ru': 'Исторический роман Кадыри о любви Мирзо Анвара и Рано и кознях коварных ханских фарисеев '
                     '(«скорпионов из алтаря»).',
               'en': "Qadiri's second novel exposes hypocrisy among the religious hypocrites and courtiers plotting "
                     "against Mirzo Anvar and Ra'no."},
  'aliases': ['mehrobdan chayon', 'qodiriy', 'скорпион из алтаря', 'кадыри', 'scorpion from the altar']},
 {'id': 'lit_emoji_050',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧢🧙\u200d♂️🍯🪙✈️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🧢🧙\u200d♂️🍯🪙✈️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧢🧙\u200d♂️🍯🪙✈️'},
  'options': {'uz': ["«Shum bola» (G'afur G'ulom)",
                     "«Sariq devni minib» (Xudoyberdi To'xtaboyev)",
                     "«Shirin qovunlar mamlakati» (To'xtaboyev)",
                     "«Mungli ko'zlar» (To'xtaboyev)"],
              'ru': ['«Озорник» (Гафур Гулям)',
                     '«Верхом на жёлтом диве» (Худайберды Тухтабаев)',
                     '«Страна сладких дынь» (Тухтабаев)',
                     '«Печальные глаза» (Тухтабаев)'],
              'en': ["'The Mischievous Boy' (Ghafur Ghulam)",
                     "'Riding the Yellow Giant' (Khudoyberdi Tukhtabayev)",
                     "'Land of Sweet Melons' (Tukhtabayev)",
                     "'Sorrowful Eyes' (Tukhtabayev)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Sariq devni minib» (Xudoyberdi To'xtaboyev)",
                     'ru': '«Верхом на жёлтом диве» (Худайберды Тухтабаев)',
                     'en': "'Riding the Yellow Giant' (Khudoyberdi Tukhtabayev)"},
  'image_url': None,
  'fun_fact': {'uz': 'Hoshimjonning sehrli qalpoqcha orqali kutilmagan sarguzashtlarga tushishi va oxir-oqibat mehnat '
                     "va bilimdan boshqa mo''jiza yo'qligini tushunishi.",
               'ru': 'Хашимджан мечтает разбогатеть без труда с помощью волшебной шапки-невидимки, но попадает в '
                     'комичные переделки и осознаёт ценность учёбы.',
               'en': 'Hoshimjon uses an invisibility cap to dodge school and chase shortcuts to glory, ultimately '
                     'realizing knowledge and hard work are true magic.'},
  'aliases': ['sariq devni minib', "to'xtaboyev", 'верхом на желтом диве', 'тухтабаев', 'hoshimjon']},
 {'id': 'lit_emoji_051',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏹🐎🛡️👸⛓️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏹🐎🛡️👸⛓️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏹🐎🛡️👸⛓️'},
  'options': {'uz': ["«Go'ro'g'li» dostoni",
                     "«Kuntug'mish» dostoni",
                     "«Alpomish» (O'zbek xalq qahramonlik eposi)",
                     '«Rustamxon» dostoni'],
              'ru': ['«Гёроглы»', '«Кунтугмыш»', '«Алпамыш» (узбекский героический эпос)', '«Рустамхан»'],
              'en': ["'Gorogly'", "'Kuntugmish'", "'Alpomish' (Uzbek Heroic Folk Epic)", "'Rustamkhan'"]},
  'correct_index': 2,
  'correct_answer': {'uz': "«Alpomish» (O'zbek xalq qahramonlik eposi)",
                     'ru': '«Алпамыш» (узбекский героический эпос)',
                     'en': "'Alpomish' (Uzbek Heroic Folk Epic)"},
  'image_url': None,
  'fun_fact': {'uz': "Qo'ng'irot urug'i bahodiri Hakimbek (Alpomish)ning Barchinoy sevgisi yo'lidagi mardligi, "
                     "Boychibor oti va zindondan qutulishi haqidagi ulug'vor doston.",
               'ru': 'Эпос о богатыре Алпамыше, его верном коне Байчибаре и подвигах во имя возлюбленной Барчин; '
                     'жемчужина узбекского сказительства (бахши).',
               'en': 'Uzbek oral epic about the heroic warrior Alpomish, his magical steed Boychibor, and his tests to '
                     'win Lady Barchin.'},
  'aliases': ['alpomish', 'алпамыш', 'barchinoy', 'boychibor']},
 {'id': 'lit_emoji_052',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⚰️👶🐎⚔️🏰',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⚰️👶🐎⚔️🏰',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⚰️👶🐎⚔️🏰'},
  'options': {'uz': ['«Alpomish» dostoni',
                     '«Avazxon» dostoni',
                     "«Kuntug'mish» dostoni",
                     "«Go'ro'g'li» dostoni (Go'rda tug'ilgan botir)"],
              'ru': ['«Алпамыш»', '«Авазхан»', '«Кунтугмыш»', '«Гёроглы» (богатырь, рождённый в могиле)'],
              'en': ["'Alpomish'", "'Avazkhan'", "'Kuntugmish'", "'Gorogly' (The Hero Born in the Grave)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Go'ro'g'li» dostoni (Go'rda tug'ilgan botir)",
                     'ru': '«Гёроглы» (богатырь, рождённый в могиле)',
                     'en': "'Gorogly' (The Hero Born in the Grave)"},
  'image_url': None,
  'fun_fact': {'uz': "Go'rda (qabrda) tug'ilib Ravshan deb nom olgan, G'irot laqabli uchar oti bilan Chambil elini "
                     'himoya qilgan afsonaviy adolatli xalq bahodiri.',
               'ru': 'Легендарный богатырь тюркских народов, основатель сказочной страны Чамбил, защитник бедных и '
                     'покровитель справедливости.',
               'en': "Legendary Turkic hero born miraculously in his mother's tomb, defending the egalitarian realm of "
                     'Chambil atop winged stallion Ghiroth.'},
  'aliases': ["go'ro'g'li", 'gorogly', 'гёроглы', 'ravshan']},
 {'id': 'lit_emoji_053',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⛏️⛰️💧👑👰\u200d♀️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '⛏️⛰️💧👑👰\u200d♀️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⛏️⛰️💧👑👰\u200d♀️'},
  'options': {'uz': ['«Farhod va Shirin» (Alisher Navoiy)',
                     '«Layli va Majnun» (Navoiy)',
                     '«Hayrat ul-abror» (Navoiy)',
                     "«Sab'ai sayyor» (Navoiy)"],
              'ru': ['«Фархад и Ширин» (Алишер Навои)',
                     '«Лейли и Меджнун» (Навои)',
                     '«Смятение праведных» (Навои)',
                     '«Семь планет» (Навои)'],
              'en': ["'Farhad and Shirin' (Alisher Navoi)",
                     "'Layla and Majnun' (Navoi)",
                     "'Hayrat al-Abrar' (Navoi)",
                     "'Seven Planets' (Navoi)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Farhod va Shirin» (Alisher Navoiy)',
                     'ru': '«Фархад и Ширин» (Алишер Навои)',
                     'en': "'Farhad and Shirin' (Alisher Navoi)"},
  'image_url': None,
  'fun_fact': {'uz': "Xitoy hoqonining o'g'li Farhod Arman eli malikasi Shirin sevgisi yo'lida Bisotun tog'ini teshib "
                     'ariq qaziydi; Navoiy uni mehnatsevar va olijanob qahramon qilgan.',
               'ru': 'Вторая поэма «Хамсы» Навои: китайский царевич Фархад прорубает канал сквозь гранитные скалы ради '
                     'любви к армянской красавице Ширин.',
               'en': "Second epic poem of Navoi's Khamsa, portraying prince Farhad carving a canal through granite "
                     'cliffs for love of Princess Shirin.'},
  'aliases': ['farhod va shirin', 'navoiy', 'фархад и ширин', 'farhad and shirin']},
 {'id': 'lit_emoji_054',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏜️💔🦁🦌📿',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏜️💔🦁🦌📿',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏜️💔🦁🦌📿'},
  'options': {'uz': ['«Farhod va Shirin» (Navoiy)',
                     '«Layli va Majnun» (Alisher Navoiy)',
                     '«Tohir va Zuhra»',
                     '«Vomiq va Uzro»'],
              'ru': ['«Фархад и Ширин» (Навои)',
                     '«Лейли и Меджнун» (Алишер Навои)',
                     '«Тахир и Зухра»',
                     '«Вамик и Азра»'],
              'en': ["'Farhad and Shirin' (Navoi)",
                     "'Layla and Majnun' (Alisher Navoi)",
                     "'Tohir and Zuhra'",
                     "'Vomiq and Uzro'"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Layli va Majnun» (Alisher Navoiy)',
                     'ru': '«Лейли и Меджнун» (Алишер Навои)',
                     'en': "'Layla and Majnun' (Alisher Navoi)"},
  'image_url': None,
  'fun_fact': {'uz': "Qaysning Layliga bo'lgan cheksiz muhabbati uni Majnun (ishqdan telba) qilib sahroga olib ketadi; "
                     "u yerda yovvoyi kiyiklar va sherlar unga hamroh bo'ladi.",
               'ru': 'Классическая восточная поэма о безответной любви Кайса к Лейли, заставившей его скитаться по '
                     'пустыне в окружении диких зверей.',
               'en': "Navoi's lyrical epic of Qays driven to holy madness by his unattainable love for Layla, "
                     'wandering the desert among beasts.'},
  'aliases': ['layli va majnun', 'navoiy', 'лейли и меджнун', 'layla and majnun']},
 {'id': 'lit_emoji_055',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🦅🦜🕊️🪶👑',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🦅🦜🕊️🪶👑',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🦅🦜🕊️🪶👑'},
  'options': {'uz': ['«Hayrat ul-abror» (Navoiy)',
                     '«Mahbub ul-qulub» (Navoiy)',
                     '«Lison ut-tayr» / «Qushlar tili» (Alisher Navoiy)',
                     '«Mantiq ut-tayr» (Farididdin Attor)'],
              'ru': ['«Смятение праведных» (Навои)',
                     '«Возлюбленный сердец» (Навои)',
                     '«Язык птиц» / «Лисон ут-тайр» (Алишер Навои)',
                     '«Беседа птиц» (Аттар)'],
              'en': ["'Hayrat al-Abrar' (Navoi)",
                     "'Mahbub al-Qulub' (Navoi)",
                     "'The Language of the Birds' (Alisher Navoi)",
                     "'The Conference of the Birds' (Attar)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Lison ut-tayr» / «Qushlar tili» (Alisher Navoiy)',
                     'ru': '«Язык птиц» / «Лисон ут-тайр» (Алишер Навои)',
                     'en': "'The Language of the Birds' (Alisher Navoi)"},
  'image_url': None,
  'fun_fact': {'uz': "Qushlar o'zlariga podshoh topish uchun Hudhud yetakchiligida Simurg'ni izlab 7 ta vodiy (talab, "
                     "ishq, ma'rifat...)dan o'tadilar va oxirida o'zlari 'si-murg'' (30 qush) ekanini anglaydilar.",
               'ru': 'Суфийская аллегорическая поэма Навои: птицы летят через семь долин в поисках царя Симурга, пока '
                     'не понимают, что Симург («тридцать птиц») живёт в них самих.',
               'en': 'Sufi allegorical epic in which thirty surviving birds traverse seven perilous valleys to '
                     'discover that the divine Simurgh is within themselves.'},
  'aliases': ['lison ut-tayr', 'qushlar tili', 'navoiy', 'язык птиц', 'language of the birds']},
 {'id': 'lit_emoji_056',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👑🐎✍️🌺🇮🇳',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👑🐎✍️🌺🇮🇳',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👑🐎✍️🌺🇮🇳'},
  'options': {'uz': ['«Humoyunnoma» (Gulbadanbegim)',
                     '«Zafarnoma» (Sharafiddin Ali Yazdiy)',
                     '«Tarixi Rashidiy» (Mirzo Haydar)',
                     '«Boburnoma» (Zahiriddin Muhammad Bobur)'],
              'ru': ['«Хумаюн-наме» (Гульбадан-бегим)',
                     '«Зафар-наме» (Шарафаддин Али Язди)',
                     '«Тарих-и Рашиди» (Мирза Хайдар)',
                     '«Бабур-наме» (Захириддин Мухаммад Бабур)'],
              'en': ["'Humayunnama' (Gulbadan Begum)",
                     "'Zafarnama' (Sharaf ad-Din Ali Yazdi)",
                     "'Tarikh-i Rashidi' (Mirza Muhammad Haidar)",
                     "'Baburnama' (Zahiriddin Muhammad Babur)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Boburnoma» (Zahiriddin Muhammad Bobur)',
                     'ru': '«Бабур-наме» (Захириддин Мухаммад Бабур)',
                     'en': "'Baburnama' (Zahiriddin Muhammad Babur)"},
  'image_url': None,
  'fun_fact': {'uz': "Bobur Mirzoning o'z hayoti, Farg'ona, Kobul va Hindistondagi harbiy yurishlari, tabiat va "
                     'xalqlar madaniyati haqida yozgan betakror memuar asari.',
               'ru': 'Бесценные мемуары основателя империи Великих Моголов Бабура, написанные живым чагатайским '
                     'тюркским языком о географии, фауне и людях Азии.',
               'en': 'The pioneering autobiographical memoirs of Mughal Emperor Babur describing flora, fauna, '
                     'campaigns, and people of Central and South Asia.'},
  'aliases': ['boburnoma', 'bobur', 'бабур-наме', 'бабур', 'baburnama']},
 {'id': 'lit_emoji_057',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🚪🏠💔🎖️🌾',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🚪🏠💔🎖️🌾',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🚪🏠💔🎖️🌾'},
  'options': {'uz': ["«Ikki eshik orasi» (O'tkir Hoshimov)",
                     "«Dunyoning ishlari» (O'tkir Hoshimov)",
                     '«Ufq» (Said Ahmad)',
                     "«Yulduzlar mangu yonadi» (Tog'ay Murod)"],
              'ru': ['«Между двух дверей» / «Войти и выйти» (Уткир Хашимов)',
                     '«Дела земные» (Хашимов)',
                     '«Горизонт» (Саид Ахмад)',
                     '«Звёзды горят вечно» (Тогай Мурад)'],
              'en': ["'Between Two Doors' (O'tkir Hoshimov)",
                     "'Affairs of this World' (Hoshimov)",
                     "'The Horizon' (Said Ahmad)",
                     "'Stars Burn Forever' (Toghay Murad)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«Ikki eshik orasi» (O'tkir Hoshimov)",
                     'ru': '«Между двух дверей» / «Войти и выйти» (Уткир Хашимов)',
                     'en': "'Between Two Doors' (O'tkir Hoshimov)"},
  'image_url': None,
  'fun_fact': {'uz': 'Kimsan, Robiya, Umar zakovchi va Qora amma kabi qahramonlarning Ikkinchi jahon urushi '
                     'yillaridagi fojiali va murakkab taqdirlari aks ettirilgan roman.',
               'ru': 'Один из лучших романов Хашимова о военном лихолетье, мужестве узбекских женщин в тылу и цене '
                     'человеческой совести.',
               'en': "Hoshimov's sweeping novel depicting ordinary Uzbek villagers facing hardship, love, and tragedy "
                     'during World War II.'},
  'aliases': ['ikki eshik orasi', "o'tkir hoshimov", 'между двух дверей', 'hoshimov']},
 {'id': 'lit_emoji_058',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👵👵👰👰\u200d♀️💥',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👵👵👰👰\u200d♀️💥',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👵👵👰👰\u200d♀️💥'},
  'options': {'uz': ['«Kuyov» (Said Ahmad)',
                     "«Kelinlar qo'zg'oloni» (Said Ahmad)",
                     '«Tobutdan tovush» (Abdulla Qahhor)',
                     '«Temir xotin» (Sharof Boshbekov)'],
              'ru': ['«Жених» (Саид Ахмад)',
                     '«Бунт невесток» (Саид Ахмад)',
                     '«Голос из гроба» (Абдулла Каххар)',
                     '«Железная женщина» (Башбеков)'],
              'en': ["'The Groom' (Said Ahmad)",
                     "'The Revolt of the Daughters-in-Law' (Said Ahmad)",
                     "'Voice from the Grave' (Abdulla Qahhor)",
                     "'Iron Woman' (Sharof Boshbekov)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Kelinlar qo'zg'oloni» (Said Ahmad)",
                     'ru': '«Бунт невесток» (Саид Ахмад)',
                     'en': "'The Revolt of the Daughters-in-Law' (Said Ahmad)"},
  'image_url': None,
  'fun_fact': {'uz': "Qattiqqo'l qaynona Farmon bibi va uning 7 o'g'lining 7 kelini (ayniqsa erkinfikrli Nigora) "
                     "o'rtasidagi munosabatlarni tasvirlagan mashhur komediya.",
               'ru': 'Легендарная узбекская комедия о властной свекрови Фармон-биби и восстании её семи невесток во '
                     'главе с городской невесткой Нигорой.',
               'en': "Said Ahmad's famous comedy play about the matriarch Farmon Bibi ruling her seven sons and "
                     'daughters-in-law until the newest bride rebels.'},
  'aliases': ["kelinlar qo'zg'oloni", 'said ahmad', 'farmon bibi', 'бунт невесток', 'саид ахмад']},
 {'id': 'lit_emoji_059',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐎🌙🏆👴❤️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐎🌙🏆👴❤️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐎🌙🏆👴❤️'},
  'options': {'uz': ["«Oydinda yurgan odamlar» (Tog'ay Murod)",
                     "«Yulduzlar mangu yonadi» (Tog'ay Murod)",
                     "«Ot kishnagan oqshom» (Tog'ay Murod)",
                     '«Chavandoz» (Shukur Xolmirzayev)'],
              'ru': ['«Люди, идущие при луне» (Тогай Мурад)',
                     '«Звёзды горят вечно» (Тогай Мурад)',
                     '«Вечер, когда ржал конь» / «Лошадиное ржание» (Тогай Мурад)',
                     '«Всадник» (Холмирзаев)'],
              'en': ["'People Walking in the Moonlight' (Toghay Murad)",
                     "'Stars Burn Forever' (Toghay Murad)",
                     "'The Evening the Horse Neighed' (Toghay Murad)",
                     "'The Horseman' (Kholmirzaev)"]},
  'correct_index': 2,
  'correct_answer': {'uz': "«Ot kishnagan oqshom» (Tog'ay Murod)",
                     'ru': '«Вечер, когда ржал конь» / «Лошадиное ржание» (Тогай Мурад)',
                     'en': "'The Evening the Horse Neighed' (Toghay Murad)"},
  'image_url': None,
  'fun_fact': {'uz': "Ziyodulla chavandoz va uning sevimli uchar oti Tarlon o'rtasidagi sadoqat, milliy ko'pkari "
                     "(uloq) an'anasi haqidagi betakror dostonmonand qissa.",
               'ru': 'Повесть Тогая Мурада о наезднике Зиядулле и его коне Тарлоне, воспевающая древние традиции '
                     'купкари и узбекскую ментальность.',
               'en': "Toghay Murad's lyrical novella honoring the bond between equestrian Ziyodulla and his champion "
                     'horse Tarlon in traditional kupkari races.'},
  'aliases': ['ot kishnagan oqshom', "tog'ay murod", 'вечер когда ржал конь', 'тогай мурад', 'tarlon']},
 {'id': 'lit_emoji_060',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🪁🇦🇫👦💔🏃\u200d♂️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🪁🇦🇫👦💔🏃\u200d♂️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🪁🇦🇫👦💔🏃\u200d♂️'},
  'options': {'uz': ["«Ming quyosh shu'lasi» (Xolid Husayniy)",
                     "«Tog'lar ham sado berdi» (Xolid Husayniy)",
                     '«Qor» (Orxan Pamuk)',
                     '«Shamol ortidan yugurib» / «Varrak ortidan» (Xolid Husayniy)'],
              'ru': ['«Тысяча сияющих солнц» (Халед Хоссейни)',
                     '«И эхо летит по горам» (Халед Хоссейни)',
                     '«Снег» (Орхан Памук)',
                     '«Бегущий за ветром» (Халед Хоссейни)'],
              'en': ["'A Thousand Splendid Suns' (Khaled Hosseini)",
                     "'And the Mountains Echoed' (Khaled Hosseini)",
                     "'Snow' (Orhan Pamuk)",
                     "'The Kite Runner' (Khaled Hosseini)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Shamol ortidan yugurib» / «Varrak ortidan» (Xolid Husayniy)',
                     'ru': '«Бегущий за ветром» (Халед Хоссейни)',
                     'en': "'The Kite Runner' (Khaled Hosseini)"},
  'image_url': None,
  'fun_fact': {'uz': "Kobullik Amir va uning sadoqatli xizmatkori Hasan do'stligi, xiyonat va oradan yillar o'tib o'z "
                     "gunohini yuvish uchun Afg'onistonga qaytishi haqidagi bestseller.",
               'ru': 'История дружбы двух мальчиков в дореволюционном Кабуле, предательства, эмиграции в США и '
                     'искупления вины спустя десятилетия.',
               'en': 'Amir journeys from California back to Taliban-ruled Afghanistan to atone for betraying his loyal '
                     'childhood friend Hassan.'},
  'aliases': ['shamol ortidan yugurib',
              'xolid husayniy',
              'бегущий за ветром',
              'хоссейни',
              'the kite runner',
              'khaled hosseini']},
 {'id': 'lit_emoji_061',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n☀️🧕🇦🇫💔👩\u200d👧',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n☀️🧕🇦🇫💔👩\u200d👧',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n☀️🧕🇦🇫💔👩\u200d👧'},
  'options': {'uz': ["«Ming quyosh shu'lasi» (Xolid Husayniy)",
                     '«Varrak ortidan» (Xolid Husayniy)',
                     "«Tog'lar ham sado berdi» (Xolid Husayniy)",
                     '«Mening ismim Qirmizi» (Orxan Pamuk)'],
              'ru': ['«Тысяча сияющих солнц» (Халед Хоссейни)',
                     '«Бегущий за ветром» (Халед Хоссейни)',
                     '«И эхо летит по горам» (Халед Хоссейни)',
                     '«Имя мне — Красный» (Орхан Памук)'],
              'en': ["'A Thousand Splendid Suns' (Khaled Hosseini)",
                     "'The Kite Runner' (Khaled Hosseini)",
                     "'And the Mountains Echoed' (Khaled Hosseini)",
                     "'My Name Is Red' (Orhan Pamuk)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«Ming quyosh shu'lasi» (Xolid Husayniy)",
                     'ru': '«Тысяча сияющих солнц» (Халед Хоссейни)',
                     'en': "'A Thousand Splendid Suns' (Khaled Hosseini)"},
  'image_url': None,
  'fun_fact': {'uz': "Afg'oniston urushlari davrida zolim er qo'lida qolgan ikki ayol — Maryam va Layloning bir-biriga "
                     "tayanch bo'lgan sadoqatli do'stligi.",
               'ru': 'Трагическая история дружбы и солидарности двух афганских женщин Мариам и Лейлы на фоне тридцати '
                     'лет войн в Кабуле.',
               'en': "Hosseini's gripping novel of female solidarity in war-torn Kabul between two wives, Mariam and "
                     'Laila, married to the abusive Rasheed.'},
  'aliases': ["ming quyosh shu'lasi", 'xolid husayniy', 'тысяча сияющих солнц', 'a thousand splendid suns']},
 {'id': 'lit_emoji_062',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐑🏜️🇪🇬💎⭐',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐑🏜️🇪🇬💎⭐',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐑🏜️🇪🇬💎⭐'},
  'options': {'uz': ["«Veronika o'lishga qaror qildi» (Paulo Koelo)",
                     '«Alkimyogar» (Paulo Koelo)',
                     "«O'n bir daqiqa» (Paulo Koelo)",
                     "«Payg'ambar» (Xalil Jibron)"],
              'ru': ['«Вероника решает умереть» (Коэльо)',
                     '«Алхимик» (Пауло Коэльо)',
                     '«Одиннадцать минут» (Коэльо)',
                     '«Пророк» (Халиль Джебран)'],
              'en': ["'Veronika Decides to Die' (Paulo Coelho)",
                     "'The Alchemist' (Paulo Coelho)",
                     "'Eleven Minutes' (Paulo Coelho)",
                     "'The Prophet' (Kahlil Gibran)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Alkimyogar» (Paulo Koelo)',
                     'ru': '«Алхимик» (Пауло Коэльо)',
                     'en': "'The Alchemist' (Paulo Coelho)"},
  'image_url': None,
  'fun_fact': {'uz': "Andalusiyalik cho'pon yigit Santyago tushida ko'rgan xazinani qidirib Misr piramidalariga yo'l "
                     "oladi va o'z Taqdirini ro'yobga chiqarish sirini o'rganadi.",
               'ru': 'Испанский пастух Сантьяго отправляется к египетским пирамидам в поисках сокровища, постигая '
                     '«Свою Стезю» и «Душу Мира».',
               'en': 'Andalusian shepherd boy Santiago travels across North Africa to the Egyptian Pyramids in search '
                     'of treasure and his Personal Legend.'},
  'aliases': ['alkimyogar', 'koelo', 'алхимик', 'коэльо', 'the alchemist', 'paulo coelho']},
 {'id': 'lit_emoji_063',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🚣\u200d♂️🐅🌊🦺🐟',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🚣\u200d♂️🐅🌊🦺🐟',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🚣\u200d♂️🐅🌊🦺🐟'},
  'options': {'uz': ['«Chol va dengiz» (Ernest Xeminguey)',
                     '«Robinzon Kruzo» (Daniel Defo)',
                     '«Pining hayoti» (Yann Martel)',
                     "«Dengiz bo'risi» (Jek London)"],
              'ru': ['«Старик и море» (Хемингуэй)',
                     '«Робинзон Крузо» (Дефо)',
                     '«Жизнь Пи» (Янн Мартел)',
                     '«Морской волк» (Джек Лондон)'],
              'en': ["'The Old Man and the Sea' (Hemingway)",
                     "'Robinson Crusoe' (Defoe)",
                     "'Life of Pi' (Yann Martel)",
                     "'The Sea-Wolf' (Jack London)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Pining hayoti» (Yann Martel)',
                     'ru': '«Жизнь Пи» (Янн Мартел)',
                     'en': "'Life of Pi' (Yann Martel)"},
  'image_url': None,
  'fun_fact': {'uz': "Kema halokatidan so'ng Tinch okeanida qutqaruv qayig'ida Richard Parker laqabli ulkan Bengaliya "
                     "yo'lbarsi bilan 227 kun omon qolgan hind yigiti Pi Patel hikoyasi.",
               'ru': 'Индийский юноша Пи Патель выживает в шлюпке посреди океана 227 дней в компании бенгальского '
                     'тигра по кличке Ричард Паркер.',
               'en': "Piscine Molitor 'Pi' Patel survives 227 days adrift on a lifeboat in the Pacific Ocean alongside "
                     'a Bengal tiger named Richard Parker.'},
  'aliases': ['pining hayoti', 'yann martel', 'жизнь пи', 'life of pi', 'richard parker']},
 {'id': 'lit_emoji_064',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🤵\u200d♂️🐴🔫🍝🌹',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🤵\u200d♂️🐴🔫🍝🌹',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🤵\u200d♂️🐴🔫🍝🌹'},
  'options': {'uz': ['«Sitsiliyalik» (Mario Pyuzo)',
                     "«So'nggi don» (Mario Pyuzo)",
                     '«Omerta» (Mario Pyuzo)',
                     "«Cho'qintirgan ota» (Mario Pyuzo)"],
              'ru': ['«Сицилиец» (Марио Пьюзо)',
                     '«Последний дон» (Марио Пьюзо)',
                     '«Омерта» (Марио Пьюзо)',
                     '«Крёстный отец» (Марио Пьюзо)'],
              'en': ["'The Sicilian' (Mario Puzo)",
                     "'The Last Don' (Mario Puzo)",
                     "'Omertà' (Mario Puzo)",
                     "'The Godfather' (Mario Puzo)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Cho'qintirgan ota» (Mario Pyuzo)",
                     'ru': '«Крёстный отец» (Марио Пьюзо)',
                     'en': "'The Godfather' (Mario Puzo)"},
  'image_url': None,
  'fun_fact': {'uz': "Don Vito Korleone boshchiligidagi Nyu-York italyan mafiyasi oilasi va uning o'rnini egallagan "
                     "kenja o'g'il Maykl Korleone tarixi.",
               'ru': 'Криминальная сага 1969 года о клане Корлеоне, власти, семье и превращении героя войны Майкла '
                     'Корлеоне в безжалостного дона мафии.',
               'en': "Mario Puzo's 1969 mafia saga chronicling the Corleone family and Michael Corleone's tragic "
                     'ascent as the new Don.'},
  'aliases': ["cho'qintirgan ota", 'mario pyuzo', 'крёстный отец', 'марио пьюзо', 'the godfather', 'vito corleone']},
 {'id': 'lit_emoji_065',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👃🧴💐🔪🇫🇷',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👃🧴💐🔪🇫🇷',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👃🧴💐🔪🇫🇷'},
  'options': {'uz': ['«Atirchi: Bir qotil tarixi» (Patrik Zyuskind)',
                     '«Kabutar» (Patrik Zyuskind)',
                     '«Mister Sommerning hikoyasi» (Zyuskind)',
                     '«Dorian Greyning portreti» (Uayld)'],
              'ru': ['«Парфюмер. История одного убийцы» (Патрик Зюскинд)',
                     '«Голубка» (Патрик Зюскинд)',
                     '«Повесть о господине Зоммере» (Зюскинд)',
                     '«Портрет Дориана Грея» (Уайльд)'],
              'en': ["'Perfume: The Story of a Murderer' (Patrick Süskind)",
                     "'The Pigeon' (Patrick Süskind)",
                     "'The Story of Mr Sommer' (Süskind)",
                     "'The Picture of Dorian Gray' (Wilde)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Atirchi: Bir qotil tarixi» (Patrik Zyuskind)',
                     'ru': '«Парфюмер. История одного убийцы» (Патрик Зюскинд)',
                     'en': "'Perfume: The Story of a Murderer' (Patrick Süskind)"},
  'image_url': None,
  'fun_fact': {'uz': "G'ayritabiiy hid bilish qobiliyatiga ega, ammo o'z hidi bo'lmagan Jan-Batist Grenuy mukammal "
                     "ifor yaratish uchun 25 nafar qizni o'ldiradi.",
               'ru': 'Жан-Батист Гренуй, родившийся на рыбном рынке в Париже без собственного запаха, создаёт аромат '
                     'абсолютной власти над любовью людей.',
               'en': 'Born with superhuman olfactory senses but no body odor of his own, Jean-Baptiste Grenouille '
                     'murders young women to distill the ultimate scent.'},
  'aliases': ['atirchi', 'zyuskind', 'парфюмер', 'зюскинд', 'perfume', 'patrick suskind']},
 {'id': 'lit_emoji_066',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🖼️🗝️🏛️🩸🔍',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🖼️🗝️🏛️🩸🔍',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🖼️🗝️🏛️🩸🔍'},
  'options': {'uz': ['«Farishtalar va shaytonlar» (Den Braun)',
                     '«Da Vinchi siri» (Den Braun)',
                     '«Infernolar» (Den Braun)',
                     "«Yo'qotilgan ramz» (Den Braun)"],
              'ru': ['«Ангелы и демоны» (Дэн Браун)',
                     '«Код да Винчи» (Дэн Браун)',
                     '«Инферно» (Дэн Браун)',
                     '«Утраченный символ» (Дэн Браун)'],
              'en': ["'Angels & Demons' (Dan Brown)",
                     "'The Da Vinci Code' (Dan Brown)",
                     "'Inferno' (Dan Brown)",
                     "'The Lost Symbol' (Dan Brown)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Da Vinchi siri» (Den Braun)',
                     'ru': '«Код да Винчи» (Дэн Браун)',
                     'en': "'The Da Vinci Code' (Dan Brown)"},
  'image_url': None,
  'fun_fact': {'uz': "Garvardlik simvolshunos Robert Lengdon Luvrda sodir bo'lgan qotillik va Leonardo da Vinchining "
                     "'Sirli kecha' asaridagi Muqaddas Graal sirini fosh etadi.",
               'ru': 'Профессор Роберт Лэнгдон и криптограф Софи Неве разгадывают шифры Леонардо да Винчи о тайне '
                     'священного Грааля и Марии Магдалины.',
               'en': 'Symbologist Robert Langdon investigates a murder in the Louvre, decoding anagrams hidden in '
                     "Leonardo da Vinci's paintings."},
  'aliases': ['da vinchi siri', 'den braun', 'код да винчи', 'дэн браун', 'the da vinci code', 'dan brown']},
 {'id': 'lit_emoji_067',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🇻🇦⚛️🔥🗡️⛪',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🇻🇦⚛️🔥🗡️⛪',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🇻🇦⚛️🔥🗡️⛪'},
  'options': {'uz': ['«Da Vinchi siri» (Den Braun)',
                     '«Inferno» (Den Braun)',
                     '«Farishtalar va shaytonlar» (Den Braun)',
                     '«Kelib chiqish» (Den Braun)'],
              'ru': ['«Код да Винчи» (Дэн Браун)',
                     '«Инферно» (Дэн Браун)',
                     '«Ангелы и демоны» (Дэн Браун)',
                     '«Происхождение» (Дэн Браун)'],
              'en': ["'The Da Vinci Code' (Dan Brown)",
                     "'Inferno' (Dan Brown)",
                     "'Angels & Demons' (Dan Brown)",
                     "'Origin' (Dan Brown)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Farishtalar va shaytonlar» (Den Braun)',
                     'ru': '«Ангелы и демоны» (Дэн Браун)',
                     'en': "'Angels & Demons' (Dan Brown)"},
  'image_url': None,
  'fun_fact': {'uz': "Illyuminatlar maxfiy birodarligi CERN laboratoriyasidan antimateriyani o'g'irlab, Rim Papasi "
                     'saylovi paytida Vatikanni portlatish bilan tahdid qiladi.',
               'ru': 'Роберт Лэнгдон спасает Ватикан от взрыва украденного контейнера с антиматерией по следам '
                     'древнего тайного ордена иллюминатов.',
               'en': 'Robert Langdon follows the Path of Illumination across Rome to stop an antimatter bomb from '
                     'obliterating the Vatican conclave.'},
  'aliases': ['farishtalar va shaytonlar', 'den braun', 'ангелы и демоны', 'angels and demons']},
 {'id': 'lit_emoji_068',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏹🎯🐦🔥🌲',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏹🎯🐦🔥🌲',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏹🎯🐦🔥🌲'},
  'options': {'uz': ['«Labirintda yuguruvchi» (Jeyms Deshner)',
                     '«Divergent» (Veronika Rot)',
                     '«Pashshalar tangrisi» (Uilyam Golding)',
                     "«Ochlik o'yinlari» (Syuzen Kollinz)"],
              'ru': ['«Бегущий в лабиринте» (Джеймс Дэшнер)',
                     '«Дивергент» (Вероника Рот)',
                     '«Повелитель мух» (Голдинг)',
                     '«Голодные игры» (Сьюзен Коллинз)'],
              'en': ["'The Maze Runner' (James Dashner)",
                     "'Divergent' (Veronica Roth)",
                     "'Lord of the Flies' (Golding)",
                     "'The Hunger Games' (Suzanne Collins)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Ochlik o'yinlari» (Syuzen Kollinz)",
                     'ru': '«Голодные игры» (Сьюзен Коллинз)',
                     'en': "'The Hunger Games' (Suzanne Collins)"},
  'image_url': None,
  'fun_fact': {'uz': "Panem davlatining Kapitoliy poytaxti 12 ta distriktdan qiz va o'g'il bolalarni tirik qolish "
                     'uchun shafqatsiz tele-shou maydonida jangga majburlaydi.',
               'ru': 'Китнисс Эвердин вызывается добровольцем на ежегодные смертельные игры дистриктов вместо своей '
                     'младшей сестры Прим.',
               'en': "Katniss Everdeen volunteers as tribute for her sister Prim in Panem's televised "
                     'fight-to-the-death tournament.'},
  'aliases': ["ochlik o'yinlari", 'голодные игры', 'hunger games', 'katniss everdeen']},
 {'id': 'lit_emoji_069',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👘🌸💄🎎🇯🇵',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👘🌸💄🎎🇯🇵',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👘🌸💄🎎🇯🇵'},
  'options': {'uz': ['«Geyshaning esdaliklari» (Artur Golden)',
                     "«Norveg o'rmoni» (Murakami)",
                     '«Choyxona sirlari» (Okakura)',
                     '«Kokoro» (Natsume Soseki)'],
              'ru': ['«Мемуары гейши» (Артур Голден)',
                     '«Норвежский лес» (Мураками)',
                     '«Книга чая» (Окакура)',
                     '«Сердце» (Нацумэ Сосэки)'],
              'en': ["'Memoirs of a Geisha' (Arthur Golden)",
                     "'Norwegian Wood' (Murakami)",
                     "'The Book of Tea' (Okakura)",
                     "'Kokoro' (Natsume Sōseki)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Geyshaning esdaliklari» (Artur Golden)',
                     'ru': '«Мемуары гейши» (Артур Голден)',
                     'en': "'Memoirs of a Geisha' (Arthur Golden)"},
  'image_url': None,
  'fun_fact': {'uz': "Kichik qashshoq qishloqdan sotib olingan ko'zlari havorang Chiyo Kioto shahrida mashhur Sayuri "
                     "nomli geyshaga aylanish mashaqqatli yo'lini bosib o'tadi.",
               'ru': 'История девочки Чио с редкими серо-голубыми глазами, проданной в Киото и ставшей легендарной '
                     'гейшей Саюри.',
               'en': 'Chiyo is sold into an okiya in Kyoto, enduring harsh training to become the celebrated geisha '
                     'Sayuri amid pre-war and post-war Japan.'},
  'aliases': ['geyshaning esdaliklari', 'мемуары гейши', 'memoirs of a geisha', 'sayuri']},
 {'id': 'lit_emoji_070',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n⚡👓🪄🦉🏰',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n⚡👓🪄🦉🏰',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n⚡👓🪄🦉🏰'},
  'options': {'uz': ['«Uzuklar hukmdori» (Tolkin)',
                     '«Garri Potter va falsafiy tosh» (J.K. Rouling)',
                     '«Narniya yilnomalari» (Lyuis)',
                     '«Persi Jekson» (Rik Riordan)'],
              'ru': ['«Властелин колец» (Толкин)',
                     '«Гарри Поттер и философский камень» (Дж. К. Роулинг)',
                     '«Хроники Нарнии» (Льюис)',
                     '«Перси Джексон» (Рик Риордан)'],
              'en': ["'The Lord of the Rings' (Tolkien)",
                     "'Harry Potter and the Philosopher's Stone' (J.K. Rowling)",
                     "'The Chronicles of Narnia' (Lewis)",
                     "'Percy Jackson' (Rick Riordan)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Garri Potter va falsafiy tosh» (J.K. Rouling)',
                     'ru': '«Гарри Поттер и философский камень» (Дж. К. Роулинг)',
                     'en': "'Harry Potter and the Philosopher's Stone' (J.K. Rowling)"},
  'image_url': None,
  'fun_fact': {'uz': "11 yoshida sehrgar ekanini bilib Hogvarts maktabiga qabul qilingan o'sha peshonasida "
                     'chaqmoqsimon chandiqli yetim bola haqidagi roman.',
               'ru': 'Первая книга всемирной саги о мальчике, который выжил, дружбе с Роном и Гермионой и борьбе с '
                     'лордом Волан-де-Мортом.',
               'en': 'On his eleventh birthday, orphan Harry Potter discovers he is a wizard and attends Hogwarts '
                     'School of Witchcraft and Wizardry.'},
  'aliases': ['garri potter', 'harry potter', 'гарри поттер', 'rouling', 'philosophers stone']},
 {'id': 'lit_emoji_071',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🚪🧥❄️🦁🧙\u200d♀️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🚪🧥❄️🦁🧙\u200d♀️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🚪🧥❄️🦁🧙\u200d♀️'},
  'options': {'uz': ['«Kanzas sehrgari» (Frenk Baum)',
                     '«Piter Pen» (Jeyms Barri)',
                     '«Arslon, jodugar va javon» (K.S. Lyuis)',
                     "«Alisa mo''jizalar mamlakatida» (Kerroll)"],
              'ru': ['«Волшебник Изумрудного города» (Волков)',
                     '«Питер Пэн» (Барри)',
                     '«Лев, колдунья и платяной шкаф» (К. С. Льюис)',
                     '«Алиса в Стране чудес» (Кэрролл)'],
              'en': ["'The Wizard of Oz' (Baum)",
                     "'Peter Pan' (Barrie)",
                     "'The Lion, the Witch and the Wardrobe' (C.S. Lewis)",
                     "'Alice in Wonderland' (Carroll)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Arslon, jodugar va javon» (K.S. Lyuis)',
                     'ru': '«Лев, колдунья и платяной шкаф» (К. С. Льюис)',
                     'en': "'The Lion, the Witch and the Wardrobe' (C.S. Lewis)"},
  'image_url': None,
  'fun_fact': {'uz': "To'rt aka-uka va opa-singil (Piter, Syuzan, Edmund, Lyusi) eski javon orqali doimiy qish hukm "
                     'surgan Narniya mamlakatiga tushib qoladilar.',
               'ru': 'Четверо детей через платяной шкаф попадают в заколдованную страну Нарнию, где царит вечная зима '
                     'Белой Колдуньи.',
               'en': 'Four siblings step through a wardrobe into Narnia, a frozen land held under perpetual winter by '
                     'the White Witch.'},
  'aliases': ['arslon jodugar va javon',
              'narniya',
              'лев колдунья и платяной шкаф',
              'хроники нарнии',
              'lion witch and wardrobe']},
 {'id': 'lit_emoji_072',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👧🏚️🏰🔥💍',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👧🏚️🏰🔥💍',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👧🏚️🏰🔥💍'},
  'options': {'uz': ['«Momaqaldiroqli dovon» (Emili Bronte)',
                     "«G'urur va andisha» (Jeyn Ostin)",
                     '«Emma» (Jeyn Ostin)',
                     '«Jeyn Eyr» (Sharlotta Bronte)'],
              'ru': ['«Грозовой перевал» (Эмили Бронте)',
                     '«Гордость и предубеждение» (Джейн Остин)',
                     '«Эмма» (Джейн Остин)',
                     '«Джейн Эйр» (Шарлотта Бронте)'],
              'en': ["'Wuthering Heights' (Emily Brontë)",
                     "'Pride and Prejudice' (Jane Austen)",
                     "'Emma' (Jane Austen)",
                     "'Jane Eyre' (Charlotte Brontë)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Jeyn Eyr» (Sharlotta Bronte)',
                     'ru': '«Джейн Эйр» (Шарлотта Бронте)',
                     'en': "'Jane Eyre' (Charlotte Brontë)"},
  'image_url': None,
  'fun_fact': {'uz': "Lovud maktabida o'sgan yetim qiz Jeyn Eyr Tornfild saroyida murabbiy bo'lib ishlaydi va saroy "
                     "egasi mister Rochesterning yashirin siri bilan to'qnashadi.",
               'ru': 'История гувернантки-сироты Джейн Эйр, полюбившей мистера Рочестера и узнавшей тайну его безумной '
                     'жены на чердаке.',
               'en': 'Orphan Jane Eyre takes a governess post at Thornfield Hall, falling for Edward Rochester before '
                     'discovering a mad wife locked in the attic.'},
  'aliases': ['jeyn eyr', 'sharlotta bronte', 'джейн эйр', 'jane eyre']},
 {'id': 'lit_emoji_073',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏚️💨⛈️🖤🪦',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏚️💨⛈️🖤🪦',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏚️💨⛈️🖤🪦'},
  'options': {'uz': ['«Momaqaldiroqli dovon» (Emili Bronte)',
                     '«Jeyn Eyr» (Sharlotta Bronte)',
                     "«G'urur va andisha» (Jeyn Ostin)",
                     '«Rebekka» (Dafna dyu Morye)'],
              'ru': ['«Грозовой перевал» (Эмили Бронте)',
                     '«Джейн Эйр» (Шарлотта Бронте)',
                     '«Гордость и предубеждение» (Джейн Остин)',
                     '«Ребекка» (Дафна дю Морье)'],
              'en': ["'Wuthering Heights' (Emily Brontë)",
                     "'Jane Eyre' (Charlotte Brontë)",
                     "'Pride and Prejudice' (Jane Austen)",
                     "'Rebecca' (Daphne du Maurier)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Momaqaldiroqli dovon» (Emili Bronte)',
                     'ru': '«Грозовой перевал» (Эмили Бронте)',
                     'en': "'Wuthering Heights' (Emily Brontë)"},
  'image_url': None,
  'fun_fact': {'uz': "Yorkshir botqoqliklaridagi Xitklif va Ketrin Ernshoning azobli, rashk va qasosga to'la ehtirosli "
                     'sevgisi.',
               'ru': 'Мрачная сага о разрушительной страсти и мести найдёныша Хитклиффа на вересковых пустошах '
                     'Йоркшира.',
               'en': 'A tempestuous tale of passionate, destructive love and multi-generational revenge between '
                     'Heathcliff and Catherine Earnshaw.'},
  'aliases': ['momaqaldiroqli dovon', 'emili bronte', 'грозовой перевал', 'wuthering heights', 'heathcliff']},
 {'id': 'lit_emoji_074',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n💌💃🎩💃🇬🇧',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n💌💃🎩💃🇬🇧',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n💌💃🎩💃🇬🇧'},
  'options': {'uz': ['«Aql va hislar» (Jeyn Ostin)',
                     "«G'urur va andisha» (Jeyn Ostin)",
                     '«Emma» (Jeyn Ostin)',
                     '«Jeyn Eyr» (Sharlotta Bronte)'],
              'ru': ['«Чувство и чувствительность» (Джейн Остин)',
                     '«Гордость и предубеждение» (Джейн Остин)',
                     '«Эмма» (Джейн Остин)',
                     '«Джейн Эйр» (Бронте)'],
              'en': ["'Sense and Sensibility' (Jane Austen)",
                     "'Pride and Prejudice' (Jane Austen)",
                     "'Emma' (Jane Austen)",
                     "'Jane Eyre' (Brontë)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«G'urur va andisha» (Jeyn Ostin)",
                     'ru': '«Гордость и предубеждение» (Джейн Остин)',
                     'en': "'Pride and Prejudice' (Jane Austen)"},
  'image_url': None,
  'fun_fact': {'uz': "Elizabet Bennetning o'tkir tili va mag'rur aristokrat mister Darsining g'ururi hamda "
                     "bir-birlariga bo'lgan samimiy muhabbati.",
               'ru': 'Умная и независимая Элизабет Беннет преодолевает предвзятость, а богатый мистер Дарси смиряет '
                     'свою сословную гордость.',
               'en': 'Elizabeth Bennet clashes with proud, wealthy Fitzwilliam Darcy, both overcoming vanity and '
                     'prejudice to find true affection.'},
  'aliases': ["g'urur va andisha", 'jeyn ostin', 'гордость и предубеждение', 'pride and prejudice', 'mr darcy']},
 {'id': 'lit_emoji_075',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧠❤️👭💔💍',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🧠❤️👭💔💍',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧠❤️👭💔💍'},
  'options': {'uz': ["«G'urur va andisha» (Jeyn Ostin)",
                     '«Mansfild-park» (Jeyn Ostin)',
                     '«Aql va hislar» (Jeyn Ostin)',
                     '«Shimoliy abbatlik» (Jeyn Ostin)'],
              'ru': ['«Гордость и предубеждение» (Джейн Остин)',
                     '«Мэнсфилд-парк» (Джейн Остин)',
                     '«Разум и чувства» / «Чувство и чувствительность» (Джейн Остин)',
                     '«Нортенгерское аббатство» (Джейн Остин)'],
              'en': ["'Pride and Prejudice' (Jane Austen)",
                     "'Mansfield Park' (Jane Austen)",
                     "'Sense and Sensibility' (Jane Austen)",
                     "'Northanger Abbey' (Jane Austen)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Aql va hislar» (Jeyn Ostin)',
                     'ru': '«Разум и чувства» / «Чувство и чувствительность» (Джейн Остин)',
                     'en': "'Sense and Sensibility' (Jane Austen)"},
  'image_url': None,
  'fun_fact': {'uz': "Ikki opa-singil — aql va sabr timsoli Elinor hamda jo'shqin hissiyot timsoli Marianna "
                     'Deshvudning sevgi va turmush sinovlari.',
               'ru': 'Роман 1811 года о двух сёстрах Дэшвуд: рассудительной Элинор («Разум») и страстной романтичной '
                     'Марианне («Чувства»).',
               'en': "Austen's 1811 novel contrasting the reserved, rational Elinor Dashwood with her romantic, "
                     'emotional sister Marianne.'},
  'aliases': ['aql va hislar', 'jeyn ostin', 'разум и чувства', 'sense and sensibility']},
 {'id': 'lit_emoji_076',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🕶️🔫🥃⛓️⚖️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🕶️🔫🥃⛓️⚖️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🕶️🔫🥃⛓️⚖️'},
  'options': {'uz': ['«Murdalar gapirmaydilar» (Tohir Malik)',
                     '«Ufq» (Said Ahmad)',
                     '«Chinor» (Asqad Muxtor)',
                     '«Shaytanat» (Tohir Malik)'],
              'ru': ['«Мертвецы молчат» (Малик)',
                     '«Горизонт» (Саид Ахмад)',
                     '«Чинар» (Аскад Мухтар)',
                     '«Шайтанат» (Тохир Малик)'],
              'en': ["'The Dead Keep Silent' (Malik)",
                     "'The Horizon' (Said Ahmad)",
                     "'The Plane Tree' (Mukhtar)",
                     "'Shaytanat' (Tohir Malik)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Shaytanat» (Tohir Malik)',
                     'ru': '«Шайтанат» (Тохир Малик)',
                     'en': "'Shaytanat' (Tohir Malik)"},
  'image_url': None,
  'fun_fact': {'uz': 'Asadbekning jinoiy dunyodagi saltanati, Chuvrindi va Elchin fojiasi hamda gunohning shafqatsiz '
                     "badali aks etgan o'zbek detektivi.",
               'ru': 'Многосерийная криминальная сага о теневом авторитете Асадбеке, борьбе преступных группировок и '
                     'неотвратимой расплате за содеянное.',
               'en': 'Iconic Uzbek crime drama centering on mafia boss Asadbek and the corrupting web of retribution '
                     'and underworld justice.'},
  'aliases': ['shaytanat', 'tohir malik', 'asadbek', 'шайтанат', 'тохир малик']},
 {'id': 'lit_emoji_077',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👑🔭🌌⚔️🇮🇳',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👑🔭🌌⚔️🇮🇳',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👑🔭🌌⚔️🇮🇳'},
  'options': {'uz': ['«Yulduzli tunlar» (Pirimqul Qodirov)',
                     '«Avlodlar dovoni» (Pirimqul Qodirov)',
                     "«Qutlug' qon» (Oybek)",
                     '«Navoiy» romani (Oybek)'],
              'ru': ['«Звёзды ночи» / «Бабур» (Пиримкул Кадыров)',
                     '«Перевал поколений» (Кадыров)',
                     '«Священная кровь» (Айбек)',
                     '«Навои» (Айбек)'],
              'en': ["'Starry Nights' / 'Babur' (Pirimqul Qodirov)",
                     "'Pass of Generations' (Qodirov)",
                     "'Sacred Blood' (Oybek)",
                     "'Navoi' (Oybek)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Yulduzli tunlar» (Pirimqul Qodirov)',
                     'ru': '«Звёзды ночи» / «Бабур» (Пиримкул Кадыров)',
                     'en': "'Starry Nights' / 'Babur' (Pirimqul Qodirov)"},
  'image_url': None,
  'fun_fact': {'uz': "Bobur Mirzoning 12 yoshida Andijon taxtiga o'tirishi, Samarqand uchun janglari, vatandan ayri "
                     "tushib Hindistonda ulug' davlat qurishi tarixi.",
               'ru': 'Исторический роман о Захириддине Мухаммаде Бабуре, его полководческом гении, поэтической душе и '
                     'тоске по родной Фергане.',
               'en': 'Epic biographical novel chronicling Babur from his boyhood accession in Andijan to establishing '
                     'the Mughal Empire in Hindustan.'},
  'aliases': ['yulduzli tunlar', 'pirimqul qodirov', 'bobur romani', 'звёздные ночи', 'starry nights']},
 {'id': 'lit_emoji_078',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🩸🌾🐴💰💔',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🩸🌾🐴💰💔',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🩸🌾🐴💰💔'},
  'options': {'uz': ['«Navoiy» (Oybek)', "«Qutlug' qon» (Oybek)", "«O'tkan kunlar» (Qodiriy)", '«Ufq» (Said Ahmad)'],
              'ru': ['«Навои» (Айбек)',
                     '«Священная кровь» (Айбек)',
                     '«Минувшие дни» (Кадыри)',
                     '«Горизонт» (Саид Ахмад)'],
              'en': ["'Navoi' (Oybek)",
                     "'Sacred Blood' (Oybek)",
                     "'Bygone Days' (Qadiri)",
                     "'The Horizon' (Said Ahmad)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Qutlug' qon» (Oybek)", 'ru': '«Священная кровь» (Айбек)', 'en': "'Sacred Blood' (Oybek)"},
  'image_url': None,
  'fun_fact': {'uz': "Kambag'al botir yigit Yo'lchi, uning sevgilisi Gulnor va boyvachcha Mirzakarimboy zulmiga qarshi "
                     "1916 yilgi xalq qo'zg'oloni.",
               'ru': 'Роман Айбека о бедном батраке Юлчи, его любви к Гульнар и народном восстании 1916 года в '
                     'Туркестане.',
               'en': "Oybek's 1940 classic following farm laborer Yo'lchi, beautiful Gulnor, and the explosive 1916 "
                     'anti-colonial uprising in Central Asia.'},
  'aliases': ["qutlug' qon", 'oybek', 'священная кровь', 'айбек', "yo'lchi", 'gulnor']},
 {'id': 'lit_emoji_079',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐪🚂🛰️💀🏜️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐪🚂🛰️💀🏜️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐪🚂🛰️💀🏜️'},
  'options': {'uz': ['«Oq kema» (Aytmatov)',
                     '«Kunda» (Aytmatov)',
                     '«Asrga tatigulik kun» (Chingiz Aytmatov)',
                     '«Jamila» (Aytmatov)'],
              'ru': ['«Белый пароход» (Айтматов)',
                     '«Плаха» (Айтматов)',
                     '«И дольше века длится день» (Чингиз Айтматов)',
                     '«Джамиля» (Айтматов)'],
              'en': ["'The White Ship' (Aitmatov)",
                     "'The Scaffold' (Aitmatov)",
                     "'The Day Lasts More Than a Hundred Years' (Chingiz Aitmatov)",
                     "'Jamila' (Aitmatov)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Asrga tatigulik kun» (Chingiz Aytmatov)',
                     'ru': '«И дольше века длится день» (Чингиз Айтматов)',
                     'en': "'The Day Lasts More Than a Hundred Years' (Chingiz Aitmatov)"},
  'image_url': None,
  'fun_fact': {'uz': "Bo'ronli bekati temiryo'lchisi Yedigey do'sti Qozonqopni qadimiy Ona-Beyit qabristoniga dafn "
                     'etishga borishi, manqurt afsonasi va kosmik operatsiya.',
               'ru': 'Едигей хоронит старого друга Казангапа на кладбище Ана-Бейит; роман соединяет древнюю легенду о '
                     'манкурте с фантастическим космическим сюжетом.',
               'en': 'Yedigei leads a camel funeral procession across the Kazakh steppe to the ancestral Ana-Beyit '
                     'cemetery, blending folklore with sci-fi.'},
  'aliases': ['asrga tatigulik kun', 'aytmatov', 'и дольше века длится день', 'айтматов', 'mankurt']},
 {'id': 'lit_emoji_080',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🚢🦌👦👴🌊',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🚢🦌👦👴🌊',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🚢🦌👦👴🌊'},
  'options': {'uz': ['«Dengiz yoqalab chopayotgan olapar» (Aytmatov)',
                     '«Erta qaytgan turnalar» (Aytmatov)',
                     '«Birinchi muallim» (Aytmatov)',
                     '«Oq kema» (Chingiz Aytmatov)'],
              'ru': ['«Пегий пёс, бегущий краем моря» (Айтматов)',
                     '«Ранние журавли» (Айтматов)',
                     '«Первый учитель» (Айтматов)',
                     '«Белый пароход» (Чингиз Айтматов)'],
              'en': ["'Piebald Dog' (Aitmatov)",
                     "'Early Cranes' (Aitmatov)",
                     "'The First Teacher' (Aitmatov)",
                     "'The White Ship' / 'The White Steamship' (Chingiz Aitmatov)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Oq kema» (Chingiz Aytmatov)',
                     'ru': '«Белый пароход» (Чингиз Айтматов)',
                     'en': "'The White Ship' / 'The White Steamship' (Chingiz Aitmatov)"},
  'image_url': None,
  'fun_fact': {'uz': "Yetti yoshli bolakay, uning mehridaryo bobosi Mo'min chol, Shoxdor ona kiyik afsonasi va "
                     "Isiqko'l bo'ylab suzib o'tuvchi chiroyli Oq kema.",
               'ru': 'Чистая сказка семилетнего мальчика о священной Рогатой матери-оленихе и мечта уплыть рыбой к '
                     'далёкому белому пароходу.',
               'en': "A boy lives isolated with his grandfather Mo'mun in the forest, believing in the sacred Horned "
                     'Mother Deer until brutal poaching destroys his world.'},
  'aliases': ['oq kema', 'aytmatov', 'белый пароход', 'айтматов', 'the white ship']},
 {'id': 'lit_emoji_081',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐺👶🚂🩸🏜️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐺👶🚂🩸🏜️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐺👶🚂🩸🏜️'},
  'options': {'uz': ['«Kunda» / «Qiyomat» (Chingiz Aytmatov)',
                     '«Asrga tatigulik kun» (Aytmatov)',
                     '«Oq kema» (Aytmatov)',
                     '«Sarvqomat dilbarim» (Aytmatov)'],
              'ru': ['«Плаха» (Чингиз Айтматов)',
                     '«И дольше века длится день» (Айтматов)',
                     '«Белый пароход» (Айтматов)',
                     '«Тополёк мой в красной косынке» (Айтматов)'],
              'en': ["'The Scaffold' / 'Plakha' (Chingiz Aitmatov)",
                     "'The Day Lasts More Than a Hundred Years' (Aitmatov)",
                     "'The White Ship' (Aitmatov)",
                     "'My Little Poplar' (Aitmatov)"]},
  'correct_index': 0,
  'correct_answer': {'uz': '«Kunda» / «Qiyomat» (Chingiz Aytmatov)',
                     'ru': '«Плаха» (Чингиз Айтматов)',
                     'en': "'The Scaffold' / 'Plakha' (Chingiz Aitmatov)"},
  'image_url': None,
  'fun_fact': {'uz': "Akbara va Toshchaynir ismli bo'rilar juftligi, ularning bolalari nobud bo'lishi va Avdiy "
                     'Kallistratovning fojiali qismati aks etgan falsafiy roman.',
               'ru': 'Трагедия волчицы Акбары, потерявшей волчат по вине браконьеров, и судьба бывшего семинариста '
                     'Авдия Каллистратова.',
               'en': "Aitmatov's 1986 eco-philosophical novel weaving the tragedy of the blue-eyed she-wolf Akbara "
                     'with ex-seminarian Avdiy Kallistratov.'},
  'aliases': ['kunda', 'plaxa', 'aytmatov', 'плаха', 'айтматов', 'akbara']},
 {'id': 'lit_emoji_082',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🏫👧📚🌱🌳',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🏫👧📚🌱🌳',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🏫👧📚🌱🌳'},
  'options': {'uz': ['«Jamila» (Aytmatov)',
                     '«Birinchi muallim» (Chingiz Aytmatov)',
                     '«Momo yer» (Aytmatov)',
                     '«Gulsari» (Aytmatov)'],
              'ru': ['«Джамиля» (Айтматов)',
                     '«Первый учитель» (Чингиз Айтматов)',
                     '«Материнское поле» (Айтматов)',
                     '«Прощай, Гульсары!» (Айтматов)'],
              'en': ["'Jamila' (Aitmatov)",
                     "'The First Teacher' (Chingiz Aitmatov)",
                     "'Mother Earth' (Aitmatov)",
                     "'Farewell, Gulsary!' (Aitmatov)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Birinchi muallim» (Chingiz Aytmatov)',
                     'ru': '«Первый учитель» (Чингиз Айтматов)',
                     'en': "'The First Teacher' (Chingiz Aitmatov)"},
  'image_url': None,
  'fun_fact': {'uz': "Olis qirg'iz ovulida qorli qishda qizaloq Oltinoyni beliga ko'tarib daryodan o'tkazib maktabga "
                     "olib borgan fidoyi o'qituvchi Duyshen haqidagi qissa.",
               'ru': 'Повесть о самоотверженном красноармейце Дюйшене, открывшем первую школу в аиле и спасшем сироту '
                     'Алтынай для науки.',
               'en': 'Devoted teacher Duyshen establishes the first village school in a mountain aul and carries young '
                     'orphan Altynai through icy streams.'},
  'aliases': ['birinchi muallim', 'duyshen', 'первый учитель', 'дюйшен', 'айтматов', 'the first teacher']},
 {'id': 'lit_emoji_083',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🌾🐎🎶❤️🎨',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🌾🐎🎶❤️🎨',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🌾🐎🎶❤️🎨'},
  'options': {'uz': ['«Birinchi muallim» (Aytmatov)',
                     '«Momo yer» (Aytmatov)',
                     '«Jamila» (Chingiz Aytmatov)',
                     '«Sarvqomat dilbarim» (Aytmatov)'],
              'ru': ['«Первый учитель» (Айтматов)',
                     '«Материнское поле» (Айтматов)',
                     '«Джамиля» (Чингиз Айтматов)',
                     '«Тополёк мой в красной косынке» (Айтматов)'],
              'en': ["'The First Teacher' (Aitmatov)",
                     "'Mother Earth' (Aitmatov)",
                     "'Jamila' (Chingiz Aitmatov)",
                     "'My Poplar' (Aitmatov)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Jamila» (Chingiz Aytmatov)',
                     'ru': '«Джамиля» (Чингиз Айтматов)',
                     'en': "'Jamila' (Chingiz Aitmatov)"},
  'image_url': None,
  'fun_fact': {'uz': "Urush yillarida don tashiyotgan Jamila va jarohatlangan frontchi Doniyorning sehrli qo'shiqlari "
                     "orqali kurtak otgan go'zal sevgisi.",
               'ru': 'История любви свободолюбивой Джамили и фронтовика Данияра, чьё дивное пение в степи покорило её '
                     'сердце.',
               'en': 'Young artist Seit narrates how radiant Jamila falls in love with the silent, wounded soldier '
                     'Daniyar through his soulful singing.'},
  'aliases': ['jamila', 'aytmatov', 'джамиля', 'айтматов', 'jamila aitmatov']},
 {'id': 'lit_emoji_084',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🍎🤰💔🏚️🪙',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🍎🤰💔🏚️🪙',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🍎🤰💔🏚️🪙'},
  'options': {'uz': ["«O'g'ri» (Qahhor)", '«Bemor» (Qahhor)', '«Dahshat» (Qahhor)', '«Anor» (Abdulla Qahhor)'],
              'ru': ['«Вор» (Каххар)', '«Больная» (Каххар)', '«Ужас» (Каххар)', '«Гранат» (Абдулла Каххар)'],
              'en': ["'The Thief' (Qahhor)",
                     "'The Patient' (Qahhor)",
                     "'The Horror' (Qahhor)",
                     "'The Pomegranate' (Abdulla Qahhor)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Anor» (Abdulla Qahhor)',
                     'ru': '«Гранат» (Абдулла Каххар)',
                     'en': "'The Pomegranate' (Abdulla Qahhor)"},
  'image_url': None,
  'fun_fact': {'uz': "Turobjon homilador xotini xush ko'rgan bittagina anorni topib kelolmaydi, boylarning mevali "
                     "bog'laridan quviladi va oxiri xotinini kaltaklaydi.",
               'ru': 'Драматический рассказ о бедняке Турабджане, не сумевшем достать для беременной жены гранат и '
                     'срывающем бессилие на ней.',
               'en': 'Impoverished laborer Turobjon wanders through orchards begging for a pomegranate for his '
                     'expectant wife, ending in bitter domestic despair.'},
  'aliases': ['anor', 'abdulla qahhor', 'гранат', 'turobjon']},
 {'id': 'lit_emoji_085',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🐂🌾👮\u200d♂️⚖️💸',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🐂🌾👮\u200d♂️⚖️💸',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🐂🌾👮\u200d♂️⚖️💸'},
  'options': {'uz': ["«O'g'ri» (Abdulla Qahhor)",
                     '«Anor» (Qahhor)',
                     '«Mayiz yemagan xotin» (Qahhor)',
                     "«Shum bola» (G'afur G'ulom)"],
              'ru': ['«Вор» (Абдулла Каххар)',
                     '«Гранат» (Каххар)',
                     '«Жена, не знавшая изюма» (Каххар)',
                     '«Озорник» (Гафур Гулям)'],
              'en': ["'The Thief' (Abdulla Qahhor)",
                     "'The Pomegranate' (Qahhor)",
                     "'The Wife Who Never Ate Raisins' (Qahhor)",
                     "'The Mischievous Boy' (Ghafur Ghulam)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«O'g'ri» (Abdulla Qahhor)",
                     'ru': '«Вор» (Абдулла Каххар)',
                     'en': "'The Thief' (Abdulla Qahhor)"},
  'image_url': None,
  'fun_fact': {'uz': "Qobil boboning yo'qolgan ho'kizini topish bahonasida ellikboshi, amin va pristav boboning "
                     "qo'lidagi bor-yo'g'ini shilib olishadi.",
               'ru': 'У деда Кабыла пропал вол, но продажные царские чиновники и старшины вымогают у бедняка последние '
                     'деньги.',
               'en': "Grandfather Qobil's single ox is stolen, and corrupt colonial authorities rob him of everything "
                     'he owns under the guise of investigating.'},
  'aliases': ["o'g'ri", 'qahhor', 'вор', 'каххар', 'qobil bobo']},
 {'id': 'lit_emoji_086',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🪦🌙👧🥶☠️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🪦🌙👧🥶☠️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🪦🌙👧🥶☠️'},
  'options': {'uz': ['«Anor» (Qahhor)', '«Dahshat» (Abdulla Qahhor)', "«O'g'ri» (Qahhor)", '«Bemor» (Qahhor)'],
              'ru': ['«Гранат» (Каххар)', '«Ужас» (Абдулла Каххар)', '«Вор» (Каххар)', '«Больная» (Каххар)'],
              'en': ["'The Pomegranate' (Qahhor)",
                     "'The Horror' (Abdulla Qahhor)",
                     "'The Thief' (Qahhor)",
                     "'The Patient' (Qahhor)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Dahshat» (Abdulla Qahhor)',
                     'ru': '«Ужас» (Абдулла Каххар)',
                     'en': "'The Horror' (Abdulla Qahhor)"},
  'image_url': None,
  'fun_fact': {'uz': "Jasur Unsin qiz garov bog'lab kechasi qabristonga borib qoziq qoqadi, ammo etagini ham yerga "
                     "qoqib qo'yganini bilmay vahimadan yuragi yoriladi.",
               'ru': 'Бесстрашная девушка Унсин идёт ночью на кладбище на спор, но случайно прибивает колышком подол '
                     'собственного платья и умирает от страха.',
               'en': 'Spirited girl Unsin accepts a midnight dare to drive a wooden stake into a cemetery grave, '
                     'accidentally pinning her own skirt and dying of shock.'},
  'aliases': ['dahshat', 'qahhor', 'ужас', 'каххар', 'unsin']},
 {'id': 'lit_emoji_087',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👨\u200d🎓🚗💔🧑\u200d⚕️🏥',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n'
                     '\n'
                     '👨\u200d🎓🚗💔🧑\u200d⚕️🏥',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n'
                     '\n'
                     '👨\u200d🎓🚗💔🧑\u200d⚕️🏥'},
  'options': {'uz': ['«Fotima va Zuhra» (Umarbekov)',
                     '«Sevgim — sevgilim» (Umarbekov)',
                     "«Odam bo'lish qiyin» (O'lmas Umarbekov)",
                     '«Dunyoning ishlari» (Hoshimov)'],
              'ru': ['«Фатима и Зухра» (Умарбеков)',
                     '«Любовь моя — радость моя» (Умарбеков)',
                     '«Трудно быть человеком» (Ульмас Умарбеков)',
                     '«Дела земные» (Хашимов)'],
              'en': ["'Fatima and Zuhra' (Umarbekov)",
                     "'My Love' (Umarbekov)",
                     "'It's Hard to Be a Human Being' (O'lmas Umarbekov)",
                     "'Affairs of this World' (Hoshimov)"]},
  'correct_index': 2,
  'correct_answer': {'uz': "«Odam bo'lish qiyin» (O'lmas Umarbekov)",
                     'ru': '«Трудно быть человеком» (Ульмас Умарбеков)',
                     'en': "'It's Hard to Be a Human Being' (O'lmas Umarbekov)"},
  'image_url': None,
  'fun_fact': {'uz': "Abdullaning xudbinligi, shon-shuhrat ketidan quvib o'z sevgilisi Gulchehrani va do'stlarini "
                     'xiyonatga giriftor qilishi fojiasi.',
               'ru': 'Роман о молодом человеке Абдулле, чей карьеризм и эгоизм разрушают судьбы близких людей.',
               'en': "Abdulla's vanity and careerism lead him to betray his pure-hearted lover Gulchehra and his true "
                     'principles.'},
  'aliases': ["odam bo'lish qiyin", 'umarbekov', 'трудно быть человеком', 'умарбеков']},
 {'id': 'lit_emoji_088',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👨\u200d👦💰🍷🔪🪦',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👨\u200d👦💰🍷🔪🪦',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👨\u200d👦💰🍷🔪🪦'},
  'options': {'uz': ['«Hind ixtilochilari» (Fitrat)',
                     '«Zaharli hayot» (Hamza)',
                     '«Boy ila xizmatchi» (Hamza)',
                     "«Padarkush» (Mahmudxo'ja Behbudiy)"],
              'ru': ['«Индийские мятежники» (Фитрат)',
                     '«Отравленная жизнь» (Хамза)',
                     '«Бай и батрак» (Хамза)',
                     '«Падаркуш» / «Отцеубийца» (Махмудходжа Бехбуди)'],
              'en': ["'Indian Rebels' (Fitrat)",
                     "'Poisonous Life' (Hamza)",
                     "'The Bey and the Farmhand' (Hamza)",
                     "'The Patricide' (Mahmudkhoja Behbudi)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Padarkush» (Mahmudxo'ja Behbudiy)",
                     'ru': '«Падаркуш» / «Отцеубийца» (Махмудходжа Бехбуди)',
                     'en': "'The Patricide' (Mahmudkhoja Behbudi)"},
  'image_url': None,
  'fun_fact': {'uz': "1911 yilda yozilgan o'zbek professional dramaturgiyasining birinchi asari bo'lib, o'qimagan "
                     "nodon o'g'il Toshmurodning pul uchun otasini o'ldirishi fojiasidir.",
               'ru': 'Первая узбекская драма эпохи джадидизма (1911), обличающая невежество и бескультурье, доводящие '
                     'сына до убийства родного отца.',
               'en': 'The first modern Uzbek theatrical play, written in 1911 by Jadid reformer Behbudi to illustrate '
                     'how illiteracy leads an uneducated son to kill his father.'},
  'aliases': ['padarkush', 'behbudiy', 'падаркуш', 'бехбуди', 'the patricide']},
 {'id': 'lit_emoji_089',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🌕👴👵👶🙏💔',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🌕👴👵👶🙏💔',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🌕👴👵👶🙏💔'},
  'options': {'uz': ["«Oydinda yurgan odamlar» (Tog'ay Murod)",
                     "«Ot kishnagan oqshom» (Tog'ay Murod)",
                     "«Yulduzlar mangu yonadi» (Tog'ay Murod)",
                     "«Bu dunyoda o'lib bo'lmaydi» (Tog'ay Murod)"],
              'ru': ['«Люди, идущие при луне» (Тогай Мурад)',
                     '«Вечер, когда ржал конь» (Тогай Мурад)',
                     '«Звёзды горят вечно» (Тогай Мурад)',
                     '«В этом мире нельзя умереть» (Тогай Мурад)'],
              'en': ["'People Walking in the Moonlight' (Toghay Murad)",
                     "'The Evening the Horse Neighed' (Toghay Murad)",
                     "'Stars Burn Forever' (Toghay Murad)",
                     "'One Cannot Die in This World' (Toghay Murad)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«Oydinda yurgan odamlar» (Tog'ay Murod)",
                     'ru': '«Люди, идущие при луне» (Тогай Мурад)',
                     'en': "'People Walking in the Moonlight' (Toghay Murad)"},
  'image_url': None,
  'fun_fact': {'uz': "Qoplon bobo va Oymomo xolaning butun umr tirnoqqa zor bo'lib farzand orzusida chekkan mungli va "
                     "go'zal armonlari aks etgan doston-qissa.",
               'ru': 'Пронзительная лирическая повесть Тогая Мурада о пожилых супругах Каплане и Оймомо, пронёсших '
                     'через жизнь мечту о ребёнке.',
               'en': "Toghay Murad's poignant novella depicting elderly couple Qoplon and Oymomo united by their "
                     'lifelong yearning for a child.'},
  'aliases': ['oydinda yurgan odamlar', "tog'ay murod", 'люди идущие при луне', 'тогай мурад']},
 {'id': 'lit_emoji_090',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👴🎖️🚩📻🇺🇿',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👴🎖️🚩📻🇺🇿',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👴🎖️🚩📻🇺🇿'},
  'options': {'uz': ["«Ot kishnagan oqshom» (Tog'ay Murod)",
                     "«Bu dunyoda o'lib bo'lmaydi» (Tog'ay Murod)",
                     "«Oydinda yurgan odamlar» (Tog'ay Murod)",
                     '«Chinor» (Asqad Muxtor)'],
              'ru': ['«Вечер, когда ржал конь» (Тогай Мурад)',
                     '«В этом мире нельзя умереть» (Тогай Мурад)',
                     '«Люди, идущие при луне» (Тогай Мурад)',
                     '«Чинар» (Аскад Мухтар)'],
              'en': ["'The Evening the Horse Neighed' (Toghay Murad)",
                     "'One Cannot Die in This World' (Toghay Murad)",
                     "'People Walking in the Moonlight' (Toghay Murad)",
                     "'The Plane Tree' (Asqad Mukhtar)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Bu dunyoda o'lib bo'lmaydi» (Tog'ay Murod)",
                     'ru': '«В этом мире нельзя умереть» (Тогай Мурад)',
                     'en': "'One Cannot Die in This World' (Toghay Murad)"},
  'image_url': None,
  'fun_fact': {'uz': "Sho'ro davri mafkurasiga qattiq ishongan Botir firqaning mustaqillik arafasida o'z ideallari "
                     'puchga chiqqanini anglashidagi fojiali va achchiq taqdiri.',
               'ru': 'Роман Тогая Мурада о драме престарелого коммуниста-идеалиста Батыра Фиркы в эпоху слома '
                     'советской эпохи.',
               'en': "Toghay Murad's satirical yet tragic novel chronicling elderly staunch communist Botir Firqa "
                     'witnessing his lifelong illusions crumble.'},
  'aliases': ["bu dunyoda o'lib bo'lmaydi", "tog'ay murod", 'в этом мире нельзя умереть', 'тогай мурад']},
 {'id': 'lit_emoji_091',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🌊📦🗡️💔👸',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🌊📦🗡️💔👸',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🌊📦🗡️💔👸'},
  'options': {'uz': ['«Farhod va Shirin» (Navoiy)',
                     '«Layli va Majnun» (Navoiy)',
                     '«Tohir va Zuhra» (Xalq dostoni / Sayyodiy)',
                     "«Kuntug'mish» dostoni"],
              'ru': ['«Фархад и Ширин» (Навои)',
                     '«Лейли и Меджнун» (Навои)',
                     '«Тахир и Зухра» (узбекский народный дастан)',
                     '«Кунтугмыш»'],
              'en': ["'Farhad and Shirin' (Navoi)",
                     "'Layla and Majnun' (Navoi)",
                     "'Tohir and Zuhra' (Uzbek Folk Dastan)",
                     "'Kuntugmish'"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Tohir va Zuhra» (Xalq dostoni / Sayyodiy)',
                     'ru': '«Тахир и Зухра» (узбекский народный дастан)',
                     'en': "'Tohir and Zuhra' (Uzbek Folk Dastan)"},
  'image_url': None,
  'fun_fact': {'uz': "Shoh qizi Zuhra va vazir o'g'li Tohir sevgisi; Tohir sandiqqa solinib daryoga oqiziladi, ammo "
                     "uning muhabbati so'nmaydi.",
               'ru': 'Народный эпос о любви ханской дочери Зухры и сына визиря Тахира, брошенного в кованом сундуке в '
                     'бурные воды реки.',
               'en': "Classic romantic dastan about princess Zuhra and vizier's son Tohir, cast into a raging river "
                     'inside a locked chest.'},
  'aliases': ['tohir va zuhra', 'sayyodiy', 'тахир и зухра', 'tohir', 'zuhra']},
 {'id': 'lit_emoji_092',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n👑🏜️👶👶🐺',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n👑🏜️👶👶🐺',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n👑🏜️👶👶🐺'},
  'options': {'uz': ['«Alpomish» dostoni', "«Go'ro'g'li» dostoni", '«Rustamxon» dostoni', "«Kuntug'mish» dostoni"],
              'ru': ['«Алпамыш»', '«Гёроглы»', '«Рустамхан»', '«Кунтугмыш» (народный дастан)'],
              'en': ["'Alpomish'", "'Gorogly'", "'Rustamkhan'", "'Kuntugmish' (Uzbek Folk Dastan)"]},
  'correct_index': 3,
  'correct_answer': {'uz': "«Kuntug'mish» dostoni",
                     'ru': '«Кунтугмыш» (народный дастан)',
                     'en': "'Kuntugmish' (Uzbek Folk Dastan)"},
  'image_url': None,
  'fun_fact': {'uz': "Shahzoda Kuntug'mish va Xolbekaning sevgisi, cho'lda chaqaloqlaridan ayrilib qolishi va ko'plab "
                     "sarguzashtlardan so'ng yana oila birlashishi.",
               'ru': 'Романтический эпос о скитаниях Кунтугмыша и его верной жены Холбеки, потерявших детей в пустыне '
                     'и нашедших их спустя годы.',
               'en': 'Folk epic of prince Kuntugmish and beloved Kholbeka who lose their twin infant boys in the '
                     'desert before reuniting after epic trials.'},
  'aliases': ["kuntug'mish", 'xolbeka', 'кунтугмыш', 'kuntugmish']},
 {'id': 'lit_emoji_093',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🪐🏰👸🎶🦌',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🪐🏰👸🎶🦌',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🪐🏰👸🎶🦌'},
  'options': {'uz': ["«Sab'ai sayyor» / «Yetti sayyora» (Alisher Navoiy)",
                     '«Saddi Iskandariy» (Navoiy)',
                     '«Hayrat ul-abror» (Navoiy)',
                     '«Farhod va Shirin» (Navoiy)'],
              'ru': ['«Семь планет» / «Сабъаи сайёр» (Алишер Навои)',
                     '«Вал Искандара» (Навои)',
                     '«Смятение праведных» (Навои)',
                     '«Фархад и Ширин» (Навои)'],
              'en': ["'Seven Planets' (Alisher Navoi)",
                     "'Sadd-i Iskandari' (Navoi)",
                     "'Hayrat al-Abrar' (Navoi)",
                     "'Farhad and Shirin' (Navoi)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«Sab'ai sayyor» / «Yetti sayyora» (Alisher Navoiy)",
                     'ru': '«Семь планет» / «Сабъаи сайёр» (Алишер Навои)',
                     'en': "'Seven Planets' (Alisher Navoi)"},
  'image_url': None,
  'fun_fact': {'uz': "Bahrom Go'r 7 ta rangli qasrda 7 iqlim malikalaridan 7 xil hikoyat tinglaydi; doston Diloromning "
                     'fojiali sevgisi bilan boshlanadi.',
               'ru': 'Четвёртая поэма «Хамсы» Навои о шахе Бахраме Гуре, певице Дилорам и семи сказках царевен в семи '
                     'разноцветных дворцах.',
               'en': "Fourth epic of Navoi's Khamsa, recounting King Bahrom Gur, his lost musician love Dilorom, and "
                     'seven stories in seven colored pavilions.'},
  'aliases': ["sab'ai sayyor", 'yetti sayyora', 'navoiy', 'семь планет', "bahrom go'r"]},
 {'id': 'lit_emoji_094',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧱🛡️👑⚔️🗺️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🧱🛡️👑⚔️🗺️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧱🛡️👑⚔️🗺️'},
  'options': {'uz': ["«Sab'ai sayyor» (Navoiy)",
                     '«Saddi Iskandariy» (Alisher Navoiy)',
                     '«Hayrat ul-abror» (Navoiy)',
                     '«Farhod va Shirin» (Navoiy)'],
              'ru': ['«Семь планет» (Навои)',
                     '«Вал Искандара» (Алишер Навои)',
                     '«Смятение праведных» (Навои)',
                     '«Фархад и Ширин» (Navoiy)'],
              'en': ["'Seven Planets' (Navoi)",
                     "'The Wall of Alexander' (Alisher Navoi)",
                     "'Hayrat al-Abrar' (Navoi)",
                     "'Farhad and Shirin' (Navoi)"]},
  'correct_index': 1,
  'correct_answer': {'uz': '«Saddi Iskandariy» (Alisher Navoiy)',
                     'ru': '«Вал Искандара» (Алишер Навои)',
                     'en': "'The Wall of Alexander' (Alisher Navoi)"},
  'image_url': None,
  'fun_fact': {'uz': 'Navoiy «Xamsa»sining beshinchi dostoni; unda adolatli jahongir Iskandar Zulqarnaynning jahon '
                     "kezishi va Ya'juj-Ma'jujga qarshi mustahkam devor qurishi tasvirlangan.",
               'ru': 'Заключительная поэма «Хамсы» Навои об Александре Македонском (Искандаре), философах Аристотеле и '
                     'Платоне и возведении железной стены.',
               'en': "The final epic of Navoi's Khamsa portraying Alexander the Great as an enlightened "
                     'philosopher-king constructing an iron barrier against Gog and Magog.'},
  'aliases': ['saddi iskandariy', 'navoiy', 'вал искандара', 'iskandar devori', 'alexander wall']},
 {'id': 'lit_emoji_095',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🌳👴🧒🇺🇿📜',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🌳👴🧒🇺🇿📜',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🌳👴🧒🇺🇿📜'},
  'options': {'uz': ["«Tug'ilish» (Asqad Muxtor)",
                     "«Bo'ronlarda bordek halovat» (Asqad Muxtor)",
                     '«Chinor» romani (Asqad Muxtor)',
                     '«Ufq» (Said Ahmad)'],
              'ru': ['«Рождение» (Мухтар)',
                     '«В бурях есть покой» (Мухтар)',
                     '«Чинар» (роман Аскада Мухтара)',
                     '«Горизонт» (Саид Ахмад)'],
              'en': ["'The Birth' (Mukhtar)",
                     "'Peace in the Tempest' (Mukhtar)",
                     "'The Plane Tree' (Asqad Mukhtar)",
                     "'The Horizon' (Said Ahmad)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Chinor» romani (Asqad Muxtor)',
                     'ru': '«Чинар» (роман Аскада Мухтара)',
                     'en': "'The Plane Tree' (Asqad Mukhtar)"},
  'image_url': None,
  'fun_fact': {'uz': "Keksa Ochil buva va uning ko'p tarmoqli avlodi orqali o'zbek oilasi, qadriyatlari va tarixining "
                     'chinor daraxtidek chuqur tomir otishi aks ettirilgan.',
               'ru': 'Философский роман-эпопея Аскада Мухтара, где вековой чинар символизирует нерушимую связь '
                     'поколений узбекского народа.',
               'en': "Asqad Mukhtar's multi-generational family chronicle using a giant ancient plane tree as an "
                     'allegory for cultural resilience.'},
  'aliases': ['chinor', 'asqad muxtor', 'чинар', 'аскад мухтар', 'ochil buva']},
 {'id': 'lit_emoji_096',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n✨⛓️❄️🇷🇺🎖️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n✨⛓️❄️🇷🇺🎖️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n✨⛓️❄️🇷🇺🎖️'},
  'options': {'uz': ['«Shinelli yillar» (Shuhrat)',
                     '«Jannat qidirganlar» (Shuhrat)',
                     '«Ufq» (Said Ahmad)',
                     '«Oltin zanglamas» (Shuhrat)'],
              'ru': ['«Годы в шинели» (Шухрат)',
                     '«Искатели рая» (Шухрат)',
                     '«Горизонт» (Саид Ахмад)',
                     '«Золото не ржавеет» (Шухрат)'],
              'en': ["'Years in an Overcoat' (Shukhrat)",
                     "'Seekers of Paradise' (Shukhrat)",
                     "'The Horizon' (Said Ahmad)",
                     "'Gold Never Rusts' (Shukhrat)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Oltin zanglamas» (Shuhrat)',
                     'ru': '«Золото не ржавеет» (Шухрат)',
                     'en': "'Gold Never Rusts' (Shukhrat)"},
  'image_url': None,
  'fun_fact': {'uz': "Stalin qatag'onlari davrida nohaq qamalib, Sibir katorgasi sinovlaridan o'tgan, vijdoni va "
                     "insoniyligini pok saqlagan o'zbek ziyolilari jasorati.",
               'ru': 'Роман Шухрата о репрессиях 1930-50-х годов и лагерях ГУЛАГа в Сибири; благородный человек, как '
                     'золото, не ржавеет ни при каких невзгодах.',
               'en': "Shukhrat's courageous novel based on his own Gulag imprisonment, proving that true human virtue, "
                     'like gold, never corrodes.'},
  'aliases': ['oltin zanglamas', 'shuhrat', 'золото не ржавеет', 'шухрат']},
 {'id': 'lit_emoji_097',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🧙\u200d♂️⚔️🎒🐝🍯',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🧙\u200d♂️⚔️🎒🐝🍯',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🧙\u200d♂️⚔️🎒🐝🍯'},
  'options': {'uz': ["«Sariq devning o'limi» (Xudoyberdi To'xtaboyev)",
                     "«Sariq devni minib» (To'xtaboyev)",
                     "«Besh bolali yigitcha» (To'xtaboyev)",
                     "«Shirin qovunlar mamlakati» (To'xtaboyev)"],
              'ru': ['«Конец жёлтого дива» (Худайберды Тухтабаев)',
                     '«Верхом на жёлтом диве» (Тухтабаев)',
                     '«Мальчик с пятью детьми» (Тухтабаев)',
                     '«Страна сладких дынь» (Тухтабаев)'],
              'en': ["'Death of the Yellow Giant' (Khudoyberdi Tukhtabayev)",
                     "'Riding the Yellow Giant' (Tukhtabayev)",
                     "'Boy with Five Children' (Tukhtabayev)",
                     "'Land of Sweet Melons' (Tukhtabayev)"]},
  'correct_index': 0,
  'correct_answer': {'uz': "«Sariq devning o'limi» (Xudoyberdi To'xtaboyev)",
                     'ru': '«Конец жёлтого дива» (Худайберды Тухтабаев)',
                     'en': "'Death of the Yellow Giant' (Khudoyberdi Tukhtabayev)"},
  'image_url': None,
  'fun_fact': {'uz': "«Sariq devni minib» qissasining mantiqiy davomi bo'lib, unda Hoshimjon o'z ichidagi dangasalik "
                     "va xudbinlik 'devi'ni qanday yenggani tasvirlanadi.",
               'ru': 'Продолжение приключений Хашимджана, где победа над дивом означает окончательную победу мальчика '
                     'над собственной ленью и хвастовством.',
               'en': "The acclaimed sequel in which Hoshimjon conquers his inner 'giant' of indolence and vanity "
                     'through diligence and honesty.'},
  'aliases': ["sariq devning o'limi", "to'xtaboyev", 'конец желтого дива', 'тухтабаев']},
 {'id': 'lit_emoji_098',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🥺🚗💰💔🏢',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🥺🚗💰💔🏢',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🥺🚗💰💔🏢'},
  'options': {'uz': ["«Sariq devni minib» (To'xtaboyev)",
                     "«Mungli ko'zlar» (Xudoyberdi To'xtaboyev)",
                     "«Qasoskorning oltin boshi» (To'xtaboyev)",
                     '«Dunyoning ishlari» (Hoshimov)'],
              'ru': ['«Верхом на жёлтом диве» (Тухтабаев)',
                     '«Печальные глаза» / «Грустные глаза» (Худайберды Тухтабаев)',
                     '«Золотая голова мстителя» (Тухтабаев)',
                     '«Дела земные» (Хашимов)'],
              'en': ["'Riding the Yellow Giant' (Tukhtabayev)",
                     "'Sorrowful Eyes' (Khudoyberdi Tukhtabayev)",
                     "'The Avenger's Golden Head' (Tukhtabayev)",
                     "'Affairs of this World' (Hoshimov)"]},
  'correct_index': 1,
  'correct_answer': {'uz': "«Mungli ko'zlar» (Xudoyberdi To'xtaboyev)",
                     'ru': '«Печальные глаза» / «Грустные глаза» (Худайберды Тухтабаев)',
                     'en': "'Sorrowful Eyes' (Khudoyberdi Tukhtabayev)"},
  'image_url': None,
  'fun_fact': {'uz': "Boylik va poraxo'rlik girdobiga botgan ota-onaning bolalari — Zafar va Nigora taqdiri orqali "
                     "ma'naviy qashshoqlik fojiasi ochib berilgan roman.",
               'ru': 'Драматический роман Тухтабаева о детях из семьи коррумпированного чиновника, страдающих от '
                     'алчности и духовной черствости родителей.',
               'en': "Tukhtabayev's realistic novel examining the moral neglect of children in a materialistic "
                     'household seduced by corruption.'},
  'aliases': ["mungli ko'zlar", "to'xtaboyev", 'печальные глаза', 'тухтабаев']},
 {'id': 'lit_emoji_099',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🥋⚔️👑🐎🏔️',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🥋⚔️👑🐎🏔️',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🥋⚔️👑🐎🏔️'},
  'options': {'uz': ["«Qil ko'prik» (Xolmirzayev)",
                     "«To'maris» (Mirkarim Osim)",
                     '«Qora kamar» dramasi (Shukur Xolmirzayev)',
                     '«Ibn Sino» (Mirkarim Osim)'],
              'ru': ['«Волосяной мост» (Холмирзаев)',
                     '«Томирис» (Миркарим Осим)',
                     '«Чёрный пояс» (драма Шукура Холмирзаева)',
                     '«Ибн Сина» (Осим)'],
              'en': ["'Hair-Thin Bridge' (Kholmirzaev)",
                     "'Tomiris' (Mirkarim Osim)",
                     "'The Black Belt' (Shukur Kholmirzaev)",
                     "'Avicenna' (Osim)"]},
  'correct_index': 2,
  'correct_answer': {'uz': '«Qora kamar» dramasi (Shukur Xolmirzayev)',
                     'ru': '«Чёрный пояс» (драма Шукура Холмирзаева)',
                     'en': "'The Black Belt' (Shukur Kholmirzaev)"},
  'image_url': None,
  'fun_fact': {'uz': "Buxoro amirligi qulashi davridagi murakkab tarixiy voqealar va Ibrohimbek qo'rboshi fojeasini "
                     'ilk bor xolis yoritgan tarixiy drama.',
               'ru': 'Историческая драма Холмирзаева, впервые смело и правдиво показавшая трагедию повстанческого '
                     'движения басмачей в 1920-е годы.',
               'en': "Kholmirzaev's bold historical play re-evaluating the 1920s resistance in the Bukhara region and "
                     'the tragedy of leader Ibrahimbek.'},
  'aliases': ['qora kamar', 'xolmirzayev', 'чёрный пояс', 'холмирзаев']},
 {'id': 'lit_emoji_0100',
  'sub_mode': 'book_emojis',
  'question': {'uz': 'Quyidagi emojilar qaysi mashhur kitob / adabiy asarni ifodalaydi?\n\n🤖👩\u200d🦰🧹🍲🚜',
               'ru': 'Какую знаменитую книгу или литературное произведение зашифровывают эти эмодзи?\n\n🤖👩\u200d🦰🧹🍲🚜',
               'en': 'Which famous book or literary masterpiece is represented by these emojis?\n\n🤖👩\u200d🦰🧹🍲🚜'},
  'options': {'uz': ["«Kelinlar qo'zg'oloni» (Said Ahmad)",
                     '«Taqdir eshigi» (Sharof Boshbekov)',
                     '«Eski shahar gavroshlari» (Boshbekov)',
                     '«Temir xotin» (Sharof Boshbekov)'],
              'ru': ['«Бунт невесток» (Саид Ахмад)',
                     '«Дверь судьбы» (Башбеков)',
                     '«Гавроши старого города» (Башбеков)',
                     '«Железная женщина» (Шароф Башбеков)'],
              'en': ["'The Revolt of the Daughters-in-Law' (Said Ahmad)",
                     "'The Door of Fate' (Boshbekov)",
                     "'Old City Gavroches' (Boshbekov)",
                     "'The Iron Woman' (Sharof Boshbekov)"]},
  'correct_index': 3,
  'correct_answer': {'uz': '«Temir xotin» (Sharof Boshbekov)',
                     'ru': '«Железная женщина» (Шароф Башбеков)',
                     'en': "'The Iron Woman' (Sharof Boshbekov)"},
  'image_url': None,
  'fun_fact': {'uz': "Ixtirochi olim Olimtoy ichkilikka berilgan Qo'chqor aka uchun charchamaydigan robot ayol "
                     "'Alomat'ni yasab beradi; o'zbek fantastik kinokomediyasining durdonasi.",
               'ru': 'Искромётная фантастическая комедия об изобретателе робота-женщины Аломат для сварливого '
                     'деревенского дехканина Кучкара.',
               'en': "Sharof Boshbekov's famous sci-fi comedy play in which an inventor builds a tireless female "
                     'humanoid robot named Alomat for a rustic villager.'},
  'aliases': ['temir xotin', 'sharof boshbekov', 'железная женщина', 'башбеков', 'alomat']},
 {'id': 'lit_auth_001',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Alisher Navoiy', 'Zahiriddin Muhammad Bobur', 'Lutfiy', 'Abdurahmon Jomiy'],
              'ru': ['Алишер Навои', 'Захириддин Мухаммад Бабур', 'Лутфи', 'Абдурахман Джами'],
              'en': ['Alisher Navoi', 'Babur', 'Lutfi', 'Jami']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Alisher Navoiy', 'ru': 'Алишер Навои', 'en': 'Alisher Navoi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Alisher_Navoiy_portrait.jpg',
  'fun_fact': {'uz': "1441-1501 yillarda Hirotda yashagan Alisher Navoiy turkiy tilda birinchi bo'lib «Xamsa» yaratgan "
                     'buyuk shoir va davlat arbobidir.',
               'ru': 'Великий поэт, мыслитель и государственный деятель XV века, основоположник староузбекского '
                     'литературного языка и автор первой тюркской «Хамсы».',
               'en': 'Founder of early Uzbek literature and statesman in Herat, who in 1483-1485 composed the first '
                     "'Khamsa' (Quintet) in a Turkic language."},
  'aliases': ['alisher navoiy', 'navoiy', 'алишер навои', 'навои', 'alisher navoi']},
 {'id': 'lit_auth_002',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Alisher Navoiy', 'Zahiriddin Muhammad Bobur', "Mirzo Ulug'bek", 'Husayn Boyqaro'],
              'ru': ['Алишер Навои', 'Захириддин Мухаммад Бабур', 'Мирзо Улугбек', 'Хусейн Байкара'],
              'en': ['Alisher Navoi', 'Babur', 'Mirzo Ulugbek', 'Husayn Bayqara']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Zahiriddin Muhammad Bobur', 'ru': 'Захириддин Мухаммад Бабур', 'en': 'Babur'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Babur_portrait.jpg',
  'fun_fact': {'uz': 'Temuriylar sulolasi vakili, buyuk shoir va sarkarda, Hindistonda Boburiylar imperiyasi asoschisi '
                     'hamda nodir «Boburnoma» muallifi.',
               'ru': 'Потомок Тамерлана, полководец, основатель империи Великих Моголов в Индии и автор уникального '
                     'автобиографического труда «Бабур-наме».',
               'en': 'Timurid prince, poet, founder of the Mughal Empire in India, and author of the celebrated '
                     "autobiographical 'Baburnama'."},
  'aliases': ['bobur', 'zahiriddin muhammad bobur', 'бабур', 'babur']},
 {'id': 'lit_auth_003',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ["Abdulhamid Cho'lpon", 'Abdurauf Fitrat', 'Abdulla Qodiriy (Julqunboy)', "Mahmudxo'ja Behbudiy"],
              'ru': ['Абдулхамид Чулпан', 'Абдурауф Фитрат', 'Абдулла Кадыри (Джулкунбай)', 'Махмудходжа Бехбуди'],
              'en': ['Abdulhamid Cholpon', 'Abdurauf Fitrat', 'Abdulla Qadiri (Julqunboy)', 'Mahmudkhoja Behbudi']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Abdulla Qodiriy (Julqunboy)',
                     'ru': 'Абдулла Кадыри (Джулкунбай)',
                     'en': 'Abdulla Qadiri (Julqunboy)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Abdulla_Qodiriy.jpg',
  'fun_fact': {'uz': "O'zbek romanchiligining asoschisi, «O'tkan kunlar» va «Mehrobdan chayon» romanlari muallifi; "
                     "1938 yilda nohaq qatag'on qurboni bo'lgan.",
               'ru': 'Основоположник узбекского романа, автор бессмертных произведений «Минувшие дни» и «Скорпион из '
                     'алтаря», репрессирован в 1938 году.',
               'en': "Pioneering founder of the Uzbek novel genre, author of 'Bygone Days', executed during the "
                     'Stalinist Great Purge in 1938.'},
  'aliases': ['abdulla qodiriy', 'qodiriy', 'julqunboy', 'абдулла кадыри', 'кадыри', 'qadiri']},
 {'id': 'lit_auth_004',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Abdulla Qodiriy', 'Usmon Nosir', 'Hamid Olimjon', "Abdulhamid Cho'lpon"],
              'ru': ['Абдулла Кадыри', 'Усман Насыр', 'Хамид Алимджан', 'Абдулхамид Чулпан'],
              'en': ['Abdulla Qadiri', 'Usmon Nosir', 'Hamid Olimjon', 'Abdulhamid Cholpon']},
  'correct_index': 3,
  'correct_answer': {'uz': "Abdulhamid Cho'lpon", 'ru': 'Абдулхамид Чулпан', 'en': 'Abdulhamid Cholpon'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Abdulhamid_Cho%27lpon.jpg',
  'fun_fact': {'uz': "Jadidchilik adabiyotining ulug' shoiri, «Kecha va kunduz» romani, «Ko'ngil», «Buzilgan o'lkaga» "
                     "kabi o'tli erksevar she'rlar muallifi.",
               'ru': 'Выдающийся поэт и прозаик джадидского возрождения, автор романа «Ночь и день» и шедевров '
                     'узбекской гражданской лирики.',
               'en': "Foremost poet of the Central Asian Jadid movement, author of 'Night and Day' and passionate "
                     'anthems of national liberty.'},
  'aliases': ["cho'lpon", "abdulhamid cho'lpon", 'чулпан', 'cholpon']},
 {'id': 'lit_auth_005',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Abdurauf Fitrat', "Mahmudxo'ja Behbudiy", "Fayzulla Xo'jayev", 'Munavvarqori Abdurashidxonov'],
              'ru': ['Абдурауф Фитрат', 'Махмудходжа Бехбуди', 'Файзулла Ходжаев', 'Мунавваркары Абдурашидханов'],
              'en': ['Abdurauf Fitrat', 'Mahmudkhoja Behbudi', 'Fayzulla Khojayev', 'Munawwar Qari']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Abdurauf Fitrat', 'ru': 'Абдурауф Фитрат', 'en': 'Abdurauf Fitrat'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/07/Abdurauf_Fitrat.jpg',
  'fun_fact': {'uz': 'Buxoro jadidlarining yetakchisi, olim, dramaturg va davlat arbobi, «Munozara», «Hind '
                     'ixtilochilari», «Qiyomat» asarlari muallifi.',
               'ru': 'Один из лидеров младобухарцев и джадидизма, выдающийся учёный-филолог, автор драм «Спор» и '
                     '«Индийские мятежники».',
               'en': 'Leader of the Young Bukharians and Jadid enlightenment, scholar, playwright, and statesman '
                     'executed in 1938.'},
  'aliases': ['fitrat', 'abdurauf fitrat', 'фитрат']},
 {'id': 'lit_auth_006',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Abdurauf Fitrat', "Mahmudxo'ja Behbudiy", 'Abdulla Avloniy', 'Hamza Hakimzoda Niyoziy'],
              'ru': ['Абдурауф Фитрат', 'Махмудходжа Бехбуди', 'Абдулла Авлони', 'Хамза Хакимзаде Ниязи'],
              'en': ['Abdurauf Fitrat', 'Mahmudkhoja Behbudi', 'Abdulla Avloni', 'Hamza Hakimzade Niyazi']},
  'correct_index': 1,
  'correct_answer': {'uz': "Mahmudxo'ja Behbudiy", 'ru': 'Махмудходжа Бехбуди', 'en': 'Mahmudkhoja Behbudi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ee/Mahmudxo%27ja_Behbudiy.jpg',
  'fun_fact': {'uz': "Turkiston jadidchiligining otasi, birinchi o'zbek dramasi «Padarkush» muallifi, «Samarqand» "
                     'gazetasi va «Oyna» jurnali noshiri.',
               'ru': '«Отец туркестанского джадидизма», просветитель, издатель журналов и автор первой узбекской пьесы '
                     '«Падаркуш» (1911).',
               'en': 'Foundational leader of Turkestan Jadidism, educator, journalist, and author of the first modern '
                     "Uzbek drama 'The Patricide'."},
  'aliases': ['behbudiy', "mahmudxo'ja behbudiy", 'бехбуди', 'behbudi']},
 {'id': 'lit_auth_007',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Abdulla Avloniy', 'Sadriddin Ayniy', 'Hamza Hakimzoda Niyoziy', "G'afur G'ulom"],
              'ru': ['Абдулла Авлони', 'Садриддин Айни', 'Хамза Хакимзаде Ниязи', 'Гафур Гулям'],
              'en': ['Abdulla Avloni', 'Sadriddin Ayni', 'Hamza Hakimzade Niyazi', 'Ghafur Ghulam']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Hamza Hakimzoda Niyoziy', 'ru': 'Хамза Хакимзаде Ниязи', 'en': 'Hamza Hakimzade Niyazi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Hamza_Hakimzoda_Niyoziy.jpg',
  'fun_fact': {'uz': "O'zbek sovet dramaturgiyasi va teatrining asoschilaridan biri, «Boy ila xizmatchi», «Maysaraning "
                     'ishi» komediyasi muallifi.',
               'ru': 'Драматург, поэт и общественный деятель, основоположник узбекского советского театра, автор '
                     'комедии «Проказы Майсары».',
               'en': 'Poet and pioneer of early 20th-century Uzbek theatre, author of famous plays including '
                     "'Maysara's Pranks'."},
  'aliases': ['hamza', 'hamza hakimzoda niyoziy', 'хамза', 'хамза ниязи']},
 {'id': 'lit_auth_008',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ["G'afur G'ulom", 'Abdulla Qahhor', 'Hamid Olimjon', "Muso Toshmuhammad o'g'li Oybek"],
              'ru': ['Гафур Гулям', 'Абдулла Каххар', 'Хамид Алимджан', 'Муса Ташмухамедов (Айбек)'],
              'en': ['Ghafur Ghulam', 'Abdulla Qahhor', 'Hamid Olimjon', 'Musa Tashmukhamedov (Oybek)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Muso Toshmuhammad o'g'li Oybek",
                     'ru': 'Муса Ташмухамедов (Айбек)',
                     'en': 'Musa Tashmukhamedov (Oybek)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/a/af/Oybek.jpg',
  'fun_fact': {'uz': "O'zbekiston xalq yozuvchisi, akademik, mashhur «Navoiy» va «Qutlug' qon» romanlari muallifi, "
                     "Pushkinning «Yevgeniy Onegin»ini o'zbek tiliga mahorat bilan tarjima qilgan.",
               'ru': 'Классик узбекской литературы, академик, автор исторических эпопей «Навои» и «Священная кровь», '
                     'блестящий переводчик Пушкина.',
               'en': "Prominent Uzbek writer and scholar, author of masterpieces 'Navoi' and 'Sacred Blood', and "
                     "translator of Pushkin's 'Eugene Onegin'."},
  'aliases': ['oybek', 'айбек', 'musa tashmukhamedov']},
 {'id': 'lit_auth_009',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ["G'afur G'ulom", 'Oybek', 'Hamid Olimjon', 'Abdulla Qahhor'],
              'ru': ['Гафур Гулям', 'Айбек', 'Хамид Алимджан', 'Абдулла Каххар'],
              'en': ['Ghafur Ghulam', 'Oybek', 'Hamid Olimjon', 'Abdulla Qahhor']},
  'correct_index': 0,
  'correct_answer': {'uz': "G'afur G'ulom", 'ru': 'Гафур Гулям', 'en': 'Ghafur Ghulam'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/30/G%27afur_G%27ulom.jpg',
  'fun_fact': {'uz': "O'zbekiston xalq shoiri, akademik, «Shum bola» qissasi hamda urush yillaridagi «Sen yetim "
                     "emassan» kabi shoh she'rlar muallifi.",
               'ru': 'Народный поэт Узбекистана, автор бессмертной повести «Озорник» и пронзительного военного '
                     'стихотворения «Ты не сирота».',
               'en': "Major Uzbek poet and novelist, creator of 'The Mischievous Boy' and the moving wartime anthem "
                     "'You Are Not an Orphan'."},
  'aliases': ["g'afur g'ulom", 'gafur gulyam', 'гафур гулям', 'ghafur ghulam']},
 {'id': 'lit_auth_010',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ["G'afur G'ulom", 'Abdulla Qahhor', 'Said Ahmad', "O'tkir Hoshimov"],
              'ru': ['Гафур Гулям', 'Абдулла Каххар', 'Саид Ахмад', 'Уткир Хашимов'],
              'en': ['Ghafur Ghulam', 'Abdulla Qahhor', 'Said Ahmad', "O'tkir Hoshimov"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Abdulla Qahhor', 'ru': 'Абдулла Каххар', 'en': 'Abdulla Qahhor'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Abdulla_Qahhor.jpg',
  'fun_fact': {'uz': "O'zbek hikoyanavisligining tengsiz ustasi, «Anor», «O'g'ri», «Bemor», «Sinchalak» kabi durdona "
                     'asarlar hamda «Tobutdan tovush» komediyasi muallifi.',
               'ru': '«Узбекский Чехов», непревзойдённый мастер новеллы и острой социальной сатиры («Гранат», «Вор», '
                     '«Птичка-невеличка»).',
               'en': 'Regarded as the master of the modern Uzbek short story, known for his psychological brevity in '
                     "'The Pomegranate' and 'The Thief'."},
  'aliases': ['abdulla qahhor', 'qahhor', 'абдулла каххар', 'каххар']},
 {'id': 'lit_auth_011',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Usmon Nosir', 'Oybek', 'Hamid Olimjon', 'Maqsud Shayxzoda'],
              'ru': ['Усман Насыр', 'Айбек', 'Хамид Алимджан', 'Максуд Шейхзаде'],
              'en': ['Usmon Nosir', 'Oybek', 'Hamid Olimjon', 'Maqsud Shayxzoda']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Hamid Olimjon', 'ru': 'Хамид Алимджан', 'en': 'Hamid Olimjon'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/6b/Hamid_Olimjon.jpg',
  'fun_fact': {'uz': "O'zbek she'riyatining jo'shqin bulbuli, «Oygul bilan Baxtiyor», «Zaynab va Omon», «Semurg'» "
                     "dostonlari muallifi; Zulfiyaning turmush o'rtog'i.",
               'ru': 'Выдающийся узбекский поэт-лирик, драматург, автор фольклорных поэм «Айгуль и Бахтияр» и '
                     '«Семург»; супруг поэтессы Зульфии.',
               'en': 'Lyrical poet and dramatist of dramatic romantic epics, husband of renowned poet Zulfiya, died '
                     'tragically young in 1944.'},
  'aliases': ['hamid olimjon', 'olimjon', 'хамид алимджан', 'алимджан']},
 {'id': 'lit_auth_012',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Nodira', 'Uvaysiy', 'Halima Xudoyberdiyeva', 'Zulfiya (Zulfiya Isroilova)'],
              'ru': ['Нодира', 'Увайси', 'Халима Худойбердыева', 'Зульфия (Зульфия Исраилова)'],
              'en': ['Nodira', 'Uvaysiy', 'Halima Xudoyberdiyeva', 'Zulfiya (Zulfiya Isroilova)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Zulfiya (Zulfiya Isroilova)',
                     'ru': 'Зульфия (Зульфия Исраилова)',
                     'en': 'Zulfiya (Zulfiya Isroilova)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/07/Zulfiya_Isroilova.jpg',
  'fun_fact': {'uz': "O'zbekiston xalq shoirasi, xalqaro Javoharla'l Neru va Nilufar mukofotlari laureati, sadoqat va "
                     "bahor kuychisi; nomidagi davlat mukofoti ta'sis etilgan.",
               'ru': 'Народная поэтесса Узбекистана, символ верности и женской мудрости («Весна пришла, тебя '
                     'окликнув»); в её честь учреждена Госпремия.',
               'en': 'National Poet of Uzbekistan, international Lotus Prize laureate, celebrated for her lyrics of '
                     'spring and devotion; a prestigious state award bears her name.'},
  'aliases': ['zulfiya', 'zulfiya isroilova', 'зульфия']},
 {'id': 'lit_auth_013',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Erkin Vohidov', 'Abdulla Oripov', 'Muhammad Yusuf', 'Rauf Parfi'],
              'ru': ['Эркин Вахидов', 'Абдулла Арипов', 'Мухаммад Юсуф', 'Рауф Парфи'],
              'en': ['Erkin Vohidov', 'Abdulla Oripov', 'Muhammad Yusuf', 'Rauf Parfi']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Erkin Vohidov', 'ru': 'Эркин Вахидов', 'en': 'Erkin Vohidov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Erkin_Vohidov.jpg',
  'fun_fact': {'uz': "O'zbekiston Qahramoni, xalq shoiri, «O'zbegim» qasidasi, «Ruhlar isyoni» dostoni, «Oltin devor» "
                     'komediyasi muallifi va Gyotening «Faust»ini tarjima qilgan ulkan ijodkor.',
               'ru': 'Герой Узбекистана, народный поэт, автор поэмы «Узбегим» и трагедии «Восстание бессмертных», '
                     'автор непревзойдённого перевода «Фауста» Гёте.',
               'en': "Hero of Uzbekistan, poet, statesman, author of the ode 'O'zbegim' and master translator of "
                     "Goethe's 'Faust' into Uzbek."},
  'aliases': ['erkin vohidov', 'vohidov', 'эркин вахидов', 'вахидов']},
 {'id': 'lit_auth_014',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Erkin Vohidov', 'Abdulla Oripov', 'Shavkat Rahmon', 'Usmon Azim'],
              'ru': ['Эркин Вахидов', 'Абдулла Арипов', 'Шавкат Рахмон', 'Усман Азим'],
              'en': ['Erkin Vohidov', 'Abdulla Oripov', 'Shavkat Rahmon', 'Usmon Azim']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Abdulla Oripov', 'ru': 'Абдулла Арипов', 'en': 'Abdulla Oripov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/64/Abdulla_Oripov.jpg',
  'fun_fact': {'uz': "O'zbekiston Qahramoni, xalq shoiri, O'zbekiston Respublikasi Davlat madhiyasi matni muallifi "
                     'hamda Dantening «Ilohiy komediya»sini tarjima qilgan buyuk shoir.',
               'ru': 'Герой Узбекистана, народный поэт, автор текста Государственного гимна Узбекистана и гениального '
                     'перевода «Божественной комедии» Данте.',
               'en': "Hero of Uzbekistan, author of the lyrics of Uzbekistan's National Anthem, and translator of "
                     "Dante's 'Divine Comedy'."},
  'aliases': ['abdulla oripov', 'oripov', 'абдулла арипов', 'арипов']},
 {'id': 'lit_auth_015',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ["O'tkir Hoshimov", 'Shukur Xolmirzayev', 'Said Ahmad', 'Tohir Malik'],
              'ru': ['Уткир Хашимов', 'Шукур Холмирзаев', 'Саид Ахмад', 'Тохир Малик'],
              'en': ["O'tkir Hoshimov", 'Shukur Kholmirzaev', 'Said Ahmad', 'Tohir Malik']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Said Ahmad', 'ru': 'Саид Ахмад', 'en': 'Said Ahmad'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Said_Ahmad.jpg',
  'fun_fact': {'uz': "O'zbekiston Qahramoni, xalq yozuvchisi, mashhur «Ufq» trilogiyasi va «Kelinlar qo'zg'oloni» "
                     "komediyasi muallifi; Saida Zunnunovaning umr yo'ldoshi.",
               'ru': 'Герой Узбекистана, мастер юмора и эпической прозы, автор монументальной трилогии «Горизонт» и '
                     'пьесы «Бунт невесток».',
               'en': "Hero of Uzbekistan, novelist and satirist, creator of the 'Horizon' trilogy and legendary "
                     "theatrical hit 'The Revolt of the Daughters-in-Law'."},
  'aliases': ['said ahmad', 'саид ахмад']},
 {'id': 'lit_auth_016',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Said Ahmad', "O'lmas Umarbekov", "Tog'ay Murod", "O'tkir Hoshimov"],
              'ru': ['Саид Ахмад', 'Ульмас Умарбеков', 'Тогай Мурад', 'Уткир Хашимов'],
              'en': ['Said Ahmad', "O'lmas Umarbekov", 'Toghay Murad', "O'tkir Hoshimov"]},
  'correct_index': 3,
  'correct_answer': {'uz': "O'tkir Hoshimov", 'ru': 'Уткир Хашимов', 'en': "O'tkir Hoshimov"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ee/O%27tkir_Hoshimov.jpg',
  'fun_fact': {'uz': "O'zbekiston xalq yozuvchisi, «Dunyoning ishlari», «Ikki eshik orasi», «Tushda kechgan umrlar» "
                     'romanlari va «Daftar hoshiyasidagi bitiklar» aforizmlari muallifi.',
               'ru': 'Народный писатель Узбекистана, автор любимых романов «Дела земные», «Между двух дверей» и '
                     'философских заметок на полях.',
               'en': "People's Writer of Uzbekistan, renowned for deeply humanitarian novels including 'Between Two "
                     "Doors' and 'Affairs of this World'."},
  'aliases': ["o'tkir hoshimov", 'уткир хашимов', 'otkir hoshimov']},
 {'id': 'lit_auth_017',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ["Tog'ay Murod", 'Shukur Xolmirzayev', "Erkin A'zam", "Murod Muhammad Do'st"],
              'ru': ['Тогай Мурад', 'Шукур Холмирзаев', 'Эркин Агзам', 'Мурад Мухаммад Дост'],
              'en': ['Toghay Murad', 'Shukur Kholmirzaev', "Erkin A'zam", 'Murod Muhammad Dost']},
  'correct_index': 0,
  'correct_answer': {'uz': "Tog'ay Murod", 'ru': 'Тогай Мурад', 'en': 'Toghay Murad'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/23/Tog%27ay_Murod.jpg',
  'fun_fact': {'uz': "O'zbekiston xalq yozuvchisi, «Ot kishnagan oqshom», «Oydinda yurgan odamlar», «Otamdan qolgan "
                     'dalalar» kabi betakror dostonmonand qissalar muallifi.',
               'ru': 'Народный писатель Узбекистана, создатель уникального фольклорно-песенного стиля в прозе («Вечер, '
                     'когда ржал конь», «Поля, оставшиеся от отца»).',
               'en': "Celebrated Uzbek novelist whose rhythmic, poetic style captured rural pastoral life in 'The "
                     "Evening the Horse Neighed'."},
  'aliases': ["tog'ay murod", 'тогай мурад', 'toghay murad']},
 {'id': 'lit_auth_018',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Shavkat Rahmon', 'Muhammad Yusuf', 'Rauf Parfi', 'Matnazar Abdulhakim'],
              'ru': ['Шавкат Рахмон', 'Мухаммад Юсуф', 'Рауф Парфи', 'Матназар Абдулхаким'],
              'en': ['Shavkat Rahmon', 'Muhammad Yusuf', 'Rauf Parfi', 'Matnazar Abdulhakim']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Muhammad Yusuf', 'ru': 'Мухаммад Юсуф', 'en': 'Muhammad Yusuf'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/69/Muhammad_Yusuf.jpg',
  'fun_fact': {'uz': "O'zbekiston xalq shoiri, xalqning eng sevimli lirik shoirlaridan biri, Vatan, ona, yor haqidagi "
                     "yuzlab qo'shiqlar matni muallifi.",
               'ru': 'Всенародно любимый узбекский лирик, автор сотен песен о любви, матери и Родине («Был я '
                     'мальчишкой босоногим...»).',
               'en': 'Beloved contemporary Uzbek lyric poet whose heartfelt verses on motherland, mother, and romance '
                     'became ubiquitous folk songs.'},
  'aliases': ['muhammad yusuf', 'мухаммад юсуф']},
 {'id': 'lit_auth_019',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Anvar Obidjon', "Po'lat Mo'min", "Xudoyberdi To'xtaboyev", 'Quddus Muhammadiy'],
              'ru': ['Анвар Обиджан', 'Пулат Мумин', 'Худайберды Тухтабаев', 'Куддус Мухаммади'],
              'en': ['Anvar Obidjon', 'Pulat Mumin', 'Khudoyberdi Tukhtabayev', 'Quddus Muhammadi']},
  'correct_index': 2,
  'correct_answer': {'uz': "Xudoyberdi To'xtaboyev", 'ru': 'Худайберды Тухтабаев', 'en': 'Khudoyberdi Tukhtabayev'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Xudoyberdi_To%27xtaboyev.jpg',
  'fun_fact': {'uz': "O'zbekiston xalq yozuvchisi, bolalar adabiyotining ulug' namoyandasi, «Sariq devni minib», "
                     "«Shirin qovunlar mamlakati», «Mungli ko'zlar» asarlari muallifi.",
               'ru': 'Классик узбекской детской литературы, автор книг о Хашимджане («Верхом на жёлтом диве»), '
                     'переведённых во многих странах мира.',
               'en': "Master of Uzbek children's literature, creator of the mischievous Hoshimjon in 'Riding the "
                     "Yellow Giant'."},
  'aliases': ["xudoyberdi to'xtaboyev", 'тухтабаев', 'худайберды тухтабаев']},
 {'id': 'lit_auth_020',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ["O'lmas Umarbekov", 'Muxtor Avezov', 'Sobir Ahmadqulov', 'Chingiz Aytmatov'],
              'ru': ['Ульмас Умарбеков', 'Мухтар Ауэзов', 'Сабир Ахмадкулов', 'Чингиз Айтматов'],
              'en': ["O'lmas Umarbekov", 'Mukhtar Auezov', 'Sobir Ahmadqulov', 'Chingiz Aitmatov']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Chingiz Aytmatov', 'ru': 'Чингиз Айтматов', 'en': 'Chingiz Aitmatov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/03/Chinghiz_Aitmatov_%281984%29.jpg',
  'fun_fact': {'uz': "Qirg'iziston xalq yozuvchisi, jahon adabiyoti klassigi, «Jamila», «Oq kema», «Asrga tatigulik "
                     'kun», «Kunda» asarlari muallifi.',
               'ru': 'Всемирно известный писатель, классик советской и мировой литературы, дипломат; автор «Белого '
                     'парохода» и термина «манкурт».',
               'en': "World-renowned Kyrgyz and Russian author and diplomat whose novels 'The White Ship' and 'Jamila' "
                     'are translated into over 150 languages.'},
  'aliases': ['chingiz aytmatov', 'aytmatov', 'чингиз айтматов', 'айтматов', 'aitmatov']},
 {'id': 'lit_auth_021',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Uilyam Shekspir', 'Kristofer Marlo', 'Jon Milton', 'Ben Jonson'],
              'ru': ['Уильям Шекспир', 'Кристофер Марло', 'Джон Мильтон', 'Бен Джонсон'],
              'en': ['William Shakespeare', 'Christopher Marlowe', 'John Milton', 'Ben Jonson']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Uilyam Shekspir', 'ru': 'Уильям Шекспир', 'en': 'William Shakespeare'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg',
  'fun_fact': {'uz': "Ingliz dramaturgiyasining buyuk dahosi, Stratferd-apon-Eyvonda tug'ilgan; 38 ta pesa, 154 ta "
                     'sonet muallifi («Hamlet», «Romeo va Juletta», «Otello»).',
               'ru': 'Величайший англоязычный драматург эпохи Возрождения («Эйвонский лебедь»), автор «Гамлета», '
                     '«Короля Лира» и 154 сонетов.',
               'en': "England's national poet and the 'Bard of Avon', widely considered the greatest dramatist of the "
                     'English language.'},
  'aliases': ['shekspir', 'uilyam shekspir', 'шекспир', 'shakespeare', 'william shakespeare']},
 {'id': 'lit_auth_022',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Lope de Vega', 'Migel de Servantes', 'Pedro Kalderon', 'Fransisko Kevedo'],
              'ru': ['Лопе де Вега', 'Мигель де Сервантес Сааведра', 'Педро Кальдерон', 'Франсиско де Кеведо'],
              'en': ['Lope de Vega', 'Miguel de Cervantes', 'Pedro Calderón de la Barca', 'Francisco de Quevedo']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Migel de Servantes', 'ru': 'Мигель де Сервантес Сааведра', 'en': 'Miguel de Cervantes'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/09/Cervantes_J%C3%A1uregui.jpg',
  'fun_fact': {'uz': "Buyuk ispan yozuvchisi, Lepanto dengiz jangida chap qo'lidan ayrilgan qahramon; zamonaviy roman "
                     'janrining ilk durdonasi «Don Kixot» muallifi.',
               'ru': 'Испанский гений («однорукий из Лепанто»), создатель бессмертного образа рыцаря печального образа '
                     'Дон Кихота Ламанчского.',
               'en': "Giant of Spanish literature wounded at Lepanto; author of 'Don Quixote', widely cited as the "
                     'first modern Western novel.'},
  'aliases': ['servantes', 'migel de servantes', 'сервантес', 'cervantes']},
 {'id': 'lit_auth_023',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Franchesko Petrarka', 'Jovanni Bokkachcho', 'Dante Aligyeri', 'Nikkolo Makiavelli'],
              'ru': ['Франческо Петрарка', 'Джованни Боккаччо', 'Данте Алигьери', 'Никколо Макиавелли'],
              'en': ['Petrarch', 'Giovanni Boccaccio', 'Dante Alighieri', 'Niccolò Machiavelli']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Dante Aligyeri', 'ru': 'Данте Алигьери', 'en': 'Dante Alighieri'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/6f/Portrait_de_Dante.jpg',
  'fun_fact': {'uz': "Florensiyalik daho, italyan adabiy tilining otasi, sevikli Beatrichesiga bag'ishlangan "
                     'monumental «Ilohiy komediya» muallifi.',
               'ru': 'Великий итальянский поэт эпохи Предвозрождения, автор монументальной «Божественной комедии» и '
                     '«Новой жизни».',
               'en': 'Florentine poet who established the Italian vernacular in literature with his monumental '
                     "theological epic 'The Divine Comedy'."},
  'aliases': ['dante', 'dante aligyeri', 'данте', 'данте алигьери']},
 {'id': 'lit_auth_024',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Fridrix Shiller', 'Genrix Geyne', 'Tomas Mann', 'Iogann Volfgang fon Gyote'],
              'ru': ['Фридрих Шиллер', 'Генрих Гейне', 'Томас Манн', 'Иоганн Вольфганг фон Гёте'],
              'en': ['Friedrich Schiller', 'Heinrich Heine', 'Thomas Mann', 'Johann Wolfgang von Goethe']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Iogann Volfgang fon Gyote',
                     'ru': 'Иоганн Вольфганг фон Гёте',
                     'en': 'Johann Wolfgang von Goethe'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Goethe_%28Stieler_1828%29.jpg',
  'fun_fact': {'uz': "Nemis Uyg'onish davrining eng buyuk mutafakkiri, shoir, davlat arbobi va tabiatshunos olimi; "
                     'butun umri davomida yaratgan shoh asari — «Faust» tragediyasi.',
               'ru': 'Титан немецкого Просвещения, поэт, учёный-естествоиспытатель и государственный деятель в '
                     'Веймаре, автор трагедии «Фауст».',
               'en': 'Supreme figure of German literature and Weimar Classicism, polymath, statesman, and creator of '
                     "the monumental dramatic poem 'Faust'."},
  'aliases': ['gyote', 'гёте', 'goethe', 'johann wolfgang von goethe']},
 {'id': 'lit_auth_025',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Viktor Gyugo', 'Aleksandr Dyuma', 'Onore de Balzak', 'Gustav Flober'],
              'ru': ['Виктор Гюго', 'Александр Дюма', 'Оноре де Бальзак', 'Гюстав Флобер'],
              'en': ['Victor Hugo', 'Alexandre Dumas', 'Honoré de Balzac', 'Gustave Flaubert']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Viktor Gyugo', 'ru': 'Виктор Гюго', 'en': 'Victor Hugo'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/14/Victor_Hugo_by_%C3%89tienne_Carjat_1876_-_crop.jpg',
  'fun_fact': {'uz': "Fransuz romantizmining yetakchisi, «Parij Bibi Maryam ibodatxonasi», «Xo'rlanganlar» va "
                     '«Kulayotgan odam» romanlari muallifi.',
               'ru': 'Вождь французского романтизма, гуманист, автор «Отверженных», «Собора Парижской Богоматери» и '
                     'пламенный борец за отмену смертной казни.',
               'en': "Leader of the French Romantic movement and humanitarian advocate, famous for 'Les Misérables' "
                     "and 'The Hunchback of Notre-Dame'."},
  'aliases': ['gyugo', 'viktor gyugo', 'гюго', 'виктор гюго', 'victor hugo']},
 {'id': 'lit_auth_026',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Viktor Gyugo', 'Aleksandr Dyuma (ota)', 'Jyul Vern', 'Onore de Balzak'],
              'ru': ['Виктор Гюго', 'Александр Дюма-отец', 'Жюль Верн', 'Оноре де Бальзак'],
              'en': ['Victor Hugo', 'Alexandre Dumas (père)', 'Jules Verne', 'Honoré de Balzac']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Aleksandr Dyuma (ota)', 'ru': 'Александр Дюма-отец', 'en': 'Alexandre Dumas (père)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ea/Alexandre_Dumas_by_Nadar%2C_1855.jpg',
  'fun_fact': {'uz': 'Tarixiy sarguzasht janrining tengsiz qiroli, «Uch mushketyor», «Graf Monte-Kristo» va «Qirolicha '
                     'Margo» romanlari muallifi.',
               'ru': 'Один из самых читаемых французских авторов в истории, создатель «Трёх мушкетёров» и «Графа '
                     'Монте-Кристо».',
               'en': "Prolific French historical adventure master whose works including 'The Three Musketeers' and "
                     "'The Count of Monte Cristo' have been translated into nearly 100 languages."},
  'aliases': ['dyuma', 'aleksandr dyuma', 'дюма', 'alexandre dumas']},
 {'id': 'lit_auth_027',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Uilyam Tekkerey', 'Artur Konan Doyl', 'Charlz Dikkens', 'Tomas Hardi'],
              'ru': ['Уильям Теккерей', 'Артур Конан Дойл', 'Чарльз Диккенс', 'Томас Гарди'],
              'en': ['William Makepeace Thackeray', 'Arthur Conan Doyle', 'Charles Dickens', 'Thomas Hardy']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Charlz Dikkens', 'ru': 'Чарльз Диккенс', 'en': 'Charles Dickens'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/a/aa/Dickens_Gurney_head.jpg',
  'fun_fact': {'uz': 'Viktoriya davri Angliyasining eng buyuk romannavisi, «Oliver Tvist», «Devid Kopperfild», «Ikki '
                     "shahar qissasi» va «Rojdestvo qo'shig'i» muallifi.",
               'ru': 'Величайший английский писатель викторианской эпохи, мастер ярких характеров («Оливер Твист», '
                     '«Рождественская песнь»).',
               'en': "Definitive Victorian novelist whose unforgettable characters in 'Oliver Twist' and 'Great "
                     "Expectations' championed social reform."},
  'aliases': ['dikkens', 'charlz dikkens', 'диккенс', 'charles dickens']},
 {'id': 'lit_auth_028',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Sharlotta Bronte', 'Emili Bronte', 'Meri Shelli', 'Jeyn Ostin'],
              'ru': ['Шарлотта Бронте', 'Эмили Бронте', 'Мэри Шелли', 'Джейн Остин'],
              'en': ['Charlotte Brontë', 'Emily Brontë', 'Mary Shelley', 'Jane Austen']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jeyn Ostin', 'ru': 'Джейн Остин', 'en': 'Jane Austen'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/cc/CassandraAusten-JaneAusten%28c.1810%29_hires.jpg',
  'fun_fact': {'uz': "Ingliz adabiyotida nozik kinoya va oilaviy munosabatlar ustasi, «G'urur va andisha», «Aql va "
                     'hislar», «Emma» romanlari muallifi.',
               'ru': 'Классик английской литературы, создательница социально-психологических шедевров «Гордость и '
                     'предубеждение» и «Эмма».',
               'en': "Renowned English novelist whose wit, irony, and social realism in 'Pride and Prejudice' cemented "
                     'her among the giants of world literature.'},
  'aliases': ['jeyn ostin', 'ostin', 'джейн остин', 'остин', 'jane austen']},
 {'id': 'lit_auth_029',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Mark Tven (Semuel Klemens)', 'Jek London', 'Edgar Allan Po', 'O. Genri'],
              'ru': ['Марк Твен (Сэмюэл Клеменс)', 'Джек Лондон', 'Эдгар Аллан По', 'О. Генри'],
              'en': ['Mark Twain (Samuel Clemens)', 'Jack London', 'Edgar Allan Poe', 'O. Henry']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Mark Tven (Semuel Klemens)',
                     'ru': 'Марк Твен (Сэмюэл Клеменс)',
                     'en': 'Mark Twain (Samuel Clemens)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/0c/Mark_Twain_by_AF_Bradley.jpg',
  'fun_fact': {'uz': "«Amerika adabiyotining otasi» (Xeminguey ta'rifi), Missisipi daryosi bo'yidagi Tom Soyer va "
                     'Geklberri Finn sarguzashtlari yaratuvchisi.',
               'ru': '«Отец американской литературы», лоцман на Миссисипи, непревзойдённый юморист и автор '
                     '«Приключений Тома Сойера».',
               'en': "Celebrated as the 'father of American literature', famous for his Mississippian classics 'The "
                     "Adventures of Tom Sawyer' and 'Huckleberry Finn'."},
  'aliases': ['mark tven', 'tven', 'марк твен', 'mark twain', 'samuel clemens']},
 {'id': 'lit_auth_030',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Govard Lavkraft', 'Edgar Allan Po', 'Artur Konan Doyl', 'Brem Stoker'],
              'ru': ['Говард Лавкрафт', 'Эдгар Аллан По', 'Артур Конан Дойл', 'Брэм Стокер'],
              'en': ['H.P. Lovecraft', 'Edgar Allan Poe', 'Arthur Conan Doyle', 'Bram Stoker']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Edgar Allan Po', 'ru': 'Эдгар Аллан По', 'en': 'Edgar Allan Poe'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/75/Edgar_Allan_Poe_2_edit.jpg',
  'fun_fact': {'uz': "Zamonaviy detektiv janri (Ogyust Dyupen) va psixologik qo'rqinchli adabiyotning asoschisi, "
                     "«Qarg'a» dostoni muallifi.",
               'ru': 'Родоначальник детективного жанра и психологического триллера, мастер готической новеллы и автор '
                     'культовой поэмы «Ворон».',
               'en': "Pioneer of the modern detective story and master of macabre short fiction, famous for 'The "
                     "Raven' and 'The Tell-Tale Heart'."},
  'aliases': ['edgar po', 'edgar allan po', 'эдгар по', 'эдгар аллан по', 'edgar allan poe']},
 {'id': 'lit_auth_031',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Agata Kristi', 'Edgar Allan Po', 'Artur Konan Doyl', 'Robert Lyuis Stivenson'],
              'ru': ['Агата Кристи', 'Эдгар Аллан По', 'Артур Конан Дойл', 'Роберт Льюис Стивенсон'],
              'en': ['Agatha Christie', 'Edgar Allan Poe', 'Arthur Conan Doyle', 'Robert Louis Stevenson']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Artur Konan Doyl', 'ru': 'Артур Конан Дойл', 'en': 'Arthur Conan Doyle'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b5/Arthur_Conan_Doyle_by_Herbert_Rose_Barraud_1893.jpg',
  'fun_fact': {'uz': 'Shotlandiyalik shifokor va yozuvchi, afsonaviy xufiya Sherlok Xolms va doktor Vatson obrazlari '
                     'yaratuvchisi.',
               'ru': 'Британский врач и писатель, создавший бессмертный дуэт гениального сыщика Шерлока Холмса и '
                     'доктора Ватсона.',
               'en': "British physician and writer who created the world's most famous consulting detective, Sherlock "
                     'Holmes of 221B Baker Street.'},
  'aliases': ['konan doyl', 'artur konan doyl', 'конан дойл', 'arthur conan doyle']},
 {'id': 'lit_auth_032',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Gerbert Uells', 'Aleksandr Belyayev', 'Aleksandr Dyuma', 'Jyul Vern'],
              'ru': ['Герберт Уэллс', 'Александр Беляев', 'Александр Дюма', 'Жюль Верн'],
              'en': ['H.G. Wells', 'Alexander Belyaev', 'Alexandre Dumas', 'Jules Verne']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jyul Vern', 'ru': 'Жюль Верн', 'en': 'Jules Verne'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/77/F%C3%A9lix_Nadar_1820-1910_portraits_Jules_Verne.jpg',
  'fun_fact': {'uz': "Ilmiy fantastika janrining otasi; suvosti kemasi, oyga uchish va vertolyotlarni o'z asarlarida "
                     "bashorat qilgan («Suv ostida 20 000 lye», «Sakson kunda yer yuzi bo'ylab»).",
               'ru': '«Отец научной фантастики», предсказавший появление подводных лодок, полётов на Луну и аквалангов '
                     'в серии «Необыкновенные путешествия».',
               'en': "French pioneer of science fiction whose 'Extraordinary Voyages' predicted submarines, space "
                     'travel, and helicopters long before they existed.'},
  'aliases': ['jyul vern', 'жюль верн', 'jules verne']},
 {'id': 'lit_auth_033',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Lev Tolstoy', 'Fyodor Dostoevskiy', 'Ivan Turgenev', 'Anton Chexov'],
              'ru': ['Лев Толстой', 'Фёдор Достоевский', 'Иван Тургенев', 'Антон Чехов'],
              'en': ['Leo Tolstoy', 'Fyodor Dostoevsky', 'Ivan Turgenev', 'Anton Chekhov']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Lev Tolstoy', 'ru': 'Лев Толстой', 'en': 'Leo Tolstoy'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c6/L.N.Tolstoy_Prokudin-Gorsky.jpg',
  'fun_fact': {'uz': 'Yasnaya Polyana grafligi egasi, buyuk mutafakkir va romannavis, «Urush va tinchlik», «Anna '
                     'Karenina» va «Tirilish» epopeyalari muallifi.',
               'ru': 'Один из величайших писателей мира, граф из Ясной Поляны, автор «Войны и мира», мыслитель и '
                     'проповедник ненасильственного сопротивления.',
               'en': 'Master of realistic fiction from Yasnaya Polyana whose philosophical ideals of nonviolent '
                     'resistance influenced Gandhi and Martin Luther King Jr.'},
  'aliases': ['lev tolstoy', 'tolstoy', 'лев толстой', 'толстой', 'leo tolstoy']},
 {'id': 'lit_auth_034',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Lev Tolstoy', 'Fyodor Dostoevskiy', 'Nikolay Gogol', 'Ivan Goncharov'],
              'ru': ['Лев Толстой', 'Фёдор Достоевский', 'Николай Гоголь', 'Иван Гончаров'],
              'en': ['Leo Tolstoy', 'Fyodor Dostoevsky', 'Nikolai Gogol', 'Ivan Goncharov']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Fyodor Dostoevskiy', 'ru': 'Фёдор Достоевский', 'en': 'Fyodor Dostoevsky'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/78/Vasily_Perov_-_%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%D0%A4.%D0%9C.%D0%94%D0%BE%D1%81%D1%82%D0%BE%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_-_Google_Art_Project.jpg',
  'fun_fact': {'uz': 'Inson ruhiyati va vijdoni qarama-qarshiliklarini chuqur tadqiq etgan daho; «Jinoyat va jazo», '
                     '«Aka-uka Karamazovlar», «Idiot» romanlari muallifi.',
               'ru': 'Великий знаток глубин человеческой души, философ-экзистенциалист («Преступление и наказание», '
                     '«Братья Карамазовы», «Бесы»).',
               'en': 'Literary titan exploring the psychological depths of human suffering and spiritual redemption in '
                     "'Crime and Punishment' and 'The Brothers Karamazov'."},
  'aliases': ['dostoevskiy', 'fyodor dostoevskiy', 'достоевский', 'фёдор достоевский', 'dostoevsky']},
 {'id': 'lit_auth_035',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Mixail Lermontov', 'Vasiliy Jukovskiy', 'Aleksandr Pushkin', 'Nikolay Nekrasov'],
              'ru': ['Михаил Лермонтов', 'Василий Жуковский', 'Александр Пушкин', 'Николай Некрасов'],
              'en': ['Mikhail Lermontov', 'Vasily Zhukovsky', 'Alexander Pushkin', 'Nikolay Nekrasov']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Aleksandr Pushkin', 'ru': 'Александр Пушкин', 'en': 'Alexander Pushkin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Alexander_Pushkin_by_Orest_Kiprensky.jpg',
  'fun_fact': {'uz': "Zamonaviy rus adabiy tilining asoschisi, «Yevgeniy Onegin» she'riy romani, «Kapitan qizi» va "
                     "o'nlab mashhur ertaklar muallifi; duelda halok bo'lgan.",
               'ru': '«Солнце русской поэзии», создатель современного русского литературного языка, автор романа в '
                     'стихах «Евгений Онегин».',
               'en': "Founder of modern Russian literature, poet of genius who penned 'Eugene Onegin' and fell in a "
                     'fatal duel at age 37.'},
  'aliases': ['pushkin', 'aleksandr pushkin', 'пушкин', 'александр пушкин']},
 {'id': 'lit_auth_036',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Maksim Gorkiy', 'Ivan Bunin', 'Nikolay Gogol', 'Anton Chexov'],
              'ru': ['Максим Горький', 'Иван Бунин', 'Николай Гоголь', 'Антон Чехов'],
              'en': ['Maxim Gorky', 'Ivan Bunin', 'Nikolai Gogol', 'Anton Chekhov']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Anton Chexov', 'ru': 'Антон Чехов', 'en': 'Anton Chekhov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/71/Chekhov_1898_by_Osip_Braz.jpg',
  'fun_fact': {'uz': "Kasbi shifokor bo'lgan buyuk dramaturg va hikoyanavis, qisqalik va lirik dramatizm ustasi "
                     "(«Chayka», «Vanya tog'a», «Olchazor»).",
               'ru': 'Врач по профессии, драматург-реформатор мирового театра («Вишнёвый сад», «Чайка», «Три сестры») '
                     'и мастер короткого рассказа.',
               'en': 'Practicing physician and master playwright whose understated realism transformed modern world '
                     "drama ('The Cherry Orchard', 'The Seagull')."},
  'aliases': ['chexov', 'anton chexov', 'чехов', 'антон чехов', 'chekhov']},
 {'id': 'lit_auth_037',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Nikolay Gogol', 'Ivan Turgenev', 'Mixail Saltikov-Shedrin', 'Aleksandr Ostrovskiy'],
              'ru': ['Николай Гоголь', 'Иван Тургенев', 'Михаил Салтыков-Щедрин', 'Александр Островский'],
              'en': ['Nikolai Gogol', 'Ivan Turgenev', 'Mikhail Saltykov-Shchedrin', 'Alexander Ostrovsky']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Nikolay Gogol', 'ru': 'Николай Гоголь', 'en': 'Nikolai Gogol'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/58/N.V.Gogol_by_F.Moller_%281840%2C_Tretyakov_gallery%29_CROPPED.jpg',
  'fun_fact': {'uz': "Grotesk, satira va mistika ustasi, «Revizor», «O'lik jonlar», «Taras Bulba» va «Shinel» asarlari "
                     'muallifi.',
               'ru': 'Классик комедии и мистического гротеска, автор поэмы «Мёртвые души», комедии «Ревизор» и повести '
                     '«Шинель».',
               'en': "Ukrainian-born master of satirical surrealism and grotesque realism, author of 'Dead Souls' and "
                     "'The Government Inspector'."},
  'aliases': ['gogol', 'nikolay gogol', 'гоголь', 'николай гоголь']},
 {'id': 'lit_auth_038',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Aleksandr Pushkin', 'Mixail Lermontov', 'Fyodor Tyutchev', 'Afanasiy Fet'],
              'ru': ['Александр Пушкин', 'Михаил Лермонтов', 'Фёдор Тютчев', 'Афанасий Фет'],
              'en': ['Alexander Pushkin', 'Mikhail Lermontov', 'Fyodor Tyutchev', 'Afanasy Fet']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Mixail Lermontov', 'ru': 'Михаил Лермонтов', 'en': 'Mikhail Lermontov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e0/Mikhail_Lermontov_by_Zabolotskiy_%281837%29.jpg',
  'fun_fact': {'uz': "Romantizm daho vakili, 26 yoshida duelda halok bo'lgan shoir; «Zamonamiz qahramoni» ilk rus "
                     'psixologik romani va «Mtsiri» dostonining muallifi.',
               'ru': 'Гений романтической поэзии, погибший на дуэли в 26 лет; автор первого русского психологического '
                     'романа «Герой нашего времени».',
               'en': "Romantic genius who fell in a duel at age 26, leaving behind 'A Hero of Our Time', Russia's "
                     'first major psychological novel.'},
  'aliases': ['lermontov', 'mixail lermontov', 'лермонтов', 'михаил лермонтов']},
 {'id': 'lit_auth_039',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Lev Tolstoy', 'Ivan Goncharov', 'Ivan Turgenev', 'Nikolay Leskov'],
              'ru': ['Лев Толстой', 'Иван Гончаров', 'Иван Тургенев', 'Николай Лесков'],
              'en': ['Leo Tolstoy', 'Ivan Goncharov', 'Ivan Turgenev', 'Nikolai Leskov']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Ivan Turgenev', 'ru': 'Иван Тургенев', 'en': 'Ivan Turgenev'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Ivan_Turgenev_by_Ilya_Repin.jpg',
  'fun_fact': {'uz': "Yevropada birinchi bo'lib tan olingan rus klassigi, «Ovchining xotiralari», «Otalar va bolalar» "
                     'romani (Bazarov obrazi) yaratuvchisi.',
               'ru': 'Тончайший стилист русского языка, познакомивший Западную Европу с русской культурой; автор '
                     'романов «Отцы и дети» и «Дворянское гнездо».',
               'en': 'Novelist who popularized Russian literature abroad, creator of the iconic generational clash in '
                     "'Fathers and Sons'."},
  'aliases': ['turgenev', 'ivan turgenev', 'тургенев', 'иван тургенев']},
 {'id': 'lit_auth_040',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Anton Chexov', 'Vladimir Mayakovskiy', 'Mixail Sholoxov', 'Maksim Gorkiy (Aleksey Peshkov)'],
              'ru': ['Антон Чехов', 'Владимир Маяковский', 'Михаил Шолохов', 'Максим Горький (Алексей Пешков)'],
              'en': ['Anton Chekhov', 'Vladimir Mayakovsky', 'Mikhail Sholokhov', 'Maxim Gorky (Alexei Peshkov)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Maksim Gorkiy (Aleksey Peshkov)',
                     'ru': 'Максим Горький (Алексей Пешков)',
                     'en': 'Maxim Gorky (Alexei Peshkov)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/86/Maxim_Gorky_1906.jpg',
  'fun_fact': {'uz': "Sotsialistik realizm adabiyotining asoschisi, «Ona» romani, «Tubanlikda» dramasi va «Bo'ron "
                     "qushi haqida qo'shiq» muallifi.",
               'ru': 'Буревестник революции, пятикратный номинант на Нобелевскую премию, автор драмы «На дне» и романа '
                     '«Мать».',
               'en': 'Founder of Socialist Realism, five-time Nobel nominee, famous for plays depicting outcasts such '
                     "as 'The Lower Depths'."},
  'aliases': ['gorkiy', 'maksim gorkiy', 'горький', 'максим горький', 'maxim gorky']},
 {'id': 'lit_auth_041',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Mixail Bulgakov', 'Boris Pasternak', 'Vladimir Nabokov', 'Yevgeniy Zamyatin'],
              'ru': ['Михаил Булгаков', 'Борис Пастернак', 'Владимир Набоков', 'Евгений Замятин'],
              'en': ['Mikhail Bulgakov', 'Boris Pasternak', 'Vladimir Nabokov', 'Yevgeny Zamyatin']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Mixail Bulgakov', 'ru': 'Михаил Булгаков', 'en': 'Mikhail Bulgakov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Mikhail_Bulgakov_1930s.jpg',
  'fun_fact': {'uz': "Kiyevda tug'ilgan shifokor va yozuvchi, sehrli satira cho'qqisi bo'lgan «Usta va Margarita» "
                     'hamda «It yuragi» romanlari muallifi.',
               'ru': 'Автор бессмертного мистико-сатирического шедевра «Мастер и Маргарита», а также повестей «Собачье '
                     'сердце» и «Белая гвардия».',
               'en': "Kiev-born physician turned writer whose magnum opus 'The Master and Margarita' was published "
                     'posthumously to worldwide acclaim.'},
  'aliases': ['bulgakov', 'mixail bulgakov', 'булгаков', 'михаил булгаков', 'mikhail bulgakov']},
 {'id': 'lit_auth_042',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Osip Mandelshtam', 'Boris Pasternak', 'Iosif Brodskiy', 'Mixail Bulgakov'],
              'ru': ['Осип Мандельштам', 'Борис Пастернак', 'Иосиф Бродский', 'Михаил Булгаков'],
              'en': ['Osip Mandelstam', 'Boris Pasternak', 'Joseph Brodsky', 'Mikhail Bulgakov']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Boris Pasternak', 'ru': 'Борис Пастернак', 'en': 'Boris Pasternak'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/29/Boris_Pasternak_1934.jpg',
  'fun_fact': {'uz': "1958 yilda «Doktor Jivago» romani uchun Nobel mukofotiga sazovor bo'lgan, ammo sovet hukumati "
                     'tazyiqi ostida undan voz kechishga majbur qilingan shoir.',
               'ru': 'Лауреат Нобелевской премии по литературе 1958 года за роман «Доктор Живаго», от которой был '
                     'вынужден отказаться под угрозой высылки.',
               'en': "Poet and novelist awarded the 1958 Nobel Prize for 'Doctor Zhivago', which he was forced by "
                     'Soviet authorities to decline.'},
  'aliases': ['pasternak', 'boris pasternak', 'пастернак', 'борис пастернак']},
 {'id': 'lit_auth_043',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Emili Bronte', 'Jeyn Ostin', 'Sharlotta Bronte', 'Meri Shelli'],
              'ru': ['Эмили Бронте', 'Джейн Остин', 'Шарлотта Бронте', 'Мэри Шелли'],
              'en': ['Emily Brontë', 'Jane Austen', 'Charlotte Brontë', 'Mary Shelley']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Sharlotta Bronte', 'ru': 'Шарлотта Бронте', 'en': 'Charlotte Brontë'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Charlotte_Bront%C3%AB_by_George_Richmond.jpg',
  'fun_fact': {'uz': "Karr Bell taxallusi bilan ijod qilgan, dunyoga mashhur «Jeyn Eyr» romani muallifi bo'lgan uch "
                     "yozuvchi opa-singil Bronte'larning to'ng'ichi.",
               'ru': 'Старшая из знаменитых сестёр-писательниц Бронте, автор новаторского романа «Джейн Эйр» (1847).',
               'en': "Eldest of the three Brontë literary sisters, author of the feminist Gothic masterpiece 'Jane "
                     "Eyre' (1847)."},
  'aliases': ['sharlotta bronte', 'bronte', 'шарлотта бронте', 'бронте', 'charlotte bronte']},
 {'id': 'lit_auth_044',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Sharlotta Bronte', 'Jorj Eliot', 'Jeyn Ostin', 'Emili Bronte'],
              'ru': ['Шарлотта Бронте', 'Джордж Элиот', 'Джейн Остин', 'Эмили Бронте'],
              'en': ['Charlotte Brontë', 'George Eliot', 'Jane Austen', 'Emily Brontë']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Emili Bronte', 'ru': 'Эмили Бронте', 'en': 'Emily Brontë'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Emily_Bront%C3%AB_by_Patrick_Branwell_Bront%C3%AB_restored.jpg',
  'fun_fact': {'uz': "Ellis Bell taxallusi bilan atigi 30 yil umr ko'rib yagona, ammo o'lmas «Momaqaldiroqli dovon» "
                     "romanini qoldirgan iste'dodli adiba.",
               'ru': 'Автор единственного, но признанного шедевром романа «Грозовой перевал» (1847), прожившая всего '
                     '30 лет.',
               'en': 'English novelist and poet who lived secluded in Yorkshire, writing a single incandescent '
                     "masterpiece: 'Wuthering Heights'."},
  'aliases': ['emili bronte', 'эмили бронте', 'emily bronte']},
 {'id': 'lit_auth_045',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Onore de Balzak', 'Stendal', 'Gustav Flober', 'Emil Zolya'],
              'ru': ['Оноре де Бальзак', 'Стендаль', 'Гюстав Флобер', 'Эмиль Золя'],
              'en': ['Honoré de Balzac', 'Stendhal', 'Gustave Flaubert', 'Émile Zola']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Onore de Balzak', 'ru': 'Оноре де Бальзак', 'en': 'Honoré de Balzac'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c8/Honor%C3%A9_de_Balzac_%281842%29_by_Daguerre_clean.jpg',
  'fun_fact': {'uz': '90 dan ortiq roman va qissalarni birlashtirgan ulkan «Inson komediyasi» epopeyasi yaratuvchisi '
                     '(«Gorio ota», «Yevgeniya Grande», «Shagren terisi»).',
               'ru': 'Титан французского реализма, создавший грандиозную 90-томную «Человеческую комедию», панораму '
                     'французского общества XIX века.',
               'en': "French realist novelist whose monumental multi-volume sequence 'La Comédie Humaine' offered an "
                     'exhaustive study of 19th-century society.'},
  'aliases': ['balzak', 'onore de balzak', 'бальзак', 'оноре де бальзак', 'honore de balzac']},
 {'id': 'lit_auth_046',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Onore de Balzak', 'Stendal (Anri Beyl)', 'Prosper Merime', 'Gi de Mopassan'],
              'ru': ['Оноре де Бальзак', 'Стендаль (Анри Бейль)', 'Проспер Мериме', 'Ги де Мопассан'],
              'en': ['Honoré de Balzac', 'Stendhal (Henri Beyle)', 'Prosper Mérimée', 'Guy de Maupassant']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Stendal (Anri Beyl)', 'ru': 'Стендаль (Анри Бейль)', 'en': 'Stendhal (Henri Beyle)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Stendhal_1840.jpg',
  'fun_fact': {'uz': 'Psixologik romanning asoschisi, «Qizil va qora» (Jyulen Sorel fojiasi) hamda «Parma '
                     'ibodatxonasi» romanlari muallifi.',
               'ru': 'Основоположник французского психологического романа, автор шедевров «Красное и чёрное» и '
                     '«Пармская обитель».',
               'en': "French pioneer of psychological realism, renowned for his acute analysis of character in 'The "
                     "Red and the Black'."},
  'aliases': ['stendal', 'стендаль', 'stendhal', 'henri beyle']},
 {'id': 'lit_auth_047',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Emil Zolya', 'Gi de Mopassan', 'Gustav Flober', 'Marsel Prust'],
              'ru': ['Эмиль Золя', 'Ги де Мопассан', 'Гюстав Флобер', 'Марсель Пруст'],
              'en': ['Émile Zola', 'Guy de Maupassant', 'Gustave Flaubert', 'Marcel Proust']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Gustav Flober', 'ru': 'Гюстав Флобер', 'en': 'Gustave Flaubert'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Gustave_Flaubert.jpg',
  'fun_fact': {'uz': "Badiiy uslubda 'yagona to'g'ri so'z' (le mot juste) talabchan ustasi, mashhur «Madam Bovari» va "
                     '«Salambo» romanlari muallifi.',
               'ru': 'Мастер безупречного литературного стиля («точное слово»), автор бессмертной психологической '
                     'драмы «Госпожа Бовари» (1856).',
               'en': "Leading exponent of literary realism in France, celebrated for his scrupulous search for 'le mot "
                     "juste' in 'Madame Bovary'."},
  'aliases': ['flober', 'gustav flober', 'флобер', 'гюстав флобер', 'gustave flaubert']},
 {'id': 'lit_auth_048',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Onore de Balzak', 'Gustav Flober', 'Alfons Dode', 'Gi de Mopassan'],
              'ru': ['Оноре де Бальзак', 'Гюстав Флобер', 'Альфонс Доде', 'Ги де Мопассан'],
              'en': ['Honoré de Balzac', 'Gustave Flaubert', 'Alphonse Daudet', 'Guy de Maupassant']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Gi de Mopassan', 'ru': 'Ги де Мопассан', 'en': 'Guy de Maupassant'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Guy_de_Maupassant_foto_nadar.jpg',
  'fun_fact': {'uz': 'Qisqa novella janrining buyuk fransuz ustasi, 300 ga yaqin hikoya hamda «Azizim» (Bel-Ami) va '
                     "«Do'ndiq» (Boule de Suif) asarlari muallifi.",
               'ru': 'Блестящий французский новеллист, ученик Флобера, автор 300 новелл («Пышка») и романа «Милый '
                     'друг».',
               'en': "French master of the short story, author of 300 concise tales including 'Boule de Suif' and the "
                     "cynical novel 'Bel-Ami'."},
  'aliases': ['mopassan', 'gi de mopassan', 'мопассан', 'ги де мопассан', 'guy de maupassant']},
 {'id': 'lit_auth_049',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Emil Zolya', 'Gustav Flober', 'Viktor Gyugo', 'Gi de Mopassan'],
              'ru': ['Эмиль Золя', 'Гюстав Флобер', 'Виктор Гюго', 'Ги де Мопассан'],
              'en': ['Émile Zola', 'Gustave Flaubert', 'Victor Hugo', 'Guy de Maupassant']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Emil Zolya', 'ru': 'Эмиль Золя', 'en': 'Émile Zola'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Emile_Zola_1902.jpg',
  'fun_fact': {'uz': 'Adabiyotdagi naturalizm oqimining yetakchisi, 20 jildlik «Rugon-Makkarlar» epopeyasi '
                     '(«Jerminal», «Nana») va «Men qoralayman!» (Dreyfus ishi) maqolasi muallifi.',
               'ru': 'Теоретик и лидер натурализма, автор 20-томного цикла «Ругон-Маккары» («Жерминаль») и знаменитого '
                     'открытого письма «Я обвиняю!».',
               'en': 'Foremost figure of naturalism, creator of the 20-novel Rougon-Macquart series and defender of '
                     "Alfred Dreyfus with 'J'accuse!'."},
  'aliases': ['emil zolya', 'zolya', 'эмиль золя', 'золя', 'emile zola']},
 {'id': 'lit_auth_050',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['August Strindberg', 'Genrik Ibsen', 'Bernard Shou', 'Knut Hamsun'],
              'ru': ['Август Стриндберг', 'Генрик Ибсен', 'Бернард Шоу', 'Кнут Гамсун'],
              'en': ['August Strindberg', 'Henrik Ibsen', 'George Bernard Shaw', 'Knut Hamsun']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Genrik Ibsen', 'ru': 'Генрик Ибсен', 'en': 'Henrik Ibsen'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Henrik_Ibsen_by_Gustav_Borgen.jpg',
  'fun_fact': {'uz': "Norvegiyalik 'Yangi drama' otasi, «Qo'g'irchoqxona» (Nora fojiasi), «Per Gyunt» va «Vahimalar» "
                     'pesalari muallifi.',
               'ru': 'Норвежский драматург, основатель европейской «новой драмы», автор пьес «Кукольный дом» (Нора) и '
                     '«Пер Гюнт».',
               'en': "Norwegian titan of modern realistic drama, famous for questioning bourgeois marriage norms in 'A "
                     "Doll's House' and 'Hedda Gabler'."},
  'aliases': ['ibsen', 'genrik ibsen', 'ибсен', 'генрик ибсен', 'henrik ibsen']},
 {'id': 'lit_auth_051',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['F. Skott Fitsjerald', 'Uilyam Folkner', 'Ernest Xeminguey', 'Jon Steynbek'],
              'ru': ['Ф. Скотт Фицджеральд', 'Уильям Фолкнер', 'Эрнест Хемингуэй', 'Джон Стейнбек'],
              'en': ['F. Scott Fitzgerald', 'William Faulkner', 'Ernest Hemingway', 'John Steinbeck']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Ernest Xeminguey', 'ru': 'Эрнест Хемингуэй', 'en': 'Ernest Hemingway'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/28/ErnestHemingway.jpg',
  'fun_fact': {'uz': "«Yo'qotilgan avlod» vakili, «Aysberg nazariyasi» asoschisi, 1954 yil Nobel mukofoti sohibi "
                     '(«Chol va dengiz», «Alvido, qurol!»).',
               'ru': 'Лауреат Нобелевской премии 1954 года, мастер телеграфного лаконизма («принцип айсберга») и '
                     'страстный любитель корриды и сафари.',
               'en': "Nobel laureate of 1954 famed for his minimalist 'iceberg theory' style and adventurous life in "
                     'Paris, Key West, and Cuba.'},
  'aliases': ['xeminguey', 'ernest xeminguey', 'хемингуэй', 'hemingway', 'ernest hemingway']},
 {'id': 'lit_auth_052',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Ernest Xeminguey', 'Teodor Drayzer', 'Sinler Lyuis', 'F. Skott Fitsjerald'],
              'ru': ['Эрнест Хемингуэй', 'Теодор Драйзер', 'Синклер Льюис', 'Ф. Скотт Фицджеральд'],
              'en': ['Ernest Hemingway', 'Theodore Dreiser', 'Sinclair Lewis', 'F. Scott Fitzgerald']},
  'correct_index': 3,
  'correct_answer': {'uz': 'F. Skott Fitsjerald', 'ru': 'Ф. Скотт Фицджеральд', 'en': 'F. Scott Fitzgerald'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/5c/F_Scott_Fitzgerald_1921.jpg',
  'fun_fact': {'uz': '«Jaz asri» kuychisi, Amerika orzusi va uning puch ekanini tasvirlagan «Buyuk Getsbi» hamda «Tun '
                     'mayin» romanlari muallifi.',
               'ru': 'Летописец «века джаза», автор романа «Великий Гэтсби» (1925), тонко описавший иллюзии и '
                     'разочарования богатой молодёжи.',
               'en': 'Chronicler of the Roaring Twenties Jazz Age, best known for depicting the glittering illusions '
                     "of the American Dream in 'The Great Gatsby'."},
  'aliases': ['fitsjerald', 'f skott fitsjerald', 'фицджеральд', 'fitzgerald', 'f scott fitzgerald']},
 {'id': 'lit_auth_053',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Jorj Oruell (Erik Artur Bler)', 'Oldos Xaksli', 'Rey Bredberi', 'Artur Kestler'],
              'ru': ['Джордж Оруэлл (Эрик Артур Блэр)', 'Олдос Хаксли', 'Рэй Брэдбери', 'Артур Кёстлер'],
              'en': ['George Orwell (Eric Arthur Blair)', 'Aldous Huxley', 'Ray Bradbury', 'Arthur Koestler']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Jorj Oruell (Erik Artur Bler)',
                     'ru': 'Джордж Оруэлл (Эрик Артур Блэр)',
                     'en': 'George Orwell (Eric Arthur Blair)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/George_Orwell_press_photo.jpg',
  'fun_fact': {'uz': 'Totalitarizm, soxta tashviqot va erkinlik kurashini ochib bergan buyuk antiutopik asarlar — '
                     "«1984» va «Molxona» («Hayvonlar xo'jaligi») muallifi.",
               'ru': 'Британский публицист и романист, автор термина «новояз» и антиутопий «1984» и «Скотный двор».',
               'en': 'English novelist, essayist, and critic famous for his warnings against totalitarianism in '
                     "'Animal Farm' and 'Nineteen Eighty-Four'."},
  'aliases': ['oruell', 'jorj oruell', 'оруэлл', 'джордж оруэлл', 'george orwell', 'orwell']},
 {'id': 'lit_auth_054',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Tomas Mann', 'Frans Kafka', 'German Gesse', 'Robert Muzil'],
              'ru': ['Томас Манн', 'Франц Кафка', 'Герман Гессе', 'Роберт Музиль'],
              'en': ['Thomas Mann', 'Franz Kafka', 'Hermann Hesse', 'Robert Musil']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Frans Kafka', 'ru': 'Франц Кафка', 'en': 'Franz Kafka'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Kafka1906_cropped.jpg',
  'fun_fact': {'uz': 'Pragada nemis tilida ijod qilgan, zamonaviy odamning chorasizligi va byurokratiya dahshatini aks '
                     'ettirgan «Evrilish», «Sud jarayoni», «Qasr» asarlari muallifi.',
               'ru': 'Пражский писатель-страховой чиновник, чьё имя стало синонимом абсурда и экзистенциального ужаса '
                     '(«Процесс», «Превращение», «Замок»).',
               'en': "Bohemian writer whose nightmarish, bureaucratic parables in 'The Metamorphosis' and 'The Trial' "
                     "gave rise to the term 'Kafkaesque'."},
  'aliases': ['kafka', 'frans kafka', 'кафка', 'франц кафка', 'franz kafka']},
 {'id': 'lit_auth_055',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Jan-Pol Sartr', 'Romen Rollan', 'Alber Kamyu', 'Andre Marlo'],
              'ru': ['Жан-Поль Сартр', 'Ромен Роллан', 'Альбер Камю', 'Андре Мальро'],
              'en': ['Jean-Paul Sartre', 'Romain Rolland', 'Albert Camus', 'André Malraux']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Alber Kamyu', 'ru': 'Альбер Камю', 'en': 'Albert Camus'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/08/Albert_Camus%2C_gagnant_du_prix_Nobel%2C_portrait_en_buste%2C_pos%C3%A9_au_bureau%2C_fume_une_cigarette%2C_content_cropped.jpg',
  'fun_fact': {'uz': 'Absurdizm falsafasi va ekzistensializm vakili, 1957 yil Nobel mukofoti laureati, «Begona», '
                     '«Vabo», «Sizif haqida asotir» asarlari muallifi.',
               'ru': 'Франко-алжирский философ и писатель, теоретик абсурдизма, лауреат Нобелевской премии 1957 года '
                     '(«Посторонний», «Чума», «Миф о Сизифе»).',
               'en': "French-Algerian philosopher and Nobel laureate known for developing absurdist philosophy in 'The "
                     "Stranger' and 'The Myth of Sisyphus'."},
  'aliases': ['kamyu', 'alber kamyu', 'камю', 'альбер камю', 'camus', 'albert camus']},
 {'id': 'lit_auth_056',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Alber Kamyu', 'Mishel Fuko', 'Jak Derrida', 'Jan-Pol Sartr'],
              'ru': ['Альбер Камю', 'Мишель Фуко', 'Жак Деррида', 'Жан-Поль Сартр'],
              'en': ['Albert Camus', 'Michel Foucault', 'Jacques Derrida', 'Jean-Paul Sartre']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jan-Pol Sartr', 'ru': 'Жан-Поль Сартр', 'en': 'Jean-Paul Sartre'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ef/Sartre_1967_crop.jpg',
  'fun_fact': {'uz': "Fransuz ekzistensializmi yetakchisi, «Ko'ngil aynishi» romani, «Borliq va yo'qlik» falsafiy "
                     'asari muallifi; 1964 yilgi Nobel mukofotidan ixtiyoriy voz kechgan.',
               'ru': 'Лидер французского экзистенциализма («бытие предшествует сущности»), добровольно отказавшийся от '
                     'Нобелевской премии по литературе 1964 года.',
               'en': 'Philosopher and playwright who formulated existentialist humanism, famously refusing the 1964 '
                     'Nobel Prize in Literature.'},
  'aliases': ['sartr', 'jan-pol sartr', 'сартр', 'жан-поль сартр', 'sartre', 'jean-paul sartre']},
 {'id': 'lit_auth_057',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Gabriel Garsia Markes (Gabo)', 'Xorxe Luis Borxes', 'Mario Vargas Lyosa', 'Xulio Kortasar'],
              'ru': ['Габриэль Гарсиа Маркес (Габо)', 'Хорхе Луис Борхес', 'Марио Варгас Льоса', 'Хулио Кортасар'],
              'en': ['Gabriel García Márquez (Gabo)', 'Jorge Luis Borges', 'Mario Vargas Llosa', 'Julio Cortázar']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Gabriel Garsia Markes (Gabo)',
                     'ru': 'Габриэль Гарсиа Маркес (Габо)',
                     'en': 'Gabriel García Márquez (Gabo)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/0f/Gabriel_Garcia_Marquez.jpg',
  'fun_fact': {'uz': "Kolumbiyalik sehrli realizm dahosi, 1982 yil Nobel mukofoti sohibi («Yolg'izlikning yuz yili», "
                     '«Vabo davridagi muhabbat», «Patriarx kuzi»).',
               'ru': 'Колумбийский патриарх магического реализма, лауреат Нобелевской премии 1982 года за эпопею «Сто '
                     'лет одиночества».',
               'en': 'Colombian novelist who popularized magical realism worldwide with his Nobel Prize-winning '
                     "masterpiece 'One Hundred Years of Solitude'."},
  'aliases': ['markes', 'garsia markes', 'маркес', 'габриэль гарсиа маркес', 'marquez', 'gabriel garcia marquez']},
 {'id': 'lit_auth_058',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Gabriel Garsia Markes', 'Xorxe Luis Borxes', 'Oktavio Pas', 'Pablo Neruda'],
              'ru': ['Габриэль Гарсиа Маркес', 'Хорхе Луис Борхес', 'Октавио Пас', 'Пабло Неруда'],
              'en': ['Gabriel García Márquez', 'Jorge Luis Borges', 'Octavio Paz', 'Pablo Neruda']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Xorxe Luis Borxes', 'ru': 'Хорхе Луис Борхес', 'en': 'Jorge Luis Borges'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/d/df/Jorge_Luis_Borges_1976.jpg',
  'fun_fact': {'uz': "Argentina adabiyoti dahosi, labirintlar, cheksiz kutubxonalar va ko'zgular falsafasi ustasi "
                     "(«Alef», «Fiktsiyalar», «To'qima mavjudotlar kitobi»).",
               'ru': 'Аргентинский классик философской новеллы, создатель метафор Вавилонской библиотеки, лабиринта '
                     'времени и зеркальных миров.',
               'en': 'Argentine master of the philosophical labyrinth, infinite library, and metaphysical fantasy in '
                     "'Ficciones' and 'The Aleph'."},
  'aliases': ['borxes', 'xorxe luis borxes', 'борхес', 'хорхе луис борхес', 'borges']},
 {'id': 'lit_auth_059',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Alber Kamyu', 'Jan Kokto', 'Antuan de Sent-Ekzyuperi', 'Marsel Prust'],
              'ru': ['Альбер Камю', 'Жан Кокто', 'Антуан де Сент-Экзюпери', 'Марсель Пруст'],
              'en': ['Albert Camus', 'Jean Cocteau', 'Antoine de Saint-Exupéry', 'Marcel Proust']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Antuan de Sent-Ekzyuperi',
                     'ru': 'Антуан де Сент-Экзюпери',
                     'en': 'Antoine de Saint-Exupéry'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/77/Antoine_de_Saint-Exup%C3%A9ry.jpg',
  'fun_fact': {'uz': 'Fransuz professional harbiy uchuvchisi va yozuvchisi, afsonaviy «Kichkina shahzoda», «Insonlar '
                     "zamini» va «Tungi parvoz» asarlari muallifi; 1944 yilda samolyotda bedarak yo'qolgan.",
               'ru': 'Французский военный лётчик и писатель-гуманист, создатель бессмертной сказки «Маленький принц»; '
                     'погиб в боевом вылете в 1944 году.',
               'en': "French aviator and author of the beloved philosophical fable 'The Little Prince', who vanished "
                     'over the Mediterranean during WWII.'},
  'aliases': ['ekzyuperi', 'sent-ekzyuperi', 'экзюпери', 'сент-экзюпери', 'saint-exupery']},
 {'id': 'lit_auth_060',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Bernard Shou', 'Somerset Moem', 'Jorj Bayron', 'Oskar Uayld'],
              'ru': ['Бернард Шоу', 'Сомерсет Моэм', 'Джордж Байрон', 'Оскар Уайльд'],
              'en': ['George Bernard Shaw', 'W. Somerset Maugham', 'Lord Byron', 'Oscar Wilde']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Oskar Uayld', 'ru': 'Оскар Уайльд', 'en': 'Oscar Wilde'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Oscar_Wilde_by_Napoleon_Sarony_c1882.jpg',
  'fun_fact': {'uz': "Irlandiyalik nozik didli estet, o'tkir aforizmlar qiroli, «Dorian Greyning portreti» romani va "
                     "«Jiddiy bo'lish qanchalik muhim» komediyasi muallifi.",
               'ru': 'Блестящий ирландский эстет, король остроумия и парадокса, автор романа «Портрет Дориана Грея» и '
                     'сказки «Счастливый принц».',
               'en': 'Irish playwright and supreme wit of late-Victorian London, renowned for his flamboyant '
                     "aestheticism and 'The Picture of Dorian Gray'."},
  'aliases': ['uayld', 'oskar uayld', 'уайльд', 'оскар уайльд', 'oscar wilde', 'wilde']},
 {'id': 'lit_auth_061',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['German Gesse', 'Tomas Mann', 'Frans Kafka', 'Erix Mariya Remark'],
              'ru': ['Герман Гессе', 'Томас Манн', 'Франц Кафка', 'Эрих Мария Ремарк'],
              'en': ['Hermann Hesse', 'Thomas Mann', 'Franz Kafka', 'Erich Maria Remarque']},
  'correct_index': 0,
  'correct_answer': {'uz': 'German Gesse', 'ru': 'Герман Гессе', 'en': 'Hermann Hesse'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/d/da/Hermann_Hesse_1927.jpg',
  'fun_fact': {'uz': "1946 yil Nobel mukofoti sovrindori bo'lgan nemis-shveytsar yozuvchisi, ma'naviy izlanishlar "
                     "ustasi («Cho'l bo'risi», «Siddharta», «Marjonlar o'yini»).",
               'ru': 'Немецко-швейцарский писатель, лауреат Нобелевской премии 1946 года, автор духовных '
                     'романов-исканий «Степной волк» и «Игра в бисер».',
               'en': 'German-Swiss Nobel laureate whose explorations of Eastern spirituality and human duality include '
                     "'Siddhartha' and 'Steppenwolf'."},
  'aliases': ['gesse', 'german gesse', 'гессе', 'герман гессе', 'hermann hesse']},
 {'id': 'lit_auth_062',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['German Gesse', 'Tomas Mann', 'Geynrix Mann', 'Stefan Sveyg'],
              'ru': ['Герман Гессе', 'Томас Манн', 'Генрих Манн', 'Стефан Цвейг'],
              'en': ['Hermann Hesse', 'Thomas Mann', 'Heinrich Mann', 'Stefan Zweig']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Tomas Mann', 'ru': 'Томас Манн', 'en': 'Thomas Mann'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Thomas_Mann_1937.jpg',
  'fun_fact': {'uz': '1929 yil Nobel mukofoti laureati, nemis intellektual romanining buyuk vakili («Buddenbroklar», '
                     "«Sehrli tog'», «Doktor Faustus»).",
               'ru': 'Глава немецкого интеллектуального романа XX века, нобелевский лауреат 1929 года за семейную '
                     'хронику «Будденброки».',
               'en': 'Master of the 20th-century German intellectual novel, winning the 1929 Nobel Prize primarily for '
                     "his epic debut 'Buddenbrooks'."},
  'aliases': ['tomas mann', 'томас манн', 'thomas mann']},
 {'id': 'lit_auth_063',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Semuel Bekket', 'Virjiniya Vulf', 'Jeyms Joys', 'Uilyam Batler Yeyts'],
              'ru': ['Сэмюэл Беккет', 'Вирджиния Вулф', 'Джеймс Джойс', 'Уильям Батлер Йейтс'],
              'en': ['Samuel Beckett', 'Virginia Woolf', 'James Joyce', 'W.B. Yeats']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Jeyms Joys', 'ru': 'Джеймс Джойс', 'en': 'James Joyce'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/Official_portrait_of_James_Joyce%2C_1904.jpg',
  'fun_fact': {'uz': "Modernizm adabiyotining cho'qqisi, 'ong oqimi' uslubining inqilobiy ustasi, Dublin hayotini "
                     "qamragan «Uliss» va «Finneganning uyg'onishi» muallifi.",
               'ru': 'Ирландский модернист, революционизировавший литературу потоком сознания в романах «Улисс» (1922) '
                     'и «Дублинцы».',
               'en': 'Irish avant-garde master who transformed fiction with his stream-of-consciousness technique in '
                     "'Ulysses'."},
  'aliases': ['joys', 'jeyms joys', 'джойс', 'джеймс джойс', 'james joyce']},
 {'id': 'lit_auth_064',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Agata Kristi', 'Silviya Plat', 'Jorj Eliot', 'Virjiniya Vulf'],
              'ru': ['Агата Кристи', 'Сильвия Плат', 'Джордж Элиот', 'Вирджиния Вулф'],
              'en': ['Agatha Christie', 'Sylvia Plath', 'George Eliot', 'Virginia Woolf']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Virjiniya Vulf', 'ru': 'Вирджиния Вулф', 'en': 'Virginia Woolf'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/George_Charles_Beresford_-_Virginia_Woolf_in_1902_-_Restoration.jpg',
  'fun_fact': {'uz': "Blumsberi to'garagi yetakchisi, ong oqimi va modernizmning yirik namoyandasi («Missis Dellouey», "
                     "«Mayoqqa», «O'zining shaxsiy xonasi»).",
               'ru': 'Британская писательница-новатор, ключевая фигура модерна и феминистской критики («Миссис '
                     'Дэллоуэй», «На маяк»).',
               'en': 'Central figure in modernist fiction and feminist theory, renowned for nonlinear narrative in '
                     "'Mrs Dalloway' and 'To the Lighthouse'."},
  'aliases': ['vulf', 'virjiniya vulf', 'вулф', 'вирджиния вулф', 'virginia woolf']},
 {'id': 'lit_auth_065',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Marsel Prust', 'Andre Jid', 'Jan Kokto', 'Pol Valeri'],
              'ru': ['Марсель Пруст', 'Андре Жид', 'Жан Кокто', 'Поль Валери'],
              'en': ['Marcel Proust', 'André Gide', 'Jean Cocteau', 'Paul Valéry']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Marsel Prust', 'ru': 'Марсель Пруст', 'en': 'Marcel Proust'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/85/Marcel_Proust_1895.jpg',
  'fun_fact': {'uz': "Fransuz modernizmining yorqin dahosi, 7 jilddan iborat 3200 sahifalik epik «Yo'qotilgan vaqtni "
                     'izlab» romani muallifi (Madeleyn pechenyesi xotiralari).',
               'ru': 'Создатель монументального цикла «В поисках утраченного времени», исследовавший тончайшие '
                     'механизмы непроизвольной памяти.',
               'en': "French novelist who created the monumental seven-volume epic 'In Search of Lost Time', famous "
                     'for the madeleine cake episode.'},
  'aliases': ['prust', 'marsel prust', 'пруст', 'марсель пруст', 'marcel proust']},
 {'id': 'lit_auth_066',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['K.S. Lyuis', 'J.R.R. Tolkin', 'Jorj R.R. Martin', 'Robert Jordan'],
              'ru': ['К. С. Льюис', 'Дж. Р. Р. Толкин', 'Джордж Р. Р. Мартин', 'Роберт Джордан'],
              'en': ['C.S. Lewis', 'J.R.R. Tolkien', 'George R.R. Martin', 'Robert Jordan']},
  'correct_index': 1,
  'correct_answer': {'uz': 'J.R.R. Tolkin', 'ru': 'Дж. Р. Р. Толкин', 'en': 'J.R.R. Tolkien'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/d/d4/J._R._R._Tolkien%2C_ca._1925.jpg',
  'fun_fact': {'uz': "Oksford universiteti filolog-professori, O'rta Yer olami, elflar tili hamda «Xobbit» va «Uzuklar "
                     'hukmdori» epik trilogiyasi yaratuvchisi.',
               'ru': 'Оксфордский профессор филологии, создатель Средиземья, эльфийских языков и фундаментального '
                     'фэнтези «Властелин колец».',
               'en': "Oxford philologist whose creation of Middle-earth, invented languages, and 'The Lord of the "
                     "Rings' founded modern high fantasy."},
  'aliases': ['tolkin', 'толкин', 'jrr tolkien', 'tolkien']},
 {'id': 'lit_auth_067',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['J.R.R. Tolkin', 'Filip Pulman', 'K.S. Lyuis (Klayv Steyplz Lyuis)', 'Roald Dal'],
              'ru': ['Дж. Р. Р. Толкин', 'Филип Пулман', 'К. С. Льюис (Клайв Стейплз Льюис)', 'Роальд Даль'],
              'en': ['J.R.R. Tolkien', 'Philip Pullman', 'C.S. Lewis', 'Roald Dahl']},
  'correct_index': 2,
  'correct_answer': {'uz': 'K.S. Lyuis (Klayv Steyplz Lyuis)',
                     'ru': 'К. С. Льюис (Клайв Стейплз Льюис)',
                     'en': 'C.S. Lewis'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/C.s.lewis3.jpg',
  'fun_fact': {'uz': "Oksford va Kembrij professori, Tolkinning yaqin do'sti, mashhur 7 kitobdan iborat «Narniya "
                     'yilnomalari» muallifi.',
               'ru': 'Британский богослов и писатель, член кружка «Инклингов», автор любимого цикла сказок «Хроники '
                     'Нарнии».',
               'en': 'Oxford scholar, theologian, and close friend of Tolkien, famous for the allegorical fantasy '
                     "series 'The Chronicles of Narnia'."},
  'aliases': ['lyuis', 'k.s. lyuis', 'льюис', 'к.с. льюис', 'c.s. lewis']},
 {'id': 'lit_auth_068',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Artur Konan Doyl', 'Doroti Seyers', 'Dafna dyu Morye', 'Agata Kristi (Detektiv qirolichasi)'],
              'ru': ['Артур Конан Дойл', 'Дороти Сэйерс', 'Дафна дю Морье', 'Агата Кристи (Королева детектива)'],
              'en': ['Arthur Conan Doyle',
                     'Dorothy L. Sayers',
                     'Daphne du Maurier',
                     'Agatha Christie (Queen of Crime)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Agata Kristi (Detektiv qirolichasi)',
                     'ru': 'Агата Кристи (Королева детектива)',
                     'en': 'Agatha Christie (Queen of Crime)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Agatha_Christie.png',
  'fun_fact': {'uz': "Ginnes rekordlar kitobiga ko'ra dunyodagi eng ko'p sotilgan fantastik asarlar muallifi (2 "
                     'milliarddan ortiq); Erkyul Puaro va Miss Marpl yaratuvchisi.',
               'ru': '«Королева детектива», самая продаваемая писательница в истории (свыше 2 млрд книг), '
                     'создательница Эркюля Пуаро и мисс Марпл.',
               'en': "The 'Queen of Crime', recorded by Guinness World Records as the best-selling fiction writer of "
                     'all time, creator of Hercule Poirot and Miss Marple.'},
  'aliases': ['agata kristi', 'kristi', 'агата кристи', 'agatha christie']},
 {'id': 'lit_auth_069',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Rey Bredberi', 'Ayzek Azimov', 'Artur Klark', 'Filip Dik'],
              'ru': ['Рэй Брэдбери', 'Айзек Азимов', 'Артур Кларк', 'Филип К. Дик'],
              'en': ['Ray Bradbury', 'Isaac Asimov', 'Arthur C. Clarke', 'Philip K. Dick']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Rey Bredberi', 'ru': 'Рэй Брэдбери', 'en': 'Ray Bradbury'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Ray_Bradbury_1975_photo_portrait.jpg',
  'fun_fact': {'uz': "Amerikalik buyuk fantast va lirik adib, «Farengeyt bo'yicha 451 daraja», «Mars yilnomalari» va "
                     '«Momaqaymoq vinosi» asarlari muallifi.',
               'ru': 'Американский классик фантастики и поэтической прозы, автор шедевров «451 градус по Фаренгейту» и '
                     '«Вино из одуванчиков».',
               'en': "Prolific American master of speculative fiction and nostalgia, acclaimed for 'Fahrenheit 451' "
                     "and 'The Martian Chronicles'."},
  'aliases': ['bredberi', 'rey bredberi', 'брэдбери', 'рэй брэдбери', 'ray bradbury']},
 {'id': 'lit_auth_070',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Rey Bredberi', 'Ayzek Azimov', 'Artur Klark', 'Stanislav Lem'],
              'ru': ['Рэй Брэдбери', 'Айзек Азимов', 'Артур Кларк', 'Станислав Лем'],
              'en': ['Ray Bradbury', 'Isaac Asimov', 'Arthur C. Clarke', 'Stanislaw Lem']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Ayzek Azimov', 'ru': 'Айзек Азимов', 'en': 'Isaac Asimov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/34/Isaac.Asimov01.jpg',
  'fun_fact': {'uz': 'Bioximiya professori va fantastika klassigi, robototexnikaning 3 qonunini yaratgan hamda '
                     '«Poydevor» (Foundation) va «Men, robot» kitoblari muallifi.',
               'ru': 'Один из «Большой тройки» писателей-фантастов, сформулировавший знаменитые Три закона '
                     'робототехники и создавший сагу «Основание».',
               'en': 'Biochemistry professor and sci-fi giant who formulated the Three Laws of Robotics and penned the '
                     "epic 'Foundation' series."},
  'aliases': ['azimov', 'ayzek azimov', 'азимов', 'айзек азимов', 'isaac asimov']},
 {'id': 'lit_auth_071',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Ayzek Azimov', 'Robert Xaynlayn', 'Artur Klark (Ser Artur Klark)', 'Gerbert Uells'],
              'ru': ['Айзек Азимов', 'Роберт Хайнлайн', 'Артур Кларк (сэр Артур Кларк)', 'Герберт Уэллс'],
              'en': ['Isaac Asimov', 'Robert A. Heinlein', 'Arthur C. Clarke', 'H.G. Wells']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Artur Klark (Ser Artur Klark)',
                     'ru': 'Артур Кларк (сэр Артур Кларк)',
                     'en': 'Arthur C. Clarke'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Arthur_C._Clarke_1965.jpg',
  'fun_fact': {'uz': "Geostatsionar aloqa sun'iy yo'ldoshlarini bashorat qilgan va Stenli Kubrik bilan birgalikda "
                     '«2001: Fazo Odisseyasi» asarini yaratgan britaniyalik yozuvchi-olim.',
               'ru': 'Британский писатель и футуролог, предсказавший геостационарные спутники связи, автор сценария '
                     'шедевра «Космическая одиссея 2001 года».',
               'en': "Visionary British science fiction author and inventor who co-wrote Stanley Kubrick's '2001: A "
                     "Space Odyssey' and conceived satellite communications."},
  'aliases': ['artur klark', 'klark', 'артур кларк', 'arthur c clarke']},
 {'id': 'lit_auth_072',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Oskar Uayld', 'Semuel Bekket', 'Jon Golsuorsi', 'Jorj Bernard Shou'],
              'ru': ['Оскар Уайльд', 'Сэмюэл Беккет', 'Джон Голсуорси', 'Джордж Бернард Шоу'],
              'en': ['Oscar Wilde', 'Samuel Beckett', 'John Galsworthy', 'George Bernard Shaw']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jorj Bernard Shou', 'ru': 'Джордж Бернард Шоу', 'en': 'George Bernard Shaw'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/50/Bernard_Shaw_1936.jpg',
  'fun_fact': {'uz': "Tarixda ham adabiyot bo'yicha Nobel mukofotini (1925), ham «Oskar» mukofotini (1938, "
                     "«Pigmalion») qo'lga kiritgan yagona ijodkor.",
               'ru': 'Единственный в мире человек, удостоенный одновременно Нобелевской премии по литературе (1925) и '
                     'кинопремии «Оскар» (1938 за «Пигмалион»).',
               'en': 'The only person to win both a Nobel Prize in Literature (1925) and an Academy Award (1938 for '
                     "the screenplay of 'Pygmalion')."},
  'aliases': ['bernard shou', 'shou', 'бернард шоу', 'шоу', 'george bernard shaw']},
 {'id': 'lit_auth_073',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Uolt Uitmen', 'Genri Toro', 'Edgar Allan Po', 'Robert Frost'],
              'ru': ['Уолт Уитмен', 'Генри Торо', 'Эдгар Аллан По', 'Роберт Фрост'],
              'en': ['Walt Whitman', 'Henry David Thoreau', 'Edgar Allan Poe', 'Robert Frost']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Uolt Uitmen', 'ru': 'Уолт Уитмен', 'en': 'Walt Whitman'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/f/f3/Walt_Whitman_-_1860s_-_head_and_shoulders.jpg',
  'fun_fact': {'uz': 'AQSHning milliy shoiri, erkin vazn (verlibir) inqilobchisi, mashhur «Maysa yaproqlari» (Leaves '
                     'of Grass) kitobi muallifi.',
               'ru': 'Американский поэт-новатор, реформатор стиха, воспевший демократию и всеединство в эпохальной '
                     'книге «Листья травы».',
               'en': "American poet who transformed world poetry with free verse in his landmark collection 'Leaves of "
                     "Grass'."},
  'aliases': ['uitmen', 'uolt uitmen', 'уитмен', 'уолт уитмен', 'walt whitman']},
 {'id': 'lit_auth_074',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Silviya Plat', 'Emili Dikinson', 'Virjiniya Vulf', 'Sharlotta Bronte'],
              'ru': ['Сильвия Плат', 'Эмили Дикинсон', 'Вирджиния Вулф', 'Шарлотта Бронте'],
              'en': ['Sylvia Plath', 'Emily Dickinson', 'Virginia Woolf', 'Charlotte Brontë']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Emili Dikinson', 'ru': 'Эмили Дикинсон', 'en': 'Emily Dickinson'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Black-white_photograph_of_Emily_Dickinson2.png',
  'fun_fact': {'uz': "Amerikalik buyuk sirli shoira; butun umrini o'z xonasida o'tkazib, qisqa chiziqchalar va chuqur "
                     "falsafiy metaforalarga boy 1800 ta nodir she'r qoldirgan.",
               'ru': 'Затворница из Массачусетса, создавшая уникальную герметичную лирику с тире и нестандартной '
                     'рифмой, опередившую время на столетие.',
               'en': 'Solitary American poet from Amherst, Massachusetts, whose unconventional, intensely compressed '
                     '1,800 poems emerged posthumously.'},
  'aliases': ['dikinson', 'emili dikinson', 'дикинсон', 'эмили дикинсон', 'emily dickinson']},
 {'id': 'lit_auth_075',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Uolt Uitmen', 'T.S. Eliot', 'Robert Frost', 'Uilyam Folkner'],
              'ru': ['Уолт Уитмен', 'Т. С. Элиот', 'Роберт Фрост', 'Уильям Фолкнер'],
              'en': ['Walt Whitman', 'T.S. Eliot', 'Robert Frost', 'William Faulkner']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Robert Frost', 'ru': 'Роберт Фрост', 'en': 'Robert Frost'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Robert_Frost_NYWTS.jpg',
  'fun_fact': {'uz': "She'riyat bo'yicha to'rt marta Pulitser mukofotini olgan yagona amerikalik shoir («Tanlanmagan "
                     "yo'l» she'ri muallifi).",
               'ru': 'Четырёхкратный лауреат Пулитцеровской премии, воспевший сельскую природу Новой Англии и '
                     'философскую драму человеческого выбора.',
               'en': "Beloved American poet and only writer to win four Pulitzer Prizes for Poetry, famous for 'The "
                     "Road Not Taken'."},
  'aliases': ['robert frost', 'frost', 'роберт фрост', 'фрост']},
 {'id': 'lit_auth_076',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Mark Tven', 'Teodor Drayzer', 'O. Genri', 'Jek London (Jon Griffit Cheyni)'],
              'ru': ['Марк Твен', 'Теодор Драйзер', 'О. Генри', 'Джек Лондон (Джон Гриффит Чейни)'],
              'en': ['Mark Twain', 'Theodore Dreiser', 'O. Henry', 'Jack London']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jek London (Jon Griffit Cheyni)',
                     'ru': 'Джек Лондон (Джон Гриффит Чейни)',
                     'en': 'Jack London'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/2d/Jack_London_young.jpg',
  'fun_fact': {'uz': "Shimoliy qorli o'lkalarda oltin izlovchilar, bo'rilar va mard insonlar hayotini kuylagan "
                     "yozuvchi («Oqso'yloq», «Ajdodlar chorlovi», «Martin Iden»).",
               'ru': 'Классик приключенческой прозы, золотоискатель на Клондайке, автор романов «Мартин Иден», «Белый '
                     'Клык» и «Зов предков».',
               'en': "Pioneering commercial writer and Klondike prospector whose rugged tales of survival include 'The "
                     "Call of the Wild' and 'White Fang'."},
  'aliases': ['jek london', 'london', 'джек лондон', 'jack london']},
 {'id': 'lit_auth_077',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Jon Steynbek', 'Ernest Xeminguey', 'Uilyam Folkner', 'F. Skott Fitsjerald'],
              'ru': ['Джон Стейнбек', 'Эрнест Хемингуэй', 'Уильям Фолкнер', 'Ф. Скотт Фицджеральд'],
              'en': ['John Steinbeck', 'Ernest Hemingway', 'William Faulkner', 'F. Scott Fitzgerald']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Jon Steynbek', 'ru': 'Джон Стейнбек', 'en': 'John Steinbeck'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/John_Steinbeck_1939_%28cropped%29.jpg',
  'fun_fact': {'uz': '1962 yil Nobel mukofoti laureati, Buyuk depressiya davridagi mehnatkashlar hayotini aks ettirgan '
                     "«G'azab mevalari» va «Sichqonlar va odamlar haqida» romanlari muallifi.",
               'ru': 'Нобелевский лауреат 1962 года, описавший трагедию фермеров эпохи Великой депрессии в романе '
                     '«Гроздья гнева».',
               'en': "1962 Nobel laureate whose compassionate portraits of migrant workers in 'The Grapes of Wrath' "
                     'defined Great Depression literature.'},
  'aliases': ['steynbek', 'jon steynbek', 'стейнбек', 'джон стейнбек', 'john steinbeck']},
 {'id': 'lit_auth_078',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Jon Steynbek', 'Uilyam Folkner', 'Ernest Xeminguey', 'Tomas Vulf'],
              'ru': ['Джон Стейнбек', 'Уильям Фолкнер', 'Эрнест Хемингуэй', 'Томас Вулф'],
              'en': ['John Steinbeck', 'William Faulkner', 'Ernest Hemingway', 'Thomas Wolfe']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Uilyam Folkner', 'ru': 'Уильям Фолкнер', 'en': 'William Faulkner'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Carl_Van_Vechten_-_William_Faulkner.jpg',
  'fun_fact': {'uz': 'Amerika Janubining afsonaviy Yoknapatofa okrugi yaratuvchisi, 1949 yil Nobel mukofoti sohibi '
                     "(«Shovqin va g'azab», «Men o'layotganimda»).",
               'ru': 'Американский модернист, нобелевский лауреат 1949 года, создатель вымышленного южного округа '
                     'Йокнапатофа («Шум и ярость»).',
               'en': 'Southern Gothic master and 1949 Nobel laureate who set profound stream-of-consciousness dramas '
                     "like 'The Sound and the Fury' in fictional Yoknapatawpha County."},
  'aliases': ['folkner', 'uilyam folkner', 'фолкнер', 'уильям фолкнер', 'faulkner', 'william faulkner']},
 {'id': 'lit_auth_079',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Boris Pasternak', 'Ivan Bunin', 'Vladimir Nabokov', 'Iosif Brodskiy'],
              'ru': ['Борис Пастернак', 'Иван Бунин', 'Владимир Набоков', 'Иосиф Бродский'],
              'en': ['Boris Pasternak', 'Ivan Bunin', 'Vladimir Nabokov', 'Joseph Brodsky']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Vladimir Nabokov', 'ru': 'Владимир Набоков', 'en': 'Vladimir Nabokov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Vladimir_Nabokov_1973.jpg',
  'fun_fact': {'uz': 'Ham rus, ham ingliz tilida tengsiz uslub yaratgan entomolog-olim va yozuvchi, «Lolita», «Lujin '
                     'himoyasi», «Hadyalar» romanlari muallifi.',
               'ru': 'Билингвальный гений стиля, энтомолог-лепидоптеролог, автор романов «Лолита», «Защита Лужина» и '
                     '«Дар».',
               'en': 'Bilingual Russian-American master of prose style, lepidopterist, and author of celebrated novels '
                     "including 'Lolita' and 'Pale Fire'."},
  'aliases': ['nabokov', 'vladimir nabokov', 'набоков', 'владимир набоков']},
 {'id': 'lit_auth_080',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Maksim Gorkiy', 'Aleksandr Fadeyev', 'Konstantin Simonov', 'Mixail Sholoxov'],
              'ru': ['Максим Горький', 'Александр Фадеев', 'Константин Симонов', 'Михаил Шолохов'],
              'en': ['Maxim Gorky', 'Alexander Fadeyev', 'Konstantin Simonov', 'Mikhail Sholokhov']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Mixail Sholoxov', 'ru': 'Михаил Шолохов', 'en': 'Mikhail Sholokhov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Mikhail_Sholokhov_1938.jpg',
  'fun_fact': {'uz': "1965 yilda «Tinch oqar Don» epopeyasi uchun adabiyot bo'yicha Nobel mukofotini qo'lga kiritgan "
                     'don kazaklari kuychisi.',
               'ru': 'Донской классик, лауреат Нобелевской премии 1965 года за монументальный роман «Тихий Дон».',
               'en': 'Soviet novelist who chronicled the Don Cossacks through World War I and Civil War in the 1965 '
                     "Nobel-winning 'And Quiet Flows the Don'."},
  'aliases': ['sholoxov', 'mixail sholoxov', 'шолохов', 'михаил шолохов', 'sholokhov']},
 {'id': 'lit_auth_081',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Anna Axmatova (Gorenko)', 'Marina Svetayeva', 'Bella Axmadulina', 'Zulfiya'],
              'ru': ['Анна Ахматова (Горенко)', 'Марина Цветаева', 'Белла Ахмадулина', 'Зульфия'],
              'en': ['Anna Akhmatova', 'Marina Tsvetaeva', 'Bella Akhmadulina', 'Zulfiya']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Anna Axmatova (Gorenko)', 'ru': 'Анна Ахматова (Горенко)', 'en': 'Anna Akhmatova'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Anna_Akhmatova_by_K._Petrov-Vodkin_%281922%2C_GRM%29.jpg',
  'fun_fact': {'uz': "Rus kumush asrining buyuk shoirasi, akmeizm oqimi vakili, qatag'on yillaridagi fojiani aks "
                     'ettirgan «Rekviyem» va «Qahramonsiz doston» muallifi; Toshkentda evakuatsiyada yashagan.',
               'ru': 'Великая русская поэтесса Серебряного века, голос трагедии народа в годы репрессий («Реквием»); в '
                     'годы войны жила в Ташкенте.',
               'en': "One of the acclaimed poets of Russia's Silver Age whose poignant 'Requiem' captured the grief of "
                     "Stalin's Great Terror."},
  'aliases': ['axmatova', 'anna axmatova', 'ахматова', 'анна ахматова', 'anna akhmatova']},
 {'id': 'lit_auth_082',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Anna Axmatova', 'Marina Svetayeva', 'Zinaida Gippius', 'Nadejda Mandelshtam'],
              'ru': ['Анна Ахматова', 'Марина Цветаева', 'Зинаида Гиппиус', 'Надежда Мандельштам'],
              'en': ['Anna Akhmatova', 'Marina Tsvetaeva', 'Zinaida Gippius', 'Nadezhda Mandelstam']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Marina Svetayeva', 'ru': 'Марина Цветаева', 'en': 'Marina Tsvetaeva'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Marina_Cvetaeva.jpg',
  'fun_fact': {'uz': "Jo'shqin va fojiali lirik shoira, o'ziga xos ritm va hissiyot ustasi; 1941 yilda Yelabugada "
                     "fojeali tarzda hayotdan ko'z yumgan.",
               'ru': 'Трагический гений Серебряного века с неповторимым синкопированным ритмом и предельной '
                     'эмоциональной обнажённостью стиха.',
               'en': 'Brilliant and tragic Russian Silver Age poet known for passionate, rhythmically inventive '
                     'verse.'},
  'aliases': ['svetayeva', 'marina svetayeva', 'цветаева', 'марина цветаева', 'tsvetaeva']},
 {'id': 'lit_auth_083',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Varlam Shalamov', 'Iosif Brodskiy', 'Aleksandr Soljenitsin', 'Boris Pasternak'],
              'ru': ['Варлам Шаламов', 'Иосиф Бродский', 'Александр Солженицын', 'Борис Пастернак'],
              'en': ['Varlam Shalamov', 'Joseph Brodsky', 'Aleksandr Solzhenitsyn', 'Boris Pasternak']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Aleksandr Soljenitsin', 'ru': 'Александр Солженицын', 'en': 'Aleksandr Solzhenitsyn'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Aleksandr_Solzhenitsyn_1974.jpg',
  'fun_fact': {'uz': '1970 yil Nobel mukofoti sohibi, GULAG lagerlari fojiasini fosh etgan monumental «GULAG '
                     'arxipelagi» va «Ivan Denisovichning bir kuni» asarlari muallifi.',
               'ru': 'Лауреат Нобелевской премии 1970 года, диссидент, открывший миру правду о сталинских лагерях в '
                     '«Архипелаге ГУЛАГ».',
               'en': "Nobel laureate whose epic documentary expose 'The Gulag Archipelago' brought worldwide attention "
                     'to the Soviet forced-labor camp system.'},
  'aliases': ['soljenitsin', 'солженицын', 'александр солженицын', 'solzhenitsyn']},
 {'id': 'lit_auth_084',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Osip Mandelshtam', 'Boris Pasternak', 'Vladimir Nabokov', 'Iosif Brodskiy'],
              'ru': ['Осип Мандельштам', 'Борис Пастернак', 'Владимир Набоков', 'Иосиф Бродский'],
              'en': ['Osip Mandelstam', 'Boris Pasternak', 'Vladimir Nabokov', 'Joseph Brodsky']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Iosif Brodskiy', 'ru': 'Иосиф Бродский', 'en': 'Joseph Brodsky'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Joseph_Brodsky_1988.jpg',
  'fun_fact': {'uz': "Leningradlik daho shoir, 1987 yilda 47 yoshida adabiyot bo'yicha Nobel mukofotiga sazovor "
                     "bo'lgan eng yosh laureatlardan biri.",
               'ru': 'Один из величайших русских поэтов XX века, лауреат Нобелевской премии 1987 года, профессор '
                     'американских университетов.',
               'en': 'Russian and American poet and essayist who won the 1987 Nobel Prize in Literature at age 47 for '
                     'luminous, metaphysical verse.'},
  'aliases': ['brodskiy', 'iosif brodskiy', 'бродский', 'иосиф бродский', 'joseph brodsky']},
 {'id': 'lit_auth_085',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Rabindranat Tagor', 'Xalil Jibron', 'Mahatma Gandi', 'Aurobindo Gxosh'],
              'ru': ['Рабиндранат Тагор', 'Халиль Джебран', 'Махатма Ганди', 'Ауробиндо Гхош'],
              'en': ['Rabindranath Tagore', 'Kahlil Gibran', 'Mahatma Gandhi', 'Sri Aurobindo']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Rabindranat Tagor', 'ru': 'Рабиндранат Тагор', 'en': 'Rabindranath Tagore'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Rabindranath_Tagore_in_1909.jpg',
  'fun_fact': {'uz': "Hindiston va Bangladesh madhiyalarining muallifi, 1913 yilda adabiyot bo'yicha Nobel mukofotini "
                     'olgan birinchi osiyolik («Gitanjali»).',
               'ru': 'Бенгальский гений-мыслитель, первый азиатский лауреат Нобелевской премии (1913); автор гимнов '
                     'сразу двух государств — Индии и Бангладеш.',
               'en': 'Bengali polymath who became the first non-European to win the Nobel Prize in Literature (1913); '
                     'composed national anthems for India and Bangladesh.'},
  'aliases': ['tagor', 'rabindranat tagor', 'тагор', 'рабиндранат тагор', 'tagore', 'rabindranath tagore']},
 {'id': 'lit_auth_086',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Najib Mahfuz', 'Xalil Jibron', 'Amin ar-Rayhoniy', 'Mixail Nuayma'],
              'ru': ['Нагиб Махфуз', 'Халиль Джебран', 'Амин ар-Рейхани', 'Михаил Нуайме'],
              'en': ['Naguib Mahfouz', 'Kahlil Gibran', 'Ameen Rihani', 'Mikhail Naimy']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Xalil Jibron', 'ru': 'Халиль Джебран', 'en': 'Kahlil Gibran'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Kahlil_Gibran_1913.jpg',
  'fun_fact': {'uz': "Livanlik buyuk faylasuf, rassom va shoir, Sharq va G'arb donishmandligini mujassam etgan "
                     "«Payg'ambar» (The Prophet, 1923) kitobi muallifi.",
               'ru': 'Ливанский и американский писатель, поэт и философ, автор всемирно известной книги «Пророк» '
                     '(1923).',
               'en': "Lebanese-American philosophical poet and visual artist whose 1923 inspirational classic 'The "
                     "Prophet' sold tens of millions of copies."},
  'aliases': ['xalil jibron', 'jibron', 'халиль джебран', 'джебран', 'kahlil gibran']},
 {'id': 'lit_auth_087',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Lao She', 'Mo Yan', 'Lu Syun (Chjou Shujen)', 'Ba Jin'],
              'ru': ['Лао Шэ', 'Мо Янь', 'Лу Синь (Чжоу Шужэнь)', 'Ба Цзинь'],
              'en': ['Lao She', 'Mo Yan', 'Lu Xun (Zhou Shuren)', 'Ba Jin']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Lu Syun (Chjou Shujen)', 'ru': 'Лу Синь (Чжоу Шужэнь)', 'en': 'Lu Xun (Zhou Shuren)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Luxun_1930.jpg',
  'fun_fact': {'uz': 'Zamonaviy Xitoy adabiyotining otasi, «Telba kundaligi» va «A-Q haqiqiy tarixi» asarlari orqali '
                     'feodal xurofotlarni shafqatsiz fosh etgan buyuk adib.',
               'ru': 'Основоположник современной китайской литературы, автор первой модернистской повести на '
                     'разговорном языке «Записки сумасшедшего» (1918).',
               'en': "Foundational father of modern Chinese vernacular literature, author of satirical masterworks 'A "
                     "Madman's Diary' and 'The True Story of Ah Q'."},
  'aliases': ['lu syun', 'лу синь', 'lu xun']},
 {'id': 'lit_auth_088',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Yasunari Kavabata', 'Yukio Misima', 'Osamu Dazay', 'Ryunoske Akutagava'],
              'ru': ['Ясунари Кавабата', 'Юкио Мисима', 'Осаму Дадзай', 'Рюноскэ Акутагава'],
              'en': ['Yasunari Kawabata', 'Yukio Mishima', 'Osamu Dazai', 'Ryunosuke Akutagawa']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ryunoske Akutagava', 'ru': 'Рюноскэ Акутагава', 'en': 'Ryunosuke Akutagawa'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Akutagawa_Ryunosuke_1927.jpg',
  'fun_fact': {'uz': 'Yapon novellasi klassigi, «Rasyomon darvozasi» va «Chakalakzorda» (Kurosava filmi asosi) '
                     "hikoyalari muallifi; nomidagi Yaponiyaning bosh adabiy mukofoti ta'sis etilgan.",
               'ru': 'Классик японской новеллистики («Ворота Расёмон», «В чаще»); в его честь названа главная '
                     'литературная премия Японии.',
               'en': "Japanese master of the short story whose 'In a Grove' and 'Rashomon' inspired Akira Kurosawa's "
                     "landmark film; Japan's top literary prize honors his name."},
  'aliases': ['akutagava', 'ryunoske akutagava', 'акутагава', 'рюноскэ акутагава', 'akutagawa']},
 {'id': 'lit_auth_089',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Yasunari Kavabata', 'Yukio Misima', 'Kenzaburo Oe', 'Ryunoske Akutagava'],
              'ru': ['Ясунари Кавабата', 'Юкио Мисима', 'Кэндзабуро Оэ', 'Рюноскэ Акутагава'],
              'en': ['Yasunari Kawabata', 'Yukio Mishima', 'Kenzaburo Oe', 'Ryunosuke Akutagawa']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Yasunari Kavabata', 'ru': 'Ясунари Кавабата', 'en': 'Yasunari Kawabata'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Yasunari_Kawabata_1968.jpg',
  'fun_fact': {'uz': "1968 yilda adabiyot bo'yicha Nobel mukofotini qo'lga kiritgan birinchi yapon adibi («Qorli "
                     "o'lka», «Ming qanotli turna», «Eski poytaxt»).",
               'ru': 'Первый японский лауреат Нобелевской премии по литературе (1968) за виртуозное мастерство '
                     'повествования («Снежная страна»).',
               'en': 'First Japanese Nobel laureate in Literature (1968), praised for conveying the essence of the '
                     "Japanese mind in novels like 'Snow Country'."},
  'aliases': ['kavabata', 'yasunari kavabata', 'кавабата', 'ясунари кавабата', 'kawabata']},
 {'id': 'lit_auth_090',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Yasunari Kavabata', 'Yukio Misima (Kimitake Xiraoka)', 'Osamu Dazay', 'Kobo Abe'],
              'ru': ['Ясунари Кавабата', 'Юкио Мисима (Кимитакэ Хираока)', 'Осаму Дадзай', 'Кобо Абэ'],
              'en': ['Yasunari Kawabata', 'Yukio Mishima', 'Osamu Dazai', 'Kobo Abe']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Yukio Misima (Kimitake Xiraoka)',
                     'ru': 'Юкио Мисима (Кимитакэ Хираока)',
                     'en': 'Yukio Mishima'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Yukio_Mishima_1956.jpg',
  'fun_fact': {'uz': 'Yaponiyaning eng shov-shuvli millatparvar adibi, «Oltin ibodatxona», «Niqob iqrori» muallifi; '
                     '1970 yilda harbiy bazada harakiri (seppuku) qilib vafot etgan.',
               'ru': 'Один из ярчайших послевоенных авторов Японии («Золотой храм»), совершивший ритуальное сэппуку '
                     'после неудачной попытки монархического переворота.',
               'en': "Prolific Japanese novelist and aesthetic nationalist known for 'The Temple of the Golden "
                     "Pavilion', who committed ritual seppuku in 1970."},
  'aliases': ['misima', 'yukio misima', 'мисима', 'юкио мисима', 'mishima', 'yukio mishima']},
 {'id': 'lit_auth_091',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Ryu Murakami', 'Kadzuo Isiguro', 'Xaruki Murakami', 'Kenzaburo Oe'],
              'ru': ['Рю Мураками', 'Кадзуо Исигуро', 'Харуки Мураками', 'Кэндзабуро Оэ'],
              'en': ['Ryu Murakami', 'Kazuo Ishiguro', 'Haruki Murakami', 'Kenzaburo Oe']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Xaruki Murakami', 'ru': 'Харуки Мураками', 'en': 'Haruki Murakami'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Haruki_Murakami_2009.jpg',
  'fun_fact': {'uz': "Zamonaviy yapon bestseller muallifi, sehrli realizm va melanxoliya ustasi («Norveg o'rmoni», "
                     '«Sohilda Kafka», «1Q84»).',
               'ru': 'Всемирно популярный современный японский писатель, мастер сюрреалистической меланхолии и '
                     'джазовых аллюзий («Норвежский лес», «1Q84»).',
               'en': 'Internationally acclaimed Japanese author blending surrealism with melancholy pop culture in '
                     "'Norwegian Wood' and 'Kafka on the Shore'."},
  'aliases': ['murakami', 'xaruki murakami', 'мураками', 'харуки мураками', 'haruki murakami']},
 {'id': 'lit_auth_092',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Nodim Gursel', 'Yashar Kamol', 'Elif Shafaq', 'Orxan Pamuk'],
              'ru': ['Недим Гюрсель', 'Яшар Кемаль', 'Элиф Шафак', 'Орхан Памук'],
              'en': ['Nedim Gürsel', 'Yashar Kemal', 'Elif Shafak', 'Orhan Pamuk']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Orxan Pamuk', 'ru': 'Орхан Памук', 'en': 'Orhan Pamuk'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Orhan_Pamuk_2009.jpg',
  'fun_fact': {'uz': "2006 yilda adabiyot bo'yicha Nobel mukofotiga sazovor bo'lgan birinchi turk yozuvchisi («Mening "
                     "ismim Qirmizi», «Qor», «Ma'sumlik muzeyi»).",
               'ru': 'Первый турецкий лауреат Нобелевской премии по литературе (2006), автор постмодернистских романов '
                     '«Имя мне — Красный» и «Музей невинности».',
               'en': 'First Turkish Nobel laureate in Literature (2006) whose East-West cultural crossroad novels '
                     "include 'My Name Is Red' and 'Snow'."},
  'aliases': ['orxan pamuk', 'pamuk', 'орхан памук', 'памук', 'orhan pamuk']},
 {'id': 'lit_auth_093',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Najib Mahfuz', 'Taha Husayn', 'Tavfiq al-Hakim', 'Gassan Kanafaniy'],
              'ru': ['Нагиб Махфуз', 'Таха Хусейн', 'Тауфик аль-Хаким', 'Гасан Канафани'],
              'en': ['Naguib Mahfouz', 'Taha Hussein', 'Tawfiq al-Hakim', 'Ghassan Kanafani']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Najib Mahfuz', 'ru': 'Нагиб Махфуз', 'en': 'Naguib Mahfouz'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/6/69/Naguib_Mahfouz_1960s.jpg',
  'fun_fact': {'uz': "1988 yilda adabiyot bo'yicha Nobel mukofotini olgan birinchi arab yozuvchisi, «Qohira "
                     'trilogiyasi» va «Jabalavi bolalari» asarlari muallifi.',
               'ru': 'Египетский классик, первый арабский лауреат Нобелевской премии по литературе (1988) за '
                     'монументальную «Каирскую трилогию».',
               'en': 'Egyptian master and the first Arabic writer to win the Nobel Prize in Literature (1988), '
                     "celebrated for his epic 'Cairo Trilogy'."},
  'aliases': ['najib mahfuz', 'mahfuz', 'нагиб махфуз', 'махфуз', 'naguib mahfouz']},
 {'id': 'lit_auth_094',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Shams Tabriziy', 'Jaloliddin Rumiy (Mavlono)', 'Farididdin Attor', "Sa'diy Sheroziy"],
              'ru': ['Шамс Тебризи', 'Джалаладдин Руми (Мавляна)', 'Фаридаддин Аттар', 'Саади Ширази'],
              'en': ['Shams Tabrizi', 'Jalaluddin Rumi (Mawlana)', 'Farid ud-Din Attar', 'Saadi Shirazi']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Jaloliddin Rumiy (Mavlono)',
                     'ru': 'Джалаладдин Руми (Мавляна)',
                     'en': 'Jalaluddin Rumi (Mawlana)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Mevlana_statue_Buca.jpg',
  'fun_fact': {'uz': "Balxda tug'ilib Ko'nyada yashagan buyuk so'fiy shoir, «Masnaviy» muallifi va Mavlaviya "
                     "darveshlar tariqatining ma'naviy rahnamosi.",
               'ru': 'Величайший суфийский поэт XIII века, автор грандиозной поэмы «Маснави» и вдохновитель ордена '
                     'кружащихся дервишей Мевлеви.',
               'en': "13th-century Persian poet and Sufi mystic in Konya whose spiritual masterpiece 'Masnavi' makes "
                     'him one of the most widely read poets worldwide.'},
  'aliases': ['rumiy', 'jaloliddin rumiy', 'руми', 'джалаладдин руми', 'rumi', 'mawlana']},
 {'id': 'lit_auth_095',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Hofiz Sheroziy', 'Nizomiy Ganjaviy', 'Umar Xayyom', 'Alisher Navoiy'],
              'ru': ['Хафиз Ширази', 'Низами Гянджеви', 'Омар Хайям', 'Алишер Навои'],
              'en': ['Hafez', 'Nizami Ganjavi', 'Omar Khayyam', 'Alisher Navoi']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Umar Xayyom', 'ru': 'Омар Хайям', 'en': 'Omar Khayyam'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Omar_Khayyam_tomb_statue.jpg',
  'fun_fact': {'uz': 'Nishopurda yashagan buyuk matematik (kubik tenglamalar yechimi), astronom (Jaloliy taqvimi) va '
                     'dunyoga mashhur falsafiy ruboiylar ustasi.',
               'ru': 'Персидский учёный-энциклопедист XI века, реформатор календаря, математик и создатель философских '
                     'четверостиший-рубаи.',
               'en': '11th-century Persian mathematician, astronomer, and poet whose existential quatrains became '
                     "globally renowned through FitzGerald's translation."},
  'aliases': ['umar xayyom', 'xayyom', 'омар хайям', 'хайям', 'omar khayyam']},
 {'id': 'lit_auth_096',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Hofiz Sheroziy', 'Jomiy', 'Sanoyiy', "Sa'diy Sheroziy"],
              'ru': ['Хафиз Ширази', 'Джами', 'Санаи', 'Саади Ширази'],
              'en': ['Hafez', 'Jami', 'Sanai', 'Saadi Shirazi']},
  'correct_index': 3,
  'correct_answer': {'uz': "Sa'diy Sheroziy", 'ru': 'Саади Ширази', 'en': 'Saadi Shirazi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Saadi_Shirazi_statue_Shiraz.jpg',
  'fun_fact': {'uz': "Sharq axloq-odobi va hikmatining buyuk ustozi, «Guliston» (nasriy-she'riy) va «Bo'ston» "
                     "(she'riy) durdonalari muallifi.",
               'ru': 'Классик персидской литературы XIII века, моралист и путешественник, автор бессмертных сборников '
                     'притч «Гулистан» и «Бустан».',
               'en': 'Major Persian poet and master moralist of the 13th century, revered for his didactic prose and '
                     "verse masterworks 'Gulistan' and 'Bustan'."},
  'aliases': ["sa'diy", 'saadi', 'саади', 'саади ширази', 'saadi shirazi']},
 {'id': 'lit_auth_097',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Hofiz Sheroziy (Xoja Hofiz)', "Sa'diy Sheroziy", 'Umar Xayyom', 'Jaloliddin Rumiy'],
              'ru': ['Хафиз Ширази (Шамсаддин Мухаммад)', 'Саади Ширази', 'Омар Хайям', 'Джалаладдин Руми'],
              'en': ['Hafez Shirazi', 'Saadi Shirazi', 'Omar Khayyam', 'Jalaluddin Rumi']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Hofiz Sheroziy (Xoja Hofiz)',
                     'ru': 'Хафиз Ширази (Шамсаддин Мухаммад)',
                     'en': 'Hafez Shirazi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Hafez_portrait.jpg',
  'fun_fact': {'uz': "Sharq g'azalnavisligining eng buyuk sultoni, Gyoteni lol qoldirgan va «G'arbu sharq devoni»ga "
                     'ilhom bergan Sheroz bulbuli.',
               'ru': '«Язык сокровенных тайн», величайший мастер персидской газели XIV века, вдохновивший Гёте на '
                     'создание «Западно-восточного дивана».',
               'en': 'The supreme master of the Persian ghazal in 14th-century Shiraz whose mystical poetry inspired '
                     "Goethe's 'West-Eastern Divan'."},
  'aliases': ['hofiz', 'hofiz sheroziy', 'хафиз', 'хафиз ширази', 'hafez', 'hafez shirazi']},
 {'id': 'lit_auth_098',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Nizomiy Ganjaviy', 'Abulqosim Firdavsiy', 'Rudakiy', 'Asadiy Tusiy'],
              'ru': ['Низами Гянджеви', 'Абулькасим Фирдоуси', 'Рудаки', 'Асади Туси'],
              'en': ['Nizami Ganjavi', 'Ferdowsi', 'Rudaki', 'Asadi Tusi']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Abulqosim Firdavsiy', 'ru': 'Абулькасим Фирдоуси', 'en': 'Ferdowsi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Ferdowsi_statue_Rome.jpg',
  'fun_fact': {'uz': 'Fors-tojik milliy eposi «Shohnoma» muallifi; 30 yil davomida 50 000 bayt yaratib, qadimgi Eron '
                     'va Turon afsonaviy podshohlari tarixini tiklagan.',
               'ru': 'Создатель монументального эпоса «Шахнаме» («Книга царей»), возродивший персидский язык и '
                     'мифологию героев Заля и Рустама.',
               'en': "Author of the 'Shahnameh' (Book of Kings), national epic of Greater Iran preserving 50,000 "
                     'couplets of Persian history and legend.'},
  'aliases': ['firdavsiy', 'фирдоуси', 'ferdowsi']},
 {'id': 'lit_auth_099',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Alisher Navoiy', 'Amir Xusrav Dehlaviy', 'Nizomiy Ganjaviy', 'Abdurahmon Jomiy'],
              'ru': ['Алишер Навои', 'Амир Хосров Дехлеви', 'Низами Гянджеви', 'Абдурахман Джами'],
              'en': ['Alisher Navoi', 'Amir Khusrow', 'Nizami Ganjavi', 'Jami']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Nizomiy Ganjaviy', 'ru': 'Низами Гянджеви', 'en': 'Nizami Ganjavi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Nizami_Ganjavi_statue_Baku.jpg',
  'fun_fact': {'uz': "Sharq adabiyotida birinchi «Xamsa» («Panj ganj» — Besh xazina) an'anasiga asos solgan XII asr "
                     'daho shoiri («Maxzan ul-asror», «Xusrav va Shirin», «Layli va Majnun»).',
               'ru': 'Классик восточной поэзии XII века, родоначальник жанра «Хамсы» («Пятерицы»), прославивший сюжеты '
                     'о Лейли и Меджнуне и Хосрове и Ширин.',
               'en': "12th-century poet who pioneered the 'Khamsa' (Quintet) tradition, immortalizing tragic love in "
                     "'Layla and Majnun' and 'Khosrow and Shirin'."},
  'aliases': ['nizomiy', 'nizomiy ganjaviy', 'низами', 'низами гянджеви', 'nizami', 'nizami ganjavi']},
 {'id': 'lit_auth_0100',
  'sub_mode': 'authors',
  'question': {'uz': 'Suratda tasvirlangan mashhur adib / shoir kim?',
               'ru': 'Какой знаменитый писатель или поэт изображен на портрете?',
               'en': 'Which famous author or poet is depicted in this portrait?'},
  'options': {'uz': ['Firdavsiy', 'Ibn Sino', 'Daqiqiy', 'Abu Abdulloh Rudakiy'],
              'ru': ['Фирдоуси', 'Ибн Сина', 'Дакики', 'Абу Абдаллах Рудаки'],
              'en': ['Ferdowsi', 'Avicenna', 'Daqiqi', 'Rudaki']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Abu Abdulloh Rudakiy', 'ru': 'Абу Абдаллах Рудаки', 'en': 'Rudaki'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Rudaki_statue_Dushanbe.jpg',
  'fun_fact': {'uz': "«Fors-tojik she'riyatining otasi» va Somoniylar saroyining bosh shoiri; «Kalila va Dimna» "
                     "masallarini she'riy yo'lga solgan daho.",
               'ru': '«Адам поэтов», основоположник классической персидско-таджикской поэзии IX–X веков при дворе '
                     'Саманидов в Бухаре.',
               'en': "The 'Adam of Poets', considered the foundational father of classical Persian poetry at the "
                     '10th-century Samanid court in Bukhara.'},
  'aliases': ['rudakiy', 'рудаки', 'rudaki']},
 {'id': 'lit_char_001',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Toshkentlik savdogar Yusufbek hojining o'qimishli, olijanob o'g'liman.\n"
                     "2-maslahat: Marg'ilonda Kumushbibini uchratib, unga bir ko'rishda oshiq bo'laman.\n"
                     "3-maslahat: Abdulla Qodiriyning o'zbek adabiyotidagi ilk romanining bosh qahramoniman.",
               'ru': 'Подсказка 1: Образованный и благородный юноша из Ташкента, сын купца Юсуфбека-ходжи.\n'
                     'Подсказка 2: В Маргилане встречаю прекрасную Кумушбиби и влюбляюсь в неё с первого взгляда.\n'
                     'Подсказка 3: Главный герой первого узбекского романа «Минувшие дни» Абдуллы Кадыри.',
               'en': 'Clue 1: Educated and noble young merchant from Tashkent, son of Yusufbek Haji.\n'
                     'Clue 2: In Margilan, I meet Kumushbibi and fall deeply in love with her.\n'
                     "Clue 3: The tragic male protagonist of Abdulla Qadiri's groundbreaking first Uzbek novel 'Past "
                     "Days'."},
  'options': {'uz': ['Otabek', 'Anvar', "Yo'lchi", 'Homid'],
              'ru': ['Отабек', 'Анвар', 'Юлчи', 'Хомид'],
              'en': ['Otabek', 'Anvar', 'Yolchi', 'Homid']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Otabek', 'ru': 'Отабек', 'en': 'Otabek'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Abdulla_Qodiriy_1920s.jpg/640px-Abdulla_Qodiriy_1920s.jpg',
  'fun_fact': {'uz': "Otabek obrazi o'zbek adabiyotida yangi zamon ziyolisi, ilg'or fikrli va erkin sevgiga intiluvchi "
                     'qahramon timsolidir.',
               'ru': 'Отабек символизирует новое поколение просвещенных узбеков рубежа эпох, стремящихся к свободе '
                     'выбора и искренней любви.',
               'en': 'Otabek represents the enlightened generation of young Central Asians striving for modern values '
                     'and true love.'},
  'aliases': ['otabek', 'отабек', "otabek yusufbek hoji o'g'li"]},
 {'id': 'lit_char_002',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Marg'ilonlik Mirzakarim qutidor va Oftob oyimning suyukli qiziman.\n"
                     "2-maslahat: Husnda tengsiz, nozikta'b qiz bo'lib, taqdirim rashk qurboni sifatida zaharlanish "
                     'bilan fojiali yakun topadi.\n'
                     "3-maslahat: «O'tkan kunlar» romanining bosh ayol qahramoni va Otabekning haqiqiy sevgilisiman.",
               'ru': 'Подсказка 1: Любимая дочь маргиланского торговца Мирзакарима-кутидора и Офтоб-оим.\n'
                     'Подсказка 2: Девушка неземной красоты, ставшая жертвой ревности и погибшая от яда.\n'
                     'Подсказка 3: Главная героиня романа Абдуллы Кадыри «Минувшие дни», возлюбленная Отабека.',
               'en': 'Clue 1: Beloved daughter of Mirzakarim Qutidor and Oftob Oyim from Margilan.\n'
                     'Clue 2: A maiden of ethereal beauty who falls victim to poisoned food caused by domestic '
                     'jealousy.\n'
                     "Clue 3: The tragic female protagonist of Abdulla Qadiri's classic 'Past Days', true love of "
                     'Otabek.'},
  'options': {'uz': ['Zaynab', 'Kumushbibi', "Ra'no", 'Barchinoy'],
              'ru': ['Зайнаб', 'Кумушбиби', 'Рано', 'Барчиной'],
              'en': ['Zaynab', 'Kumushbibi', 'Rano', 'Barchinoy']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Kumushbibi', 'ru': 'Кумушбиби', 'en': 'Kumushbibi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Abdulla_Qodiriy_1920s.jpg/640px-Abdulla_Qodiriy_1920s.jpg',
  'fun_fact': {'uz': "Kumushbibining fojiali o'limi o'zbek adabiyotidagi eng ta'sirli va yurakni larzaga soluvchi "
                     'sahnalardan biridir.',
               'ru': 'Сцена гибели Кумушбиби считается одной из самых эмоциональных и драматичных в узбекской '
                     'классической литературе.',
               'en': 'The deathbed scene of Kumushbibi is regarded as one of the most poignant emotional climaxes in '
                     'Central Asian fiction.'},
  'aliases': ['kumushbibi', 'kumush', 'кумушбиби', 'кумуш']},
 {'id': 'lit_char_003',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Ota-onasining qistovi bilan Otabekka ikkinchi xotin qilib uzatilgan toshkentlik '
                     'qizman.\n'
                     "2-maslahat: Erimning ko'ngli doimo Marg'ilondagi kundoshimda bo'lgani tufayli qattiq rashk "
                     "o'tida yonaman.\n"
                     "3-maslahat: Oxir-oqibat Kumushbibining ovqatiga zahar qo'shib, uning o'limiga sababchi bo'laman "
                     "va aqlan parishon bo'laman.",
               'ru': 'Подсказка 1: Девушка из Ташкента, выданная замуж за Отабека второй женой по настоянию его '
                     'родителей.\n'
                     'Подсказка 2: Терзалась ревностью из-за того, что муж всем сердцем любил соперницу из Маргилана.\n'
                     'Подсказка 3: Подсыпала яд в еду Кумушбиби, став виновницей трагедии, и потеряла рассудок в '
                     'романе «Минувшие дни».',
               'en': "Clue 1: Forced into marriage as Otabek's second wife due to his mother's insistence.\n"
                     'Clue 2: Consumed by bitter jealousy because my husband never ceased loving his first wife.\n'
                     "Clue 3: I tragically poisoned Kumushbibi's pomegranate dish and lost my sanity in Abdulla "
                     "Qadiri's 'Past Days'."},
  'options': {'uz': ['Kumushbibi', "Xushro'y", 'Zaynab', 'Oftob oyim'],
              'ru': ['Кумушбиби', 'Хушруй', 'Зайнаб', 'Офтоб оим'],
              'en': ['Kumushbibi', 'Khushroy', 'Zaynab', 'Oftob Oyim']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Zaynab', 'ru': 'Зайнаб', 'en': 'Zaynab'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Abdulla_Qodiriy_1920s.jpg/640px-Abdulla_Qodiriy_1920s.jpg',
  'fun_fact': {'uz': "Qodiriy Zaynabni mutlaq yovuz emas, balki feodal xurofotlar va ko'pxotinlilik qurboni bo'lgan "
                     'murakkab qahramon sifatida tasvirlagan.',
               'ru': 'Кадыри показал Зайнаб не абсолютной злодейкой, а жертвой патриархальных устоев и полигамии.',
               'en': 'Qadiri depicted Zaynab not as pure evil, but as a tragic victim of feudal traditions and '
                     'polygamy.'},
  'aliases': ['zaynab', 'зайнаб']},
 {'id': 'lit_char_004',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Mirzo Bobur va Xudoyorxon davri Qo'qon xonligidagi munshiy, xattot yigitman.\n"
                     "2-maslahat: Mirzakarim munshiy oilasida tarbiyalanib, uning qizi Ra'noga ko'ngil qo'yganman.\n"
                     '3-maslahat: Xon saroyining qallobliklariga qarshi kurashuvchi, «Mehrobdan chayon» romanining '
                     'bosh qahramoniman.',
               'ru': 'Подсказка 1: Образованный юноша-писарь (мунши) при дворе Худояр-хана в Коканде.\n'
                     'Подсказка 2: Воспитывался в семье Мирзакарима-мунши и полюбил его дочь Рано.\n'
                     'Подсказка 3: Главный герой исторического романа Абдуллы Кадыри «Скорпион из алтаря».',
               'en': "Clue 1: Gifted young calligrapher and court scribe (munshi) in Kokand during Khudayar Khan's "
                     'reign.\n'
                     "Clue 2: Raised in Mirzakarim Munshi's household and deeply in love with his daughter Rano.\n"
                     "Clue 3: Protagonist of Abdulla Qadiri's historical masterpiece 'Scorpion from the Altar'."},
  'options': {'uz': ['Otabek', "Safar bo'zchi", 'Shohruhxon', 'Anvar'],
              'ru': ['Отабек', 'Сафар бузчи', 'Шахруххан', 'Анвар'],
              'en': ['Otabek', 'Safar', 'Shahrukh', 'Anvar']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Anvar', 'ru': 'Анвар', 'en': 'Anvar'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Abdulla_Qodiriy_1920s.jpg/640px-Abdulla_Qodiriy_1920s.jpg',
  'fun_fact': {'uz': "Anvar Qodiriy qalamiga mansub «Mehrobdan chayon»da xon zulmiga mardona bosh ko'targan jasur "
                     'kotib sifatida gavdalanadi.',
               'ru': 'Анвар воплощает смелость, острый ум и неподкупность перед лицом жестокого кокандского '
                     'деспотизма.',
               'en': 'Anvar embodies integrity, sharp wit, and defiance against the corrupt tyrannical rulers of the '
                     'Kokand Khanate.'},
  'aliases': ['anvar', 'анвар', 'mirzo anvar']},
 {'id': 'lit_char_005',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Mirzakarim munshiyning aqlli, zukko va she'riyatga oshiq erka qiziman.\n"
                     '2-maslahat: Xudoyorxonga xotinlikka tanlanganimda xonning taxt-u tojini rad etib, bolalikdagi '
                     'sevgilim Anvarga sodiq qolaman.\n'
                     '3-maslahat: Abdulla Qodiriyning «Mehrobdan chayon» romanidagi jasur bosh ayol qahramonman.',
               'ru': 'Подсказка 1: Дочь Мирзакарима-мунши, умная, остроумная и образованная девушка.\n'
                     'Подсказка 2: Отвергла предложение стать наложницей Худояр-хана ради любви к бедному писарю '
                     'Анвару.\n'
                     'Подсказка 3: Главная героиня романа Абдуллы Кадыри «Скорпион из алтаря».',
               'en': 'Clue 1: Witty, educated, and poetry-loving daughter of scribe Mirzakarim Munshi.\n'
                     'Clue 2: Defied the tyrannical Khan of Kokand when selected for his royal harem, staying faithful '
                     'to Anvar.\n'
                     "Clue 3: Heroine of Abdulla Qadiri's famous romantic and social novel 'Scorpion from the Altar'."},
  'options': {'uz': ["Ra'no", 'Kumushbibi', 'Nigor oyim', 'Zaynab'],
              'ru': ['Рано', 'Кумушбиби', 'Нигор оим', 'Зайнаб'],
              'en': ['Rano', 'Kumushbibi', 'Nigor Oyim', 'Zaynab']},
  'correct_index': 0,
  'correct_answer': {'uz': "Ra'no", 'ru': 'Рано', 'en': 'Rano'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Abdulla_Qodiriy_1920s.jpg/640px-Abdulla_Qodiriy_1920s.jpg',
  'fun_fact': {'uz': "Ra'no o'zbek adabiyotida xon istagiga ochiqdan-ochiq qarshi chiqa olgan matonatli ayol "
                     'timsolidir.',
               'ru': 'Образ Рано стал символом женского достоинства, верности и бесстрашного сопротивления феодальному '
                     'насилию.',
               'en': 'Rano stands out in Uzbek literature as a symbol of female courage and integrity against royal '
                     'oppression.'},
  'aliases': ["ra'no", 'rano', 'рано', 'раъно']},
 {'id': 'lit_char_006',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Qo'ng'irot elida Boybo'ri xonadonida dunyoga kelgan pahlavonman, asl ismim "
                     'Hakimbek.\n'
                     "2-maslahat: Otim Boychibor va sehrli 14 botmonli yoy-o'qim bor; Qalmoq yurtida 7 yil zindonda "
                     'yotaman.\n'
                     '3-maslahat: Turkiy xalqlarning eng buyuk qahramonlik dostonining alp bosh qahramoniman.',
               'ru': 'Подсказка 1: Богатырь из племени кунграт, сын правителя Байбури, настоящее имя — Хакимбек.\n'
                     'Подсказка 2: Мой верный конь — Байчибар, провел семь лет в темнице в калмыцкой земле.\n'
                     'Подсказка 3: Главный богатырь одноименного общетюркского героического эпоса.',
               'en': 'Clue 1: Hero of the Kungrat tribe, born to ruler Boybori, with the birth name Hakimbek.\n'
                     'Clue 2: My legendary steed is Boychibor, and I endured seven years in an underground dungeon.\n'
                     'Clue 3: Legendary warrior hero of the monumental Central Asian heroic epic named after me.'},
  'options': {'uz': ["Go'ro'g'li", 'Alpomish (Hakimbek)', 'Rustam doston', "Kuntug'mish"],
              'ru': ['Гёроглы', 'Алпомыш (Хакимбек)', 'Рустам', 'Кунтугмыш'],
              'en': ['Gorogly', 'Alpamysh (Hakimbek)', 'Rustam', 'Kuntugmysh']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Alpomish (Hakimbek)', 'ru': 'Алпомыш (Хакимбек)', 'en': 'Alpamysh (Hakimbek)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Alpomish_statue_Termez.jpg/640px-Alpomish_statue_Termez.jpg',
  'fun_fact': {'uz': "«Alpomish» dostoni Fozil Yo'ldosh o'g'lidan yozib olingan bo'lib, UNESCO tomonidan 1999 yilda "
                     '1000 yillik yubileyi nishonlangan.',
               'ru': 'Тысячелетие эпоса «Алпомыш» широко отмечалось под эгидой ЮНЕСКО в 1999 году.',
               'en': 'The 1000th anniversary of the epic of Alpamysh was celebrated worldwide under UNESCO auspices in '
                     '1999.'},
  'aliases': ['alpomish', 'hakimbek', 'алпомыш', 'хакимбек', 'alpamysh']},
 {'id': 'lit_char_007',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Boybichaning qizi, Alpomishning beshikkerti bo'lgan qahramon qizman.\n"
                     "2-maslahat: Qalmoq botirlari sovchi qo'yganda to'rtta shart (poyga, yoy otish, kurash, nishon "
                     "urish) qo'yganman.\n"
                     '3-maslahat: «Alpomish» dostonining jasur, vafodor va alp qiyofasidagi bosh ayol qahramoniman.',
               'ru': 'Подсказка 1: Дочь бая Байсары, нареченная невеста богатыря Алпомыша с колыбели.\n'
                     'Подсказка 2: Поставила калмыцким женихам четыре тяжелейших богатырских условия (скачки, стрельба '
                     'из лука, борьба).\n'
                     'Подсказка 3: Главная героиня узбекского эпоса «Алпомыш», образец верности и мужества.',
               'en': 'Clue 1: Daughter of Baysari, betrothed in cradle to hero Alpamysh.\n'
                     'Clue 2: Imposed four epic tests (horse race, archery, wrestling, target shooting) upon Kalmyk '
                     'suitors.\n'
                     "Clue 3: Heroine of the epic 'Alpamysh', renowned for her loyalty, courage, and athletic "
                     'prowess.'},
  'options': {'uz': ['Kumushbibi', "Qaldirg'ochoyim", 'Barchinoy (Gulbarchin)', 'Tavka oyim'],
              'ru': ['Кумушбиби', 'Калдыргач', 'Барчиной (Гульбарчин)', 'Тавка'],
              'en': ['Kumushbibi', 'Qaldirgoch', 'Barchinoy (Gulbarchin)', 'Tavka']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Barchinoy (Gulbarchin)', 'ru': 'Барчиной (Гульбарчин)', 'en': 'Barchinoy (Gulbarchin)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Alpomish_statue_Termez.jpg/640px-Alpomish_statue_Termez.jpg',
  'fun_fact': {'uz': "Barchinoy dostonlarda nafaqat go'zallik, balki mardlik, merganlik va o'z taqdirini o'zi hal "
                     'qilish qudratiga ega alp ayol timsolidir.',
               'ru': 'Гульбарчин — образ богатырки, способной на равных состязаться с сильнейшими воинами степей.',
               'en': 'Gulbarchin is a warrior maiden who set heroic martial contests to determine her own suitor.'},
  'aliases': ['barchinoy', 'gulbarchin', 'барчиной', 'гульбарчин']},
 {'id': 'lit_char_008',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Mozorda, vafot etgan onadan tug'ilganim sababli ismim «go'r o'g'li» ma'nosini "
                     'beradi.\n'
                     '2-maslahat: Qirot laqabli afsonaviy uchar qanotli otim va Chambil elida qirq yigitim bor.\n'
                     "3-maslahat: Ko'plab turkiy xalqlar folklorida adolat va erkinlik kurashchisi bo'lgan turkum "
                     'dostonlar qahramoniman.',
               'ru': 'Подсказка 1: Родился в могиле у умершей матери, откуда и получил свое имя.\n'
                     'Подсказка 2: Мой крылатый конь — Гырат (Кирот), а моя страна и крепость — Чамбил с дружиной из '
                     'сорока джигитов.\n'
                     'Подсказка 3: Легендарный эпический герой циклов тюркских дастанов, защитник бедных и борец за '
                     'справедливость.',
               'en': "Clue 1: Born in a tomb to a deceased mother, which gave rise to my mystical name ('Son of the "
                     "Grave').\n"
                     'Clue 2: My winged steed is Gyrat (Qirot) and my sovereign fortress is Chambil, defended by 40 '
                     'warriors.\n'
                     'Clue 3: Epic hero of a sprawling cycle of Turkic heroic oral traditions.'},
  'options': {'uz': ['Alpomish', 'Avazxon', 'Rustam zol', "Go'ro'g'li (Ro'shan)"],
              'ru': ['Алпомыш', 'Авазхан', 'Рустам Зал', 'Гёроглы (Кёроглу)'],
              'en': ['Alpamysh', 'Avazkhan', 'Rustam Zal', 'Gorogly (Koroglu)']},
  'correct_index': 3,
  'correct_answer': {'uz': "Go'ro'g'li (Ro'shan)", 'ru': 'Гёроглы (Кёроглу)', 'en': 'Gorogly (Koroglu)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Gorogly_monument_Ashgabat.jpg/640px-Gorogly_monument_Ashgabat.jpg',
  'fun_fact': {'uz': "Go'ro'g'li turkumi o'zbek baxshilari repertuarida 60 dan ortiq mustaqil dostonlarni o'z ichiga "
                     'oladi.',
               'ru': 'Цикл о Гёроглы у узбекских сказителей-бахши включает более 60 самостоятельных эпических '
                     'сказаний.',
               'en': 'The epic cycle of Gorogly contains over 60 distinct poetic tales in Uzbek bardic oral lore.'},
  'aliases': ["go'ro'g'li", 'gorogli', 'koroglu', 'гёроглы', 'кёроглу']},
 {'id': 'lit_char_009',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Dars tayyorlashni yomon ko'radigan, ammo bir kunda butun dunyoni lol qoldirishni "
                     'orzu qiluvchi qishloqi bolaman.\n'
                     "2-maslahat: Bo'yi bir qarich keladigan g'alati sehrgar — «Sehrli qalpoqcha» egasiga aylanaman.\n"
                     "3-maslahat: Xudoyberdi To'xtaboyevning eng mashhur sarguzasht qissasining bosh qahramoniman.",
               'ru': 'Подсказка 1: Деревенский мальчишка-лентяй, мечтающий прославиться без всякого труда.\n'
                     'Подсказка 2: Находит шапку-невидимку, становится невидимым и попадает в курьезные приключения.\n'
                     'Подсказка 3: Главный персонаж знаменитой детской повести Худайберды Тухтабаева «Верхом на желтом '
                     'диве».',
               'en': 'Clue 1: A mischievous, lazy village boy who dreams of becoming famous without studying.\n'
                     'Clue 2: Acquired a magical invisibility cap, creating hilarious chaos before learning '
                     'responsibility.\n'
                     "Clue 3: Protagonist of Khudoyberdi Tokhtabayev's beloved children's adventure 'Riding the Yellow "
                     "Giant'."},
  'options': {'uz': ["Hoshimjon Ro'ziyev", 'Qoravoy', 'Shum bola', 'Akrom'],
              'ru': ['Хошимжон Рузиев', 'Каравой', 'Озорник', 'Акром'],
              'en': ['Hoshimjon Roziyev', 'Qoravoy', 'Shum bola', 'Akrom']},
  'correct_index': 0,
  'correct_answer': {'uz': "Hoshimjon Ro'ziyev", 'ru': 'Хошимжон Рузиев', 'en': 'Hoshimjon Roziyev'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Hudoyberdi_Tohtaboev.jpg/640px-Hudoyberdi_Tohtaboev.jpg',
  'fun_fact': {'uz': '«Sariq devni minib» asari dunyoning 30 dan ortiq tillariga tarjima qilingan va Italiyada Janubiy '
                     "bolalar adabiyoti mukofotiga sazovor bo'lgan.",
               'ru': 'Повесть «Верхом на желтом диве» была переведена на десятки языков и удостоена международной '
                     'литературной премии в Италии.',
               'en': "The novel was translated into over 30 languages and won prestigious children's literature awards "
                     'in Europe.'},
  'aliases': ['hoshimjon', "hoshimjon ro'ziyev", 'хошимжон', 'хошимжон рузиев']},
 {'id': 'lit_char_010',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Qornimni to'ydirish uchun podachi, novvoy shogirdi, firibgar boylar va boyvachchalar "
                     'xizmatida yuraman.\n'
                     '2-maslahat: Gapdonlik, quvlik va hozirjavoblik bilan har qanday mushkul vaziyatdan chiqib '
                     'ketaman.\n'
                     "3-maslahat: G'afur G'ulomning avtobiografik mashhur qissasining sarguzashtsevar bosh "
                     'qahramoniman.',
               'ru': 'Подсказка 1: Мальчик из бедной ташкентской семьи, вынужденный скитаться в поисках куска хлеба.\n'
                     'Подсказка 2: Находчивый, остроумный хитрец, служащий баям, шарлатанам и ворам, но всегда '
                     'обводящий их вокруг пальца.\n'
                     'Подсказка 3: Главный персонаж автобиографической повести Гафура Гуляма «Озорник».',
               'en': 'Clue 1: Resourceful street-smart orphan boy wandering across early 20th-century Uzbekistan '
                     'seeking food.\n'
                     'Clue 2: Outwitting corrupt mullahs, greedy merchants, and bandits with sheer quick-witted '
                     'humor.\n'
                     "Clue 3: Protagonist of Gafur Gulyam's satirical autobiographical novella 'The Mischievous Boy'."},
  'options': {'uz': ['Hoshimjon', 'Shum bola (Qoravoy)', "Yo'lchi", 'Otabek'],
              'ru': ['Хошимжон', 'Озорник (Шум бола)', 'Юлчи', 'Отабек'],
              'en': ['Hoshimjon', 'Shum Bola (The Mischievous Boy)', 'Yolchi', 'Otabek']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Shum bola (Qoravoy)', 'ru': 'Озорник (Шум бола)', 'en': 'Shum Bola (The Mischievous Boy)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Gafur_Gulyam_1930s.jpg/640px-Gafur_Gulyam_1930s.jpg',
  'fun_fact': {'uz': "«Shum bola» asosida 1977 yilda Damir Salimov tomonidan suratga olingan kinofilm o'zbek "
                     'kinosining durdonasiga aylangan.',
               'ru': 'Фильм «Озорник» 1977 года режиссера Дамира Салимова входит в золотой фонд узбекского '
                     'кинематографа.',
               'en': "The 1977 cinematic adaptation of 'Shum Bola' became an enduring landmark in Uzbek classic "
                     'cinema.'},
  'aliases': ['shum bola', 'шум бола', 'озорник', 'qoravoy']},
 {'id': 'lit_char_011',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Qishloqdan Toshkentga tog'asi Mirzakarimboydan ish va najot izlab kelgan mehnatkash "
                     'yigitman.\n'
                     "2-maslahat: Boyning qabihliklari, sudxo'rligi va Gulnorga ko'z olaytirganiga qarshi bosh "
                     "ko'taraman.\n"
                     "3-maslahat: Oybekning «Qutlug' qon» romanidagi haqiqatparvar va fojiali bosh qahramonman.",
               'ru': 'Подсказка 1: Бедный честный батрак, пришедший в Ташкент в поисках заработка к богатому дяде '
                     'Мирзакаримбаю.\n'
                     'Подсказка 2: Борется за честь любимой девушки Гульнор и справедливость для простых тружеников.\n'
                     'Подсказка 3: Главный герой романа Айбека «Священная кровь».',
               'en': 'Clue 1: Honest young laborer arriving in Tashkent seeking work from his wealthy uncle '
                     'Mirzakarimboy.\n'
                     'Clue 2: Stood bravely against exploitation to defend the oppressed workers and his beloved '
                     'Gulnor.\n'
                     "Clue 3: Protagonist of Aybek's historic social novel 'Sacred Blood'."},
  'options': {'uz': ['Yodgor', 'Otabek', "Yo'lchi", 'Anvar'],
              'ru': ['Ядгар', 'Отабек', 'Юлчи', 'Анвар'],
              'en': ['Yodgor', 'Otabek', 'Yolchi', 'Anvar']},
  'correct_index': 2,
  'correct_answer': {'uz': "Yo'lchi", 'ru': 'Юлчи', 'en': 'Yolchi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Musa_Tashmukhamedov_Oybek.jpg/640px-Musa_Tashmukhamedov_Oybek.jpg',
  'fun_fact': {'uz': "«Qutlug' qon» romanida Yo'lchi obrazi 1916 yilgi xalq g'alayonlari arafasidagi milliy uyg'onish "
                     'timsolidir.',
               'ru': 'Образ Юлчи олицетворяет пробуждение классового и национального самосознания накануне восстания '
                     '1916 года.',
               'en': 'Yolchi reflects the rising social consciousness and tragic resistance of pre-revolutionary '
                     'Central Asia.'},
  'aliases': ["yo'lchi", 'yolchi', 'юлчи']},
 {'id': 'lit_char_012',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Bolalikda qattiq xiyonat va xo'rlikni boshidan kechirib, jinoiy olamning qudratli "
                     'avtoritetiga aylangan shaxsman.\n'
                     "2-maslahat: Bir qo'lida qonun, bir qo'lida qon bilan o'z mafiya saltanatimni boshqaraman, ammo "
                     'qizim Zaynabning taqdiri meni sindiradi.\n'
                     '3-maslahat: Tohir Malikning mashhur «Shaytanat» asarining markaziy va ziddiyatli personajiman.',
               'ru': 'Подсказка 1: Человек с трагическим детством, ставший могущественным главой подпольного '
                     'преступного мира.\n'
                     'Подсказка 2: Жестокий мафиозный авторитет, чьей величайшей слабостью и болью стала судьба '
                     'любимой дочери Зайнаб.\n'
                     'Подсказка 3: Главный герой культового криминального романа Тохира Малика «Шайтанат».',
               'en': 'Clue 1: A man hardened by childhood trauma who rose to become an almighty underworld crime '
                     'boss.\n'
                     'Clue 2: Controlled a mafia empire with ruthless discipline, yet was spiritually shattered by his '
                     "daughter's tragic fate.\n"
                     "Clue 3: The enigmatic antihero protagonist of Tohir Malik's blockbuster crime epic 'Shaytanat'."},
  'options': {'uz': ['Chuvrindi', 'Hosiyatxon', 'Zelimxon', 'Asadbek'],
              'ru': ['Чувринди', 'Хосият', 'Зелимхан', 'Асадбек'],
              'en': ['Chuvrindi', 'Hosiyat', 'Zelimkhan', 'Asadbek']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Asadbek', 'ru': 'Асадбек', 'en': 'Asadbek'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Tohir_Malik.jpg/640px-Tohir_Malik.jpg',
  'fun_fact': {'uz': "«Shaytanat» asari o'zbek adabiyotidagi ilk detektiv-mafiya epopeyasi bo'lib, Asadbek rolini "
                     'ekranda Yoqub Ahmedov mahorat bilan ijro etgan.',
               'ru': 'В популярной многосерийной экранизации «Шайтаната» роль Асадбека непревзойденно сыграл народный '
                     'артист Ёкуб Ахмедов.',
               'en': 'In the TV series based on the novel, Asadbek was portrayed by legendary Uzbek actor Yoqub '
                     'Ahmedov.'},
  'aliases': ['asadbek', 'асадбек']},
 {'id': 'lit_char_013',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Yetti o'g'il, yetti kelin va o'nlab nabiralarni temir intizom bilan boshqaruvchi "
                     'qudratli qaynona.\n'
                     "2-maslahat: Kelinlarim menga qarshi «qo'zg'olon» ko'targanida o'zbekona donolik va mehr bilan "
                     'oilani saqlab qolaman.\n'
                     "3-maslahat: Said Ahmadning o'zbek sahnasining shoh asari bo'lmish «Kelinlar qo'zg'oloni» "
                     'komediyasining bosh qahramoniman.',
               'ru': 'Подсказка 1: Властная, но мудрая и любящая свекровь, держащая в строгом порядке семерых сыновей '
                     'и снох.\n'
                     'Подсказка 2: Переживает «бунт невесток» и сохраняет мир в огромной семье благодаря жизненной '
                     'мудрости.\n'
                     'Подсказка 3: Главная героиня комедии Саида Ахмада «Бунт невесток».',
               'en': 'Clue 1: Formidable yet deeply caring matriarch ruling an extended family of seven sons and their '
                     'wives.\n'
                     'Clue 2: Weathered a domestic rebellion of her daughters-in-law through wisdom and maternal '
                     'warmth.\n'
                     "Clue 3: Central matriarch of Said Ahmad's classic theatrical comedy 'The Revolt of the "
                     "Daughters-in-Law'."},
  'options': {'uz': ['Farmonbibi', 'Nigora', 'Kifoyatxon', 'Sotti'],
              'ru': ['Фармонбиби', 'Нигора', 'Кифоят', 'Сотти'],
              'en': ['Farmonbibi', 'Nigora', 'Kifoyat', 'Sotti']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Farmonbibi', 'ru': 'Фармонбиби', 'en': 'Farmonbibi'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Said_Ahmad.jpg/640px-Said_Ahmad.jpg',
  'fun_fact': {'uz': "Farmonbibi rolini teatr va kinoda buyuk o'zbek aktrisasi Tursunoy Ja'farova hamda Zaynab "
                     'Sadriyeva ijro etgan.',
               'ru': 'Бессмертный сценический образ Фармонбиби блистательно воплотила народная артистка Зайнаб '
                     'Садриева.',
               'en': 'Farmonbibi became an iconic archetype in Central Asian drama, immortalized by actress Zaynab '
                     'Sadriyeva.'},
  'aliases': ['farmonbibi', 'фармонбиби']},
 {'id': 'lit_char_014',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Xoqonning o'g'li bo'lsam-da, taxtdan voz kechib tosh yo'nish va muhandislik "
                     "san'atini o'rgangan shahzodaman.\n"
                     "2-maslahat: Arman malikasining xalqiga suv chiqarish uchun tog'ni teshib, toshlarni kuldek "
                     'maydalayman.\n'
                     '3-maslahat: Alisher Navoiy «Xamsa»sining ikkinchi dostonidagi buyuk mehnat va sadoqat '
                     'timsoliman.',
               'ru': 'Подсказка 1: Сын китайского хакана, отвергший трон ради изучения ремесел, зодчества и '
                     'каменотесного дела.\n'
                     'Подсказка 2: Ради любви к армянской красавице Ширин пробивает канал сквозь гранитные скалы.\n'
                     'Подсказка 3: Главный герой поэмы Алишера Навои «Фархад и Ширин».',
               'en': 'Clue 1: Prince of China who renounced the throne to master stone-carving, engineering, and fine '
                     'arts.\n'
                     'Clue 2: Pierced monumental mountain rock to bring water to the suffering people of Princess '
                     'Shirin.\n'
                     "Clue 3: Hero of Alisher Navoi's second epic poem in his Khamsa, 'Farhad and Shirin'."},
  'options': {'uz': ['Majnun', 'Farhod', 'Bahrom', 'Xusrav'],
              'ru': ['Меджнун', 'Фархад', 'Бахрам', 'Хосров'],
              'en': ['Majnun', 'Farhad', 'Bahram', 'Khosrow']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Farhod', 'ru': 'Фархад', 'en': 'Farhad'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alisher_Navoiy_portrait.jpg/640px-Alisher_Navoiy_portrait.jpg',
  'fun_fact': {'uz': "Navoiy o'z asarida Farhodni Nizomiy qahramonidan farqli ravishda oddiy tosh yo'nuvchi emas, "
                     "balki ilohiy ilmlar egasi bo'lgan oliyjanob shahzoda sifatida talqin qiladi.",
               'ru': 'В отличие от Низами, Навои сделал Фархада не простым каменотесом, а благородным царевичем и '
                     'носителем высшего разума.',
               'en': "Unlike Nizami's version, Navoi elevated Farhad into a royal visionary prince devoted to selfless "
                     'labor.'},
  'aliases': ['farhod', 'фархад', 'farhad']},
 {'id': 'lit_char_015',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Armaniston hukmdori Mehinbonuning jiyani bo'lgan sohibjamol malikaman.\n"
                     "2-maslahat: Farhodning fidoiy mehnati va pok sevgisiga vafodor bo'lib, uning o'lim xabarini "
                     'eshitgach jonsiz qulayman.\n'
                     "3-maslahat: Alisher Navoiy va Nizomiy Ganjaviy dostonlarining poklik va go'zallik timsoli "
                     "bo'lgan bosh ayol qahramoniman.",
               'ru': 'Подсказка 1: Племянница царицы Армении Мехинбану, прекрасная дева с чистым сердцем.\n'
                     'Подсказка 2: Покорила сердце Фархада и пала замертво над телом любимого, узнав о его гибели.\n'
                     'Подсказка 3: Героиня романтической поэмы Алишера Навои «Фархад и Ширин».',
               'en': 'Clue 1: Armenian royal princess, niece of Queen Mehinbanu, renowned for grace and virtue.\n'
                     'Clue 2: Loved Farhad devotedly and fell dead beside him upon discovering the deceit that killed '
                     'him.\n'
                     "Clue 3: Title heroine of Alisher Navoi's and Nizami's immortal poetic epic 'Farhad and Shirin'."},
  'options': {'uz': ['Layli', 'Dilorom', 'Shirin', 'Barchinoy'],
              'ru': ['Лейли', 'Дилором', 'Ширин', 'Барчиной'],
              'en': ['Layla', 'Dilorom', 'Shirin', 'Barchinoy']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Shirin', 'ru': 'Ширин', 'en': 'Shirin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alisher_Navoiy_portrait.jpg/640px-Alisher_Navoiy_portrait.jpg',
  'fun_fact': {'uz': 'Farhod va Shirin sevgisi Sharq xalqlari adabiyotida xudbinlikdan xoli, fidoiy sadoqat ramziga '
                     'aylangan.',
               'ru': 'Образ Ширин олицетворяет в восточной поэзии верность и самоотверженность высшего порядка.',
               'en': 'Shirin remains the quintessential embodiment of poetic fidelity and devotion in Eastern '
                     'literature.'},
  'aliases': ['shirin', 'ширин']},
 {'id': 'lit_char_016',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Asl ismim Qays bo'lib, arab Omir qabilasi boshlig'ining suyukli o'g'liman.\n"
                     "2-maslahat: Maktabdalik paytimdanoq qizaloqqa oshiq bo'lib, ishq savdosida cho'llarga ketaman va "
                     "sahro hayvonlari bilan do'stlashaman.\n"
                     '3-maslahat: Odamlar meni aqldan ozgan deb ataydilar; Alisher Navoiy «Xamsa»sining uchinchi '
                     'dostonining bosh qahramoniman.',
               'ru': 'Подсказка 1: Сын вождя арабского племени амиридов, настоящее имя — Кайс.\n'
                     'Подсказка 2: С детства полюбил Лейли, от неразделенной тоски ушел в пустыню и жил среди диких '
                     'зверей.\n'
                     'Подсказка 3: Прозван «Меджнуном» (одержимым любовью), герой знаменитой поэмы Алишера Навои.',
               'en': 'Clue 1: Born Qays, noble son of an Arab chieftain of the Banu Amir clan.\n'
                     'Clue 2: Bewitched by love for Layla, I wandered naked into the blistering desert, companioned by '
                     'wild beasts.\n'
                     "Clue 3: Known as 'Majnun' ('madman with love'), protagonist of Alisher Navoi's sublime mystical "
                     'allegory.'},
  'options': {'uz': ['Farhod', 'Bahrom', 'Navfal', 'Majnun (Qays)'],
              'ru': ['Фархад', 'Бахрам', 'Навфаль', 'Меджнун (Кайс)'],
              'en': ['Farhad', 'Bahram', 'Nawfal', 'Majnun (Qays)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Majnun (Qays)', 'ru': 'Меджнун (Кайс)', 'en': 'Majnun (Qays)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alisher_Navoiy_portrait.jpg/640px-Alisher_Navoiy_portrait.jpg',
  'fun_fact': {'uz': "Tasavvufda Majnunning Layliga bo'lgan sevgisi majoziy ishqdan ilohiy (haqiqiy) ishqqa "
                     "ko'tarilish timsoli deb qaraladi.",
               'ru': 'В суфизме любовь Меджнуна к Лейли трактуется как восхождение от земной привязанности к познанию '
                     'божественной истины.',
               'en': "In Sufi philosophy, Majnun's unyielding passion symbolizes the human soul's longing to unite "
                     'with the Divine.'},
  'aliases': ['majnun', 'qays', 'меджнун', 'кайс']},
 {'id': 'lit_char_017',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Arab qabilasi boshlig'ining husnda beqiyos, tim qora sochli qiziman.\n"
                     "2-maslahat: Oila an'analari tufayli sevgilim Qaysga yetisha olmay, badavlat Ibn Salomga "
                     'majburlab uzatilsam-da, qalbimni sof saqlayman.\n'
                     '3-maslahat: Sharq adabiyotidagi eng mashhur ishqiy dostonning fojiali qahramoni va Majnunning '
                     'ilohiy sevgilisiman.',
               'ru': 'Подсказка 1: Красавица из арабского рода, чье имя означает «ночь».\n'
                     'Подсказка 2: Разлучена с Каком жестокими обычаями и выдана против воли за богатого Ибн Салама.\n'
                     'Подсказка 3: Главная героиня бессмертной поэмы Навои и Низами о великой трагической любви.',
               'en': "Clue 1: Beautiful maiden whose name signifies 'night', daughter of an Arab nobleman.\n"
                     'Clue 2: Separated from Qays by tribal law and wed against her will to Ibn Salam while remaining '
                     'true in spirit.\n'
                     "Clue 3: Heroine of the classic Eastern romance 'Layli and Majnun' in Alisher Navoi's Khamsa."},
  'options': {'uz': ['Layli', 'Shirin', 'Dilorom', 'Zulayho'],
              'ru': ['Лейли', 'Ширин', 'Дилором', 'Зулейха'],
              'en': ['Layla', 'Shirin', 'Dilorom', 'Zulaykho']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Layli', 'ru': 'Лейли', 'en': 'Layla'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alisher_Navoiy_portrait.jpg/640px-Alisher_Navoiy_portrait.jpg',
  'fun_fact': {'uz': 'Layli vafot etgach, Majnun uning qabri ustida jon beradi va oshiqlar ramzi sifatida mangu '
                     'yashaydi.',
               'ru': 'После смерти Лейли Меджнун испустил дух на ее могиле, обессмертив эту любовь в веках.',
               'en': "Upon Layla's passing, Majnun collapsed upon her grave, immortalizing their union in cultural "
                     'memory.'},
  'aliases': ['layli', 'leyba', 'лейли', 'layla']},
 {'id': 'lit_char_018',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Soz chalish va xonandalikda tengsiz iste'dodga ega bo'lgan kanizakman.\n"
                     "2-maslahat: Bahrom Go'rning ovdagi maqtanishiga noo'rin tanbeh berganim uchun sahroga tashlab "
                     'ketilaman.\n'
                     "3-maslahat: Alisher Navoiyning «Sab'ai sayyor» («Yetti sayyora») dostonining asosiy ayol "
                     'qahramoniman.',
               'ru': 'Подсказка 1: Прекрасная музыкантша и певица, виртуозно играющая на лютне (барбате).\n'
                     'Подсказка 2: За откровенные слова во время охоты была изгнана в пустыню шахом Бахрамом.\n'
                     'Подсказка 3: Главная героиня поэмы Алишера Навои «Семь планет» (Сабъаи сайёр).',
               'en': 'Clue 1: Exquisite harpist and vocalist of enchanting musical talent at the royal Persian court.\n'
                     'Clue 2: Exiled into the desolate sands by King Bahram Gur for telling him the unvarnished truth '
                     'during a hunt.\n'
                     "Clue 3: Central heroine of Alisher Navoi's philosophical romantic masterpiece 'The Seven "
                     "Planets'."},
  'options': {'uz': ['Shirin', 'Dilorom', 'Layli', 'Fitna'],
              'ru': ['Ширин', 'Дилором', 'Лейли', 'Фитна'],
              'en': ['Shirin', 'Dilorom', 'Layla', 'Fitna']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Dilorom', 'ru': 'Дилором', 'en': 'Dilorom'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alisher_Navoiy_portrait.jpg/640px-Alisher_Navoiy_portrait.jpg',
  'fun_fact': {'uz': "Navoiy Nizomiy dostonidagi Fitna ismini o'zgartirib, uni ko'ngil oromi ma'nosini anglatuvchi "
                     'Dilorom deb atagan.',
               'ru': 'Навои заменил имя героини (у Низами она звалась Фитна — «смута») на Дилором — «услада сердца».',
               'en': "Navoi renamed Nizami's character from Fitna ('strife') to Dilorom ('soother of the heart')."},
  'aliases': ['dilorom', 'дилором']},
 {'id': 'lit_char_019',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Zol va Rudobaning o'g'li bo'lib, Zobuliston pahlavoni va Eron shohlarining bosh "
                     'himoyachisiman.\n'
                     "2-maslahat: Afsonaviy Raxsh otim bor; o'z o'g'lim Suhrobni tanimay, jang maydonida halok etgan "
                     'fojiali qahramonman.\n'
                     "3-maslahat: Firdavsiyning mashhur «Shohnoma» epopeyasining eng ulug'vor alp pahlavoniman.",
               'ru': 'Подсказка 1: Богатырь из Забулистана, сын Заля и Рудабе, защитник трона шахов Ирана.\n'
                     'Подсказка 2: Владелец верного коня Рахша; в поединке смертельно ранил собственного сына Сухраба, '
                     'не узнав его.\n'
                     'Подсказка 3: Величайший эпический богатырь поэмы Фирдоуси «Шахнаме».',
               'en': 'Clue 1: Titan warrior of Zabulistan, son of Zal and Rudaba, champion defender of Persian '
                     'crowns.\n'
                     'Clue 2: Master of the fierce stallion Rakhsh; fatally struck down his own son Sohrab before '
                     'recognizing him.\n'
                     "Clue 3: The premier legendary warrior of Ferdowsi's epic monument 'Shahnameh'."},
  'options': {'uz': ['Suhrob', 'Siyovush', 'Rustam (Pahlavon Rustam)', 'Gershasp'],
              'ru': ['Сухраб', 'Сиявуш', 'Рустам (богатырь)', 'Гершасп'],
              'en': ['Sohrab', 'Siyavash', 'Rostam', 'Garshasp']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Rustam (Pahlavon Rustam)', 'ru': 'Рустам (богатырь)', 'en': 'Rostam'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Rostam_slays_the_white_div.jpg/640px-Rostam_slays_the_white_div.jpg',
  'fun_fact': {'uz': 'Rustam «Shohnoma»da 500 yildan ortiq yashab, Eronni dushmanlardan va yovuz devlardan (Oq dev) '
                     'xalos qiladi.',
               'ru': 'Рустам совершил семь подвигов («Хафт хан») и победил Белого Дива.',
               'en': "Rostam's Seven Labors ('Haft Khan') and slaying of the White Demon are legendary milestones of "
                     'epic folklore.'},
  'aliases': ['rustam', 'pahlavon rustam', 'рустам', 'rostam']},
 {'id': 'lit_char_020',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Rustam pahlavon va Samangon shohi qizi Taxminaning alp qaddi-qomatli yosh '
                     "o'g'liman.\n"
                     "2-maslahat: Otamni qidirib Turon qo'shini safida Eronga yurish qilaman, ammo hiyla tufayli otam "
                     'meni tanimaydi.\n'
                     "3-maslahat: Firdavsiy «Shohnoma»sida o'z otasi Rustam qo'lida fojiali tarzda halok bo'ladigan "
                     'pahlavon yigitman.',
               'ru': 'Подсказка 1: Юный богатырь, сын Рустама и принцессы Тахмины из Самангана.\n'
                     'Подсказка 2: Отправился в поход, чтобы найти отца и возвести его на престол, но пал жертвой '
                     'обмана шаха и туранцев.\n'
                     'Подсказка 3: Погибает от руки родного отца Рустама в одной из самых душераздирающих сцен '
                     '«Шахнаме».',
               'en': 'Clue 1: Prodigious young warrior of heroic strength, son of Rostam and princess Tahmina of '
                     'Samangan.\n'
                     'Clue 2: Marched into Persia hoping to unite with his father and crown him king.\n'
                     'Clue 3: Fatally stabbed in single combat by his own father in the most celebrated tragedy of '
                     "Ferdowsi's 'Shahnameh'."},
  'options': {'uz': ['Rustam', 'Siyovush', 'Isfandiyor', 'Suhrob'],
              'ru': ['Рустам', 'Сиявуш', 'Исфандияр', 'Сухраб'],
              'en': ['Rostam', 'Siyavash', 'Esfandiyar', 'Sohrab']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Suhrob', 'ru': 'Сухраб', 'en': 'Sohrab'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Rostam_slays_the_white_div.jpg/640px-Rostam_slays_the_white_div.jpg',
  'fun_fact': {'uz': "Suhrob o'lim to'shagida bilagidagi Rustam bergan tumor-nishonni ko'rsatgandagina ota o'z "
                     "o'g'lini tanib, faryod chekadi.",
               'ru': 'Лишь умирающий Сухраб открыл Рустаму браслет-оберег, подаренный отцом много лет назад Тахмине.',
               'en': 'Only as he lay dying did Sohrab reveal the jewel amulet given by Rostam years earlier to '
                     'identify his son.'},
  'aliases': ['suhrob', 'сухраб', 'sohrab']},
 {'id': 'lit_char_021',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Daniya shahzodasiman, otamning sharpasi menga amakim Klavdiy uni zaharlab '
                     "o'ldirganini aytadi.\n"
                     "2-maslahat: Haqiqatni bilish uchun o'zimni jinnilikka solaman va aktyorlar orqali «Qopqon» "
                     'sahnasini uyushtiraman.\n'
                     "3-maslahat: «Bo'lmoq yo bo'lmaslik — mana masala» falsafiy monologi bilan mashhur bo'lgan "
                     'Shekspir fojiasi bosh qahramoniman.',
               'ru': 'Подсказка 1: Принц датский, узнавший от призрака отца, что тот был подло отравлен братом '
                     'Клавдием.\n'
                     'Подсказка 2: Притворяется безумцем, чтобы разоблачить дядю-узурпатора с помощью театральной '
                     'постановки «Мышеловка».\n'
                     'Подсказка 3: Автор бессмертного монолога «Быть или не быть» в одноименной трагедии Уильяма '
                     'Шекспира.',
               'en': "Clue 1: Prince of Denmark who learns from his father's ghost that his uncle Claudius committed "
                     'regicide.\n'
                     "Clue 2: Feigned madness and staged the play-within-a-play 'The Mousetrap' to test the king's "
                     'guilty conscience.\n'
                     "Clue 3: Ponders 'To be, or not to be' in William Shakespeare's immortal revenge tragedy."},
  'options': {'uz': ['Hamlet', 'Otello', 'Makbet', 'Qirol Lir'],
              'ru': ['Гамлет', 'Отелло', 'Макбет', 'Король Лир'],
              'en': ['Prince Hamlet', 'Othello', 'Macbeth', 'King Lear']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Hamlet', 'ru': 'Гамлет', 'en': 'Prince Hamlet'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Shakespeare_Hamlet_Act_5_Scene_1_Delacroix.jpg/640px-Shakespeare_Hamlet_Act_5_Scene_1_Delacroix.jpg',
  'fun_fact': {'uz': 'Shekspirning «Hamlet» pyesasi qabriston sahnasida qiziqchi Yorikning bosh suyagini ushlab '
                     'aytilgan monolog bilan butun dunyoga tanilgan.',
               'ru': 'Сцена с черепом шута Йорика на кладбище стала одним из самых узнаваемых визуальных символов '
                     'мировой культуры.',
               'en': 'Holding the skull of Yorick the jester remains one of the iconic visual metaphors in world '
                     'theater.'},
  'aliases': ['hamlet', 'гамлет', 'shahzoda hamlet']},
 {'id': 'lit_char_022',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Veronadagi Montekki xonadonining yosh va his-tuyg'ularga boy vakiliman.\n"
                     "2-maslahat: Oilamizning ashaddiy dushmani bo'lgan Kapuletti xonadoni balida nozik bir qizni "
                     "ko'rib oshiq bo'laman.\n"
                     "3-maslahat: Sevgilimning uxlatuvchi doridan vafot etgan deb o'ylab, uning qabri oldida zahar "
                     "ichib o'lgan fojia qahramoniman.",
               'ru': 'Подсказка 1: Юный наследник знатного веронского рода Монтекки.\n'
                     'Подсказка 2: На балу во враждебном доме Капулетти встречает Джульетту и без памяти влюбляется в '
                     'неё.\n'
                     'Подсказка 3: По ошибке сочтя возлюбленную мертвой, выпивает яд в её фамильном склепе в трагедии '
                     'Шекспира.',
               'en': "Clue 1: Passionate young scion of Verona's noble House of Montague.\n"
                     'Clue 2: Crashed a masquerade ball at the rival House of Capulet and instantly lost his heart.\n'
                     "Clue 3: Drank poison in the family tomb believing his bride dead in Shakespeare's quintessential "
                     'romantic tragedy.'},
  'options': {'uz': ['Tibald', 'Romeo Montekki', 'Merkutsio', 'Benvolio'],
              'ru': ['Тибальт', 'Ромео Монтекки', 'Меркуцио', 'Бенволио'],
              'en': ['Tybalt', 'Romeo Montague', 'Mercutio', 'Benvolio']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Romeo Montekki', 'ru': 'Ромео Монтекки', 'en': 'Romeo Montague'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Romeo_and_juliet_brown.jpg/640px-Romeo_and_juliet_brown.jpg',
  'fun_fact': {'uz': 'Shekspir «Romeo va Juletta» asarini yaratishda qadimiy italyan afsonalari va Artur Bruk '
                     'poemasidan ilhomlangan.',
               'ru': 'Шекспир создал пьесу в 1590-х годах, сделав имена Ромео и Джульетты синонимами чистой '
                     'трагической любви.',
               'en': "Written in the 1590s, Romeo and Juliet became literature's universal archetypes of star-crossed "
                     'lovers.'},
  'aliases': ['romeo', 'romeo montekki', 'ромео', 'ромео монтекки']},
 {'id': 'lit_char_023',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Verona shahridagi boy Kapuletti oilasining 14 yoshga to'lmagan yagona qiziman.\n"
                     "2-maslahat: Balkonda turib dushman urug'iga mansub oshig'im bilan mangu sevgi ahdini "
                     "bog'layman.\n"
                     "3-maslahat: Xanjarni yuragimga urib o'z jonimga qasd qilgan, Shekspirning eng mashhur sevgi "
                     'fojiasi qahramoniman.',
               'ru': 'Подсказка 1: Единственная юная дочь синьора Капулетти из Вероны.\n'
                     'Подсказка 2: Обручилась на балконе с Ромео, представителем враждующего клана Монтекки.\n'
                     'Подсказка 3: Очнувшись в склепе и увидев мертвого мужа, заколола себя его кинжалом в трагедии '
                     'Шекспира.',
               'en': 'Clue 1: Adolescent daughter and heir of Lord Capulet in renaissance Verona.\n'
                     'Clue 2: Shared an impassioned exchange with her beloved from her moonlit garden balcony.\n'
                     'Clue 3: Awoke to find her young husband lifeless and pierced her heart with his dagger.'},
  'options': {'uz': ['Ofeliya', 'Dezdemona', 'Juletta Kapuletti', 'Kordeliya'],
              'ru': ['Офелия', 'Дездемона', 'Джульетта Капулетти', 'Корделия'],
              'en': ['Ophelia', 'Desdemona', 'Juliet Capulet', 'Cordelia']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Juletta Kapuletti', 'ru': 'Джульетта Капулетти', 'en': 'Juliet Capulet'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Romeo_and_juliet_brown.jpg/640px-Romeo_and_juliet_brown.jpg',
  'fun_fact': {'uz': 'Verona shahrida har yili Juletta uyiga dunyoning turli chekkalaridan minglab oshiqlar xat yozib '
                     'qoldiradilar.',
               'ru': '«Дом Джульетты» в Вероне с его знаменитым балконом ежегодно посещают сотни тысяч туристов со '
                     'всего мира.',
               'en': 'Thousands of letters addressed to Juliet arrive annually in Verona, answered by the volunteer '
                     "'Juliet Club'."},
  'aliases': ['juletta', 'juletta kapuletti', 'джульетта', 'juliet']},
 {'id': 'lit_char_024',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Venetsiya respublikasi armiyasiga boshchilik qiluvchi kelib chiqishi mavr bo'lgan "
                     'jasur sarkardaman.\n'
                     '2-maslahat: Venetsiyalik aslzoda qiz Dezdemonaga uylanaman, ammo xiyonatkor safdoshim Yagoning '
                     'fitnasiga aldanaman.\n'
                     "3-maslahat: Soxta rashk o'tida begunoh xotinimni bo'g'ib o'ldirib, so'ng o'z jonimga qasd qilgan "
                     'Shekspir fojiasi bosh qahramoniman.',
               'ru': 'Подсказка 1: Благородный полководец-мавр на службе Венецианской республики.\n'
                     'Подсказка 2: Тайно венчается с прекрасной Дездемоной, но становится жертвой коварных интриг '
                     'коварного поручика Яго.\n'
                     'Подсказка 3: Ослепленный яростной ревностью из-за потерянного платка, душит жену в финале '
                     'трагедии Шекспира.',
               'en': 'Clue 1: Renowned Moorish general commanding the mercenary armed forces of Renaissance Venice.\n'
                     'Clue 2: Wed noble Desdemona, yet fell victim to the venomous machinations of his ensign Iago.\n'
                     'Clue 3: Smothered his innocent bride in their nuptial bed in a fit of manufactured jealousy.'},
  'options': {'uz': ['Yago', 'Kassio', 'Rodorigo', 'Otello'],
              'ru': ['Яго', 'Кассио', 'Родриго', 'Отелло'],
              'en': ['Iago', 'Cassio', 'Roderigo', 'Othello']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Otello', 'ru': 'Отелло', 'en': 'Othello'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Othello_and_Desdemona.jpg/640px-Othello_and_Desdemona.jpg',
  'fun_fact': {'uz': "Shekspir Otelloni fojiali qahramon qilib, rashk hissiyotining naqadar halokatli va ko'r bo'lishi "
                     "mumkinligini ko'rsatgan.",
               'ru': 'Сюжет основан на новелле Джамбаттисты Джиральди Чинцио из сборника «Экатомитти» (1565).',
               'en': "The missing embroidered handkerchief with strawberries became literature's most devastating "
                     'misplaced prop.'},
  'aliases': ['otello', 'отелло', 'othello']},
 {'id': 'lit_char_025',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Sarkardam kassir Kassioni leytenantlikka ko'targani uchun undan va Otellodan qattiq "
                     'nafratlanaman.\n'
                     "2-maslahat: Yuzimda samimiy do'stlik niqobini kiyib, makkorona rejalarim bilan atrofdagilarni "
                     'bir-biriga gij-gijlayman.\n'
                     "3-maslahat: Yo'qolgan ro'molcha orqali rashk olovini yoqib fojia keltirib chiqargan Shekspir "
                     'asaridagi eng buyuk yovuz (antagonist) qahramonman.',
               'ru': 'Подсказка 1: Офицер на службе Венеции, обойденный повышением по службе в пользу Кассио.\n'
                     'Подсказка 2: Лицемерный интриган («честный Яго»), плетущий паутину козней за спиной у своего '
                     'командира.\n'
                     'Подсказка 3: Величайший злодей в творчестве Шекспира, погубивший Отелло и Дездемону.',
               'en': 'Clue 1: Venetian ensign passed over for promotion in favor of young Michael Cassio.\n'
                     'Clue 2: Master puppeteer hiding beneath an exterior of blunt honesty, manipulating everyone '
                     'around him.\n'
                     "Clue 3: Shakespeare's ultimate Machiavellian antagonist whose poison destroyed Othello and "
                     'Desdemona.'},
  'options': {'uz': ['Yago', 'Otello', 'Klavdiy', 'Tibald'],
              'ru': ['Яго', 'Отелло', 'Клавдий', 'Тибальт'],
              'en': ['Iago', 'Othello', 'Claudius', 'Tybalt']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Yago', 'ru': 'Яго', 'en': 'Iago'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Othello_and_Desdemona.jpg/640px-Othello_and_Desdemona.jpg',
  'fun_fact': {'uz': 'Yago adabiyotshunoslikda sababsiz yovuzlik («motiveless malignancy») tushunchasining yorqin '
                     'timsoli hisoblanadi.',
               'ru': 'Критик Кольридж назвал поведение Яго классическим примером «беспричинного злодейства».',
               'en': "Critic Samuel Taylor Coleridge famously termed Iago's destructive malice 'motiveless "
                     "malignancy'."},
  'aliases': ['yago', 'iago', 'яго']},
 {'id': 'lit_char_026',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: La-Manchalik kambag'al dvoryanman, ritsarlik romanlarini ko'p o'qib aqldan ozaman.\n"
                     '2-maslahat: Rosinant otimga minib, shamol tegirmonlarini maxluq deb hisoblab jangga kirishaman.\n'
                     '3-maslahat: Servantesning dunyo adabiyoti durdonasi hisoblangan romanining xomxayol, olijanob '
                     'ritsari bosh qahramoniman.',
               'ru': 'Подсказка 1: Обедневший идальго из Ла-Манчи, потерявший рассудок от чтения рыцарских романов.\n'
                     'Подсказка 2: На тощей кляче Росинанте отправляется совершать подвиги, принимая ветряные мельницы '
                     'за великанов.\n'
                     'Подсказка 3: «Рыцарь печального образа», главный герой бессмертного шедевра Мигеля де '
                     'Сервантеса.',
               'en': 'Clue 1: Impoverished hidalgo from La Mancha who lost his wits devouring chivalric romances.\n'
                     'Clue 2: Mounted his scrawny steed Rocinante and charged giant windmills mistaking them for '
                     'monstrous fiends.\n'
                     "Clue 3: 'The Knight of the Sorrowful Countenance', immortal protagonist of Miguel de Cervantes."},
  'options': {'uz': ['Sancho Pansa', 'Don Kixot', "D'Artanyan", 'Gulliver'],
              'ru': ['Санчо Панса', 'Дон Кихот', "Д'Артаньян", 'Гулливер'],
              'en': ['Sancho Panza', 'Don Quixote', "D'Artagnan", 'Gulliver']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Don Kixot', 'ru': 'Дон Кихот', 'en': 'Don Quixote'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Don_Quixote_and_Sancho_Panza.jpg/640px-Don_Quixote_and_Sancho_Panza.jpg',
  'fun_fact': {'uz': "Don Kixot romani barcha davrlarning eng ko'p tarjima qilingan va chop etilgan badiiy asarlaridan "
                     'biridir.',
               'ru': 'Роман Сервантеса признан Норвежским книжным клубом величайшим литературным произведением в '
                     'истории человечества.',
               'en': 'Voted the greatest literary work in human history by a worldwide panel of 100 distinguished '
                     'authors in 2002.'},
  'aliases': ['don kixot', 'don quixote', 'дон кихот']},
 {'id': 'lit_char_027',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Oddiy, yerga yaqin, maqol-matallarni yaxshi biladigan va ovqatlanishni sevadigan '
                     'dehqonman.\n'
                     "2-maslahat: Bo'lajak orol gubernatori bo'lish va'dasiga ishonib, eshagimga minib ritsarning "
                     "qurolbardori bo'lib yo'lga chiqaman.\n"
                     "3-maslahat: Don Kixotning sodiq hamrohi va doimiy aql o'rgatuvchi sherigiman.",
               'ru': 'Подсказка 1: Практичный крестьянин, любящий сытно поесть и сыплющий народными пословицами.\n'
                     'Подсказка 2: Соблазнился обещанием получить в управление остров и отправился в путь на своем '
                     'ослике оруженосцем.\n'
                     'Подсказка 3: Верный оруженосец и земной противовес Дон Кихота в романе Сервантеса.',
               'en': 'Clue 1: Earthy, proverb-quoting peasant who loves hearty meals and peaceful sleep.\n'
                     "Clue 2: Lured by the promise of governing an insular realm ('insula'), mounted his donkey to "
                     'serve as squire.\n'
                     "Clue 3: Faithful, pragmatic companion balancing Don Quixote's wild fantasies in Cervantes' "
                     'classic.'},
  'options': {'uz': ['Don Kixot', 'Doktor Vatson', 'Sancho Pansa', 'Paserpartu'],
              'ru': ['Дон Кихот', 'Доктор Ватсон', 'Санчо Панса', 'Паспарту'],
              'en': ['Don Quixote', 'Dr. Watson', 'Sancho Panza', 'Passepartout']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Sancho Pansa', 'ru': 'Санчо Панса', 'en': 'Sancho Panza'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Don_Quixote_and_Sancho_Panza.jpg/640px-Don_Quixote_and_Sancho_Panza.jpg',
  'fun_fact': {'uz': "Sancho Pansa Don Kixotning orzu-xayollariga qarama-qarshi bo'lgan amaliy xalq donoligini o'zida "
                     'mujassam etadi.',
               'ru': 'Санчо Панса олицетворяет народный здравый смысл, добродушие и фольклорную мудрость Испании.',
               'en': 'Sancho Panza represents common sense and folklore realism counterpoised against Quixotic '
                     'idealism.'},
  'aliases': ['sancho pansa', 'sancho panza', 'санчо панса']},
 {'id': 'lit_char_028',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Londonning Beyker-strit 221B manzilida yashovchi shaxsiy maslahatchi izquvarman.\n'
                     '2-maslahat: Deduksiya usuli, skripka chalish va tamaki trubkasini tutatish orqali eng chigal '
                     'jinoyatlarni fosh qilaman.\n'
                     '3-maslahat: Artur Konan Doyl qalamiga mansub dunyoning eng mashhur detektividirman.',
               'ru': 'Подсказка 1: Частный сыщик-консультант, живущий в Лондоне по адресу Бейкер-стрит, 221B.\n'
                     'Подсказка 2: Раскрывает самые загадочные преступления благодаря дедуктивному методу, играет на '
                     'скрипке и курит трубку.\n'
                     'Подсказка 3: Легендарный персонаж детективных повестей и рассказов Артура Конан Дойла.',
               'en': 'Clue 1: Consulting detective residing at 221B Baker Street in Victorian London.\n'
                     'Clue 2: Uses keen forensic deduction, plays the violin, and smokes a briar pipe while cracking '
                     'unsolvable puzzles.\n'
                     "Clue 3: Arthur Conan Doyle's globally celebrated detective, the most portrayed literary human in "
                     'screen history.'},
  'options': {'uz': ['Doktor Jon Vatson', 'Erkul Puaro', 'Komissar Megre', 'Sherlok Xolms'],
              'ru': ['Доктор Джон Ватсон', 'Эркюль Пуаро', 'Комиссар Мегрэ', 'Шерлок Холмс'],
              'en': ['Dr. John Watson', 'Hercule Poirot', 'Inspector Maigret', 'Sherlock Holmes']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Sherlok Xolms', 'ru': 'Шерлок Холмс', 'en': 'Sherlock Holmes'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Sherlock_Holmes_Portrait_Paget.jpg/640px-Sherlock_Holmes_Portrait_Paget.jpg',
  'fun_fact': {'uz': "Ginnesning rekordlar kitobiga ko'ra Sherlok Xolms kinoda eng ko'p gavdalantirilgan (250 dan "
                     'ortiq filmda) adabiy qahramondir.',
               'ru': 'Шерлок Холмс внесен в Книгу рекордов Гиннесса как самый экранизируемый литературный '
                     'персонаж-человек.',
               'en': 'Listed in Guinness World Records as the most portrayed human literary character in cinema '
                     'history.'},
  'aliases': ['sherlok xolms', 'sherlock holmes', 'шерлок холмс']},
 {'id': 'lit_char_029',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Afg'onistondagi urushda yaralanib Londoniga qaytgan harbiy vrachman.\n"
                     "2-maslahat: Beyker-stritda xonadon ijaraga olib, daho izquvarning do'sti, yordamchisi va "
                     'solnomachisiga aylanaman.\n'
                     '3-maslahat: Artur Konan Doylning Sherlok Xolms haqidagi hikoyalarining deyarli barchasini '
                     "so'zlab beruvchi hikoyachiman.",
               'ru': 'Подсказка 1: Военный врач в отставке, раненый в Афганистане и вернувшийся в Лондон.\n'
                     'Подсказка 2: Снял квартиру на Бейкер-стрит с гениальным сыщиком и стал его верным другом, '
                     'биографом и помощником.\n'
                     'Подсказка 3: Рассказчик почти всех историй о Шерлоке Холмсе, созданный Артуром Конан Дойлом.',
               'en': 'Clue 1: Former British Army surgeon invalided home after suffering a wound in the Second '
                     'Anglo-Afghan War.\n'
                     'Clue 2: Lodged at 221B Baker Street and became chronicler, companion, and confidant to an '
                     'eccentric detective.\n'
                     "Clue 3: Arthur Conan Doyle's beloved narrator of almost all Sherlock Holmes mysteries."},
  'options': {'uz': ['Doktor Jon Vatson', 'Sherlok Xolms', 'Inspektor Lestreyd', 'Maykroft Xolms'],
              'ru': ['Доктор Джон Ватсон', 'Шерлок Холмс', 'Инспектор Лестрейд', 'Майкрофт Холмс'],
              'en': ['Dr. John Watson', 'Sherlock Holmes', 'Inspector Lestrade', 'Mycroft Holmes']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Doktor Jon Vatson', 'ru': 'Доктор Джон Ватсон', 'en': 'Dr. John Watson'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Sherlock_Holmes_Portrait_Paget.jpg/640px-Sherlock_Holmes_Portrait_Paget.jpg',
  'fun_fact': {'uz': "Konan Doyl Doktor Vatson obrazini o'zining tibbiy bilimlaridan va hamkasbi vrachlardan "
                     'ilhomlanib yaratgan.',
               'ru': 'Доктор Ватсон является воплощением верности, здравого смысла и викторианской порядочности.',
               'en': 'Watson represents the voice of Victorian honor, medical rationality, and steadfast loyalty.'},
  'aliases': ['doktor vatson', 'vatson', 'jon vatson', 'доктор ватсон', 'ватсон', 'dr watson']},
 {'id': 'lit_char_030',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Bir paytlar nufuzli universitetda matematika kafedrasi professori bo'lgan daho "
                     'olimman.\n'
                     '2-maslahat: «Jinoyat olamining Napoleoni» deb atalib, soyada turib butun Yevropa jinoiy '
                     "to'rlarini boshqaraman.\n"
                     '3-maslahat: Reyxenbax sharsharasida Sherlok Xolms bilan yakkama-yakka olishib jarlikka qulagan '
                     'bosh dushmanman.',
               'ru': 'Подсказка 1: Бывший блестящий профессор математики, автор революционного трактата о биноме '
                     'Ньютона.\n'
                     'Подсказка 2: Организатор преступного синдиката, названный Холмсом «Наполеоном преступного '
                     'мира».\n'
                     'Подсказка 3: Заклятый враг Шерлока Холмса, сорвавшийся вместе с ним в бездну Рейхенбахского '
                     'водопада.',
               'en': 'Clue 1: Former prodigy and professor of mathematics who authored a treatise on the binomial '
                     'theorem.\n'
                     "Clue 2: Dubbed by Holmes as 'the Napoleon of crime', sitting motionless at the hub of European "
                     'vice.\n'
                     'Clue 3: Arch-nemesis of Sherlock Holmes who grappled with him atop the Reichenbach Falls.'},
  'options': {'uz': ['Polkovnik Moran', 'Professor Jeyms Moriarti', 'Doktor Grimesbi Roylott', 'Iren Adler'],
              'ru': ['Полковник Моран', 'Профессор Джеймс Мориарти', 'Доктор Ройлотт', 'Ирен Адлер'],
              'en': ['Colonel Moran', 'Professor James Moriarty', 'Dr. Roylott', 'Irene Adler']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Professor Jeyms Moriarti',
                     'ru': 'Профессор Джеймс Мориарти',
                     'en': 'Professor James Moriarty'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Sherlock_Holmes_Portrait_Paget.jpg/640px-Sherlock_Holmes_Portrait_Paget.jpg',
  'fun_fact': {'uz': "Konan Doyl Moriartini faqatgina Sherlok Xolmsni o'ldirish va silsilani tugatish uchungina o'ylab "
                     'topgan edi.',
               'ru': 'Конан Дойл придумал Мориарти исключительно для того, чтобы «убить» Холмса и освободиться от '
                     'персонажа.',
               'en': 'Doyle invented Moriarty strictly as an intellectual peer capable of killing off Sherlock '
                     'Holmes.'},
  'aliases': ['professor moriarti', 'moriarti', 'профессор мориарти', 'мориарти', 'professor moriarty']},
 {'id': 'lit_char_031',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: «Pekod» nomli kit ovlash kemasining bir oyog'i kashalot suyagidan yasalgan qahrli "
                     'kapitaniman.\n'
                     "2-maslahat: Bir paytlar oyog'imni uzib olgan ulkan oq kashalotni (kitni) topib, undan qasos "
                     'olish vasvasasida yonaman.\n'
                     "3-maslahat: Herman Melvillning jahon adabiyoti durdonasi bo'lgan «Mobi Dik» romanining fojiali "
                     'bosh qahramoniman.',
               'ru': 'Подсказка 1: Угрюмый и фанатичный капитан китобойного судна «Пекод» с протезом из челюсти '
                     'кашалота.\n'
                     'Подсказка 2: Одержим слепой жаждой мести белому киту-убийце, лишившему его ноги в прошлом '
                     'плавании.\n'
                     'Подсказка 3: Трагический главный герой великого морского романа Германа Мелвилла «Моби Дик».',
               'en': 'Clue 1: Monomaniacal captain of the whaling ship Pequod, pacing the quarterdeck on an ivory '
                     'peg-leg.\n'
                     'Clue 2: Consumed by a blasphemous vendetta against the terrifying albino sperm whale that maimed '
                     'him.\n'
                     "Clue 3: Protagonist of Herman Melville's 1851 American epic 'Moby-Dick'."},
  'options': {'uz': ['Ismoil', 'Kvikveg', 'Kapitan Axav', 'Kapitan Nemo'],
              'ru': ['Измаил', 'Квикег', 'Капитан Ахав', 'Капитан Немо'],
              'en': ['Ishmael', 'Queequeg', 'Captain Ahab', 'Captain Nemo']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Kapitan Axav', 'ru': 'Капитан Ахав', 'en': 'Captain Ahab'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/A_white_whale_leaps_from_the_sea_into_a_crowded_whaleboat.jpg/640px-A_white_whale_leaps_from_the_sea_into_a_crowded_whaleboat.jpg',
  'fun_fact': {'uz': "Kapitan Axav obrazi insonning tabiat kuchlari va o'z ichki jinlari bilan halokatli kurashining "
                     'timsolidir.',
               'ru': 'Капитан Ахав стал вечным символом разрушительной одержимости и бунта человека против рока и '
                     'природы.',
               'en': 'Captain Ahab is celebrated in world literature as the ultimate literary portrait of fatal '
                     'obsession.'},
  'aliases': ['kapitan axav', 'axav', 'капитан ахав', 'ахав', 'captain ahab']},
 {'id': 'lit_char_032',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Fransiyalik yosh dengizchi bo'lib, to'yim kuni tuhmat bilan dahshatli If qal'asi "
                     'zindoniga tashlanaman.\n'
                     "2-maslahat: Zindonda abbat Fariadan ta'lim olib, oroldagi beqiyos xazinani qo'lga kiritaman va "
                     'qasos olishga kirishaman.\n'
                     '3-maslahat: Aleksandr Dyumaning eng mashhur sarguzasht romanidagi Graf Monte-Kristo nomini olgan '
                     'bosh qahramonman.',
               'ru': 'Подсказка 1: Молодой марсельский моряк, несправедливо заключенный в замок Иф в день своей '
                     'помолвки.\n'
                     'Подсказка 2: Сбегает из крепости после 14 лет заточения, находит несметные сокровища аббата '
                     'Фариа и возвращается карателем.\n'
                     'Подсказка 3: Главный герой приключенческого романа Александра Дюма «Граф Монте-Кристо».',
               'en': 'Clue 1: Young Marseilles sailor falsely denounced for treason on his betrothal day and thrown '
                     "into the Château d'If.\n"
                     'Clue 2: Tutored by Abbé Faria during 14 years of imprisonment before staging an audacious escape '
                     'to recover an island treasure.\n'
                     "Clue 3: Alexandre Dumas' aristocratic avenger known as the Count of Monte Cristo."},
  'options': {'uz': ["D'Artanyan", 'Jan Valjan', 'Fernan Mondego', 'Edmon Dantes (Graf Monte-Kristo)'],
              'ru': ["Д'Артаньян", 'Жан Вальжан', 'Фернан Мондего', 'Эдмон Дантес (Граф Монте-Кристо)'],
              'en': ["D'Artagnan", 'Jean Valjean', 'Fernand Mondego', 'Edmond Dantès (Count of Monte Cristo)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Edmon Dantes (Graf Monte-Kristo)',
                     'ru': 'Эдмон Дантес (Граф Монте-Кристо)',
                     'en': 'Edmond Dantès (Count of Monte Cristo)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Alexandre_Dumas_by_Nadar%2C_1855.jpg/640px-Alexandre_Dumas_by_Nadar%2C_1855.jpg',
  'fun_fact': {'uz': 'Edmon Dantes sarguzashtlari orqali Dyuma qasos va adolat, inson sabr-toqati va kechirim '
                     'mavzularini chuqur ochib bergan.',
               'ru': 'Роман Дюма был основан на реальной криминальной истории парижского сапожника Франсуа Пико.',
               'en': "Dumas based Dantès' vendetta on the police archives account of shoemaker François Picaud."},
  'aliases': ['edmon dantes',
              'graf monte-kristo',
              'monte kristo',
              'эдмон дантес',
              'граф монте-кристо',
              'edmond dantes']},
 {'id': 'lit_char_033',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Gaskoniyalik yosh, kambag'al dvoryan bo'lib, eski sariq otimda Parijga mushketyor "
                     "bo'lish uchun kelaman.\n"
                     '2-maslahat: Dastlabki kunda uch nafar mushketyor bilan duelga kelishib, keyin ularning ajralmas '
                     "do'stiga aylanaman.\n"
                     '3-maslahat: «Barchamiz birimiz uchun, birimiz barchamiz uchun» shiori ostida qirolicha sharafini '
                     'himoya qiluvchi Dyuma romani qahramoniman.',
               'ru': 'Подсказка 1: Бедный юный дворянин из Гаскони, приехавший в Париж на желтой кляче поступать в '
                     'королевские мушкетеры.\n'
                     'Подсказка 2: В первый же день вызвал на дуэль троих мушкетеров, которые стали его верными '
                     'товарищами.\n'
                     'Подсказка 3: Главный герой трилогии Александра Дюма «Три мушкетера».',
               'en': 'Clue 1: Impoverished young Gascon gentleman riding into Paris on a yellow nag to seek royal '
                     'glory.\n'
                     'Clue 2: Challenged three musketeers to duels within three hours, forging a lifelong '
                     'brotherhood.\n'
                     "Clue 3: Daring protagonist of Alexandre Dumas' swashbuckling classic 'The Three Musketeers'."},
  'options': {'uz': ["D'Artanyan", 'Atos', 'Portos', 'Aramis'],
              'ru': ["Д'Артаньян", 'Атос', 'Портос', 'Арамис'],
              'en': ["D'Artagnan", 'Athos', 'Porthos', 'Aramis']},
  'correct_index': 0,
  'correct_answer': {'uz': "D'Artanyan", 'ru': "Д'Артаньян", 'en': "D'Artagnan"},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Alexandre_Dumas_by_Nadar%2C_1855.jpg/640px-Alexandre_Dumas_by_Nadar%2C_1855.jpg',
  'fun_fact': {'uz': "D'Artanyan prototipi tarixiy shaxs — Qirol Lyudovik XIV ning gvardiya kapitani Sharl de Batz de "
                     "Kastelmor bo'lgan.",
               'ru': "Прототипом д'Артаньяна был реальный капитан-лейтенант королевских мушкетеров Шарль де Бац де "
                     'Кастельмор.',
               'en': "D'Artagnan was modeled on the historical captain of Louis XIV's musketeers, Charles de "
                     'Batz-Castelmore.'},
  'aliases': ["d'artanyan", 'dartanyan', "д'артаньян", 'дартаньян', "d'artagnan"]},
 {'id': 'lit_char_034',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Och qolgan singlimning bolalari uchun bir burda non o'g'irlab, 19 yil katorgada azob "
                     'chekkan mahbusman (24601-raqamli).\n'
                     "2-maslahat: Yepiskop Mirielning kechirimliligi qalbimni o'zgartiradi va badavlat janob Madlen "
                     'qiyofasida saxiy odamga aylanaman.\n'
                     "3-maslahat: Inspektor Javertning ta'qibidan qochib, yetim qiz Kozettani tarbiyalagan Viktor "
                     "Gyugoning «Xo'rlanganlar» romani qahramoniman.",
               'ru': 'Подсказка 1: Бывший каторжник № 24601, отсидевший 19 лет на галерах за кражу буханки хлеба для '
                     'голодной семьи сестры.\n'
                     'Подсказка 2: Преобразился под влиянием доброты епископа Мириэля и стал благодетелем под именем '
                     'мсье Мадлен.\n'
                     'Подсказка 3: Главный герой грандиозного романа Виктора Гюго «Отверженные».',
               'en': 'Clue 1: Convict number 24601 who served 19 years of hard labor for stealing a loaf of bread for '
                     "his sister's starving family.\n"
                     "Clue 2: Transformed by Bishop Myriel's mercy, reinventing himself as the benevolent factory "
                     'mayor Monsieur Madeleine.\n'
                     "Clue 3: Noble fugitive hero raising orphan Cosette in Victor Hugo's epic masterpiece 'Les "
                     "Misérables'."},
  'options': {'uz': ['Javer', 'Jan Valjan', 'Marius Ponmersi', 'Tenardye'],
              'ru': ['Жавер', 'Жан Вальжан', 'Мариус', 'Тенардье'],
              'en': ['Javert', 'Jean Valjean', 'Marius', 'Thénardier']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Jan Valjan', 'ru': 'Жан Вальжан', 'en': 'Jean Valjean'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Jean_Valjean_Cosette_Bayard.jpg/640px-Jean_Valjean_Cosette_Bayard.jpg',
  'fun_fact': {'uz': "Jan Valjanning Kozettani asrab olishi va qutqarishi insoniylik, mehr-oqibat va ma'naviy "
                     'najotning buyuk timsoliga aylangan.',
               'ru': '«Отверженные» разошлись тиражом, потрясшим Европу XIX века, а образ Вальжана стал символом '
                     'милосердия.',
               'en': "Valjean's moral redemption is celebrated as one of the most powerful arcs in 19th-century world "
                     'literature.'},
  'aliases': ['jan valjan', 'jean valjean', 'жан вальжан']},
 {'id': 'lit_char_035',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Zindonda tug'ilib o'sganman, qonunga ko'r-ko'rona itoat etishni hayotimning yagona "
                     'mazmuni deb bilaman.\n'
                     "2-maslahat: Sobiq katorgachi Jan Valjanni ko'p yillar davomida soyadek tinimsiz ta'qib qilib "
                     'yurgan politsiya inspektoriman.\n'
                     "3-maslahat: Dushmanim meni o'limdan qutqargach, vijdoni va qonun talabi o'rtasidagi ziddiyatga "
                     "chiday olmay Sena daryosiga o'zini tashlaganman.",
               'ru': 'Подсказка 1: Неподкупный и безжалостный полицейский инспектор, считающий закон абсолютным высшим '
                     'божеством.\n'
                     'Подсказка 2: Годами преследовал бывшего каторжника Жана Вальжана, не веря в возможность '
                     'нравственного исправления.\n'
                     'Подсказка 3: Потерпев крушение своих принципов, бросается в Сену в романе Виктора Гюго '
                     '«Отверженные».',
               'en': 'Clue 1: Inflexible police inspector born inside a prison, devoted blindly to rigid statutory '
                     'law.\n'
                     'Clue 2: Relentlessly hunted former felon Jean Valjean for decades, unable to accept that a '
                     'criminal can redeem himself.\n'
                     "Clue 3: Flung himself into the River Seine when Valjean spared his life in Victor Hugo's 'Les "
                     "Misérables'."},
  'options': {'uz': ['Jan Valjan', 'Tenardye', 'Inspektor Javer', 'Enjolras'],
              'ru': ['Жан Вальжан', 'Тенардье', 'Инспектор Жавер', 'Анжольрас'],
              'en': ['Jean Valjean', 'Thénardier', 'Inspector Javert', 'Enjolras']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Inspektor Javer', 'ru': 'Инспектор Жавер', 'en': 'Inspector Javert'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Jean_Valjean_Cosette_Bayard.jpg/640px-Jean_Valjean_Cosette_Bayard.jpg',
  'fun_fact': {'uz': 'Javer timsoli qotib qolgan dogma va rahm-shafqatsiz qonunparastlikning fojiasini ifodalaydi.',
               'ru': 'Трагедия Жавера — в столкновении сухого параграфа закона с высшим христианским милосердием.',
               'en': 'Javert illustrates the psychological rupture when unbending legal absolutism collides with '
                     'divine grace.'},
  'aliases': ['javer', 'inspektor javer', 'жавер', 'инспектор жавер', 'javert']},
 {'id': 'lit_char_036',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Bir ko'zi ko'r, bukri va quloqlari cherkov qo'ng'iroqlari sadosidan kar bo'lib "
                     'qolgan zangori odamman.\n'
                     "2-maslahat: Parij Bibi Maryam ibodatxonasida qo'ng'iroqchi bo'lib yashayman va lo'li qiz "
                     "Esmeraldaga fidokorona oshiq bo'laman.\n"
                     "3-maslahat: Viktor Gyugoning eng mashhur tarixiy romanidagi tashqi qiyofasi qo'rqinchli, ammo "
                     'yuragi pok bosh qahramonman.',
               'ru': 'Подсказка 1: Уродливый, глухой от звона колоколов горбун с чистой и преданной душой.\n'
                     'Подсказка 2: Служит звонарем в соборе Парижской Богоматери и спасает от виселицы цыганку '
                     'Эсмеральду.\n'
                     'Подсказка 3: Заглавный герой знаменитого исторического романа Виктора Гюго «Собор Парижской '
                     'Богоматери».',
               'en': 'Clue 1: Deformed, hunchbacked bell-ringer deafened by the thunderous chimes of cathedral bells.\n'
                     'Clue 2: Found sanctuary within Notre-Dame and harbored hopeless, selfless love for the Romani '
                     'dancer Esmeralda.\n'
                     "Clue 3: Heartbreaking protagonist of Victor Hugo's 1831 gothic masterpiece 'The Hunchback of "
                     "Notre-Dame'."},
  'options': {'uz': ['Klod Frollo', 'Feb de Shaboper', 'Pyer Grenvuar', 'Kvazimodo'],
              'ru': ['Клод Фролло', 'Феб де Шатопер', 'Пьер Гренгуар', 'Квазимодо'],
              'en': ['Claude Frollo', 'Phoebus', 'Pierre Gringoire', 'Quasimodo']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Kvazimodo', 'ru': 'Квазимодо', 'en': 'Quasimodo'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Luc-Olivier_Merson_-_The_Hunchback_of_Notre-Dame.jpg/640px-Luc-Olivier_Merson_-_The_Hunchback_of_Notre-Dame.jpg',
  'fun_fact': {'uz': "Gyugo Kvazimodo va Esmeralda orqali tashqi xunuklik ortidagi ma'naviy go'zallik va jamiyat "
                     "shafqatsizligini ko'rsatgan.",
               'ru': 'Имя Квазимодо происходит от первого воскресенья после Пасхи (Quasimodo), когда младенца '
                     'подбросили в собор.',
               'en': 'His name derives from Quasimodo Sunday, the day the deformed orphan was placed at the foundling '
                     'crèche.'},
  'aliases': ['kvazimodo', 'квазимодо', 'quasimodo']},
 {'id': 'lit_char_037',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Parij ko'chalarida Djali laqabli aqlli echkisi bilan raqsga tushib tirikchilik "
                     "qiluvchi lo'li qizman.\n"
                     "2-maslahat: Aslida o'g'irlab ketilgan fransuz qizi Agnes bo'lib, kapitan Febga oshiq bo'laman, "
                     "ammo arxidiakon Klod Frolloning ta'qibiga uchrayman.\n"
                     '3-maslahat: Viktor Gyugoning «Parij Bibi Maryam ibodatxonasi» romanidagi begunoh osib '
                     "o'ldirilgan go'zal qahramonman.",
               'ru': 'Подсказка 1: Прекрасная уличная танцовщица, выступающая на площадях Парижа с козочкой Джали.\n'
                     'Подсказка 2: Становится жертвой губительной страсти архидьякона Клода Фролло и погибает на '
                     'эшафоте.\n'
                     'Подсказка 3: Трагическая героиня романа Виктора Гюго «Собор Парижской Богоматери».',
               'en': 'Clue 1: Radiant street dancer captivating Paris with her tamborine and performing goat Djali.\n'
                     'Clue 2: Pursued by the obsessively jealous Archdeacon Claude Frollo, despite her love for '
                     'Captain Phoebus.\n'
                     "Clue 3: The tragic, doomed heroine of Victor Hugo's 'The Hunchback of Notre-Dame'."},
  'options': {'uz': ['Esmeralda', 'Fleur-de-Lis', 'Kozetta', 'Fantina'],
              'ru': ['Эсмеральда', 'Флёр-де-Лис', 'Козетта', 'Фантина'],
              'en': ['Esmeralda', 'Fleur-de-Lys', 'Cosette', 'Fantine']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Esmeralda', 'ru': 'Эсмеральда', 'en': 'Esmeralda'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Luc-Olivier_Merson_-_The_Hunchback_of_Notre-Dame.jpg/640px-Luc-Olivier_Merson_-_The_Hunchback_of_Notre-Dame.jpg',
  'fun_fact': {'uz': "Esmeralda obrazi soflik, begunohlik va maftunkor san'atning yovuz dunyo qarshisidagi ojizligini "
                     'aks ettiradi.',
               'ru': 'Роман способствовал сохранению и реставрации шедевра готики — Собора Парижской Богоматери.',
               'en': "Hugo's novel ignited such passion that it prompted the historic architectural restoration of "
                     'Notre-Dame Cathedral.'},
  'aliases': ['esmeralda', 'эсмеральда']},
 {'id': 'lit_char_038',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Londonning maftunkor yosh boyvachchasi bo'lib, go'zalligim va yoshligim hech qachon "
                     "so'nmasligini orzu qilaman.\n"
                     "2-maslahat: Men o'rniga rassom Bezil Xolluord chizgan portretim qariydi, buziladi va mening "
                     "barcha gunohlarimni o'zida aks ettiradi.\n"
                     '3-maslahat: Oskar Uayldning yagona romani hisoblangan estetik-falsafiy asarning bosh '
                     'qahramoniman.',
               'ru': 'Подсказка 1: Юный лондонский аристократ ослепительной красоты, заключивший негласную сделку с '
                     'вечностью.\n'
                     'Подсказка 2: Сохраняет юность и невинный облик, в то время как скрытый на чердаке портрет '
                     'стареет и впитывает его пороки.\n'
                     'Подсказка 3: Главный герой единственного романа Оскара Уайльда «Портрет Дориана Грея».',
               'en': 'Clue 1: Narcissistic, breathtakingly handsome young London aristocrat wishing his youth would '
                     'never fade.\n'
                     "Clue 2: Remains physically unblemished while Basil Hallward's portrait absorbs all his age, "
                     'crimes, and corruption.\n'
                     "Clue 3: Decadent antihero of Oscar Wilde's only novel 'The Picture of Dorian Gray'."},
  'options': {'uz': ['Lord Genri Uotton', 'Dorian Grey', 'Bezil Xolluord', 'Sibila Veyn'],
              'ru': ['Лорд Генри Уоттон', 'Дориан Грей', 'Бэзил Холлуорд', 'Сибила Вейн'],
              'en': ['Lord Henry Wotton', 'Dorian Gray', 'Basil Hallward', 'Sibyl Vane']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Dorian Grey', 'ru': 'Дориан Грей', 'en': 'Dorian Gray'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Oscar_Wilde_Sarony.jpg/640px-Oscar_Wilde_Sarony.jpg',
  'fun_fact': {'uz': "Oskar Uayld: «Bezil — men o'zim deb biladigan, Lord Genri — dunyo meni bilgan, Dorian esa men "
                     "bo'lishni xohlagan shaxs» deb aytgan.",
               'ru': 'Оскар Уайльд говорил: «Бэзил — это я, каким я себя считаю; лорд Генри — каким меня видят; а '
                     'Дориан — каким я хотел бы быть».',
               'en': "Oscar Wilde famously remarked: 'Basil is what I think I am; Lord Henry is what the world thinks "
                     "me; Dorian what I would like to be'."},
  'aliases': ['dorian grey', 'dorian gray', 'дориан грей']},
 {'id': 'lit_char_039',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Oilasini boquvchi oddiy kommiyavojer (tijorat sayohatchisi) bo'lib, tinimsiz "
                     'ishlayman.\n'
                     "2-maslahat: Bir kuni ertalab dahshatli tushlardan uyg'onib, to'shagimda bahaybat va jirkanch "
                     "hasharotga aylanganimni ko'raman.\n"
                     '3-maslahat: Frans Kafkaning mashhur «Evrilish» («Metamorfoza») novellasining bosh qahramoniman.',
               'ru': 'Подсказка 1: Скромный коммивояжер, усердно содержащий родителей и сестру.\n'
                     'Подсказка 2: Однажды утром, проснувшись после беспокойного сна, обнаруживает себя превратившимся '
                     'в страшное насекомое.\n'
                     'Подсказка 3: Главный персонаж знаменитой экзистенциальной повести Франца Кафки «Превращение».',
               'en': "Clue 1: Conscientious traveling salesman laboring relentlessly to pay off his parents' debt.\n"
                     'Clue 2: Awoke one morning from uneasy dreams to discover himself transformed into a monstrous '
                     'verminous insect.\n'
                     "Clue 3: Protagonist of Franz Kafka's celebrated existential novella 'The Metamorphosis'."},
  'options': {'uz': ['Yozef K.', 'Karl Rossman', 'Gregor Zamza', "Yer o'lchovchi K."],
              'ru': ['Йозеф К.', 'Карл Росман', 'Грегор Замза', 'Землемер К.'],
              'en': ['Josef K.', 'Karl Rossmann', 'Gregor Samsa', 'K. (The Castle)']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Gregor Zamza', 'ru': 'Грегор Замза', 'en': 'Gregor Samsa'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Kafka1906_cropped.jpg/640px-Kafka1906_cropped.jpg',
  'fun_fact': {'uz': "Kafkaning «Evrilish» asari insonning jamiyat va hatto o'z oilasi tomonidan begonalashuvi "
                     'fojiasini ochib beruvchi asardir.',
               'ru': 'Повесть «Превращение» 1915 года стала ключевым текстом мирового модернизма и литературы абсурда.',
               'en': "Published in 1915, 'The Metamorphosis' became a defining masterwork of 20th-century modernism "
                     'and alienation.'},
  'aliases': ['gregor zamza', 'gregor samsa', 'грегор замза']},
 {'id': 'lit_char_040',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Peterburgda chordoqda qashshoqlikda yashovchi sobiq huquq fakulteti talabasiman.\n'
                     "2-maslahat: Odamlarni «titroq maxluqlar» va buyuk ishlar uchun qon to'kishga haqli "
                     '«Napoleonlar»ga ajratuvchi nazariya yarataman.\n'
                     "3-maslahat: Kampir sudxo'rni bolta bilan chopib o'ldirib, vijdon azobida yonuvchi "
                     'Dostoyevskiyning «Jinoyat va jazo» romani bosh qahramoniman.',
               'ru': 'Подсказка 1: Бывший петербургский студент-юрист, живущий в нищете в каморке под самой крышей.\n'
                     'Подсказка 2: Создал чудовищную теорию о делении людей на «тварей дрожащих» и «право имеющих» '
                     'наполеонов.\n'
                     'Подсказка 3: Убил топором старуху-процентщицу Алену Ивановну в романе Фёдора Достоевского '
                     '«Преступление и наказание».',
               'en': 'Clue 1: Impoverished former law student inhabiting a squalid garret room in Saint Petersburg.\n'
                     "Clue 2: Conceived an extraordinary theory dividing mankind into 'trembling creatures' and "
                     'extraordinary men permitted to transgress moral law.\n'
                     "Clue 3: Slew an elderly pawnbroker with an axe in Fyodor Dostoevsky's psychological epic 'Crime "
                     "and Punishment'."},
  'options': {'uz': ['Dmitriy Razumixin', 'Arkadiy Svidrigaylov', 'Pyotr Lujin', 'Rodion Raskolnikov'],
              'ru': ['Дмитрий Разумихин', 'Аркадий Свидригайлов', 'Петр Лужин', 'Родион Раскольников'],
              'en': ['Razumikhin', 'Svidrigailov', 'Luzhin', 'Rodion Raskolnikov']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Rodion Raskolnikov', 'ru': 'Родион Раскольников', 'en': 'Rodion Raskolnikov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Dostoevsky_1872_by_Perov.jpg/640px-Dostoevsky_1872_by_Perov.jpg',
  'fun_fact': {'uz': "Raskolnikovning Sibir katorgasidagi ma'naviy tirilishi unga ergashgan fidoiy Sonya Marmeladova "
                     "tufayli ro'y beradi.",
               'ru': 'Фамилия героя происходит от слова «раскол», символизируя раздвоение его личности и сознания.',
               'en': "His surname derives from 'raskol' (schism or split), reflecting the inner division of his "
                     'tormented soul.'},
  'aliases': ['rodion raskolnikov', 'raskolnikov', 'родион раскольников', 'раскольников']},
 {'id': 'lit_char_041',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Ichkilikboz otam va och qolgan o'gay aka-singillarimni boqish uchun «sariq chipta» "
                     'olgan qizman.\n'
                     "2-maslahat: O'zim tubanlikka tushsam-da, qalbimning pokligi va chuqur nasroniy iymonimni saqlab "
                     'qolaman.\n'
                     "3-maslahat: Raskolnikovga o'z jinoyatiga iqror bo'lishni aytib, Sibir katorgasiga uning ortidan "
                     'borgan Dostoyevskiy romani qahramoniman.',
               'ru': 'Подсказка 1: Дочь спившегося титулярного советника Мармеладова, пожертвовавшая собой ради '
                     'голодных детей мачехи.\n'
                     'Подсказка 2: Пошла на улицу по желтому билету, сохранив кристальную чистоту души, кротость и '
                     'глубокую веру.\n'
                     'Подсказка 3: Подвигла Раскольникова на покаяние и последовала за ним в Сибирь в романе '
                     '«Преступление и наказание».',
               'en': 'Clue 1: Daughter of drunken clerk Marmeladov, sacrificing her body with a yellow ticket to feed '
                     'starving step-siblings.\n'
                     'Clue 2: Retained saintly purity of soul, enduring debasement with boundless Christian faith and '
                     'humility.\n'
                     'Clue 3: Inspired Raskolnikov to confess his murder and followed him into Siberian penal exile.'},
  'options': {'uz': ['Sonya Marmeladova', 'Dunya Raskolnikova', 'Katerina Ivanovna', 'Nastensiya'],
              'ru': ['Соня Мармеладова', 'Дуня Раскольникова', 'Катерина Ивановна', 'Настенька'],
              'en': ['Sonya Marmeladova', 'Dunya', 'Katerina Ivanovna', 'Nastenka']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Sonya Marmeladova', 'ru': 'Соня Мармеладова', 'en': 'Sonya Marmeladova'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Dostoevsky_1872_by_Perov.jpg/640px-Dostoevsky_1872_by_Perov.jpg',
  'fun_fact': {'uz': "Dostoyevskiy Sonya orqali o'zini qurbon qilish, kechirim va muhabbat orqali gunohlardan "
                     "poklanish g'oyasini ilgari surgan.",
               'ru': 'Чтение Соней главы из Евангелия о воскрешении Лазаря — один из смысловых центров романа '
                     'Достоевского.',
               'en': 'Sonya reading the raising of Lazarus to Raskolnikov is the spiritual and moral turning point of '
                     'the book.'},
  'aliases': ['sonya marmeladova', 'соня мармеладова', 'сонечка']},
 {'id': 'lit_char_042',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Shveytsariyadagi ruhiy davolanishdan Rossiyaga qaytgan 26 yoshli oxirgi knyaz '
                     'avlodiman.\n'
                     "2-maslahat: Soxtalik va yolg'ondan yiroq, bolalardek sodda va haddan tashqari mehribon bo'lganim "
                     'sababli jamiyat meni «telba» deb ataydi.\n'
                     "3-maslahat: «Go'zallik dunyoni qutqaradi» degan mashhur so'zlarni aytgan, Nastasya Filippovnani "
                     'fojiali sevgan Dostoyevskiy romani bosh qahramoniman.',
               'ru': 'Подсказка 1: Последний отпрыск знатного рода, возвращающийся в Петербург после лечения в '
                     'Швейцарии.\n'
                     'Подсказка 2: Кроткий, невинный и кристально честный человек, которого циничное общество считает '
                     'чудаком и глупцом.\n'
                     'Подсказка 3: Главный герой романа Фёдора Достоевского «Идиот», воплощение христианского идеала '
                     'добра.',
               'en': "Clue 1: Last descendant of an ancient prince's line returning to Petersburg after years in a "
                     'Swiss sanatorium.\n'
                     'Clue 2: Radically truthful, childlike, and incapable of deceit, seen as a holy fool by cynical '
                     'high society.\n'
                     "Clue 3: Saintly protagonist of Fyodor Dostoevsky's masterpiece 'The Idiot' who proclaimed "
                     "'Beauty will save the world'."},
  'options': {'uz': ['Parfen Rogojin', 'Knyaz Lev Mishkin', 'Ivan Karamazov', 'Stavrogin'],
              'ru': ['Парфен Рогожин', 'Князь Лев Мышкин', 'Иван Карамазов', 'Николай Ставрогин'],
              'en': ['Parfyon Rogozhin', 'Prince Lev Myshkin', 'Ivan Karamazov', 'Stavrogin']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Knyaz Lev Mishkin', 'ru': 'Князь Лев Мышкин', 'en': 'Prince Lev Myshkin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Dostoevsky_1872_by_Perov.jpg/640px-Dostoevsky_1872_by_Perov.jpg',
  'fun_fact': {'uz': "Dostoyevskiy knyaz Mishkin obrazida «chinakam go'zal inson» va Masih (Isoning) yer yuzidagi "
                     'qiyofasini yaratishni maqsad qilgan.',
               'ru': 'Достоевский задумывал образ Мышкина как попытку изобразить «вполне прекрасного человека» по '
                     'образцу Христа.',
               'en': "Dostoevsky intended Prince Myshkin as an artistic portrait of the 'positively good and beautiful "
                     "man'."},
  'aliases': ['knyaz mishkin', 'lev mishkin', 'князь мышкин', 'лев мышкин', 'prince myshkin']},
 {'id': 'lit_char_043',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Fyodor Pavlovich Karamazovning o'tkir aql-idrokli, ratsionalist ikkinchi o'g'liman.\n"
                     "2-maslahat: «Agar Xudo bo'lmasa, demak hamma narsa mumkin» va «Buyuk inkvizitor» afsonasining "
                     'muallifiman.\n'
                     "3-maslahat: Otamning o'ldirilishida o'z fikrlarim tufayli ichki aybdorlik his qilib aqlan "
                     "parishon bo'ladigan Dostoyevskiy qahramoniman.",
               'ru': 'Подсказка 1: Блестящий мыслитель, средний сын Федора Павловича Карамазова, бунтующий против '
                     'мироустройства.\n'
                     'Подсказка 2: Сочинитель философской поэмы «Великий инквизитор» и автор формулы «Если Бога нет, '
                     'то все позволено».\n'
                     'Подсказка 3: Герой последнего романа Ф. Достоевского «Братья Карамазовы», теряющий рассудок в '
                     'кошмаре с чертом.',
               'en': 'Clue 1: Brilliant, brooding second son of Fyodor Karamazov, locked in an intellectual rebellion '
                     'against divine order.\n'
                     "Clue 2: Author of the famous philosophical parable 'The Grand Inquisitor' and the maxim 'If God "
                     "does not exist, everything is permitted'.\n"
                     "Clue 3: Brooding rationalist driven mad by hallucinatory guilt in Fyodor Dostoevsky's 'The "
                     "Brothers Karamazov'."},
  'options': {'uz': ['Dmitriy Karamazov', 'Alyosha Karamazov', 'Ivan Karamazov', 'Pavel Smerdyakov'],
              'ru': ['Дмитрий Карамазов', 'Алёша Карамазов', 'Иван Карамазов', 'Павел Смердяков'],
              'en': ['Dmitri Karamazov', 'Alyosha Karamazov', 'Ivan Karamazov', 'Pavel Smerdyakov']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Ivan Karamazov', 'ru': 'Иван Карамазов', 'en': 'Ivan Karamazov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Dostoevsky_1872_by_Perov.jpg/640px-Dostoevsky_1872_by_Perov.jpg',
  'fun_fact': {'uz': "Ivan Karamazovning «Buyuk inkvizitor» dostoni erkin iroda, insoniyat azoblari va e'tiqod "
                     "haqidagi jahon falsafasining eng cho'qqi matnlaridan biridir.",
               'ru': 'Глава «Великий инквизитор» признана одной из вершин мировой философской и экзистенциальной '
                     'мысли.',
               'en': "'The Grand Inquisitor' chapter is widely considered a supreme pinnacle of world existential and "
                     'philosophical inquiry.'},
  'aliases': ['ivan karamazov', 'иван карамазов']},
 {'id': 'lit_char_044',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: 1930-yillar Moskvaga qora sehr seansi o'tkazish uchun chet ellik professor niqobida "
                     'tashrif buyuraman.\n'
                     "2-maslahat: Hamrohim bo'lgan Korovyov, Mushuk Begemot, Azazello va Gella bilan birga sovet "
                     "poytaxtida shov-shuv va sarosima ko'taraman.\n"
                     '3-maslahat: «Men mangu yovuzlikni istab, mangu ezgulik qiluvchi kuchning bir qismiman» degan, '
                     'Bulgakovning «Usta va Margarita» romani qahramoniman.',
               'ru': 'Подсказка 1: Загадочный иностранец, профессор черной магии, неожиданно появившийся на Патриарших '
                     'прудах в Москве.\n'
                     'Подсказка 2: Со своей свитой (Коровьев, кот Бегемот, Азазелло) устраивает сеанс магии в театре '
                     'Варьете и бал Сатаны.\n'
                     'Подсказка 3: Повелитель сил тьмы (Сатана) в великом романе Михаила Булгакова «Мастер и '
                     'Маргарита».',
               'en': "Clue 1: Mysterious foreign professor of black magic who materializes at Patriarch's Ponds in "
                     '1930s Moscow.\n'
                     'Clue 2: Staged chaos across bureaucratic Moscow with his demonic retinue (Koroviev, Behemoth, '
                     "Azazello) and hosted Satan's Ball.\n"
                     "Clue 3: The Prince of Darkness in Mikhail Bulgakov's magical realist masterpiece 'The Master and "
                     "Margarita'."},
  'options': {'uz': ['Korovyov-Fagot', 'Azazello', 'Mushuk Begemot', 'Voland (Iblis)'],
              'ru': ['Коровьев', 'Азазелло', 'Кот Бегемот', 'Воланд (Сатана)'],
              'en': ['Koroviev', 'Azazello', 'Behemoth', 'Woland (Satan)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Voland (Iblis)', 'ru': 'Воланд (Сатана)', 'en': 'Woland (Satan)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Mikhail_Bulgakov_1928.jpg/640px-Mikhail_Bulgakov_1928.jpg',
  'fun_fact': {'uz': "Voland obrazi Gyotening «Faust»idagi Mefistofeldan ilhomlanib yaratilgan bo'lib, u yovuzlik "
                     "orqali adolat o'rnatuvchi adolatli sudyadir.",
               'ru': 'Эпиграфом к роману Булгаков взял слова Мефистофеля из «Фауста» Гёте.',
               'en': "Bulgakov prefaced the novel with Goethe's Faust epigraph defining Woland's complex moral "
                     'agency.'},
  'aliases': ['voland', 'воланд', 'shayton voland', 'woland']},
 {'id': 'lit_char_045',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Tarixchi bo'lib, lotereyada 100 ming rubl yutib olgach qoraerto'lada Pontiy Pilat "
                     'haqida roman yozaman.\n'
                     "2-maslahat: Asarim tanqidchilar tomonidan shafqatsizlarcha toptalgach, qo'lyozmani pechda "
                     'yondirib ruhiy kasalxonaga tushaman.\n'
                     "3-maslahat: «Qo'lyozmalar yonmaydi» iborasi bilan abadiylashgan, Bulgakov romanidagi "
                     'Margaritaning sevgilisiman.',
               'ru': 'Подсказка 1: Бывший историк, выигравший крупную сумму в лотерею и написавший гениальный роман о '
                     'Понтии Пилате.\n'
                     'Подсказка 2: Затравленный советскими критиками, сжег свою рукопись в печке и укрылся в клинике '
                     'для душевнобольных.\n'
                     'Подсказка 3: Заглавный герой романа Михаила Булгакова «Мастер и Маргарита», обретший вечный '
                     'покой.',
               'en': 'Clue 1: Historian who won the lottery and retreated to a basement flat to craft a genius novel '
                     'about Pontius Pilate.\n'
                     'Clue 2: Hounded by cynical literary critics, burned his masterpiece manuscript in despair, and '
                     'entered a psychiatric asylum.\n'
                     "Clue 3: Co-titular hero of Mikhail Bulgakov's 'The Master and Margarita', rewarded with eternal "
                     'peace.'},
  'options': {'uz': ['Usta (Master)', 'Ivan Bezdomniy', 'Mixail Berlioz', 'Voland'],
              'ru': ['Мастер', 'Иван Бездомный', 'Михаил Берлиоз', 'Воланд'],
              'en': ['The Master', 'Ivan Bezdomny', 'Mikhail Berlioz', 'Woland']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Usta (Master)', 'ru': 'Мастер', 'en': 'The Master'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Mikhail_Bulgakov_1928.jpg/640px-Mikhail_Bulgakov_1928.jpg',
  'fun_fact': {'uz': "Usta obrazi ko'p jihatdan Mixail Bulgakovning o'z taqdiri va senzuraga qarshi fojiali kurashini "
                     'aks ettiradi.',
               'ru': 'Образ Мастера во многом автобиографичен: Булгаков сам сжигал черновики своего романа в марте '
                     '1930 года.',
               'en': "The Master mirrors Bulgakov's own persecution and his literal burning of the manuscript's "
                     'initial drafts in 1930.'},
  'aliases': ['usta', 'master', 'мастер', 'the master']},
 {'id': 'lit_char_046',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Qo'limda sariq gullar ushlab Tverskaya ko'chasida ketayotib hayotimdagi haqiqiy "
                     'muhabbatni uchrataman.\n'
                     '2-maslahat: Sevgilimni qutqarish uchun Azazelloning sehrli surtmasini surtib jodugarga aylanaman '
                     'va supurvada uchib ketaman.\n'
                     "3-maslahat: Shaytonning bahorgi balida qirolicha bo'lib xizmat qilgan, Bulgakovning durdona "
                     'asaridagi jasur ayol qahramonman.',
               'ru': 'Подсказка 1: Бездетная и несчастная в богатом браке женщина, вышедшая в переулок с желтыми '
                     'тревожными цветами.\n'
                     'Подсказка 2: Ради спасения любимого Мастера наносит крем Азазелло, становится ведьмой и летит на '
                     'метле над ночной Москвой.\n'
                     'Подсказка 3: Королева на великом балу у Сатаны в бессмертном романе Михаила Булгакова «Мастер и '
                     'Маргарита».',
               'en': 'Clue 1: Trapped in a loveless affluent marriage, carrying unsettling yellow flowers down a '
                     'Moscow lane when she met true love.\n'
                     'Clue 2: Anoints herself with demonic ointment, transforms into a radiant witch, and flies naked '
                     'over Moscow to save her Master.\n'
                     "Clue 3: The courageous, regal hostess of Satan's Great Ball in Mikhail Bulgakov's 'The Master "
                     "and Margarita'."},
  'options': {'uz': ['Gella', 'Margarita', 'Nastasya Filippovna', 'Natasha Rostova'],
              'ru': ['Гелла', 'Маргарита', 'Настасья Филипповна', 'Наташа Ростова'],
              'en': ['Hella', 'Margarita', 'Nastasya Filippovna', 'Natasha Rostova']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Margarita', 'ru': 'Маргарита', 'en': 'Margarita'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Mikhail_Bulgakov_1928.jpg/640px-Mikhail_Bulgakov_1928.jpg',
  'fun_fact': {'uz': 'Margarita timsolining prototipi Bulgakovning uchinchi xotini Yelena Sergeyevna Shilovskaya '
                     "bo'lgan.",
               'ru': 'Прототипом Маргариты была третья жена писателя Елена Сергеевна Булгакова (Шиловская).',
               'en': "Margarita was inspired by Bulgakov's devoted third wife, Elena Sergeevna Shilovskaya."},
  'aliases': ['margarita', 'маргарита']},
 {'id': 'lit_char_047',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Orqa panjalarida yuradigan, tramvayga chipta olib minmoqchi bo'lgan bahaybat qora "
                     'mushukman.\n'
                     "2-maslahat: Arosatdagi restoranda kerosin gaz pechi va to'pponcha bilan otishma qilaman, "
                     'qadahdagi toza spirtni ichaman.\n'
                     "3-maslahat: «Men xushmuomala hayvonman, faqat primusni yamamoqdaman» degan g'alati hazilkash "
                     'Voland mulozimiman.',
               'ru': 'Подсказка 1: Громадный черный кот-оборотень, разгуливающий на задних лапах и пытающийся оплатить '
                     'проезд в трамвае.\n'
                     'Подсказка 2: Обожает чистый спирт, маринованные грибы, играет в шахматы и устраивает перестрелку '
                     'в квартире № 50.\n'
                     'Подсказка 3: Шут и любимый подручный Воланда в романе Булгакова «Мастер и Маргарита», починяющий '
                     'примус.',
               'en': 'Clue 1: Enormous talking black demon-cat who walks on two legs and tries to pay a nickel on a '
                     'Moscow streetcar.\n'
                     'Clue 2: Relishes straight grain alcohol with pickled mushrooms, plays chess, and shoots a '
                     'Browning pistol.\n'
                     "Clue 3: Woland's wisecracking demonic jester famously claiming: 'I'm not bothering anybody, I'm "
                     "just sitting here mending the primus stove'."},
  'options': {'uz': ['Korovyov-Fagot', 'Azazello', 'Mushuk Begemot', 'Abadonna'],
              'ru': ['Коровьев-Фагот', 'Азазелло', 'Кот Бегемот', 'Абадонна'],
              'en': ['Koroviev', 'Azazello', 'Behemoth (The Cat)', 'Abadonna']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Mushuk Begemot', 'ru': 'Кот Бегемот', 'en': 'Behemoth (The Cat)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Mikhail_Bulgakov_1928.jpg/640px-Mikhail_Bulgakov_1928.jpg',
  'fun_fact': {'uz': "Begemot qiyofasi Bibliyadagi qudratli hayvon va qadimiy demonologiya an'analariga asoslangan "
                     'satirik timsoldir.',
               'ru': 'Фраза «Не шалю, никого не трогаю, починяю примус» стала одной из самых цитируемых в русской '
                     'культуре.',
               'en': 'His quip about mending the primus stove remains one of the most celebrated comedic lines in '
                     'Russian literature.'},
  'aliases': ['mushuk begemot', 'begemot', 'кот бегемот', 'бегемот', 'behemoth']},
 {'id': 'lit_char_048',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Golfstrim oqimida 84 kundan beri bitta ham baliq tutolmay yurgan qari kubalik '
                     'baliqchiman.\n'
                     '2-maslahat: 85-kuni ulkan qilichbaliqni (marlin) qarmoqqa ilintirib, u bilan ochiq dengizda uch '
                     'kunlik mardona kurash olib boraman.\n'
                     "3-maslahat: «Inson yengilish uchun yaratilmagan, uni mahv etish mumkin, ammo mag'lub qilib "
                     "bo'lmaydi» degan Ernest Xeminguey qissasi qahramoniman.",
               'ru': 'Подсказка 1: Старый кубинский рыбак, который 84 дня выходил в море и не поймал ни одной рыбы.\n'
                     'Подсказка 2: На 85-й день зацепил гигантского марлина и вел с ним изнурительную многодневную '
                     'дуэль в открытом океане.\n'
                     'Подсказка 3: Главный герой повести Эрнеста Хемингуэя «Старик и море», провозгласивший '
                     'несгибаемость человека.',
               'en': 'Clue 1: Aging Cuban fisherman who went 84 agonizing days into the Gulf Stream without catching a '
                     'single fish.\n'
                     'Clue 2: Hooked a gigantic 18-foot marlin on day 85, waging an epic solitary battle before sharks '
                     'scavenged the carcass.\n'
                     "Clue 3: Resilient hero of Ernest Hemingway's Nobel Prize-winning novella 'The Old Man and the "
                     "Sea'."},
  'options': {'uz': ['Manolin', 'Kapitan Axav', 'Robinzon Kruzo', 'Santyago (Chol)'],
              'ru': ['Манолин', 'Капитан Ахав', 'Робинзон Крузо', 'Сантьяго (Старик)'],
              'en': ['Manolin', 'Captain Ahab', 'Robinson Crusoe', 'Santiago (The Old Man)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Santyago (Chol)', 'ru': 'Сантьяго (Старик)', 'en': 'Santiago (The Old Man)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/ErnestHemingway.jpg/640px-ErnestHemingway.jpg',
  'fun_fact': {'uz': "Xeminguey ushbu qissasi uchun 1953 yilda Pulitser, 1954 yilda esa Adabiyot bo'yicha Nobel "
                     "mukofotiga sazovor bo'lgan.",
               'ru': 'Повесть «Старик и море» принесла Хемингуэю Пулитцеровскую премию и сыграла ключевую роль в '
                     'присуждении Нобелевской премии.',
               'en': "'The Old Man and the Sea' won the Pulitzer Prize in 1953 and propelled Hemingway to the 1954 "
                     'Nobel Prize.'},
  'aliases': ['santyago', 'chol', 'сантьяго', 'старик', 'santiago']},
 {'id': 'lit_char_049',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Nyu-Yorkning Long-Aylendidagi hashamatli qasrda har dam olish kunlari dabdabali '
                     'ziyofatlar beruvchi sirli millioner.\n'
                     "2-maslahat: O'tmishdagi sevgilim Deyzi Byukenenni qaytarish ilinjida ko'rfaz narigi tomonidagi "
                     'yashil chiroqqa termulib yashayman.\n'
                     "3-maslahat: F. Skott Fitsjeraldning «Yo'qotilgan avlod» va «Jaz asri» durdonasi bo'lgan "
                     'romanining fojiali bosh qahramoniman.',
               'ru': 'Подсказка 1: Загадочный миллионер из особняка в Уэст-Эгге, закатывающий самые пышные вечеринки '
                     '«эпохи джаза».\n'
                     'Подсказка 2: Каждую ночь смотрит на зеленый огонек на том берегу залива, мечтая вернуть любовь '
                     'Дэйзи Бьюкенен.\n'
                     'Подсказка 3: Трагический главный герой великого американского романа Ф. Скотта Фицджеральда '
                     '«Великий Гэтсби».',
               'en': 'Clue 1: Enigmatic bootlegger-millionaire throwing extravagant, glamorous parties at his Long '
                     'Island estate.\n'
                     'Clue 2: Yearns across the bay toward the green light at the end of the dock where his lost love '
                     'Daisy Buchanan lives.\n'
                     "Clue 3: Tragic protagonist of F. Scott Fitzgerald's seminal masterpiece 'The Great Gatsby'."},
  'options': {'uz': ['Buyuk Getsbi (Jey Getsbi)', 'Nik Karrauey', 'Tom Byukenen', 'Jordanj Beyker'],
              'ru': ['Джей Гэтсби (Великий Гэтсби)', 'Ник Каррауэй', 'Том Бьюкенен', 'Джордан Бейкер'],
              'en': ['Jay Gatsby (The Great Gatsby)', 'Nick Carraway', 'Tom Buchanan', 'Jordan Baker']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Buyuk Getsbi (Jey Getsbi)',
                     'ru': 'Джей Гэтсби (Великий Гэтсби)',
                     'en': 'Jay Gatsby (The Great Gatsby)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/F_Scott_Fitzgerald_1921.jpg/640px-F_Scott_Fitzgerald_1921.jpg',
  'fun_fact': {'uz': 'Getsbi obrazi Amerika orzusi («American Dream»)ning sarobligi va ideal sevgining fojeasi '
                     'sifatida talqin qilinadi.',
               'ru': '«Великий Гэтсби» считается главным художественным отражением взлета и краха «американской мечты» '
                     '1920-х годов.',
               'en': 'Gatsby embodies the intoxicating splendor and hollow disillusionment of the post-WWI American '
                     'Dream.'},
  'aliases': ['jey getsbi', 'getsbi', 'buyuk getsbi', 'джей гэтсби', 'гэтсби', 'jay gatsby']},
 {'id': 'lit_char_050',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Pensi maktab-internatidan imtihonlarni topshirolmay haydalgan 16 yoshli o'smirman.\n"
                     '2-maslahat: Qizil ovchi kepkasini kiyib, kattalarning soxtakorligi («phony») va riyokorligidan '
                     'nafratlanib Nyu-Yorkda kezaman.\n'
                     '3-maslahat: J. D. Selinjerning yoshlar isyoni ifodalangan «Javdorda jarlik yoqasida» romanining '
                     'bosh qahramoniman.',
               'ru': 'Подсказка 1: Шестнадцатилетний подросток, исключенный за неуспеваемость из престижной '
                     'школы-пансиона Пэнси.\n'
                     'Подсказка 2: Бродит по зимнему Нью-Йорку в красной охотничьей шапке, протестуя против фальши и '
                     'лицемерия мира взрослых.\n'
                     'Подсказка 3: Главный герой культового романа Дж. Д. Сэлинджера «Над пропастью во ржи».',
               'en': 'Clue 1: Disillusioned 16-year-old expelled from Pencey Prep boarding school for failing four '
                     'classes.\n'
                     'Clue 2: Wears a red hunting hat backwards and wanders a wintry Manhattan railing against adult '
                     "'phoniness'.\n"
                     "Clue 3: Alienated teenage narrator of J. D. Salinger's landmark coming-of-age novel 'The Catcher "
                     "in the Rye'."},
  'options': {'uz': ['Stredleyter', 'Xolden Kolfild', 'Fibi Kolfild', 'Akli'],
              'ru': ['Стрэдлейтер', 'Холден Колфилд', 'Фиби Колфилд', 'Экли'],
              'en': ['Stradlater', 'Holden Caulfield', 'Phoebe Caulfield', 'Ackley']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Xolden Kolfild', 'ru': 'Холден Колфилд', 'en': 'Holden Caulfield'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/J._D._Salinger.jpg/640px-J._D._Salinger.jpg',
  'fun_fact': {'uz': "Xoldenning orzusi — javdorda jarlik yoqasida o'ynayotgan bolalar jarga qulab tushmasligi uchun "
                     "ularni ushlab qoluvchi bo'lishdir.",
               'ru': 'Название романа связано с мечтой Холдена — стать ловцом играющих во ржи детей над пропастью, '
                     'спасая их невинность.',
               'en': "Holden dreams of preserving children's purity by acting as a catcher saving them from falling "
                     'off a cliff.'},
  'aliases': ['xolden kolfild', 'holden caulfield', 'холден колфилд', 'xolden', 'холден']},
 {'id': 'lit_char_051',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Alabama shtatidagi Meykomb shaharchasida yashovchi qat'iyatli, olijanob advokat va "
                     'beva otaman.\n'
                     "2-maslahat: Oq tanli ayolni zo'rlashda nohaq ayblangan qora tanli Tom Robinsonni sudda barcha "
                     'nafratga qaramay himoya qilaman.\n'
                     "3-maslahat: Harper Lining irqiy adolatsizlikka qarshi qaratilgan «Mazaxchini o'ldirish» "
                     'romanining qahramoniman.',
               'ru': 'Подсказка 1: Принципиальный адвокат и мудрый отец-одиночка из сонного городка Мейкомб в штате '
                     'Алабама.\n'
                     'Подсказка 2: Вопреки давлению расистского общества берется защищать в суде невиновного '
                     'чернокожего Тома Робинсона.\n'
                     'Подсказка 3: Центральный нравственный ориентир романа Харпер Ли «Убить пересмешника».',
               'en': 'Clue 1: Principled, widowed attorney and father residing in Maycomb, Alabama.\n'
                     'Clue 2: Defended Tom Robinson, a Black man falsely accused of rape, in defiance of deep-seated '
                     'racial prejudice.\n'
                     "Clue 3: Moral pillar of Harper Lee's Pulitzer Prize-winning classic 'To Kill a Mockingbird'."},
  'options': {'uz': ['Tom Robinson', 'Bu Redli', 'Attikus Finch', 'Bob Yuel'],
              'ru': ['Том Робинсон', 'Страшила Рэдли', 'Аттикус Финч', 'Боб Юэлл'],
              'en': ['Tom Robinson', 'Boo Radley', 'Atticus Finch', 'Bob Ewell']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Attikus Finch', 'ru': 'Аттикус Финч', 'en': 'Atticus Finch'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Harper_Lee_1960.jpg/640px-Harper_Lee_1960.jpg',
  'fun_fact': {'uz': 'Attikus Finch Amerika Kino instituti (AFI) tomonidan barcha davrlarning birinchi raqamli kino '
                     'qahramoni deb topilgan.',
               'ru': 'Американский институт киноискусства (AFI) признал Аттикуса Финча величайшим положительным героем '
                     'в истории кино.',
               'en': 'The American Film Institute named Atticus Finch the greatest screen hero in American cinema '
                     'history.'},
  'aliases': ['attikus finch', 'attikus', 'аттикус финч', 'аттикус', 'atticus finch']},
 {'id': 'lit_char_052',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Shirdagi Xobbiton qishlog'ida yashovchi, amakim Bilbodan qolgan sehrli uzukni meros "
                     'olgan xobbitman.\n'
                     "2-maslahat: Butun O'rta Yerni Sauron zulmidan qutqarish uchun Orollik tog'i (Orodruin) oloviga "
                     'Uzukni tashlashga otlanaman.\n'
                     "3-maslahat: J.R.R. Tolkinning «Uzuklar hukmdori» epopeyasidagi Uzuk sohibi bo'lgan bosh "
                     'qahramonman.',
               'ru': 'Подсказка 1: Скромный хоббит из Шира, унаследовавший от дядюшки Бильбо таинственное золотое '
                     'кольцо.\n'
                     'Подсказка 2: Принимает на себя тяжелейшую ношу — отнести Кольцо Всевластья в Мордор и уничтожить '
                     'его в Роковой горе.\n'
                     'Подсказка 3: Хранитель Кольца, главный герой монументальной трилогии Дж. Р. Р. Толкина '
                     '«Властелин колец».',
               'en': 'Clue 1: Modest Shire hobbit who inherited a golden magic ring from his eccentric uncle Bilbo.\n'
                     'Clue 2: Volunteered as Ring-bearer at the Council of Elrond to carry the One Ring into the fires '
                     'of Mount Doom.\n'
                     "Clue 3: Enduring hero of J.R.R. Tolkien's legendary high-fantasy epic 'The Lord of the Rings'."},
  'options': {'uz': ['Semvayz Gemji', 'Bilbo Beggins', 'Peregrin Tuk', 'Frodo Beggins'],
              'ru': ['Сэмуайз Гэмджи', 'Бильбо Бэггинс', 'Перегрин Тук', 'Фродо Бэггинс'],
              'en': ['Samwise Gamgee', 'Bilbo Baggins', 'Pippin', 'Frodo Baggins']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Frodo Beggins', 'ru': 'Фродо Бэггинс', 'en': 'Frodo Baggins'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/J._R._R._Tolkien%2C_ca._1925.jpg/640px-J._R._R._Tolkien%2C_ca._1925.jpg',
  'fun_fact': {'uz': "Frodoning sadoqatli bog'boni va do'sti Sem Gemji bo'lmaganida, uzukni halokat tog'iga yetkazish "
                     "mutlaqo imkonsiz bo'lardi.",
               'ru': 'Толкин однажды признался в письме, что считал настоящим главным героем книги скромного Сэма '
                     'Гэмджи.',
               'en': 'Tolkien personally reflected in his letters that Samwise Gamgee was the true chief hero of the '
                     'epic.'},
  'aliases': ['frodo beggins', 'frodo', 'фродо бэггинс', 'фродо', 'frodo baggins']},
 {'id': 'lit_char_053',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Kulrang xalat kiygan, uzun oq soqolli, hassali va uchli shlyapa kiygan afsonaviy '
                     'donishmand afsungarman (Istar).\n'
                     '2-maslahat: Moriya yerosti konlarida qadimiy Balrog maxluqi bilan jangga kirishib, «Siz bu '
                     "yerdan o'tolmaysiz!» deb xitob qilaman.\n"
                     "3-maslahat: Tolkin asarlarida Kulrang Gandalfdan Oq Gandalfga evrilib, O'rta Yerni saqlab qolgan "
                     "ulug' sehrgarman.",
               'ru': 'Подсказка 1: Могущественный маг (истари) в сером плаще и остроконечной шляпе, друг хоббитов и '
                     'эльфов.\n'
                     'Подсказка 2: В копях Мории преграждает путь древнему огненному демону Балрогу с возгласом «Ты не '
                     'пройдешь!».\n'
                     'Подсказка 3: Возродился из Сердцевины мира как Гэндальф Белый в трилогии Толкина «Властелин '
                     'колец».',
               'en': 'Clue 1: Wandering wizard (Istar) clad in gray robes and pointed hat, trusted friend of elves and '
                     'hobbits.\n'
                     "Clue 2: Cast down the fiery Balrog in the chasm of Moria with the thunderous shout 'You shall "
                     "not pass!'.\n"
                     "Clue 3: Reborn as Gandalf the White to lead the Free Peoples of Middle-earth in Tolkien's "
                     'legendarium.'},
  'options': {'uz': ['Gandalf (Mithrandir)', 'Saruman', 'Radagast', 'Dambldor'],
              'ru': ['Гэндальф (Митрандир)', 'Саруман', 'Радагаст', 'Дамблдор'],
              'en': ['Gandalf (Mithrandir)', 'Saruman', 'Radagast', 'Dumbledore']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Gandalf (Mithrandir)', 'ru': 'Гэндальф (Митрандир)', 'en': 'Gandalf (Mithrandir)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/J._R._R._Tolkien%2C_ca._1925.jpg/640px-J._R._R._Tolkien%2C_ca._1925.jpg',
  'fun_fact': {'uz': 'Elflar tilida Gandalf «Mitrandir» (Kulrang darbadar) deb ataladi va u ilohiy Mayar xilqatiga '
                     'mansubdir.',
               'ru': 'На эльфийском синдарине Гэндальфа зовут Митрандир — «Серый странник».',
               'en': 'Known among the Elves as Mithrandir, he is an immortal spiritual being known as a Maia.'},
  'aliases': ['gandalf', 'mithrandir', 'гэндальф', 'митрандир']},
 {'id': 'lit_char_054',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Shimol darbadari bo'lib, «Kezuvchi» (Strider) nomi bilan tanilgan jasur jangchiman.\n"
                     "2-maslahat: Isildurning sinib ketgan Narsil qilichi qayta quyilgach (Anduril), o'z qonuniy "
                     "taxtimga da'vogarlik qilaman.\n"
                     "3-maslahat: Gondor va Arnor qirolligining qonuniy merosxo'ri Elessar, Tolkinning «Uzuklar "
                     'hukmdori» qahramoniman.',
               'ru': 'Подсказка 1: Опытный следопыт Севера по прозвищу Бродяжник (Колоброд), потомок древних '
                     'нуменорских королей.\n'
                     'Подсказка 2: Обнажает перекованный меч Нарсиль (Андрил) и ведет армию людей против сил Мордора.\n'
                     'Подсказка 3: Законный король Гондора и Арнора Элессар в эпопее Толкина «Властелин колец».',
               'en': 'Clue 1: Weathered Northern Dúnedain ranger introduced at the Prancing Pony inn under the alias '
                     'Strider.\n'
                     'Clue 2: Wielded the reforged sword Andúril, Flame of the West, leading the host of the West at '
                     'the Black Gate.\n'
                     "Clue 3: True heir of Isildur crowned King Elessar of Gondor and Arnor in J.R.R. Tolkien's epic."},
  'options': {'uz': ['Boromir', 'Aragorn (Strider)', 'Faramir', 'Teoden'],
              'ru': ['Боромир', 'Арагорн (Следопыт)', 'Фарамир', 'Теоден'],
              'en': ['Boromir', 'Aragorn (Strider)', 'Faramir', 'Theoden']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Aragorn (Strider)', 'ru': 'Арагорн (Следопыт)', 'en': 'Aragorn (Strider)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/J._R._R._Tolkien%2C_ca._1925.jpg/640px-J._R._R._Tolkien%2C_ca._1925.jpg',
  'fun_fact': {'uz': "Aragorn elf malikasi Arven bilan turmush qurib, O'rta Yerdagi odamlar va elflar o'rtasidagi "
                     "so'nggi ittifoqni bog'laydi.",
               'ru': 'Брак Арагорна и эльфийской владычицы Арвен символизировал объединение двух древних родов '
                     'Средиземья.',
               'en': 'His union with the half-elven Arwen Undómiel renewed the royal lineage of men and Eldar.'},
  'aliases': ['aragorn', 'strider', 'elessar', 'арагорн', 'колоброд']},
 {'id': 'lit_char_055',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Qadimda Smeagol ismli daryo xobbiti edim, amakivachcham Degolni uzuk uchun o'ldirib "
                     "qo'yganman.\n"
                     "2-maslahat: Tumanli tog'lar ostidagi zulmatda asrlar bo'yi yashab, maxluqqa aylandim va uzukni "
                     '«mening jajji xazinam» deb atayman.\n'
                     "3-maslahat: Tolkin asarlarida uzuk bilan birga Orodruin olovli qa'riga qulab, uni yo'q qilgan "
                     'ikki qiyofali mavjudotman.',
               'ru': 'Подсказка 1: Некогда речной хоббит по имени Смеагол, убивший друга ради обладания золотым '
                     'кольцом.\n'
                     'Подсказка 2: Провел столетия в темных пещерах Мглистых гор, непрестанно повторяя «Моя прелесть!» '
                     '(My Precious).\n'
                     'Подсказка 3: Жалкое и коварное существо, чье падение в лаву Роковой горы уничтожило Кольцо '
                     'Всевластья у Толкина.',
               'en': 'Clue 1: Once a Stoor hobbit named Sméagol who murdered his kin Déagol on his birthday to claim a '
                     'golden trinket.\n'
                     'Clue 2: Withered underground for nearly 500 years, muttering sibilantly about his lost '
                     "'Precious'.\n"
                     'Clue 3: Dual-personality wretched creature whose final plunge into Mount Doom destroyed the One '
                     'Ring.'},
  'options': {'uz': ['Bilbo Beggins', 'Sauron', 'Gollum (Smeagol)', 'Grima Ilontil'],
              'ru': ['Бильбо Бэггинс', 'Саурон', 'Голлум (Смеагол)', 'Грима Гнилоуст'],
              'en': ['Bilbo Baggins', 'Sauron', 'Gollum (Smeagol)', 'Grima Wormtongue']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Gollum (Smeagol)', 'ru': 'Голлум (Смеагол)', 'en': 'Gollum (Smeagol)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/J._R._R._Tolkien%2C_ca._1925.jpg/640px-J._R._R._Tolkien%2C_ca._1925.jpg',
  'fun_fact': {'uz': 'Piter Jekson filmlarida Gollum rolini harakatlarni qayd etish (motion capture) texnologiyasi '
                     'orqali Endi Serkis ijro etgan.',
               'ru': 'Энди Серкис совершил революцию в кинематографе, вдохнув жизнь в образ Голлума через захват '
                     'движения.',
               'en': "Andy Serkis' pioneering motion-capture portrayal of Gollum revolutionized digital performance in "
                     'film history.'},
  'aliases': ['gollum', 'smeagol', 'голлум', 'смеагол']},
 {'id': 'lit_char_056',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Peshonasida chaqmoqsimon chandiq bo'lgan, xolasi va tog'asining zinalar ostidagi "
                     "qorong'i xonasida ulg'aygan yetim bolaman.\n"
                     '2-maslahat: 11 yoshimda Xogvarts afsungarlik va sehrgarlik maktabiga qabul qilinib, Griffindor '
                     'fakultetiga tushaman.\n'
                     '3-maslahat: «Omon qolgan bola» sifatida Lord Voldemortga qarshi kurashgan J.K. Rouling romanlar '
                     'turkumi bosh qahramoniman.',
               'ru': 'Подсказка 1: Сирота со шрамом в виде молнии на лбу, живший в чулане под лестницей у жестоких '
                     'родственников Дурслей.\n'
                     'Подсказка 2: В 11 лет узнает, что он волшебник, и отправляется учиться в школу магии Хогвартс на '
                     'факультет Гриффиндор.\n'
                     'Подсказка 3: «Мальчик, который выжил», победивший Темного Лорда Волан-де-Морта в книгах Дж. К. '
                     'Роулинг.',
               'en': 'Clue 1: Orphaned boy with a lightning-bolt scar on his forehead, raised in a cupboard under the '
                     'stairs by the Dursleys.\n'
                     'Clue 2: Discovered his magical heritage on his 11th birthday and was sorted into Gryffindor '
                     'house at Hogwarts.\n'
                     "Clue 3: 'The Boy Who Lived', titular hero of J.K. Rowling's record-shattering wizarding fantasy "
                     'saga.'},
  'options': {'uz': ['Ron Uizli', 'Drako Malfoy', 'Nevil Longbottom', 'Garri Potter'],
              'ru': ['Рон Уизли', 'Драко Малфой', 'Невилл Долгопупс', 'Гарри Поттер'],
              'en': ['Ron Weasley', 'Draco Malfoy', 'Neville Longbottom', 'Harry Potter']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Garri Potter', 'ru': 'Гарри Поттер', 'en': 'Harry Potter'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/640px-J._K._Rowling_2010.jpg',
  'fun_fact': {'uz': 'Garri Potter kitoblari 80 dan ortiq tillarga tarjima qilingan va 500 million nusxadan ortiq '
                     'tirajda sotilgan.',
               'ru': 'Книги о Гарри Поттере разошлись тиражом свыше 500 миллионов экземпляров, став самой продаваемой '
                     'серией в истории.',
               'en': 'The Harry Potter series has sold over 500 million copies, making it the best-selling book series '
                     'in world history.'},
  'aliases': ['garri potter', 'harry potter', 'гарри поттер', 'garri']},
 {'id': 'lit_char_057',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Tish shifokorlari bo'lgan oddiy odamlar (magllar) oilasida tug'ilgan juda tirishqoq "
                     'qizman.\n'
                     "2-maslahat: Xogvartsda o'z avlodining eng a'lochi o'quvchisi bo'lib, kutubxonasiz yashay "
                     'olmayman va vaqt buragichidan foydalanaman.\n'
                     '3-maslahat: Garri Potter va Ron Uizlining eng yaqin sadoqatli dugonasi, afsungar qahramonman.',
               'ru': 'Подсказка 1: Дочь маглов-дантистов, поражающая всех невероятной эрудицией и любовью к '
                     'библиотекам.\n'
                     'Подсказка 2: Лучшая ученица Хогвартса на факультете Гриффиндор, использовавшая маховик времени '
                     'для посещения всех уроков.\n'
                     'Подсказка 3: Верная подруга Гарри Поттера и Рона Уизли в семикнижии Дж. К. Роулинг.',
               'en': 'Clue 1: Muggle-born daughter of dentists renowned for her insatiable bookishness and fierce '
                     'intellect.\n'
                     'Clue 2: Top student of her year in Gryffindor, granted a Time-Turner to attend overlapping class '
                     'schedules.\n'
                     "Clue 3: Invaluable best friend of Harry Potter and Ron Weasley throughout J.K. Rowling's saga."},
  'options': {'uz': ['Germiona Greyndjer', 'Jinni Uizli', 'Polumna Lavgood', 'Chjou Chang'],
              'ru': ['Гермиона Грейнджер', 'Джинни Уизли', 'Полумна Лавгуд', 'Чжоу Чанг'],
              'en': ['Hermione Granger', 'Ginny Weasley', 'Luna Lovegood', 'Cho Chang']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Germiona Greyndjer', 'ru': 'Гермиона Грейнджер', 'en': 'Hermione Granger'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/640px-J._K._Rowling_2010.jpg',
  'fun_fact': {'uz': "Rouling Germiona xarakterini ko'p jihatdan 11 yoshlik o'zidan nusxa olib yaratganini tan olgan.",
               'ru': 'Дж. К. Роулинг признавалась, что образ Гермионы во многом списан с неё самой в школьные годы.',
               'en': 'J.K. Rowling revealed that Hermione was largely an exaggerated caricature of herself when '
                     'young.'},
  'aliases': ['germiona greyndjer', 'germiona', 'гермиона грейнджер', 'гермиона', 'hermione granger']},
 {'id': 'lit_char_058',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Yetimxonada ulg'aygan Tom Marvolo Ridl ismli yarimqon sehrgarman, Salazar "
                     "Slizerinning to'g'ridan-to'g'ri avlodiman.\n"
                     "2-maslahat: O'lmaslikka erishish uchun jonimni yetti qismga bo'lib krestajlarga (horcrux) "
                     'joylashtirgan Qora Lordman.\n'
                     "3-maslahat: Sehrgarlar dunyosida nomi aytilishidan qo'rqiladigan («Ismini aytib bo'lmaydigan "
                     'zot») Garri Potterning ashaddiy yovuz dushmaniman.',
               'ru': 'Подсказка 1: Наследник Салазара Слизерина по имени Том Марволо Реддл, выросший в сиротском '
                     'приюте.\n'
                     'Подсказка 2: Разделил свою душу на крестражи в погоне за бессмертием и возглавил Пожирателей '
                     'смерти.\n'
                     'Подсказка 3: Главный злодей саги о Гарри Поттере, известный как «Тот-Кого-Нельзя-Называть».',
               'en': 'Clue 1: Born Tom Marvolo Riddle in an orphanage, proud descendant of Hogwarts founder Salazar '
                     'Slytherin.\n'
                     'Clue 2: Split his soul into seven Horcruxes to attain immortality, commanding the masked Death '
                     'Eaters.\n'
                     'Clue 3: Supreme Dark Lord and arch-villain of the Harry Potter universe, whispered as '
                     "'He-Who-Must-Not-Be-Named'."},
  'options': {'uz': ['Severus Sneyp', 'Lord Voldemort (Tom Ridl)', 'Gellert Grindevald', 'Lyutsius Malfoy'],
              'ru': ['Северус Снегг', 'Волан-де-Морт (Том Реддл)', 'Геллерт Грин-де-Вальд', 'Люциус Малфой'],
              'en': ['Severus Snape', 'Lord Voldemort (Tom Riddle)', 'Gellert Grindelwald', 'Lucius Malfoy']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Lord Voldemort (Tom Ridl)',
                     'ru': 'Волан-де-Морт (Том Реддл)',
                     'en': 'Lord Voldemort (Tom Riddle)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/640px-J._K._Rowling_2010.jpg',
  'fun_fact': {'uz': "«Voldemort» fransuzcha «vol de mort» birikmasidan olingan bo'lib, «o'limdan qochish» yoki «o'lim "
                     "parvozi» ma'nosini beradi.",
               'ru': 'Имя Voldemort происходит от французского словосочетания, означающего «полет смерти» или «побег '
                     'от смерти».',
               'en': "The name Voldemort originates from the French phrase meaning 'flight from death'."},
  'aliases': ['voldemort', 'lord voldemort', 'tom ridl', 'волан-де-морт', 'воландеморт', 'lord voldemort']},
 {'id': 'lit_char_059',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Slizerin fakulteti dekani, Xogvartsda damlamalar (potion) fani bo'yicha qattiqqo'l "
                     "o'qituvchiman.\n"
                     '2-maslahat: Bolalikdagi sevgilim Lili Potterga sadoqatim tufayli Dambldorning maxfiy josusi '
                     "sifatida O'lim qassoblariga qo'shilaman.\n"
                     "3-maslahat: «Always» («Hamisha») so'zi bilan kitobxonlar qalbini larzaga solgan yarimzot "
                     'shahzoda (Half-Blood Prince) qahramoniman.',
               'ru': 'Подсказка 1: Мрачный и строгий декан факультета Слизерин, преподаватель зельеварения в '
                     'Хогвартсе.\n'
                     'Подсказка 2: Двойной агент Дамблдора среди Пожирателей смерти, движимый вечной любовью к Лили '
                     'Поттер.\n'
                     'Подсказка 3: «Принц-полукровка», чье слово «Всегда» (Always) раскрыло одну из величайших тайн '
                     'саги Роулинг.',
               'en': 'Clue 1: Brooding Potions Master and Head of Slytherin House at Hogwarts Castle.\n'
                     'Clue 2: Double agent acting between Dumbledore and Voldemort, motivated by lifelong, unspoken '
                     'devotion to Lily Evans.\n'
                     "Clue 3: The 'Half-Blood Prince' whose patronus doe and single word 'Always' revealed his true "
                     'allegiance.'},
  'options': {'uz': ['Albus Dambldor', 'Sirius Blek', 'Severus Sneyp', 'Remus Lyupin'],
              'ru': ['Альбус Дамблдор', 'Сириус Блэк', 'Северус Снегг (Снейп)', 'Римус Люпин'],
              'en': ['Albus Dumbledore', 'Sirius Black', 'Severus Snape', 'Remus Lupin']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Severus Sneyp', 'ru': 'Северус Снегг (Снейп)', 'en': 'Severus Snape'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/640px-J._K._Rowling_2010.jpg',
  'fun_fact': {'uz': 'Aktrisa Alan Rikman ushbu rolni mahorat bilan ijro etishi uchun Rouling unga Sneypning siri '
                     'haqida avvaldan pichirlab aytgan yagona shaxs edi.',
               'ru': 'Алан Рикман был единственным актером, которому Роулинг заранее раскрыла тайну любви Снегга к '
                     'Лили.',
               'en': "Alan Rickman was the only cast member to whom Rowling revealed Snape's true motivations before "
                     'the books finished.'},
  'aliases': ['severus sneyp', 'sneyp', 'северус снегг', 'северус снейп', 'снегг', 'snape']},
 {'id': 'lit_char_060',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: 12-okrugda yashovchi, singlim Prim o'rniga qonli turnirda ko'ngilli bo'lib "
                     "qatnashishga rozi bo'lgan 16 yoshli qizman.\n"
                     "2-maslahat: Kamondan bexato otish qobiliyatim va g'alati «Masxarachi qush» (Mockingjay) ramzim "
                     'bilan Panem zolimlariga qarshi isyon boshlayman.\n'
                     "3-maslahat: Syuzen Kollinzning «Ochlik o'yinlari» distopiya trilogiyasining bosh ayol "
                     'qahramoniman.',
               'ru': 'Подсказка 1: Шестнадцатилетняя охотница из бедного Дистрикта 12, добровольно занявшая место '
                     'младшей сестры Прим.\n'
                     'Подсказка 2: Метко стреляет из лука и становится символом восстания угнетенных — '
                     '«Сойкой-пересмешницей».\n'
                     'Подсказка 3: Главная героиня антиутопической трилогии Сьюзен Коллинз «Голодные игры».',
               'en': 'Clue 1: Skilled hunter from the impoverished Seam in District 12 who volunteered to take her '
                     "sister Prim's place.\n"
                     'Clue 2: Armed with a bow and arrow, she sparked a nationwide revolution under the symbol of the '
                     'Mockingjay.\n'
                     "Clue 3: 'The Girl on Fire', protagonist of Suzanne Collins' blockbuster dystopian saga 'The "
                     "Hunger Games'."},
  'options': {'uz': ['Pita Mellark', 'Geyl Xotorn', 'Tris Prayor', 'Ketniss Everdin'],
              'ru': ['Пит Мелларк', 'Гейл Хоторн', 'Трис Приор', 'Китнисс Эвердин'],
              'en': ['Peeta Mellark', 'Gale Hawthorne', 'Tris Prior', 'Katniss Everdeen']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ketniss Everdin', 'ru': 'Китнисс Эвердин', 'en': 'Katniss Everdeen'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Suzanne_Collins_2009.jpg/640px-Suzanne_Collins_2009.jpg',
  'fun_fact': {'uz': "«Ochlik o'yinlari» kinoekranlashtirishida Ketniss rolini ijro etgan Jennifer Lourens dunyo "
                     'miqyosidagi yulduzga aylangan.',
               'ru': 'Роль Китнисс в экранизации принесла всемирную славу актрисе Дженнифер Лоуренс.',
               'en': "Jennifer Lawrence's portrayal of Katniss launched her to international stardom."},
  'aliases': ['ketniss everdin', 'ketniss', 'китнисс эвердин', 'китнисс', 'katniss everdeen']},
 {'id': 'lit_char_061',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Belgiyalik sobiq politsiyachi bo'lib, o'ziga xos tuxumsimon boshim va qat'iy "
                     "parvarishlangan mo'ylovim bor.\n"
                     "2-maslahat: Jismoniy izlar izlab o'tirmay, miyadagi «kichkina kulrang hujayralar» (little grey "
                     'cells) vositasida eng murakkab qotilliklarni ochaman.\n'
                     "3-maslahat: Agata Kristining 33 ta romani va o'nlab hikoyalarining bosh qahramoni bo'lgan buyuk "
                     'detektivman.',
               'ru': 'Подсказка 1: Бельгийский сыщик невысокого роста с яйцеобразной головой и тщательно ухоженными '
                     'усами.\n'
                     'Подсказка 2: Раскрывает запутанные дела вроде «Убийства в Восточном экспрессе» с помощью '
                     '«маленьких серых клеточек» мозга.\n'
                     'Подсказка 3: Знаменитый герой 33 детективных романов Агаты Кристи.',
               'en': 'Clue 1: Dapper Belgian private detective with an egg-shaped head and impeccably waxed '
                     'moustaches.\n'
                     "Clue 2: Relies on psychology and order, methodically activating his 'little grey cells' to solve "
                     'impossible locked-room murders.\n'
                     "Clue 3: Celebrated sleuth created by Agatha Christie appearing in 33 novels including 'Murder on "
                     "the Orient Express'."},
  'options': {'uz': ['Erkul Puaro', 'Sherlok Xolms', 'Miss Marpl', 'Komissar Megre'],
              'ru': ['Эркюль Пуаро', 'Шерлок Холмс', 'Мисс Марпл', 'Комиссар Мегрэ'],
              'en': ['Hercule Poirot', 'Sherlock Holmes', 'Miss Marple', 'Inspector Maigret']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Erkul Puaro', 'ru': 'Эркюль Пуаро', 'en': 'Hercule Poirot'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Agatha_Christie.png/640px-Agatha_Christie.png',
  'fun_fact': {'uz': "Erkul Puaro 1975 yilda vafot etganida «New York Times» gazetasining bosh sahifasida ta'ziyanoma "
                     "chop etilgan yagona to'qima adabiy qahramondir.",
               'ru': 'Эркюль Пуаро — единственный вымышленный литературный персонаж, чей некролог появился на первой '
                     'полосе газеты The New York Times.',
               'en': 'Poirot is the only fictional character ever to receive a front-page obituary in The New York '
                     'Times (August 6, 1975).'},
  'aliases': ['erkul puaro', 'puaro', 'эркюль пуаро', 'пуаро', 'hercule poirot']},
 {'id': 'lit_char_062',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Sent-Meri-Mid qishlog'ida yolg'iz yashovchi, paypoq to'qishni va bog'dorchilikni "
                     "yaxshi ko'radigan qariya xonimman.\n"
                     '2-maslahat: Qishloq hayoti va inson tabiati haqidagi chuqur kuzatuvlarim orqali professional '
                     'politsiya yecholmagan qotilliklarni fosh qilaman.\n'
                     "3-maslahat: Agata Kristi tomonidan yaratilgan xushfe'l va ziyrak havaskor ayol izquvarman.",
               'ru': 'Подсказка 1: Пожилая незамужняя леди, вяжущая шерстяные вещи в тихой английской деревушке '
                     'Сент-Мэри-Мид.\n'
                     'Подсказка 2: Сравнивая мотивы преступников с бытовыми деревенскими сплетнями, раскрывает '
                     'сложнейшие загадки.\n'
                     'Подсказка 3: Знаменитая сыщица-любительница из произведений Агаты Кристи.',
               'en': 'Clue 1: Gentle elderly spinster residing in the quaint English hamlet of St. Mary Mead, fond of '
                     'knitting and gardening.\n'
                     'Clue 2: Cracks impenetrable murder cases by drawing razor-sharp parallels with ordinary village '
                     'human nature.\n'
                     'Clue 3: Beloved amateur consulting sleuth featured in 12 novels by Dame Agatha Christie.'},
  'options': {'uz': ['Erkul Puaro', 'Miss Jeyn Marpl', 'Iren Adler', 'Meri Morsten'],
              'ru': ['Эркюль Пуаро', 'Мисс Джейн Марпл', 'Ирен Адлер', 'Мэри Морстен'],
              'en': ['Hercule Poirot', 'Miss Jane Marple', 'Irene Adler', 'Mary Morstan']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Miss Jeyn Marpl', 'ru': 'Мисс Джейн Марпл', 'en': 'Miss Jane Marple'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Agatha_Christie.png/640px-Agatha_Christie.png',
  'fun_fact': {'uz': "Agata Kristi Miss Marpl obrazini o'z buvisi va uning qishloqdagi dugonalaridan ilhomlanib "
                     'yaratgan.',
               'ru': 'Агата Кристи говорила, что прообразом мисс Марпл послужила ее собственная бабушка.',
               'en': 'Christie stated that Miss Marple was inspired by her grandmother and her Victorian circle of '
                     'friends.'},
  'aliases': ['miss marpl', 'jeyn marpl', 'мисс марпл', 'miss marple']},
 {'id': 'lit_char_063',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Yorklik ingliz dengizchisi bo'lib, kema halokatidan so'ng kimsasiz yovvoyi orolga "
                     'tushib qolaman.\n'
                     "2-maslahat: Orolida 28 yil yashab, dehqonchilik qilaman, echki boqaman, loydan ko'zalar yasayman "
                     'va qutqargan yovvoyiga «Juma» deb ism beraman.\n'
                     "3-maslahat: Daniyel Defoning jahon sarguzasht adabiyoti poydevorini qo'ygan romani bosh "
                     'qahramoniman.',
               'ru': 'Подсказка 1: Моряк из Йорка, потерпевший кораблекрушение и выброшенный на необитаемый остров.\n'
                     'Подсказка 2: Прожил на острове 28 лет, обустроив быт, приручив диких коз и спасши туземца по '
                     'имени Пятница.\n'
                     'Подсказка 3: Главный герой эпохального приключенческого романа Даниэля Дефо.',
               'en': 'Clue 1: Mariner from York cast ashore on an uninhabited desert island near the Orinoco River '
                     'mouth.\n'
                     'Clue 2: Survived 28 years mastering agriculture, pottery, and shelter, eventually saving the '
                     'native youth Friday.\n'
                     "Clue 3: Title protagonist of Daniel Defoe's 1719 foundational work of realistic adventure "
                     'fiction.'},
  'options': {'uz': ['Juma', 'Gulliver', 'Robinzon Kruzo', 'Kapitan Nemo'],
              'ru': ['Пятница', 'Гулливер', 'Робинзон Крузо', 'Капитан Немо'],
              'en': ['Friday', 'Gulliver', 'Robinson Crusoe', 'Captain Nemo']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Robinzon Kruzo', 'ru': 'Робинзон Крузо', 'en': 'Robinson Crusoe'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Robinson_Crusoe_1719.jpg/640px-Robinson_Crusoe_1719.jpg',
  'fun_fact': {'uz': "Robinzon Kruzo prototipi shotlandiyalik dengizchi Aleksandr Selkirk bo'lib, u kimsasiz orolda 4 "
                     'yil yashagan.',
               'ru': 'Прототипом Крузо послужил шотландский боцман Александр Селькирк, проживший на необитаемом '
                     'острове более 4 лет.',
               'en': 'Defoe was inspired by real-life Scottish castaway Alexander Selkirk, who spent over four years '
                     'marooned on Más a Tierra.'},
  'aliases': ['robinzon kruzo', 'robinzon', 'робинзон крузо', 'робинзон', 'robinson crusoe']},
 {'id': 'lit_char_064',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Karib dengizidagi orolga odamxo'rlar tomonidan qurbonlikka keltirilgan yosh tubjoy "
                     'aborigenman.\n'
                     '2-maslahat: Oq tanli kemachi tomonidan qutqarilib, u bilan birga yashayman va u meni haftaning '
                     'men qutqarilgan kuni bilan ataydi.\n'
                     "3-maslahat: Robinzon Kruzoning eng sodiq do'sti va yordamchisi bo'lgan Daniyel Defo "
                     'qahramoniman.',
               'ru': 'Подсказка 1: Юноша-туземец, плененный людоедами и приговоренный к смерти на пустынном острове.\n'
                     'Подсказка 2: Спасен от гибели Робинзоном Крузо и назван в честь дня недели, когда обрел '
                     'свободу.\n'
                     'Подсказка 3: Верный спутник и преданный друг Робинзона Крузо в романе Даниэля Дефо.',
               'en': 'Clue 1: Young indigenous native captured by cannibals and marked for sacrifice on a deserted '
                     'beach.\n'
                     'Clue 2: Rescued by a castaway mariner who named him after the weekday on which his life was '
                     'saved.\n'
                     "Clue 3: Faithful companion and devoted friend to Robinson Crusoe in Daniel Defoe's novel."},
  'options': {'uz': ['Robinzon Kruzo', 'Kvikveg', 'Chinga', 'Juma (Friday)'],
              'ru': ['Робинзон Крузо', 'Квикег', 'Чингачгук', 'Пятница'],
              'en': ['Robinson Crusoe', 'Queequeg', 'Chingachgook', 'Friday']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Juma (Friday)', 'ru': 'Пятница', 'en': 'Friday'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Robinson_Crusoe_1719.jpg/640px-Robinson_Crusoe_1719.jpg',
  'fun_fact': {'uz': "«Mening jumam» iborasi ko'plab xalqlar tilida eng ishonchli va sadoqatli yordamchi ma'nosida "
                     'ishlatiladi.',
               'ru': 'Идиома «верный Пятница» (Man Friday) вошла в английский язык как обозначение надежного '
                     'помощника.',
               'en': "The idiom 'Man Friday' became standard English for an exceptionally loyal and indispensable "
                     'personal aide.'},
  'aliases': ['juma', 'пятница', 'friday']},
 {'id': 'lit_char_065',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Avval jarroh, keyin kema kapitani bo'lib, bir necha bor g'alati va afsonaviy "
                     'mamlakatlarga tushib qolaman.\n'
                     '2-maslahat: Kichkintoy liliputlar yurtida bahaybat dev, ulkan brobdingneglar yurtida esa '
                     'mittivoyga aylanaman.\n'
                     '3-maslahat: Jonatan Sviftning insoniyat jamiyati qusurlarini ayovsiz fosh etgan satirik '
                     'romanining bosh qahramoniman.',
               'ru': 'Подсказка 1: Английский судовой врач и путешественник, потерпевший крушение у неведомых '
                     'берегов.\n'
                     'Подсказка 2: Был великаном в стране лилипутов (Лилипутии) и крошечным карликом среди гигантов '
                     'Бробдингнега.\n'
                     'Подсказка 3: Главный герой всемирно известной сатирической тетралогии Джонатана Свифта.',
               'en': 'Clue 1: English ship surgeon whose ocean voyages led to extraordinary unknown realms.\n'
                     'Clue 2: A giant mountain-man among six-inch Lilliputians, and a fragile plaything in Brobdingnag '
                     'among 60-foot giants.\n'
                     "Clue 3: Traveler protagonist of Jonathan Swift's biting satirical masterpiece 'Gulliver's "
                     "Travels'."},
  'options': {'uz': ['Lemuel Gulliver', 'Robinzon Kruzo', 'Baron Myunxauzen', 'Sinbad'],
              'ru': ['Лемюэль Гулливер', 'Робинзон Крузо', 'Барон Мюнхгаузен', 'Синдбад-мореход'],
              'en': ['Lemuel Gulliver', 'Robinson Crusoe', 'Baron Munchausen', 'Sinbad']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Lemuel Gulliver', 'ru': 'Лемюэль Гулливер', 'en': 'Lemuel Gulliver'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Jonathan_Swift_by_Charles_Jervas_detail.jpg/640px-Jonathan_Swift_by_Charles_Jervas_detail.jpg',
  'fun_fact': {'uz': "Gulliver to'rtinchi sayohatida donishmand otlar (Guigngnmlar) va yovvoyi odamsimon maxluqlar "
                     '(Yaxular) yurtiga borib qoladi.',
               'ru': 'Свифт написал «Путешествия Гулливера» не как детскую сказку, а как острую политическую и '
                     'философскую сатиру на человечество.',
               'en': 'Swift wrote the book not as a fairy tale, but as a scathing political and philosophical '
                     'indictment of human folly.'},
  'aliases': ['gulliver', 'lemuel gulliver', 'гулливер', 'лемюэль гулливер']},
 {'id': 'lit_char_066',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Falsafa, tibbiyot, huquq va ilohiyotni o'rganib ham hayotning tub mohiyatini "
                     'topolmagan qari olimman.\n'
                     "2-maslahat: Cheksiz bilim va yoshlik evaziga o'z qonim bilan shayton Mefistofelga qalbimni "
                     'sotishga ahdnomaga imzo chekaman.\n'
                     "3-maslahat: «To'xta, ey lahza, sen naqadar go'zalsan!» degan, Gyotening monumental fojiasi bosh "
                     'qahramoniman.',
               'ru': 'Подсказка 1: Престарелый ученый, разочаровавшийся в книжной науке и жаждущий постичь сокровенную '
                     'тайну мироздания.\n'
                     'Подсказка 2: Заключает сделку с Мефистофелем, подписанную кровью, вернув себе молодость и любовь '
                     'прекрасной Гретхен.\n'
                     'Подсказка 3: Главный герой великой философской трагедии Иоганна Вольфганга Гёте.',
               'en': "Clue 1: Aging scholar exhausted by dry academia who laments knowing nothing of the cosmos's "
                     'beating heart.\n'
                     'Clue 2: Signed a pact in blood with the devil Mephistopheles in exchange for worldly youth, '
                     'passion, and boundless experience.\n'
                     "Clue 3: Protagonist of Johann Wolfgang von Goethe's monumental dramatic tragedy."},
  'options': {'uz': ['Mefistofel', 'Iogann Faust (Doktor Faust)', 'Vagner', 'Valentin'],
              'ru': ['Мефистофель', 'Иоганн Фауст (Доктор Фауст)', 'Вагнер', 'Валентин'],
              'en': ['Mephistopheles', 'Doctor Faust', 'Wagner', 'Valentin']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Iogann Faust (Doktor Faust)', 'ru': 'Иоганн Фауст (Доктор Фауст)', 'en': 'Doctor Faust'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Goethe_%28Stieler_1828%29.jpg/640px-Goethe_%28Stieler_1828%29.jpg',
  'fun_fact': {'uz': "Gyote «Faust» asarini yozishga butun umrini — 60 yildan ortiq vaqtini bag'ishlagan (1773-1831).",
               'ru': 'Гёте работал над созданием «Фауста» на протяжении шестидесяти лет, завершив его незадолго до '
                     'смерти.',
               'en': 'Goethe worked on Faust across six decades, completing Part Two shortly before his death in '
                     '1832.'},
  'aliases': ['faust', 'doktor faust', 'фауст', 'доктор фауст', 'doctor faust']},
 {'id': 'lit_char_067',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Xudo bilan olim inson qalbini yo'ldan ozdirish borasida samoviy bahs boylagan qora "
                     'kuchman.\n'
                     "2-maslahat: Qora pudel it qiyofasida paydo bo'lib, inkor ruhi va zaharxanda masxaralash "
                     'timsoliga aylanaman.\n'
                     '3-maslahat: Gyotening «Faust» asaridagi vasvasaga soluvchi iblis (shayton) timsoliman.',
               'ru': 'Подсказка 1: Дух вечного отрицания и сомнения, заключивший на небесах пари с Создателем о душе '
                     'человека.\n'
                     'Подсказка 2: Является Фаусту в облике черного пуделя и становится его циничным проводником по '
                     'земным искушениям.\n'
                     'Подсказка 3: Образ дьявола в бессмертной трагедии Иоганна Вольфганга Гёте «Фауст».',
               'en': 'Clue 1: Spirit of eternal negation who makes a wager with the Lord in Heaven regarding the '
                     'limits of human virtue.\n'
                     "Clue 2: Entered Faust's study in the guise of a black poodle, serving as his sardonic, worldly "
                     'tempter.\n'
                     "Clue 3: The cunning devil incarnate in Johann Wolfgang von Goethe's supreme drama 'Faust'."},
  'options': {'uz': ['Faust', 'Voland', 'Mefistofel', 'Lyusifer'],
              'ru': ['Фауст', 'Воланд', 'Мефистофель', 'Люцифер'],
              'en': ['Faust', 'Woland', 'Mephistopheles', 'Lucifer']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Mefistofel', 'ru': 'Мефистофель', 'en': 'Mephistopheles'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Goethe_%28Stieler_1828%29.jpg/640px-Goethe_%28Stieler_1828%29.jpg',
  'fun_fact': {'uz': "Mefistofel so'zlari: «Men hamisha yomonlikni istab, ezgulik yaratuvchi qudratning bir "
                     "bo'lagiman».",
               'ru': 'Мефистофель описывает себя как «часть той силы, что вечно хочет зла и вечно совершает благо».',
               'en': "Mephistopheles famously identifies himself as 'Part of that Power which would the Evil ever do, "
                     "and ever does the Good'."},
  'aliases': ['mefistofel', 'мефистофель', 'mephistopheles']},
 {'id': 'lit_char_068',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Dengiz ma'budasi Fetida va mirmodonlar shohi Peleyning yengilmas yarim ma'bud "
                     "o'g'liman.\n"
                     "2-maslahat: Onam meni Stiks daryosiga botirgan, faqat tovongina daxlsiz qolgan, do'stim "
                     "Patroklning qasosi uchun Gektorni o'ldiraman.\n"
                     '3-maslahat: Gomerning Troya urushi haqidagi mashhur «Iliada» dostonining eng markaziy '
                     'qahramoniman.',
               'ru': 'Подсказка 1: Величайший ахейский герой Троянской войны, сын морской богини Фетиды и царя Пелея.\n'
                     'Подсказка 2: Неуязвим для оружия везде, кроме пяты; сразил в поединке троянского царевича '
                     'Гектора, мстя за Патрокла.\n'
                     'Подсказка 3: Главный воин поэмы Гомера «Илиада», чей гнев воспевается в первой строке эпоса.',
               'en': 'Clue 1: Supreme Achaean warrior of the Trojan War, son of sea nymph Thetis and King Peleus.\n'
                     "Clue 2: Invulnerable everywhere except his heel; slew Hector outside Troy's walls to avenge his "
                     'beloved Patroclus.\n'
                     "Clue 3: Central epic champion whose destructive rage opens Homer's 'Iliad'."},
  'options': {'uz': ['Gektor', 'Odissey', 'Agamemnon', 'Axill (Axilles)'],
              'ru': ['Гектор', 'Одиссей', 'Агамемнон', 'Ахилл (Ахиллес)'],
              'en': ['Hector', 'Odysseus', 'Agamemnon', 'Achilles']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Axill (Axilles)', 'ru': 'Ахилл (Ахиллес)', 'en': 'Achilles'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Bust_Achilles_MAN_Napoli_inv9013.jpg/640px-Bust_Achilles_MAN_Napoli_inv9013.jpg',
  'fun_fact': {'uz': '«Axill tovoni» iborasi har qanday eng qudratli narsaning ham eng nozik va ojiz joyini anglatadi.',
               'ru': 'Крылатое выражение «ахиллесова пята» означает наиболее уязвимое место человека.',
               'en': "The idiom 'Achilles' heel' became universal shorthand for an individual's sole fatal "
                     'vulnerability.'},
  'aliases': ['axill', 'axilles', 'ахилл', 'ахиллес', 'achilles']},
 {'id': 'lit_char_069',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Itaka oroli hukmdori, aqlli va makkorligi tufayli «Troya oti» hiylasini o'ylab "
                     'topgan yunon sarkardasiman.\n'
                     "2-maslahat: Bir ko'zli siklop Polifemni ko'r qilib, maftunkor sirenalar va yovuz Sikilla va "
                     "Xaribdadan omon o'taman.\n"
                     "3-maslahat: Urushdan so'ng vatanimga qaytish uchun 10 yil dengizlarda sargardon bo'lgan Gomer "
                     'dostonining bosh qahramoniman.',
               'ru': 'Подсказка 1: Царь Итаки, многоопытный и хитроумный герой, придумавший уловку с Троянским конём.\n'
                     'Подсказка 2: Ослепил циклопа Полифема, избежал гибели от сирен, Сциллы и Харибды на пути к жене '
                     'Пенелопе.\n'
                     'Подсказка 3: Главный персонаж одноименной бессмертной эпической поэмы Гомера.',
               'en': 'Clue 1: Cunning King of Ithaca whose tactical mind devised the fall of Troy via the Trojan '
                     'Horse.\n'
                     'Clue 2: Blinded Polyphemus the Cyclops and defied Circe, Scylla, and the Sirens while striving '
                     'to reach Penelope.\n'
                     "Clue 3: Epic wanderer whose perilous ten-year journey home forms Homer's 'Odyssey'."},
  'options': {'uz': ['Odissey (Uliss)', 'Axill', 'Telemax', 'Menelay'],
              'ru': ['Одиссей (Улисс)', 'Ахилл', 'Телемах', 'Менелай'],
              'en': ['Odysseus (Ulysses)', 'Achilles', 'Telemachus', 'Menelaus']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Odissey (Uliss)', 'ru': 'Одиссей (Улисс)', 'en': 'Odysseus (Ulysses)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Head_Odysseus_MAR_Sperlonga.jpg/640px-Head_Odysseus_MAR_Sperlonga.jpg',
  'fun_fact': {'uz': "Odisseyning sadoqatli rafiqasi Penelopa 20 yil davomida uning qaytishini kutib, mato to'qish "
                     'hiylasi bilan sovchilarni aldab kelgan.',
               'ru': 'Пенелопа ткала саван и распускала его по ночам, чтобы оттянуть новый брак до возвращения мужа.',
               'en': 'Penelope stalled importunate suitors for years by secretly unweaving her shroud by candlelight '
                     'each night.'},
  'aliases': ['odissey', 'uliss', 'одиссей', 'улисс', 'odysseus']},
 {'id': 'lit_char_070',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Peterburg aslzodasi, dunyoviy hayot, ballar va ko'ngilxushliklardan bezor bo'lib "
                     '(«rus xandasi») qishloqqa borgan yigitman.\n'
                     "2-maslahat: Tatyana Larinaning samimiy sevgi izhorini rad etib, duelda shoir do'stim Lenskiyni "
                     "otib o'ldiraman.\n"
                     "3-maslahat: Aleksandr Pushkinning she'riy romanidagi «ortiqcha odam» (lishniy chelovek) "
                     'toifasiga kiruvchi bosh qahramoniman.',
               'ru': 'Подсказка 1: Петербургский денди, охваченный хандрой («русской тоской»), получивший наследство '
                     'дядюшки в деревне.\n'
                     'Подсказка 2: Высокомерно отверг письмо Татьяны, а позже убил на глупой дуэли своего юного '
                     'друга-поэта Ленского.\n'
                     'Подсказка 3: Главный персонаж одноименного бессмертного романа в стихах Александра Сергеевича '
                     'Пушкина.',
               'en': "Clue 1: World-weary St. Petersburg dandy overtaken by spleen, who retreats to his late uncle's "
                     'country estate.\n'
                     "Clue 2: Coldly rebuffed Tatyana Larina's impassioned love letter and fatally shot poet Lensky in "
                     'a foolish duel.\n'
                     "Clue 3: Titular 'superfluous man' of Alexander Pushkin's supreme novel in verse."},
  'options': {'uz': ['Vladimir Lenskiy', 'Yevgeniy Onegin', 'Grigoriy Pechorin', 'Andrey Bolkonskiy'],
              'ru': ['Владимир Ленский', 'Евгений Онегин', 'Григорий Печорин', 'Андрей Болконский'],
              'en': ['Vladimir Lensky', 'Eugene Onegin', 'Pechorin', 'Andrei Bolkonsky']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Yevgeniy Onegin', 'ru': 'Евгений Онегин', 'en': 'Eugene Onegin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/AleksandrPushkin.jpg/640px-AleksandrPushkin.jpg',
  'fun_fact': {'uz': 'Belinskiy Pushkinning «Yevgeniy Onegin» asarini «rus hayotining ensiklopediyasi» deb yuqori '
                     'baholagan.',
               'ru': 'Критик Белинский назвал роман «Евгений Онегин» подлинной «энциклопедией русской жизни».',
               'en': "Vissarion Belinsky famously characterized Pushkin's Eugene Onegin as an 'encyclopedia of Russian "
                     "life'."},
  'aliases': ['yevgeniy onegin', 'onegin', 'евгений онегин', 'онегин', 'eugene onegin']},
 {'id': 'lit_char_071',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Fransuzcha ishqiy romanlarni o'qib, tabiat qo'ynida yolg'izlikni xush ko'ruvchi "
                     'qishloqi aslzoda qizman.\n'
                     '2-maslahat: «Men sizga yozmoqdaman — yana nima deyishim mumkin?» deb Oneginga yuragimni ochib '
                     "maktub yo'llayman.\n"
                     "3-maslahat: Oxirida generalning xotini bo'lgach, «Men boshqaga berilganman va umrbod unga "
                     "vafodor bo'laman» degan Pushkin asari qahramoniman.",
               'ru': 'Подсказка 1: Задумчивая и мечтательная дворянская девушка из провинции, воспитанная на '
                     'сентиментальных романах.\n'
                     'Подсказка 2: Написала знаменитое искреннее письмо с признанием: «Я к вам пишу — чего же '
                     'боле?..».\n'
                     'Подсказка 3: «Милый идеал» Пушкина в романе «Евгений Онегин», оставшаяся верной мужу-генералу.',
               'en': 'Clue 1: Introspective country maiden raised on French romance novels, living close to nature.\n'
                     "Clue 2: Penned the iconic vulnerable confession: 'I write to you — what more is there to say?'.\n"
                     "Clue 3: Pushkin's 'dearest ideal' in 'Eugene Onegin' who later resolves: 'I am given to another; "
                     "to him I will be faithful forever'."},
  'options': {'uz': ['Olga Larina', 'Natasha Rostova', 'Tatyana Larina', 'Anna Karenina'],
              'ru': ['Ольга Ларина', 'Наташа Ростова', 'Татьяна Ларина', 'Анна Каренина'],
              'en': ['Olga Larina', 'Natasha Rostova', 'Tatyana Larina', 'Anna Karenina']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Tatyana Larina', 'ru': 'Татьяна Ларина', 'en': 'Tatyana Larina'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/AleksandrPushkin.jpg/640px-AleksandrPushkin.jpg',
  'fun_fact': {'uz': 'Tatyana obrazi rus adabiyotida ayollik sadoqati, axloqiy poklik va ruhiy qudratning eng yuksak '
                     'timsolidir.',
               'ru': 'Татьяна Ларина стала первообразом русской нравственно безупречной женщины в литературе XIX века.',
               'en': 'Tatyana Larina became the archetype of moral nobility and emotional resilience in 19th-century '
                     'fiction.'},
  'aliases': ['tatyana larina', 'tatyana', 'татьяна ларина', 'татьяна', 'tatyana']},
 {'id': 'lit_char_072',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Kavkazga xizmatga yuborilgan yosh, o'tkir aql-idrokli, ammo hayotdan bezor bo'lgan "
                     'rus zobitiman.\n'
                     "2-maslahat: Merining sevgisini o'yinchoq qilaman, duelda Grushnitskiyni o'ldiraman va knyajna "
                     "Belaning o'limiga sababchi bo'laman.\n"
                     '3-maslahat: Mixail Lermontovning mashhur «Zamonamiz qahramoni» romanidagi ziddiyatli va hissiz '
                     'bosh qahramonman.',
               'ru': 'Подсказка 1: Офицер на Кавказе, наделенный сильной волей и блестящим умом, но глубоко '
                     'разочарованный во всем.\n'
                     'Подсказка 2: Разрушает судьбы влюбленной Бэлы и княжны Мэри, безжалостно убивает Грушницкого на '
                     'дуэли.\n'
                     'Подсказка 3: Главный персонаж психологического романа Михаила Лермонтова «Герой нашего времени».',
               'en': 'Clue 1: Brilliant yet cynical Russian officer stationed in the Caucasus, plagued by existential '
                     'apathy.\n'
                     'Clue 2: Toys with Princess Mary, brings tragedy to the Circassian girl Bela, and shoots '
                     'Grushnitsky in a duel on a cliff.\n'
                     "Clue 3: Disaffected antihero of Mikhail Lermontov's landmark psychological novel 'A Hero of Our "
                     "Time'."},
  'options': {'uz': ['Maksim Maksimich', 'Yevgeniy Onegin', 'Yunkir Grushnitskiy', 'Grigoriy Pechorin'],
              'ru': ['Максим Максимыч', 'Евгений Онегин', 'Юнкер Грушницкий', 'Григорий Печорин'],
              'en': ['Maksim Maksimych', 'Eugene Onegin', 'Grushnitsky', 'Grigory Pechorin']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Grigoriy Pechorin', 'ru': 'Григорий Печорин', 'en': 'Grigory Pechorin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Mikhail_Lermontov_by_Zabolotskiy.jpg/640px-Mikhail_Lermontov_by_Zabolotskiy.jpg',
  'fun_fact': {'uz': 'Lermontov kitob muqaddimasida Pechorin «bir avlodning butun qusurlaridan tarkib topgan portret» '
                     'ekanini yozgan.',
               'ru': 'Лермонтов указал в предисловии: «Герой Нашего Времени — портрет, составленный из пороков всего '
                     'нашего поколения».',
               'en': "Lermontov prefaced the book stating Pechorin was 'a portrait composed of all the vices of our "
                     "generation'."},
  'aliases': ['grigoriy pechorin', 'pechorin', 'григорий печорин', 'печорин', 'pechorin']},
 {'id': 'lit_char_073',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Knyaz Nikolay Bolkonskiyning shon-shuhrat orzusidagi mag'rur va yuksak aql sohibi "
                     "bo'lgan o'g'liman.\n"
                     "2-maslahat: Austerlits jangida qo'lda bayroq bilan yaralanib, cheksiz ko'k osmonga termulib "
                     "shuhratning bema'niligini anglayman.\n"
                     "3-maslahat: Natasha Rostovaga ko'ngil qo'ygan, Borodino jangida og'ir yaralanib vafot etgan Lev "
                     'Tolstoyning «Urush va tinchlik» qahramoniman.',
               'ru': 'Подсказка 1: Гордый аристократ, сын старого князя Николая Андреевича, мечтавший о славе '
                     'наподобие наполеоновской.\n'
                     'Подсказка 2: Раненый при Аустерлице со знаменем в руках, глядит в высокое бесконечное небо и '
                     'переосмысливает жизнь.\n'
                     'Подсказка 3: Жених Наташи Ростовой, смертельно раненный при Бородино в эпопее Льва Толстого '
                     '«Война и мир».',
               'en': 'Clue 1: Proud, intellectual prince striving for military renown in emulation of Napoleon '
                     'Bonaparte.\n'
                     'Clue 2: Wounded clutching a standard at Austerlitz, gazing into the vast tranquil sky to '
                     'perceive the emptiness of glory.\n'
                     "Clue 3: Tragic aristocrat engaged to Natasha Rostova, mortally wounded at Borodino in Tolstoy's "
                     "'War and Peace'."},
  'options': {'uz': ['Knyaz Andrey Bolkonskiy', 'Pyer Bezuxov', 'Nikolay Rostov', 'Anatol Kuragin'],
              'ru': ['Князь Андрей Болконский', 'Пьер Безухов', 'Николай Ростов', 'Анатоль Курагин'],
              'en': ['Prince Andrei Bolkonsky', 'Pierre Bezukhov', 'Nikolai Rostov', 'Anatole Kuragin']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Knyaz Andrey Bolkonskiy', 'ru': 'Князь Андрей Болконский', 'en': 'Prince Andrei Bolkonsky'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/L.N.Tolstoy_Prokudin-Gorsky.jpg/640px-L.N.Tolstoy_Prokudin-Gorsky.jpg',
  'fun_fact': {'uz': "Andrey Bolkonskiyning keksa eman daraxti bilan bog'liq ruhiy yangilanish epizodi jahon "
                     'adabiyotidagi mashhur psixologik sahnalardan biridir.',
               'ru': 'Встречи князя Андрея с вековым дубом на пути в Отрадное символизируют увядание и весеннее '
                     'возрождение его души.',
               'en': "Andrei's encounters with the ancient oak tree symbolize the cycles of desolation and spiritual "
                     'rejuvenation.'},
  'aliases': ['andrey bolkonskiy', 'knyaz bolkonskiy', 'андрей болконский', 'andrei bolkonsky']},
 {'id': 'lit_char_074',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Graf Rostovning xushchaqchaq, qalbga to'la, musiqaga va hayotga oshiq qiziman.\n"
                     '2-maslahat: Birinchi katta balimda Andrey Bolkonskiy bilan vals tushaman, keyinroq Anatol '
                     'Kuragin vasvasasiga aldanaman.\n'
                     "3-maslahat: Moskva yonayotganida yarador askarlarga aravachalarni bo'shatib bergan, Lev "
                     'Tolstoyning «Urush va tinchlik» bosh ayol qahramoniman.',
               'ru': 'Подсказка 1: Обаятельная, искренняя и непосредственная графиня, воплощение радости жизни и '
                     'поэзии юности.\n'
                     'Подсказка 2: Танцует свой первый бал с князем Андреем, но едва не разрушает счастье увлечением '
                     'Анатолем Курагиным.\n'
                     'Подсказка 3: Главная героиня романа-эпопеи Льва Толстого «Война и мир», ставшая женой Пьера '
                     'Безухова.',
               'en': 'Clue 1: Spontaneous, radiant young countess overflowing with musical grace and pure zest for '
                     'life.\n'
                     'Clue 2: Danced her breathtaking debut ball with Prince Andrei before nearly ruining her life '
                     'over Anatole Kuragin.\n'
                     "Clue 3: Enduring heroine of Leo Tolstoy's 'War and Peace' who ultimately finds domestic harmony "
                     'with Pierre Bezukhov.'},
  'options': {'uz': ['Knyajna Marya Bolkonskaya', 'Natasha Rostova', 'Helen Kuragina', 'Sonya Rostova'],
              'ru': ['Марья Болконская', 'Наташа Ростова', 'Элен Курагина', 'Соня Ростова'],
              'en': ['Princess Marya', 'Natasha Rostova', 'Hélène Kuragina', 'Sonya']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Natasha Rostova', 'ru': 'Наташа Ростова', 'en': 'Natasha Rostova'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/L.N.Tolstoy_Prokudin-Gorsky.jpg/640px-L.N.Tolstoy_Prokudin-Gorsky.jpg',
  'fun_fact': {'uz': "Lev Tolstoy Natasha obrazini yaratishda o'z rafiqasi Sofya Andreyevna va uning singlisi Tatyana "
                     'Bersdan andoza olgan.',
               'ru': 'Прототипами Наташи Ростовой были жена писателя Софья Андреевна и ее младшая сестра Татьяна Берс.',
               'en': 'Tolstoy fashioned Natasha from composite traits of his wife Sophia and her younger sister '
                     'Tatyana Behrs.'},
  'aliases': ['natasha rostova', 'natasha', 'наташа ростова', 'наташа', 'natasha rostova']},
 {'id': 'lit_char_075',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Keksa graf Bezuxovning noqonuniy o'g'li bo'lib, to'satdan ulkan boylik va graf "
                     "unvoniga ega bo'laman.\n"
                     "2-maslahat: Masonlik, falsafa va ezgulik izlayman, 1812 yilda Napoleonni o'ldirmoqchi bo'lib "
                     'frantsuzlarga asirga tushaman.\n'
                     '3-maslahat: Asirlikda Platon Karatayev orqali oddiy hayot donoligini anglagan Lev Tolstoyning '
                     '«Urush va tinchlik» bosh qahramoniman.',
               'ru': 'Подсказка 1: Незаконнорожденный сын графа Безухова, внезапно ставший обладателем огромного '
                     'состояния.\n'
                     'Подсказка 2: Искренний правдоискатель, увлекавшийся масонством, пытавшийся убить Наполеона в '
                     'пылающей Москве.\n'
                     'Подсказка 3: Главный мыслитель и искатель истины в эпопее Льва Толстого «Война и мир».',
               'en': 'Clue 1: Illegitimate son of Count Bezukhov unexpectedly inheriting vast wealth and aristocratic '
                     'rank.\n'
                     'Clue 2: Searcher after moral purpose through Freemasonry, arrested in burning Moscow while '
                     "plotting Napoleon's assassination.\n"
                     "Clue 3: Philosophical spiritual hero of Leo Tolstoy's 'War and Peace' transformed by fellow "
                     'prisoner Platon Karataev.'},
  'options': {'uz': ['Andrey Bolkonskiy', 'Nikolay Rostov', 'Pyer Bezuxov', 'Vasiliy Kuragin'],
              'ru': ['Андрей Болконский', 'Николай Ростов', 'Пьер Безухов', 'Василий Курагин'],
              'en': ['Andrei Bolkonsky', 'Nikolai Rostov', 'Pierre Bezukhov', 'Vasili Kuragin']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Pyer Bezuxov', 'ru': 'Пьер Безухов', 'en': 'Pierre Bezukhov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/L.N.Tolstoy_Prokudin-Gorsky.jpg/640px-L.N.Tolstoy_Prokudin-Gorsky.jpg',
  'fun_fact': {'uz': "Pyer Bezuxov o'zida Tolstoyning shaxsiy ma'naviy izlanishlarini eng ko'p aks ettirgan "
                     'avtobiografik xarakterdir.',
               'ru': 'Пьер выражает сокровенные духовные и философские искания самого Льва Толстого.',
               'en': "Pierre serves as Tolstoy's primary philosophical surrogate, voicing the author's deepest "
                     'spiritual inquiries.'},
  'aliases': ['pyer bezuxov', 'pyer', 'пьер безухов', 'пьер', 'pierre bezukhov']},
 {'id': 'lit_char_076',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Peterburg yuqori tabaqa xonimi, nufuzli davlat amaldori Aleksey Kareninning '
                     'rafiqasiman.\n'
                     "2-maslahat: Yosh ofitser Aleksey Vronskiyga aqldan ozdiruvchi ehtiros bilan oshiq bo'lib, "
                     "o'g'lim Seryojadan va dunyoviy jamiyatdan voz kechaman.\n"
                     "3-maslahat: Rashk, yolg'izlik va jamiyat la'natiga dosh berolmay temir yo'l vagoni ostiga o'zini "
                     'tashlagan Lev Tolstoy fojiasi qahramoniman.',
               'ru': 'Подсказка 1: Блестящая петербургская светская дама, жена высокопоставленного сановника Алексея '
                     'Каренина.\n'
                     'Подсказка 2: Жертвует сыном и репутацией ради всепоглощающей страсти к молодому офицеру '
                     'Вронскому.\n'
                     'Подсказка 3: Трагическая героиня романа Льва Толстого, бросившаяся под поезд на станции '
                     'Обираловка.',
               'en': 'Clue 1: Elegant St. Petersburg high-society matron wed to rigid government minister Alexei '
                     'Karenin.\n'
                     'Clue 2: Surrendered social standing and access to her beloved son for an all-consuming affair '
                     'with Count Vronsky.\n'
                     "Clue 3: Doomed heroine of Leo Tolstoy's 1878 tragic masterpiece who ends her torment under a "
                     'rushing train.'},
  'options': {'uz': ['Dolli Oblonskaya', 'Kitti Shcherbatskaya', 'Betsi Tverskaya', 'Anna Karenina'],
              'ru': ['Долли Облонская', 'Кити Щербацкая', 'Бетси Тверская', 'Анна Каренина'],
              'en': ['Dolly Oblonskaya', 'Kitty Shcherbatskaya', 'Betsy Tverskaya', 'Anna Karenina']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Anna Karenina', 'ru': 'Анна Каренина', 'en': 'Anna Karenina'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/L.N.Tolstoy_Prokudin-Gorsky.jpg/640px-L.N.Tolstoy_Prokudin-Gorsky.jpg',
  'fun_fact': {'uz': 'Tolstoy romanning epigrafini Muqaddas Kitobdan olgan: «Qasos Menikidir va Men qasos olaman».',
               'ru': 'Эпиграф к роману «Мне отмщение, и Аз воздам» задает глубокий христианский смысл трагедии '
                     'героини.',
               'en': "The biblical epigraph 'Vengeance is mine, I will repay' sets the moral complexity of Anna's "
                     'tragedy.'},
  'aliases': ['anna karenina', 'анна каренина']},
 {'id': 'lit_char_077',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Brichkada sayohat qiluvchi, o'zini yoqimli va odobli kollej maslahatchisi qilib "
                     "ko'rsatuvchi uddaburon janobman.\n"
                     "2-maslahat: Aholini qayta ro'yxatga olishdan oldin vafot etgan, ammo qog'ozda tirik hisoblangan "
                     'krepostnoy dehqonlarni sotib olaman.\n'
                     "3-maslahat: Nikolay Gogolning «O'lik jonlar» nomli she'riy roman-poemasidagi firibgar bosh "
                     'qahramonman.',
               'ru': 'Подсказка 1: Предприимчивый господин средней руки, коллежский советник, разъезжающий в бричке с '
                     'кучером Селифаном.\n'
                     'Подсказка 2: Скупает у окрестных помещиков умерших крепостных крестьян («мертвые души»), '
                     'числящихся живыми по ревизии.\n'
                     'Подсказка 3: Главный персонаж поэмы Николая Васильевича Гоголя «Мёртвые души».',
               'en': 'Clue 1: Middle-aged collegial councillor traveling town-to-town in a modest carriage with '
                     'servant Petrushka.\n'
                     "Clue 2: Concocts a scheme to purchase deceased serfs ('dead souls') still legally documented on "
                     'the tax census.\n'
                     "Clue 3: Ambitious swindler protagonist of Nikolai Gogol's 1842 satirical prose epic 'Dead "
                     "Souls'."},
  'options': {'uz': ['Pavel Ivanovich Chichikov', 'Nozdryov', 'Sobakevich', 'Manilov'],
              'ru': ['Павел Иванович Чичиков', 'Ноздрёв', 'Собакевич', 'Манилов'],
              'en': ['Pavel Ivanovich Chichikov', 'Nozdryov', 'Sobakevich', 'Manilov']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Pavel Ivanovich Chichikov',
                     'ru': 'Павел Иванович Чичиков',
                     'en': 'Pavel Ivanovich Chichikov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Nikolai_Gogol.jpg/640px-Nikolai_Gogol.jpg',
  'fun_fact': {'uz': "Gogolga «O'lik jonlar» syujetini Aleksandr Pushkin sovg'a qilgan bo'lib, o'sha paytda janubiy "
                     "viloyatlarda bunday firibgarliklar ro'y bergan edi.",
               'ru': 'Сюжет о скупке мертвых душ Гоголю подсказал А. С. Пушкин, узнавший о подобной реальной афере.',
               'en': 'Alexander Pushkin provided Gogol with the plot premise based on true fraudulent speculation in '
                     'dead serfs.'},
  'aliases': ['chichikov', 'pavel ivanovich chichikov', 'чичиков', 'павел иванович чичиков']},
 {'id': 'lit_char_078',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Zaporojye Sechining qari, qaysar va jangari kazak polkovnigiman.\n'
                     "2-maslahat: Ikki o'g'lim — Ostap va Andriyni kiyev akademiyasidan olib urushga tashlayman, "
                     "dushman polyak qiziga oshiq bo'lgan o'g'limni o'z qo'lim bilan otib o'ldiraman.\n"
                     "3-maslahat: «Men seni dunyoga keltirdim, men seni o'ldiraman!» degan so'zlar bilan mashhur "
                     'Nikolay Gogol qissasi qahramoniman.',
               'ru': 'Подсказка 1: Старый суровый запорожский полковник, для которого война и Сечь — единственный '
                     'смысл бытия.\n'
                     'Подсказка 2: Карает смертью младшего сына Андрия за измену казачеству ради прекрасной польской '
                     'панночки.\n'
                     'Подсказка 3: Главный богатырь одноименной исторической повести Николая Гоголя «Тарас Бульба».',
               'en': 'Clue 1: Fierce, veteran Zaporozhian Cossack colonel who considers war and the Sich the sole '
                     'manly domain.\n'
                     'Clue 2: Executed his younger son Andriy with his own musket after the youth defected for love of '
                     'a Polish noblewoman.\n'
                     "Clue 3: Indomitable Cossack patriarch immortalized in Nikolai Gogol's historical epic 'Taras "
                     "Bulba'."},
  'options': {'uz': ['Ostap Bulba', 'Taras Bulba', 'Andriy Bulba', 'Kukubenko'],
              'ru': ['Остап Бульба', 'Тарас Бульба', 'Андрий Бульба', 'Кукубенко'],
              'en': ['Ostap Bulba', 'Taras Bulba', 'Andriy Bulba', 'Kukubenko']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Taras Bulba', 'ru': 'Тарас Бульба', 'en': 'Taras Bulba'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Nikolai_Gogol.jpg/640px-Nikolai_Gogol.jpg',
  'fun_fact': {'uz': "Taras Bulbaning o't ichida turib o'z quroldoshlariga yo'l ko'rsatgan qahramonona o'lim sahnasi "
                     'dostonnamo ruhda yozilgan.',
               'ru': 'Фраза Тараса «Я тебя породил, я тебя и убью!» стала одной из самых знаменитых в славянской '
                     'культуре.',
               'en': "Bulba's line 'I gave you life, and I will take it away!' became an indelible folkloric quote."},
  'aliases': ['taras bulba', 'тарас бульба']},
 {'id': 'lit_char_079',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Peterburgda Goroxovaya ko'chasida xalat kiyib divandan turmay yotuvchi помещик (yer "
                     'egasi) dvoryanman.\n'
                     "2-maslahat: Faol do'stim Shtolts va sevgilim Olga Ilinskayaning harakatlariga qaramay, "
                     "harakatsizlik va orom olamimni afzal ko'raman.\n"
                     "3-maslahat: Rus jamiyatidagi yalqovlik va ruhiy turg'unlikni anglatuvchi «oblomovchilik» "
                     'atamasini keltirib chiqargan Goncharov romani qahramoniman.',
               'ru': 'Подсказка 1: Помещик-дворянин, проводящий все дни лежа на диване в халате в квартире на '
                     'Гороховой улице.\n'
                     'Подсказка 2: Не способен преодолеть апатию даже ради любви Ольги Ильинской и дружеских '
                     'увещеваний деятельного Штольца.\n'
                     'Подсказка 3: Главный герой романа Ивана Гончарова, породивший понятие «обломовщина».',
               'en': 'Clue 1: Affluent young gentleman spending entire weeks reclining on his divan in an oriental '
                     'dressing gown.\n'
                     'Clue 2: Incapable of purposeful action despite the prodding of industrious friend Stolz and the '
                     'love of Olga Ilyinskaya.\n'
                     "Clue 3: Titular indolent antihero of Ivan Goncharov's novel whose name inspired the sociological "
                     "term 'Oblomovism'."},
  'options': {'uz': ['Andrey Shtolts', 'Zaxar', 'Ilya Ilyich Oblomov', 'Tarantyev'],
              'ru': ['Андрей Штольц', 'Захар', 'Илья Ильич Обломов', 'Тарантьев'],
              'en': ['Andrei Stolz', 'Zakhar', 'Ilya Ilyich Oblomov', 'Tarantyev']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Ilya Ilyich Oblomov', 'ru': 'Илья Ильич Обломов', 'en': 'Ilya Ilyich Oblomov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ivan_Goncharov.jpg/640px-Ivan_Goncharov.jpg',
  'fun_fact': {'uz': 'Tanqidchi Dobrolyubovning «Oblomovchilik nima?» maqolasi 19-asr rus ijtimoiy fikrida inqilobiy '
                     'aks-sado bergan.',
               'ru': 'Статья критика Добролюбова «Что такое обломовщина?» стала классикой русской литературной '
                     'критики.',
               'en': "Dobrolyubov's essay 'What Is Oblomovism?' established the character as a devastating indictment "
                     'of feudal inertia.'},
  'aliases': ['oblomov', 'ilya oblomov', 'обломов', 'илья ильич обломов']},
 {'id': 'lit_char_080',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: «Buyuk kombinator» laqabli, pul topishning 400 ta qonuniy usulini biladigan '
                     'jozibador firibgarman.\n'
                     "2-maslahat: Kisa Vorobyaninov bilan birga olmoslar yashirilgan o'n ikkita stulni qidirib butun "
                     "Sovet Ittifoqi bo'ylab sarguzasht kechiraman.\n"
                     '3-maslahat: Rio-de-Janeyroga oq shimlarda ketishni orzu qilgan Ilf va Petrov romanlarining '
                     'mashhur bosh qahramoniman.',
               'ru': 'Подсказка 1: «Великий комбинатор», знающий «четыреста сравнительно честных способов отъема '
                     'денег».\n'
                     'Подсказка 2: Охотится за драгоценностями мадам Петуховой, зашитыми в один из 12 стульев '
                     'орехового гарнитура.\n'
                     'Подсказка 3: Бессмертный остроумный авантюрист из сатирических романов И. Ильфа и Е. Петрова.',
               'en': "Clue 1: 'The Great Combinator', a charming rogue who boasts four hundred relatively honest "
                     'methods of acquiring money.\n'
                     "Clue 2: Teaming with Kisa Vorobyaninov to track down Madame Petukhova's family jewels hidden "
                     'inside one of twelve chairs.\n'
                     "Clue 3: Irrepressible con artist protagonist of Ilf and Petrov's classic Soviet satires 'The "
                     "Twelve Chairs' and 'The Golden Calf'."},
  'options': {'uz': ['Kisa Vorobyaninov', 'Shura Balaganov', 'Panikovskiy', 'Ostap Bender'],
              'ru': ['Киса Воробьянинов', 'Шура Балаганов', 'Паниковский', 'Остап Бендер'],
              'en': ['Kisa Vorobyaninov', 'Shura Balaganov', 'Panikovsky', 'Ostap Bender']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ostap Bender', 'ru': 'Остап Бендер', 'en': 'Ostap Bender'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Ostap_Bender_sculpture_Saint_Petersburg.jpg/640px-Ostap_Bender_sculpture_Saint_Petersburg.jpg',
  'fun_fact': {'uz': "Ostap Bender sarguzashtlari o'zbek tiliga ham mohirona tarjima qilingan bo'lib, uning yuzlab "
                     'iqtiboslari xalq orasida maqolga aylangan.',
               'ru': 'Фразы Бендера («Командовать парадом буду я!», «Лед тронулся») разошлись на миллионы цитат.',
               'en': "Bender's aphorisms ('Gentlemen of the jury, the ice is broken!') became foundational "
                     'catchphrases of Eastern European satire.'},
  'aliases': ['ostap bender', 'bender', 'остап бендер', 'бендер']},
 {'id': 'lit_char_081',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Ilgari ko'chadagi daydi it edim, professor Preobrajenskiy menga inson gipofiz bezi "
                     "va urug'donini ko'chirib o'tkazadi.\n"
                     "2-maslahat: Odob-axloqsiz, balalayka chaluvchi va daydi mushuklarni bo'g'ib yo'qotuvchi bo'lim "
                     'mudiriga aylanaman.\n'
                     '3-maslahat: Mixail Bulgakovning shafqatsiz satirik asari «It yuragi»ning shov-shuvli gibrid '
                     'qahramoniman.',
               'ru': 'Подсказка 1: Дворовый пес Шарик, которому профессор Преображенский пересадил гипофиз и семенники '
                     'погибшего дебошира Клима Чугункина.\n'
                     'Подсказка 2: Превращается в хама, пьяницу и заведующего подотделом очистки города от бродячих '
                     'котов.\n'
                     'Подсказка 3: Заглавный антигерой сатирической повести Михаила Булгакова «Собачье сердце».',
               'en': 'Clue 1: Stray mongrel dog transformed into a human through an experimental pituitary and gonadal '
                     'transplant performed by Professor Preobrazhensky.\n'
                     'Clue 2: Adopted coarse habits, plays the balalaika, and became head of the Moscow Sub-Department '
                     'for Purging Stray Animals.\n'
                     "Clue 3: Grotesque antihero of Mikhail Bulgakov's biting anti-Soviet satire 'Heart of a Dog'."},
  'options': {'uz': ['Poligraf Poligrafovich Sharikov', 'Professor Preobrajenskiy', 'Doktor Bormental', 'Shvonder'],
              'ru': ['Полиграф Полиграфович Шариков', 'Профессор Преображенский', 'Доктор Борменталь', 'Швондер'],
              'en': ['Poligraf Poligrafovich Sharikov', 'Professor Preobrazhensky', 'Dr. Bormenthal', 'Shvonder']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Poligraf Poligrafovich Sharikov',
                     'ru': 'Полиграф Полиграфович Шариков',
                     'en': 'Poligraf Poligrafovich Sharikov'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Mikhail_Bulgakov_1928.jpg/640px-Mikhail_Bulgakov_1928.jpg',
  'fun_fact': {'uz': "Sharikovning «Hammayoqni tortib olib, teng bo'lib berish kerak» degan fikri bo'sh populizmning "
                     'timsoliga aylangan.',
               'ru': 'Шариков стал нарицательным символом воинствующего невежества, люмпенской наглости и хамства.',
               'en': 'Sharikov became an indelible literary emblem of militant ignorance and totalitarian '
                     'lumpen-proletarian vulgarity.'},
  'aliases': ['sharikov', 'poligraf sharikov', 'шариков', 'полиграф полиграфович']},
 {'id': 'lit_char_082',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Aslida Hindiston shahzodasi Dakkar bo'lib, Britaniya mustamlakachilariga qarshi "
                     "kurashda oilasini yo'qotganman.\n"
                     "2-maslahat: Insoniyat jamiyatidan voz kechib, «Nautilus» nomli mo''jizaviy suvosti kemasida "
                     "okeanlar qa'rida erkin yashayman.\n"
                     '3-maslahat: Jyul Vernning «Suv ostida 20 000 lye» va «Sirli orol» romanlarining daho, sirli bosh '
                     'qahramoniman.',
               'ru': 'Подсказка 1: Индийский принц Даккар, поднявший восстание сипаев против британцев и потерявший '
                     'жену и детей.\n'
                     'Подсказка 2: Создал фантастическую подводную лодку «Наутилус», на которой бороздит океанские '
                     'глубины, уйдя от цивилизации.\n'
                     'Подсказка 3: Загадочный и благородный капитан в романах Жюля Верна «Двадцать тысяч лье под '
                     'водой» и «Таинственный остров».',
               'en': 'Clue 1: Indian Prince Dakkar who lost family and kingdom after leading the Sepoy Rebellion '
                     'against British rule.\n'
                     'Clue 2: Renounced corrupt human civilization and sailed the oceanic depths aboard the advanced '
                     'electric submarine Nautilus.\n'
                     "Clue 3: Enigmatic polymath captain of Jules Verne's 'Twenty Thousand Leagues Under the Sea' and "
                     "'The Mysterious Island'."},
  'options': {'uz': ['Kapitan Grant', 'Kapitan Nemo', 'Fileas Fogg', 'Professor Aronaks'],
              'ru': ['Капитан Грант', 'Капитан Немо', 'Филеас Фогг', 'Профессор Аронакс'],
              'en': ['Captain Grant', 'Captain Nemo', 'Phileas Fogg', 'Professor Aronnax']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Kapitan Nemo', 'ru': 'Капитан Немо', 'en': 'Captain Nemo'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Captain_Nemo_Riou.jpg/640px-Captain_Nemo_Riou.jpg',
  'fun_fact': {'uz': "«Nemo» so'zi lotinchada «Hech kim» degan ma'noni anglatadi — bu Odisseyning Siklop Polifemga "
                     'aytgan nomiga ishoradir.',
               'ru': 'Имя «Немо» на латыни означает «Никто» — прямая отсылка к ответу Одиссея циклопу Полифему.',
               'en': "Latin for 'Nobody', Nemo echoes Odysseus' clever trick against the Cyclops Polyphemus."},
  'aliases': ['kapitan nemo', 'nemo', 'капитан немо', 'немо', 'captain nemo']},
 {'id': 'lit_char_083',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Londonning «Reform-klub» a'zosi bo'lgan juda intizomli, sovuqqon va daqiqamatn "
                     'ingliz jentlmeniman.\n'
                     "2-maslahat: Klubdoshlarim bilan 20 000 funt sterlingga bahslashib, o'sha davr uchun rekord "
                     'muddatda yer yuzini aylanib chiqishga otlanaman.\n'
                     '3-maslahat: Yangi xizmatkorim Paspartu bilan sayohatga chiqqan Jyul Vernning «80 kunda olam '
                     "bo'ylab» romani qahramoniman.",
               'ru': 'Подсказка 1: Педантичный и хладнокровный лондонский джентльмен, член аристократического '
                     '«Реформ-клуба».\n'
                     'Подсказка 2: Заключает пари на 20 тысяч фунтов, что сумеет обогнуть земной шар за восемьдесят '
                     'дней.\n'
                     'Подсказка 3: Главный герой приключенческого романа Жюля Верна «Вокруг света за 80 дней».',
               'en': "Clue 1: Impeccably punctual, unflappable English gentleman belonging to London's exclusive "
                     'Reform Club.\n'
                     'Clue 2: Wagered half his £40,000 fortune that modern steam technology allowed circling the globe '
                     'in eighty days.\n'
                     "Clue 3: Dauntless globetrotter of Jules Verne's 1872 adventure classic 'Around the World in "
                     "Eighty Days'."},
  'options': {'uz': ['Jan Paspartu', 'Inspektor Fiks', 'Fileas Fogg', 'Kapitan Nemo'],
              'ru': ['Жан Паспарту', 'Инспектор Фикс', 'Филеас Фогг', 'Капитан Немо'],
              'en': ['Jean Passepartout', 'Inspector Fix', 'Phileas Fogg', 'Captain Nemo']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Fileas Fogg', 'ru': 'Филеас Фогг', 'en': 'Phileas Fogg'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Jules_Verne_by_Nadar_1878.jpg/640px-Jules_Verne_by_Nadar_1878.jpg',
  'fun_fact': {'uz': 'Fogg vaqt mintaqalari (sharqqa harakatlanish) hisobiga bir kun yutganini bilmay poygani '
                     "yutqazdim deb o'ylagan edi.",
               'ru': 'Фогг выиграл пари благодаря тому, что двигался на восток и пересек линию перемены дат, выиграв '
                     'сутки.',
               'en': 'Fogg unwittingly gained a calendar day by traveling eastward across international time '
                     'boundaries.'},
  'aliases': ['fileas fogg', 'fogg', 'филеас фогг', 'фогг', 'phileas fogg']},
 {'id': 'lit_char_084',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Afrika qirg'og'ida halok bo'lgan ingliz lordi Greystokning o'rmonda yetim qolgan "
                     "chaqalog'iman.\n"
                     '2-maslahat: Maymunlar malikasi Kala tomonidan boqib tarbiyalanib, lianalarda uchuvchi vahshiy '
                     "o'rmonlar hukmdoriga aylanaman.\n"
                     '3-maslahat: Jeyn Porterni sevib insoniy madaniyatga qaytgan, Edgar Rays Berrouzning mashhur '
                     'personajiman.',
               'ru': 'Подсказка 1: Сын английского лорда Грейстока, потерявший родителей во младенчестве в джунглях '
                     'Африки.\n'
                     'Подсказка 2: Воспитан гигантской обезьяной Калой и стал непревзойденным владыкой диких '
                     'джунглей.\n'
                     'Подсказка 3: Легендарный герой приключенческих романов Эдгара Райса Берроуза, полюбивший Джейн '
                     'Портер.',
               'en': 'Clue 1: Orphaned infant heir of Lord and Lady Greystoke stranded on the equatorial African '
                     'coast.\n'
                     'Clue 2: Adopted and nurtured by the great ape Kala, growing into the feral king of the African '
                     'canopy.\n'
                     "Clue 3: Edgar Rice Burroughs' iconic jungle lord who falls in love with Jane Porter."},
  'options': {'uz': ['Maugli', 'Robinzon Kruzo', 'Kinan', 'Tarzan (Jon Kleyton)'],
              'ru': ['Маугли', 'Робинзон Крузо', 'Конан', 'Тарзан (Джон Клейтон)'],
              'en': ['Mowgli', 'Robinson Crusoe', 'Conan', 'Tarzan (John Clayton)']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Tarzan (Jon Kleyton)', 'ru': 'Тарзан (Джон Клейтон)', 'en': 'Tarzan (John Clayton)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tarzan_First_Edition.jpg/640px-Tarzan_First_Edition.jpg',
  'fun_fact': {'uz': "Tarzan maymunlar tilida «Oq teri» ma'nosini bildiradi.",
               'ru': 'На языке человекообразных обезьян Берроуза имя «Тарзан» буквально означает «Белокожий».',
               'en': "In Burroughs' fictional Great Ape language, the name 'Tarzan' translates literally as "
                     "'White-Skin'."},
  'aliases': ['tarzan', 'тарзан', 'john clayton', 'greystoke']},
 {'id': 'lit_char_085',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Hindiston changalzorlarida yo'qolib qolib, Sioniya bo'rilari to'dasi tomonidan asrab "
                     'olingan inson bolasiman.\n'
                     "2-maslahat: Qora pantera Bagira, ayiq Balu va bo'g'ma ilon Kaa mening ustozlarim va sadoqatli "
                     "do'stlarimdir.\n"
                     "3-maslahat: Qonxo'r yo'lbars Sherxonga «Qizil gul» (olov) bilan qarshi chiqqan Redyard "
                     'Kiplingning «Jungli kitobi» bosh qahramoniman.',
               'ru': 'Подсказка 1: Индийский мальчик («лягушонок»), потерявшийся в джунглях и принятый в волчью стаю '
                     'Акелы.\n'
                     'Подсказка 2: Обучен закону джунглей медведем Балу, пантерой Багирой и мудрым питоном Каа.\n'
                     'Подсказка 3: Главный герой сказочных повестей Редьярда Киплинга «Книга джунглей», одолевший '
                     'тигра Шер-Хана.',
               'en': 'Clue 1: Indian man-cub lost in the Seoni forests and adopted into the wolf pack of Mother Wolf '
                     'and Akela.\n'
                     'Clue 2: Tutored in the Law of the Jungle by Baloo the bear, Bagheera the panther, and Kaa the '
                     'rock python.\n'
                     "Clue 3: Rudyard Kipling's feral child hero of 'The Jungle Book' who brought the Red Flower to "
                     'vanquish Shere Khan.'},
  'options': {'uz': ['Maugli', 'Tarzan', 'Kim', 'Hoshimjon'],
              'ru': ['Маугли', 'Тарзан', 'Ким', 'Хошимжон'],
              'en': ['Mowgli', 'Tarzan', 'Kim', 'Hoshimjon']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Maugli', 'ru': 'Маугли', 'en': 'Mowgli'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Rudyard_Kipling_by_John_Collier_1891.jpg/640px-Rudyard_Kipling_by_John_Collier_1891.jpg',
  'fun_fact': {'uz': "Kipling «Jungli qonuni» orqali tabiat bilan inson uyg'unligi va birdamlik tamoyillarini go'zal "
                     'badiiy tilda ifodalagan.',
               'ru': 'Слова «Мы с тобой одной крови — ты и я!» стали всемирно известным гимном дружбы и верности.',
               'en': "The Jungle Master Word 'We be of one blood, ye and I' became an international symbol of "
                     'kinship.'},
  'aliases': ['maugli', 'mowgli', 'маугли']},
 {'id': 'lit_char_086',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Shervud o'rmonida yashovchi, yashil kiyim kiygan, kamondan o'q otishda tengsiz "
                     'merganman.\n'
                     "2-maslahat: Kichik Jon, Rohib Tuk va o'rmon yigitlari bilan boylardan tortib olib, "
                     "kambag'allarga ulashaman.\n"
                     "3-maslahat: Nottingem sherifiga qarshi kurashgan o'rta asr ingliz xalq balladalarining afsonaviy "
                     'olijanob qaroqchisi bosh qahramoniman.',
               'ru': 'Подсказка 1: Легендарный предводитель вольных стрелков, скрывающийся в Шервудском лесу в зеленом '
                     'плаще.\n'
                     'Подсказка 2: Меткий стрелок из лука, который отбирает золото у богатых феодалов и раздает его '
                     'беднякам.\n'
                     'Подсказка 3: Благородный разбойник из средневековых английских народных баллад, враг шерифа '
                     'Ноттингемского.',
               'en': 'Clue 1: Legendary green-clad outlaw archer holding court beneath the canopy of Sherwood Forest.\n'
                     'Clue 2: Steals from tyrannical Norman barons and greedy clergy to distribute coin to the '
                     'destitute peasantry.\n'
                     'Clue 3: Folk hero of English medieval ballads perpetually outwitting the Sheriff of Nottingham.'},
  'options': {'uz': ['Vilgelm Tell', 'Robin Gud', 'Ayvengo', 'Qirol Artur'],
              'ru': ['Вильгельм Телль', 'Робин Гуд', 'Айвенго', 'Король Артур'],
              'en': ['William Tell', 'Robin Hood', 'Ivanhoe', 'King Arthur']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Robin Gud', 'ru': 'Робин Гуд', 'en': 'Robin Hood'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Robin_Hood_statue%2C_Nottingham.jpg/640px-Robin_Hood_statue%2C_Nottingham.jpg',
  'fun_fact': {'uz': 'Robin Gud afsonasi 13-asrdan buyon adabiyot, musiqa va kinoda adolat va tenglikning bosh timsoli '
                     'sifatida yashab kelmoqda.',
               'ru': 'Памятник Робин Гуду установлен у стен Ноттингемского замка в Англии.',
               'en': 'A bronze statue of Robin Hood drawing his longbow stands outside Nottingham Castle.'},
  'aliases': ['robin gud', 'robin hood', 'робин гуд']},
 {'id': 'lit_char_087',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Boshi qipiqqa to'la, asalni dunyodagi eng totli ne'mat deb biladigan xushchaqchaq "
                     'ayiqchaman.\n'
                     "2-maslahat: Yuz akrlik o'rmonda Cho'chqacha (Pyatachok), Eshakcha (Ia-Ia) va Quyi bilan "
                     'qiziqarli voqealarni boshdan kechiraman.\n'
                     "3-maslahat: A.A. Milnning o'g'li Kristofer Robin uchun to'qigan ertaklarining bosh qahramoniman.",
               'ru': 'Подсказка 1: Плюшевый медвежонок с опилками в голове, обожающий мед и сочиняющий шумелки и '
                     'ворчалки.\n'
                     'Подсказка 2: Живет в Чудесном лесу с Пятачком, осликом Иа-Иа, Кроликом и Совой.\n'
                     'Подсказка 3: Главный персонаж всемирно любимых детских сказок Алана Александра Милна.',
               'en': "Clue 1: 'Bear of Very Little Brain' with an insatiable appetite for 'hunny' and a habit of "
                     'humming little hums.\n'
                     'Clue 2: Lives in the Hundred Acre Wood alongside Piglet, Eeyore, Rabbit, and Owl.\n'
                     'Clue 3: Lovable stuffed bear created by A.A. Milne for his young son Christopher Robin.'},
  'options': {'uz': ['Pyatachok', 'Ia-Ia', 'Vinni-Pux', 'Paddington'],
              'ru': ['Пятачок', 'Иа-Иа', 'Винни-Пух', 'Паддингтон'],
              'en': ['Piglet', 'Eeyore', 'Winnie-the-Pooh', 'Paddington Bear']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Vinni-Pux', 'ru': 'Винни-Пух', 'en': 'Winnie-the-Pooh'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/A_A_Milne_with_Christopher_Robin_and_Pooh_Bear.jpg/640px-A_A_Milne_with_Christopher_Robin_and_Pooh_Bear.jpg',
  'fun_fact': {'uz': "Vinni-Pux haqiqiy qora ayiq Vinnipeg sharafiga nomlangan bo'lib, Miln va uning o'g'li uni London "
                     "hayvonot bog'ida ko'rgan edilar.",
               'ru': 'Медвежонок получил имя от реальной канадской медведицы Виннипег из лондонского зоопарка.',
               'en': 'Milne named the character after Winnipeg, an orphaned black bear at London Zoo.'},
  'aliases': ['vinni-pux', 'vinni pux', 'винни-пух', 'винни пух', 'winnie-the-pooh']},
 {'id': 'lit_char_088',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: B-612 asteroidida yashovchi, uchta vulqoni va injiq go'zal atirguli bor tillarang "
                     'sochli bolaman.\n'
                     "2-maslahat: Sahroda samolyoti qulagan uchuvchi bilan uchrashib, undan qo'zichoq rasmini chizib "
                     "berishni so'rayman.\n"
                     "3-maslahat: «Faqat qalb bilangina aniq ko'rish mumkin, eng muhim narsa ko'zga ko'rinmaydi» degan "
                     'Antuan de Sent-Ekzyuperi falsafiy ertagining bosh qahramoniman.',
               'ru': 'Подсказка 1: Златовласый мальчик с крошечного астероида Б-612, где растут три вулкана и '
                     'прекрасная капризная Роза.\n'
                     'Подсказка 2: Встречает в пустыне Сахара потерпевшего крушение летчика и просит: «Нарисуй мне '
                     'барашка».\n'
                     'Подсказка 3: Главный герой трогательной философской сказки-притчи Антуана де Сент-Экзюпери.',
               'en': 'Clue 1: Golden-haired child inhabiting asteroid B-612 with three knee-high volcanoes and a '
                     'beloved vain rose.\n'
                     "Clue 2: Encountered a stranded aviator in the Sahara Desert, immediately greeting him with 'Draw "
                     "me a sheep!'.\n"
                     "Clue 3: Philosophical title wanderer of Antoine de Saint-Exupéry's globally translated lyrical "
                     'fable.'},
  'options': {'uz': ['Uchuvchi', 'Tulki', 'Qirol', 'Kichkina shahzoda'],
              'ru': ['Лётчик', 'Лис', 'Король', 'Маленький принц'],
              'en': ['The Aviator', 'The Fox', 'The King', 'The Little Prince']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Kichkina shahzoda', 'ru': 'Маленький принц', 'en': 'The Little Prince'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Antoine_de_Saint-Exup%C3%A9ry.jpg/640px-Antoine_de_Saint-Exup%C3%A9ry.jpg',
  'fun_fact': {'uz': "«Kichkina shahzoda» dunyoda Bibliyadan keyin eng ko'p tillarga (500 dan ortiq til va shevalarga) "
                     'tarjima qilingan kitobdir.',
               'ru': '«Маленький принц» переведен более чем на 500 языков и диалектов, уступая по этому показателю '
                     'только Библии.',
               'en': 'Translated into over 500 languages and dialects, it is the most translated non-religious book in '
                     'the world.'},
  'aliases': ['kichkina shahzoda', 'маленький принц', 'the little prince']},
 {'id': 'lit_char_089',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Yoz faslida daryo bo'yida jiyalak kiyib ketayotgan cho'ntak soatli Oq Quyon ortidan "
                     'quyon iniga sakragan qizchaman.\n'
                     '2-maslahat: «Meni ich» va «Meni ye» yozuvlari tufayli kattalashib-kichrayaman, Cheshir mushugi '
                     'va Jinni shlyapadoz bilan choy ichaman.\n'
                     "3-maslahat: Lyuis Kerrollning mantiqsizlik va fantastikaga boy «Mo''jizalar mamlakatidagi "
                     'sarguzashtlar» kitobi bosh qahramoniman.',
               'ru': 'Подсказка 1: Любознательная девочка, побежавшая за Белым Кроликом с карманными часами и '
                     'провалившаяся в кроличью нору.\n'
                     'Подсказка 2: Пьет безумный чай с Безумным Шляпником и Мартовским Зайцем, встречает Чеширского '
                     'кота и играет в крикет с Королевой.\n'
                     'Подсказка 3: Главная героиня сказок Льюиса Кэрролла «Алиса в Стране чудес» и «Алиса в '
                     'Зазеркалье».',
               'en': 'Clue 1: Inquisitive Victorian schoolgirl tumbling down a rabbit hole after a waistcoat-wearing '
                     'White Rabbit.\n'
                     'Clue 2: Shrinks and expands with magic pastries, attends a Mad Tea-Party, and chats with the '
                     'grinning Cheshire Cat.\n'
                     "Clue 3: Lewis Carroll's intrepid young heroine exploring Wonderland and the Looking-Glass "
                     'world.'},
  'options': {'uz': ['Alisa', 'Doroti Geyl', 'Vendi Darling', 'Meri Poppins'],
              'ru': ['Алиса', 'Дороти Гейл', 'Венди Дарлинг', 'Мэри Поппинс'],
              'en': ['Alice', 'Dorothy Gale', 'Wendy Darling', 'Mary Poppins']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Alisa', 'ru': 'Алиса', 'en': 'Alice'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Lewis_Carroll_1863.jpg/640px-Lewis_Carroll_1863.jpg',
  'fun_fact': {'uz': 'Ertak haqiqiy 10 yoshli qizaloq Alisa Liddell iltimosiga binoan Oksford professori Charlz '
                     "Dodjson tomonidan to'qilgan.",
               'ru': 'Кэрролл сочинил эту сказку во время лодочной прогулки по Темзе для десятилетней Алисы Лидделл.',
               'en': 'Carroll invented the tale on a July boating expedition along the Isis for ten-year-old Alice '
                     'Liddell.'},
  'aliases': ['alisa', 'alice', 'алиса']},
 {'id': 'lit_char_090',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Yog'och xodadan usta Karlo (yoki Jepetto) tomonidan yo'nib yasalgan, burni uzun "
                     "bo'lgan yog'och qo'g'irchoq bolaman.\n"
                     "2-maslahat: Yolg'on gapirsam burnim cho'zilib ketadi; Oltin kalitni izlab Ahmoqlar maydoni va "
                     'Qoplonlar yurtida sarguzashtlarga duch kelaman.\n'
                     "3-maslahat: Karlo Kollodi va Aleksey Tolstoy ertaklarining mashhur sho'x yog'och qahramoniman.",
               'ru': 'Подсказка 1: Деревянный мальчик с длинным носом, выструганный из говорящего полена мастером '
                     'Джеппетто (папой Карло).\n'
                     'Подсказка 2: Его нос растет при каждой лжи; в поисках счастья и Золотого ключика спасается от '
                     'кота Базилио и лисы Алисы.\n'
                     'Подсказка 3: Знаменитый герой сказок Карло Коллоди (Пиноккио) и Алексея Толстого (Буратино).',
               'en': 'Clue 1: Living wooden puppet carved from an unruly piece of pine by woodcarver Geppetto (or Papa '
                     'Carlo).\n'
                     'Clue 2: His nose lengthens whenever he tells a fib; sought a golden key and dreamed of becoming '
                     'a real boy.\n'
                     'Clue 3: Immortal wooden marionette created by Carlo Collodi and reimagined by Aleksey Tolstoy.'},
  'options': {'uz': ['Pero', 'Pinokkio (Buratino)', 'Arlekin', 'Chipollino'],
              'ru': ['Пьеро', 'Пиноккио (Буратино)', 'Арлекин', 'Чиполлино'],
              'en': ['Pierrot', 'Pinocchio (Buratino)', 'Harlequin', 'Cipollino']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Pinokkio (Buratino)', 'ru': 'Пиноккио (Буратино)', 'en': 'Pinocchio (Buratino)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Carlo_Collodi.jpg/640px-Carlo_Collodi.jpg',
  'fun_fact': {'uz': "Kollodining asl ertagida Pinokkio qiyin axloqiy sinovlardan o'tib, fidoyiligi evaziga haqiqiy "
                     'tirik insonga aylanadi.',
               'ru': 'Имя «Буратино» происходит от итальянского слова burattino, означающего «деревянная '
                     'кукла-марионетка».',
               'en': "The name Buratino originates from the Italian theatrical term 'burattino' meaning wooden "
                     'puppet.'},
  'aliases': ['pinokkio', 'buratino', 'пиноккио', 'буратино', 'pinocchio']},
 {'id': 'lit_char_091',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Hech qachon ulg'ayishni istamaydigan, sehrli parilar changi yordamida uchishni "
                     "biladigan o'g'il bolaman.\n"
                     "2-maslahat: Netlandiya (Neverland) sehrli orolida yo'qolgan bolalar bilan yashayman va Qora "
                     'Soqolli Kapitan Kryuk bilan jang qilaman.\n'
                     '3-maslahat: J.M. Barrining mashhur bolalar pyesasi va ertagining bosh qahramoniman.',
               'ru': 'Подсказка 1: Летающий мальчик, который наотрез отказался взрослеть, убежав из дома в '
                     'Кенсингтонские сады.\n'
                     'Подсказка 2: Обитает на волшебном острове Нетинебудет (Neverland) с феей Динь-Динь и сражается с '
                     'пиратом Капитаном Крюком.\n'
                     'Подсказка 3: Бессмертный персонаж сказочных книг и пьес шотландского писателя Джеймса Барри.',
               'en': 'Clue 1: Mischievous boy who can fly and stubbornly refuses to grow up, having escaped to '
                     'Kensington Gardens.\n'
                     'Clue 2: Leads the Lost Boys on the island of Neverland alongside fairy Tinker Bell, battling '
                     'Captain Hook.\n'
                     "Clue 3: Ageless hero of J.M. Barrie's beloved classic play and novel 'Peter and Wendy'."},
  'options': {'uz': ['Kapitan Kryuk', 'Jon Darling', 'Piter Pen', 'Maykl Darling'],
              'ru': ['Капитан Крюк', 'Джон Дарлинг', 'Питер Пэн', 'Майкл Дарлинг'],
              'en': ['Captain Hook', 'John Darling', 'Peter Pan', 'Michael Darling']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Piter Pen', 'ru': 'Питер Пэн', 'en': 'Peter Pan'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Peter_pan_statue_kensington_gardens.jpg/640px-Peter_pan_statue_kensington_gardens.jpg',
  'fun_fact': {'uz': 'J.M. Barri Piter Pen asarlaridan tushgan barcha mualliflik huquqi gonorarlarini London bolalar '
                     'kasalxonasiga (Great Ormond Street Hospital) vasiyat qilgan.',
               'ru': 'Джеймс Барри передал все авторские права на Питера Пэна детской больнице Great Ormond Street в '
                     'Лондоне.',
               'en': 'Barrie gifted all copyright royalties from Peter Pan in perpetuity to the Great Ormond Street '
                     'Hospital for Children.'},
  'aliases': ['piter pen', 'peter pan', 'питер пэн']},
 {'id': 'lit_char_092',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Londonning ziqna, toshbag'ir va sovuq naqd puldor sudxo'riman; Rojdestvoni "
                     "bema'nilik («Humbug!») deb atayman.\n"
                     "2-maslahat: Bayram kechasi vafot etgan sherigim Marli va o'tmish, bugun, kelajakning uchta "
                     'Rojdestvo ruhi ziyoratimga keladi.\n'
                     "3-maslahat: Dahshatli qabr toshimni ko'rib tavba qilgan, Charlz Dikkensning «Rojdestvo "
                     "qo'shig'i» asari qahramoniman.",
               'ru': 'Подсказка 1: Бессердечный лондонский скряга и ростовщик, ненавидящий праздники и кричащий '
                     '«Чепуха!» (Bah! Humbug!).\n'
                     'Подсказка 2: В сочельник его посещают духи Прошлого, Настоящего и Будущего Рождества, показывая '
                     'его одинокую гибель.\n'
                     'Подсказка 3: Преобразившийся в щедрого благодетеля герой повести Чарльза Диккенса '
                     '«Рождественская песнь».',
               'en': 'Clue 1: Squeezing, grasping, cold-hearted London moneylender dismissing Christmas cheer with '
                     "'Bah! Humbug!'.\n"
                     'Clue 2: Visited on Christmas Eve by the chain-bound ghost of Jacob Marley followed by three '
                     'spectral Spirits of Christmas.\n'
                     "Clue 3: Redeemed miser protagonist of Charles Dickens' immortal festive classic 'A Christmas "
                     "Carol'."},
  'options': {'uz': ['Bob Kretchit', 'Yakob Marli', 'Fezzivig', 'Ebenezer Skruj'],
              'ru': ['Боб Крэтчит', 'Джейкоб Марли', 'Феззивиг', 'Эбенезер Скрудж'],
              'en': ['Bob Cratchit', 'Jacob Marley', 'Fezziwig', 'Ebenezer Scrooge']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Ebenezer Skruj', 'ru': 'Эбенезер Скрудж', 'en': 'Ebenezer Scrooge'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Dickens_Gurney_head.jpg/640px-Dickens_Gurney_head.jpg',
  'fun_fact': {'uz': 'Dikkens ushbu qissasi orqali butun dunyoda Rojdestvoning mehr-oqibat va xayriya bayrami sifatida '
                     "qayta tug'ilishiga sababchi bo'lgan.",
               'ru': 'Имя Скруджа стало нарицательным синонимом скряги, вдохновив создание персонажа Скруджа Макдака.',
               'en': "Scrooge's name became universal English slang for a miser and directly inspired Disney's Scrooge "
                     'McDuck.'},
  'aliases': ['ebenezer skruj', 'skruj', 'эбенезер скрудж', 'скрудж', 'ebenezer scrooge']},
 {'id': 'lit_char_093',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Mehnat uyida tug'ilib, doimiy ochlikda ulg'aygan yetim bolaman; «Iltimos, janob, "
                     "yana ozgina bering» deb bo'tqa so'rayman.\n"
                     "2-maslahat: London ko'chalarida Fegin boshchiligidagi yosh cho'ntakkesarlar to'dasi tuzog'iga "
                     'tushib qolaman.\n'
                     '3-maslahat: Charlz Dikkensning Angliyadagi shafqatsiz bolalar ekspluatatsiyasini fosh etgan '
                     'mashhur romanining bosh qahramoniman.',
               'ru': 'Подсказка 1: Сирота из работного дома, осмелившийся робко попросить лишнюю миску каши: '
                     '«Пожалуйста, сэр, я хочу еще».\n'
                     'Подсказка 2: Сбегает в Лондон и попадает в преступное логово старого скупщика краденого Феджина '
                     'и карманника Доджера.\n'
                     'Подсказка 3: Главный герой знаменитого воспитательного романа Чарльза Диккенса.',
               'en': "Clue 1: Workhouse-born parish orphan who famously dared to ask: 'Please, sir, I want some "
                     "more'.\n"
                     'Clue 2: Escaped to London only to be trapped into the juvenile pickpocket gang run by the '
                     'sinister Fagin.\n'
                     "Clue 3: Enduring title orphan hero of Charles Dickens' 1838 social novel 'Oliver Twist'."},
  'options': {'uz': ['Oliver Tvist', 'Artful Dodger', 'Devid Kopperfild', 'Fegin'],
              'ru': ['Оливер Твист', 'Ловкий Плут', 'Дэвид Копперфильд', 'Фейгин'],
              'en': ['Oliver Twist', 'The Artful Dodger', 'David Copperfield', 'Fagin']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Oliver Tvist', 'ru': 'Оливер Твист', 'en': 'Oliver Twist'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Dickens_Gurney_head.jpg/640px-Dickens_Gurney_head.jpg',
  'fun_fact': {'uz': '«Oliver Tvist» romani Buyuk Britaniya parlamentida bolalar mehnati va qashshoqlik qonunlarini '
                     'isloh qilishga turtki bergan.',
               'ru': 'Публикация романа вызвала волну общественных дебатов и ускорила реформу системы работных домов в '
                     'Англии.',
               'en': 'Publication sparked national moral outrage that hastened the reform of Victorian child labor '
                     'laws.'},
  'aliases': ['oliver tvist', 'oliver twist', 'оливер твист']},
 {'id': 'lit_char_094',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Missisipi bo'yidagi Sankt-Peterburg shaharchasida xolam Polli qo'lida "
                     "tarbiyalanuvchi sho'x bolaman.\n"
                     "2-maslahat: Devor oqlash jazosini tengdoshlarimga zavqli ish deb ko'rsatib, ulardan olma va "
                     "o'yinchoqlar undirib olaman.\n"
                     "3-maslahat: Bekki Tetcherga oshiq bo'lgan, Mark Tvenning jahon bolalar adabiyoti durdonasi bosh "
                     'qahramoniman.',
               'ru': 'Подсказка 1: Неугомонный мальчишка-проказник из городка на реке Миссисипи, воспитываемый тетей '
                     'Полли.\n'
                     'Подсказка 2: Превратил наказание в виде побелки забора в прибыльный бизнес, получив от мальчишек '
                     'яблоки и дохлую крысу.\n'
                     'Подсказка 3: Главный герой приключенческого шедевра Марка Твена.',
               'en': 'Clue 1: Spirited, imaginative mischief-maker living with his long-suffering Aunt Polly in St. '
                     'Petersburg, Missouri.\n'
                     'Clue 2: Convinced neighborhood boys that whitewashing a fence was an artistic privilege, trading '
                     'turns for trinkets.\n'
                     "Clue 3: Adventurous protagonist of Mark Twain's 1876 classic 'The Adventures of Tom Sawyer'."},
  'options': {'uz': ['Geklberri Finn', 'Tom Soyer', 'Sid Soyer', 'Jo Garper'],
              'ru': ['Гекльберри Финн', 'Том Сойер', 'Сид Сойер', 'Джо Гарпер'],
              'en': ['Huckleberry Finn', 'Tom Sawyer', 'Sid Sawyer', 'Joe Harper']},
  'correct_index': 1,
  'correct_answer': {'uz': 'Tom Soyer', 'ru': 'Том Сойер', 'en': 'Tom Sawyer'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mark_Twain_by_AF_Bradley.jpg/640px-Mark_Twain_by_AF_Bradley.jpg',
  'fun_fact': {'uz': "Mark Tven o'zining barcha bolalik xotiralari va Missisipi daryosi bo'yidagi do'stlarini Tom "
                     'Soyer sarguzashtlarida jamlagan.',
               'ru': 'Эпизод с покраской забора вошел в учебники менеджмента и психологии как пример мотивации.',
               'en': 'The whitewashing episode became a textbook psychological illustration of reframing labor into '
                     'play.'},
  'aliases': ['tom soyer', 'tom sawyer', 'том сойер']},
 {'id': 'lit_char_095',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Daydi ichkilikbozning o'g'li bo'lib, bochkada uxlaydigan, maktab va kiyimlarni yomon "
                     "ko'radigan erkin bolaman.\n"
                     "2-maslahat: Qochqin qora tanli qul Jim bilan birgalikda solda Missisipi daryosi oqimi bo'ylab "
                     'erkinlik sari suzaman.\n'
                     '3-maslahat: Ernest Xeminguey: «Zamonaviy Amerika adabiyoti bitta kitobdan — uning '
                     'sarguzashtlaridan boshlangan» deb aytgan personajman.',
               'ru': 'Подсказка 1: Сын местного пьяницы, вольный бродяга, предпочитающий спать в пустой бочке и не '
                     'знающий правил этикета.\n'
                     'Подсказка 2: Сбегает на плоту по реке Миссисипи вместе с беглым чернокожим рабом Джимом в '
                     'поисках свободы.\n'
                     'Подсказка 3: Главный герой великого романа Марка Твена, заложившего основы современной '
                     'американской литературы.',
               'en': 'Clue 1: Free-spirited son of the town drunkard who sleeps in hogsheads and rejects polite '
                     "'sivilization'.\n"
                     'Clue 2: Floated down the mighty Mississippi River on a wooden raft alongside runaway slave Jim.\n'
                     "Clue 3: Narrator hero of Mark Twain's masterpiece, heralded by Hemingway as the origin of all "
                     'modern American fiction.'},
  'options': {'uz': ['Tom Soyer', 'Qul Jim', 'Geklberri Finn', 'Pap Finn'],
              'ru': ['Том Сойер', 'Негр Джим', 'Гекльберри Финн', 'Папаша Финн'],
              'en': ['Tom Sawyer', 'Jim', 'Huckleberry Finn', 'Pap Finn']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Geklberri Finn', 'ru': 'Гекльберри Финн', 'en': 'Huckleberry Finn'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mark_Twain_by_AF_Bradley.jpg/640px-Mark_Twain_by_AF_Bradley.jpg',
  'fun_fact': {'uz': "Gek Finn o'z vijdoni va o'sha davr qonunlari o'rtasida tanlov qilib, do'sti Jimni qullikka "
                     "sotmaslik uchun «Mayli, do'zaxga ketaman!» deydi.",
               'ru': 'Моральная победа Гека выражена в его решимости спасти друга: «Ну что ж, пойду тогда в ад!» — '
                     'одна из вершин мировой прозы.',
               'en': "Huck's crisis of conscience ('All right, then, I'll go to hell!') marks a supreme moral climax "
                     'in world literature.'},
  'aliases': ['geklberri finn', 'gek finn', 'huckleberry finn', 'гекльберри финн', 'гек финн']},
 {'id': 'lit_char_096',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Qattiqqo'l Lovud maktab-internatida azob bilan katta bo'lgan, tashqi ko'rinishi "
                     'sodda yetim qizman.\n'
                     "2-maslahat: Tornfild qasrida kichik qizchaga tarbiyachi (governess) bo'lib ishga kirib, uning "
                     "qahrli xo'jayini Edvard Rochesterga oshiq bo'laman.\n"
                     "3-maslahat: Sharlotta Brontening ayol mustaqilligi, vijdoni va tenglik g'oyalarini kuylagan "
                     'klassik romani bosh qahramoniman.',
               'ru': 'Подсказка 1: Неприметная сирота с несгибаемым характером, пережившая суровые лишения в Ловудском '
                     'приюте.\n'
                     'Подсказка 2: Устраивается гувернанткой в поместье Торнфилд и влюбляется в загадочного мистера '
                     'Рочестера.\n'
                     'Подсказка 3: Главная героиня автобиографического романа Шарлотты Бронте о женской независимости '
                     'и чистой любви.',
               'en': 'Clue 1: Resolute, plain orphan who survived abuse at Gateshead Hall and brutal austerity at '
                     'Lowood School.\n'
                     'Clue 2: Became a governess at Thornfield Hall and fell passionately in love with the brooding '
                     'master Edward Rochester.\n'
                     "Clue 3: Indomitable heroine of Charlotte Brontë's revolutionary 1847 bildungsroman 'Jane Eyre'."},
  'options': {'uz': ['Berta Meyson', 'Keti Ernsho', 'Adel Varens', 'Jeyn Eyr'],
              'ru': ['Берта Мейсон', 'Кэтрин Эрншо', 'Адель Варанс', 'Джейн Эйр'],
              'en': ['Bertha Mason', 'Catherine Earnshaw', 'Adèle Varens', 'Jane Eyre']},
  'correct_index': 3,
  'correct_answer': {'uz': 'Jeyn Eyr', 'ru': 'Джейн Эйр', 'en': 'Jane Eyre'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Charlotte_Bront%C3%AB_by_George_Richmond.jpg/640px-Charlotte_Bront%C3%AB_by_George_Richmond.jpg',
  'fun_fact': {'uz': "Jeyn Eyr adabiyot tarixida go'zalligi bilan emas, balki chuqur ma'naviy kuchi, aqli va axloqiy "
                     'prinsiplari bilan sevilgan ilk ayol qahramonlardandir.',
               'ru': 'Шарлотта Бронте доказала, что героиня может быть некрасивой, но обладать богатейшим внутренним '
                     'миром и достоинством.',
               'en': 'Charlotte Brontë pioneered the literary convention of a heroine who is physically plain yet '
                     'morally magnetic.'},
  'aliases': ['jeyn eyr', 'jane eyre', 'джейн эйр']},
 {'id': 'lit_char_097',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Liverpul ko'chalaridan janob Ernsho tomonidan qabul qilingan qora sochli, qorong'i "
                     "ko'zli yetim bolaman.\n"
                     '2-maslahat: Bolalikdagi sevgilim Ketrin boshqa badavlat kishiga (Edgar Linton) turmushga '
                     'chiqqach, butun oiladan shafqatsiz qasos olishga kirishaman.\n'
                     '3-maslahat: Emili Brontening «Momaqaldiroqli dovon» («Uthering Heights») romanidagi yonar '
                     'ehtirosli, zolim antiqahramonman.',
               'ru': 'Подсказка 1: Черноволосый сирота-найденыш цыганского вида, привезенный мистером Эрншо в поместье '
                     'Грозовой Перевал.\n'
                     'Подсказка 2: Одержим неистовой, разрушительной любовью к Кэтрин Эрншо и жаждой мести двум '
                     'соседним семействам.\n'
                     'Подсказка 3: Мрачный байронический антигерой единственного шедевра Эмили Бронте «Грозовой '
                     'перевал».',
               'en': "Clue 1: Dark-skinned, sullen orphan found wandering Liverpool's docks and taken in at Wuthering "
                     'Heights.\n'
                     'Clue 2: Consumed by a ferocious, tempestuous passion for Catherine Earnshaw that turned into an '
                     'unrelenting multigenerational vendetta.\n'
                     "Clue 3: Iconic Byronic antihero of Emily Brontë's solitary masterpiece 'Wuthering Heights'."},
  'options': {'uz': ['Xitkliff', 'Edgar Linton', 'Hindli Ernsho', 'Edvard Rochester'],
              'ru': ['Хитклифф', 'Эдгар Линтон', 'Хиндли Эрншо', 'Эдвард Рочестер'],
              'en': ['Heathcliff', 'Edgar Linton', 'Hindley Earnshaw', 'Edward Rochester']},
  'correct_index': 0,
  'correct_answer': {'uz': 'Xitkliff', 'ru': 'Хитклифф', 'en': 'Heathcliff'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Emily_Bront%C3%AB_by_Patrick_Branwell_Bront%C3%AB_restored.jpg/640px-Emily_Bront%C3%AB_by_Patrick_Branwell_Bront%C3%AB_restored.jpg',
  'fun_fact': {'uz': "Xitkliff va Ketrin o'rtasidagi munosabatlar dunyo adabiyotidagi eng jo'shqin va qorong'i "
                     'muhabbat silsilasi hisoblanadi.',
               'ru': '«Грозовой перевал» признан эталоном английского романтического готического романа.',
               'en': "'Wuthering Heights' is widely celebrated as the crowning pinnacle of romantic gothic fiction."},
  'aliases': ['xitkliff', 'heathcliff', 'хитклифф']},
 {'id': 'lit_char_098',
  'sub_mode': 'characters',
  'question': {'uz': '1-maslahat: Graflik unvoni (Graf de La Fer) va katta boyligidan voz kechib oddiy qirol '
                     'mushketyoriga aylangan sirli jangchiman.\n'
                     "2-maslahat: O'tmishda yelkasida nilufar tamg'asi bo'lgan xiyonatkor xotinim (Miledi de Vinter) "
                     "bilan fojiali bog'liqligim bor.\n"
                     "3-maslahat: Aleksandr Dyumaning «Uch mushketyor» asaridagi eng dono, asil va ulug'vor "
                     'qahramonman.',
               'ru': 'Подсказка 1: Самый благородный, молчаливый и мудрый из королевских мушкетеров, скрывающий '
                     'подлинное графское имя де Ла Фер.\n'
                     'Подсказка 2: Хранит страшную тайну о своей казненной жене Миледи, чье плечо было заклеймено '
                     'позорной королевской лилией.\n'
                     "Подсказка 3: Близкий наставник и друг д'Артаньяна в романе Александра Дюма «Три мушкетера».",
               'en': 'Clue 1: Oldest, most melancholic and aristocratic musketeer, concealing his noble identity as '
                     'Count de la Fère.\n'
                     'Clue 2: Harbored a dark secret concerning his treacherous former wife, the branded felon Milady '
                     'de Winter.\n'
                     "Clue 3: Father figure and steadfast sword to d'Artagnan in Alexandre Dumas' 'The Three "
                     "Musketeers'."},
  'options': {'uz': ['Portos', 'Atos (Graf de La Fer)', 'Aramis', "D'Artanyan"],
              'ru': ['Портос', 'Атос (Граф де Ла Фер)', 'Арамис', "Д'Артаньян"],
              'en': ['Porthos', 'Athos (Count de la Fère)', 'Aramis', "D'Artagnan"]},
  'correct_index': 1,
  'correct_answer': {'uz': 'Atos (Graf de La Fer)', 'ru': 'Атос (Граф де Ла Фер)', 'en': 'Athos (Count de la Fère)'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Alexandre_Dumas_by_Nadar%2C_1855.jpg/640px-Alexandre_Dumas_by_Nadar%2C_1855.jpg',
  'fun_fact': {'uz': 'Dyuma Atos obrazida qadimiy fransuz ritsarligining or-nomusi va fojiali burch hissiyotini '
                     'mujassamlashtirgan.',
               'ru': 'Имя Атоса происходит от названия греческой горы Афон (Athos) и реального мушкетера Армана де '
                     "Силлег д'Атос д'Отевиль.",
               'en': 'Athos was named in part after Mount Athos in Greece, derived from the historical mousquetaire '
                     'Armand de Sillègue.'},
  'aliases': ['atos', 'graf de la fer', 'атос', 'граф де ла фер', 'athos']},
 {'id': 'lit_char_099',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: Sud palatasi a'zosi, hayotini «yaxshi odamlar kabi» qulay, hashamatli va qonuniy "
                     "o'tkazgan 45 yoshli rus mansabdoriman.\n"
                     '2-maslahat: Yangi xonadondagi pardani ilishda yonboshim bilan yiqilib, davosiz kasallikka '
                     "uchrayman va asta-sekin o'limga yaqinlashaman.\n"
                     "3-maslahat: O'lim arafasida butun o'tgan hayotim soxta bo'lganini anglagan Lev Tolstoyning "
                     'mashhur psixologik qissasi qahramoniman.',
               'ru': 'Подсказка 1: Успешный судебный чиновник, проживший жизнь «легко, приятно и прилично», как '
                     'требовали светские приличия.\n'
                     'Подсказка 2: Ударившись боком о ручку стремянки при развешивании штор, заболевает смертельным '
                     'недугом.\n'
                     'Подсказка 3: Главный персонаж потрясающей экзистенциальной повести Льва Толстого «Смерть Ивана '
                     'Ильича».',
               'en': 'Clue 1: Successful High Court magistrate who lived his life strictly according to bourgeois '
                     'social convention.\n'
                     'Clue 2: Injured his side on a window latch while hanging curtains in his lavish apartment, '
                     'falling into terminal agony.\n'
                     "Clue 3: Protagonist of Leo Tolstoy's existential masterpiece 'The Death of Ivan Ilyich'."},
  'options': {'uz': ['Gerasim', 'Pyotr Ivanovich', 'Ivan Ilyich Golovin', 'Praskovya Fedorovna'],
              'ru': ['Герасим', 'Пётр Иванович', 'Иван Ильич Головин', 'Прасковья Фёдоровна'],
              'en': ['Gerasim', 'Pyotr Ivanovich', 'Ivan Ilyich Golovin', 'Praskovya Fedorovna']},
  'correct_index': 2,
  'correct_answer': {'uz': 'Ivan Ilyich Golovin', 'ru': 'Иван Ильич Головин', 'en': 'Ivan Ilyich Golovin'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/L.N.Tolstoy_Prokudin-Gorsky.jpg/640px-L.N.Tolstoy_Prokudin-Gorsky.jpg',
  'fun_fact': {'uz': "«Ivan Ilyichning o'limi» asari jahon tibbiyoti va bioetikasida bemorlar psixologiyasini "
                     "o'rganishda majburiy darslik sifatida o'qitiladi.",
               'ru': 'Повесть Толстого изучается на медицинских факультетах ведущих университетов мира как шедевр '
                     'описания паллиативного опыта.',
               'en': "Tolstoy's novella is widely assigned in medical schools worldwide as a masterwork on mortality "
                     'and hospice ethics.'},
  'aliases': ['ivan ilyich', 'ivan ilyich golovin', 'иван ильич', 'ivan ilyich']},
 {'id': 'lit_char_0100',
  'sub_mode': 'characters',
  'question': {'uz': "1-maslahat: No'g'ay elida tug'ilgan podshozoda, tushida ko'rgan Zangiboy qizi Xolbekaga oshiq "
                     "bo'lib yo'lga chiqqan alpman.\n"
                     "2-maslahat: Zangi qabilasi zindonida azob tortib, cho'lda ikki o'g'lim Gurkiboy va Mohiboydan "
                     'ayrilib qolaman.\n'
                     "3-maslahat: Egri Qilich bilan dushmanlarni yengib baxtiga erishgan, mashhur o'zbek "
                     'ishqiy-qahramonlik dostonining bosh qahramoniman.',
               'ru': 'Подсказка 1: Царевич из ногайской земли, увидевший во сне прекрасную Холбеку и отправившийся на '
                     'ее поиски.\n'
                     'Подсказка 2: Испытал тяжелые лишения в пустыне, разлучился с сыновьями Гуркибаем и Мохибаем, '
                     'попав в рабство.\n'
                     'Подсказка 3: Главный герой одноименного классического узбекского романического эпоса-дастана.',
               'en': 'Clue 1: Nogai prince who fell in love with princess Kholbeka through a prophetic dream and set '
                     'out across the steppes.\n'
                     'Clue 2: Endured cruel captivity and lost his sons Gurkiboy and Mohiboy before miraculous '
                     'reunions.\n'
                     'Clue 3: Hero of the celebrated classic Uzbek romantic-heroic verse epic named after him.'},
  'options': {'uz': ['Alpomish', "Go'ro'g'li", 'Avazxon', "Kuntug'mish"],
              'ru': ['Алпомыш', 'Гёроглы', 'Авазхан', 'Кунтугмыш'],
              'en': ['Alpamysh', 'Gorogly', 'Avazkhan', 'Kuntugmysh']},
  'correct_index': 3,
  'correct_answer': {'uz': "Kuntug'mish", 'ru': 'Кунтугмыш', 'en': 'Kuntugmysh'},
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Alpomish_statue_Termez.jpg/640px-Alpomish_statue_Termez.jpg',
  'fun_fact': {'uz': "«Kuntug'mish» dostoni o'zbek xalq dostonchiligida sadoqat, sabr-toqat va adolat tantanasini "
                     'tarannum etuvchi nodir durdonadir.',
               'ru': 'Дастан «Кунтугмыш» в исполнении сказителя Эргаша Джуманбулбул оглы является жемчужиной '
                     'узбекского фольклора.',
               'en': 'Recited by master bard Ergash Jumanbulbul-oghli, Kuntugmysh is a cherished gem of Central Asian '
                     'bardic heritage.'},
  'aliases': ["kuntug'mish", 'kuntugmish', 'кунтугмыш']}]

LITERATURE_QUESTIONS: List[Dict[str, Any]] = LITERATURE_DATA

LITERATURE_BY_ID: Dict[str, Dict[str, Any]] = {item["id"]: item for item in LITERATURE_DATA}
LITERATURE_BY_SUBMODE: Dict[str, List[Dict[str, Any]]] = {}
for item in LITERATURE_DATA:
    LITERATURE_BY_SUBMODE.setdefault(item["sub_mode"], []).append(item)
LITERATURE_BY_SUB_MODE = LITERATURE_BY_SUBMODE


def get_literature_item_by_id(item_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a literature trivia item by its unique ID."""
    return LITERATURE_BY_ID.get(item_id)


def get_literature_question_by_id(question_id: str) -> Optional[Dict[str, Any]]:
    """Alias for get_literature_item_by_id."""
    return get_literature_item_by_id(question_id)


def get_literature_items_by_submode(sub_mode: str) -> List[Dict[str, Any]]:
    """Retrieve all literature items for a specific sub-mode."""
    return LITERATURE_BY_SUBMODE.get(sub_mode, [])


def get_literature_questions_by_submode(sub_mode: str) -> List[Dict[str, Any]]:
    """Alias for get_literature_items_by_submode."""
    return get_literature_items_by_submode(sub_mode)


def get_random_literature_items(count: int = 1, sub_mode: Optional[str] = None) -> List[Dict[str, Any]]:
    """Sample random literature items without replacement, optionally filtered by sub-mode."""
    pool = LITERATURE_BY_SUBMODE.get(sub_mode, LITERATURE_DATA) if sub_mode else LITERATURE_DATA
    if not pool:
        return []
    return random.sample(pool, min(count, len(pool)))


def get_random_literature_questions(count: int = 1, sub_mode: Optional[str] = None) -> List[Dict[str, Any]]:
    """Alias for get_random_literature_items."""
    return get_random_literature_items(count=count, sub_mode=sub_mode)


def search_literature_by_alias(query: str) -> List[Dict[str, Any]]:
    """Search literature items by alias or name match."""
    q = query.lower().strip()
    results = []
    for item in LITERATURE_DATA:
        if any(q in alias for alias in item["aliases"]):
            results.append(item)
            continue
        for lang in ["uz", "ru", "en"]:
            if q in item["correct_answer"][lang].lower():
                results.append(item)
                break
    return results
