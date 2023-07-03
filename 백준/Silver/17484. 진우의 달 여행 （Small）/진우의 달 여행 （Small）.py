n,m = map(int, input().split())

maps = [[int(1e15)]+list(map(int, input().split()))+[int(1e15)] for _ in range(n)]

map1 = [[int(1e15)]*(m+2) for _ in range(n)]
map2 = [[int(1e15)]*(m+2) for _ in range(n)]
map3 = [[int(1e15)]*(m+2) for _ in range(n)]
map1[0], map2[0], map3[0] = maps[0].copy(), maps[0].copy(), maps[0].copy()

for i in range(1, n):
    for j in range(1, m+1):
        map1[i][j] = min(map2[i-1][j], map3[i-1][j+1]) + maps[i][j]
        map2[i][j] = min(map1[i-1][j-1], map3[i-1][j+1]) + maps[i][j]
        map3[i][j] = min(map1[i-1][j-1], map2[i-1][j]) + maps[i][j]

print(min(min(map1[n-1]), min(map2[n-1]), min(map3[n-1])))