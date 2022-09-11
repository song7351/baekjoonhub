N = int(input())
board = [[0]* N for _ in range(N)]
K = int(input())
for i in range(K):
    x,y = map(int,input().split())  # 사과
    board[x-1][y-1] = 1
L = int(input())

direction = []
for i in range(L):
    x,y = input().split()
    x = int(x)
    direction.append([x,y]) # x초에는 y방향으로 꺽어라

snake = [[0,0]]     # 꼬리 ~ 머리
board[0][0] = 3     # 뱀위치는 3
tail = snake[0]     # 꼬리위치
head = snake[-1]    # 머리위치

di = [-1,0,1,0]     # 상 좌 하 우
dj = [0,-1,0,1]
d = 3               # 현재 방향

cnt = 0             # 초
idx= 0
while True:
    tail = snake[0]  # 꼬리위치
    head = snake[-1]  # 머리위치
    cnt += 1
    ni = head[0] + di[d]
    nj = head[1] + dj[d]

    if 0<= ni < N and 0<= nj <N:
        snake.append([ni,nj])
        if board[ni][nj] == 0:              # 사과가 없다면
            board[tail[0]][tail[1]] = 0     # 꼬리를 땡겨라
            snake.pop(0)
        elif board[ni][nj] == 3:            # 몸통이랑 접촉하면 끝
            break
        board[ni][nj] = 3                   # 사과 또는 아무것도 없다면 진행
    else:
        break

    if idx < L:
        if cnt == direction[idx][0]:
            if direction[idx][1] == 'L':
                d = (d+1)%4
            else:
                d = (d-1)%4
            idx += 1

print(cnt)