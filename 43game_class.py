class Game(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, game_map):
        pass
    def play(self):
        pass

class Death(Game):

    def enter(self):
        pass

class CentralCorridor(game):

    def enter(self):
        pass


class LaserWeapon(game):

    def enter(self):
        pass



class TheBridge(game):

    def enter(self):
        pass


class EscapePod(game):

    def enter(self):
        pass



class Map(object):

    def __init__(self, last_game):
        pass

    def next_game(self, game_name):
        pass

    def opening_game(self):
        pass

a_map = Map('CentralCorridor')
a_game = Engine(a_map)
a_map.play()
