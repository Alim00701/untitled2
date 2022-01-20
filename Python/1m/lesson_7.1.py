import time

def stopwatch():
    start = 0
    while 1:
        print(start)
        time.sleep(1)
        start += 1
    
stopwatch()


#def timer(start):
#    while start >= 0:
#        print(start)
#        time.sleep(1)
#        start -= 1

#timer(5)







#import random
#import datetime
#start = datetime.datetime.now()
#students = [1, 2, 3, 4, 5, 7, 8, 10, 12, 15, 16, 17, 18]
#while len(students) != 0:
#    print(students.pop(students.index(random.choice(students))))
#    input('Следующий! ')
#    print(students)
#end = datetime.datetime.now() - start
#print(
#    'Опрос завершился\n'
#    f'Время программы: {end}'
#)
