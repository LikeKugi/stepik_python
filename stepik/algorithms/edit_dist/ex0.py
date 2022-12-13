#  Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2,
#  содержащих строчные буквы латинского алфавита.
def edit_distance(line_a: str, line_b: str) -> int:
    """
    i, n: line_a
    j, m: line_b
    :param line_a: str
        first line to compare
    :param line_b: str
        second line to compare
    :return: int
        distance between lines
    """
    if line_a == line_b: return 0
    n, m = len(line_a), len(line_b)
    distances = [[0 if i and j else i or j for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            print(len(distances))
            print(len(distances[i]))
            print(f'{i = }; {n = }; {line_a = }')
            print(f'{j = }; {m = }; {line_b = }')
            print(f'{distances[i][j] = }')
            diff = (1, 0)[line_a[i-1] == line_b[j-1]]
            print(f'{line_a[i-1] = }; {line_b[j-1] = }; {diff = }')
            distances[i][j] = min(distances[i-1][j] + 1, distances[i][j-1] + 1, distances[i-1][j-1] + diff)

    print(*distances,sep='\n')
    return distances[-1][-1]


def main():
    line_a = input()
    line_b = input()
    print(edit_distance(line_a, line_b))


if __name__ == '__main__':
    main()