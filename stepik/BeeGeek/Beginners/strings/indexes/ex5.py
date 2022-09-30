"""
На вход программе подается натуральное число, записанное в десятичной системе счисления.
Напишите программу, которая переводит данное число в двоичную систему счисления.
"""

number = int(input())
binary_number=''
while number >0:
    binary_number+=str(number%2)
    number//=2
print(binary_number[::-1])