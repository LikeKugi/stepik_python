import random as rd

a = 5
while a > 0:
    print(a, end=' ')  # end - smth at the end of the line
    a -= 1
# ////////////////////////////////////////////////////////
print()
# ////////////////////////////////////////////////////////
n = 5
while n <= 55:
    print(n if n % 2 != 0 else '', end=' ')
    n += 1
# ////////////////////////////////////////////////////////
print()
# ////////////////////////////////////////////////////////
i = 0
while i <= 10:
    print('*', end='.')
    i = i + 1
    if i > 7:
        i = i + 2
print('\t', i)
# ////////////////////////////////////////////////////////
print()
# ////////////////////////////////////////////////////////
star = '*'
i = 1
while i < 10:
    print((star * i))
    i += 1
# ////////////////////////////////////////////////////////
print()
# ////////////////////////////////////////////////////////
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
# ////////////////////////////////////////////////////////
print()
# ////////////////////////////////////////////////////////
start = rd.randint(1, 5)
end = rd.randint(8, 10)
print(start, ' ', end)
sum = 0
while start <= end:
    sum += start
    start += 1
print(sum)
