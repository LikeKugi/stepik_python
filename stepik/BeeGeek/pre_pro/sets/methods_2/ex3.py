# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая выводит все числа в порядке возрастания,
# которые есть в первой строке, но отсутствуют во второй.

print(*sorted(set(input().split()) - set(input().split()), key=int))
