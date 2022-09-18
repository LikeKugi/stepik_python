# inputLine = input()

digits = list(input())

#print(digits)
sum1 = sum2 = 0

for i in range(int(len(digits) / 2)):
    sum1 += int(digits[i])
for i in range(int(len(digits) / 2), len(digits)):
    sum2 += int(digits[i])
print("Счастливый" if sum1==sum2 else "Обычный")