board = [[0]*102 for _ in range(102)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] += 1

area = 0
for i in range(102):
    for j in range(102):
        if board[i][j] != 0:
            area += 1

print(area)