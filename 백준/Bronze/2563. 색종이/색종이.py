"""
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지

 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이

여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램
"""

N = int(input())

board = [[0]*100 for _ in range(100)]       # 가로세로 크기가 100인 도화지

for _ in range(N):
    x,y = map(int, input().split())         # 시작 좌표

    for i in range(x, x+10):                # 가로세로 크기는 10이다.
        for j in range(y, y+10):
            board[i][j] += 1

area = 0
for i in range(100):
    for j in range(100):
        if board[i][j] != 0:
            area += 1

print(area)