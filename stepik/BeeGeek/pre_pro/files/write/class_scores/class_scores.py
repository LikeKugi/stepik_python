"""
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида:
фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.

Напишите программу для добавления 5 баллов к каждому результату теста
и вывода фамилий и новых результатов тестов в файл new_scores.txt.
"""

with open('class_scores.txt') as inf, open('new_scores.txt', 'w') as ouf:
    for line in inf:
        name, score = map(str.rstrip, line.split())
        score = str(min(int(score) + 5, 100))
        print(name, score, file=ouf)
