"""
0, 가로일때: 대각선/ 가로
1, 세로일때: 대각선/ 세로
2, 대각선일때: 대각선/ 가로/ 세로
1은 벽
3은 파이프

dfs방식 : 63% 시간초과
"""
def search(i,j,d):
    global ans
    if i == N-1 and j == N-1:
        ans += 1
        return
    board[i][j] = 3

    if d == 0:
        if 0<= i <N and 0<= j+1<N:
            if board[i][j+1] != 1:
                search(i,j+1,0)

        if 0<= i+1 <N and 0<= j+1<N:
            if board[i+1][j+1] != 1 and board[i+1][j] != 1 and board[i][j+1] != 1:
                search(i+1,j+1,2)
    elif d == 1:
        if 0 <= i+1 < N and 0 <= j < N:
            if board[i+1][j] != 1:
                search(i+1, j, 1)

        if 0 <= i + 1 < N and 0 <= j + 1 < N:
            if board[i+1][j+1] != 1 and board[i+1][j] != 1 and board[i][j+1] != 1:
                search(i + 1, j + 1, 2)
        pass
    elif d == 2:
        if 0<= i <N and 0<= j+1<N:
            if board[i][j + 1] != 1:
                search(i, j + 1, 0)

        if 0 <= i+1 < N and 0 <= j < N:
            if board[i+1][j] != 1:
                search(i + 1, j, 1)

        if 0 <= i + 1 < N and 0 <= j + 1 < N:
            if board[i+1][j+1] != 1 and board[i+1][j] != 1 and board[i][j+1] != 1:
                search(i + 1, j + 1, 2)

import sys
N = int(input())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
board[0][0], board[0][1] = 3,3
ans = 0
search(0,1,0)
print(ans)
