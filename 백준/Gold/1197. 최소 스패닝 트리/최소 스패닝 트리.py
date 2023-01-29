"""
최소신장트리
여러개의 경로 노드가 제공된다. 우리는 그중 모든 노드가 연결된 그래프중 최소값을 찾는다.

방법.
1. 가중치가 가장 작은 순서의 연결 노드를 선택
2. 그 2개의 노드가 아직 연결이 안되어 있다면 연결
2-1. 연결(x) == 부모노드가 같은가(find)? 다르다면 연결(union)
"""
import sys
import heapq

input = sys.stdin.readline

n,m = map(int, input().split())

edge = []
parent = [i for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    heapq.heappush(edge, (c,a,b))

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

cnt, ans = 0,0

while cnt < n-1:
    c,a,b = heapq.heappop(edge)
    if find(a) != find(b):
        union(a,b)
        cnt += 1
        ans += c

print(ans)