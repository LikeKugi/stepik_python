# Даны целые числа
# необходимо найти остаток от деления nn-го числа Фибоначчи на mm.

def find_pisano(n, m):
    periods = [0, 1]
    for i in range(n):
        current_number = (periods[-2] % m + periods[-1] % m) % m
        periods.append(current_number)
        if periods[-2] == 0 and periods[-1] == 1:
            periods.pop()
            periods.pop()
            break
    print(periods[n % len(periods)])


def tests():
    test_sets = [
        (9, 2),  # 0
        (10, 2),  # 1
        (1025, 55),  # 5
        (12589, 369),  # 89
        (1598753, 25897),  # 20305
        (60282445765134413, 2263)  # 974
    ]
    for n, m in test_sets:
        find_pisano(n, m)


def main():
    number, m_number = map(int, input().split())
    find_pisano(number, m_number)


if __name__ == '__main__':
    main()
