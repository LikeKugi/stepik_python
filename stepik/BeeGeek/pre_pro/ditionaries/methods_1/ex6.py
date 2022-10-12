"""
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""

words = [word.strip('.,!?:;-') for word in input().lower().split()]
count_words = {}
for word in words:
    count_words.setdefault(words.count(word), []).append(word)
print(sorted(count_words.get(min(count_words)))[0])