"""
https://www.acmicpc.net/problem/2887

N개의 행성 3차원좌표 2개의 행성 각축 기준 좌표차의 절대값중 가장 작은값
총 N-1개의 터널 모든 행성 연결

기존 크루스칼  = 메모리초과

"""
import sys
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

x = []
y = []
z = []
for i in range(1, n+1):
    a,b,c = map(int, sys.stdin.readline().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

lst = []
for i in range(n-1):
    lst.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    lst.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    lst.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

lst.sort()

result = 0
for tmp in lst:
    c,a,b = tmp
    if find(parent,a) != find(parent, b):
        result += c
        union(parent, a, b)

print(result)