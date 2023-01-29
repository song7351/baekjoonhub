import sys
from queue import PriorityQueue

input = sys.stdin.readline
n,m = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i
    
for i in range(m):
    s,e,w = map(int, input().split())
    pq.put((w,s,e))
    
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

cnt = 0
ans = 0

while cnt < n-1:
    w,s,e = pq.get()
    if find(s) != find(e):
        union(s,e)
        ans += w
        cnt += 1
        
print(ans)