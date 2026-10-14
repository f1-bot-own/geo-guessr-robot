/**
 * GeoGuessr Telegram Mini App Client
 * Leaflet.js Interactive Guess Map + Telegram WebApp SDK Integration
 */

// Initialize Telegram WebApp SDK
const tg = window.Telegram?.WebApp;
if (tg) {
  tg.ready();
  tg.expand();
  if (tg.enableClosingConfirmation) {
    tg.enableClosingConfirmation();
  }
}

// Translations Dictionary
const I18N = {
  uz: {
    round: "Raund",
    score: "ball",
    loading: "Rasm yuklanmoqda...",
    drivingRight: "Harakat: O'ng tomon",
    drivingLeft: "Harakat: Chap tomon",
    streetView: "Ko'cha manzarasi",
    landmark: "Tarixiy obida",
    hintMap: "Xaritani bosing va taxminiy joyni belgilang 📍",
    guessBtn: "📍 Taxmin qilish",
    distance: "Masofa",
    pointsAwarded: "To'plangan ball",
    funFactPrefix: "💡 Fakt:",
    nextRound: "Keyingi raund ➡️",
    gameOver: "O'YIN YAKUNLANDI!",
    submitScore: "📤 Natijani Botga Saqlash",
    playAgain: "🔄 Qayta O'ynash",
    rankExplorer: "🌟 Yangi Sayyoh",
    rankNavigator: "🧭 Mohir Navigator",
    rankMaster: "👑 Dunyo Geografi",
    rankLegend: "⚡ GeoGuessr Afsonasi",
    nearPerfect: "Dahshatli aniqlik! 🎯",
    close: "Juda yaqin! 👏",
    decent: "Yaxshi urinish! 👍",
    far: "Biroz uzoq ketdi! 🌍",
    panorama360: "🔄 360° Aylantiring (Panorama)",
  },
  ru: {
    round: "Раунд",
    score: "очков",
    loading: "Загрузка фото...",
    drivingRight: "Движение: Справа",
    drivingLeft: "Движение: Слева",
    streetView: "Панорама улицы",
    landmark: "Достопримечательность",
    hintMap: "Нажмите на карту, чтобы поставить метку 📍",
    guessBtn: "📍 Подтвердить догадку",
    distance: "Дистанция",
    pointsAwarded: "Получено очков",
    funFactPrefix: "💡 Факт:",
    nextRound: "Следующий раунд ➡️",
    gameOver: "ИГРА ОКОНЧЕНА!",
    submitScore: "📤 Сохранить в боте",
    playAgain: "🔄 Сыграть снова",
    rankExplorer: "🌟 Начинающий турист",
    rankNavigator: "🧭 Опытный штурман",
    rankMaster: "👑 Знаток планеты",
    rankLegend: "⚡ Легенда GeoGuessr",
    nearPerfect: "Невероятная точность! 🎯",
    close: "Очень близко! 👏",
    decent: "Хорошая попытка! 👍",
    far: "Далековато! 🌍",
    panorama360: "🔄 360° Круговой обзор (Панорама)",
  },
  en: {
    round: "Round",
    score: "pts",
    loading: "Loading image...",
    drivingRight: "Traffic: Right side",
    drivingLeft: "Traffic: Left side",
    streetView: "Street View",
    landmark: "Historical Landmark",
    hintMap: "Tap the map to place your pin 📍",
    guessBtn: "📍 Guess Location",
    distance: "Distance",
    pointsAwarded: "Points Earned",
    funFactPrefix: "💡 Fact:",
    nextRound: "Next Round ➡️",
    gameOver: "GAME OVER!",
    submitScore: "📤 Submit to Bot",
    playAgain: "🔄 Play Again",
    rankExplorer: "🌟 World Explorer",
    rankNavigator: "🧭 Master Navigator",
    rankMaster: "👑 Geo Champion",
    rankLegend: "⚡ GeoGuessr Legend",
    nearPerfect: "Incredible accuracy! 🎯",
    close: "Very close! 👏",
    decent: "Nice attempt! 👍",
    far: "A bit far off! 🌍",
    panorama360: "🔄 360° Interactive Panorama",
  }
};

// Curated Locations Database (50+ handpicked worldwide locations with exact coordinates)
const LOCATIONS = [
  {
    id: "pano_swiss_alps",
    name: { uz: "Dent de Volion (Yura tog'lari)", ru: "Вершина Дан-де-Вольон (Юра)", en: "Dent de Vaulion (Jura Mountains)" },
    country: { uz: "Shveytsariya", ru: "Швейцария", en: "Switzerland" },
    city: { uz: "Vo kantoni", ru: "Кантон Во", en: "Canton of Vaud" },
    flag: "🇨🇭",
    lat: 46.6811,
    lng: 6.3578,
    driving: "right",
    type: "streetview",
    is360: true,
    panorama: "panoramas/swiss-alps.jpg",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Dent_de_Vaulion_-_360_degree_panorama.jpg/1280px-Dent_de_Vaulion_-_360_degree_panorama.jpg",
    fact: {
      uz: "Dent de Vaulion cho'qqisidan bir vaqtning o'zida Shveytsariya va Fransiyaning 7 ta ko'li hamda Monblan ko'rinadi.",
      ru: "С вершины открывается потрясающий 360-градусный вид на 7 альпийских озёр Швейцарии и Франции, а также Монблан.",
      en: "From the peak, you get a 360-degree panorama of seven Swiss and French lakes as well as Mont Blanc."
    }
  },
  {
    id: "pano_atacama_cerro_toco",
    name: { uz: "Serro Toko cho'qqisi (Atakama)", ru: "Вулкан Серро-Токо (Атакама)", en: "Cerro Toco Peak (Atacama)" },
    country: { uz: "Chili", ru: "Чили", en: "Chile" },
    city: { uz: "San-Pedro-de-Atakama", ru: "Сан-Педро-де-Атакама", en: "San Pedro de Atacama" },
    flag: "🇨🇱",
    lat: -22.9564,
    lng: -67.7772,
    driving: "right",
    type: "streetview",
    is360: true,
    panorama: "panoramas/cerro-toco.jpg",
    image: "https://pannellum.org/images/cerro-toco-0.jpg",
    fact: {
      uz: "Atakama sahrosi dunyodagi eng qurg'oqchil baland tog' cho'li bo'lib, uning manzarasi Mars sayyorasiga o'xshaydi.",
      ru: "Пустыня Атакама — самое сухое место на планете, её марсианский рельеф привлекает учёных со всего мира.",
      en: "Atacama is the driest high-altitude desert on Earth, often used by NASA to test Mars rovers."
    }
  },
  {
    id: "pano_alma_observatory",
    name: { uz: "ALMA Teleskoplar majmuasi", ru: "Обсерватория ALMA", en: "ALMA Observatory Array" },
    country: { uz: "Chili", ru: "Чили", en: "Chile" },
    city: { uz: "Chajnanto platosi", ru: "Плато Чахнантор", en: "Chajnantor Plateau" },
    flag: "🇨🇱",
    lat: -23.0293,
    lng: -67.7548,
    driving: "right",
    type: "landmark",
    is360: true,
    panorama: "panoramas/alma.jpg",
    image: "https://pannellum.org/images/alma.jpg",
    fact: {
      uz: "ALMA 5 000 metr balandlikda joylashgan bo'lib, koinotning eng qadimiy galaktikalarini tadqiq qiladi.",
      ru: "Крупнейший в мире комплекс радиотелескопов на высоте 5000 метров исследует глубины далёкого космоса.",
      en: "Located at 5,000m elevation in the Andes, ALMA is the most powerful radio observatory in the world."
    }
  },
  {
    id: "pano_boston_beacon_hill",
    name: { uz: "Charlz-strit (Bikon-Xill)", ru: "Чарльз-стрит (Бикон-Хилл)", en: "Charles Street (Beacon Hill)" },
    country: { uz: "AQSH", ru: "США", en: "United States" },
    city: { uz: "Boston", ru: "Бостон", en: "Boston" },
    flag: "🇺🇸",
    lat: 42.3582,
    lng: -71.0706,
    driving: "right",
    type: "streetview",
    is360: true,
    panorama: "panoramas/charles-street.jpg",
    image: "https://pannellum.org/images/charles-street.jpg",
    fact: {
      uz: "Bostonning tarixiy Bikon-Xill ko'chalari bugungi kungacha asl 19-asr gaz chiroqlari bilan yoritiladi.",
      ru: "Исторический квартал Бостона с газовыми фонарями XIX века и архитектурой времён Войны за независимость.",
      en: "Beacon Hill is famous for its narrow gas-lit cobblestone streets and Victorian architecture."
    }
  },
  {
    id: "pano_boston_jfk_harbor",
    name: { uz: "Boston bandargohi va JFK majmuasi", ru: "Гавань Бостона и Мемориал Кеннеди", en: "Boston Harbor & JFK Memorial" },
    country: { uz: "AQSH", ru: "США", en: "United States" },
    city: { uz: "Boston", ru: "Бостон", en: "Boston" },
    flag: "🇺🇸",
    lat: 42.3168,
    lng: -71.0345,
    driving: "right",
    type: "landmark",
    is360: true,
    panorama: "panoramas/boston-jfk.jpg",
    image: "https://pannellum.org/images/jfk.jpg",
    fact: {
      uz: "Atlantika okeani qirg'og'ida qad rostlagan ushbu memorial mashhur me'mor I. M. Pei tomonidan loyihalangan.",
      ru: "Президентский комплекс на побережье Атлантического океана, спроектированный архитектором И. М. Пэем.",
      en: "Overlooking Dorchester Bay on the Atlantic coast, designed by renowned architect I. M. Pei."
    }
  },
  {
    id: "pano_baltimore_art_museum",
    name: { uz: "Baltimor San'at Muzeyi bog'i", ru: "Сад Музея искусств Балтимора", en: "Baltimore Museum of Art Garden" },
    country: { uz: "AQSH", ru: "США", en: "United States" },
    city: { uz: "Baltimor", ru: "Балтимор", en: "Baltimore" },
    flag: "🇺🇸",
    lat: 39.3262,
    lng: -76.6198,
    driving: "right",
    type: "landmark",
    is360: true,
    panorama: "panoramas/baltimore-art.jpg",
    image: "https://pannellum.org/images/bma-0.jpg",
    fact: {
      uz: "Muzey bog'ida dunyoning eng mashhur zamonaviy haykaltaroshlarining 30 dan ortiq durdona asarlari ochiq osmon ostida joylashgan.",
      ru: "В парке скульптур музея под открытым небом выставлены более 30 шедевров современного искусства.",
      en: "The sculpture gardens feature over 30 masterworks of modern art across three landscaped acres."
    }
  },
  {
    id: "registan",
    name: { uz: "Registon maydoni", ru: "Площадь Регистан", en: "Registan Square" },
    country: { uz: "O'zbekiston", ru: "Узбекистан", en: "Uzbekistan" },
    city: { uz: "Samarqand", ru: "Самарканд", en: "Samarkand" },
    flag: "🇺🇿",
    lat: 39.6548,
    lng: 66.9757,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/RegistanSquare_Samarkand.jpg/1280px-RegistanSquare_Samarkand.jpg",
    fact: {
      uz: "Registon maydoni uchta qadimiy madrasadan iborat: Ulug'bek, Sherdor va Tillakori.",
      ru: "Регистан — главная площадь Самарканда с тремя величественными медресе XV–XVII веков.",
      en: "Registan Square features three iconic madrasahs dating back to the 15th-17th centuries."
    }
  },
  {
    id: "eiffel_tower",
    name: { uz: "Eyfel minorasi", ru: "Эйфелева башня", en: "Eiffel Tower" },
    country: { uz: "Fransiya", ru: "Франция", en: "France" },
    city: { uz: "Parij", ru: "Париж", en: "Paris" },
    flag: "🇫🇷",
    lat: 48.8584,
    lng: 2.2945,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg/1280px-Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg",
    fact: {
      uz: "Yoz faslida metall qizib kengayishi sababli minora 15 santimetrgacha balandlashadi.",
      ru: "Летом металл расширяется на солнце, и башня становится выше примерно на 15 см.",
      en: "Thermal expansion makes the tower grow up to 15 cm taller during summer."
    }
  },
  {
    id: "times_square",
    name: { uz: "Tayms-skver", ru: "Таймс-сквер", en: "Times Square" },
    country: { uz: "AQSH", ru: "США", en: "United States" },
    city: { uz: "Nyu-York", ru: "Нью-Йорк", en: "New York City" },
    flag: "🇺🇸",
    lat: 40.7580,
    lng: -73.9855,
    driving: "right",
    type: "streetview",
    image: "https://images.unsplash.com/photo-1534430480872-3498386e7856?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Dunyoning eng gavjum chorrahalaridan biri, har kuni 300 000 dan ortiq piyoda o'tadi.",
      ru: "Сердце Манхэттена с гигантскими неоновыми экранами, центр театрального квартала.",
      en: "Known as 'The Crossroads of the World', visited by over 300,000 pedestrians daily."
    }
  },
  {
    id: "colosseum",
    name: { uz: "Rim Kolizeyi", ru: "Римский Колизей", en: "The Colosseum" },
    country: { uz: "Italiya", ru: "Италия", en: "Italy" },
    city: { uz: "Rim", ru: "Рим", en: "Rome" },
    flag: "🇮🇹",
    lat: 41.8902,
    lng: 12.4922,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg",
    fact: {
      uz: "Qadimgi dunyoning eng ulkan amfiteatri, 50 000 dan ziyod tomoshabin sig'dirgan.",
      ru: "Крупнейший амфитеатр античного мира, вмещавший более 50 000 зрителей.",
      en: "The largest ancient amphitheatre ever built, hosting gladiator battles for centuries."
    }
  },
  {
    id: "shibuya_crossing",
    name: { uz: "Shibuya chorrahasi", ru: "Перекрёсток Сибуя", en: "Shibuya Crossing" },
    country: { uz: "Yaponiya", ru: "Япония", en: "Japan" },
    city: { uz: "Tokio", ru: "Токио", en: "Tokyo" },
    flag: "🇯🇵",
    lat: 35.6595,
    lng: 139.7005,
    driving: "left",
    type: "streetview",
    image: "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Bitta yashil chiroqda 3 000 gacha odam bir vaqtning o'zida ko'chani kesib o'tadi.",
      ru: "Один из самых оживлённых перекрёстков в мире, левостороннее движение.",
      en: "Up to 3,000 people cross this intersection simultaneously on a single green light."
    }
  },
  {
    id: "taj_mahal",
    name: { uz: "Toj Mahal", ru: "Тадж-Махал", en: "Taj Mahal" },
    country: { uz: "Hindiston", ru: "Индия", en: "India" },
    city: { uz: "Agra", ru: "Агра", en: "Agra" },
    flag: "🇮🇳",
    lat: 27.1751,
    lng: 78.0421,
    driving: "left",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Taj_Mahal_%28Edited%29.jpeg/1280px-Taj_Mahal_%28Edited%29.jpeg",
    fact: {
      uz: "Oq marmardan bunyod etilgan maqbara, Shoh Jahon suyukli xotini xotirasiga qurdirgan.",
      ru: "Шедевр могольской архитектуры из белого мрамора, меняющий оттенок на солнце.",
      en: "Ivory-white marble mausoleum commissioned by Mughal emperor Shah Jahan."
    }
  },
  {
    id: "sydney_opera",
    name: { uz: "Sidney Opera Teatri", ru: "Сиднейский оперный театр", en: "Sydney Opera House" },
    country: { uz: "Avstraliya", ru: "Австралия", en: "Australia" },
    city: { uz: "Sidney", ru: "Сидней", en: "Sydney" },
    flag: "🇦🇺",
    lat: -33.8568,
    lng: 151.2153,
    driving: "left",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Sydney_Opera_House_-_Dec_2008.jpg/1280px-Sydney_Opera_House_-_Dec_2008.jpg",
    fact: {
      uz: "Uning yelkan shaklidagi tomi 1 milliondan ortiq shved keramik plitkalari bilan qoplangan.",
      ru: "Кровля в форме ракушек покрыта более чем 1 миллионом керамических плиток.",
      en: "Its iconic sail-like roof structure is covered in over 1 million ceramic tiles."
    }
  },
  {
    id: "christ_redeemer",
    name: { uz: "Xaloskor Iso haykali", ru: "Статуя Христа-Искупителя", en: "Christ the Redeemer" },
    country: { uz: "Braziliya", ru: "Бразилия", en: "Brazil" },
    city: { uz: "Rio-de-Janeyro", ru: "Рио-де-Жанейро", en: "Rio de Janeiro" },
    flag: "🇧🇷",
    lat: -22.9519,
    lng: -43.2105,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Aerial_view_of_the_Statue_of_Christ_the_Redeemer.jpg/1280px-Aerial_view_of_the_Statue_of_Christ_the_Redeemer.jpg",
    fact: {
      uz: "Korkovadu tog'i cho'qqisida qad rostlagan, balandligi 38 metrni tashkil etadi.",
      ru: "Монумент высотой 38 метров возвышается над Рио на вершине горы Корковаду.",
      en: "Stands 38 meters tall atop the 700-meter Corcovado mountain overlooking Rio."
    }
  },
  {
    id: "pyramids_giza",
    name: { uz: "Giza Piramidalari", ru: "Пирамиды Гизы", en: "Pyramids of Giza" },
    country: { uz: "Misr", ru: "Египет", en: "Egypt" },
    city: { uz: "Giza / Qohira", ru: "Гиза / Каир", en: "Giza" },
    flag: "🇪🇬",
    lat: 29.9792,
    lng: 31.1342,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/All_Gizah_Pyramids.jpg/1280px-All_Gizah_Pyramids.jpg",
    fact: {
      uz: "Qadimgi dunyoning yetti mo'jizasidan bugungi kungacha saqlanib qolgan yagona obida.",
      ru: "Единственное из семи чудес древнего мира, сохранившееся до наших дней.",
      en: "The only surviving wonder of the ancient world, built over 4,500 years ago."
    }
  },
  {
    id: "burj_khalifa",
    name: { uz: "Burj Xalifa", ru: "Бурдж-Халифа", en: "Burj Khalifa" },
    country: { uz: "BAA", ru: "ОАЭ", en: "United Arab Emirates" },
    city: { uz: "Dubay", ru: "Дубай", en: "Dubai" },
    flag: "🇦🇪",
    lat: 25.1972,
    lng: 55.2744,
    driving: "right",
    type: "streetview",
    image: "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Balandligi 828 metr bo'lgan dunyodagi eng baland bino va inshoot.",
      ru: "Самое высокое здание в мире (828 метров), насчитывает 163 этажа.",
      en: "The tallest artificial structure in the world, soaring 828 meters into the sky."
    }
  },
  {
    id: "chorsu_bazaar",
    name: { uz: "Chorsu bozori", ru: "Базар Чорсу", en: "Chorsu Bazaar" },
    country: { uz: "O'zbekiston", ru: "Узбекистан", en: "Uzbekistan" },
    city: { uz: "Toshkent", ru: "Ташкент", en: "Tashkent" },
    flag: "🇺🇿",
    lat: 41.3275,
    lng: 69.2401,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Chorsu_bazaar_Tashkent.jpg/1280px-Chorsu_bazaar_Tashkent.jpg",
    fact: {
      uz: "Ulkan feruzarang gumbaz ostidagi Toshkentning eng mashhur va qadimiy sharqona bozori.",
      ru: "Один из старейших рынков Центральной Азии под монументальным бирюзовым куполом.",
      en: "One of the oldest traditional bazaars in Central Asia beneath a monumental blue dome."
    }
  },
  {
    id: "golden_gate",
    name: { uz: "Oltin Darvoza Ko'prigi", ru: "Мост Золотые Ворота", en: "Golden Gate Bridge" },
    country: { uz: "AQSH", ru: "США", en: "United States" },
    city: { uz: "San-Fransisko", ru: "Сан-Франциско", en: "San Francisco" },
    flag: "🇺🇸",
    lat: 37.8199,
    lng: -122.4783,
    driving: "right",
    type: "streetview",
    image: "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Ko'prikning o'ziga xos to'q sariq rangi 'Xalqaro to'q sariq' deb ataladi.",
      ru: "Знаменитый висячий мост через пролив Золотые Ворота с уникальным оранжевым цветом.",
      en: "Painted in 'International Orange' to enhance visibility through thick Pacific fog."
    }
  },
  {
    id: "route66_az",
    name: { uz: "Tarixiy 66-yo'l", ru: "Трасса 66", en: "Historic Route 66" },
    country: { uz: "AQSH", ru: "США", en: "United States" },
    city: { uz: "Arizona", ru: "Аризона", en: "Arizona" },
    flag: "🇺🇸",
    lat: 35.2828,
    lng: -113.5658,
    driving: "right",
    type: "streetview",
    image: "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Amerika avtomobil madaniyatining bosh belgisi bo'lgan 'Onalar yo'li'.",
      ru: "Легендарная трасса США, соединившая Чикаго и Лос-Анджелес через бескрайние прерии.",
      en: "Nicknamed the 'Mother Road', spanning across 8 states from Chicago to California."
    }
  },
  {
    id: "big_ben",
    name: { uz: "Big Ben va Vestminster", ru: "Биг-Бен и Вестминстер", en: "Big Ben & Westminster" },
    country: { uz: "Buyuk Britaniya", ru: "Великобритания", en: "United Kingdom" },
    city: { uz: "London", ru: "Лондон", en: "London" },
    flag: "🇬🇧",
    lat: 51.5007,
    lng: -0.1246,
    driving: "left",
    type: "landmark",
    image: "https://images.unsplash.com/photo-1529655683826-aba9b3e77383?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Temza daryosi bo'yidagi mashhur soat minorasi, chap tomonlama harakat.",
      ru: "Знаменитая башня Елизаветы на берегу Темзы. В Великобритании левостороннее движение.",
      en: "Officially named Elizabeth Tower, standing beside the River Thames in London."
    }
  },
  {
    id: "brandenburg_gate",
    name: { uz: "Brandenburg darvozasi", ru: "Бранденбургские ворота", en: "Brandenburg Gate" },
    country: { uz: "Germaniya", ru: "Германия", en: "Germany" },
    city: { uz: "Berlin", ru: "Берлин", en: "Berlin" },
    flag: "🇩🇪",
    lat: 52.5163,
    lng: 13.3777,
    driving: "right",
    type: "landmark",
    image: "https://images.unsplash.com/photo-1560969184-10fe8719e047?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Berlinning bosh ramzi, 1791 yilda neoklassik uslubda barpo etilgan.",
      ru: "Символ объединения Германии и один из шедевров берлинского классицизма.",
      en: "18th-century neoclassical monument and an enduring symbol of European peace and unity."
    }
  },
  {
    id: "hagia_sophia",
    name: { uz: "Ayasofya", ru: "Собор Святой Софии", en: "Hagia Sophia" },
    country: { uz: "Turkiya", ru: "Турция", en: "Turkey" },
    city: { uz: "Istanbul", ru: "Стамбул", en: "Istanbul" },
    flag: "🇹🇷",
    lat: 41.0086,
    lng: 28.9802,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Hagia_Sophia_Mars_2013.jpg/1280px-Hagia_Sophia_Mars_2013.jpg",
    fact: {
      uz: "Qariyb 1 500 yillik tarixga ega, Vizantiya va Usmonli madaniyatining durdonasi.",
      ru: "Величественный собор и мечеть с полуторатысячелетней историей на берегу Босфора.",
      en: "Built in 537 AD, served as a cathedral, mosque, and museum over 1,500 years."
    }
  },
  {
    id: "sagrada_familia",
    name: { uz: "Sagrada Familia", ru: "Саграда Фамилия", en: "Sagrada Família" },
    country: { uz: "Ispaniya", ru: "Испания", en: "Spain" },
    city: { uz: "Barselona", ru: "Барселона", en: "Barcelona" },
    flag: "🇪🇸",
    lat: 41.4036,
    lng: 2.1744,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Sagrada_Familia_01.jpg/1280px-Sagrada_Familia_01.jpg",
    fact: {
      uz: "Antoni Gaudi tomonidan loyihalashtirilgan, qurilishi 140 yildan ortiq davom etmoqda.",
      ru: "Шедевр Антонио Гауди, строительство которого продолжается с 1882 года.",
      en: "Masterpiece of Antoni Gaudí, under continuous construction since 1882."
    }
  },
  {
    id: "marina_bay_sands",
    name: { uz: "Marina Bay Sands", ru: "Марина Бэй Сэндс", en: "Marina Bay Sands" },
    country: { uz: "Singapur", ru: "Сингапур", en: "Singapore" },
    city: { uz: "Singapur", ru: "Сингапур", en: "Singapore" },
    flag: "🇸🇬",
    lat: 1.2838,
    lng: 103.8591,
    driving: "left",
    type: "streetview",
    image: "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "Uchta bino ustidagi osmon bog'i va suzish havzasi bilan mashhur osmono'par majmua.",
      ru: "Уникальный комплекс с небесным парком на высоте 200 метров. Левостороннее движение.",
      en: "Integrated resort known for its world-famous cantilevered SkyPark and infinity pool."
    }
  },
  {
    id: "great_wall",
    name: { uz: "Buyuk Xitoy Devori", ru: "Великая Китайская стена", en: "Great Wall of China" },
    country: { uz: "Xitoy", ru: "Китай", en: "China" },
    city: { uz: "Pekin yaqinida", ru: "Окрестности Пекина", en: "Near Beijing" },
    flag: "🇨🇳",
    lat: 40.4319,
    lng: 116.5704,
    driving: "right",
    type: "landmark",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/The_Great_Wall_of_China_at_Jinshanling-edit.jpg/1280px-The_Great_Wall_of_China_at_Jinshanling-edit.jpg",
    fact: {
      uz: "Barcha tarmoqlari bilan umumiy uzunligi 21 000 kilometrdan oshadi.",
      ru: "Общая протяжённость со всеми ответвлениями превышает 21 000 км.",
      en: "Total length with all defensive branches exceeds 21,000 kilometers."
    }
  },
  {
    id: "machu_picchu",
    name: { uz: "Machu-Pikchu", ru: "Мачу-Пикчу", en: "Machu Picchu" },
    country: { uz: "Peru", ru: "Перу", en: "Peru" },
    city: { uz: "Kusko", ru: "Куско", en: "Cusco Region" },
    flag: "🇵🇪",
    lat: -13.1631,
    lng: -72.5450,
    driving: "right",
    type: "landmark",
    image: "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=1200&q=80",
    fact: {
      uz: "And tog'larida 2 430 metr balandlikda joylashgan inka sivilizatsiyasi shahri.",
      ru: "Таинственный город инков на вершине горного хребта в Андах на высоте 2 430 м.",
      en: "15th-century Inca citadel situated on a mountain ridge 2,430 meters above sea level."
    }
  }
];

// App State
let currentLang = "uz";
let gameRounds = [];
let currentRoundIndex = 0;
let totalScore = 0;
let roundResults = [];

let map = null;
let guessMarker = null;
let trueMarker = null;
let polyline = null;
let selectedLatLng = null;

// DOM Elements
const panoramaViewer = document.getElementById("panoramaViewer");
let pannellumViewer = null;
const roundBadge = document.getElementById("roundBadge");
const scoreBadge = document.getElementById("scoreBadge");
const locationImg = document.getElementById("locationImg");
const imageLoader = document.getElementById("imageLoader");
const clueDrivingText = document.getElementById("clueDrivingText");
const clueTypeText = document.getElementById("clueTypeText");
const guessBtn = document.getElementById("guessBtn");
const guessBtnText = document.getElementById("guessBtnText");
const mapHintText = document.getElementById("mapHintText");
const expandPhotoBtn = document.getElementById("expandPhotoBtn");
const photoContainer = document.getElementById("photoContainer");

const resultModal = document.getElementById("resultModal");
const resFlag = document.getElementById("resFlag");
const resLocationName = document.getElementById("resLocationName");
const resCountryName = document.getElementById("resCountryName");
const resDistance = document.getElementById("resDistance");
const resPoints = document.getElementById("resPoints");
const resFunFact = document.getElementById("resFunFact");
const nextRoundBtn = document.getElementById("nextRoundBtn");
const nextRoundBtnText = document.getElementById("nextRoundBtnText");

const gameOverScreen = document.getElementById("gameOverScreen");
const finalTotalScore = document.getElementById("finalTotalScore");
const finalRankBadge = document.getElementById("finalRankBadge");
const roundsBreakdown = document.getElementById("roundsBreakdown");
const btnSubmitScore = document.getElementById("btnSubmitScore");
const btnPlayAgain = document.getElementById("btnPlayAgain");

// Calculate Distance (Haversine formula in km)
function calculateDistance(lat1, lon1, lat2, lon2) {
  const R = 6371; // Earth's radius in km
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a = 
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * 
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return Math.round(R * c);
}

// Calculate Score (GeoGuessr exponential formula: up to 5,000 pts per round)
function calculateScore(distanceKm) {
  if (distanceKm <= 20) return 5000;
  // Exponential decay curve
  const pts = Math.round(5000 * Math.exp(-distanceKm / 2000));
  return Math.max(0, pts);
}

// Custom Leaflet Icons
function createCustomPin(emoji, isTrueLocation = false) {
  return L.divIcon({
    className: "custom-leaflet-marker",
    html: `<div class="custom-pin ${isTrueLocation ? 'true-pin' : ''}">${emoji}</div>`,
    iconSize: [30, 30],
    iconAnchor: [15, 28]
  });
}

// Initialize Leaflet Map
function initMap() {
  map = L.map("map", {
    center: [25, 10],
    zoom: 2,
    minZoom: 1,
    maxZoom: 18,
    zoomControl: false,
    attributionControl: false
  });

  // Dark Matter CartoDB tiles
  L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png", {
    subdomains: "abcd",
    maxZoom: 19
  }).addTo(map);

  // Add zoom control top right
  L.control.zoom({ position: "topright" }).addTo(map);

  // Map Click Listener
  map.on("click", (e) => {
    onMapClick(e.latlng);
  });
}

function onMapClick(latlng) {
  if (guessMarker && guessBtn.disabled === false && resultModal.classList.contains("show")) {
    return; // Don't allow click during results
  }

  selectedLatLng = latlng;

  // Haptic feedback
  if (tg?.HapticFeedback) {
    tg.HapticFeedback.impactOccurred("light");
  }

  if (guessMarker) {
    guessMarker.setLatLng(latlng);
  } else {
    guessMarker = L.marker(latlng, {
      icon: createCustomPin("📍", false),
      draggable: true
    }).addTo(map);

    guessMarker.on("dragend", (evt) => {
      selectedLatLng = evt.target.getLatLng();
    });
  }

  // Enable Guess Button
  guessBtn.disabled = false;
  mapHintText.style.opacity = "0";
}

// Start Game (5 random rounds)
function startNewGame() {
  totalScore = 0;
  currentRoundIndex = 0;
  roundResults = [];
  
  // Guarantee an exciting mix of interactive 360° panoramas and classic street views
  const panos = LOCATIONS.filter(l => l.is360);
  const others = LOCATIONS.filter(l => !l.is360);

  const shuffledPanos = [...panos].sort(() => 0.5 - Math.random());
  const shuffledOthers = [...others].sort(() => 0.5 - Math.random());

  // Guarantee 2 interactive 360° spherical rounds + 3 landmark/street rounds
  const selected = [...shuffledPanos.slice(0, 2), ...shuffledOthers.slice(0, 3)].sort(() => 0.5 - Math.random());
  gameRounds = selected;

  gameOverScreen.classList.remove("show");
  resultModal.classList.remove("show");

  loadRound(currentRoundIndex);
}

// Load Round
function loadRound(index) {
  const loc = gameRounds[index];
  const t = I18N[currentLang];

  roundBadge.textContent = `${t.round} ${index + 1}/5`;
  scoreBadge.textContent = `${totalScore.toLocaleString()} ${t.score}`;

  // Reset map markers
  if (guessMarker) {
    map.removeLayer(guessMarker);
    guessMarker = null;
  }
  if (trueMarker) {
    map.removeLayer(trueMarker);
    trueMarker = null;
  }
  if (polyline) {
    map.removeLayer(polyline);
    polyline = null;
  }
  selectedLatLng = null;

  guessBtn.disabled = true;
  mapHintText.style.opacity = "1";
  mapHintText.textContent = t.hintMap;
  map.setView([25, 10], 2);

  // Clean up previous 360 viewer if present
  if (pannellumViewer) {
    try {
      pannellumViewer.destroy();
    } catch (e) {
      console.warn("Pannellum destroy notice:", e);
    }
    pannellumViewer = null;
  }

  // Load Media (360 Panorama vs Static Street Photo)
  imageLoader.classList.remove("hidden");
  const is360 = Boolean(loc.is360 && loc.panorama);

  if (is360) {
    locationImg.classList.add("hidden");
    panoramaViewer.classList.remove("hidden");

    if (window.pannellum) {
      try {
        pannellumViewer = window.pannellum.viewer("panoramaViewer", {
          type: "equirectangular",
          panorama: loc.panorama,
          autoLoad: true,
          autoRotate: -1.2,
          compass: true,
          showZoomCtrl: true,
          showFullscreenCtrl: false,
          mouseZoom: true,
          hfov: 100,
          minHfov: 50,
          maxHfov: 120
        });

        pannellumViewer.on("load", () => {
          imageLoader.classList.add("hidden");
        });

        pannellumViewer.on("error", (err) => {
          console.warn("Pannellum load failed, falling back to static image:", err);
          panoramaViewer.classList.add("hidden");
          locationImg.classList.remove("hidden");
          locationImg.style.opacity = "0";
          locationImg.onload = () => {
            imageLoader.classList.add("hidden");
            locationImg.style.opacity = "1";
          };
          locationImg.src = loc.image;
        });
      } catch (err) {
        console.error("Pannellum init error:", err);
        panoramaViewer.classList.add("hidden");
        locationImg.classList.remove("hidden");
        locationImg.style.opacity = "0";
        locationImg.onload = () => {
          imageLoader.classList.add("hidden");
          locationImg.style.opacity = "1";
        };
        locationImg.src = loc.image;
      }
    } else {
      panoramaViewer.classList.add("hidden");
      locationImg.classList.remove("hidden");
      locationImg.style.opacity = "0";
      locationImg.onload = () => {
        imageLoader.classList.add("hidden");
        locationImg.style.opacity = "1";
      };
      locationImg.src = loc.image;
    }
  } else {
    panoramaViewer.classList.add("hidden");
    locationImg.classList.remove("hidden");
    locationImg.style.opacity = "0";
    locationImg.onload = () => {
      imageLoader.classList.add("hidden");
      locationImg.style.opacity = "1";
    };
    locationImg.src = loc.image;
  }

  // Clues
  clueDrivingText.textContent = loc.driving === "right" ? t.drivingRight : t.drivingLeft;
  if (is360) {
    clueTypeText.textContent = t.panorama360 || "🔄 360° Panorama";
  } else {
    clueTypeText.textContent = loc.type === "landmark" ? t.landmark : t.streetView;
  }
}

// Submit Guess
function submitGuess() {
  if (!selectedLatLng) return;

  const loc = gameRounds[currentRoundIndex];
  const t = I18N[currentLang];

  // Haptic feedback
  if (tg?.HapticFeedback) {
    tg.HapticFeedback.impactOccurred("medium");
  }

  // Calculate distance & points
  const distKm = calculateDistance(selectedLatLng.lat, selectedLatLng.lng, loc.lat, loc.lng);
  const roundPts = calculateScore(distKm);
  totalScore += roundPts;

  roundResults.push({
    round: currentRoundIndex + 1,
    location: loc.name[currentLang] || loc.name.en,
    country: loc.country[currentLang] || loc.country.en,
    flag: loc.flag,
    distanceKm: distKm,
    points: roundPts
  });

  // Reveal True Location on Map
  trueMarker = L.marker([loc.lat, loc.lng], {
    icon: createCustomPin("🏁", true)
  }).addTo(map);

  // Draw dashed polyline between Guess and True Location
  polyline = L.polyline([selectedLatLng, [loc.lat, loc.lng]], {
    color: "#38bdf8",
    weight: 4,
    opacity: 0.9,
    dashArray: "8, 8"
  }).addTo(map);

  // Fit bounds to show both pins
  const bounds = L.latLngBounds([selectedLatLng, [loc.lat, loc.lng]]);
  map.fitBounds(bounds, { padding: [40, 40], maxZoom: 8 });

  // Update Result Modal
  resFlag.textContent = loc.flag;
  resLocationName.textContent = loc.name[currentLang] || loc.name.en;
  resCountryName.textContent = `${loc.city[currentLang] || loc.city.en}, ${loc.country[currentLang] || loc.country.en}`;
  resDistance.textContent = `${distKm.toLocaleString()} km`;
  resPoints.textContent = `+${roundPts.toLocaleString()}`;
  resFunFact.innerHTML = `<b>${t.funFactPrefix}</b> ${loc.fact[currentLang] || loc.fact.en}`;

  // Show Modal after brief delay so user sees pins connecting
  setTimeout(() => {
    resultModal.classList.add("show");
    if (tg?.HapticFeedback) {
      if (roundPts > 4000) {
        tg.HapticFeedback.notificationOccurred("success");
      } else {
        tg.HapticFeedback.notificationOccurred("warning");
      }
    }
  }, 600);
}

// Next Round or Game Over
function onNextRound() {
  resultModal.classList.remove("show");

  currentRoundIndex++;
  if (currentRoundIndex < 5) {
    loadRound(currentRoundIndex);
  } else {
    showGameOver();
  }
}

// Show Game Over
function showGameOver() {
  const t = I18N[currentLang];
  finalTotalScore.textContent = totalScore.toLocaleString();

  // Determine Rank
  let rankText = t.rankExplorer;
  if (totalScore >= 22000) rankText = t.rankLegend;
  else if (totalScore >= 18000) rankText = t.rankMaster;
  else if (totalScore >= 12000) rankText = t.rankNavigator;
  finalRankBadge.textContent = rankText;

  // Breakdown rows
  roundsBreakdown.innerHTML = roundResults.map(r => `
    <div class="round-row">
      <span class="round-row-name">${r.flag} ${r.location}</span>
      <div class="round-row-stats">
        <span class="round-row-dist">${r.distanceKm.toLocaleString()} km</span>
        <span class="round-row-pts">+${r.points.toLocaleString()}</span>
      </div>
    </div>
  `).join("");

  gameOverScreen.classList.add("show");

  if (tg?.HapticFeedback) {
    tg.HapticFeedback.notificationOccurred("success");
  }
}

// Submit Score to Bot (Telegram WebApp sendData)
function submitScoreToBot() {
  const data = {
    action: "miniapp_score",
    total_score: totalScore,
    rounds_count: 5,
    rank: finalRankBadge.textContent,
    results: roundResults
  };

  if (tg && tg.sendData) {
    tg.sendData(JSON.stringify(data));
    tg.close();
  } else {
    alert(`Natija: ${totalScore} ball! Telegram WebApp orqali ochilganda natija botga yoziladi.`);
  }
}

// Switch Language
function setLanguage(lang) {
  if (!I18N[lang]) return;
  currentLang = lang;

  document.querySelectorAll(".lang-btn").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.lang === lang);
  });

  const t = I18N[lang];
  document.getElementById("txtLoading").textContent = t.loading;
  document.getElementById("lblDistance").textContent = t.distance;
  document.getElementById("lblPoints").textContent = t.pointsAwarded;
  guessBtnText.textContent = t.guessBtn;
  nextRoundBtnText.textContent = t.nextRound;
  document.getElementById("txtGameOver").textContent = t.gameOver;
  btnSubmitScore.textContent = t.submitScore;
  btnPlayAgain.textContent = t.playAgain;

  if (gameRounds.length > 0 && currentRoundIndex < 5) {
    const loc = gameRounds[currentRoundIndex];
    roundBadge.textContent = `${t.round} ${currentRoundIndex + 1}/5`;
    scoreBadge.textContent = `${totalScore.toLocaleString()} ${t.score}`;
    clueDrivingText.textContent = loc.driving === "right" ? t.drivingRight : t.drivingLeft;
    if (loc.is360 && loc.panorama) {
      clueTypeText.textContent = t.panorama360 || "🔄 360° Panorama";
    } else {
      clueTypeText.textContent = loc.type === "landmark" ? t.landmark : t.streetView;
    }
    if (!guessMarker) {
      mapHintText.textContent = t.hintMap;
    }
  }
}

// Event Listeners
guessBtn.addEventListener("click", submitGuess);
nextRoundBtn.addEventListener("click", onNextRound);
btnSubmitScore.addEventListener("click", submitScoreToBot);
btnPlayAgain.addEventListener("click", startNewGame);

expandPhotoBtn.addEventListener("click", () => {
  photoContainer.classList.toggle("fullscreen");
  expandPhotoBtn.textContent = photoContainer.classList.contains("fullscreen") ? "✕" : "🔍";
  setTimeout(() => {
    if (map) map.invalidateSize();
    if (pannellumViewer && typeof pannellumViewer.resize === "function") {
      pannellumViewer.resize();
    }
  }, 350);
});

document.querySelectorAll(".lang-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    setLanguage(btn.dataset.lang);
  });
});

// Auto-detect Telegram user language if available
if (tg?.initDataUnsafe?.user?.language_code) {
  const userLang = tg.initDataUnsafe.user.language_code.toLowerCase();
  if (userLang.startsWith("ru")) setLanguage("ru");
  else if (userLang.startsWith("uz")) setLanguage("uz");
  else setLanguage("en");
}

// Start on load
window.addEventListener("DOMContentLoaded", () => {
  initMap();
  startNewGame();
});
