"""
поле для сапёра
"""


def PrintList(field_p):
    for i in range(len(field_p)):
        for j in range(len(field_p[i])):
            print(field_p[i][j] if field_p[i][j] > 0  else '*' if field_p[i][j] == -1 else '.', end='  ')
        print()


def PlaceMines(field_all, mines_count):
    for i in range(mines_count):
        r, c = (int(el) - 1 for el in input().split())
        field_all[r][c] = -1


def PlaceCounts(mines_field):
    r = len(mines_field)
    c = len(mines_field[r-1])
    for i in range(r):
        for j in range(c):
            if mines_field[i][j] == 0:
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ai = i + di
                        aj = j + dj
                        if 0 <= ai < r and 0 <= aj < c and mines_field[ai][aj] == -1:
                            mines_field[i][j] += 1


rows, columns, fieldset = (int(i) for i in input().split())

field = []
for i in range(rows):
    field.append([])
    for j in range(columns):
        field[i].append(0)
PlaceMines(field, fieldset)
PlaceCounts(field)
PrintList(field)
