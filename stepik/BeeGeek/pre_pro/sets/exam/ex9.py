"""
Формат входных данных
На вход программе в первой строке дается число m – количество уроков, проведенных с начала учебного года.
Далее идёт m блоков строк, описывающих листки с фамилиями.
На первой строке каждого блока указано количество фамилий n строчек с фамилиями тех, кто был на i-ом уроке.

Формат выходных данных
Программа должна вывести фамилии учеников, которые были на всех уроках, отсортированных в лексикографическом порядке.
Каждая фамилия должна быть записана на отдельной строке.

Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.
"""
from functools import reduce

lectures = int(input())
total = list()
for _ in range(lectures):
    total.append({input() for i in range(int(input()))})
pupils = reduce(lambda x, y: x & y, total)
print(*sorted(pupils), sep='\n')
