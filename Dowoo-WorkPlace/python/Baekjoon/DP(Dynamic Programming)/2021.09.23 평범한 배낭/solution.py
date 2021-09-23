# https://www.acmicpc.net/problem/12865

# 문제해석
# 물건의 갯수와 내가 최대 들수 있는 무게가 주어짐
# 물건은 무게와 가치가 주어짐
# 내가 가져갈 수 있는 최대 가치는 얼마인가?

# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# 입력으로 주어지는 모든 수는 정수이다.

# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

# 예제 입력 1 
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
# 예제 출력 1 
# 14

# 문제풀이
# dp문제의 경우는 3+4 이런개념이 아니라
# 0번쨰는 얼마 1번쨰는 얼마? 이런개념으로 접근해야함.


import sys
N, P = map(int, sys.stdin.readline().split())
WV = [[0,0]]
dp = [[0 for _ in range(P+1)] for _ in range(N+1)]

for _ in range(N) :
    WV.append(list(map(int, sys.stdin.readline().split())))

for i in range (1, N+1) : # N개 의 수 차례
    for j in range(1, P+1) : # 내가 가지고 가질 수 있는 무게
        W = WV[i][0] # 해당된 물건의 무게
        V = WV[i][1] # 해당된 물건의 가치

        if j < W : # 해당 물건의 무게보다 작은 것
            dp[i][j] = dp[i-1][j] # 이전 차순의 가치와 동일
        else : # 같거나 그 이상의 경우 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V) # 이전 차순의 가치 또는 이전 무게의 가치 + 해당 물건의 가치

print(dp[N][P])
        


