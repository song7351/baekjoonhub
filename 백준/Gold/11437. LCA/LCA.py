import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeTree(node, dep):
    depth[node] = dep
    for c in child[node]:
        if parents[c] == 0:
            parents[c] = node
            makeTree(c, dep+1)
            
def lca(a, b):    
    if a > b: 
        a, b = b, a
    x, y = a, b
        
    if (a, b) in answers:
        return answers[(a, b)]
    
    if depth[a] > depth[b]:
        a, b = b, a
    
    if (a, b) in answers:
        return answers[(a, b)]
    
    while depth[a] != depth[b]:
        b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]   
    
    answers[(x, y)] = a
    return a      

n = int(input())
depth = [0]*(n+1)
parents = [0]*(n+1)
child = [[] for _ in range(n+1)]
answers = {}

for _ in range(n-1):
    a, b = map(int, input().split())
    child[a].append(b) 
    child[b].append(a)
    
parents[1] = 1
makeTree(1, 1)  

m = int(input())
for _ in range(m):
    a, b = map(int, input().split()) 
    print(lca(a, b))