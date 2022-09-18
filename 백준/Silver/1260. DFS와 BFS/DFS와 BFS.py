"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
"""
import sys
sys.setrecursionlimit(10**5)

def dfs(v):
    print(v, end=' ')    #  v 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 w
            dfs(w)

def bfs(v,idx):
    if v not in wait:
        wait.append(v)
    for w in adjList[v]:
        if w not in wait:
            wait.append(w)
    print(wait[idx], end=" ")
    idx += 1
    if idx < len(wait):
        bfs(wait[idx],idx)


N, M, V = map(int, input().split())
adjList = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

for i in range(N+1):
    adjList[i].sort()

visited = [0] * (N+1)
dfs(V)
print()
wait = []
bfs(V,0)

