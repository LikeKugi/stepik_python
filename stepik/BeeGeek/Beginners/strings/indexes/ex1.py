"""
На вход программе подается одна строка состоящая из цифр.
Напишите программу, которая считает сумму цифр данной строки.
"""
from functools import reduce
digits = input()
sum = reduce(lambda x,y: int(x)+int(y),digits)
print(sum)