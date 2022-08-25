N = int(input())
max_len = 1
ans = [N]

for i in range(1,N+1):
    lst = [N, i]
    start = 0
    while True:
        x = lst[start] - lst[start+1]
        if x < 0:
            break
        else:
            lst.append(x)
        start += 1

    if len(lst) > max_len:
        max_len = len(lst)
        ans = lst[:]

ans = map(str, ans)
print(max_len)
print(' '.join(ans))
