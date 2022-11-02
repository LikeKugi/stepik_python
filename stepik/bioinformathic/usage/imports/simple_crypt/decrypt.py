from simplecrypt import decrypt
with open("encrypted.bin", "rb") as inf_bin:
    encrypted = inf_bin.read()

with open('passwords.txt') as inf:
    passwords = map(str.rstrip, inf.readlines())

variants = []

for password in passwords:
    try:
        plaintext = (decrypt(password,encrypted).decode('utf-8'))
        print(plaintext)
    except:
        continue


print(*variants,sep='\n')