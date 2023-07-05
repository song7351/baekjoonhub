def solution(m, n, puddles):
    answer = 0
    maps = [[0] + [1] * m for _ in range(n+1)]
    
    for x,y in puddles:
        maps[y][x] = 0
    
    check = 1
    for i in range(1, m+1):
        if check == 0:
            maps[1][i] = 0
        elif maps[1][i] == 0:
            check = 0

    for x in range(2, n+1):
        for y in range(1, m+1):
            if maps[x][y] != 0:
                maps[x][y] = (maps[x-1][y] + maps[x][y-1])%1000000007
                
    answer = maps[-1][-1]
    return answer