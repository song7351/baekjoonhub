import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 노드개수
M = int(input()) # 간선개수
lst = [[] for _ in range(N+1)]
dis = [int(1e9)] * (N+1)

for _ in range(M):
    u,v,w = map(int, input().split())
    lst[u].append((v,w))

s,e = map(int, input().split())

q = [(s,0)]
dis[s] = 0

while q:
    n, v = heapq.heappop(q)

    if dis[n] >= v:
        for node, V in lst[n]:
            tmp = V + v
            if tmp < dis[node]:
                dis[node] = tmp
                heapq.heappush(q, (node, tmp))

print(dis[e])