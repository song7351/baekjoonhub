from collections import deque


def solution(board):
    answer = 0
    board = [list(i) for i in board]
    n, m = len(board), len(board[0])

    def f1(n, m):
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'R':
                    return [i, j]

    R = f1(n, m) + [answer]
    q = deque([R])

    check = [[False] * m for _ in range(n)]

    while q:
        x, y, c = q.popleft()
        check[x][y] = True
        if board[x][y] == 'G':
            answer = c
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tmp_cnt = 0
            for i in range(101):
                cnt = i + 1
                di = x + dx * cnt
                dj = y + dy * cnt
                if 0 <= di < n and 0 <= dj < m and board[di][dj] != 'D':
                    continue
                else:
                    tmp_cnt = cnt - 1
                    break
            di = x + dx * tmp_cnt
            dj = y + dy * tmp_cnt
            if 0 <= di < n and 0 <= dj < m and check[di][dj] == False:
                check[di][dj] = True
                q.append([di, dj, c + 1])

    if answer == 0:
        answer -= 1
    return answer