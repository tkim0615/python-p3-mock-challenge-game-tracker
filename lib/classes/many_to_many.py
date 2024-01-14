class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, 'value'):
            self._title = value
    
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        scores_list = [result.score for result in self.results() if result.player == player]
        return sum(scores_list) / len(scores_list)
        






class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and (2 <= len(username) <= 16):
            self._username = username
        # else:
        #     raise Exception

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results() if result.player == self]))

    def played_game(self, game):
        game_title_list = [g.title for g in self.games_played()]
        return game.title in game_title_list

    def num_times_played(self, game):
        game_inst_list = [result.game for result in self.results() if result.game == game]
        return len(game_inst_list)

class Result:
    all =[]
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score 
    @score.setter
    def score(self, score):
        if isinstance(score, int) and (1<= score <= 5000) and not hasattr(self, 'score'):
            self._score = score
        # else:
        #     raise Exception

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game    