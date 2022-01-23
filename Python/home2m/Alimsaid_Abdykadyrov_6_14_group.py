
num = int(input('Введите желаемое целое число: '))


class S:
    def __init__(self, numbers: list, desired_sum: int):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def index(self):
        for i in range(len(self.numbers)):
            for n in range(i + 1, len(self.numbers)):
                if (self.numbers[i] + self.numbers[n]) == self.desired_sum:
                    return [i, n]


num_1 = S(numbers=[2, 7, 11, 15], desired_sum=num)
print(num)
print(num_1.index())