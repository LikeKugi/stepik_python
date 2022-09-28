
for i in range(10):
    print(i, end='*')
    if i > 6:
        break
print()
i = 100
while i > 0:
    if i == 40:
        break
    print(i, end='*')
    i -= 20
print()
n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')
print()
result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i
print(result)
mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)

count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')