from collections import deque

"""
2(2+3*3)+2*3
-> 2*2 + 2*3*3 + 2*3
"""

lst = list(input())
stack = deque()
ans = 0
tmp = 1

for i in range(len(lst)):
    word = lst[i]
    # 무조건 열리면 곱하기를 한다.
    if word == "(":
        tmp *= 2
        stack.append(word)
    elif word == '[':
        tmp *= 3
        stack.append(word)

    # 닫힌다면?
    elif word == ")":
        # 예외케이스는 ans = 0
        if not stack or stack[-1] == "[":
            ans = 0
            break
        # 정상적으로 닫힌다면, 2(2 + 3*3 ~
        # 2(2 -> 2*2로 바꿔서 더한다.
        if lst[i-1] == "(":
            ans += tmp
        # 무사히 바꿔서 더했다면, 그 뒤의 덧셈에 여전히 곱해야되므로 //2 를 진행한다.
        tmp //= 2
        stack.pop()
    elif word == "]":
        # 예외케이스는 ans = 0
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if lst[i-1] == "[":
            ans += tmp
        tmp //= 3
        stack.pop()

if stack:
    ans = 0

print(ans)