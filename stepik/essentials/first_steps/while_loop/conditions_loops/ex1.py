"""
Давайте переберем все числа от а до b включительно и будем их выводить на экран,
при этом нужно выполнить следующие условия:

пропускать (не выводить) числа, которые делятся на 2 или на 3
если встречаете число, кратное 777, необходимо принудительно закончить цикл, само это число не выводить
Постарайтесь не использовать цикл for
"""
a, b = int(input()), int(input())
while a <= b:
    if not a % 777:
        break
    if (a % 2 and a % 3):
        print(a)
    a += 1
