import sys
input = sys.stdin.readline

n = int(input())
lst = [(int(input()), i) for i in range(n)]
lst.sort()

maxV = 0
for i in range(n):
    if maxV < lst[i][1] - i:
        maxV = lst[i][1] - i

print(maxV + 1)
