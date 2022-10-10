# На вход программе подаются две строки, состоящие из цифр.
# Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?

digits = list()
for _ in range(2):
    digits.extend([int(el) for el in input()])
if len(set(digits)) == 10:
    print('YES')
else:
    print('NO')

print(('NO', 'YES')[len(set(input() + input())) == 10])