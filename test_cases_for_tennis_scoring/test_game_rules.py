import unittest
from match import Match


class TestGameRules(unittest.TestCase):

    def test_point_won_method_is_increasing_player_points(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 1')
        match.point_won_by('player 1')
        self.assertEqual(3, match.player1.points)

    def test_match_score_method_returns_status_correctly(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        self.assertEqual('0-0, 15-15', match.score())

    def test_player_NOT_advantage_when_one_player_has_below_3points_with_1_point_ahead(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        self.assertEqual('0-0, 40-30', match.score())

    def test_player_is_advantage_when_both_player_has_above_3points_with_1_point_ahead(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        self.assertEqual('0-0, Advantage player 2', match.score())

    def test_match_score_is_deuce_if_both_has_3_points_or_above_and_has_equal_points(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        self.assertEqual('0-0, deuce', match.score())

    def test_NOT_deuce_if_player_points_are_equal_but_less_than_3points(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        self.assertEqual('0-0, 30-30', match.score())

    # A game is won by the first player
    # to have won at least 4 points in total and at least 2 points more than the opponent.
    def test_game_is_won_when_player_gets_4_points_with_2_points_advantage(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 1')
        match.point_won_by('player 1')
        self.assertEqual('1-0, ', match.score())

    def test_game_is_NOT_won_when_player_gets_above_4points_with_only_1point_advantage(self):
        match = Match('player 1', 'player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        match.point_won_by('player 2')
        match.point_won_by('player 1')
        self.assertEqual('0-0, Advantage player 1', match.score())


if __name__ == '__main__':
    unittest.main()

