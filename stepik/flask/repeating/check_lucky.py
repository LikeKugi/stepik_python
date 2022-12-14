# Напишите функцию с названием detect_lucky, которая принимает в качестве аргумента шестизначное число
# и возвращает True, если оно является счастливым, и False в противном случае.
# Счастливым называется шестизначное число, сумма первых трех цифр которого равна сумме последних трех цифр.

def detect_lucky(n: int) ->bool:

    return sum([int(el) for el in str(n)[:3]]) == sum([int(el) for el in str(n)[3:]])

print(detect_lucky(985778))