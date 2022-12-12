#  Найдите наибольшую невозрастающую подпоследовательность в A.
#  В первой строке выведите её длину k, во второй — её индексы
def get_max_subsequence(numbers: list) -> list:
    n = len(numbers)
    subsequences = [0] * n
    prev = [0] * n

    for i in range(n):
        subsequences[i] = 1
        prev[i] = -1
        for j in range(i):
            if (numbers[i] <= numbers[j]) and subsequences[j] + 1 > subsequences[i]:
                subsequences[i] = subsequences[j] + 1
                prev[i] = j
    get_indexes(prev, subsequences)
    return subsequences


def get_indexes(previous: list, subsequences: list):
    indexes = []
    print(subsequences)
    min_el = max(subsequences)
    i = subsequences.index(min_el)
    print(i)
    while i != -1:
        indexes.append(i+1)
        print(i)
        i = previous[i]
    print(f'{min_el = }')
    print('indexes: ', end='')
    print(*indexes[::-1])


def main():
    length = int(input())
    sequence = list(map(int, input().split()))
    sub = get_max_subsequence(sequence)


if __name__ == '__main__':
    main()
