words = []
for _ in range(int(input())):
    words.append(input().lower())
mistakes = []
for _ in range(int(input())):
    line = input().split()
    for el in line:
        if el.lower() not in words and el not in mistakes:
            mistakes.append(el)

for el in mistakes:
    print(el)