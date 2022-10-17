"""
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.
"""
def sum_digits_compare(n):
    return sum([int(digit) for digit in str(n)])

numbers = [int(el) for el in input().split()]

numbers.sort(key=sum_digits_compare)

print(*numbers)