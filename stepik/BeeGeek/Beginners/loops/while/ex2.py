"""
На вход программе подается последовательность слов,
каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» (без кавычек).
Напишите программу, которая выводит члены данной последовательности.
"""
line = ''
words = []
while line != 'КОНЕЦ':
    words.append(line)
    line = input()
print(*words,sep='\n')