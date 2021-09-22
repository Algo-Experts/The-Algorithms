# https://www.acmicpc.net/problem/11054

# 문제요약
# 올라갔다 내려오는 수열의 최대길이를 구하라

# 입력
# 첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

# 예제 입력 1 
# 10
# 1 5 2 1 4 3 4 5 2 1
# 예제 출력 1 
# 7
# 힌트
# 예제의 경우 {1 5 2 1 4 3 4 5 2 1}이 가장 긴 바이토닉 부분 수열이다.

# 문제풀이
# 증가와 감소를 나눠서 생각 

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dpU = [1 for _ in range(N)]
dpD = [1 for _ in range(N)]
dp = [0 for _ in range(N)]

# 증가하는 수
for i in range(N) :
    for j in range(i) :
        if arr[i]>arr[j] and dpU[i] < dpU[j] +1 :
            dpU[i] = dpU[j] +1

# 내려가는 수
for i in range(N-1, -1, -1) :
    for j in range(i+1,N) :
        if arr[i]>arr[j] and dpD[i] < dpD[j] +1 :
            dpD[i] = dpD[j] +1           
    dp[i] = dpU[i] + dpD[i] -1

print(max(dp))