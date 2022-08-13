import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]
num = 0

for i in num_list:
    num += i
    sum_list.append(num)
    
for i in range(M):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start-1])