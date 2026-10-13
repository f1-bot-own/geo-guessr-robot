"""
Unit tests for game engines: GroupGameSession, SoloGameSession, DailyChallengeSession.
"""
import unittest
import time
from game.engine import GroupGameSession, SoloGameSession, DailyChallengeSession, game_manager

class TestGameEngine(unittest.TestCase):

    def test_group_game_lifecycle(self):
        session = GroupGameSession(chat_id=-100123, mode="mix", total_rounds=2, round_time=20, lang="en")
        self.assertFalse(session.is_active)

        # Round 1
        q1 = session.start_next_round()
        self.assertTrue(session.is_active)
        self.assertTrue(session.is_round_active)
        self.assertEqual(session.current_round, 1)

        # Wrong answer by user 1
        wrong_id = [opt.id for opt in q1.options if not opt.is_correct][0]
        res1 = session.process_answer(user_id=1, user_name="Alice", option_id=wrong_id)
        self.assertEqual(res1.status, "wrong")
        self.assertEqual(res1.penalty, 20)
        self.assertTrue(session.is_round_active)

        # Duplicate answer by user 1 in same round
        res_dup = session.process_answer(user_id=1, user_name="Alice", option_id=q1.correct_option_id)
        self.assertEqual(res_dup.status, "already_answered")

        # Correct answer by user 2
        res2 = session.process_answer(user_id=2, user_name="Bob", option_id=q1.correct_option_id)
        self.assertEqual(res2.status, "correct")
        self.assertGreaterEqual(res2.points_awarded, 100)
        self.assertFalse(session.is_round_active)
        self.assertFalse(res2.is_game_over)

        # Round 2
        q2 = session.start_next_round()
        self.assertEqual(session.current_round, 2)
        res3 = session.process_answer(user_id=1, user_name="Alice", option_id=q2.correct_option_id)
        self.assertEqual(res3.status, "correct")
        self.assertTrue(res3.is_game_over)
        self.assertFalse(session.is_active)

        standings = session.get_standings()
        self.assertEqual(len(standings), 2)
        # Verify standings sorted
        self.assertGreaterEqual(standings[0][2], standings[1][2])

    def test_duel_participants_restriction(self):
        session = GroupGameSession(
            chat_id=-100123,
            mode="flag",
            total_rounds=3,
            round_time=15,
            duel_participants={10, 20}
        )
        q = session.start_next_round()
        
        # User 99 tries to answer
        res_unauthorized = session.process_answer(user_id=99, user_name="Intruder", option_id=q.correct_option_id)
        self.assertEqual(res_unauthorized.status, "not_participant")

        # User 10 answers
        res_valid = session.process_answer(user_id=10, user_name="Player1", option_id=q.correct_option_id)
        self.assertEqual(res_valid.status, "correct")

    def test_solo_game_lifecycle(self):
        solo = SoloGameSession(user_id=500, lang="en")
        self.assertEqual(solo.lives, 3)
        self.assertEqual(solo.score, 0)

        # Question 1
        q1 = solo.next_question()
        wrong_id = [opt.id for opt in q1.options if not opt.is_correct][0]

        # Use 50/50 lifeline
        removed = solo.use_5050()
        expected_removed = 2 if len(q1.options) > 2 else 1
        self.assertEqual(len(removed), expected_removed)
        self.assertFalse(solo.lifelines["5050"])
        # Second call should return empty
        self.assertEqual(solo.use_5050(), [])

        # Use hint
        hint = solo.use_hint()
        self.assertIsNotNone(hint)
        self.assertFalse(solo.lifelines["hint"])

        # Correct answer
        is_corr, is_over, _ = solo.process_answer(q1.correct_option_id)
        self.assertTrue(is_corr)
        self.assertFalse(is_over)
        self.assertEqual(solo.score, 100)

        # Wrong answers until death
        for _ in range(3):
            q = solo.next_question()
            w_id = [opt.id for opt in q.options if not opt.is_correct][0]
            is_corr, is_over, _ = solo.process_answer(w_id)
            self.assertFalse(is_corr)

        self.assertEqual(solo.lives, 0)
        self.assertTrue(is_over)
        self.assertFalse(solo.is_active)

    def test_daily_challenge_lifecycle(self):
        daily = DailyChallengeSession(user_id=999, date_seed="2026-10-10", lang="en")
        self.assertEqual(len(daily.questions), 5)
        self.assertEqual(daily.total_rounds, 5)

        for i in range(5):
            q = daily.start_next_round()
            self.assertIsNotNone(q)
            is_corr, is_done, ans = daily.process_answer(q.correct_option_id)
            self.assertTrue(is_corr)
            if i == 4:
                self.assertTrue(is_done)
            else:
                self.assertFalse(is_done)

        self.assertEqual(daily.score, 500)

if __name__ == "__main__":
    unittest.main()
