import sys


test_case = int(input())

num_list = []
for i in range(test_case):
    a = int(sys.stdin.readline())
    num_list.append(a)

num_list.sort()

for i in num_list:
    print(i)