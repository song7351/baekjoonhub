"""
a이상 b이하 소수출력
"""
a,b = map(int, input().split())
if a == 1:
    a = 2
    
# 전체 소수 리스트
lst = [0]*(b+1)

for num in range(2, b+1):
    tmp = 2
    while num*tmp <= b:
        lst[num*tmp] = 1
        tmp += 1

for num in range(a,b+1):
    if lst[num] == 0:
        print(num)