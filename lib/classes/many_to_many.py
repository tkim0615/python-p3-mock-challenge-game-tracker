class Game:
    def __init__(self, title):
        self.title = title

    @property #get properties
    def title(self):
        return self._title
    @title.setter  #set properties
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
                                            
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        #get list of score for the player. sum it and divide by length of list
        list_ofscore = [result.score for result in self.results() if result.player == player]
        return sum(list_ofscore) / len(list_ofscore)
        

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and (2<= len(username) <=16):
            self._username = username

    def results(self): #list of results
        return [result for result in Result.all if result.player == self]
    
    def games_played(self):  #list of game instances
        return list(set([result.game for result in self.results()]))

    def played_game(self, game): #list of game instances filtered by game parameter
        return game in self.games_played()

    def num_times_played(self, game): #tyler played soccer 2 times
        given_games_played = [result.game for result in self.results() if result.game == game]
        print(given_games_played)
        return len(given_games_played)
    # def num_times_played(self, game):
    #     games_played = [result.game for result in self.results()]
    #     print(games_played)
    #     return games_played.count(game)

class Result:
    all = []
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

    