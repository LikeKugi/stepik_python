"""
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
"""
key = input()
value = input()
decode = input()
encode = input()
dictionary = dict(zip(key, value))
inverted = dict(zip(value,key))
out_decode, out_encode = '', ''
for char in decode:
    out_decode += dictionary[char]
print(out_decode)
for char in encode:
    out_encode += inverted[char]
print(out_encode)
