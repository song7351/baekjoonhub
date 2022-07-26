n, m =input().split()
n , m = int(n), int(m)
a = list(map(int, input().split()))
max_a = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if max_a < a[i] + a[j] + a[k] <= m:
                max_a = a[i] + a[j] + a[k]
print(max_a)

