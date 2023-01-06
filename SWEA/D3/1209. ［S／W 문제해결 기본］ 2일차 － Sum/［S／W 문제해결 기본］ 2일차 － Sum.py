for _ in range(10):
    tc = int(input())
    arr = [ list(map(int, input().split())) for _ in range(100) ]

    ans = []

    a,b = 0,0
    for i in range(100):
        c,d = 0,0 
        for j in range(100):
            if i == j:
                a += arr[i][j]
            if i + j == 99:
                b += arr[i][j]
            c += arr[i][j]
            d += arr[j][i]
        
        ans.append(c)
        ans.append(d)
    ans.append(a)
    ans.append(b)

    print(f"#{tc} {max(ans)}")