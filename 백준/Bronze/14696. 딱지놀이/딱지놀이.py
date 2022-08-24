N = int(input())

for _ in range(N):
    a_ttagi = [0] * 5
    b_ttagi = [0] * 5
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 세모(1), 네모(2), 동그라미(3), 별(4)
    for i in range(1, len(A)):
        a_ttagi[A[i]] += 1
    for i in range(1, len(B)):
        b_ttagi[B[i]] += 1

    cnt = 0
    for i in range(4, 0, -1):
        if a_ttagi[i] == b_ttagi[i]:
            cnt += 1
        else:
            if a_ttagi[i] > b_ttagi[i]:
                ans = 'A'
            else:
                ans = 'B'
            break

    if cnt == 4:
        print('D')
    else:
        print(ans)