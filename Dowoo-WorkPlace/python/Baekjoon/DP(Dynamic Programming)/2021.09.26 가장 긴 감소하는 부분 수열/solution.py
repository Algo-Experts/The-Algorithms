# https://www.acmicpc.net/problem/11722

# 문제요약
# 가장 긴 감소하는 부분 수열의 길이를 구하라!

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

# 예제 입력 1 
# 6
# 10 30 10 20 20 10
# 예제 출력 1 
# 3

# 문제풀이
# 22일에 푼 바이토닉의 감소부분만 구하면됨!

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]

for i in range(1, N) : # 앞에서 부터 계산
    for j in range(i) : # 이전꺼를 쭉 더해본다
        if arr[j] > arr[i] : # 내 앞숫자들이 본인보다 컷을때 
            dp[i] = max(dp[j] +1, dp[i]) # 비교후 가장 큰 값을 넣어줌           

print(max(dp))