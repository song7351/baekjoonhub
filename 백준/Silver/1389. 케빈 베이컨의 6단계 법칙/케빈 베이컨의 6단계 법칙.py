import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 유저수, 친구관계수
INF = int(1e9)
board = [ [INF]*N for _ in range(N) ]

for _ in range(M):
    a,b = map(int, input().split()) # 양방향
    board[a-1][b-1] = 1 # 서로 친구관계
    board[b-1][a-1] = 1

for i in range(N):
    board[i][i] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            if board[a][k] and board[k][b]:
                board[a][b] = min(board[a][b], board[a][k]+board[k][b])

ans = [0] * N

for i in range(N):
    ans[i] = sum(board[i])
    # print(*board[i])

tmp = min(ans)

for i in range(N):
    if ans[i] == tmp:
        print(i+1)
        break