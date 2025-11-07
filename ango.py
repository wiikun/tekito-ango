import sys
import getpass

with open(sys.argv[1],"rb") as file:
    raw = file.read()

lst = bytearray()
old = 0

key = bytearray(getpass.getpass(prompt="input key:").encode("utf-8"))

klen = len(key)

keyi = 0

for i in raw:
    lst.append((i + old + key[keyi]) % 256)
    old = i
    key[keyi] = abs(key[keyi] + ((key[keyi] % 5) + 1) * (-1) if key[keyi] % 5 % 2 == 0 else (1)) % 256
    keyi = keyi + 1 if keyi + 1 < klen else 0

with open(sys.argv[2],"wb") as file:
    file.write(lst)