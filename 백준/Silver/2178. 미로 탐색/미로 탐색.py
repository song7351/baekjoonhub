"""
https://www.acmicpc.net/problem/2178
1: 이동가능
0: 이동불가
규칙
1. 인접한 칸으로만 이동가능
2. 시작위치와 도착위치또한 카운트에 들어간다.
3. 미로크기 N*M일때, 1,1에서 출발해서 N,M에 도착할때 최솟값을 구하시오
"""
N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]

INF = int(1e9)
cnt_board = [[INF]*M for _ in range(N)]
cnt_board[0][0] = 1

# 우리는 0,0 -> N-1,M-1을 계산할꺼다.
# 최솟값 찾는 문제는 일단 무지성 bfs로 접근해봅시다.

q = [(0,0)]
while q:
    x,y = q.pop(0)
    cnt = cnt_board[x][y]
    for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        di = x + dx
        dj = y + dy
        if 0<= di < N and 0<= dj < M and board[di][dj] == 1:
            tmp_cnt = cnt + 1
            if tmp_cnt < cnt_board[di][dj]:
                cnt_board[di][dj] = tmp_cnt
                q.append((di,dj))

print(cnt_board[N-1][M-1])