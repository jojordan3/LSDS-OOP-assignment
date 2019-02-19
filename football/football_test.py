import unittest
from players import Player, Quarterback
from teams import team_names
from game import Game


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_default_generate_random_games(self):
        games = Game().generate_rand_games()
        self.assertEqual(len(games), 4)
        for game in games:
            self.assertIn(game.teams[0], team_names)
            self.assertIn(game.teams[1], team_names)
            self.assertEqual(list(game.score.keys()), game.teams)
            self.assertEqual({game.teams[0]: 12, game.teams[1]: 28}, game.score)

    def test_field_goal_made(self):
        pass  # TODO

    def test_get_winnerr(self):
        pass  # TODO

#class FootballPlayerTest(unittest.Testcase):
    # Check the default values for Player and Quarterback


if __name__ == '__main__':
    unittest.main()