"""
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
"""

digits = [int(i) for i in input()]
count_three = 0
for i in digits:
    if i == 3:
        count_three +=1
print(count_three)
print(digits.count(digits[-1]))
count_even = len(list(filter(lambda x: (x%2==0),digits)))
print(count_even)
sum_greater_five = sum(list(filter(lambda x: (x>5),digits)))
print(sum_greater_five)
product_greater_seven = 1
for i in digits:
    if i > 7:
        product_greater_seven *= i
print(product_greater_seven)
count_zero_five = 0
for i in digits:
    if i == 0 or i == 5:
        count_zero_five += 1
print(count_zero_five)
