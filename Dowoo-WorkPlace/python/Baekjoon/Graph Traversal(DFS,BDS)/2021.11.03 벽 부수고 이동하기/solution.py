# https://www.acmicpc.net/problem/2206

# 문제요약
# 0은 이동 1은 벽
# 1,1에서 N,M까지 최단경로로 이동함
# 벽은 1개까지 부실 수 있다. 

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

# 예제 입력 1 
# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000
# 예제 출력 1 
# 15
# 예제 입력 2 
# 4 4
# 0111
# 1111
# 1111
# 1110
# 예제 출력 2 
# -1

# 문제풀이
# 최단거리를 물었기 때문에 bfs로 풀어야함
# 어려운 문제아님 벽을 허무는 방법을 생각헤 내야함

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, list(input().strip()))) for _ in range(N)] 
# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 1)) # 처음위치 0,0 + 1은 벽을 뚫을 수 있음
    v = [[[0] * 2 for i in range(M)] for i in range(N)] # 방문
    v[0][0][1] = 1 # 처음위치에 방문표시
    while q:
        a, b, w = q.popleft()
        
        if a == N - 1 and b == M - 1: # 끝에 도달했을 경우 완료
            return v[a][b][w]

        for i in range(4): # 아닐경우 반복함
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if maps[x][y] == 1 and w == 1: # 벽이 있는 경우 뚫어버리고  +1 함
                    v[x][y][0] = v[a][b][1] + 1
                    q.append([x, y, 0])
                elif maps[x][y] == 0 and v[x][y][w] == 0: # 벽이 아닌경우
                    v[x][y][w] = v[a][b][w] + 1 # 그냥 +1해줌
                    q.append([x, y, w])
    return -1 # 못가면 -1을 출력

print(bfs())