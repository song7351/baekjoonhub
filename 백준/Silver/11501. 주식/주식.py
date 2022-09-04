test_case = int(input())

for tc in range(1,test_case+1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_val = lst[-1]
    ans = 0
    for i in range(N-1, -1, -1):
        if lst[i] < max_val:
            ans += max_val - lst[i]
        else:
            max_val = lst[i]

    print(ans)