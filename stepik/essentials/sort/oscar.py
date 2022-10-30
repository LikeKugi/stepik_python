# Ваша задача написать программу, которая находит информацию,
# кто из актеров получил наибольшее и наименьшее количество статуэток
actors = []
for _ in range(int(input())):
    actors.append(input())

print(f'{max(actors, key=lambda x: actors.count(x))}, {actors.count(max(actors, key=lambda x: actors.count(x)))}')
print(f'{min(actors, key=lambda x: actors.count(x))}, {actors.count(min(actors, key=lambda x: actors.count(x)))}')