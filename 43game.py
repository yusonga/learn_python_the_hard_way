from sys import exit
from random import randint
from textwrap import dedent


class Game(object):

    def enter(self):
        print("not yet.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, game_map):
        self.game_map = game_map

    def play(self):
        current_game = self.game_map.opening_game()
        last_game = self.game_map.next_game('finished')

        while current_game != last_game:
            next_game_name = current_game.enter()
            current_game = self.game_map.next_game(next_game_name)

        current_game.enter()

class Death(Game):

    quips = [
         "You died. you loser.",
         "you kinda suck at this.",
         "You're worse that my small puppy.",
         "Maybe you can use your brain."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Game):

    def enter(self):
        print(dedent("""
              You are at CentralCorridor
              """))
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                  a alien eats you.
                  """))
            return 'death'
        elif action == "dodage!":
            print(dedent("""
                  a alien eats you.
                  """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
                  lucy for you, you get a LaserWeapon.
                  """))
            return 'laserweapon'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'



class LaserWeapon(Game):

    def enter(self):
        print(dedent("""
              The code is 3 digits.
              """))
        code = '434'#f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZZZEDDDDDDD!!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                      The container open and there is a bridge.
                      """))
            return 'the_bridge'
        else:
            print(dedent("""
                      The lock buzzes one last time and you die.
                      """))
            return 'death'




class TheBridge(Game):

    def enter(self):
        print(dedent("""
              You burst onto the bridge.
              """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                  In a panic, you fall.
                  """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
                  You escape."""))

            return 'escape_pod'
        else:
            print("DOES DOT COMPUTE!!")
            return 'the_bridge'

class EscapePod(Game):

    def enter(self):
        print(dedent("""
              make up your mind, which one do you take?
              """))

        good_pod = 3 #randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                  You jump into pod {guess},
                  it's crushing your body into jam jelly.
                  """))

            return 'death'
        else:
            print(dedent("""
                  You jump into pod {guess}, lucy you, you won!!
                  """))

            return 'finished'

class Finished(Game):

    def enter(self):
        print("Damn, you won!")
        return 'finished'




class Map(object):
    game = {
          'central_corridor': CentralCorridor(),
          'laserweapon': LaserWeapon(),
          'the_bridge': TheBridge(),
          'escape_pod': EscapePod(),
          'death': Death(),
          'finished': Finished(),
    }

    def __init__(self, start_game):
        self.start_game = start_game

    def next_game(self, game_name):
        val = Map.game.get(game_name)
        return val

    def opening_game(self):
        return self.next_game(self.start_game)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
