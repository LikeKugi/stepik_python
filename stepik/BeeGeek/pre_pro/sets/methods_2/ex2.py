# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая выводит все числа в порядке возрастания,
# которые есть как в первой строке, так и во второй.

print(*sorted(set(int(el) for el in input().split()) & set(int(el) for el in input().split())))