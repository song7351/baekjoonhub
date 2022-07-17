a = [0]*4

def sol(x):
    a[0] = x//1000
    a[1] = (x%1000)//100
    a[2] = ((x%1000)%100)//10
    a[3] = ((x%1000)%100)%10

b = int(input())
n = 0

for i in range(1,b+1):
    sol(i)
    if 0 < i < 100:
        n += 1
    if 99 < i <1000:
        if a[1]-a[2] == a[2]-a[3]:
            n += 1

print(n)
