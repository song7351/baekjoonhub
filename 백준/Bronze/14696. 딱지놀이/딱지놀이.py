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

    if a_ttagi == b_ttagi:
        print("D")
    elif a_ttagi[2:] == b_ttagi[2:]:
        if a_ttagi[1] > b_ttagi[1]:
            print("A")
        else:
            print("B")
    elif a_ttagi[3:] == b_ttagi[3:]:
        if a_ttagi[2] > b_ttagi[2]:
            print("A")
        else:
            print("B")
    elif a_ttagi[4] == b_ttagi[4]:
        if a_ttagi[3] > b_ttagi[3]:
            print("A")
        else:
            print("B")
    else:
        if a_ttagi[4] > b_ttagi[4]:
            print("A")
        else:
            print("B")