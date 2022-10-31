n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
lst2 = [x/m*100 for x in lst]
print(sum(lst2)/n)