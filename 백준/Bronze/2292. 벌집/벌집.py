a = int(input())
ans = 0
x = 1
while True:
    if a <= (1+3*x*(x-1)):
        ans = x
        break
    x += 1

print(ans)