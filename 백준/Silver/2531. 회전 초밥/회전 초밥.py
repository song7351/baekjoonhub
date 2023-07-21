"""
d: 초밥가짓수
k: 연속해서 먹는 접시의수
c: 쿠폰번호
"""

n,d,k,c = map(int, input().split())

lst = [ int(input()) for _ in range(n) ]
lst = lst + lst

ans = 0
for i in range(n):
    s,e = i, i+k
    lst1 = lst[s:e]
    lst2 = set(lst1)
    lst2.add(c)
    ans = max(ans, len(lst2))

print(ans)
