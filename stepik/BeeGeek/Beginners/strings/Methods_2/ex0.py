s = 'aabbAAccDDaa'
s = s.lower()
print(s.count('a'))

s = 'www.stepik.org'
print(s.startswith('www'))

s = 'www.stepik.org'
print(s.endswith('.ru'))

s = 'I learn Python language. Python - awesome!'
print(s.find('Python'))

s = '     I learn Python language               '
print(s.strip())

s = 'abcdababa'
print(s.replace('ab', '123'))