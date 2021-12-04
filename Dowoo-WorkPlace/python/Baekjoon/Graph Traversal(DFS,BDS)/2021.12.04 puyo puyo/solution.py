# https://www.acmicpc.net/problem/11559

# 문제요약 
# 뿌요는 다른 뿌요가 나올때까지 아래로 떨어짐
# 같은색이 4개이상 연결되어 있으면 사라짐
# 사라지면 위에있던 것들은 아래로 떨어짐
# 연쇄 +1
# 동시에 터질경우도 연쇄증가

# 입력
# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

# 이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

# 입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

# 출력
# 현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.

# 예제 입력 1 
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# .Y....
# .YG...
# RRYG..
# RRYGG.
# 예제 출력 1 
# 3

# 문제풀이
# 색이 같으면 터트려 주고 +1 해주면됨

from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
g = [list(input().strip()) for i in range(12)]
res = 0

def bfs(i, j, char):
    q = deque()
    q.append([i, j]) 
    chain.append([i, j])
    while q:
        x1, y1 = q.popleft()
        for k in range(4):
            x = x1 + dx[k]
            y = y1 + dy[k]
            if 0 <= x < 12 and 0 <= y < 6 and visit[x][y] == 0 and g[x][y] == char: # 색이 같은경우
                visit[x][y] = 1
                q.append([x, y])
                chain.append([x, y]) # 값을 추가해줌
def down(): 
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if g[j][i] != "." and g[k][i] == ".": # 위가 빈칸이 아니고 아래가 빈칸이면 내림
                    g[k][i] = g[j][i]
                    g[j][i] = "."
                    break

while True:
    isTrue = False
    visit = [[0] * 6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if g[i][j] != "." and visit[i][j] == 0:
                visit[i][j] = 1
                chain = []
                bfs(i, j, g[i][j]) #g[i][j]는 색상임
                if len(chain) > 3: # 4개일 경우 터짐
                    isTrue = True
                    for x, y in chain: 
                        g[x][y] = "." # 체인들을 다 빈칸으로 바꿔줌
    if not isTrue: # 안터질경우 = false로 남을경우
        break # 멈춤
    down() # 터지면 아래로 내림
    res += 1 # 체인 +1해줌
print(res)