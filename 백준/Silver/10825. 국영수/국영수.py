"""
학생이름, 국어, 영어, 수학 점수를 입력받는다.
기준 1. 국어 내림차순
기준 2. 영어 오름차순
기준 3. 수학 내림차순
기준 4. 이름 오름차순
"""

N = int(input())
lst = []
for i in range(N):
    name, x, y, z = input().split()
    x,y,z = int(x), int(y), int(z)
    lst.append([name,x,y,z])

lst.sort(key=lambda a:(-a[1],a[2],-a[3],a[0]))

for i in lst:
    print(i[0])