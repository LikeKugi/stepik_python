"""
Напишите функцию is_password_good(password), которая принимает в качестве аргумента
строковое значение пароля password и возвращает значение
True если пароль является надежным и
False в противном случае.

Пароль является надежным если:

его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
"""


# объявление функции
def is_password_good(password):
    if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(
            char.isupper() for char in password) and len(password) >= 8:
        return True
    return False


# считываем данные
# txt = input()

# вызываем функцию
# print(is_password_good(txt))

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
