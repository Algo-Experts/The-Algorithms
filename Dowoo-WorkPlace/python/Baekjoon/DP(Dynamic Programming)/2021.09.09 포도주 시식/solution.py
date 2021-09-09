# https://www.acmicpc.net/problem/2156

# 문제요약
# 연속적으로 놓여있는 3잔 불가능
# 최대로 마실수 있는 방법

# 입력
# 첫째 줄에 포도주 잔의 개수 n이 주어진다. (1≤n≤10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

# 출력
# 첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

# 예제 입력 1 
# 6
# 6
# 10
# 13
# 9
# 8
# 1
# 예제 출력 1 
# 33

# 문제풀이

import sys

N = int(sys.stdin.readline())
arr = [] 
dp = [] 

for i in range(N) :
    arr.append(int(sys.stdin.readline()))

dp.append(arr[0]) # 1개일때 맨 처음 수

if N > 1: # 2개일 때
    dp.append(arr[0]+arr[1])

if N > 2 : # 3개일 때
    dp.append(max(arr[2]+arr[1],arr[2]+arr[0],dp[1]))
    
for i in range(3,N) : # 그 이상일때 
    dp.append(max(arr[i] + dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1]))

#  arr[i] + dp[i-2] // 전전꺼 마시고 전꺼 안먹고 현재꺼 마심
#  dp[i-1] // 안먹었을 때
#  arr[i]+arr[i-1]+dp[i-3] // 전꺼 현재꺼 마시고 전전꺼 안마심 + 전전전꺼는 마심

print(dp[N-1])