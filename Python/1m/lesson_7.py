from pprint import pprint
import random
from random import randint, choice
from datetime import datetime
import time


def greetings(name):
    hours = datetime.now().hour
    print(hours)
    if hours >= 4 and hours <= 11:
        print(f'Доброе утро!! {name}')
    if hours >= 12 and hours <= 17:
        print(f'Добрый день!!{name}')
    if hours >= 18 and hours <= 23:
        print(f'Добрый вечер!!{name}')

greetings('Azat')


#print(datetime.now())
#time.sleep(5)
#print(datetime.now().hour)

#start = datetime.now()


#guys = ['jack', 'alice', 'murat', 'anna', 'gregoriy']
#pprint(a)
#pprint.pprint(random.sample(guys, 2))
#print(randint(1, 5))
#print(choice(guys))
#print()

#from lesson_5 import greetings as g
#import lesson_5

#greetings('Azamat')
#lesson_5.greetings('Samat')
#g('Kanat')
