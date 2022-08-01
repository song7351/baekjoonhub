a,b = map(int, input().split())

ans_list = []
for i in range(a):
    c = input()
    ans_list.append(c)

test_list = []
for i in range(b):
    d = input()
    test_list.append(d)

cnt = 0
for i in test_list:
    cnt += ans_list.count(i)

print(cnt)