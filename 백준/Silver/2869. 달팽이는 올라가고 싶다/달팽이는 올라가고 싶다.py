a,b,v = map(int, input().split())

if (v-a)%(a-b) == 0:
    day = (v-a)//(a-b) + 1
else:
    day = (v-a)//(a-b) + 2

print(day)