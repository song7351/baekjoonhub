"""

sort = 메모리 초과
카운트 정렬
"""
import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 10001
for _ in range(n):
    idx = int(input())
    lst[idx] += 1

for i in range(1, 10001):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)