class Animal:
    Class = ['Mammalian', 'Insect']
    def __init__(self, name, color, age, weight):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be str')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be str')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age should be int')
        if isinstance(weight, float):
            self.weight = weight
        else:
            raise ValueError('Weight should be float')

    def __str__(self):
        return f'Gender: {self.name}\n' \
               f'Color: {self.color}\n' \
               f'Age: {self.age}\n' \
               f'Weight: {self.weight}\n'


mammalian = Animal('tiger', 'orange', 5, 56.5)
print(mammalian)

class Insect(Animal):
    def __init__(self, gender, color, age, weight, speed):
        super().__init__(gender, color, age, weight)
        if isinstance(speed, str):
            self.speed = speed
        else:
            raise ValueError('Speed should be string')

    def __str__(self):
        return super(Insect, self).__str__() + f'Speed: {self.speed} \n'

insect = Insect('snail', 'yellow', 1, 0.1, 'very fast')
print(insect)
