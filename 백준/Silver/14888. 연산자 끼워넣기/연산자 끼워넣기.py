"""
N개의 수로 이루어진 수열
N-1개의 연산자
이때, 주어진 수의 순서를 바꾸면 안 된다.
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
나눗셈은 무조건 정수의 몫
음수의 경우 양수로 바꾼뒤 나눈 몫을 음수로 바꿈

1줄: N
2줄: 수열
3줄:  덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
"""
from itertools import permutations

N = int(input())
lst = list(map(int, input().split()))
lst_op = list(map(int, input().split()))
op = ['+']*lst_op[0] + ['-']*lst_op[1] + ['*']*lst_op[2] + ['//']*lst_op[3]
new_op = list(permutations(op,N-1))
new_op = list(set(new_op))
#print(new_op)
ans_lst = []
for op1 in new_op:
    ans = lst[0]
    for i in range(N-1):
        if op1[i] == '+':
            ans += lst[i+1]
        elif op1[i] == '-':
            ans -= lst[i+1]
        elif op1[i] == '*':
            ans *= lst[i+1]
        else:
            if ans <0:
                ans = -ans
                ans = ans//lst[i+1]
                ans = -ans
            else:
                ans = ans//lst[i+1]
    ans_lst.append(ans)
    
print(max(ans_lst))
print(min(ans_lst))