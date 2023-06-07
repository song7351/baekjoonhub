def solution(dirs):
    answer = 0
    maps = [[False] * 11 for _ in range(11)]
    dx,dy = 5,5
    dic = {"U":[-1,0], "D":[1,0], "L":[0,-1], "R":[0,1]}
    lst = []
    for word in list(dirs):
        x,y = dic[word]
        tmp_x, tmp_y = dx+x, dy+y
        
        if 0<= tmp_x < 11 and 0<= tmp_y < 11:
            tmp1 = ''.join(list(map(str, [dx,dy,tmp_x,tmp_y])))
            tmp2 = ''.join(list(map(str, [tmp_x,tmp_y, dx,dy])))
            if tmp1 not in lst:
                answer += 1
                lst.append(tmp1)
                lst.append(tmp2)
            dx,dy = tmp_x, tmp_y
            
    return answer