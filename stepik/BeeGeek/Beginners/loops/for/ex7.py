"""
На вход программе подается натуральное число n, а затем n целых чисел,
каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.
"""
total = 0
for _ in range(int(input())):
    total += int(input())
print(total)