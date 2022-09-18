x = int(input('input number: '))

if x % 2 == 0:
    print('watch for tabs')
    print('even')
else:
    print('odd')

print()

a = int(input('1 number: '))
b = int(input('2 number: '))
if b != 0:
    print(a / b)
else:
    print('no division')
    b = int(input('enter another number: '))
    print(a / b)
