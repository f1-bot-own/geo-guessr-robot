"""
Country Fun Facts and Trivia for GeoGuru & GeoGuessr Bot.
Provides fascinating educational insights after each question.
"""

FUN_FACTS = {
    "uz": {
        "en": "Uzbekistan is one of only two doubly landlocked countries in the world (surrounded entirely by other landlocked countries; the other is Liechtenstein).",
        "ru": "Узбекистан — одна из двух стран мира, дважды не имеющих выхода к морю (вторая — Лихтенштейн).",
        "uz": "O'zbekiston dunyoda dengizga chiqish yo'liga ega bo'lmagan davlatlar bilan o'ralgan faqatgina ikkita davlatdan biridir (ikkinchisi — Lixtenshteyn)."
    },
    "kz": {
        "en": "Kazakhstan is the 9th largest country in the world and the largest landlocked country on Earth.",
        "ru": "Казахстан — девятая по величине страна в мире и самое крупное государство без выхода к мировому океану.",
        "uz": "Qozog'iston dunyodagi 9-eng yirik mamlakat va dengizga chiqish imkoni bo'lmagan dunyodagi eng katta davlatdir."
    },
    "kg": {
        "en": "Kyrgyzstan has Lake Issyk-Kul, the second-largest alpine lake in the world, which never freezes.",
        "ru": "В Кыргызстане находится озеро Иссык-Куль — второе по величине высокогорное озеро в мире, которое никогда не замерзает.",
        "uz": "Qirg'izistonda dunyodagi ikkinchi eng yirik baland tog' ko'li — Issiqko'l joylashgan bo'lib, u hech qachon muzlamaydi."
    },
    "tj": {
        "en": "Tajikistan is more than 93% covered by mountains, predominantly the dramatic Pamir range.",
        "ru": "Более 93% территории Таджикистана покрыто горами, главным образом величественным Памиром.",
        "uz": "Tojikiston hududining 93 foizdan ortig'i baland tog'lardan, asosan mahobatli Pomir tizmasidan iborat."
    },
    "tm": {
        "en": "Turkmenistan is home to the Darvaza Gas Crater ('Door to Hell'), which has been burning continuously since 1971.",
        "ru": "В Туркменистане находится газовый кратер Дарваза («Врата ада»), горящий без перерыва с 1971 года.",
        "uz": "Turkmanistonda 1971 yildan beri uzluksiz yonib kelayotgan mashhur Darvoza gaz krateri ('Jahannam darvozasi') joylashgan."
    },
    "tr": {
        "en": "Istanbul, Turkey is the only major city in the world straddling two continents: Europe and Asia.",
        "ru": "Стамбул в Турции — единственный мегаполис мира, расположенный одновременно в Европе и Азии.",
        "uz": "Turkiyaning Istanbul shahri bir vaqtning o'zida ikki qit'ada (Yevropa va Osiyo) joylashgan dunyodagi yagona megapolisdir."
    },
    "us": {
        "en": "The United States spans six time zones across the 50 states, plus additional territories.",
        "ru": "США охватывают 6 часовых поясов на территории 50 штатов, не считая островных территорий.",
        "uz": "AQSH 50 ta shtat bo'ylab 6 ta vaqt mintaqasini qamrab oladi."
    },
    "gb": {
        "en": "In the United Kingdom, no point on the main island is more than 113 km (70 miles) from the sea.",
        "ru": "В Великобритании ни одна точка острова не удалена от морского побережья более чем на 113 км.",
        "uz": "Buyuk Britaniyada orolning istalgan nuqtasi dengiz qirg'og'idan ko'pi bilan 113 km uzoqlikda joylashgan."
    },
    "fr": {
        "en": "France holds the record for the most time zones of any country (12 time zones), due to its overseas territories.",
        "ru": "Франция удерживает мировой рекорд по количеству часовых поясов (12 поясов) благодаря заморским территориям.",
        "uz": "Fransiya o'zining dengizorti hududlari tufayli dunyoda eng ko'p vaqt mintaqasiga ega davlatdir (12 ta mintaqa)."
    },
    "de": {
        "en": "Germany borders nine different countries, tying with Russia for the highest number of borders in Europe.",
        "ru": "Германия граничит с 9 государствами — рекорд среди стран Западной и Центральной Европы.",
        "uz": "Germaniya 9 ta davlat bilan chegaradosh bo'lib, G'arbiy va Markaziy Yevropada eng ko'p qo'shniga ega."
    },
    "it": {
        "en": "Italy has more UNESCO World Heritage Sites (59) than any other nation in the world.",
        "ru": "В Италии насчитывается 59 объектов Всемирного наследия ЮНЕСКО — больше, чем в любой другой стране мира.",
        "uz": "Italiya dunyo bo'yicha YUNESKO Butunjahon merosi ro'yxatiga eng ko'p ob'ekt (59 ta) kiritilgan mamlakatdir."
    },
    "es": {
        "en": "Spain produces more than 40% of the world's total supply of olive oil.",
        "ru": "Испания производит более 40% всего мирового объема оливкового масла.",
        "uz": "Ispaniya butun dunyodagi zaytun moyining 40 foizdan ortig'ini yetishtirib beradi."
    },
    "jp": {
        "en": "Japan consists of an archipelago of 6,852 islands, with four main islands making up most of the land.",
        "ru": "Япония состоит из архипелага из 6 852 островов, из которых 4 главных формируют основную территорию.",
        "uz": "Yaponiya 6 852 ta oroldan iborat arxipelag bo'lib, hududining asosiy qismini 4 ta yirik orol tashkil etadi."
    },
    "kr": {
        "en": "South Korea has the fastest average internet speeds in the world and over 64% forest coverage.",
        "ru": "Южная Корея славится самым быстрым интернетом в мире, а более 64% ее территории покрыто лесами.",
        "uz": "Janubiy Koreya dunyodagi eng tezkor internetga ega bo'lib, hududining 64% dan ortig'i o'rmonlar bilan qoplangan."
    },
    "cn": {
        "en": "Despite spanning five geographical time zones, all of China officially uses a single time zone (UTC+8).",
        "ru": "Несмотря на охват пяти географических поясов, весь Китай официально живет по единому времени (UTC+8).",
        "uz": "Xitoy beshta geografik vaqt mintaqasini egallashiga qaramay, butun mamlakat rasman yagona vaqtda (UTC+8) yashaydi."
    },
    "in": {
        "en": "India is the world's most populous nation and the birthplace of chess (known originally as chaturanga).",
        "ru": "Индия — самая населенная страна на планете и родина шахмат (изначально известная как чатуранга).",
        "uz": "Hindiston dunyodagi eng ko'p aholiga ega davlat va shaxmat o'yini vatanidir (qadimda chatiranga deb atalgan)."
    },
    "br": {
        "en": "Brazil borders every single country in South America except Ecuador and Chile.",
        "ru": "Бразилия граничит со всеми странами Южной Америки, кроме Эквадора и Чили.",
        "uz": "Braziliya Janubiy Amerikadagi Ekvador va Chilidan tashqari barcha davlatlar bilan chegaradosh."
    },
    "ca": {
        "en": "Canada contains more than half of all natural lakes on Earth, and boasts the world's longest coastline.",
        "ru": "В Канаде находится больше половины всех озер планеты, а также самая протяженная береговая линия в мире.",
        "uz": "Kanadada butun sayyoradagi tabiiy ko'llarning yarmidan ko'pi va dunyodagi eng uzun dengiz qirg'og'i mavjud."
    },
    "au": {
        "en": "Australia is the only country on Earth that occupies an entire continent by itself.",
        "ru": "Австралия — единственное государство на Земле, занимающее целый континент целиком.",
        "uz": "Avstraliya butun bir qit'ani bir o'zi to'liq egallagan dunyodagi yagona davlatdir."
    },
    "eg": {
        "en": "Egypt's River Nile was historically considered the longest river on Earth at roughly 6,650 km.",
        "ru": "Река Нил в Египте традиционно считается самой длинной рекой на Земле (около 6 650 км).",
        "uz": "Misrdagi Nil daryosi 6 650 km uzunlik bilan an'anaviy ravishda dunyodagi eng uzun daryo deb hisoblanadi."
    },
    "is": {
        "en": "Iceland has zero mosquitoes and gets almost 100% of its electricity from renewable geothermal and hydro energy.",
        "ru": "В Исландии совершенно нет комаров, а почти 100% электроэнергии вырабатывается из геотермальных источников.",
        "uz": "Islandiyada umuman chivinlar yo'q va elektr energiyasining 100% ga yaqini geotermal va gidro manbalardan olinadi."
    }
}

def get_fun_fact(country_code: str, lang: str = "en") -> str:
    """Retrieve fun fact for country code or return general geo fact."""
    code = country_code.lower()
    if code in FUN_FACTS:
        return FUN_FACTS[code].get(lang) or FUN_FACTS[code].get("en", "")
    
    defaults = {
        "en": "Geography shapes the culture, history, and economy of nations across the globe!",
        "ru": "География формирует культуру, историю и развитие стран по всему миру!",
        "uz": "Geografiya butun dunyodagi davlatlarning madaniyati, tarixi va rivojlanishini belgilaydi!"
    }
    return defaults.get(lang, defaults["en"])
