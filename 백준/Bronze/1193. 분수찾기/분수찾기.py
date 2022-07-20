a = int(input())
x = 1
max = 0

while True:
    if a <= x*(x+1)*0.5:
        max = x*(x+1)*0.5
        break
    x += 1

#분자
b = int(x-(max-a))
#분모
c = int(1+(max-a))
if x%2 == 0:
    print(f"{b}/{c}")
elif x%2 == 1:
    print(f"{c}/{b}")