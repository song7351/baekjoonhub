n = int(input())

a = 0
b = 0
min = n
for i in range(n):
    for j in range(n):
        c = 5*i + 3*j
        if c == n and (i+j) <= min:
            min = i+j

if min == n:
    print(-1)
else:
    print(min)
            