from collections import deque

def solution(n, results):
    answer = 0
    lst1 = [[] for _ in range(n+1)]
    cnt1 = [1]*(n+1)
    lst2 = [[] for _ in range(n+1)]
    cnt2 = [n]*(n+1)
    
    for winner, looser in results:
        lst1[looser].append(winner)
        lst2[winner].append(looser)
    
    def bfs(x, lst):
        q = deque([x])
        visited = [False]*(n+1)
        
        while q:
            num = q.popleft()
            visited[num] = True
            
            for m in lst[num]:
                if visited[m] == False:
                    visited[m] = True
                    q.append(m)
                    
        return visited.count(True)-1
    
    for i in range(1, n+1):
        cnt = bfs(i, lst1)
        cnt1[i] += cnt
        cnt = bfs(i, lst2)
        cnt2[i] -= cnt
    
    for i in range(1, n+1):
        if cnt1[i] == cnt2[i]:
            answer += 1
    return answer