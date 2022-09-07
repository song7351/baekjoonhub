N = list(map(int, input()))
n = len(N)
sum_a = 0

for i in range(n//2):
    sum_a += N[i]

if sum(N)-sum_a == sum_a:
    print('LUCKY')
else:
    print('READY')