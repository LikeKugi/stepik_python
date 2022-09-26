"""
Вводятся 3 строки в случайном порядке.
Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
"""
lengths = []
for _ in range(3):
    lengths.append(len(input()))
lengths.sort()
if lengths[0] - lengths[1] == lengths[1] - lengths[2]:
    print('YES')
else:
    print('NO')