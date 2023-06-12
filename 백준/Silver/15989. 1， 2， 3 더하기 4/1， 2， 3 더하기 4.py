"""
https://www.acmicpc.net/problem/15989
"""

for tc in range(int(input())):
    n = int(input())
    tmp3 = n//3
    tmp2 = n//2
    lst = [0]*(tmp3+1)
    lst[0] = tmp2 + 1
    if n%2 == 1:
        for i in range(1,tmp3+1):
            if i%2 == 1:
                lst[i] = lst[i-1] - 1
            else:
                lst[i] = lst[i-1] - 2
    else:
        for i in range(1,tmp3+1):
            if i%2 == 1:
                lst[i] = lst[i-1] - 2
            else:
                lst[i] = lst[i-1] - 1
    print(sum(lst))