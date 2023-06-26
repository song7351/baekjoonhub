"""
https://ksb-dev.tistory.com/214
참고로, 문제에서 주어지는 range의 [0]과 [1]의 값은 시작과 끝 까지 부터 떨어진 값(Offset)입니다.

k가 6인 상태에서
range[0,0]이라면, [0, 6-0]입니다.
range[1,-2]이라면, [0+1, 6-2]입니다.
range의 [0]을 a라 하고, [1]을 b라고 했을 때, 문제 조건에 의해 a는 양의 정수, b는 음의 정수만 주어집니다.

ㅅㅂ; 이걸 설명하는 블로그가 여기 하나뿐이다. 저거아니면 내가 range값을 어떻게 이해하냐고
a,b -> x=a, x=b 라면서 
"""


def solution(k, ranges):
    answer = []
    lst = [k]
    lst2 = [0]

    def f():
        while lst[-1] != 1:
            a = lst[-1]
            if a % 2 == 0:
                a //= 2
            elif a % 2 == 1:
                a = a * 3 + 1
            lst.append(a)

    def f1():
        n = len(lst)
        for i in range(n - 1):
            tmp = lst2[-1] + (lst[i] + lst[i + 1]) / 2
            lst2.append(tmp)

    f()
    f1()
    n = len(lst)
    
    for s, e in ranges:
        s, e = 0 + s, n-1 + e
        if s > e:
            answer.append(-1.0)
            continue

        answer.append(lst2[e] - lst2[s])
    return answer