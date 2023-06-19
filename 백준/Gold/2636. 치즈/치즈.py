"""
0으로 시작해서 근접한 1들을 모두 다 0으로 바꿔줄 예정이다.
"""
from collections import deque

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

b_cnt = 0
f_cnt = 0
t = 0

while True:
    f_cnt = 0
    t += 1
    q = deque([(0,0)])
    board2 = board.copy()
    board3 = [[False]*m for _ in range(n)]
    lst = []
    while q:
        x,y = q.popleft()
        board3[x][y] = True
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            di = x + dx
            dj = y + dy
            if 0<= di < n and 0<= dj < m and board3[di][dj] == False:
                board3[di][dj] = True
                if board[di][dj] == 0:
                    q.append((di,dj))
                elif board[di][dj] == 1:
                    board2[di][dj] = 0
                    f_cnt += 1
                    lst.append((di,dj))
    # print(lst)
    if f_cnt == 0:
        break
    board = board2.copy()
    b_cnt = f_cnt


print(t-1)
print(b_cnt)