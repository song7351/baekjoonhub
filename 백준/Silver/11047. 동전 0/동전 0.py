"""
 동전은 총 N종류이고,
  그 가치의 합을 K로 만들려고 한다
  필요한 동전 개수의 최솟값
"""
N, K = map(int, input().split())
# 돈의 크기가 오름차순으로 제시된다.
lst = [int(input()) for _ in range(N)]
ans = 0

# 가장 큰 단위부터 나눈다.
for i in range(N-1, -1, -1):
    ans += K // lst[i]
    K = K % lst[i]

print(ans)