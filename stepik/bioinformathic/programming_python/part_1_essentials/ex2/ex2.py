X = int(input())
H = int(input())
M = int(input())

HS = X // 60
MS = X % 60

HH = H + HS
MM = M + MS
if MM > 60:
    HH += MM // 60
    MM %= 60

print(HH)
print(MM)