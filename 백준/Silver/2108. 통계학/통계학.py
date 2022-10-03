import sys
N = int(input())

lst = []
dict_N = dict()

for _ in range(N):
    i = int(sys.stdin.readline())
    lst.append(i)
    if i not in dict_N:
        dict_N[i] = 1
    else:
        dict_N[i] += 1

lst.sort()

print(round(sum(lst)/N))
print(lst[N//2])

#print(dict_N)
sorted_N = sorted(dict_N.items(), key=lambda x:(-x[1],x[0]))

#print(dict_N.items())

if N == 1:
    print(lst[0])
else:
    if sorted_N[0][1] == sorted_N[1][1]:
        print(sorted_N[1][0])
    else:
        print(sorted_N[0][0])
print(lst[-1] - lst[0])