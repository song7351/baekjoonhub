"""
t이후 상황을 보고싶다.
"""
n,m,t = map(int, input().split())

board = [list(input()) for _ in range(n)]

if t == 1:
    for lst in board:
        print(''.join(lst))
    exit(0)
if t == 2:
    board = [['O']*m for _ in range(n)]
    for lst in board:
        print(''.join(lst))
    exit(0)

for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            board[i][j] = 3
        elif board[i][j] == 'O':
            board[i][j] = 1
t -= 2

def refill():
    for i in range(n):
        for j in range(m):
            if board[i][j] <= 0:
                board[i][j] = 3

def timer():
    for i in range(n):
        for j in range(m):
            board[i][j] -= 1
def boom():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    dx = i + di
                    dy = j + dj
                    if 0<= dx < n and 0<= dy < m and board[dx][dy] != 0:
                        board[dx][dy] = -1

flag = True
while t > 0:
    t -= 1
    timer()
    if flag:
        boom()
        flag = False
    else:
        refill()
        flag = True

for i in range(n):
    for j in range(m):
        if board[i][j] >= 1:
            board[i][j] = 'O'
        else:
            board[i][j] = '.'

for lst in board:
    print(''.join(lst))