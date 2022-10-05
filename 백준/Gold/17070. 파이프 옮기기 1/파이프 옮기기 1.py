"""
0, 가로일때: 대각선/ 가로
1, 세로일때: 대각선/ 세로
2, 대각선일때: 대각선/ 가로/ 세로
1은 벽
3은 파이프

dfs방식 : 63% 시간초과    (pypy는 통과)
dp 구현
"""

import sys
N = int(input())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)]    # dp[0] 가로이동기록, dp[1] 세로이동기록, dp[2] 대각선이동기록

for i in range(N):          # 첫줄은 가로로만 이동이 가능하다.
    if board[0][i] == 0:
        dp[0][0][i] = 1
    else:
        break

for i in range(1,N):        # 첫줄은 위에서 이미 설정함.
    for j in range(2,N):    # 최초에 가로로 설정했기때문에 세로0과 세로1은 설정할 수 없음.
        # 대각선 먼저 체크를 해보겠습니다.

        # 현재위치가 대각선이라면, 대각선-대각선, 가로-대각선, 세로-대각선의 합이다.
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[2][i][j] = dp[2][i-1][j-1] + dp[1][i-1][j-1] + dp[0][i-1][j-1]

        # 가로 세로를 확인하겠습니다.
        if board[i][j] == 0:
            # 현재위치가 세로일경우, 대각선에서 세로로 오는경우 + 세로에서 세로로 오는경우
            dp[1][i][j] = dp[2][i-1][j] + dp[1][i-1][j]
            # 현재위치가 가로일경우, 대각선에서 가로로 오는경우 + 가로에서 가로로 오는경우
            dp[0][i][j] = dp[2][i][j-1] + dp[0][i][j-1]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])
