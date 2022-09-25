a = 2
b = 4
c = 6
print(a == 2 or b > 2)
print(6 <= c and a > 3)
print(1 != b and c != 3)
print(a >= -1 or a <= b)
print(not (a > 2))
print(not (c <= 10))

num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')

a = 7 
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)