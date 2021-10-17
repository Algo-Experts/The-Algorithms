# https://www.acmicpc.net/problem/11049

# 문제요약
# 행렬 NxM MxK일 경우 N*M*K이다 
# 행렬을 곱하는데 필요한 곱셈 연산 횟수를 최소값을 구하라

# 입력
# 첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.

# 둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)

# 항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

# 출력
# 첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 정답은 231-1 보다 작거나 같은 자연수이다. 또한, 최악의 순서로 연산해도 연산 횟수가 231-1보다 작거나 같다.

# 예제 입력 1 
# 3
# 5 3
# 3 2
# 2 6
# 예제 출력 1 
# 90

# 문제풀이
# 처음에 쉽게 봤는데 아니었다.
# 파일 합치기랑 좀 비슷한 개념이다.
# 대각선으로 문제가 풀어진다.
# 다시 보지만 너무 어렵다...
# 시간초과 걸려서 pypy3으로 풀었다.


import sys

N = int(sys.stdin.readline())
rc = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for i in range(1,N):
    for j in range(N-i): # 대각선의 우측 한칸씩 이동
        x = j+i # 현재 대각선에서 몇번째인지 
        dp[j][x] = 2**32 # 최대값
        for k in range(j,x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + rc[j][0] * rc[k][1] * rc[x][1])

print(dp[0][-1])