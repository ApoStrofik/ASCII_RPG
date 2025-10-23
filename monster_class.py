import random

from items_class import Potion


class Monster:

    def __init__(self):
        self.life = 10


class Skeleton(Monster):
    def __init__(self):
        super().__init__()

        self.name = "SQUELETTE"
        self.attack = random.randint(1,6)
        self.defense = 10
        self.agility = 0

class Wolf(Monster):
    def __init__(self):
        super().__init__()

        self.name = "LOUP"
        self.attack = random.randint(3,8)
        self.defense = 10
        self.agility = 5