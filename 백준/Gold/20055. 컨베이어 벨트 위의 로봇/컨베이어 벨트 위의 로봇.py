"""
로봇이 n-1인덱스 도착(이동)시 바로 제거된다.
1. 로봇과 벨트가 동시에 움직인다.(감가X)
2. 로봇이 다음칸으로 이동한다.
    단, 다음칸이 0이거나 로봇이 있다면 이동하지 않는다.
3. 로봇을 새로추가한다.
    단, 추가하는 위치값이 0이면 추가하지 않는다.
"""
from collections import Counter
import sys

input = sys.stdin.readline

n,k = map(int, input().split())
robots = [False] * n
belt = list(map(int, input().split()))
answer = 0

while Counter(belt)[0] < k:
    # 한칸 이동한다.
    answer += 1

    # 벨트와 로봇이 이동한다.
    tmp_belt = belt.pop()
    belt = [tmp_belt] + belt

    robots.pop()
    robots = [False] + robots

    # 맨 마지막 로봇제거
    robots[n-1] = False

    # 로봇을 이동한다.
    for i in range(n-2, -1, -1):
        # 현재 인덱스에 로봇이 존재할때
        if robots[i] == True:
            # 다음 컨베이어벨트가 0이 아니고, 다음 로봇자리가 비어있다면
            if belt[i+1] != 0 and robots[i+1] == False:
                robots[i+1], robots[i] = True, False
                belt[i+1] -= 1


    # 로봇추가
    tmp_robot = True
    if belt[0] == 0:
        tmp_robot = False
    robots[0] = tmp_robot
    if tmp_robot:
        belt[0] -= 1

print(answer)