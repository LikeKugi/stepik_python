"""
Напишите программу, которая определяет, какой температуре по шкале Цельсия
соответствует указанное значение по шкале Фаренгейта.

Используйте формулу для перевода: C = (5 / 9) * (F− 32)

"""

fahrenheit_temperature = float(input())
cels_temperature = (5 / 9) * (fahrenheit_temperature - 32)
print(cels_temperature)
