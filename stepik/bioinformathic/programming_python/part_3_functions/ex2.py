"""
подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить
для каждого уникального слова в этой строке число его повторений
(без учёта регистра) в формате "слово количество"
"""

words = input().lower().split()
counter = 0
dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word] = words.count(word)

for key,value in dictionary.items():
    print(key, value)