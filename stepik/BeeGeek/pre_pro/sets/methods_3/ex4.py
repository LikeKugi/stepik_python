# Даны по 10-балльной шкале оценки по информатике трех учеников.
# Напишите программу, которая выводит множество оценок, которые есть и у первого и у второго учеников,
# но которых нет у третьего ученика.
grades = [[int(grade) for grade in input().split()] for _ in range(3)]
print(*sorted(set(grades[0]) & set(grades[1]) - set(grades[2]), reverse=True))

print()
