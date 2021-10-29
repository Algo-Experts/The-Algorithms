# https://www.acmicpc.net/problem/2468

# 문제요약
# 어떤 지역의 높이 정보가 주어졌을 때 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 구하라
# 상하좌우로 인접해 있으면 하나의 영역으로 침

# 입력
# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

# 출력
# 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.

# 예제 입력 1 
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
# 예제 출력 1 
# 5
# 예제 입력 2 
# 7
# 9 9 9 9 9 9 9
# 9 2 1 2 1 2 9
# 9 1 8 7 8 1 9
# 9 2 7 9 7 2 9
# 9 1 8 7 8 1 9
# 9 2 1 2 1 2 9
# 9 9 9 9 9 9 9
# 예제 출력 2 
# 6

# 문제풀이
# 단지번호붙이기 / 유기농배추/ 섬의개수 보다 조금 더 어려운 문제
# 경우의 수를 자 체크해야함
# BFS로 풀이함

import sys 
from collections import deque 

N = int(sys.stdin.readline())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cMin = min(map(min, city)) # 가장 낮은
cMax = max(map(max, city)) # 가장 높은
cnt = 1 # 영역의 갯수


def bfs(a,b,c) : 
    visit[a][b] = 1
    q=deque()
    q.append((a,b))

    while q :     
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]

            if 0 <= x <N and 0<= y < N and city[x][y] >= c and visit[x][y] == 0: 
                q.append((x,y))
                visit[x][y] = 1

for i in range(cMin, cMax+1) : # 최저높이에서 최고 높이까지
    visit=[[0]*N for _ in range(N)] # 방문은 계속 초기화 시켜야함
    temp = 0 # 해당장마의 카운터
    for  j in range(N) :
        for k in range(N) :
            if city[j][k] >= i and visit[j][k] == 0 :
                bfs(j,k,i)
                temp+=1
    
    if temp > cnt : # 기존보다 높으면 바꿔줌
        cnt = temp

print(cnt)



