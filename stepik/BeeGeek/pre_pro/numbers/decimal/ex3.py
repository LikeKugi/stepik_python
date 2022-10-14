"""
Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.
"""
from decimal import *
num = Decimal(input())

digits = [int(digit) for digit in str(num) if digit.isdigit()]
print(max(digits) + min(digits))

cyphers = num.as_tuple().digits
print(max(cyphers) + min(cyphers) * (abs(num) >= 1))