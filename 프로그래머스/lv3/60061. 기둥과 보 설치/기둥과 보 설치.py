def build(x,y,a,result):
    if a:   # 만약에 보라면
        # 보위치 아래 혹은 오른쪽 아래에 기둥이 있는가?
        for test in [[x,y-1,0],[x+1,y-1,0]]:
            if test in result:
                result.append([x,y,a])
                return result
        # 보위치의 왼쪽 오른쪽에 보가 있는가?
        if [x-1,y,1] in result and [x+1,y,1] in result:
            result.append([x,y,a])
            return result
    else:   # 만약에 기둥이라면
        # 기둥이 바닥으로부터 설치를 하는가?
        if y == 0:
            result.append([x,y,a])
            return result
        # 기둥의 아래가 기둥이거나 현재자리 혹은 왼쪽이 보인가?
        for test in [[x,y-1,0],[x,y,1], [x-1,y,1]]:
            if test in result:
                result.append([x,y,a])
                return result
    # 만약 모든조건이 해당하지 않는다면 추가하지말고 그냥 다시 돌려주세요.
    return result

def destroy(x,y,a,result):
    # 일단 삭제요청이 들어오면 삭제하세요.
    result.remove([x, y, a])
    ans = [item[:] for item in result]
    for items in result:
        test = build(items[0],items[1],items[2],ans)
        if len(test) == len(result):
            result.append([x,y,a])
            return result
        else:
            ans.remove([items[0],items[1],items[2]])
    else:
        return result

def solution(n, build_frame):
    result = []
    for item in build_frame:
        x,y,a,b = item[0], item[1], item[2], item[3]
        if b == 1:
            result = build(x,y,a,result)
        else:
            result = destroy(x,y,a,result)
        #print(result)
    result.sort(key=lambda z:(z[0],z[1],z[2]))
    #print(result)
    return result