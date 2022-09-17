import sys

def enque(n):
    global last
    last += 1
    lst[last] = n
    c = last
    p = c//2
    while p and lst[c] > lst[p]:
        lst[p], lst[c] = lst[c],lst[p]
        c = p
        p = c//2

def deque():
    global last
    tmp = lst[1]
    lst[1] = lst[last]
    last -= 1
    if last <= 0:
        last = 0
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and lst[c] < lst[c + 1]:  # 오른쪽 자식도 있고, 오른쪽자식이 더 크면
            c += 1
        if lst[p] < lst[c]:
            lst[p], lst[c] = lst[c], lst[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

N = int(sys.stdin.readline())
lst = [0] * (100000+1)
last = 0
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        enque(x)
    else:
        if not last:
            print('0')
        else:
            print(deque())