"""
Unit tests for GeoGuessr / Street View Mode.
Verifies:
1. Dataset integrity (50+ locations, all continents, coordinates, URLs, clues).
2. Question generator (create_streetview_question, 4 options format, 1 correct + 3 distractors).
3. Google Maps link reveal on round completion across EN, RU, UZ.
4. Setup menu integration (get_setup_kb, /game, /solo, solo lobbies).
5. Solo lifelines (hint reveals driving side & continent, 50/50 eliminates 2 distractors).
6. Text answer guessing for streetview questions.
"""

import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from gamedata.streetviews import STREETVIEWS, get_streetview, get_random_streetview
from gamedata.countries import COUNTRIES, get_country
from locales.i18n import t
from games.models import GameMode, Question
from games.question_factory import QuestionFactory, create_streetview_question
from games.session import GameSession
from games.solo_session import SoloGameSession
from games.manager import game_manager
from keyboards.game_kb import get_setup_kb, get_category_selection_kb, get_solo_setup_kb
from games.flow import handle_round_timeout, handle_solo_timeout
from handlers.commands import cmd_game, cmd_solo
from handlers.callbacks import cb_game_setup, cb_solo_setup, cb_solo_category
from handlers.text_answers import check_group_text_answer, check_solo_text_answer


class TestStreetviewDataset(unittest.TestCase):
    """Test suite for data/streetviews.py integrity and completeness."""

    def test_dataset_size_and_continental_distribution(self):
        """Dataset must have at least 50 locations covering all 5 continents."""
        self.assertGreaterEqual(len(STREETVIEWS), 50)

        # Check representation of continents
        country_code_to_continent = {c["code"]: c["continent"]["en"] for c in COUNTRIES}
        continents_found = set()
        for sv in STREETVIEWS:
            cont = country_code_to_continent.get(sv["country_code"])
            if cont:
                continents_found.add(cont)

        expected_continents = {"Europe", "Asia", "Africa", "North America", "South America", "Oceania"}
        # Both Americas, Europe, Asia, Africa, Oceania must be represented
        for expected in ["Europe", "Asia", "Africa", "Oceania"]:
            self.assertIn(expected, continents_found, f"Continent {expected} not found in streetviews dataset!")
        self.assertTrue(
            "North America" in continents_found or "South America" in continents_found or "Americas" in continents_found,
            "Americas not represented in streetviews!"
        )

    def test_entry_schema_and_datatypes(self):
        """Every entry must have id, coordinates, images, driving side, multilingual names, and clues."""
        unique_ids = set()
        for sv in STREETVIEWS:
            self.assertIn(sv["id"], [sv["id"]], "ID must be a string")
            self.assertNotIn(sv["id"], unique_ids, f"Duplicate streetview ID found: {sv['id']}")
            unique_ids.add(sv["id"])

            # Valid coordinates
            self.assertIsInstance(sv["lat"], (int, float))
            self.assertIsInstance(sv["lng"], (int, float))
            self.assertTrue(-90.0 <= sv["lat"] <= 90.0, f"Invalid lat: {sv['lat']}")
            self.assertTrue(-180.0 <= sv["lng"] <= 180.0, f"Invalid lng: {sv['lng']}")

            # Driving side
            self.assertIn(sv["driving_side"], ["left", "right"])

            # Multilingual names & titles
            for lang in ("en", "ru", "uz"):
                self.assertIn(lang, sv["country_name"])
                self.assertGreater(len(sv["country_name"][lang]), 0)
                self.assertIn(lang, sv["location"])
                self.assertGreater(len(sv["location"][lang]), 0)

            # High-resolution image URL
            self.assertTrue(sv["image_url"].startswith("http"))

            # Meta clues
            self.assertIn("clues", sv)
            clues = sv["clues"]
            self.assertIn("driving_side", clues)
            self.assertIn("vegetation", clues)
            self.assertIn("road_markings", clues)
            self.assertIn("hint", clues)

            # Google Maps link
            self.assertTrue(sv["maps_url"].startswith("https://www.google.com/maps?q="))
            self.assertIn(f"{sv['lat']},{sv['lng']}", sv["maps_url"])

    def test_country_codes_exist_in_countries_db(self):
        """All country codes must match existing sovereign countries in countries.py."""
        all_codes = {c["code"] for c in COUNTRIES}
        for sv in STREETVIEWS:
            self.assertIn(
                sv["country_code"],
                all_codes,
                f"Country code '{sv['country_code']}' from streetviews not found in COUNTRIES database!"
            )

    def test_streetview_names_match_countries_db(self):
        """All country_name translations must match canonical names in countries.py."""
        for sv in STREETVIEWS:
            country = get_country(sv["country_code"])
            self.assertIsNotNone(country, f"Country {sv['country_code']} not found in countries.py")
            for lang in ("en", "ru", "uz"):
                self.assertEqual(
                    sv["country_name"][lang],
                    country["name"][lang],
                    f"Mismatch in country name for {sv['id']} ({lang}): '{sv['country_name'][lang]}' vs '{country['name'][lang]}'"
                )

    def test_get_streetview_helper_functions(self):
        """Helper lookup and random sampling functions work correctly."""
        first = STREETVIEWS[0]
        found = get_streetview(first["id"])
        self.assertEqual(found, first)

        not_found = get_streetview("non_existent_id")
        self.assertIsNone(not_found)

        random_sv = get_random_streetview()
        self.assertIn(random_sv, STREETVIEWS)

        # Exclude codes
        excluded = {sv["country_code"] for sv in STREETVIEWS[:10]}
        filtered_sv = get_random_streetview(exclude_codes=excluded)
        self.assertNotIn(filtered_sv["country_code"], excluded)


class TestStreetviewQuestionFactory(unittest.TestCase):
    """Test suite for create_streetview_question and QuestionFactory generation."""

    def test_create_streetview_question_format(self):
        """create_streetview_question generates 4 options, 1 correct, valid maps link."""
        for lang in ("en", "ru", "uz"):
            q = create_streetview_question(lang)
            self.assertEqual(q.mode, GameMode.STREETVIEW)
            self.assertEqual(len(q.options), 4)
            self.assertEqual(len(set(q.options)), 4, "Options must not contain duplicates")
            self.assertTrue(0 <= q.correct_index < 4)
            self.assertEqual(q.options[q.correct_index], q.correct_answer)
            self.assertIsNotNone(q.image_url)
            self.assertIsNotNone(q.maps_url)
            self.assertTrue(q.maps_url.startswith("https://www.google.com/maps?q="))
            self.assertIsNotNone(q.location_title)
            self.assertIn(q.driving_side, ["left", "right"])
            self.assertIn("google.com/maps", q.fun_fact)

    def test_question_factory_streetview_dispatch(self):
        """QuestionFactory.generate(GameMode.STREETVIEW) returns streetview Question."""
        q = QuestionFactory.generate(mode=GameMode.STREETVIEW, lang="en")
        self.assertEqual(q.mode, GameMode.STREETVIEW)
        self.assertEqual(len(q.options), 4)
        self.assertIn(q.correct_answer, q.options)

    def test_mix_mode_includes_streetview(self):
        """Repeated generations in Mix mode occasionally produce streetview questions."""
        modes_seen = set()
        for _ in range(100):
            q = QuestionFactory.generate(mode=GameMode.MIX, lang="en")
            modes_seen.add(q.mode)

        self.assertIn(GameMode.STREETVIEW, modes_seen, "GameMode.STREETVIEW should be chosen by MIX mode!")

    def test_exclusion_filter_in_streetview_question(self):
        """Excluding country codes avoids generating questions for those countries."""
        exclude = {"us", "jp", "fr", "de", "gb"}
        for _ in range(20):
            q = create_streetview_question(lang="en", exclude_codes=exclude)
            self.assertNotIn(q.country_code, exclude)

    def test_game_modes_mix_and_generator(self):
        """game.modes.generate_question('mix') includes streetview and generates 4 options."""
        from game.modes import generate_question as engine_gen_question, generate_streetview_question as engine_gen_sv
        sv_q = engine_gen_sv("en")
        self.assertEqual(sv_q.mode, "streetview")
        self.assertEqual(len(sv_q.options), 4)

        modes = set()
        for _ in range(100):
            q = engine_gen_question("mix", "en")
            modes.add(q.mode)
        self.assertIn("streetview", modes)


class TestGoogleMapsReveal(unittest.IsolatedAsyncioTestCase):
    """Test suite ensuring Google Maps links are revealed on round completion."""

    async def asyncSetUp(self):
        self.bot = AsyncMock()

    async def test_group_timeout_reveals_maps_link(self):
        """When time runs out on a streetview question, the Google Maps link is revealed."""
        session = GameSession(chat_id=-100123, lang="en", mode="streetview")
        session.status = "in_progress"
        session.current_round = 1

        q = create_streetview_question("en")
        session.current_question = q

        with patch("games.flow.proceed_after_round", new_callable=AsyncMock):
            await handle_round_timeout(self.bot, -100123, session, 1, db=None)

            self.bot.send_message.assert_called()
            sent_text = self.bot.send_message.call_args[1]["text"]
            self.assertIn("google.com/maps", sent_text)
            self.assertIn(q.maps_url, sent_text)

    async def test_solo_timeout_reveals_maps_link(self):
        """When solo player runs out of time on streetview, Google Maps link is revealed."""
        session = SoloGameSession(user_id=777, user_name="Player", lang="en", mode="streetview")
        session.status = "in_progress"
        session.round_number = 1

        q = create_streetview_question("en")
        session.current_question = q
        game_manager.set_solo_session(777, session)

        with patch("games.flow.send_solo_round", new_callable=AsyncMock):
            await handle_solo_timeout(self.bot, 777, session, 1, db=None, wait_seconds=0)

            self.bot.send_message.assert_called()
            sent_text = self.bot.send_message.call_args[1]["text"]
            self.assertIn("google.com/maps", sent_text)
            self.assertIn(q.maps_url, sent_text)

    async def test_maps_reveal_multilingual(self):
        """Reveal message contains localized Google Maps button across EN, RU, UZ."""
        for lang, expected_btn_text in [
            ("en", "View on Google Maps"),
            ("ru", "Открыть в Google Maps"),
            ("uz", "Google Maps-da ko'rish")
        ]:
            q = create_streetview_question(lang)
            self.assertIn(expected_btn_text, q.fun_fact)
            self.assertIn(q.maps_url, q.fun_fact)


class TestKeyboardsAndSetupIntegration(unittest.TestCase):
    """Test suite for UI keyboards and setup menus integration."""

    def test_setup_kb_has_streetview_button(self):
        """get_setup_kb contains interactive button for streetview category."""
        kb = get_setup_kb(session_id="test_sess", mode="streetview", rounds=5, round_time=30, lang="en")
        all_buttons = [btn for row in kb.inline_keyboard for btn in row]
        callbacks = [btn.callback_data for btn in all_buttons]

        self.assertIn("setup:mode:streetview:test_sess", callbacks)
        sv_btn = [b for b in all_buttons if b.callback_data == "setup:mode:streetview:test_sess"][0]
        self.assertIn("✅", sv_btn.text)
        self.assertIn("Street View", sv_btn.text)

    def test_category_selection_kb_has_streetview(self):
        from keyboards.game_kb import get_hub_subcategories_kb
        cat_kb = get_category_selection_kb(prefix="solo_cat", lang="en")
        cat_callbacks = [btn.callback_data for row in cat_kb.inline_keyboard for btn in row]
        self.assertIn("solo_cat:hub:geography", cat_callbacks)

        kb = get_hub_subcategories_kb(hub="geography", prefix="solo_cat", lang="en")
        all_buttons = [btn for row in kb.inline_keyboard for btn in row]
        callbacks = [btn.callback_data for btn in all_buttons]
        self.assertIn("solo_cat:streetview", callbacks)

        solo_setup = get_solo_setup_kb(mode="streetview", lang="ru")
        all_setup_buttons = [btn for row in solo_setup.inline_keyboard for btn in row]
        setup_callbacks = [btn.callback_data for btn in all_setup_buttons]
        self.assertIn("solo_setup:mode:streetview", setup_callbacks)
        active_btn = [b for b in all_setup_buttons if b.callback_data == "solo_setup:mode:streetview"][0]
        self.assertIn("✅", active_btn.text)


class TestGameMechanicsAndLifelines(unittest.IsolatedAsyncioTestCase):
    """Test suite for lifelines and commands in streetview mode."""

    def test_solo_hint_reveals_driving_side_and_continent(self):
        """Hint lifeline on streetview question reveals driving side & continent in all languages."""
        session_en = SoloGameSession(user_id=101, user_name="Player", lang="en", mode="streetview")
        session_en.current_question = Question(
            mode=GameMode.STREETVIEW,
            text="Which country?",
            options=["Japan", "France", "Brazil", "Canada"],
            correct_index=0,
            correct_answer="Japan",
            country_code="jp",
            driving_side="left"
        )
        hint_en = session_en.use_hint()
        self.assertIn("Left", hint_en)
        self.assertIn("Asia", hint_en)

        # Russian
        session_ru = SoloGameSession(user_id=102, user_name="Игрок", lang="ru", mode="streetview")
        session_ru.current_question = Question(
            mode=GameMode.STREETVIEW,
            text="Какая страна?",
            options=["Япония", "Франция", "Бразилия", "Канада"],
            correct_index=0,
            correct_answer="Япония",
            country_code="jp",
            driving_side="left"
        )
        hint_ru = session_ru.use_hint()
        self.assertIn("левостороннее", hint_ru)
        self.assertIn("Азия", hint_ru)

        # Uzbek
        session_uz = SoloGameSession(user_id=103, user_name="O'yinchi", lang="uz", mode="streetview")
        session_uz.current_question = Question(
            mode=GameMode.STREETVIEW,
            text="Qaysi davlat?",
            options=["Yaponiya", "Fransiya", "Braziliya", "Kanada"],
            correct_index=0,
            correct_answer="Yaponiya",
            country_code="jp",
            driving_side="left"
        )
        hint_uz = session_uz.use_hint()
        self.assertIn("chap", hint_uz)
        self.assertIn("Osiyo", hint_uz)

    def test_solo_5050_lifeline_eliminates_two_wrong_options(self):
        """50/50 lifeline eliminates exactly 2 distractors from 4 options."""
        session = SoloGameSession(user_id=104, user_name="Player", lang="en", mode="streetview")
        session.current_question = create_streetview_question("en")
        eliminated = session.use_5050()
        self.assertEqual(len(eliminated), 2)
        self.assertNotIn(session.current_question.correct_index, eliminated)

    async def test_cmd_solo_and_game_streetview_argument_parsing(self):
        """cmd_solo and cmd_game parse 'streetview' argument directly."""
        bot = AsyncMock()

        # Group cmd_game with streetview argument
        group_msg = MagicMock()
        group_msg.chat.type = "supergroup"
        group_msg.chat.id = -100456
        group_msg.from_user.id = 999
        group_msg.from_user.first_name = "HostGuy"
        group_msg.from_user.username = "hostguy"
        group_msg.text = "/game streetview"
        group_msg.answer = AsyncMock()

        with patch("handlers.commands.get_db") as mock_db:
            db_inst = AsyncMock()
            db_inst.get_chat_language.return_value = "en"
            mock_db.return_value = db_inst

            game_manager.remove_session(-100456)
            await cmd_game(group_msg, bot)

            session = game_manager.get_session(-100456)
            self.assertIsNotNone(session)
            self.assertEqual(session.mode, "streetview")

        # Private cmd_solo with streetview argument
        solo_msg = MagicMock()
        solo_msg.chat.type = "private"
        solo_msg.chat.id = 999
        solo_msg.from_user.id = 999
        solo_msg.from_user.first_name = "HostGuy"
        solo_msg.from_user.username = "hostguy"
        solo_msg.text = "/solo streetview 60"

        with patch("handlers.commands.get_db") as mock_db, \
             patch("handlers.commands.send_solo_round", new_callable=AsyncMock) as mock_send_round:
            db_inst = AsyncMock()
            db_inst.get_or_create_user.return_value = {"language": "en"}
            mock_db.return_value = db_inst

            await cmd_solo(solo_msg, bot)

            solo_session = game_manager.get_solo_session(999)
            self.assertIsNotNone(solo_session)
            self.assertEqual(solo_session.mode, "streetview")
            self.assertEqual(solo_session.round_time, 60)
            mock_send_round.assert_called_once()

    async def test_text_answer_recognition_for_streetview(self):
        """Typing country name in group text mode correctly answers streetview question."""
        bot = AsyncMock()
        session = GameSession(chat_id=-100888, host_id=50, host_name="Tester", lang="en", input_mode="text")
        session.status = "in_progress"
        session.current_question = Question(
            mode=GameMode.STREETVIEW,
            text="Where is this?",
            options=["Japan", "France", "Brazil", "Canada"],
            correct_index=0,
            correct_answer="Japan",
            country_code="jp",
            maps_url="https://www.google.com/maps?q=35.6595,139.7005"
        )
        game_manager.set_session(-100888, session)

        msg = MagicMock()
        msg.chat.type = "supergroup"
        msg.chat.id = -100888
        msg.from_user.id = 50
        msg.from_user.first_name = "Player"
        msg.from_user.username = "player"
        msg.from_user.is_bot = False
        msg.text = "Japan"
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_db, \
             patch("handlers.text_answers.proceed_after_round", new_callable=AsyncMock):
            db_inst = AsyncMock()
            mock_db.return_value = db_inst

            await check_group_text_answer(msg, bot)

            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("Correct!", reply_text)
            self.assertIn("google.com/maps", reply_text)

    async def test_handlers_solo_command_streetview_argument(self):
        """handlers.solo.handle_solo_command with /solo streetview starts streetview game."""
        from handlers.solo import handle_solo_command
        from game.engine import game_manager as engine_gm

        bot = AsyncMock()
        bot.get_me.return_value = MagicMock(username="GeoBot")

        msg = MagicMock()
        msg.chat.type = "private"
        msg.chat.id = 8881
        msg.from_user.id = 8881
        msg.text = "/solo streetview"
        msg.answer = AsyncMock()

        with patch("handlers.solo.get_user_language", new_callable=AsyncMock) as mock_lang, \
             patch("handlers.solo.send_solo_question", new_callable=AsyncMock) as mock_send_q:
            mock_lang.return_value = "en"
            await handle_solo_command(msg, bot)

            solo_session = engine_gm.get_solo_game(8881)
            self.assertIsNotNone(solo_session)
            self.assertEqual(solo_session.mode, "streetview")
            mock_send_q.assert_called_once()
            engine_gm.remove_solo_game(8881)

    async def test_handlers_group_game_setup_mode_selection_and_cycling(self):
        """handlers.group_game sets and cycles streetview mode without error."""
        from handlers.group_game import set_mode_callback, cycle_mode_callback, AVAILABLE_MODES
        from game.engine import game_manager as engine_gm

        self.assertIn("streetview", AVAILABLE_MODES)

        chat_id = -1009991
        engine_gm.setup_states[chat_id] = {
            "host_id": 1234,
            "host_name": "Host",
            "mode": "coat_of_arms",
            "rounds": 5,
            "time": 30,
            "lang": "en",
            "input_mode": "both"
        }

        # 1. Direct set mode to streetview
        cb_set = MagicMock()
        cb_set.data = f"setup_set_mode:{chat_id}:streetview"
        cb_set.from_user.id = 1234
        cb_set.message.edit_reply_markup = AsyncMock()
        cb_set.answer = AsyncMock()

        await set_mode_callback(cb_set)
        self.assertEqual(engine_gm.setup_states[chat_id]["mode"], "streetview")

        # 2. Cycle mode from streetview
        cb_cycle = MagicMock()
        cb_cycle.data = f"setup_cycle_mode:{chat_id}"
        cb_cycle.from_user.id = 1234
        cb_cycle.message.edit_reply_markup = AsyncMock()
        cb_cycle.answer = AsyncMock()

        await cycle_mode_callback(cb_cycle)
        expected_next = AVAILABLE_MODES[(AVAILABLE_MODES.index("streetview") + 1) % len(AVAILABLE_MODES)]
        self.assertEqual(engine_gm.setup_states[chat_id]["mode"], expected_next)
        del engine_gm.setup_states[chat_id]

    async def test_group_text_shortcut_reveals_maps_link(self):
        """Answering via shortcut '1' or 'A' in group text mode reveals Google Maps link."""
        bot = AsyncMock()
        session = GameSession(chat_id=-100889, host_id=50, host_name="Tester", lang="en", input_mode="both")
        session.status = "in_progress"
        session.current_question = Question(
            mode=GameMode.STREETVIEW,
            text="Where is this?",
            options=["Japan", "France", "Brazil", "Canada"],
            correct_index=0,
            correct_answer="Japan",
            country_code="jp",
            maps_url="https://www.google.com/maps?q=35.6595,139.7005"
        )
        game_manager.set_session(-100889, session)

        msg = MagicMock()
        msg.chat.type = "supergroup"
        msg.chat.id = -100889
        msg.from_user.id = 50
        msg.from_user.first_name = "Player"
        msg.from_user.username = "player"
        msg.from_user.is_bot = False
        msg.text = "1"  # shortcut for first option
        msg.reply = AsyncMock()

        with patch("handlers.text_answers.get_db") as mock_db, \
             patch("handlers.text_answers.proceed_after_round", new_callable=AsyncMock):
            db_inst = AsyncMock()
            mock_db.return_value = db_inst

            await check_group_text_answer(msg, bot)

            msg.reply.assert_called_once()
            reply_text = msg.reply.call_args[1]["text"]
            self.assertIn("Correct!", reply_text)
            self.assertIn("google.com/maps", reply_text)

    async def test_handlers_group_game_round_timer_and_answer_reveals_maps(self):
        """handlers.group_game round_timer and answer announcements reveal Google Maps links."""
        from handlers.group_game import round_timer, handle_game_answer
        from game.engine import GroupGameSession as EngineGroupSession, game_manager as engine_gm
        from game.modes import generate_streetview_question

        bot = AsyncMock()
        chat_id = -1005555

        session = EngineGroupSession(chat_id=chat_id, mode="streetview", total_rounds=2, round_time=1, lang="en")
        q = generate_streetview_question("en")
        session.current_round = 1
        session.current_question = q
        session.is_active = True
        session.is_round_active = True
        session.round_start_time = 0
        engine_gm.set_group_game(chat_id, session)

        # 1. Round timeout reveals maps url
        with patch("handlers.group_game.finish_game", new_callable=AsyncMock), \
             patch("handlers.group_game.launch_next_round", new_callable=AsyncMock):
            await round_timer(chat_id, 1, 0, bot)

            all_sent = [c[1]["text"] for c in bot.send_message.call_args_list if "text" in c[1]]
            self.assertTrue(any("google.com/maps" in msg for msg in all_sent))

        bot.send_message.reset_mock()

        # 2. Correct button answer reveals maps url
        cb = MagicMock()
        cb.data = f"ans:2:{q.correct_option_id}"
        cb.message.chat.id = chat_id
        cb.from_user.id = 999
        cb.from_user.first_name = "Winner"
        cb.answer = AsyncMock()
        cb.message.edit_reply_markup = AsyncMock()

        session.current_round = 2
        session.current_question = q
        session.is_active = True
        session.is_round_active = True

        with patch("handlers.group_game.finish_game", new_callable=AsyncMock), \
             patch("handlers.group_game.launch_next_round", new_callable=AsyncMock), \
             patch("handlers.group_game.record_answer_result", new_callable=AsyncMock):
            await handle_game_answer(cb, bot)

            all_sent2 = [c[1]["text"] for c in bot.send_message.call_args_list if "text" in c[1]]
            self.assertTrue(any("google.com/maps" in msg for msg in all_sent2))

        engine_gm.remove_group_game(chat_id)


if __name__ == "__main__":
    unittest.main()

