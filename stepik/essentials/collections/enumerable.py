"""
Luhn algorithm

Упрощенная версия алгоритма выглядит так:

Цифры проверяемой последовательности нумеруются справа налево.
Цифры, оказавшиеся на нечётных местах, остаются без изменений.
Цифры, стоящие на чётных местах, умножаются на 2.
Если в результате такого умножения возникает число больше 9, оно уменьшается на значение 9
Все полученные в результате преобразования 16 цифр складываются. Если сумма кратна 10, то исходные данные верны.

"""

card_number = [int(digit) for digit in input()]
card_number.reverse()
print(card_number)

for i in range(len(card_number)):
    if i % 2:
        card_number[i] = (card_number[i] * 2) if (card_number[i] * 2 < 10) else (card_number[i] * 2 - 9)

print(card_number)
print(('False','True')[sum(card_number)%10==0])