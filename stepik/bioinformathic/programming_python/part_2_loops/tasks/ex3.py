"""
Напишите программу, которая считывает список чисел lst из первой строки
и число xx из второй строки, которая выводит все позиции,
на которых встречается число xx в переданном списке lst.
"""

lst = [int(i) for i in input().split()]
number = int(input())
indexes = []
for i in range(len(lst)):
    if lst[i] == number:
        indexes.append(i)
if len(indexes)>0:
    print(*indexes)
else:
    print('Отсутствует')