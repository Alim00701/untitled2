while True:
    string = int(input("Enter a letter: "))
    if string < 0 or str(string) != str(string)[::-1]:
        print("Универсальное число")
    else:
        print("Не универсальные")
        break
