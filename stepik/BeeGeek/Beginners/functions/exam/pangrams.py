"""
Панграмма – это фраза, содержащая в себе все буквы алфавита.
Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.

Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке
и возвращает значение True если текст является панграммой и False в противном случае.
"""


# объявление функции
def is_pangram(text):
    chars = set(el.lower() for el in text if el.isalpha())
    print(chars)
    if len(chars) == 26:
        return True
    return False


print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('razy Fredrick bought many very exquisite opal'))

