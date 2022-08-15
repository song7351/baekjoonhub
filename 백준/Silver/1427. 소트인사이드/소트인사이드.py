num_list = list(map(int, input()))
N = len(num_list)
for i in range(N):
    for j in range(N-1):
        if num_list[j] < num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
num_list = map(str, num_list)
print(''.join(num_list))