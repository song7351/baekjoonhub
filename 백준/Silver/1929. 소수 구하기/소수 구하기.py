a,b = map(int, input().split())

for i in range(a, b+1):
    if i == 1:
        continue    
    k = int(i ** 0.5)
    flag = 0
    for j in range(2, k+1):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)



