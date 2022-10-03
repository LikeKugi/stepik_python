"""
Напишите функцию convert_to_python_case(text),
которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
"""


# объявление функции
def convert_to_python_case(text):
    new_text = ''
    for i in range(len(text)):
        if i == 0:
            new_text += text[0].lower()
            continue
        if text[i].isupper():
            new_text += '_' + text[i].lower()
        else:
            new_text += text[i]
    return new_text


print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
