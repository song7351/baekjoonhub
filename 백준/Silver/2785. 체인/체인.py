def chain(arr,n):
    cnt, m = 0, n-1
    for i in range(n):
        if arr[i] < m:
            cnt += arr[i]
            m = m-1-arr[i]
        else:
            cnt += m
            m -= m

        if m == 0:
            return cnt

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = chain(lst, N)
print(ans)