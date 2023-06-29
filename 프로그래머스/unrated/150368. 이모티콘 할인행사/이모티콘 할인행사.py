def solution(users, emoticons):
    answer = [0,0]
    n, m = len(users), len(emoticons)

    def dfs(idx_emoticons, m, lst):
        nonlocal answer
        if idx_emoticons >= m:
            tmp_cnt, tmp_price = 0, 0
            for i in range(n):
                if lst[i] >= users[i][1]:
                    tmp_cnt += 1
                else:
                    tmp_price += lst[i]
            if answer[0] == tmp_cnt and answer[1] < tmp_price:
                answer[1] = tmp_price
            elif answer[0] < tmp_cnt:
                answer = [tmp_cnt, tmp_price]
        else:
            for dis in [40, 30, 20, 10]:
                lst2 = lst.copy()
                for i in range(n):
                    if users[i][0] <= dis:  # 할인율이 쎄면 산다.
                        lst2[i] += emoticons[idx_emoticons] * (100-dis) // 100
                dfs(idx_emoticons + 1, m, lst2)

    dfs(0, m, [0] * n)
    return answer