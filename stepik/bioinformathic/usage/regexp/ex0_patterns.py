import re

pattern = r'a[bc]c'
string = 'abc'
string2 = 'acc'

match_object = re.match(pattern,string)
print(match_object)
match_object = re.match(pattern,string2)
print(match_object)