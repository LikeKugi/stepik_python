"""
Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки) и выводит самое частое слово в этом тексте
и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое
(можно использовать оператор < для строк).

"""

with open('dataset_3363_3 (1).txt') as inf:
    words = inf.read().strip().split()
words.sort()
dictionary = {}
max = 0
output = []
for word in words:
    if word.lower() not in dictionary:
        dictionary[word.lower()] = words.count(word)
        if words.count(word) > max:
            max = words.count(word)
            output.clear()
            output.append(word)
print(*output, max)