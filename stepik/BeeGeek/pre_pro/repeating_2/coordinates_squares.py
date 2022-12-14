"""
Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел —
координат точки (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.
"""

coordinates = [0] * 4
for _ in range(int(input())):
    x, y = (int(i) for i in input().split())
    if x == 0 or y == 0:
        continue
    else:
        if y > 0:
            if x > 0:
                coordinates[0] += 1
            else:
                coordinates[1] += 1
        else:
            if x > 0:
                coordinates[3] += 1
            else:
                coordinates[2] += 1

print(f'Первая четверть: {coordinates[0]}')
print(f'Вторая четверть: {coordinates[1]}')
print(f'Третья четверть: {coordinates[2]}')
print(f'Четвертая четверть: {coordinates[3]}')