# Component Interface
class Character:
    def get_abilities(self):
        raise NotImplementedError


# Concrete Component
class Mario(Character):
    def get_abilities(self):
        return "Mario"


# Abstract Decorator
class CharacterDecorator(Character):
    def __init__(self, character: Character):
        self.character = character


# Concrete Decorators
class HeightUp(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " with HeightUp"


class GunPowerUp(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " with Gun"


class StarPowerUp(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " with Star Power (Limited Time)"

    def __del__(self):
        print("Destroying StarPowerUp Decorator")


# Client Code
if __name__ == "__main__":
    mario = Mario()
    print("Basic Character:", mario.get_abilities())

    mario = HeightUp(mario)
    print("After HeightUp:", mario.get_abilities())

    mario = GunPowerUp(mario)
    print("After GunPowerUp:", mario.get_abilities())

    mario = StarPowerUp(mario)
    print("After StarPowerUp:", mario.get_abilities())
"""Mario is the base object

Power-ups are decorators

Each decorator wraps Mario and adds behavior

Features are added dynamically at runtime

No modification to original Mario class ✔"""