"""
Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические
значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.
"""
from functools import reduce
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
avars = list()
for el in numbers:
    avars.append(reduce(lambda a,b:a+b,el)/len(el))
print(avars)