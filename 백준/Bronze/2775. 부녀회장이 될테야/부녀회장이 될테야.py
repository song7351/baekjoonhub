test_case = int(input())

for i in range(test_case):
    a = int(input())
    b = int(input())
    answer = 0
    c = []
    d = []
    for i in range(1,15):
        d.append(i)
    
    for i in range(a):
        for j in range(b):
            if j == 0:
                c.append(1)
            else:
                c.append(c[j-1] + d[j])
            
        d = c
        c = []
    answer = d[b-1]
    print(answer)