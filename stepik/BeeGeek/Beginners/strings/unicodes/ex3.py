"""
Caesars Cipher
"""

moved = int(input())
line = input()
for el in line:
    num = ord(el)-moved
    if num<97:
        num = 122 - (96-num)
    print(chr(num),end='')