def rotate(k):
    n = len(k)
    KEY = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            KEY[j][n-i-1] = k[i][j]
    return KEY

def check(key,board,lock):
    m = len(key)
    n = len(lock)
    test = [item[:] for item in board]
    x,y = 0,0
    for i in range(3*n-m):
        for j in range(3*n-m):
            cnt = 0
            x = 0
            for k in range(i,i+m):
                y = 0
                for l in range(j,j+m):
                    test[k][l] += key[x][y]
                    y += 1
                x += 1

            for k in range(n,2*n):
                for l in range(n,2*n):
                    if test[k][l] == 1:
                        cnt += 1

            if cnt == n*n:
                return True
            else:
                test = [item[:] for item in board]
    return False

def solution(key, lock):
    N = len(lock)
    board = [[0]*(3*N) for _ in range(3*N)]
    answer = False
    x,y = 0,0
    for i in range(N, 2*N):
        y = 0
        for j in range(N, 2*N):
            board[i][j] = lock[x][y]
            y += 1
        x += 1
    for _ in range(4):
        # 키회전
        key = rotate(key)
        # 회전한키 확인
        answer = check(key, board, lock)
        if answer:
            return answer
    return answer