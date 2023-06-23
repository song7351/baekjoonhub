def solution(n):
    answer = []
    
    def hanoi(s,e,m, n):
        if n == 1:
            answer.append([s,e])
        else:
            hanoi(s,m,e, n-1)
            hanoi(s,e,m, 1)
            hanoi(m,e,s, n-1)
    
    hanoi(1,3,2,n)
    return answer