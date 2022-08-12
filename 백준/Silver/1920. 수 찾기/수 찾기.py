import sys

N = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

def binarysort(arr, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return 1
        elif arr[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return 0

for target in m_list:
    print(binarysort(n_list, target, 0, N-1))
