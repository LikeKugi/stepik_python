import math

b, q, n = int(input()), int(input()), int(input())
print(b * q ** (n - 1))

pupils, count = int(input()), int(input())
print(count // pupils)
print(count % pupils)

people = int(input())
print(people // 2 if people % 2 == 0 else (people + 1) // 2)

seat = int(input())
print(math.ceil(seat / 4))

mins = int(input())
hours = mins // 60
minutes = mins - hours * 60
print(mins, 'мин - это',hours,'час', minutes,'минут.')
