from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
#basic class for scene have the common things that all scenes do.
#more like a demontration of what we would do

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            #be sure to print out rhe last scene
        current_scene.enter()

class Death(Scene):

    quips = [
          "You died. You kinda suck at this.",
          "Your Mom would be proud... if she were smarter.",
          "Such a luser.",
          "I have a small puppy that's better at this.",
          "You're worse that your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              The Gothons of Planet Percal #25 have invaded your shop and destroyed your entire crew. You are the last surviving member and your last .
              He's bloking the door to the armory and about to pull a weapon to blast you.
              """))
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                 Quicl on the draw. Then he eats you.
            """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
                  Like a world class boxer you dodge,
                  on your head and eats you.
            """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
                  Lucky for you thet made you learn Gothon
                  the jump through the Weapon Armory door.
            """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
             You do
             The code is 3 digits.
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZZEDDDDD!")
            guesses += 1
            guess = input("[keypad]> ")

            if guess == code:
                print(dedent("""
                      The container clicks open and seal breaks,
                      in the right spot.
                """))
                return 'the_bridge'
            else:
                print(dedent("""
                     The lock buzzes one last time and then you hear a
                     and you die.
                """))
                return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst onto the Bridge
        set it off.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            In a panic
            when it goes off.
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
            You point your blaster
            get off this tin can.
            """))


            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        You rush through
        which one do you take?
        """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
            You jump into pod {guess}
            crushing your body into jam jelly.
            """))
            return 'death'
        else:
            print(dedent("""
            You jump into pod{guess}
            You won!
            """))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
           'central_corridor': CentralCorridor(),
           'laser_weapon_armory': LaserWeaponArmory(),
           'the_bridge': TheBridge(),
           'escape_pod': EscapePod(),
           'death': Death(),
           'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
