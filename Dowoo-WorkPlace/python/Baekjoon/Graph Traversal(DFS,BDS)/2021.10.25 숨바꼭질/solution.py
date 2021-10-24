# https://www.acmicpc.net/problem/1697

# 수빈이의 위치가 x일때 걸으면 1초 후 x-1 또는 x+1
# 순간이동 하면 1초 후 2*x로 이동함
# 수빈이와 동생의 위치가 주어졌을 때 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 인가

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 4

# 문제풀이
# 최단초 찾기 이므로 BFS로 풀어야함

from collections import deque
import sys

def bfs():
    q = deque()
    q.append(N)

    while(q):
        x = q.popleft()
        if x == K : # 같으면 출력!
            print(d[x])
            break
        
        for i in (x-1,x+1,x*2) :
            if 0<=i<=100000 and not d[i] : # 했던것은 포함하지 않음
                d[i] = d[x] +1 # 기존에 +1를 해줘야함
                q.append(i)
            
N, K = map(int,sys.stdin.readline().split())
d = [0] * 100001 # 맥스가 100000이므로
bfs()
