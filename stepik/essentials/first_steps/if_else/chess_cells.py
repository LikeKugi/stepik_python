"""
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.
"""

def find_cell(n):
    return (ord(n[0])-ord('a')+1, int(n[1]))

if sum(c1:= find_cell(input())) % 2 == sum(c2 := find_cell(input())) % 2:
    print('YES')
else:
    print('NO')


# /---------------------------------------------------------------------/

print(('YES', 'NO')[sum(map(ord, input() + input())) % 2])