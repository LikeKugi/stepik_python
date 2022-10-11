"""
Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:
"""
d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

number = input()
line = ''
for digit in number:
    print(d.get(int(digit)),end=' ')