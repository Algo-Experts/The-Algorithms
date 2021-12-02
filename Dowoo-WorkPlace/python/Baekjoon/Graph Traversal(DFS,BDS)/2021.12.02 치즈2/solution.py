# https://www.acmicpc.net/problem/2638

# 문제요약
# 4변중 적어도 2변이상이 접촉시 공기접촉으로 간주됨
# 막혀있는 곳은 공기가 없는것으로 간주됨

# 입력
# 첫째 줄에는 모눈종이의 크기를 나타내는 두 개의 정수 N, M (5 ≤ N, M ≤ 100)이 주어진다. 그 다음 N개의 줄에는 모눈종이 위의 격자에 치즈가 있는 부분은 1로 표시되고, 치즈가 없는 부분은 0으로 표시된다. 또한, 각 0과 1은 하나의 공백으로 분리되어 있다.

# 출력
# 출력으로는 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 정수로 첫 줄에 출력한다.

# 예제 입력 1 
# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 0
# 0 0 0 1 1 0 1 1 0
# 0 0 1 1 1 1 1 1 0
# 0 0 1 1 1 1 1 0 0
# 0 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 예제 출력 1 
# 4

# 문제풀이
# 치즈1보다 생각해야할 것이 많다

import sys
from collections import deque
input = sys.stdin.readline
 
N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
res = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs() :
    q=deque()
    q.append((0,0))
    visit = [[-1]*M for _ in range(N)]
    visit[0][0] = 0

    while q:
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]

            if 0 <= x < N and 0 <= y < M and visit[x][y] == -1 :
                if g[x][y] >=1 : # 인접한 칸이 치즈면 1증가
                    g[x][y] +=1
                else : # 아니면 방문 표시만함
                    visit[x][y] = 0
                    q.append((x,y))
                    
while True :
    bfs()
    t = 0

    for i in range(N) :
        for j in range(M) :
            if g[i][j] >=3: # 3이상 = 인접한 칸에 공기가 2개 이상인곳
                g[i][j] = 0 # 녹았으니 없애줌
                t = 1 # 시간증가
            elif g[i][j] == 2: 
                g[i][j] = 1 # 다시 원상복귀 
    
    if t == 1 : # 계속 반복하여 걸리는 시간 확인
        res += 1
    else:
        break
print(res)


