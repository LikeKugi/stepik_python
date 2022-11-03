# Выведите строки, содержащие обратный слеш "\".
import sys
import re

sys.stdin = open('backslash_inp.txt')

for line in sys.stdin:
    if re.search(r'\\', line):
        print(line.rstrip())