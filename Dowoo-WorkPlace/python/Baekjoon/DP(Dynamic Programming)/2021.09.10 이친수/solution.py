# https://www.acmicpc.net/problem/2193

# 문제요약
# 이친수는 0으로 시작하지 않는다.
# 이친수는 1이 두번 연속 안됨.

# 입력
# 첫째 줄에 N이 주어진다.

# 출력
# 첫째 줄에 N자리 이친수의 개수를 출력한다.

# 예제 입력 1 
# 3
# 예제 출력 1 
# 2

# 문제풀이
# 결과값들을 적어보니 결국 피보나치 dp문제는 피보나치가 많은것 같다.
# 만약 이게 dp문제라고 몰랐다면 이걸 dp로 풀 수 있었을까? 

import sys

N = int(sys.stdin.readline())
dp = [0,1,1,2,3]

for i in range(5,N+1) :
    dp.append(dp[i-1]+dp[i-2])

print(dp[N])