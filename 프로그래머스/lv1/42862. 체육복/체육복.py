def solution(n, lost, reserve):
    answer = 0
    lst = [1] * (n+2)
    
    for x in lost:
        lst[x] -= 1
        
    for x in reserve:
        lst[x] += 1
        
    for i in range(1, n+1):
        if lst[i] > 1:
            if lst[i-1] == 0:
                lst[i-1] += 1
            elif lst[i+1] == 0:
                lst[i+1] += 1
            lst[i] = 1
            
    answer = lst.count(1) - 2
    return answer