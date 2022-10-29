#  В этой задаче вам необходимо скачать файл, в котором записаны натуральные числа. Ваша задача найти
#
# количество трехзначных чисел;
# сумму двухзначных чисел
# В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов.
# Сперва количество, потом сумма

with open('numbers.txt') as inf:
    sum_decimals = 0
    count_hundreds = 0
    for line in inf:
        if 9 < int(line.rstrip()) < 100:
            sum_decimals += int(line.rstrip())
        elif 99 < int(line.rstrip()) < 1000:
            count_hundreds += 1

print(f'{count_hundreds},{sum_decimals}')