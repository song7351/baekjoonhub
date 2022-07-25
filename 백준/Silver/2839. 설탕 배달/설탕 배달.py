a = int(input())
cnt = 0
while a%5 != 0:
    a = a-3
    cnt += 1
    if a < 0:
        break
cnt += a//5
if a%5 == 0:
    print(cnt)
else:
    print(-1)