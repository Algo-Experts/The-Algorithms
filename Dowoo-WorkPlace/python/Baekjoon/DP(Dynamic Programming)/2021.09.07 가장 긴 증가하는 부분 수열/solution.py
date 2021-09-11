# https://www.acmicpc.net/problem/11053

# 문제요약
# 긴 증가하는 수열을 만드는 것!
# 크기가 점점 커지는 숫자로 만드는것!

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 예제 입력 1 
# 6
# 10 20 10 30 20 50
# 예제 출력 1 
# 4

# 문제풀이
# 이 문제는 이전과 다르게 값을 먼저 넣어줘야함.
# 길이를 구하는 것이기 때문에 1개만 있어도 길이가 1임 따라서 1로 채움

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]*N #N만큼 1로 채움

for i in range(N) : # N번까지 돌릴꺼임
    for j in range(i) : # 0~i 번까지 또 반복할꺼!
        if arr[j]<arr[i] : # 비교해서 나보다 작으면 +1할꺼!
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))



