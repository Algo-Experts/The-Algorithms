# https://www.acmicpc.net/problem/2294

# 문제요약
# n가지의 종류의 동전이 있음 k원을 만들고자함
# 최소값을 구하라

# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

# 출력
# 첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

# 예제 입력 1 
# 3 15
# 1
# 5
# 12
# 예제 출력 1 
# 3

# 문제풀이
# 최저값을 구해야한다는걸 잊지말것!
# 처음에 dp를 -1로 하려고 했으나 최저값이므로 존재할 수 없는 수를 써야함
# 점화식도 어렵..

import sys

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)] 
dp = [0]+[10001 for _ in range(K)] # 0번쨰는 0으로 만들고 그 뒤는 K보다 큰 10001로 채움

for i in coin : # 코인리스트
    for j in range(i,K+1) : #시작은 코인~
        dp[j] = min(dp[j],dp[j-i]+1) # ex dp[1] = min(10001, dp[0]+1) 이므로 0+1인 1이됨

if dp[-1] != 10001 : # K가 10001이 아닐경우 즉 답이 나온경우
    print(dp[-1])
else : # 못풀경우
    print(-1)
