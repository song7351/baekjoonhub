"""
https://www.acmicpc.net/problem/2750
오름차순으로 정렬하세요.
"""
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
for x in lst:
    print(x)