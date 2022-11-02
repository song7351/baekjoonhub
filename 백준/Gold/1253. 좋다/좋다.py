"""
https://www.acmicpc.net/problem/1253

n개의 수중에 2개를 뽑아 다른 한개를 만들 수 있는 경우의 수는?

"""

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

cnt = 0
for i in range(n):
    s,e, target = 0, n-1, lst[i]
    if s == i:
        s += 1
    if e == i:
        e -= 1

    while s<e:
        tmp = lst[s] + lst[e]
        if tmp > target:
            e -= 1
        else:
            s += 1
            if tmp == target:
                cnt += 1
                break
        if s == i:
            s += 1
        if e == i:
            e -= 1

print(cnt)