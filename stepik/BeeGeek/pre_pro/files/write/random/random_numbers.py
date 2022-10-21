"""
Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел
в диапазоне от 111 до 777 (включительно), каждое с новой строки.
"""
from random import randint as ri

with open('random.txt', 'w') as ouf:
    print(*[ri(111,777) for _ in range(25)],file=ouf,sep='\n')