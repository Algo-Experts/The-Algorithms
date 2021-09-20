# https://www.acmicpc.net/problem/2293

# 문제요약
# 동전종류의 갯수 N / 동전의 합 K가 주어지고
# N만큼 동전의 가치가 주어짐
# 경우의 수를 구하라

# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.

# 예제 입력 1 
# 3 10
# 1
# 2
# 5
# 예제 출력 1 
# 10

# 문제풀이
# dp는 K의 수다.
# 동전의 가치를 넣고 해당하는 곳에 방법을 계속 더해줌
# dp 5의 경우 1로 만들경우 1가지 / 2가 포함될경우 2가지 / 5에 1가지 총 4가지가 되는것

import sys

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)] # 값이 계속 줄뗴 힌즐쓰기
dp = [1]+[0 for _ in range(K)]

for i in coin : # 주어진 가치
    for j in range(1,K+1) : # 1부터 시작
        if j - i >= 0 :
            dp[j] += dp[j-i] # dp에 더해준다

print(dp[K])
