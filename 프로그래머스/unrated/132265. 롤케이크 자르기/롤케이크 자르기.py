def solution(topping):
    answer = 0
    n = len(topping)
    lst1 = [0] * n
    lst2 = [0] * n
    
    me = set()
    you = set()
    
    for i in range(n):
        j = n-1 - i
        me.add(topping[i])
        you.add(topping[j])
        lst1[i] = len(me)
        lst2[j] = len(you)
    
    for i in range(n-1):
        if lst1[i] == lst2[i+1]:
            answer += 1
            
    return answer