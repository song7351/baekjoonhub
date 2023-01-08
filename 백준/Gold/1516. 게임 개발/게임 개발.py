"""
첫째 줄에 건물의 종류 수 N(1 ≤ N ≤ 500)이 주어진다.
다음 N개의 줄에는 각 건물을 짓는데 걸리는 시간과
그 건물을 짓기 위해 먼저 지어져야 하는 건물들의 번호가 주어진다.
건물의 번호는 1부터 N까지로 하고, 각 줄은 -1로 끝난다고 하자.
각 건물을 짓는데 걸리는 시간은 100,000보다 작거나 같은 자연수이다.
모든 건물을 짓는 것이 가능한 입력만 주어진다.
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = [ [] for _ in range(N+1) ]
lst = [0] * (N+1)
tlst = [0] * (N+1)

for i in range(1,N+1):
    tmp = list(map(int, input().split()))
    tlst[i] = tmp[0]
    n = len(tmp) - 1
    for j in range(1, n):
        arr[tmp[j]].append(i)
        lst[i] += 1

q = deque()

for i in range(1, N+1):
    if lst[i] == 0:
        q.append(i)

ans = tlst[:]
while q:
    start = q.popleft()
    for i in arr[start]:
        lst[i] -= 1
        ans[i] = max(ans[i], tlst[i]+ans[start])
        if lst[i] == 0:
            q.append(i)
            
for x in ans[1:]:
    print(x)