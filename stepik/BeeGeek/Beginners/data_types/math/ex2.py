"""
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
"""
import math

r = float(input())
s = math.pi * r **2
c = 2 * math.pi * r
print(s,c,sep='\n')