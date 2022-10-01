"""
На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
"""

words = list()
for _ in range(int(input())):
    word = input()
    if word not in words:
        words.append(word)
print(*words,sep='\n')