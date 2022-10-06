"""
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
верхнюю,
нижнюю,
левую
правую.

Напишите программу, которая вычисляет сумму элементов:
верхней четверти;
правой четверти;
нижней четверти;
левой четверти.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.
"""
import numpy as np


def get_dimensions(): return int(input())


def fill_matrix(n: int):
    array = [[int(el) for el in input().split()] for _ in range(n)]
    return array


def create_matrix():
    n = get_dimensions()
    matrix = fill_matrix(n)
    return matrix


def find_sum_of_quorter_matrix(matrix: list):
    k = len(matrix)
    sum_qurter = np.zeros(4, dtype=np.int_)
    for i in range(k):
        for j in range(k):
            if (i < k - 1 - j) and (i < j):
                sum_qurter[0] += matrix[i][j]
            elif k - 1 - j < i < j:
                sum_qurter[1] += matrix[i][j]
            elif (i > j) and (i > k - 1 - j):
                sum_qurter[2] += matrix[i][j]
            elif j < i < k - 1 - j:
                sum_qurter[3] += matrix[i][j]
    return sum_qurter


def main():
    matrix = create_matrix()
    sums = find_sum_of_quorter_matrix(matrix)
    print(f'Верхняя четверть: {sums[0]}')
    print(f'Правая четверть: {sums[1]}')
    print(f'Нижняя четверть: {sums[2]}')
    print(f'Левая четверть: {sums[3]}')


if __name__ == '__main__':
    main()
