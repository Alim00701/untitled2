#Задача №1
class Grandpa:
    def __init__(self, name, surname, height, age, car, passport, pension, wrinkles):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name is string')
        if isinstance(surname, str):
            self.surname = surname
        else:
            raise ValueError('Surname is string')
        if isinstance(height, float):
            self.height = height
        else:
            raise ValueError('Height is float')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(car, bool):
            self.car = car
        else:
            raise ValueError('Car is boolean')
        if isinstance(passport, str):
            self.passport = passport
        else:
            raise ValueError('Passport is boolean')
        if isinstance(pension, bool):
            self.pension = pension
        else:
            raise ValueError('Pension is boolean')
        if isinstance(wrinkles, bool):
            self.wrinkles = wrinkles
        else:
            raise ValueError('Wrinkles is boolean')

    def has_a_pension(self, source):
        return f'He has a {source}, because he is {self.age} years old'

    def has_a_wrinkles(self, source):
        return f'He has a {source}, because he is {self.age} years old\n'

    def __str__(self):
        return f'Name : {self.name}\n' \
               f'Surname : {self.surname}\n' \
               f'Height : {self.height}\n' \
               f'Age : {self.age}\n'


grandpa = Grandpa('Djusuke', 'Abdykadyrov', 1.70, 89, True, 'passport', True, True)

print(grandpa)
print(grandpa.has_a_pension('pension'))
print(grandpa.has_a_wrinkles('wrinkles'))


class Father(Grandpa):
    def __init__(self, name, surname, height, age, car, passport, pension, wrinkles):
        super().__init__(name, surname, height, age, car, passport, pension, wrinkles)

    def can_drive_car(self, source):
        return f'He can drive а {source}, because he has a {self.passport}'

    def can_drink_alcohol(self, source):
        return f'He can drink a {source}, because he has a {self.passport}\n'

    def __str__(self):
        return super(Father, self).__str__() + f'Car : {self.car}\n' \
                                               f'Passport : {self.passport}\n'


father = Father('Kalybek', 'Abdykadyrov', 1.69, 43, True, 'passport', False, False)
print(father)
print(father.can_drive_car('car'))
print(father.can_drink_alcohol('alcohol'))


class Son(Father):
    def __init__(self, name, surname, height, age, car, passport, pension, wrinkles):
        super().__init__(name, surname, height, age, car, passport, pension, wrinkles)

    def can_go_to_school(self, source):
        return f'He can go to school {source}, because he is {self.age} years old'

    def can_play_basketball(self, source):
        return f'He can play {source}, because his height {self.height}m\n'


son = Son('Alim', 'Abdykadyrov', 1.79, 12, False, 'note', False, False)
print(son)
print(son.can_go_to_school('himself'))
print(son.can_play_basketball('basketball'))

#Задача №2
print('Задача №2')


class Washing_machine:
    def __init__(self, brand, can):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand is string')
        if isinstance(can, str):
            self.__can = can
        else:
            raise ValueError('Can is string')

    def __str__(self):
        return f'Brand : {self.brand}\n' \
               f'Can : {self.__can}\n'

    def wash(self):
        return f"Washing machine ('{self.brand}') can {self.__can}\n"


washing_machine = Washing_machine('LG', 'wash')
print(washing_machine)
print(washing_machine.wash())

#Задача №3
print(
    'Задача 3'
)


class CaptainAmerica:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.skill}\n'

    def attack(self):
        return f'{self.name} attack with {self.skill}'


class Tor:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.skill}\n'

    def attack(self):
        return f'{self.name} attack with {self.skill}'


class SpiderMan:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.skill}\n'

    def attack(self):
        return f'{self.name} attack with {self.skill}\n'


cap = CaptainAmerica('Captain America', 'shild')
tor = Tor('Tor', 'hammer')
spider = SpiderMan('Peter Parker', 'web')
print(cap.attack())
print(tor.attack())
print(spider.attack())


#Задача 4
print(
    'Задача 4'
)


class Level1:
    def __init__(self, name, belt_color, age):
        self.name = name
        self.belt = belt_color
        self.age = age

    def __str__(self):
        return f'Name : {self.name}\n' \
               f'Belt color : {self.belt}\n' \
               f'Age : {self.age}\n'


class Level2(Level1):
    def __init__(self, name, belt_color, age):
        super().__init__(name, belt_color, age)

    def __str__(self):
        return super(Level2, self).__str__()


class Level3(Level2):
    def __init__(self, name, belt_color, age):
        super().__init__(name, belt_color, age)

    def __str__(self):
        return super(Level3, self).__str__()


level1 = Level1('Tilek', 'white', 13)
print(level1)
level2 = Level2('Alim', 'brown', 16)
print(level2)
level3 = Level3('Omar', 'black', 19)
print(level3)
