"""
최소힙을 유지시킨다.
"""
from heapq import heappush,heappop

N = int(input())
heap = []

for _ in range(N):
    heappush(heap, int(input()))

ans = 0
while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    ans += (a+b)
    heappush(heap, a+b)

print(ans)
