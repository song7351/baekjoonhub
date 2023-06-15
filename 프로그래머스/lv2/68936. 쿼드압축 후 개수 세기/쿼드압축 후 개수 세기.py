def solution(arr):
    answer = [0, 0]

    def check(maps):
        n = len(maps)
        cnt = [0, 0]
        for lst in maps:
            cnt[0] += lst.count(0)
            cnt[1] += lst.count(1)
            if 0 not in cnt:
                break
        if 0 in cnt:
            if cnt[0] != 0:
                answer[0] += 1
            else:
                answer[1] += 1
        else:
            maps1, maps2, maps3, maps4 = [], [], [], []
            m = n // 2
            for i in range(m):
                maps1.append(maps[i][:m])
                maps2.append(maps[i][m:])
                maps3.append(maps[i + m][:m])
                maps4.append(maps[i + m][m:])
            check(maps1)
            check(maps2)
            check(maps3)
            check(maps4)

    check(arr)
    return answer