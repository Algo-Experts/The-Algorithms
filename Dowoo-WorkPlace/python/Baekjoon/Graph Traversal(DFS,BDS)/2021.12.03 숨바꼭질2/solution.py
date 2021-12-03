# https://www.acmicpc.net/problem/12851

# 문제요약
# 가장 빠른 시간이 몇초인지
# 몇가지 방법인지 구하라

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 4
# 2

# 문제풀이
# 숨바꼭질문제이다
# 이번엔 방법의 갯수를 구하는 것

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
g = [-1] * 100001
cnt = 0

def bfs() :
    global cnt
    q = deque()
    q.append(N)
    g[N] = 0
    
    while q:
        x = q.popleft()
        if x==K:
            cnt+=1 #어떤 방법으로든 도착했을 경우 +1증가
        for y in [x*2, x+1, x-1]:
            if 0 <= y < 100001:
                if g[y]==-1 or g[y]>=g[x]+1:
                    g[y]=g[x]+1
                    q.append(y)

bfs()
print(g[K])
print(cnt)