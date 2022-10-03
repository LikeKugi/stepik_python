print(bin(10))
print(bin(128))
print(bin(150))
print(bin(18765))

print(oct(10))
print(oct(128))
print(oct(150))
print(oct(18765))

print(hex(10))
print(hex(128))
print(hex(150))
print(hex(18765))

num = 127

bin_num = bin(num)  # 0b1111111
oct_num = oct(num)  # 0o177
hex_num = hex(num)  # 0x7f

print(bin_num[2:])  # 1111111
print(oct_num[2:])  # 177
print(hex_num[2:])  # 7f