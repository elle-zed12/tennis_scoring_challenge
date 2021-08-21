from game import Game


class Set:

    def __init__(self, player1, player2):
        self.all_games = []
        self.winner = None
        self.current_game = None
        self.counter = 0
        self.add_game(player1, player2)
        self.tie_breaker_mode = False

    def add_game(self, player1, player2):
        a_game = Game(player1, player2)
        self.all_games.append(a_game)
        self.current_game = a_game
        self.current_game.reset_players_score()

    def check_if_set_is_won(self):
        player1 = self.current_game.players[0]
        player2 = self.current_game.players[1]
        lower_limit = 6
        max_diff = 2
        player1_diff_game_won = player1.game_won - player2.game_won
        player2_diff_game_won = player2.game_won - player1.game_won
        if player1.game_won >= lower_limit or player2.game_won >= lower_limit:
            if player1_diff_game_won == 0:
                self.tie_breaker(player1, player2)
            elif player1_diff_game_won >= max_diff:
                self.winner = player1
                self.counter += 1
            elif player2_diff_game_won >= max_diff:
                self.winner = player2
                self.counter += 1
            elif player1_diff_game_won == 1 and self.tie_breaker_mode is True:
                self.winner = player1
                self.counter += 1
            elif player2_diff_game_won == 1 and self.tie_breaker_mode is True:
                self.winner = player2
                self.counter += 1
        else:
            return

    def tie_breaker(self, player1, player2):
        game = Game(player1, player2)
        self.all_games.append(game)
        self.current_game = game
        self.tie_breaker_mode = True





