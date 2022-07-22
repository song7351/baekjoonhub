m = int(input())

for i in range(m):
    h, w, n = map(int, input().split())
    if n%h == 0:
        front_a = str(h)
        back_a = n//h
    else:
        front_a = str(n%h)
        back_a = n//h + 1
    
    if back_a < 10:
        back_a = '0'+str(back_a)
    else:
        back_a = str(back_a)
    
    print(front_a + back_a)
    
    