import re

file_path = 'MOCK_DATA.txt'
surname_name_patronymic = 'names'
mail = 'mail'
file_extension = 'file extension'
color_code = 'color code'

file_reader = open(file_path, mode='r', encoding='Latin-1')
surname_name = open(surname_name_patronymic, mode='w', encoding='Latin-1')
m = open(mail, mode='w', encoding='Latin-1')
f = open(file_extension, mode='w', encoding='Latin-1')
c = open(color_code, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()

what_search = r"[A-Z][a-z_-]+[\s][de\sA-Z'\s]+[a-zA-Z]+"
results = re.findall(what_search, my_text_file)
print(results)

for item in results:
    print(item)
    surname_name.write(item + '\n')

what_search = r'[\w_-]+@[\w_-]+.[\w.]+'
results = re.findall(what_search, my_text_file)
print(results)

for item in results:
    print(item)
    m.write(item + '\n')

print(f'Total results of file : {str(len(results))}')

what_search = r'[A-Z\s]+[a-zA-Z]+[.][a-z\d]+'
results = re.findall(what_search, my_text_file)
print(results)

for item in results:
    print(item)
    f.write(item + '\n')

print(f'Total results of file : {str(len(results))}')

what_search = r'#[\d[a-z]\w+'
results = re.findall(what_search, my_text_file)
print(results)


for item in results:
    print(item)
    c.write(item + '\n')

print(f'Total results of file : {str(len(results))}')
