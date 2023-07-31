n = int(input())
lst = [0] * (n+1)

for i in range(n):
    lst[i+1] = int(input())

ans = []

def dfs(now, start, lst1, lst2):
    if now not in lst1 and lst[now] not in lst2:
        lst1.append(now)
        lst2.append(lst[now])
        return dfs(lst[now],start, lst1, lst2)
    else:
        lst1.sort()
        lst2.sort()
        if lst1 == lst2:
            return lst1
        else:
            return []


for i in range(1, n+1):
    if i == lst[i]:
        ans.append(lst[i])
        continue

    if i not in ans:
        ans += dfs(i, i, [], [])

ans.sort()

print(len(ans))
for x in ans:
    print(x)