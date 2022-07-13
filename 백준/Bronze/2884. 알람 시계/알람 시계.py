H,M=map(int,input().split())

time= 60*H+M-45
H=time//60
M=time%60

if H == -1:
	H = 23
	
print(H, M)
