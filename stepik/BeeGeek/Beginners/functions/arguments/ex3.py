"""
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
"""

# объявление функции
def print_digit_sum(num):
    print(sum([int(digit) for digit in str(num)]))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)