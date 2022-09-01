S = list(map(int,input()))
zero_cnt = 0
one_cnt = 0

if S[0] == 0:
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        if S[i] == 0:
            zero_cnt += 1
        else:
            one_cnt += 1

print(min([zero_cnt, one_cnt]))