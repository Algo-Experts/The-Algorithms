# https://www.acmicpc.net/problem/2573

# 문제요약
# 빙산이 주어지고 시간이 흐르는데 빙산이 분리되는 최초의 시간을 출력
# 물과 접촉한 갯수만큼 줄어듬

# 입력
# 첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

# 출력
# 첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

# 예제 입력 1 
# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0
# 예제 출력 1 
# 2

# 문제풀이
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) 
g = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
year = 0

def bfs(a,b) : 
    q = deque()
    q.append((a,b))
    visit[a][b] = 1
    
    while q :     
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]
            if 0 <= x < N and 0 <= y < M and visit[x][y] == 0 :
                if g[x][y] != 0 :
                    visit[x][y] = 1
                    q.append((x,y))
                elif g[x][y] == 0 :
                    count[x1][y1] += 1
    return 1

# 빙산이 분리될때까지 돌림
while True : 
    visit = [[0]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    res = []
    for i in range(N) :
        for j in range(M) :
            if g[i][j] != 0 and visit[i][j] == 0 :
                res.append(bfs(i,j))
    # 빙산 깍아줌
    for i in range(N) :
        for j in range(M) :
            g[i][j] -= count[i][j]
            if g[i][j] < 0:
                g[i][j] = 0
    if len(res) == 0 : # 빙산이 다 없어지면 0출력
        year = 0
        break
    if len(res) >= 2 : # 빙산 분리되면 분리
        break
    year += 1

print(year)


            

