#https://www.acmicpc.net/problem/13549

# 문제요약
# 1초 +1 -1 / 0초에 2*X
# 최단시간 구하기

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 2

# 문제풀이
import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int, input().split())
g = [0] * 100001

def bfs() :
    q = deque()
    q.append((N))
    while q:
        x = q.popleft()
        if x==K :
            return g[x]
        for i in (x-1,x+1, 2*x) :
            if 0<=i<100001 and not g[i] :
                if i == 2*x and x !=0 :
                    g[i] = g[x]
                    q.appendleft(i)
                else :
                    g[i] = g[x] +1
                    q.append(i)
print(bfs()) 