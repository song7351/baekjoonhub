a = int(input())

for i in range(a):
    b = str(i)
    list_b = list(map(int, b))
    b = int(b)
    sum_b = sum(list_b)+b
    if sum_b == a:
        print(b)
        break
else:
    print(0)
