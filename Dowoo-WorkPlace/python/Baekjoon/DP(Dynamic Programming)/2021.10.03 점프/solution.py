# https://www.acmicpc.net/problem/1890

# 문제요약
# 왼쪽 위에서 오른쪽 아래로 가는데 해당하는 지역에 도착할경우 오른쪽이나 아래로 적힌 수만큼 점프함
# 경로의 갯수를 구하라

# 입력
# 첫째 줄에 게임 판의 크기 N (4 ≤ N ≤ 100)이 주어진다. 그 다음 N개 줄에는 각 칸에 적혀져 있는 수가 N개씩 주어진다. 칸에 적혀있는 수는 0보다 크거나 같고, 9보다 작거나 같은 정수이며, 가장 오른쪽 아래 칸에는 항상 0이 주어진다.

# 출력
# 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 문제의 규칙에 맞게 갈 수 있는 경로의 개수를 출력한다. 경로의 개수는 263-1보다 작거나 같다.

# 예제 입력 1 
# 4
# 2 3 3 1
# 1 2 1 3
# 1 2 3 1
# 3 1 1 0
# 예제 출력 1 
# 3

# 문제풀이
# 가는 방향은 오른쪽과 아래밖에 없음

import sys

N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1 # 첫 시작은 1로 시작

for i in range(N) :
    for j in range(N) :
        if i == N-1 and j == N-1 : # 끝에 도달하면 끝!
            break 
        num = map[i][j] # 점프할 숫자
        if j + num < N : # 오른쪽으로 이동시
            dp[i][j+num] += dp[i][j]
        if i + num < N : # 아래로 이동시
            dp[i+num][j] += dp[i][j]

print(dp[-1][-1])
