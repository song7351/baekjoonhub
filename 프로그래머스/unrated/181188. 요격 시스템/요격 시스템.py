"""
s<= <e
"""
from collections import deque

def solution(targets):
    answer = 0
    targets.sort(key=lambda x : x[1])
    missile = -1
    for taget in targets:
        s,e = taget
        if s > missile:
            answer += 1
            missile = e - 0.5
            
    return answer