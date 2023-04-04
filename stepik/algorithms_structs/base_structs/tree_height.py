def make_nodes(arr: list[int]) -> dict[int, list[int]]:
    node = {}
    for i, el in enumerate(arr):
        if el in node.keys():
            node[el].append(i)
        else:
            node[el] = [i]
    print(node)
    return node


def find_height(nodes: dict[int, list[int]], root: int) -> int:
    height = 1
    if root in nodes:
        print(f'{root = }')
        print(nodes[root])
        for child in nodes[root]:
            height = max(height, find_height(nodes, child) + 1)
            print(f'{height = }')
    return height


def iterate_height():
    n, parents = int(input()), [int(i) for i in input().split()]
    a = [[] for i in range(n + 1)]
    for i in range(n):
        a[parents[i]] += [i]

    root, lev = a[-1], 0
    while len(root):
        q, root = root, []
        for b in q:
            root += a[b]
        lev += 1
    print(lev)


if __name__ == '__main__':
    count_nodes = int(input())
    arr = list(map(int, input().split()))
    nodes = make_nodes(arr)
    print(find_height(nodes, -1) - 1)
