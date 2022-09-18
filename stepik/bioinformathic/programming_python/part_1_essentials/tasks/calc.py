a = float(input())
b = float(input())
do = input()

if do == '+':
    print(a + b)
elif do == '-':
    print(a - b)
elif do == '*':
    print(a * b)
elif do == 'pow':
    print((a ** b))
elif b == 0:
    print("Деление на 0!")
elif do == '/':
    print(a / b)
elif do == 'mod':
    print(a % b)
else:
    print(a // b)
