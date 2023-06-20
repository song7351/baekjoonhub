def solution(p):
    answer = ''
    if p == answer:
        return answer
    
    def check(w):
        tmp_lst = []
        for x in w:
            if x == '(':
                tmp_lst.append('(')
            else:
                if not tmp_lst:
                    return False
                if tmp_lst[-1] != '(':
                    return False
                else:
                    tmp_lst.pop()
        if tmp_lst:
            return False
        
        return True
    
    def chg(w):
        w = w[1:-1]
        tmp_w = ''
        for x in w:
            if x == '(':
                tmp_w += ')'
            else:
                tmp_w += '('
        return tmp_w
    
    def dfs(w):
        tmp_u = ''
        tmp_v = ''
        ca,cb = 0,0
        if w == '':
            return ''
        
        for i in range(len(w)):
            if w[i] == '(':
                ca += 1
            elif w[i] == ')':
                cb += 1
            tmp_u += w[i]
            if ca == cb != 0:
                tmp_v = w[i+1:]
                break
        
        if check(tmp_u):
            return tmp_u + dfs(tmp_v)
        else:
            return '(' + dfs(tmp_v) + ')' + chg(tmp_u)
        
    answer = dfs(p)
    
    return answer