class Player:

    def __init__(self, the_id):
        self.Id = the_id
        self.__score_dict = {0: '0', 1: '15', 2: '30', 3: '40', 4: 'game'}
        self.points = 0
        self.game_won = 0

    def won_points(self):
        self.points += 1

    def get_score(self):
        if self.points < 4:
            return self.__score_dict[self.points]
        else:
            return self.__score_dict[4]

    def reset_score(self):
        self.points = 0

