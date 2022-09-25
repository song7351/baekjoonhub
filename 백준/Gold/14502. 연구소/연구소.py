"""
연구소는 크기가 N×M
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
 0은 빈 칸, 1은 벽, 2는 바이러스
 
 원리
 1. 모든 빈칸의 좌표를 구해서 3개인 조합을 만든다.
 2. 각조합을 순서대로 꺼내서 벽을 세운다.
    2-1. 바이러스 좌표에서 상하좌우로 바이러스를 확산시킨다.
        2-2. 전체배열에서 빈칸을 카운트한다.
 3. 카운트한 안전구역의 리스트(ans)중 가장 큰 값을 출력한다.
"""
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
zero_lst = []
virus_lst = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zero_lst.append([i,j])
        elif board[i][j] == 2:
            virus_lst.append([i,j])

select_zero_lst = list(combinations(zero_lst,3))
#print(select_zero_lst)

di = [-1,1,0,0]
dj = [0,0,-1,1]

def change_virus(N,M):
    for i,j in virus_lst:
        waited = [[i,j]]
        while waited:
            tmp = waited.pop(0)
            x,y = tmp[0], tmp[1]
            for k in range(4):
                ni = x + di[k]
                nj = y + dj[k]
                if 0<= ni < N and 0<= nj<M and new_board[ni][nj] == 0:
                    new_board[ni][nj] = 2
                    waited.append([ni,nj])

ans = []
for i in select_zero_lst:
    new_board = [item[:] for item in board]
    for x,y in i:
        new_board[x][y] = 1

    change_virus(N,M)

    cnt = 0
    for x in range(N):
        for y in range(M):
            if new_board[x][y] == 0:
                cnt += 1
    ans.append(cnt)

print(max(ans))