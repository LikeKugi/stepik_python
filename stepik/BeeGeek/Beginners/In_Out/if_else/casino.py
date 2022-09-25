number = int(input())
if not (0 <= number <= 36):
    print('ошибка ввода')
elif number == 0:
    print('зеленый')
elif ((number in range(1, 11) or number in range(19, 29)) and number % 2 != 0) or (
        (number in range(11, 19) or number in range(29, 37)) and number % 2 == 0):
    print('красный')
else:
    print('черный')
