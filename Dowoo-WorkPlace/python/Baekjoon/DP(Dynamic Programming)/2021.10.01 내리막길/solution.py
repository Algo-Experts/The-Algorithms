# https://www.acmicpc.net/problem/1520

# 문제요약
# 숫자를 내림차순으로 이동할경우 경로의 갯수를 구하는 것

# 입력
# 첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

# 출력
# 첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.

# 예제 입력 1 
# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10
# 예제 출력 1 
# 3

# 문제풀이
# 혼자서 풀어보려고 했는데.. 도저히 모르겠음.
# 찾아보니까 DFS 탐색을 알아야지 풀 수 있다고 함.
# 탐색 공부겸 참고하면서 풀어봄.
# 이해는 가지만 다시 하라고 하면 할 수 있을까 싶음.. DFS를 많이 풀어봐야 할것같음.


import sys
sys.setrecursionlimit(10000)

M, N = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(M)] 
dp = [[-1]*N for _ in range(M)] # 안가본 곳은 -1로 처리함
dx = [1, -1, 0, 0] # x축 방향
dy = [0, 0, -1, 1] # y축 방향


def dfs(x, y):
    if x == 0 and y == 0: #처음으로 왔을 경우 1반환
        return 1
        
    if dp[x][y] == -1: # 안가본곳일경우
        dp[x][y] = 0  # 첫 방문 표시
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if map[x][y] < map[nx][ny]:# 큰 방향으로 이동해야 하므로 맵쪽이 더 크면
                    dp[x][y] += dfs(nx, ny) # 결과물을 더해줌 # 즉 계속 dfs를 반복하고 0.0까지 진행

    return dp[x][y] 

print(dfs(M-1,N-1)) 
