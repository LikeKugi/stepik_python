"""
Список data содержит слова на русском языке. Напишите программу его сортировки по возрастанию длины слов,
а затем в лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом пробела.
"""

data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

a = sorted(data, key=lambda x: (len(x), x))
print(a)

print(*sorted(data, key=lambda x: (len(x), x)))