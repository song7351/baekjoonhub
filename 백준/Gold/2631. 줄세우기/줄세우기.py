"""
위치를 옮기는 아이들의 수를 최소로 하려고 한다.
"""
n = int(input())

lst = [int(input()) for _ in range(n)]

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))