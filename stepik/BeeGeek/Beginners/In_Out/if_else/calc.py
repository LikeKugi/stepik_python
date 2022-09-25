n1, n2 = int(input()), int(input())
oper = input()
if oper not in ['+', '-', '*', '/']:
    print('Неверная операция')
elif oper == '+':
    print(n1 + n2)
elif oper == '-':
    print(n1 - n2)
elif oper == '*':
    print(n1 * n2)
else:
    if n2 != 0:
        print(n1 / n2)
    else:
        print('На ноль делить нельзя!')
