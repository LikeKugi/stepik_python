"""
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки.
"""


def get_dimensions(): return int(input())


def fill_matrix(n: int):
    array = [[int(el) for el in input().split()] for _ in range(n)]
    return array


def create_matrix():
    n = get_dimensions()
    matrix = fill_matrix(n)
    return matrix


def find_averages(matrix:list):
    averages = list()
    for row in matrix:
        averages.append(sum(row)/len(row))
    return averages

def count_elements_bigger_averages(matrix:list, averages:list):
    k = len(averages)
    for i in range(k):
        counter = 0
        for j in range(k):
            if matrix[i][j] > averages[i]:
                counter += 1
        print(counter)

def main():
    matrix = create_matrix()
    avars = find_averages(matrix)
    count_elements_bigger_averages(matrix,avars)

if __name__ == '__main__':
    main()
