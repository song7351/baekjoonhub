def bingo(arr):
    cnt = 0
    for i in range(5):
        r_sum = 0
        c_sum = 0
        for j in range(5):
            r_sum += arr[i][j]
            c_sum += arr[j][i]
        if r_sum == 0:
            cnt += 1
        if c_sum == 0:
            cnt += 1
        if cnt >= 3:
            return "bingo"

    if arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4] == 0:
        cnt += 1
    if arr[0][4] + arr[1][3] + arr[2][2] + arr[3][1] + arr[4][0] == 0:
        cnt += 1
    if cnt >= 3:
        return "bingo"



N = 5
board = [list(map(int, input().split())) for _ in range(N)]
check = []
for _ in range(N):
    check += list(map(int, input().split()))

for i in range(25):
    # 찾아서 x칸 칠하기
    for j in range(N):
        for k in range(N):
            if board[j][k] == check[i]:
                board[j][k] = 0
    # 3빙고의 최소 칸은 12칸
    if i > 10:
        ans = bingo(board)
        if ans == "bingo":
            print(i+1)
            break