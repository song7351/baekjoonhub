"""
https://www.acmicpc.net/problem/2018
N을 만드는
연속된 숫자의 합 <<--- 해당 경우의 수를 구하세요.
"""
n = int(input())
s = 1
tmp, cnt = 0, 0

for i in range(s,n+1):
    if tmp + i <= n:
        tmp += i
        if tmp == n:
            cnt += 1
            tmp -= s
            s += 1
    else:
        while tmp + i > n:
            tmp -= s
            s += 1
        tmp += i
        if tmp == n:
            cnt += 1
            tmp -= s
            s += 1

print(cnt)