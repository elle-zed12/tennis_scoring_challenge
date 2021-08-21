from set import Set
from player import Player
from guido_singleton import Singleton


class Match(Singleton):

    def __init__(self, player1, player2):
        self.set = Set(Player(player1), Player(player2))
        self.game = self.set.current_game
        self.player1 = self.set.current_game.players[0]
        self.player2 = self.set.current_game.players[1]

    def point_won_by(self, player_name):
        if player_name == self.player1.Id:
            self.player1.won_points()
            self.__check_rule()
        elif player_name == self.player2.Id:
            self.player2.won_points()
            self.__check_rule()
        else:
            print('Unknown player')

    def __check_rule(self):
        if self.set.tie_breaker_mode is False:
            self.game.check_status()
            self.set.check_if_set_is_won()
        if self.set.tie_breaker_mode is True:
            self.game.tie_breaker_scoring()
        if self.game.winner is not None and self.set.tie_breaker_mode is True:
            self.set.check_if_set_is_won()
        else:
            return

    def score(self):
        status = f'{self.player1.game_won}-{self.player2.game_won}, {self.game.status}'
        return status


if __name__ == '__main__':  # client
    # expected interface
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    # this will return "0-0, 15-15"
    print(match.score())
    match.point_won_by("player 1")
    match.point_won_by("player 1")
    # this will return "0-0, 40-15"
    print(match.score())
    match.point_won_by("player 2")
    match.point_won_by("player 2")
    # this will return "0-0, Deuce"
    print(match.score())
    match.point_won_by("player 1")
    # this will return "0-0, Advantage player 1"
    print(match.score())
    match.point_won_by("player 1")
    # this will return "1-0, "
    print(match.score())

