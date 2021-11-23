# https://www.acmicpc.net/problem/2636

# 문제요약
# 치즈에는 하나 이상의 구멍이 있을 수 있다.
# 한시간이 지나면 녹아 없어짐
# 치즈가 모두 녹아 없어지는데 걸리는 시간과, 
# 모두 녹기 한시간전 남아있는 치즈조각의 칸을 구하라

# 입력
# 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

# 출력
# 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.

# 예제 입력 1 
# 13 12
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 1 0 0 0
# 0 1 1 1 0 0 0 1 1 0 0 0
# 0 1 1 1 1 1 1 0 0 0 0 0
# 0 1 1 1 1 1 0 1 1 0 0 0
# 0 1 1 1 1 0 0 1 1 0 0 0
# 0 0 1 1 0 0 0 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 예제 출력 1 
# 3
# 5

# 문제풀이
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []
time = 0

def bfs() :
    visit = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visit[0][0] = 1
    cnt = 0
    while q:
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 :
                if g[x][y] == 0:
                    visit[x][y] = 1
                    q.append((x,y))
                elif g[x][y] == 1:
                    g[x][y] = 0 # 녹게 만들어줌
                    cnt += 1
                    visit[x][y] = 1
    ans.append(cnt)
    return cnt
        
while True:
    time +=1
    cnt = bfs()
    if cnt == 0: # 모든 치즈가 녹음
        break

print(time-1) # 시간
print(ans[-2]) # 남은 치즈의 갯수

