"""
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек).
Напишите программу, которая выводит члены данной последовательности.
"""

words = []
while True:
    line = input()
    if line.upper() != 'КОНЕЦ':
        words.append(line)
    else:
        break
print(*words,sep='\n')