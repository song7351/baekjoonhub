import sys

tc = 1

def bfs():
    waited = [(0, 0)]
    while waited:
        x, y = waited.pop(0)
        c = cost[x][y]
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = x + di
            nj = y + dj
            if 0 <= ni < N and 0 <= nj < N:
                c2 = c + board[ni][nj]
                if c2 < cost[ni][nj]:
                    cost[ni][nj] = c2
                    waited.append((ni, nj))

INF = int(1e9)
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cost = [[INF] * N for _ in range(N)]
    cost[0][0] = board[0][0]
    bfs()
    print(f'Problem {tc}: {cost[N - 1][N - 1]}')
    tc += 1