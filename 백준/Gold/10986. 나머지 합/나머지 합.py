"""
https://www.acmicpc.net/problem/10986

"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = [0]*m
tmp = 0
for i in range(n):
    tmp += lst[i]
    lst2[tmp%m] += 1

ans = lst2[0]
for i in range(m):
    if lst2[i] >= 2:
        ans += lst2[i] * (lst2[i]-1) // 2

print(ans)