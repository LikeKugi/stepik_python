# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

for _ in range(int(input())):
    print(len(set(input().lower())))