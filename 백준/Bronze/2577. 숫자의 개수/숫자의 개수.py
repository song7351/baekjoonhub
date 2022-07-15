a = int(input())
b = int(input())
c = int(input())
d = a*b*c
e = len(str(d))
list = [ 0 for i in range(10)]

for i in range(e):
    f = d%10
    d = int(d/10)
    list[f] += 1

for i in range(10):
    print(list[i])
