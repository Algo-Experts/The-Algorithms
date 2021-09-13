# https://www.acmicpc.net/problem/9461

# 문제요약
# 나선 모영으로 정상각형을 계속 추가함
# P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다. 명시됨

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

# 출력
# 각 테스트 케이스마다 P(N)을 출력한다.

# 예제 입력 1 
# 2
# 6
# 12
# 예제 출력 1 
# 3
# 16

# 문제풀이
# 이미 문제에 dp값을 알려주었고
# 점화식을 찾았다. 
# 전전값+전전전값이 현재값으로 확인됨

import sys

T = int(sys.stdin.readline())

for i in range(T) : 
    dp = [1,1,1] #기본 dp값
    P = int(sys.stdin.readline()) # 숫자받음

    for j in range(3,P) :
        dp.append(dp[j-3] + dp[j-2]) # 점화식

    print(dp[P-1])
