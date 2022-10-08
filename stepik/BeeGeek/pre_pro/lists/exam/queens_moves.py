"""
На шахматной доске 8×8 стоит ферзь.
Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
остальные клетки заполните точками.
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
            if i == row or j == column or abs(i-row) == abs(j-column):
                field[i, j] = 1
    field[row, column] = -1
    return field


def print_moves(field: np.array):
    n = field.shape[0]
    m = field.shape[1]
    for i in range(n):
        for j in range(m):
            if field[n - i - 1, j] == -1:
                char = 'Q'
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
