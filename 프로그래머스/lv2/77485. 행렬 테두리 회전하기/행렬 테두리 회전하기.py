import heapq

def solution(rows, columns, queries):
    answer = []
    n, m = rows, columns
    board = [[0] * m for _ in range(n)]
    num = 0

    for i in range(n):
        for j in range(m):
            num += 1
            board[i][j] = num

    for info in queries:
        heap = []

        x1,y1,x2,y2 = info
        x1, y1, x2, y2  = x1-1,y1-1,x2-1,y2-1
        tmp1 = board[x1+1][y1]
        tmp2 = 0
        for y in range(y1, y2+1):
            tmp2 = board[x1][y]
            heapq.heappush(heap, tmp2)
            board[x1][y], tmp1 = tmp1, tmp2

        for x in range(x1+1, x2+1):
            tmp2 = board[x][y2]
            heapq.heappush(heap, tmp2)
            board[x][y2], tmp1 = tmp1, tmp2

        for y in range(y2-1, y1-1, -1):
            tmp2 = board[x2][y]
            heapq.heappush(heap, tmp2)
            board[x2][y], tmp1 = tmp1, tmp2

        for x in range(x2-1, x1-1, -1):
            tmp2 = board[x][y1]
            heapq.heappush(heap, tmp2)
            board[x][y1], tmp1 = tmp1, tmp2

        answer.append(heap[0])
    return answer
