'''
Напишите программу, считывающую с пользовательского ввода
целое число nn (неотрицательное), выводящее это число в консоль
вместе с правильным образом изменённым словом "программист",
для того, чтобы робот мог нормально общаться с людьми,
например: 1 программист, 2 программиста, 5 программистов.
'''

count = int(input())

if (count % 10 == 1 and count%100 != 11):
    print(count, "программист")
elif (2 <= count % 10 <= 4 and not (12 <= count % 100 <= 14)):
    print(count, "программиста")
else:
    print(count, "программистов")

