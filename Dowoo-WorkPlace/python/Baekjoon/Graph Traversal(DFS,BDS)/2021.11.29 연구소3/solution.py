# https://www.acmicpc.net/problem/17142

# 문제요약
# 바이러스가 퍼짐
# 바이러스는 비활성화 되어있는데 활성화 시키는 갯수가 주어진 후
# 모든 빈칸에 바이러스가 퍼지는 최소의 시간을 구함
# 0빈칸 1벽 2바이러스

# 입력
# 첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

# 둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

# 출력
# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.

# 예제 입력 1 
# 7 3
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 2 0 1 1
# 0 1 0 0 0 0 0
# 2 1 0 0 0 0 2
# 예제 출력 1 
# 4

# 문제풀이
# 경우의 수를 구해야하는 어려운 문제임
# dfs bfs 둘다 사용해야하나
# 파이썬에서 combinations을 사용하면 쉽게 가능

from itertools import combinations as com
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = []
q = []
b = 0
inf = 100000000
result = inf
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]

# 맵정보 받아서 바이러스정도 넣어줌
for i in range(n):
    a = list(map(int, input().split()))
    g.append(a)
    for j in range(n):
        if a[j] == 2: q.append([i, j])
        if a[j] != 1: b += 1

# 바이러스 퍼트림
def bfs():
    while a:
        x, y = a.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and g[nx][ny] != 1:
                visit[nx][ny] = 1
                a.append([nx, ny])
                cs[nx][ny] = cs[x][y] + 1


cq = list(com(q, m))

for i in cq:
    cs = [[-1] * n for i in range(n)]
    visit = [[0] * n for i in range(n)]
    a = deque()
    for x, y in i:
        visit[x][y] = 1
        cs[x][y] = 0
        a.append([x, y])
    bfs()
    cnt = 0
    for j in visit: cnt += j.count(1)
    if b == cnt:
        max_n = 0
        for j in range(n):
            for k in range(n):
                if g[j][k] != 1 and [j, k] not in q:
                    max_n = max(max_n, cs[j][k])
        result = min(result, max_n)
        
print(result if result != inf else -1)
