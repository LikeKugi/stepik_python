pass1 = input()
pass2 = input()

if pass1 == pass2:
    print("Пароль принят")
else:
    print("Пароль не принят")

number = input()
if int(number[0]) + int(number[-1]) == int(number[1]) - int(number[2]):
    print('ДА')
else:
    print('НЕТ')

a, b, c = int(input()), int(input()), int(input())
if (a - b) == (b - c):
    print('YES')
else:
    print('NO')

a, b = int(input()), int(input())
print(min(a, b))

age = int(input())
if age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
else:
    print('старость')

a, b, c = int(input()), int(input()), int(input())
sum = (a if a > 0 else 0) + (b if b > 0 else 0) + (c if c > 0 else 0)
