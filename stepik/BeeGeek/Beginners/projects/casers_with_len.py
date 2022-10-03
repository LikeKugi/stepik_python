punctuations = '\!\"\#\$\%\&\'\(\)\*\+\,\ \-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~'

upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt_line(text, lang, key=0):
    words = text.split()
    encrypted_text = ''
    for word in words:
        chars = [el for el in word if el.isalpha()]
        key = len(chars)
        for char in word:
            pos = (lang.find(char.upper()) + key) % len(lang)
            if char.isupper():
                encrypted_text += lang[pos]
            elif char.islower():
                encrypted_text += lang[pos].lower()
            else:
                encrypted_text += char
        encrypted_text += ' '
    print(encrypted_text)
    return


text = input()
encrypt_line(text,upper_eng_alphabet)
