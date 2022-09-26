"""
N×N크기의 땅
1줄: N,L,R
N줄: 국가,인구정보

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
"""
import sys
sys.setrecursionlimit(10**5)

N,L,R = map(int,input().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
check_board = [[0]*N for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
ans = 0

def dfs(i,j,num):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<= ni < N and 0<= nj < N:
            if L <= abs(board[ni][nj] - board[i][j]) <= R:
                if check_board[ni][nj] == 0:
                    check_board[ni][nj] = num
                    dfs(ni,nj,num)

while True:
    check_board = [[0] * N for _ in range(N)]
    num = 1
    for i in range(N):
        for j in range(N):
            if check_board[i][j] == 0:
                check_board[i][j] = num
                dfs(i,j, num)
                num += 1
    if num == (N**2)+1:
        #print(check_board)
        break
    else:
        ans += 1

    calcul_list = [[0,0] for _ in range(num+1)]
    for i in range(N):
        for j in range(N):
            calcul_list[check_board[i][j]][0] += board[i][j]
            calcul_list[check_board[i][j]][1] += 1

    for i in range(N):
        for j in range(N):
            board[i][j] = calcul_list[check_board[i][j]][0]//calcul_list[check_board[i][j]][1]

print(ans)