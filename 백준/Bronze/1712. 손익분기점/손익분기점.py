a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if b >= c:
    ans = -1
else:
    ans = a//(c-b) + 1

print(ans)
    
