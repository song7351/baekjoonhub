"""
https://www.acmicpc.net/problem/13023

첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

문제에서 요구하는것.
-> 몇번에서 출발하든간에 깊이 5에 도달하는가를 확인해라.
기본골자는 23_연결노드 DFS풀이방식과 비슷한듯 하다.

"""
import sys
sys.setrecursionlimit(10**9)

def dfs(x,depth):
    global ans

    if depth == 4:
        print(1)
        exit(0)

    if visited[x] == 0:
        visited[x] = 1
        for y in graph[x]:
            if visited[y] == 0:
                dfs(y,depth+1)
        # dfs로 깊이 들어가면서 탐색시 주의할 사항. 방문기록을 초기화시켜줘야됨.
        visited[x] = 0

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
# print(graph)
for _ in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

for i in range(N):
    visited = [0] * N
    dfs(i,0)

print(0)