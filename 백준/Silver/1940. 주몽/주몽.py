"""
https://www.acmicpc.net/problem/1940
n개의 수를 제공한다.
해당 수들을 활용해서 m을 만드는 경우의 수는? (x)
n개의 수중 2개를 골라서 m을 만드는 경우의 수는?
"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().split()))
lst.sort()

s,e = 0, n-1
cnt = 0
while s < e:
    tmp = lst[s] + lst[e]
    if tmp > m:
        e -= 1
    else:
        s += 1
        if tmp == m:
            cnt += 1

print(cnt)