class Character:
    def __init__(self, name, height, skill):
        self.name = name
        self.height = height
        self.skill = skill

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Height: {self.height}\n' \
               f'Skill: {self.skill}\n' \

class Magician(Character):

    def attack(self):
        return f'Attack with spell {self.skill}'

class Paladin(Character):

    def attack(self):
        return f'Attack with {self.skill}'

class Archer(Character):

    def attack(self):
        return f'Attacking with bow and {self.skill}'

mag = Magician('Gendelf', 200, 'FireBall')
paladin_1 = Paladin('Georg', 210, 'Holy word')
arc = Archer('Zelle', 180, 'Poisoned arrow')
print(mag.attack())
print(paladin_1.attack())
print(arc.attack())
