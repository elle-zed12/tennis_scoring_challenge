from player import Player


class Game:

    def __init__(self, player1, player2):
        self.players = []
        self.players.append(player1)
        self.players.append(player2)
        self.counter = 0
        self.winner = None
        self.status = ''

    def check_status(self):
        player1 = self.players[0]
        player2 = self.players[1]
        lower_limit = 3
        min_diff = 1
        if player1.points >= lower_limit and player2.points >= lower_limit:
            if player1.points == player2.points:
                self.status = 'deuce'
            elif player1.points - player2.points == min_diff:
                self.status = f'Advantage {player1.Id}'
            elif player2.points - player1.points == min_diff:
                self.status = f'Advantage {player2.Id}'
            else:
                self.__check_winner(player1, player2)
        elif player1.points >= lower_limit or player2.points >= lower_limit:
            self.__check_winner(player1, player2)
        else:
            self.status = f'{player1.get_score()}-{player2.get_score()}'

    def __check_winner(self, player1, player2):
        player1_lead_score = player1.points - player2.points
        player2_lead_score = player2.points - player1.points
        if player1.points >= 4 and player1_lead_score >= 2:
            self.__game_over(player1)
        elif player2.points >= 4 and player2_lead_score >= 2:
            self.__game_over(player2)
        else:
            self.status = f'{player1.get_score()}-{player2.get_score()}'

    def __game_over(self, player):
        player.game_won += 1
        self.counter += 1
        self.winner = player
        self.status = ''

    def tie_breaker_scoring(self):
        player1 = self.players[0]
        player2 = self.players[1]
        goal = 7
        min_diff = 2
        if player1.points >= goal or player2.points >= goal:
            if player1.points - player2.points >= min_diff:
                self.__game_over(player1)
            elif player2.points - player1.points >= min_diff:
                self.__game_over(player2)
        self.status = f'{player1.points}-{player2.points}'
        return

    def reset_players_score(self):
        for player in self.players:
            player.reset_score()

