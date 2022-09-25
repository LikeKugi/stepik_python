a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a2 > b1) or (a1 > b2):
    print('пустое множество')
elif a2 == b1:
    print(a2)
elif a1 == b2:
    print(a1)
else:
    print(min(b1, max(a1, a2)), min(b1, b2))
