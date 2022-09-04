N, K = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0

for i in range(N-1, -1, -1):
    if K // lst[i] != 0:
        cnt += K//lst[i]
        K = K % lst[i]

print(cnt)