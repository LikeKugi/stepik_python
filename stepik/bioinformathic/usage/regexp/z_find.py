# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
import sys
import re

sys.stdin = open('input_z.txt')

for line in sys.stdin:
    if re.search(r'z.{3}z',line):
        print(line.rstrip())