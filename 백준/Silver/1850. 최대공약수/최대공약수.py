"""
a,b 최대 공약수를 구하라
단 a,b는 1의 개수다
즉, 3,5가 주어짐ㄴ 111, 11111의 최대 공약수를 구하라

"""
import math

a,b = map(int, input().split())
c = math.gcd(a,b)
print('1'*c)