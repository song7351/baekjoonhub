"""
식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고,
최솟값을 찾으세요.

어떻게 찾을까?
-> '-' 뒤에 수가 커야된다.
-> '-' 뒤 다음 '-'나올때까지 수를 전부 더한다.
-> '-'가 나올때까지 수들을 합한다.
-> 그냥 첫번째 '-'뒤는 사실 전부 '-'가 아닐까?
"""

tmp = list(input())

ans = 0
flag = 0
num = ''
for x in tmp:
    if x.isdigit():
        num += x
    else:
        # 첫번째 마이너스가 나온 이후
        if flag:
            ans -= int(num)
            num = ''
        # 첫번째 마이너스가 나오기 전
        else:
            ans += int(num)
            num = ''

        if x == '-':
            flag = 1

if flag:
    ans -= int(num)
else:
    ans += int(num)

print(ans)