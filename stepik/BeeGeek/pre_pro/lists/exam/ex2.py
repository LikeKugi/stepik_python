"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
o o o *
o o * *
o * * *
* * * *
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
    max_el = matrix[-1][0]
    for i in range(k):
        for j in range(k):
            if i >= k - j - 1:
                if matrix[i][j] > max_el:
                    max_el = matrix[i][j]
    return max_el


def main():
    matrix = create_matrix()
    print(find_max_of_lower_matrix(matrix))


if __name__ == '__main__':
    main()