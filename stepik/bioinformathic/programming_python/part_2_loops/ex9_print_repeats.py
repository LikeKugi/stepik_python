'''
Напишите программу, которая принимает на вход список чисел в одной строке
и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
'''

numbers = [int(i) for i in input().split()]

repeats = []
for i in numbers:
    if numbers.count(i) > 1 and repeats.count(i) == 0:
        repeats.append(i)
        print(i, end=' ')