"""
На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y) и аппликат (z)
точек трехмерного пространства.
Напишите программу для проверки расположения всех точек с введенными координатами внутри либо на поверхности шара
с центром в начале координат и радиусом R = 2.

Формат входных данных
На вход программе подаются три строки текста с вещественными числами,
разделенными символом пробела – абсциссы, ординаты и аппликаты точек в трехмерной системе координат.

Формат выходных данных
Программа должна вывести True если все точки с введенными координатами находятся внутри или на границе шара
и False, если вне.
"""


def checking_into_ball(x_coord, y_coord, z_coord, *, r=2):
    return all([(x ** 2 + y ** 2 + z ** 2) <= r ** 2 for x, y, z in zip(x_coord, y_coord, z_coord)])


abscissas = [float(el) for el in input().split()]
ordinates = [float(el) for el in input().split()]
applicates = [float(el) for el in input().split()]

print(checking_into_ball(abscissas, ordinates, applicates))
