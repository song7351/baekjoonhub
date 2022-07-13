a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    print(10000+a*1000)
if a == b != c:
    print(1000+a*100)
if a != b == c:
    print(1000+b*100)
if a == c != b:
    print(1000+c*100)
if a != b != c !=a:
    print(max(a,b,c)*100) 