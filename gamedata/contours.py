"""
Country Silhouettes & Contours Dataset for GeoGuru & GeoGuessr.
Features high-contrast geographic outline maps (PNG) for sovereign nations.
"""

from typing import Optional, Dict

CONTOUR_DATA = [
    # Iconic / Distinctive shapes
    {"code": "it", "shape_trivia": {"uz": "Dunyodagi eng mashhur 'etik' shaklidagi yarim orol davlat", "ru": "Знаменитый полуостров в форме сапога", "en": "The iconic 'boot-shaped' Mediterranean peninsula"}},
    {"code": "uz", "shape_trivia": {"uz": "Markaziy Osiyoning qoq markazida joylashgan, ikki marta quruqlik bilan o'ralgan (double-landlocked) davlat", "ru": "Сердце Центральной Азии, дважды окруженное сушей государство", "en": "Heart of Central Asia, uniquely doubly-landlocked nation"}},
    {"code": "jp", "shape_trivia": {"uz": "Tinch okeani bo'ylab cho'zilgan 4 ta yirik va minglab mayda orollar yoyi", "ru": "Изогнутая дуга из тысяч тихоокеанских островов", "en": "An iconic volcanic island arc stretching across the Pacific"}},
    {"code": "cl", "shape_trivia": {"uz": "Dunyoning eng uzun va ingichka mamlakati (uzunligi 4 300 km)", "ru": "Самая длинная и узкая страна в мире вдоль побережья Анд", "en": "World's longest and narrowest country running 4,300 km along the Andes"}},
    {"code": "fr", "shape_trivia": {"uz": "O'ziga xos 6 burchakli shakli sababli 'Geksagon' deb ataladi", "ru": "Известна как «Шестиугольник» (L'Hexagone) благодаря геометрии границ", "en": "Known affectionately as 'The Hexagon' due to its six-sided outline"}},
    {"code": "gb", "shape_trivia": {"uz": "Atlantika okeani va Shimoliy dengiz orasidagi yirik orol davlat", "ru": "Островное государство между Атлантикой и Северным морем", "en": "Distinctive island archipelago between the North Sea and the Atlantic"}},
    {"code": "in", "shape_trivia": {"uz": "Hind okeaniga turtib chiqqan ulkan uchburchak yarimorol", "ru": "Огромный полуостров субконтинента, вдающийся в Индийский океан", "en": "Vast triangular subcontinent protruding into the Indian Ocean"}},
    {"code": "br", "shape_trivia": {"uz": "Janubiy Amerikaning qariyb yarmini egallagan bahaybat davlat", "ru": "Гигантское государство, занимающее почти половину Южной Америки", "en": "Colossal nation occupying nearly half of South America"}},
    {"code": "us", "shape_trivia": {"uz": "Ikki okean orasida joylashgan va shimolda Alyaskaga ega qit'aviy davlat", "ru": "Континентальное государство от Атлантики до Тихого океана плюс Аляска", "en": "Sprawling continental landmass spanning from Atlantic to Pacific"}},
    {"code": "ca", "shape_trivia": {"uz": "Dunyodagi eng uzun dengiz qirg'og'iga va qutb orollariga ega mamlakat", "ru": "Страна с самой протяженной береговой линией и арктическими островами", "en": "World's second largest nation with vast northern archipelago"}},
    {"code": "tr", "shape_trivia": {"uz": "Osiyo va Yevropani bog'lovchi to'g'ri to'rtburchaksimon Anatoliya yarimoroli", "ru": "Анатолийский полуостров, соединяющий Азию и Европу", "en": "Rectangular Anatolian landbridge connecting Asia and Europe"}},
    {"code": "eg", "shape_trivia": {"uz": "Qizil dengiz va O'rtayer dengizi burchagidagi deyarli to'rtburchak sahro davlati", "ru": "Почти идеальный прямоугольник на стыке Африки и Азии вдоль Нила", "en": "Striking quadrilateral outline centered around the fertile Nile"}},
    {"code": "gr", "shape_trivia": {"uz": "Frakiya, Peloponnes va yuzlab Egey orollaridan iborat bo'lingan qirg'oq", "ru": "Изрезанный полуостров с Пелопоннесом и сотнями островов Эгейского моря", "en": "Ragged southern tip of the Balkans with the Peloponnese and Greek isles"}},
    {"code": "es", "shape_trivia": {"uz": "Pireney yarimorolining 85% qismini egallagan davlat", "ru": "Занимает большую часть Пиренейского полуострова", "en": "Dominates most of the rugged Iberian peninsula"}},
    {"code": "de", "shape_trivia": {"uz": "Yevropaning qoq markazidagi Boltiq va Shimoliy dengizlarga chiquvchi kontur", "ru": "Сердце Европы, простирающееся от Балтики до Альп", "en": "Central European powerhouse stretching from Baltic Sea to Bavarian Alps"}},
    {"code": "no", "shape_trivia": {"uz": "Skandinaviyaning chuqur fjordlar bilan o'yilgan uzun qirg'og'i", "ru": "Вытянутая северная полоса с тысячами изрезанных фьордов", "en": "Slender, winding Scandinavian ribbon indented by thousands of fjords"}},
    {"code": "se", "shape_trivia": {"uz": "Boltiq dengizi bo'ylab cho'zilgan Skandinaviya davlati", "ru": "Протянувшаяся вдоль Ботнического залива скандинавская страна", "en": "Elongated Scandinavian nation flanking the Baltic Sea"}},
    {"code": "fi", "shape_trivia": {"uz": "Minglab ko'llar va Botnik ko'rfaziga tutash shimoliy mamlakat", "ru": "«Страна тысячи озёр» на северо-востоке Европы", "en": "Distinctive Baltic silhouette known as the land of a thousand lakes"}},
    {"code": "ru", "shape_trivia": {"uz": "Dunyodagi eng katta maydonga ega 11 vaqt mintaqali bahaybat davlat", "ru": "Крупнейшее по площади государство мира, охватывающее 11 часовых поясов", "en": "Massive transcontinental expanse spanning 11 time zones"}},
    {"code": "kz", "shape_trivia": {"uz": "Dunyodagi eng katta dengizga chiqish yo'li bo'lmagan (landlocked) dasht davlati", "ru": "Крупнейшее в мире государство без выхода к Мировому океану", "en": "World's largest landlocked country, spanning vast Eurasian steppes"}},
    {"code": "sa", "shape_trivia": {"uz": "Arabiston yarimorolining asosiy qismini egallagan ulkan sahro konturi", "ru": "Занимает почти весь Аравийский полуостров между Красным морем и Заливом", "en": "Occupies roughly 80 percent of the vast Arabian Peninsula"}},
    {"code": "za", "shape_trivia": {"uz": "Afrika qit'asining eng janubiy burchagi, ichida Lesotoni to'liq o'rab olgan", "ru": "Южная оконечность Африки, окружающая анклав Лесото", "en": "Southern tip of the continent completely enclosing the enclave of Lesotho"}},
    {"code": "mg", "shape_trivia": {"uz": "Afrika sharqidagi Hind okeanida joylashgan ulkan orol", "ru": "Четвертый по величине остров в мире у восточного берега Африки", "en": "Fourth-largest island on Earth, isolated in the Indian Ocean"}},
    {"code": "mx", "shape_trivia": {"uz": "Kaliforniya yarimoroli va Yukatan burunlari bilan boylangan kontur", "ru": "Характерный «рог изобилия» с полуостровами Калифорния и Юкатан", "en": "Curving horn of plenty bordered by Baja California and Yucatan"}},
    {"code": "ar", "shape_trivia": {"uz": "Janubiy Amerika janubidagi uchburchak shaklidagi Patagoniya o'lkasi", "ru": "Сужающийся к югу континент с Патагонией и Огненной Землей", "en": "Inverted triangular landmass tapering down to Tierra del Fuego"}},
    {"code": "pe", "shape_trivia": {"uz": "Tinch okeani sohillari va Amazonka havzasi tutashgan And o'lkasi", "ru": "Характерный изгиб тихоокеанского побережья Южной Америки", "en": "Notched western coastline cradled against the high Andes"}},
    {"code": "au", "shape_trivia": {"uz": "Janubiy yarim shardagi alohida qit'a-davlat va Tasmaniya oroli", "ru": "Целый континент-остров в Южном полушарии плюс Тасмания", "en": "Distinctive island-continent anchored by the island of Tasmania"}},
    {"code": "nz", "shape_trivia": {"uz": "Kuk bo'g'ozi bilan ajralgan Shimoliy va Janubiy ikki yirik orol", "ru": "Два главных вытянутых острова (Северный и Южный) в Тихом океане", "en": "Two main long islands (North and South) in the southwestern Pacific"}},
    {"code": "kr", "shape_trivia": {"uz": "Koreys yarimorolining 38-paralleldan janubdagi yarmi", "ru": "Южная половина Корейского полуострова со множеством островов", "en": "Southern half of the rugged Korean Peninsula"}},
    {"code": "id", "shape_trivia": {"uz": "Sumatra, Yava, Kalimantan, Sulavesi va Papua orollaridan iborat ulkan arxipelag", "ru": "Огромный пояс из тысяч экваториальных островов", "en": "Vast equatorial archipelago spanning over 17,000 islands"}},
    {"code": "th", "shape_trivia": {"uz": "Fil boshi va xartumi shakliga o'xshash Janubi-Sharqiy Osiyo davlati", "ru": "Очертания напоминают голову слона с хоботом вдоль Малакки", "en": "Resembles the head and trunk of an elephant dipping into Malaya"}},
    {"code": "vn", "shape_trivia": {"uz": "Janubiy Xitoy dengizi sohilida cho'zilgan 'S' harfi shaklidagi mamlakat", "ru": "Вытянутая узкая полоса в форме буквы «S» вдоль побережья", "en": "Elongated narrow coastal strip shaped distinctly like the letter 'S'"}},
    {"code": "cu", "shape_trivia": {"uz": "Meksika qo'ltig'i kirishida joylashgan timsoh shaklidagi Karib oroli", "ru": "Крупнейший карибский остров, силуэт которого напоминает крокодила", "en": "Long Caribbean island affectionately likened to the shape of a caiman"}},
    {"code": "pt", "shape_trivia": {"uz": "Pireney yarimorolining eng g'arbidagi Atlantika bo'yi to'rtburchagi", "ru": "Прямоугольник на крайнем западе Европы вдоль Атлантического океана", "en": "Compact Atlantic rectangle forming the western face of Iberia"}},
    {"code": "nl", "shape_trivia": {"uz": "Reyndan shimoldagi to'g'onlar va Eysselmer ko'li bilan ajralib turuvchi kontur", "ru": "Низменная земля у Северного моря с заливом Эйсселмер", "en": "Low-lying coastal nation notched by the Zuiderzee / IJsselmeer"}},
    {"code": "ch", "shape_trivia": {"uz": "Alp tog'lari markazida qisilib turgan ixcham neytral davlat", "ru": "Компактная альпийская страна в самом сердце Западной Европы", "en": "Compact landlocked puzzle-piece nestled high in the Alps"}},
    {"code": "at", "shape_trivia": {"uz": "Sharqdan g'arbga qarab cho'zilgan gitara yoki skripka shaklidagi davlat", "ru": "Очертания напоминают гитару или куриную ножку, вытянутую с запада на восток", "en": "Elongated shape tapering west into the Tyrol, resembling a guitar"}},
    {"code": "pl", "shape_trivia": {"uz": "Markaziy Yevropadagi deyarli yumaloq/to'rtburchak tekislik konturi", "ru": "Равнинное государство почти правильной квадратной формы у Балтики", "en": "Broad, roughly circular expanse spreading from the Carpathians to Baltic"}},
    {"code": "ua", "shape_trivia": {"uz": "Sharqiy Yevropadagi Qora dengiz sohiliga ega eng katta hududiy davlat", "ru": "Крупнейшая страна, целиком находящаяся в Европе, с побережьем Черного моря", "en": "Expansive Eastern European nation bordering the Black Sea"}},
    {"code": "ge", "shape_trivia": {"uz": "Kavkaz tizmalari va Qora dengiz oralig'idagi tog'li mamlakat", "ru": "Горная страна между Большим Кавказом и Черным морем", "en": "Mountainous buffer between the Greater Caucasus and Black Sea"}},
    {"code": "am", "shape_trivia": {"uz": "Kavkazortidagi Sevan ko'liga ega ixcham tog'lik davlat", "ru": "Небольшая высокогорная страна с озером Севан", "en": "Compact, rugged highland contour wrapped around Lake Sevan"}},
    {"code": "az", "shape_trivia": {"uz": "Kaspiy dengiziga burgut tumshug'i kabi turtib chiqqan Apsheron yarimoroli", "ru": "Апшеронский полуостров, клювом вдающийся в Каспийское море", "en": "Features the distinctive Absheron peninsula jutting into the Caspian"}},
    {"code": "kg", "shape_trivia": {"uz": "Tyan-Shan tog'lari orasida Issiqko'lni quchoqlab yotgan kontur", "ru": "Горные хребты Тянь-Шаня с синим пятном озера Иссык-Куль в центре", "en": "Dramatic mountainous outline cupping the jewel of Lake Issyk-Kul"}},
    {"code": "tj", "shape_trivia": {"uz": "Pomir va So'g'd vodiysini bog'lovchi tog'li kontur", "ru": "Высокогорное государство с Памиром и «ручкой» Согдийской области", "en": "High mountain topography with a northern hook reaching Fergana"}},
    {"code": "tm", "shape_trivia": {"uz": "Qoraqum sahrosi va Kaspiy dengizi sharqiy sohillari", "ru": "Пустыня Каракумы и восточное побережье Каспия", "en": "Vast desert expanse flanking the eastern shoreline of the Caspian"}},
    {"code": "is", "shape_trivia": {"uz": "Shimoliy Atlantikadagi yolg'iz vulqonli muz orol", "ru": "Одинокий вулканический остров гейзеров и ледников у полярного круга", "en": "Solitary volcanic island of glaciers and fjords near the Arctic Circle"}},
    {"code": "ie", "shape_trivia": {"uz": "Buyuk Britaniya g'arbidagi yashil orol (Shimoliy Irlandiyasiz)", "ru": "«Изумрудный остров» к западу от Великобритании", "en": "The Emerald Isle contour framing the western edge of Europe"}},
    {"code": "ke", "shape_trivia": {"uz": "Sharqiy Afrikadagi ekvator chizig'i kesib o'tuvchi davlat", "ru": "Восточноафриканская страна на экваторе с выходом к Индийскому океану", "en": "Equatorial East African nation bordering Lake Victoria and Indian Ocean"}},
    {"code": "ma", "shape_trivia": {"uz": "Gibraltar bo'g'ozi qarshisidagi shimoliy-g'arbiy Afrika burchagi", "ru": "Северо-западный угол Африки у Гибралтарского пролива", "en": "Northwestern corner of Africa standing guard over the Strait of Gibraltar"}},
]

CONTOUR_BY_CODE: Dict[str, dict] = {item["code"]: item for item in CONTOUR_DATA}

def get_contour_url(country_code: str) -> str:
    """Returns the direct high-res outline PNG URL for the given country code."""
    code = country_code.lower()
    return f"https://raw.githubusercontent.com/djaiss/mapsicon/master/all/{code}/1024.png"

def get_contour_info(country_code: str) -> Optional[dict]:
    """Returns contour trivia and metadata for the given country code."""
    return CONTOUR_BY_CODE.get(country_code.lower())
