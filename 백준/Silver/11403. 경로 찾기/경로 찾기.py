import sys
input = sys.stdin.readline

N = int(input()) # 크기가 N인 인접행렬이 제시
board = [ [] for _ in range(N) ]
ans = [ [0]*N for _ in range(N) ]

for i in range(N):
    board[i] = list(map(int, input().split()))

for k in range(N):
    for a in range(N):
        for b in range(N):
            if board[a][k] and board[k][b]:
                board[a][b] = 1

for i in range(N):
    print(*board[i])