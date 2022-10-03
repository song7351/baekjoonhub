"""
접근방법
간격을 이진탐색으로 조사한다.
간격: 최소1, 최대(최대좌표-최소좌표)
간격의 중간값으로 공유기를 설치한다.
그런데 공유기가 목표한 설치횟수(C)보다 많다면? -> 간격을 너무 좁게 설정한것. 즉, 간격을 오른쪽 이진탐색실행
공유기가 목표한 설치횟수(C)보다 적다면? -> 간격을 너무 넓게 설정한것. 즉, 간격을 왼쪽 이진탐색실행

그런데 공유기가 목표설치횟수랑 동일할때, 바로 return 하면 될까? (X)
why? -> 같은 횟수일때는 가장 큰 값을 찾아야됨.
how? -> 목표횟수랑 동일할때도 큰 값에 있는지 확인하기 위해서 간격을 오른쪽 이진탐색실행.
"""
import sys

N, C = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
#이진탐색 조건1. 오름차순.
arr.sort()
start = 1
end = arr[-1] - arr[0]
ans = 0

def search(s,e):
    global ans
    while s<=e:
        m = (s + e) // 2
        now = arr[0]
        cnt = 1
        for i in range(1, N):
            if arr[i] >= now + m:
                cnt += 1
                now = arr[i]
                
        if cnt >= C:
            s = m+1
            ans = m
        else:
            e = m-1

search(start, end)
print(ans)

