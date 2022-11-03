print('cabcd'.find('ab'))
print(str.find.__doc__)

print('-'*10)
s = 'The man in black fled across the desert, and the gunslinger followed'
print(s.startswith(('T', 't', 'z', 'The')))
print('-'*10)
print(s.count('the'))
print(s.lower().count('the'))
print('-'*10)

ss = 'abacaba'
print(ss.find('aba'))
print(ss.rfind('aba'))