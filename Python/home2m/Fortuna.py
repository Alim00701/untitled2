from random import choice


class Fortuna:
    def game(self, z):
        self.result = 0
        weirdos = ["Гном", "Эльф", "Левиафан"]
        w = choice(weirdos)
        question = choice(weirdos)
        answer = input(f"За дверью стоит {question}? ")
        if z > 0:
            if answer == "Верю" and w == question or answer == "Не верю" and w != question:
                print(f"За дверью стоял {w}")
                self.result = z * 2
                print(f"Вы победили!: {self.result}$")
            if answer == "верю" and w != question or answer == "не верю" and w == question:
                print(f"За дверью стоял {w}")
                self.result = 0
                print(f"Вы победили!: {self.result}$")
        elif z < 0:
            if answer == "верю" and w == question or answer == "не верю" and w != question:
                print(f"За дверью стоял {w}")
                self.result = 0
                print(f"Вы проиграли!: {self.result}$")
            if answer == "верю" and w != question or answer == "не верю" and w == question:
                print(f"За дверью стоял {w}")
                self.result = z * 2
                print(f"Вы проиграли!: {self.result}$")
