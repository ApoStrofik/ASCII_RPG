
class Player:

    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):

        self.name = name
        self.level = 1
        self.experience = 0
        self.life = life
        self.max_life = max_life
        self.defense = defense
        self.dexterity = dexterity
        self.magic = magic
        self.gold = gold

        self.items_bag = []


class Warrior(Player):
    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):
        super().__init__(name, life, max_life, defense, dexterity, magic, gold)

        self.classNAME = "GUERRIER"
        self.force = 10

class Mage(Player):
    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):
        super().__init__(name, life, max_life, defense, dexterity, magic, gold)

        self.classNAME = "MAGE"
        self.intel = 10

class Rogue(Player):
    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):
        super().__init__(name, life, max_life, defense, dexterity, magic, gold)

        self.classNAME = "VOLEUR"
        self.esquive = 10