n,p = map(int, input().split())
jileumgil = [[] for _ in range(10001)]
doros = [int(1e9)]*(10001)

for i in range(p):
    jileumgil[i].append([i+1, 1])

for _ in range(n):
    s,e,v = map(int, input().split())
    if e-s > v:
        jileumgil[s].append([e,v])

doros[0] = 0

def f():
    for i in range(p+1):
        for e,v in jileumgil[i]:
            doros[e] = min(doros[i]+v, doros[e])

f()

print(doros[p])