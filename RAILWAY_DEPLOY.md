# 🚂 Railway.app Serveriga Joylash Bo'yicha To'liq Qo'llanma (Railway Deployment Guide)

Ushbu qo'llanma orqali siz **GeoGuru & GeoGuessr Telegram Bot**ni [Railway.app](https://railway.app) bulutli serveriga 5 daqiqada muammosiz joylab (deploy qilib), 24/7 uzluksiz ishlatishingiz mumkin.

---

## 📁 Tayyorlangan Fayllar
Loyiha ichiga Railway uchun barcha zaruriy konfiguratsiyalar kiritildi:
- [`Dockerfile`](Dockerfile) — Python 3.11-slim asosidagi ishlab chiqarish konteyneri
- [`railway.json`](railway.json) — Railway uchun build va deploy qoidalari
- [`Procfile`](Procfile) — Worker jarayoni deklaratsiyasi
- [`.dockerignore`](.dockerignore) — Konteyner hajmini kichik va xavfsiz saqlash
- [`requirements.txt`](requirements.txt) — Barcha kerakli Python kutubxonalari
- [`runtime.txt`](runtime.txt) — Python 3.11.9 versiyasi

---

## 🚀 1-QADAM: Loyihani GitHub-ga Yuklash (Push to GitHub)

1. Agar hali Git boshlanmagan bo'lsa, loyiha papkasida terminalni oching:
   ```powershell
   git init
   git add .
   git commit -m "GeoGuru & GeoGuessr Bot ready for Railway"
   ```
2. GitHub-da yangi shaxsiy yoki ochiq repozitoriy yarating (masalan: `geoguru-geoguessr-bot`).
3. Kodni GitHub-ga yuklang:
   ```powershell
   git remote add origin https://github.com/USERNAME/geoguru-geoguessr-bot.git
   git branch -M main
   git push -u origin main
   ```

---

## 🚂 2-QADAM: Railway.app da Loyiha Yaratish

1. [Railway.app](https://railway.app) saytiga kiring va GitHub profilingiz orqali tizimga kiring (Login with GitHub).
2. Asosiy sahifada **"New Project"** (Yangi loyiha) tugmasini bosing.
3. **"Deploy from GitHub repo"** bandini tanlang.
4. O'zingiz yuklagan `geoguru-geoguessr-bot` repozitoriyasini tanlang va **"Deploy now"** tugmasini bosing.

Railway avtomatik ravishda loyihangizdagi `Dockerfile`ni aniqlaydi va konteynerni yig'ishni (Build) boshlaydi.

---

## 🔑 3-QADAM: Bot Tokenni Sozlash (Environment Variables)

Bot Telegramga ulanishi uchun unga token berish kerak:

1. Railway-dagi loyihangizga kiring va xizmat (Service) ustiga bosing.
2. Yuqori menyudan **"Variables"** bo'limiga o'ting.
3. **"New Variable"** tugmasini bosing va quyidagilarni kiriting:
   - **VARIABLE_NAME:** `BOT_TOKEN`
   - **VALUE:** `Sizning_Bot_Tokeningiz` (masalan: `123456789:ABCdefGHI...`)
4. Shuningdek (ixtiyoriy, agar standartdan boshqa joyda saqlamoqchi bo'lsangiz):
   - **VARIABLE_NAME:** `DEFAULT_LANGUAGE`
   - **VALUE:** `en`
5. **"Add"** tugmasini bosing. Railway o'zgaruvchilar qo'shilishi bilanoq botni avtomatik ravishda qayta ishga tushiradi!

---

## 💾 4-QADAM (Tavsiya etiladi): Ma'lumotlar Bazasi Uchun Doimiy Xotira (Persistent Volume)

> **💡 Muhim eslatma:** Railway har gal yangi versiya yuklanganda yoki qayta ishga tushganda fayllarni tozalaydi. O'yinchilarning ballari, darajalari (XP), va reytinglari saqlanib qolishi uchun doimiy xotira (Volume) ulash tavsiya etiladi:

1. Railway xizmatining **"Settings"** bo'limiga o'ting.
2. Pastroqqa tushib, **"Volumes"** bo'limini toping va **"Add Volume"** tugmasini bosing.
3. Mount Path (ulanish manzili) sifatida quyidagini yozing:
   ```text
   /app/data
   ```
4. **"Variables"** bo'limiga o'tib, quyidagi o'zgaruvchini qo'shing:
   - **VARIABLE_NAME:** `DB_PATH`
   - **VALUE:** `/app/data/geobot.db`
5. Endi botingiz ma'lumotlar bazasi va kesh fayllari doimiy xotirada saqlanadi va server yangilansa ham ma'lumotlar hech qachon o'chib ketmaydi!

---

## 📊 5-QADAM: Ishlashini Tekshirish (Logs)

1. Railway xizmatining **"Deployments"** yoki **"View Logs"** tugmasini bosing.
2. Loglarda quyidagi yozuv paydo bo'lishini ko'rasiz:
   ```text
   [INFO] GeoBot: Initializing GeoGuru & GeoGuessr Bot...
   [INFO] database.db: Database schema initialized successfully.
   [INFO] GeoBot: Bot started successfully. Waiting for updates...
   [INFO] aiogram.dispatcher: Start polling
   [INFO] aiogram.dispatcher: Run polling for bot @guessrrobot
   ```
3. Telegramga kiring va botingizga `/start` buyrug'ini yuboring. Bot endi 24/7 internetda doimiy faol ishlaydi! 🎉

---

## 🛠 Muammolarni Hal Qilish (Troubleshooting)

- **Q: "Conflict: terminated by other getUpdates request" xatosi chiqsa?**
  - **Javob:** Kompyuteringizda (lokal) `python main.py` hali ishlab turgan bo'lsa, uni to'xtating. Bir vaqtning o'zida bot faqat bitta joyda (Railway-da) ishlashi kerak.
- **Q: Bot javob bermasa?**
  - **Javob:** Railway-dagi `BOT_TOKEN` to'g'ri kiritilganini tekshiring va Logs bo'limidagi xatoliklarni ko'ring.
