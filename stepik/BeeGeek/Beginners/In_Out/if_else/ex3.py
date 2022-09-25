r1, c1, r2, c2 = int(input()), int(input()), int(input()), int(input())
if (r1 == r2 and c1 != c2) or (r1 != r2 and c1 == c2):
    print('YES')
else:
    print('NO')

if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1:
    print('YES')
else:
    print('NO')
