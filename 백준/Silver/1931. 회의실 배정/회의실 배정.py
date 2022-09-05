N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key=lambda x: (x[1], x[0]))
n = lst[0]
cnt = 1
for i in range(1,N):
    if lst[i][0] >= n[1]:
        n = lst[i]
        cnt += 1
print(cnt)