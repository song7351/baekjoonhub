t = int(input())

for tc in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1,n):
        lst[0][i] = max(lst[0][i-1], lst[1][i-1]+lst[0][i])
        lst[1][i] = max(lst[1][i-1], lst[0][i-1]+lst[1][i])
    print(max(lst[0][n-1], lst[1][n-1]))