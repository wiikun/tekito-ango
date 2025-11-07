import sys

with open(sys.argv[1],"rb") as file:
    raw = file.read()

lst = bytearray()
old = 0

for i in raw:
    lst.append((i + old) % 256)
    old = i % 256

with open(sys.argv[2],"wb") as file:
    file.write(lst)