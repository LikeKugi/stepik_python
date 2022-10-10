# Даны по 10-балльной шкале оценки по физике трех учеников.
# Напишите программу, которая выводит множество оценок третьего ученика,
# которые не встречаются ни у первого, ни у второго ученика.

grades = [[int(grade) for grade in input().split()] for _ in range(3)]
print(*sorted(set(grades[2]) - (set(grades[0]) | set(grades[1])), reverse=True))
