"""
첫째 줄에 도시의 개수 n(1 ≤ n ≤ 10,000)이 주어지고
둘째 줄에는 도로의 개수 m(1 ≤ m ≤ 100,000)이 주어진다. 그리고
셋째 줄부터 m+2줄까지 다음과 같은 도로의 정보가 주어진다.

처음에는 도로의 출발 도시의 번호가 주어지고 그 다음에는 도착 도시의 번호,
그리고 마지막에는 이 도로를 지나는데 걸리는 시간이 주어진다.
도로를 지나가는 시간은 10,000보다 작거나 같은 자연수이다.

그리고 m+3째 줄에는 지도를 그리는 사람들이 출발하는 출발 도시와 도착 도시가 주어진다.
모든 도시는 출발 도시로부터 도달이 가능하고, 모든 도시로부터 도착 도시에 도달이 가능하다.
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [ [] for _ in range(n+1) ]
rev_arr = [ [] for _ in range(n+1) ]
lst = [0] * (n+1)

for _ in range(m):
    s,e,t = map(int, input().split())
    arr[s].append((e,t))
    rev_arr[e].append((s,t))
    lst[e] += 1

start, end = map(int, input().split())

q = deque()
q.append(start)
ans = [0] * (n+1)

while q:
    now = q.popleft()
    for x in arr[now]:
        lst[x[0]] -= 1
        ans[x[0]] = max(ans[x[0]], ans[now]+x[1])
        if lst[x[0]] == 0:
            q.append(x[0])

cnt = 0
visited = [0] * (n+1)
q.clear()
q.append(end)
visited[end] = 1

while q:
    now = q.popleft()
    for x in rev_arr[now]:
        if ans[x[0]] + x[1] == ans[now]:
            cnt += 1
            if not visited[x[0]]:
                visited[x[0]] = 1
                q.append(x[0])

print(ans[end])
print(cnt)