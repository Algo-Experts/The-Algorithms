# https://www.acmicpc.net/problem/14502

# 문제요약
# 바이러스는 상하좌우로 인접한 빈 칸으로 퍼져나감
# 벽의 갯수는 3개를 세워야함
# 0은 빈칸 1은 벽 2는 바이러스
# 안전영역의 최댓값을 구하여라


#입력
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

# 빈 칸의 개수는 3개 이상이다.

# 출력
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

# 예제 입력 1 
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 예제 출력 1 
# 27
# 예제 입력 2 
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2
# 예제 출력 2 
# 9
# 예제 입력 3 
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 예제 출력 3 
# 3

# 문제풀이
# 삼성SW역량 테스트 기출
# 조합사용 / BFS사용
# 

import sys
import copy

N,M = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
# 빈칸의 최대갯수
cnt = 0
# 바이러스 칸
virus = []

for i in range(N) :
    for j in range(M) :
        if g[i][j] == 2: # 2일경우엔 값 넣어줌
            virus.append((i,j))

def wall(start,count):
    global cnt
    if count == 3 : # 종료조건, 벽3개완료
        sel_g = copy.deepcopy(g) # 벽이 선택된 배열 복사
        for num in range(len(virus)):
            x, y = virus[num]
            spread_virus(x, y, sel_g) # 바이러스 퍼트림
        safe_counts = sum(i.count(0) for i in sel_g) # 터트렸을때의 값 
        cnt = max(cnt,safe_counts)
        return True
    else :
        for i in range(start, N*M): # 2차원 배열에서 조합구하기
            x = i // M
            y = i % M
            if g[x][y] == 0 : # 안전영역인 경우 가능
                g[x][y] = 1  # 벽으로 변경
                wall(i,count+1) # 벽선택
                g[x][y] = 0

def spread_virus(x,y,sel_g): # 바이러스 퍼짐
    if sel_g[x][y] == 2:
        for dir in range(4):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if nx >= 0 and ny >=0 and nx < N and ny < M : 
                if sel_g[nx][ny] == 0 :
                    sel_g[nx][ny] = 2
                    spread_virus(nx,ny,sel_g)

wall(0,0)
print(cnt)