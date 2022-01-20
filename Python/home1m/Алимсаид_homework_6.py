ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(lambda x: x % 2 == 0, ten))
evens = list(map(lambda x: x**2, b))
print(evens)

def ten_d(list=ten):
    while 1:
        index = input('Enter the index: ')
        if index == 'q':
            print("The program is completed!")
            break
        try:
            index = int(index)
            print(list[index])
        except IndexError:
            print(f"Вводить только числа! от 0 до {len(ten) -1, а для выхода нажмите 'q' ")
        except ValueError:
            print('НЕ вводить буквы!!!')
ten_d(ten)
