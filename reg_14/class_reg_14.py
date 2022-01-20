import re

my_text = 'Vasya, 1998, vasya@gmail.com, 4000$, male* ' \
          'Adilet, 1997 adilet@gmail.com, 5000$ male* ' \
          'Aidana, 2000, aidana@gmail.com, 8976$ female% ' \
          'Aman, 1999, aman@mail.ru, 789$ female% ' \
          'Regina, 1999, regina@yahoo.ru, 69$ female% ' \
          'Lol, 6789, lol@gmail.com 9087$ male* '

"""
\d -- Он ищит подряд стоящие числа [0-9]
\D -- Он ищит любые , но не числа
\w -- Ищет любой алфавитный символ [A-Z a-z]
\W -- Любой не алфавитный символ
\s -- Ищет проблемы
\S -- Специальные символы
"""

file_path = 'demo_mock_data.txt'
result_file_path = 'results.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_search = r'[a-z]+@[\w+_-]\S\w+\S\w+\S[a-z]+'
results = re.findall(what_search, my_text_file)
print(results)

for item in results:
    print(item)
    result_file.write(item + '\n')

print(f'Total results of file : {str(len(results))}')
