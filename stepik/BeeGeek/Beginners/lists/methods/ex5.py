"""
На вход программе подается натуральное число n.
Напишите программу, которая создает список состоящий из делителей введенного числа.
"""

divigers = list()
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        divigers.append(i)
print(divigers)
