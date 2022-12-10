"""
https://www.acmicpc.net/problem/11724
정점은 1~N
연결요소의 개수를 구해라

내가 이해한것.
-> 최종 부모노드의 개수는?
"""
import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


# N: 정점의개수, M: 노드의개수
N, M = list(map(int, input().split()))

# 부모노드를 본인으로 초기화
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

for _ in range(M):
    s, e = list(map(int, input().split()))
    parent_s = find(s)
    parent_e = find(e)
    if parent_s < parent_e:
        parent[parent_e] = parent_s
    else:
        parent[parent_s] = parent_e

# 전체 싹다 한번 find실행
for i in range(1, N+1):
    tmp = find(parent[i])
    if tmp != parent[i]:
        parent[i] = tmp

# print(parent)
# 기록남기기
used = [0] * (N + 1)
for i in range(N + 1):
    used[parent[i]] = 1

ans = 0
# print(used)
for i in range(1, N + 1):
    if used[i] == 1:
        ans += 1

print(ans)
