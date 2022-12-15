# Даны число ступенек лестницы и целые числа , которыми помечены ступеньки.
# Найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх
# (от нулевой до nn-й ступеньки), каждый раз поднимаясь на одну или две ступеньки.
def find_max_sum(stairs: list) -> int:

    n = len(stairs)
    sums = [0] * (n + 1)
    sums[1] = stairs[0]

    if n > 1:
        for i in range(2, n + 1):
            print([0],stairs)
            print(sums)
            sums[i] = max(sums[i-1], sums[i-2]) + stairs[i-1]

    print(sums)
    print(sums[-1])


def main():
    length = int(input())
    stairs = list(map(int, input().split()))
    find_max_sum(stairs)

if __name__ == '__main__':
    main()