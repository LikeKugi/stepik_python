i = 0
while i<0:
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(a*b)
    i+=1


i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
print(i)

i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)