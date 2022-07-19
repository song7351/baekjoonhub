a,b = input().split()
list_a = list(a)
list_b = list(b)

list_a = list(reversed(list_a))
list_b = list(reversed(list_b))

a = "".join(list_a)
b = "".join(list_b)

if a > b:
    print(a)
else:
    print(b)