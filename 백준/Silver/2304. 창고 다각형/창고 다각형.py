N = int(input()) #사각형 개수
row = []
col = []
for _ in range(N):
    n, m = map(int, input().split())
    row.append(n)
    col.append(m)

# 가로기준 오름차순
for i in range(N-1):
    for j in range(N-1):
        if row[j] > row[j+1]:
            row[j], row[j+1] = row[j+1], row[j]
            col[j], col[j+1] = col[j+1], col[j]

area = 0

max_idx1 = 0        # 정순
max_idx2 = N-1        # 역순
for i in range(N):
    if col[max_idx1] < col[i]:
        max_idx1 = i
    if col[max_idx2] < col[N-1-i]:
        max_idx2 = N-1-i

area += (row[max_idx2] - row[max_idx1] + 1) * col[max_idx1]

start_idx = 0

for i in range(max_idx1 + 1):
    if col[i] > col[start_idx]:
        area += (row[i] - row[start_idx]) * col[start_idx]
        start_idx = i

start_idx = N-1
for i in range(N-1, max_idx2-1, -1):
    if col[i] > col[start_idx]:
        area += (row[start_idx] - row[i]) * col[start_idx]
        start_idx = i

print(area)