"""
Напишите функцию is_valid_triangle(side1, side2, side3),
которая принимает в качестве аргументов три натуральных числа,
и возвращает значение True если существует невырожденный треугольник
со сторонами side1, side2, side3 и False в противном случае.
"""


# объявление функции
def is_valid_triangle(side1, side2, side3):
    total = side1 + side2 + side3
    max_side = max(side1, side2, side3)
    return True if total - max_side > max_side else False


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
