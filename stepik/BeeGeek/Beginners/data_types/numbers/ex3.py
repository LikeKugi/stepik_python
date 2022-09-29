"""
На вход программе подается число nn – количество собачьих лет.
Напишите программу, которая вычисляет возраст собаки в человеческих годах.

Формат входных данных
На вход программе подаётся натуральное число – количество собачьих лет.

Формат выходных данных
Программа должна вывести возраст собаки в человеческих годах.

Примечание. В течение первых двух лет собачий год равен 10.5 человеческим годам.
После этого каждый год собаки равен 4 человеческим годам.
"""
for i in range(1,20):
    dog_age = i  # int(input())
    humans_age = (dog_age - 2) * 4 + 21 if dog_age > 2 else dog_age * 10.5
    print(humans_age)