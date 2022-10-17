"""
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.
"""

def sum_digits_compare(n):
    return sum([int(digit) for digit in str(n)]) ,n

numbers = [int(el) for el in input().split()]
numbers.sort(key=sum_digits_compare)

print(*numbers)