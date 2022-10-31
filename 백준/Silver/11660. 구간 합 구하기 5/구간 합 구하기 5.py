"""
https://www.acmicpc.net/problem/11660
2차원 구간합구하기
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sum_board = [[0] for _ in range(n)]
for i in range(n):
    num = 0
    for j in range(n):
        num += board[i][j]
        sum_board[i].append(num)
#print(sum_board)
for i in range(1,n):
    for j in range(n+1):
        sum_board[i][j] += sum_board[i-1][j]
sum_board = [[0]*(n+1)] + sum_board
#print(sum_board)
for _ in range(m):
    ax,ay,bx,by = map(int, input().split())
    ans = sum_board[bx][by] - sum_board[ax-1][by] - sum_board[bx][ay-1] + sum_board[ax-1][ay-1]
    print(ans)

