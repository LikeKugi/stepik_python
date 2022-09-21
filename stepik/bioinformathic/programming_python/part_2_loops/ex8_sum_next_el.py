'''
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
'''

numbers = [int(i) for i in input().split()]
sumNumbers = []
for i in range(len(numbers)):
    y = i - 1 if i - 1 >= 0 else len(numbers) - i - 1
    z = i + 1 if i + 1 < len(numbers) else i + 1 - len(numbers)
    sumNumbers.append((numbers[y] + numbers[z]) if len(numbers) > 1 else numbers[i])
for i in sumNumbers:
    print(i, end=' ')
