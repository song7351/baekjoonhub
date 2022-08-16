"""
원리: 
1. 9개중 7개의 합이 100이라면, 9중 2개의 합은 100의 초과분일것이다.
2. 2개를 더해서 초과분(diff)을 찾는다.
3. 찾았다면 기존 리스트에서 제거(.remove)해주고 리스트를 오름차순으로 정렬
4. print

"""
hobit = []
N = 9
sum_hobit = 0
for _ in range(N):
    height = int(input())
    hobit.append(height)
    sum_hobit += height

# 1. 9개중 7개의 합이 100이라면, 9중 2개의 합은 100의 초과분일것이다.
diff = sum_hobit - 100

# 2. 2개를 더해서 초과분(diff)을 찾는다.
for i in range(N):
    a = 0
    for j in range(i+1, N):
        if hobit[i] + hobit[j] == diff:
            a = hobit[i]
            b = hobit[j]
            break
    if a != 0:
        break
        
# 3. 찾았다면 기존 리스트에서 제거(.remove)해주고 리스트를 오름차순으로 정렬
hobit.remove(a)
hobit.remove(b)

for i in range(len(hobit)):
    for j in range(len(hobit)-1):
        if hobit[j] > hobit[j+1]:
            hobit[j], hobit[j+1] = hobit[j+1], hobit[j]

# 4. print
for i in hobit:
    print(i)