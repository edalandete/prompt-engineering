import unittest
from game import play_round

class TestPlayRound(unittest.TestCase):
    def test_tie(self):
        result, user_score, computer_score = play_round('rock', 'rock')
        self.assertEqual(result, "It's a tie!")
        self.assertEqual(user_score, 0)
        self.assertEqual(computer_score, 0)

    def test_user_wins(self):
        result, user_score, computer_score = play_round('rock', 'scissors')
        self.assertEqual(result, "You win!")
        self.assertEqual(user_score, 1)
        self.assertEqual(computer_score, 0)

    def test_computer_wins(self):
        result, user_score, computer_score = play_round('rock', 'paper')
        self.assertEqual(result, "You lose!")
        self.assertEqual(user_score, 0)
        self.assertEqual(computer_score, 1)

if __name__ == '__main__':
    unittest.main()