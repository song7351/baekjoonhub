melon = int(input())

direction = []
distance = []
for _ in range(6):
    n, m = map(int, input().split())
    direction.append(n)
    distance.append(m)

direction += direction
distance += distance
max_row = 0
max_col = 0

# 가로 세로중 각 길이의 최대값을 뽑아서 곱하면 최대 넓이를 구할 수 있다.
for i in range(12):
    if direction[i] in [1, 2] and distance[i] > max_row:
        max_row = distance[i]

    if direction[i] in [3, 4] and distance[i] > max_col:
        max_col = distance[i]

max_area = max_row * max_col

# 연속되는 4개의 인덱스가 각각 1 == 3, 2 == 4를 만족한다면 2, 3에서 꺽인다. => 빼줘야될 사각형.
for i in range(9):
    if direction[i] == direction[i+2] and direction[i+1] == direction[i+3]:
        min_area = distance[i+2] * distance[i+1]
        break

print((max_area - min_area) * melon)