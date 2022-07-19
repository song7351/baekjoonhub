a = input()
b = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
n = 0
for i in b:
    if i in a:
        if a.count(i) > 1:
            n += (a.count(i)-1)
        a = a.replace(i,"!")
        n += 1
        
c = list(a)
c = len(c) - c.count("!")
n = c+n
print(n)