#테스트케이스
C = int(input())

for i in range(C):
    a = list(map(int, input().split()))
    n = a[0]
    avg = (sum(a)-n)/(len(a)-1)
    over = 0
    for j in range(1,len(a)):
        if a[j]>avg:
            over += 1
    ans = over/(len(a)-1)*100
    ans = format(round(ans, 3), ".3f")
    print(ans+"%")

