word = ('one', 'two', 'three', 'four', '12')
numbers = [1, 2, 3, 4, 5]

new = dict(zip(word, numbers))
print(new)
a = list(filter(lambda x: x >= 2 and x <= 4, numbers))
b = list(map(lambda x: x*x, numbers))
print(b)
print(a)
print(type(a))

dct = {}

#c = 0
#while c < len(word):
#    dct[word[c]] = numbers[c]
#    c += 1
#    print(dct)


#fltr = lambda x: x ** 2

#print(fltr(5))


#def bigger(list, func):
#    for i in list:
#        print(func(i))

#bigger(word, lambda words: words.title() + '!')


#lf = lambda words: words.title() + '!'
#bigger(word, lf)

#def up_letter(words):
#    return words.title() + '!'

#new = lambda x, y: print(x)

#bigger(word, up_letter)

#lambda значение: выражение

#new = lambda x=2, y=3: (x * 3) / y

#print(new())