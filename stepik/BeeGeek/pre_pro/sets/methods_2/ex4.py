# На вход программе подается натуральное число n, а затем n различных натуральных чисел,
# каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
from functools import reduce

digits = [{int(el) for el in input()} for _ in range(int(input()))]
common_digits = sorted(reduce(lambda x, y: x & y, digits))

print(*common_digits)