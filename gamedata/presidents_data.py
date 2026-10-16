# -*- coding: utf-8 -*-
"""
GeoGuru Game Dataset: Presidents and World Leaders Database.
Contains 144 world-famous presidents, prime ministers, and heads of state.
Includes leaders from Uzbekistan, Central Asia, Europe, Americas, Asia, Middle East, and Africa.
"""
import random

PRESIDENTS = [
    {
        "id": "shavkat_mirziyoyev",
        "name": {
            "uz": "Shavkat Mirziyoyev",
            "ru": "Шавкат Мирзиёев",
            "en": "Shavkat Mirziyoyev"
        },
        "country": {
            "uz": "O'zbekiston",
            "ru": "Узбекистан",
            "en": "Uzbekistan"
        },
        "role": {
            "uz": "O'zbekiston Prezidenti (2016-yildan)",
            "ru": "Президент Узбекистана (с 2016)",
            "en": "President of Uzbekistan (since 2016)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Vladimir_Putin_and_Shavkat_Mirziyoyev_%282025-05-09%29_%28Shavkat_Mirziyoyev_1%29.jpg/640px-Vladimir_Putin_and_Shavkat_Mirziyoyev_%282025-05-09%29_%28Shavkat_Mirziyoyev_1%29.jpg",
        "aliases": [
            "shavkat mirziyoyev",
            "mirziyoyev",
            "shavkat miromonovich mirziyoyev",
            "шавкат мирзиёев",
            "мирзиёев",
            "shavkat mirziyoev",
            "mirziyoev"
        ],
        "fun_fact": {
            "uz": "Yangi O'zbekiston strategiyasini ilgari surib, mamlakatda keng ko'lamli iqtisodiy va ijtimoiy islohotlarni amalga oshirdi.",
            "ru": "Инициировал масштабные социально-экономические реформы и стратегию «Новый Узбекистан».",
            "en": "Launched the 'New Uzbekistan' reform strategy, opening the country's economy and liberalizing currency exchange."
        }
    },
    {
        "id": "islom_karimov",
        "name": {
            "uz": "Islom Karimov",
            "ru": "Ислам Каримов",
            "en": "Islam Karimov"
        },
        "country": {
            "uz": "O'zbekiston",
            "ru": "Узбекистан",
            "en": "Uzbekistan"
        },
        "role": {
            "uz": "O'zbekistonning Birinchi Prezidenti (1991–2016)",
            "ru": "Первый Президент Узбекистана (1991–2016)",
            "en": "First President of Uzbekistan (1991–2016)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Islam_karimov_ITN.jpg/640px-Islam_karimov_ITN.jpg",
        "aliases": [
            "islom karimov",
            "karimov",
            "islam karimov",
            "ислам каримов",
            "каримов",
            "islom abdug'aniyevich karimov"
        ],
        "fun_fact": {
            "uz": "1991-yilda O'zbekiston mustaqilligini e'lon qilgan va mamlakatni 25 yil davomida boshqargan.",
            "ru": "Объявил государственную независимость Узбекистана в 1991 году и руководил страной четверть века.",
            "en": "Declared the independence of Uzbekistan in 1991 and served as its leader for 25 years."
        }
    },
    {
        "id": "kassym_jomart_tokayev",
        "name": {
            "uz": "Qosim-Jo'mart Toqayev",
            "ru": "Касым-Жомарт Токаев",
            "en": "Kassym-Jomart Tokayev"
        },
        "country": {
            "uz": "Qozog'iston",
            "ru": "Казахстан",
            "en": "Kazakhstan"
        },
        "role": {
            "uz": "Qozog'iston Prezidenti (2019-yildan)",
            "ru": "Президент Казахстана (с 2019)",
            "en": "President of Kazakhstan (since 2019)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Kassym-Jomart_Tokayev_%282026-05-08%29_%28cropped%29.jpg",
        "aliases": [
            "qosim-jo'mart toqayev",
            "toqayev",
            "токаев",
            "касым-жомарт токаев",
            "kassym-jomart tokayev",
            "tokayev",
            "toqaev"
        ],
        "fun_fact": {
            "uz": "Professional diplomat bo'lib, BMT Bosh kotibi o'rinbosari va Jenevadagi bo'linmasi bosh direktori lavozimida ishlagan.",
            "ru": "Кадровый дипломат, занимал пост заместителя Генерального секретаря ООН в Женеве.",
            "en": "A seasoned diplomat who served as Director-General of the United Nations Office at Geneva."
        }
    },
    {
        "id": "nursultan_nazarbayev",
        "name": {
            "uz": "Nursulton Nazarboyev",
            "ru": "Нурсултан Назарбаев",
            "en": "Nursultan Nazarbayev"
        },
        "country": {
            "uz": "Qozog'iston",
            "ru": "Казахстан",
            "en": "Kazakhstan"
        },
        "role": {
            "uz": "Qozog'istonning Birinchi Prezidenti (1991–2019)",
            "ru": "Первый Президент Казахстана (1991–2019)",
            "en": "First President of Kazakhstan (1991–2019)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/%D0%92%D1%81%D1%82%D1%80%D0%B5%D1%87%D0%B0_%D1%81_%D0%9D%D1%83%D1%80%D1%81%D1%83%D0%BB%D1%82%D0%B0%D0%BD%D0%BE%D0%BC_%D0%9D%D0%B0%D0%B7%D0%B0%D1%80%D0%B1%D0%B0%D0%B5%D0%B2%D1%8B%D0%BC_%282025-05-29%29_3_%28cropped%29.jpg/640px-%D0%92%D1%81%D1%82%D1%80%D0%B5%D1%87%D0%B0_%D1%81_%D0%9D%D1%83%D1%80%D1%81%D1%83%D0%BB%D1%82%D0%B0%D0%BD%D0%BE%D0%BC_%D0%9D%D0%B0%D0%B7%D0%B0%D1%80%D0%B1%D0%B0%D0%B5%D0%B2%D1%8B%D0%BC_%282025-05-29%29_3_%28cropped%29.jpg",
        "aliases": [
            "nursulton nazarboyev",
            "nazarboyev",
            "назарбаев",
            "нурсултан назарбаев",
            "nursultan nazarbayev"
        ],
        "fun_fact": {
            "uz": "Qozog'iston poytaxtini Olmaotadan Ostonaga ko'chirgan va mamlakatni qariyb 30 yil boshqargan.",
            "ru": "Инициировал перенос столицы Казахстана из Алматы в Астану и правил страной почти 30 лет.",
            "en": "Led Kazakhstan for nearly three decades and relocated the capital to Astana in 1997."
        }
    },
    {
        "id": "sadyr_japarov",
        "name": {
            "uz": "Sadir Japarov",
            "ru": "Садыр Жапаров",
            "en": "Sadyr Japarov"
        },
        "country": {
            "uz": "Qirg'iziston",
            "ru": "Кыргызстан",
            "en": "Kyrgyzstan"
        },
        "role": {
            "uz": "Qirg'iziston Prezidenti (2021-yildan)",
            "ru": "Президент Кыргызстана (с 2021)",
            "en": "President of Kyrgyzstan (since 2021)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Sadyr_Japarov_%282024_Victory_Day%2C_cropped%29.jpg/640px-Sadyr_Japarov_%282024_Victory_Day%2C_cropped%29.jpg",
        "aliases": [
            "sadir japarov",
            "japarov",
            "жапаров",
            "садыр жапаров",
            "sadyr japarov",
            "zhaparov"
        ],
        "fun_fact": {
            "uz": "2020-yilgi siyosiy voqealardan so'ng prezidentlikka saylanib, Kumtor oltin konini davlat tasarrufiga qaytargan.",
            "ru": "Пришел к власти в 2020 году и вернул крупнейшее золоторудное месторождение «Кумтор» государству.",
            "en": "Elected president in 2021 and successfully nationalized the massive Kumtor gold mine for Kyrgyzstan."
        }
    },
    {
        "id": "roza_otunbayeva",
        "name": {
            "uz": "Roza Otunbayeva",
            "ru": "Роза Отунбаева",
            "en": "Roza Otunbayeva"
        },
        "country": {
            "uz": "Qirg'iziston",
            "ru": "Кыргызстан",
            "en": "Kyrgyzstan"
        },
        "role": {
            "uz": "Qirg'iziston Prezidenti (2010–2011)",
            "ru": "Президент Кыргызстана (2010–2011)",
            "en": "President of Kyrgyzstan (2010–2011)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Deputy_Secretary_Sherman_Meeting_with_Special_Representative_for_Afghanistan_Rosa_Otunbayeva_%2852566453759%29_%28Roza_Otunbayeva%29.jpg/640px-Deputy_Secretary_Sherman_Meeting_with_Special_Representative_for_Afghanistan_Rosa_Otunbayeva_%2852566453759%29_%28Roza_Otunbayeva%29.jpg",
        "aliases": [
            "roza otunbayeva",
            "otunbayeva",
            "отунбаева",
            "роза отунбаева",
            "roza otunbaeva"
        ],
        "fun_fact": {
            "uz": "Markaziy Osiyo tarixidagi birinchi ayol prezident bo'lib, keyinchalik BMT Bosh kotibining Afg'oniston bo'yicha maxsus vakili bo'lgan.",
            "ru": "Первая женщина-президент в истории стран Центральной Азии, спецпредставитель генсека ООН по Афганистану.",
            "en": "The first female president of any Central Asian nation, later serving as the UN Special Representative for Afghanistan."
        }
    },
    {
        "id": "almazbek_atambayev",
        "name": {
            "uz": "Almazbek Atambayev",
            "ru": "Алмазбек Атамбаев",
            "en": "Almazbek Atambayev"
        },
        "country": {
            "uz": "Qirg'iziston",
            "ru": "Кыргызстан",
            "en": "Kyrgyzstan"
        },
        "role": {
            "uz": "Qirg'iziston Prezidenti (2011–2017)",
            "ru": "Президент Кыргызстана (2011–2017)",
            "en": "President of Kyrgyzstan (2011–2017)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Almazbek_Atambayev_%2809-11-2017%29.jpg/640px-Almazbek_Atambayev_%2809-11-2017%29.jpg",
        "aliases": [
            "almazbek atambayev",
            "atambayev",
            "атамбаев",
            "алмазбек атамбаев",
            "almazbek atambaev"
        ],
        "fun_fact": {
            "uz": "Qirg'iziston tarixida hokimiyatni tinch yo'l bilan yangi saylangan prezidentga topshirgan birinchi rahbar.",
            "ru": "Первый президент Кыргызстана, мирно передавший власть избранному преемнику по завершении срока.",
            "en": "The first president in Kyrgyzstan's history to peacefully transfer power upon completing his constitutional term."
        }
    },
    {
        "id": "askar_akayev",
        "name": {
            "uz": "Asqar Akayev",
            "ru": "Аскар Акаев",
            "en": "Askar Akayev"
        },
        "country": {
            "uz": "Qirg'iziston",
            "ru": "Кыргызстан",
            "en": "Kyrgyzstan"
        },
        "role": {
            "uz": "Qirg'izistonning Birinchi Prezidenti (1990–2005)",
            "ru": "Первый Президент Кыргызстана (1990–2005)",
            "en": "First President of Kyrgyzstan (1990–2005)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Askar_Akaev_MoscowRia_08-2016_%28cropped_2%29.jpg/640px-Askar_Akaev_MoscowRia_08-2016_%28cropped_2%29.jpg",
        "aliases": [
            "asqar akayev",
            "akayev",
            "акаев",
            "аскар акаев",
            "askar akayev"
        ],
        "fun_fact": {
            "uz": "Siyosatga kirishdan oldin mashhur fizik-olim, Fanlar akademiyasi akademigi bo'lgan.",
            "ru": "До прихода в политику был выдающимся советским физиком-оптиком и президентом Академии наук Киргизской ССР.",
            "en": "A distinguished laser physicist and academy president who became Kyrgyzstan's founding president."
        }
    },
    {
        "id": "emomali_rahmon",
        "name": {
            "uz": "Emomali Rahmon",
            "ru": "Эмомали Рахмон",
            "en": "Emomali Rahmon"
        },
        "country": {
            "uz": "Tojikiston",
            "ru": "Таджикистан",
            "en": "Tajikistan"
        },
        "role": {
            "uz": "Tojikiston Prezidenti (1994-yildan)",
            "ru": "Президент Таджикистана (с 1994)",
            "en": "President of Tajikistan (since 1994)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Emomali_Rahmon_in_2026.jpg/640px-Emomali_Rahmon_in_2026.jpg",
        "aliases": [
            "emomali rahmon",
            "rahmon",
            "рахмон",
            "эмомали рахмон",
            "emomali rakhmon",
            "rakhmon"
        ],
        "fun_fact": {
            "uz": "Tojikistondagi fuqarolar urushini 1997-yilgi bitim bilan yakunlashga erishgan va 'Millat peshvosi' unvoniga ega.",
            "ru": "Носит официальный статус «Лидер нации», остановил разрушительную гражданскую войну в Таджикистане.",
            "en": "Brokered the end of the Tajik Civil War in 1997 and holds the title 'Leader of the Nation'."
        }
    },
    {
        "id": "serdar_berdimuhamedov",
        "name": {
            "uz": "Serdar Berdimuhamedov",
            "ru": "Сердар Бердымухамедов",
            "en": "Serdar Berdimuhamedov"
        },
        "country": {
            "uz": "Turkmaniston",
            "ru": "Туркменистан",
            "en": "Turkmenistan"
        },
        "role": {
            "uz": "Turkmaniston Prezidenti (2022-yildan)",
            "ru": "Президент Туркменистана (с 2022)",
            "en": "President of Turkmenistan (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Serdar_Berdimuhamedov_on_December_20%2C_2025_%28cropped%29.jpg/640px-Serdar_Berdimuhamedov_on_December_20%2C_2025_%28cropped%29.jpg",
        "aliases": [
            "serdar berdimuhamedov",
            "berdimuhamedov",
            "бердымухамедов",
            "сердар бердымухамедов"
        ],
        "fun_fact": {
            "uz": "Otasi Gurbanguly Berdimuhamedovdan so'ng 2022-yilda davlat rahbari etib saylangan.",
            "ru": "Был избран президентом Туркменистана в марте 2022 года, сменив своего отца.",
            "en": "Elected president of Turkmenistan in 2022, succeeding his father Gurbanguly Berdimuhamedov."
        }
    },
    {
        "id": "gurbanguly_berdimuhamedov",
        "name": {
            "uz": "Gurbanguly Berdimuhamedov",
            "ru": "Гурбангулы Бердымухамедов",
            "en": "Gurbanguly Berdimuhamedov"
        },
        "country": {
            "uz": "Turkmaniston",
            "ru": "Туркменистан",
            "en": "Turkmenistan"
        },
        "role": {
            "uz": "Turkmaniston Prezidenti (2006–2022)",
            "ru": "Президент Туркменистана (2006–2022)",
            "en": "President of Turkmenistan (2006–2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/%D0%93%D1%83%D1%80%D0%B1%D0%B0%D0%BD%D0%B3%D1%83%D0%BB%D1%8B_%D0%91%D0%B5%D1%80%D0%B4%D1%8B%D0%BC%D1%83%D1%85%D0%B0%D0%BC%D0%BC%D0%B5%D0%B4%D0%BE%D0%B2_-_02_%2827-09-2025%29_%28cropped%29.jpg/640px-%D0%93%D1%83%D1%80%D0%B1%D0%B0%D0%BD%D0%B3%D1%83%D0%BB%D1%8B_%D0%91%D0%B5%D1%80%D0%B4%D1%8B%D0%BC%D1%83%D1%85%D0%B0%D0%BC%D0%BC%D0%B5%D0%B4%D0%BE%D0%B2_-_02_%2827-09-2025%29_%28cropped%29.jpg",
        "aliases": [
            "gurbanguly berdimuhamedov",
            "berdimuhamedov",
            "бердымухамедов",
            "гурбангулы бердымухамедов",
            "arkadag"
        ],
        "fun_fact": {
            "uz": "'Arkadag' (Homiy) unvoni bilan mashhur bo'lib, oq marmarli Ashxobodni keng qamrovli qurdirgan.",
            "ru": "Носит официальный титул «Аркадаг» (Покровитель) и увлекается конным спортом на ахалтекинцах.",
            "en": "Known by the honorific 'Arkadag' (Protector) and celebrated for white-marble architecture in Ashgabat."
        }
    },
    {
        "id": "saparmurat_niyazov",
        "name": {
            "uz": "Saparmurod Niyozov",
            "ru": "Сапармурат Ниязов",
            "en": "Saparmurat Niyazov"
        },
        "country": {
            "uz": "Turkmaniston",
            "ru": "Туркменистан",
            "en": "Turkmenistan"
        },
        "role": {
            "uz": "Turkmanistonning Birinchi Prezidenti (1991–2006)",
            "ru": "Первый Президент Туркменистана (1991–2006)",
            "en": "First President of Turkmenistan (1991–2006)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Nyyazov_in_February_1998.jpg/640px-Nyyazov_in_February_1998.jpg",
        "aliases": [
            "saparmurod niyozov",
            "niyozov",
            "ниязов",
            "сапармурат ниязов",
            "turkmanboshi",
            "saparmurat niyazov"
        ],
        "fun_fact": {
            "uz": "'Turkmanboshi' nomi bilan mashhur bo'lgan va 'Ruhnoma' falsafiy kitobini yozgan.",
            "ru": "Имел официальный титул «Туркменбаши» (Глава туркмен) и написал философский трактат «Рухнама».",
            "en": "Adopted the title 'Turkmenbashi' (Leader of Turkmens) and authored the spiritual treatise Ruhnama."
        }
    },
    {
        "id": "ilham_aliyev",
        "name": {
            "uz": "Ilhom Aliyev",
            "ru": "Ильхам Алиев",
            "en": "Ilham Aliyev"
        },
        "country": {
            "uz": "Ozarbayjon",
            "ru": "Азербайджан",
            "en": "Azerbaijan"
        },
        "role": {
            "uz": "Ozarbayjon Prezidenti (2003-yildan)",
            "ru": "Президент Азербайджана (с 2003)",
            "en": "President of Azerbaijan (since 2003)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Ilham_Aliyev%2C_December_2025_%28cropped%29.jpg/640px-Ilham_Aliyev%2C_December_2025_%28cropped%29.jpg",
        "aliases": [
            "ilhom aliyev",
            "aliyev",
            "алиев",
            "ильхам алиев",
            "ilham aliyev"
        ],
        "fun_fact": {
            "uz": "2020 va 2023-yillarda Qorabog' ustidan Ozarbayjonning to'liq suverenitetini tiklagan.",
            "ru": "Восстановил полный суверенитет Азербайджана над Карабахом в ходе событий 2020 и 2023 годов.",
            "en": "Restored full Azerbaijani territorial sovereignty over Karabakh following the conflicts of 2020 and 2023."
        }
    },
    {
        "id": "heydar_aliyev",
        "name": {
            "uz": "Haydar Aliyev",
            "ru": "Гейдар Алиев",
            "en": "Heydar Aliyev"
        },
        "country": {
            "uz": "Ozarbayjon",
            "ru": "Азербайджан",
            "en": "Azerbaijan"
        },
        "role": {
            "uz": "Ozarbayjon Prezidenti (1993–2003)",
            "ru": "Президент Азербайджана (1993–2003)",
            "en": "President of Azerbaijan (1993–2003)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Heydar_Aliyev_%28crop%29.jpg/640px-Heydar_Aliyev_%28crop%29.jpg",
        "aliases": [
            "haydar aliyev",
            "aliyev",
            "алиев",
            "гейдар алиев",
            "heydar aliyev"
        ],
        "fun_fact": {
            "uz": "Ozarbayjonning zamonaviy neft strategiyasi va 'Asr shartnomasi'ga asos solgan umummilliy yetakchi.",
            "ru": "Считается общенациональным лидером современного Азербайджана, подписал исторический «Контракт века».",
            "en": "Regarded as the national leader of modern Azerbaijan, negotiating the landmark 'Contract of the Century'."
        }
    },
    {
        "id": "nikol_pashinyan",
        "name": {
            "uz": "Nikol Pashinyan",
            "ru": "Никол Пашинян",
            "en": "Nikol Pashinyan"
        },
        "country": {
            "uz": "Armaniston",
            "ru": "Армения",
            "en": "Armenia"
        },
        "role": {
            "uz": "Armaniston Bosh vaziri (2018-yildan)",
            "ru": "Премьер-министр Армении (с 2018)",
            "en": "Prime Minister of Armenia (since 2018)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/K%C3%A4tlemine_Armeenia_peaminister_Pashinyan%27iga_%28552477480461%29.jpg/640px-K%C3%A4tlemine_Armeenia_peaminister_Pashinyan%27iga_%28552477480461%29.jpg",
        "aliases": [
            "nikol pashinyan",
            "pashinyan",
            "пашинян",
            "никол пашинян"
        ],
        "fun_fact": {
            "uz": "2018-yilgi tinch 'Baxmal inqilobi' orqali bosh vazir lavozimiga kelgan sobiq muxolifatchi jurnalist.",
            "ru": "Пришел к власти в результате мирной «Бархатной революции» в мае 2018 года, бывший журналист.",
            "en": "Came to power following the peaceful 2018 Velvet Revolution in Armenia, originally an opposition journalist."
        }
    },
    {
        "id": "salome_zourabichvili",
        "name": {
            "uz": "Salome Zurabishvili",
            "ru": "Саломе Зурабишвили",
            "en": "Salome Zourabichvili"
        },
        "country": {
            "uz": "Gruziya",
            "ru": "Грузия",
            "en": "Georgia"
        },
        "role": {
            "uz": "Gruziya Prezidenti (2018-yildan)",
            "ru": "Президент Грузии (с 2018)",
            "en": "President of Georgia (since 2018)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Salome_Zourabichvili_in_2024_%28cropped%29.jpg/640px-Salome_Zourabichvili_in_2024_%28cropped%29.jpg",
        "aliases": [
            "salome zurabishvili",
            "zurabishvili",
            "зурабишвили",
            "саломе зурабишвили",
            "salome zourabichvili"
        ],
        "fun_fact": {
            "uz": "Fransiyada gruzin muhojirlari oilasida tug'ilgan va Gruziyaning birinchi ayol prezidenti bo'lgan.",
            "ru": "Родилась в Париже в семье грузинских эмигрантов, стала первой женщиной-президентом Грузии.",
            "en": "Born in Paris to Georgian emigrants, she served as a French diplomat before becoming Georgia's first female president."
        }
    },
    {
        "id": "mikhail_saakashvili",
        "name": {
            "uz": "Mixail Saakashvili",
            "ru": "Михаил Саакашвили",
            "en": "Mikheil Saakashvili"
        },
        "country": {
            "uz": "Gruziya",
            "ru": "Грузия",
            "en": "Georgia"
        },
        "role": {
            "uz": "Gruziya Prezidenti (2004–2013)",
            "ru": "Президент Грузии (2004–2013)",
            "en": "President of Georgia (2004–2013)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/06/%D0%9C%D0%B8%D1%85%D0%B0%D0%B8%D0%BB_%D0%A1%D0%B0%D0%B0%D0%BA%D0%B0%D1%88%D0%B2%D0%B8%D0%BB%D0%B8_%2804-10-2021%29_%28cropped%29.jpg",
        "aliases": [
            "mixail saakashvili",
            "saakashvili",
            "саакашвили",
            "михаил саакашвили",
            "mikheil saakashvili"
        ],
        "fun_fact": {
            "uz": "2003-yilgi 'Atirgullar inqilobi' orqali hokimiyatga kelib, politsiya va davlat xizmatlarida radikal islohotlar o'tkazgan.",
            "ru": "Возглавил «Революцию роз» 2003 года и провел радикальные антикоррупционные реформы в Грузии.",
            "en": "Led the 2003 Rose Revolution and enacted sweepingly successful anti-corruption reforms in Georgia."
        }
    },
    {
        "id": "donald_trump",
        "name": {
            "uz": "Donald Tramp",
            "ru": "Дональд Трамп",
            "en": "Donald Trump"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 45 va 47-Prezidenti",
            "ru": "45-й и 47-й Президент США",
            "en": "45th and 47th President of the United States"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Official_Presidential_Portrait_of_President_Donald_J._Trump_%282025%29.jpg/640px-Official_Presidential_Portrait_of_President_Donald_J._Trump_%282025%29.jpg",
        "aliases": [
            "donald trump",
            "trump",
            "tramp",
            "donald tramp",
            "трамп",
            "дональд трамп"
        ],
        "fun_fact": {
            "uz": "Grover Klivlenddan so'ng Amerika tarixida oraliq tanaffus bilan ikki marta saylangan ikkinchi prezident.",
            "ru": "Стал вторым президентом в истории США после Гровера Кливленда, избранным на два непоследовательных срока.",
            "en": "Became only the second US president in history to be elected to two non-consecutive terms."
        }
    },
    {
        "id": "joe_biden",
        "name": {
            "uz": "Jo Bayden",
            "ru": "Джо Байден",
            "en": "Joe Biden"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 46-Prezidenti (2021–2025)",
            "ru": "46-й Президент США (2021–2025)",
            "en": "46th President of the United States (2021–2025)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Joe_Biden_presidential_portrait.jpg/640px-Joe_Biden_presidential_portrait.jpg",
        "aliases": [
            "joe biden",
            "biden",
            "bayden",
            "jo bayden",
            "байден",
            "джо байден"
        ],
        "fun_fact": {
            "uz": "AQSH tarixida lavozimga kirishgan paytda eng yoshi katta (78 yosh) prezident bo'lgan.",
            "ru": "Стал самым пожилым человеком, когда-либо вступавшим в должность президента США (в 78 лет).",
            "en": "Was the oldest person to assume the US presidency, taking office at age 78."
        }
    },
    {
        "id": "barack_obama",
        "name": {
            "uz": "Barak Obama",
            "ru": "Барак Обама",
            "en": "Barack Obama"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 44-Prezidenti (2009–2017)",
            "ru": "44-й Президент США (2009–2017)",
            "en": "44th President of the United States (2009–2017)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/640px-President_Barack_Obama.jpg",
        "aliases": [
            "barack obama",
            "obama",
            "barak obama",
            "обама",
            "барак обама"
        ],
        "fun_fact": {
            "uz": "AQSH tarixidagi birinchi afroamerikalik prezident bo'lib, 2009-yilda Nobel Tinchlik mukofotini olgan.",
            "ru": "Первый афроамериканец на посту президента США, лауреат Нобелевской премии мира 2009 года.",
            "en": "The first African American US president and the recipient of the 2009 Nobel Peace Prize."
        }
    },
    {
        "id": "george_w_bush",
        "name": {
            "uz": "Jorj Bush (kichik)",
            "ru": "Джордж Буш-младший",
            "en": "George W. Bush"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 43-Prezidenti (2001–2009)",
            "ru": "43-й Президент США (2001–2009)",
            "en": "43rd President of the United States (2001–2009)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/George-W-Bush.jpeg/640px-George-W-Bush.jpeg",
        "aliases": [
            "george w bush",
            "george bush",
            "bush",
            "буш",
            "джордж буш",
            "jorj bush"
        ],
        "fun_fact": {
            "uz": "Uning prezidentlik davrida 2001-yil 11-sentabr teraktlari sodir bo'lgan va 'terrorizmga qarshi urush' e'lon qilingan.",
            "ru": "Возглавлял США во время терактов 11 сентября 2001 года и начал «Войну против терроризма».",
            "en": "Led the United States during the September 11 terrorist attacks and launched the global War on Terror."
        }
    },
    {
        "id": "bill_clinton",
        "name": {
            "uz": "Bill Klinton",
            "ru": "Билл Клинтон",
            "en": "Bill Clinton"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 42-Prezidenti (1993–2001)",
            "ru": "42-й Президент США (1993–2001)",
            "en": "42nd President of the United States (1993–2001)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Bill_Clinton.jpg/640px-Bill_Clinton.jpg",
        "aliases": [
            "bill clinton",
            "clinton",
            "klinton",
            "билл клинтон",
            "клинтон"
        ],
        "fun_fact": {
            "uz": "Uning davrida AQSH iqtisodiyoti eng uzoq muddatli o'sish davrini boshdan kechirgan va byudjet profisiti kuzatilgan.",
            "ru": "Его президентство совпало с самым продолжительным периодом мирного экономического подъема в истории США.",
            "en": "Presided over the longest economic expansion in peacetime American history, leaving a budget surplus."
        }
    },
    {
        "id": "george_h_w_bush",
        "name": {
            "uz": "Jorj Bush (katta)",
            "ru": "Джордж Буш-старший",
            "en": "George H. W. Bush"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 41-Prezidenti (1989–1993)",
            "ru": "41-й Президент США (1989–1993)",
            "en": "41st President of the United States (1989–1993)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/George_H._W._Bush_presidential_portrait_%28cropped%29_%282%29.jpg/640px-George_H._W._Bush_presidential_portrait_%28cropped%29_%282%29.jpg",
        "aliases": [
            "george h w bush",
            "george bush senior",
            "katta jorj bush",
            "буш старший"
        ],
        "fun_fact": {
            "uz": "Sovuq urush tugashi va SSSR parchalanishi davrida AQSHni boshqargan hamda Fors ko'rfazi urushini olib borgan.",
            "ru": "Руководил США в период окончания Холодной войны, распада СССР и войны в Персидском заливе.",
            "en": "Presided over the end of the Cold War, the dissolution of the USSR, and Operation Desert Storm."
        }
    },
    {
        "id": "ronald_reagan",
        "name": {
            "uz": "Ronald Reygan",
            "ru": "Рональд Рейган",
            "en": "Ronald Reagan"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 40-Prezidenti (1981–1989)",
            "ru": "40-й Президент США (1981–1989)",
            "en": "40th President of the United States (1981–1989)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Official_Portrait_of_President_Reagan_1981.jpg/640px-Official_Portrait_of_President_Reagan_1981.jpg",
        "aliases": [
            "ronald reagan",
            "reagan",
            "reygan",
            "рейган",
            "рональд рейган"
        ],
        "fun_fact": {
            "uz": "Siyosatga kirishdan oldin mashhur Gollivud aktyori bo'lgan va 'Reyganomika' iqtisodiy siyosatini olib borgan.",
            "ru": "До политической карьеры был популярным голливудским актером, известен политикой «рейганомики».",
            "en": "A former Hollywood actor whose supply-side economic policies became known worldwide as 'Reaganomics'."
        }
    },
    {
        "id": "jimmy_carter",
        "name": {
            "uz": "Jimmi Karter",
            "ru": "Джимми Картер",
            "en": "Jimmy Carter"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 39-Prezidenti (1977–1981)",
            "ru": "39-й Президент США (1977–1981)",
            "en": "39th President of the United States (1977–1981)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Jimmy_Carter_Official_Portrait2_%283x4_cropped%29.jpg/640px-Jimmy_Carter_Official_Portrait2_%283x4_cropped%29.jpg",
        "aliases": [
            "jimmy carter",
            "carter",
            "karter",
            "картер",
            "джимми картер"
        ],
        "fun_fact": {
            "uz": "AQSH tarixida 100 yoshga to'lgan birinchi prezident bo'lib, Kemp-Devid tinchlik bitimlariga vositachilik qilgan.",
            "ru": "Стал первым президентом США, дожившим до 100 лет, автор Кэмп-Дэвидских мирных соглашений.",
            "en": "Brokered the historic Camp David Accords and became the first US president to reach the age of 100."
        }
    },
    {
        "id": "richard_nixon",
        "name": {
            "uz": "Richard Nikson",
            "ru": "Ричард Никсон",
            "en": "Richard Nixon"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 37-Prezidenti (1969–1974)",
            "ru": "37-й Президент США (1969–1974)",
            "en": "37th President of the United States (1969–1974)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Richard_Nixon_presidential_portrait_%281%29.jpg/640px-Richard_Nixon_presidential_portrait_%281%29.jpg",
        "aliases": [
            "richard nixon",
            "nixon",
            "nikson",
            "никсон",
            "ричард никсон"
        ],
        "fun_fact": {
            "uz": "Xitoy bilan diplomatik munosabatlarni ochgan, Uotergeyt mojarosi tufayli iste'foga chiqqan yagona AQSH prezidenti.",
            "ru": "Открыл дипотношения с КНР и стал единственным президентом США, ушедшим в отставку из-за Уотергейта.",
            "en": "Opened diplomatic relations with China and became the only US president to resign from office (Watergate)."
        }
    },
    {
        "id": "john_f_kennedy",
        "name": {
            "uz": "Jon F. Kennedi",
            "ru": "Джон Кеннеди",
            "en": "John F. Kennedy"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 35-Prezidenti (1961–1963)",
            "ru": "35-й Президент США (1961–1963)",
            "en": "35th President of the United States (1961–1963)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/John_F._Kennedy%2C_White_House_color_photo_portrait.jpg/640px-John_F._Kennedy%2C_White_House_color_photo_portrait.jpg",
        "aliases": [
            "john f kennedy",
            "kennedy",
            "jfk",
            "kennedi",
            "кеннеди",
            "джон кеннеди"
        ],
        "fun_fact": {
            "uz": "Oyga insonni qo'ndirish bo'yicha 'Apollon' kosmik dasturini e'lon qilgan va 1963-yilda Dallasda o'ldirilgan.",
            "ru": "Инициировал лунную программу «Аполлон», был трагически убит в Далласе в ноябре 1963 года.",
            "en": "Initiated the Apollo Moon mission and established the Peace Corps before his assassination in 1963."
        }
    },
    {
        "id": "dwight_d_eisenhower",
        "name": {
            "uz": "Duayt Eyzenxauer",
            "ru": "Дуайт Эйзенхауэр",
            "en": "Dwight D. Eisenhower"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 34-Prezidenti (1953–1961)",
            "ru": "34-й Президент США (1953–1961)",
            "en": "34th President of the United States (1953–1961)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Dwight_D._Eisenhower%2C_official_photo_portrait%2C_May_29%2C_1959_%28cropped%29%283%29.jpg/640px-Dwight_D._Eisenhower%2C_official_photo_portrait%2C_May_29%2C_1959_%28cropped%29%283%29.jpg",
        "aliases": [
            "dwight eisenhower",
            "eisenhower",
            "eyzenxauer",
            "эйзенхауэр",
            "дуайт эйзенхауэр",
            "ike"
        ],
        "fun_fact": {
            "uz": "Ikkinchi jahon urushida Ittifoqchilar kuchlarining Oliy qo'mondoni bo'lgan va NASA agentligini tashkil etgan.",
            "ru": "Был верховным главнокомандующим союзных войск во Второй мировой войне, создал агентство NASA.",
            "en": "Supreme Allied Commander in Europe during WWII who later signed the Interstate Highway Act and created NASA."
        }
    },
    {
        "id": "harry_s_truman",
        "name": {
            "uz": "Garri Trumen",
            "ru": "Гарри Трумэн",
            "en": "Harry S. Truman"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 33-Prezidenti (1945–1953)",
            "ru": "33-й Президент США (1945–1953)",
            "en": "33rd President of the United States (1945–1953)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/TRUMAN_58-766-06_%28cropped%29.jpg/640px-TRUMAN_58-766-06_%28cropped%29.jpg",
        "aliases": [
            "harry truman",
            "truman",
            "трумэн",
            "гарри трумэн",
            "garri trumen"
        ],
        "fun_fact": {
            "uz": "Ikkinchi jahon urushini yakunlagan, Marshall rejasi orqali Yevropani qayta tiklagan va NATOga asos solgan.",
            "ru": "Утвердил «План Маршалла» по восстановлению Европы и стоял у истоков создания блока НАТО.",
            "en": "Authorized the Marshall Plan to rebuild post-war Europe and oversaw the founding of NATO."
        }
    },
    {
        "id": "franklin_d_roosevelt",
        "name": {
            "uz": "Franklin D. Ruzvelt",
            "ru": "Франклин Рузвельт",
            "en": "Franklin D. Roosevelt"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 32-Prezidenti (1933–1945)",
            "ru": "32-й Президент США (1933–1945)",
            "en": "32nd President of the United States (1933–1945)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/FDR-1944-Campaign-Portrait_%283x4_retouched%2C_cropped%29.jpg/640px-FDR-1944-Campaign-Portrait_%283x4_retouched%2C_cropped%29.jpg",
        "aliases": [
            "franklin d roosevelt",
            "roosevelt",
            "fdr",
            "ruzvelt",
            "рузвельт",
            "франклин рузвельт"
        ],
        "fun_fact": {
            "uz": "AQSH tarixida to'rt marta prezidentlikka saylangan yagona rahbar bo'lib, 'Yangi kelishuv' (New Deal) islohotlarini o'tkazgan.",
            "ru": "Единственный президент США, избиравшийся более двух раз (четыре срока), создал «Новый курс».",
            "en": "The only US president elected to four terms, leading the nation through the Great Depression and World War II."
        }
    },
    {
        "id": "theodore_roosevelt",
        "name": {
            "uz": "Teodor Ruzvelt",
            "ru": "Теодор Рузвельт",
            "en": "Theodore Roosevelt"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 26-Prezidenti (1901–1909)",
            "ru": "26-й Президент США (1901–1909)",
            "en": "26th President of the United States (1901–1909)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Theodore_Roosevelt_by_the_Pach_Bros_%284x5_cropped%29_%282%29.jpg/640px-Theodore_Roosevelt_by_the_Pach_Bros_%284x5_cropped%29_%282%29.jpg",
        "aliases": [
            "theodore roosevelt",
            "teddy roosevelt",
            "ruzvelt",
            "рузвельт",
            "теодор рузвельт"
        ],
        "fun_fact": {
            "uz": "AQSH tarixidagi eng yosh prezident (42 yoshda kirishgan) va Panama kanalining qurilishini boshlab bergan.",
            "ru": "Самый молодой президент в истории США (вступил в должность в 42 года), инициировал строительство Панамского канала.",
            "en": "The youngest person to become US president (at 42), champion of national parks and builder of the Panama Canal."
        }
    },
    {
        "id": "woodrow_wilson",
        "name": {
            "uz": "Vudro Vilson",
            "ru": "Вудро Вильсон",
            "en": "Woodrow Wilson"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 28-Prezidenti (1913–1921)",
            "ru": "28-й Президент США (1913–1921)",
            "en": "28th President of the United States (1913–1921)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/President_Woodrow_Wilson_Harris_%26_Ewing_%283x4_cropped_b%29.jpg/640px-President_Woodrow_Wilson_Harris_%26_Ewing_%283x4_cropped_b%29.jpg",
        "aliases": [
            "woodrow wilson",
            "wilson",
            "vilson",
            "вильсон",
            "вудро вильсон"
        ],
        "fun_fact": {
            "uz": "Millatlar Ligasini tashkil etish g'oyasini ilgari surgan va 1919-yilda Nobel Tinchlik mukofotiga sazovor bo'lgan.",
            "ru": "Создатель Лиги Наций и концепции «Четырнадцати пунктов», лауреат Нобелевской премии мира 1919 года.",
            "en": "Architect of the League of Nations and the Fourteen Points, awarded the 1919 Nobel Peace Prize."
        }
    },
    {
        "id": "abraham_lincoln",
        "name": {
            "uz": "Avraam Linkoln",
            "ru": "Авраам Линкольн",
            "en": "Abraham Lincoln"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 16-Prezidenti (1861–1865)",
            "ru": "16-й Президент США (1861–1865)",
            "en": "16th President of the United States (1861–1865)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg/640px-Abraham_Lincoln_O-77_matte_collodion_print.jpg",
        "aliases": [
            "abraham lincoln",
            "lincoln",
            "linkoln",
            "линкольн",
            "авраам линкольн"
        ],
        "fun_fact": {
            "uz": "AQSH Fuqarolar urushida mamlakat birligini saqlab qolgan va 1863-yilda quldorlikni bekor qilgan.",
            "ru": "Сохранил единство США в Гражданской войне и отменил рабство Декларацией об освобождении.",
            "en": "Preserved the Union through the Civil War and abolished slavery with the Emancipation Proclamation."
        }
    },
    {
        "id": "george_washington",
        "name": {
            "uz": "Jorj Vashington",
            "ru": "Джордж Вашингтон",
            "en": "George Washington"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning Birinchi Prezidenti (1789–1797)",
            "ru": "Первый Президент США (1789–1797)",
            "en": "First President of the United States (1789–1797)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg/640px-Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg",
        "aliases": [
            "george washington",
            "washington",
            "vashington",
            "вашингтон",
            "джордж вашингтон"
        ],
        "fun_fact": {
            "uz": "Amerika Qo'shma Shtatlarining 'Ota-asoschisi' bo'lib, AQSH Konstitutsiyaviy konventiga raislik qilgan.",
            "ru": "Один из отцов-основателей США, командующий Континентальной армией в Войне за независимость.",
            "en": "Commander-in-Chief of the Continental Army and the universally revered first President of the United States."
        }
    },
    {
        "id": "thomas_jefferson",
        "name": {
            "uz": "Tomas Jefferson",
            "ru": "Томас Джефферсон",
            "en": "Thomas Jefferson"
        },
        "country": {
            "uz": "AQSH",
            "ru": "США",
            "en": "United States"
        },
        "role": {
            "uz": "AQSHning 3-Prezidenti (1801–1809)",
            "ru": "3-й Президент США (1801–1809)",
            "en": "3rd President of the United States (1801–1809)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Official_Presidential_portrait_of_Thomas_Jefferson_%28by_Rembrandt_Peale%2C_1800%29.jpg/640px-Official_Presidential_portrait_of_Thomas_Jefferson_%28by_Rembrandt_Peale%2C_1800%29.jpg",
        "aliases": [
            "thomas jefferson",
            "jefferson",
            "джефферсон",
            "томас джефферсон",
            "tomas jefferson"
        ],
        "fun_fact": {
            "uz": "AQSH Mustaqillik Deklaratsiyasining bosh muallifi va Luiziana sotib olinishini amalga oshirgan rahbar.",
            "ru": "Основной автор Декларации независимости США, приобрел Луизиану у Франции в 1803 году.",
            "en": "Principal author of the Declaration of Independence who doubled the nation's size via the Louisiana Purchase."
        }
    },
    {
        "id": "justin_trudeau",
        "name": {
            "uz": "Jastin Tryudo",
            "ru": "Джастин Трюдо",
            "en": "Justin Trudeau"
        },
        "country": {
            "uz": "Kanada",
            "ru": "Канада",
            "en": "Canada"
        },
        "role": {
            "uz": "Kanada Bosh vaziri (2015-yildan)",
            "ru": "Премьер-министр Канады (с 2015)",
            "en": "Prime Minister of Canada (since 2015)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Prime_Minister_Trudeau%27s_message_on_Christmas_2023_%280m29s%29_%28cropped%29.jpg/640px-Prime_Minister_Trudeau%27s_message_on_Christmas_2023_%280m29s%29_%28cropped%29.jpg",
        "aliases": [
            "justin trudeau",
            "trudeau",
            "tryudo",
            "трюдо",
            "джастин трюдо"
        ],
        "fun_fact": {
            "uz": "Kanada sobiq bosh vaziri Pyer Tryudoning o'g'li bo'lib, Kanada tarixidagi eng yosh ikkinchi bosh vazir bo'lgan.",
            "ru": "Сын знаменитого премьера Пьера Трюдо, второй самый молодой премьер-министр в истории Канады.",
            "en": "Second youngest prime minister in Canadian history and son of former Prime Minister Pierre Trudeau."
        }
    },
    {
        "id": "pierre_trudeau",
        "name": {
            "uz": "Pyer Tryudo",
            "ru": "Пьер Трюдо",
            "en": "Pierre Trudeau"
        },
        "country": {
            "uz": "Kanada",
            "ru": "Канада",
            "en": "Canada"
        },
        "role": {
            "uz": "Kanada Bosh vaziri (1968–1979, 1980–1984)",
            "ru": "Премьер-министр Канады",
            "en": "Prime Minister of Canada"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Prime_Minister_Pierre_Trudeau_1975_%28UPI_press_photo%29_%28cropped%29.jpg/640px-Prime_Minister_Pierre_Trudeau_1975_%28UPI_press_photo%29_%28cropped%29.jpg",
        "aliases": [
            "pierre trudeau",
            "trudeau",
            "пьер трюдо",
            "pyer tryudo"
        ],
        "fun_fact": {
            "uz": "Zamonaviy Kanada Konstitutsiyasini qabul qildirgan va ingliz hamda fransuz tillarini teng rasmiy tilga aylantirgan.",
            "ru": "Добился конституционной независимости Канады от Великобритании (Патриация) в 1982 году.",
            "en": "Patriated the Constitution of Canada and established official bilingualism nationwide."
        }
    },
    {
        "id": "claudia_sheinbaum",
        "name": {
            "uz": "Klaudiya Sheynbaum",
            "ru": "Клаудия Шейнбаум",
            "en": "Claudia Sheinbaum"
        },
        "country": {
            "uz": "Meksika",
            "ru": "Мексика",
            "en": "Mexico"
        },
        "role": {
            "uz": "Meksika Prezidenti (2024-yildan)",
            "ru": "Президент Мексики (с 2024)",
            "en": "President of Mexico (since 2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Claudia_Sheinbaum_in_2025_%283x4_cropped%29.jpg/640px-Claudia_Sheinbaum_in_2025_%283x4_cropped%29.jpg",
        "aliases": [
            "claudia sheinbaum",
            "sheinbaum",
            "шейнбаум",
            "клаудия шейнбаум"
        ],
        "fun_fact": {
            "uz": "Meksika tarixidagi birinchi ayol prezident bo'lib, kasbi bo'yicha energetik olim va fan doktori.",
            "ru": "Первая женщина-президент в истории Мексики, ученый-физик и лауреат Нобелевской премии мира в составе МГЭИК.",
            "en": "The first female president in Mexican history, holding a doctorate in energy engineering."
        }
    },
    {
        "id": "andres_manuel_lopez_obrador",
        "name": {
            "uz": "Andres Manuel Lopes Obrador",
            "ru": "Андрес Мануэль Лопес Обрадор",
            "en": "Andrés Manuel López Obrador"
        },
        "country": {
            "uz": "Meksika",
            "ru": "Мексика",
            "en": "Mexico"
        },
        "role": {
            "uz": "Meksika Prezidenti (2018–2024)",
            "ru": "Президент Мексики (2018–2024)",
            "en": "President of Mexico (2018–2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Andr%C3%A9s_Manuel_L%C3%B3pez_Obrador_junio_2024.jpg/640px-Andr%C3%A9s_Manuel_L%C3%B3pez_Obrador_junio_2024.jpg",
        "aliases": [
            "andres manuel lopez obrador",
            "amlo",
            "лопес обрадор",
            "lopes obrador"
        ],
        "fun_fact": {
            "uz": "Ko'pincha AMLO qisqartmasi bilan tanilgan va Meksikada 'To'rtinchi o'zgarish' siyosatini yurgizgan.",
            "ru": "Широко известен как AMLO, проводил масштабную программу «Четвертая трансформация».",
            "en": "Widely known as AMLO, he led Mexico through the ambitious 'Fourth Transformation' populist platform."
        }
    },
    {
        "id": "luiz_inacio_lula_da_silva",
        "name": {
            "uz": "Luis Inasiu Lula da Silva",
            "ru": "Луис Инасиу Лула да Силва",
            "en": "Luiz Inácio Lula da Silva"
        },
        "country": {
            "uz": "Braziliya",
            "ru": "Бразилия",
            "en": "Brazil"
        },
        "role": {
            "uz": "Braziliya Prezidenti (2003–2010, 2023-yildan)",
            "ru": "Президент Бразилии (2003–2010, с 2023)",
            "en": "President of Brazil (2003–2010, since 2023)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Foto_oficial_de_Luiz_In%C3%A1cio_Lula_da_Silva_%28ombros%29_denoise_%28cropped%29.jpg/640px-Foto_oficial_de_Luiz_In%C3%A1cio_Lula_da_Silva_%28ombros%29_denoise_%28cropped%29.jpg",
        "aliases": [
            "lula da silva",
            "lula",
            "luiz inacio lula da silva",
            "лула",
            "лула да силва"
        ],
        "fun_fact": {
            "uz": "Metallurgiya ishchisidan prezidentlikka ko'tarilib, Braziliya tarixida 3 marta saylangan birinchi prezident bo'ldi.",
            "ru": "Бывший профсоюзный лидер и рабочий металлург, трижды избранный на пост президента Бразилии.",
            "en": "Rose from metalworker and union leader to serve three terms as President of Brazil."
        }
    },
    {
        "id": "jair_bolsonaro",
        "name": {
            "uz": "Jair Bolsonaru",
            "ru": "Жаир Болсонару",
            "en": "Jair Bolsonaro"
        },
        "country": {
            "uz": "Braziliya",
            "ru": "Бразилия",
            "en": "Brazil"
        },
        "role": {
            "uz": "Braziliya Prezidenti (2019–2022)",
            "ru": "Президент Бразилии (2019–2022)",
            "en": "President of Brazil (2019–2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Jair_Bolsonaro_em_24_de_abril_de_2019_%281%29_%283x4%29.jpg/640px-Jair_Bolsonaro_em_24_de_abril_de_2019_%281%29_%283x4%29.jpg",
        "aliases": [
            "jair bolsonaro",
            "bolsonaro",
            "bolsonaru",
            "болсонару",
            "жаир болсонару"
        ],
        "fun_fact": {
            "uz": "Sobiq harbiy kapitan bo'lib, o'zining o'ta o'ng konservativ qarashlari bilan mashhur bo'lgan.",
            "ru": "Бывший офицер-десантник, придерживавшийся правой консервативной идеологии.",
            "en": "A former army captain and conservative nationalist who presided over Brazil from 2019 to 2022."
        }
    },
    {
        "id": "javier_milei",
        "name": {
            "uz": "Xavyer Miley",
            "ru": "Хавьер Милей",
            "en": "Javier Milei"
        },
        "country": {
            "uz": "Argentina",
            "ru": "Аргентина",
            "en": "Argentina"
        },
        "role": {
            "uz": "Argentina Prezidenti (2023-yildan)",
            "ru": "Президент Аргентины (с 2023)",
            "en": "President of Argentina (since 2023)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Javier_Milei_in_pull-aside_meeting_at_the_United_Nations_Headquarters_%283x4_cropped%29.jpg/640px-Javier_Milei_in_pull-aside_meeting_at_the_United_Nations_Headquarters_%283x4_cropped%29.jpg",
        "aliases": [
            "javier milei",
            "milei",
            "miley",
            "милей",
            "хавьер милей"
        ],
        "fun_fact": {
            "uz": "Dunyoning birinchi libertar-anarxo-kapitalist prezidenti sifatida davlat xarajatlarini radikal qisqartirgan.",
            "ru": "Первый в мире либертарианский президент, радикально сокративший число министерств.",
            "en": "The world's first self-described libertarian president, campaigning to drastically cut public spending."
        }
    },
    {
        "id": "jose_mujica",
        "name": {
            "uz": "Xose Muxika",
            "ru": "Хосе Мухика",
            "en": "José Mujica"
        },
        "country": {
            "uz": "Urugvay",
            "ru": "Уругвай",
            "en": "Uruguay"
        },
        "role": {
            "uz": "Urugvay Prezidenti (2010–2015)",
            "ru": "Президент Уругвая (2010–2015)",
            "en": "President of Uruguay (2010–2015)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Mujica.jpg/640px-Mujica.jpg",
        "aliases": [
            "jose mujica",
            "mujica",
            "muxika",
            "мухика",
            "хосе мухика"
        ],
        "fun_fact": {
            "uz": "'Dunyoning eng kamtar prezidenti' deb atalgan, oyligining 90%ini xayriyaga bergan va eski 'Folksvagen Juk' avtomobilida yurgan.",
            "ru": "Получил известность как «самый бедный президент в мире», отдавал почти всю зарплату на благотворительность.",
            "en": "Dubbed 'the world's humblest president' for donating 90% of his salary and driving a 1987 Volkswagen Beetle."
        }
    },
    {
        "id": "gabriel_boric",
        "name": {
            "uz": "Gabriel Borich",
            "ru": "Габриэль Борич",
            "en": "Gabriel Boric"
        },
        "country": {
            "uz": "Chili",
            "ru": "Чили",
            "en": "Chile"
        },
        "role": {
            "uz": "Chili Prezidenti (2022-yildan)",
            "ru": "Президент Чили (с 2022)",
            "en": "President of Chile (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Retrato_Oficial_Presidente_Boric_Font.jpg/640px-Retrato_Oficial_Presidente_Boric_Font.jpg",
        "aliases": [
            "gabriel boric",
            "boric",
            "borich",
            "борич",
            "габриэль борич"
        ],
        "fun_fact": {
            "uz": "Chili tarixidagi eng yosh prezident (36 yoshda saylangan), sobiq talabalar harakati yetakchisi.",
            "ru": "Стал самым молодым президентом в истории Чили (в возрасте 36 лет), бывший студенческий лидер.",
            "en": "Elected as Chile's youngest president at age 36 after rising to prominence through student protest movements."
        }
    },
    {
        "id": "gustavo_petro",
        "name": {
            "uz": "Gustavo Petro",
            "ru": "Густаво Петро",
            "en": "Gustavo Petro"
        },
        "country": {
            "uz": "Kolumbiya",
            "ru": "Колумбия",
            "en": "Colombia"
        },
        "role": {
            "uz": "Kolumbiya Prezidenti (2022-yildan)",
            "ru": "Президент Колумбии (с 2022)",
            "en": "President of Colombia (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Foto_Oficial_Presidente_Gustavo_Petro_%283x4_cropped%29.jpg/640px-Foto_Oficial_Presidente_Gustavo_Petro_%283x4_cropped%29.jpg",
        "aliases": [
            "gustavo petro",
            "petro",
            "петро",
            "густаво петро"
        ],
        "fun_fact": {
            "uz": "Kolumbiya tarixidagi birinchi so'l qanot prezidenti va sobiq partizan harakati a'zosi.",
            "ru": "Первый в истории Колумбии президент левых взглядов, в молодости состоял в повстанческом движении М-19.",
            "en": "Colombia's first left-wing president, a former member of the M-19 guerrilla movement turned mayor and senator."
        }
    },
    {
        "id": "nayib_bukele",
        "name": {
            "uz": "Nayib Bukele",
            "ru": "Найиб Букеле",
            "en": "Nayib Bukele"
        },
        "country": {
            "uz": "El Salvador",
            "ru": "Сальвадор",
            "en": "El Salvador"
        },
        "role": {
            "uz": "El Salvador Prezidenti (2019-yildan)",
            "ru": "Президент Сальвадора (с 2019)",
            "en": "President of El Salvador (since 2019)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Presidente_Nayib_Bukele_%28cropped%29.jpg/640px-Presidente_Nayib_Bukele_%28cropped%29.jpg",
        "aliases": [
            "nayib bukele",
            "bukele",
            "букеле",
            "найиб букеле"
        ],
        "fun_fact": {
            "uz": "Bitkoinni rasmiy to'lov vositasi sifatida qabul qilgan birinchi davlat rahbari va jinoyatchilikni keskin pasaytirgan.",
            "ru": "Первым в мире сделал биткоин официальным платежным средством и радикально победил бандитизм.",
            "en": "Made Bitcoin legal tender in El Salvador and drastically reduced national homicide rates through tough policing."
        }
    },
    {
        "id": "fidel_castro",
        "name": {
            "uz": "Fidel Kastro",
            "ru": "Фидель Кастро",
            "en": "Fidel Castro"
        },
        "country": {
            "uz": "Kuba",
            "ru": "Куба",
            "en": "Cuba"
        },
        "role": {
            "uz": "Kuba inqilobi yetakchisi va Prezidenti (1959–2008)",
            "ru": "Лидер Кубинской революции и Президент Кубы (1959–2008)",
            "en": "Leader of the Cuban Revolution (1959–2008)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Fidel_Castro_1950s_%28cropped%29.jpg/640px-Fidel_Castro_1950s_%28cropped%29.jpg",
        "aliases": [
            "fidel castro",
            "castro",
            "kastro",
            "кастро",
            "фидель кастро"
        ],
        "fun_fact": {
            "uz": "1959-yilgi Kuba inqilobiga rahbarlik qilgan va mamlakatni deyarli yarim asr davomida boshqargan.",
            "ru": "Возглавил Кубинскую революцию 1959 года и руководил Кубой на протяжении почти полувека.",
            "en": "Commanded the Cuban Revolution of 1959 and governed Cuba as supreme leader for almost 50 years."
        }
    },
    {
        "id": "hugo_chavez",
        "name": {
            "uz": "Ugo Chaves",
            "ru": "Уго Чавес",
            "en": "Hugo Chávez"
        },
        "country": {
            "uz": "Venesuela",
            "ru": "Венесуэла",
            "en": "Venezuela"
        },
        "role": {
            "uz": "Venesuela Prezidenti (1999–2013)",
            "ru": "Президент Венесуэлы (1999–2013)",
            "en": "President of Venezuela (1999–2013)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Hugo_Chavez_Portrait_%28cropped%29.jpg/640px-Hugo_Chavez_Portrait_%28cropped%29.jpg",
        "aliases": [
            "hugo chavez",
            "chavez",
            "chaves",
            "чавес",
            "уго чавес"
        ],
        "fun_fact": {
            "uz": "Venesuelada 'Bolivar inqilobi' va 'XXI asr sotsializmi'ni e'lon qilgan karizmatik yetakchi.",
            "ru": "Провозгласил «Боливарианскую революцию» и социализм XXI века, опираясь на доходы от нефти.",
            "en": "Led the Bolivarian Revolution in Venezuela, advocating 21st-century socialism and regional integration."
        }
    },
    {
        "id": "nicolas_maduro",
        "name": {
            "uz": "Nikolas Maduro",
            "ru": "Николас Мадуро",
            "en": "Nicolás Maduro"
        },
        "country": {
            "uz": "Venesuela",
            "ru": "Венесуэла",
            "en": "Venezuela"
        },
        "role": {
            "uz": "Venesuela Prezidenti (2013-yildan)",
            "ru": "Президент Венесуэлы (с 2013)",
            "en": "President of Venezuela (since 2013)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Nicol%C3%A1s_Maduro_2023_%28cropped2%29.jpg/640px-Nicol%C3%A1s_Maduro_2023_%28cropped2%29.jpg",
        "aliases": [
            "nicolas maduro",
            "maduro",
            "мадуро",
            "николас мадуро"
        ],
        "fun_fact": {
            "uz": "Sobiq avtobus haydovchisi va kasaba uyushmasi faoli bo'lib, Ugo Chavesning siyosiy vorisi bo'lgan.",
            "ru": "Бывший водитель автобуса и профсоюзный деятель, ставший преемником Уго Чавеса.",
            "en": "A former bus driver and trade union leader chosen by Hugo Chávez as his political successor."
        }
    },
    {
        "id": "vladimir_putin",
        "name": {
            "uz": "Vladimir Putin",
            "ru": "Владимир Путин",
            "en": "Vladimir Putin"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "role": {
            "uz": "Rossiya Federatsiyasi Prezidenti",
            "ru": "Президент Российской Федерации",
            "en": "President of the Russian Federation"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Vladimir_Putin_%282026_02_23%29.jpg/640px-Vladimir_Putin_%282026_02_23%29.jpg",
        "aliases": [
            "vladimir putin",
            "putin",
            "путин",
            "владимир путин",
            "vladimir vladimirovich putin"
        ],
        "fun_fact": {
            "uz": "Rossiyani 2000-yildan buyon (prezident va bosh vazir sifatida) boshqarib kelayotgan eng uzoq muddatli zamonaviy rahbar.",
            "ru": "Возглавляет Россию в качестве президента и премьер-министра с 2000 года.",
            "en": "Has led the Russian Federation as President and Prime Minister continuously since 2000."
        }
    },
    {
        "id": "dmitry_medvedev",
        "name": {
            "uz": "Dmitriy Medvedev",
            "ru": "Дмитрий Медведев",
            "en": "Dmitry Medvedev"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "role": {
            "uz": "Rossiya Federatsiyasi Prezidenti (2008–2012)",
            "ru": "Президент Российской Федерации (2008–2012)",
            "en": "President of Russia (2008–2012)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Dmitry_Medvedev_%282026-02-06%29.jpg/640px-Dmitry_Medvedev_%282026-02-06%29.jpg",
        "aliases": [
            "dmitry medvedev",
            "medvedev",
            "медведев",
            "дмитрий медведев",
            "dmitriy medvedev"
        ],
        "fun_fact": {
            "uz": "Prezidentligi davrida 'Skolkovo' innovatsiya markazini tashkil etgan va texnologiyalarni modernizatsiyalashni ilgari surgan.",
            "ru": "Инициировал создание инновационного центра «Сколково» и программу модернизации экономики.",
            "en": "Championed technological modernization and spearheaded the creation of the Skolkovo Innovation Center."
        }
    },
    {
        "id": "boris_yeltsin",
        "name": {
            "uz": "Boris Yelsin",
            "ru": "Борис Ельцин",
            "en": "Boris Yeltsin"
        },
        "country": {
            "uz": "Rossiya",
            "ru": "Россия",
            "en": "Russia"
        },
        "role": {
            "uz": "Rossiya Federatsiyasining Birinchi Prezidenti (1991–1999)",
            "ru": "Первый Президент Российской Федерации (1991–1999)",
            "en": "First President of Russia (1991–1999)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Boris_Yeltsin_%283x4_cropped%29.jpg/640px-Boris_Yeltsin_%283x4_cropped%29.jpg",
        "aliases": [
            "boris yeltsin",
            "yeltsin",
            "yelsin",
            "ельцин",
            "борис ельцин"
        ],
        "fun_fact": {
            "uz": "SSSR parchalanishidan so'ng yangi Rossiyaning birinchi prezidenti bo'lib, 1999-yil 31-dekabrda kutilmaganda iste'fo bergan.",
            "ru": "Первый президент постсоветской России, объявил о досрочной отставке в новогоднем обращении 1999 года.",
            "en": "The first president of independent Russia following the collapse of the Soviet Union, resigning on New Year's Eve 1999."
        }
    },
    {
        "id": "mikhail_gorbachev",
        "name": {
            "uz": "Mixail Gorbachyov",
            "ru": "Михаил Горбачёв",
            "en": "Mikhail Gorbachev"
        },
        "country": {
            "uz": "SSSR / Rossiya",
            "ru": "СССР / Россия",
            "en": "Soviet Union / Russia"
        },
        "role": {
            "uz": "SSSRning oxirgi rahbari va birinchi Prezidenti (1985–1991)",
            "ru": "Последний Генеральный секретарь ЦК КПСС и Президент СССР",
            "en": "Last General Secretary and President of the Soviet Union"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/RIAN_archive_850809_General_Secretary_of_the_CPSU_CC_M._Gorbachev_%28crop%29.jpg/640px-RIAN_archive_850809_General_Secretary_of_the_CPSU_CC_M._Gorbachev_%28crop%29.jpg",
        "aliases": [
            "mikhail gorbachev",
            "gorbachev",
            "gorbachyov",
            "горбачев",
            "михаил горбачев"
        ],
        "fun_fact": {
            "uz": "'Qayta qurish' (Perestroyka) va 'Oshkoralik' (Glasnost) siyosatini joriy etib, Sovuq urushga barham bergan.",
            "ru": "Инициатор «перестройки» и «гласности», лауреат Нобелевской премии мира 1990 года.",
            "en": "Introduced Perestroika and Glasnost, bringing an end to the Cold War, and received the 1990 Nobel Peace Prize."
        }
    },
    {
        "id": "volodymyr_zelenskyy",
        "name": {
            "uz": "Vladimir Zelenskiy",
            "ru": "Владимир Зеленский",
            "en": "Volodymyr Zelenskyy"
        },
        "country": {
            "uz": "Ukraina",
            "ru": "Украина",
            "en": "Ukraine"
        },
        "role": {
            "uz": "Ukraina Prezidenti (2019-yildan)",
            "ru": "Президент Украины (с 2019)",
            "en": "President of Ukraine (since 2019)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Volodymyr_Zelensky_2022_official_portrait_%28cropped%29.jpg/640px-Volodymyr_Zelensky_2022_official_portrait_%28cropped%29.jpg",
        "aliases": [
            "volodymyr zelenskyy",
            "zelensky",
            "zelenskiy",
            "зеленский",
            "владимир зеленский"
        ],
        "fun_fact": {
            "uz": "Sobiq aktyor va komik bo'lib, 'Xalq xizmatchisi' serialida prezident rolini o'ynagan va 2019-yilda haqiqatan ham prezident etib saylangan.",
            "ru": "Бывший актер и шоумен, сыгравший президента в комедийном сериале «Слуга народа» перед реальным избранием.",
            "en": "Former comedic actor who starred as an accidental president in 'Servant of the People' before winning the presidency."
        }
    },
    {
        "id": "petro_poroshenko",
        "name": {
            "uz": "Pyotr Poroshenko",
            "ru": "Пётр Порошенко",
            "en": "Petro Poroshenko"
        },
        "country": {
            "uz": "Ukraina",
            "ru": "Украина",
            "en": "Ukraine"
        },
        "role": {
            "uz": "Ukraina Prezidenti (2014–2019)",
            "ru": "Президент Украины (2014–2019)",
            "en": "President of Ukraine (2014–2019)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Official_portrait_of_Petro_Poroshenko.jpg/640px-Official_portrait_of_Petro_Poroshenko.jpg",
        "aliases": [
            "petro poroshenko",
            "poroshenko",
            "порошенко",
            "петр порошенко"
        ],
        "fun_fact": {
            "uz": "Muvaffaqiyatli qandolat magnati ('Roshen' asoschisi) bo'lib, Yevromaydon voqealaridan so'ng prezident bo'lgan.",
            "ru": "Бизнесмен и основатель корпорации «Рошен», ставший президентом после событий Евромайдана 2014 года.",
            "en": "Confectionery billionaire (founder of Roshen) who led Ukraine through the aftermath of the 2014 Euromaidan."
        }
    },
    {
        "id": "aleksandr_lukashenko",
        "name": {
            "uz": "Aleksandr Lukashenko",
            "ru": "Александр Лукашенко",
            "en": "Alexander Lukashenko"
        },
        "country": {
            "uz": "Belarus",
            "ru": "Беларусь",
            "en": "Belarus"
        },
        "role": {
            "uz": "Belarus Prezidenti (1994-yildan)",
            "ru": "Президент Республики Беларусь (с 1994)",
            "en": "President of Belarus (since 1994)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Meeting_of_the_Supreme_State_Council_of_the_Union_State_-_February_2026_-_4_%28cropped%29.jpg/640px-Meeting_of_the_Supreme_State_Council_of_the_Union_State_-_February_2026_-_4_%28cropped%29.jpg",
        "aliases": [
            "aleksandr lukashenko",
            "lukashenko",
            "лукашенко",
            "александр лукашенко"
        ],
        "fun_fact": {
            "uz": "Yevropada davlat boshida eng uzoq vaqt (1994-yildan buyon) turgan prezident hisoblanadi.",
            "ru": "Бессменно руководит Беларусью с 1994 года, являясь дольше всех правящим лидером в Европе.",
            "en": "Has served as President of Belarus since 1994, making him Europe's longest-ruling head of state."
        }
    },
    {
        "id": "emmanuel_macron",
        "name": {
            "uz": "Emmanuel Makron",
            "ru": "Эмманюэль Макрон",
            "en": "Emmanuel Macron"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "role": {
            "uz": "Fransiya Prezidenti (2017-yildan)",
            "ru": "Президент Франции (с 2017)",
            "en": "President of France (since 2017)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Emmanuel_Macron_2025_%28cropped%29.jpg/640px-Emmanuel_Macron_2025_%28cropped%29.jpg",
        "aliases": [
            "emmanuel macron",
            "macron",
            "makron",
            "макрон",
            "эмманюэль макрон"
        ],
        "fun_fact": {
            "uz": "Napoleon Bonapartdan keyin Fransiya tarixidagi eng yosh davlat rahbari (39 yoshda saylangan).",
            "ru": "Стал самым молодым главой французского государства со времен Наполеона Бонапарта (в 39 лет).",
            "en": "Became the youngest head of state in French history since Napoleon Bonaparte when elected at age 39."
        }
    },
    {
        "id": "francois_hollande",
        "name": {
            "uz": "Fransua Olland",
            "ru": "Франсуа Олланд",
            "en": "François Hollande"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "role": {
            "uz": "Fransiya Prezidenti (2012–2017)",
            "ru": "Президент Франции (2012–2017)",
            "en": "President of France (2012–2017)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Fran%C3%A7ois_Hollande_-_2017_%2827869823159%29_%28cropped_2%29.jpg/640px-Fran%C3%A7ois_Hollande_-_2017_%2827869823159%29_%28cropped_2%29.jpg",
        "aliases": [
            "francois hollande",
            "hollande",
            "olland",
            "олланд",
            "франсуа олланд"
        ],
        "fun_fact": {
            "uz": "Uning davrida Parijda tarixiy Iqlim bo'yicha Parij bitimi imzolangan.",
            "ru": "В период его правления было принято историческое Парижское соглашение по климату 2015 года.",
            "en": "Hosted the COP21 summit that produced the landmark 2015 Paris Climate Agreement."
        }
    },
    {
        "id": "nicolas_sarkozy",
        "name": {
            "uz": "Nikola Sarkozi",
            "ru": "Николя Саркози",
            "en": "Nicolas Sarkozy"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "role": {
            "uz": "Fransiya Prezidenti (2007–2012)",
            "ru": "Президент Франции (2007–2012)",
            "en": "President of France (2007–2012)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Nicolas_Sarkozy_in_2010.jpg/640px-Nicolas_Sarkozy_in_2010.jpg",
        "aliases": [
            "nicolas sarkozy",
            "sarkozy",
            "sarkozi",
            "саркози",
            "николя саркози"
        ],
        "fun_fact": {
            "uz": "2008-yilgi Yevropa moliyaviy inqirozi va Gruziyadagi urushda vositachilik qilgan fransuz yetakchisi.",
            "ru": "Выступил ключевым посредником при урегулировании вооруженного конфликта в Южной Осетии в 2008 году.",
            "en": "Brokered the ceasefire agreement that ended the 2008 Russo-Georgian War during France's EU presidency."
        }
    },
    {
        "id": "jacques_chirac",
        "name": {
            "uz": "Jak Shirak",
            "ru": "Жак Ширак",
            "en": "Jacques Chirac"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "role": {
            "uz": "Fransiya Prezidenti (1995–2007)",
            "ru": "Президент Франции (1995–2007)",
            "en": "President of France (1995–2007)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Jacques_Chirac_%281997%29_%28cropped%29.jpg/640px-Jacques_Chirac_%281997%29_%28cropped%29.jpg",
        "aliases": [
            "jacques chirac",
            "chirac",
            "shirak",
            "ширак",
            "жак ширак"
        ],
        "fun_fact": {
            "uz": "Fransiyaning 2003-yildagi Iroq urushiga qatnashishiga qat'iy qarshi chiqqan va Parij merligida uzoq yil ishlagan.",
            "ru": "Решительно выступил против вторжения коалиции во главе с США в Ирак в 2003 году.",
            "en": "Vehemently opposed the 2003 invasion of Iraq and served 18 years as Mayor of Paris before the presidency."
        }
    },
    {
        "id": "charles_de_gaulle",
        "name": {
            "uz": "Sharl de Goll",
            "ru": "Шарль де Голль",
            "en": "Charles de Gaulle"
        },
        "country": {
            "uz": "Fransiya",
            "ru": "Франция",
            "en": "France"
        },
        "role": {
            "uz": "Fransiya Prezidenti (1959–1969), Beshinchi Respublika asoschisi",
            "ru": "Основатель Пятой республики и Президент Франции (1959–1969)",
            "en": "Leader of Free France and President of France (1959–1969)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/De_Gaulle-OWI_%28cropped%29_%28c%29%282%29.jpg/640px-De_Gaulle-OWI_%28cropped%29_%28c%29%282%29.jpg",
        "aliases": [
            "charles de gaulle",
            "de gaulle",
            "sharl de goll",
            "де голль",
            "шарль де голль"
        ],
        "fun_fact": {
            "uz": "Ikkinchi jahon urushida 'Ozod Fransiya' harakatiga boshchilik qilgan va Fransiyaning Beshinchi Respublikasiga asos solgan.",
            "ru": "Лидер французского Сопротивления во Второй мировой войне, создал современную политическую систему Франции.",
            "en": "Led the Free French forces during WWII and founded France's Fifth Republic with its current constitution."
        }
    },
    {
        "id": "olaf_scholz",
        "name": {
            "uz": "Olaf Shols",
            "ru": "Олаф Шольц",
            "en": "Olaf Scholz"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Germany"
        },
        "role": {
            "uz": "Germaniya Federal Kansleri (2021-yildan)",
            "ru": "Федеральный канцлер Германии (с 2021)",
            "en": "Chancellor of Germany (since 2021)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Olaf_Scholz_September_2024.jpg/640px-Olaf_Scholz_September_2024.jpg",
        "aliases": [
            "olaf scholz",
            "scholz",
            "shols",
            "шольц",
            "олаф шольц"
        ],
        "fun_fact": {
            "uz": "Germaniya xavfsizlik siyosatida tarixiy burilish hisoblangan 'Zeitenwende' (Davrlar burilishi) strategiyasini e'lon qilgan.",
            "ru": "Провозгласил исторический поворот в оборонной политике Германии под названием «Zeitenwende».",
            "en": "Announced Germany's historic 'Zeitenwende' defense and energy policy pivot following the 2022 invasion of Ukraine."
        }
    },
    {
        "id": "angela_merkel",
        "name": {
            "uz": "Angela Merkel",
            "ru": "Ангела Меркель",
            "en": "Angela Merkel"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Germany"
        },
        "role": {
            "uz": "Germaniya Federal Kansleri (2005–2021)",
            "ru": "Федеральный канцлер Германии (2005–2021)",
            "en": "Chancellor of Germany (2005–2021)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Angela_Merkel_2019_cropped.jpg/640px-Angela_Merkel_2019_cropped.jpg",
        "aliases": [
            "angela merkel",
            "merkel",
            "меркель",
            "ангела меркель"
        ],
        "fun_fact": {
            "uz": "Germaniyaning birinchi ayol kansleri bo'lib, 16 yil davomida Yevropa Ittifoqining norasmiy yetakchisi hisoblangan.",
            "ru": "Первая женщина на посту канцлера Германии, руководила страной 16 лет и считалась лидером свободного мира.",
            "en": "The first female Chancellor of Germany, leading the European Union through multiple global crises over 16 years."
        }
    },
    {
        "id": "helmut_kohl",
        "name": {
            "uz": "Gelmut Kol",
            "ru": "Гельмут Коль",
            "en": "Helmut Kohl"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Germany"
        },
        "role": {
            "uz": "Germaniya Kansleri (1982–1998)",
            "ru": "Федеральный канцлер Германии (1982–1998)",
            "en": "Chancellor of Germany (1982–1998)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Helmut_Kohl_%281996%29_cropped_%282%29.jpg/640px-Helmut_Kohl_%281996%29_cropped_%282%29.jpg",
        "aliases": [
            "helmut kohl",
            "kohl",
            "kol",
            "коль",
            "гельмут коль"
        ],
        "fun_fact": {
            "uz": "1990-yilda Berlin devori qulashidan so'ng Germaniyaning birlashuviga rahbarlik qilgan va yevro valyutasini kiritgan.",
            "ru": "«Канцлер единства», добившийся объединения ФРГ и ГДР в 1990 году, архитектор введения евро.",
            "en": "The 'Chancellor of Unity' who presided over German reunification and the signing of the Maastricht Treaty."
        }
    },
    {
        "id": "frank_walter_steinmeier",
        "name": {
            "uz": "Frank-Valter Shtaynmayyer",
            "ru": "Франк-Вальтер Штайнмайер",
            "en": "Frank-Walter Steinmeier"
        },
        "country": {
            "uz": "Germaniya",
            "ru": "Германия",
            "en": "Germany"
        },
        "role": {
            "uz": "Germaniya Federal Prezidenti (2017-yildan)",
            "ru": "Федеральный президент Германии (с 2017)",
            "en": "President of Germany (since 2017)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Frank-Walter_Steinmeier_2026.jpeg/640px-Frank-Walter_Steinmeier_2026.jpeg",
        "aliases": [
            "frank-walter steinmeier",
            "steinmeier",
            "штайнмайер",
            "франк-вальтер штайнмайер"
        ],
        "fun_fact": {
            "uz": "Uzoq yillar Germaniya tashqi ishlar vaziri bo'lib xizmat qilgan va 'Shtaynmayyer formulasi' muallifi.",
            "ru": "Возглавлял МИД Германии, автор дипломатической инициативы «Формула Штайнмайера».",
            "en": "Former long-serving German Foreign Minister known for authoring the 'Steinmeier Formula' diplomatic proposal."
        }
    },
    {
        "id": "keir_starmer",
        "name": {
            "uz": "Kir Starmer",
            "ru": "Кир Стармер",
            "en": "Keir Starmer"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "role": {
            "uz": "Buyuk Britaniya Bosh vaziri (2024-yildan)",
            "ru": "Премьер-министр Великобритании (с 2024)",
            "en": "Prime Minister of the United Kingdom (since 2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Prime_Minister_Keir_Starmer_Portrait_%28cropped%29.jpg/640px-Prime_Minister_Keir_Starmer_Portrait_%28cropped%29.jpg",
        "aliases": [
            "keir starmer",
            "starmer",
            "стармер",
            "кир стармер"
        ],
        "fun_fact": {
            "uz": "Leyboristlar partiyasini 14 yillik tanaffusdan keyin tarixiy g'alaba bilan hokimiyatga qaytargan sobiq bosh prokuror.",
            "ru": "Бывший генеральный прокурор, вернувший Лейбористскую партию к власти после 14 лет в оппозиции.",
            "en": "Former Director of Public Prosecutions who led the Labour Party back to a landslide victory in 2024."
        }
    },
    {
        "id": "rishi_sunak",
        "name": {
            "uz": "Rishi Sunak",
            "ru": "Риши Сунак",
            "en": "Rishi Sunak"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "role": {
            "uz": "Buyuk Britaniya Bosh vaziri (2022–2024)",
            "ru": "Премьер-министр Великобритании (2022–2024)",
            "en": "Prime Minister of the United Kingdom (2022–2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Portrait_of_Prime_Minister_Rishi_Sunak_%28cropped%29.jpg/640px-Portrait_of_Prime_Minister_Rishi_Sunak_%28cropped%29.jpg",
        "aliases": [
            "rishi sunak",
            "sunak",
            "сунак",
            "риши сунак"
        ],
        "fun_fact": {
            "uz": "Britaniya tarixidagi birinchi kelib chiqishi hindistonlik bo'lgan bosh vazir va zamonaviy davrdagi eng yosh rahbarlardan biri.",
            "ru": "Первый британский премьер-министр индийского происхождения и исповедующий индуизм.",
            "en": "The first British Asian prime minister and the youngest person to hold the office in modern history."
        }
    },
    {
        "id": "boris_johnson",
        "name": {
            "uz": "Boris Jonson",
            "ru": "Борис Джонсон",
            "en": "Boris Johnson"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "role": {
            "uz": "Buyuk Britaniya Bosh vaziri (2019–2022)",
            "ru": "Премьер-министр Великобритании (2019–2022)",
            "en": "Prime Minister of the United Kingdom (2019–2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Boris_Johnson_official_portrait_%28cropped%29.jpg/640px-Boris_Johnson_official_portrait_%28cropped%29.jpg",
        "aliases": [
            "boris johnson",
            "johnson",
            "jonson",
            "джонсон",
            "борис джонсон"
        ],
        "fun_fact": {
            "uz": "'Get Brexit Done' shiori ostida Buyuk Britaniyaning Yevropa Ittifoqidan chiqish jarayonini yakunlagan.",
            "ru": "Осуществил выход Великобритании из Европейского союза (Brexit) под лозунгом «Get Brexit Done».",
            "en": "Delivered Brexit for the UK with a resounding parliamentary majority under the slogan 'Get Brexit Done'."
        }
    },
    {
        "id": "tony_blair",
        "name": {
            "uz": "Toni Bler",
            "ru": "Тони Блэр",
            "en": "Tony Blair"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "role": {
            "uz": "Buyuk Britaniya Bosh vaziri (1997–2007)",
            "ru": "Премьер-министр Великобритании (1997–2007)",
            "en": "Prime Minister of the United Kingdom (1997–2007)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Tony_Blair_%282010%29.jpg/640px-Tony_Blair_%282010%29.jpg",
        "aliases": [
            "tony blair",
            "blair",
            "bler",
            "блэр",
            "тони блэр"
        ],
        "fun_fact": {
            "uz": "'Yangi leyboristlar' harakatini yaratgan va Shimoliy Irlandiyada 'Xayrli juma' tinchlik bitimini imzolagan.",
            "ru": "Создатель концепции «Новых лейбористов», подписал Соглашение Страстной пятницы в Северной Ирландии.",
            "en": "Pioneered 'New Labour' and secured the historic 1998 Good Friday Agreement in Northern Ireland."
        }
    },
    {
        "id": "margaret_thatcher",
        "name": {
            "uz": "Margaret Tetcher",
            "ru": "Маргарет Тэтчер",
            "en": "Margaret Thatcher"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "role": {
            "uz": "Buyuk Britaniya Bosh vaziri (1979–1990), 'Temir xonim'",
            "ru": "Премьер-министр Великобритании (1979–1990), «Железная леди»",
            "en": "Prime Minister of the United Kingdom (1979–1990)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Margaret_Thatcher_stock_portrait_%28cropped%29.jpg/640px-Margaret_Thatcher_stock_portrait_%28cropped%29.jpg",
        "aliases": [
            "margaret thatcher",
            "thatcher",
            "tetcher",
            "тэтчер",
            "маргарет тэтчер",
            "temir xonim"
        ],
        "fun_fact": {
            "uz": "Buyuk Britaniyaning birinchi ayol bosh vaziri bo'lib, o'zining qat'iyati uchun 'Temir xonim' laqabini olgan.",
            "ru": "Первая женщина премьер-министр Великобритании, вошедшая в мировую историю как «Железная леди».",
            "en": "Known as the 'Iron Lady', she was the UK's first female prime minister and transformed the British economy."
        }
    },
    {
        "id": "winston_churchill",
        "name": {
            "uz": "Uinston Cherchill",
            "ru": "Уинстон Черчилль",
            "en": "Winston Churchill"
        },
        "country": {
            "uz": "Buyuk Britaniya",
            "ru": "Великобритания",
            "en": "United Kingdom"
        },
        "role": {
            "uz": "Buyuk Britaniya Bosh vaziri (1940–1945, 1951–1955)",
            "ru": "Премьер-министр Великобритании (1940–1945, 1951–1955)",
            "en": "Prime Minister of the United Kingdom (1940–1945, 1951–1955)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Sir_Winston_Churchill_-_19086236948_%28restored%29.jpg/640px-Sir_Winston_Churchill_-_19086236948_%28restored%29.jpg",
        "aliases": [
            "winston churchill",
            "churchill",
            "cherchill",
            "черчилль",
            "уинстон черчилль"
        ],
        "fun_fact": {
            "uz": "Ikkinchi jahon urushida Buyuk Britaniyani natsizm ustidan g'alabaga yetaklagan va adabiyot bo'yicha Nobel mukofotini olgan.",
            "ru": "Привел Британию к победе над нацизмом во Второй мировой войне, лауреат Нобелевской премии по литературе.",
            "en": "Rallied the British nation to victory in WWII and was awarded the Nobel Prize in Literature in 1953."
        }
    },
    {
        "id": "giorgia_meloni",
        "name": {
            "uz": "Jorjiya Meloni",
            "ru": "Джорджа Мелони",
            "en": "Giorgia Meloni"
        },
        "country": {
            "uz": "Italiya",
            "ru": "Италия",
            "en": "Italy"
        },
        "role": {
            "uz": "Italiya Bosh vaziri (2022-yildan)",
            "ru": "Премьер-министр Италии (с 2022)",
            "en": "Prime Minister of Italy (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Giorgia_Meloni_Official_2024_%28cropped%29.jpg/640px-Giorgia_Meloni_Official_2024_%28cropped%29.jpg",
        "aliases": [
            "giorgia meloni",
            "meloni",
            "мелони",
            "джорджа мелони"
        ],
        "fun_fact": {
            "uz": "Italiya tarixidagi birinchi ayol bosh vazir bo'lib, o'ng markazchi 'Italiya birodarlari' partiyasiga rahbarlik qiladi.",
            "ru": "Первая женщина в истории на посту премьер-министра Италии, лидер партии «Братья Италии».",
            "en": "The first female prime minister of Italy, leading the Brothers of Italy party."
        }
    },
    {
        "id": "sergio_mattarella",
        "name": {
            "uz": "Serjo Mattarella",
            "ru": "Серджо Маттарелла",
            "en": "Sergio Mattarella"
        },
        "country": {
            "uz": "Italiya",
            "ru": "Италия",
            "en": "Italy"
        },
        "role": {
            "uz": "Italiya Prezidenti (2015-yildan)",
            "ru": "Президент Италии (с 2015)",
            "en": "President of Italy (since 2015)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Sergio_Mattarella_Presidente_della_Repubblica_Italiana.jpg/640px-Sergio_Mattarella_Presidente_della_Repubblica_Italiana.jpg",
        "aliases": [
            "sergio mattarella",
            "mattarella",
            "маттарелла",
            "серджо маттарелла"
        ],
        "fun_fact": {
            "uz": "Sobiq konstitutsiyaviy sudya bo'lib, Italiya tarixida ikkinchi muddatga qayta saylangan kam sonli prezidentlardan biri.",
            "ru": "Опытный юрист и бывший судья Конституционного суда, переизбран на второй президентский срок.",
            "en": "Former Constitutional Court judge who became only the second Italian president to be re-elected for a second term."
        }
    },
    {
        "id": "silvio_berlusconi",
        "name": {
            "uz": "Silvio Berluskoni",
            "ru": "Сильвио Берлускони",
            "en": "Silvio Berlusconi"
        },
        "country": {
            "uz": "Italiya",
            "ru": "Италия",
            "en": "Italy"
        },
        "role": {
            "uz": "Italiya Bosh vaziri (to'rt marta)",
            "ru": "Премьер-министр Италии (четыре срока)",
            "en": "Prime Minister of Italy (four terms)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Silvio_Berlusconi_%282010%29_cropped.jpg/640px-Silvio_Berlusconi_%282010%29_cropped.jpg",
        "aliases": [
            "silvio berlusconi",
            "berlusconi",
            "берлускони",
            "сильвио берлускони"
        ],
        "fun_fact": {
            "uz": "Milliarder media-magnat va 'Milan' futbol klubining afsonaviy egasi bo'lgan.",
            "ru": "Медиамагнат и миллиардер, многолетний владелец футбольного клуба «Милан».",
            "en": "Billionaire media tycoon and longtime owner of AC Milan who served as prime minister in four separate governments."
        }
    },
    {
        "id": "pedro_sanchez",
        "name": {
            "uz": "Pedro Sanches",
            "ru": "Педро Санчес",
            "en": "Pedro Sánchez"
        },
        "country": {
            "uz": "Ispaniya",
            "ru": "Испания",
            "en": "Spain"
        },
        "role": {
            "uz": "Ispaniya Bosh vaziri (2018-yildan)",
            "ru": "Председатель правительства Испании (с 2018)",
            "en": "Prime Minister of Spain (since 2018)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Pedro_S%C3%A1nchez_2026_Portrait_%283x4_cropped%29.jpg/640px-Pedro_S%C3%A1nchez_2026_Portrait_%283x4_cropped%29.jpg",
        "aliases": [
            "pedro sanchez",
            "sanchez",
            "sanches",
            "санчес",
            "педро санчес"
        ],
        "fun_fact": {
            "uz": "Ispaniya tarixida ishonchsizlik votumi orqali hukumat tepasiga kelgan birinchi bosh vazir.",
            "ru": "Первый премьер-министр в истории Испании, пришедший к власти в результате вотума недоверия предшественнику.",
            "en": "Became Prime Minister of Spain after winning a historic motion of no confidence against Mariano Rajoy."
        }
    },
    {
        "id": "andrzej_duda",
        "name": {
            "uz": "Anjey Duda",
            "ru": "Анджей Дуда",
            "en": "Andrzej Duda"
        },
        "country": {
            "uz": "Polsha",
            "ru": "Польша",
            "en": "Poland"
        },
        "role": {
            "uz": "Polsha Prezidenti (2015-yildan)",
            "ru": "Президент Польши (с 2015)",
            "en": "President of Poland (since 2015)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/President_of_Poland_Andrzej_Duda_Full_Resolution_%283x4_cropped%29.jpg/640px-President_of_Poland_Andrzej_Duda_Full_Resolution_%283x4_cropped%29.jpg",
        "aliases": [
            "andrzej duda",
            "duda",
            "дуда",
            "анджей дуда"
        ],
        "fun_fact": {
            "uz": "Polshaning NATO va mintaqadagi 'Uch dengiz tashabbusi' mudofaa aloqalarini mustahkamlashda faol rol o'ynagan.",
            "ru": "Активный сторонник укрепления восточного фланга НАТО и проекта «Инициатива трёх морей».",
            "en": "Key proponent of the Three Seas Initiative and strengthening NATO's eastern flank defenses."
        }
    },
    {
        "id": "lech_walesa",
        "name": {
            "uz": "Lex Valensa",
            "ru": "Лех Валенса",
            "en": "Lech Wałęsa"
        },
        "country": {
            "uz": "Polsha",
            "ru": "Польша",
            "en": "Poland"
        },
        "role": {
            "uz": "Polsha Prezidenti (1990–1995), 'Birdamlik' yetakchisi",
            "ru": "Президент Польши (1990–1995), лидер «Солидарности»",
            "en": "President of Poland (1990–1995)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/03.17_%E7%B8%BD%E7%B5%B1%E6%8E%A5%E8%A6%8B%E3%80%8C%E6%B3%A2%E8%98%AD%E5%89%8D%E7%B8%BD%E7%B5%B1%E8%8F%AF%E5%8B%92%E6%B2%99%E4%B9%99%E8%A1%8C%E3%80%8D_-_55151702432_%28cropped%29.jpg/640px-03.17_%E7%B8%BD%E7%B5%B1%E6%8E%A5%E8%A6%8B%E3%80%8C%E6%B3%A2%E8%98%AD%E5%89%8D%E7%B8%BD%E7%B5%B1%E8%8F%AF%E5%8B%92%E6%B2%99%E4%B9%99%E8%A1%8C%E3%80%8D_-_55151702432_%28cropped%29.jpg",
        "aliases": [
            "lech walesa",
            "walesa",
            "valensa",
            "валенса",
            "лех валенса"
        ],
        "fun_fact": {
            "uz": "Gdansklik elektrchi bo'lib, 'Birdamlik' kasaba uyushmasini tuzgan va Sharqiy Yevropada kommunizm qulashida hal qiluvchi rol o'ynagan.",
            "ru": "Электрик с Гданьской судоверфи, основавший профсоюз «Солидарность», лауреат Нобелевской премии мира 1983 года.",
            "en": "Gdansk shipyard electrician who co-founded Solidarity, won the Nobel Peace Prize, and became president of democratic Poland."
        }
    },
    {
        "id": "viktor_orban",
        "name": {
            "uz": "Viktor Orban",
            "ru": "Виктор Орбан",
            "en": "Viktor Orbán"
        },
        "country": {
            "uz": "Vengriya",
            "ru": "Венгрия",
            "en": "Hungary"
        },
        "role": {
            "uz": "Vengriya Bosh vaziri (1998–2002, 2010-yildan)",
            "ru": "Премьер-министр Венгрии (с 2010)",
            "en": "Prime Minister of Hungary (since 2010)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Viktor_Orban_2025_%28cropped%29.jpg/640px-Viktor_Orban_2025_%28cropped%29.jpg",
        "aliases": [
            "viktor orban",
            "orban",
            "орбан",
            "виктор орбан"
        ],
        "fun_fact": {
            "uz": "Yevropa Ittifoqida milliy suverenitet va noan'anaviy konservativ siyosat tarafdori sifatida tanilgan.",
            "ru": "Известен отстаиванием национального суверенитета Венгрии и концепцией «нелиберальной демократии».",
            "en": "Long-serving prime minister known for his conservative policies and defense of national sovereignty within the EU."
        }
    },
    {
        "id": "recep_tayyip_erdogan",
        "name": {
            "uz": "Rajab Toyyib Erdo'g'an",
            "ru": "Реджеп Тайип Эрдоган",
            "en": "Recep Tayyip Erdoğan"
        },
        "country": {
            "uz": "Turkiya",
            "ru": "Турция",
            "en": "Turkey"
        },
        "role": {
            "uz": "Turkiya Respublikasi Prezidenti (2014-yildan)",
            "ru": "Президент Турецкой Республики (с 2014)",
            "en": "President of Turkey (since 2014)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Turkish_President_Recep_Tayyip_Erdo%C4%9Fan_in_January_2024_%28cropped%29.jpg/640px-Turkish_President_Recep_Tayyip_Erdo%C4%9Fan_in_January_2024_%28cropped%29.jpg",
        "aliases": [
            "recep tayyip erdogan",
            "erdogan",
            "erdo'g'an",
            "эрдоган",
            "реджеп эрдоган"
        ],
        "fun_fact": {
            "uz": "Turkiyani parlamentar respublikadan prezidentlik boshqaruv shakliga o'tkazgan va Istanbul meri lavozimida ishlagan.",
            "ru": "Возглавляет Турцию более двух десятилетий, перевел страну на президентскую форму правления.",
            "en": "Transformed Turkey's political system into an executive presidency after serving as prime minister and mayor of Istanbul."
        }
    },
    {
        "id": "mustafa_kemal_ataturk",
        "name": {
            "uz": "Mustafo Kamol Otaturk",
            "ru": "Мустафа Кемаль Ататюрк",
            "en": "Mustafa Kemal Atatürk"
        },
        "country": {
            "uz": "Turkiya",
            "ru": "Турция",
            "en": "Turkey"
        },
        "role": {
            "uz": "Turkiya Respublikasining Birinchi Prezidenti va Asoschisi",
            "ru": "Основатель и первый Президент Турецкой Республики",
            "en": "Founder and First President of the Republic of Turkey"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Ataturk1930s.jpg/640px-Ataturk1930s.jpg",
        "aliases": [
            "mustafa kemal ataturk",
            "ataturk",
            "otaturk",
            "ататюрк",
            "мустафа кемаль ататюрк"
        ],
        "fun_fact": {
            "uz": "Usmonlilar imperiyasi qulagach mustaqillik urushiga yetakchilik qilib, zamonaviy dunyoviy Turkiya davlatini tuzgan.",
            "ru": "Создал современную светскую Турцию, провел реформы алфавита, правовой системы и образования.",
            "en": "Father of modern secular Turkey who led the Turkish War of Independence and introduced far-reaching modernizing reforms."
        }
    },
    {
        "id": "kyriakos_mitsotakis",
        "name": {
            "uz": "Kiriakos Mitsotakis",
            "ru": "Кириакос Мицотакис",
            "en": "Kyriakos Mitsotakis"
        },
        "country": {
            "uz": "Gretsiya",
            "ru": "Греция",
            "en": "Greece"
        },
        "role": {
            "uz": "Gretsiya Bosh vaziri (2019-yildan)",
            "ru": "Премьер-министр Греции (с 2019)",
            "en": "Prime Minister of Greece (since 2019)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Kyriakos_Mitsotakis_2026.jpg/640px-Kyriakos_Mitsotakis_2026.jpg",
        "aliases": [
            "kyriakos mitsotakis",
            "mitsotakis",
            "мицотакис",
            "кириакос мицотакис"
        ],
        "fun_fact": {
            "uz": "Garvard bitiruvchisi bo'lib, chuqur iqtisodiy inqirozdan so'ng Gretsiya iqtisodiyotini jadal tiklashga muvaffaq bo'ldi.",
            "ru": "Выпускник Гарварда, добившийся быстрого восстановления греческой экономики после долгового кризиса.",
            "en": "Harvard-educated leader who presided over Greece's strong post-debt-crisis economic revival."
        }
    },
    {
        "id": "alexander_stubb",
        "name": {
            "uz": "Aleksandr Stubb",
            "ru": "Александр Стубб",
            "en": "Alexander Stubb"
        },
        "country": {
            "uz": "Finlandiya",
            "ru": "Финляндия",
            "en": "Finland"
        },
        "role": {
            "uz": "Finlandiya Prezidenti (2024-yildan)",
            "ru": "Президент Финляндии (с 2024)",
            "en": "President of Finland (since 2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Finnish_President_Alexander_Stubb_arrives_to_the_South_Portico_of_the_White_House_for_a_meeting_with_President_Donald_Trump_%2854732037329%29_%28cropped_2%29.jpg/640px-Finnish_President_Alexander_Stubb_arrives_to_the_South_Portico_of_the_White_House_for_a_meeting_with_President_Donald_Trump_%2854732037329%29_%28cropped_2%29.jpg",
        "aliases": [
            "alexander stubb",
            "stubb",
            "стубб",
            "александр стубб"
        ],
        "fun_fact": {
            "uz": "Finlandiya NATOga qo'shilganidan keyin saylangan birinchi prezident bo'lib, poliatlet-triatlonchi hamdir.",
            "ru": "Первый президент Финляндии после вступления страны в НАТО, страстный триатлонист.",
            "en": "Elected President of Finland following the country's historic accession to NATO; an avid Ironman triathlete."
        }
    },
    {
        "id": "sanna_marin",
        "name": {
            "uz": "Sanna Marin",
            "ru": "Санна Марин",
            "en": "Sanna Marin"
        },
        "country": {
            "uz": "Finlandiya",
            "ru": "Финляндия",
            "en": "Finland"
        },
        "role": {
            "uz": "Finlandiya Bosh vaziri (2019–2023)",
            "ru": "Премьер-министр Финляндии (2019–2023)",
            "en": "Prime Minister of Finland (2019–2023)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/SannaMarin-byPhilipRomano.jpg/640px-SannaMarin-byPhilipRomano.jpg",
        "aliases": [
            "sanna marin",
            "marin",
            "марин",
            "санна марин"
        ],
        "fun_fact": {
            "uz": "34 yoshida lavozimga kirishib, o'sha paytda dunyodagi eng yosh amaldagi bosh vazir bo'lgan.",
            "ru": "Вступила в должность в возрасте 34 лет, став самым молодым действующим премьер-министром в мире.",
            "en": "Became the world's youngest serving prime minister when taking office in 2019 at age 34, guiding Finland toward NATO."
        }
    },
    {
        "id": "mark_rutte",
        "name": {
            "uz": "Mark Ryutte",
            "ru": "Марк Рютте",
            "en": "Mark Rutte"
        },
        "country": {
            "uz": "Niderlandiya",
            "ru": "Нидерланды",
            "en": "Netherlands"
        },
        "role": {
            "uz": "Niderlandiya Bosh vaziri (2010–2024), NATO Bosh kotibi",
            "ru": "Премьер-министр Нидерландов (2010–2024), Генсек НАТО",
            "en": "Prime Minister of the Netherlands, NATO Secretary General"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Mark_Rutte_NATO_Secretary_General_2026_%28cropped%29.jpg/640px-Mark_Rutte_NATO_Secretary_General_2026_%28cropped%29.jpg",
        "aliases": [
            "mark rutte",
            "rutte",
            "ryutte",
            "рютте",
            "марк рютте"
        ],
        "fun_fact": {
            "uz": "Niderlandiya tarixida eng uzoq bosh vazirlik qilgan va ishga velosipedda qatnashi bilan tanilgan.",
            "ru": "Самый долгоправящий премьер в истории Нидерландов, часто ездивший на работу на велосипеде; ныне генсек НАТО.",
            "en": "Longest-serving Dutch prime minister, famed for cycling to work, who went on to become NATO Secretary General."
        }
    },
    {
        "id": "ursula_von_der_leyen",
        "name": {
            "uz": "Ursula fon der Lyayen",
            "ru": "Урсула фон дер Ляйен",
            "en": "Ursula von der Leyen"
        },
        "country": {
            "uz": "Yevropa Ittifoqi / Germaniya",
            "ru": "Европейский союз / Германия",
            "en": "European Union / Germany"
        },
        "role": {
            "uz": "Yevropa Komissiyasi Prezidenti (2019-yildan)",
            "ru": "Председатель Европейской комиссии (с 2019)",
            "en": "President of the European Commission (since 2019)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Ursula_von_der_Leyen_2024.jpg/640px-Ursula_von_der_Leyen_2024.jpg",
        "aliases": [
            "ursula von der leyen",
            "von der leyen",
            "фон дер ляйен",
            "урсула фон дер ляйен"
        ],
        "fun_fact": {
            "uz": "Yevropa Komissiyasini boshqargan birinchi ayol rahbar bo'lib, Yevropa Yashil bitimini ilgari surgan.",
            "ru": "Первая женщина во главе Европейской комиссии, инициировала масштабный «Европейский зеленый курс».",
            "en": "The first woman to serve as President of the European Commission, leading the European Green Deal."
        }
    },
    {
        "id": "vaclav_havel",
        "name": {
            "uz": "Vatslav Gavel",
            "ru": "Вацлав Гавел",
            "en": "Václav Havel"
        },
        "country": {
            "uz": "Chexiya",
            "ru": "Чехия",
            "en": "Czech Republic"
        },
        "role": {
            "uz": "Chexoslovakiya va Chexiya Prezidenti (1989–2003)",
            "ru": "Президент Чехословакии и Чехии (1989–2003)",
            "en": "President of Czechoslovakia and Czech Republic"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Vaclav_Havel.jpg/640px-Vaclav_Havel.jpg",
        "aliases": [
            "vaclav havel",
            "havel",
            "гавел",
            "вацлав гавел",
            "vatslav gavel"
        ],
        "fun_fact": {
            "uz": "Mashhur dramaturg va dissident bo'lib, 1989-yilgi 'Baxmal inqilobi'ga rahbarlik qilib prezident bo'lgan.",
            "ru": "Выдающийся драматург и диссидент, лидер «Бархатной революции» 1989 года в Чехословакии.",
            "en": "Playwright, essayist, and dissident who led the 1989 Velvet Revolution to become Czechoslovakia's first post-communist president."
        }
    },
    {
        "id": "petr_pavel",
        "name": {
            "uz": "Petr Pavel",
            "ru": "Петр Павел",
            "en": "Petr Pavel"
        },
        "country": {
            "uz": "Chexiya",
            "ru": "Чехия",
            "en": "Czech Republic"
        },
        "role": {
            "uz": "Chexiya Prezidenti (2023-yildan)",
            "ru": "Президент Чехии (с 2023)",
            "en": "President of the Czech Republic (since 2023)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Petr_Pavel.jpg/640px-Petr_Pavel.jpg",
        "aliases": [
            "petr pavel",
            "pavel",
            "павел",
            "петр павел"
        ],
        "fun_fact": {
            "uz": "Sobiq armiya generali va NATO Harbiy qo'mitasining birinchi Sharqiy Yevropalik raisi bo'lgan.",
            "ru": "Бывший генерал армии и первый представитель восточноевропейских стран во главе Военного комитета НАТО.",
            "en": "Former army general who served as Chairman of the NATO Military Committee before being elected president in 2023."
        }
    },
    {
        "id": "aleksandar_vucic",
        "name": {
            "uz": "Aleksandr Vuchich",
            "ru": "Александр Вучич",
            "en": "Aleksandar Vučić"
        },
        "country": {
            "uz": "Serbiya",
            "ru": "Сербия",
            "en": "Serbia"
        },
        "role": {
            "uz": "Serbiya Prezidenti (2017-yildan)",
            "ru": "Президент Сербии (с 2017)",
            "en": "President of Serbia (since 2017)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Aleksandar_Vu%C4%8Di%C4%87_2025_%28cropped%29.jpg/640px-Aleksandar_Vu%C4%8Di%C4%87_2025_%28cropped%29.jpg",
        "aliases": [
            "aleksandar vucic",
            "vucic",
            "вучич",
            "александр вучич",
            "aleksandr vuchich"
        ],
        "fun_fact": {
            "uz": "Serbiyani Yevropa Ittifoqiga integratsiya qilish hamda Sharq va G'arb o'rtasida muvozanatli tashqi siyosat yurgizishga intilayotgan rahbar.",
            "ru": "Проводит многовекторную политику балансирования между Европейским союзом, Россией и Китаем.",
            "en": "Pursues a delicate balancing policy between the European Union, Russia, and China for Serbia."
        }
    },
    {
        "id": "xi_jinping",
        "name": {
            "uz": "Si Szinpin",
            "ru": "Си Цзиньпин",
            "en": "Xi Jinping"
        },
        "country": {
            "uz": "Xitoy",
            "ru": "Китай",
            "en": "China"
        },
        "role": {
            "uz": "Xitoy Xalq Respublikasi Raisi (2013-yildan)",
            "ru": "Председатель КНР (с 2013)",
            "en": "President of China, General Secretary of the CCP"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Prime_Minister_Keir_Starmer_visits_China_%2855066713683%29_%28cropped%2Bangle%29.jpg/640px-Prime_Minister_Keir_Starmer_visits_China_%2855066713683%29_%28cropped%2Bangle%29.jpg",
        "aliases": [
            "xi jinping",
            "xi",
            "si szinpin",
            "си цзиньпин",
            "си"
        ],
        "fun_fact": {
            "uz": "'Bir makon, bir yo'l' global tashabbusini e'lon qilgan va Xitoyning global nufuzini keskin oshirgan.",
            "ru": "Инициировал глобальный мегапроект «Один пояс — один путь» и провозгласил «Китайскую мечту».",
            "en": "Spearheaded the global Belt and Road Initiative and consolidated China's status as a superpower."
        }
    },
    {
        "id": "hu_jintao",
        "name": {
            "uz": "Xu Szintao",
            "ru": "Ху Цзиньтао",
            "en": "Hu Jintao"
        },
        "country": {
            "uz": "Xitoy",
            "ru": "Китай",
            "en": "China"
        },
        "role": {
            "uz": "Xitoy Xalq Respublikasi Raisi (2003–2013)",
            "ru": "Председатель КНР (2003–2013)",
            "en": "President of China (2003–2013)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Chinese_President_Hu_Jintao_in_2011.jpg/640px-Chinese_President_Hu_Jintao_in_2011.jpg",
        "aliases": [
            "hu jintao",
            "ху цзиньтао",
            "xu szintao"
        ],
        "fun_fact": {
            "uz": "Uning davrida Pekinda 2008-yilgi Yozgi Olimpiya o'yinlari o'tkazilgan va Xitoy iqtisodiyoti jahonda 2-o'ringa chiqqan.",
            "ru": "В годы его правления Китай успешно провел Олимпиаду-2008 в Пекине и стал второй экономикой мира.",
            "en": "Presided over an era of consistent double-digit economic growth and the celebrated 2008 Beijing Olympics."
        }
    },
    {
        "id": "jiang_zemin",
        "name": {
            "uz": "Szyan Szemin",
            "ru": "Цзян Цзэминь",
            "en": "Jiang Zemin"
        },
        "country": {
            "uz": "Xitoy",
            "ru": "Китай",
            "en": "China"
        },
        "role": {
            "uz": "Xitoy Xalq Respublikasi Raisi (1993–2003)",
            "ru": "Председатель КНР (1993–2003)",
            "en": "President of China (1993–2003)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/President_Jiang_Zemin_2002.png/640px-President_Jiang_Zemin_2002.png",
        "aliases": [
            "jiang zemin",
            "цзян цзэминь",
            "szyan szemin"
        ],
        "fun_fact": {
            "uz": "Gonkong va Makaoning Xitoyga tinch yo'l bilan qaytarilishiga boshchilik qilgan va Xitoyni JSTga kiritgan.",
            "ru": "При нем состоялось возвращение Гонконга и Макао под суверенитет КНР, а также вступление Китая в ВТО.",
            "en": "Oversaw the historic handovers of Hong Kong and Macau and guided China into the World Trade Organization."
        }
    },
    {
        "id": "deng_xiaoping",
        "name": {
            "uz": "Den Syaopin",
            "ru": "Дэн Сяопин",
            "en": "Deng Xiaoping"
        },
        "country": {
            "uz": "Xitoy",
            "ru": "Китай",
            "en": "China"
        },
        "role": {
            "uz": "Xitoyning Bosh arxitektori va islohotchisi (1978–1989)",
            "ru": "Главный архитектор китайских экономических реформ",
            "en": "Paramount Leader of China (1978–1989)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Deng_Xiaoping_at_the_arrival_ceremony_for_the_Vice_Premier_of_China_%28cropped%29.jpg/640px-Deng_Xiaoping_at_the_arrival_ceremony_for_the_Vice_Premier_of_China_%28cropped%29.jpg",
        "aliases": [
            "deng xiaoping",
            "дэн сяопин",
            "den syaopin"
        ],
        "fun_fact": {
            "uz": "'Islohotlar va ochiqlik' siyosati orqali zamonaviy Xitoy iqtisodiy mo''jizasiga poydevor qo'ygan.",
            "ru": "Создатель китайского «социализма с китайской спецификой», превративший бедную страну в мировую фабрику.",
            "en": "The architect of modern China's economic reforms and opening-up policy, lifting hundreds of millions out of poverty."
        }
    },
    {
        "id": "mao_zedong",
        "name": {
            "uz": "Mao Szedun",
            "ru": "Мао Цзэдун",
            "en": "Mao Zedong"
        },
        "country": {
            "uz": "Xitoy",
            "ru": "Китай",
            "en": "China"
        },
        "role": {
            "uz": "Xitoy Xalq Respublikasining Asoschisi (1949–1976)",
            "ru": "Основатель Китайской Народной Республики",
            "en": "Founding Father of the People's Republic of China"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Mao_Zedong_1950_Portrait_%283x4_cropped%29%282%29.jpg/640px-Mao_Zedong_1950_Portrait_%283x4_cropped%29%282%29.jpg",
        "aliases": [
            "mao zedong",
            "mao",
            "мао цзэдун",
            "мао"
        ],
        "fun_fact": {
            "uz": "1949-yilda Pekinda Tyanyanmen maydonida Xitoy Xalq Respublikasi tuzilganini e'lon qilgan.",
            "ru": "1 октября 1949 года провозгласил создание Китайской Народной Республики на площади Тяньаньмэнь.",
            "en": "Proclaimed the establishment of the People's Republic of China on Tiananmen Square on October 1, 1949."
        }
    },
    {
        "id": "narendra_modi",
        "name": {
            "uz": "Narendra Modi",
            "ru": "Нарендра Моди",
            "en": "Narendra Modi"
        },
        "country": {
            "uz": "Hindiston",
            "ru": "Индия",
            "en": "India"
        },
        "role": {
            "uz": "Hindiston Bosh vaziri (2014-yildan)",
            "ru": "Премьер-министр Индии (с 2014)",
            "en": "Prime Minister of India (since 2014)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Narendra_Modi_Portrait_2026.jpg/640px-Narendra_Modi_Portrait_2026.jpg",
        "aliases": [
            "narendra modi",
            "modi",
            "моди",
            "нарендра моди"
        ],
        "fun_fact": {
            "uz": "'Make in India' va 'Digital India' loyihalarini yo'lga qo'yib, Hindistonni dunyoning eng yirik iqtisodiyotlaridan biriga aylantirdi.",
            "ru": "Запустил масштабные программы модернизации 'Make in India' и цифровизации 'Digital India'.",
            "en": "Launched the 'Make in India' and 'Digital India' initiatives, transforming India into the world's fifth-largest economy."
        }
    },
    {
        "id": "manmohan_singh",
        "name": {
            "uz": "Manmoxan Singx",
            "ru": "Манмохан Сингх",
            "en": "Manmohan Singh"
        },
        "country": {
            "uz": "Hindiston",
            "ru": "Индия",
            "en": "India"
        },
        "role": {
            "uz": "Hindiston Bosh vaziri (2004–2014)",
            "ru": "Премьер-министр Индии (2004–2014)",
            "en": "Prime Minister of India (2004–2014)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Official_Portrait_of_the_Prime_Minister_Dr._Manmohan_Singh_%283x4_cropped%29.jpg/640px-Official_Portrait_of_the_Prime_Minister_Dr._Manmohan_Singh_%283x4_cropped%29.jpg",
        "aliases": [
            "manmohan singh",
            "singh",
            "сингх",
            "манмохан сингх"
        ],
        "fun_fact": {
            "uz": "Oksford universitetini bitirgan iqtisodchi bo'lib, 1991-yilda Hindiston bozor iqtisodiyotini erkinlashtirishga asos solgan.",
            "ru": "Выдающийся экономист, архитектор индийских рыночных реформ 1991 года, открывших страну миру.",
            "en": "Renowned economist and former central bank governor who liberalized the Indian economy in 1991."
        }
    },
    {
        "id": "indira_gandhi",
        "name": {
            "uz": "Indira Gandi",
            "ru": "Индира Ганди",
            "en": "Indira Gandhi"
        },
        "country": {
            "uz": "Hindiston",
            "ru": "Индия",
            "en": "India"
        },
        "role": {
            "uz": "Hindiston Bosh vaziri (1966–1977, 1980–1984)",
            "ru": "Премьер-министр Индии",
            "en": "Prime Minister of India (first female)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Indira_Gandhi_official_portrait.png/640px-Indira_Gandhi_official_portrait.png",
        "aliases": [
            "indira gandhi",
            "gandhi",
            "gandi",
            "ганди",
            "индира ганди"
        ],
        "fun_fact": {
            "uz": "Hindistonning birinchi va yagona ayol bosh vaziri bo'lib, 1971-yilda Bangladesh mustaqillikka erishishiga yordam bergan.",
            "ru": "Первая и единственная женщина премьер-министр в истории Индии, дочь Джавахарлала Неру.",
            "en": "India's first and only female prime minister, leading India during the 1971 war that established Bangladesh."
        }
    },
    {
        "id": "jawaharlal_nehru",
        "name": {
            "uz": "Javoharla'l Neru",
            "ru": "Джавахарлал Неру",
            "en": "Jawaharlal Nehru"
        },
        "country": {
            "uz": "Hindiston",
            "ru": "Индия",
            "en": "India"
        },
        "role": {
            "uz": "Mustaqil Hindistonning Birinchi Bosh vaziri (1947–1964)",
            "ru": "Первый Премьер-министр независимой Индии",
            "en": "First Prime Minister of India (1947–1964)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Nehru_in_the_Netherlands%2C_1957.jpg/640px-Nehru_in_the_Netherlands%2C_1957.jpg",
        "aliases": [
            "jawaharlal nehru",
            "nehru",
            "neru",
            "неру",
            "джавахарлал неру"
        ],
        "fun_fact": {
            "uz": "Mahatma Gandining eng yaqin safdoshi bo'lib, Qo'shilmaslik harakatining asoschilaridan biri.",
            "ru": "Ближайший соратник Махатмы Ганди, один из основателей Движения неприсоединения.",
            "en": "Central figure in Indian independence and co-founder of the Non-Aligned Movement during the Cold War."
        }
    },
    {
        "id": "a_p_j_abdul_kalam",
        "name": {
            "uz": "A. P. J. Abdul Kalom",
            "ru": "А. П. Дж. Абдул Калам",
            "en": "A. P. J. Abdul Kalam"
        },
        "country": {
            "uz": "Hindiston",
            "ru": "Индия",
            "en": "India"
        },
        "role": {
            "uz": "Hindiston Prezidenti (2002–2007), 'Raketachi odam'",
            "ru": "Президент Индии (2002–2007), «Ракетный человек»",
            "en": "President of India (2002–2007), 'Missile Man'"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/A._P._J._Abdul_Kalam.jpg/640px-A._P._J._Abdul_Kalam.jpg",
        "aliases": [
            "abdul kalam",
            "kalam",
            "калам",
            "абдул калам",
            "a p j abdul kalam"
        ],
        "fun_fact": {
            "uz": "Hindistonning kosmik va raketa dasturlari yetakchi olimi bo'lib, xalq orasida 'Xalq Prezidenti' deb ardoqlangan.",
            "ru": "Выдающийся ученый-аэрокосмик, создатель индийских баллистических ракет, прозван «Народным президентом».",
            "en": "Beloved aerospace scientist known as the 'Missile Man of India' who served with distinction as President."
        }
    },
    {
        "id": "shigeru_ishiba",
        "name": {
            "uz": "Sigeru Isiba",
            "ru": "Сигэру Исиба",
            "en": "Shigeru Ishiba"
        },
        "country": {
            "uz": "Yaponiya",
            "ru": "Япония",
            "en": "Japan"
        },
        "role": {
            "uz": "Yaponiya Bosh vaziri (2024-yildan)",
            "ru": "Премьер-министр Японии (с 2024)",
            "en": "Prime Minister of Japan (since 2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Ishiba_Shigeru_20241001_%28cropped%29.jpg/640px-Ishiba_Shigeru_20241001_%28cropped%29.jpg",
        "aliases": [
            "shigeru ishiba",
            "ishiba",
            "isiba",
            "исиба",
            "сигэру исиба"
        ],
        "fun_fact": {
            "uz": "Yaponiya mudofaa siyosatining yetakchi mutaxassisi bo'lib, qishloq hududlarini rivojlantirish dasturini ilgari surgan.",
            "ru": "Эксперт по вопросам национальной обороны и регионального возрождения Японии.",
            "en": "Defense expert and longtime political veteran who became Prime Minister of Japan in October 2024."
        }
    },
    {
        "id": "shinzo_abe",
        "name": {
            "uz": "Sindzo Abe",
            "ru": "Синдзо Абэ",
            "en": "Shinzo Abe"
        },
        "country": {
            "uz": "Yaponiya",
            "ru": "Япония",
            "en": "Japan"
        },
        "role": {
            "uz": "Yaponiya Bosh vaziri (2006–2007, 2012–2020)",
            "ru": "Премьер-министр Японии",
            "en": "Prime Minister of Japan (longest-serving)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Shinz%C5%8D_Abe_20120501.jpg/640px-Shinz%C5%8D_Abe_20120501.jpg",
        "aliases": [
            "shinzo abe",
            "abe",
            "абэ",
            "синдзо абэ"
        ],
        "fun_fact": {
            "uz": "Yaponiya tarixida eng uzoq muddat xizmat qilgan bosh vazir bo'lib, 'Abenomika' iqtisodiy islohotlarini o'tkazgan.",
            "ru": "Рекордсмен по продолжительности пребывания на посту премьер-министра Японии, автор «абэномики».",
            "en": "Japan's longest-serving prime minister, famed for his signature 'Abenomics' economic revitalization strategy."
        }
    },
    {
        "id": "yoon_suk_yeol",
        "name": {
            "uz": "Yun Sok Yol",
            "ru": "Юн Сок Ёль",
            "en": "Yoon Suk Yeol"
        },
        "country": {
            "uz": "Janubiy Koreya",
            "ru": "Южная Корея",
            "en": "South Korea"
        },
        "role": {
            "uz": "Janubiy Koreya Prezidenti (2022-yildan)",
            "ru": "Президент Республики Корея (с 2022)",
            "en": "President of South Korea (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/South_Korea_President_Yoon_Suk_Yeol_portrait_%28crop%29.jpg/640px-South_Korea_President_Yoon_Suk_Yeol_portrait_%28crop%29.jpg",
        "aliases": [
            "yoon suk yeol",
            "yoon",
            "юн сок ёль",
            "yun sok yol"
        ],
        "fun_fact": {
            "uz": "Sobiq Bosh prokuror bo'lib, siyosatga to'g'ridan-to'g'ri sud-huquq sohasidan kirib kelgan va prezidentlikka saylangan.",
            "ru": "Бывший генеральный прокурор Южной Кореи, перенесший официальную резиденцию из «Голубого дома».",
            "en": "Former prosecutor general who won the presidency and relocated the executive office away from the Blue House."
        }
    },
    {
        "id": "moon_jae_in",
        "name": {
            "uz": "Mun Chje In",
            "ru": "Мун Чжэ Ин",
            "en": "Moon Jae-in"
        },
        "country": {
            "uz": "Janubiy Koreya",
            "ru": "Южная Корея",
            "en": "South Korea"
        },
        "role": {
            "uz": "Janubiy Koreya Prezidenti (2017–2022)",
            "ru": "Президент Республики Корея (2017–2022)",
            "en": "President of South Korea (2017–2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/President_Moon_Jae_In.jpg/640px-President_Moon_Jae_In.jpg",
        "aliases": [
            "moon jae-in",
            "moon jae in",
            "мун чжэ ин",
            "mun chje in"
        ],
        "fun_fact": {
            "uz": "Inson huquqlari himoyachisi bo'lib, Shimoliy Koreya bilan sammitlar o'tkazib munosabatlarni iliqlashtirishga uringan.",
            "ru": "Организовал исторические межкорейские саммиты и встречу Дональда Трампа с Ким Чен Ыном в Пханмунчжоме.",
            "en": "Human rights attorney who brokered unprecedented inter-Korean summits and peace talks at Panmunjom."
        }
    },
    {
        "id": "park_geun_hye",
        "name": {
            "uz": "Pak Kin Xe",
            "ru": "Пак Кын Хе",
            "en": "Park Geun-hye"
        },
        "country": {
            "uz": "Janubiy Koreya",
            "ru": "Южная Корея",
            "en": "South Korea"
        },
        "role": {
            "uz": "Janubiy Koreya Prezidenti (2013–2017)",
            "ru": "Президент Республики Корея (2013–2017)",
            "en": "President of South Korea (2013–2017)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Park_Geun-hye_presidential_portrait.png/640px-Park_Geun-hye_presidential_portrait.png",
        "aliases": [
            "park geun-hye",
            "park geun hye",
            "пак кын хе",
            "pak kin xe"
        ],
        "fun_fact": {
            "uz": "Janubiy Koreya va butun Sharqiy Osiyo tarixidagi birinchi saylangan ayol davlat rahbari bo'lgan.",
            "ru": "Первая женщина-президент в истории Южной Кореи и Восточной Азии, дочь генерала Пак Чон Хи.",
            "en": "The first female president of South Korea and the first elected female head of state in East Asia."
        }
    },
    {
        "id": "kim_jong_un",
        "name": {
            "uz": "Kim Chen In",
            "ru": "Ким Чен Ын",
            "en": "Kim Jong Un"
        },
        "country": {
            "uz": "Shimoliy Koreya",
            "ru": "Северная Корея",
            "en": "North Korea"
        },
        "role": {
            "uz": "KXDR Oliy yetakchisi (2011-yildan)",
            "ru": "Высший руководитель КНДР (с 2011)",
            "en": "Supreme Leader of North Korea (since 2011)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Kim_Jong-un_and_Vladimir_Putin_%282023-09-13%29_12_%28cropped_2%29.jpg/640px-Kim_Jong-un_and_Vladimir_Putin_%282023-09-13%29_12_%28cropped_2%29.jpg",
        "aliases": [
            "kim jong un",
            "ким чен ын",
            "kim chen in"
        ],
        "fun_fact": {
            "uz": "Kim sulolasining uchinchi avlod rahbari bo'lib, 2018-yilda AQSH prezidenti bilan birinchi marotaba sammitda uchrashgan.",
            "ru": "Третий представитель династии Кимов, первый лидер КНДР, встретившийся с действующим президентом США.",
            "en": "Third-generation supreme leader of North Korea who held historic summits with US President Donald Trump in 2018–2019."
        }
    },
    {
        "id": "kim_il_sung",
        "name": {
            "uz": "Kim Ir Sen",
            "ru": "Ким Ир Сен",
            "en": "Kim Il Sung"
        },
        "country": {
            "uz": "Shimoliy Koreya",
            "ru": "Северная Корея",
            "en": "North Korea"
        },
        "role": {
            "uz": "KXDR Asoschisi va 'Mangu Prezidenti'",
            "ru": "Основатель и «Вечный президент» КНДР",
            "en": "Founder and Eternal President of North Korea"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Kim_Il-sung_in_1950_%28cropped%29.jpg/640px-Kim_Il-sung_in_1950_%28cropped%29.jpg",
        "aliases": [
            "kim il sung",
            "ким ир сен",
            "kim ir sen"
        ],
        "fun_fact": {
            "uz": "Chuchxe mafkurasiga asos solgan va vafotidan so'ng ham mamlakatning 'Mangu Prezidenti' deb e'lon qilingan.",
            "ru": "Создатель государственной идеологии Чучхе, посмертно наделен конституционным статусом «Вечного президента».",
            "en": "Formulated the state ideology of Juche and was designated posthumously as North Korea's 'Eternal President'."
        }
    },
    {
        "id": "joko_widodo",
        "name": {
            "uz": "Joko Vidodo",
            "ru": "Джоко Видодо",
            "en": "Joko Widodo"
        },
        "country": {
            "uz": "Indoneziya",
            "ru": "Индонезия",
            "en": "Indonesia"
        },
        "role": {
            "uz": "Indoneziya Prezidenti (2014–2024)",
            "ru": "Президент Индонезии (2014–2024)",
            "en": "President of Indonesia (2014–2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Joko_Widodo_2019_official_portrait.jpg/640px-Joko_Widodo_2019_official_portrait.jpg",
        "aliases": [
            "joko widodo",
            "jokowi",
            "джокови",
            "джоко видодо"
        ],
        "fun_fact": {
            "uz": "Xalq orasida 'Jokovi' nomi bilan mashhur bo'lib, Indoneziya yangi poytaxti Nusantarani qurishni boshlagan.",
            "ru": "Широко известен как Джокови, инициировал перенос столицы Индонезии из Джакарты в новый город Нусантара.",
            "en": "Popularly known as Jokowi, he launched the megaproject to relocate Indonesia's capital from Jakarta to Nusantara."
        }
    },
    {
        "id": "prabowo_subianto",
        "name": {
            "uz": "Prabovo Subianto",
            "ru": "Прабово Субианто",
            "en": "Prabowo Subianto"
        },
        "country": {
            "uz": "Indoneziya",
            "ru": "Индонезия",
            "en": "Indonesia"
        },
        "role": {
            "uz": "Indoneziya Prezidenti (2024-yildan)",
            "ru": "Президент Индонезии (с 2024)",
            "en": "President of Indonesia (since 2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Prabowo_Subianto_2024_official_portrait.jpg/640px-Prabowo_Subianto_2024_official_portrait.jpg",
        "aliases": [
            "prabowo subianto",
            "prabowo",
            "прабово субианто",
            "prabovo subianto"
        ],
        "fun_fact": {
            "uz": "Sobiq general va mudofaa vaziri bo'lib, 2024-yilda dunyoning 4-eng yirik aholiga ega davlatiga prezident etib saylangan.",
            "ru": "Бывший генерал спецназа и министр обороны, одержавший победу на выборах президента Индонезии в 2024 году.",
            "en": "Former special forces general and defense minister who assumed the presidency of Indonesia in October 2024."
        }
    },
    {
        "id": "sukarno",
        "name": {
            "uz": "Sukarno",
            "ru": "Сукарно",
            "en": "Sukarno"
        },
        "country": {
            "uz": "Indoneziya",
            "ru": "Индонезия",
            "en": "Indonesia"
        },
        "role": {
            "uz": "Indoneziyaning Birinchi Prezidenti (1945–1967)",
            "ru": "Первый Президент Индонезии (1945–1967)",
            "en": "First President of Indonesia (1945–1967)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Presiden_Sukarno.jpg/640px-Presiden_Sukarno.jpg",
        "aliases": [
            "sukarno",
            "сукарно"
        ],
        "fun_fact": {
            "uz": "1945-yilda Indoneziya mustaqilligini e'lon qilgan va 1955-yilgi tarixiy Bandung konferensiyasiga mezbonlik qilgan.",
            "ru": "Провозгласил независимость Индонезии в 1945 году, лидер исторической Бандунгской конференции 1955 года.",
            "en": "Proclaimed Indonesian independence in 1945 and hosted the historic 1955 Asian-African Bandung Conference."
        }
    },
    {
        "id": "lee_kuan_yew",
        "name": {
            "uz": "Li Kuan Yu",
            "ru": "Ли Куан Ю",
            "en": "Lee Kuan Yew"
        },
        "country": {
            "uz": "Singapur",
            "ru": "Сингапур",
            "en": "Singapore"
        },
        "role": {
            "uz": "Singapur Asoschisi va Bosh vaziri (1959–1990)",
            "ru": "Основатель и первый Премьер-министр Сингапура",
            "en": "Founding Father and First Prime Minister of Singapore"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Prime_Minister_Lee_Kuan_Yew_of_Singapore_Making_a_Toast_at_a_State_Dinner_Held_in_His_Honor%2C_1975.jpg/640px-Prime_Minister_Lee_Kuan_Yew_of_Singapore_Making_a_Toast_at_a_State_Dinner_Held_in_His_Honor%2C_1975.jpg",
        "aliases": [
            "lee kuan yew",
            "ли куан ю",
            "li kuan yu"
        ],
        "fun_fact": {
            "uz": "Tabiiy resurslarsiz kichik orol-davlatni uchinchi dunyo mamlakatidan dunyoning eng boy markazlaridan biriga aylantirgan.",
            "ru": "Превратил бедную колонию без природных ресурсов в один из самых процветающих финансовых центров планеты.",
            "en": "Architect of Singapore's transformation 'from third world to first' within a single generation."
        }
    },
    {
        "id": "mahathir_mohamad",
        "name": {
            "uz": "Maxatxir Moxamad",
            "ru": "Махатхир Мохамад",
            "en": "Mahathir Mohamad"
        },
        "country": {
            "uz": "Malayziya",
            "ru": "Малайзия",
            "en": "Malaysia"
        },
        "role": {
            "uz": "Malayziya Bosh vaziri (1981–2003, 2018–2020)",
            "ru": "Премьер-министр Малайзии",
            "en": "Prime Minister of Malaysia"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Mahathir_Mohamad_13112018_%28cropped%29.jpg/640px-Mahathir_Mohamad_13112018_%28cropped%29.jpg",
        "aliases": [
            "mahathir mohamad",
            "mahathir",
            "махатхир",
            "махатхир мохамад",
            "maxatxir moxamad"
        ],
        "fun_fact": {
            "uz": "Malayziyani zamonaviy sanoatlashgan davlatga aylantirgan va 92 yoshida yana bosh vazirlik lavozimiga qaytgan.",
            "ru": "Модернизатор Малайзии, вернулся на пост премьер-министра в возрасте 92 лет, став старейшим лидером в мире.",
            "en": "Modernized Malaysia and became the world's oldest sitting prime minister when re-elected at age 92 in 2018."
        }
    },
    {
        "id": "ferdinand_marcos_jr",
        "name": {
            "uz": "Ferdinand Markos (kichik)",
            "ru": "Фердинанд Маркос-младший",
            "en": "Ferdinand Marcos Jr."
        },
        "country": {
            "uz": "Filippin",
            "ru": "Филиппины",
            "en": "Philippines"
        },
        "role": {
            "uz": "Filippin Prezidenti (2022-yildan)",
            "ru": "Президент Филиппин (с 2022)",
            "en": "President of the Philippines (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Portrait_of_President_Ferdinand_R._Marcos%2C_Jr_%28cropped2%29.jpg/640px-Portrait_of_President_Ferdinand_R._Marcos%2C_Jr_%28cropped2%29.jpg",
        "aliases": [
            "ferdinand marcos jr",
            "bongbong marcos",
            "маркос",
            "фердинанд маркос младший"
        ],
        "fun_fact": {
            "uz": "Odatda 'Bongbong' nomi bilan tanilgan bo'lib, sobiq prezident Ferdinand Markosning o'g'lidir.",
            "ru": "Широко известен как Бонгбонг Маркос, сын бывшего филиппинского лидера Фердинанда Маркоса.",
            "en": "Commonly known as 'Bongbong', he is the son of former president Ferdinand Marcos and won a landslide victory in 2022."
        }
    },
    {
        "id": "rodrigo_duterte",
        "name": {
            "uz": "Rodrigo Duterte",
            "ru": "Родриго Дутерте",
            "en": "Rodrigo Duterte"
        },
        "country": {
            "uz": "Filippin",
            "ru": "Филиппины",
            "en": "Philippines"
        },
        "role": {
            "uz": "Filippin Prezidenti (2016–2022)",
            "ru": "Президент Филиппин (2016–2022)",
            "en": "President of the Philippines (2016–2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/President_Rodrigo_Duterte_portrait_%28cropped%29.jpg/640px-President_Rodrigo_Duterte_portrait_%28cropped%29.jpg",
        "aliases": [
            "rodrigo duterte",
            "duterte",
            "дутерте",
            "родриго дутерте"
        ],
        "fun_fact": {
            "uz": "Narkotrafikka qarshi favqulodda shafqatsiz kurash olib borgan va Davao shahrining ko'p yillik meri bo'lgan.",
            "ru": "Прославился бескомпромиссной и жесткой войной против наркокартелей на Филиппинах.",
            "en": "Former longtime mayor of Davao City known for his aggressive nationwide crackdown on illegal drugs."
        }
    },
    {
        "id": "corazon_aquino",
        "name": {
            "uz": "Korason Akino",
            "ru": "Корасон Акино",
            "en": "Corazon Aquino"
        },
        "country": {
            "uz": "Filippin",
            "ru": "Филиппины",
            "en": "Philippines"
        },
        "role": {
            "uz": "Filippin Prezidenti (1986–1992)",
            "ru": "Президент Филиппин (1986–1992)",
            "en": "President of the Philippines (1986–1992)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Corazon_Aquino_1986.jpg/640px-Corazon_Aquino_1986.jpg",
        "aliases": [
            "corazon aquino",
            "aquino",
            "акино",
            "корасон акино",
            "cory aquino"
        ],
        "fun_fact": {
            "uz": "1986-yilgi 'Xalq kuchi' tinch inqilobi yetakchisi va Osiyodagi birinchi ayol prezident bo'lgan.",
            "ru": "Лидер мирной «Желтой революции» 1986 года, первая женщина-президент в Азии.",
            "en": "Leader of the 1986 People Power Revolution and the first female president in Asian history."
        }
    },
    {
        "id": "shehbaz_sharif",
        "name": {
            "uz": "Shahboz Sharif",
            "ru": "Шахбаз Шариф",
            "en": "Shehbaz Sharif"
        },
        "country": {
            "uz": "Pokiston",
            "ru": "Пакистан",
            "en": "Pakistan"
        },
        "role": {
            "uz": "Pokiston Bosh vaziri (2022–2023, 2024-yildan)",
            "ru": "Премьер-министр Пакистана (с 2024)",
            "en": "Prime Minister of Pakistan (since 2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Shehbaz_Sharif_2026_portrait.jpg/640px-Shehbaz_Sharif_2026_portrait.jpg",
        "aliases": [
            "shehbaz sharif",
            "sharif",
            "шариф",
            "шахбаз шариф",
            "shahboz sharif"
        ],
        "fun_fact": {
            "uz": "Panjob viloyatining sobiq bosh vaziri va yirik infratuzilma loyihalarining tezkor ijrochisi sifatida tanilgan.",
            "ru": "Известен эффективным управлением провинцией Пенджаб и реализацией инфраструктурных мегапроектов.",
            "en": "Known for his administrative efficiency as Punjab's chief minister, now serving as Pakistan's prime minister."
        }
    },
    {
        "id": "imran_khan",
        "name": {
            "uz": "Imron Xon",
            "ru": "Имран Хан",
            "en": "Imran Khan"
        },
        "country": {
            "uz": "Pokiston",
            "ru": "Пакистан",
            "en": "Pakistan"
        },
        "role": {
            "uz": "Pokiston Bosh vaziri (2018–2022)",
            "ru": "Премьер-министр Пакистана (2018–2022)",
            "en": "Prime Minister of Pakistan (2018–2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Prime_Minister_Imran_Khan_Adresses_the_Forum_01.jpg/640px-Prime_Minister_Imran_Khan_Adresses_the_Forum_01.jpg",
        "aliases": [
            "imran khan",
            "khan",
            "хан",
            "имран хан",
            "imron xon"
        ],
        "fun_fact": {
            "uz": "1992-yilda kriket bo'yicha Pokiston terma jamoasini Jahon kubogi chempioni qilgan afsonaviy sportchi va siyosatchi.",
            "ru": "Легендарный капитан сборной Пакистана по крикету, выигравший Кубок мира 1992 года.",
            "en": "Led Pakistan to cricket World Cup glory in 1992 before founding the PTI party and becoming prime minister."
        }
    },
    {
        "id": "benazir_bhutto",
        "name": {
            "uz": "Benazir Bxutto",
            "ru": "Беназир Бхутто",
            "en": "Benazir Bhutto"
        },
        "country": {
            "uz": "Pokiston",
            "ru": "Пакистан",
            "en": "Pakistan"
        },
        "role": {
            "uz": "Pokiston Bosh vaziri (1988–1990, 1993–1996)",
            "ru": "Премьер-министр Пакистана",
            "en": "Prime Minister of Pakistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Oliver_Mark_-_Benazir_Bhutto%2C_Dubai_2006_%28cropped%29.jpg/640px-Oliver_Mark_-_Benazir_Bhutto%2C_Dubai_2006_%28cropped%29.jpg",
        "aliases": [
            "benazir bhutto",
            "bhutto",
            "бхутто",
            "беназир бхутто",
            "benazir bxutto"
        ],
        "fun_fact": {
            "uz": "Musulmon dunyosi tarixida demokratik yo'l bilan hukumat rahbari etib saylangan birinchi ayol.",
            "ru": "Первая в современной истории женщина, возглавившая правительство в мусульманской стране.",
            "en": "The first woman elected to head a democratic government in a Muslim-majority nation."
        }
    },
    {
        "id": "muhammad_ali_jinnah",
        "name": {
            "uz": "Muhammad Ali Jinna",
            "ru": "Мухаммад Али Джинна",
            "en": "Muhammad Ali Jinnah"
        },
        "country": {
            "uz": "Pokiston",
            "ru": "Пакистан",
            "en": "Pakistan"
        },
        "role": {
            "uz": "Pokiston Asoschisi va 'Qoidi A'zam'",
            "ru": "Основатель Пакистана, Великий лидер",
            "en": "Founder and First Governor-General of Pakistan"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Jinnah1945c.jpg/640px-Jinnah1945c.jpg",
        "aliases": [
            "muhammad ali jinnah",
            "jinnah",
            "джинна",
            "мухаммад али джинна",
            "jinna"
        ],
        "fun_fact": {
            "uz": "Pokistonda rasmiy ravishda 'Qoidi A'zam' (Buyuk Yo'lboshchi) unvoni bilan e'tirof etiladi.",
            "ru": "В Пакистане почитается как «Каид-и-Азам» (Великий вождь) и Отец нации.",
            "en": "Revered as Quaid-i-Azam ('Great Leader') and Baba-i-Qaum ('Father of the Nation') in Pakistan."
        }
    },
    {
        "id": "sheikh_hasina",
        "name": {
            "uz": "Shayx Hasina",
            "ru": "Шейх Хасина",
            "en": "Sheikh Hasina"
        },
        "country": {
            "uz": "Bangladesh",
            "ru": "Бангладеш",
            "en": "Bangladesh"
        },
        "role": {
            "uz": "Bangladesh Bosh vaziri (1996–2001, 2009–2024)",
            "ru": "Премьер-министр Бангладеш (1996–2001, 2009–2024)",
            "en": "Prime Minister of Bangladesh"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Sheikh_Hasina_meets_Editors%27_Guild_Bangladesh_and_Journalists%27_Union_Ganabhaban_2024-01-03_%28PID-0011626%29_%28cropped%29.jpg/640px-Sheikh_Hasina_meets_Editors%27_Guild_Bangladesh_and_Journalists%27_Union_Ganabhaban_2024-01-03_%28PID-0011626%29_%28cropped%29.jpg",
        "aliases": [
            "sheikh hasina",
            "hasina",
            "хасина",
            "шейх хасина"
        ],
        "fun_fact": {
            "uz": "Dunyo tarixida eng uzoq muddat (20 yildan ortiq) hukumatni boshqargan ayol bosh vazir hisoblanadi.",
            "ru": "Самая долгоправящая женщина-премьер-министр в мировой истории, дочь основателя Бангладеш Муджибура Рахмана.",
            "en": "The world's longest-serving female head of government, leading Bangladesh for over 20 combined years."
        }
    },
    {
        "id": "muhammad_yunus",
        "name": {
            "uz": "Muhammad Yunus",
            "ru": "Мухаммад Юнус",
            "en": "Muhammad Yunus"
        },
        "country": {
            "uz": "Bangladesh",
            "ru": "Бангладеш",
            "en": "Bangladesh"
        },
        "role": {
            "uz": "Bangladesh Muvaqqat Hukumati Rahbari (2024-yildan), Nobel mukofoti sohibi",
            "ru": "Глава временного правительства Бангладеш (с 2024)",
            "en": "Chief Adviser of Bangladesh (since 2024), Nobel Laureate"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Muhammad_Yunus_speaking_at_Jamuna_State_Guesthouse%2C_Dhaka_2026-02-16_%28cropped%29.jpg/640px-Muhammad_Yunus_speaking_at_Jamuna_State_Guesthouse%2C_Dhaka_2026-02-16_%28cropped%29.jpg",
        "aliases": [
            "muhammad yunus",
            "yunus",
            "юнус",
            "мухаммад юнус"
        ],
        "fun_fact": {
            "uz": "Mikrokredit va 'Grameen Bank' asoschisi sifatida 2006-yilda Nobel Tinchlik mukofotini olgan iqtisodchi.",
            "ru": "Основатель Grameen Bank и концепции микрокредитования, лауреат Нобелевской премии мира 2006 года.",
            "en": "Social entrepreneur and banker who won the 2006 Nobel Peace Prize for pioneering microcredit with Grameen Bank."
        }
    },
    {
        "id": "benjamin_netanyahu",
        "name": {
            "uz": "Benyamin Netanyaxu",
            "ru": "Биньямин Нетаньяху",
            "en": "Benjamin Netanyahu"
        },
        "country": {
            "uz": "Isroil",
            "ru": "Израиль",
            "en": "Israel"
        },
        "role": {
            "uz": "Isroil Bosh vaziri (1996–1999, 2009–2021, 2022-yildan)",
            "ru": "Премьер-министр Израиля",
            "en": "Prime Minister of Israel (longest-serving)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Benjamin_Netanyahu%2C_February_2023.jpg/640px-Benjamin_Netanyahu%2C_February_2023.jpg",
        "aliases": [
            "benjamin netanyahu",
            "netanyahu",
            "bibi",
            "нетаньяху",
            "биньямин нетаньяху",
            "netanyaxu"
        ],
        "fun_fact": {
            "uz": "Isroil davlati tashkil topganidan so'ng tug'ilgan birinchi bosh vazir va mamlakat tarixidagi eng uzoq hukm surgan rahbar.",
            "ru": "Рекордсмен по продолжительности пребывания на посту премьер-министра в истории Государства Израиль.",
            "en": "The longest-serving prime minister in Israeli history and the first born after the nation's 1948 independence."
        }
    },
    {
        "id": "shimon_peres",
        "name": {
            "uz": "Shimon Peres",
            "ru": "Шимон Перес",
            "en": "Shimon Peres"
        },
        "country": {
            "uz": "Isroil",
            "ru": "Израиль",
            "en": "Israel"
        },
        "role": {
            "uz": "Isroil Prezidenti (2007–2014) va Bosh vaziri",
            "ru": "Президент и Премьер-министр Израиля",
            "en": "President and Prime Minister of Israel"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Shimon_Peres_2010_%28cropped_2%29.jpg/640px-Shimon_Peres_2010_%28cropped_2%29.jpg",
        "aliases": [
            "shimon peres",
            "peres",
            "перес",
            "шимон перес"
        ],
        "fun_fact": {
            "uz": "Oslo tinchlik kelishuvlari uchun Nobel Tinchlik mukofotiga sazovor bo'lgan va deyarli 70 yil davlat arbobi bo'lib ishlagan.",
            "ru": "Лауреат Нобелевской премии мира 1994 года за подписание соглашений в Осло.",
            "en": "Nobel Peace Prize laureate who signed the Oslo Accords and served in nearly every major Israeli cabinet post."
        }
    },
    {
        "id": "golda_meir",
        "name": {
            "uz": "Golda Meir",
            "ru": "Голда Меир",
            "en": "Golda Meir"
        },
        "country": {
            "uz": "Isroil",
            "ru": "Израиль",
            "en": "Israel"
        },
        "role": {
            "uz": "Isroil Bosh vaziri (1969–1974), 'Temir ledi'",
            "ru": "Премьер-министр Израиля (1969–1974)",
            "en": "Prime Minister of Israel (1969–1974)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Golda_Meir_%281964%29_cropped.jpg/640px-Golda_Meir_%281964%29_cropped.jpg",
        "aliases": [
            "golda meir",
            "meir",
            "меир",
            "голда меир"
        ],
        "fun_fact": {
            "uz": "Isroilning birinchi va yagona ayol bosh vaziri bo'lib, 1973-yilgi Yom Kipur urushida mamlakatni boshqargan.",
            "ru": "Первая и единственная женщина на посту премьер-министра Израиля, руководила страной во время Войны Судного дня.",
            "en": "Israel's fourth prime minister and first female head of government, leading through the 1973 Yom Kippur War."
        }
    },
    {
        "id": "masoud_pezeshkian",
        "name": {
            "uz": "Mas'ud Pezeshkiyon",
            "ru": "Масуд Пезешкиан",
            "en": "Masoud Pezeshkian"
        },
        "country": {
            "uz": "Eron",
            "ru": "Иран",
            "en": "Iran"
        },
        "role": {
            "uz": "Eron Islom Respublikasi Prezidenti (2024-yildan)",
            "ru": "Президент Исламской Республики Иран (с 2024)",
            "en": "President of Iran (since 2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Masoud_Pezeshkian_2025_%28cropped%29.jpg/640px-Masoud_Pezeshkian_2025_%28cropped%29.jpg",
        "aliases": [
            "masoud pezeshkian",
            "pezeshkian",
            "пезешкиан",
            "масуд пезешкиан",
            "masud pezeshkiyon"
        ],
        "fun_fact": {
            "uz": "Kasbi bo'yicha taniqli kardioxirurg va islohotchi siyosatchi bo'lib, 2024-yilgi saylovda g'alaba qozongan.",
            "ru": "Кардиохирург и реформатор, одержавший победу на внеочередных президентских выборах в 2024 году.",
            "en": "Cardiac surgeon and reformist lawmaker who won Iran's snap presidential election in July 2024."
        }
    },
    {
        "id": "ebrahim_raisi",
        "name": {
            "uz": "Ibrohim Raisiy",
            "ru": "Ибрахим Раиси",
            "en": "Ebrahim Raisi"
        },
        "country": {
            "uz": "Eron",
            "ru": "Иран",
            "en": "Iran"
        },
        "role": {
            "uz": "Eron Islom Respublikasi Prezidenti (2021–2024)",
            "ru": "Президент Ирана (2021–2024)",
            "en": "President of Iran (2021–2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Ebrahim_Raisi_in_2024_%283x4_cropped%29.jpg/640px-Ebrahim_Raisi_in_2024_%283x4_cropped%29.jpg",
        "aliases": [
            "ebrahim raisi",
            "raisi",
            "раиси",
            "ибрахим раиси",
            "ibrohim raisiy"
        ],
        "fun_fact": {
            "uz": "Eronning konservativ diniy va sud tizimi yetakchisi bo'lib, 2024-yilda vertolyot halokatida vafot etgan.",
            "ru": "Возглавлял судебную систему Ирана перед президентством; трагически погиб в авиакатастрофе в мае 2024 года.",
            "en": "Former chief justice who led Iran until his death in a helicopter crash in East Azerbaijan province in May 2024."
        }
    },
    {
        "id": "hassan_rouhani",
        "name": {
            "uz": "Hasan Ruhoniy",
            "ru": "Хасан Рухани",
            "en": "Hassan Rouhani"
        },
        "country": {
            "uz": "Eron",
            "ru": "Иран",
            "en": "Iran"
        },
        "role": {
            "uz": "Eron Islom Respublikasi Prezidenti (2013–2021)",
            "ru": "Президент Ирана (2013–2021)",
            "en": "President of Iran (2013–2021)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Hassan_Rouani_2017_portrait.jpg/640px-Hassan_Rouani_2017_portrait.jpg",
        "aliases": [
            "hassan rouhani",
            "rouhani",
            "ruhoniy",
            "рухани",
            "хасан рухани"
        ],
        "fun_fact": {
            "uz": "2015-yilda jahonning yetakchi 6 davlati bilan tarixiy Eron yadroviy kelishuvini (JCPOA) imzolagan.",
            "ru": "Заключил историческую «ядерную сделку» (СВПД) с мировыми державами в 2015 году.",
            "en": "Centrist cleric who negotiated the landmark 2015 Joint Comprehensive Plan of Action (Iran nuclear deal)."
        }
    },
    {
        "id": "mahmoud_ahmadinejad",
        "name": {
            "uz": "Mahmud Ahmadinajod",
            "ru": "Махмуд Ахмадинежад",
            "en": "Mahmoud Ahmadinejad"
        },
        "country": {
            "uz": "Eron",
            "ru": "Иран",
            "en": "Iran"
        },
        "role": {
            "uz": "Eron Islom Respublikasi Prezidenti (2005–2013)",
            "ru": "Президент Ирана (2005–2013)",
            "en": "President of Iran (2005–2013)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Mahmoud_Ahmedinejad_July_2026_%28cropped%29.jpg/640px-Mahmoud_Ahmedinejad_July_2026_%28cropped%29.jpg",
        "aliases": [
            "mahmoud ahmadinejad",
            "ahmadinejad",
            "ахмадинежад",
            "махмуд ахмадинежад",
            "ahmadinajod"
        ],
        "fun_fact": {
            "uz": "Tehronning sobiq meri bo'lib, o'zining keskin populistik va G'arbga qarshi nutqlari bilan xalqaro maydonda tanilgan.",
            "ru": "Бывший мэр Тегерана, известный бескомпромиссной антизападной риторикой и развитием ядерной программы.",
            "en": "Known for his confrontational populist speeches abroad and rapid advancement of Iran's nuclear enrichment."
        }
    },
    {
        "id": "ali_khamenei",
        "name": {
            "uz": "Ali Xomanaiy",
            "ru": "Али Хаменеи",
            "en": "Ali Khamenei"
        },
        "country": {
            "uz": "Eron",
            "ru": "Иран",
            "en": "Iran"
        },
        "role": {
            "uz": "Eron Islom Respublikasi Oliy Rahbari (1989-yildan)",
            "ru": "Высший руководитель Ирана (с 1989)",
            "en": "Supreme Leader of Iran (since 1989)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Ali_Khamenei_Nowruz_message_official_portrait_1397_02_%283_x_4_cropped%29.jpg/640px-Ali_Khamenei_Nowruz_message_official_portrait_1397_02_%283_x_4_cropped%29.jpg",
        "aliases": [
            "ali khamenei",
            "khamenei",
            "хаменеи",
            "али хаменеи",
            "xomanaiy"
        ],
        "fun_fact": {
            "uz": "Oyatulloh Xumayniydan keyin Eronning ikkinchi Oliy Rahbari bo'lib, Yaqin Sharqdagi eng uzoq boshqargan yetakchilardan.",
            "ru": "Преемник аятоллы Хомейни, второй Высший руководитель Ирана, занимает пост более 35 лет.",
            "en": "Successor to Ayatollah Khomeini and the longest-serving head of state in the Middle East."
        }
    },
    {
        "id": "ruhollah_khomeini",
        "name": {
            "uz": "Ruholloh Xumayniy",
            "ru": "Рухолла Хомейни",
            "en": "Ruhollah Khomeini"
        },
        "country": {
            "uz": "Eron",
            "ru": "Иран",
            "en": "Iran"
        },
        "role": {
            "uz": "Eron Islom Inqilobi Yetakchisi va Birinchi Oliy Rahbari",
            "ru": "Лидер Исламской революции и первый Высший руководитель Ирана",
            "en": "Founder and First Supreme Leader of the Islamic Republic of Iran"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Portrait_of_Ruhollah_Khomeini_By_Ali_Kaveh.jpg/640px-Portrait_of_Ruhollah_Khomeini_By_Ali_Kaveh.jpg",
        "aliases": [
            "ruhollah khomeini",
            "khomeini",
            "хомейни",
            "рухолла хомейни",
            "xumayniy"
        ],
        "fun_fact": {
            "uz": "1979-yilgi Eron Islom inqilobiga rahbarlik qilib, 2500 yillik Eron monarxiyasini tugatgan.",
            "ru": "Возглавил Исламскую революцию 1979 года, свергнувшую шахский режим и основавшую исламскую республику.",
            "en": "Led the 1979 Iranian Revolution overthrowing the Pahlavi dynasty to establish the Islamic Republic."
        }
    },
    {
        "id": "mohammed_bin_salman",
        "name": {
            "uz": "Muhammad bin Salmon",
            "ru": "Мухаммед ибн Салман",
            "en": "Mohammed bin Salman"
        },
        "country": {
            "uz": "Saudiya Arabistoni",
            "ru": "Саудовская Аравия",
            "en": "Saudi Arabia"
        },
        "role": {
            "uz": "Saudiya Arabistoni Valiahd shahzodasi va Bosh vaziri",
            "ru": "Наследный принц и премьер-министр Саудовской Аравии",
            "en": "Crown Prince and Prime Minister of Saudi Arabia (MBS)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/%D8%A7%D9%84%D8%B5%D9%88%D8%B1%D8%A9_%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A%D8%A9_%D9%84%D9%84%D8%A3%D9%85%D9%8A%D8%B1_%D9%85%D8%AD%D9%85%D8%AF_%D8%A8%D9%86_%D8%B3%D9%84%D9%85%D8%A7%D9%86_%D8%A8%D9%86_%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B9%D8%B2%D9%8A%D8%B2_%D8%A2%D9%84_%D8%B3%D8%B9%D9%88%D8%AF_%28%D9%85%D9%82%D8%B5%D9%88%D8%B5%D8%A9%29.jpg/640px-%D8%A7%D9%84%D8%B5%D9%88%D8%B1%D8%A9_%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A%D8%A9_%D9%84%D9%84%D8%A3%D9%85%D9%8A%D8%B1_%D9%85%D8%AD%D9%85%D8%AF_%D8%A8%D9%86_%D8%B3%D9%84%D9%85%D8%A7%D9%86_%D8%A8%D9%86_%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B9%D8%B2%D9%8A%D8%B2_%D8%A2%D9%84_%D8%B3%D8%B9%D9%88%D8%AF_%28%D9%85%D9%82%D8%B5%D9%88%D8%B5%D8%A9%29.jpg",
        "aliases": [
            "mohammed bin salman",
            "mbs",
            "мухаммед ибн салман",
            "muhammad bin salmon"
        ],
        "fun_fact": {
            "uz": "'Vision 2030' dasturi orqali Saudiya Arabistonini modernizatsiya qilish va NEOM mega-shahrini qurish tashabbuskori.",
            "ru": "Инициатор программы масштабной модернизации «Видение 2030» и футуристического мегаполиса NEOM.",
            "en": "Known globally as MBS, he launched the Vision 2030 agenda including the futuristic Neom megacity."
        }
    },
    {
        "id": "mohammed_bin_zayed",
        "name": {
            "uz": "Muhammad bin Zoid Ol Nahayon",
            "ru": "Мухаммад ибн Заид Аль Нахайян",
            "en": "Mohamed bin Zayed Al Nahyan"
        },
        "country": {
            "uz": "BAA",
            "ru": "ОАЭ",
            "en": "United Arab Emirates"
        },
        "role": {
            "uz": "BAA Prezidenti va Abu-Dabi hukmdori (2022-yildan)",
            "ru": "Президент ОАЭ и правитель Абу-Даби (с 2022)",
            "en": "President of the United Arab Emirates (MBZ)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Mohamed_bin_Zayed_Al_Nahyan_-_2024_%28cropped%29.jpg/640px-Mohamed_bin_Zayed_Al_Nahyan_-_2024_%28cropped%29.jpg",
        "aliases": [
            "mohamed bin zayed",
            "mbz",
            "мухаммад ибн заид",
            "muhammad bin zoid"
        ],
        "fun_fact": {
            "uz": "BAAni Yaqin Sharqdagi yetakchi texnologik va iqtisodiy qudratga aylantirgan 'MBZ' nomi bilan mashhur rahbar.",
            "ru": "Широко известен как MBZ, превратил Эмираты в глобальный финансовый и технологический центр.",
            "en": "Known worldwide as MBZ, he modernised the UAE's armed forces and oversaw dramatic economic diversification."
        }
    },
    {
        "id": "tamim_bin_hamad",
        "name": {
            "uz": "Tamim bin Hamad Ol Soniy",
            "ru": "Тамим бин Хамад Аль Тани",
            "en": "Tamim bin Hamad Al Thani"
        },
        "country": {
            "uz": "Qatar",
            "ru": "Катар",
            "en": "Qatar"
        },
        "role": {
            "uz": "Qatar Amiri (2013-yildan)",
            "ru": "Эмир Катара (с 2013)",
            "en": "Emir of Qatar (since 2013)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Emir_of_Qatar_on_February_19%2C_2025_%28cropped%29.jpg/640px-Emir_of_Qatar_on_February_19%2C_2025_%28cropped%29.jpg",
        "aliases": [
            "tamim bin hamad",
            "emir of qatar",
            "тамим бин хамад",
            "эмир катара",
            "tamim bin hamad al thani"
        ],
        "fun_fact": {
            "uz": "Tarixdagi eng muvaffaqiyatli FIFA Jahon chempionatlaridan biri bo'lgan 2022-yilgi Qatar Jahon Kubogiga mezbonlik qilgan amir.",
            "ru": "Успешно провел в Катаре Чемпионат мира по футболу 2022 года, став самым молодым монархом в Заливе.",
            "en": "Hosted the prestigious 2022 FIFA World Cup in Qatar and oversaw dramatic modernization as the Gulf's youngest monarch."
        }
    },
    {
        "id": "bashar_al_assad",
        "name": {
            "uz": "Bashar al-Asad",
            "ru": "Башар Асад",
            "en": "Bashar al-Assad"
        },
        "country": {
            "uz": "Suriya",
            "ru": "Сирия",
            "en": "Syria"
        },
        "role": {
            "uz": "Suriya Prezidenti (2000–2024)",
            "ru": "Президент Сирии (2000–2024)",
            "en": "President of Syria (2000–2024)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Bashar_al-Assad_in_May_2024.png/640px-Bashar_al-Assad_in_May_2024.png",
        "aliases": [
            "bashar al-assad",
            "assad",
            "asad",
            "асад",
            "башар асад"
        ],
        "fun_fact": {
            "uz": "Londonda tahsil olgan oftalmolog shifokor bo'lib, akasining vafotidan so'ng otasi o'rniga hokimiyatga kelgan.",
            "ru": "По образованию врач-офтальмолог, руководил Сирией на протяжении более двух десятилетий.",
            "en": "Trained as an ophthalmologist in London before returning to succeed his father Hafez al-Assad in 2000."
        }
    },
    {
        "id": "saddam_hussein",
        "name": {
            "uz": "Saddam Husayn",
            "ru": "Саддам Хусейн",
            "en": "Saddam Hussein"
        },
        "country": {
            "uz": "Iroq",
            "ru": "Ирак",
            "en": "Iraq"
        },
        "role": {
            "uz": "Iroq Prezidenti (1979–2003)",
            "ru": "Президент Ирака (1979–2003)",
            "en": "President of Iraq (1979–2003)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Saddam_Hussein_in_1998.jpg/640px-Saddam_Hussein_in_1998.jpg",
        "aliases": [
            "saddam hussein",
            "saddam",
            "хусейн",
            "саддам хусейн",
            "saddam husayn"
        ],
        "fun_fact": {
            "uz": "Baas partiyasi yetakchisi sifatida Iroq-Eron urushini va 1990-yilda Quvaytga bosqinni boshqargan.",
            "ru": "Руководил Ираком почти четверть века, вел многолетнюю войну с Ираном и вторгся в Кувейт в 1990 году.",
            "en": "Led Iraq for over two decades, presiding over the Iran-Iraq War and the 1990 invasion of Kuwait."
        }
    },
    {
        "id": "yasser_arafat",
        "name": {
            "uz": "Yosir Arofat",
            "ru": "Ясир Арафат",
            "en": "Yasser Arafat"
        },
        "country": {
            "uz": "Falastin",
            "ru": "Палестина",
            "en": "Palestine"
        },
        "role": {
            "uz": "Falastin ozodlik tashkiloti yetakchisi va Prezidenti",
            "ru": "Председатель исполкома ООП и Президент Палестины",
            "en": "Chairman of the PLO and President of the Palestinian National Authority"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Leader_of_the_PLO%2C_Yasser_Arafat%2C_1996_Dan_Hadani_Archive.jpg/640px-Leader_of_the_PLO%2C_Yasser_Arafat%2C_1996_Dan_Hadani_Archive.jpg",
        "aliases": [
            "yasser arafat",
            "arafat",
            "арафат",
            "ясир арафат",
            "yosir arofat"
        ],
        "fun_fact": {
            "uz": "Falastin milliy harakati yetakchisi, kufiya ro'moli bilan mashhur bo'lgan va 1994-yilda Nobel Tinchlik mukofotini olgan.",
            "ru": "Многолетний лидер палестинского национального движения, лауреат Нобелевской премии мира 1994 года.",
            "en": "Longtime leader of the PLO who signed the 1993 Oslo Accords and shared the 1994 Nobel Peace Prize."
        }
    },
    {
        "id": "nelson_mandela",
        "name": {
            "uz": "Nelson Mandela",
            "ru": "Нельсон Мандела",
            "en": "Nelson Mandela"
        },
        "country": {
            "uz": "Janubiy Afrika Respublikasi",
            "ru": "ЮАР",
            "en": "South Africa"
        },
        "role": {
            "uz": "JARning Birinchi Qora Tanli Prezidenti (1994–1999)",
            "ru": "Первый темнокожий Президент ЮАР (1994–1999)",
            "en": "First Black President of South Africa (1994–1999)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Nelson_Mandela_1994.jpg/640px-Nelson_Mandela_1994.jpg",
        "aliases": [
            "nelson mandela",
            "mandela",
            "мандела",
            "нельсон мандела",
            "madiba"
        ],
        "fun_fact": {
            "uz": "Aparteid rejimiga qarshi kurashib 27 yil qamoqda o'tirgan va 1993-yilda Nobel Tinchlik mukofotiga sazovor bo'lgan.",
            "ru": "Провел 27 лет в тюрьме за борьбу против апартеида, всемирный символ примирения и лауреат Нобелевской премии мира.",
            "en": "Spent 27 years imprisoned for opposing apartheid before being elected president and receiving the Nobel Peace Prize."
        }
    },
    {
        "id": "cyril_ramaphosa",
        "name": {
            "uz": "Siril Ramafosa",
            "ru": "Сирил Рамафоса",
            "en": "Cyril Ramaphosa"
        },
        "country": {
            "uz": "Janubiy Afrika Respublikasi",
            "ru": "ЮАР",
            "en": "South Africa"
        },
        "role": {
            "uz": "JAR Prezidenti (2018-yildan)",
            "ru": "Президент ЮАР (с 2018)",
            "en": "President of South Africa (since 2018)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Cyril_Ramaphosa_in_2026.jpg/640px-Cyril_Ramaphosa_in_2026.jpg",
        "aliases": [
            "cyril ramaphosa",
            "ramaphosa",
            "рамафоса",
            "сирил рамафоса"
        ],
        "fun_fact": {
            "uz": "Nelson Mandelaning asosiy muzokarachisi bo'lgan, kasaba uyushmasi yetakchisidan milliarder tadbirkor va prezident darajasiga yetgan.",
            "ru": "Главный переговорщик Манделы при отмене апартеида, влиятельный профсоюзный лидер и бизнесмен.",
            "en": "Mandela's chief negotiator during the end of apartheid, former trade unionist and billionaire businessman."
        }
    },
    {
        "id": "abdel_fattah_el_sisi",
        "name": {
            "uz": "Abdul Fattoh as-Sisi",
            "ru": "Абдул-Фаттах ас-Сиси",
            "en": "Abdel Fattah el-Sisi"
        },
        "country": {
            "uz": "Misr",
            "ru": "Египет",
            "en": "Egypt"
        },
        "role": {
            "uz": "Misr Prezidenti (2014-yildan)",
            "ru": "Президент Египта (с 2014)",
            "en": "President of Egypt (since 2014)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/AbdelFattah_Elsisi_%28cropped%29.jpg/640px-AbdelFattah_Elsisi_%28cropped%29.jpg",
        "aliases": [
            "abdel fattah el-sisi",
            "sisi",
            "el-sisi",
            "сиси",
            "ас-сиси",
            "абдул-фаттах ас-сиси"
        ],
        "fun_fact": {
            "uz": "Yangi Suvaysh kanalini qazdirgan va Qohira yaqinida yangi ma'muriy poytaxt bunyod etgan harbiy marshaldan chiqqan rahbar.",
            "ru": "Инициировал строительство Новой административной столицы Египта и расширение Суэцкого канала.",
            "en": "Oversaw the expansion of the Suez Canal and the construction of Egypt's massive New Administrative Capital."
        }
    },
    {
        "id": "gamal_abdel_nasser",
        "name": {
            "uz": "Jamol Abdul Nosir",
            "ru": "Гамаль Абдель Насер",
            "en": "Gamal Abdel Nasser"
        },
        "country": {
            "uz": "Misr",
            "ru": "Египет",
            "en": "Egypt"
        },
        "role": {
            "uz": "Misr Prezidenti (1954–1970), Panarabizm yetakchisi",
            "ru": "Президент Египта (1954–1970)",
            "en": "President of Egypt (1954–1970)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Stevan_Kragujevic%2C_Gamal_Abdel_Naser_u_Beogradu%2C_1962.jpg/640px-Stevan_Kragujevic%2C_Gamal_Abdel_Naser_u_Beogradu%2C_1962.jpg",
        "aliases": [
            "gamal abdel nasser",
            "nasser",
            "насер",
            "гамаль абдель насер",
            "jamol abdul nosir"
        ],
        "fun_fact": {
            "uz": "1956-yilda Suvaysh kanalini milliylashtirgan va Asvon to'g'onini qurdirgan panarab harakati yetakchisi.",
            "ru": "Национализировал Суэцкий канал в 1956 году и построил Асуанскую плотину, лидер движения неприсоединения.",
            "en": "Nationalised the Suez Canal in 1956 and built the Aswan High Dam, becoming the icon of pan-Arab nationalism."
        }
    },
    {
        "id": "anwar_sadat",
        "name": {
            "uz": "Anvar Sadat",
            "ru": "Анвар Садат",
            "en": "Anwar Sadat"
        },
        "country": {
            "uz": "Misr",
            "ru": "Египет",
            "en": "Egypt"
        },
        "role": {
            "uz": "Misr Prezidenti (1970–1981)",
            "ru": "Президент Египта (1970–1981)",
            "en": "President of Egypt (1970–1981)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Anwar_El_Sadat_%28cropped%29.jpg/640px-Anwar_El_Sadat_%28cropped%29.jpg",
        "aliases": [
            "anwar sadat",
            "sadat",
            "садат",
            "анвар садат"
        ],
        "fun_fact": {
            "uz": "Isroil bilan tarixiy Kemp-Devid tinchlik bitimini imzolagan birinchi arab yetakchisi, Nobel mukofoti sohibi.",
            "ru": "Первый арабский лидер, заключивший мирный договор с Израилем в Кэмп-Дэвиде, лауреат Нобелевской премии мира.",
            "en": "First Arab leader to visit Israel and sign a peace treaty (Camp David Accords), winning the 1978 Nobel Peace Prize."
        }
    },
    {
        "id": "muammar_gaddafi",
        "name": {
            "uz": "Muammar Qazzofiy",
            "ru": "Муаммар Каддафи",
            "en": "Muammar Gaddafi"
        },
        "country": {
            "uz": "Liviya",
            "ru": "Ливия",
            "en": "Libya"
        },
        "role": {
            "uz": "Liviya Inqilobi Yetakchisi (1969–2011)",
            "ru": "Лидер Ливийской революции (1969–2011)",
            "en": "Brotherly Leader of Libya (1969–2011)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Moamer_el_Gadafi_%28cropped%29.jpg/640px-Moamer_el_Gadafi_%28cropped%29.jpg",
        "aliases": [
            "muammar gaddafi",
            "gaddafi",
            "qaddafi",
            "каддафи",
            "муаммар каддафи",
            "muammar qazzofiy"
        ],
        "fun_fact": {
            "uz": "Liviyani 42 yil boshqargan, 'Yashil kitob' muallifi va ulkan 'Buyuk texnogen daryo' suv loyihasini qurdirgan.",
            "ru": "Руководил Ливией 42 года, автор «Зеленой книги» и создатель Великой рукотворной реки в Сахаре.",
            "en": "Governed Libya for 42 years, author of 'The Green Book' and builder of the Great Man-Made River."
        }
    },
    {
        "id": "paul_kagame",
        "name": {
            "uz": "Pol Kagame",
            "ru": "Поль Кагаме",
            "en": "Paul Kagame"
        },
        "country": {
            "uz": "Ruanda",
            "ru": "Руанда",
            "en": "Rwanda"
        },
        "role": {
            "uz": "Ruanda Prezidenti (2000-yildan)",
            "ru": "Президент Руанды (с 2000)",
            "en": "President of Rwanda (since 2000)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Paul_Kagame_2024_%28cropped%29.jpg/640px-Paul_Kagame_2024_%28cropped%29.jpg",
        "aliases": [
            "paul kagame",
            "kagame",
            "кагаме",
            "поль кагаме"
        ],
        "fun_fact": {
            "uz": "1994-yilgi genotsiddan so'ng mamlakatni qayta tiklab, Ruandani 'Afrikaning Singapuri'ga aylantirgan.",
            "ru": "Остановил геноцид 1994 года и превратил Руанду в одну из самых безопасных и технологичных стран Африки.",
            "en": "Led the forces that ended the 1994 Rwandan genocide and transformed Rwanda into a leading African tech hub."
        }
    },
    {
        "id": "william_ruto",
        "name": {
            "uz": "Uilyam Ruto",
            "ru": "Уильям Руто",
            "en": "William Ruto"
        },
        "country": {
            "uz": "Keniya",
            "ru": "Кения",
            "en": "Kenya"
        },
        "role": {
            "uz": "Keniya Prezidenti (2022-yildan)",
            "ru": "Президент Кении (с 2022)",
            "en": "President of Kenya (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/President_Ruto_Potrait_2022_%28cropped%29.jpg/640px-President_Ruto_Potrait_2022_%28cropped%29.jpg",
        "aliases": [
            "william ruto",
            "ruto",
            "руто",
            "уильям руто"
        ],
        "fun_fact": {
            "uz": "O'zini 'hustler' (mehnatkash) deb atab, kambag'al qatlamni qo'llab-quvvatlash shiori bilan saylovda g'alaba qozongan.",
            "ru": "Построил предвыборную кампанию на защите простых тружеников («хастлеров») и возглавил Кению в 2022 году.",
            "en": "Rose from selling chickens along roadside highways to become the fifth president of Kenya."
        }
    },
    {
        "id": "anthony_albanese",
        "name": {
            "uz": "Entoni Albanez",
            "ru": "Энтони Албаниз",
            "en": "Anthony Albanese"
        },
        "country": {
            "uz": "Avstraliya",
            "ru": "Австралия",
            "en": "Australia"
        },
        "role": {
            "uz": "Avstraliya Bosh vaziri (2022-yildan)",
            "ru": "Премьер-министр Австралии (с 2022)",
            "en": "Prime Minister of Australia (since 2022)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Anthony_Albanese_portrait_%28re-crop%29.jpg/640px-Anthony_Albanese_portrait_%28re-crop%29.jpg",
        "aliases": [
            "anthony albanese",
            "albanese",
            "албаниз",
            "энтони албаниз",
            "albo"
        ],
        "fun_fact": {
            "uz": "Avstraliyada 'Albo' laqabi bilan tanilgan, ijtimoiy uyda yolg'iz ona tomonidan tarbiyalangan bosh vazir.",
            "ru": "Известен в Австралии как «Альбо», вырос в муниципальном жилье с матерью-одиночкой.",
            "en": "Popularly nicknamed 'Albo', he led the Labor Party back to power after nine years in opposition."
        }
    },
    {
        "id": "jacinda_ardern",
        "name": {
            "uz": "Jasinda Ardern",
            "ru": "Джасинда Ардерн",
            "en": "Jacinda Ardern"
        },
        "country": {
            "uz": "Yangi Zelandiya",
            "ru": "Новая Зеландия",
            "en": "New Zealand"
        },
        "role": {
            "uz": "Yangi Zelandiya Bosh vaziri (2017–2023)",
            "ru": "Премьер-министр Новой Зеландии (2017–2023)",
            "en": "Prime Minister of New Zealand (2017–2023)"
        },
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/New_Zealand_Prime_Minister_Jacinda_Ardern_in_2018.jpg/640px-New_Zealand_Prime_Minister_Jacinda_Ardern_in_2018.jpg",
        "aliases": [
            "jacinda ardern",
            "ardern",
            "ардерн",
            "джасинда ардерн"
        ],
        "fun_fact": {
            "uz": "Dunyo tarixida lavozimda bo'lgan paytida farzand ko'rgan ikkinchi bosh vazir bo'lgan.",
            "ru": "Стала второй в мировой истории женщиной-главой правительства, родившей ребенка во время пребывания на посту.",
            "en": "Became only the second elected world leader in modern history to give birth while in office."
        }
    }
]

PRESIDENTS_BY_ID = {p["id"]: p for p in PRESIDENTS}

def get_president_by_id(president_id: str) -> dict | None:
    """Retrieve president data dictionary by unique string ID."""
    return PRESIDENTS_BY_ID.get(president_id)

def get_random_presidents(count: int = 4, exclude_id: str | None = None) -> list[dict]:
    """Return a random sample of presidents, optionally excluding a specific ID."""
    pool = [p for p in PRESIDENTS if p["id"] != exclude_id] if exclude_id else PRESIDENTS
    return random.sample(pool, min(count, len(pool)))

def search_president_by_alias(alias: str) -> dict | None:
    """Case-insensitive search by name or alias."""
    norm = alias.strip().lower()
    for p in PRESIDENTS:
        if norm in p["aliases"] or any(norm == v.lower() for v in p["name"].values()):
            return p
    return None
