a = list(input())

time = 0
for i in a:
    if ord(i) < ord('D'):
        time += 3
    elif ord(i) < ord('G'):
        time += 4
    elif ord(i) < ord('J'):
        time += 5
    elif ord(i) < ord('M'):
        time += 6
    elif ord(i) < ord('P'):
        time += 7
    elif ord(i) < ord('T'):
        time += 8
    elif ord(i) < ord('W'):
        time += 9
    else:
        time += 10

print(time)