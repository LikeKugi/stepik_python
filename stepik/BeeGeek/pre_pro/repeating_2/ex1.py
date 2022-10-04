"""
На вход программе подается строка текста из натуральных чисел.
Из элементов строки формируется список чисел.
Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
"""

numbers = [int(number) for number in input().split()]
l = len(numbers)
moved_numbers = [0]*l
for i in range(l):
    moved_numbers[i] = numbers[(i-1)%l]
print(*moved_numbers)