"""
Напишите программу, вычисляющую значение тригонометрического выражения
sin(x)+cos(x)+tan^2(x)
 по заданному числу градусов x.
"""
import math

x = float(input())
x = math.radians(x)
print(math.sin(x) + math.cos(x) + math.tan(x) ** 2)
