C, R = map(int, input().split())        # 좌석크기
K = int(input())                        # K번 관객
board = [[0]*C for _ in range(R)]

# 시작지점은 0,0 하우상좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

i, j, num = -1, 0, 0
direction = 0
if K > C*R:                 # 좌석보다 더 많다면, 0
    print(0)
else:
    while num < K:
        k = direction % 4
        ni = i + di[k]
        nj = j + dj[k]
        if 0<= ni < R and 0<= nj < C and board[ni][nj] == 0:
            num += 1
            board[ni][nj] = num
            i,j = ni, nj
        else:
            direction += 1

    print(j+1, i+1)