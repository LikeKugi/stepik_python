# У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
# заменить x на 2x, 3x или x+1. По данному целому числу определите минимальное число операций k,
# необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.

# 96234     14
# 74074     17
# 1         0
# 5         3
# 10        3
# 71        9
# 863       14
# 8639      19
# 77759     24

def get_path(n: int) -> None:
    counter = [0] * (n + 1)
    path = []

    for i in range(2, n + 1):
        element = min(counter[i - 1], counter[i // 2 if (not i % 2) else i - 1],
                      counter[i // 3 if (not i % 3) else i - 1])
        counter[i] = element + 1
    print(f'finding = {counter[-1]}')

    i = len(counter) - 1
    while i > 0:
        path.append(i)
        element = min(counter[i - 1], counter[i // 2 if (not i % 2) else i - 1],
                      counter[i // 3 if (not i % 3) else i - 1])
        if not (i % 3) and element == counter[i // 3]:
            i //= 3
        elif not (i % 2) and element == counter[i // 2]:
            i //= 2
        else:
            i -= 1
    if path[-1] != 1:
        path.append(1)
    print()
    print(*path[::-1])


def main():
    number = int(input())
    get_path(number)


if __name__ == '__main__':
    main()
