#  По известному списку всех дней рождения научитесь определять, у кого день рождения в заданном месяце.

from collections import defaultdict
birthdays = defaultdict(list)

for _ in range(int(input())):
    name, date, mon = input().split()
    birthdays[mon].append(name)
    birthdays[mon].sort()

for _ in range(int(input())):
    print(*birthdays.get(input(), ['Нет данных']))