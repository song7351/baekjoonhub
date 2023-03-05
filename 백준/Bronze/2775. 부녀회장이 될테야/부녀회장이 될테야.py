"""
0~14층 -> 총 15층이고
0층 1호부터 거주민 존재.
아랫층의 1호부터 자신의 호까지의 합을 구해야됨.
근데 아랫층의 자신의호 직전까지의 합은 자신의 옆집임.
그럼 나는 내 아랫층과 내 옆집의 합만 알고있으면됨.
"""

tc = int(input())
apt = [ [1]*15 for _ in range(15) ]

for i in range(15):
    for j in range(1,15):
        if i == 0:
            apt[i][j] = apt[i][j-1] + 1
        else:
            apt[i][j] = apt[i-1][j] + apt[i][j-1]

for _ in range(tc):
    k = int(input())
    n = int(input())
    print(apt[k][n-1])