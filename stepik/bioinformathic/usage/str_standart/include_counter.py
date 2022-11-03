#  Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.

s = input()
t = input()


def count_overlaying(line: str, query: str) -> int:
    counter = 0
    i = 0
    while i != -1:
        i = line.find(query, i) + 1
        if i == 0:
            i = -1
        else:
            counter += 1
    return counter

print(count_overlaying(s, t))