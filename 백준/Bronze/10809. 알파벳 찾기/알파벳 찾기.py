#기본리스트
a = [-1]*26

#입력리스트
b = list(input())

#리스트 길이
c = len(b)

for i in range(c):
    #기존리스트 인덱스
    d = ord(b[i])-ord('a')
    if a[d] == -1:
        a[d] = i

print(*a)