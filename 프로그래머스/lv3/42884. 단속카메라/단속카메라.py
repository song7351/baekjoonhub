def solution(routes):
    answer = 0
    n = len(routes)
    routes.sort(key=lambda x : (x[1],x[0]))
    idx = 0
    while idx < n:
        s,e = routes[idx]
        idx += 1
        while idx < n and routes[idx][1] >= e  and routes[idx][0] <= e:
            idx += 1
        answer += 1
        
    return answer