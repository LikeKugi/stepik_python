# Первая строка входа содержит целые числа W и n — вместимость рюкзака и число золотых слитков.
# Следующая строка содержит n целых чисел, задающих веса слитков.
# Найдите максимальный вес золота, который можно унести в рюкзаке.
def fill_backpack(W: int, n: int, weights: list[int]) -> int:
    variants = [[0] * (W + 1) for _ in range(n + 1)]
    print(variants)
    print()
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            variants[i][j] = variants[i][j - 1]
            if weights[i - 1] <= j:
                print(f'{weights[i-1] = }')
                print(f'{i = } {j = }')
                variants[i][j] = max(variants[i - 1][j], variants[i - 1][j - weights[i - 1]] + weights[i - 1])
            else:
                variants[i][j] = variants[i - 1][j]
        print(*variants, sep='\n')
        print()
    print(variants[-1][-1])
    return variants[-1][-1]


def main():
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    fill_backpack(W, n, weights)


if __name__ == '__main__':
    main()
