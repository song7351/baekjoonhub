import math

def find1(a,b,c,d):
    if int(d) == 0:
        return 0
    else:
        for x in range(0,1000001):
            aa,bb,cc = a*x*x*x , b*x*x , c*x
            if aa + bb + cc + d == 0:
                return x
            elif -aa + bb -cc + d == 0:
                return -x

for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    n = find1(a,b,c,d)
    ans = set()

    A = a
    B = b + A*n
    C = c + B*n
    bb4ac = B*B - (4*A*C)
    if bb4ac >= 0:
        n2 = (-B + math.sqrt(bb4ac))/(2*A)
        n3 = (-B - math.sqrt(bb4ac))/(2*A)
        ans.add(n2)
        ans.add(n3)

    ans.add(n)
    ans = list(ans)
    ans.sort()
    for x in ans:
        print("{:.4f}".format(x), end=" ")
    print()