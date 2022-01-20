data_tuple = ('h', 6.13, 'c', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'G')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    elif type(i) == int or type(i) == float:
        numbers.append(i)

letters.append(True)
del numbers[-3]
numbers.sort()
letters.reverse()
numbers.insert(1, 2)
letters = tuple(letters)
numbers = tuple(numbers)
print(f'letters: {letters}')
print(f'numbers: {numbers}')