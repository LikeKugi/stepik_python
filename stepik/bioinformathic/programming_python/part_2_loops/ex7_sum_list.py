'''
Напишите программу, на вход которой подается одна строка
с целыми числами. Программа должна вывести сумму этих чисел.
'''
numbers = [int(i) for i in input().split()]
print(sum(numbers))