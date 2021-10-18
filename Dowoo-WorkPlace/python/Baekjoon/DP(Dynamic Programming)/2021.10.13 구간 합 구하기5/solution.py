# https://www.acmicpc.net/problem/11660

# 문제요약
# NxN의 표가 있고
# 좌표가 주어지면 
# 좌표1 ~ 좌표2까지의 합을 구하라

# 입력
# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

# 출력
# 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

# 예제 입력 1 
# 4 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 2 2 3 4
# 3 4 3 4
# 1 1 4 4
# 예제 출력 1 
# 27
# 6
# 64
# 예제 입력 2 
# 2 4
# 1 2
# 3 4
# 1 1 1 1
# 1 2 1 2
# 2 1 2 1
# 2 2 2 2
# 예제 출력 2 
# 1
# 2
# 3
# 4

# 문제풀이
# 우선 값을 더해주는 dp를 만들어준다
# 값이 주어지면 처음부터 끝까지의 값을 구할려면 끝값 - (x축 시작점까지의 합 + y축 시작점까지의 합 - 0,0 에서 시작점까지의 합)을 계산하면 된다. 

import sys

N, M = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*(N+ 1) for _ in range(N+1)]

for i in range(N) :
    for j in range(N) : # 쭉 더해주는 dp값을 만들어줌
        dp[i+1][j+1] = table[i][j] + (dp[i][j+1] + dp[i+1][j] - dp[i][j])

for _ in range(M) :
    a,b,c,d = map(int, sys.stdin.readline().split()) # 좌표를 받음
    print(dp[c][d] - (dp[a-1][d]+dp[c][b-1]-dp[a-1][b-1]))  # 받은 좌표를 이용해서 값을 구함