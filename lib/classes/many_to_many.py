class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title


    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        all_score_for_player = [result.score for result in self.results() if result.player == player]
        return sum(all_score_for_player) / len(all_score_for_player)

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2<= len(username) <= 16:
            self._username = username


    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results() if result.player == self]))

    def played_game(self, game):
        return game in self.games_played()
            
    def num_times_played(self, game):
        #get list of all results for the particular game. then get length of list
        results_for_game = [result for result in self.results() if result.game == game]
        return len(results_for_game)
        

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.add_to_all(self)
    
    @classmethod
    def add_to_all(cls, instance):
        if isinstance(instance, Result):
            cls.all.append(instance)
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1<= score <= 5000 and not hasattr(self, 'score'):
            self._score = score
    