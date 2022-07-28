a = int(input())
b = int(input())
c = []
for i in range(a, b+1):
    flag = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        c.append(i)

if not c:
    print(-1)
else:
    print(sum(c))
    print(c[0])