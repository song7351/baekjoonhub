def solution(N, road, K):
    answer = 0
    
    maps = [[int(1e9)]*(N+1) for _ in range(N+1)]
    lst = set()
    for x,y,v in road:
        maps[x][y] = min(maps[x][y], v)
        maps[y][x] = min(maps[y][x], v)
    for i in range(N+1):
        maps[i][i] = 0
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])
    
    for i in range(1,N+1):
        if maps[1][i] <= K:
            answer += 1
            
    return answer