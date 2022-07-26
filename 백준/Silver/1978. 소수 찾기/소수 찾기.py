a = int(input())
b = input()

b= list(map(int, b.split()))
cnt = 0
for i in range(a):
    c = 1
    flag = 0
    while c < b[i]:
        if c != 1 and b[i] % c == 0:
            flag = 1
        c += 1
    if b[i] != 1 and flag == 0:
        cnt += 1
print(cnt)

