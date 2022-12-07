# В первой строке даны целое число n и массив из n различных натуральных чисел,
# не превышающих 10^9, в порядке возрастания,
# во второй — целое число и k натуральных чисел не превышающих 10^9.
#
# Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n, для которого A[j]=b, или −1, если такого j нет.

def get_int_list(): return list(map(int, input().split()))


def binary_search(numbers: list, query: int) -> int:
    start = 0
    end = len(numbers) - 1
    print(query)
    while start <= end:
        mid = (end + start) // 2
        print(f's: {start}; e: {end}; m: {mid}')
        if numbers[mid] == query:
            return mid
        elif numbers[mid] < query:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return -1


def main():
    n, *numbers = get_int_list()
    k, *queries = get_int_list()

    indexes = []
    print(numbers)
    for q in queries:
        i = binary_search(numbers, q)
        print(f'q: {q}; i: {i}')
        indexes.append(i + 1 if i != -1 else -1)
    print(*indexes)


if __name__ == '__main__':
    main()
