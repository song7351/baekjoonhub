ans = int(input())
cnt = 0
num = 665
while True:
    num = str(num)
    if "666" in num:
        cnt += 1
        if cnt  == ans:
            break
    num = int(num) + 1

print(num)