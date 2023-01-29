"""
플로이드 워셜
-> 최단경로를 구하는 알고리즘

방법.
1. 기본적으로 INF 값인 그래프를 만든다.
2. 자기 자신으로 가는 값은 항상 0이다.
3. a->b 를 가는것과 a->k + k-> b 값중 작은 값을 설정한다.

"""
import sys
input = sys.stdin.readline

n = int(input()) # 도시개수
m = int(input()) # 버스개수

# 1. 기본적으로 INF 값인 그래프를 만든다.
INF = int(1e9)
board = [ [INF] * (n+1) for _ in range(n+1) ]

for _ in range(m):
    a,b,c = map(int, input().split())
    if c < board[a][b]:
        # 문제에서는 같은 노선 다른값이 제시될 수 있다.
        board[a][b] = c

# 2. 자기 자신으로 가는 값은 항상 0이다.
for i in range(1, n+1):
    board[i][i] = 0

# 3. a->b 를 가는것과 a->k + k-> b 값중 작은 값을 설정한다.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == INF:
            print(0, end=' ')
        else:
            print(board[i][j], end=' ')
    print()