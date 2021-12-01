# https://www.acmicpc.net/problem/1600

# 문제요약
# 말처럼 움직이는 것은 k번만 가능
# 그 뒤로 인접한 칸으로 이동가능
# 최소의 동작으로 도착지점까지가라

# 입력
# 첫째 줄에 정수 K가 주어진다. 둘째 줄에 격자판의 가로길이 W, 세로길이 H가 주어진다. 그 다음 H줄에 걸쳐 W개의 숫자가 주어지는데, 0은 아무것도 없는 평지, 1은 장애물을 뜻한다. 장애물이 있는 곳으로는 이동할 수 없다. 시작점과 도착점은 항상 평지이다. W와 H는 1이상 200이하의 자연수이고, K는 0이상 30이하의 정수이다.

# 출력
# 첫째 줄에 원숭이의 동작수의 최솟값을 출력한다. 시작점에서 도착점까지 갈 수 없는 경우엔 -1을 출력한다.

# 예제 입력 1 
# 1
# 4 4
# 0 0 0 0
# 1 0 0 0
# 0 0 1 0
# 0 1 0 0
# 예제 출력 1 
# 4
# 예제 입력 2 
# 2
# 5 2
# 0 0 1 1 0
# 0 0 1 1 0
# 예제 출력 2 
# -1

# 문제풀이
# 말의 움직임 먼저 다 써야만 가능하다고 생각했는데
# 그럴 필요가 없었음. 그래서 오래걸렸다

from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
s = [list(map(int, input().split())) for i in range(h)]

# 일반이동 
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# k번만큼 말처럼
d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
d2 = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    q = deque()
    q.append((0, 0, k))
    # 3차배열인 이유는 k의 갯수가 정해져있기 때문
    visit = [[[0 for i in range(31)] for i in range(w)] for i in range(h)] 
    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1: 
            return visit[x][y][z]
        
        # 여기서 중요한 포인트는 말의 움직임을 먼저 다 쓸필요가 없음

        for i in range(4): # 원숭이
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z] == 0:
                visit[nx][ny][z] = visit[x][y][z] + 1 # 시간의 흐름에 따라 1더해줌
                q.append((nx, ny, z))
        
        if z > 0: # 말처럼
            for i in range(8):
                nx = x + d1[i]
                ny = y + d2[i]
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z - 1] == 0:
                    visit[nx][ny][z - 1] = visit[x][y][z] + 1 # z-1에 더해줌 1차감해야함
                    q.append((nx, ny, z - 1))
    return -1

print(bfs())