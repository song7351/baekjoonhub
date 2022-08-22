N = int(input())

students = []

# 학생들 순서 생성
for i in range(1, N+1):
    students.append(i)

# 번호표 발부
waiting = list(map(int, input().split()))
ans = []
for i in range(N):
    if waiting[i] == 0:
        ans.append(students[i])
    else:
        ans.insert(i - waiting[i], students[i])

ans = map(str, ans)

print(' '.join(ans))