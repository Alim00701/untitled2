class TimeDesc:
    def __init__(self, second):
        self.second = second
        self.sec = second % 60
        self.min = second % 3600 // 60
        self.hour = second % 86400 // 3600
        self.day = second // 86400

    def __str__(self):
        return f'Дней: {self.day}, Часов: {self.hour}, Минут: {self.min}, Секунд: {self.sec}'


test = TimeDesc(89000)
print(test)


