# И так, ваша задача создать функцию caesar_cipher , которая принимает на вход текст и значение сдвига.
#
# Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому символу
# и преобразовать его по следующим правилам:
#
# если символ является знаком пунктуации, оставляем его как есть
# если это буква, то сместить ее при помощи ранее написанной функции shift_letter
# Закодированный текст необходимо вернуть в качестве ответа.

def shift_letter(letter: str, shift: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))


def caesar_cipher(text: str, shift: int) -> str:
    '''Шифр цезаря'''
    out = ''
    for char in text:
        if char.isalpha():
            char = shift_letter(char, shift)
        out += char
    return out


print(caesar_cipher('leave out all the rest', -1))
print(caesar_cipher('one more light', 3))