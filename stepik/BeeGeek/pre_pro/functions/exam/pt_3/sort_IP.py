"""
Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания
в соответствии с десятичным представлением.
"""

adresses = [input() for _ in range(int(input()))]


def tenth_imagine(adress):
    adress = list(map(int, adress.split('.')))
    return sum([(256 ** (3 - i)) * j for i, j in enumerate(adress)])



print(*sorted(adresses,key=tenth_imagine),sep='\n')