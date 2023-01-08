"""
1줄: N, M 학생수, 비교횟수
M줄: a b a가 b보다 크다

방향 주의
a가 b보다 먼저 나와야한다. 단, 판단할 수 없다면 순서는 상관없다.
"""

N, M = map(int, input().split())

arr = [ [] for _ in range(N+1) ]
lst = [0] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    lst[b] += 1

q = []

for i in range(1, N+1):
    if lst[i] == 0:
        q.append(i)

ans = []

while q:
    start = q.pop(0)
    ans.append(start)
    for i in arr[start]:
        lst[i] -= 1
        if lst[i] == 0:
            q.append(i)

print(*ans)