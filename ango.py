import sys
import getpass
import base64

with open(sys.argv[1],"rb") as file:
    raw = file.read()

lst = bytearray()
old = 0

key = bytearray(getpass.getpass(prompt="input key:").encode("utf-8"))

klen = len(key)

keyi = 0
loter2 = 0
loter3 = 0

for i in raw:
    lst.append((i + old + key[keyi]) % 256)
    key[keyi] = abs(key[keyi] + (old + (key[keyi] % 5) + 1 + loter2 - loter3) * (-1) if key[keyi] % 5 % 2 == 0 else (1)) % 256
    keyi = keyi + 1 if keyi + 1 < klen else 0
    old = i
    loter2 = i % 4
    loter3 = i % 5

with open(sys.argv[2],"wb") as file:
    file.write(base64.b64encode(lst))