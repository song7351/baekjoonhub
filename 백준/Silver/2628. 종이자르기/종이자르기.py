N, M = map(int, input().split())
K = int(input())
row = [0,M]
col = [0,N]

# 가로 세로별 잘리는 포인트 추가
for i in range(K):
    d, idx = map(int, input().split())
    if d == 0:
        row.append(idx)
    else:
        col.append(idx)

# 크기별 정렬
for i in range(len(row)-1):
    for j in range(i+1, len(row)):
        if row[i] > row[j]:
            row[i], row[j] = row[j], row[i]

for i in range(len(col)-1):
    for j in range(i+1, len(col)):
        if col[i] > col[j]:
            col[i], col[j] = col[j], col[i]

# 잘린 구간별 크기 리스트
r = []
c = []

for i in range(len(row)-1):
    r.append(row[i+1] - row[i])
for i in range(len(col)-1):
    c.append(col[i+1] - col[i])

# 넓이의 최대값
max_num = 0
for i in r:
    for j in c:
        if i*j > max_num:
            max_num = i*j

print(max_num)
