# По данному числу n найдите максимальное число k, для которого n можно представить
# как сумму k различных натуральных слагаемых.
# Выведите в первой строке число k, во второй — k слагаемых.
def get_unique_components(n: int) -> list[int]:
    components = set()
    for i in range(1, n + 1):

        if n - i == 0 or n - i > i:
            components.add(i)
            n -= i
        if n == 0:
            return sorted(components)


def main():
    # n = int(input())
    answer = [0]
    for n in range(2, 50):
        answer = get_unique_components(n)
        print(f'{n} {sum(answer)}:\n{answer}')

    print(len(answer))
    print(*answer)


if __name__ == '__main__':
    main()
