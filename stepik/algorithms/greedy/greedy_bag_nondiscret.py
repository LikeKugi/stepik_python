# Первая строка содержит количество предметов и вместимость рюкзака
# Каждая из следующих nn строк задаёт стоимость и объём предмета.
# Выведите максимальную стоимость частей предметов (от каждого предмета
# можно отделить любую часть, стоимость и объём при этом пропорционально
# уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
def get_greedy_bag(W, goods):
    price = 0
    for good in goods:
        print(f'current weight {W}')
        print(f'good weight {good[1]}')

        if W - good[1] > 0:
            W -= good[1]
            price += good[0]
        else:
            count = W
            price_count = (good[0] / good[1]) * count
            W -= count
            price += price_count

        print(f'weight: {W}')
        print(f'current price {price}')
        print()

        if W == 0:
            return price
    else:
        return price


def main():
    goods = []
    n, W = map(int, input().split())

    for _ in range(n):
        goods.append([int(el) for el in input().split()])

    goods.sort(key=lambda x: -x[0] / x[1])
    print(goods)
    price = get_greedy_bag(W, goods)
    print(f'{price:.3f}')

if __name__ == '__main__':
    main()
