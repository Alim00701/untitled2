


#dct = {
#    'name': 'asam',
#    'age': 20
#}
#print(dct.get('hobby', 'нет такого'))
#print(dct['hobby'])

#try:
#    print(2 / 0)
#except ZeroDivisionError:
#    print('НЕ делим на ноль')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
words = ['dict', 'list', 'tuple']
def obj_index(list):
    while 1:
        try:
            index = int(input('Enter index: '))
            print([index])
        except IndexError:
            print(f'Вводить только числа! от 0 до {len(list) - 1}')
        except ValueError:
            print('НЕ вводить буквы!!!')
obj_index(numbers)
