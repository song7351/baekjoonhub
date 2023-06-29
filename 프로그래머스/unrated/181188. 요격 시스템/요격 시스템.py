def solution(targets):
    answer = 0
    targets.sort(key=lambda x : x[1])   # 요격의 끝이 가장 빠른 순
    missile = -1
    for taget in targets:
        s,e = taget
        if s > missile:                 # 시작점이 미사일지점보다 크다면, 미사일 추가발사해야됨
            answer += 1
            missile = e - 0.5           # 편의상 미사일지점은 끝점에서 -0.5
            
    return answer