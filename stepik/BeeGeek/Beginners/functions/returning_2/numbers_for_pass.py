"""
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c,
где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента
строковое значение пароля password и возвращает значение True
если пароль является действительным паролем BEEGEEK банка и False в противном случае.
"""
import math


def is_prime(num):
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0 or num == 1:
        return False
    for i in range(1, math.ceil(math.sqrt(num))):
        if (num % (6 * i - 1) == 0 and (6 * i - 1) != num) or (num % (6 * i + 1) == 0 and (6 * i + 1) != num):
            return False
    return True


# объявление функции
def is_valid_password(password):
    numbers = password.split(':')
    if len(numbers)==3:
        if numbers[0] == numbers[0][::-1] and is_prime(int(numbers[1])) and int(numbers[2])%2==0:
            return True
    return False


print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
print(is_valid_password('15551:7:290'))

