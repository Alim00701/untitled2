colors1 = {
    'kg': {'red', 'yellow'},
    'ru': {'blue', 'red', 'white'},
    'ua': {'red', 'blue', 'white'},
    'kz': {'blue', 'yellow'},
    'tr': {'red', 'white'}
}
while True:
    color2 = input(f'Enter the color: ')
    a = []
    if color2 == "q":
        print("The program is completed!")
        break
    color = color2.split()
    for key, value in colors1.items():
        check_color = True
        for colors in color:
            if colors not in value:
                check_color = False
                break
        if check_color:
            a.append(key)
    if len(a) > 0:
        for a in a:
            print(a)
    else:
        print(f'this color is not in the list, please try again!!!')