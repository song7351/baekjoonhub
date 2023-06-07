"""
시작 0,0
끝 n-1,m-1

"""
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = -1
    
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0:
        answer = -1
    else:
        q = deque([[0,0,1]])
        while q:
            di, dj, v = q.popleft()

            if di == n-1 and dj == m-1:
                return v
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x = di + dx
                y = dj + dy
                if 0<= x < n and 0<= y < m and maps[x][y] == 1:
                    maps[x][y] = 0
                    q.append([x,y,v+1])
    return answer