"""
Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

На плоскости манхэттенское расстояние между двумя точками (p1;p2) и (q1;q2)
определяется так: |p1-q1|+|p2-q2|
"""

p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
s = abs(p1 - q1) + abs(p2 - q2)
print(s)