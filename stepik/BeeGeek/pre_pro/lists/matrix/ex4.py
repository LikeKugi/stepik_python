"""
* o o o o
* * o o o
* * * o o
* * * * o
* * * * *

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
"""


def get_dimensions(): return int(input())


def fill_matrix(n: int):
    array = [[int(el) for el in input().split()] for _ in range(n)]
    return array


def create_matrix():
    n = get_dimensions()
    matrix = fill_matrix(n)
    return matrix


def find_max_of_lower_matrix(matrix: list):
    k = len(matrix)
    max_el = matrix[0][0]
    for i in range(k):
        for j in range(i + 1):
            if matrix[i][j] > max_el:
                max_el = matrix[i][j]
    return max_el


def main():
    matrix = create_matrix()
    print(find_max_of_lower_matrix(matrix))


if __name__ == '__main__':
    main()
