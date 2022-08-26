w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if t > w-p:
    a = t - (w-p)
    x = a//w
    y = a % w
    if x % 2 == 0:
        p = w-y
    else:
        p = y
else:
    p = p+t

if t > h-q:
    b = t - (h-q)
    x = b//h
    y = b % h
    if x % 2 == 0:
        q = h-y
    else:
        q = y
else:
    q = q+t

print(p,q)