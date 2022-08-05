test_case = int(input())

total_list = []
for i in range(test_case):
    h,w = map(int,input().split())
    a = (h,w)
    total_list.append(a)

for i in range(test_case):
    r = 1
    for j in range(test_case):
        if total_list[i][0] < total_list[j][0] and total_list[i][1] < total_list[j][1]:
            r += 1
    print(r, end=" ")