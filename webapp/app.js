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
    btnSatellite: "🛰 Sun'iy yo'ldosh",
    btnStreet: "🗺 Xarita (Davlatlar)",
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
    btnSatellite: "🛰 Спутник",
    btnStreet: "🗺 Карта (Страны)",
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
    btnSatellite: "🛰 Satellite",
    btnStreet: "🗺 Map (Countries)",
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
    id: "pano_milan_duomo",
    name: { uz: "Sobor maydoni (Piazza del Duomo)", ru: "Соборная площадь (Пьяцца-дель-Дуомо)", en: "Piazza del Duomo" },
    country: { uz: "Italiya", ru: "Италия", en: "Italy" },
    city: { uz: "Milan", ru: "Милан", en: "Milan" },
    flag: "🇮🇹",
    lat: 45.4641,
    lng: 9.1895,
    driving: "right",
    type: "landmark",
    is360: true,
    panorama: "panoramas/milan_duomo.jpg",
    fact: {
      uz: "Milan sobori dunyodagi 5-o'rindagi eng yirik nasroniy ibodatxonasidir va 6 asr davomida qurilgan.",
      ru: "Миланский собор Дуомо из белого мрамора строился почти шесть столетий.",
      en: "The Milan Cathedral took nearly six centuries to complete and is the 5th largest church in the world."
    }
  },
  {
    id: "pano_france_provence",
    name: { uz: "Kungaboqar vodiysi (Provans)", ru: "Долина подсолнухов (Прованс)", en: "Sunflower Valleys (Provence)" },
    country: { uz: "Fransiya", ru: "Франция", en: "France" },
    city: { uz: "Provans", ru: "Прованс", en: "Provence" },
    flag: "🇫🇷",
    lat: 43.8845,
    lng: 4.8870,
    driving: "right",
    type: "streetview",
    is360: true,
    panorama: "panoramas/france_provence.jpg",
    fact: {
      uz: "Provans quyoshli kungaboqar va lavanda dalalari, uzumzorlari va o'rta asr qishloqlari bilan dunyoga mashhur.",
      ru: "Прованс всемирно известен своими лавандовыми и подсолнуховыми полями, вдохновлявшими Ван Гога.",
      en: "Provence is renowned for its sun-drenched sunflower fields that famously inspired Vincent van Gogh."
    }
  },
  {
    id: "pano_france_puydesancy",
    name: { uz: "Pyui-de-Sansi cho'qqisi", ru: "Вершина Пюи-де-Санси", en: "Puy de Sancy Peak" },
    country: { uz: "Fransiya", ru: "Франция", en: "France" },
    city: { uz: "Overn tog'lari", ru: "Овернь", en: "Auvergne" },
    flag: "🇫🇷",
    lat: 45.5283,
    lng: 2.8122,
    driving: "right",
    type: "streetview",
    is360: true,
    panorama: "panoramas/france_puydesancy.jpg",
    fact: {
      uz: "Pyui-de-Sansi — qadimiy o'chgan vulqon bo'lib, Fransiya Markaziy massividagi eng baland nuqtadir (1886 m).",
      ru: "Высочайшая точка Центрального массива Франции (1886 м), древний стратовулкан.",
      en: "Highest point of the Massif Central in France at 1,886m, an ancient dormant stratovolcano."
    }
  },
  {
    id: "pano_norway_snow",
    name: { uz: "Skandinaviya qorli taygasi", ru: "Скандинавская снежная тайга", en: "Scandinavian Snow Forest" },
    country: { uz: "Norvegiya", ru: "Норвегия", en: "Norway" },
    city: { uz: "Lillexammer", ru: "Лиллехаммер", en: "Lillehammer" },
    flag: "🇳🇴",
    lat: 61.1153,
    lng: 10.4662,
    driving: "right",
    type: "streetview",
    is360: true,
    panorama: "panoramas/norway_snow.jpg",
    fact: {
      uz: "Norvegiyaning qorli o'rmonlari qishki olimpiada sport turlarining vatani sanaladi.",
      ru: "Норвежские хвойные леса и заснеженные фьорды — столица зимних видов спорта.",
      en: "Lillehammer hosted the 1994 Winter Olympics amidst these dense snow-laden Nordic forests."
    }
  },
  {
    id: "pano_baltimore_garden",
    name: { uz: "Baltimor Haykaltaroshlik xiyoboni", ru: "Парк скульптур Балтимора", en: "Baltimore Sculpture Promenade" },
    country: { uz: "AQSH", ru: "США", en: "United States" },
    city: { uz: "Baltimor", ru: "Балтимор", en: "Baltimore" },
    flag: "🇺🇸",
    lat: 39.3255,
    lng: -76.6195,
    driving: "right",
    type: "landmark",
    is360: true,
    panorama: "panoramas/baltimore_garden.jpg",
    fact: {
      uz: "Ushbu xiyobonda Aleksandr Kolder va Genri Mur kabi asr ustalari ijodiga mansub monumentlar joylashgan.",
      ru: "Прогулочные аллеи с работами классиков модерна, включая Александра Колдера и Генри Мура.",
      en: "Features world-famous outdoor monumental sculptures by masters such as Alexander Calder."
    }
  },
  {
    id: "pano_brazil_amazon_forest",
    name: { uz: "Amazoniya tropik yomg'irli o'rmonlari", ru: "Тропические леса Амазонии", en: "Amazon Rainforest Canopy" },
    country: { uz: "Braziliya", ru: "Бразилия", en: "Brazil" },
    city: { uz: "Amazonas", ru: "Амазонас", en: "Amazonas" },
    flag: "🇧🇷",
    lat: -3.1190,
    lng: -60.0217,
    driving: "right",
    type: "streetview",
    is360: true,
    panorama: "panoramas/forest_canopy.jpg",
    fact: {
      uz: "Amazonka o'rmonlari 'Yer sayyorasining o'pkasi' deb ataladi va sayyoramizdagi turlarning 10% dan ortig'iga boshpana beradi.",
      ru: "Джунгли Амазонки — «лёгкие планеты», дом для более чем 10% всех видов флоры и фауны Земли.",
      en: "The Amazon produces 20% of Earth's oxygen and is home to 1 in 10 known species on the planet."
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
let markersGroup = null;
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
let currentTileLayer = null;
let isSatellite = false;

const TILE_ESRI = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}";
const TILE_SAT = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}";

function initMap() {
  map = L.map("map", {
    center: [20, 10],
    zoom: 2,
    minZoom: 1,
    maxZoom: 18,
    worldCopyJump: true,
    zoomControl: false,
    attributionControl: false
  });

  // Esri World Street Map (GeoGuessr-style crisp borders, clear country labels, 100% free)
  currentTileLayer = L.tileLayer(TILE_ESRI, {
    maxZoom: 19,
    attribution: '&copy; Esri World Street Map'
  }).addTo(map);

  // LayerGroup to guarantee complete cleanup between rounds
  markersGroup = L.layerGroup().addTo(map);

  // Add zoom control top right
  L.control.zoom({ position: "topright" }).addTo(map);

  // Map Click Listener
  map.on("click", (e) => {
    onMapClick(e.latlng);
  });
}

function toggleMapLayer() {
  if (!map) return;
  isSatellite = !isSatellite;
  if (currentTileLayer) {
    map.removeLayer(currentTileLayer);
  }
  const url = isSatellite ? TILE_SAT : TILE_ESRI;
  currentTileLayer = L.tileLayer(url, {
    maxZoom: 19,
    attribution: isSatellite ? '&copy; Esri Satellite' : '&copy; Esri World Street'
  }).addTo(map);

  const t = I18N[currentLang];
  const btn = document.getElementById("mapLayerToggle");
  if (btn) {
    btn.textContent = isSatellite ? (t.btnStreet || "🗺 Xarita (Davlatlar)") : (t.btnSatellite || "🛰 Sun'iy yo'ldosh");
  }
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
    }).addTo(markersGroup);

    guessMarker.on("dragend", (evt) => {
      selectedLatLng = evt.target.getLatLng();
    });
  }

  // Enable Guess Button
  guessBtn.disabled = false;
  mapHintText.style.opacity = "0";
}

// Start Game (5 random rounds - 100% 360° interactive spherical panoramas)
function startNewGame() {
  totalScore = 0;
  currentRoundIndex = 0;
  roundResults = [];
  
  // Shuffle all 12 authentic 360° locations and pick 5
  const shuffled = [...LOCATIONS].sort(() => 0.5 - Math.random());
  gameRounds = shuffled.slice(0, 5);

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

  // Reset all map markers and polylines completely
  if (markersGroup) {
    markersGroup.clearLayers();
  }
  guessMarker = null;
  trueMarker = null;
  polyline = null;
  selectedLatLng = null;

  guessBtn.disabled = true;
  mapHintText.style.opacity = "1";
  mapHintText.textContent = t.hintMap;
  map.setView([20, 10], 2);
  setTimeout(() => {
    if (map) map.invalidateSize();
  }, 200);

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
  }).addTo(markersGroup);

  // Draw dashed polyline between Guess and True Location
  polyline = L.polyline([selectedLatLng, [loc.lat, loc.lng]], {
    color: "#38bdf8",
    weight: 4,
    opacity: 0.9,
    dashArray: "8, 8"
  }).addTo(markersGroup);

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

  const btnMapToggle = document.getElementById("mapLayerToggle");
  if (btnMapToggle) {
    btnMapToggle.textContent = isSatellite ? (t.btnStreet || "🗺 Xarita (Davlatlar)") : (t.btnSatellite || "🛰 Sun'iy yo'ldosh");
  }
}

// Event Listeners
guessBtn.addEventListener("click", submitGuess);
nextRoundBtn.addEventListener("click", onNextRound);
btnSubmitScore.addEventListener("click", submitScoreToBot);
btnPlayAgain.addEventListener("click", startNewGame);

const mapLayerToggle = document.getElementById("mapLayerToggle");
if (mapLayerToggle) {
  mapLayerToggle.addEventListener("click", toggleMapLayer);
}

const mapSizeToggle = document.getElementById("mapSizeToggle");
const mapContainer = document.getElementById("mapContainer");
if (mapSizeToggle && mapContainer) {
  mapSizeToggle.addEventListener("click", (e) => {
    e.stopPropagation();
    mapContainer.classList.toggle("maximized");
    mapSizeToggle.textContent = mapContainer.classList.contains("maximized") ? "🗗" : "⛶";
    setTimeout(() => {
      if (map) map.invalidateSize();
    }, 350);
  });
}

const mobileMapBtn = document.getElementById("mobileMapBtn");
if (mobileMapBtn && mapContainer) {
  mobileMapBtn.addEventListener("click", () => {
    mapContainer.classList.remove("collapsed");
    mapContainer.classList.add("expanded");
    mobileMapBtn.classList.add("hidden");
    setTimeout(() => {
      if (map) map.invalidateSize();
    }, 350);
  });
}

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
