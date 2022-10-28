# Ваша задача создать функцию create_matrix, которая принимает
#
# необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает значение 3;
# необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали.
# По умолчанию равен 0;
# необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся выше главной диагонали.
# По умолчанию равен 0;
# Функция create_matrix должна возвращать квадратную матрицу размером size х size,
# на диагонали которой располагаются числа от 1 до size.
# Все остальные элементы заполнены согласно параметрам up_fill и down_fill.

def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list[list]:
    matrix = []
    for i in range(size):
        matrix.append([0] * size)
        for j in range(size):
            if i == j:
                matrix[i][j] = i + 1
            elif i > j:
                matrix[i][j] = down_fill
            else:
                matrix[i][j] = up_fill
    return matrix


print(create_matrix())
print(create_matrix(4))
print(create_matrix(up_fill=7))
print(create_matrix(up_fill=7, down_fill=9))
print(create_matrix(size=4, up_fill=7, down_fill=9))