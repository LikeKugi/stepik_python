"""
На плоскости евклидово расстояние между двумя точками
"""
import math

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
range = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(range)
