"""
World Landmarks and Street Views Database for GeoGuessr Mode.
Each entry has multilingual names, country code, high-quality image URL, clues, and fun facts.
"""

LANDMARKS = [
    {
        "id": "registan",
        "name": {"en": "Registan Square", "ru": "Площадь Регистан", "uz": "Registon maydoni"},
        "country_code": "uz",
        "city": {"en": "Samarkand", "ru": "Самарканд", "uz": "Samarqand"},
        "image_url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Heart of the ancient city of Samarkand, framed by three magnificent Islamic madrasahs.", "ru": "Сердце древнего Самарканда, окруженное тремя величественными медресе.", "uz": "Qadimiy Samarqand markazi, uchta muhtasham madrasa bilan o'ralgan."},
        "fun_fact": {"en": "Registan means 'sandy place' or 'desert' in Persian.", "ru": "Регистан переводится с персидского как «песчаное место».", "uz": "Registon forscha 'qumli joy' yoki 'sahro' degan ma'noni anglatadi."}
    },
    {
        "id": "eiffel_tower",
        "name": {"en": "Eiffel Tower", "ru": "Эйфелева башня", "uz": "Eyfel minorasi"},
        "country_code": "fr",
        "city": {"en": "Paris", "ru": "Париж", "uz": "Parij"},
        "image_url": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Iconic wrought-iron lattice tower on the Champ de Mars beside the Seine River.", "ru": "Знаменитая ажурная металлическая башня на Марсовом поле у реки Сена.", "uz": "Sena daryosi bo'yidagi Mars maydonida joylashgan ramziy metall minora."},
        "fun_fact": {"en": "It grows about 15 cm taller during summer due to thermal expansion of the iron.", "ru": "Летом башня вырастает примерно на 15 см из-за расширения металла на жаре.", "uz": "Yozda quyosh issig'ida metall kengayib, minora 15 sm gacha balandlashadi."}
    },
    {
        "id": "statue_of_liberty",
        "name": {"en": "Statue of Liberty", "ru": "Статуя Свободы", "uz": "Ozodlik haykali"},
        "country_code": "us",
        "city": {"en": "New York", "ru": "Нью-Йорк", "uz": "Nyu-York"},
        "image_url": "https://images.unsplash.com/photo-1605130284535-11dd9eedc58a?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Colossal neoclassical sculpture on Liberty Island welcoming immigrants.", "ru": "Колоссальная неоклассическая скульптура на острове Свободы.", "uz": "Ozodlik orolidagi ulkan neoklassik haykal."},
        "fun_fact": {"en": "It was a gift from the people of France to the United States in 1886.", "ru": "Это был подарок от народа Франции Соединённым Штатам в 1886 году.", "uz": "1886 yilda Fransiya xalqi tomonidan AQShga sovg'a qilingan."}
    },
    {
        "id": "colosseum",
        "name": {"en": "Colosseum", "ru": "Колизей", "uz": "Kolizey"},
        "country_code": "it",
        "city": {"en": "Rome", "ru": "Рим", "uz": "Rim"},
        "image_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Massive ancient stone amphitheatre where gladiators once fought.", "ru": "Древнеримский амфитеатр, где когда-то сражались гладиаторы.", "uz": "Qadimgi Rim amfiteatri, bu yerda gladiatorlar jang qilgan."},
        "fun_fact": {"en": "Could hold between 50,000 and 80,000 spectators in antiquity.", "ru": "В древности вмещал от 50 000 до 80 000 зрителей.", "uz": "Qadimgi davrda 50 000 dan 80 000 gacha tomoshabinni sig'dira olgan."}
    },
    {
        "id": "taj_mahal",
        "name": {"en": "Taj Mahal", "ru": "Тадж-Махал", "uz": "Toj Mahal"},
        "country_code": "in",
        "city": {"en": "Agra", "ru": "Агра", "uz": "Agra"},
        "image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "White marble mausoleum commissioned by Mughal emperor Shah Jahan for his favorite wife.", "ru": "Мавзолей из белого мрамора, построенный падишахом Шах-Джаханом в память о жене.", "uz": "Boburiy hukmdor Shoh Jahon suyukli xotini xotirasiga qurdirgan oq marmar maqbara."},
        "fun_fact": {"en": "It changes color depending on the light: pinkish in morning, milky white in evening, golden at night.", "ru": "Меняет оттенок в зависимости от времени суток: розоватый утром, белый днем и золотистый ночью.", "uz": "Kun vaqtiga qarab rangi o'zgaradi: tongda pushti, kunduzi oq, tunda esa tillarang tovlanadi."}
    },
    {
        "id": "great_wall_china",
        "name": {"en": "Great Wall of China", "ru": "Великая Китайская стена", "uz": "Buyuk Xitoy devori"},
        "country_code": "cn",
        "city": {"en": "Beijing region", "ru": "Регион Пекина", "uz": "Pekin viloyati"},
        "image_url": "https://images.unsplash.com/photo-1508804185872-d7badad00f7d?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Ancient series of fortifications stretching thousands of miles across northern borders.", "ru": "Древняя цепь оборонительных укреплений протяженностью в тысячи километров.", "uz": "Shimoliy chegara bo'ylab minglab kilometrga cho'zilgan ulkan mudofaa inshooti."},
        "fun_fact": {"en": "Its total length with all branches is over 21,000 kilometers.", "ru": "Общая протяжённость со всеми ответвлениями превышает 21 000 километров.", "uz": "Barcha tarmoqlari bilan umumiy uzunligi 21 000 kilometrdan oshadi."}
    },
    {
        "id": "pyramids_giza",
        "name": {"en": "Great Pyramids of Giza", "ru": "Пирамиды Гизы", "uz": "Giza ehromlari"},
        "country_code": "eg",
        "city": {"en": "Cairo / Giza", "ru": "Каир / Гиза", "uz": "Qohira / Giza"},
        "image_url": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Ancient monumental royal tombs guarded by the Great Sphinx on the desert plateau.", "ru": "Древние царские гробницы на плато в пустыне, охраняемые Большим сфинксом.", "uz": "Sahro platosida Katta Sfinks qo'riqlayotgan qadimiy shohlar maqbaralari."},
        "fun_fact": {"en": "The oldest and only remaining intact wonder of the ancient world.", "ru": "Самое древнее и единственное сохранившееся чудо древнего мира.", "uz": "Qadimgi dunyoning yetti mo'jizasidan bugungi kungacha saqlanib qolgan yagona mo'jiza."}
    },
    {
        "id": "machu_picchu",
        "name": {"en": "Machu Picchu", "ru": "Мачу-Пикчу", "uz": "Machu-Pikchu"},
        "country_code": "pe",
        "city": {"en": "Cusco Region", "ru": "Куско", "uz": "Kusko"},
        "image_url": "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "15th-century Inca citadel located high on a mountain ridge above the Sacred Valley.", "ru": "Цитадель инков XV века, расположенная высоко на горном хребте в Андах.", "uz": "And tog'lari cho'qqisida joylashgan XV asrga oid qadimiy Inka shahri."},
        "fun_fact": {"en": "Built without mortar — stones fit together so tightly a knife blade cannot slip between them.", "ru": "Построен без цемента — камни подогнаны так плотно, что между ними не пролезет лезвие ножа.", "uz": "Qorishmasiz qurilgan — toshlar shunday zich terilganki, orasiga pichoq tig'i ham kirmaydi."}
    },
    {
        "id": "christ_redeemer",
        "name": {"en": "Christ the Redeemer", "ru": "Христос-Искупитель", "uz": "Najotkor Iso haykali"},
        "country_code": "br",
        "city": {"en": "Rio de Janeiro", "ru": "Рио-де-Жанейро", "uz": "Rio-de-Janeyro"},
        "image_url": "https://images.unsplash.com/photo-1598970434795-0c54fe7c0648?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Giant Art Deco statue overlooking a coastal city from the summit of Mount Corcovado.", "ru": "Гигантская статуя в стиле ар-деко на вершине горы Корковаду с видом на залив.", "uz": "Korkovadu tog'i cho'qqisidan shahar va dengizga qarab turgan ulkan haykal."},
        "fun_fact": {"en": "Stands 38 meters tall and was named one of the New Seven Wonders of the World.", "ru": "Высота статуи 38 метров, включена в Новые семь чудес света.", "uz": "Balandligi 38 metr bo'lib, Yangi Dunyo Mo'jizalari ro'yxatiga kiritilgan."}
    },
    {
        "id": "sydney_opera_house",
        "name": {"en": "Sydney Opera House", "ru": "Сиднейский оперный театр", "uz": "Sidney opera teatri"},
        "country_code": "au",
        "city": {"en": "Sydney", "ru": "Сидней", "uz": "Sidney"},
        "image_url": "https://images.unsplash.com/photo-1624138784614-87fd1b6528f8?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Iconic performing arts centre famous for its distinctive sail-shaped shell design in the harbor.", "ru": "Театр в бухте, знаменитый своей формой парусов или ракушек.", "uz": "Bandargohda joylashgan, yelkan shaklidagi o'ziga xos arxitekturaga ega opera binosi."},
        "fun_fact": {"en": "The roof consists of over 1 million ceramic tiles imported from Sweden.", "ru": "Крыша покрыта более чем 1 миллионом керамических плиток из Швеции.", "uz": "Tomi Shvetsiyadan keltirilgan 1 milliondan ortiq keramik koshinlar bilan qoplangan."}
    },
    {
        "id": "big_ben",
        "name": {"en": "Big Ben & Palace of Westminster", "ru": "Биг-Бен и Вестминстерский дворец", "uz": "Big Ben va Vestminster saroyi"},
        "country_code": "gb",
        "city": {"en": "London", "ru": "Лондон", "uz": "London"},
        "image_url": "https://images.unsplash.com/photo-1529655683826-aba9b3e77383?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Gothic clock tower standing tall by the River Thames next to Parliament.", "ru": "Знаменитая неоготическая часовая башня у реки Темзы возле парламента.", "uz": "Temza daryosi bo'yida parlament binosi yonida qad ko'targan soatli minora."},
        "fun_fact": {"en": "Big Ben is actually the nickname of the giant 13-ton bell inside the tower.", "ru": "«Биг-Бен» — это прозвище 13-тонного колокола внутри часовой башни.", "uz": "'Big Ben' aslida minoraning emas, uning ichidagi 13 tonnalik katta qo'ng'iroqning nomidir."}
    },
    {
        "id": "petra",
        "name": {"en": "Petra (The Treasury / Al-Khazneh)", "ru": "Петра (Эль-Хазне)", "uz": "Petra (Al-Xazna)"},
        "country_code": "jo",
        "city": {"en": "Ma'an Governorate", "ru": "Вади-Муса", "uz": "Vodi-Muso"},
        "image_url": "https://images.unsplash.com/photo-1548786811-dd6e453ccca7?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Ancient Nabataean city carved entirely into pink rose sandstone canyon walls.", "ru": "Древний город набатеев, высеченный прямо в розовых скалах каньона.", "uz": "Pushti qoyatosh daralariga o'yib ishlangan qadimiy Nabatiylar poytaxti."},
        "fun_fact": {"en": "Often called the Rose City due to the color of the stone from which it is carved.", "ru": "Называется Розовым городом из-за цвета песчаника, в котором он высечен.", "uz": "Qoyalarning rangi tufayli 'Pushti shahar' deb ham ataladi."}
    },
    {
        "id": "sagrada_familia",
        "name": {"en": "Sagrada Familia", "ru": "Саграда Фамилия", "uz": "Sagrada Familiya"},
        "country_code": "es",
        "city": {"en": "Barcelona", "ru": "Барселона", "uz": "Barselona"},
        "image_url": "https://images.unsplash.com/photo-1587595431973-160d0d94add1?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Astonishing unfinished modernist basilica designed by Antoni Gaudí.", "ru": "Потрясающий модернистский собор, творение архитектора Антонио Гауди.", "uz": "Me'mor Antoni Gaudi tomonidan loyihalashtirilgan betakror neo-gotik sobor."},
        "fun_fact": {"en": "Under construction since 1882 — it has taken longer to build than the Egyptian Pyramids!", "ru": "Строится с 1882 года — дольше, чем возводились египетские пирамиды!", "uz": "1882 yildan beri qurilmoqda — qurilishi Misr ehromlaridan ham ko'proq vaqt olmoqda!"}
    },
    {
        "id": "burj_khalifa",
        "name": {"en": "Burj Khalifa", "ru": "Бурдж-Халифа", "uz": "Burj Xalifa"},
        "country_code": "ae",
        "city": {"en": "Dubai", "ru": "Дубай", "uz": "Dubay"},
        "image_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Tallest structure and skyscraper in the world soaring 828 meters high.", "ru": "Самое высокое здание и небоскреб в мире высотой 828 метров.", "uz": "Balandligi 828 metr bo'lgan dunyodagi eng baland bino va osmono'par inshoot."},
        "fun_fact": {"en": "You can watch the sunset from the ground, take the elevator up, and watch it set again!", "ru": "Можно увидеть закат у подножия, подняться на лифте и посмотреть его во второй раз!", "uz": "Pastda turib quyosh botishini ko'rib, tezkor liftda tepaga chiqib yana bir bor quyosh botishini tomosha qilish mumkin!"}
    },
    {
        "id": "mount_fuji",
        "name": {"en": "Mount Fuji", "ru": "Гора Фудзияма", "uz": "Fudzi tog'i"},
        "country_code": "jp",
        "city": {"en": "Honshu Island", "ru": "Остров Хонсю", "uz": "Xonsyu oroli"},
        "image_url": "https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Perfect symmetrical snow-capped sacred volcano and national symbol.", "ru": "Симметричный священный вулкан с заснеженной вершиной, символ страны.", "uz": "Usti qor bilan qoplangan muqaddas vulqon va milliy timsol."},
        "fun_fact": {"en": "It is an active stratovolcano that last erupted in 1707.", "ru": "Это действующий вулкан, последнее извержение которого произошло в 1707 году.", "uz": "Faol vulqon hisoblanadi, oxirgi marta 1707 yilda otilgan."}
    },
    {
        "id": "acropolis_athens",
        "name": {"en": "Acropolis of Athens (Parthenon)", "ru": "Афинский Акрополь (Парфенон)", "uz": "Afina Akropoli (Parfenon)"},
        "country_code": "gr",
        "city": {"en": "Athens", "ru": "Афины", "uz": "Afina"},
        "image_url": "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Ancient citadel on a rocky outcrop containing the Parthenon temple overlooking the capital.", "ru": "Древняя цитадель на скале с храмом Парфенон, возвышающаяся над столицей.", "uz": "Toshli qoya ustidagi Parfenon ibodatxonasi joylashgan qadimiy me'moriy ansambl."},
        "fun_fact": {"en": "Dedicated to the goddess Athena, protector of the ancient city.", "ru": "Был посвящен богине Афине, покровительнице города.", "uz": "Afina shahrining homiysi ma'buda Afina sharafiga bunyod etilgan."}
    },
    {
        "id": "saint_basils",
        "name": {"en": "Saint Basil's Cathedral", "ru": "Храм Василия Блаженного", "uz": "Vasiliy Blajenniy ibodatxonasi"},
        "country_code": "ru",
        "city": {"en": "Moscow", "ru": "Москва", "uz": "Moskva"},
        "image_url": "https://images.unsplash.com/photo-1513326738677-b964603b136d?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Iconic cathedral with brightly colored onion domes on Red Square.", "ru": "Храм с яркими узорчатыми куполами-луковицами на Красной площади.", "uz": "Qizil maydonda joylashgan yorqin naqshli piyozsimon gumbazli mashhur bino."},
        "fun_fact": {"en": "Legend says Ivan the Terrible blinded the architects so they could never build anything as beautiful.", "ru": "По легенде, Иван Грозный ослепил зодчих, чтобы они не смогли повторить такую красоту.", "uz": "Rivoyatga ko'ra, shoh Ivan Grozniy me'morlar bunday go'zal binoni boshqa qura olmasligi uchun ularning ko'zini ko'r qilgan."}
    },
    {
        "id": "neuschwanstein",
        "name": {"en": "Neuschwanstein Castle", "ru": "Замок Нойшванштайн", "uz": "Noyshvanshtayn qal'asi"},
        "country_code": "de",
        "city": {"en": "Bavaria", "ru": "Бавария", "uz": "Bavariya"},
        "image_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Fairy-tale 19th-century Romanesque Revival palace perched on a rugged hill in the Alps.", "ru": "Сказочный замок XIX века на скалистом холме в предгорьях Альп.", "uz": "Alp tog'lari etagidagi qoyada qad ko'targan ertaknamo qirollik qasri."},
        "fun_fact": {"en": "Served as the real-life inspiration for Disney's Sleeping Beauty castle.", "ru": "Послужил прообразом замка Спящей красавицы в Диснейленде.", "uz": "Disneyning 'Uyqudagi go'zal' multfilmidagi ertaknamo qasrga prototip bo'lgan."}
    },
    {
        "id": "brandenburg_gate",
        "name": {"en": "Brandenburg Gate", "ru": "Бранденбургские ворота", "uz": "Brandenburg darvozasi"},
        "country_code": "de",
        "city": {"en": "Berlin", "ru": "Берлин", "uz": "Berlin"},
        "image_url": "https://images.unsplash.com/photo-1560969184-10fe8719e047?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "18th-century neoclassical monument crowned with the Quadriga chariot in the capital.", "ru": "Неоклассические триумфальные ворота с квадригой, символ объединения страны.", "uz": "Tepasida to'rtta otli arava (kvadriga) o'rnatilgan g'alaba darvozasi."},
        "fun_fact": {"en": "During the Cold War, it stood directly in the restricted border zone between East and West.", "ru": "Во время Холодной войны находились прямо в запретной зоне у Берлинской стены.", "uz": "Sovuq urush davrida Sharqiy va G'arbiy Berlin chegarasidagi yopiq zonada qolgan edi."}
    },
    {
        "id": "leaning_tower_pisa",
        "name": {"en": "Leaning Tower of Pisa", "ru": "Пизанская башня", "uz": "Piza minorasi"},
        "country_code": "it",
        "city": {"en": "Pisa", "ru": "Пиза", "uz": "Piza"},
        "image_url": "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Freestanding bell tower famous worldwide for its unintended four-degree tilt.", "ru": "Знаменитая колокольня собора, наклонившаяся из-за мягкого грунта.", "uz": "Zamin cho'kishi oqibatida 4 daraja qiyshayib qolgan dunyoga mashhur qo'ng'iroqxona minorasi."},
        "fun_fact": {"en": "Took nearly 200 years to build, from 1173 to 1372.", "ru": "Строительство башни заняло почти 200 лет (с 1173 по 1372 год).", "uz": "Qurilishi deyarli 200 yil (1173 yildan 1372 yilgacha) davom etgan."}
    },
    {
        "id": "chichen_itza",
        "name": {"en": "Chichen Itza (El Castillo)", "ru": "Чичен-Ица (Эль-Кастильо)", "uz": "Chichen-Itsa (El-Kastilo)"},
        "country_code": "mx",
        "city": {"en": "Yucatan", "ru": "Юкатан", "uz": "Yukatan"},
        "image_url": "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Large pre-Columbian step-pyramid city built by the Maya civilization.", "ru": "Древний город цивилизации майя со ступенчатой пирамидой пернатого змея Кукулькана.", "uz": "Mayya tamadduniga tegishli qadimiy piramida va muqaddas shahar."},
        "fun_fact": {"en": "During equinoxes, the afternoon sun creates the illusion of a snake crawling down the stairs.", "ru": "В дни равноденствия тени создают оптическую иллюзию ползущей змеи.", "uz": "Kun va tun tenglashgan kunlarda quyosh nuri zinalar bo'ylab ilon sudralayotgani ko'rinishini hosil qiladi."}
    },
    {
        "id": "angkor_wat",
        "name": {"en": "Angkor Wat", "ru": "Ангкор-Ват", "uz": "Angkor-Vat"},
        "country_code": "kh",
        "city": {"en": "Siem Reap", "ru": "Сиемреап", "uz": "Siemreap"},
        "image_url": "https://images.unsplash.com/photo-1569154941061-e231b4725ef1?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Enormous temple complex and the largest religious monument in the world.", "ru": "Огромный храмовый комплекс в джунглях, крупнейшее религиозное сооружение в мире.", "uz": "Chakalakzor ichidagi ulkan ibodatxona majmuasi, dunyodagi eng yirik diniy inshoot."},
        "fun_fact": {"en": "It appears on the country's national flag.", "ru": "Изображение храма украшает государственный флаг страны.", "uz": "Ushbu ibodatxona tasviri mamlakatning davlat bayrog'ida aks ettirilgan."}
    },
    {
        "id": "hagia_sophia",
        "name": {"en": "Hagia Sophia", "ru": "Айя-София", "uz": "Ayo Sofiya"},
        "country_code": "tr",
        "city": {"en": "Istanbul", "ru": "Стамбул", "uz": "Istanbul"},
        "image_url": "https://images.unsplash.com/photo-1541432901042-2d8bd64b4a9b?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Historic major basilica with massive central dome and four minarets on the Bosphorus strait.", "ru": "Величественный собор-мечеть с огромным куполом и четырьмя минаретами у Босфора.", "uz": "Bosfor bo'g'ozi bo'yida joylashgan ulkan gumbazli va to'rtta minorali muazzam ibodatxona."},
        "fun_fact": {"en": "Served as an Eastern Orthodox cathedral for almost 1,000 years before becoming an imperial mosque.", "ru": "Почти 1000 лет был главным православным собором, затем стал мечетью.", "uz": "Deyarli 1000 yil pravoslav sobori bo'lgan, keyin esa masjidga aylantirilgan."}
    },
    {
        "id": "table_mountain",
        "name": {"en": "Table Mountain", "ru": "Столовая гора", "uz": "Stol tog'i"},
        "country_code": "za",
        "city": {"en": "Cape Town", "ru": "Кейптаун", "uz": "Keyptaun"},
        "image_url": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Flat-topped mountain forming a prominent landmark overlooking the coastal city.", "ru": "Гора с плоской вершиной, возвышающаяся над прибрежным городом.", "uz": "Sohilbo'yi shahri tepasida cho'qqisi stol kabi tekis bo'lgan mashhur tog'."},
        "fun_fact": {"en": "One of the oldest mountains on Earth, over 240 million years old.", "ru": "Одна из старейших гор на Земле, ее возраст более 240 миллионов лет.", "uz": "Yer yuzidagi eng qadimiy tog'lardan biri, yoshi 240 million yildan oshadi."}
    },
    {
        "id": "niagara_falls",
        "name": {"en": "Niagara Falls (Horseshoe Falls)", "ru": "Ниагарский водопад", "uz": "Niagara sharsharasi"},
        "country_code": "ca",
        "city": {"en": "Ontario", "ru": "Онтарио", "uz": "Ontario"},
        "image_url": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Massive horseshoe-shaped cascades with roaring thunderous water on the international border.", "ru": "Мощный водопад в форме подковы с грохотом воды на границе двух государств.", "uz": "Ikki davlat chegarasida taqa shaklida quyiluvchi haybatli sharshara."},
        "fun_fact": {"en": "Over 3,160 tons of water flow over the falls every single second.", "ru": "Каждую секунду с водопада обрушивается более 3160 тонн воды.", "uz": "Har bir soniyada sharsharadan 3160 tonnadan ortiq suv quyiladi."}
    },
    {
        "id": "moai_statues",
        "name": {"en": "Moai Statues of Easter Island", "ru": "Статуи Моаи на острове Пасхи", "uz": "Pasxa orolidagi Moai haykallari"},
        "country_code": "cl",
        "city": {"en": "Rapa Nui", "ru": "Рапа-Нуи", "uz": "Rapa-Nui"},
        "image_url": "https://images.unsplash.com/photo-1510097467424-192d713fd8b2?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Mysterious monumental monolithic human figures carved by the Rapa Nui people in the remote Pacific.", "ru": "Монолитные каменные истуканы с крупными головами на далеком острове в Тихом океане.", "uz": "Tinch okeanidagi chekka orolda qad rostlagan ulkan tosh bosh haykallar."},
        "fun_fact": {"en": "Almost all moai face inland toward the villages, rather than out toward the sea.", "ru": "Почти все статуи смотрят внутрь острова на деревни, а не в сторону океана.", "uz": "Deyarli barcha haykallar okeanga emas, orol ichkarisidagi qishloqlarga qarab turadi."}
    },
    {
        "id": "marina_bay_sands",
        "name": {"en": "Marina Bay Sands", "ru": "Марина Бэй Сэндс", "uz": "Marina Bey Sends"},
        "country_code": "sg",
        "city": {"en": "Singapore", "ru": "Сингапур", "uz": "Singapur"},
        "image_url": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Integrated resort of three soaring towers joined by a sky park and infinity pool like a ship on top.", "ru": "Три небоскреба, увенчанные огромной площадкой в форме корабля с бассейном на крыше.", "uz": "Usti kema shaklidagi istirohat bog'i bilan birlashtirilgan uchta osmono'par bino."},
        "fun_fact": {"en": "The rooftop infinity pool is the largest elevated body of water in the world at 191 meters up.", "ru": "Пейзажный бассейн на крыше на высоте 191 м — самый большой высотный открытый бассейн.", "uz": "191 metr balandlikdagi tomsimon ochiq basseyn dunyodagi eng katta balandlikdagi hovuzdir."}
    },
    {
        "id": "petronas_towers",
        "name": {"en": "Petronas Twin Towers", "ru": "Башни-близнецы Петронас", "uz": "Petronas egizak minoralari"},
        "country_code": "my",
        "city": {"en": "Kuala Lumpur", "ru": "Куала-Лумпур", "uz": "Kuala-Lumpur"},
        "image_url": "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Twin 88-floor supertall skyscrapers joined by a double-decker skybridge.", "ru": "Башни-близнецы высотой 88 этажей, соединенные двухэтажным воздушным мостом.", "uz": "88 qavatli egizak osmono'par minoralar, oraliq osma ko'prik bilan tutashgan."},
        "fun_fact": {"en": "Held the title of the tallest buildings in the world from 1998 to 2004.", "ru": "С 1998 по 2004 год носили титул самых высоких зданий в мире.", "uz": "1998 yildan 2004 yilgacha dunyodagi eng baland bino unvoniga ega bo'lgan."}
    },
    {
        "id": "hallstatt",
        "name": {"en": "Hallstatt Village", "ru": "Деревня Гальштат", "uz": "Xalshtatt qishlog'i"},
        "country_code": "at",
        "city": {"en": "Upper Austria", "ru": "Верхняя Австрия", "uz": "Yuqori Avstriya"},
        "image_url": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Picturesque alpine lakeside village nestled between steep mountains and shimmering water.", "ru": "Живописная альпийская деревня на берегу озера у подножия крутых гор.", "uz": "Tik tog'lar va moviy ko'l bo'yida joylashgan go'zal Alp qishlog'i."},
        "fun_fact": {"en": "Home to the world's oldest known salt mine, operating for over 7,000 years.", "ru": "Здесь находится старейшая в мире соляная шахта возрастом более 7000 лет.", "uz": "Bu yerda 7000 yildan ortiq vaqtdan beri mavjud bo'lgan dunyodagi eng qadimgi tuz koni joylashgan."}
    },
    {
        "id": "blue_mosque",
        "name": {"en": "Sultan Ahmed (Blue) Mosque", "ru": "Голубая мечеть", "uz": "Moviy masjid"},
        "country_code": "tr",
        "city": {"en": "Istanbul", "ru": "Стамбул", "uz": "Istanbul"},
        "image_url": "https://images.unsplash.com/photo-1527838832700-5059252407fa?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Historic Ottoman imperial mosque with six soaring minarets and blue interior tiles.", "ru": "Османская мечеть с шестью минаретами, украшенная голубой плиткой ручной работы.", "uz": "Oltita minorasi va moviy naqshli koshinlari bilan mashhur Usmonli me'moriy durdonasi."},
        "fun_fact": {"en": "Interior is lined with more than 20,000 handmade ceramic Iznik tiles.", "ru": "Внутри украшена более чем 20 000 керамических плиток ручной работы из Изника.", "uz": "Ichki qismi 20 000 dan ziyod qo'lda ishlangan Iznik koshinlari bilan bezatilgan."}
    },
    {
        "id": "golden_gate_bridge",
        "name": {"en": "Golden Gate Bridge", "ru": "Мост Золотые Ворота", "uz": "Oltin Darvoza ko'prigi"},
        "country_code": "us",
        "city": {"en": "San Francisco", "ru": "Сан-Франциско", "uz": "San-Fransisko"},
        "image_url": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Famous suspension bridge painted in International Orange spanning the strait to the bay.", "ru": "Знаменитый оранжевый висячий мост через одноименный пролив в залив.", "uz": "Ko'rfaz bo'g'ozi ustida qizil-to'q sariq rangga bo'yalgan dunyoga mashhur osma ko'prik."},
        "fun_fact": {"en": "Its distinct color is officially named 'International Orange'.", "ru": "Официальное название фирменного цвета моста — International Orange.", "uz": "Ko'prikning o'ziga xos rangi rasman 'Xalqaro to'q sariq' deb ataladi."}
    },
    {
        "id": "stonehenge",
        "name": {"en": "Stonehenge", "ru": "Стоунхендж", "uz": "Stounxendj"},
        "country_code": "gb",
        "city": {"en": "Wiltshire", "ru": "Уилтшир", "uz": "Uiltshir"},
        "image_url": "https://images.unsplash.com/photo-1599833975787-5c143f373c30?auto=format&fit=crop&w=1200&q=80",
        "clue": {"en": "Prehistoric circle of standing stones erected on Salisbury Plain thousands of years ago.", "ru": "Доисторический кромлех из гигантских камней на равнине Солсбери.", "uz": "Salisberi tekisligida qad ko'targan ming yillik ulkan tosh halqasi."},
        "fun_fact": {"en": "Aligned with the rising sun on the summer solstice and sunset on the winter solstice.", "ru": "Камни ориентированы точно по восходу солнца в день летнего солнцестояния.", "uz": "Toshlar yozgi quyosh turishi va qishki botishi nuqtalari bilan mukammal moslashtirilgan."}
    }
]

LANDMARKS_BY_ID = {l["id"]: l for l in LANDMARKS}

# Ensure both clue and hint keys exist on each entry
for lm in LANDMARKS:
    if "clue" in lm and "hint" not in lm:
        lm["hint"] = lm["clue"]
    elif "hint" in lm and "clue" not in lm:
        lm["clue"] = lm["hint"]

def get_landmark(lid: str):
    """Retrieve landmark by unique ID."""
    return LANDMARKS_BY_ID.get(lid)

get_landmark_by_id = get_landmark

def get_random_landmarks(count: int = 1):
    """Sample random landmarks without replacement."""
    import random
    sample_size = min(count, len(LANDMARKS))
    return random.sample(LANDMARKS, sample_size)

