# https://www.acmicpc.net/problem/2589

# 문제요약
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두곳에 나뉘어 묻혀있다.
# 즉 최단거리로 계산했을 때 가장 최장길이 구하기

# 입력
# 첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.

# 출력
# 첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.

# 예제 입력 1 
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW
# 예제 출력 1 
# 8

# 문제풀이
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
g = [list(input().rstrip()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

def bfs(i,j) :
    q = deque()
    q.append((i,j))
    max_n = 0
    while q:
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]
            if 0 <= x < N and 0 <= y < M and visit[x][y] == 0 and g[x][y] != "W":
                visit[x][y] = 1
                g[x][y] = g[x1][y1] +1
                # 최대값 저장
                max_n = max(max_n, g[x][y])
                q.append((x,y))
    return max_n

# 하나씩 다 돌아가며 최대를 구하고 그중의 최대값을 구함
for i in range(N) :
    for j in range(M) :
        if g[i][j] != "W" :
            visit = [[0]*M for _ in range(N)]
            g[i][j] = 0
            visit[i][j] = 1
            res = max(res,bfs(i,j)) 

print(res)



