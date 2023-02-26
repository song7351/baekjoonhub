"""
최소공통조상: 2개의 노드의 최소공통조상을 찾는다.
두개가 같은 깊이일때 2개의 부모노드가 같다면? -> 최소공통조상
두개가 같은 깊이인데도 부모노드가 다르다? -> 각자의 부모노드로 올라간다.

우선해야될것.
부모노드설정과 깊이설정 how? dfs, bfs
"""
import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

# 양방향 노드
for i in range(N-1):
    s,e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (N+1)
parent = [0] * (N+1)
visited = [0] * (N+1)

def bfs(node):
    lst = [node]
    visited[node] = 1
    level = 1
    now_size = 1
    count = 0
    while lst:
        now_node = lst.pop(0)
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = 1
                lst.append(next)
                parent[next] = now_node
                depth[next] = level
        count += 1
        if count == now_size:
            count = 0
            now_size = len(lst)
            level += 1

# 루트는 1이다.
bfs(1)

def find(a,b):
    #  만약 a가 깊이가 더 얕으면 b를 한단계 높여야 한다.
    if depth[a] < depth[b]:
        a,b = b,a

    # 어떻게? 무조건 깊이가 더 얕은쪽은 a로 설정한다.
    # 두개의 깊이가 같을때까지 한쪽을 끌어올린다.
    while depth[a] != depth[b]:
        a = parent[a]

    # 그렇게해서 a랑 b가 다르면? 둘다 깊이를 끌어올린다.
    # 그래서 두개가 같아지면? return한다.
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

M = int(input())

for _ in range(M):
    a,b = map(int, input().split())
    print(find(a,b))