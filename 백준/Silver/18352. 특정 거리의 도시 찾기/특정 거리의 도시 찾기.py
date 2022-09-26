"""
1번부터 N번까지의 도시
M개의 단방향 도로
목적: 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
"""
import sys
input = sys.stdin.readline

def bfs(doro, p, visited):
    global K
    waited = [[p,0]]
    visited[p] = 1
    cnt = 0

    while waited:
        lst = waited.pop(0)
        c = lst[0]
        cnt = lst[1]
        if cnt == K:
            ans.append(c)
        elif cnt < K:
            for i in doro[c]:
                if not visited[i]:
                    waited.append([i,cnt+1])
                    visited[i] = 1

N, M, K, X = map(int,input().split())
doro = [[] for _ in range(N+1)]

for i in range(M):
    s,e = map(int,input().split())
    doro[s].append(e)

ans = []
visited = [0] * (N+1)
waited = [[X,0]]
#시작점 X, 현재이동횟수
bfs(doro, X, visited)
if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
