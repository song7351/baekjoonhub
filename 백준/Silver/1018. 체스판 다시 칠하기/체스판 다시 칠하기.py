n,m = map(int, input().split())

# (n,m)이 (0,0)을 기준으로 8칸을 테스트한다.
# 다음엔 (1,0)을 기준으로 (9,8) 8칸을 테스트한다...
# 각 테스트 결과가 min_ans = 64 (최대 8*8 64칸이 틀린다.)보다 작다면,
# min_ans를 교체하고 반복문이 끝난다면, min_ans를 print()한다.

min_ans = 64 #최소값
total_board = [] #전체 입력한 보드판. 각 i번째 요소는 각 행을 의미.
for i in range(n):
    #행별 입력단어를 list로 저장
    n_word = list(input())
    #total_board에 추가
    total_board.append(n_word)
    
#total_board완성.
#print(total_board)

# (n,m)이 (0,0)을 기준으로 8칸을 테스트한다.
# 다음엔 (1,0)을 기준으로 (9,8) 8칸을 테스트한다...
for k in range(n-7):
    for i in range(m-7):
        cnt = 0
        #시작단어 확인
        #시작단어가 B일때
        # 8*8 한번 검사.
        for h in range(k,k+8):
            for j in range(i, i+8):
                #검사 실행
                if (h+j-k-i)%2 == 0 and total_board[h][j] == 'W':
                    cnt += 1
                elif (h+j-k-i)%2 == 1 and total_board[h][j] == 'B':
                    cnt += 1
        # 8*8 검사결과가 끝나고 cnt가 min_ans보다 작다면 최소값을 바꿔줌
        if cnt < min_ans:
            min_ans = cnt
    #시작단어가 W일떄
        # 8*8 한번 검사.
        cnt = 0
        for h in range(k,k+8):
            for j in range(i, i+8):
                #검사 실행
                if (h+j-k-i)%2 == 0 and total_board[h][j] == 'B':
                    cnt += 1
                elif (h+j-k-i)%2 == 1 and total_board[h][j] == 'W':
                    cnt += 1
        # 8*8 검사결과가 끝나고 cnt가 min_ans보다 작다면 최소값을 바꿔줌
        if cnt < min_ans:
            min_ans = cnt
print(min_ans)
