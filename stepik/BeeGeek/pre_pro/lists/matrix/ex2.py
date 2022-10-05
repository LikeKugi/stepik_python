"""
Следом квадратной матрицы называется сумма элементов главной диагонали.
Напишите программу, которая выводит след заданной квадратной матрицы.
"""


def fill_matrix(matrix, n):
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)


def get_len(): return int(input())


def ask_matrix():
    n = get_len()
    matrix = list()
    fill_matrix(matrix, n)
    return matrix


def find_sum_main(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

def main():
    matrix = ask_matrix()
    print(find_sum_main(matrix))

if __name__ == '__main__':
    main()