def solution(n, times):
    answer = int(1e15)
    s,e = 0, int(1e15)
    
    while s <= e:
        m = (s+e)//2
        tmp = 0
        for t in times:
            tmp += m//t
        
        if tmp < n:
            s = m+1
        elif tmp >= n:
            answer = min(answer, m)
            e = m-1
    
    return answer