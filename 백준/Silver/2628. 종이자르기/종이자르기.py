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
row.sort()
col.sort()

# 잘린 구간별 크기 리스트
r = []
c = []

for i in range(len(row)-1):
    r.append(row[i+1] - row[i])
for i in range(len(col)-1):
    c.append(col[i+1] - col[i])

# 넓이의 최대값
a = max(r)
b = max(c)
max_num = a*b

print(max_num)