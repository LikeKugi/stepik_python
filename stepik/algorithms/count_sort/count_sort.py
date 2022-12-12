# Первая строка содержит число n, вторая — n натуральных чисел,
# не превышающих 10. Выведите упорядоченную по не убыванию последовательность этих чисел.
def count_sort(numbers: map) -> list:
    temp_list = [0] * 10
    for el in numbers:
        temp_list[el] += 1
    out_list = []
    for i, n in enumerate(temp_list):
        out_list.extend([i] * n)
    return out_list


def main():
    n = int(input())
    numbers = map(int, input().split())
    print(*count_sort(numbers))


if __name__ == '__main__':
    main()
