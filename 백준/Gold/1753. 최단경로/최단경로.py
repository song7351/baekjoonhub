#다익스트라 사용
import sys
import heapq
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
node=[[]for _ in range(V+1)]
distance=[1e10 for _ in range(V+1)]
for i in range(E):
    u,v,w=map(int,input().split())
    node[u].append((v,w))
distance[K]=0

q=[(0,K)]

while q:
    time,point=heapq.heappop(q)
    if distance[point]<time :
        continue
    for newpoint,newtime in node[point]:
        temptime=time+newtime
        if temptime <distance[newpoint]:
            distance[newpoint]=temptime
            heapq.heappush(q,[temptime,newpoint])

for i in range(1,V+1):
    if distance[i]==1e10:
        print('INF')
    else :
        print(distance[i])