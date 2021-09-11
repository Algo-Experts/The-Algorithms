# https://www.acmicpc.net/problem/2748

# 문제요약
# 그냥 피보나치문제..

# 입력
# 첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 55

# 문제풀이 

# 이전의 피보나치 문제와 같음.. 복습함

import sys

N = int(sys.stdin.readline())
dp = [0,1,1,2]

for i in range(4,N+1) :
    dp.append(dp[i-1]+dp[i-2])

print(dp[N])