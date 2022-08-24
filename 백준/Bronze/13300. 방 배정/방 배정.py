N, K = map(int, input().split())

students = {}
for _ in range(N):
    S, Y = map(int, input().split())
    if Y not in students:
        students[Y] = [S]
    else:
        students[Y].append(S)

room = 0
for i in students:
    female = 0
    male = 0
    for j in students[i]:
        if j == 0:
            female += 1
        else:
            male += 1
    if female != 0 and female % K == 0:
        room += female//K
    elif female != 0 and female % K != 0:
        room += female//K + 1
    if male != 0 and male % K == 0:
        room += male//K
    elif male != 0 and male % K != 0:
        room += male//K + 1

print(room)