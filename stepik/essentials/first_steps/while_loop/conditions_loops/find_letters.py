"""
Вам на вход поступает слово и ваша задача в цикле while обойти все его буквы и распечатать их в формате фразы:

«Текущая буква: <letter>».

Как только вы встретите строчные английские буквы «e» или «a» нужно вывести фразу «Ага! Нашлась»,
перестать печатать буквы и принудительно выйти из цикла.

В случае, если в слове не оказалось букв «e» или «a» необходимо вывести фразу «Распечатали все буквы»
"""
i = 0
word = input()
while i < len(word):
    if word[i] in ('a', 'e'):
        print('Ага! Нашлась')
        break
    else:
        print(f'Текущая буква: {word[i]}')
    i += 1
else:
    print('Распечатали все буквы')
