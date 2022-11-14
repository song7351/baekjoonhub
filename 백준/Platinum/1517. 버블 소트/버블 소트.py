"""
버블정렬이 몇번 발생하는가?
8
3 2 8 1 7 4 5 6

"""
import sys
input = sys.stdin.readline

def merge_sort(s,e):
    global cnt
    if e-s < 1:
        return

    m = int(s + (e-s) / 2)
    merge_sort(s,m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]

    k = s
    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
            cnt += m - index1 + 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1


    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

n = int(input())
A = [0] + list(map(int, input().split()))
tmp = [0] * int(n+1)

cnt = 0
merge_sort(1,n)
print(cnt)