def solution(quiz):
    answer = []
    for q in quiz:
        lst = list(q.split())
        a,b,c = int(lst[0]), int(lst[2]), int(lst[4])
        x = lst[1]
        ans = "X"
        if x == '+' and a + b == c:
            ans = "O"
        elif x == '-' and a - b == c:
            ans = "O"
        answer.append(ans)
        
    return answer