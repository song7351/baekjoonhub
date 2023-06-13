from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    wq = deque()
    t = deque()
    while q:
        answer += 1
        if len(t) > 0:
            if t[0] + bridge_length == answer:
                t.popleft()
                wq.popleft()
            
        if sum(wq) + q[0] <= weight and len(wq) < bridge_length:
            wq.append(q[0])
            t.append(answer)
            q.popleft()
        
            
        
    
    return answer+bridge_length