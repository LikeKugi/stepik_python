start, end = (int(i) for i in input().split())
start = int(start)
end = int(end)

sum = 0
if (start % 2 == 0):
    start += 1
for i in range(start, end + 1, 2):
    sum += i
print(sum)
