# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

digits = [[int(digit) for digit in input()] for _ in range(2)]
if set(digits[0]).isdisjoint(set(digits[1])):
    print('NO')
else:
    print('YES')


print(('YES','NO')[set(input()).isdisjoint(set(input()))])