number = 999000112233
i = 0
while number > 0:
    i+=1
    number = number // 10
print(i)


number = 1234567890
count = 0
while number > 0:
    last_digit = number % 10
    if last_digit < 3:
        count = count + 1
    number = number // 10
print(count)

number = 73408
m = 0
s = 0
while number > 0:
    last_digit = number % 10
    s = s + last_digit
    if last_digit > m:
        m = last_digit
    number = number // 10
print(s + m)