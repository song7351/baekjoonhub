#테스트케이스
n = int(input())

for i in range(n):
    a = list(input().split('X'))
    b= len(a)
    d = 0
    for j in range(b):
        c = len(a[j]) * (len(a[j])+1) // 2
        d += c
    print(d)
