"""
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

접근
-> 그럼 각 노드의 최고 부모를 가장 작은걸로 판단하면 되는것 아닐까?
-> 이럼 그래프가 너무 많다. 걍 dfs돌립시다.
-> 문제 이해를 잘못함. 그냥 어느 노드점에서 출발했을때 무조건 인접 노드들을 2그룹으로 나눠야함.
-> 모든 노드점에서 퐁당퐁당을 하고 만약 퐁당퐁당에서 실패하면 NO -> 시간초과.
-> 만약 총 4개로 이루어진 서클이라면? -> 어느 포인트에서 잡아도 퐁당퐁당 ok
-> 총 3개로 이루어진 서클이라면? -> 어느 포인트에서 잡아도 fail
"""
import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    # 노드정보, 간선정보
    V, E = map(int, input().split())

    # 그래프 최초
    lst = [ [] for _ in range(V+1) ]
    used = [0] * (V + 1)

    # 이분 그래프
    flag = True

    for _ in range(E):
        u,v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)

    def dfs(x):
        global flag
        q = deque([x])
        if used[x] == 0:
            used[x] = 1
        while q:
            start = q.popleft()
            flag = used[start]

            for i in lst[start]:
                if used[i] == 0:
                    used[i] = -flag
                    q.append(i)
                elif used[i] == flag:
                    print("NO")
                    return False
        return True


    for i in range(1, V+1):
        if used[i] == 0:
            if not dfs(i):
                flag = False
                break

    if flag:
        print("YES")
