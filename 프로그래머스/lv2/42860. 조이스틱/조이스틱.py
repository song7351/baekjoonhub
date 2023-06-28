from collections import deque
"""
65, 90
0부터 시작해서 방향을 반대로 돌리는 케이스를 bfs에 추가한다
qqq = "BBBBAAAABA"
답12 왼왼오오오오오
"""
def solution(name):
    answer = 0
    lst = list(name)
    n = len(lst)
    lst2 = deque([]) #이동할 인덱스만 모은다.
    # 상하 스틱 카운트
    for i in range(n):
        tmp = ord(lst[i])
        lst[i] = min((tmp - 65), (91 - tmp))
        if lst[i] != 0 and i != 0:
            lst2.append(i)

    # 좌우 스틱 카운트(걍 dfs돌림)
    m = len(lst2)
    tmp = int(1e9)
    def dfs(now, lst3, res):
        nonlocal tmp
        lst3 = deque(lst3)
        if not lst3:
            if res < tmp:
                tmp = res
        else:
            # 현재 위치에서 갈수있는 인덱스는 리스트의 처음과 끝뿐이다.
            a,b = lst3[0],lst3[-1]

            # 갈 수 있는 각 인덱스는 현재 위치기준 왼쪽인지 오른쪽인지에 따라 최소이동값이 다르다.
            if a <= now:
                aa = min((abs(now-a)), a+n-now)
            else:
                aa = min((abs(now-a)), now+n-a)
            if b <= now:
                bb = min((abs(now-b)), b+n-now)
            else:
                bb = min((abs(now-b)), now+n-b)
            lst3.popleft()
            dfs(a,lst3, res+aa)
            lst3.appendleft(a)
            lst3.pop()
            dfs(b,lst3, res+bb)
            lst3.append(b)

    dfs(0,lst2,0)

    return sum(lst) + tmp