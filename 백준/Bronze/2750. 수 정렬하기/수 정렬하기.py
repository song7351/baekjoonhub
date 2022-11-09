"""
https://www.acmicpc.net/problem/2750
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
for x in lst:
    print(x)