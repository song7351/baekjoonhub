"""
https://www.acmicpc.net/problem/12891
문자열길이 n
임의 문자열길이 m
문자열~
{'A','C','G','T'}의 최소개수
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = list(input())
lock = list(map(int, input().split()))
lock2 = [0]*91
lock2[65], lock2[67], lock2[71], lock2[84] = lock[0], lock[1], lock[2], lock[3]

cnt = 0
for i in range(m):
    lock2[ord(lst[i])] -= 1

for x in [65,67,71,84]:
    if lock2[x] > 0:
        break
else:
    cnt += 1

s = 0
for i in range(m,n):
    lock2[ord(lst[i])] -= 1
    lock2[ord(lst[s])] += 1
    s += 1
    for x in [65, 67, 71, 84]:
        if lock2[x] > 0:
            break
    else:
        cnt += 1

print(cnt)
