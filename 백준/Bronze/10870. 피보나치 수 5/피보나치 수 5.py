a = int(input())

def fibo(a):
    if a < 2:
        b = a
    else:
        b = fibo(a-1) + fibo(a-2)
    return b

print(fibo(a))