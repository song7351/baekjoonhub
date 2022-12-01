"""
https://www.acmicpc.net/problem/26083
"""
import sys
input = sys.stdin.readline

def check1(y,m,d):
    if 0<= y <= 99:
        # 윤년이 아닐때
        if y%4 != 0 and 0<m<13:
            if m in [1,3,5,7,8,10,12]:
                if 0<d<32:
                    return True
            elif m == 2:
                if 0<d<29:
                    return True
            else:
                if 0<d<31:
                    return True
        # 윤년일때
        elif y%4 == 0 and 0<m<13:
            if m in [1, 3, 5, 7, 8, 10, 12]:
                if 0 < d < 32:
                    return True
            elif m == 2:
                if 0 < d < 30:
                    return True
            else:
                if 0 < d < 31:
                    return True
    return False

def check2(y,m,d):
    global ty, tm, td

    if y > ty:
        return True
    elif y == ty:
        if m > tm:
            return True
        elif m == tm:
            if d >= td:
                return True
    return False

ty, tm, td = map(int, input().split())

test_case = int(input())

for tc in range(test_case):
    t1, t2, t3 = map(int, input().split())
    valid_cnt = False
    # 연도/월/일인 경우
    if check1(t1,t2,t3):
        valid_cnt = True
        if not check2(t1, t2, t3):
            print("unsafe")
            continue

    if check1(t3,t2,t1):
        valid_cnt = True
        if not check2(t3, t2, t1):
            print("unsafe")
            continue

    if check1(t3,t1,t2):
        valid_cnt = True
        if not check2(t3, t1, t2):
            print("unsafe")
            continue

    if not valid_cnt:
        print("invalid")
    else:
        print("safe")
