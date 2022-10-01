"""
На вход программе подается натуральное число n и n строк, а затем число k.
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.
"""

words = list()
for _ in range(int(input())):
    words.append(input())
k = int(input())
for word in words:
    if len(word)>=k:
        print(word[k-1],end='')