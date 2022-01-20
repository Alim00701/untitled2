abiaturients1 = [
    {'name': 'Irina', 'OPT': 160},
    {'name': 'Wayne', 'ОРТ': 220},
    {'name': 'Fred', 'ОРТ': 90}
]

abiaturients2 = [
    {'name': 'Anton', 'ОРТ': 150},
    {'name': 'Eliza', 'ОРТ': 220},
    {'name': 'Timur', 'ОРТ': 90}
]

def list_students(list):
    for i in list:
        for k, v in i.items():
            print(f'{k}: {v}')

#list_students(abiaturients1)
#list_students(abiaturients2)

def add_student(list, name, OPT):
    list.append(dict(name=name, OPT=OPT))
    list_students(list)

#add_students(abiaturient2, 'Paul', 160)

def delete_students(list, name):
    for i in list:
        if name.title == i['name']:
            del_s = i.pop(list.index(i))
            print(f"{del_s['name']} Удалён из студентов!")
    list_students(list)

delete_students(abiaturients1, 'Fred')

while True:
    user = input()
    if user == 1:
        add_student()

