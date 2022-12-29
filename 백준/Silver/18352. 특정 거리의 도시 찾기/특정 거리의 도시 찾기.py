"""
1줄: N M K X
N 도시의 개수
M 도로의 개수
K 거리 정보
X 출발 도시 번호

M줄: A B (단방향)

출력: X도시에서 최단거리 K만큼 이동가능한 도시를 오름차순으로 출력(없다면 -1)
"""
import sys
input = sys.stdin.readline

def bfs(k, x):
    q = [(k,x)]
    while q:
        cnt, start = q.pop(0)
        used[start] = 1
        if cnt == 0:
            ans.append(start)
        else:
            for i in lst[start]:
                if used[i] == 0 and cnt-1 >= 0:
                    q.append((cnt-1, i))
                    used[i] = 1

N,M,K,X = map(int, input().split())

lst = [ [] for _ in range(N+1) ]
used = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)

ans = []
bfs(K, X)
ans.sort()

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)