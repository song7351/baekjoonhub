n = int(input())

a = list(map(int, input().split()))
b = max(a)
sum = 0
for i in range(n):
    sum += (a[i]/b*100)
avg = sum/n
print(avg)