a, b = input().split()
a= int(a)
b= int(b)
c = int(input())
d = b+c
while d >= 60:
    d -= 60
    a += 1
while a >=24:
    a -= 24
print(a,d)
   
