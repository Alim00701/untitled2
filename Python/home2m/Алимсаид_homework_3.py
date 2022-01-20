#Задача 1
class Teacher:
    def __init__(self, name, iq, laptop, numb_lesson):
        self.name = name
        self.iq = iq
        self.laptop = laptop
        self.numb = numb_lesson

    def Sertificate(self, args):
        return f'Наличие сертификата : {args}'

    def experience(self, ex):
        return f'Experience : {ex}'

    def __str__(self):
        return f'Name : {self.name}\n' \
               f'His IQ : {self.iq} iq\n' \
               f'Laptop : {self.laptop}\n'


student_1 = Teacher('Adilet', 140, 'Asus', 'end')
print(student_1)
print(student_1.Sertificate(True))
print(student_1.experience('High'))
print('-'*40)


class Student_back(Teacher):
    def __init__(self, name, iq, laptop, numb_lesson):
        super().__init__(name, iq, laptop, numb_lesson)

    def Sertificate(self, args):
        return f'Наличие сертификата : {args}'

    def experience(self, ex):
        return f'Experience : {ex}'

    def __str__(self):
        return super(Student_back, self).__str__() + \
               f'He studied {self.numb} lessons\n' \



stud_back = Student_back('Dima', 111, 'Acer', 4)
print(stud_back)
print(stud_back.Sertificate(False))
print(stud_back.experience('Average'))
print('-'*40)


class Student_front(Teacher):
    def __init__(self, name, iq, laptop, numb_lesson):
        super().__init__(name, iq, laptop, numb_lesson)

    def Sertificate(self, args):
        return f'Наличие сертификата : {args}'

    def experience(self, ex):
        return f'Experience : {ex}\n'

    def __str__(self):
        return super(Student_front, self).__str__() + f'He studied {self.numb} lessons\n' \



student_front = Student_front('Sofia', 123, 'Asus', 5)
print(student_front)
print(student_front.Sertificate(False))
print(student_front.experience('Average'))
print('-'*40)


class Programist(Student_back, Student_front):
    def __init__(self, name, iq, laptop, numb_lesson):
        super().__init__(name, iq, laptop, numb_lesson)


    def Sertificate(self, args):
        return f'Наличие сертификата : {args}'

    def experience(self, ex):
        return f'Experience : {ex}'

    def wage(self, wage):
        return f'Wage : {wage} $ in month'

    def __str__(self):
        return super(Programist, self).__str__()


programist = Programist('Alim', 130, 'HP', 'end')
print(programist)
print(programist.Sertificate(True))
print(programist.experience('High'))
print(programist.wage(200))
print('-'*40)

programist_2 = Programist('Latifa', 132, 'MackBook', 'end')
print(programist_2)
print(programist_2.Sertificate(True))
print(programist_2.experience('High'))
print(programist.wage(700))


#Задача 2
class Operator:
    def __init__(self, name, tarif, number, signal):
        self.name = name
        self.tarif = tarif
        self.number = number
        self.signal = signal

    def __str__(self):
        return f'Name : {self.name}\n' \
               f'Tarif : {self.tarif}\n' \
               f'Number : {self.number}\n' \
               f'Signal : {self.signal}\n'


test = Operator('MTC', 'normal', 495, 'normal')
print(test)


class Oshka(Operator):
    def __init__(self, name, tarif, number, signal):
        super().__init__(name, tarif, number, signal)

    def tariph(self, arg):
        return f'His tarif : {arg}'

    def __str__(self):
        return super(Oshka, self).__str__()


test_1 = Oshka('O!', 'good', 707, 'very good')
print(test_1)
print(test_1.tariph('Okuuchu'))


class MegaCom(Operator):
    def __init__(self, name, tarif, number, signal):
        super().__init__(name, tarif, number, signal)

    def tariph(self, arg):
        return f'His tarif : {arg}'

    def __str__(self):
        return super(MegaCom, self).__str__()


test_2 = MegaCom('MegaCom', 'normal', 550, 'good')
print(test_2)
print(test_2.tariph('Супер выгодный'))


class Beeline(Operator):
    def __init__(self, name, tarif, number, signal):
        super().__init__(name, tarif, number, signal)

    def tariph(self, arg):
        return f'His tarif : {arg}'

    def __str__(self):
        return super(Beeline, self).__str__()


test_3 = Beeline('Beeline', 'good', 777, 'normal')
print(test_3)
print(test_3.tariph('гиги за шаги'))

#Задача 3
class Cinema:
    def __init__(self, film):
        self.film = film
        self.cost = 0

        if self.film == 'Spider-Man':
            self.cost += 150
        if self.film == 'Hulk':
            self.cost += 130
        if self.film == 'Djock':
            self.cost += 120

    def __str__(self):
        return f'Your choose film: {self.film}\n' \
               f'Ticket price : {self.cost}$\n'


spider = Cinema('Spider-Man')
print(spider)


class Starbucks:

    def __len__(self, name):
        if len(name) >= 9:
            name = name[:5]
        elif len(name) < 5:
            name = name[-3:]
        return name


amer = Starbucks()
print(amer.__len__('Alimsaid'))

