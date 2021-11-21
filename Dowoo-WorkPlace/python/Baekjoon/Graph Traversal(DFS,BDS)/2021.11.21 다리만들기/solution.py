# https://www.acmicpc.net/problem/2146

# 문제요약
# 두 대륙을 연결하는 방법을 찾아라

# 입력
# 첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

# 출력
# 첫째 줄에 가장 짧은 다리의 길이를 출력한다.

# 예제 입력 1 
# 10
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 0 0 0 0 1 1
# 1 0 1 1 0 0 0 0 1 1
# 0 0 1 1 1 0 0 0 0 1
# 0 0 0 1 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0

# 문제풀이

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

g = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
cnt = 1
ans = sys.maxsize # 정수의 최대수 지정
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 섬구분
def bfs1(a, b):
    global cnt
    q = deque()
    q.append((a, b))
    visit[a][b] = 1
    g[a][b] = cnt

    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            x = x1 + dx[i]
            y = y1 + dy[i]
            if 0 <= x < N and 0 <= y < N and g[x][y] == 1 and visit[x][y] == 0:
                visit[x][y] = 1
                g[x][y] = cnt
                q.append((x, y))

# 바다를 건너는 가장 짧은 거리
def bfs2(c):
    global ans
    dist = [[-1] * N for _ in range(N)] # 거리가 저장될 배열
    q = deque()

    for i in range(N):
        for j in range(N):
            if g[i][j] == c:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            x = x1 + dx[i]
            y = y1 + dy[i]

            # 갈수 없는 곳이면 계속 진행
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if g[x][y] > 0 and g[x][y] != c:
                ans = min(ans, dist[x1][y1])
                return
            # 바다 만나면 거리 1증가
            if g[x][y] == 0 and dist[x][y] == -1:
                dist[x][y] = dist[x1][y1] + 1
                q.append((x, y))

for i in range(N):
    for j in range(N):
        if not visit[i][j] and g[i][j] == 1:
            bfs1(i, j)
            cnt += 1

for i in range(1, cnt) :
    bfs2(i)

print(ans)




