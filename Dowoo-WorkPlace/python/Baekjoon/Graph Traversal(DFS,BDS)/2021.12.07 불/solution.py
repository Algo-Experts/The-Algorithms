# https://www.acmicpc.net/problem/5427

# 문제요약
# 빌딩을 얼마나 빨리 탈출하는가 

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

# 각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

# 다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
# 각 지도에 @의 개수는 하나이다.

# 출력
# 각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

# 예제 입력 1 
# 5
# 4 3
# ####
# #*@.
# ####
# 7 6
# ###.###
# #*#.#*#
# #.....#
# #.....#
# #..@..#
# #######
# 7 4
# ###.###
# #....*#
# #@....#
# .######
# 5 5
# .....
# .***.
# .*@*.
# .***.
# .....
# 3 3
# ###
# #@#
# ###
# 예제 출력 1 
# 2
# 5
# IMPOSSIBLE
# IMPOSSIBLE
# IMPOSSIBLE

# 문제풀이 
# 예전 탈출과 같은 맥락의 문제
# 불과 사람이 같이 움직일 때 보관할 수 있는 것을 만들어줌

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global q, f
    while q: 
        temp = deque() # 한차례씩 이동해야 하므로 만들어줌
        while q:
            x, y = q.popleft()
            if (x == h - 1 or y == w - 1 or x == 0 or y == 0) and s[x][y] != "*": 
                return s[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "." and s[x][y] != "*":
                    s[nx][ny] = s[x][y] + 1
                    temp.append([nx, ny])
        
        q = temp # 다시 q에 넣어주고
        temp = deque()  # 초기화

        while f: # 불의 움직임
            x, y = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and s[nx][ny] != "#":
                    s[nx][ny] = "*"
                    visit[nx][ny] = 1
                    temp.append([nx, ny])
        f = temp # 불 이동 끝나고 다시 값 넣어줌


for i in range(t):
    w, h = map(int, input().split())
    s, f, q = [], deque(), deque()
    visit = [[0] * w for i in range(h)]
    for j in range(h):
        a = list(input().strip())
        s.append(a)
        for k in range(w):
            if a[k] == "@":
                s[j][k] = 0
                q.append([j, k]) # 상근이 q에 넣어줌
            elif a[k] == "*":
                f.append([j, k]) # 불 f에 넣어줌
                visit[j][k] = 1
    result = bfs()
    print(result + 1 if result != None else "IMPOSSIBLE")