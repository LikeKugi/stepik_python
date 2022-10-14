from decimal import *

d1 = Decimal(1)
d2 = Decimal(567)
d3 = Decimal(-93)
d4 = Decimal('12345')
d5 = Decimal('52.198')

print(d1, d2, d3, d4, d5, sep='\n')

num = Decimal(0.1)

print(num)

num1 = Decimal('5.2')
num2 = Decimal('2.3')

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)

getcontext().prec = 3      # устанавливаем точность в 3 знака

num = Decimal('3.1415')

print(num)
print(num * 1)
print(num * 2)
print(num / 2)