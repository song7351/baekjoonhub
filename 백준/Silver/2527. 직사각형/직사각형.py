"""
 왼쪽 아래 꼭짓점 좌표 (x, y)와 오른쪽 위 꼭짓점 좌표 (p, q)
 4개의 정수 x y p q 로 표현
"""
test_case = 4
for _ in range(test_case):
    x1,y1,p1,q1, x2,y2,p2,q2 = map(int, input().split())
    if p2 < x1 or q2 < y1 or x2 > p1 or y2 > q1:        # 공통부분이 없는 경우
        print("d")
    elif (p2,q2) == (x1,y1) or (x2,y2) == (p1,q1) or (p2,y2) == (x1,q1) or (x2,q2) == (p1,y1):
        print("c")  # 각 꼭지점이 만나는 경우
    elif q2 == y1 or y2 == q1 or p2 == x1 or x2 == p1:
        print('b')  # 각 선분이 만나는 경우
    else:
        print('a')  # 이외 겹치는 경우