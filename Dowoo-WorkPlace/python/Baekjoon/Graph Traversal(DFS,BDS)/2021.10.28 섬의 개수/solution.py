# https://www.acmicpc.net/problem/4963

# 문제요약
# 섬의 갯수를 구하는것
# 기존엔 상하좌우 했다면 지금은 대각선도 포함된다

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 출력
# 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

# 예제 입력 1 
# 1 1
# 0
# 2 2
# 0 1
# 1 0
# 3 2
# 1 1 1
# 1 1 1
# 5 4
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 1
# 1 0 0 1 0
# 5 4
# 1 1 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 1
# 5 5
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0
# 예제 출력 1 
# 0
# 1
# 1
# 3
# 1
# 9

# 문제풀이
# 단지번호붙이기 / 유기농배추에서 업그레이드 된 문제
# BFS로 풀이함
# 그 전꺼를 풀었다면 어려운 문제는 아님

import sys 
from collections import deque 

# 방향 대각선까지!
dx = [-1, 1, 0, 0, -1, -1, 1, 1] 
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(a,b) : 
    maps[a][b] = 0 
    q=deque()
    q.append((a,b))

    while q :     
        x1,y1 = q.popleft()
        for i in range(8) :
            x = x1 + dx[i]
            y = y1 + dy[i]

            if 0 <= x <H and 0<= y < W and maps[x][y] == 1: # 방향주의! H가 x가 되어야하고 W가 y가됨
                q.append((x,y))
                maps[x][y] = 0 


while True : # 0 0 이 나올때까지 무한반복!
    W, H= map(int, sys.stdin.readline().split())
    cnt = 0

    if W == 0 and H == 0 :
        break

    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    
    for i in range(H) :
        for j in range(W) :
            if maps[i][j] == 1 : 
                bfs(i,j) 
                cnt +=1
             
    print(cnt)