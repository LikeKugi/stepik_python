# Напишите функцию shift_letter , которая принимает два аргумента:
#
# letter одна английская буква в нижнем регистре
# shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
# Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift.
# Сдвиг может быть цикличным в пределах от a до z.
#
# Не забудьте проаннотировать аргументы и также добавьте doc-строку «Функция сдвигает символ letter на shift позиций»
#
# Функция shift_letter должна вернуть новый символ.


def shift_letter(letter: str, shift: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))


print(shift_letter('b', 2))
print(shift_letter('d', 1))
print(shift_letter('z', 1))
print(shift_letter('d', -2))
print(shift_letter('d', 26))
print(shift_letter('b', -3))
