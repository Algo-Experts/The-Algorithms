# https://www.acmicpc.net/problem/1915

# 문제요약
# n×m의 0, 1로 된 배열이 있다.
# 1로 된 가장 큰 정사각형의 크기를 구하라

# 입력
# 첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

# 출력
# 첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.

# 예제 입력 1 
# 4 4
# 0100
# 0111
# 1110
# 0010
# 예제 출력 1 
# 4

# 문제풀이
# 처음에 어렵게 생각했지만 결국엔 1이 나오면 계속 값을 더해주면 된다.
# 정사각형이기 때문에 꼭 min을 넣어주어 가장 작은값을 더해야한다.

import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)] # 띄어쓰기 없이 받을땐 list를 써주고 rstrip()써서 공백을 없애준다 
dp = [[0]*(m+1) for _ in range(n+1)]
result = 0

for i in range(1,n+1) :
    for j in range(1,m+1):
        if arr[i-1][j-1] == 1 : # 1일때 
            dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) +1 # 여기에 min이 필요한 이유는 직각 삼각형이 나올 수 있기 때문
        result = max(result, dp[i][j])
print(result*result)
