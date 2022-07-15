list = [ 0 for i in range(42)]
for i in range(10):
    a = int(input())
    a = a%42
    list[a] += 1

b = 0
for i in range(42):
    if list[i] != 0:
        b += 1

print(b) 