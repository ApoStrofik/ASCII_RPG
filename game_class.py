
class Player:

    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):

        self.name = name
        self.level = 1
        self.experience = 0
        self.life = life
        self.max_life = max_life
        self.attack = 5
        self.defense = defense
        self.dexterity = dexterity
        self.magic = magic
        self.gold = gold

        self.items_bag = []


class Warrior(Player):
    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):
        super().__init__(name, life, max_life, defense, dexterity, magic, gold)

        self.classNAME = "GUERRIER"
        self.force = 20

    def attack_calc(self):
        return int(self.attack + (self.force / 2))

    def lvl_up(self):
        self.level += 1
        self.experience = 0
        self.life += 15
        self.max_life += 15
        self.force += 5


class Mage(Player):
    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):
        super().__init__(name, life, max_life, defense, dexterity, magic, gold)

        self.classNAME = "MAGE"
        self.intel = 10

    def attack_calc(self):
        return int(self.attack + (self.intel / 2))

    def lvl_up(self):
        self.level += 1
        self.experience = 0
        self.life += 15
        self.max_life += 15
        self.intel += 5


class Rogue(Player):
    def __init__(self, name, life, max_life, defense, dexterity, magic, gold):
        super().__init__(name, life, max_life, defense, dexterity, magic, gold)

        self.classNAME = "VOLEUR"
        self.esquive = 10

    def attack_calc(self):
        return int(self.attack + (self.esquive / 2))

    def lvl_up(self):
        self.level += 1
        self.experience = 0
        self.life += 15
        self.max_life += 15
        self.esquive += 5


class Niveau:
    def __init__(self):
        self.lvl = 0