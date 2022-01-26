class In:
    while True:
        try:
            string = int(input("Введите число: "))
            if string > 999 or string < 100:
                raise ValueError
            break
        except ValueError:
            print('Вводить только трехзначные целые числа!!!')

    if string < 0 or str(string) != str(string)[::-1]:
        print("Не палиндромное число")
    else:
        print("Палиндромное число")
