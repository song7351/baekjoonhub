"""

"""
def solution(n, l, r):
    answer = 0
    
    def f(n):
        if n%5 == 2:
            return False
        if n < 5:
            return True
        return f(n//5)
    
    for num in range(l-1, r):
        if f(num):
            answer += 1
        
    return answer