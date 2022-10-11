"""
Формат входных данных
На вход программе подаются две строки с числами: в первой строке числа с первого листочка, во второй со второго.

Формат выходных данных
Программа должна вывести числа, встретившиеся на обоих листках в отсортированном по убыванию порядке,
либо словосочетание BAD DAY, если таких чисел нет.
"""

numbers = [[int(number) for number in input().split()] for _ in range(2)]
common_numbers = set(numbers[0]) & set(numbers[1])
if common_numbers:
    print(*sorted(common_numbers,reverse=True))
else:
    print('BAD DAY')