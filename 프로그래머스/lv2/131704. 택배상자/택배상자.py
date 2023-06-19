def solution(order):
    wait = []
    num = 1
    idx = 0 
    while num != len(order)+1:
        wait.append(num)
        while wait and wait[-1] == order[idx]:
            idx += 1
            wait.pop()
            
        num += 1
    return idx