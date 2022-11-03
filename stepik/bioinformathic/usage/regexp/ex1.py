# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
import re
import sys
sys.stdin = open('input_cat.txt')


for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)