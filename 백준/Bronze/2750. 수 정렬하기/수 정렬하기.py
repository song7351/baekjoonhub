a = int(input())

n = []
for i in range(a):
    b = int(input())
    n.append(b)
n.sort()

for i in range(a):
    print(n[i])