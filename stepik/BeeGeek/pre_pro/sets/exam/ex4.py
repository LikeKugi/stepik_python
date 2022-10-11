"""
Формат входных данных
На вход программе подаются две строки с числами: в первой строке показанные кандидату, а во второй ответы кандидата.

Формат выходных данных
Программа должна вывести YES, если кандидат прошел испытание и его можно брать на работу и NO в противном случае.
"""

original_numbers = {int(number) for number in input().split()}
answer_numbers = {int(number) for number in input().split()}
print(('NO','YES')[original_numbers == answer_numbers])