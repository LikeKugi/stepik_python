# Какова сумма всех натуральных делителей числа 34?
divigers = []
for i in range(1,35):
    if not 34%i:
        divigers.append(i)
print(sum(divigers))