# https://www.acmicpc.net/problem/2133

# 문제풀이
# 3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 경우의 수를 구하라

# 예제 입력 1 
# 2
# 예제 출력 1 
# 3

# 문제풀이 
# 어려운 문제다... 식을 찾기가 너무 어려워서 찾을 수 밖에 없었음
# 홀수의경우는 만들어질수 없으므로 0개 
# 3 x 2 기준으로 3가지
# 3 x 4 기준으로 2가지 추가됨
# 3 x 4 : 3*3 +2 = 11이 됨

import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+2)] # N+1 했더니 백준에서는 계속 인덱스 오류가 떠서 +2로 수정
dp[2] = 3

for i in range(4,N+1,2) : # 짝수만 계산
    dp[i] = dp[2] * dp[i-2]
    for j in range(4,i,2) :
        dp[i] += 2 * dp[i-j]
    dp[i] += 2

print(dp[N])