# Даны по 10-балльной шкале оценки по биологии трех учеников.
# Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.

total = set(range(11))
grades = [[int(grade) for grade in input().split()] for _ in range(3)]

print(*sorted(set(range(11)) - (set(grades[2]) | (set(grades[0]) | set(grades[1])))))