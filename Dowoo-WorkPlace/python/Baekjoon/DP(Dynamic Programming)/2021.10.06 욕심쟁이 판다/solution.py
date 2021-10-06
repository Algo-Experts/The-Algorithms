# https://www.acmicpc.net/problem/1937

# 문제요약
# 대나무 숲이 있다
# 판다는 양이 많은 곳으로 이동함
# 처음 위치 x
# 최대한 오래 살기 위한 경로를 구하라 (최장길이) 

# 입력
# 첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다. 대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.

# 예제 입력 1 
# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8
# 예제 출력 1 
# 4

# 문제풀이
# 내리막길문제 응용함 그래도 어려워서 참고함.
# 즉 DFS+DP 문제임
# 처음 위치가 지정되어있지 않음 가장 오래살수 있는 최장길이를 구해야함 이게 다른점임
# DFS 감이 오지만 여전히 어려움


import sys 
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dx = [1, -1, 0, 0] # x축 이동
dy = [0, 0, -1, 1] # y축 이동

def dfs(x, y):
    if dp[x][y]: # dp존재시 다시 탐색할 필요 없음. # 없을 시 계속 찾음.
        return dp[x][y]

    dp[x][y] =1 # 해당하는 곳이기 때문에 1 최소 하루 살수 있음 
    for i in range(4): # 4방향 검색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if map[x][y] < map[nx][ny]: # 큰 방향으로 이동함
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1) # dp 저장값과 비교함

    return dp[x][y] 

ans = 0 
# 시작 좌표
for i in range(N): 
    for j in range(N):
        ans = max(ans, dfs(i,j)) # 최대길이의 값

print(ans) 

