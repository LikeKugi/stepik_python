"""
Формат входных данных
На вход программе подается строка, содержащая три целых неотрицательных числа,
компоненты R, G и B начального цвета,  разделенные символом пробела.

Формат выходных данных
Программа должна вывести три компонента R, G и B противоположного цвета, разделенные символом пробела.
"""


print(*map(lambda x:255-int(x),input().split()))