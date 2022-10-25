# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20.
total = 0
for num in range(1000, 10000):
    if sum([int(el) for el in str(num)]) == 20:
        total += num
print(total)
