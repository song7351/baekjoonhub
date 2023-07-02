"""
상하좌우 벽을 무조건 친다.
그렇기때문에 해당 벽을 기준으로 대칭좌표값으로 넘겼을때의 최단거리가 나온다.

a,b
y=n 대칭 a,(n-b)+n
y=0 대칭 a, -b
x=m 대칭 (m-a)+m, b
x=0 대칭 -a,b
"""
def solution(m, n, startX, startY, balls):
    answer = []
    x,y = startX,startY
    for a,b in balls:
        tmp_k,k1,k2,k3,k4 = int(1e15),int(1e15),int(1e15),int(1e15),int(1e15)
        if not (x == a and y > b):
            k1 = (x-a)**2 + (y-(-b))**2         # 아래 반전
        if not (x == a and y < b):
            k2 = (x-a)**2 + (y-((n-b)+n))**2    # 위 반전
        tmp_k = min(tmp_k, k1, k2)
        if not (y == b and a < x):
            k3 = (x-(-a))**2 + (y-b)**2         # 왼쪽 반전
        if not (y == b and a > x):
            k4 = (x-((m-a)+m))**2 + (y-b)**2    # 오른쪽 반전
        tmp_k = min(tmp_k, k3, k4)
        answer.append(tmp_k)
        
    return answer