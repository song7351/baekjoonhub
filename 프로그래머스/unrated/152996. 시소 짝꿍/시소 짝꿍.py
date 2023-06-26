from collections import Counter

"""
22, 23, 24
32, 33, 34
42, 43, 44
우리는 큰것만 비교할꺼다 왜냐? 작은것부터 확인하기때문에 중복이 됨
같을때는 중복제외 뽑는 경우의수 n(n-1)//2
다를때는 걍 곱하면됨
23,24,34 -> 1:3/2 2:4/2 3:4/3
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