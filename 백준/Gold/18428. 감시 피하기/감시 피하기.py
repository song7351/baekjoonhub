"""
N*N 크기의 복도
각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시
복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다.
장애물로 막히기 전까지의 학생들은 모두 볼 수 있다

정확히 3개의 장애물을 설치해야 한다
목표: 모든 학생들이 감시에서 벗어남.

X, S, T : 공백, 학생, 선생
"""
import sys
from itertools import combinations
N = int(input())
board = [list(sys.stdin.readline().split()) for _ in range(N)]
X_list = []
T_list = []
S_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            X_list.append([i,j])
        elif board[i][j] == 'T':
            T_list.append([i,j])
        else:
            S_list.append([i,j])

O_list = list(combinations(X_list,3))
di = [-1,1,0,0]
dj = [0,0,-1,1]

ans = 'NO'
for target_O in O_list:
    new_board = [item[:] for item in board]
    for x,y in target_O:
        new_board[x][y] = 'O'

    flag = 0
    pass_cnt = 0
    for tx,ty in T_list:
        cnt = 0
        for k in range(4):
            L = 1
            while True:
                ni = tx + di[k]*L
                nj = ty + dj[k]*L
                if 0<= ni < N and 0<= nj < N:
                    if new_board[ni][nj] == 'S':
                        flag = 1
                        break
                    elif new_board[ni][nj] == 'O':
                        cnt += 1
                        break
                else:
                    cnt += 1
                    break
                L += 1
            if cnt == 4:
                pass_cnt += 1
            if flag == 1:
                break
        if flag == 1:
            break
    if flag == 1:
        continue
    if pass_cnt == len(T_list):
        ans = "YES"
        break

print(ans)