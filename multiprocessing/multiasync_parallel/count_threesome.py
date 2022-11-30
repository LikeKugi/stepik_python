def read_ints(path):
    lst = []

    with open(path) as inf:
        while line := inf.readline():
            lst.append(int(line))

    return lst


def count_three_sum(ints, thread_name=''):
    print('started count three numbers to sum 0')
    print(f'name: {thread_name}')
    n = len(ints)
    counter = 0
    cc_done = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                cc_done += 1
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'in {thread_name}: ',end='')
                    print(f'triple found: {ints[i]} + {ints[j]} + {ints[k]}')

    print(f'ended count threesome triples: {counter}')
    print(f'iterations {cc_done}')
