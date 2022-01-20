#dict = {key: value}
dct = (['apple', 'яблоко'], ['lemon', 'лимон'], ['orange', 'апельсин'])

dict_en_ru = dict(dct)

new = dict_en_ru.copy()
new['orange'] = "fefhef"

print(dict_en_ru)
print(new)


#student1 = dict(name='Alim', last_name='Said')

#student1 = {
 #   'name': 'Mary',
  #  'age': 15,
   # 'height': 1.65,
   # 1: True,
    #'hobby': ['books', 'chess'],
    #'name2': 'Marina'
#}
#for k, v in student1.items():
 #   print(f'{k}: {v}')


#print(student1.keys())
#print(student1.values())
#print(student1.items())
#student.update(student1)

#student['hobby'].append('cooking')
#del student[1],
#student.pop('name2')

#student['job'] = 'doctor'
#student['age'] = 21

#print(student)

#print(student['name'])
#print(student['age'])