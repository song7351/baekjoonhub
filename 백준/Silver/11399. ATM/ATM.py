n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans, tmp = 0,0

for i in range(1,n):
    lst[i] = lst[i]+lst[i-1]

print(sum(lst))