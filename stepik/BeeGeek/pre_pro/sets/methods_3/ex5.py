# Даны по 1010-балльной шкале оценки по математике трех учеников.
# Напишите программу, которая выводит множество оценок, имеющихся у учеников,
# которые встречаются не более, чем у двух из указанных учеников.

grades = [[int(grade) for grade in input().split()] for _ in range(3)]
print(*sorted((set(grades[0]) | set(grades[1]) | set(grades[2])) - (set(grades[0]) & set(grades[1]) & set(grades[2]))))

