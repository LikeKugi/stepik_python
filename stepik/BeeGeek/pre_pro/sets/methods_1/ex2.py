# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

letters = set()
for _ in range(int(input())):
    letters = letters | set(input().lower())
print(len(letters))
