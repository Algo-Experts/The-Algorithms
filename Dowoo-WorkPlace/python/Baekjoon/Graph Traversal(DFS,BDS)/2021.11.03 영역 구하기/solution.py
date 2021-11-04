# https://www.acmicpc.net/problem/2583

# 문제요약
# K개의 직사각형을 그릴때 나머지 부분이 몇개의 영역으로 분리되는지
# 구하는 문제

# 입력
# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

# 출력
# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

# 예제 입력 1 
# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2
# 예제 출력 1 
# 3
# 1 7 13

# 문제풀이
# 단지번호 붙이기와 비슷한 느낌이다
# BFS로 찾는다

import sys
from collections import deque

M,N,K = map(int, sys.stdin.readline().split())
g = [[0]*N for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
r = [] # 결과저장

for _ in range(K) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2): # y1~y2까지
        for j in range(x1, x2): # x1~x2까지
            g[i][j] = 1 # 해당범위를 1로 채움

def bfs(a,b): # 맨날 헸던 bfs
    g[a][b] = 1
    q = deque()
    q.append((a,b))
    cnt = 1
    while q:
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]

            if 0 <= x < M and 0<= y < N and g[x][y] == 0: 
                q.append((x,y))
                g[x][y] = 1
                cnt += 1 # +1씩 해줌
    return cnt # 지역의 갯수를 알아야 하기때문에 

for i in range(M) :
     for j in range(N):
        if g[i][j] == 0:
            r.append(bfs(i, j))

print(len(r)) # 길이 = 갯수
print(*sorted(r)) # *풀어서 오름차순으로 출력
