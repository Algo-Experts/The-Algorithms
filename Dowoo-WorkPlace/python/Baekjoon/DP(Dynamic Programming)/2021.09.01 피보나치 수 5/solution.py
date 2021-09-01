# https://www.acmicpc.net/problem/10870

# 문제요약
# 피보나치를 구하라!

# 입력
# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 55

# 문제풀이
# DP식으로 문제를 풀어봄

import sys

N = int(sys.stdin.readline())
dp = [0,1,1,2] # 결과값을 정리함

for i in range(4,N+1) :
    dp.append(dp[i-1]+dp[i-2]) # 정규화식

print(dp[N])

# 숏코딩! 근데 이렇게 하려기도 힘들다 ㅠㅠ
a=0;b=1;exec("a,b=b,a+b;"*int(input()));print(a)