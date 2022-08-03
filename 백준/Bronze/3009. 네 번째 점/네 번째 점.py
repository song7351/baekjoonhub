x_list = []
y_list = []
for i in range(3):
    a,b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)

for i in x_list:
    if x_list.count(i) == 1:
        print(i, end=" ")

for j in y_list:
    if y_list.count(j) == 1:
        print(j, end=" ")
    