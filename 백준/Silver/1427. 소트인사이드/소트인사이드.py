n = list(input())
n_lst = list(map(int, n))
n_lst.sort(reverse=True)
n_lst = list(map(str, n_lst))
print(''.join(n_lst))
