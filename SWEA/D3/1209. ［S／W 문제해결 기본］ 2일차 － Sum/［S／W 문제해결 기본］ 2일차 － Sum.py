'''
모든 경우에 해당하는 합들을 구한다.
'''

for tc in range(1,10+1):     # 총 10번의 테스트
    num_board = []
    max_ans = 0 
    right_diagonal = 0
    left_diagonal = 0
    N = int(input())    # 테스트케이스 번호
    
    for i in range(100):   # 각 행마다 값을 받는다
        num_list = list(map(int, input().split()))
        right_diagonal += num_list[i]
        left_diagonal += num_list[99-i]
        num_board.append(num_list)
    
    for i in num_board:     # 가로행 합
        sum = 0
        for j in i:
            sum += j
        if sum > max_ans:
            max_ans = sum

    for i in range(100):     # 세로행 합
        sum = 0
        for j in range(100):
            sum += num_board[j][i]
        if sum > max_ans:
            max_ans = sum
            
    if right_diagonal > max_ans:
        max_ans = right_diagonal
    
    if left_diagonal > max_ans:
        max_ans = left_diagonal

    print(f"#{tc} {max_ans}")