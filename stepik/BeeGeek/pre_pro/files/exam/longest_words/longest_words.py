"""
Вам доступен текстовый файл words.txt со словами, разделенными пробелом.
Напишите программу, которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования.
"""

with open('words.txt') as inf:
    words = inf.read().rstrip().split()
    print(*filter(lambda x: len(x) == len(max(words, key=len)), words), sep='\n')