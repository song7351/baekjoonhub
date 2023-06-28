from collections import deque

def solution(plans):
    answer = []
    lst = []
    for sb, st, t in plans:
        sh, sm = list(map(int, list(st.split(":"))))
        t = int(t)
        s = sh * 60 + sm
        lst.append([s, t, sb])
    lst.sort()

    q = deque()

    for s, t, sb in lst:
        if not q:
            q.append([s, t, sb])
        else:
            timer = s - q[-1][0]
            while q:
                if q[-1][1] == 0:
                    answer.append(q[-1][2])
                    q.pop()
                else:
                    if timer >= q[-1][1]:
                        timer -= q[-1][1]
                        q[-1][1] = 0
                    else:
                        q[-1][1] -= timer
                        break
            q.append([s, t, sb])

    while q:
        s, t, sb = q.pop()
        answer.append(sb)

    return answer