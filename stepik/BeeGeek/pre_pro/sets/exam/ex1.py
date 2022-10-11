"""
Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур,
однако к концу игры ввиду своего возраста забывают, какие города уже называли.

Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.
"""

cities = set()
for _ in range(int(input())+1):
    city = input().lower()
    if city in cities:
        print('REPEAT')
        break
    cities.add(city)
else:
    print('OK')

print(cities)