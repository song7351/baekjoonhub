from math import ceil


a = input().split()
a = list(map(int, a))
v, b, a = a[2],a[1],a[0]

day = ceil((v-a)/(a-b) + 1)

print(day)