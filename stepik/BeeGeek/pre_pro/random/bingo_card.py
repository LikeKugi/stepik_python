"""
Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.
"""
import numpy as np
from random import randrange as rr
import random as rd

card = np.zeros((5, 5), dtype=np.int_)

# for i in range(5):
#     for j in range(5):
#         # card[i,j] = rr(1,76) if not i ==  j == 2 else 0
#         print(str(card[i, j]).ljust(3), end='')
#     print()

numbers = [*range(1, 76)]

bingo = [[numbers.pop(rr(len(numbers))) if not i == j == 2 else 0 for i in range(5)] for j in range(5)]
for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3),end='')
    print()

#print(bingo)

#
# print(card)
# bingo_card = [[rr(1,100) for j in range(5)] for i in range(5)]
# print(bingo_card)
