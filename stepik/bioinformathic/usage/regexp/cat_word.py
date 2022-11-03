# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
import re
import sys
sys.stdin = open('input_cat_word.txt')

for line in sys.stdin:
    if re.search(r'\bcat\b',line):
        print(line)