n = int(input())

lst = [0] * 1000001
lst[1] = 1

for i in range(2,n+1):
    if i % 2 == 1:
        lst[i] = lst[i-1]
    else:
        lst[i] = (lst[i-1] + lst[i//2]) % 1000000000

print(lst[n])