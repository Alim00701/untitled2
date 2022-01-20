from Fortuna import Fortuna
from Logic import Casino

cash = 1000
plus_or_minus = 0
while True:
    slot = int(input("Выберите слот от 1 до 30: "))
    bid = int(input("Ваша ставка: "))
    play = Casino(cash, plus_or_minus)
    play.game(slot, bid)
    plus_or_minus = play.plus_or_minus
    print('-' * 40)
    ret = input("Хотите продолжить?: да или нет? ")
    if ret == "да":
        continue
    else:
        if play.plus_or_minus > 0:
            print(f"Вы выиграли: {play.plus_or_minus}$")
        else:
            print(f"Вы проиграли: {play.plus_or_minus}$")
        f = input("Хотите сыграться в фортуну 'Верю Не верю'? ")
        if f == "да":
            print('-' * 40)
            print("Ответить только : Верю или Не верю")
            play_2 = Fortuna()
            play_2.game(play.plus_or_minus)
            cash += play_2.result
            print('-' * 40)
            print(f"Теперь у вас есть {cash}$")
            break
        else:
            cash += play.plus_or_minus
            print('-' * 40)
            print(f"Теперь у вас есть {cash}$")
            break
