from collections import deque

n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1]*m for _ in range(n)]

x,y = 0,0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            x,y = i,j
            answer[i][j] = 0
        if maps[i][j] == 0:
            answer[i][j] = 0

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        i,j = q.popleft()
        v = answer[i][j]
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dx,dy = i+di, j+dj
            if 0<= dx < n and 0<= dy < m:
                if answer[dx][dy] == -1 and maps[dx][dy] == 1:
                    answer[dx][dy] = v+1
                    q.append((dx,dy))
bfs(x,y)

for x in answer:
    print(*x)