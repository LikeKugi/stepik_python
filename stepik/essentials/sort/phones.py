#  Напишите программу, которая поможет Пете находить все номера определённого друга.
from collections import defaultdict
phones = defaultdict(list)
for _ in range(int(input())):
    ph, nm = input().split()
    phones[nm].append(int(ph))

print(phones)

for _ in range(int(input())):
    print(*phones.get(input(), ['Неизвестный номер']))