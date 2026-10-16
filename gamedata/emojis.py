"""
Emoji Riddles Dataset for GeoGuru & GeoGuessr.
Contains 65+ curated iconic emoji riddles representing countries worldwide.
"""

EMOJI_RIDDLES = [
    # Asia
    {"code": "uz", "emojis": "🫓 🕌 🍇", "hint": {"uz": "O'zbekiston noni, qadimiy Registon va shirin uzumlar", "ru": "Лепешки, мечети Самарканда и сладкий виноград", "en": "Tandir bread, ancient mosques and sweet grapes"}},
    {"code": "jp", "emojis": "🍣 ⛩️ 🗻", "hint": {"uz": "Sushi, Torii darvozasi va Fuji tog'i", "ru": "Суши, священные тории и вулкан Фудзияма", "en": "Sushi, Torii shrine gates and Mount Fuji"}},
    {"code": "cn", "emojis": "🐼 🥟 🐉", "hint": {"uz": "Panda, chuchvara va afsonaviy ajdarho", "ru": "Панда, пельмени димсам и дракон", "en": "Giant panda, dumplings and mythical dragon"}},
    {"code": "in", "emojis": "🍛 🪷 🐅", "hint": {"uz": "Karri taomi, lotos guli va Bengaliya yo'lbarsi", "ru": "Острое карри, лотос и бенгальский тигр", "en": "Spicy curry, sacred lotus and Bengal tiger"}},
    {"code": "sa", "emojis": "🌴 🐪 🛢️", "hint": {"uz": "Xurmo daraxtlari, tuyalar va neft boyliklari", "ru": "Финики, верблюды и нефтяные богатства", "en": "Date palms, desert camels and petroleum"}},
    {"code": "kr", "emojis": "🥢 🎤 🥟", "hint": {"uz": "K-pop musiqasi, tayoqchalar va kimchili taomlar", "ru": "К-поп культура, палочки для еды и кимчи", "en": "K-pop music, chopsticks and spicy cuisine"}},
    {"code": "tr", "emojis": "🥙 ☕ 🕌", "hint": {"uz": "Kebab, turk qahvasi va moviy masjidlar", "ru": "Кебаб, кофе по-турецки и мечети Стамбула", "en": "Doner kebab, Turkish coffee and iconic mosques"}},
    {"code": "kz", "emojis": "🐎 ⛺ 🦅", "hint": {"uz": "Keng dashtlar, bedov otlar va burgutlar", "ru": "Бескрайние степи, кони и степные беркуты", "en": "Steppe horses, yurts and golden eagles"}},
    {"code": "th", "emojis": "🐘 🥥 🥊", "hint": {"uz": "Oq fillar, kokos palmalari va Muay-Tay", "ru": "Слоны, кокосы и тайский бокс Муай-Тай", "en": "Sacred elephants, coconuts and Muay Thai"}},
    {"code": "ae", "emojis": "🏙️ 🏎️ 🏜️", "hint": {"uz": "Burj Xalifa, superkarlar va qum sahrosi", "ru": "Бурдж-Халифа, суперкары и дубайская пустыня", "en": "Burj Khalifa sky-scrapers, supercars and desert"}},
    {"code": "id", "emojis": "🏝️ 🌋 🦎", "hint": {"uz": "Tropik orollar, vulqonlar va Komodo ajdahosi", "ru": "Тысячи островов, вулканы и дракон Комодо", "en": "Tropical islands, volcanoes and Komodo dragons"}},
    {"code": "vn", "emojis": "🍜 🛵 🏮", "hint": {"uz": "Fo sho'rvasi, ko'p millionli skuterlar va fonuslar", "ru": "Суп фо, миллионы мопедов и шелковые фонарики", "en": "Pho noodle soup, mopeds and lanterns"}},
    {"code": "ge", "emojis": "🥟 🍷 🏔️", "hint": {"uz": "Xinkali, qadimiy vinolar va Kavkaz tog'lari", "ru": "Хинкали, родина виноделия и горы Кавказа", "en": "Khinkali, ancient winemaking and Caucasus peaks"}},
    {"code": "kg", "emojis": "🏔️ ⛺ 🐴", "hint": {"uz": "Tyan-Shan tog'lari, kigiz o'tovlar va Issiqko'l", "ru": "Горы Тянь-Шаня, юрты и озеро Иссык-Куль", "en": "Tien Shan mountains, felt yurts and horses"}},
    {"code": "tj", "emojis": "🏔️ 💧 🍇", "hint": {"uz": "Pomir 'Dunyo tomi' va Nurek suv ombori", "ru": "Памир («Крыша мира») и чистейшие горные реки", "en": "Pamir Mountains (Roof of the World) and reservoirs"}},
    {"code": "tm", "emojis": "🐎 🏛️ 🕳️", "hint": {"uz": "Ahalteka arg'umoqlari va 'Jahannam darvozasi' gaz krateri", "ru": "Ахалтекинские скакуны и газовый кратер Дарваза", "en": "Akhal-Teke horses and Darvaza Gas Crater"}},
    {"code": "az", "emojis": "🔥 🫖 🛢️", "hint": {"uz": "Olovlar yurti, armudu stakandagi choy va Kaspiy nefti", "ru": "Страна огней, стаканы армуду и Каспийская нефть", "en": "Land of fire, armudu tea glasses and Caspian oil"}},
    {"code": "pk", "emojis": "🏏 🏔️ 🥭", "hint": {"uz": "Kriket, K2 cho'qqisi va shirin mango", "ru": "Крикет, горная вершина К2 и сладкие манго", "en": "Cricket passion, K2 peak and sweet mangoes"}},

    # Europe
    {"code": "it", "emojis": "🍕 🍝 🏛️", "hint": {"uz": "Pitsa, pasta va Rim Kolizeyi", "ru": "Пицца, паста и римский Колизей", "en": "Pizza, pasta and the Roman Colosseum"}},
    {"code": "fr", "emojis": "🥐 🥖 🗼", "hint": {"uz": "Kruassan, baget va Eyfel minorasi", "ru": "Круассаны, багеты и Эйфелева башня", "en": "Croissants, baguettes and the Eiffel Tower"}},
    {"code": "de", "emojis": "🍺 🥨 🚗", "hint": {"uz": "Pivo, bretsel va sifatli avtomobillar", "ru": "Октоберфест, крендели и знаменитый автопром", "en": "Oktoberfest, pretzels and world-class cars"}},
    {"code": "gb", "emojis": "🍵 👑 🚌", "hint": {"uz": "Besh choyi, qirolicha toji va qizil avtobus", "ru": "Файв-о-клок чай, корона и красный двухэтажный автобус", "en": "Five o'clock tea, royal crown and red double-decker bus"}},
    {"code": "es", "emojis": "🥘 💃 🐂", "hint": {"uz": "Paella, flamenko raqsi va buqalar jangi", "ru": "Паэлья, страстное фламенко и коррида", "en": "Paella, flamenco dancing and the bull"}},
    {"code": "ch", "emojis": "🧀 🍫 🏔️", "hint": {"uz": "Shveytsariya pishlog'i, shokolad va Alp tog'lari", "ru": "Швейцарский сыр, шоколад и Альпы", "en": "Swiss cheese, chocolates and the snowy Alps"}},
    {"code": "nl", "emojis": "🌷 🧀 🚲", "hint": {"uz": "Lola dalalari, pishloq va millionlab velosipedlar", "ru": "Поля тюльпанов, сыр и велосипеды", "en": "Tulip fields, Gouda cheese and windmills/bicycles"}},
    {"code": "gr", "emojis": "🏛️ 🫒 🏺", "hint": {"uz": "Akropol ibodatxonasi, zaytun mevasi va olimpiada vatani", "ru": "Акрополь, оливки и родина Олимпийских игр", "en": "The Acropolis, olives and origin of the Olympics"}},
    {"code": "ru", "emojis": "🪆 🐻 ❄️", "hint": {"uz": "Matryoshka qo'g'irchog'i, ayiq va Sibir qahratoni", "ru": "Матрешка, медведь и сибирские морозы", "en": "Matryoshka dolls, brown bear and winter snow"}},
    {"code": "pt", "emojis": "🥧 ⚽ 🌊", "hint": {"uz": "Pastel de nata shirinligi, futbol va Atlantika to'lqinlari", "ru": "Паштел-де-ната, футбол Криштиану и океан", "en": "Pastel de nata pastry, football and Atlantic surf"}},
    {"code": "no", "emojis": "❄️ 🏔️ 🎣", "hint": {"uz": "Fjordlar, qorli tog'lar va losos balig'i", "ru": "Фьорды, снежные вершины и северная рыбалка", "en": "Glacial fjords, Nordic snow and salmon fishing"}},
    {"code": "se", "emojis": "🛋️ 🦌 🌲", "hint": {"uz": "IKEA mebellari, shimoliy bug'u va qalin o'rmonlar", "ru": "Дизайн IKEA, северный олень и хвойные леса", "en": "IKEA design, moose and evergreen forests"}},
    {"code": "fi", "emojis": "🧖 🎅 📱", "hint": {"uz": "Fin saunasi, Santa-Klaus vatani va Nokia", "ru": "Сауна, Лапландия Санта-Клауса и северное сияние", "en": "Finnish sauna, home of Santa Claus and northern lights"}},
    {"code": "be", "emojis": "🧇 🍫 🍻", "hint": {"uz": "Bryussel vaflilari, shokolad va abbat pivosi", "ru": "Бельгийские вафли, шоколадные конфеты и пенное", "en": "Belgian waffles, artisan chocolates and abbey brews"}},
    {"code": "at", "emojis": "🎻 ⛷️ 🏔️", "hint": {"uz": "Motsart klassik musiqasi, tog' chang'isi va Vena", "ru": "Классическая музыка Моцарта, горные лыжи и Вена", "en": "Mozart's classical music, ski resorts and Vienna"}},
    {"code": "ie", "emojis": "🍀 🍻 🌈", "hint": {"uz": "To'rt bargli beda, Ginness pivosi va Leprekon afsonasi", "ru": "Клевер-трилистник, Гиннесс и день Святого Патрика", "en": "Four-leaf clover, dark stout and St. Patrick"}},
    {"code": "pl", "emojis": "🥟 🏰 🦬", "hint": {"uz": "Pirogi chuchvarasi, qadimiy qal'alar va Belovej zubrlari", "ru": "Вареники-пероги, средневековые замки и зубры", "en": "Pierogi dumplings, royal castles and European bison"}},
    {"code": "ua", "emojis": "🍲 🌻 🌾", "hint": {"uz": "Ukrain borschli sho'rvasi, kungaboqar dalalari va bug'doy", "ru": "Борщ, золотые поля подсолнухов и пшеница", "en": "Traditional borscht, vast sunflower fields and wheat"}},

    # Americas
    {"code": "us", "emojis": "🍔 🗽 🏈", "hint": {"uz": "Burger, Ozodlik haykali va Amerika futboli", "ru": "Бургеры, Статуя Свободы и американский футбол", "en": "Cheeseburgers, Statue of Liberty and gridiron football"}},
    {"code": "br", "emojis": "⚽ ☕ 🌴", "hint": {"uz": "Samba karnavali, futbol va Amazonka o'rmonlari", "ru": "Карнавал в Рио, кофе и джунгли Амазонки", "en": "Samba carnival, coffee beans and Amazon rainforest"}},
    {"code": "mx", "emojis": "🌮 🌵 🎺", "hint": {"uz": "Tako, sahro kaktusi va Mariachi musiqachilari", "ru": "Тако, кактусы и зажигательная музыка мариачи", "en": "Tacos, desert cactus and Mariachi brass bands"}},
    {"code": "ca", "emojis": "🍁 🏒 🐻", "hint": {"uz": "Chinor yaprog'i, xokkey va qutb ayiqlari", "ru": "Кленовый лист, хоккей на льду и бурые медведи", "en": "Maple leaf syrup, ice hockey and grizzly bears"}},
    {"code": "ar", "emojis": "🥩 ⚽ 💃", "hint": {"uz": "Asado go'shti, Lionel Messi va Tango raqsi", "ru": "Сочные стейки асадо, футбол Месси и танго", "en": "Juicy asado steaks, football legends and passion of tango"}},
    {"code": "cl", "emojis": "🌶️ 🏔️ 🗿", "hint": {"uz": "Ingichka uzun mamlakat, And tog'lari va Pasxa oroli toshlari", "ru": "Узкая страна вдоль Анд и истуканы Моаи", "en": "Long coastline along the Andes and Easter Island Moai"}},
    {"code": "pe", "emojis": "🦙 🏛️ 🌽", "hint": {"uz": "Lama hayvoni, Machu-Pikchu qadimiy shahri va rangli makkajo'xori", "ru": "Ламы, загадочный Мачу-Пикчу и цивилизация инков", "en": "Llamas, ancient Machu Picchu citadel and Inca heritage"}},
    {"code": "co", "emojis": "☕ 🌸 💃", "hint": {"uz": "Mashhur Kolumbiya qahvasi, orxideyalar va salsa", "ru": "Колумбийский арабика кофе, орхидеи и сальса", "en": "Supreme Colombian coffee, exotic orchids and salsa"}},
    {"code": "cu", "emojis": "🚗 🎷 🌴", "hint": {"uz": "Retro mashinalar, Gavana va Karib dengizi", "ru": "Ретро-автомобили, кубинские сигары и Гавана", "en": "Vintage retro cars, Caribbean rhythm and Havana"}},

    # Africa
    {"code": "eg", "emojis": "🐫 🏛️ 🏺", "hint": {"uz": "Giza piramidalari, tuya va Nil daryosi sivilizatsiyasi", "ru": "Пирамиды Гизы, верблюды и древняя река Нил", "en": "Pyramids of Giza, camels and ancient Nile civilization"}},
    {"code": "za", "emojis": "🦁 💎 🏉", "hint": {"uz": "Safari sherlari, olmos konlari va regbi chempionlari", "ru": "Сафари со львами, алмазы и пингвины мыса Доброй Надежды", "en": "African safari lions, diamond mines and Table Mountain"}},
    {"code": "ma", "emojis": "🕌 🫖 🍊", "hint": {"uz": "Sharqiy bozorlar, yalpizli choy va mandarinlar", "ru": "Пестрые базары Марракеша, мятный чай и мандарины", "en": "Marrakech souks, mint tea and Moroccan arches"}},
    {"code": "ke", "emojis": "🦁 🦒 🏃", "hint": {"uz": "Buyuk savannalar, jirafalar va marafon chempionlari", "ru": "Дикая саванна Масаи-Мара, жирафы и марафонцы", "en": "Great savanna wildlife, giraffes and marathon runners"}},
    {"code": "ng", "emojis": "🛢️ 🦅 🎬", "hint": {"uz": "Nollywood kinosi, Afrika burguti va boy neft konlari", "ru": "Африканский кинематограф Нолливуд, орлы и нефть", "en": "Nollywood cinema, super eagles and natural resources"}},
    {"code": "mg", "emojis": "🐒 🌴 🏝️", "hint": {"uz": "Lemur maymunlari, Baobab daraxtlari xiyoboni va ulkan orol", "ru": "Забавные лемуры, аллея баобабов и экзотический остров", "en": "Ring-tailed lemurs, avenue of the baobabs and island"}},
    {"code": "et", "emojis": "☕ 🏃 👑", "hint": {"uz": "Qahvaning asl vatani va qadimiy afsonaviy podshohlik", "ru": "Родина кофейного зерна и древнейшая цивилизация", "en": "Historic birthplace of coffee and ancient highlands"}},
    {"code": "tz", "emojis": "🏔️ 🦁 🏝️", "hint": {"uz": "Kilimanjaro qorli cho'qqisi va Zanzibar moviy oroli", "ru": "Вулкан Килиманджаро, сафари Серенгети и Занзибар", "en": "Mount Kilimanjaro, Serengeti wildlife and Zanzibar"}},

    # Oceania
    {"code": "au", "emojis": "🦘 🐨 🏜️", "hint": {"uz": "Kenguru, koala va qizil qumli ulkan materik", "ru": "Кенгуру, сонные коалы и Сиднейская опера", "en": "Kangaroos, koalas and the vast red outback"}},
    {"code": "nz", "emojis": "🥝 🐑 🏉", "hint": {"uz": "Kivi qushi, cheksiz qo'y podalari va 'Uzuklar Hukmdori' manzaralari", "ru": "Птица киви, пейзажи «Властелина колец» и регби All Blacks", "en": "Kiwi bird, sheep pastures and Middle-earth scenery"}},
]

EMOJI_BY_CODE = {item["code"]: item for item in EMOJI_RIDDLES}

def get_emoji_riddle(country_code: str):
    return EMOJI_BY_CODE.get(country_code.lower())
