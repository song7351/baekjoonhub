import sys
N = int(sys.stdin.readline())
num_list = [False] * 2000001
for i in range(N):
    num_list[int(sys.stdin.readline())] = True
print('\n'.join([str(num) for num in range(-1000000 , 1000001) if num_list[num] == True]))
'''
<참고용> 
최초에 해당 범위 리스트 False를 만들고 받는 값들을 전부받고 True인 값들만
출력한다면? 이게 왜 더 빠르지...?
import sys
N = int(sys.stdin.readline())
num_list = [False] * 2000001
for i in range(N):
    num_list[int(sys.stdin.readline())] = True
print('\n'.join([str(num) for num in range(-1000000 , 1000001) if num_list[num] == True]))
'''