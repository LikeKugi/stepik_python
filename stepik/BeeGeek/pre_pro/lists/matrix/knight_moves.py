"""
На шахматной доске 8×8 стоит конь.
Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь.
Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
отметьте символами *, остальные клетки заполните точками.
"""
import numpy as np

cols = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def get_position():
    column, row = (el for el in input())
    column = cols.get(column) - 1
    row = int(row) - 1
    return row, column


def create_chess_field(): return np.zeros((8, 8), dtype=np.int8)


def put_position(field: np.array, row, column):
    field[row, column] = -1
    return field


def put_moves(field: np.array, row, column):
    n = field.shape[0]
    m = field.shape[1]
    for i in range(n):
        for j in range(m):
            if (abs(i - row) == 1 and abs(j - column) == 2) or (abs(i - row) == 2 and abs(j - column) == 1):
                field[i, j] = 1
    return field


def print_moves(field: np.array):
    n = field.shape[0]
    m = field.shape[1]
    for i in range(n):
        for j in range(m):
            if field[n - i - 1, j] == -1:
                char = 'N'
            elif field[n - i - 1, j] == 1:
                char = '*'
            else:
                char = '.'
            print(char, end=' ')
        print()


def main():
    row, column = get_position()
    field = create_chess_field()
    put_position(field, row, column)
    put_moves(field, row, column)
    print_moves(field)


if __name__ == '__main__':
    main()
