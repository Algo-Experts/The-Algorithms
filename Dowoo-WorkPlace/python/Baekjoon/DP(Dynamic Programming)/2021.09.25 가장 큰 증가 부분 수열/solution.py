# https://www.acmicpc.net/problem/11055

# 문제요약
# 증가하는 부분 수열 중 합이 가장 큰 것을 찾는것!

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

# 예제 입력 1 
# 10
# 1 100 2 50 60 3 5 6 7 8
# 예제 출력 1 
# 113

# 문제풀이

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [i for i in arr] # dp에 값이 리스트 값을 넣어줌

for i in range(N) : # 앞에서 부터 시작! 
    for j in range(i) : # 누적시킴
        if arr[i] > arr[j] : # 리스트 값이 i번째 보다 작을경우 
            dp[i] = max(dp[i], dp[j]+arr[i]) # dp값을 증가시켜나감

print(max(dp))



