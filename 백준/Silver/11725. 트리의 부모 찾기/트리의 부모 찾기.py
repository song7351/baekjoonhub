"""
루트 없는 트리가 주어진다.
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(n):
    #print(ans)
    if test[n] != 1:
        test[n] = 1
        for i in range(len(lst[n])):
            if not ans[lst[n][i]]:
                ans[lst[n][i]] = n
                dfs(lst[n][i])

N = int(input())
lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

#print(lst)
ans = [0] * (N+1)
test = [0] * (N+1)
dfs(1)
#print(ans)

for i in range(2,N+1):
    print(ans[i])