import math

tc = int(input())

for _ in range(tc):
    a,b = map(int, input().split())
    print(math.lcm(a,b))