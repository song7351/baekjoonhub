N = int(input())                            # 수열의 길이
num_list = list(map(int, input().split()))  # 수열
max_cnt = 1     # 최고길이
big_cnt = 1     # 커지는 단발성 길이
small_cnt = 1   # 작아지는 단발성 길이

for i in range(N-1):
    if num_list[i] == num_list[i+1]:        # 연속해서 같을 경우
        big_cnt += 1
        small_cnt += 1
        if big_cnt > max_cnt:
            max_cnt = big_cnt
        if small_cnt > max_cnt:
            max_cnt = small_cnt

    if num_list[i] < num_list[i+1]:         # 연속해서 커질 경우
        big_cnt += 1
        small_cnt = 1
        if big_cnt > max_cnt:
            max_cnt = big_cnt

    if num_list[i] > num_list[i+1]:         # 연속해서 작아질 경우
        big_cnt = 1
        small_cnt += 1
        if small_cnt > max_cnt:
            max_cnt = small_cnt

print(max_cnt)