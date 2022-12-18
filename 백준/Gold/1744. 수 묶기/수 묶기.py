"""
https://www.acmicpc.net/problem/1744
순서상관없이 2개의 수를 묶을 수 있다.(안해도됨)

2이상 양수

1은 무조건 더한다.

0은 마이너스랑 곱하거나 더한다.

마이너스는 마이너스와 곱하거나 더한다.
그냥 통짜로 계산하면 틀림 -> 2이산이 짝수개라면 문제가 없지만, 홀수개라면 1개는 무조건 더해야됨.
"""
N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
ans = 0
minus = 0
plus = 0
flag = 0

for i in range(N):
    num = lst[i]
    if num < 0:
        if minus == 0:
            minus = num
        else:
            ans += minus*num
            minus = 0

    elif num == 0:
        minus = 0

    elif num == 1:
        ans += 1 + minus
        minus = 0

    elif num > 1:
        if flag == 0:
            flag = 1
            if (N-i) % 2 != 0:
                ans += num
            else:
                plus = num
        else:
            if plus == 0:
                plus = num
            else:
                ans += plus*num
                plus = 0

print(ans+plus+minus)