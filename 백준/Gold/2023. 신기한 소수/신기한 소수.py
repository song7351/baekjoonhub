"""
N자리수 신기한 소수를 찾아 오름차순으로 출력하세요.
신기한 소수란?
왼쪽부터
1자리도 소수
2자리도 소수
3자리도 소수
...... N자리도 소수
"""
import sys
sys.setrecursionlimit(10**9)

def check(x):
    for i in range(2,int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def dfs(x):
    # 소수인지 확인
    if check(x):
        # 길이가 N자리인가?
        if len(str(x)) == n:
            print(x)
        # 길이가 짧다면,
        elif len(str(x)) < n:
            str_x = str(x)
            # 1~9를 붙여라
            for i in [1,3,5,7,9]:
                tmp_x = str_x + str(i)
                dfs(int(tmp_x))

n = int(input())

# 1자리소수는 2,3,5,7
for i in [2,3,5,7]:
    dfs(i)
