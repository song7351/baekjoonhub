"""
1줄: N, K N은 board크기, K는 바이러스 종류(1~K)
N줄: board정보
마지막줄: S, X, Y  -> S초뒤 (x,y)의 바이러스는?

원리:
바이러스는 넘버링이 작은순서부터 증식. 겹치기 불가.
바이러스 번호를 인덱스로 가지는 리스트 생성(virus_lst)
매초마다 순서대로 확산 실행
"""
import sys

N, K = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S,X,Y = map(int, input().split())
X,Y = X-1, Y-1                                  # 입력값이 1~N을 제공하므로 -1씩 진행.

#print(board)
virus_dict = dict()

for i in range(K+1):
    virus_dict[i] = []

for i in range(N):
    for j in range(N):
        if board[i][j]:
            virus_dict[board[i][j]].append([i,j])

#print(virus_dict)

di = [-1,1,0,0]
dj = [0,0,-1,1]
def f(S):
    while S:
        S -= 1
        for i in range(1, K+1):
            new_virus_lst = []
            for x,y in virus_dict[i]:
                for k in range(4):
                    ni = x + di[k]
                    nj = y + dj[k]
                    if 0<= ni < N and 0<= nj < N and board[ni][nj] == 0:
                        board[ni][nj] = i
                        new_virus_lst.append([ni,nj])
                        if ni == X and nj == Y:
                            return
            virus_dict[i] = new_virus_lst
            #print(virus_dict)

f(S)
#print(board)
print(board[X][Y])
