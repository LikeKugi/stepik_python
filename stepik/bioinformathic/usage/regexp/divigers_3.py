#  Вам дана последовательность строк.
# Выведите строки, содержащие двоичную запись числа, кратного 3.
#
# Двоичной записью числа называется его запись в двоичной системе счисления.
import re

lines = ['0',
         '10010',
         '00101',
         '01001',
         'Not a number',
         '1 1',
         '0 0']

for line in lines:
    line_3 = re.sub(r'(1(01*0)*1(11)*0*)+', '0', line.rstrip())
    if re.fullmatch('0+', line_3):
        print(line.rstrip())
    # print(line_3)
