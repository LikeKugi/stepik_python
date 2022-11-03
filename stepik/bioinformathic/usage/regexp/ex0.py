import re

print(re.match)  # подходит ли строка под шаблон
print(re.search)  # находит первую подстроку, которая подходит под шаблон
print(re.findall)  # находит все подстроки, которые подходят под шаблон
print(re.sub)  # заменить все вхождения подстрок чем-нибудь другим
print('-' * 10)

pattern = r'abc'
string = 'abcabc'
string_2 = 'accb'
string_3 = 'Abcabc'

match_object = re.match(pattern, string)
print(match_object)

match_object_2 = re.match(pattern, string_2)
print(match_object_2)
print('-' * 10)
print('match - search differences')
print(f'P: {pattern}, str: {string_3}')
match_object_3 = re.match(pattern, string_3)
print(match_object_3)
search_object_3 = re.search(pattern, string_3)
print(search_object_3)
print('-' * 10)

line = 'abc acc aac'
pattern = r'a[abc]c'
print('all inclusions')
print(f'L: {line}, P: {pattern}')
all_inclusions = re.findall(pattern, line)
print(all_inclusions)
print('-' * 10)

print('fix line')
print('all inclusions')
print(f'L: {line}, P: {pattern}, F: {"abc"}')
fixed_typos = re.sub(pattern, 'abc', line)
print(fixed_typos)

