def solution(participant, completion):
    answer = ''
    d1 = {}
    for p in participant:
        if p not in d1:
            d1[p] = 1
        else:
            d1[p] += 1
    
    for c in completion:
        d1[c] -= 1
    
    for k,v in d1.items():
        if v > 0 :
            answer = k
            break
            
    return answer