N = int(input())
num_list = list(map(int, input().split()))
x = int(input())
num_list.sort()
left = 0
right = N - 1
cnt = 0
while left < right:
    check = num_list[left] + num_list[right]
    if check == x:
        cnt += 1
    if check < x:
        left += 1
        continue
    right -= 1
print(cnt)