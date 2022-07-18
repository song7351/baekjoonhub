a = input()
a = a.lower()
a = list(a)
b = [0]*26
c = len(a)
for i in range(c):
    d = ord(a[i])-97
    b[d] += 1

e = max(b)
n = 0

for i in range(26):
    if b[i] == e:
        n += 1
        if n == 2:
            print("?")
            break

if n != 2:
    f = b.index(e)+97
    g = chr(f)
    h = g.upper()
    print(h)