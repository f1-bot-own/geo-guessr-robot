# -*- coding: utf-8 -*-
"""Part 2: Deduction questions (zakovat_126 to zakovat_250)."""

DEDUCTION_QUESTIONS = [
    {
        "id": "zakovat_126",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ikkinchi jahon urushida matematik Abraham Vald bazaga qaytgan bombardimonchi samolyotlardagi o'q izlarini o'rganib, zirhni eng ko'p o'q tekkan joylarga emas, aynan qaysi joylarga o'rnatishni taklif qilgan?",
            "ru": "Внимание, вопрос на логику: Во Вторую мировую математик Абрахам Вальд, изучив пробоины на вернувшихся бомбардировщиках, предложил бронировать не изрешечённые места, а какие именно?",
            "en": "Attention, deductive question: In WWII, mathematician Abraham Wald studied bullet holes on returning bombers and famously advised placing armor not where holes were clustered, but where?"
        },
        "options": {
            "uz": [
                "Qaytmagan (urilgan) samolyotlar joyiga",
                "Eng ko'p o'q tekkan qanotlarga",
                "Samolyot dumi va yon tomonlariga",
                "Faqat yoqilg'i baklariga"
            ],
            "ru": [
                "Места, где у вернувшихся самолётов НЕ было пробоин",
                "Места с наибольшим числом пробоин",
                "Хвостовое оперение и крылья",
                "Исключительно топливные баки"
            ],
            "en": [
                "Where returning planes had NO bullet holes",
                "Where returning planes had the most holes",
                "Tail wings and fuselage flanks",
                "Exclusively fuel tanks"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Qaytmagan (urilgan) samolyotlar joyiga",
            "ru": "Места, где у вернувшихся самолётов НЕ было пробоин",
            "en": "Where returning planes had NO bullet holes"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Vald 'tirik qolganlarning xatosi'ni (survivorship bias) anglab yetdi: dvigateliga o'q tekkan samolyotlar bazaga umuman qayta olmagan.",
            "ru": "Вальд открыл 'систематическую ошибку выжившего': самолёты с повреждениями двигателей и кабины просто не долетали до базы.",
            "en": "Wald recognized survivorship bias: planes shot in the engines never returned to be counted."
        },
        "aliases": [
            "qaytmagan joylarga",
            "o'q tegmagan joylarga",
            "dvigatelga",
            "survivorship bias",
            "ошибку выжившего"
        ]
    },
    {
        "id": "zakovat_127",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Miloddan avvalgi 390-yilda gallar tunda Rimdagi Kapitoliyni egallamoqchi bo'lganida, xudolar ibodatxonasidagi qaysi hayvonlar shovqin ko'tarib rimliklarni uyg'otgan va Rimni qutqarib qolgan?",
            "ru": "Внимание, вопрос на логику: В 390 году до н.э., когда галлы крались к Капитолию Рима, стража и собаки спали. Какие храмовые птицы подняли шум и спасли Рим?",
            "en": "Attention, deductive question: In 390 BC, when Gauls stealthily scaled Rome's Capitoline Hill while watchdogs slept, which sacred temple birds honked and saved Rome?"
        },
        "options": {
            "uz": [
                "Itlar",
                "G'ozlar",
                "Mushuklar",
                "Burgutlar"
            ],
            "ru": [
                "Собаки",
                "Гуси",
                "Кошки",
                "Орлы"
            ],
            "en": [
                "Dogs",
                "Geese",
                "Cats",
                "Eagles"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "G'ozlar",
            "ru": "Гуси",
            "en": "Geese"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Yunon ma'budasi Yunona ibodatxonasida boqilgan g'ozlar sezgir eshitishi tufayli gallar qadam tovushini payqagan.",
            "ru": "Священные гуси богини Юноны обладали чутким слухом и загоготали от звука крадущихся врагов.",
            "en": "Sacred geese of the goddess Juno detected the muffled footsteps of climbing Gauls and raised an alarm."
        },
        "aliases": [
            "g'ozlar",
            "gozlar",
            "gusi",
            "geese",
            "гуси"
        ]
    },
    {
        "id": "zakovat_128",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 1854-yilda Londonda vabo tarqalganda, shifokor Jon Snou kasallik havodan emas, suvdan yuqishini isbotlash uchun Broad-stritdagi qaysi keskin chorani qo'llagan?",
            "ru": "Внимание, вопрос на логику: В 1854 году во время холеры в Лондоне доктор Джон Сноу, доказав водный путь заражения, совершил на Брод-стрит какое простое действие?",
            "en": "Attention, deductive question: In 1854, to halt London's Soho cholera outbreak after identifying contaminated well water, Dr. John Snow famously did what to the Broad Street pump?"
        },
        "options": {
            "uz": [
                "Bemorlarni shahardan quvib chiqargan",
                "Havoni tutatqilar bilan tozalagan",
                "Suv nasosi (kolonka) dastasini yechib tashlagan",
                "Barcha dorixonalarni yopgan"
            ],
            "ru": [
                "Изолировал больных за стенами города",
                "Окуривал воздух благовониями",
                "Снял рукоятку водоразборной колонки",
                "Закрыл все городские аптеки"
            ],
            "en": [
                "Expelled sick citizens beyond city walls",
                "Fumigated the atmosphere with incense",
                "Removed the handle of the water pump",
                "Shut down all neighborhood pharmacies"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Suv nasosi (kolonka) dastasini yechib tashlagan",
            "ru": "Снял рукоятку водоразборной колонки",
            "en": "Removed the handle of the water pump"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Snou suv kolonkasi dastasini olib tashlagach, odamlar u yerdan ifloslangan suv ichishni to'xtatgan va vabo epidemiyasi darhol pasaygan.",
            "ru": "После снятия ручки насоса жители перестали пить зараженную воду, и эпидемия прекратилась.",
            "en": "Removing the pump handle cut off community access to the contaminated cesspool-adjacent well."
        },
        "aliases": [
            "nasos dastasini",
            "kolonka dastasini",
            "nasos",
            "рукоятку",
            "ручку насоса",
            "pump handle"
        ]
    },
    {
        "id": "zakovat_129",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Yaponiya temir yo'l kompaniyalari bekatlarning chetlariga va temir yo'l kesishmalariga nima maqsadda ko'k rangli LED chiroqlar o'rnatgan?",
            "ru": "Внимание, вопрос на логику: Японские железнодорожные компании установили на платформах и переездах синие светодиодные фонари с какой целью?",
            "en": "Attention, deductive question: Why did Japanese railway companies install soft blue LED lighting along train platforms and level crossings?"
        },
        "options": {
            "uz": [
                "Poyezdlar to'xtash joyini belgilash uchun",
                "Elektr energiyasini tejash uchun",
                "Ko'zi ojizlarga yo'l ko'rsatish uchun",
                "O'z joniga qasd qilish (suitsid) hollarini kamaytirish uchun"
            ],
            "ru": [
                "Для разметки мест остановки вагонов",
                "Для экономии электроэнергии",
                "Для ориентации слабовидящих",
                "Для снижения числа самоубийств"
            ],
            "en": [
                "To mark exact train door stopping spots",
                "To save electrical energy",
                "To guide visually impaired commuters",
                "To reduce suicide rates"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "O'z joniga qasd qilish (suitsid) hollarini kamaytirish uchun",
            "ru": "Для снижения числа самоубийств",
            "en": "To reduce suicide rates"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Tadqiqotlar shuni ko'rsatdiki, ko'k rang inson asab tizimiga tinchlantiruvchi ta'sir ko'rsatib, suitsid holatlarini 84 foizga kamaytirgan.",
            "ru": "Исследования показали, что синий свет успокаивает психику, и число прыжков под поезд упало на 84%.",
            "en": "Blue light physiologically induces calm in agitated brains, reducing railway suicide attempts by up to 84%."
        },
        "aliases": [
            "suitsid",
            "o'z joniga qasd",
            "samoubiystvo",
            "suicide",
            "самоубийств"
        ]
    },
    {
        "id": "zakovat_130",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: O'rta asrlarda dengizchilar va qaroqchilar qulog'iga tilla sirg'a taqib yurishining asosiy sababi nima bo'lgan?",
            "ru": "Внимание, вопрос на логику: Зачем моряки и пираты носили в ухе массивную золотую серьгу?",
            "en": "Attention, deductive question: What was the primary pragmatic motivation for historic sailors to wear a heavy gold hoop earring?"
        },
        "options": {
            "uz": [
                "Dafn marosimi xarajatlarini to'lash uchun",
                "Dengiz kasalligidan qutulish uchun",
                "Eshitish qobiliyatini yaxshilash uchun",
                "Shohga qarashli ekanini bildirish uchun"
            ],
            "ru": [
                "Для оплаты христианских похорон",
                "Для защиты от морской болезни",
                "Для улучшения слуха канониров",
                "В знак верности короне"
            ],
            "en": [
                "To pay for a proper burial",
                "To ward off seasickness",
                "To protect gunners' hearing from cannon fire",
                "To indicate allegiance to the crown"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Dafn marosimi xarajatlarini to'lash uchun",
            "ru": "Для оплаты христианских похорон",
            "en": "To pay for a proper burial"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Agar dengizchi halok bo'lib, jasadi qirg'oqqa chiqib qolsa, qulog'idagi tilla uning dafn marosimini o'tkazgan odamga haq sifatida qoldirilgan.",
            "ru": "Если моряк погибал и его выбрасывало на берег, золото серьги служило платой за погребение по христианскому обряду.",
            "en": "The gold in the earring served as payment to anyone who discovered their washed-up body to fund a decent Christian burial."
        },
        "aliases": [
            "dafn",
            "dafn marosimi",
            "pohoroni",
            "burial",
            "похорон"
        ]
    },
    {
        "id": "zakovat_131",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Dengiz qaroqchilarining ko'pchiligi ikki ko'zi soppa-sog' bo'lsa ham, nima sababdan bir ko'ziga qora bog'ich taqib yurishgan?",
            "ru": "Внимание, вопрос на логику: Почему пираты носили повязку на глазу, даже если оба их глаза были абсолютно здоровы?",
            "en": "Attention, deductive question: Why did historical pirates frequently wear an eyepatch even when both of their eyes had perfect vision?"
        },
        "options": {
            "uz": [
                "Jangda ko'zidan ayrilgani uchun",
                "Qorong'ida ko'rish moslashuvini saqlab qolish uchun",
                "Dushmanga qo'rqinchli ko'rinish uchun",
                "Ko'z kasalliklarini yashirish uchun"
            ],
            "ru": [
                "Из-за слепоты на один глаз от ранения",
                "Чтобы сохранить адаптацию глаза к темноте",
                "Для устрашения противника",
                "Чтобы скрыть инфекцию глаза"
            ],
            "en": [
                "Because they lost an eye in battle",
                "To maintain dark adaptation",
                "To intimidate enemy boarding crews",
                "To conceal an eye infection"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Qorong'ida ko'rish moslashuvini saqlab qolish uchun",
            "ru": "Чтобы сохранить адаптацию глаза к темноте",
            "en": "To maintain dark adaptation"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Yorug' palubadan quyosh tushmaydigan qorong'i tryumga tushganda bog'ich boshqa ko'zga surilgan va ko'z darhol qorong'ilikda aniq ko'rgan.",
            "ru": "Спустившись с залитой солнцем палубы в темный трюм, пират сдвигал повязку и видел приученным к темноте глазом мгновенно.",
            "en": "Shifting the patch allowed instant night vision when entering pitch-black cargo holds during boarding combat."
        },
        "aliases": [
            "qorong'ida ko'rish",
            "k darkness",
            "adaptatsiya",
            "темнота",
            "адаптация",
            "dark adaptation"
        ]
    },
    {
        "id": "zakovat_132",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qadimgi Misrda xonadonda boqiladigan sevimli mushuk vafot etganda, oilaning barcha a'zolari chuqur motam belgisi sifatida o'zlarida qanday o'zgarish qilishgan?",
            "ru": "Внимание, вопрос на логику: В Древнем Египте, когда в доме умирала любимая кошка, что сбривали все члены семьи в знак траура?",
            "en": "Attention, deductive question: In ancient Egypt, when a beloved household cat passed away, what did all family members shave off to display mourning?"
        },
        "options": {
            "uz": [
                "Qora libos kiyib ro'za tutishgan",
                "Sochlarini yulib yig'lashgan",
                "Qoshlarini qirib tashlashgan",
                "Uylarini tashlab ketishgan"
            ],
            "ru": [
                "Носили чёрное и постились сорок дней",
                "Стригли волосы наголо",
                "Сбривали брови в знак траура",
                "Покидали свой дом"
            ],
            "en": [
                "Wore black garments and fasted for forty days",
                "Shaved their heads bald",
                "Shaved their eyebrows",
                "Abandoned their dwellings temporarily"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Qoshlarini qirib tashlashgan",
            "ru": "Сбривали брови в знак траура",
            "en": "Shaved their eyebrows"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Gerodot yozishicha, mushuk o'lganda hamma qoshini qirgan, it o'lganda esa butun badanidagi tuklarni qirishgan.",
            "ru": "Геродот отмечал, что при смерти кошки домочадцы сбривали брови, а при смерти собаки — всё тело.",
            "en": "Herodotus recorded that grieving Egyptian owners shaved their eyebrows, mourning until the hair grew back."
        },
        "aliases": [
            "qosh",
            "qoshlarini",
            "brovi",
            "eyebrows",
            "брови"
        ]
    },
    {
        "id": "zakovat_133",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Rembrandtning mashhur 'Tungi soqchilar' (Nochnoy dozor) kartinasi 1940-yillarda tozalanganda san'atshunoslar qanday hayratlanarli haqiqatni aniqlashgan?",
            "ru": "Внимание, вопрос на логику: Когда в 1940-х картину Рембрандта 'Ночной дозор' расчистили от векового лака, какое открытие поразило искусствоведов?",
            "en": "Attention, deductive question: When Rembrandt's famous painting 'The Night Watch' was cleaned of old varnish in the 1940s, what surprising truth emerged?"
        },
        "options": {
            "uz": [
                "Rembrandt faqat qorong'ida rasm chizgan",
                "Tasvirlangan voqea tunda sodir bo'lgan",
                "Qora bo'yoq eng arzon bo'lgan",
                "Aslida kunduzgi sahna bo'lib, lak va tutundan qorayib ketgan"
            ],
            "ru": [
                "Рембрандт писал её исключительно ночью",
                "Событие действительно происходило в полночь",
                "Тёмные краски стоили дешевле всего",
                "Действие происходит днём, но лак потемнел от копоти"
            ],
            "en": [
                "Rembrandt exclusively painted at night",
                "The historic muster occurred at midnight",
                "Black pigment was the cheapest available",
                "It is set in daytime, but varnish and soot darkened it"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Aslida kunduzgi sahna bo'lib, lak va tutundan qorayib ketgan",
            "ru": "Действие происходит днём, но лак потемнел от копоти",
            "en": "It is set in daytime, but varnish and soot darkened it"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Asar aslida yorug' quyoshli kunduz kuni ro'yxatga olingan merganlar rotasini tasvirlagan, asrlar davomida kamin tutuni va qora lak uni 'tungi'ga aylantirgan.",
            "ru": "Картина изображает выход роты ясным днём; копоть каминов и темный лак за века превратили день в ночь.",
            "en": "The painting actually depicts a daylight scene; centuries of fireplace soot and darkened varnish had made it look nocturnal."
        },
        "aliases": [
            "kunduz",
            "kunduzgi",
            "lak",
            "dnem",
            "daylight",
            "днём",
            "день"
        ]
    },
    {
        "id": "zakovat_134",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ernest Hemingway garov o'ynab, bor-yo'g'i 6 ta so'zdan iborat eng ta'sirli qisqa hikoya yozgan: 'Sotiladi: ..., hech qachon kiyilmagan'. Nuqtalar o'rnidagi so'zni toping.",
            "ru": "Внимание, вопрос на логику: Эрнест Хемингуэй поспорил, что напишет самый короткий и трогательный рассказ из 6 слов: 'Продаются: ..., неношеные'. Что продавалось?",
            "en": "Attention, deductive question: Ernest Hemingway famously won a bet by writing a devastating six-word story: 'For sale: ..., never worn.' What was for sale?"
        },
        "options": {
            "uz": [
                "Bolalar poyabzali (oyoq kiyimi)",
                "To'y libosi",
                "Qadimiy avtomobil",
                "Oltin soat"
            ],
            "ru": [
                "Детские ботиночки",
                "Свадебное платье",
                "Старинный автомобиль",
                "Золотые часы"
            ],
            "en": [
                "Baby shoes",
                "Wedding dress",
                "Vintage car",
                "Gold watch"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Bolalar poyabzali (oyoq kiyimi)",
            "ru": "Детские ботиночки",
            "en": "Baby shoes"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "'For sale: baby shoes, never worn' — 6 ta so'z orqali dunyodagi eng katta fojia — tug'ilmay nobud bo'lgan go'dak dardi ifodalangan.",
            "ru": "Шесть слов 'For sale: baby shoes, never worn' выражают безмерную трагедию неродившегося или умершего младенца.",
            "en": "The tragedy of an infant dying before birth is captured in those poignant six words."
        },
        "aliases": [
            "bolalar poyabzali",
            "poyabzal",
            "botinochki",
            "baby shoes",
            "ботиночки",
            "обувь"
        ]
    },
    {
        "id": "zakovat_135",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bugungi kunda har bir telefonda bor 'kalkulyator' so'zi lotincha 'calculus' so'zidan olingan. 'Calculus' so'zi qadimgi Rimda nimani anglatgan?",
            "ru": "Внимание, вопрос на логику: Слово 'калькулятор' происходит от латинского 'calculus'. Что изначально означало это слово в Древнем Риме?",
            "en": "Attention, deductive question: The word 'calculator' derives from the Latin noun 'calculus'. What did 'calculus' literally mean in ancient Rome?"
        },
        "options": {
            "uz": [
                "Qadimgi tangalar",
                "Kichik toshchalar (shag'al)",
                "Yog'och cho'plar",
                "Qush suyaklari"
            ],
            "ru": [
                "Древние монетки",
                "Мелкие камешки для счёта",
                "Деревянные палочки",
                "Птичьи косточки"
            ],
            "en": [
                "Ancient coins",
                "Small counting pebbles",
                "Wooden tally sticks",
                "Bird bones"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Kichik toshchalar (shag'al)",
            "ru": "Мелкие камешки для счёта",
            "en": "Small counting pebbles"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Rimliklar abak (cho't) taxtasida hisob-kitob qilishda mayda ohaktosh toshchalaridan (calculus) foydalanishgan.",
            "ru": "Римляне производили подсчёты на абаке с помощью известняковых камешков — calculus.",
            "en": "Romans used small limestone pebbles (calculi) as counters on their counting boards."
        },
        "aliases": [
            "toshchalar",
            "toshcha",
            "kameshki",
            "pebbles",
            "stone",
            "камешки"
        ]
    },
    {
        "id": "zakovat_136",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qadimgi Rim imperatorlari (masalan, Kaligula va Vitelliy) bazmlarida eng qimmatbaho va hashamatli noz-ne'mat sifatida qaysi qush a'zosi minglab donalab tortilgan?",
            "ru": "Внимание, вопрос на логику: На пирах римских императоров Вителлия и Гелиогабала верхом роскоши считалось блюдо из тысяч каких частей фламинго?",
            "en": "Attention, deductive question: At lavish imperial Roman banquets hosted by Heliogabalus and Vitellius, what anatomical delicacy from thousands of flamingos was served?"
        },
        "options": {
            "uz": [
                "Qush pati",
                "Tovuq yuragi",
                "Flamingoning tillari",
                "Qurbaqa ko'zi"
            ],
            "ru": [
                "Перья павлина",
                "Куриные сердца",
                "Языки фламинго",
                "Глаза лягушек"
            ],
            "en": [
                "Peacock feathers",
                "Chicken hearts",
                "Flamingo tongues",
                "Frog eyes"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Flamingoning tillari",
            "ru": "Языки фламинго",
            "en": "Flamingo tongues"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Pliniy Katta o'z asarida flamingo tili eng nozik ta'mga ega ekanligini ta'riflagan va bitta taom uchun minglab qush nobud qilingan.",
            "ru": "Плиний Старший писал, что язык фламинго обладает изумительным вкусом; для одного блюда истребляли тысячи птиц.",
            "en": "Pliny the Elder noted that the fleshy tongues of flamingos were prized above all delicacies by decadent emperors."
        },
        "aliases": [
            "tili",
            "flamingoning tili",
            "yaziki flamingo",
            "flamingo tongues",
            "языки фламинго"
        ]
    },
    {
        "id": "zakovat_137",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Napoleon Bonapart askarlar mundirining yenglariga qator qilib mis tugmalar qadash haqida maxsus buyruq berganining kulgili sababi nima edi?",
            "ru": "Внимание, вопрос на логику: Зачем Наполеон приказал пришивать металлические пуговицы на обшлага рукавов солдатских мундиров?",
            "en": "Attention, deductive question: What practical etiquette reason prompted Napoleon to order rows of brass buttons sewn onto the cuffs of soldier coats?"
        },
        "options": {
            "uz": [
                "Qo'lqoplarni mahkamlash uchun",
                "Rutbasini bildirish uchun",
                "Qon to'xtatuvchi jgut vazifasida",
                "Askarlar burunlarini yengiga artishining oldini olish uchun"
            ],
            "ru": [
                "Для пристёгивания перчаток",
                "Для обозначения воинского звания",
                "В качестве жгута при ранении",
                "Чтобы солдаты не вытирали нос рукавом"
            ],
            "en": [
                "To fasten winter gloves",
                "To denote military rank",
                "To serve as tourniquets for wounds",
                "To stop soldiers wiping their noses on sleeves"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Askarlar burunlarini yengiga artishining oldini olish uchun",
            "ru": "Чтобы солдаты не вытирали нос рукавом",
            "en": "To stop soldiers wiping their noses on sleeves"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Askarlar qishki sovuqda burunlarini qimmatbaho matodan tikilgan mundir yengiga artib kiyimni rasvo qilmasliklari uchun metall tugmalar qo'yilgan.",
            "ru": "Солдаты на морозе вытирали сопли рукавами и портили сукно; металлические пуговицы царапали лицо и отучили их.",
            "en": "Soldiers wiped cold runny noses on their woolen sleeves; the scratchy metal buttons discouraged the habit."
        },
        "aliases": [
            "burun artmaslik",
            "burun",
            "нос",
            "вытирать нос",
            "wipe nose",
            "noses"
        ]
    },
    {
        "id": "zakovat_138",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Tennis o'yinidagi g'alati hisob-kitob (15, 30, 40) qaysi buyumning choraklariga bo'linishi asosida paydo bo'lgan?",
            "ru": "Внимание, вопрос на логику: Откуда в теннисе взялась странная система подсчёта очков: 15, 30, 40?",
            "en": "Attention, deductive question: What mechanical instrument's quarters originally determined tennis scoring (15, 30, 45)?"
        },
        "options": {
            "uz": [
                "Soat siferblati (choraklari)",
                "Kamon o'qlari masofasi",
                "Fransuz tangalari qiymati",
                "Qadamlar soni"
            ],
            "ru": [
                "Циферблат часов (четверти часа)",
                "Дистанция полёта стрелы",
                "Номиналы французских монет",
                "Шаги игроков"
            ],
            "en": [
                "Clock face quadrants",
                "Archery arrow distances",
                "French coin denominations",
                "Court paces"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Soat siferblati (choraklari)",
            "ru": "Циферблат часов (четверти часа)",
            "en": "Clock face quadrants"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Dastlab kort chetida soat qo'yilgan va har bir ochkoda mil 15, 30 va 45 daqiqaga surilgan, keyinchalik 45 tez aytish uchun 40 ga qisqargan.",
            "ru": "Очки отмечали по циферблату часов: стрелку двигали на 15, 30 и 45 минут; со временем 45 сократили до 40.",
            "en": "Points were tracked on a clock face: advancing the hand to 15, 30, and 45 minutes (later shortened to 40)."
        },
        "aliases": [
            "soat",
            "soat siferblati",
            "tsiferblat",
            "clock",
            "clock face",
            "циферблат"
        ]
    },
    {
        "id": "zakovat_139",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Buyuk Britaniya va uning sobiq mustamlakalarida chap tomonlama harakatlanishning tarixiy sababi nimada?",
            "ru": "Внимание, вопрос на логику: Почему в Великобритании исторически сложилось левостороннее движение?",
            "en": "Attention, deductive question: What feudal martial reason led to Great Britain adopting left-hand traffic on roads?"
        },
        "options": {
            "uz": [
                "Otlar faqat chapga yurgani uchun",
                "O'ng qo'lda qilichni erkin ushlash va qindan chiqarish uchun",
                "Quyosh ko'zga tushmasligi uchun",
                "Izvoshchilar chapakay bo'lgani uchun"
            ],
            "ru": [
                "Лошади охотнее поворачивали влево",
                "Чтобы держать правую руку со шпагой свободной",
                "Чтобы солнце не слепило глаза",
                "Кучера поголовно были левшами"
            ],
            "en": [
                "Horses naturally turned left",
                "To keep the right sword hand free",
                "To prevent sunlight blinding riders",
                "Coachmen were predominantly left-handed"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "O'ng qo'lda qilichni erkin ushlash va qindan chiqarish uchun",
            "ru": "Чтобы держать правую руку со шпагой свободной",
            "en": "To keep the right sword hand free"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "O'rta asrlarda ritsarlar yo'lda ro'paradan kelayotgan notanish kishiga qarshi o'ng qo'li bilan darhol qilich yalang'ochlashi uchun chapdan yurgan.",
            "ru": "Рыцари ехали по левой стороне дороги, чтобы правая рука с мечом была готова к защите от встречного всадника.",
            "en": "Knights rode on the left so their right sword hand was closest to oncoming strangers."
        },
        "aliases": [
            "qilich",
            "o'ng qo'l",
            "shpagoy",
            "mech",
            "sword",
            "правая рука"
        ]
    },
    {
        "id": "zakovat_140",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 1986-yilgacha Buyuk Britaniya ko'mir konlarida zaharli uglerod oksidi (is gazi) paydo bo'lganini oldindan sezish uchun qaysi sariq sayroqi qushdan foydalanilgan?",
            "ru": "Внимание, вопрос на логику: Какую жёлтую птичку шахтёры брали в забой вплоть до 1986 года как живой датчик угарного газа?",
            "en": "Attention, deductive question: Which sensitive yellow songbird did coal miners carry underground until 1986 as an early-warning alarm for toxic carbon monoxide?"
        },
        "options": {
            "uz": [
                "Qaldirg'och",
                "Boyo'g'li",
                "Kanareyka qushi",
                "Kaptar"
            ],
            "ru": [
                "Ласточка",
                "Сова",
                "Канарейка",
                "Голубь"
            ],
            "en": [
                "Swallow",
                "Owl",
                "Canary",
                "Pigeon"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Kanareyka qushi",
            "ru": "Канарейка",
            "en": "Canary"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Kanareykaning moddalar almashinuvi juda tez bo'lgani uchun u zaharli gaz ta'sirida odamlardan ancha oldin hushidan ketgan va konchilarni ogohlantirgan.",
            "ru": "Из-за быстрого метаболизма канарейка теряла сознание от малейшей доли угарного газа задолго до людей.",
            "en": "Canaries have extremely high metabolic rates and collapse rapidly from carbon monoxide before humans notice."
        },
        "aliases": [
            "kanareyka",
            "kanareika",
            "canary",
            "канарейка"
        ]
    },
    {
        "id": "zakovat_141",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bugungi kunda xalqaro miqyosda ishlatiladigan 'karantin' so'zi venetsiyaliklarning 'quaranta giorni' iborasidan olingan. Bu muddat necha kunni bildiradi?",
            "ru": "Внимание, вопрос на логику: Слово 'карантин' происходит от венецианского 'quaranta giorni'. Сколько дней длилась эта изоляция судов во время чумы?",
            "en": "Attention, deductive question: The international word 'quarantine' stems from Venetian 'quaranta giorni'. How many days did arriving ships have to anchor in isolation?"
        },
        "options": {
            "uz": [
                "14 kun",
                "30 kun",
                "100 kun",
                "40 kun"
            ],
            "ru": [
                "14 дней",
                "30 дней",
                "100 дней",
                "40 дней"
            ],
            "en": [
                "14 days",
                "30 days",
                "100 days",
                "40 days"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "40 kun",
            "ru": "40 дней",
            "en": "40 days"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "O'lat tarqagan mamlakatlardan Venetsiyaga kelgan kemalar kasallik tarqalmasligi uchun qat'iy 40 kun langarda turishga majbur bo'lgan.",
            "ru": "В XIV веке корабли из зачумлённых стран стояли на рейде Венеции ровно 40 дней перед высадкой на берег.",
            "en": "During the Black Death, ships arriving in Venice were forced to anchor offshore for 40 days before landing."
        },
        "aliases": [
            "40 kun",
            "40",
            "40 dney",
            "40 days",
            "сорок",
            "40 дней"
        ]
    },
    {
        "id": "zakovat_142",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ikkinchi jahon urushida inglizlar nemislarga 'uchuvchilarimiz tunda sabzi yeb ko'zlari o'tkirlashgani uchun sizning samolyotlaringizni urib tushirmoqda' degan afsonani tarqatishdan ko'zlagan maqsadi nima edi?",
            "ru": "Внимание, вопрос на логику: Зачем британская пропаганда во Вторую мировую уверяла немцев, что их пилоты метко сбивают самолёты ночью благодаря поеданию моркови?",
            "en": "Attention, deductive question: Why did British WWII intelligence spread the rumor that RAF fighter aces shot down nighttime Luftwaffe bombers because they ate copious carrots?"
        },
        "options": {
            "uz": [
                "Maxfiy radarlar ixtirosini sir saqlash uchun",
                "Sabzi hosilini ko'paytirish uchun",
                "Nemis parhezini buzish uchun",
                "Shirinlik tanqisligini yopish uchun"
            ],
            "ru": [
                "Чтобы скрыть изобретение бортовых радаров",
                "Для распродажи излишков урожая моркови",
                "Чтобы нарушить диету немцев",
                "Вместо дефицитного сахара"
            ],
            "en": [
                "To conceal secret airborne radar",
                "To sell off surplus domestic carrot crops",
                "To disrupt German nutritional science",
                "To substitute for rationed sugar"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Maxfiy radarlar ixtirosini sir saqlash uchun",
            "ru": "Чтобы скрыть изобретение бортовых радаров",
            "en": "To conceal secret airborne radar"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Britaniya o'z samolyotlariga o'rnatilgan yangi maxfiy radar tizimini nemislardan yashirish uchun 'sabzi' afsonasini o'ylab topgan.",
            "ru": "Британцы скрывали появление на самолётах секретных радаров, объясняя ночные победы 'морковной диетой'.",
            "en": "The British Ministry of Information invented the carrot myth to disguise their revolutionary airborne radar technology."
        },
        "aliases": [
            "radar",
            "radarlarni",
            "radar ixtirosini",
            "радар",
            "радары",
            "radar invention"
        ]
    },
    {
        "id": "zakovat_143",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Inglizcha 'salary' (maosh) so'zi lotincha 'salarium' so'zidan kelib chiqqan. Qadimgi Rimda askarlarga qaysi moddani sotib olish uchun pul ajratilgan?",
            "ru": "Внимание, вопрос на логику: Слово 'salary' (зарплата) восходит к латинскому 'salarium'. На покупку какого ценного продукта выдавали эти деньги римским легионерам?",
            "en": "Attention, deductive question: The English word 'salary' originates from Latin 'salarium'. What essential seasoning were Roman soldiers given an allowance to purchase?"
        },
        "options": {
            "uz": [
                "Bug'doy",
                "Tuz",
                "Zaytun moyi",
                "Kumush"
            ],
            "ru": [
                "Пшеница",
                "Соль",
                "Оливковое масло",
                "Серебро"
            ],
            "en": [
                "Wheat",
                "Salt",
                "Olive oil",
                "Silver"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Tuz",
            "ru": "Соль",
            "en": "Salt"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Rimda tuz juda qimmatli bo'lib, askarlarga go'shtni buzilishdan asrash uchun tuz sotib olishga maxsus pul (salarium) berilgan.",
            "ru": "Соль (sal) ценилась на вес золота; пособие на её приобретение легионерам называлось salarium argentum.",
            "en": "Salt ('sal') was essential for soldiers to preserve meat rations during long campaigns."
        },
        "aliases": [
            "tuz",
            "sol",
            "salt",
            "соль"
        ]
    },
    {
        "id": "zakovat_144",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Flamingo jo'jalari oq-kulrang bo'lib tug'iladi. Ular ulg'aygach nima sababdan pushti yoki och qizil rangga kiradi?",
            "ru": "Внимание, вопрос на логику: Птенцы фламинго рождаются серыми. Отчего их перья со временем становятся розовыми?",
            "en": "Attention, deductive question: Flamingo chicks hatch with drab grey feathers. What causes them to develop their vivid pink plumage as adults?"
        },
        "options": {
            "uz": [
                "Quyosh nurida kuyishi natijasida",
                "Tug'ilgandanoq terisi qizil bo'ladi",
                "Qisqichbaqasimonlar va suvo'tlar tarkibidagi karotin pigmenti tufayli",
                "Dengiz tuzi patlarini bo'yashi tufayli"
            ],
            "ru": [
                "От солнечных ожогов кожи",
                "От рождения имеют ярко-розовый цвет",
                "Из-за поедания рачков и водорослей с каротином",
                "От морской соли, въедающейся в перья"
            ],
            "en": [
                "From sunburning in tropical heat",
                "They are naturally born bright pink",
                "From eating brine shrimp and algae rich in carotenoids",
                "From sea salt dyeing their plumage"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Qisqichbaqasimonlar va suvo'tlar tarkibidagi karotin pigmenti tufayli",
            "ru": "Из-за поедания рачков и водорослей с каротином",
            "en": "From eating brine shrimp and algae rich in carotenoids"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Flamingolar iste'mol qiladigan mayda artemiya qisqichbaqalari va suvo'tlarida qizil karotinoid pigmenti ko'p bo'lib, patlariga rang beradi.",
            "ru": "В рационе фламинго преобладают рачки артемия и сине-зелёные водоросли, богатые пигментом каротиноидом.",
            "en": "Flamingos metabolize alpha- and beta-carotenoids from brine shrimp and spirulina algae into pink pigments in feathers."
        },
        "aliases": [
            "karotin",
            "qisqichbaqa",
            "suvo't",
            "rachki",
            "karotinoid",
            "carotenoids",
            "shrimp",
            "рачки"
        ]
    },
    {
        "id": "zakovat_145",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Piza minorasi 5 darajadan ortiq qiyalikda tursa-da, 1280-yildan beri kamida to'rtta kuchli zilzilada nega qulab tushmagan?",
            "ru": "Внимание, вопрос на логику: Почему Пизанская башня, стоящая с опасным наклоном, уцелела при четырёх сильнейших землетрясениях?",
            "en": "Attention, deductive question: Why has the drastically tilted Leaning Tower of Pisa survived at least four major earthquakes since 1280 without collapsing?"
        },
        "options": {
            "uz": [
                "Minoraning fundamenti yer osti qoyasiga bog'langan",
                "Minora ichida maxsus mayatnik o'rnatilgan",
                "Zilzila kuchi minorani to'g'irlab qo'yadi",
                "Minora egilishiga sabab bo'lgan yumshoq tuproq zilzila to'lqinlarini so'ndiradi"
            ],
            "ru": [
                "Фундамент башни прикован к скале цепями",
                "Внутри башни установлен маятник-гаситель",
                "Стены башни построены из полого кирпича",
                "Мягкий грунт гасит разрушительные волны землетрясений"
            ],
            "en": [
                "The tower is anchored to bedrock with iron chains",
                "A counterweight pendulum is hidden inside",
                "The masonry walls are built of hollow lightweight volcanic ash",
                "The soft soil dampens destructive seismic shockwaves"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Minora egilishiga sabab bo'lgan yumshoq tuproq zilzila to'lqinlarini so'ndiradi",
            "ru": "Мягкий грунт гасит разрушительные волны землетрясений",
            "en": "The soft soil dampens destructive seismic shockwaves"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Olimlar buni dinamik tuproq-struktura o'zaro ta'siri (DSSI) deb atashadi: poydevor ostidagi bo'sh tuproq zilzila tebranishlarini yutib yuboradi.",
            "ru": "Парадокс: мягкий грунт, вызвавший наклон башни, одновременно гасит резонансные колебания грунта при землетрясениях.",
            "en": "Dynamic soil-structure interaction: the very soft soil that caused the tilt also prevents the tower from resonating during quakes."
        },
        "aliases": [
            "tuproq",
            "yumshoq tuproq",
            "grunt",
            "soil",
            "soft soil",
            "грунт"
        ]
    },
    {
        "id": "zakovat_146",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Nima sababdan shahar ko'chalaridagi kanalizatsiya lyuklarining qopqoqlari kvadrat yoki uchburchak emas, balki doira shaklida qilinadi?",
            "ru": "Внимание, вопрос на логику: Почему крышки канализационных люков почти всегда делают круглыми, а не квадратными?",
            "en": "Attention, deductive question: Why are municipal sewer manhole covers almost universally circular rather than square or rectangular?"
        },
        "options": {
            "uz": [
                "Doira shaklidagi qopqoq o'z teshigiga hech qachon tushib ketmaydi",
                "Dumaloq qopqoqni quyish arzonroq",
                "Kanalizatsiya quvurlari ham dumaloq bo'ladi",
                "Burchakli qopqoqlar mashina g'ildiragini teshib yuboradi"
            ],
            "ru": [
                "Круглая крышка ни под каким углом не провалится в люк",
                "Круглую крышку дешевле отливать из чугуна",
                "Канализационные трубы круглые",
                "Углы крышки прокалывали бы шины машин"
            ],
            "en": [
                "A circular cover cannot fall through its own opening",
                "Circular castings are cheaper to manufacture",
                "Sewer tunnels are geometrically cylindrical",
                "Square corners puncture automobile tires"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Doira shaklidagi qopqoq o'z teshigiga hech qachon tushib ketmaydi",
            "ru": "Круглая крышка ни под каким углом не провалится в люк",
            "en": "A circular cover cannot fall through its own opening"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Kvadrat qopqoq diagonal bo'yicha teshikka tushib ketishi mumkin, doiraning diametri esa har tomonda bir xil bo'lgani uchun u hech qachon tushib ketmaydi.",
            "ru": "Квадратная крышка легко провалится по диагонали колодца, а круг не провалится ни при каком развороте.",
            "en": "A square lid turned diagonally easily falls into its hole, whereas a circle has constant diameter and can never fall through."
        },
        "aliases": [
            "tushib ketmaydi",
            "dumaloq",
            "provalitsya",
            "fall through",
            "не провалится",
            "диагональ"
        ]
    },
    {
        "id": "zakovat_147",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 1903-yilda Elizabeth Magie 'Monopoliya' o'yinining ilk varianti — 'The Landlord's Game'ni yaratganda asl maqsadi nima bo'lgan?",
            "ru": "Внимание, вопрос на логику: Какую цель на самом деле преследовала Элизабет Мэги в 1903 году, создавая настольную игру 'Землевладелец' — прообраз 'Монополии'?",
            "en": "Attention, deductive question: What was feminist Lizzie Magie's original progressive purpose when she patented 'The Landlord's Game' (the precursor to Monopoly) in 1903?"
        },
        "options": {
            "uz": [
                "Bank tizimini ommalashtirish uchun",
                "Yakka hokimlik (monopoliya) va yer ijarasining zararini ko'rsatish uchun",
                "Bolalarga hisoblashni o'rgatish uchun",
                "Katta pul yutishni targ'ib qilish uchun"
            ],
            "ru": [
                "Для рекламы американской банковской системы",
                "Показать порочность земельной монополии и жадности",
                "Чтобы обучать детей арифметике",
                "Для пропаганды быстрого обогащения"
            ],
            "en": [
                "To promote the American commercial banking system",
                "To demonstrate the evils of land monopolization",
                "To teach children basic arithmetic",
                "To celebrate capitalist wealth accumulation"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Yakka hokimlik (monopoliya) va yer ijarasining zararini ko'rsatish uchun",
            "ru": "Показать порочность земельной монополии и жадности",
            "en": "To demonstrate the evils of land monopolization"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Megi iqtisodchi Henry Georgening g'oyalari asosida, yerning bitta odam qo'lida to'planishi boshqalarni xonavayron qilishini isbotlash uchun o'yinni o'ylab topgan.",
            "ru": "Мэги хотела показать, что обогащение одного землевладельца за счёт аренды неизбежно разоряет всех остальных игроков.",
            "en": "Magie designed the game as a critique of predatory monopolies to show how landlords impoverish tenants."
        },
        "aliases": [
            "monopoliya zarari",
            "ijara",
            "monopolya",
            "monopoly",
            "монополия",
            "landlord"
        ]
    },
    {
        "id": "zakovat_148",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Biz qadimgi Yunoniston va Rim haykallarini oppoq marmar deb bilamiz. Aslida antik davrda ular qanday ko'rinishda bo'lgan?",
            "ru": "Внимание, вопрос на логику: Мы привыкли видеть античные мраморные статуи белыми. Какими они были на самом деле в древности?",
            "en": "Attention, deductive question: We revere ancient Greek and Roman marble statues as pristine white stone. What was their true appearance in antiquity?"
        },
        "options": {
            "uz": [
                "Qadimgi yunonlar faqat oq marmarni muqaddas bilgan",
                "Haykallarni bo'yash taqiqlangan",
                "Ular yorqin ranglarga bo'yalgan bo'lgan, bo'yoqlar vaqt o'tishi bilan o'chib ketgan",
                "Oq rang soflik ramzi bo'lgan"
            ],
            "ru": [
                "Греки признавали священным только белый мрамор",
                "Красить скульптуры запрещал закон полиса",
                "Они были ярко раскрашены, но краска стёрлась за века",
                "Белый цвет символизировал чистоту богов"
            ],
            "en": [
                "Greeks considered bare white marble sacred",
                "City statutes banned painting stone idols",
                "They were painted in vibrant colors that weathered away",
                "White stone symbolized the purity of the gods"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Ular yorqin ranglarga bo'yalgan bo'lgan, bo'yoqlar vaqt o'tishi bilan o'chib ketgan",
            "ru": "Они были ярко раскрашены, но краска стёрлась за века",
            "en": "They were painted in vibrant colors that weathered away"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Ultrafiolet nurlar ostidagi tadqiqotlar haykallarning barchasi yorqin qizil, ko'k, sariq bo'yoqlar bilan bo'yalganini fosh etdi; asrlar davomida bo'yoq to'kilib ketgan.",
            "ru": "Спектральный анализ показал, что все античные статуи были ярко расписаны красками, стёршимися от времени.",
            "en": "Spectroscopic imaging proves ancient classical statues were brightly and garishly painted with vivid pigments that eroded away."
        },
        "aliases": [
            "bo'yalgan",
            "rangli",
            "raskrasheni",
            "painted",
            "colors",
            "раскрашены",
            "яркие краски"
        ]
    },
    {
        "id": "zakovat_149",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Sartaroshxonalar (barbershop) peshtoqidagi qizil, oq va ko'k aylanuvchi chiziqlardan iborat ustunning ma'nosi nima?",
            "ru": "Внимание, вопрос на логику: Что изначально символизировали красные, белые и синие полосы на вращающемся столбике у входа в парикмахерскую?",
            "en": "Attention, deductive question: What historic medical practice do the red, white, and blue spiraling stripes on a traditional barber's pole represent?"
        },
        "options": {
            "uz": [
                "Fransiya va AQSh bayrog'i ranglari",
                "Shampun, suv va qaychi ramzi",
                "Soch ranglari (qizil, oq va qora)",
                "Qon olish va jarrohlik muolajalari (qon, bint va vena tomirlari)"
            ],
            "ru": [
                "Цвета национальных флагов Франции и США",
                "Символ мыльной пены, воды и ножниц",
                "Разные цвета волос клиентов",
                "Кровопускание и хирургия (кровь, бинты и вены)"
            ],
            "en": [
                "National flag colors of France and the US",
                "Symbols of shaving foam, water, and razors",
                "Representations of hair colors",
                "Bloodletting surgery (blood, bandages, and veins)"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Qon olish va jarrohlik muolajalari (qon, bint va vena tomirlari)",
            "ru": "Кровопускание и хирургия (кровь, бинты и вены)",
            "en": "Bloodletting surgery (blood, bandages, and veins)"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "O'rta asrlarda sartaroshlar tish sug'urgan va qon olgan: qizil rang arteriya qoni, ko'k rang vena qoni, oq rang esa qon shimdirilgan bintlarni anglatgan.",
            "ru": "В Средневековье цирюльники пускали кровь: красный цвет — кровь, белый — бинты, синий — вены.",
            "en": "Medieval barbers were surgeons who performed bloodletting: red signified arterial blood, blue veins, and white clean bandages."
        },
        "aliases": [
            "qon olish",
            "bint",
            "jarrohlik",
            "krovopuskanie",
            "bloodletting",
            "кровопускание",
            "бинты"
        ]
    },
    {
        "id": "zakovat_150",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bugungi kunda har qadamda takrorlanadigan gaplar uchun ishlatiladigan 'kliche' (cliché) so'zi aslida qanday hodisadan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Откуда происходит слово 'клише', означающее заезженную фразу или речевой штамп?",
            "en": "Attention, deductive question: Where does the word 'cliché', denoting an overused unoriginal phrase or expression, originate mechanically?"
        },
        "options": {
            "uz": [
                "Matbaa bosma qolipi urilganda chiqaradigan tovush",
                "Qadimgi fransuz qulfi nomi",
                "Shoirlarning maxsus qalamchasi",
                "Rasm chiziladigan qog'oz turi"
            ],
            "ru": [
                "Звук штамповки металлической печатной пластины",
                "Название старинного французского дверного замка",
                "Особое перо для записи стихов",
                "Сорт тонкой бумаги для эстампов"
            ],
            "en": [
                "The clicking sound of a metal printing stereotype plate",
                "Name of an ancient French door latch",
                "Special quill pen used by court poets",
                "Type of translucent engraving paper"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Matbaa bosma qolipi urilganda chiqaradigan tovush",
            "ru": "Звук штамповки металлической печатной пластины",
            "en": "The clicking sound of a metal printing stereotype plate"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Fransuz matbaachilarida tez-tez takrorlanadigan matnlar uchun quyilgan metall plastinka matbuotga urilganda 'cliché' degan tovush chiqargan.",
            "ru": "Французские типографы отливали целые готовые фразы на металлической пластине, издававшей при печати щелчок 'клише'.",
            "en": "French letterpress printers cast frequently used words into a single stereotype plate that clicked ('cliché') during stamping."
        },
        "aliases": [
            "matbaa",
            "tovush",
            "shtamp",
            "zvuk",
            "printing plate",
            "звук",
            "типография"
        ]
    },
    {
        "id": "zakovat_151",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Tabiiy kauchuk sutdek oq rangda bo'lishiga qaramay, nima sababdan barcha avtomobil shinalari qora rangda ishlab chiqariladi?",
            "ru": "Внимание, вопрос на логику: Почему автомобильные шины чёрные, хотя натуральный каучук молочно-белого цвета?",
            "en": "Attention, deductive question: Why are automobile tires uniformly black even though natural rubber latex is milky white?"
        },
        "options": {
            "uz": [
                "Qora rang quyosh nurlaridan asraydi",
                "Kauchukka uglerod qurumi (saja) qo'shilgani uchun",
                "Rezina o'z tabiiy holatida qora bo'ladi",
                "Qora rangda loy va kir ko'rinmaydi"
            ],
            "ru": [
                "Чёрный цвет защищает от ультрафиолета",
                "В резину добавлен углеродный технический углерод (сажа)",
                "Резина сама по себе от природы абсолютно чёрная",
                "На чёрном цвете не видно дорожной грязи"
            ],
            "en": [
                "Black color shields from solar ultraviolet",
                "Carbon black is added to the rubber compound",
                "Natural rubber is naturally jet black",
                "Road grime is invisible on black"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Kauchukka uglerod qurumi (saja) qo'shilgani uchun",
            "ru": "В резину добавлен углеродный технический углерод (сажа)",
            "en": "Carbon black is added to the rubber compound"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Uglerod qurumi (uglerod qorasi) shina chidamliligini 10 baravar oshiradi va issiqlikni tarqatib yorilishdan saqlaydi.",
            "ru": "Сажа (углерод) связывается с каучуком на молекулярном уровне, повышая износостойкость в 10 раз.",
            "en": "Carbon black chemically reinforces the vulcanized rubber and dissipates thermal buildup during high-speed rolling."
        },
        "aliases": [
            "saja",
            "qurum",
            "uglerod",
            "carbon black",
            "сажа",
            "углерод"
        ]
    },
    {
        "id": "zakovat_152",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bank cheklaridagi yoki hujjatlardagi imzo qo'yiladigan 'uzoq uzluksiz chiziq' mikroskop ostida qaralganda aslida nima ekanligi ko'rinadi?",
            "ru": "Внимание, вопрос на логику: Что представляет собой сплошная линия для подписи на банковском чеке при рассмотрении под сильной лупой?",
            "en": "Attention, deductive question: What does the solid signature line on a legitimate banking check or bond actually reveal when viewed under magnification?"
        },
        "options": {
            "uz": [
                "Kantselyariya qoidasiga ko'ra chiziq shunday chiziladi",
                "Qog'ozni buklash qulay bo'lishi uchun",
                "Nusxa ko'chirganda loyqalanib ketadigan mikroyozuvlar",
                "Printer siyohini tejash maqsadida"
            ],
            "ru": [
                "Стандартная пунктирная линия бланка",
                "Линия для удобного сгибания чека",
                "Микропечать крошечных слов, расплывающаяся на ксероксе",
                "Способ экономии краски в типографии"
            ],
            "en": [
                "Standard dotted signature rule",
                "Crease line for folding documents",
                "Microprinting of tiny words that blurs when copied",
                "Technique for conserving press ink"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Nusxa ko'chirganda loyqalanib ketadigan mikroyozuvlar",
            "ru": "Микропечать крошечных слов, расплывающаяся на ксероксе",
            "en": "Microprinting of tiny words that blurs when copied"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Chiziq aslida mikroskopik o'lchamdagi harflardan iborat bo'lib, rangli kserokopiya apparati uni o'qiy olmaydi va loyqa chiziqqa aylantiradi.",
            "ru": "Это непрерывный текст микропечати; сканеры и ксероксы мошенников превращают его в смазанную линию.",
            "en": "The line is comprised of microprinted text that photocopiers and scanners cannot resolve, blurring it into an obvious fake."
        },
        "aliases": [
            "mikroyozuv",
            "mikromatn",
            "mikropechat",
            "microprinting",
            "микропечать",
            "микротекст"
        ]
    },
    {
        "id": "zakovat_153",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 1950-yillarda ilk reaktiv yo'lovchi samolyotlari 'De Havilland Comet' havoda to'satdan parchalanavergach, muhandislar derazalarni kvadratdan nima sababdan dumaloq shaklga o'tkazishgan?",
            "ru": "Внимание, вопрос на логику: Почему после катастроф первых реактивных лайнеров 'Комета' иллюминаторы стали делать исключительно круглыми или овальными?",
            "en": "Attention, deductive question: Why were rectangular airplane windows completely redesigned into rounded ovals following the fatal De Havilland Comet jet crashes in 1954?"
        },
        "options": {
            "uz": [
                "Yo'lovchilarga tashqarini ko'rish qulay bo'lishi uchun",
                "Dumaloq oynani ishlab chiqarish arzonroq",
                "Aerodinamik havo qarshiligini kamaytirish uchun",
                "Burchaklardagi ortiqcha mexanik zo'riqish va yoriqlarning oldini olish uchun"
            ],
            "ru": [
                "Пассажирам удобнее смотреть в круглые иллюминаторы",
                "Круглые стекла дешевле в производстве",
                "Для снижения внешнего лобового сопротивления воздуха",
                "Чтобы избежать опасной концентрации напряжений и трещин в углах"
            ],
            "en": [
                "Passengers enjoy circular panoramic views",
                "Round glass panes are cheaper to mold",
                "To reduce external air drag on the fuselage",
                "To prevent dangerous stress concentrations at corners"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Burchaklardagi ortiqcha mexanik zo'riqish va yoriqlarning oldini olish uchun",
            "ru": "Чтобы избежать опасной концентрации напряжений и трещин в углах",
            "en": "To prevent dangerous stress concentrations at corners"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Kvadrat burchaklarda bosim farqi tufayli ulkan zo'riqish to'planadi va metall charchab yorilib ketadi, dumaloq shaklda esa bosim bir tekis taqsimlanadi.",
            "ru": "В прямых углах скапливалось критическое напряжение металла, приводившее к взрывной декомпрессии на высоте.",
            "en": "Sharp 90-degree corners create intense mechanical stress concentrations that cause catastrophic fuselage metal fatigue fractures."
        },
        "aliases": [
            "burchak",
            "zo'riqish",
            "yoriq",
            "napryajenie",
            "stress",
            "трещины",
            "углы"
        ]
    },
    {
        "id": "zakovat_154",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Nima sababdan ko'plab sifatli chizmachilik qalamlari dumaloq emas, aynan olti burchakli (qirrali) qilib yasaladi?",
            "ru": "Внимание, вопрос на логику: Почему большинство классических карандашей делают шестигранными, а не идеально круглыми?",
            "en": "Attention, deductive question: Why are standard drafting and carpentry pencils shaped with a hexagonal cross-section rather than smooth cylinders?"
        },
        "options": {
            "uz": [
                "Nishab chizmachilik stollaridan yumalab tushib ketmasligi uchun",
                "Qo'lda ushlab turish charchatmasligi uchun",
                "Yog'ochni tejash maqsadida",
                "Qalamtaroshda yo'nish oson bo'lishi uchun"
            ],
            "ru": [
                "Чтобы не скатывался с наклонного чертёжного стола",
                "Рука меньше устает при длительном письме",
                "Ради экономии ценных пород древесины",
                "Так его легче затачивать точилкой"
            ],
            "en": [
                "To prevent rolling off tilted drafting tables",
                "Fingers fatigue less during prolonged drawing",
                "To minimize lumber milling waste",
                "To facilitate easier rotary sharpening"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Nishab chizmachilik stollaridan yumalab tushib ketmasligi uchun",
            "ru": "Чтобы не скатывался с наклонного чертёжного стола",
            "en": "To prevent rolling off tilted drafting tables"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Olti burchakli qalam qiya stollarda joyida mahkam turadi va dumalab yerga tushib ichidagi nozik grafit sinishidan saqlanadi.",
            "ru": "Шестигранный карандаш лежит устойчиво на наклонном столе архитектора и не падает на пол, ломая стержень.",
            "en": "Hexagonal facets prevent pencils from rolling off inclined drafting tables, which would fracture the brittle inner graphite core."
        },
        "aliases": [
            "yumalab tushmaslik",
            "dumalamaslik",
            "skativatsya",
            "roll off",
            "не скатывался",
            "падать"
        ]
    },
    {
        "id": "zakovat_155",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 1873-yilda tikuvchi Jacob Davis va Levi Strauss jinsi shimlarning cho'ntak burchaklariga nima sababdan mis parchinlar (klepka) qadashgan?",
            "ru": "Внимание, вопрос на логику: Зачем в 1873 году портной Джейкоб Дэвис укрепил углы карманов джинсов медными заклёпками?",
            "en": "Attention, deductive question: Why did tailor Jacob Davis and Levi Strauss add copper rivets to the pocket corners of denim jeans in 1873?"
        },
        "options": {
            "uz": [
                "Chiroyli dizayn va bezak sifatida",
                "Oltin qumi va og'ir rudalar cho'ntak choklarini yirtib yubormasligi uchun",
                "Askarlar o'q joylashi uchun",
                "Magnit bilan tekshirish uchun"
            ],
            "ru": [
                "Исключительно для красоты и моды",
                "Чтобы карманы не рвались под тяжестью золотых самородков",
                "Чтобы удерживать патроны золотоискателей",
                "Для проверки карманов магнитом"
            ],
            "en": [
                "Strictly decorative aesthetic flair",
                "To stop pockets ripping under heavy gold nuggets",
                "To anchor miner ammunition loops",
                "To enable magnetic pocket inspection"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Oltin qumi va og'ir rudalar cho'ntak choklarini yirtib yubormasligi uchun",
            "ru": "Чтобы карманы не рвались под тяжестью золотых самородков",
            "en": "To stop pockets ripping under heavy gold nuggets"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Konchilar cho'ntaklariga og'ir ruda va qurollarni solganda choklar doimiy yirtilib ketgan, mis mixchalar esa matoni mahkam ushlab turgan.",
            "ru": "Золотоискатели набивали карманы тяжёлыми камнями и инструментами, отчего швы мгновенно лопались.",
            "en": "Miners constantly tore off pocket seams by loading them with heavy ore samples, gold nuggets, and iron tools."
        },
        "aliases": [
            "chok yirtilmasligi",
            "og'ir ruda",
            "karman",
            "shov",
            "pockets ripping",
            "заклёпки",
            "швы"
        ]
    },
    {
        "id": "zakovat_156",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Jinsilarning o'ng old cho'ntagi ichida joylashgan mittigina cho'ntakcha dastlab nima maqsadda tikilgan?",
            "ru": "Внимание, вопрос на логику: Для чего изначально предназначался крошечный кармашек внутри правого переднего кармана джинсов?",
            "en": "Attention, deductive question: What was the original intended function of the tiny rectangular pocket nested inside the right front jeans pocket?"
        },
        "options": {
            "uz": [
                "Tanga va mayda pullar uchun",
                "Gugurt chaqmoqlarini qo'yish uchun",
                "Cho'ntak soatini xavfsiz saqlash uchun",
                "Zippo zajigalkasi uchun"
            ],
            "ru": [
                "Для мелких монет и центов",
                "Для охотничьих спичек",
                "Для карманных часов на цепочке",
                "Для бензиновой зажигалки Zippo"
            ],
            "en": [
                "For loose coins and cents",
                "For waterproof friction matches",
                "To hold a pocket watch safely",
                "For Zippo fuel lighters"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Cho'ntak soatini xavfsiz saqlash uchun",
            "ru": "Для карманных часов на цепочке",
            "en": "To hold a pocket watch safely"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "19-asrda kovboylar va temiryo'lchilar zanjirli cho'ntak soatlarini sinishdan asrash uchun aynan shu kichik cho'ntakchaga solib yurishgan.",
            "ru": "В XIX веке ковбои и рабочие носили в нём карманные часы на цепочке, защищая их от ударов.",
            "en": "In the 1870s, cowboys and railroaders kept their fragile mechanical pocket watches securely protected in this watch pocket."
        },
        "aliases": [
            "cho'ntak soati",
            "soat",
            "chasi",
            "pocket watch",
            "часы",
            "карманные часы"
        ]
    },
    {
        "id": "zakovat_157",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Simsiz ma'lumot uzatish texnologiyasi bo'lgan 'Bluetooth' (Moviy tish) nima sababdan bunday g'alati nomlangan?",
            "ru": "Внимание, вопрос на логику: В честь кого беспроводная технология передачи данных получила название 'Bluetooth' (Синезубый)?",
            "en": "Attention, deductive question: Why was the short-range wireless communication standard named 'Bluetooth'?"
        },
        "options": {
            "uz": [
                "Ixtirochining ko'k tishi bo'lgani uchun",
                "Moviy rangli nurlar orqali uzatilgani uchun",
                "Muzeydagi qadimiy tish sharafiga",
                "Skandinaviya qabilalarini birlashtirgan qirol Garald Moviy tish sharafiga"
            ],
            "ru": [
                "У ведущего инженера был синий зубной протез",
                "Сигнал передавался в синей части спектра",
                "В честь цвета первого светодиода прибора",
                "В честь короля Харальда Синезубого, объединившего племена"
            ],
            "en": [
                "The lead engineer had a blue dental crown",
                "Signal pulses traveled via blue spectrum",
                "In honor of the first blue indicator LED",
                "After King Harald Bluetooth who united Scandinavian tribes"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Skandinaviya qabilalarini birlashtirgan qirol Garald Moviy tish sharafiga",
            "ru": "В честь короля Харальда Синезубого, объединившего племена",
            "en": "After King Harald Bluetooth who united Scandinavian tribes"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Daniya qiroli Garald I (Bluetooth) qabilalarni bitta davlatga birlashtirganidek, ushbu texnologiya ham kompyuter va telefonlarni birlashtiradi.",
            "ru": "Датский король Харальд объединил враждовавшие скандинавские племена, как технология объединила гаджеты.",
            "en": "Just as King Harald Bluetooth united Scandinavia, the Bluetooth protocol united disparate communication platforms."
        },
        "aliases": [
            "harald",
            "garald",
            "moviy tish",
            "синезубый",
            "bluetooth",
            "король"
        ]
    },
    {
        "id": "zakovat_158",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Elektron pochtadagi keraksiz reklama xabarlari nima sababdan konservalangan go'sht nomi bo'lgan 'SPAM' so'zi bilan atala boshlangan?",
            "ru": "Внимание, вопрос на логику: Почему навязчивую рекламную рассылку назвали словом 'спам', позаимствовав имя дешёвых мясных консервов?",
            "en": "Attention, deductive question: Why did unwanted junk emails come to be known by the trademarked canned spiced ham brand 'SPAM'?"
        },
        "options": {
            "uz": [
                "Monti Payton hajviyasida vikiinglar baqirib boshqa gaplarni eshitdirmagani uchun",
                "Spam firmasining xakerlik hujumi tufayli",
                "Bu so'z qisqartma (akronim) bo'lgani uchun",
                "Amerika harbiy kodi bo'lgani uchun"
            ],
            "ru": [
                "Из скетча 'Монти Пайтон', где викинги заглушали разговор криками 'Спам!'",
                "Из-за вирусной атаки мясной компании",
                "Слово является технической аббревиатурой",
                "Секретный код радиосвязи флота США"
            ],
            "en": [
                "From a Monty Python sketch where Vikings shouted 'Spam!' over everyone",
                "Due to a cyberattack by a canned meat maker",
                "The word is an acronym for storage protocol",
                "Secret naval telegraphic transmission code"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Monti Payton hajviyasida vikiinglar baqirib boshqa gaplarni eshitdirmagani uchun",
            "ru": "Из скетча 'Монти Пайтон', где викинги заглушали разговор криками 'Спам!'",
            "en": "From a Monty Python sketch where Vikings shouted 'Spam!' over everyone"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "1970-yilda mashhur ingliz komiklari kafe sahnasida har bir taomga konserva go'shti tiqishtirib, quloqni qomatga keltirgan sahnasidan olingan.",
            "ru": "В скетче 'Monty Python' посетителям навязывали консервы Spam, а хор викингов заглушал диалог криками 'Spam!'.",
            "en": "A 1970 Monty Python sketch depicted a cafe where every menu item included Spam, drowning out all conversation with chanting."
        },
        "aliases": [
            "monti payton",
            "monty python",
            "sketch",
            "консервы",
            "монти пайтон"
        ]
    },
    {
        "id": "zakovat_159",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bugungi kunda nufuzli kinofestival va sammitlarda mehmonlar oldiga qizil gilam to'shalishi an'anasi ilk bor qayerdan boshlangan?",
            "ru": "Внимание, вопрос на логику: Откуда берёт начало традиция расстилать красную дорожку перед почётными гостями на торжествах?",
            "en": "Attention, deductive question: Where did the ceremonial tradition of rolling out a red carpet for dignitaries originate in literature and history?"
        },
        "options": {
            "uz": [
                "Qizil rang chang va loyni yaxshi yashirgani uchun",
                "Qadimgi Yunonistonda qonli gilam faqat xudolar va g'olib shohlar qadami uchun to'shalgan",
                "Qizil bo'yoq eng arzon bo'lgani uchun",
                "Gilamdo'zlar faqat qizil mato to'qigani uchun"
            ],
            "ru": [
                "Красный цвет лучше всего маскировал уличную пыль",
                "В Древней Греции по ней ступали только боги и цари-триумфаторы",
                "Пурпурная краска была самой доступной",
                "Ткачи не умели красить шерсть в другие цвета"
            ],
            "en": [
                "Red dye best concealed street dust",
                "In ancient Greece it was walked upon only by gods and kings",
                "Purple and red dye was the cheapest pigment",
                "Carpet weavers only had access to red madder"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Qadimgi Yunonistonda qonli gilam faqat xudolar va g'olib shohlar qadami uchun to'shalgan",
            "ru": "В Древней Греции по ней ступали только боги и цари-триумфаторы",
            "en": "In ancient Greece it was walked upon only by gods and kings"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Esxilning 'Agamemnon' tragediyasida shoh Troyadan qaytganda uning xotini Klitemnestra oyoqlari ostiga xudolarga loyiq qizil baxmal yo'lak to'shagan.",
            "ru": "В трагедии Эсхила царь Агамемнон ступает по багряному ковру, страшась гнева богов за такое святотатство.",
            "en": "In Aeschylus' play Agamemnon (458 BC), the returning conqueror fears treading upon the crimson tapestries reserved for the immortal gods."
        },
        "aliases": [
            "esxil",
            "agamemnon",
            "yunoniston",
            "боги",
            "греция",
            "agamemnon",
            "gods"
        ]
    },
    {
        "id": "zakovat_160",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Katta tennis to'plarining sirtidagi sariq-yashil tukli (patli) qoplama nima maqsadga xizmat qiladi?",
            "ru": "Внимание, вопрос на логику: Какую важную физическую функцию выполняет пушистый ворсистый покров на теннисном мяче?",
            "en": "Attention, deductive question: What crucial aerodynamic function is served by the fuzzy felt nap covering the surface of modern tennis balls?"
        },
        "options": {
            "uz": [
                "To'p o'yinchilar qo'lidan sirg'alib ketmasligi uchun",
                "Yashil maysaga o'xshab ko'rinishi uchun",
                "Aerodinamik qarshilik hosil qilib, to'p tezligini pasaytirish va parvozni barqarorlashtirish uchun",
                "Zarba ovozini pasaytirish maqsadida"
            ],
            "ru": [
                "Чтобы мяч не скользил в руках игроков",
                "Чтобы мяч гармонировал с цветом корта",
                "Для аэродинамического торможения и стабильности полёта",
                "Для глушения громкого звука удара ракеткой"
            ],
            "en": [
                "To prevent the ball slipping in sweaty hands",
                "To match the green grass on the court",
                "To create aerodynamic drag, slow the ball, and stabilize flight",
                "To muffle the acoustic crack of racket impacts"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Aerodinamik qarshilik hosil qilib, to'p tezligini pasaytirish va parvozni barqarorlashtirish uchun",
            "ru": "Для аэродинамического торможения и стабильности полёта",
            "en": "To create aerodynamic drag, slow the ball, and stabilize flight"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Agar tuklar bo'lmasa, silliq to'p soatiga 300 km tezlikda boshqarib bo'lmaydigan darajada uchib, o'yinni imkonsiz qilgan bo'lardi.",
            "ru": "Без ворса гладкий мяч летел бы с бешеным ускорением, а ворс создаёт завихрения, стабилизируя траекторию.",
            "en": "The felt nap creates aerodynamic boundary layer turbulence that dramatically increases air resistance, making high-speed rallies controllable."
        },
        "aliases": [
            "aerodinamik",
            "tezlikni pasaytirish",
            "qarshilik",
            "tormojenie",
            "aerodynamic",
            "ворс",
            "стабильность"
        ]
    },
    {
        "id": "zakovat_161",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Biron shaxs yoki tashkilot bilan iqtisodiy va ijtimoiy aloqalarni uzishni anglatuvchi 'boykot' so'zi qanday kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Как возникло слово 'бойкот', означающее отказ от общения или сотрудничества?",
            "en": "Attention, deductive question: What historic event gave rise to the term 'boycott' as a form of social and economic protest?"
        },
        "options": {
            "uz": [
                "Boykot ismli dengiz kemasi sharafiga",
                "Bu so'z harbiy hujum atamasi bo'lgani uchun",
                "Qadimgi lotincha so'zdan olingani uchun",
                "Charlz Boykot ismli yer boshqaruvchisiga barcha xalq salom bermay aloqani uzgani uchun"
            ],
            "ru": [
                "В честь военного корабля 'Бойкотт'",
                "Слово означает боевое столкновение",
                "От латинского термина судебного запрета",
                "В честь управляющего Чарльза Бойкотта, которому объявили полную изоляцию"
            ],
            "en": [
                "In honor of the blockade warship HMS Boycott",
                "The term originally designated an armed assault",
                "From a medieval Latin legal injunction",
                "After estate agent Charles Boycott, whom tenant farmers ostracized"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Charlz Boykot ismli yer boshqaruvchisiga barcha xalq salom bermay aloqani uzgani uchun",
            "ru": "В честь управляющего Чарльза Бойкотта, которому объявили полную изоляцию",
            "en": "After estate agent Charles Boycott, whom tenant farmers ostracized"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "1880-yilda Irlandiyada shafqatsiz boshqaruvchi Charlz Boykotga qarshi hech kim xizmat ko'rsatmagan, do'konlar unga non sotmagan, hatto pochtachi xat bermagan.",
            "ru": "В 1880 году ирландцы объявили управляющему Бойкотту бойкот: с ним никто не здоровался и не продавал еду.",
            "en": "In 1880, Irish tenants organized by the Land League isolated estate agent Captain Charles Boycott so thoroughly that no shop would sell to him."
        },
        "aliases": [
            "charlz boykot",
            "boycott",
            "борга",
            "бойкотт",
            "управляющий"
        ]
    },
    {
        "id": "zakovat_162",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Odam yoki buyumning faqat qora qiyofasi (soya chizgisi) nima sababdan 'siluet' deb nomlangan?",
            "ru": "Внимание, вопрос на логику: Почему теневой контурный портрет человека называют словом 'силуэт'?",
            "en": "Attention, deductive question: Why are dark outline shadow portraits called 'silhouettes'?"
        },
        "options": {
            "uz": [
                "Haddan tashqari xasis fransuz moliya vaziri Eten de Siluet sharafiga",
                "Qadimgi soya teatri aktyori sharafiga",
                "Qora bo'yoq ixtirochisi familiyasidan",
                "Venetsiyalik ko'zoynak ustasi nomidan"
            ],
            "ru": [
                "В честь крайне экономного министра финансов Этьена де Силуэта",
                "В честь актёра теневого театра",
                "По фамилии изобретателя чёрной туши",
                "По имени венецианского мастера зеркал"
            ],
            "en": [
                "After French finance minister Étienne de Silhouette, known for penny-pinching",
                "After an 18th-century shadow puppeteer",
                "After the inventor of black India ink",
                "After a Venetian darkroom mirror artisan"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Haddan tashqari xasis fransuz moliya vaziri Eten de Siluet sharafiga",
            "ru": "В честь крайне экономного министра финансов Этьена де Силуэта",
            "en": "After French finance minister Étienne de Silhouette, known for penny-pinching"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Moliya vaziri Siluet o'z saroyini qimmat moybo'yoq portretlar bilan emas, arzon qora qog'oz qiyqimlari bilan bezatgani uchun parijliklar buni masxara qilishgan.",
            "ru": "Министр Силуэт прославился жесткой экономией казны, и его имя стало синонимом дешевых портретов из бумаги.",
            "en": "Étienne de Silhouette imposed severe budget cuts in 1759, causing his name to become synonymous with cheap, rudimentary shadow profile cuts."
        },
        "aliases": [
            "siluet",
            "eten de siluet",
            "vazir",
            "силуэт",
            "министр",
            "silhouette"
        ]
    },
    {
        "id": "zakovat_163",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bugungi kunda dunyo bo'ylab kelinlarning oppoq to'y libosi kiyishi qaysi tarixiy shaxsning to'yidan keyin an'anaga aylangan?",
            "ru": "Внимание, вопрос на логику: Свадьба какой исторической личности сделала белое подвенечное платье мировым стандартом для невест?",
            "en": "Attention, deductive question: Whose high-profile royal wedding in 1840 popularized the modern white wedding gown across Western civilization?"
        },
        "options": {
            "uz": [
                "Qadimdan barcha dinlar faqat oq rangni buyurgani uchun",
                "Qirolicha Viktoriya to'yida ilk bor oq libos kiyib moda yaratgani uchun",
                "Oq mato eng arzon va ommabop bo'lgani uchun",
                "Oq rang tabiatda qish ramzi bo'lgani uchun"
            ],
            "ru": [
                "Все религии издревле требовали исключительно белый цвет",
                "Королева Виктория надела белое кружевное платье, начав мировую моду",
                "Белая ткань была самой дешёвой и доступной",
                "Белый цвет символизировал приход зимы"
            ],
            "en": [
                "Ancient world religions strictly mandated white fabric",
                "Queen Victoria wore a white lace gown in 1840, establishing a trend",
                "Unbleached white cloth was the cheapest available",
                "White symbolized winter solstices"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Qirolicha Viktoriya to'yida ilk bor oq libos kiyib moda yaratgani uchun",
            "ru": "Королева Виктория надела белое кружевное платье, начав мировую моду",
            "en": "Queen Victoria wore a white lace gown in 1840, establishing a trend"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "1840-yilgacha kelinlar o'zlarining eng chiroyli qizil, ko'k yoki yashil liboslarini kiyishgan; Viktoriya oq rangni tanlab jahon to'y sanoatini o'zgartirdi.",
            "ru": "До свадьбы Виктории и принца Альберта в 1840 году невесты выходили замуж в цветных платьях (красных, синих).",
            "en": "Prior to Queen Victoria's 1840 wedding to Prince Albert, brides wore colorful gowns in scarlet, emerald, or sapphire."
        },
        "aliases": [
            "viktoriya",
            "qirolicha viktoriya",
            "victoria",
            "виктория",
            "королева виктория"
        ]
    },
    {
        "id": "zakovat_164",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: O'rta asrlarda qo'lyozma kitoblar sahifalari chetida juda keng bo'sh hoshiyalar (polya) qoldirilishining pragmatik sababi nima edi?",
            "ru": "Внимание, вопрос на логику: Зачем в средневековых рукописях оставляли огромные пустые поля вокруг текста?",
            "en": "Attention, deductive question: What pragmatic preservation reason explained why medieval scribes left exceptionally wide blank margins around precious texts?"
        },
        "options": {
            "uz": [
                "O'quvchilar o'z sharhlarini yozib qoldirishi uchun",
                "Chiroyli bezak va ramkalar chizish uchun",
                "Kitob qurtlari va kemiruvchilar matnga yetib bormasligi uchun",
                "Qog'oz qalin bo'lishini ta'minlash uchun"
            ],
            "ru": [
                "Чтобы читатели записывали свои комментарии",
                "Для рисования золотых миниатюр и рамок",
                "Чтобы книжные черви и мыши не сгрызали драгоценный текст",
                "Для обеспечения прочности переплёта"
            ],
            "en": [
                "So readers could write analytical commentary",
                "To frame gold leaf illuminated miniatures",
                "To prevent bookworms and rodents gnawing away the text",
                "To add structural heft to leather binding"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Kitob qurtlari va kemiruvchilar matnga yetib bormasligi uchun",
            "ru": "Чтобы книжные черви и мыши не сгрызали драгоценный текст",
            "en": "To prevent bookworms and rodents gnawing away the text"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Kitob qurtlari va sichqonlar avval varaqning chetlarini kemiradi; keng hoshiyalar matnning shikastlanmasdan asrlar osha saqlanishiga xizmat qilgan.",
            "ru": "Мыши и книжные черви объедают края пергамента; широкие поля служили буфером, спасавшим текст от уничтожения.",
            "en": "Bookworms and mice nibbled outward page margins first; broad margins sacrificed blank parchment to preserve holy scriptures."
        },
        "aliases": [
            "kemiruvchilar",
            "sichqon",
            "qurt",
            "knijnie chervi",
            "mishi",
            "bookworms",
            "mice",
            "мыши"
        ]
    },
    {
        "id": "zakovat_165",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Jahon adabiyotidagi eng chuqur dramatik janr — 'Tragediya' so'zi qadimgi yunoncha 'tragos' va 'oide' so'zlaridan yasalgan bo'lib, so'zma-so'z qanday ma'noni bildiradi?",
            "ru": "Внимание, вопрос на логику: Что буквально означает греческое слово 'трагедия' (tragos + oide)?",
            "en": "Attention, deductive question: What does the classical Greek word 'tragedy' (from 'tragos' and 'oide') literally translate to?"
        },
        "options": {
            "uz": [
                "Qahramonlar nolasi",
                "Xudolar yig'isi",
                "O'lim marosimi",
                "Echki qo'shig'i (Echki nolasini kuylash)"
            ],
            "ru": [
                "Плач героев",
                "Слёзы богов",
                "Погребальный гимн",
                "Песнь козла"
            ],
            "en": [
                "Lament of heroes",
                "Tears of the gods",
                "Funeral dirge",
                "Goat song"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Echki qo'shig'i (Echki nolasini kuylash)",
            "ru": "Песнь козла",
            "en": "Goat song"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qadimgi Yunonistonda Dionis bayramlarida echki qurbonlik qilingan yoki xor ishtirokchilari echki terisi kiyib nolali qo'shiqlar kuylagan.",
            "ru": "В дионисийских мистериях в жертву приносили козла, а сатиры в козлиных шкурах пели погребальные гимны.",
            "en": "Dionysian religious rites featured the ritual sacrifice of a prize goat, accompanied by choral songs chanted in satyr goat-skins."
        },
        "aliases": [
            "echki qo'shig'i",
            "echki",
            "pesn kozla",
            "goat song",
            "песнь козла"
        ]
    },
    {
        "id": "zakovat_166",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Flamingolar nima sababdan soatlab muzdek suvda faqat bitta oyog'ida turishadi?",
            "ru": "Внимание, вопрос на логику: Почему фламинго часами стоят в воде на одной ноге?",
            "en": "Attention, deductive question: Why do flamingos habitually stand on a single leg for hours in chilly lake water?"
        },
        "options": {
            "uz": [
                "Tanadagi issiqlikni saqlab qolish uchun (termoregulyatsiya)",
                "Ikkinchi oyog'i og'riganligi uchun",
                "Uxlash paytida yiqilmaslik uchun",
                "Suv tubidagi baliqlarni cho'chitmaslik uchun"
            ],
            "ru": [
                "Для сохранения тепла тела (терморегуляция)",
                "Потому что вторая нога затекает",
                "Чтобы не упасть во время сна",
                "Чтобы не пугать рыбу в воде двумя ногами"
            ],
            "en": [
                "To conserve vital body heat (thermoregulation)",
                "Because the other leg cramps up",
                "To prevent falling over in strong winds",
                "To avoid startling fish with two moving legs"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Tanadagi issiqlikni saqlab qolish uchun (termoregulyatsiya)",
            "ru": "Для сохранения тепла тела (терморегуляция)",
            "en": "To conserve vital body heat (thermoregulation)"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qushlarning oyoqlarida pat bo'lmaydi, suv esa havodan 25 marta tezroq issiqlikni tortib oladi. Bitta oyoqni patlar orasiga yashirish issiqlik yo'qotishni 50% ga kamaytiradi.",
            "ru": "Голые ноги птиц быстро отдают тепло в воде; пряча одну ногу в перья, фламинго экономит энергию.",
            "en": "Unfeathered avian legs radiate body heat rapidly into water; tucking one leg into warm breast feathers cuts heat loss in half."
        },
        "aliases": [
            "issiqlik",
            "termoregulyatsiya",
            "teplo",
            "heat",
            "thermoregulation",
            "сохранение тепла"
        ]
    },
    {
        "id": "zakovat_167",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Olimlarning so'nggi kashfiyotlariga ko'ra, zebralarning oq-qora yo'l-yo'l chiziqlari nima uchun xizmat qiladi?",
            "ru": "Внимание, вопрос на логику: Каково истинное эволюционное назначение полос у зебры согласно современным биофизическим опытам?",
            "en": "Attention, deductive question: According to modern entomological and optical research, what is the primary evolutionary function of zebra stripes?"
        },
        "options": {
            "uz": [
                "Yirtqich sherlardan niqoblanish uchun",
                "Tsetse pashshasi va so'nalar chaqishidan himoyalanish uchun",
                "Quyoshda qizib ketmaslik uchun",
                "Podada bir-birini tanish uchun"
            ],
            "ru": [
                "Для маскировки от хищных львов",
                "Для защиты от укусов мухи цеце и слепней",
                "Чтобы не перегреваться под палящим солнцем",
                "Чтобы узнавать сородичей в стаде"
            ],
            "en": [
                "To camouflage against stalking lions in grass",
                "To protect against biting tsetse flies and horseflies",
                "To reflect equatorial sunlight",
                "To help herd members identify relatives"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Tsetse pashshasi va so'nalar chaqishidan himoyalanish uchun",
            "ru": "Для защиты от укусов мухи цеце и слепней",
            "en": "To protect against biting tsetse flies and horseflies"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qonxo'r hasharotlarning murakkab ko'zlari qutblangan yorug'likni yo'l-yo'l chiziqlarda ajrata olmaydi va ular zebraga qo'na olmay chalg'iydi.",
            "ru": "Сложные фасеточные глаза мух цеце дезориентируются поляризацией света на полосах и не могут приземлиться.",
            "en": "The polarized light patterns created by alternating black and white stripes disrupt the landing mechanics of bloodsucking tabanid flies."
        },
        "aliases": [
            "pashsha",
            "tsetse",
            "muha tse-tse",
            "flies",
            "tsetse",
            "слепни",
            "мухи"
        ]
    },
    {
        "id": "zakovat_168",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ko'plab mamlakatlarda o't o'chirish gidrantlarining ustki qismi qizil, to'q sariq, yashil yoki ko'k ranglarga bo'yalganining sababi nima?",
            "ru": "Внимание, вопрос на логику: Зачем верхушки пожарных гидрантов красят в разные цвета (синий, зелёный, оранжевый, красный)?",
            "en": "Attention, deductive question: Why are the caps and bonnets of municipal fire hydrants color-coded in blue, green, orange, or red?"
        },
        "options": {
            "uz": [
                "Qaysi ko'chaga tegishli ekanini bildirish uchun",
                "Qishda muzlash darajasini ko'rsatish uchun",
                "Suv bosimi va oqim tezligini (litr/sekund) bildirish uchun",
                "Shunchaki shahar bezagi sifatida"
            ],
            "ru": [
                "Для обозначения принадлежности к району",
                "Чтобы знать глубину промерзания",
                "Для указания напора и расхода воды (галлонов в минуту)",
                "Для декоративного разнообразия улиц"
            ],
            "en": [
                "To designate neighborhood municipal districts",
                "To show underground freezing depth",
                "To indicate water flow capacity (gallons per minute)",
                "Purely for decorative street aesthetics"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Suv bosimi va oqim tezligini (litr/sekund) bildirish uchun",
            "ru": "Для указания напора и расхода воды (галлонов в минуту)",
            "en": "To indicate water flow capacity (gallons per minute)"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Ranglar o't o'chiruvchilarga gidrantdan sekundiga necha litr suv olish mumkinligini darhol ko'rsatadi (ko'k rang eng kuchli bosimni bildiradi).",
            "ru": "Цвет указывает пожарным напор: синий — более 1500 галлонов в минуту, красный — наименее мощный поток.",
            "en": "NFPA standards color-code hydrants by flow capacity (GPM): blue delivers over 1,500 GPM, while red delivers under 500 GPM."
        },
        "aliases": [
            "suv bosimi",
            "bosim",
            "oqim",
            "napor vodi",
            "water flow",
            "flow capacity",
            "напор"
        ]
    },
    {
        "id": "zakovat_169",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Dengizchilikda kemaning o'ng tomoni 'starboard', chap tomoni esa 'port' deb atalishining tarixiy sababi nimada?",
            "ru": "Внимание, вопрос на логику: Почему в мореплавании правый борт называется 'starboard', а левый — 'port'?",
            "en": "Attention, deductive question: Why is the right side of a vessel termed 'starboard' and the left side termed 'port'?"
        },
        "options": {
            "uz": [
                "Dengizda shamol faqat chapdan esgani uchun",
                "Kapitanlar doim chap tomonda uxlagani uchun",
                "Kema dumi o'ngga og'ib ketgani uchun",
                "Vikinglar boshqaruv kuragini (rulini) o'ng tomonga o'rnatgani uchun"
            ],
            "ru": [
                "Ветер в море чаще дул слева",
                "Каюта капитана всегда была слева",
                "Корма корабля была смещена вправо",
                "Викинги крепили рулевое весло справа (steer-board)"
            ],
            "en": [
                "Prevailing oceanic winds blew from the left",
                "The captain's quarters were on the port side",
                "The ship's stern listed naturally to the right",
                "Vikings mounted the steering oar on the right side"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Vikinglar boshqaruv kuragini (rulini) o'ng tomonga o'rnatgani uchun",
            "ru": "Викинги крепили рулевое весло справа (steer-board)",
            "en": "Vikings mounted the steering oar on the right side"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Vikinglar qayig'ida rul vazifasini o'tovchi kurak o'ng tomonga o'rnatilgan (steer-board), shuning uchun kemalar qirg'oqqa (portga) faqat chap tomoni bilan to'xtagan.",
            "ru": "Рулевое весло (steer) крепилось справа, поэтому швартоваться к пристани (port) можно было только левым бортом.",
            "en": "Early Norsemen steered with an oar on the right ('steer-board'); to avoid damaging it, they docked at the pier on the left ('port') side."
        },
        "aliases": [
            "rul",
            "boshqaruv kuragi",
            "rulevoe veslo",
            "steering oar",
            "весло",
            "викинги"
        ]
    },
    {
        "id": "zakovat_170",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Zamonaviy bank seyflarida kod kiritilgandan so'ng eshik darhol ochilmay, kamida 15-30 daqiqa vaqt o'tishi shart qilib belgilanganining sababi nima?",
            "ru": "Внимание, вопрос на логику: Зачем в банковских хранилищах ставят замки с задержкой времени на 15–30 минут после ввода верного кода?",
            "en": "Attention, deductive question: Why do commercial bank vaults incorporate mandatory 15-to-30-minute time-delay locks after the correct code is entered?"
        },
        "options": {
            "uz": [
                "Qurolli bosqinchilar xodimlarni zudlik bilan seyfni ochishga majburlashini bartaraf etish uchun",
                "Bank xodimlari uxlab qolmasligi uchun",
                "Kechalari seyf qizib ketmasligi uchun",
                "Elektr toki uzilib qolsa himoyalanish uchun"
            ],
            "ru": [
                "Чтобы грабители не могли заставить кассира открыть сейф мгновенно",
                "Чтобы кассиры не засыпали на посту",
                "Чтобы электронные платы не перегревались",
                "На случай отключения электричества"
            ],
            "en": [
                "To prevent armed robbers forcing staff to open the safe immediately",
                "To keep tellers alert during night shifts",
                "To prevent electronic circuit boards overheating",
                "In case of lightning-induced electrical blackouts"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Qurolli bosqinchilar xodimlarni zudlik bilan seyfni ochishga majburlashini bartaraf etish uchun",
            "ru": "Чтобы грабители не могли заставить кассира открыть сейф мгновенно",
            "en": "To prevent armed robbers forcing staff to open the safe immediately"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Bosqinchilar politsiya yetib kelguncha bir necha daqiqa kutishga jur'at eta olmaydi, bu esa qurolli bosqinlarni ma'nosiz qiladi.",
            "ru": "Бандиты не могут ждать полчаса из-за скорого прибытия полиции, что делает вооружённый налёт бессмысленным.",
            "en": "Armed bank robbers rely on rapid grab-and-flee tactics; facing a 30-minute mechanical lockout guarantees police will arrive."
        },
        "aliases": [
            "bosqinchilar",
            "vaqt kechikishi",
            "rabbery",
            "time delay",
            "грабители",
            "задержка времени"
        ]
    },
    {
        "id": "zakovat_171",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bugungi kunda ishni topshirishning oxirgi muddati ma'nosida ishlatiladigan 'Dedlayn' (Deadline — o'lim chizig'i) so'zi AQSh fuqarolar urushida qanday paydo bo'lgan?",
            "ru": "Внимание, вопрос на логику: Откуда в Гражданскую войну в США возник термин 'дедлайн' (deadline — линия смерти)?",
            "en": "Attention, deductive question: Where did the modern business term 'deadline' originate during the American Civil War?"
        },
        "options": {
            "uz": [
                "Gazeta bosilishining oxirgi soati",
                "Harbiy asirlar lageridagi o'lim chizig'i (undan o'tganlar otib tashlangan)",
                "Sud hukmi ijro etiladigan muddat",
                "Telegraf simlarining oxirgi nuqtasi"
            ],
            "ru": [
                "Крайний час сдачи газеты в типографию",
                "Черта вокруг лагеря военнопленных, за пересечение которой расстреливали",
                "Срок исполнения судебного приговора",
                "Конечная точка телеграфного кабеля"
            ],
            "en": [
                "Final hour for printing a newspaper",
                "A prison boundary line; crossing it meant being shot dead",
                "Judicial execution deadline",
                "End of a telegraph cable"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Harbiy asirlar lageridagi o'lim chizig'i (undan o'tganlar otib tashlangan)",
            "ru": "Черта вокруг лагеря военнопленных, за пересечение которой расстреливали",
            "en": "A prison boundary line; crossing it meant being shot dead"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Andersonvill asirlar lagerida to'siqdan 5 metr narida yerga chiziq tortilgan bo'lib, unga qadam bosgan asirlar soqchilar tomonidan ogohlantirishsiz otilgan.",
            "ru": "В лагере Андерсонвилль черта на земле обозначала границу, шаг за которую карался немедленным расстрелом без предупреждения.",
            "en": "In Civil War military stockades like Andersonville, a boundary was designated where guards shot any captive on sight."
        },
        "aliases": [
            "o'lim chizig'i",
            "asirlar",
            "lager",
            "rasstrel",
            "deadline",
            "черта смерти",
            "лагерь"
        ]
    },
    {
        "id": "zakovat_172",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Tovlamachilik va tahdid orqali pul talab qilishni anglatuvchi 'blekmeyl' (Blackmail) so'zining asl tarixiy ma'nosi nima?",
            "ru": "Внимание, вопрос на логику: Каково буквальное историческое происхождение термина 'шантаж/вымогательство' (blackmail)?",
            "en": "Attention, deductive question: What was the original medieval meaning of the extortion term 'blackmail' in the Scottish Highlands?"
        },
        "options": {
            "uz": [
                "Qora qog'ozga yozilgan xat",
                "Qora bo'yoq bilan belgilangan uy",
                "Shotlandiyada bosqinchilarga o'lpon sifatida berilgan qora mollar (qoramol)",
                "Qora kiyimli qaroqchilar xizmati"
            ],
            "ru": [
                "Письмо с угрозами на чёрной бумаге",
                "Дом, помеченный чёрной краской",
                "Дань скотом (чёрным скотом), которую платили горцам за защиту от набегов",
                "Налог на чёрную ткань для траура"
            ],
            "en": [
                "Black-inked extortion demand letter",
                "A house marked with black coal",
                "Tribute paid in black cattle to Scottish raiders for protection",
                "Tax levied on black mourning cloth"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Shotlandiyada bosqinchilarga o'lpon sifatida berilgan qora mollar (qoramol)",
            "ru": "Дань скотом (чёрным скотом), которую платили горцам за защиту от набегов",
            "en": "Tribute paid in black cattle to Scottish raiders for protection"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Shotlandiyada 'mail' qadimgi tilda soliq degani bo'lib, qora mollar (black cattle) talonchilik qilmasliklari uchun tog'lik qaroqchilarga o'lpon sifatida to'langan.",
            "ru": "Шотландские фермеры платили разбойникам дань 'чёрным' скотом (mail = налог), чтобы их деревни не сжигали.",
            "en": "Scottish border tenants paid protection rent in 'black cattle' ('mail') to highland clans to deter plundering."
        },
        "aliases": [
            "qoramol",
            "shotlandiya",
            "o'lpon",
            "skot",
            "blackmail",
            "дань",
            "скот"
        ]
    },
    {
        "id": "zakovat_173",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Plastik sut idishlarining (baklajkalarning) yon tomonida nima sababdan dumaloq chuqurcha (botiqlik) yasaladi?",
            "ru": "Внимание, вопрос на логику: Зачем на боку больших пластиковых кувшинов для молока выдувают круглую впадину?",
            "en": "Attention, deductive question: Why do gallon plastic milk jugs feature a circular indented dimple on their side walls?"
        },
        "options": {
            "uz": [
                "Idishni qo'lda ushlash qulay bo'lishi uchun",
                "Plastmassani tejash maqsadida",
                "Sut yog'liligini ko'rsatuvchi belgi",
                "Idish tushib ketsa yoki muzlasa, tashqariga bo'rtib chiqib idish yorilishidan saqlaydi"
            ],
            "ru": [
                "Удобная выемка для пальцев руки",
                "Экономия полиэтилена при выдуве",
                "Метка жирности молока",
                "При падении или замерзании она выгибается наружу, спасая канистру от разрыва"
            ],
            "en": [
                "Ergonomic finger grip indentation",
                "To conserve plastic during blow molding",
                "A calibrated marker of milk fat content",
                "It expands outward if dropped or frozen, preventing rupture"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Idish tushib ketsa yoki muzlasa, tashqariga bo'rtib chiqib idish yorilishidan saqlaydi",
            "ru": "При падении или замерзании она выгибается наружу, спасая канистру от разрыва",
            "en": "It expands outward if dropped or frozen, preventing rupture"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Agar to'la idish yerga tushib ketsa, gidravlik zarba tufayli bu doiracha tashqariga shishib chiqadi va qopqoq yoki choklar portlab ketishiga yo'l qo'ymaydi.",
            "ru": "При ударе или расширении льда круглая мембрана выщелкивается наружу, гася гидроудар и сохраняя швы.",
            "en": "When dropped, the hydraulic pressure spike pops the concave dimple outward, absorbing shock and preventing seam bursting."
        },
        "aliases": [
            "botiqlik",
            "yorilishdan saqlash",
            "bosim",
            "gidroudar",
            "rupture",
            "разрыв",
            "выгибается"
        ]
    },
    {
        "id": "zakovat_174",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Supermarketlardagi qadoqlangan nonlarning og'ziga qadalgan plastik qisqichlar (klipsalar) rangi (ko'k, yashil, qizil, oq, sariq) nimani bildiradi?",
            "ru": "Внимание, вопрос на логику: Что означает цвет пластиковой клипсы на пакете с нарезанным хлебом в супермаркете?",
            "en": "Attention, deductive question: What standard retail information is communicated by the color-coded plastic twist tags on commercial bread bags?"
        },
        "options": {
            "uz": [
                "Non qaysi haftaning kunida pishirilganligini bildiradi",
                "Nonning navi va un sifatini",
                "Xamirda shakar miqdorini",
                "Nonvoyxona smenasini"
            ],
            "ru": [
                "День недели, в который был выпечен хлеб",
                "Сорт муки и категорию хлеба",
                "Количество сахара в тесте",
                "Номер бригады пекарей"
            ],
            "en": [
                "The day of the week on which the bread was baked",
                "The flour grade and grain blend",
                "Sugar concentration in the dough",
                "The bakery shift identifier"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Non qaysi haftaning kunida pishirilganligini bildiradi",
            "ru": "День недели, в который был выпечен хлеб",
            "en": "The day of the week on which the bread was baked"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Har bir rang haftaning 5 ta kuniga to'g'ri keladi (masalan, dushanba ko'k, seshanba yashil), bu do'kondorlarga eskirgan nonlarni darhol javondan olishga yordam beradi.",
            "ru": "Цвета соответствуют дням недели по алфавиту, помогая мерчандайзерам быстро снимать несвежий хлеб.",
            "en": "Standard color codes correspond to delivery days (e.g., Monday blue, Tuesday green), allowing workers to quickly rotate stock."
        },
        "aliases": [
            "kun",
            "hafta kuni",
            "haftaning kuni",
            "den nedeli",
            "day of week",
            "день недели"
        ]
    },
    {
        "id": "zakovat_175",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Dastlabki baland osmono'par binolarda odamlar liftning sekin harakatlanishidan norozi bo'lishganda, muhandislar lift ichiga qanday oddiy narsani o'rnatib muammoni hal qilishgan?",
            "ru": "Внимание, вопрос на логику: Как владельцы первых небоскрёбов решили жалобы жильцов на 'слишком медленные лифты' без ускорения моторов?",
            "en": "Attention, deductive question: When early skyscraper tenants complained that elevators were too slow, how did building managers solve the psychological problem without faster motors?"
        },
        "options": {
            "uz": [
                "Lift motoriga tushadigan og'irlikni kamaytirish uchun",
                "Yo'lovchilar o'z aksiga qarab vaqt o'tganini va torlikni sezmasligi uchun",
                "Favqulodda yorug'likni qaytarish maqsadida",
                "Kuzatuv kameralarini yashirish uchun"
            ],
            "ru": [
                "Для снижения веса кабины лифта",
                "Чтобы пассажиры смотрели на себя, отвлекаясь от ожидания и тесноты",
                "Для лучшего отражения аварийного света",
                "Чтобы прятать скрытые камеры охраны"
            ],
            "en": [
                "To reduce the structural weight of the elevator cab",
                "Passengers look at themselves, distracting them from waiting and tight space",
                "To reflect emergency illumination",
                "To conceal security camera lenses"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Yo'lovchilar o'z aksiga qarab vaqt o'tganini va torlikni sezmasligi uchun",
            "ru": "Чтобы пассажиры смотрели на себя, отвлекаясь от ожидания и тесноты",
            "en": "Passengers look at themselves, distracting them from waiting and tight space"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Liftga ko'zgular o'rnatilgach, odamlar o'z soch va kiyimlarini to'g'rilash bilan band bo'lib, lift sekinligidan shikoyat qilishni butunlay to'xtatgan.",
            "ru": "Установка зеркал в лифтах заняла внимание людей разглядыванием себя, и жалобы на медлительность прекратились.",
            "en": "Installing mirrors in elevator cabs distracted passengers with grooming, eliminating complaints about ride duration."
        },
        "aliases": [
            "ko'zgu",
            "oyna",
            "zerkalo",
            "mirror",
            "зеркало",
            "отвлечение"
        ]
    },
    {
        "id": "zakovat_176",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bosh oshpazlarning an'anaviy baland oq qalpoqlarida (toque) aynan 100 ta qatlama (burma) bo'lishining sababi nima?",
            "ru": "Внимание, вопрос на логику: Что традиционно символизируют ровно 100 складок на высоком белом колпаке шеф-повара?",
            "en": "Attention, deductive question: What legendary culinary mastery milestone do the traditional 100 pleats on a grand chef's toque represent?"
        },
        "options": {
            "uz": [
                "Fransiya qiroli sharafiga 100 kun",
                "Pazandaning yoshi va stajini",
                "Mohir oshpaz tuxumni pishirishning 100 xil usulini bilishi ramzi",
                "Oshxonadagi 100 xil ziravorni"
            ],
            "ru": [
                "100 дней осады Парижа",
                "Стаж работы шеф-повара в годах",
                "100 способов приготовления яиц, которыми владеет шеф-повар",
                "100 классических французских специй"
            ],
            "en": [
                "100 days of the Paris siege",
                "The chef's years of culinary apprenticeship",
                "100 distinct culinary techniques for cooking eggs",
                "100 classic French master spices"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Mohir oshpaz tuxumni pishirishning 100 xil usulini bilishi ramzi",
            "ru": "100 способов приготовления яиц, которыми владеет шеф-повар",
            "en": "100 distinct culinary techniques for cooking eggs"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Klassik fransuz gastronomiyasida bu oshpazning oddiygina tuxumdan 100 xil turli xil nafis taom tayyorlay olish mahoratini bildirgan.",
            "ru": "Во французской кухне считалось, что истинный мастер знает ровно 100 различных рецептов приготовления яиц.",
            "en": "In haute cuisine tradition, each pleat celebrated a different technique the chef had mastered for preparing eggs."
        },
        "aliases": [
            "tuxum",
            "tuxum pishirish",
            "yaytso",
            "100 sposobov",
            "eggs",
            "яйца",
            "колпак"
        ]
    },
    {
        "id": "zakovat_177",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Yo'lni belgilanmagan joydan kesib o'tishni bildiruvchi 'Jaywalking' so'zidagi 'jay' 20-asr boshlarida Amerikada kimlarga nisbatan haqoratli laqab bo'lgan?",
            "ru": "Внимание, вопрос на логику: Кого в начале XX века в США презрительно называли словом 'jay', от которого пошёл термин 'jaywalking'?",
            "en": "Attention, deductive question: Who did the derogatory slang 'jay' originally refer to in early 1900s America before forming the term 'jaywalking'?"
        },
        "options": {
            "uz": [
                "Qushlar kabi uchib o'tuvchi odam",
                "Ko'chani chopib o'tadigan bezori",
                "Chorrahadagi tilanchi",
                "Shahar yo'l harakati qoidalarini bilmaydigan qishloqi (provinsial)"
            ],
            "ru": [
                "Человек, перебегающий дорогу как птица сойка",
                "Уличный хулиган-зачинщик",
                "Нищий на перекрёстке дорог",
                "Неопытный деревенщина, не знающий правил городского движения"
            ],
            "en": [
                "Pedestrian darting across like a blue jay bird",
                "A reckless street gang ruffian",
                "A panhandler loitering in traffic intersections",
                "An inexperienced rural rustic who was oblivious to city traffic"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Shahar yo'l harakati qoidalarini bilmaydigan qishloqi (provinsial)",
            "ru": "Неопытный деревенщина, не знающий правил городского движения",
            "en": "An inexperienced rural rustic who was oblivious to city traffic"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "'Jay' so'zi katta shaharga birinchi marta kelib qolib, ot-aravalardan va avtomobillardan qochishni bilmay ko'chaning o'rtasida dovdirab qolgan qishloqi odamlarga aytilgan.",
            "ru": "Словом 'jay' горожане обзывали простофиль из деревни, которые глазели по сторонам и путались под колесами.",
            "en": "In the early 1900s, 'jay' was urban slang for an unsophisticated country rube who gaped at buildings and walked in traffic."
        },
        "aliases": [
            "qishloqi",
            "jay",
            "derevenshina",
            "rural rustic",
            "деревенщина"
        ]
    },
    {
        "id": "zakovat_178",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Amerika qishloqlaridagi qadimiy omborxonalarning (barn) devorlari nima sababdan doimo qizil rangga bo'yalgan?",
            "ru": "Внимание, вопрос на логику: Почему традиционные фермерские амбары в США исторически красили исключительно в красный цвет?",
            "en": "Attention, deductive question: Why were traditional American rural barns historically painted a distinctive dark red color?"
        },
        "options": {
            "uz": [
                "Zang (temir oksidi) va zig'ir moyi eng arzon va zamburug'dan asrovchi bo'yoq bo'lgan",
                "Qizil rang bo'ron paytida uzoqdan ko'ringani uchun",
                "Qoramollar qizil rangni yaxshi ko'rgani uchun",
                "Qizil bo'yoq davlat tomonidan tekin berilgan"
            ],
            "ru": [
                "Ржавчина (оксид железа) и льняное масло были самым дешёвым антисептиком",
                "Красный цвет виден издалека в метель",
                "Коровы охотнее шли в красный амбар",
                "Красная краска бесплатно выдавалась правительством"
            ],
            "en": [
                "Rust (iron oxide) mixed with linseed oil was cheap and killed mold",
                "Red was visible from afar during blizzards",
                "Dairy cows preferred entering red barns",
                "Red paint was distributed free by government"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Zang (temir oksidi) va zig'ir moyi eng arzon va zamburug'dan asrovchi bo'yoq bo'lgan",
            "ru": "Ржавчина (оксид железа) и льняное масло были самым дешёвым антисептиком",
            "en": "Rust (iron oxide) mixed with linseed oil was cheap and killed mold"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Fermerlar yog'ochni chirishdan asrash uchun zig'ir moyiga zanglagan temir kukunini aralashtirishgan; temir oksidi arzon bo'yoq va kuchli zamburug' qotili bo'lgan.",
            "ru": "Фермеры смешивали дешёвое льняное масло с оксидом железа (ржавчиной), создавая защитное и ядовитое для плесени покрытие.",
            "en": "Early farmers concocted cheap sealant by blending linseed oil, milk, and iron oxide (rust), which inhibited moss and fungi."
        },
        "aliases": [
            "zang",
            "temir oksidi",
            "rjavchina",
            "iron oxide",
            "rust",
            "ржавчина",
            "оксид железа"
        ]
    },
    {
        "id": "zakovat_179",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: O'zini yomon his qilish yoki betoblikni anglatuvchi 'Under the weather' (Ob-havo ostida) iborasi qayerdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Откуда возникло английское выражение 'under the weather' в значении 'нездоровится'?",
            "en": "Attention, deductive question: What nautical condition gave rise to the English idiom 'under the weather' meaning feeling unwell?"
        },
        "options": {
            "uz": [
                "Yomg'irda soyabonsiz qolgan",
                "Dengiz kasalligi tutganda to'lqin va bo'rondan qochib pastki palubaga tushgan",
                "Sovuq havoda qalin kiyinmagan",
                "Bulutli kunda kayfiyati tushgan"
            ],
            "ru": [
                "Промокли под проливным дождем",
                "При морской болезни спускались в трюм под укрытие от непогоды",
                "Замерзли на ветру без теплой одежды",
                "Испытали хандру от пасмурной погоды"
            ],
            "en": [
                "Got drenched outside in a torrential rain",
                "Seasick sailors retreated below deck to shelter from the weather",
                "Froze in the gale without heavy woolens",
                "Suffered low spirits from overcast skies"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Dengiz kasalligi tutganda to'lqin va bo'rondan qochib pastki palubaga tushgan",
            "ru": "При морской болезни спускались в трюм под укрытие от непогоды",
            "en": "Seasick sailors retreated below deck to shelter from the weather"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Dengizchilar qattiq to'lqinlarda ko'ngli ayniganda kemaning pastki yopiq xonalariga (ob-havo va shamoldan xoli joyga) jo'natilgan.",
            "ru": "Укачавшихся от качки моряков отправляли в нижние каюты — 'под защиту непогоды' (under the weather).",
            "en": "Sailors incapacitated by seasickness were sent below deck to recover underneath the exposure of foul weather."
        },
        "aliases": [
            "dengiz kasalligi",
            "paluba",
            "tryum",
            "morskaya bolezn",
            "seasick",
            "трюм",
            "морская болезнь"
        ]
    },
    {
        "id": "zakovat_180",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Golf to'plari sirtida 300 dan 500 tagacha mayda chuqurchalar (dimples) bo'lishining aerodinamik siri nimada?",
            "ru": "Внимание, вопрос на логику: Зачем на поверхности мяча для гольфа делают сотни круглых ямочек?",
            "en": "Attention, deductive question: Why is the surface of modern golf balls engineered with hundreds of dimples rather than being completely smooth?"
        },
        "options": {
            "uz": [
                "Koptok tayoqchadan sirg'alib ketmasligi uchun",
                "Koptokni quyishda qoliplardan qolgan izlar",
                "Aerodinamik havo qarshiligini kamaytirib, uchish masofasini ikki baravar oshiradi",
                "O'yinchilar koptokni o'tlar orasida oson topishi uchun"
            ],
            "ru": [
                "Мяч меньше скользит по головке клюшки",
                "Следствие технологического дефекта формы",
                "Создают турбулентный пограничный слой, удваивая дальность полёта",
                "Чтобы мяч легче находился в густой траве"
            ],
            "en": [
                "The clubface grips the ball better on impact",
                "Residual mold marks from manufacturing",
                "Creates a turbulent boundary layer, halving drag and doubling range",
                "Makes the ball easier to locate in deep rough"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Aerodinamik havo qarshiligini kamaytirib, uchish masofasini ikki baravar oshiradi",
            "ru": "Создают турбулентный пограничный слой, удваивая дальность полёта",
            "en": "Creates a turbulent boundary layer, halving drag and doubling range"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Chuqurchalar to'p ortidagi havoning uyurmasini kichraytiradi, bu esa qarshilikni 50% ga kamaytiradi va silliq to'pdan ikki baravar uzoqroqqa uchishini ta'minlaydi.",
            "ru": "Ямочки затягивают турбулентный слой ближе к мячу, уменьшая вихревой след и воздушное торможение.",
            "en": "Dimples induce turbulence in the boundary air layer, delaying airflow separation and halving aerodynamic drag."
        },
        "aliases": [
            "aerodinamika",
            "uchish masofasi",
            "qarshilik",
            "dalnost",
            "aerodynamics",
            "drag",
            "турбулентность"
        ]
    },
    {
        "id": "zakovat_181",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Basketbol to'pi yuzasida minglab mayda bo'rtiqchalar (pufakchalar) bo'lishining sababi nima?",
            "ru": "Внимание, вопрос на логику: Зачем вся поверхность баскетбольного мяча покрыта тысячами мелких резиновых пупырышков?",
            "en": "Attention, deductive question: Why is the entire leather or rubber exterior of a basketball textured with thousands of tiny pebbles?"
        },
        "options": {
            "uz": [
                "To'p polda yaxshiroq sakrashi uchun",
                "Ichidagi havoni ushlab turish maqsadida",
                "To'pning vaznini kamaytirish uchun",
                "Terlagan qo'llar bilan ushlaganda sirpanib ketmasligi (ishqalanish) uchun"
            ],
            "ru": [
                "Для лучшего отскока от паркета",
                "Для удержания воздуха под давлением",
                "Для облегчения веса мяча",
                "Для сцепления со скользкими от пота ладонями игроков"
            ],
            "en": [
                "To enhance vertical bounce height off hardwood",
                "To seal internal pressurized bladder seams",
                "To reduce the overall weight of the leather",
                "To increase friction against sweaty palms for superior grip"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Terlagan qo'llar bilan ushlaganda sirpanib ketmasligi (ishqalanish) uchun",
            "ru": "Для сцепления со скользкими от пота ладонями игроков",
            "en": "To increase friction against sweaty palms for superior grip"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Bu bo'rtiqchalar to'pning kaftga tegish yuzasini oshiradi va o'yinchilarning terlagan barmoqlari to'pni mahkam tutishiga imkon beradi.",
            "ru": "Пупырышки увеличивают площадь контакта и предотвращают выскальзывание мяча из потных рук игроков.",
            "en": "The pebble texture generates mechanical grip and friction, preventing the ball from slipping from sweaty hands during dribbling."
        },
        "aliases": [
            "sirpanmaslik",
            "ishqalanish",
            "terlagan qo'l",
            "stseplenie",
            "grip",
            "friction",
            "сцепление"
        ]
    },
    {
        "id": "zakovat_182",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Tungi og'ir navbatchilikni anglatuvchi 'Graveyard shift' (Qabriston smenasi) iborasi qanday tarixiy xavf bilan bog'liq?",
            "ru": "Внимание, вопрос на логику: С каким мрачным медицинским страхом прошлого связано выражение 'кладбищенская смена' (graveyard shift)?",
            "en": "Attention, deductive question: What historic medical dread led to the creation of the nighttime 'graveyard shift' watch?"
        },
        "options": {
            "uz": [
                "Tiriklayin ko'milganlarni qutqarish uchun qabrdagi qo'ng'iroqlarni poylash",
                "Kasalxonalarda tunda o'liklarni tashish",
                "Tungi navbatchilikda qabr qazish",
                "Shaharda o'g'rilarni ushlash"
            ],
            "ru": [
                "Дежурство у могил с колокольчиками для спасения случайно погребённых",
                "Вывоз умерших по ночам в больницах",
                "Рытьё могил при свете факелов",
                "Поимка расхитителей гробниц ночью"
            ],
            "en": [
                "Watching cemetery bells tied to corpses in case of premature burial",
                "Transporting hospital casualties after hours",
                "Digging burial plots by torchlight",
                "Nighttime patrols against grave robbers"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Tiriklayin ko'milganlarni qutqarish uchun qabrdagi qo'ng'iroqlarni poylash",
            "ru": "Дежурство у могил с колокольчиками для спасения случайно погребённых",
            "en": "Watching cemetery bells tied to corpses in case of premature burial"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Letargik uyqudagi odamlar xatolan ko'milganda, ularning qo'liga bog'langan ip yerdagi qo'ng'iroqni chalgan; qorovul tuni bilan bu tovushni eshitish uchun hushyor turgan.",
            "ru": "В XIX веке сторож дежурил ночью, чтобы услышать звон колокольчика, если погребённый очнётся в гробу.",
            "en": "Guards watched cemeteries overnight to listen for bells rung by strings tied to the hands of prematurely buried victims."
        },
        "aliases": [
            "tiriklayin ko'milgan",
            "qo'ng'iroq",
            "qabr",
            "pogrebenie",
            "kolokolchik",
            "graveyard",
            "premature burial"
        ]
    },
    {
        "id": "zakovat_183",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Siyosatda qonunlarni o'z manfaatiga moslashtirishni bildiruvchi 'Lobbizm' (Lobbying) so'zi qanday binoning qismidan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: От какого помещения в здании парламента произошло политическое понятие 'лоббизм'?",
            "en": "Attention, deductive question: What architectural part of a government building gave birth to the political practice of 'lobbying'?"
        },
        "options": {
            "uz": [
                "Lordlar palatasining maxfiy xonasi",
                "Deputatlarni koridorda tutib olib talab bildirgan odamlar yig'iladigan joy",
                "Angliya qirolining ov uyi",
                "Sud majlislari zali"
            ],
            "ru": [
                "Тайная комната Палаты лордов",
                "Вестибюль (лобби) парламента, где просители перехватывали депутатов",
                "Охотничий домик короля",
                "Зал судебных заседаний"
            ],
            "en": [
                "The private antechamber of the House of Lords",
                "The entrance lobby of parliament where petitioners accosted lawmakers",
                "The royal hunting lodge",
                "The central judicial court bench"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Deputatlarni koridorda tutib olib talab bildirgan odamlar yig'iladigan joy",
            "ru": "Вестибюль (лобби) парламента, где просители перехватывали депутатов",
            "en": "The entrance lobby of parliament where petitioners accosted lawmakers"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Britaniya parlamenti yoki Vashingtondagi mehmonxona dahlizida (lobby) oddiy fuqarolar qonun chiqaruvchilarni ovlab, o'z talablarini aytishgan.",
            "ru": "В вестибюле (lobby) британской Палаты общин избиратели караулили депутатов, прося поддержать закон.",
            "en": "Citizens gathered in the entrance lobby of the British House of Commons to plead with members before debates."
        },
        "aliases": [
            "lobby",
            "vestibyul",
            "dahliz",
            "koridor",
            "вестибюль",
            "лобби"
        ]
    },
    {
        "id": "zakovat_184",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Bouling keglilari nima sababdan to'g'ri silindr emas, aynan ingichka bo'yinli va pastki qismi keng noksimon shaklda yasaladi?",
            "ru": "Внимание, вопрос на логику: Почему кегли для боулинга имеют характерную форму бутылки с узкой шейкой и широким центром тяжести?",
            "en": "Attention, deductive question: Why are tenpin bowling pins uniquely contoured with a narrow bottleneck and bulging belly rather than straight blocks?"
        },
        "options": {
            "uz": [
                "Koptok kelib urilishi qulay bo'lishi uchun",
                "Yog'ochni tejash maqsadida",
                "Urilganda yonidagi boshqa keglilarni zanjirli reaksiyada yiqitishi uchun",
                "Avtomatik mexanizm ko'tarishi oson bo'lishi uchun"
            ],
            "ru": [
                "Чтобы мяч легче попадал по центру",
                "Ради экономии кленовой древесины",
                "Чтобы падение одной кегли вызывало цепную реакцию и сбивало соседние",
                "Чтобы механизм-пинсеттер легче хватал их"
            ],
            "en": [
                "To make the sweet spot easier for the ball to hit",
                "To save hard rock maple wood",
                "So falling pins strike neighbors in an explosive chain reaction",
                "To help pinsetting machines grasp the neck"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Urilganda yonidagi boshqa keglilarni zanjirli reaksiyada yiqitishi uchun",
            "ru": "Чтобы падение одной кегли вызывало цепную реакцию и сбивало соседние",
            "en": "So falling pins strike neighbors in an explosive chain reaction"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Kegli yiqilganda aylanib harakatlanadi va o'z bo'yni hamda qorni bilan qo'shni keglilarga urilib, to'liq 'strayk' qilishga zamin yaratadi.",
            "ru": "Бутылочная форма заставляет сбитую кеглю лететь кувырком, увлекая за собой веером остальные кегли.",
            "en": "The bottleneck profile ensures struck pins bounce horizontally and spin dynamically, scattering adjoining pins into a strike."
        },
        "aliases": [
            "zanjirli reaksiya",
            "strayk",
            "yiqitish",
            "tsepnaya reaktsiya",
            "chain reaction",
            "цепная реакция"
        ]
    },
    {
        "id": "zakovat_185",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Gazlangan ichimliklar quyiladigan alyuminiy bankalarning tagi nima sababdan ichkariga qarab botiq (gumbazsimon) qilib yasaladi?",
            "ru": "Внимание, вопрос на логику: Почему донышко алюминиевой банки для газировки делают сильно вогнутым внутрь?",
            "en": "Attention, deductive question: Why are the bottom bases of aluminum carbonated beverage cans manufactured with an inward concave dome?"
        },
        "options": {
            "uz": [
                "Bankani barmoq bilan ushlash qulay bo'lishi uchun",
                "Suyuqlik hajmini kamaytirish maqsadida",
                "Sovutgichga qo'yganda tez sovishi uchun",
                "Gazlangan ichimlikning ichki yuqori bosimiga chidash uchun (arka effekti)"
            ],
            "ru": [
                "Банку удобнее удерживать пальцами снизу",
                "Для визуального увеличения объёма напитка",
                "Для более быстрого охлаждения в холодильнике",
                "Вогнутый купол работает как арка, выдерживая высокое давление газа"
            ],
            "en": [
                "To provide a thumb grip for drinking",
                "To visually exaggerate beverage volume",
                "To accelerate cooling in refrigerators",
                "The inward dome functions as an arch, resisting internal gas pressure"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Gazlangan ichimlikning ichki yuqori bosimiga chidash uchun (arka effekti)",
            "ru": "Вогнутый купол работает как арка, выдерживая высокое давление газа",
            "en": "The inward dome functions as an arch, resisting internal gas pressure"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Ichidagi karbonat angidrid gazi ulkan bosim hosil qiladi; botiq gumbaz arxitekturadagi arka kabi bosimni chetlarga tarqatadi va metallni yirtilishdan saqlaydi.",
            "ru": "Углекислый газ давит с силой до 6 атмосфер; вогнутое дно распределяет нагрузку на стенки, как купол собора.",
            "en": "Internal carbonation can exceed 90 psi; the concave dome functions like an architectural arch, distributing stress without buckling."
        },
        "aliases": [
            "ichki bosim",
            "arka",
            "gaz bosimi",
            "davlenie gaza",
            "pressure",
            "давление газа",
            "купол"
        ]
    },
    {
        "id": "zakovat_186",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ser Isaak Nyuton Britaniya Qirollik zarbxonasi boshlig'i bo'lganida, tangalarning yon chetiga mayda qirrali tirqishlar (gurt) kiritishni buyurganining sababi nima edi?",
            "ru": "Внимание, вопрос на логику: Зачем Исаак Ньютон на посту смотрителя Монетного двора ввёл обязательные насечки (гурт) на ребро всех монет?",
            "en": "Attention, deductive question: Why did Sir Isaac Newton, as Master of the Royal Mint, mandate milled serrations (reeding) on the edges of all gold and silver coins?"
        },
        "options": {
            "uz": [
                "Firibgarlar qimmatbaho metallni tanga chetidan qirqib o'g'irlashiga yo'l qo'ymaslik uchun",
                "Tanga qo'ldan sirg'alib ketmasligi uchun",
                "Ko'zi ojizlar tangani ushlab tanishi uchun",
                "Tanga mashinalari qabul qilishi uchun"
            ],
            "ru": [
                "Чтобы мошенники не спиливали и не срезали золото с краёв монет",
                "Чтобы монета не выскальзывала из пальцев",
                "Чтобы слепые различали номинал на ощупь",
                "Для приёма монеты в автоматах"
            ],
            "en": [
                "To stop thieves filing or shaving precious metal off coin edges",
                "To prevent the coin slipping from moist fingers",
                "To enable visually impaired people to feel denominations",
                "For calibration in automated coin-operated vending machines"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Firibgarlar qimmatbaho metallni tanga chetidan qirqib o'g'irlashiga yo'l qo'ymaslik uchun",
            "ru": "Чтобы мошенники не спиливали и не срезали золото с краёв монет",
            "en": "To stop thieves filing or shaving precious metal off coin edges"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Tirqishlar bo'lmasa, qaroqchilar tanga chetidan oltin-kumushni qirqib olib, tangani yana muomalaga kiritishgan; gurt shikastlansa darhol sezilgan.",
            "ru": "До насечек мошенники срезали ножницами стружку драгметалла с краев; насечки мгновенно выдавали обрезанную монету.",
            "en": "Unscrupulous merchants used clippers to shave silver from coin circumferences; milled ridges made any clipping instantly obvious."
        },
        "aliases": [
            "tangani qirqish",
            "oltinni o'g'irlash",
            "gurt",
            "spilivanie",
            "clipping",
            "гурт",
            "спиливание"
        ]
    },
    {
        "id": "zakovat_187",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Nima sababdan dunyo bo'ylab barcha svetoforlarda to'xtash signali sifatida aynan qizil rang tanlangan?",
            "ru": "Внимание, вопрос на логику: Какова физическая причина выбора именно красного цвета для запрещающего сигнала светофора?",
            "en": "Attention, deductive question: What optical physics reason dictated the universal selection of red as the stop signal for traffic lights?"
        },
        "options": {
            "uz": [
                "Qizil rang qon va xavf ramzi bo'lgani uchun",
                "Qizil rang eng uzun to'lqin uzunligiga ega bo'lib, tuman va changda kam sochilishi tufayli",
                "Qizil svetodiodlar eng arzon bo'lgani uchun",
                "Odam ko'zi faqat qizil rangni tez payqagani uchun"
            ],
            "ru": [
                "Красный цвет ассоциируется с огнём и опасностью",
                "Красный свет имеет наибольшую длину волны и меньше рассеивается в тумане",
                "Красные стекла светофоров были дешевле всего",
                "Человеческий глаз быстрее всего устаёт от красного"
            ],
            "en": [
                "Red universally symbolizes blood and aggression",
                "Red light has the longest wavelength and scatters least in fog",
                "Red optical glass lenses were the cheapest to cast",
                "The human retina fatigues quickest under red photons"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Qizil rang eng uzun to'lqin uzunligiga ega bo'lib, tuman va changda kam sochilishi tufayli",
            "ru": "Красный свет имеет наибольшую длину волны и меньше рассеивается в тумане",
            "en": "Red light has the longest wavelength and scatters least in fog"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Reley sochilishi qonuniga ko'ra, qizil rang atmosferadagi chang, yomg'ir va tuman zarralarida eng kam sochiluvchi to'lqindir va eng uzoqdan ko'rinadi.",
            "ru": "Красный свет имеет максимальную длину волны в оптическом спектре и пробивает туман и дождь на максимальную дистанцию.",
            "en": "Due to Rayleigh scattering, red photons have the longest wavelength in the visible spectrum, penetrating rain, dust, and fog with minimal dispersal."
        },
        "aliases": [
            "to'lqin uzunligi",
            "tuman",
            "sochilmaslik",
            "dlina volni",
            "wavelength",
            "длина волны",
            "туман"
        ]
    },
    {
        "id": "zakovat_188",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: AQSh va ko'plab mamlakatlarda maktab avtobuslari nima sababdan aynan maxsus 'National School Bus Glossy Yellow' sariq rangiga bo'yaladi?",
            "ru": "Внимание, вопрос на логику: Почему школьные автобусы красят в особый яркий жёлто-оранжевый цвет, а не в красный?",
            "en": "Attention, deductive question: Why are American school buses painted in a distinctive 'National School Bus Glossy Yellow' rather than bright safety red?"
        },
        "options": {
            "uz": [
                "Sariq bo'yoq boshqa ranglardan ancha arzon",
                "Bolalar sariq rangni juda yaxshi ko'radi",
                "Insonning periferik (chetki) ko'rishi bu sariq rangni qizildan 1,24 baravar tez payqaydi",
                "Kechalari sariq rang qora bo'lib ko'rinadi"
            ],
            "ru": [
                "Жёлтая краска для автобусов была самой дешёвой",
                "Дети интуитивно тянутся к жёлтому цвету",
                "Периферическое зрение человека замечает этот оттенок в 1,24 раза быстрее красного",
                "Ночью жёлтый цвет кажется флуоресцентным"
            ],
            "en": [
                "Yellow paint was subsidized and economical",
                "Schoolchildren intuitively gravitate toward yellow",
                "Human peripheral vision detects this yellow hue 1.24 times faster than red",
                "Yellow appears phosphorescent at night under headlights"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Insonning periferik (chetki) ko'rishi bu sariq rangni qizildan 1,24 baravar tez payqaydi",
            "ru": "Периферическое зрение человека замечает этот оттенок в 1,24 раза быстрее красного",
            "en": "Human peripheral vision detects this yellow hue 1.24 times faster than red"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "1939-yilda olim Frank Cyr tomonidan o'tkazilgan tadqiqotlar sariq rang haydovchining yon nigohiga (chetki ko'rishiga) boshqa har qanday rangdan tezroq urilishini isbotlagan.",
            "ru": "Исследования показали, что боковое (периферическое) зрение водителя реагирует на этот спектр жёлтого быстрее всего.",
            "en": "Scientific testing proved that human lateral peripheral vision detects this specific yellow-orange frequency 1.24 times faster than bright red."
        },
        "aliases": [
            "periferik ko'rish",
            "sariq",
            "yon ko'rish",
            "perifericheskoe zrenie",
            "peripheral vision",
            "периферическое зрение"
        ]
    },
    {
        "id": "zakovat_189",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Jarrohlar operatsiya xonasida oq xalat emas, nima sababdan yashil yoki ko'k rangli kiyim kiyishadi?",
            "ru": "Внимание, вопрос на логику: Почему хирурги в операционной носят зелёную или сине-голубую форму, а не традиционные белые халаты?",
            "en": "Attention, deductive question: Why do surgeons wear green or blue scrubs in operating rooms rather than standard white lab coats?"
        },
        "options": {
            "uz": [
                "Yashil rangda dog'lar ko'rinmaydi",
                "Bemorlarni tinchlantirish uchun",
                "Yashil mato bakteriyalarni o'ldiradi",
                "Qonga uzoq qaraganda to'r pardada paydo bo'ladigan qizil dog'ni neytrallash uchun"
            ],
            "ru": [
                "На зелёной ткани меньше видны пятна крови",
                "Чтобы успокаивать нервничающих пациентов",
                "Зелёные красители обладают антисептическим свойством",
                "Для нейтрализации остаточного зрительного эффекта после взгляда на алую кровь"
            ],
            "en": [
                "Blood stains appear invisible on dark green cloth",
                "To soothe anxious patients on the gurney",
                "Green textile dye possesses antiseptic qualities",
                "To neutralize retinal red afterimage illusions caused by looking at blood"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Qonga uzoq qaraganda to'r pardada paydo bo'ladigan qizil dog'ni neytrallash uchun",
            "ru": "Для нейтрализации остаточного зрительного эффекта после взгляда на алую кровь",
            "en": "To neutralize retinal red afterimage illusions caused by looking at blood"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Uzoq vaqt qizil qonga qaragan ko'z oq devorga qarasa, to'r pardada chalg'ituvchi yashil-ko'k arvoh dog'lar ko'rinadi; yashil kiyim bu ko'rish toliqishini yo'qotadi.",
            "ru": "Долгий взгляд на красные органы утомляет рецепторы; взгляд на белое давал бы иллюзорные зелёные пятна-призраки.",
            "en": "Staring at red blood fatigues retinal cone cells; shifting gaze to a white wall generates green illusory afterimages that blue/green scrubs neutralize."
        },
        "aliases": [
            "qizil dog'",
            "to'r parda",
            "afterimage",
            "neytrallash",
            "сетчатка",
            "остаточное изображение",
            "послеобраз"
        ]
    },
    {
        "id": "zakovat_190",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Vino shishalarining tubidagi chuqur botiqlik (fransuzcha 'punt') nima maqsadga xizmat qiladi?",
            "ru": "Внимание, вопрос на логику: Зачем в дне винных бутылок делается глубокое коническое углубление (пунт)?",
            "en": "Attention, deductive question: What structural and oenological purpose is served by the deep indentation ('punt') at the bottom of wine bottles?"
        },
        "options": {
            "uz": [
                "Shisha mustahkamligini oshirish va sharob cho'kindilarini chetda to'plash uchun",
                "Shishaga kamroq sharob sig'dirish uchun",
                "Shisha ustiga muz qo'yish maqsadida",
                "Qo'lda ushlab turishni osonlashtirish uchun"
            ],
            "ru": [
                "Увеличивает прочность стекла под давлением и собирает осадок у краёв",
                "Чтобы обмануть покупателя меньшим объёмом вина",
                "Чтобы насыпать лёд под дно бутылки",
                "Для облегчения машинной укупорки"
            ],
            "en": [
                "Strengthens bottle integrity against pressure and traps sediment at edges",
                "To deceptively diminish the internal liquid volume",
                "To allow ice cubes to be packed underneath",
                "To assist automated mechanical bottling claws"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Shisha mustahkamligini oshirish va sharob cho'kindilarini chetda to'plash uchun",
            "ru": "Увеличивает прочность стекла под давлением и собирает осадок у краёв",
            "en": "Strengthens bottle integrity against pressure and traps sediment at edges"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Punt bosimni butun korpusga teng taqsimlab shishani yorilishdan saqlaydi (ayniqsa shampanda) va qadimiy vinolardagi cho'kindi halqaga to'planib, quyishda qadahga tushmaydi.",
            "ru": "Пунт распределяет внутреннее давление углекислоты (в шампанском) и не даёт осадку взбалтываться при разливе.",
            "en": "The punt distributes internal gas pressure outward and creates a perimeter trough where heavy tannin sediment settles undisturbed."
        },
        "aliases": [
            "punt",
            "shisha mustahkamligi",
            "cho'kindi",
            "osadok",
            "davlenie",
            "sediment",
            "пунт",
            "осадок"
        ]
    },
    {
        "id": "zakovat_191",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Birovning aybi uchun nohaq javobgar qilingan odamga nisbatan aytiladigan 'Qurbonlik echkisi' (Scapegoat / Kozel otpushcheniya) iborasining manbai nima?",
            "ru": "Внимание, вопрос на логику: Откуда происходит библейское выражение 'козёл отпущения' (scapegoat)?",
            "en": "Attention, deductive question: What ancient religious ritual is the historical source of the idiom 'scapegoat'?"
        },
        "options": {
            "uz": [
                "Qurbonlik qilingan eng chiroyli qo'chqor",
                "Yom-Kipur marosimida butun jamoat gunohlari yuklanib cho'lga haydalgan echki",
                "Bo'rilar podaga hujum qilganda yem bo'lgan echki",
                "Cho'ponga bo'ysunmay adashib ketgan hayvon"
            ],
            "ru": [
                "Самый красивый жертвенный баран в храме",
                "Козёл, на которого возлагали грехи общины и изгоняли в пустыню на Йом-Кипур",
                "Животное, брошенное волкам для спасения стада",
                "Упрямый козёл, заблудившийся в горах"
            ],
            "en": [
                "The most prized ram offered at the altar",
                "A goat loaded with the sins of the community and banished on Yom Kippur",
                "An animal thrown to a wolf pack to save the herd",
                "A stubborn livestock animal lost in the hills"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Yom-Kipur marosimida butun jamoat gunohlari yuklanib cho'lga haydalgan echki",
            "ru": "Козёл, на которого возлагали грехи общины и изгоняли в пустыню на Йом-Кипур",
            "en": "A goat loaded with the sins of the community and banished on Yom Kippur"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qadimgi yahudiylarning Gunohlarni kechirish kunida bosh kohin qo'llarini echkining boshiga qo'yib, xalqning barcha gunohlarini unga o'tkazgan va uni Azazel cho'liga haydab yuborgan.",
            "ru": "В праздник Йом-Кипур первосвященник возлагал руки на козла, перенося на него грехи народа, и отсылал в пустыню.",
            "en": "During Yom Kippur in Leviticus, the high priest symbolically laid the sins of Israel upon a live goat, banishing it into the wilderness of Azazel."
        },
        "aliases": [
            "echki",
            "gunoh",
            "yom-kipur",
            "kozel otpusheniya",
            "scapegoat",
            "козёл отпущения",
            "грехи"
        ]
    },
    {
        "id": "zakovat_192",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Metrolar va savdo markazlaridagi eskalatorlarning ikki yon chetiga pastdan o'rnatilgan qattiq cho'tkalar aslida nima vazifani bajaradi?",
            "ru": "Внимание, вопрос на логику: Для чего на самом деле служат щётки вдоль нижних боковин ступеней эскалатора?",
            "en": "Attention, deductive question: What crucial safety function is performed by the continuous rows of stiff nylon bristles lining the skirts of escalators?"
        },
        "options": {
            "uz": [
                "Eskalator zinalarini changdan tozalash uchun",
                "Oyoq kiyimini yurish paytida sayqallash uchun",
                "Oyoq kiyimi va shnurkalari yon tirqishga tushib qisilib qolishining oldini olish uchun",
                "Statik elektr zaryadini yerga o'tkazish uchun"
            ],
            "ru": [
                "Для автоматической чистки ступеней от пыли",
                "Чтобы пассажиры могли чистить обувь на ходу",
                "Чтобы обувь и шнурки пассажиров не затягивало в зазор между ступенью и стеной",
                "Для снятия статического электричества с перил"
            ],
            "en": [
                "To sweep away dust and grit from moving steps",
                "To provide an automated shoe polish brush for passengers",
                "To prevent shoes and laces from being caught in the side gap",
                "To ground static electrical charges from handrails"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Oyoq kiyimi va shnurkalari yon tirqishga tushib qisilib qolishining oldini olish uchun",
            "ru": "Чтобы обувь и шнурки пассажиров не затягивало в зазор между ступенью и стеной",
            "en": "To prevent shoes and laces from being caught in the side gap"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Cho'tkalar odamga oyoq kiyimini devorga juda yaqin qo'yganini jismoniy his ettirib, poyabzal va uzun kiyimlarning tishli mexanizmga kirib ketishidan asraydi.",
            "ru": "Щётки не чистят обувь, а служат тактильным барьером, не давая ноге приближаться к опасной щели механизма.",
            "en": "The deflection brushes serve as a tactile warning, keeping feet and shoelaces away from the dangerous step-to-skirt entrapment gap."
        },
        "aliases": [
            "shnurka",
            "qisilib qolish",
            "oyoq kiyimi",
            "zazor",
            "shnurki",
            "brushes",
            "зазор",
            "шнурки"
        ]
    },
    {
        "id": "zakovat_193",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 1937-yilda Sylvan Goldman supermarket aravachalariga buklanuvchi bolalar o'rindig'ini qo'shganining asosiy tijoriy sababi nima edi?",
            "ru": "Внимание, вопрос на логику: Какая главная коммерческая причина побудила изобретателя тележек Сильвана Голдмана добавить в них откидное сиденье для ребёнка?",
            "en": "Attention, deductive question: What was the revolutionary commercial motivation behind Sylvan Goldman adding child fold-out seats to shopping carts in 1947?"
        },
        "options": {
            "uz": [
                "Bolalar tovarlarni buzib qo'ymasligi uchun",
                "Aravachaning muvozanatini saqlash maqsadida",
                "Faqat xavfsizlik qoidalariga rioya qilish uchun",
                "Kichik bolali onalar xaridni shoshmasdan davom ettirishi va ko'proq savdo qilishi uchun"
            ],
            "ru": [
                "Чтобы дети не хватали и не разбивали товары с полок",
                "Для улучшения баланса и устойчивости тележки",
                "Исключительно по требованию детских омбудсменов",
                "Чтобы матери с малышами дольше ходили по магазину и покупали больше"
            ],
            "en": [
                "To stop children grabbing and breaking merchandise",
                "To stabilize the cart's center of gravity",
                "Strictly to comply with municipal safety ordinances",
                "To keep mothers shopping comfortably longer, increasing sales"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Kichik bolali onalar xaridni shoshmasdan davom ettirishi va ko'proq savdo qilishi uchun",
            "ru": "Чтобы матери с малышами дольше ходили по магазину и покупали больше",
            "en": "To keep mothers shopping comfortably longer, increasing sales"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Bola qo'lda ko'tarilsa yoki do'konda yugursa, ona tezda toliqib do'kondan chiqib ketardi; aravachaga o'tirg'izilgan bola onaga savdo zalida erkinroq va uzoqroq aylanib ko'proq narsa xarid qilish imkonini berdi.",
            "ru": "Уставшие матери с плачущими детьми на руках спешили на кассу; посадив ребёнка в тележку, они увеличили средний чек в разы.",
            "en": "Mothers previously cut grocery trips short when children grew tired; seating toddlers allowed relaxed shopping, boosting supermarket revenues."
        },
        "aliases": [
            "bolalar o'rindig'i",
            "ko'proq savdo",
            "onalar",
            "pokupki",
            "shopping cart",
            "тележки",
            "покупки"
        ]
    },
    {
        "id": "zakovat_194",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Jinsi shimlari yillar davomida kiyilganda o'ziga xos chiroyli oqargan izlar (fade) hosil qilishi va aynan ko'k rangda bo'lishining kimyoviy sababi nima?",
            "ru": "Внимание, вопрос на логику: Какова химическая причина того, что джинсы классического цвета индиго так красиво и индивидуально вытираются со временем?",
            "en": "Attention, deductive question: What unique chemical property of indigo dye allows blue jeans to fade gracefully along wear creases over time?"
        },
        "options": {
            "uz": [
                "Indigo bo'yog'i paxta tolasining faqat ustki yuzasiga yopishib, ichiga kirmaydi",
                "Ko'k rang changni ko'rsatmaydi",
                "Dengizchilar faqat ko'k rangni kiyishgan",
                "Ko'k bo'yoq eng arzon sintetik rang bo'lgan"
            ],
            "ru": [
                "Краситель индиго связывается только с поверхностью хлопковой нити",
                "Синий цвет не привлекает полевых вредителей",
                "Шахтёры и фермеры требовали цвет морской волны",
                "Синяя краска была единственной термостойкой"
            ],
            "en": [
                "Indigo dye adheres only to the surface of the cotton fiber",
                "Blue pigmentation repels subterranean burrowing pests",
                "Laborers demanded sea-toned work apparel",
                "Blue dye was uniquely thermal-resistant"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Indigo bo'yog'i paxta tolasining faqat ustki yuzasiga yopishib, ichiga kirmaydi",
            "ru": "Краситель индиго связывается только с поверхностью хлопковой нити",
            "en": "Indigo dye adheres only to the surface of the cotton fiber"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Indigo molekulasi paxta tolasi o'zagiga kirmay, faqat tolaning tashqi qobig'iga yopishadi; kiyganda tashqi qatlam qirilib, ichki oppoq tola ko'rina boshlaydi.",
            "ru": "Индиго не проникает внутрь нити, а образует корку на поверхности. При трении краска сходит, обнажая белый хлопок.",
            "en": "Indigo dye molecules cannot penetrate deep inside cotton fibers, coating only the exterior; friction abrades the surface, exposing the white core."
        },
        "aliases": [
            "indigo",
            "oqargan izlar",
            "yuza",
            "краситель",
            "индиго",
            "вытираются",
            "surface dye"
        ]
    },
    {
        "id": "zakovat_195",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Arximed vannadan yalang'och holda 'Evrika!' (Topdim!) deb baqirib ko'chaga yugurib chiqqanda, aynan qaysi fizik qonuniyatni kashf qilgan edi?",
            "ru": "Внимание, вопрос на логику: Что именно открыл Архимед в ванне, заставившее его с криком 'Эврика!' выбежать на улицу Сиракуз?",
            "en": "Attention, deductive question: What physical principle did Archimedes realize while stepping into a public bath in Syracuse that made him shout 'Eureka!'?"
        },
        "options": {
            "uz": [
                "Sovun ko'pigi suv ustida suzib yurganini ko'rgan",
                "Vannaga tushganda tanasi o'z hajmiga teng suvni siqib chiqarganini anglagan",
                "Suv harorati pasayganini o'lchagan",
                "Suv ostida nafas olish yo'lini topgan"
            ],
            "ru": [
                "Заметил, как мыльная пена всплывает на поверхность",
                "Осознал, что погружённое тело вытесняет объём воды, равный объёму тела",
                "Измерил охлаждение воды от погружения",
                "Придумал способ дышать под водой через тростинку"
            ],
            "en": [
                "Observed soap bubbles floating on the meniscus",
                "Realized that his submerged body displaced a volume of water equal to his own",
                "Measured thermal cooling from immersion",
                "Invented an underwater breathing reed"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Vannaga tushganda tanasi o'z hajmiga teng suvni siqib chiqarganini anglagan",
            "ru": "Осознал, что погружённое тело вытесняет объём воды, равный объёму тела",
            "en": "Realized that his submerged body displaced a volume of water equal to his own"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Arximed shoh Giyeron tojining ichida kumush aralashmasi bor-yo'qligini tojning hajmini suvga botirib aniqlash mumkinligini tushunib yetgan.",
            "ru": "Архимед понял, как определить объём короны сложной формы по вытесненной воде и уличить ювелира в краже золота.",
            "en": "Archimedes realized he could calculate the precise volume of King Hiero's irregular crown by measuring water displacement to catch a gold thief."
        },
        "aliases": [
            "suvni siqib chiqarish",
            "hajm",
            "arximed",
            "vitesnenie vodi",
            "displacement",
            "архимед",
            "вытеснение"
        ]
    },
    {
        "id": "zakovat_196",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Marafon yugurishining rasmiy masofasi nega 40 yoki 42 km emas, aynan g'alati 42 kilometru 195 metr qilib belgilangan?",
            "ru": "Внимание, вопрос на логику: Почему официальная дистанция марафонского бега составляет именно 42 километра 195 метров?",
            "en": "Attention, deductive question: Why is the official Olympic marathon distance standardized to exactly 42 kilometers and 195 meters (26 miles 385 yards)?"
        },
        "options": {
            "uz": [
                "Marafon qadimiy jang maydoni shunday masofada bo'lgan",
                "Olimpiada stadioniga 26 marta aylanib kirish uchun",
                "1908-yilgi London Olimpiadasida qirolicha saroyining derazasi oldidan start berilgani uchun",
                "Gretsiya parlamenti maxsus qonun chiqargani uchun"
            ],
            "ru": [
                "Древняя дистанция от Марафона до Афин была именно такой",
                "Чтобы уложиться в 26 кругов стадиона",
                "В 1908 году в Лондоне старт перенесли под окна детской Виндзорского замка",
                "Парламент Греции издал специальный указ о точной длине"
            ],
            "en": [
                "The ancient route from Marathon to Athens measured precisely that",
                "To round out exactly 26 stadium laps",
                "At the 1908 London Games the start was moved beneath Windsor Castle nursery",
                "The Greek parliament codified that imperial distance by statute"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "1908-yilgi London Olimpiadasida qirolicha saroyining derazasi oldidan start berilgani uchun",
            "ru": "В 1908 году в Лондоне старт перенесли под окна детской Виндзорского замка",
            "en": "At the 1908 London Games the start was moved beneath Windsor Castle nursery"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Britaniya qirolichasi Aleksandra talabi bilan marafon Vindzor qasri bolalar xonasi ostidan boshlanib, stadiondagi qirolicha lojasi ro'parasida tugagan.",
            "ru": "По просьбе королевской семьи старт марафона в 1908 году дали у Виндзорского замка, а финиш — прямо перед королевской ложей стадиона.",
            "en": "In 1908, the British royal family requested the race start directly beneath the Windsor Castle nursery and end in front of the Royal Box."
        },
        "aliases": [
            "vindzor",
            "london 1908",
            "qirolicha",
            "виндзор",
            "марафон 1908",
            "windsor",
            "marathon 1908"
        ]
    },
    {
        "id": "zakovat_197",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: McDonald's, Burger King, Pizza Hut va boshqa mashhur tezkor ovqatlanish tarmoqlari o'z logotiplarida nima sababdan asosan qizil va sariq ranglardan foydalanishadi?",
            "ru": "Внимание, вопрос на логику: Почему фастфуд-гиганты (McDonald’s, Burger King) поголовно используют в оформлении сочетание красного и жёлтого цветов?",
            "en": "Attention, deductive question: Why do fast-food giants almost universally construct their brand color palettes around combinations of red and yellow?"
        },
        "options": {
            "uz": [
                "Qizil va sariq bo'yoqlar eng arzon bo'lgan",
                "Taomdagi go'sht va pishloq ramzi bo'lgani uchun",
                "Kechasi ko'cha chiroqlarida ko'rinishi uchun",
                "Bu ranglar ishtahani qo'zg'atadi va odamni tezroq ovqatlanib ketishga undaydi"
            ],
            "ru": [
                "Красная и жёлтая краска для вывесок стоила дешевле всего",
                "Символизируют цвет мяса и сыра в бургере",
                "Чтобы вывеска лучше читалась в свете фар ночью",
                "Они возбуждают аппетит и подсознательно поторапливают поесть и уйти"
            ],
            "en": [
                "Red and yellow sign paint was the most economical",
                "They represent ketchup and mustard in burgers",
                "To maximize night billboard luminescence",
                "They trigger appetite and unconsciously urge diners to eat quickly and leave"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Bu ranglar ishtahani qo'zg'atadi va odamni tezroq ovqatlanib ketishga undaydi",
            "ru": "Они возбуждают аппетит и подсознательно поторапливают поесть и уйти",
            "en": "They trigger appetite and unconsciously urge diners to eat quickly and leave"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Rang psixologiyasida qizil rang ishtaha va tezlikni uyg'otadi, sariq esa quvonch beradi; bu kombinatsiya mijozlarning stolda uzoq o'tirmay, tezda ketishini ta'minlaydi.",
            "ru": "Красный цвет учащает пульс и вызывает аппетит, а жёлтый ассоциируется с радостью; вместе они стимулируют быструю сменяемость гостей.",
            "en": "The 'Ketchup and Mustard' psychological theory: red induces urgency and salivary stimulation while yellow radiates warmth, speeding table turnover."
        },
        "aliases": [
            "ishtaha",
            "tez ketish",
            "psixologiya",
            "appetit",
            "appetite",
            "аппетит",
            "психология цвета"
        ]
    },
    {
        "id": "zakovat_198",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Harbiy va yo'lovchi kemalarining ichki eshiklarida nima sababdan odam qoqilib ketadigan darajada baland temir ostonalar (komingslar) qilinadi?",
            "ru": "Внимание, вопрос на логику: Зачем в дверных проёмах на кораблях делают высокие металлические пороги (комингсы), о которые постоянно спотыкаются новички?",
            "en": "Attention, deductive question: Why are interior watertight bulkhead doorways on ships fitted with raised step-over sills (coamings)?"
        },
        "options": {
            "uz": [
                "To'lqin yoki avariya paytida suv qo'shni germetik bo'linmalarga oqib o'tmasligi uchun",
                "Dengizchilarni qoqilib tushishdan hushyor saqlash uchun",
                "Kemaning qovurg'a ramkasini mustahkamlash uchun",
                "Kalamushlar xonalar orasida o'tmasligi uchun"
            ],
            "ru": [
                "Чтобы вода при пробое или волне не переливалась в соседние водонепроницаемые отсеки",
                "Чтобы матросы высоко поднимали ноги при беге",
                "Для усиления продольной жесткости палубы",
                "Чтобы корабельные крысы не перебегали между каютами"
            ],
            "en": [
                "To stop water spilling into adjoining watertight compartments during flooding",
                "To force sailors to lift their boots while running",
                "To reinforce deck structural longitudinal stiffness",
                "To prevent shipboard rats crawling between cabins"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "To'lqin yoki avariya paytida suv qo'shni germetik bo'linmalarga oqib o'tmasligi uchun",
            "ru": "Чтобы вода при пробое или волне не переливалась в соседние водонепроницаемые отсеки",
            "en": "To stop water spilling into adjoining watertight compartments during flooding"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Agar kemaning bitta bo'lmasi teshilsa va suv kelsa, baland ostonalar suvning qo'shni bo'lmalarga to'kilib ketishini to'xtatadi va kema cho'kishining oldini oladi.",
            "ru": "Высокий комингс удерживает слой воды на палубе при затоплении одного отсека, сохраняя непотопляемость судна.",
            "en": "Raised coamings prevent sloshing floodwater from cascading from a compromised compartment into adjacent watertight sections."
        },
        "aliases": [
            "suv o'tmasligi",
            "germetik",
            "komings",
            "voda",
            "komings",
            "coamings",
            "комингсы",
            "затопление"
        ]
    },
    {
        "id": "zakovat_199",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Har bir dengiz mayoqining chirog'i bir xil yonib turmay, nima sababdan ma'lum soniyalarda va o'ziga xos ritmda o'chib-yonadi (miltillaydi)?",
            "ru": "Внимание, вопрос на логику: Почему каждый маяк в мире имеет свой собственный уникальный световой ритм и интервал вспышек?",
            "en": "Attention, deductive question: Why does every coastal lighthouse operate on an individualized recurring rhythm and frequency of light flashes and eclipses?"
        },
        "options": {
            "uz": [
                "Chiroq qizib ketishining oldini olish uchun",
                "Dengizchilar tunda qaysi mayoq va qirg'oq ekanligini xaritada aniqlashi uchun",
                "Elektr energiyasini tejash maqsadida",
                "Mayoqlarni bir-biri bilan aloqa qilishi uchun"
            ],
            "ru": [
                "Чтобы мощная лампа маяка не перегревалась",
                "Чтобы штурманы по уникальному коду вспышек определяли координаты на карте",
                "Ради экономии дорогого керосина или тока",
                "Для оптической телеграфной связи между маяками"
            ],
            "en": [
                "To prevent high-wattage lighthouse bulbs overheating",
                "So navigators can match the unique flash signature to nautical charts",
                "To conserve kerosene fuel and battery power",
                "To establish optical telegraph links between towers"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Dengizchilar tunda qaysi mayoq va qirg'oq ekanligini xaritada aniqlashi uchun",
            "ru": "Чтобы штурманы по уникальному коду вспышек определяли координаты на карте",
            "en": "So navigators can match the unique flash signature to nautical charts"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Dengiz xaritalarida har bir mayoqning miltillash kodi yozilgan; dengizchi sekundomer bilan miltillashni o'lchab, aynan qaysi burunda turganini darhol bilib oladi.",
            "ru": "Характеристика огня маяка указана в лоции; штурман с секундомером узнаёт конкретный маяк даже в кромешной тьме.",
            "en": "Every lighthouse has a distinct 'character' (flash sequence) published in nautical charts, allowing navigators with stopwatches to pinpoint their landfall."
        },
        "aliases": [
            "mayoq kodi",
            "xaritada aniqlash",
            "miltillash",
            "navigatsiya",
            "маяк",
            "вспышки",
            "навигация"
        ]
    },
    {
        "id": "zakovat_200",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 19-asr o'rtalarida plastmassa (selluloid) kashf etilguniga qadar, professional bilyard sharlari qaysi qimmatbaho hayvon xomashyosidan yasalgan?",
            "ru": "Внимание, вопрос на логику: Из какого драгоценного сырья животного происхождения вытачивали шары для бильярда до изобретения пластмасс?",
            "en": "Attention, deductive question: What precious organic raw material were all professional billiard balls turned from prior to the invention of celluloid in the late 1860s?"
        },
        "options": {
            "uz": [
                "Qattiq eman yog'ochidan",
                "Marmar va granit toshdan",
                "Fil suyagi (fil tishlari)dan",
                "Qo'rg'oshin va po'latdan"
            ],
            "ru": [
                "Твёрдый морёный дуб",
                "Полированный мрамор и гранит",
                "Слоновая кость (бивни слонов)",
                "Сплав свинца и латуни"
            ],
            "en": [
                "Dense seasoned oak wood",
                "Polished Carrara marble",
                "Elephant ivory tusks",
                "Cast lead and brass alloy"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Fil suyagi (fil tishlari)dan",
            "ru": "Слоновая кость (бивни слонов)",
            "en": "Elephant ivory tusks"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Fil suyagi mukammal elastiklik va og'irlik balansiga ega bo'lgan; har bir bilyard to'plami uchun bir nechta fil nobud qilingani sababli sun'iy almashtiruvchiga mukofot e'lon qilingan.",
            "ru": "Из одного бивня получалось лишь 4–5 шаров; истребление слонов заставило учредить премию в $10 000 за синтетический шар.",
            "en": "Each elephant tusk yielded only four or five true-rolling balls, threatening elephant extinction until Hyatt synthesized celluloid to replace it."
        },
        "aliases": [
            "fil suyagi",
            "fil tishi",
            "slonovaya kost",
            "ivory",
            "слоновая кость",
            "бивни"
        ]
    },
    {
        "id": "zakovat_201",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: O'rta asrlarda ingliz novvoylari 12 ta non (dyujina) sotib olgan xaridorga nega doim bitta qo'shimcha non qo'shib jami 13 ta berishgan ('Novvoy o'n uchligi')?",
            "ru": "Внимание, вопрос на логику: Почему в средневековой Англии дюжина у пекарей состояла из 13 буханок ('чёртова дюжина пекаря')?",
            "en": "Attention, deductive question: Why did medieval English bakers routinely supply 13 loaves to anyone who purchased a standard dozen ('baker's dozen')?"
        },
        "options": {
            "uz": [
                "13 raqami omad keltiradi deb ishonilgani uchun",
                "O'n uchinchi non xamir qoldig'i bo'lgani uchun",
                "Nonvoyning oilasi uchun mo'ljallangani uchun",
                "Vazndan kam bo'lib chiqsa beriladigan og'ir jarimadan qutulish uchun"
            ],
            "ru": [
                "Число 13 считалось приносящим удачу в торговле",
                "Тринадцатая буханка делалась из остатков теста",
                "Она предназначалась для подмастерьев",
                "Из-за страха сурового штрафа за недовес буханки"
            ],
            "en": [
                "The number 13 was considered commercially auspicious",
                "The 13th loaf used leftover dough scraps",
                "It was reserved for shop apprentices",
                "Fear of severe penalties for selling underweight loaves"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Vazndan kam bo'lib chiqsa beriladigan og'ir jarimadan qutulish uchun",
            "ru": "Из-за страха сурового штрафа за недовес буханки",
            "en": "Fear of severe penalties for selling underweight loaves"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "1266-yildagi qonunga ko'ra, agar non belgilangan vazndan bir gramm kam chiqsa, novvoy qattiq jazolangan; xatodan qo'rqqan novvoylar qo'shimcha non berishgan.",
            "ru": "За недовес хлеба пекарю грозили огромные штрафы и позорный столб; чтобы не ошибиться при усушке, они давали 13 буханок вместо 12.",
            "en": "The 1266 Assize of Bread and Ale levied severe fines and floggings for underweight bread; adding a 13th loaf insured against accidental shrinkage."
        },
        "aliases": [
            "kam vazn",
            "jarima",
            "novvoy o'n uchligi",
            "nedoves",
            "shtraf",
            "baker's dozen",
            "недовес",
            "штраф"
        ]
    },
    {
        "id": "zakovat_202",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Hozirgi barcha yangi samolyotlarda chekish qat'iyan taqiqlangan bo'lsa-da, nega xalqaro qoidalarga ko'ra samolyot hojatxonalarida kuldon bo'lishi shart?",
            "ru": "Внимание, вопрос на логику: Почему на всех новейших лайнерах в туалетах обязаны стоять пепельницы, хотя курение на борту строжайше запрещено?",
            "en": "Attention, deductive question: Why do international aviation safety regulations mandate ashtrays inside aircraft lavatories even though smoking is strictly illegal?"
        },
        "options": {
            "uz": [
                "Noqonuniy chekkan yo'lovchi sigaretani axlat qutisiga tashlab yong'in chiqarmasligi uchun",
                "Samolyotlar juda eski bo'lgani uchun",
                "Ekipaj a'zolariga chekishga ruxsat berilgani uchun",
                "Dizayn standarti tasodifan o'zgarmay qolgani uchun"
            ],
            "ru": [
                "Чтобы нарушитель при курении не бросил окурок в бумагу и не вызвал пожар",
                "Все пассажирские самолёты слишком старые",
                "Стюардессам разрешено курить в полёте",
                "Авиакомпании забыли изменить проект кабины"
            ],
            "en": [
                "To ensure illicit smokers have a safe place to snuff out cigarettes",
                "All passenger airliners are decades old",
                "Flight attendants are permitted to smoke",
                "Airlines simply forgot to update lavatory molds"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Noqonuniy chekkan yo'lovchi sigaretani axlat qutisiga tashlab yong'in chiqarmasligi uchun",
            "ru": "Чтобы нарушитель при курении не бросил окурок в бумагу и не вызвал пожар",
            "en": "To ensure illicit smokers have a safe place to snuff out cigarettes"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Aviahalokatlar tarixida taqiqqa qaramay chekkan yo'lovchilar sigaretani qog'ozli axlat qutisiga tashlab, bortda halokatli yong'in keltirib chiqargan holatlar bo'lgan.",
            "ru": "Если нарушитель всё же закурит тайно, он должен загасить окурок в пепельнице, а не бросать в урну с горючей бумагой.",
            "en": "Federal aviation regulations mandate ashtrays so that an illicit smoker who panics has a designated fireproof receptacle rather than a bin of dry tissues."
        },
        "aliases": [
            "yong'in",
            "kuldon",
            "sigareta",
            "pojar",
            "pepelnitsa",
            "ashtray",
            "fire",
            "пожар",
            "пепельница"
        ]
    },
    {
        "id": "zakovat_203",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Baland devoriy va pol soatlarida (Grandfather clock) mayatnik uzunligi nima sababdan deyarli doim taxminan 1 metr (99,4 sm) qilib yasaladi?",
            "ru": "Внимание, вопрос на логику: Почему маятники напольных старинных часов почти всегда имеют длину около 1 метра (99,4 см)?",
            "en": "Attention, deductive question: Why do antique grandfather and longcase clocks feature a pendulum measuring approximately one meter (39.1 inches) in length?"
        },
        "options": {
            "uz": [
                "Usta bo'yiga moslab qilingani uchun",
                "Mayatnikning to'liq bitta tebranishi roppa-rosa 1 sekund davom etadi",
                "Soat shkafi chiroyli ko'rinishi uchun",
                "Og'irlik toshi yerga yetmasligi uchun"
            ],
            "ru": [
                "Мастера подгоняли длину под свой рост",
                "Период полуколебания такого маятника равен ровно 1 секунде",
                "Для эстетической гармонии деревянного шкафа",
                "Чтобы подвесные гири не касались пола"
            ],
            "en": [
                "Clockmakers sized it to the height of their benches",
                "The swing period of a one-meter pendulum is precisely one second",
                "Purely for the architectural proportions of tall casework",
                "To ensure gravity drive weights never touched the floor"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Mayatnikning to'liq bitta tebranishi roppa-rosa 1 sekund davom etadi",
            "ru": "Период полуколебания такого маятника равен ровно 1 секунде",
            "en": "The swing period of a one-meter pendulum is precisely one second"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Fizika qonunlariga ko'ra, 0,994 metrli mayatnikning bitta tebranishi (chapdan o'ngga) roppa-rosa 1 sekundni tashkil qiladi va soat aniq sekundma-sekund yuradi.",
            "ru": "Математический маятник длиной 99,4 см имеет полупериод колебания ровно 1 секунду, отмеряя эталонный секундный шаг.",
            "en": "Under gravitational acceleration, a pendulum 0.994 meters long completes a half-swing in exactly 1.000 second, ticking off seconds directly."
        },
        "aliases": [
            "1 sekund",
            "sekundli mayatnik",
            "mayatnik",
            "1 sekunda",
            "one second",
            "секунда",
            "маятник"
        ]
    },
    {
        "id": "zakovat_204",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: 1915-yilda Jon Xertz Chikago va Nyu-Yorkdagi taksi parki mashinalarini nega aynan yorqin sariq rangga bo'yashga qaror qilgan?",
            "ru": "Внимание, вопрос на логику: Почему в 1915 году Джон Герц решил красить все автомобили своего таксопарка в жёлтый цвет?",
            "en": "Attention, deductive question: Why did transportation entrepreneur John Hertz decide in 1915 to paint his entire Chicago and New York taxi fleet bright yellow?"
        },
        "options": {
            "uz": [
                "Sariq bo'yoq eng arzon bo'lgani uchun",
                "Nyu-York meri sariq rangni yaxshi ko'rgani uchun",
                "O'tkazilgan ilmiy tadqiqot sariq rang uzoqdan eng tez ko'rinishini isbotlagani uchun",
                "Taksilar qora mashinalardan ajralib turishi uchun"
            ],
            "ru": [
                "Жёлтая краска для кузовов была самой дешёвой",
                "Мэр Нью-Йорка издал указ в честь своего любимого цвета",
                "Научное исследование доказало, что жёлтый цвет лучше всего заметен издалека",
                "Чтобы полиция не путала такси с личными авто"
            ],
            "en": [
                "Yellow automobile lacquer was cheapest",
                "The Mayor of New York favored yellow",
                "A scientific study proved yellow was the most visible color from a distance",
                "So police wouldn't mistake taxis for luxury limousines"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "O'tkazilgan ilmiy tadqiqot sariq rang uzoqdan eng tez ko'rinishini isbotlagani uchun",
            "ru": "Научное исследование доказало, что жёлтый цвет лучше всего заметен издалека",
            "en": "A scientific study proved yellow was the most visible color from a distance"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Chikago universiteti o'tkazgan tadqiqot shahar tirbandligida va tumanli havoda odam ko'zi uzoq masofadan eng birinchi bo'lib sariq rangni payqashini isbotlagan.",
            "ru": "Университет Чикаго по заказу Герца провёл тест и доказал, что жёлтый цвет — самый заметный для человеческого глаза на дистанции.",
            "en": "Hertz commissioned a University of Chicago study which concluded that yellow with a touch of red was the most visible color from afar."
        },
        "aliases": [
            "sariq rang",
            "uzoqdan ko'rinishi",
            "jon xertz",
            "zametnost",
            "john hertz",
            "yellow",
            "заметен"
        ]
    },
    {
        "id": "zakovat_205",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Birovga nisbatan sovuq munosabatda bo'lishni anglatuvchi 'Sovuq yelka ko'rsatmoq' (Cold shoulder) iborasi o'rta asrlarda qaysi odatdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: От какого застольного обычая средневековой Англии произошло выражение 'оказать холодный приём / холодное плечо' (cold shoulder)?",
            "en": "Attention, deductive question: What medieval dining custom gave rise to the English idiom 'giving someone the cold shoulder'?"
        },
        "options": {
            "uz": [
                "Mehmonning yelkasiga muz qo'yilgan",
                "Salomlashganda yelkadan quchoqlanmagan",
                "Sovuq xonaga joylashtirilgan",
                "Kech qolgan yoki xush ko'rilmagan mehmonga isitilmagan sovuq qo'y go'shti tortilgan"
            ],
            "ru": [
                "К плечу гостя прикладывали кусок льда",
                "Хозяин демонстративно поворачивался спиной",
                "Гостя укладывали спать в неотапливаемой комнате",
                "Нежеланному гостю подавали остывшую холодную баранью лопатку вместо горячего"
            ],
            "en": [
                "Applying ice to the guest's shoulder",
                "Turning one's back haughtily in greetings",
                "Putting guests up in unheated drafty bedrooms",
                "Serving leftover cold mutton shoulder to unwelcome guests as a hint"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Kech qolgan yoki xush ko'rilmagan mehmonga isitilmagan sovuq qo'y go'shti tortilgan",
            "ru": "Нежеланному гостю подавали остывшую холодную баранью лопатку вместо горячего",
            "en": "Serving leftover cold mutton shoulder to unwelcome guests as a hint"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Mehmon mehmondo'stlik haddini oshirib ketganda, mezbon unga issiq qovurdoq o'rniga qotgan sovuq qo'y kuragini (mutton shoulder) qo'yib, ketish vaqti kelganiga shama qilgan.",
            "ru": "Когда гость засиживался и злоупотреблял гостеприимством, хозяин подавал на стол холодную баранью лопатку, намекая, что пора уходить.",
            "en": "When an unwanted guest overstayed, the host politely signaled the visit was over by serving leftover cold mutton shoulder instead of a hot roast."
        },
        "aliases": [
            "sovuq qo'y go'shti",
            "sovuq kurak",
            "mutton shoulder",
            "kholodnaya lopatka",
            "баранья лопатка",
            "лопатка"
        ]
    },
    {
        "id": "zakovat_206",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Klassik pianino va royallarda nega kamroq yoki ko'proq emas, aynan 88 ta klavisha bo'ladi?",
            "ru": "Внимание, вопрос на логику: Почему у стандартного современного фортепиано именно 88 клавиш?",
            "en": "Attention, deductive question: Why do modern full-size concert grand pianos feature exactly 88 keys?"
        },
        "options": {
            "uz": [
                "Inson qulog'i ajrata oladigan tovush chastotalarining to'liq diapazoni bo'lgani uchun",
                "Motsart o'z asarlarini faqat 88 ta notada yozgani uchun",
                "Klavishlarni yasash uchun yog'och o'lchami shunday bo'lgan",
                "Raqam simmetriyasi (8 va 8) sharafiga"
            ],
            "ru": [
                "Они полностью покрывают диапазон слуха, различимый человеческим ухом",
                "Моцарт завещал писать музыку в пределах 88 нот",
                "Длина деки рояля диктовала размер клавиш",
                "В честь сакральной симметрии цифры 88"
            ],
            "en": [
                "They span the complete acoustic frequency range of human hearing",
                "Mozart decreed classical music fit within 88 tones",
                "Standard soundboard length constrained key widths",
                "In honor of the mystical numerology of double eights"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Inson qulog'i ajrata oladigan tovush chastotalarining to'liq diapazoni bo'lgani uchun",
            "ru": "Они полностью покрывают диапазон слуха, различимый человеческим ухом",
            "en": "They span the complete acoustic frequency range of human hearing"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "88 ta klavish eng pastki 27,5 Gerts (A0) dan eng yuqori 4186 Gerts (C8) gacha tovush beradi; bundan past yoki baland notalarni inson qulog'i musiqiy ohang sifatida ajrata olmaydi.",
            "ru": "Диапазон 88 клавиш (от 27,5 Гц до 4186 Гц) охватывает все частоты, которые ухо воспринимает как музыкальный тон, а не гул или писк.",
            "en": "The 88 keys span from A0 (27.5 Hz) to C8 (4,186 Hz); frequencies outside this range are perceived merely as indeterminate rumbles or clicks."
        },
        "aliases": [
            "chastota diapazoni",
            "eshitish diapazoni",
            "diapazon slukha",
            "audible range",
            "слух",
            "диапазон"
        ]
    },
    {
        "id": "zakovat_207",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Spektakl oldidan aktyorlarga 'Oyog'ing sinsin!' (Break a leg) deb tilak bildirishning kelib chiqishi nima bilan bog'liq?",
            "ru": "Внимание, вопрос на логику: Почему в театре перед премьерой желают 'сломать ногу' (break a leg) вместо пожелания удачи?",
            "en": "Attention, deductive question: Why do theater performers traditionally tell each other 'Break a leg' instead of wishing good luck before a show?"
        },
        "options": {
            "uz": [
                "Aktyorlar sahnada haqiqatan yiqilishi kerak bo'lgan",
                "Teatrdagi irim: omad tilasa yomonlik bo'ladi deb, aksini tilashgan yoki tizzani bukish (ta'zim qilish)",
                "Qadimgi teatr polida teshiklar ko'p bo'lgan",
                "Raqib aktyorlarni sindirish ma'nosida"
            ],
            "ru": [
                "Актёры на сцене обязаны были падать в обморок",
                "Театральное суеверие: пожелание удачи приносит провал, либо поклон зрителям",
                "В старинных сценах пол был в дырах",
                "Чтобы сломать ногу сопернику за кулисами"
            ],
            "en": [
                "Actors were expected to faint onstage dramatically",
                "Theatrical superstition that wishing luck brings failure, or bending knees to bow",
                "Ancient theater floorboards had hazardous holes",
                "To trip up rival performers in the wings"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Teatrdagi irim: omad tilasa yomonlik bo'ladi deb, aksini tilashgan yoki tizzani bukish (ta'zim qilish)",
            "ru": "Театральное суеверие: пожелание удачи приносит провал, либо поклон зрителям",
            "en": "Theatrical superstition that wishing luck brings failure, or bending knees to bow"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Teatr xalqi juda irimchi bo'lib, to'g'ridan-to'g'ri omad tilash parilar va jinlarni g'azablantiradi deb hisoblashgan; shuningdek, 'oyoqni sindirish' pardadan keyin ta'zim uchun tizzani bukishni ham anglatadi.",
            "ru": "Суеверные актёры верили, что духи сделают всё наоборот; также фраза означает согнуть ногу в колене для поклона на бис.",
            "en": "Performers believe spirits deliberately invert spoken wishes; alternatively, 'breaking the leg' referred to bending the knee to bow during ovations."
        },
        "aliases": [
            "irim",
            "ta'zim qilish",
            "sueverie",
            "bow",
            "poklon",
            "break a leg",
            "суеверие",
            "поклон"
        ]
    },
    {
        "id": "zakovat_208",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Skripka, violonchel va boshqa torli cholg'ularning kamonchasida nima sababdan sintetik tola emas, asrlar davomida aynan ot dumi qili ishlatiladi?",
            "ru": "Внимание, вопрос на логику: Почему для смычков скрипок и виолончелей веками используют исключительно волос из конского хвоста?",
            "en": "Attention, deductive question: Why have master luthiers strung violin, viola, and cello bows with stallion tail hair rather than synthetic fibers for centuries?"
        },
        "options": {
            "uz": [
                "Ot qili eng arzon tola bo'lgani uchun",
                "Ot qili mutlaqo uzilmaydi deb hisoblangani uchun",
                "Ot tuklaridagi mikroskopik tishchalar (tangachalar) simni ilashtirib tebratadi",
                "Ot qili namlikdan ta'sirlanmaydi"
            ],
            "ru": [
                "Конский волос был самым доступным материалом",
                "Конский волос невозможно порвать руками",
                "Микроскопические чешуйки конского волоса цепляют и заставляют струну петь",
                "Конский волос не реагирует на влажность"
            ],
            "en": [
                "Horsehair was the cheapest agricultural byproduct",
                "Horsehair is virtually unbreakable under tension",
                "Microscopic scales along the horsehair catch and release the string smoothly",
                "Horsehair is impervious to humidity changes"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Ot tuklaridagi mikroskopik tishchalar (tangachalar) simni ilashtirib tebratadi",
            "ru": "Микроскопические чешуйки конского волоса цепляют и заставляют струну петь",
            "en": "Microscopic scales along the horsehair catch and release the string smoothly"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Ot tuki yuzasida mayda qipiqchalar bor; qatron (kanifol) surilganda ular simni ushlab olib (stick) keyin qo'yib yuboradi (slip), natijada go'zal akustik tebranish hosil bo'ladi.",
            "ru": "Чешуйчатая структура конского волоса удерживает канифоль и создает идеальный фрикционный эффект трения о струну.",
            "en": "Natural horsehair possesses microscopic barbed scales that hold rosin and create the stick-slip friction required to sustain string oscillation."
        },
        "aliases": [
            "ot qili",
            "tangachalar",
            "kanifol",
            "cheshuyki",
            "horsehair",
            "scales",
            "конский волос",
            "чешуйки"
        ]
    },
    {
        "id": "zakovat_209",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Muz nima sababdan suv tubiga cho'kib ketmay, suv yuzasida suzib yuradi va suv havzalarining tubigacha muzlab qolishidan asraydi?",
            "ru": "Внимание, вопрос на логику: Какое уникальное физическое свойство воды заставляет лёд плавать на поверхности, спасая жизнь в водоёмах зимой?",
            "en": "Attention, deductive question: What anomalous physical property of water allows ice to float on liquid water, preserving aquatic ecosystems during winter freezes?"
        },
        "options": {
            "uz": [
                "Muz ichida havo pufakchalari qolib ketgani uchun",
                "Suv tubidagi baliqlar muzni tepaga itargani uchun",
                "Muz sovuq bo'lgani sababli tepaga intiladi",
                "Muzlaganda suv molekulalari kengayib, zichligi suyuq suvdan 9 foizga kamayadi"
            ],
            "ru": [
                "Внутри льда всегда заперты пузырьки воздуха",
                "Рыбы выталкивают лед на поверхность плавниками",
                "Холодные тела всегда стремятся вверх",
                "При замерзании вода расширяется, и плотность льда на 9% меньше воды"
            ],
            "en": [
                "Trapped ambient air bubbles buoy the ice block",
                "Aquatic animals push ice sheets toward the surface",
                "Cold solids naturally seek higher elevations",
                "Water expands upon freezing, making ice 9% less dense than liquid water"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Muzlaganda suv molekulalari kengayib, zichligi suyuq suvdan 9 foizga kamayadi",
            "ru": "При замерзании вода расширяется, и плотность льда на 9% меньше воды",
            "en": "Water expands upon freezing, making ice 9% less dense than liquid water"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Suv 4 darajadan past soviganda vodorod bog'lari heksagonal panjara hosil qilib kengayadi; agar muz cho'kkanda edi, barcha daryo va okeanlar tubidan boshlab qotib, tiriklik nobud bo'lardi.",
            "ru": "Водородные связи образуют кристаллическую решетку с пустотами, уменьшая плотность льда и создавая защитный термос на реках.",
            "en": "As water freezes below 4°C, hydrogen bonds form a rigid hexagonal crystalline lattice that spreads molecules apart, lowering density by ~9%."
        },
        "aliases": [
            "kengayish",
            "zichlik",
            "vodorod bog'i",
            "plotnost",
            "density",
            "плотность",
            "расширение"
        ]
    },
    {
        "id": "zakovat_210",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Biron vaziyatda ustunlikka erishishni anglatuvchi 'To have the upper hand' (Ustun qo'lga ega bo'lish) iborasi bolalarning qaysi o'yinidan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Из какой дворовой игры возникло английское выражение 'to have the upper hand' (взять верх, иметь преимущество)?",
            "en": "Attention, deductive question: What traditional playground bat-selection game gave rise to the idiom 'to have the upper hand'?"
        },
        "options": {
            "uz": [
                "Bita dastasini navbatma-navbat ushlab, eng tepasini ushlagan bola birinchi boshlagan",
                "Kichik barmoq boshqa barmoqlardan teparoqda turgani uchun",
                "Qilichbozlikda dushmanning qo'lini tepadan qayirish",
                "Qo'l kurashida tepadan bosish"
            ],
            "ru": [
                "Дети по очереди перехватывали биту снизу вверх; чья рука была на самом верху, тот побеждал",
                "В фехтовании верхняя позиция клинка давала перевес",
                "В армрестлинге захват пальцев сверху гарантирует победу",
                "При рукопожатии ладонь сверху означает доминирование"
            ],
            "en": [
                "Players gripped a baseball bat hand-over-hand upwards; the top hand won first pick",
                "In fencing, high parries dominated the opponent's blade",
                "In arm wrestling, a top-roll grip secures the pin",
                "In handshakes, palm-down hand placement signals dominance"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Bita dastasini navbatma-navbat ushlab, eng tepasini ushlagan bola birinchi boshlagan",
            "ru": "Дети по очереди перехватывали биту снизу вверх; чья рука была на самом верху, тот побеждал",
            "en": "Players gripped a baseball bat hand-over-hand upwards; the top hand won first pick"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Bolalar o'yinni kim boshlashini hal qilish uchun beysbol bitasini pastidan ushlab navbatma-navbat barmog'ini tepaga qo'ygan; bitaning eng uchini to'liq ushlab qolgan odam g'olib bo'lgan.",
            "ru": "Капитаны по очереди обхватывали бейсбольную биту кулаком вверх от рукояти; тот, чья рука накрывала верхушку, выбирал поле.",
            "en": "Team captains took turns placing fist over fist up the shaft of a baseball bat; whoever gripped the very top knob won first choice of players."
        },
        "aliases": [
            "bita",
            "beysbol",
            "ustun qo'l",
            "bita",
            "upper hand",
            "бита"
        ]
    },
    {
        "id": "zakovat_211",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qahva quyiladigan finjonlar (krujkalar) nima sababdan odatda qalin keramikadan yasaladi?",
            "ru": "Внимание, вопрос на логику: Почему кружки для кофе делают из толстой керамики с массивными стенками?",
            "en": "Attention, deductive question: Why are standard hot beverage mugs manufactured with thick ceramic or stoneware walls rather than thin metal or glass?"
        },
        "options": {
            "uz": [
                "Loy idishlar eng arzon bo'lgani uchun",
                "Past issiqlik o'tkazuvchanligi sababli ichimlikni issiq saqlaydi va qo'lni kuydirmaydi",
                "Chinni qahvaning ta'mini o'zgartirgani uchun",
                "Qalin idish tushib ketsa sinmaydi"
            ],
            "ru": [
                "Глиняная посуда была самой простой в лепке",
                "Низкая теплопроводность керамики долго хранит тепло и не обжигает пальцы",
                "Керамика химически реагирует с кофеином",
                "Толстые кружки не бьются при падении на стол"
            ],
            "en": [
                "Clay earthenware was the simplest material to mold",
                "Low thermal conductivity insulates heat and protects fingers from burns",
                "Ceramic glazes chemically react with caffeine acidity",
                "Thick stoneware never shatters when dropped"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Past issiqlik o'tkazuvchanligi sababli ichimlikni issiq saqlaydi va qo'lni kuydirmaydi",
            "ru": "Низкая теплопроводность керамики долго хранит тепло и не обжигает пальцы",
            "en": "Low thermal conductivity insulates heat and protects fingers from burns"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Koramika g'ovakli bo'lib, uning issiqlik o'tkazuvchanligi metalldan 100 baravar past; qalin devor qahvani sovutmaydi va tashqarisi qizib qo'lni kuydirmaydi.",
            "ru": "Пористая обожженная глина обладает отличными теплоизолирующими свойствами, удерживая температуру напитка.",
            "en": "Fired porous ceramic has low thermal conductivity, insulating the steaming liquid while allowing comfortable gripping without scalding."
        },
        "aliases": [
            "issiqlik o'tkazuvchanlik",
            "keramika",
            "kuydirmaslik",
            "teploprovodnost",
            "insulation",
            "теплопроводность"
        ]
    },
    {
        "id": "zakovat_212",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ulkan yo'lovchi samolyoti aeroport yo'lagiga g'ildiraklarini tekkazgan onda shinalar ostidan nima sababdan oppoq tutun burqsib chiqadi?",
            "ru": "Внимание, вопрос на логику: Почему в момент касания полосы шасси самолёта из-под колес всегда вырывается облачко белого дыма?",
            "en": "Attention, deductive question: Why do airliner tires consistently emit a distinct puff of white smoke the moment the landing gear touches the runway tarmac?"
        },
        "options": {
            "uz": [
                "Samolyot tormoz suyuqligi bug'lanib ketgani uchun",
                "Yo'lakdagi chang havoga ko'tarilgani uchun",
                "Harakatsiz shina uchish-qo'nish yo'lagiga tekkanda bir zumda 250 km/soatgacha aylanadi",
                "Shina ichidagi azot gazi sizib chiqqani uchun"
            ],
            "ru": [
                "Тормозные колодки шасси мгновенно вскипают",
                "Струя реактивных двигателей сдувает пыль с полосы",
                "Неподвижное колесо при касании мгновенно раскручивается до 250 км/ч, стираясь об асфальт",
                "Из колес стравливают избыточное давление азота"
            ],
            "en": [
                "Brake calipers boil away hydraulic fluid",
                "Jet engine thrust reversers blast concrete dust",
                "Stationary tires instantly spin up to 250 km/h on runway contact, burning rubber",
                "Nitrogen pressure valves release burst steam"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Harakatsiz shina uchish-qo'nish yo'lagiga tekkanda bir zumda 250 km/soatgacha aylanadi",
            "ru": "Неподвижное колесо при касании мгновенно раскручивается до 250 км/ч, стираясь об асфальт",
            "en": "Stationary tires instantly spin up to 250 km/h on runway contact, burning rubber"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Havoda turgan g'ildiraklar aylanmaydi (tezligi 0); ular yerga tekkan soniyaning mingdan birida samolyotning 250 km/soat tezligiga moslashib qattiq ishqalanadi va rezina yonib tutaydi.",
            "ru": "В воздухе колёса неподвижны; при контакте с бетоном на скорости 250 км/ч резина буквально горит миллисекунды до раскрутки.",
            "en": "The tires are stationary in flight; upon touching the concrete at 150 mph, the rubber skids violently until it spins up to matching runway speed."
        },
        "aliases": [
            "shina aylanishi",
            "ishqalanish",
            "250 km/soat",
            "raskrutka",
            "trenie",
            "spin up",
            "friction",
            "раскрутка",
            "трение"
        ]
    },
    {
        "id": "zakovat_213",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Matn terishda bosh harflar 'Upper case', kichik harflar esa 'Lower case' deb atalishi qaysi matbaa odatidan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Почему в типографике и на клавиатурах заглавные буквы называют 'upper case', а строчные — 'lower case'?",
            "en": "Attention, deductive question: Where did the typographic terms 'upper case' (capitals) and 'lower case' (small letters) originate in printing history?"
        },
        "options": {
            "uz": [
                "Katta harflar osmonga intilish ramzi bo'lgani uchun",
                "Qog'ozning yuqori qismiga katta harf yozilgani uchun",
                "Kitob muqovasi balandda turgani uchun",
                "Matbaachilar katta harflarni yuqori yog'och qutida, kichiklarni pastda saqlashgan"
            ],
            "ru": [
                "Заглавные буквы символизировали небесные сферы",
                "Наверху страницы всегда писали крупнее",
                "Королевские указы вывешивали на верхних досках",
                "Наборщики хранили литеры заглавных букв в верхнем ящике, а строчных — в нижнем"
            ],
            "en": [
                "Majuscule capitals symbolized heavenly spheres",
                "Headers were engraved at the top of scrolls",
                "Royal decrees were pinned to the top row of noticeboards",
                "Typesetters stored capital letters in the upper wooden case and small in the lower"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Matbaachilar katta harflarni yuqori yog'och qutida, kichiklarni pastda saqlashgan",
            "ru": "Наборщики хранили литеры заглавных букв в верхнем ящике, а строчных — в нижнем",
            "en": "Typesetters stored capital letters in the upper wooden case and small in the lower"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qo'rg'oshin harflarni qo'lda teruvchi matbaachilar stoli oldida ikkita quti turgan: kam ishlatiladigan bosh harflar tepada (upper case), ko'p ishlatiladigan kichik harflar pastki qutida (lower case) bo'lgan.",
            "ru": "В типографиях наборные кассы стояли друг над другом: сверху лежали редкие заглавные буквы, снизу под рукой — строчные.",
            "en": "Typesetters kept shallow wooden compartment trays called cases; capitals sat in the higher upper case and frequent small letters in the lower case."
        },
        "aliases": [
            "matbaa qutisi",
            "harf qutisi",
            "nabornaya kassa",
            "type case",
            "касса",
            "типография"
        ]
    },
    {
        "id": "zakovat_214",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ingliz va lotin alifbosidagi deyarli barcha so'zlarda (Queen, Quiet, Quick) Q harfidan keyin nima sababdan deyarli doim U harfi keladi?",
            "ru": "Внимание, вопрос на логику: Почему в латинском алфавите и европейских языках после буквы Q практически всегда обязательно следует буква U?",
            "en": "Attention, deductive question: Why is the Latin letter 'Q' almost universally followed by the letter 'U' in English and Romance vocabularies?"
        },
        "options": {
            "uz": [
                "Lotin tilida /kw/ tovushi doimo 'qu' qo'shharfi (digraf) bilan yozilgani sababli",
                "Q harfi U harfisiz o'qilmagani uchun",
                "Qadimgi fransuz qiroli sharafiga",
                "U harfi Q harfining dumi bo'lgani uchun"
            ],
            "ru": [
                "В латыни глухой звук /kw/ традиционно передавался буквосочетанием QU",
                "Буква Q потеряла свой звук в Средневековье",
                "По указу Карла Великого об алфавите",
                "Буква U служила хвостиком буквы Q"
            ],
            "en": [
                "In Latin the labiovelar sound /kw/ was written with the digraph QU",
                "The letter Q lost its independent phoneme in the Dark Ages",
                "Under Charlemagne's imperial spelling decree",
                "The letter U physically supported the tail of Q"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Lotin tilida /kw/ tovushi doimo 'qu' qo'shharfi (digraf) bilan yozilgani sababli",
            "ru": "В латыни глухой звук /kw/ традиционно передавался буквосочетанием QU",
            "en": "In Latin the labiovelar sound /kw/ was written with the digraph QU"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Klassik lotin tilida lab-til orqa tovushi (/kw/) birikmasi uchun 'Q' va 'V' (keyinchalik U) birgalikda digraf qilib olingan va barcha tillarga shunday o'tgan.",
            "ru": "Древнеримские писцы использовали диграф QU для передачи единого лабиовелярного звука, перекочевавшего в английский.",
            "en": "The Etruscans and Romans used the digraph 'QV' to transcribe the single labiovelar phoneme /kʷ/, cementing the pairing forever."
        },
        "aliases": [
            "lotin tili",
            "digraf",
            "latinskiy",
            "digraph",
            "labiovelar",
            "латынь",
            "диграф"
        ]
    },
    {
        "id": "zakovat_215",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Boyo'g'lilar kechasi sichqon va o'ljalar ustiga uchib borganida qanday qilib mutlaqo tovushsiz (akustik jimlikda) ucha oladi?",
            "ru": "Внимание, вопрос на логику: Благодаря какому уникальному строению крыльев совы летают абсолютно бесшумно в ночной тишине?",
            "en": "Attention, deductive question: What specialized anatomical feather adaptation enables nocturnal owls to fly in near-total acoustic silence over unsuspecting prey?"
        },
        "options": {
            "uz": [
                "Boyo'g'li qanot qoqmasdan faqat suzib uchgani uchun",
                "Qanot chetidagi arra tishli tuklar havo to'lqinlarini mayda sokin uyurmalarga bo'lib yuboradi",
                "Tungi havo harorati sovuq bo'lgani sababli",
                "Qanotlari maxsus yog' bilan qoplangani uchun"
            ],
            "ru": [
                "Совы планируют и никогда не машут крыльями",
                "Зубчатая бахрома на перьях дробит воздушные вихри на микропотоки",
                "Ночной воздух плотнее и гасит звуки сам",
                "Перья совы покрыты толстым слоем жира"
            ],
            "en": [
                "Owls purely glide without ever flapping wings",
                "Serrated comb fringes on feather edges break air turbulence into micro-eddies",
                "Night air density naturally absorbs acoustics",
                "Owl plumage is coated in thick damping grease"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Qanot chetidagi arra tishli tuklar havo to'lqinlarini mayda sokin uyurmalarga bo'lib yuboradi",
            "ru": "Зубчатая бахрома на перьях дробит воздушные вихри на микропотоки",
            "en": "Serrated comb fringes on feather edges break air turbulence into micro-eddies"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qanot patlarining chekkalaridagi mayda taroqsimon tukchalar qanotdan ajralayotgan havoni sokinlashtiradi va qarsillagan shovqin hosil bo'lishiga yo'l qo'ymaydi.",
            "ru": "Гребенчатые зубчики на передней кромке крыла и пуховая бахрома глушат турбулентность, исключая шум взмаха.",
            "en": "The leading edge of an owl's wing feather features a stiff comb-like serration, and the trailing edge has a soft fringe, suppressing pressure waves."
        },
        "aliases": [
            "qanot cheti",
            "arra tishli",
            "tovushsiz",
            "baxroma",
            "fringes",
            "serrated",
            "бахрома",
            "бесшумный"
        ]
    },
    {
        "id": "zakovat_216",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Havo sharlari (aerostatlar) nima sababdan to'liq sharsimon emas, pastga qaragan nok yoki teskari tomchi shaklida yasaladi?",
            "ru": "Внимание, вопрос на логику: Почему монгольфьеры (тепловые аэростаты) имеют форму перевёрнутой капли, а не идеальной сферы?",
            "en": "Attention, deductive question: Why are thermal hot air balloons patterned in an inverted natural teardrop shape rather than a perfect geometric sphere?"
        },
        "options": {
            "uz": [
                "Pastga qaragan uchi savatni ko'tarib turgani uchun",
                "Shamol kuchini kamaytirish maqsadida",
                "Ichki issiq havo bosimi mato choklariga teng taqsimlanadi va mato yirtilmaydi",
                "Shar ichiga ko'proq havo sig'dirish uchun"
            ],
            "ru": [
                "Узкий конус лучше держит подвешенную корзину",
                "Для снижения бокового сноса ветром",
                "Каплевидная форма (цепная линия) равномерно распределяет натяжение швов купола",
                "Такая форма вмещает рекордный объём газа"
            ],
            "en": [
                "The narrow neck directly anchors the burner basket",
                "To minimize sideways aerodynamic wind drift",
                "The catenary teardrop shape equalizes tension across fabric envelope seams",
                "It maximizes the volume-to-surface thermodynamic ratio"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Ichki issiq havo bosimi mato choklariga teng taqsimlanadi va mato yirtilmaydi",
            "ru": "Каплевидная форма (цепная линия) равномерно распределяет натяжение швов купола",
            "en": "The catenary teardrop shape equalizes tension across fabric envelope seams"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Teskari tomchi shakli tabiiy zanjir chizig'i (catenary curve) hisoblanadi; bu shaklda ko'taruvchi kuch mato choklarini yirtmaydi, balki yukni to'g'ri taqsimlaydi.",
            "ru": "Форма 'естественной капли' возникает под действием разницы давлений и снимает разрушающие нагрузки с вертикальных лент купола.",
            "en": "The catenary curve envelope profile equilibrates circumferential stress against the lifting buoyant gas pressure, preventing seam blowout."
        },
        "aliases": [
            "choklar zo'riqishi",
            "tomchisimon",
            "arka",
            "natyajenie",
            "catenary",
            "натяжение",
            "капля"
        ]
    },
    {
        "id": "zakovat_217",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qiyin va og'riqli vaziyatga sabr bilan chidashni anglatuvchi 'O'qni tishlamoq' (Bite the bullet) iborasi qayerdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Откуда возникло английское выражение 'bite the bullet' (стиснуть зубы, перетерпеть боль)?",
            "en": "Attention, deductive question: What gruesome battlefield surgical reality gave rise to the phrase 'bite the bullet'?"
        },
        "options": {
            "uz": [
                "Qo'rg'oshin yarani davolaydi deb ishonilgani uchun",
                "O'q dori kukunini yutish kuch bag'ishlagani uchun",
                "Dushman asir olganda o'zini o'ldirish uchun",
                "Narkoz bo'lmagan davrda maydon jarrohligida og'riqdan baqirmaslik va tilini tishlab olmaslik uchun"
            ],
            "ru": [
                "Свинец считался обеззараживающим средством",
                "Чтобы проглотить порох для храбрости в бою",
                "Для самоубийства перед угрозой пыток",
                "При ампутациях без наркоза раненым давали свинцовую пулю в зубы от болевого шока"
            ],
            "en": [
                "Lead was believed to chemically sterilize gangrene",
                "Swallowing black powder induced battle berserk courage",
                "For immediate suicide when facing torture",
                "Wounded soldiers bit on soft lead bullets during surgery before anesthesia"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Narkoz bo'lmagan davrda maydon jarrohligida og'riqdan baqirmaslik va tilini tishlab olmaslik uchun",
            "ru": "При ампутациях без наркоза раненым давали свинцовую пулю в зубы от болевого шока",
            "en": "Wounded soldiers bit on soft lead bullets during surgery before anesthesia"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Jang maydonida yarador askarlarning oyog'i yoki qo'lini anesteziyasiz arralashganda, ular tishini sindirib tilini uzib olmasligi uchun og'ziga yumshoq qo'rg'oshin o'q tishlatilgan.",
            "ru": "До изобретения анестезии солдатам перед ампутацией давали в зубы мягкую свинцовую пулю, чтобы они не откусили себе язык от крика.",
            "en": "Before ether anesthesia, surgeons operating on soldiers in military field hospitals had them clamp down on a malleable lead musket ball."
        },
        "aliases": [
            "o'qni tishlash",
            "anesteziya",
            "og'riq",
            "amputatsiya",
            "bullet",
            "пуля",
            "ампутация"
        ]
    },
    {
        "id": "zakovat_218",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ko'zguga qaraganimizda nima sababdan o'ng va chap tomonimiz almashib ko'rinadi-yu, lekin boshimiz pastda, oyog'imiz tepada bo'lib qolmaydi?",
            "ru": "Внимание, вопрос на логику: Почему зеркало меняет местами правое и левое, но никогда не переворачивает верх и низ?",
            "en": "Attention, deductive question: Why do household mirrors seem to swap left and right while leaving up and down completely unreversed?"
        },
        "options": {
            "uz": [
                "Ko'zgu o'ng-chapni emas, aslida old-orqa (chuqurlik) o'qini teskari qiladi",
                "Odamning ko'zlari gorizontal joylashgani uchun",
                "Ko'zgu shishasi yorug'likni burchak ostida sindirgani uchun",
                "Gravitatsiya kuchi vertikal ta'sir qilgani uchun"
            ],
            "ru": [
                "Зеркало инвертирует не право и лево, а ось глубины (вперёд-назад)",
                "Потому что наши глаза расположены горизонтально",
                "Стекло преломляет свет только по горизонтали",
                "Сила тяжести не даёт переворачивать верх и низ"
            ],
            "en": [
                "Mirrors do not invert left-right, but invert front-to-back (depth axis)",
                "Because human eyes are arranged on a horizontal axis",
                "Glass selectively refracts along the horizontal plane",
                "Gravity exerts vertical stabilizing forces on optical rays"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Ko'zgu o'ng-chapni emas, aslida old-orqa (chuqurlik) o'qini teskari qiladi",
            "ru": "Зеркало инвертирует не право и лево, а ось глубины (вперёд-назад)",
            "en": "Mirrors do not invert left-right, but invert front-to-back (depth axis)"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Bu optik illyuziya: ko'zgu hech narsani o'ngga yoki chapga burmaydi; agar siz shimolga qarasangiz, aksingiz janubga qaraydi — u faqat chuqurlik o'qini teskari qiladi.",
            "ru": "Зеркало вообще ничего не переворачивает в плоскости; оно выворачивает трёхмерный мир наизнанку вдоль перпендикулярной оси Z.",
            "en": "Mirrors do not flip coordinates horizontally; they invert along the orthogonal depth axis (Z-axis), reflecting perpendicular points back on themselves."
        },
        "aliases": [
            "chuqurlik o'qi",
            "old-orqa",
            "os glubini",
            "depth axis",
            "инверсия глубины",
            "ось глубины"
        ]
    },
    {
        "id": "zakovat_219",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Soxta va riyokorona yig'lashni anglatuvchi 'Timsoh ko'z yoshlari' (Crocodile tears) iborasining haqiqiy biologik sababi nima?",
            "ru": "Внимание, вопрос на логику: Какова истинная физиологическая причина выделения 'слёз' у крокодила во время поедания добычи?",
            "en": "Attention, deductive question: What is the actual biological mechanism responsible for 'crocodile tears' streaming down a feeding crocodile's snout?"
        },
        "options": {
            "uz": [
                "Qurboniga haqiqatan rahmi kelgani uchun",
                "Ko'z burchagidagi tuz bezlari tanadagi ortiqcha tuzni suyuqlik qilib chiqaradi",
                "Jag' muskullari ko'z yosh bezini siqib qo'ygani uchun",
                "Chuchuk suv ko'zini achitgani uchun"
            ],
            "ru": [
                "Крокодил испытывает раскаяние перед жертвой",
                "Солевые железы у глаз выводят избыток соли из организма во время еды",
                "Челюстные мышцы механически сдавливают слёзный мешок",
                "Речная вода раздражает роговицу глаза"
            ],
            "en": [
                "Crocodiles experience authentic biological remorse",
                "Salt glands near the eyes expel excess dietary salt as fluid while eating",
                "Jaw closing forces mechanically crush tear sacs",
                "Brackish marsh water irritates the reptile cornea"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Ko'z burchagidagi tuz bezlari tanadagi ortiqcha tuzni suyuqlik qilib chiqaradi",
            "ru": "Солевые железы у глаз выводят избыток соли из организма во время еды",
            "en": "Salt glands near the eyes expel excess dietary salt as fluid while eating"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Timsohlar suv va ozuqa bilan kirgan ortiqcha tuzni buyragi orqali chiqara olmaydi; maxsus bezlar ko'z burchagidan sho'r tomchilar ajratib chiqaradi.",
            "ru": "У крокодилов слабо развиты почки; избыток солей выводится специальными модифицированными железами прямо под веками.",
            "en": "Crocodiles have inefficient kidneys and rely on modified lachrymal salt glands located near their eye sockets to excrete excess sodium chloride."
        },
        "aliases": [
            "tuz bezlari",
            "sho'r suyuqlik",
            "solevie jelezi",
            "salt glands",
            "солевые железы"
        ]
    },
    {
        "id": "zakovat_220",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Tunda avtomobil chirog'i tushganda mushuk, bo'ri va boshqa tungi yirtqichlarning ko'zlari zumradday yonib ko'rinishining sababi nima?",
            "ru": "Внимание, вопрос на логику: Почему глаза кошек, собак и волков ярко светятся зеленым или желтым светом в темноте в лучах фар?",
            "en": "Attention, deductive question: Why do the eyes of nocturnal animals like cats, dogs, and wolves glow brightly green or gold in automobile headlights?"
        },
        "options": {
            "uz": [
                "Ko'zning o'zi fosforli nurlar taratgani uchun",
                "Ko'z qorachig'ida olov yongani uchun",
                "To'r parda ortidagi yorug'lik qaytaruvchi qatlam (tapetum lucidum)",
                "Ko'z shox pardasi muzlab qolgani tufayli"
            ],
            "ru": [
                "Глаз кошки сам по себе испускает фосфорное свечение",
                "В хрусталике концентрируется лунный свет",
                "Светоотражающий слой тапетум (tapetum lucidum) за сетчаткой",
                "Роговица отражает инфракрасное излучение тела"
            ],
            "en": [
                "Feline corneas emit intrinsic phosphorescence",
                "The crystalline lens concentrates stored moonlight",
                "The tapetum lucidum reflective layer behind the retina",
                "The iris retroreflects infrared body heat"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "To'r parda ortidagi yorug'lik qaytaruvchi qatlam (tapetum lucidum)",
            "ru": "Светоотражающий слой тапетум (tapetum lucidum) за сетчаткой",
            "en": "The tapetum lucidum reflective layer behind the retina"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Tapetum qatlami o'tib ketgan yorug'likni xuddi ko'zgu kabi to'r pardaga qayta qaytaradi, bu hayvonga qorong'ida insonnikidan 6 marta kuchliroq ko'rish imkonini beradi.",
            "ru": "Тапетум работает как зеркало, отражая фотоны обратно на палочки сетчатки для повторного улавливания в темноте.",
            "en": "The tapetum lucidum retroreflects light back through the retinal photoreceptors, giving nocturnal animals a second chance to detect dim photons."
        },
        "aliases": [
            "tapetum",
            "tapetum lucidum",
            "ko'zgu qatlami",
            "тапетум",
            "сетчатка"
        ]
    },
    {
        "id": "zakovat_221",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Kechalari suvosti kemalarida va harbiy komandir punktlarida nima sababdan xona chiroqlari o'chirilib, hamma yoq qip-qizil yoritiladi?",
            "ru": "Внимание, вопрос на логику: Зачем на подводных лодках и мостиках военных кораблей ночью включают исключительно красное освещение?",
            "en": "Attention, deductive question: Why do submarine control rooms and naval bridge decks switch exclusively to dim red ambient lighting at night?"
        },
        "options": {
            "uz": [
                "Dushmanga sezdirmaslik uchun",
                "Qizil svetodiodlar batareyani kam sarflagani uchun",
                "Dengizchilarda agressiyani oshirish uchun",
                "Qizil rang ko'zdagi rodopsin pigmentini yuvib yubormaydi va tungi ko'rishni saqlaydi"
            ],
            "ru": [
                "Чтобы свет не пробивался через обшивку лодки",
                "Красные лампы потребляют меньше тока аккумулятора",
                "Для стимуляции боевой ярости экипажа в бою",
                "Красный свет не разрушает зрительный пигмент родопсин в палочках сетчатки"
            ],
            "en": [
                "To stop light leaking through hull steel",
                "Red filament bulbs draw less battery amperage",
                "To artificially stimulate crew combat adrenaline",
                "Red light does not bleach the rhodopsin pigment in rod cells"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Qizil rang ko'zdagi rodopsin pigmentini yuvib yubormaydi va tungi ko'rishni saqlaydi",
            "ru": "Красный свет не разрушает зрительный пигмент родопсин в палочках сетчатки",
            "en": "Red light does not bleach the rhodopsin pigment in rod cells"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qizil rang tayoqchasimon hujayralarni chalg'itmaydi; shiftdan qizil nur turganda komandir periskop orqali tashqariga qarasa, ko'zi darhol qorong'ilikda ko'rishga tayyor bo'ladi.",
            "ru": "Глаз адаптируется к темноте 25 минут; красный свет оставляет палочки сетчатки в 'ночном режиме', готовыми к наблюдению в перископ.",
            "en": "Human rod cells are completely insensitive to longer red wavelengths; red illumination allows paperwork without resetting night-adjusted vision."
        },
        "aliases": [
            "rodopsin",
            "tungi ko'rish",
            "qizil nur",
            "rodopsin",
            "rhodopsin",
            "night vision",
            "родопсин",
            "ночное зрение"
        ]
    },
    {
        "id": "zakovat_222",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qadimiy kutubxonalardagi eski kitoblardan keladigan o'ziga xos yoqimli, vanil va bodomga o'xshash xushbo'y hidning ilmiy sababi nima?",
            "ru": "Внимание, вопрос на логику: Какова химическая природа неповторимого сладковатого запаха старых книг, напоминающего ваниль и миндаль?",
            "en": "Attention, deductive question: What chemical process produces the distinct, nostalgic vanilla-and-almond aroma characteristic of antique books?"
        },
        "options": {
            "uz": [
                "Qog'ozdagi lignin va sellyulozaning kimyoviy parchalanishidan vanilin ajralishi",
                "Bosmaxona siyohiga atir qo'shilgani uchun",
                "Kitob muqovasiga mum surtilgani uchun",
                "Kitob do'konlari maxsus purkagan hid"
            ],
            "ru": [
                "Химический распад лигнина и целлюлозы с выделением ванилина и бензальдегида",
                "В типографскую краску добавляли эфирные масла",
                "Кожаный переплёт вымачивали в мускусе",
                "Запах порошка от книжной моли"
            ],
            "en": [
                "Chemical breakdown of paper lignin and cellulose producing vanillin",
                "Printers blended aromatic perfume into carriage ink",
                "Leather bindings were steeped in musk",
                "Mothball powders used to preserve archives"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Qog'ozdagi lignin va sellyulozaning kimyoviy parchalanishidan vanilin ajralishi",
            "ru": "Химический распад лигнина и целлюлозы с выделением ванилина и бензальдегида",
            "en": "Chemical breakdown of paper lignin and cellulose producing vanillin"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Yog'ochdan olingan qog'oz tarkibidagi lignin asrlar davomida kislorod ta'sirida parchalanadi va vanil moddasi (vanillin) hamda benzaldegid hosil qiladi.",
            "ru": "Лигнин в составе древесной бумаги окисляется со временем, распадаясь на летучие ароматические соединения — ванилин и толуол.",
            "en": "Acidic paper contains organic polymers lignin and cellulose, which slowly break down into volatile organic compounds including sweet vanillin."
        },
        "aliases": [
            "lignin",
            "vanilin",
            "sellyuloza",
            "lignin",
            "vanillin",
            "лигнин",
            "ванилин"
        ]
    },
    {
        "id": "zakovat_223",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Insonning eng nozik va himoyasiz joyini bildiruvchi 'Axilles tovoni' iborasi qaysi mifologik hodisadan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Какое мифологическое событие сделало пятку непобедимого греческого героя Ахилла его единственным смертным местом?",
            "en": "Attention, deductive question: Why was the heel of the invincible Greek demigod Achilles the only vulnerable spot on his entire body?"
        },
        "options": {
            "uz": [
                "Tovoniga ilon chaqqani uchun",
                "Onasi uni daryoga cho'mdirayotganda tovonidan ushlab turgani uchun",
                "Jangda tovoniga nayza tekkani sababli",
                "Qadimgi etigi teshik bo'lgani uchun"
            ],
            "ru": [
                "В детстве его укусила за пятку ядовитая змея",
                "Мать держала его за пятку, погружая в священные воды реки Стикс",
                "В битве при Трое ему отсекли пяточное сухожилие",
                "Священные доспехи не закрывали ступни"
            ],
            "en": [
                "A horned viper bit his foot in childhood",
                "His mother held him by the heel while dipping him into the River Styx",
                "A Trojan spear severed his calcaneal tendon",
                "Hephaestus' celestial armor lacked greaves"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Onasi uni daryoga cho'mdirayotganda tovonidan ushlab turgani uchun",
            "ru": "Мать держала его за пятку, погружая в священные воды реки Стикс",
            "en": "His mother held him by the heel while dipping him into the River Styx"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Ma'buda Fetida o'g'lini o'q o'tmas qilish uchun yerosti daryosi Stiksga botirgan, ammo uni tovonidan ushlab turgani sababli bu joyga muqaddas suv tegmay quruq qolgan.",
            "ru": "Фетида окунула младенца в реку Стикс, держа за пятку; заколдованная вода омыла всё тело, кроме этого сухожилия.",
            "en": "The goddess Thetis dipped infant Achilles into the underworld River Styx, but the heel by which she held him remained dry and mortal."
        },
        "aliases": [
            "fetida",
            "stiks",
            "tovon",
            "stiks",
            "achilles",
            "стикс",
            "пятка"
        ]
    },
    {
        "id": "zakovat_224",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ko'plab rivojlangan mamlakatlarda o't o'chirish mashinalari an'anaviy qizil emas, nima sababdan och sariq-yashil (laym) rangga o'tkazilmoqda?",
            "ru": "Внимание, вопрос на логику: Почему многие современные пожарные службы мира перекрашивают машины из красного в яркий жёлто-зелёный (салатовый) цвет?",
            "en": "Attention, deductive question: Why have international fire departments increasingly adopted lime-yellow fleet liveries over traditional fire-engine red?"
        },
        "options": {
            "uz": [
                "Bu bo'yoq zanglashdan eng yaxshi saqlaydi",
                "Qizil bo'yoq yetishmay qolgani uchun",
                "Inson ko'zi yorug'likda aynan 555 nm (och sariq-yashil) to'lqinni eng kuchli ko'radi",
                "Shaharda boshqa sariq mashinalar yo'qligi sababli"
            ],
            "ru": [
                "Жёлто-зелёная эмаль обладает рекордной стойкостью",
                "В 1970-х возник дефицит красного пигмента",
                "Пик чувствительности сетчатки приходится на длину волны 555 нм (жёлто-зелёный)",
                "Чтобы отличать пожарные машины от почтовых"
            ],
            "en": [
                "Lime enamel resisted corrosive acids best",
                "A worldwide shortage of red dye struck in 1970",
                "Retinal photopic sensitivity peaks precisely at 555 nm (yellow-green)",
                "To distinguish fire tankers from postal parcel vans"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Inson ko'zi yorug'likda aynan 555 nm (och sariq-yashil) to'lqinni eng kuchli ko'radi",
            "ru": "Пик чувствительности сетчатки приходится на длину волны 555 нм (жёлто-зелёный)",
            "en": "Retinal photopic sensitivity peaks precisely at 555 nm (yellow-green)"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Tadqiqotlar och sariq-yashil mashinalar qizil mashinalarga qaraganda tunda va qorong'ida 3 baravar kam avariyaga uchrashini isbotladi.",
            "ru": "Дневное зрение человека максимально чувствительно к желто-зеленой части спектра (555 нм), сокращая риск ДТП на 50%.",
            "en": "Human eye daylight photopic sensitivity peaks at 555 nanometers (lime-green); lime fire engines suffer 50% fewer fatal intersection collisions."
        },
        "aliases": [
            "555 nm",
            "fotopik ko'rish",
            "sariq-yashil",
            "setchatka",
            "lime yellow",
            "сетчатка",
            "длина волны"
        ]
    },
    {
        "id": "zakovat_225",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Suvga cho'kkan odam dastlab suv tubiga g'arq bo'ladi, ammo bir necha kundan so'ng nima sababdan suv yuzasiga qalqib chiqadi?",
            "ru": "Внимание, вопрос на логику: Почему тело утонувшего человека сначала тонет на дно, а через несколько дней неизбежно всплывает на поверхность?",
            "en": "Attention, deductive question: Why does a drowned body initially sink to the floor of a lake or river, only to resurface days later?"
        },
        "options": {
            "uz": [
                "Suv harorati ko'tarilib uni itarib chiqarishi",
                "Tuzlar cho'kib suv zichligini oshirishi",
                "O'pka o'zidan suvni chiqarib tashlashi",
                "Ichki chirish bakteriyalari gazlar hosil qilib tanani shishirib yuborishi"
            ],
            "ru": [
                "Вода со временем нагревается и выталкивает тело",
                "Кожа впитывает воздух из воды",
                "Плотность воды в реке спонтанно возрастает",
                "Гнилостные бактерии вырабатывают газы, раздувающие тело изнутри"
            ],
            "en": [
                "Rising river water temperatures force the corpse up",
                "The skin absorbs dissolved oxygen from currents",
                "Water density increases over days",
                "Putrefaction bacteria generate gases that inflate the submerged body"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Ichki chirish bakteriyalari gazlar hosil qilib tanani shishirib yuborishi",
            "ru": "Гнилостные бактерии вырабатывают газы, раздувающие тело изнутри",
            "en": "Putrefaction bacteria generate gases that inflate the submerged body"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Inson tanasi suvdan biroz og'irroq, ammo o'limdan keyin ichakdagi bakteriyalar metan, vodorod sulfid gazlarini ishlab chiqaradi va tana qutqaruv halqasidek qalqib chiqadi.",
            "ru": "Бактерии вызывают брожение в тканях с выделением метана и сероводорода, превращая тело в естественный поплавок.",
            "en": "The body is slightly denser than water and sinks; anaerobic bacterial decomposition produces methane and CO2 gases, turning the corpse buoyant."
        },
        "aliases": [
            "chirish gazlari",
            "bakteriyalar",
            "gnilostnie gazi",
            "decomposition gases",
            "бактерии",
            "газы"
        ]
    },
    {
        "id": "zakovat_226",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qiyin holatdan so'nggi soniyada mo''jizaviy qutulishni anglatuvchi 'Saved by the bell' (Qo'ng'iroq bilan qutqarilgan) iborasining vujudga kelishiga qaysi kashfiyot turtki bo'lgan?",
            "ru": "Внимание, вопрос на логику: Какое медицинское изобретение XIX века породило буквальное выражение 'спасён звонком' (saved by the bell)?",
            "en": "Attention, deductive question: What macabre 19th-century patent design originally inspired the phrase 'saved by the bell'?"
        },
        "options": {
            "uz": [
                "Qabrdan qutqarish uchun tobut ichidan yerdagi qo'ng'iroqqa tortilgan arqoncha",
                "Boks raundining oxirgi qo'ng'irog'i chalinsa nokaut hisoblanmasligi",
                "Maktabda dars tugaganini bildiruvchi qo'ng'iroq",
                "Cherkov qo'ng'irog'i chalinganda ibodat boshlanishi"
            ],
            "ru": [
                "Шнур из гроба, привязанный к колокольчику на могиле на случай летаргии",
                "Гонг на ринге, спасающий боксёра от нокаута",
                "Школьный звонок, спасший ученика от двойки",
                "Звон церковного колокола, отпугивающий чуму"
            ],
            "en": [
                "A cord running from inside the coffin to an above-ground cemetery bell",
                "The boxing bell ending a round before a knockout count",
                "The classroom bell saving a pupil from an exam",
                "Church bells driving away airborne epidemic miasmas"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Qabrdan qutqarish uchun tobut ichidan yerdagi qo'ng'iroqqa tortilgan arqoncha",
            "ru": "Шнур из гроба, привязанный к колокольчику на могиле на случай летаргии",
            "en": "A cord running from inside the coffin to an above-ground cemetery bell"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Odamlarni tirik ko'mib yuborishdan qo'rqib, 'xavfsiz tobutlar' ixtiro qilingan; agar tirik qolgan odam qimirlasa, qo'liga bog'langan ip yerdagi qo'ng'iroqni jaranglatgan.",
            "ru": "В патентах 'безопасных гробов' верёвка от пальца мертвеца шла к колокольчику на кладбище, чтобы сторож откопал очнувшегося.",
            "en": "Victorian 'safety coffins' featured cords tied to the deceased's fingers leading to surface bells, ensuring prematurely buried victims could alert keepers."
        },
        "aliases": [
            "qo'ng'iroq",
            "xavfsiz tobut",
            "qabr",
            "kolokolchik",
            "grob",
            "safety coffin",
            "колокольчик",
            "гроб"
        ]
    },
    {
        "id": "zakovat_227",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Shampan va ko'pikli vinolar nega keng bokalda emas, aynan uzun ingichka naychasimon qadahda (fleyta) ichiladi?",
            "ru": "Внимание, вопрос на логику: Почему шампанское принято пить из узких вытянутых бокалов-флейт (flute), а не из широких бокалов?",
            "en": "Attention, deductive question: Why is sparkling champagne customarily served in tall, slender flute glasses rather than wide shallow coupettes?"
        },
        "options": {
            "uz": [
                "Qadah tushib ketganda sinmasligi uchun",
                "Gaz pufakchalari ustunini uzun saqlash va hidni yo'qotmaslik uchun",
                "Qadah ichida kamroq vino quyish uchun",
                "Keng piyola qadimda taqiqlangani sababli"
            ],
            "ru": [
                "Узкий бокал труднее разбить при тосте",
                "Чтобы струйки пузырьков газа дольше поднимались и аромат не улетучивался",
                "Чтобы казалось, что налито много вина",
                "Из-за средневекового запрета на широкие чаши"
            ],
            "en": [
                "Narrow glasses are harder to shatter in celebratory toasts",
                "To preserve ascending bubble columns and retain sparkling effervescence",
                "To create the optical illusion of a larger pour",
                "Due to sumptuary laws banning wide bowls"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Gaz pufakchalari ustunini uzun saqlash va hidni yo'qotmaslik uchun",
            "ru": "Чтобы струйки пузырьков газа дольше поднимались и аромат не улетучивался",
            "en": "To preserve ascending bubble columns and retain sparkling effervescence"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Tor va baland qadahda gaz pufakchalari tubdan tepaga uzoq vaqt marjondek tizilib chiqadi; keng qadahda esa gaz bir necha daqiqada butunlay chiqib ketadi.",
            "ru": "В узком высоком бокале углекислый газ выходит медленно, образуя непрерывную нить мелких искрящихся пузырьков.",
            "en": "The narrow aperture and tall vertical liquid column minimize surface area, keeping effervescent carbonation bubbles dancing upward for longer."
        },
        "aliases": [
            "gaz pufakchalari",
            "flute",
            "ko'pik",
            "puzyrki",
            "bubbles",
            "effervescence",
            "пузырьки"
        ]
    },
    {
        "id": "zakovat_228",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Vazifani oson yo'l bilan, qoidalarni aylanib o'tib chala bajarishni bildiruvchi 'Cut corners' (Burchaklarni kesib o'tish) iborasi qanday harakatdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: От какого физического действия пешеходов или кучеров пошло выражение 'cut corners' (срезать углы / схалтурить)?",
            "en": "Attention, deductive question: What common pedestrian or carriage maneuver originated the English idiom 'to cut corners' (to do something poorly or quickly)?"
        },
        "options": {
            "uz": [
                "Pichoq bilan qog'oz burchagini kesish",
                "Avtomobil g'ildiragini almashtirish",
                "Chorrahada to'g'ri burchak bo'ylab emas, diagonal bo'ylab yo'lni qisqartirib o'tish",
                "Stol chetlarini yumaloqlash"
            ],
            "ru": [
                "Срезание углов пергамента ножницами",
                "Замена колёс кареты на ходу",
                "Срезание угла перекрёстка по диагонали вместо ходьбы по тротуарам",
                "Сглаживание острых углов стола"
            ],
            "en": [
                "Trimming parchment corners with shears",
                "Swapping carriage wheels mid-journey",
                "Taking a diagonal shortcut across corners instead of turning at right angles",
                "Rounding sharp carpentry table edges"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Chorrahada to'g'ri burchak bo'ylab emas, diagonal bo'ylab yo'lni qisqartirib o'tish",
            "ru": "Срезание угла перекрёстка по диагонали вместо ходьбы по тротуарам",
            "en": "Taking a diagonal shortcut across corners instead of turning at right angles"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Izvoshchilar yoki piyodalar ko'chaning to'g'ri burchakli yo'laklaridan yurmasdan, burchakdagi maysazor yoki loyni diagonal kesib vaqtni tejashgan.",
            "ru": "Кучера карет срезали поворот по диагонали через пешеходную зону, рискуя перевернуться ради экономии нескольких секунд.",
            "en": "Carriage drivers and walkers saved time by cutting diagonally across sidewalk corners rather than traversing full perpendicular blocks."
        },
        "aliases": [
            "burchakni kesish",
            "diagonal",
            "srezat ugli",
            "cut corners",
            "срезать углы",
            "диагональ"
        ]
    },
    {
        "id": "zakovat_229",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qishda yaxmalak yo'llarga oddiy tuz sepilganda qanday fizik-kimyoviy qonuniyat tufayli muz eriydi?",
            "ru": "Внимание, вопрос на логику: Какой физический закон заставляет дорожный лёд таять при посыпании обычной поваренной солью?",
            "en": "Attention, deductive question: What colligative thermodynamic property enables ordinary rock salt to melt winter ice on roadways?"
        },
        "options": {
            "uz": [
                "Tuz kimyoviy yonish hosil qilib issiqlik chiqaradi",
                "Tuz kristallari muzni mexanik maydalaydi",
                "Tuz quyosh nurlarini o'ziga tortadi",
                "Tuzli eritmaning muzlash harorati 0 darajadan ancha past (-21°C gacha) bo'ladi"
            ],
            "ru": [
                "Соль вступает в экзотермическую реакцию горения",
                "Острые кристаллы соли истирают лёд как наждак",
                "Соль притягивает инфракрасное тепло воздуха",
                "Солевой раствор имеет температуру замерзания намного ниже нуля (до -21°C)"
            ],
            "en": [
                "Salt undergoes an exothermic chemical combustion",
                "Abrasive salt crystals mechanically shred ice like sandpaper",
                "Salt molecules trap radiant thermal ambient photons",
                "Dissolved salt lowers the freezing point of water well below 0°C (down to -21°C)"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Tuzli eritmaning muzlash harorati 0 darajadan ancha past (-21°C gacha) bo'ladi",
            "ru": "Солевой раствор имеет температуру замерзания намного ниже нуля (до -21°C)",
            "en": "Dissolved salt lowers the freezing point of water well below 0°C (down to -21°C)"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Tuz muz yuzasidagi mikroskopik suv plyonkasida eriydi; paydo bo'lgan sho'r suvning muzlash nuqtasi -21°C gacha pasayadi, natijada oddiy sovuqda muz erib ketadi.",
            "ru": "Растворяясь в тонкой плёнке влаги, соль понижает точку замерзания раствора (криоскопический эффект) до -21°C.",
            "en": "Dissolved solute molecules disrupt water's crystalline lattice, causing freezing point depression down to the eutectic point (-21.1°C)."
        },
        "aliases": [
            "muzlash harorati",
            "krioskopiya",
            "sho'r suv",
            "krioskopiya",
            "freezing point",
            "температура замерзания",
            "раствор"
        ]
    },
    {
        "id": "zakovat_230",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Insonning asl basharasini va niyatini ko'rsatishini bildiruvchi 'Haqiqiy ranglarini ko'rsatmoq' (Show your true colors) iborasi qaysi dengiz qoidasidan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Из какого морского боевого закона эпохи парусного флота произошло выражение 'показать своё истинное лицо' (show true colors)?",
            "en": "Attention, deductive question: What strict naval law from the Age of Sail originated the idiom 'to show one's true colors'?"
        },
        "options": {
            "uz": [
                "Jangovar kema to'pdan o't ochishdan oldin o'z davlatining haqiqiy bayrog'ini ko'tarishi shart bo'lgan",
                "Rassomlar bo'yoqlarni aralashtirmasdan ko'rsatgan",
                "Ritsarlar dubulg'asini yechib yuzini ko'rsatgan",
                "Bayroqni yuvganda soxta ranglar ketib qolgan"
            ],
            "ru": [
                "Военный корабль был обязан по морскому праву поднять истинный флаг перед выстрелом",
                "Художники смывали лак, обнажая истинные цвета",
                "Рыцари открывали забрало шлема перед боем",
                "При стирке ткани смывалась фальшивая краска"
            ],
            "en": [
                "A warship was required by naval law to hoist its true national flag before firing",
                "Artists washed away topcoats revealing underlying oils",
                "Knights lifted vizors revealing their heraldic faces",
                "Washing uniforms purged deceptive fugitive dyes"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Jangovar kema to'pdan o't ochishdan oldin o'z davlatining haqiqiy bayrog'ini ko'tarishi shart bo'lgan",
            "ru": "Военный корабль был обязан по морскому праву поднять истинный флаг перед выстрелом",
            "en": "A warship was required by naval law to hoist its true national flag before firing"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qaroqchilar va harbiy kemalar dushmanga yaqinlashish uchun neytral yoki soxta bayroq ilib yurishi mumkin bo'lgan, ammo to'plardan o't ochishdan bir soniya oldin qonun bo'yicha o'z vatanining haqiqiy bayrog'ini (colors) ko'tarishi shart bo'lgan.",
            "ru": "Кораблям разрешалось хитрить под чужим флагом, но первый бортовой залп без поднятия истинного флага считался военным преступлением.",
            "en": "Warships routinely sailed under neutral 'false colors' to approach targets, but maritime law strictly required hoisting genuine national flags before firing."
        },
        "aliases": [
            "bayroq",
            "haqiqiy bayroq",
            "kema",
            "istinniy flag",
            "colors",
            "flag",
            "истинный флаг",
            "флаг"
        ]
    },
    {
        "id": "zakovat_231",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Katta temir-beton ko'priklarning yo'lida har 50-100 metrda taroqsimon bir-biriga kirib turuvchi metall choklar (deformatsion choklar) nega o'rnatiladi?",
            "ru": "Внимание, вопрос на логику: Зачем на пролётах больших мостов делают зубчатые металлические деформационные швы?",
            "en": "Attention, deductive question: Why are large highway and railway bridges engineered with interlocking comb-like metal expansion joints across road decks?"
        },
        "options": {
            "uz": [
                "Ko'prik ustidagi suvni pastga oqizish uchun",
                "Yozgi issiqda ko'prik metallining kengayishi va qishda qisqarishiga imkon berish uchun",
                "Mashinalar tezligini cheklash maqsadida",
                "Zilzila paytida ko'prikni bo'laklarga ajratish uchun"
            ],
            "ru": [
                "Для быстрого слива дождевой воды с пролёта",
                "Для компенсации температурного расширения металла летом и сжатия зимой",
                "Для ограничения скорости автопотока",
                "Чтобы мост разъединялся на секции при наводнении"
            ],
            "en": [
                "To drain rainwater rapidly from highway lanes",
                "To accommodate thermal expansion in summer heat and contraction in winter",
                "To act as acoustic rumble strips slowing traffic",
                "To allow bridge sections to decouple during flooding"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Yozgi issiqda ko'prik metallining kengayishi va qishda qisqarishiga imkon berish uchun",
            "ru": "Для компенсации температурного расширения металла летом и сжатия зимой",
            "en": "To accommodate thermal expansion in summer heat and contraction in winter"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Harorat o'zgarganda kilometrlik po'lat ko'prik uzunligi 1-2 metrgacha o'zgarishi mumkin; agar bu taroqsimon bo'shliqlar bo'lmasa, ko'prik yozda qisilib sinadi.",
            "ru": "Километровый стальной мост летом удлиняется на метр; зубчатые швы сжимаются и раздвигаются, спасая конструкцию от разрушения.",
            "en": "Steel spans expand significantly in summer and contract in winter; expansion joints provide room for thermal dimensional shifts without buckling."
        },
        "aliases": [
            "kengayish",
            "deformatsion chok",
            "harorat",
            "temperaturnoe rasshirenie",
            "thermal expansion",
            "температурное расширение"
        ]
    },
    {
        "id": "zakovat_232",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Benjamin Franklin ixtiro qilgan chaqmoqqaytargichlarning (yashintusharlar) uchi nega to'mtoq emas, aynan ignadek o'tkir qilinadi?",
            "ru": "Внимание, вопрос на логику: Почему верхушку молниеотвода Бенджамина Франклина делают остроконечной, как игла, а не шарообразной?",
            "en": "Attention, deductive question: Why did Benjamin Franklin insist that the tips of lightning arresters be engineered with razor-sharp metal points rather than spheres?"
        },
        "options": {
            "uz": [
                "Chaqmoq faqat dumaloq narsalarga urilmasligi uchun",
                "Yomg'ir suvi oqib tushishi uchun",
                "O'tkir uchda elektr maydoni kuchayib, havoni ionlaydi va bulut zaryadini sokin tarqatadi",
                "Chaqmoqni tutib idishga qamash uchun"
            ],
            "ru": [
                "Молния бьёт только в тупые предметы",
                "Чтобы дождевая вода легче стекала вниз",
                "Остриё создаёт высокую напряжённость поля, ионизируя воздух и стекая заряд",
                "Для накопления заряда в конденсаторах"
            ],
            "en": [
                "Lightning exclusively strikes blunt objects",
                "To allow rainwater to bead and shed cleanly",
                "Sharp points ionize air, steadily bleeding electrostatic cloud charge",
                "To store lightning current inside battery capacitors"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "O'tkir uchda elektr maydoni kuchayib, havoni ionlaydi va bulut zaryadini sokin tarqatadi",
            "ru": "Остриё создаёт высокую напряжённость поля, ионизируя воздух и стекая заряд",
            "en": "Sharp points ionize air, steadily bleeding electrostatic cloud charge"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "O'tkir metall uchida zaryad zichligi haddan tashqari baland bo'ladi; u havodagi ionlar orqali chaqmoq chaqnashidan oldinroq bulutdagi xavfli elektrni yerga sizdirib yuboradi.",
            "ru": "Высокий коронный разряд на острие ионизирует воздух, тихо стекая заряд грозового облака в землю ещё до формирования молнии.",
            "en": "Pointed tips create intense localized electric fields that initiate point-discharge corona currents, silently dissipating cloud charges."
        },
        "aliases": [
            "ionlash",
            "o'tkir uch",
            "zaryad",
            "ionizatsiya",
            "ostrie",
            "ionization",
            "sharp point",
            "ионизация",
            "остриё"
        ]
    },
    {
        "id": "zakovat_233",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qushlar 10 000 voltli ochiq elektr uzatish simlarida bemalol o'tiradi-yu, ammo nega ularni elektr toki urmaydi?",
            "ru": "Внимание, вопрос на логику: Почему птиц не бьёт током, когда они сидят на неизолированных проводах ЛЭП под напряжением 10 000 вольт?",
            "en": "Attention, deductive question: Why can birds perch safely on bare, uninsulated 10,000-volt power lines without being electrocuted?"
        },
        "options": {
            "uz": [
                "Qushlarning panjalari tok o'tkazmaydigan shox moddadan iborat",
                "Simlar qalin rezina izolyatsiya bilan o'ralgan",
                "Qushlarning vazni juda yengil bo'lgani uchun",
                "Qushning ikkala oyog'i bir xil simda bir xil potensialda turadi, potensiallar farqi yo'q"
            ],
            "ru": [
                "Лапки птиц покрыты непроницаемым диэлектрическим слоем",
                "Высоковольтные провода изолированы резиной",
                "Птицы имеют слишком малую электрическую ёмкость",
                "Обе лапки птицы на одном проводе имеют одинаковый потенциал, нет разности напряжений"
            ],
            "en": [
                "Avian claws are sheathed in non-conductive keratin",
                "High-voltage transmission cables are rubber-insulated",
                "Birds possess negligible electrostatic capacitance",
                "Both feet are on the same cable at identical potential, meaning zero voltage drop"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Qushning ikkala oyog'i bir xil simda bir xil potensialda turadi, potensiallar farqi yo'q",
            "ru": "Обе лапки птицы на одном проводе имеют одинаковый потенциал, нет разности напряжений",
            "en": "Both feet are on the same cable at identical potential, meaning zero voltage drop"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Elektr toki oqishi uchun potensiallar farqi (kuchlanish) kerak; qush faqat bitta simda turganda uning panjalari orasida qarshilik simnikidan ancha yuqori bo'lib, tok qush tanasi orqali o'tmaydi.",
            "ru": "Ток течёт только между точками с разным потенциалом; чтобы птицу ударило током, она должна коснуться столба или второго провода.",
            "en": "Electricity requires a potential difference to flow; because both feet touch the same wire at the same voltage, no current diverts through the bird's body."
        },
        "aliases": [
            "potensial",
            "kuchlanish",
            "bir xil sim",
            "raznost potentsialov",
            "potential difference",
            "разность потенциалов"
        ]
    },
    {
        "id": "zakovat_234",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Birovga xushomad qilib, uning ko'nglini olishni bildiruvchi 'To butter someone up' (Birovga sariyog' surkamoq) iborasi qaysi qadimiy diniy odatdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: От какого древнего религиозного ритуала происходит английская идиома 'умасливать кого-то' (to butter someone up)?",
            "en": "Attention, deductive question: What ancient religious practice is the origin of the English phrase 'to butter someone up'?"
        },
        "options": {
            "uz": [
                "Hindistonda ma'budalar haykallariga ezgu tilak bilan sariyog' (gxi) sharchalari uloqtirish",
                "Fransuz novvoylari nonga ko'p sariyog' surtgani uchun",
                "Eski etikni moylab yumshatish odatidan",
                "Oshxonada oshpazga pora berish odatidan"
            ],
            "ru": [
                "В Индии верующие бросали шарики топлёного масла (гхи) в статуи богов для снискания милости",
                "Французские кондитеры мазали выпечку лучшим маслом",
                "Обычай смазывать узкие сапоги жиром",
                "Способ подкупа царских поваров"
            ],
            "en": [
                "In India worshippers hurled clarified butter (ghee) balls at god statues for favor",
                "French pastry chefs applied butter to flatter patrons",
                "The custom of greasing stiff boots for courtiers",
                "Bribing royal kitchen cooks with fresh butter"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Hindistonda ma'budalar haykallariga ezgu tilak bilan sariyog' (gxi) sharchalari uloqtirish",
            "ru": "В Индии верующие бросали шарики топлёного масла (гхи) в статуи богов для снискания милости",
            "en": "In India worshippers hurled clarified butter (ghee) balls at god statues for favor"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qadimgi Hindistonda dindorlar Ganesha va Krishna haykallariga omad va baraka so'rab tozalangan sariyog' (gxi) qumoqlarini otishgan; bu xudolarga 'xushomad qilish' hisoblangan.",
            "ru": "В Индии верующие бросали шарики ароматного топлёного масла гхи в статуи божеств, вымаливая милость и богатство.",
            "en": "In ancient India, worshippers threw balls of sacred clarified butter (ghee) at statues of Ganesh and Krishna to appease the deities."
        },
        "aliases": [
            "sariyog'",
            "haykal",
            "hindiston",
            "gxi",
            "maslo",
            "butter",
            "ghee",
            "умасливать",
            "индия"
        ]
    },
    {
        "id": "zakovat_235",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Qadimgi an'anaviy Yevropa shamol tegirmonlarining qanotlari (parraklari) nima sababdan deyarli doim soat miliga teskari aylanadi?",
            "ru": "Внимание, вопрос на логику: Почему лопасти старинных европейских ветряных мельниц почти всегда вращаются против часовой стрелки?",
            "en": "Attention, deductive question: Why do the sails of traditional historic European windmills rotate counter-clockwise almost without exception?"
        },
        "options": {
            "uz": [
                "Shamol faqat soat miliga teskari esgani uchun",
                "Tegirmon qanotlarini o'ng qo'li bilan ko'tarib yasagan o'ngaqay ustalar sababli",
                "Yerning sutkalik aylanish kuchi (Koriolis kuchi)",
                "Tegirmon toshi faqat chapga aylangani uchun"
            ],
            "ru": [
                "Ветер в Европе дует преимущественно против часовой стрелки",
                "Мельникам-правшам было удобнее натягивать парусину и поворачивать лопасти",
                "Влияние силы Кориолиса в Северном полушарии",
                "Жернова мельниц могли крутиться только влево"
            ],
            "en": [
                "Prevailing European winds circulate counter-clockwise",
                "Right-handed millwrights rigged sail canvases counter-clockwise",
                "The Coriolis effect in the Northern Hemisphere",
                "Millstones were physically incapable of clockwise rotation"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Tegirmon qanotlarini o'ng qo'li bilan ko'tarib yasagan o'ngaqay ustalar sababli",
            "ru": "Мельникам-правшам было удобнее натягивать парусину и поворачивать лопасти",
            "en": "Right-handed millwrights rigged sail canvases counter-clockwise"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qadimiy tegirmon ustalari asosan o'ngaqay bo'lgan; parraklarga mato tortishda o'ng qo'lda richagni pastga tortish qanotlarning soat miliga teskari burilish burchagini shakllantirgan.",
            "ru": "Мельники-правши забирались на крылья и натягивали паруса правой рукой, задавая наклон лезвий против часовой стрелки.",
            "en": "Centuries of right-handed millwrights climbing sail frames rigged cloths with their dominant right hand, setting the bevel for counter-clockwise rotation."
        },
        "aliases": [
            "o'ngaqay ustalar",
            "parrak",
            "soat miliga teskari",
            "pravshi",
            "right-handed",
            "мельники",
            "правши"
        ]
    },
    {
        "id": "zakovat_236",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ortiqcha qog'ozbozlik va sansalorlikni anglatuvchi 'Qizil tasma' (Red tape / Krasnaya lenta) iborasi qayerdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: Откуда происходит международное выражение 'red tape' (красная лента) в значении 'бюрократические проволочки'?",
            "en": "Attention, deductive question: What historical administrative practice gave rise to the term 'red tape' meaning frustrating bureaucratic delays?"
        },
        "options": {
            "uz": [
                "Qizil rangli muhrlar qo'yilgani sababli",
                "Qonun kitoblarining muqovasi qizil bo'lgani uchun",
                "Britaniya va Ispaniyada rasmiy davlat hujjatlari qizil lenta bilan bog'langan",
                "Chinovniklar qizil mundir kiygani sababli"
            ],
            "ru": [
                "Красный сургуч ставился на всех королевских бумагах",
                "Обложки уголовных кодексов были ярко-красными",
                "В Британии и Испании правительственные судебные декреты связывали красной лентой",
                "Чиновники носили красные форменные петлицы"
            ],
            "en": [
                "Red sealing wax was affixed to all crown mandates",
                "Criminal legal statutes were bound in crimson leather",
                "Official government and legal dossiers were bound with red or pink cloth tape",
                "Bureaucrats wore red collar tabs on uniforms"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Britaniya va Ispaniyada rasmiy davlat hujjatlari qizil lenta bilan bog'langan",
            "ru": "В Британии и Испании правительственные судебные декреты связывали красной лентой",
            "en": "Official government and legal dossiers were bound with red or pink cloth tape"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "17-asrdan boshlab Angliyada barcha rasmiy sud ishlari va qonun loyihalari qizil yoki pushti rangli lenta bilan qattiq bog'langan; ishni ochish uchun 'tasmani yechish' kerak bo'lgan.",
            "ru": "Британские чиновники перевязывали кипы судебных документов красной хлопковой лентой (red tape), требовавшей долгой возни для вскрытия.",
            "en": "In English and Spanish chancery courts, official case briefs were tied up with red or pink cotton twill tape, symbolizing cumbersome protocol."
        },
        "aliases": [
            "qizil lenta",
            "qog'ozbozlik",
            "red tape",
            "krasnaya lenta",
            "красная лента",
            "бюрократия"
        ]
    },
    {
        "id": "zakovat_237",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Temir yo'l relslari va shpallari ostiga nega silliq daryo toshlari emas, aynan burchakli chaqiq toshlar (ballast) to'shaladi?",
            "ru": "Внимание, вопрос на логику: Почему железнодорожные пути укладывают на подушку из остроугольного гранитного щебня, а не на гладкую речную гальку?",
            "en": "Attention, deductive question: Why are railroad ties bedded on sharp, jagged crushed stone ballast rather than smooth rounded river gravel?"
        },
        "options": {
            "uz": [
                "Toshlar relslarni zanglashdan asraydi",
                "Chaqiq toshlar boshqa toshlardan arzonroq",
                "Poyezd g'ildiraklarini tozalab turadi",
                "Qirrali toshlar og'irlikda bir-biriga qisilib qulflanadi, relsni siljitmaydi va suvni tez quritadi"
            ],
            "ru": [
                "Щебень химически защищает шпалы от гниения",
                "Битый камень был самым дешёвым балластом",
                "Камни полируют колеса вагонов от нагара",
                "Остроугольный щебень сцепляется гранями, гасит вибрацию и отводит дождевую воду"
            ],
            "en": [
                "Crushed rock chemically repels fungal decay in ties",
                "Broken stone was universally subsidized",
                "Track stones polish wagon wheel flanges clean",
                "Sharp angular stones interlock under load, stabilize ties, and drain water"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Qirrali toshlar og'irlikda bir-biriga qisilib qulflanadi, relsni siljitmaydi va suvni tez quritadi",
            "ru": "Остроугольный щебень сцепляется гранями, гасит вибрацию и отводит дождевую воду",
            "en": "Sharp angular stones interlock under load, stabilize ties, and drain water"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Silliq toshlar poyezd og'irligida dumalab ketgan bo'lardi; burchakli toshlar esa bir-biriga tishlashib qattiq monolit hosil qiladi va relslarni qimirlatmaydi.",
            "ru": "Гладкая галька скользила бы под тяжестью состава; острые грани щебня заклинивают друг друга, создавая гибкую и неподвижную опору.",
            "en": "Rounded gravel slides under axle loads; sharp crushed aggregate stones lock together like puzzle pieces, holding tracks securely aligned."
        },
        "aliases": [
            "chaqiq tosh",
            "ballast",
            "qulflanish",
            "sheben",
            "ballast",
            "щебень",
            "вибрация"
        ]
    },
    {
        "id": "zakovat_238",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Biron sirni muddatidan oldin yoki tasodifan fosh qilib qo'yishni bildiruvchi 'Spill the beans' (Loviyalarni to'kib yubormoq) iborasi qanday paydo bo'lgan?",
            "ru": "Внимание, вопрос на логику: Откуда возникла английская идиома 'spill the beans' (проболтаться, выдать секрет)?",
            "en": "Attention, deductive question: What electoral procedure in ancient Greece is the origin of the English idiom 'to spill the beans' (to reveal a secret)?"
        },
        "options": {
            "uz": [
                "Qadimgi Yunonistonda ovoz berishda ko'zadan oq va qora loviyalar to'kilib ketib sir fosh bo'lgan",
                "Qop yirtilib loviyalar yerga sochilgan",
                "Sehrgarlar loviya orqali fol ochgan",
                "Oshpaz qozonga loviyani to'kib yuborgan"
            ],
            "ru": [
                "При голосовании бобами в Греции кувшин опрокидывался, раскрывая тайну выборов раньше времени",
                "Мешок торговца рвался на рыночной площади",
                "Оракулы гадали по упавшим на землю бобам",
                "Повар случайно рассыпал бобы в печь"
            ],
            "en": [
                "Jars of voting beans overturned in Greece, prematurely revealing secret ballot counts",
                "A merchant's sack ripped open on the agora",
                "Oracles cast lots by scattering dry fava beans",
                "A temple cook overturned sacred bean soup"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Qadimgi Yunonistonda ovoz berishda ko'zadan oq va qora loviyalar to'kilib ketib sir fosh bo'lgan",
            "ru": "При голосовании бобами в Греции кувшин опрокидывался, раскрывая тайну выборов раньше времени",
            "en": "Jars of voting beans overturned in Greece, prematurely revealing secret ballot counts"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qadimgi Afinada mansabdorlarni saylashda har bir fuqaro ko'zaga oq (ha) yoki qora (yo'q) loviya tashlagan; agar ko'za to'kilib ketsa, saylov natijasi vaqtidanoq fosh bo'lgan.",
            "ru": "В Древней Греции голосовали белыми (за) и чёрными (против) бобами; случайное опрокидывание урны досрочно раскрывало результат.",
            "en": "Ancient Greeks voted in secret societies using white (affirmative) and black (negative) beans; an overturned jar spilled the clandestine votes."
        },
        "aliases": [
            "loviya",
            "ovoz berish",
            "yunoniston",
            "spill the beans",
            "бобы",
            "голосование"
        ]
    },
    {
        "id": "zakovat_239",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Ming yillik Misr ehromlaridan topilgan asal ham nima sababdan mutlaqo buzilmaydi va iste'molga yaroqli bo'lib qoladi?",
            "ru": "Внимание, вопрос на логику: Какое биохимическое свойство делает мёд единственным природным продуктом, который никогда не портится?",
            "en": "Attention, deductive question: Why does pure natural honey have an essentially infinite shelf life without spoiling or decaying?"
        },
        "options": {
            "uz": [
                "Asalda tabiiy alkogol bo'lgani uchun",
                "Yuqori shakar konsentratsiyasi bakteriyalardagi suvni tortib olib (osmos), ularni quritadi",
                "Asalarilar asalga zahar qo'shgani uchun",
                "Asal har doim muzlab turgani uchun"
            ],
            "ru": [
                "Мёд содержит природные соединения спирта",
                "Высокая концентрация сахаров вытягивает воду из бактерий осмосом, убивая их",
                "Пчёлы консервируют мёд змеиным ядом",
                "Мёд имеет температуру ниже комнатной"
            ],
            "en": [
                "Honey contains high concentrations of ethyl alcohol",
                "High sugar concentration draws water out of bacteria by osmosis, desiccating them",
                "Bees inject preservative venom into combs",
                "Honey remains sub-ambient in cellar storage"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Yuqori shakar konsentratsiyasi bakteriyalardagi suvni tortib olib (osmos), ularni quritadi",
            "ru": "Высокая концентрация сахаров вытягивает воду из бактерий осмосом, убивая их",
            "en": "High sugar concentration draws water out of bacteria by osmosis, desiccating them"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Asalning namligi 17-18% dan oshmaydi; bunday gipertonik shakarli muhitga tushgan har qanday mikrob osmotik bosim tufayli butun suvidan ayrilib nobud bo'ladi.",
            "ru": "Осмотическое давление сахаров буквально высасывает влагу из клеток любых бактерий, делая их размножение невозможным.",
            "en": "Honey's low moisture content creates high osmotic pressure, dehydrating any invading microbial cells through plasmolysis."
        },
        "aliases": [
            "osmos",
            "suvsizlanish",
            "bakteriyalar",
            "osmos",
            "osmotic",
            "осмос",
            "сахар"
        ]
    },
    {
        "id": "zakovat_240",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Biror kamchilik yoki qonunbuzarlikka 'ko'z yummoq' ma'nosidagi 'Turn a blind eye' (Ko'r ko'zni burmoq) iborasi qaysi buyuk sarkardaga tegishli?",
            "ru": "Внимание, вопрос на логику: Какой великий флотоводец подарил миру выражение 'смотреть сквозь пальцы / закрыть глаза' (turn a blind eye)?",
            "en": "Attention, deductive question: Which legendary British naval commander originated the idiom 'to turn a blind eye' at the Battle of Copenhagen?"
        },
        "options": {
            "uz": [
                "Rim qozisi ko'zi bog'liq holda hukm chiqargani uchun",
                "Kipr podshosi bir ko'zini yumib o'tirgani sababli",
                "Admiral Nelson Kopengagen jangida chekinish signalini ko'rmaslik uchun durbinni ko'r ko'ziga qo'ygan",
                "Qaroqchilar bir ko'zini yopib jang qilgani uchun"
            ],
            "ru": [
                "Римский судья выносил приговор с повязкой на глазах",
                "Царь Кипра слушал просителей с закрытыми глазами",
                "Адмирал Нельсон приставил подзорную трубу к слепому глазу, проигнорировав приказ об отступлении",
                "Пиратский капитан целился слепым глазом"
            ],
            "en": [
                "Roman magistrates judged with blindfolds",
                "The King of Cyprus closed one eye during hearings",
                "Admiral Nelson put his telescope to his blind eye to ignore a retreat signal",
                "Pirate captains aimed muskets with blind eyes"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Admiral Nelson Kopengagen jangida chekinish signalini ko'rmaslik uchun durbinni ko'r ko'ziga qo'ygan",
            "ru": "Адмирал Нельсон приставил подзорную трубу к слепому глазу, проигнорировав приказ об отступлении",
            "en": "Admiral Nelson put his telescope to his blind eye to ignore a retreat signal"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "1801-yilda Kopengagendagi dengiz jangida flagman kema chekinish bayrog'ini ko'targanda, Nelson durbinni jarohatlangan ko'r ko'ziga qo'yib: 'Men hech qanday signalni ko'rmayapman!' deya g'alaba qozongan.",
            "ru": "В 1801 году при Копенгагене Горацио Нельсон приставил трубу к повреждённому глазу, заявил, что не видит сигнала, и выиграл битву.",
            "en": "At Copenhagen in 1801, Admiral Horatio Nelson put his spyglass to his blind right eye, feigning inability to see his superior's signal to withdraw."
        },
        "aliases": [
            "nelson",
            "admiral nelson",
            "ko'r ko'z",
            "kopengagen",
            "нельсон",
            "blind eye",
            "горио"
        ]
    },
    {
        "id": "zakovat_241",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Sovun pufaklarini qanday shakldagi teshikdan (hatto kvadrat yoki uchburchak) puflasangiz ham, nega havoda doimo mukammal shar hosil bo'ladi?",
            "ru": "Внимание, вопрос на логику: Почему мыльный пузырь в воздухе всегда принимает форму идеальной сферы, даже если выдувать его через квадратную рамку?",
            "en": "Attention, deductive question: Why do soap bubbles floating in air always snap into a perfect sphere, even when blown through a square or triangle-shaped wand?"
        },
        "options": {
            "uz": [
                "Ichidagi havo sharsimon aylangani uchun",
                "Sovun molekulalari faqat dumaloq bo'lgani uchun",
                "Naychaning teshigi dumaloq bo'lgani tufayli",
                "Sirt taranglik kuchi berilgan hajm uchun minimal sirt maydonini (sharni) hosil qiladi"
            ],
            "ru": [
                "Воздух внутри пузыря вращается по кругу",
                "Молекулы мыла имеют форму микрошариков",
                "Отверстие трубочки всегда круглое",
                "Поверхностное натяжение стремится минимизировать площадь поверхности сферы"
            ],
            "en": [
                "Internal air swirls in a circular vortex",
                "Soap molecules are shaped like micro-spheres",
                "The blowing wand ring is circular",
                "Surface tension minimizes surface area for any given volume into a sphere"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Sirt taranglik kuchi berilgan hajm uchun minimal sirt maydonini (sharni) hosil qiladi",
            "ru": "Поверхностное натяжение стремится минимизировать площадь поверхности сферы",
            "en": "Surface tension minimizes surface area for any given volume into a sphere"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Geometriyada ma'lum bir hajmdagi havoni o'rash uchun eng kichik sirt maydoniga ega shakl shardir; sovun plyonkasidagi tortishish kuchi uni sharga aylantiradi.",
            "ru": "Сфера обладает наименьшей площадью поверхности при заданном объёме, минимизируя энергию поверхностного натяжения плёнки.",
            "en": "Surface tension pulls the liquid film into the shape with the lowest possible surface area for a given enclosed volume: a sphere."
        },
        "aliases": [
            "sirt taranglik",
            "minimal yuza",
            "shar",
            "poverxnostnoe natyajenie",
            "surface tension",
            "поверхностное натяжение",
            "сфера"
        ]
    },
    {
        "id": "zakovat_242",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Kuchli chelaklab quyayotgan yomg'irni anglatuvchi 'Raining cats and dogs' (It-mushuk yog'moqda) iborasi qaysi me'moriy holatdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: С какой особенностью средневековых жилищ связано выражение 'дождь льёт кошками и собаками' (raining cats and dogs)?",
            "en": "Attention, deductive question: What medieval architectural roof design is believed to have inspired the idiom 'it's raining cats and dogs'?"
        },
        "options": {
            "uz": [
                "Qadimgi somon tomlarda uxlagan mushuk va itlar kuchli jalada sirg'alib yerga tushgan",
                "Qadimda osmondan haqiqatan hayvonlar yoqqani uchun",
                "Mushuk va itlar janjallashgandek momaqaldiroq bo'lgani sababli",
                "Qadimgi ovchilar itlarini yomg'irda qoldirgani sababli"
            ],
            "ru": [
                "В старину спавшие на соломенных крышах кошки и собаки соскальзывали вниз в ливень",
                "В древности с неба падали животные, поднятые смерчем",
                "Шум дождя напоминал вой собак и кошачьи драки",
                "Охотники теряли собак в сильный дождь"
            ],
            "en": [
                "Cats and dogs sheltering in thatched roofs slid off during torrential cloudbursts",
                "Tornados lifted animals and dropped them as rain",
                "Rain noise sounded like howling dogs and fighting cats",
                "Hunters lost their packs of dogs during torrential rain"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Qadimgi somon tomlarda uxlagan mushuk va itlar kuchli jalada sirg'alib yerga tushgan",
            "ru": "В старину спавшие на соломенных крышах кошки и собаки соскальзывали вниз в ливень",
            "en": "Cats and dogs sheltering in thatched roofs slid off during torrential cloudbursts"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "O'rta asrlarda uylarning tomi qalin qamish va somondan bo'lib, uy hayvonlari tomdagi issiq somonda uxlagan; kuchli jala quyib tom ivib ketganda jonivorlar yerga toyib tushgan.",
            "ru": "В бедных домах Англии кошки и собаки грелись в соломенных стрехах; во время шторма промокавшая солома смывала питомцев во двор.",
            "en": "In 16th-century thatched cottages, domestic animals nestled in straw roofs for warmth; violent deluges washed them out into muddy streets."
        },
        "aliases": [
            "somon tom",
            "mushuk va it",
            "jala",
            "solomennaya krysha",
            "thatched roof",
            "соломенная крыша"
        ]
    },
    {
        "id": "zakovat_243",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Nima sababdan makkajo'xorining maxsus navi donalari qizdirilganda paqillab 'popkorn'ga aylanadi, boshqa donlar esa erimaydi?",
            "ru": "Внимание, вопрос на логику: Какое уникальное сочетание влаги и крахмала заставляет зёрна попкорна взрываться белоснежной пеной при нагреве?",
            "en": "Attention, deductive question: What physical mechanism causes popcorn kernels to violently pop into fluffy white foam when heated?"
        },
        "options": {
            "uz": [
                "Makkajo'xori yog'i qizib ketishi tufayli",
                "Don ichidagi 14% namlik qizdirilganda bug'ga aylanib, qattiq qobiqni portlatib yuboradi",
                "Ichidagi kraxmal kimyoviy reaksiyaga kirishgani uchun",
                "Don qobig'ida dinamit moddasi borligi sababli"
            ],
            "ru": [
                "Кукурузное масло самовоспламеняется внутри",
                "14% влаги внутри зерна при нагреве вскипают в пар, разрывая твёрдую оболочку изнутри",
                "Крахмал вступает в бурную реакцию с воздухом",
                "В зернах накапливается пороховой газ"
            ],
            "en": [
                "Internal corn oil auto-ignites from thermal friction",
                "Moisture trapped in the kernel flashes to steam, bursting the hull inside out",
                "Kernel starch reacts exothermically with atmospheric air",
                "Pressurized grain enzymes spontaneously combust"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Don ichidagi 14% namlik qizdirilganda bug'ga aylanib, qattiq qobiqni portlatib yuboradi",
            "ru": "14% влаги внутри зерна при нагреве вскипают в пар, разрывая твёрдую оболочку изнутри",
            "en": "Moisture trapped in the kernel flashes to steam, bursting the hull inside out"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Popkorn donasi suv o'tkazmaydigan qattiq po'stloqqa ega; qizdirilganda ichidagi suv bug'ga aylanib bosim 9 atmosferaga yetadi va kraxmal ko'pikka aylanib tashqariga yoriladi.",
            "ru": "Твёрдый перикарпий удерживает пар до 180°C и давления 9,3 атм; в момент взрыва желатинизированный крахмал застывает пеной.",
            "en": "The hard, non-porous hull traps steam until internal pressure reaches 135 psi (180°C), rupturing the hull and flash-freezing the starch into foam."
        },
        "aliases": [
            "namlik",
            "bug'",
            "bosim",
            "portlash",
            "vlag",
            "par",
            "steam",
            "explosion",
            "пар",
            "влага"
        ]
    },
    {
        "id": "zakovat_244",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Xato taxmin qilib, noto'g'ri odamdan gumon qilishni anglatuvchi 'Barking up the wrong tree' (Noto'g'ri daraxtga qarab hurmoq) iborasi qayerdan paydo bo'lgan?",
            "ru": "Внимание, вопрос на логику: Откуда в охотничьей терминологии США родилась идиома 'лаять не на то дерево' (barking up the wrong tree)?",
            "en": "Attention, deductive question: What 19th-century American hunting practice gave birth to the idiom 'barking up the wrong tree'?"
        },
        "options": {
            "uz": [
                "Qadimgi o'rmonchilar adashib daraxtlarni belgilagani",
                "Itlar daraxt sharpasidan qo'rqqani",
                "Ov itlari yenot boshqa daraxtga sakrab ketganini sezmay, bo'sh daraxtga qarab hurishi",
                "Ovchilar adashib o'rmonga o'q uzgani"
            ],
            "ru": [
                "Лесорубы по ошибке метили не те сосны",
                "Собаки пугались скрипа сухих ветвей",
                "Охотничьи гончие лаяли на дерево, с которого енот давно перепрыгнул на соседнее",
                "Охотники стреляли в птичьи гнезда вместо дичи"
            ],
            "en": [
                "Lumberjacks accidentally chalked the wrong timber",
                "Hunting dogs grew terrified of creaking branches",
                "Hounds baying at a tree after a raccoon leaped into an adjacent canopy",
                "Hunters shot at old squirrels' nests instead of game"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Ov itlari yenot boshqa daraxtga sakrab ketganini sezmay, bo'sh daraxtga qarab hurishi",
            "ru": "Охотничьи гончие лаяли на дерево, с которого енот давно перепрыгнул на соседнее",
            "en": "Hounds baying at a tree after a raccoon leaped into an adjacent canopy"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Amerikada tunda yenot ovlagan itlar hayvonni daraxtga qamagan, ammo ayyor yenot shoxlar orqali boshqa daraxtga o'tib ketgach, itlar bo'sh daraxt tagida uzoq vaqt hurib qolgan.",
            "ru": "Еноты часто прыгают с ветки на ветку, уходя верхом; собаки теряют след и продолжают азартно лаять на пустое дерево.",
            "en": "Coonhounds chased nocturnal raccoons up trees, but agile quarry often leaped to adjacent branches while dogs bayed below an empty trunk."
        },
        "aliases": [
            "yenot",
            "itlar hurishi",
            "daraxt",
            "enot",
            "gonchie",
            "raccoon",
            "barking",
            "енот",
            "гончие"
        ]
    },
    {
        "id": "zakovat_245",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Flamingolar uxlab yotganda nega uzun bo'ynini burib, boshini qanotlari va orqa patlari orasiga yashirib oladi?",
            "ru": "Внимание, вопрос на логику: Зачем фламинго во время сна на одной ноге прячут клюв и голову глубоко под крыло?",
            "en": "Attention, deductive question: Why do sleeping flamingos twist their long necks backward to bury their bills under their wing feathers?"
        },
        "options": {
            "uz": [
                "Ko'ziga tonggi yorug'lik tushmasligi uchun",
                "Bo'ynini og'irligini muvozanatlash maqsadida",
                "Boshqa qushlardan qo'rqqanligi uchun",
                "Tumshuq va ko'zdagi nozik teridan tana issiqligi yo'qolishining oldini olish uchun"
            ],
            "ru": [
                "Чтобы утреннее солнце не будило птицу",
                "Для удержания центра тяжести на ветру",
                "Чтобы спрятать глаза от летающих хищников",
                "Чтобы уменьшить потерю драгоценного тепла через неоперённый клюв и глаза"
            ],
            "en": [
                "To shield retinas from early sunrise rays",
                "To counterbalance body center of gravity",
                "To hide reflective eyes from raptors",
                "To minimize body heat loss through the bare bill and eye skin"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Tumshuq va ko'zdagi nozik teridan tana issiqligi yo'qolishining oldini olish uchun",
            "ru": "Чтобы уменьшить потерю драгоценного тепла через неоперённый клюв и глаза",
            "en": "To minimize body heat loss through the bare bill and eye skin"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Flamingoning tumshug'i va ko'z atrofidagi teri yalang'och bo'lib, shamolda tana haroratini tez yo'qotadi; patlar orasiga yashirish qushga issiqlikni saqlashga yordam beradi.",
            "ru": "Голова и клюв лишены изолирующего пуха; укутывание мордочки в перья служит птице тёплым шарфом.",
            "en": "The head, bill, and facial skin lack insulating down; tucking the head into dorsal plumage seals the main thermal leakage point."
        },
        "aliases": [
            "issiqlik saqlash",
            "boshini yashirish",
            "teplo",
            "feathers",
            "heat loss",
            "перья",
            "тепло"
        ]
    },
    {
        "id": "zakovat_246",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Alisaning mo''jizalar olamidagi 'Telba Shlyapadoz' (Mad Hatter) obrazi va ushbu ibora 19-asrdagi qaysi kasbiy kasallikdan kelib chiqqan?",
            "ru": "Внимание, вопрос на логику: С каким профессиональным отравлением шляпных мастеров XIX века связана фраза 'безумен как шляпник' (mad as a hatter)?",
            "en": "Attention, deductive question: What historical occupational poisoning syndrome gave rise to Lewis Carroll's 'Mad Hatter' and the phrase 'mad as a hatter'?"
        },
        "options": {
            "uz": [
                "Kigiz shlyapalar tayyorlashda ishlatilgan simob nitratidan surunkali zaharlanish",
                "Shlyapaning torligi miyani siqib qo'ygani uchun",
                "Bo'yoq bug'laridan hushdan ketish",
                "Qadimgi shlyapachilar ko'p spirtli ichimlik ichgani"
            ],
            "ru": [
                "Хроническое отравление нитратом ртути при обработке фетра для шляп",
                "Тесные головные уборы нарушали кровоток мозга",
                "От паров клея мастера теряли рассудок",
                "Шляпники работали без сна сутками"
            ],
            "en": [
                "Chronic mercury nitrate poisoning from curing felt for hats",
                "Tight hat bands restricted cranial blood flow",
                "Glue fumes permanently altered neurotransmitters",
                "Milliners worked sleep-deprived around the clock"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "Kigiz shlyapalar tayyorlashda ishlatilgan simob nitratidan surunkali zaharlanish",
            "ru": "Хроническое отравление нитратом ртути при обработке фетра для шляп",
            "en": "Chronic mercury nitrate poisoning from curing felt for hats"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Qunduz terisidan kigiz yasashda simob tuzlari ishlatilgan; simob bug'lari ustalar asab tizimini shikastlab, titroq, so'zlash buzilishi va telbalik keltirib chiqargan.",
            "ru": "Нитрат ртути применялся для размягчения шерсти бобра; пары ртути вызывали у шляпников психозы, тремор и потерю памяти.",
            "en": "Hatters used mercuric nitrate to process animal fur into felt; prolonged vapor inhalation caused 'mad hatter syndrome' (erethism and dementia)."
        },
        "aliases": [
            "simob",
            "zaharlanish",
            "shlyapadoz",
            "rtut",
            "mercury",
            "hatter",
            "ртуть",
            "отравление"
        ]
    },
    {
        "id": "zakovat_247",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Tuyaning o'rkachida suv emas, 35 kg gacha yog' saqlanishining cho'l issig'iga moslashishdagi asosiy siri nimada?",
            "ru": "Внимание, вопрос на логику: Какое терморегуляционное преимущество даёт верблюду то, что весь жировой запас (до 35 кг) собран в горбу, а не распределён по телу?",
            "en": "Attention, deductive question: What key thermal advantage does a desert camel gain by concentrating up to 35 kg of fat in a single dorsal hump rather than under its skin?"
        },
        "options": {
            "uz": [
                "O'rkachda 100 litr toza suv saqlanadi",
                "Yog'ning faqat bitta joyda to'planishi badanning qolgan qismidan issiqlik erkin tarqalishiga yo'l beradi",
                "O'rkach quyosh nurini qaytaruvchi qalqondir",
                "Tuyaning orqa miyasini zarbadan asrash uchun"
            ],
            "ru": [
                "В горбу запасено до 150 литров чистой пресной воды",
                "Концентрация жира в одном месте позволяет остальному телу свободно отдавать тепло",
                "Горб служит теневым зонтом для боков верблюда",
                "Горб защищает позвоночник от палящего солнца"
            ],
            "en": [
                "The humps store up to 150 liters of pure water",
                "Concentrating body fat in one dorsal mound allows cooling across the torso",
                "The hump serves as an umbrella shading the flanks",
                "The hump protects the spine from desert solar radiation"
            ]
        },
        "correct_index": 1,
        "correct_answer": {
            "uz": "Yog'ning faqat bitta joyda to'planishi badanning qolgan qismidan issiqlik erkin tarqalishiga yo'l beradi",
            "ru": "Концентрация жира в одном месте позволяет остальному телу свободно отдавать тепло",
            "en": "Concentrating body fat in one dorsal mound allows cooling across the torso"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Agar yog' boshqa hayvonlardek butun tana bo'ylab teng taqsimlansa, u ko'rpadek issiqlikni ushlab qolib, tuya 50 daraja jaziramada qizib o'lgan bo'lardi; yupqa terili qorin va yonboshlar esa tanani tez sovutadi.",
            "ru": "Подкожный слой жира сработал бы как одеяло, убив верблюда перегревом; голые бока позволяют телу охлаждаться ночью.",
            "en": "If insulating fat was distributed subcutaneous over the whole body like a blanket, the camel could not dissipate heat and would suffer fatal heatstroke."
        },
        "aliases": [
            "yog'",
            "issiqlik tarqalishi",
            "o'rkach",
            "jir",
            "termoregulyatsiya",
            "fat",
            "hump",
            "жир",
            "терморегуляция"
        ]
    },
    {
        "id": "zakovat_248",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Kitoblarda Sherlok Xolms to'g'ri yog'och naycha chekkan bo'lsa-da, tasviriy san'atda va kinoda nega u doimo bahaybat egik (kalabash) naycha bilan gavdalanadi?",
            "ru": "Внимание, вопрос на логику: Почему шерлок холмс в массовой культуре курит изогнутую трубку калабаш, хотя в книгах конан дойля курил короткую глиняную?",
            "en": "Attention, deductive question: Why is Sherlock Holmes universally depicted smoking a dramatic curved calabash pipe, despite Arthur Conan Doyle describing straight briar pipes?"
        },
        "options": {
            "uz": [
                "Conan Doyle kitobda aynan shu naychani tasvirlagani uchun",
                "Egik naychadan tutun to'g'ri ko'zga tushmasligi uchun",
                "Sahnada aktyor gapirganda tomoshabinlar uning yuzini va lablarini aniq ko'rishi uchun",
                "Qadimgi detektivlar faqat shunday naycha chekkani uchun"
            ],
            "ru": [
                "Конан Дойль детально описал именно изогнутую трубку",
                "Изогнутая трубка давала более холодный дым",
                "Чтобы на театральной сцене изогнутая трубка не заслоняла лицо и мимику актёра",
                "Такую трубку сложнее уронить при беге"
            ],
            "en": [
                "Conan Doyle explicitly specified a curved calabash in novels",
                "Curved stems generated cooler, mellower smoke",
                "So the actor's face and mouth were not blocked from the stage audience",
                "Curved pipes were impossible to drop while chasing villains"
            ]
        },
        "correct_index": 2,
        "correct_answer": {
            "uz": "Sahnada aktyor gapirganda tomoshabinlar uning yuzini va lablarini aniq ko'rishi uchun",
            "ru": "Чтобы на театральной сцене изогнутая трубка не заслоняла лицо и мимику актёра",
            "en": "So the actor's face and mouth were not blocked from the stage audience"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "1899-yilda teatrda Xolms rolini o'ynagan aktyor Uilyam Jillett to'g'ri naycha monolog aytayotganda lablarini to'sib qo'ymasligi uchun egik naychani o'ylab topgan.",
            "ru": "Актёр Уильям Жиллетт на Бродвее выбрал загнутую трубку, чтобы зрители видели мимику лица во время монологов.",
            "en": "American actor William Gillette adopted the deep-curved calabash pipe on stage in 1899 so his face, jaw, and spoken lines were clearly visible to audiences."
        },
        "aliases": [
            "aktyor",
            "yuzini to'smaslik",
            "jillett",
            "teatr",
            "aktr",
            "william gillette",
            "face",
            "актер",
            "лицо"
        ]
    },
    {
        "id": "zakovat_249",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Eski poyezdlarda ketayotganda eshitiladigan mashhur 'duk-duk, duk-duk' ritmik tovushining fizik sababi nima?",
            "ru": "Внимание, вопрос на логику: Отчего возникает классический стук колес поезда 'чух-чух / тук-тук' на старых железнодорожных путях?",
            "en": "Attention, deductive question: What causes the rhythmic 'clickety-clack' cadence of train wheels rolling over traditional jointed railway tracks?"
        },
        "options": {
            "uz": [
                "Poyezd tezligini sekinlashtirish uchun",
                "G'ildiraklardagi temir tishchalarning urilishi",
                "Shpallarning yerga cho'kishi natijasida",
                "Relslar issiqda kengayganda qiyshayib ketmasligi uchun qoldirilgan oraliq tirqishlar"
            ],
            "ru": [
                "Специальные насечки для предотвращения пробуксовки",
                "Следствие износа и овальности колёсных пар",
                "Вибрация стыков шпал в щебёночном балласте",
                "Температурные зазоры на стыках рельсов, оставленные на случай летнего расширения"
            ],
            "en": [
                "Anti-slip traction notches stamped onto railheads",
                "Asymmetric flat spots worn onto wheel tires",
                "Vibrational flexing of wooden cross-ties against ballast",
                "Thermal expansion gaps left between steel rails to prevent buckling"
            ]
        },
        "correct_index": 3,
        "correct_answer": {
            "uz": "Relslar issiqda kengayganda qiyshayib ketmasligi uchun qoldirilgan oraliq tirqishlar",
            "ru": "Температурные зазоры на стыках рельсов, оставленные на случай летнего расширения",
            "en": "Thermal expansion gaps left between steel rails to prevent buckling"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Har bir 12,5 yoki 25 metrli rels oralig'ida yozgi issiqda metall kengayishi uchun bir necha millimetr bo'shliq qoldiriladi; g'ildirak bu tirqishdan o'tganda zarb bilan uriladi.",
            "ru": "Каждые 25 метров рельсы стыкуются с зазором в пару сантиметров для теплового расширения; колесо ударяется о край зазора.",
            "en": "Rail sections were bolted with expansion gaps between fishplates; heavy wheels striking these gaps produced the characteristic acoustic cadence."
        },
        "aliases": [
            "rels oraliqlari",
            "tirqish",
            "kengayish",
            "zazor",
            "relsi",
            "rail gaps",
            "стыки",
            "зазор"
        ]
    },
    {
        "id": "zakovat_250",
        "type": "deduction",
        "question": {
            "uz": "Diqqat, mantiqiy savol: Futbol maydonlaridagi va golf maydonlaridagi mukammal och va to'q yashil yo'l-yo'l chiziqlar qanday qilib hosil qilinadi?",
            "ru": "Внимание, вопрос на логику: Как агрономы создают безупречные чередующиеся светлые и тёмные полосы на футбольных газонах?",
            "en": "Attention, deductive question: How are alternating dark and light parallel stripes created across football pitches and golf fairways?"
        },
        "options": {
            "uz": [
                "O'roq mashinasining orqa valigi maysani tomoshabinga qarab yoki teskari tomonga yotqizishi",
                "Maysa ikki xil navli urug'dan ekilgani uchun",
                "Maysaning bir qismiga o'g'it ko'p berilgani sababli",
                "Qorong'i chiziqlardagi maysa bo'yalgani sababli"
            ],
            "ru": [
                "Каток газонокосилки приминает травинку 'к зрителю' или 'от зрителя', меняя отражение света",
                "Полосы засеяны двумя разными сортами злаков",
                "На тёмные полосы вносят больше азотных удобрений",
                "Тёмные полосы подстрижены короче светлых"
            ],
            "en": [
                "The mower roller bends grass blades toward or away from viewers, altering light reflection",
                "Alternating strips are sown with different grass varieties",
                "Dark bands receive higher concentrations of nitrogen fertilizer",
                "Dark stripes are shaved closer to soil roots"
            ]
        },
        "correct_index": 0,
        "correct_answer": {
            "uz": "O'roq mashinasining orqa valigi maysani tomoshabinga qarab yoki teskari tomonga yotqizishi",
            "ru": "Каток газонокосилки приминает травинку 'к зрителю' или 'от зрителя', меняя отражение света",
            "en": "The mower roller bends grass blades toward or away from viewers, altering light reflection"
        },
        "image_url": None,
        "fun_fact": {
            "uz": "Maysa navi bir xil; o'roq mashinasi orqasidagi og'ir rolik maysani o'zi bilan birga egib ketadi: maysaning yassi tomoni quyoshni ko'proq qaytarsa och, uchi ko'rinsa to'q yashil ko'rinadi.",
            "ru": "Газонокосилка с валиком сгибает траву: по ходу движения свет отражается от стеблей (светлая полоса), против хода — свет поглощается (тёмная).",
            "en": "A heavy roller behind the mower bends grass blades: blades bent away reflect light off their broad face (light), while blades bent toward absorb light (dark)."
        },
        "aliases": [
            "maysani yotqizish",
            "valik",
            "yorug'lik qaytishi",
            "katok",
            "otrajenie sveta",
            "roller",
            "grass reflection",
            "каток",
            "отражение"
        ]
    }
]
