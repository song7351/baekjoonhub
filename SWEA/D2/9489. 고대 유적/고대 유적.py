test_case = int(input())
 
for tc in range(1,test_case+1):
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    
    max_cnt = 0
    for i in range(N):
        cnt = 1
        for j in range(M-1):
            if num_list[i][j] == num_list[i][j+1] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            if num_list[i][j] != num_list[i][j+1]:     
                cnt = 1
                if cnt > max_cnt:
                    max_cnt = cnt
                    
    for i in range(M):
        cnt = 1
        for j in range(N-1):
            if num_list[j][i] == num_list[j+1][i] == 1: 
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            if num_list[j][i] != num_list[j+1][i]:
                cnt = 1
                if cnt > max_cnt:
                    max_cnt = cnt
                    
    print(f"#{tc} {max_cnt}")