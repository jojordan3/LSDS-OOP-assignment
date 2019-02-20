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
            self.assertEqual({game.teams[0]: 12, game.teams[1]: 28},
                             game.score)

    def test_field_goal_made(self):
        pass  # TODO

    def test_get_winnerr(self):
        pass  # TODO


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb.passing_score())

    #    def set_stats(self, yards=120, touchdowns=5, safety=1,
    #         interceptions=0):
    #        self.stats = {'yards': yards, 'td': touchdowns, 'fg': field_goals,
    #        'interceptions':interceptions}
    #        return self

    # def test_set_stats_player(self):
    #   player = Player()
    #   player.set_stats()
    #   self.assertEqual()


if __name__ == '__main__':
    unittest.main()
