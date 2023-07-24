"""
1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.
"""
import copy

INF = int(1e15)

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp1,dp2,dp3 = copy.deepcopy(lst),copy.deepcopy(lst),copy.deepcopy(lst)

dp1[0][1],dp1[0][2],dp1[-1][0] = INF, INF, INF
dp2[0][0],dp2[0][2],dp2[-1][1] = INF, INF, INF
dp3[0][0],dp3[0][1],dp3[-1][2] = INF, INF, INF

ans = INF

def find(dp):
    global ans
    for i in range(1,n):
        dp[i][0] += min(dp[i-1][1], dp[i-1][2])
        dp[i][1] += min(dp[i-1][0], dp[i-1][2])
        dp[i][2] += min(dp[i-1][0], dp[i-1][1])
    ans = min(ans, min(dp[-1]))

find(dp1)
find(dp2)
find(dp3)

print(ans)