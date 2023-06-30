def solution(line):
    answer = []
    n = len(line)
    lst = set()
    INF = int(1e10)
    left, right, bottom, top = INF, -INF, INF, -INF
    for i in range(n - 1):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            adbc = a * d - b * c
            bfed_x = b * f - e * d
            bfed_y = e * c - a * f
            if adbc != 0:
                x = bfed_x / adbc
                y = bfed_y / adbc
                if x == int(x) and y == int(y):
                    if x < left:
                        left = int(x)
                    if x > right:
                        right = int(x)
                    if y < bottom:
                        bottom = int(y)
                    if y > top:
                        top = int(y)
                    lst.add((int(x), int(y)))
    n, m = top - bottom + 1, right - left + 1
    maps = [["."] * m for _ in range(n)]
    for x, y in lst:
        xx = x + (-left)
        yy = -(y + (-top))
        maps[yy][xx] = '*'

    for lst1 in maps:
        answer.append(''.join(lst1))

    return answer