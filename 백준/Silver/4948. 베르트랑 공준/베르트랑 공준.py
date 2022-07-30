import sys

def isprime(a):
    if a == 1:
        return False
    k = int(a ** 0.5) + 1
    for i in range(2, k):
        if a%i == 0:
            return False
    else:
        return True

all_list = list(range(1*2,123456*2))
sosu_list = []
for i in all_list:
    if isprime(i):
        sosu_list.append(i)

while True:
    test = int(sys.stdin.readline())
    cnt = 0
    if test == 0:
        break
    
    for i in sosu_list:
        if test < i <= 2*test:
            cnt += 1
    print(cnt)