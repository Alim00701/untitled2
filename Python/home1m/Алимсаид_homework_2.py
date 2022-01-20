letters = 'аоуиыэеёюяaeiouy'
while True:
    glas, sogl = 0, 0
    words = input("Введите слово: ")

    if words == "q":
        print("Программа завершена!")
        break

    for i in words.lower():
        if i in letters:
            glas += 1
        else:
            sogl += 1

    glas_proc = round(glas / len(words) * 100, 2)
    sogl_proc = round(sogl / len(words) * 100, 2)

    print(
        f"Слово: {words}\n"
        f"Количество букв: {len(words)}\n"
        f"Гласные: {glas}\n"
        f"Согласные: {sogl}\n"
        f"Гласные/Согласные: {glas_proc}%/{sogl_proc}%"
    )








