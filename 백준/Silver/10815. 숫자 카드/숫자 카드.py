N = int(input())
n_list = set(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1, end=" ")
    else:
        print(0, end=" ")