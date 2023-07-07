from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = [[0]*102 for _ in range(102)]
    for ax,ay,bx,by in rectangle:
        for i in range(ax*2, bx*2+1):
            for j in range(ay*2, by*2+1):
                maps[i][j] = 1
    
    def bfs():
        q = deque([[characterX*2,characterY*2,1]])
        
        while q:
            x,y,c = q.popleft()
            maps[x][y] = 2
            if [x,y] == [itemX*2, itemY*2]:
                return c
            else:
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    di,dj = x+dx, y+dy
                    if 1<= di < 101 and 1<= dj < 101 and maps[di][dj] == 1:
                        if 0 in [maps[di-1][dj-1], maps[di-1][dj], maps[di-1][dj+1], maps[di][dj-1], maps[di][dj+1], maps[di+1][dj-1], maps[di+1][dj], maps[di+1][dj+1]]:
                            maps[di][dj] = 2
                            q.append([di,dj,c+1])
    answer = bfs()
    return answer//2