# Программа должна вывести координаты вершины параболы.
a, b, c = int(input()), int(input()), int(input())
roots = (-b) / (2 * a), (4 * a * c - b ** 2) / (4 * a)
print(roots)
