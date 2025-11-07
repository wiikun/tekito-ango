import sys

with open(sys.argv[1],"rb") as file:
    raw = file.read()

lst = bytearray()
old = 0

for i in raw:
    dec = (i - old) % 256
    lst.append(dec)
    old = dec

with open(sys.argv[2],"wb") as file:
    file.write(lst)