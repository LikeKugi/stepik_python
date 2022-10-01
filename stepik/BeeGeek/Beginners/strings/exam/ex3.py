"""
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов,
заключенную между первым и последним вхождением буквы «h».
"""

line = input()
begins = line.find('h')
ends = line.rfind('h')
reversed = line[begins+1:ends]
print(reversed[::-1])
print(line[:begins]+line[ends:begins:-1]+line[ends:])
print(line.replace(line[begins+1:ends],reversed[::-1]))