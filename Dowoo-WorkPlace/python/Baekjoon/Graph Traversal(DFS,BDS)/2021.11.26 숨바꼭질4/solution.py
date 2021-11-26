# https://www.acmicpc.net/problem/13913

# 문제요약
# 만나는 가장 빠른 시간을 구하라
# 두번째 줄에는 어떻게 이동해야 하는지 공백으로 구분해 출력

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 4
# 5 10 9 18 17
# 예제 입력 2 
# 5 17
# 예제 출력 2 
# 4
# 5 4 8 16 17

# 문제풀이
import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int, input().split())
visit = [0] * 100001
path = [0] * 100001

def bfs() :
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x==K :
            print(visit[x])
            ans = []
            while  x != N :
                ans.append(x)
                x = path[x]
            ans.append(N)
            print(*ans[::-1])
            return

        for i in (x-1,x+1, 2*x) :
            if 0<=i<100001 and not visit[i] :
                visit[i] = visit[x] +1
                q.append(i)
                path[i] = x

bfs()