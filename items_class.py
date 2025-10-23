from colorama import *

class Potion:
    def __init__(self, regen, color, effect):
        self.name = "Potion"
        self.image = "*" + color + "(O)" + Style.RESET_ALL
        self.regen = regen
        self.effect = effect
