"""
1줄: N 입력수
N줄: a b c   부모노드/왼자식/오른자식   없으면 온점으로 표시
노드의 이름은 A부터 차례대로 알파벳 대문자로
"""
def preorder(n):
    if 64<n <=65+N:
        print(par[n],end='')
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if 64<n <=65+N:
        inorder(ch1[n])
        print(par[n],end='')
        inorder(ch2[n])

def postorder(n):
    if 64<n <=65+N:
        postorder(ch1[n])
        postorder(ch2[n])
        print(par[n],end='')

N = int(input())

par = [''] * (90+1)
ch1 = [''] * (90+1)
ch2 = [''] * (90+1)
idx = 1
for _ in range(N):
    a,b,c = map(ord, input().split())
    par[a] = chr(a)
    ch1[a] = b
    ch2[a] = c

#알파벳(대문자)은 65 ~ 90까지이다
preorder(65)
#ABDCEFG
print()
inorder(65)
#DBAECFG
print()
postorder(65)
#DBEGFCA