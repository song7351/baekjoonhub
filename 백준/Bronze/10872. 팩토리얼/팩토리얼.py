test_case = int(input())

def facto(a):
    if a == 1 or a == 0:
        n =1
    else:
        n = a*facto(a-1)
    return n

print(facto(test_case))
        