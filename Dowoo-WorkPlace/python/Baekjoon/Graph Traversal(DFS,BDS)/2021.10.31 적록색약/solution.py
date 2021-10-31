# https://www.acmicpc.net/problem/10026

# 문제요약
# 빨강-초록 / 파랑을 똑같이 보는 적록색약인 사람과
# 아닌사람의 구역의 수를 구하라

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

# 둘째 줄부터 N개 줄에는 그림이 주어진다.

# 출력
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

# 예제 입력 1 
# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 예제 출력 1 
# 4 3

# 문제풀이
# 구역을 구별하는 문제로 이전에 많이 풀어봤던 문제이다
# 적록색약을 가진 사람것도 필요함
# 조금 꼬아져 있기 때문에 생각을 다시해봐야했음

import sys
from collections import deque

N = int(sys.stdin.readline())
color = [list(sys.stdin.readline().rstrip()) for _ in range(N)] # 일반인이 보는 시야 arr
copy = [[0]*N for _ in range(N)] # 적록색약이 보는 시야arr
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt1 = 0 # 일반인의 값
cnt2 = 0 # 적록색약의 값

def bfs(a,b,c,arr) : # x,y,색,해당하는 arr이다
    arr[a][b] = 0 # 일반인은 color이고 색약은 copy로 된다.
    q=deque()
    q.append((a,b))

    while q :     
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]

            if 0 <= x <N and 0<= y < N and arr[x][y] == c: # 해당하는 색이어야함
                q.append((x,y))
                arr[x][y] = 0 #0으로 바꾸버림

for i in range(N) :
    for j in range(N) :
        if color[i][j] == "G" : # 그린색이면
            copy[i][j]="R" # 빨간색으로 바꿔라! 
        else :
            copy[i][j]=color[i][j] # 나머지는 그대로

for i in range(N) :
    for j in range(N) :
        if color[i][j] != 0 : # 일반인 기준 0이 아닐경우 즉 처음 방문한 경우
            bfs(i,j,color[i][j],color) # 좌표+색상+arr 이라고 생각
            cnt1 += 1 
        if copy[i][j] != 0 : # 색약 기준 0이 아닐경우 즉 처음 방문한 경우
            bfs(i,j,copy[i][j],copy)
            cnt2 += 1
 
print(cnt1, cnt2)

