"""
https://www.acmicpc.net/problem/2343

조건1. 블루레이에는 총 N개의 강의가 들어가는데
조건2. 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다.
조건3.  M개의 블루레이
조건4. 단, M개의 블루레이는 모두 같은 크기이어야 한다.

목표: 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다.

어떻게 접근해야하는가?
-> 모든구간이 균등하고 순서유지
-> 이진트리 접근
-> 전에 풀어봤던 공유기문제, 가래떡 등등 접근방법과 동일하다고 판단.
-> 이진트리로 최적의 크기를 탐색한다.
-> 해당 값으로 몇개의 블루레이가 나오는가?
-> 만약 구했다면 더 작은값으로 재탐색
"""

N,M = map(int, input().split())
lst = list(map(int, input().split()))

# 적절한 값을 탐색하는 범위(시작값은 최대값, 끝값은 총합)
s = max(lst)
e = sum(lst)


def check(target):
    cnt = 1
    tmp = 0
    for i in range(N):
        tmp += lst[i]
        if tmp > target:
            cnt += 1
            tmp = lst[i]
    return cnt


def binarysort(start, end):
    global ans
    # 우리가 정한 크기(middle)로 블루레이 수량을 구했을때 목표한 수량M보다 많다면
    # 크기가 너무 작다는 뜻이다. 크기를 더 키우라는 뜻
    while start <= end:
        middle = (start + end) // 2
        cnt = check(middle)
        if cnt > M:
            start = middle + 1
        else:
            # if cnt == M and middle < ans:
            #     ans = middle
            end = middle - 1
            ans = middle


ans = int(1e9)
binarysort(s, e)
print(ans)
