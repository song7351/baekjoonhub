def solution(x, y, n):
    answer = 0
    ans = [int(1e9)] * 1000001
    ans[x] = 0
    for number in range(x, y+1):
        if number + n <= y:
            ans[number+n] = min(ans[number+n], ans[number]+1)
        if number * 2 <= y:
            ans[number*2] = min(ans[number*2], ans[number]+1)
        if number * 3 <= y:
            ans[number*3] = min(ans[number*3], ans[number]+1)
    
    answer = ans[y]
    if answer == int(1e9):
        answer = -1
        
    return answer