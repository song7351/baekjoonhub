N, M = map(int, input().split())
#N 은 사람수, M은 수상인원
score_list = list(map(int, input().split()))

for i in range(M):
    for j in range(i+1,N):
        if score_list[i] < score_list[j]:
            score_list[i], score_list[j] = score_list[j], score_list[i]

print(score_list[M-1])