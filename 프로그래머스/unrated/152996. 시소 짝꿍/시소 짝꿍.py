from collections import Counter

"""
22, 23, 24
32, 33, 34
42, 43, 44
"""
def solution(weights):
    answer = 0
    n = len(weights)
    c = Counter(weights)
    for i in range(100, 1000+1):
        if c[i] != 0:
            answer += c[i]* (c[i] - 1)//2
            answer += c[i]* c[i*2]
            answer += c[i]* c[i*3/2]
            answer += c[i]* c[i*4/3]
            
    return answer