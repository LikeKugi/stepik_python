"""
Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

Дано положительное действительное число. Выведите его дробную часть.

"""
number = float(input())
output = (number * 10) % 10
print(int(output))

output = number - int(number)
print(output)

num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
print(num)