import sys
def search(s,e):
    global ans
    while s <= e:
        m = (s+e)//2
        tmp = 0
        for tree in namu:
            if tree > m:
                tmp += (tree - m)
        if tmp >= M:
            ans = m
            s = m+1
        else:
            e = m-1

N,M = map(int, input().split())
namu = list(map(int, sys.stdin.readline().split()))
namu.sort()
ans = 0
search(0,namu[-1])
print(ans)