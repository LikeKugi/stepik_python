"""
Напишите программу для расшифровки секретного слова методом частотного анализа.

Формат входных данных
В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре.
В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

Формат выходных данных
Программа должна вывести дешифрованное слово.

Примечание. Гарантируется, что частоты букв не повторяются.
"""

decrypted_line = input()

encryption = {}
for _ in range(int(input())):
    char, count = input().split(': ')
    encryption[char] = int(count)
decryption = {v: k for k,v in encryption.items()}
print(decryption)
print(encryption)

for char in decrypted_line:
    print(decryption.get(decrypted_line.count(char)),sep='',end='')