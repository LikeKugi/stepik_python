upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def ask_user():
    print('Wanna encrypt(1) or decrypt(2)?')
    line = input()
    if line == '1':
        flag_crypt = True  # Encrypt
    elif line == '2':
        flag_crypt = False  # Decrypt
    else:
        return
    while True:
        line = input('1 - rus or 2 - en:')
        if line == '1':
            flag_lang = upper_rus_alphabet
            max_key = len(upper_rus_alphabet)
            break
        if line == '2':
            flag_lang = upper_eng_alphabet
            max_key = len(upper_eng_alphabet)
            break
    while True:
        key = int(input('enter key: '))
        if 0<key<max_key:
            break
    line = input('enter line: ')
    start_mess(flag_crypt, flag_lang, line, key)


def start_mess(crypt, fl_lang, text, key):
    kek = input('loop decode: ')
    if kek == '1':
        for i in range(26):
            decrypt_line(text, fl_lang, i)
    if crypt:
        encrypt_line(text, fl_lang, key)
    else:
        decrypt_line(text, fl_lang, key)


def encrypt_line(text, lang, key=0):
    encrypted_text = ''
    for char in text:
        pos = (lang.find(char.upper()) + key) % len(lang)
        if char.isupper():
            encrypted_text += lang[pos]
        elif char.islower():
            encrypted_text += lang[pos].lower()
        else:
            encrypted_text += char
    print(encrypted_text)
    return


def decrypt_line(line, lang, key=0):
    decrypted_text = ''
    for char in line:
        pos = (lang.find(char.upper()) - key) % len(lang)
        if char.isupper():
            decrypted_text += lang[pos]
        elif char.islower():
            decrypted_text += lang[pos].lower()
        else:
            decrypted_text += char
    print(decrypted_text)
    return

if __name__ == '__main__':
    ask_user()