"""
На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
а затем все положительные числа, каждое на отдельной строке.
Числа должны быть выведены в том же порядке, в котором они были введены.
"""

numbers = [int(input()) for _ in range(int(input()))]
for number in numbers:
    if number < 0:
        print(number)
for number in numbers:
    if number == 0:
        print(number)
for number in numbers:
    if number > 0:
        print(number)