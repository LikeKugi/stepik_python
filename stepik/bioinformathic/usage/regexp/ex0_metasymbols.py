import re

pattern = r' English\?'
string = 'Do you speak English?'

match = re.search(pattern, string)
print(match)

pattern_1 = r'a[a-zA-Z]c'
string_1 = 'adc abc anc agc'
match_1 = re.findall(pattern_1, string_1)
print(match_1)
