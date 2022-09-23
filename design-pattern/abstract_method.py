"""
    Abstract Method ; Factory Method 일반화( 객체 생성을 group화 )
"""
''' age에 따라 다른 게임 환경을 설정 '''
class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}"
        print(msg)

class Bug:
    def __str__(self):
        return "A bug"

    def action(self):
        return "Eats it"

class FrogWorld:

    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return "Frog World"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()

class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Wizard battles with {obstacle} and {act}"
        print(msg)

class Ork:

    def __str__(self):
        return "An evil ork"

    def action(self):
        return "Kills it"

class WizardWorld:

    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return "Wizard World"

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

class GameEnvironment:

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    try:
        age = input(f"Welcome {name}. How old are you?")
        age = int(age)
    except ValueError as err:
        print(f"{age} is invalid age")
        return (False, age)
    return (True, age)

def main():
    name = input("Hello, what is your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == "__main__":

    main()