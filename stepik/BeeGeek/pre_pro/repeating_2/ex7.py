"""
Формат входных данных
В первой строке подаётся число nn – количество холодильников.
В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры,
в каждой строке от 5 до 100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел.
Если таких холодильников нет, ничего выводить не нужно.
"""

chars = ['a', 'n', 't', 'o', 'n']
texts = list()


def find_list_in_line(line: str, keys: list):
    i = 0
    for key in keys:
        i = line.find(key, i)
        if i < 0:
            return False
    return True


for _ in range(int(input())):
    texts.append(input())

for text in texts:
    if find_list_in_line(text, chars):
        print(texts.index(text) + 1, end=' ')
