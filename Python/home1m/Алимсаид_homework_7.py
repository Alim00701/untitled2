import random
import datetime
start = datetime.datetime.now()
attempt = 0
random = random.randint(1, 100)
print(random)

while True:
    attempt += 1
    try:
        enter = input("Угадайте и введите число от 1 до 100: ")
        enter = int(enter)
        if enter == 0 or enter >= 100:
            print('Вводить только целые числа от 1 до 100!')
            continue
    except ValueError:
        print('НЕ вводить буквы и не чётные числа!!!')
        continue
    if enter > random:
        print('<')
    if enter < random:
        print('>')
    if enter > random:
        if enter - random <= 5:
            print(' Очень близко - 5!   ')
        elif enter - random <= 10:
            print(' Близко - 10! ')
        print(' Это число больше чем загаданное!!! ')
    if enter < random:
        if random - enter <= 5:
            print(' Очень близко + 5 !!!')
        elif random - enter <= 10:
            print(' Близко + 10 ')
        print(' Это число меньше чем загаданное!!! ')
    if enter == random:
        print(f'Вы угадали число: {random}')
        start = datetime.datetime.now() - start
        print(
            f'Время программы: {start.seconds} секунд(ы)\n'
            f'Потрачено: {attempt} попыток'
        )
        break
