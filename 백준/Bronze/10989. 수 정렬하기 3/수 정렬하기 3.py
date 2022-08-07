import sys

test_case = int(input())

num_list = [0] * (10000+1)
for i in range(test_case):
    num = int(sys.stdin.readline())
    num_list[num] += 1
    
for i in range(10000+1):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)