import taichi as ti

ti.init()


@ti.kernel
def count_euler():
    for a in range(1, 151):
        for b in range(1, 151):
            for c in range(1, 151):
                for d in range(1, 151):
                    for e in range(1, 151):
                        if ((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5) == (
                                e ** 5)) and a < e and b < e and c < e and d < e:
                            print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'e = ', e)
                            print(a + b + c + d + e)



count_euler()
