n = int(input())
f1, f2 = 1, 1

with open('fibonacci.txt', 'w') as ouf:
    ouf.write(f'fibonacci sequence of {n}: \n')

    for i in range(1, n+1):
        ouf.write(str(i) + ':\t' + str(f1) + '\n')
        f1, f2 = f2, f1 + f2