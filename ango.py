import sys

with open(sys.argv[1],"rb") as file:
    raw = file.read()

lst = bytearray()
old = 0

if len(sys.argv) < 4:
    print("key not found")
    sys.exit(1)

key = 0
kold = 0

kbyte = sys.argv[3].encode("utf-8")

for i in kbyte:
    key += (i + kold)
    kold = i

key %= 256

for i in raw:
    lst.append((i + old + key) % 256)
    old = i % 256

with open(sys.argv[2],"wb") as file:
    file.write(lst)