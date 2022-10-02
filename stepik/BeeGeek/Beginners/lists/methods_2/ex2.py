"""
На вход программе подается строка текста, содержащая различные натуральные числа.
Из данной строки формируется список чисел.
Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
"""

numbers = [int(el) for el in input().split()]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print(numbers)
