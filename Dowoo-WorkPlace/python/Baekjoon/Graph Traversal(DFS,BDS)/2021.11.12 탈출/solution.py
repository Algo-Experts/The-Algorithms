# https://www.acmicpc.net/problem/3055

# 문제요약
# 비어 있는곳 . / 물이 있는곳 * / 돌 X / 비버굴 D / 고슴도치 S
# 매분마다 고슴도치는 현재 있는 칸과 인접한 네칸중 하나로 이동
# 물도 매 분마다 비어있는 칸으로 확장
# 돌은 통과 X
# 고슴도치는 물X 물은 비버소굴X
# 고슴도치가 비버소굴로 이동하는 최소 시간을 구하라
# 물이찰 예정인 칸으로 이동할 수 없음

# 입력
# 첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

# 다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.

# 출력
# 첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다. 만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.

# 예제 입력 1 
# 3 3
# D.*
# ...
# .S.
# 예제 출력 1 
# 3
# 예제 입력 2 
# 3 3
# D.*
# ...
# ..S

# 문제풀이

import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int, input().split()) 
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
g = []
q = deque() # 고슴도치
w = deque() # 물
visit = [[0] * C for _ in range(R)] # 방문표시

for i in range(R) :
    a = list(input().rstrip())
    g.append(a)
    for j in range(C) :
        if a[j] == "D": # 도착지
            d = [i,j] 
        elif a[j] == "S": # 고슴도치
            q.append((i,j))
            visit[i][j] = 1
            g[i][j] = 0
        elif a[j] == "*": # 물
            w.append((i,j))

def bfs() :
    while q or w :
        t1 = [] # 고슴도치 이동담음
        t2 = [] # 물 이동 담음

        while q : # 고슴도치
            x1,y1 = q.popleft()
            if g[x1][y1] != "*": # 물이지 않을경우
                for i in range(4) :
                    x = x1 + dx[i]
                    y = y1 + dy[i]
                    if 0 <= x < R and 0 <= y < C and visit[x][y] == 0 and g[x][y] != "X" and g[x][y] != "*" :
                        visit[x][y] = 1
                        g[x][y] = g[x1][y1] + 1
                        t1.append([x,y])
        
        while w: # 물
            x1,y1 = w.popleft()
            for i in range(4) :
                x = x1 + dx[i]
                y = y1 + dy[i]
                if x == d[0] and y == d[1] : # 도착지면 패스
                    continue 
                if 0 <= x < R and 0 <= y < C and g[x][y] != "*" and g[x][y] != "X":
                    g[x][y] = "*"
                    t2.append([x, y])

        for i in t1:
            q.append(i)
        for i in t2:
            w.append(i)

bfs()
res = g[d[0]][d[1]] # 결과값
print(res if res != "D" else "KAKTUS") # 도착 못하면 표시