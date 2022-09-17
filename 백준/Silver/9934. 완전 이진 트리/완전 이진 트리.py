"""
깊이가 K인 **완전 이진 트리**를 이루고 있다.
깊이가 K인 완전 이진 트리는 총 2^K-1개의 노드
중위순회 결과물을 보여주고 각 깊이 레벨별 노드값을 출력하라
1줄: K
2줄: 중위순회방문 결과물
"""
def inorder(n):
    global idx, depth
    if n <= 2**K-1:
        depth += 1      # 자식노드로 들어갈때는 깊이가 증가
        inorder(2*n)
        depth -= 1      # 왼쪽자식노드 끝나면 부모노드를 해야되므로 깊이 감소
        level[depth].append(lst[idx])
        idx += 1        # 출력했으면 다음 인덱스로 넘어감
        depth += 1      # 오른쪽 자식노드로 들어감. 깊이증가
        inorder(2 * n + 1)
        depth -= 1      # 오른쪽 자식노드 끝나면 다시 부모로 넘어가기 위해서 깊이 감소

K = int(input())
lst = list(map(int, input().split()))
level = [[] for _ in range(K+1)]
depth = 1
idx = 0
inorder(1)
for item in level[1:]:
    for i in item:
        print(i, end=' ')
    print()