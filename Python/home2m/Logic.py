from random import choice


class Casino:
    def __init__(self, wallet, plus_or_minus):
        if isinstance(wallet, int):
            self.wallet = wallet
            self.plus_or_minus = plus_or_minus

    def game(self, number, bid):
        random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30]
        random = choice(random_list)
        print(f"Вы поставили на {number}\n"
              f"Сделали ставку {bid}")
        if random == number:
            self.plus_or_minus += bid
            print(f"Выпало цифра: {random}")
            print(f"Поздравляю вы выиграли! {bid}$!")
            return True
        elif random != number:
            self.wallet -= bid
            self.plus_or_minus -= bid
            print(f"Выпало цифра: {random}")
            print(f"К сожалению вы проиграли: {bid}$")
            return True
        else:
            print("Произошла ошибка !!!")
            return True

