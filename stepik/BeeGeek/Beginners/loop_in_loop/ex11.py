"""
Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.
"""
import math

n = int(input())
sum_factorials = 0
for i in range(1,n+1):
    sum_factorials += math.factorial(i)
print(sum_factorials)